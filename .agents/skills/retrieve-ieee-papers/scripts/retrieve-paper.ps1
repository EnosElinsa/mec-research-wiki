[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$Reference,

  [string]$RepoRoot = "",
  [string]$WorkRoot = "",
  [string]$ProfileDir = "",
  [string]$DependencyRoot = "",
  [string]$SecretPath = "",
  [string]$NodePath = "",
  [string]$NpmPath = "",
  [string]$DownloaderScriptPath = "",
  [string]$MineruInvokerPath = "",
  [string]$StageScriptPath = "",
  [string]$MineruScriptPath = "",
  [string]$PlaywrightVersion = "1.61.1",
  [int]$BrowserTimeoutSeconds = 90,
  [switch]$DownloadOnly,
  [switch]$TestMode
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Quote-ProcessArgument([string]$Argument) {
  if ($null -eq $Argument) { return '""' }
  return '"' + ($Argument -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"'
}

function Invoke-CapturedProcess {
  param(
    [Parameter(Mandatory = $true)][string]$FilePath,
    [Parameter(Mandatory = $true)][string[]]$Arguments,
    [Parameter(Mandatory = $true)][string]$StdoutPath,
    [Parameter(Mandatory = $true)][string]$StderrPath
  )

  $startInfo = [Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = $FilePath
  $startInfo.UseShellExecute = $false
  $startInfo.CreateNoWindow = $true
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $startInfo.Arguments = (($Arguments | ForEach-Object { Quote-ProcessArgument $_ }) -join " ")

  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  try {
    [void]$process.Start()
    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    $process.WaitForExit()
    $stdout = $stdoutTask.GetAwaiter().GetResult()
    $stderr = $stderrTask.GetAwaiter().GetResult()
    Set-Content -LiteralPath $StdoutPath -Value $stdout -Encoding UTF8
    Set-Content -LiteralPath $StderrPath -Value $stderr -Encoding UTF8
    return [pscustomobject]@{
      ExitCode = $process.ExitCode
      Stdout = $stdout
      Stderr = $stderr
    }
  }
  finally {
    $process.Dispose()
  }
}

function Get-NormalizedPath([string]$PathValue) {
  return [IO.Path]::GetFullPath($PathValue).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
}

function Test-SamePath([string]$Left, [string]$Right) {
  return (Get-NormalizedPath $Left).Equals((Get-NormalizedPath $Right), [StringComparison]::OrdinalIgnoreCase)
}

function Test-PathContainedBy([string]$Candidate, [string]$Parent) {
  $candidatePath = Get-NormalizedPath $Candidate
  $parentPath = Get-NormalizedPath $Parent
  return $candidatePath.Equals($parentPath, [StringComparison]::OrdinalIgnoreCase) -or
    $candidatePath.StartsWith($parentPath + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)
}

function Test-PlaywrightDependency(
  [string]$Root,
  [string]$ExpectedVersion,
  [string]$ExpectedResolved,
  [string]$ExpectedIntegrity
) {
  $packagePath = Join-Path $Root "node_modules\playwright-core\package.json"
  $lockPath = Join-Path $Root "package-lock.json"
  if (-not (Test-Path -LiteralPath $packagePath -PathType Leaf) -or
      -not (Test-Path -LiteralPath $lockPath -PathType Leaf)) { return $false }
  try {
    $package = Get-Content -LiteralPath $packagePath -Raw -Encoding UTF8 | ConvertFrom-Json
    Add-Type -AssemblyName System.Web.Extensions
    $serializer = [Web.Script.Serialization.JavaScriptSerializer]::new()
    $lock = $serializer.DeserializeObject((Get-Content -LiteralPath $lockPath -Raw -Encoding UTF8))
    $lockedPackage = $lock["packages"]["node_modules/playwright-core"]
    return [string]$package.version -eq $ExpectedVersion -and
      [string]$lockedPackage["version"] -eq $ExpectedVersion -and
      [string]$lockedPackage["resolved"] -eq $ExpectedResolved -and
      [string]$lockedPackage["integrity"] -eq $ExpectedIntegrity
  }
  catch {
    return $false
  }
}

$pinnedPlaywrightVersion = "1.61.1"
$pinnedNpmRegistry = "https://registry.npmjs.org"
$pinnedPlaywrightTarball = "https://registry.npmjs.org/playwright-core/-/playwright-core-1.61.1.tgz"
$pinnedPlaywrightIntegrity = "sha512-h7Qlt6m4REp25qvIdvbDtVmD4LqVXfpRxhORv9L0jzETM05p4fuPJ3dKyuSXQxDSbXnmS79HAgi9589lGSpLkg=="
if ($PlaywrightVersion -ne $pinnedPlaywrightVersion) {
  throw "PlaywrightVersion is fixed at $pinnedPlaywrightVersion so its package integrity can be verified."
}
if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $RepoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..\..")).Path
}
$resolvedRepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$expectedWorkRoot = Get-NormalizedPath (Join-Path $resolvedRepoRoot "raw\tmp\.work")
$expectedDependencyRoot = Get-NormalizedPath (Join-Path $env:LOCALAPPDATA "Codex\deps\retrieve-ieee-papers")
$expectedProfileDir = Get-NormalizedPath (Join-Path $env:LOCALAPPDATA "Codex\browser-profiles\retrieve-ieee-papers")
if ([string]::IsNullOrWhiteSpace($WorkRoot)) {
  $WorkRoot = $expectedWorkRoot
}
if ([string]::IsNullOrWhiteSpace($DependencyRoot)) {
  $DependencyRoot = $expectedDependencyRoot
}
if ([string]::IsNullOrWhiteSpace($ProfileDir)) {
  $ProfileDir = $expectedProfileDir
}
if (-not $TestMode) {
  if (-not (Test-SamePath $WorkRoot $expectedWorkRoot)) {
    throw "WorkRoot must be the dedicated repository path: $expectedWorkRoot"
  }
  if (-not (Test-SamePath $DependencyRoot $expectedDependencyRoot)) {
    throw "DependencyRoot must be the dedicated LocalAppData path: $expectedDependencyRoot"
  }
  if (-not (Test-SamePath $ProfileDir $expectedProfileDir)) {
    throw "ProfileDir must be the dedicated LocalAppData path: $expectedProfileDir"
  }
}
if ([string]::IsNullOrWhiteSpace($NodePath)) {
  $NodePath = (Get-Command node -ErrorAction Stop).Source
}
if ([string]::IsNullOrWhiteSpace($NpmPath)) {
  $NpmPath = (Get-Command npm -ErrorAction Stop).Source
}
if ([string]::IsNullOrWhiteSpace($DownloaderScriptPath)) {
  $DownloaderScriptPath = Join-Path $PSScriptRoot "ieee-playwright.mjs"
}
if ([string]::IsNullOrWhiteSpace($MineruInvokerPath)) {
  $MineruInvokerPath = Join-Path $PSScriptRoot "invoke-mineru-fallback.ps1"
}
if ([string]::IsNullOrWhiteSpace($StageScriptPath)) {
  $StageScriptPath = Join-Path $PSScriptRoot "stage-paper.ps1"
}

foreach ($requiredScript in @($DownloaderScriptPath, $MineruInvokerPath, $StageScriptPath)) {
  if (-not (Test-Path -LiteralPath $requiredScript -PathType Leaf)) {
    throw "Required retrieval component is missing: $requiredScript"
  }
}

New-Item -ItemType Directory -Path $WorkRoot -Force | Out-Null
$resolvedWorkRoot = (Resolve-Path -LiteralPath $WorkRoot).Path
$runRoot = Join-Path $resolvedWorkRoot ("retrieve-" + [guid]::NewGuid().ToString("N"))
$downloadDir = Join-Path $runRoot "download"
$mineruDir = Join-Path $runRoot "mineru"
New-Item -ItemType Directory -Path $downloadDir -Force | Out-Null
New-Item -ItemType Directory -Path $DependencyRoot -Force | Out-Null
New-Item -ItemType Directory -Path $ProfileDir -Force | Out-Null

if (-not (Test-PlaywrightDependency $DependencyRoot $PlaywrightVersion $pinnedPlaywrightTarball $pinnedPlaywrightIntegrity)) {
  $npmLog = Join-Path $runRoot "playwright-install.log"
  $packageManifest = [ordered]@{
    name = "retrieve-ieee-papers"
    private = $true
    dependencies = [ordered]@{ "playwright-core" = $PlaywrightVersion }
  } | ConvertTo-Json -Depth 4
  $lockManifest = [ordered]@{
    name = "retrieve-ieee-papers"
    lockfileVersion = 3
    requires = $true
    packages = [ordered]@{
      "" = [ordered]@{ dependencies = [ordered]@{ "playwright-core" = $PlaywrightVersion } }
      "node_modules/playwright-core" = [ordered]@{
        version = $PlaywrightVersion
        resolved = $pinnedPlaywrightTarball
        integrity = $pinnedPlaywrightIntegrity
      }
    }
  } | ConvertTo-Json -Depth 8
  Set-Content -LiteralPath (Join-Path $DependencyRoot "package.json") -Value $packageManifest -Encoding UTF8
  Set-Content -LiteralPath (Join-Path $DependencyRoot "package-lock.json") -Value $lockManifest -Encoding UTF8
  $npmArguments = @(
    "ci",
    "--prefix", $DependencyRoot,
    "--registry", $pinnedNpmRegistry,
    "--ignore-scripts",
    "--no-audit",
    "--no-fund"
  )
  $LASTEXITCODE = 0
  $npmOutput = & $NpmPath @npmArguments 2>&1
  $npmExitCode = $LASTEXITCODE
  Set-Content -LiteralPath $npmLog -Value ($npmOutput | Out-String) -Encoding UTF8
  if ($npmExitCode -ne 0 -or
      -not (Test-PlaywrightDependency $DependencyRoot $PlaywrightVersion $pinnedPlaywrightTarball $pinnedPlaywrightIntegrity)) {
    throw "Could not install integrity-pinned playwright-core $PlaywrightVersion. See: $npmLog"
  }
}

$downloadArgs = @(
  $DownloaderScriptPath,
  "--reference", $Reference,
  "--repo-root", $resolvedRepoRoot,
  "--work-dir", $downloadDir,
  "--profile-dir", $ProfileDir,
  "--dependency-root", $DependencyRoot,
  "--timeout-ms", ([string]($BrowserTimeoutSeconds * 1000))
)
if (-not [string]::IsNullOrWhiteSpace($SecretPath)) {
  $downloadArgs += @("--secret-path", $SecretPath)
}
$downloadProcess = $null
$downloadStdoutPath = ""
$downloadStderrPath = ""
for ($downloadAttempt = 0; $downloadAttempt -lt 2; $downloadAttempt++) {
  $suffix = if ($downloadAttempt -eq 0) { "" } else { "-retry" }
  $downloadStdoutPath = Join-Path $runRoot ("download" + $suffix + ".stdout.log")
  $downloadStderrPath = Join-Path $runRoot ("download" + $suffix + ".stderr.log")
  $downloadProcess = Invoke-CapturedProcess `
    -FilePath $NodePath `
    -Arguments $downloadArgs `
    -StdoutPath $downloadStdoutPath `
    -StderrPath $downloadStderrPath
  if ($downloadProcess.ExitCode -eq 0) { break }

  $downloadError = $null
  try { $downloadError = $downloadProcess.Stderr.Trim() | ConvertFrom-Json }
  catch {}
  $downloadErrorPhase = ""
  if ($null -ne $downloadError) {
    $phaseProperty = $downloadError.PSObject.Properties["phase"]
    if ($null -ne $phaseProperty) { $downloadErrorPhase = [string]$phaseProperty.Value }
  }
  if ($downloadAttempt -eq 0 -and $downloadErrorPhase -eq "paper-metadata") {
    continue
  }
  throw "IEEE retrieval failed. See sanitized log: $downloadStderrPath"
}
if ($downloadProcess.ExitCode -ne 0) {
  throw "IEEE retrieval failed after one metadata restart. See sanitized log: $downloadStderrPath"
}

try {
  $downloadResult = $downloadProcess.Stdout.Trim() | ConvertFrom-Json
}
catch {
  throw "IEEE retrieval returned invalid JSON. See: $downloadStdoutPath"
}
if ($downloadResult.status -eq "existing" -or $DownloadOnly) {
  [Console]::Out.WriteLine(($downloadResult | ConvertTo-Json -Compress))
  exit 0
}
if ($downloadResult.status -ne "downloaded") {
  throw "IEEE retrieval returned unsupported status: $($downloadResult.status)"
}

$mineruArgs = @(
  "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $MineruInvokerPath,
  "-PdfPath", [string]$downloadResult.pdfPath,
  "-OutputDir", $mineruDir,
  "-NodePath", $NodePath
)
if (-not [string]::IsNullOrWhiteSpace($SecretPath)) {
  $mineruArgs += @("-SecretPath", $SecretPath)
}
if (-not [string]::IsNullOrWhiteSpace($MineruScriptPath)) {
  $mineruArgs += @("-MineruScriptPath", $MineruScriptPath)
}
$mineruStdoutPath = Join-Path $runRoot "mineru-wrapper.stdout.log"
$mineruStderrPath = Join-Path $runRoot "mineru-wrapper.stderr.log"
$mineruProcess = Invoke-CapturedProcess `
  -FilePath "powershell" `
  -Arguments $mineruArgs `
  -StdoutPath $mineruStdoutPath `
  -StderrPath $mineruStderrPath
if ($mineruProcess.ExitCode -eq 75) { exit 75 }
if ($mineruProcess.ExitCode -ne 0) {
  throw "MinerU conversion failed. See sanitized log: $mineruStderrPath"
}
try {
  $mineruResult = $mineruProcess.Stdout.Trim() | ConvertFrom-Json
}
catch {
  throw "MinerU conversion returned invalid JSON. See: $mineruStdoutPath"
}
if ($mineruResult.status -ne "converted" -or [string]::IsNullOrWhiteSpace([string]$mineruResult.outputDir)) {
  throw "MinerU conversion returned an unsupported result. See: $mineruStdoutPath"
}
$successfulMineruDir = Get-NormalizedPath ([string]$mineruResult.outputDir)
if (-not (Test-PathContainedBy $successfulMineruDir $mineruDir) -or
    -not (Test-Path -LiteralPath $successfulMineruDir -PathType Container)) {
  throw "MinerU conversion returned an output directory outside its run workspace."
}

$stageArgs = @(
  "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $StageScriptPath,
  "-PdfPath", [string]$downloadResult.pdfPath,
  "-MineruOutputDir", $successfulMineruDir,
  "-Title", [string]$downloadResult.title,
  "-Doi", [string]$downloadResult.doi,
  "-RepoRoot", $resolvedRepoRoot
)
$stageStdoutPath = Join-Path $runRoot "stage.stdout.log"
$stageStderrPath = Join-Path $runRoot "stage.stderr.log"
$stageProcess = Invoke-CapturedProcess `
  -FilePath "powershell" `
  -Arguments $stageArgs `
  -StdoutPath $stageStdoutPath `
  -StderrPath $stageStderrPath
if ($stageProcess.ExitCode -ne 0) {
  throw "Paper staging failed. See: $stageStderrPath"
}
try {
  $stageResult = $stageProcess.Stdout.Trim() | ConvertFrom-Json
}
catch {
  throw "Paper staging returned invalid JSON. See: $stageStdoutPath"
}
[Console]::Out.WriteLine(($stageResult | ConvertTo-Json -Compress))
