$ErrorActionPreference = "Stop"

function Assert-True([bool]$Condition, [string]$Message) {
  if (-not $Condition) { throw "ASSERT TRUE FAILED: $Message" }
}

function Assert-Equal($Actual, $Expected, [string]$Message) {
  if ($Actual -ne $Expected) {
    throw "ASSERT EQUAL FAILED: $Message expected=[$Expected] actual=[$Actual]"
  }
}

function Invoke-CapturedPowerShell([string]$ScriptPath, [string[]]$Arguments) {
  function ConvertTo-NativeArgument([string]$Value) {
    if ($Value -notmatch '[\s"]') { return $Value }
    $escaped = [regex]::Replace($Value, '(\\*)"', '$1$1\"')
    $escaped = [regex]::Replace($escaped, '(\\+)$', '$1$1')
    return '"' + $escaped + '"'
  }

  $startInfo = [Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = "powershell"
  $startInfo.UseShellExecute = $false
  $startInfo.CreateNoWindow = $true
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $nativeArguments = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $ScriptPath) + $Arguments
  $startInfo.Arguments = (($nativeArguments | ForEach-Object { ConvertTo-NativeArgument $_ }) -join " ")

  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  [void]$process.Start()
  $stdout = $process.StandardOutput.ReadToEnd()
  $stderr = $process.StandardError.ReadToEnd()
  $process.WaitForExit()
  return [pscustomobject]@{ ExitCode = $process.ExitCode; Stdout = $stdout; Stderr = $stderr }
}

$scriptsRoot = Split-Path -Parent $PSScriptRoot
$fallbackPath = Join-Path $scriptsRoot "invoke-mineru-fallback.ps1"
$secretStorePath = Join-Path $scriptsRoot "secret-store.ps1"
if (-not (Test-Path -LiteralPath $fallbackPath)) {
  throw "Expected implementation file is missing: $fallbackPath"
}
. $secretStorePath

$node = (Get-Command node -ErrorAction Stop).Source
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("retrieve-ieee-mineru-test-" + [guid]::NewGuid().ToString("N"))
$syntheticToken = "synthetic-mineru-token"

try {
  New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
  $secretPath = Join-Path $tempRoot "secrets.clixml"
  $credential = [Management.Automation.PSCredential]::new(
    "synthetic-user",
    (ConvertTo-SecureString "synthetic-password" -AsPlainText -Force)
  )
  Export-RetrievalSecrets -IeeeCredential $credential `
    -MinerUToken (ConvertTo-SecureString $syntheticToken -AsPlainText -Force) `
    -Path $secretPath

  $pdf = Join-Path $tempRoot "paper.pdf"
  [IO.File]::WriteAllBytes($pdf, [Text.Encoding]::ASCII.GetBytes("%PDF-1.4`n%%EOF`n"))
  $fakeCli = Join-Path $tempRoot "fake-mineru.mjs"
  @'
import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const expected = "synthetic-mineru-token";
if (process.env.MINERU_TOKEN !== expected) {
  process.stderr.write("missing inherited token");
  process.exit(9);
}
for (const name of ["NO_PROXY", "no_proxy"]) {
  const entries = String(process.env[name] || "").split(",").map(value => value.trim().toLowerCase());
  if (!entries.includes("cdn-mineru.openxlab.org.cn")) {
    process.stderr.write(`missing ${name} CDN bypass`);
    process.exit(8);
  }
}
const outputIndex = args.indexOf("-o");
if (outputIndex < 0) process.exit(10);
const outputDir = args[outputIndex + 1];
fs.mkdirSync(path.join(outputDir, "images"), { recursive: true });
fs.writeFileSync(path.join(outputDir, "full.md"), "# Parsed by fake MinerU\n");
fs.writeFileSync(path.join(outputDir, "invocation.json"), JSON.stringify(args));
process.stdout.write(`converted with ${expected}`);
process.stderr.write(`diagnostic ${expected}`);
'@ | Set-Content -LiteralPath $fakeCli -Encoding UTF8

  $outputDir = Join-Path $tempRoot "output"
  $originalParentToken = $env:MINERU_TOKEN
  $env:MINERU_TOKEN = "preexisting-parent-value"
  try {
    $result = & $fallbackPath -PdfPath $pdf -OutputDir $outputDir -SecretPath $secretPath `
      -NodePath $node -MineruScriptPath $fakeCli | ConvertFrom-Json
    Assert-Equal $env:MINERU_TOKEN "preexisting-parent-value" "parent token must be restored"
  }
  finally {
    $env:MINERU_TOKEN = $originalParentToken
  }

  Assert-Equal $result.status "converted" "result status"
  Assert-Equal $result.outputDir (Join-Path $outputDir "precision") "precision output must be isolated"
  Assert-True (Test-Path -LiteralPath (Join-Path $result.outputDir "full.md")) "fake Markdown output"
  $arguments = Get-Content -Raw -LiteralPath (Join-Path $result.outputDir "invocation.json") | ConvertFrom-Json
  Assert-Equal $arguments[0] "extract" "CLI subcommand"
  Assert-Equal $arguments[1] $pdf "PDF argument"
  Assert-True (($arguments -join " ") -match "-f md --model pipeline --language en") "precision CLI flags"

  $stdoutLog = Get-Content -Raw -LiteralPath $result.stdoutLog
  $stderrLog = Get-Content -Raw -LiteralPath $result.stderrLog
  Assert-True (-not $stdoutLog.Contains($syntheticToken)) "stdout log must redact token"
  Assert-True (-not $stderrLog.Contains($syntheticToken)) "stderr log must redact token"
  Assert-True ($stdoutLog.Contains("[REDACTED]")) "stdout redaction marker"
  Assert-True ($stderrLog.Contains("[REDACTED]")) "stderr redaction marker"

  $rateCli = Join-Path $tempRoot "fake-rate-limit.mjs"
  @'
process.stderr.write(`429 rate limit: ${process.env.MINERU_TOKEN}`);
process.exit(3);
'@ | Set-Content -LiteralPath $rateCli -Encoding UTF8
  $rateOutput = Join-Path $tempRoot "rate-output"
  $rate = Invoke-CapturedPowerShell $fallbackPath @(
    "-PdfPath", $pdf,
    "-OutputDir", $rateOutput,
    "-SecretPath", $secretPath,
    "-NodePath", $node,
    "-MineruScriptPath", $rateCli
  )
  Assert-Equal $rate.ExitCode 75 "rate limit exit code"
  Assert-True (-not $rate.Stdout.Contains($syntheticToken)) "rate-limit stdout must not leak token"
  Assert-True (-not $rate.Stderr.Contains($syntheticToken)) "rate-limit stderr must not leak token"
  Assert-True (-not (Get-Content -Raw -LiteralPath (Join-Path $rateOutput "mineru.stderr.log")).Contains($syntheticToken)) "rate-limit log must redact token"

  $cdnCli = Join-Path $tempRoot "fake-cdn-fallback.mjs"
  @'
import fs from "node:fs";
import path from "node:path";
const args = process.argv.slice(2);
const outputDir = args[args.indexOf("-o") + 1];
fs.mkdirSync(outputDir, { recursive: true });
const marker = path.join(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1")), "cdn-invocations.txt");
fs.appendFileSync(marker, args[0] + "\n");
if (args[0] === "extract") {
  if (!process.env.MINERU_TOKEN) process.exit(11);
  fs.mkdirSync(path.join(outputDir, "images"), { recursive: true });
  fs.writeFileSync(path.join(outputDir, "full.md"), "# Stale partial precision output\n");
  process.stderr.write("Error: download zip: Get https://cdn-mineru.openxlab.org.cn/result.zip: EOF");
  process.exit(1);
}
if (args[0] === "flash-extract") {
  if (process.env.MINERU_TOKEN) {
    process.stderr.write("flash fallback inherited token");
    process.exit(12);
  }
  fs.writeFileSync(path.join(outputDir, "full.md"), "# Parsed by flash fallback\n");
  process.stdout.write("flash converted");
  process.exit(0);
}
process.exit(13);
'@ | Set-Content -LiteralPath $cdnCli -Encoding UTF8
  $cdnOutput = Join-Path $tempRoot "cdn-output"
  $cdnResult = & $fallbackPath -PdfPath $pdf -OutputDir $cdnOutput -SecretPath $secretPath `
    -NodePath $node -MineruScriptPath $cdnCli | ConvertFrom-Json
  Assert-Equal $cdnResult.status "converted" "CDN fallback result status"
  Assert-Equal $cdnResult.mode "flash-extract" "CDN EOF should choose flash fallback"
  Assert-Equal $cdnResult.outputDir (Join-Path $cdnOutput "flash") "flash output must be isolated"
  $cdnInvocations = @(Get-Content -LiteralPath (Join-Path $tempRoot "cdn-invocations.txt"))
  Assert-Equal $cdnInvocations.Count 2 "precision and flash invocation count"
  Assert-Equal $cdnInvocations[0] "extract" "precision must run first"
  Assert-Equal $cdnInvocations[1] "flash-extract" "flash must run once after CDN EOF"
  Assert-True (Test-Path -LiteralPath (Join-Path $cdnOutput "precision\full.md")) "partial precision output remains isolated"
  Assert-True (Test-Path -LiteralPath (Join-Path $cdnResult.outputDir "full.md")) "flash fallback Markdown output"

  $nonCdnCli = Join-Path $tempRoot "fake-non-cdn-failure.mjs"
  @'
import fs from "node:fs";
import path from "node:path";
const args = process.argv.slice(2);
const marker = path.join(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1")), "non-cdn-invocations.txt");
fs.appendFileSync(marker, args[0] + "\n");
if (args[0] === "extract") {
  process.stderr.write(process.env.FAKE_MINERU_ERROR || "unexpected EOF during preprocessing");
  process.exit(1);
}
process.exit(0);
'@ | Set-Content -LiteralPath $nonCdnCli -Encoding UTF8
  foreach ($failureText in @(
    "unexpected EOF during preprocessing",
    "TLS handshake failed while contacting api.example.invalid",
    "download zip: Get https://cdn-mineru.evil.example/result.zip: EOF"
  )) {
    Remove-Item -LiteralPath (Join-Path $tempRoot "non-cdn-invocations.txt") -Force -ErrorAction SilentlyContinue
    $env:FAKE_MINERU_ERROR = $failureText
    try {
      $negativeOutput = Join-Path $tempRoot ("negative-" + [guid]::NewGuid().ToString("N"))
      $negative = Invoke-CapturedPowerShell $fallbackPath @(
        "-PdfPath", $pdf,
        "-OutputDir", $negativeOutput,
        "-SecretPath", $secretPath,
        "-NodePath", $node,
        "-MineruScriptPath", $nonCdnCli
      )
    }
    finally {
      Remove-Item Env:FAKE_MINERU_ERROR -ErrorAction SilentlyContinue
    }
    Assert-True ($negative.ExitCode -ne 0) "non-CDN transport failure must not trigger flash fallback"
    $negativeInvocations = @(Get-Content -LiteralPath (Join-Path $tempRoot "non-cdn-invocations.txt"))
    Assert-Equal $negativeInvocations.Count 1 "non-CDN failure must stop after precision"
    Assert-Equal $negativeInvocations[0] "extract" "non-CDN failure must not invoke flash"
  }

  Write-Output "PASS process-only MinerU token injection and restoration"
  Write-Output "PASS precision CLI invocation and log redaction"
  Write-Output "PASS rate-limit exit 75"
  Write-Output "PASS one-shot flash fallback for precision CDN EOF"
  Write-Output "PASS exact MinerU CDN fallback signature and isolated outputs"
}
finally {
  if (Test-Path -LiteralPath $tempRoot) {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
  }
}
