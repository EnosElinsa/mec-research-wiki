[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$PdfPath,

  [Parameter(Mandatory = $true)]
  [string]$OutputDir,

  [string]$SecretPath = "",
  [string]$NodePath = "",
  [string]$MineruScriptPath = "",
  [int]$TimeoutSeconds = 1800
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

. (Join-Path $PSScriptRoot "secret-store.ps1")

function Quote-ProcessArgument([string]$Argument) {
  if ($null -eq $Argument) { return '""' }
  return '"' + ($Argument -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"'
}

function Test-MineruRateLimit([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return $false }
  return $Text -match '(?i)(\b429\b|rate\s*limit|too many requests|quota|qps|throttl)'
}

function Test-MineruCdnTransportFailure([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return $false }
  $hasPinnedHost = $Text -match '(?i)https://cdn-mineru\.openxlab\.org\.cn(?:[/:?]|$)'
  $hasResultDownload = $Text -match '(?i)(download(?:ing)?\s+(?:the\s+)?(?:result\s+)?(?:zip|archive)|result\s+(?:zip|archive))'
  $hasTransportFailure = $Text -match '(?i)(unexpected\s+eof|\beof\b|tls(?:\s+handshake)?|handshake)'
  return $hasPinnedHost -and $hasResultDownload -and $hasTransportFailure
}

function Protect-MineruLog([string]$Text, [string]$Secret) {
  if ($null -eq $Text) { return "" }
  if ([string]::IsNullOrEmpty($Secret)) { return $Text }
  return $Text.Replace($Secret, "[REDACTED]")
}

function Add-NoProxyHost([Diagnostics.ProcessStartInfo]$StartInfo, [string]$Hostname) {
  foreach ($name in @("NO_PROXY", "no_proxy")) {
    $current = [string]$StartInfo.EnvironmentVariables[$name]
    $entries = @($current -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    if (-not ($entries | Where-Object { $_.ToLowerInvariant() -eq $Hostname.ToLowerInvariant() })) {
      $entries += $Hostname
    }
    $StartInfo.EnvironmentVariables[$name] = $entries -join ','
  }
}

function Invoke-MineruChild {
  param(
    [Parameter(Mandatory = $true)][string[]]$Arguments,
    [string]$Token = ""
  )

  $startInfo = [Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = $NodePath
  $startInfo.UseShellExecute = $false
  $startInfo.CreateNoWindow = $true
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $startInfo.Arguments = (($Arguments | ForEach-Object { Quote-ProcessArgument $_ }) -join " ")
  Add-NoProxyHost $startInfo "cdn-mineru.openxlab.org.cn"
  if ([string]::IsNullOrEmpty($Token)) {
    [void]$startInfo.EnvironmentVariables.Remove("MINERU_TOKEN")
  }
  else {
    $startInfo.EnvironmentVariables["MINERU_TOKEN"] = $Token
  }

  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  $timedOut = $false
  try {
    [void]$process.Start()
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    if (-not $process.WaitForExit($TimeoutSeconds * 1000)) {
      $timedOut = $true
      $process.Kill()
    }
    $process.WaitForExit()
    return [pscustomobject]@{
      ExitCode = $process.ExitCode
      Stdout = $stdoutTask.GetAwaiter().GetResult()
      Stderr = $stderrTask.GetAwaiter().GetResult()
      TimedOut = $timedOut
    }
  }
  finally {
    $process.Dispose()
  }
}

if (-not (Test-Path -LiteralPath $PdfPath -PathType Leaf)) {
  throw "PDF input is missing: $PdfPath"
}
if ($TimeoutSeconds -lt 1) {
  throw "TimeoutSeconds must be positive."
}

if ([string]::IsNullOrWhiteSpace($SecretPath)) {
  $SecretPath = Get-RetrievalSecretPath
}
if ([string]::IsNullOrWhiteSpace($NodePath)) {
  $NodePath = (Get-Command node -ErrorAction Stop).Source
}
if ([string]::IsNullOrWhiteSpace($MineruScriptPath)) {
  $mineruCommand = Get-Command mineru-open-api -ErrorAction Stop
  $MineruScriptPath = Join-Path (Split-Path -Parent $mineruCommand.Source) "node_modules\mineru-open-api\bin\mineru-open-api"
}
if (-not (Test-Path -LiteralPath $NodePath -PathType Leaf)) {
  throw "Node.js executable is missing: $NodePath"
}
if (-not (Test-Path -LiteralPath $MineruScriptPath -PathType Leaf)) {
  throw "mineru-open-api Node entrypoint is missing: $MineruScriptPath"
}

New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
$resolvedOutputDir = (Resolve-Path -LiteralPath $OutputDir).Path
$precisionOutputDir = Join-Path $resolvedOutputDir "precision"
$flashOutputDir = Join-Path $resolvedOutputDir "flash"
New-Item -ItemType Directory -Path $precisionOutputDir -Force | Out-Null
$stdoutLog = Join-Path $resolvedOutputDir "mineru.stdout.log"
$stderrLog = Join-Path $resolvedOutputDir "mineru.stderr.log"

$payload = Import-RetrievalSecrets -Path $SecretPath
$plainToken = ConvertFrom-RetrievalSecureString $payload.MinerUToken
try {
  $precisionArguments = @(
    $MineruScriptPath,
    "extract",
    $PdfPath,
    "-o",
    $precisionOutputDir,
    "-f",
    "md",
    "--model",
    "pipeline",
    "--language",
    "en"
  )
  $precision = Invoke-MineruChild -Arguments $precisionArguments -Token $plainToken
  $precisionStdout = Protect-MineruLog $precision.Stdout $plainToken
  $precisionStderr = Protect-MineruLog $precision.Stderr $plainToken
}
finally {
  $plainToken = $null
  $payload = $null
}

$precisionCombined = "$precisionStdout`n$precisionStderr"
if (Test-MineruRateLimit $precisionCombined) {
  Set-Content -LiteralPath $stdoutLog -Value $precisionStdout -Encoding UTF8
  Set-Content -LiteralPath $stderrLog -Value $precisionStderr -Encoding UTF8
  [Console]::Error.WriteLine("MinerU rate limit detected; retry later.")
  exit 75
}
if ($precision.TimedOut) {
  Set-Content -LiteralPath $stdoutLog -Value $precisionStdout -Encoding UTF8
  Set-Content -LiteralPath $stderrLog -Value ($precisionStderr.TrimEnd() + "`nMinerU precision CLI timed out after $TimeoutSeconds seconds.") -Encoding UTF8
  throw "mineru-open-api timed out. See sanitized log: $stderrLog"
}

$mode = "precision"
$finalStdout = $precisionStdout
$finalStderr = $precisionStderr
if ($precision.ExitCode -ne 0) {
  if (-not (Test-MineruCdnTransportFailure $precisionCombined)) {
    Set-Content -LiteralPath $stdoutLog -Value $precisionStdout -Encoding UTF8
    Set-Content -LiteralPath $stderrLog -Value $precisionStderr -Encoding UTF8
    throw "mineru-open-api failed with exit code $($precision.ExitCode). See sanitized logs: $stdoutLog and $stderrLog"
  }

  $flashArguments = @(
    $MineruScriptPath,
    "flash-extract",
    $PdfPath,
    "-o",
    $flashOutputDir,
    "--language",
    "en"
  )
  New-Item -ItemType Directory -Path $flashOutputDir -Force | Out-Null
  $flash = Invoke-MineruChild -Arguments $flashArguments
  $finalStdout = ($precisionStdout.TrimEnd() + "`n[flash fallback]`n" + $flash.Stdout.TrimStart()).Trim()
  $finalStderr = ($precisionStderr.TrimEnd() + "`n[flash fallback]`n" + $flash.Stderr.TrimStart()).Trim()
  $flashCombined = "$($flash.Stdout)`n$($flash.Stderr)"
  if (Test-MineruRateLimit $flashCombined) {
    Set-Content -LiteralPath $stdoutLog -Value $finalStdout -Encoding UTF8
    Set-Content -LiteralPath $stderrLog -Value $finalStderr -Encoding UTF8
    [Console]::Error.WriteLine("MinerU rate limit detected during flash fallback; retry later.")
    exit 75
  }
  if ($flash.TimedOut) {
    Set-Content -LiteralPath $stdoutLog -Value $finalStdout -Encoding UTF8
    Set-Content -LiteralPath $stderrLog -Value ($finalStderr.TrimEnd() + "`nMinerU flash fallback timed out after $TimeoutSeconds seconds.") -Encoding UTF8
    throw "mineru-open-api flash fallback timed out. See sanitized log: $stderrLog"
  }
  if ($flash.ExitCode -ne 0) {
    Set-Content -LiteralPath $stdoutLog -Value $finalStdout -Encoding UTF8
    Set-Content -LiteralPath $stderrLog -Value $finalStderr -Encoding UTF8
    throw "mineru-open-api flash fallback failed with exit code $($flash.ExitCode). See sanitized logs: $stdoutLog and $stderrLog"
  }
  $mode = "flash-extract"
}

Set-Content -LiteralPath $stdoutLog -Value $finalStdout -Encoding UTF8
Set-Content -LiteralPath $stderrLog -Value $finalStderr -Encoding UTF8

[ordered]@{
  status = "converted"
  mode = $mode
  outputDir = if ($mode -eq "precision") { $precisionOutputDir } else { $flashOutputDir }
  stdoutLog = $stdoutLog
  stderrLog = $stderrLog
} | ConvertTo-Json -Compress
