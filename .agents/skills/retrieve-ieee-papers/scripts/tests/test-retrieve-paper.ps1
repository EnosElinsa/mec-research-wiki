$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Assert-True([bool]$Condition, [string]$Message) {
  if (-not $Condition) { throw $Message }
}

function Assert-Equal($Actual, $Expected, [string]$Message) {
  if ($Actual -ne $Expected) { throw "$Message expected=[$Expected] actual=[$Actual]" }
}

$scriptPath = Join-Path $PSScriptRoot "..\retrieve-paper.ps1"
Assert-True (Test-Path -LiteralPath $scriptPath -PathType Leaf) "One-command retrieval entrypoint is missing."

$root = Join-Path ([IO.Path]::GetTempPath()) ("retrieve-paper-test-" + [guid]::NewGuid().ToString("N"))
try {
  $dependencyRoot = Join-Path $root "dependency"
  $packageRoot = Join-Path $dependencyRoot "node_modules\playwright-core"
  $repoRoot = Join-Path $root "repo"
  $workRoot = Join-Path $repoRoot "raw\tmp\.work"
  $profileDir = Join-Path $root "profile"
  New-Item -ItemType Directory -Path $packageRoot -Force | Out-Null
  New-Item -ItemType Directory -Path $repoRoot -Force | Out-Null
  Set-Content -LiteralPath (Join-Path $packageRoot "package.json") -Encoding UTF8 -Value '{"version":"1.61.1"}'
  Set-Content -LiteralPath (Join-Path $dependencyRoot "package-lock.json") -Encoding UTF8 -Value @'
{
  "lockfileVersion": 3,
  "packages": {
    "": { "dependencies": { "playwright-core": "1.61.1" } },
    "node_modules/playwright-core": {
      "version": "1.61.1",
      "resolved": "https://registry.npmjs.org/playwright-core/-/playwright-core-1.61.1.tgz",
      "integrity": "sha512-h7Qlt6m4REp25qvIdvbDtVmD4LqVXfpRxhORv9L0jzETM05p4fuPJ3dKyuSXQxDSbXnmS79HAgi9589lGSpLkg=="
    }
  }
}
'@

  $fakeDownloader = Join-Path $root "fake-downloader.mjs"
  $downloaderArgsPath = Join-Path $root "downloader-args.json"
  Set-Content -LiteralPath $fakeDownloader -Encoding UTF8 -Value @'
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
const args = Object.fromEntries(process.argv.slice(2).reduce((pairs, value, index, all) => {
  if (value.startsWith("--") && index + 1 < all.length && !all[index + 1].startsWith("--")) {
    pairs.push([value, all[index + 1]]);
  }
  return pairs;
}, []));
if (process.env.FAKE_DOWNLOADER_ARGS_PATH) {
  await writeFile(process.env.FAKE_DOWNLOADER_ARGS_PATH, JSON.stringify(args), "utf8");
}
await mkdir(args["--work-dir"], { recursive: true });
const pdfPath = path.join(args["--work-dir"], "paper.pdf");
await writeFile(pdfPath, "%PDF-1.7\nsynthetic\n", "ascii");
process.stdout.write(JSON.stringify({ status: "downloaded", title: "A Synthetic IEEE Paper", doi: "10.1109/TEST.2026.1", pdfPath }) + "\n");
'@

  $fakeMineru = Join-Path $root "fake-mineru.ps1"
  Set-Content -LiteralPath $fakeMineru -Encoding UTF8 -Value @'
param([string]$PdfPath, [string]$OutputDir, [string]$SecretPath = "", [string]$NodePath = "", [string]$MineruScriptPath = "")
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
Set-Content -LiteralPath (Join-Path $OutputDir "full.md") -Encoding UTF8 -Value "# Stale root output"
$successfulOutput = Join-Path $OutputDir "precision"
New-Item -ItemType Directory -Path $successfulOutput -Force | Out-Null
Set-Content -LiteralPath (Join-Path $successfulOutput "full.md") -Encoding UTF8 -Value "# Synthetic paper"
@{ status = "converted"; mode = "precision"; outputDir = $successfulOutput } | ConvertTo-Json -Compress
'@

  $fakeStage = Join-Path $root "fake-stage.ps1"
  Set-Content -LiteralPath $fakeStage -Encoding UTF8 -Value @'
param([string]$PdfPath, [string]$MineruOutputDir, [string]$Title, [string]$Doi = "", [string]$RepoRoot)
$ErrorActionPreference = "Stop"
if (-not (Test-Path -LiteralPath $PdfPath -PathType Leaf)) { throw "PDF missing" }
if (-not (Test-Path -LiteralPath (Join-Path $MineruOutputDir "full.md") -PathType Leaf)) { throw "Markdown missing" }
if ((Split-Path -Leaf $MineruOutputDir) -ne "precision") { throw "Staging received stale MinerU root instead of successful output" }
@{ status = "staged"; title = $Title; doi = $Doi; directory = (Join-Path $RepoRoot "raw\tmp\synthetic") } | ConvertTo-Json -Compress
'@

  $env:FAKE_DOWNLOADER_ARGS_PATH = $downloaderArgsPath
  $resultJson = & powershell -NoProfile -ExecutionPolicy Bypass -File $scriptPath `
    -Reference "https://ieeexplore.ieee.org/document/11014597" `
    -RepoRoot $repoRoot `
    -WorkRoot $workRoot `
    -ProfileDir $profileDir `
    -DependencyRoot $dependencyRoot `
    -DownloaderScriptPath $fakeDownloader `
    -MineruInvokerPath $fakeMineru `
    -StageScriptPath $fakeStage `
    -NodePath (Get-Command node -ErrorAction Stop).Source `
    -AcceptAttributeRelease `
    -TestMode
  if ($LASTEXITCODE -ne 0) { throw "One-command retrieval exited with $LASTEXITCODE" }
  $result = $resultJson | ConvertFrom-Json
  Assert-True ($result.status -eq "staged") "Pipeline did not return the staged result."
  Assert-True ($result.title -eq "A Synthetic IEEE Paper") "Paper metadata was not forwarded."
  Assert-True ($result.doi -eq "10.1109/TEST.2026.1") "DOI was not forwarded."
  $downloaderArgs = Get-Content -LiteralPath $downloaderArgsPath -Raw | ConvertFrom-Json
  Assert-Equal $downloaderArgs.'--accept-attribute-release' "true" "Explicit attribute-release authorization must reach the browser adapter"

  $defaultWorkRoot = Join-Path $repoRoot "default-path-test"
  $savedErrorActionPreference = $ErrorActionPreference
  $ErrorActionPreference = "Continue"
  try {
    $defaultOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $scriptPath `
      -Reference "https://ieeexplore.ieee.org/document/11014597" `
      -RepoRoot $repoRoot `
      -WorkRoot $defaultWorkRoot `
      -ProfileDir (Join-Path $root "default-profile") `
      -DependencyRoot $dependencyRoot `
      -DownloadOnly `
      -TestMode 2>&1
    $defaultExitCode = $LASTEXITCODE
  }
  finally {
    $ErrorActionPreference = $savedErrorActionPreference
  }
  Assert-True ($defaultExitCode -ne 0) "The deliberately incomplete dependency should fail after startup."
  Assert-True (($defaultOutput | Out-String) -notmatch "Cannot bind argument to parameter 'Path'") `
    "Default component paths were evaluated before PSScriptRoot was available."
  $downloadLogs = @(Get-ChildItem -LiteralPath $defaultWorkRoot -Filter "download.stderr.log" -File -Recurse)
  Assert-True ($downloadLogs.Count -eq 1) "The default downloader path was not reached."

  $retryDownloader = Join-Path $root "retry-downloader.mjs"
  Set-Content -LiteralPath $retryDownloader -Encoding UTF8 -Value @'
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
const args = Object.fromEntries(process.argv.slice(2).reduce((pairs, value, index, all) => {
  if (value.startsWith("--") && index + 1 < all.length && !all[index + 1].startsWith("--")) pairs.push([value, all[index + 1]]);
  return pairs;
}, []));
await mkdir(args["--work-dir"], { recursive: true });
const marker = path.join(args["--work-dir"], "attempt.txt");
let attempts = 0;
try { attempts = Number(await readFile(marker, "utf8")); } catch {}
attempts += 1;
await writeFile(marker, String(attempts));
if (attempts === 1) {
  process.stderr.write(JSON.stringify({ status: "error", phase: "paper-metadata", message: "transient" }) + "\n");
  process.exit(1);
}
const pdfPath = path.join(args["--work-dir"], "paper.pdf");
await writeFile(pdfPath, "%PDF-1.7\nretry\n", "ascii");
process.stdout.write(JSON.stringify({ status: "downloaded", title: "Retried IEEE Paper", doi: "10.1109/TEST.RETRY", pdfPath }) + "\n");
'@
  $retryWorkRoot = Join-Path $repoRoot "retry-work"
  $retryJson = & powershell -NoProfile -ExecutionPolicy Bypass -File $scriptPath `
    -Reference "https://ieeexplore.ieee.org/document/11014597" `
    -RepoRoot $repoRoot `
    -WorkRoot $retryWorkRoot `
    -ProfileDir (Join-Path $root "retry-profile") `
    -DependencyRoot $dependencyRoot `
    -DownloaderScriptPath $retryDownloader `
    -MineruInvokerPath $fakeMineru `
    -StageScriptPath $fakeStage `
    -NodePath (Get-Command node -ErrorAction Stop).Source `
    -DownloadOnly `
    -TestMode
  if ($LASTEXITCODE -ne 0) { throw "Bounded metadata retry exited with $LASTEXITCODE" }
  $retryResult = $retryJson | ConvertFrom-Json
  Assert-True ($retryResult.status -eq "downloaded") "Metadata restart did not recover."
  $retryAttemptFiles = @(Get-ChildItem -LiteralPath $retryWorkRoot -Filter "attempt.txt" -File -Recurse)
  Assert-True ($retryAttemptFiles.Count -eq 1) "Metadata retry did not reuse the run work directory."
  Assert-True ((Get-Content -LiteralPath $retryAttemptFiles[0].FullName -Raw).Trim() -eq "2") `
    "Only one metadata restart is allowed."

  $savedErrorActionPreference = $ErrorActionPreference
  $ErrorActionPreference = "Continue"
  try {
    $boundaryOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $scriptPath `
      -Reference "https://ieeexplore.ieee.org/document/11014597" `
      -RepoRoot $repoRoot `
      -WorkRoot (Join-Path $repoRoot "raw\sources") `
      -ProfileDir $profileDir `
      -DependencyRoot $dependencyRoot `
      -DownloadOnly 2>&1
    $boundaryExitCode = $LASTEXITCODE
  }
  finally {
    $ErrorActionPreference = $savedErrorActionPreference
  }
  Assert-True ($boundaryExitCode -ne 0) "Production mode must reject work outside raw/tmp/.work."
  Assert-True (($boundaryOutput | Out-String) -match "raw[/\\]tmp[/\\]\.work") "Work boundary error must name the allowed root."

  $plainErrorDownloader = Join-Path $root "plain-error-downloader.mjs"
  Set-Content -LiteralPath $plainErrorDownloader -Encoding UTF8 -Value @'
process.stderr.write("plain downloader failure");
process.exit(1);
'@
  $savedErrorActionPreference = $ErrorActionPreference
  $ErrorActionPreference = "Continue"
  try {
    $plainErrorOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $scriptPath `
      -Reference "https://ieeexplore.ieee.org/document/11014597" `
      -RepoRoot $repoRoot `
      -WorkRoot (Join-Path $repoRoot "raw\tmp\.work") `
      -ProfileDir (Join-Path $root "plain-profile") `
      -DependencyRoot $dependencyRoot `
      -DownloaderScriptPath $plainErrorDownloader `
      -NodePath (Get-Command node -ErrorAction Stop).Source `
      -DownloadOnly `
      -TestMode 2>&1
    $plainErrorExitCode = $LASTEXITCODE
  }
  finally {
    $ErrorActionPreference = $savedErrorActionPreference
  }
  Assert-True ($plainErrorExitCode -ne 0) "Plain downloader failure must be reported."
  Assert-True (($plainErrorOutput | Out-String) -match "IEEE retrieval failed") "Plain stderr must produce the bounded retrieval error."
  Assert-True (($plainErrorOutput | Out-String) -notmatch "property 'phase'") "Plain stderr must not trigger a StrictMode property error."

  $repairDependencyRoot = Join-Path $root "repair-dependency"
  $repairPackageRoot = Join-Path $repairDependencyRoot "node_modules\playwright-core"
  New-Item -ItemType Directory -Path $repairPackageRoot -Force | Out-Null
  Set-Content -LiteralPath (Join-Path $repairPackageRoot "package.json") -Encoding UTF8 -Value '{"version":"1.61.1"}'
  Set-Content -LiteralPath (Join-Path $repairDependencyRoot "package-lock.json") -Encoding UTF8 -Value '{"lockfileVersion":3,"packages":{"":{"dependencies":{"playwright-core":"1.61.1"}},"node_modules/playwright-core":{"version":"1.61.1","resolved":"https://untrusted.example/playwright.tgz","integrity":"sha512-wrong"}}}'
  $npmArgsPath = Join-Path $root "npm-args.txt"
  $fakeNpm = Join-Path $root "fake-npm.ps1"
  Set-Content -LiteralPath $fakeNpm -Encoding UTF8 -Value @'
$ErrorActionPreference = "Stop"
Set-Content -LiteralPath $env:FAKE_NPM_ARGS_PATH -Value ($args -join "`n") -Encoding UTF8
$prefixIndex = [Array]::IndexOf($args, "--prefix")
if ($prefixIndex -lt 0) { throw "missing --prefix" }
$dependencyRoot = $args[$prefixIndex + 1]
$packageRoot = Join-Path $dependencyRoot "node_modules\playwright-core"
New-Item -ItemType Directory -Path $packageRoot -Force | Out-Null
Set-Content -LiteralPath (Join-Path $packageRoot "package.json") -Encoding UTF8 -Value '{"version":"1.61.1"}'
Set-Content -LiteralPath (Join-Path $dependencyRoot "package-lock.json") -Encoding UTF8 -Value '{"lockfileVersion":3,"packages":{"":{"dependencies":{"playwright-core":"1.61.1"}},"node_modules/playwright-core":{"version":"1.61.1","resolved":"https://registry.npmjs.org/playwright-core/-/playwright-core-1.61.1.tgz","integrity":"sha512-h7Qlt6m4REp25qvIdvbDtVmD4LqVXfpRxhORv9L0jzETM05p4fuPJ3dKyuSXQxDSbXnmS79HAgi9589lGSpLkg=="}}}'
'@
  $env:FAKE_NPM_ARGS_PATH = $npmArgsPath
  try {
    $repairJson = & powershell -NoProfile -ExecutionPolicy Bypass -File $scriptPath `
      -Reference "https://ieeexplore.ieee.org/document/11014597" `
      -RepoRoot $repoRoot `
      -WorkRoot (Join-Path $repoRoot "raw\tmp\.work") `
      -ProfileDir (Join-Path $root "repair-profile") `
      -DependencyRoot $repairDependencyRoot `
      -NpmPath $fakeNpm `
      -DownloaderScriptPath $fakeDownloader `
      -NodePath (Get-Command node -ErrorAction Stop).Source `
      -DownloadOnly `
      -TestMode
  }
  finally {
    Remove-Item Env:FAKE_NPM_ARGS_PATH -ErrorAction SilentlyContinue
  }
  Assert-Equal ($repairJson | ConvertFrom-Json).status "downloaded" "Integrity repair pipeline status"
  $npmArgs = @(Get-Content -LiteralPath $npmArgsPath)
  Assert-Equal $npmArgs[0] "ci" "npm must install from the prebuilt integrity-pinned lockfile"
  Assert-True ($npmArgs -contains "--ignore-scripts") "npm lifecycle scripts must be disabled."
  Assert-True ($npmArgs -contains "https://registry.npmjs.org") "npm registry must be pinned to the official registry."
  Add-Type -AssemblyName System.Web.Extensions
  $serializer = [Web.Script.Serialization.JavaScriptSerializer]::new()
  $repairedLock = $serializer.DeserializeObject((Get-Content -LiteralPath (Join-Path $repairDependencyRoot "package-lock.json") -Raw))
  $repairedPackage = $repairedLock["packages"]["node_modules/playwright-core"]
  Assert-Equal $repairedPackage["version"] "1.61.1" "Playwright package version must be exact."
  Assert-Equal $repairedPackage["integrity"] `
    "sha512-h7Qlt6m4REp25qvIdvbDtVmD4LqVXfpRxhORv9L0jzETM05p4fuPJ3dKyuSXQxDSbXnmS79HAgi9589lGSpLkg==" `
    "Playwright lock integrity must be exact."

  Write-Output "PASS: one command performs download, MinerU conversion, and staging."
}
finally {
  Remove-Item Env:FAKE_DOWNLOADER_ARGS_PATH -ErrorAction SilentlyContinue
  if (Test-Path -LiteralPath $root) {
    Remove-Item -LiteralPath $root -Recurse -Force
  }
}
