$ErrorActionPreference = "Stop"

function Assert-True([bool]$Condition, [string]$Message) {
  if (-not $Condition) { throw "ASSERT TRUE FAILED: $Message" }
}

function Assert-Equal($Actual, $Expected, [string]$Message) {
  if ($Actual -ne $Expected) {
    throw "ASSERT EQUAL FAILED: $Message expected=[$Expected] actual=[$Actual]"
  }
}

function Assert-Throws([scriptblock]$Action, [string]$Message) {
  $threw = $false
  try { & $Action } catch { $threw = $true }
  if (-not $threw) { throw "ASSERT THROWS FAILED: $Message" }
}

function Write-MinimalPdf([string]$Path) {
  [IO.File]::WriteAllBytes($Path, [Text.Encoding]::ASCII.GetBytes("%PDF-1.4`n%%EOF`n"))
}

function New-TestRepo([string]$Root, [string]$NamingScript) {
  New-Item -ItemType Directory -Path (Join-Path $Root "tools") -Force | Out-Null
  New-Item -ItemType Directory -Path (Join-Path $Root "raw\sources") -Force | Out-Null
  Copy-Item -LiteralPath $NamingScript -Destination (Join-Path $Root "tools\source_naming.ps1")
}

$scriptsRoot = Split-Path -Parent $PSScriptRoot
$stagePath = Join-Path $scriptsRoot "stage-paper.ps1"
$duplicateCheckPath = Join-Path $scriptsRoot "check-paper-duplicate.ps1"
$repoRoot = (Resolve-Path (Join-Path $scriptsRoot "..\..\..\..")).Path
$namingScript = Join-Path $repoRoot "tools\source_naming.ps1"

if (-not (Test-Path -LiteralPath $stagePath)) {
  throw "Expected implementation file is missing: $stagePath"
}
if (-not (Test-Path -LiteralPath $duplicateCheckPath)) {
  throw "Expected implementation file is missing: $duplicateCheckPath"
}

. $namingScript

$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("retrieve-ieee-stage-test-" + [guid]::NewGuid().ToString("N"))

try {
  New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

  $repo = Join-Path $tempRoot "repo"
  New-TestRepo $repo $namingScript
  $pdf = Join-Path $tempRoot "paper.pdf"
  Write-MinimalPdf $pdf
  $mineru = Join-Path $tempRoot "mineru"
  New-Item -ItemType Directory -Path (Join-Path $mineru "images") -Force | Out-Null
  Set-Content -LiteralPath (Join-Path $mineru "full.md") -Value "# Parsed paper`n`n![figure](images/figure.png)" -Encoding UTF8
  [IO.File]::WriteAllBytes((Join-Path $mineru "images\figure.png"), [byte[]](1, 2, 3))

  $title = "3-D Scheduling for MEC 2.0: A Test"
  $expectedName = Get-SafeSourceName $title
  $result = & $stagePath -PdfPath $pdf -MineruOutputDir $mineru -Title $title -Doi "10.1109/TEST.2026.1" -RepoRoot $repo | ConvertFrom-Json
  $bundle = Join-Path $repo ("raw\tmp\" + $expectedName)

  Assert-Equal $result.status "staged" "result status"
  Assert-Equal $result.name $expectedName "repository naming authority"
  Assert-True (Test-Path -LiteralPath $bundle -PathType Container) "bundle directory"
  Assert-True (Test-Path -LiteralPath (Join-Path $bundle ($expectedName + ".pdf"))) "renamed PDF"
  Assert-True (Test-Path -LiteralPath (Join-Path $bundle ($expectedName + ".md"))) "renamed Markdown"
  Assert-True (Test-Path -LiteralPath (Join-Path $bundle "images\figure.png")) "images copied"
  Assert-True (-not (Test-Path -LiteralPath (Join-Path $repo "raw\sources\$expectedName"))) "must not write raw/sources"

  $preflight = & $duplicateCheckPath -Title $title -RepoRoot $repo | ConvertFrom-Json
  Assert-Equal $preflight.status "existing" "preflight finds staged paper"
  Assert-Equal $preflight.sourceRoot "raw/tmp" "preflight reports staging root"
  Assert-Equal $preflight.path $bundle "preflight returns existing path"

  $missingPreflight = & $duplicateCheckPath -Title "A New Missing Paper" -RepoRoot $repo | ConvertFrom-Json
  Assert-Equal $missingPreflight.status "missing" "preflight allows new paper"

  Assert-Throws {
    & $stagePath -PdfPath $pdf -MineruOutputDir $mineru -Title $title -RepoRoot $repo | Out-Null
  } "duplicate in raw/tmp must fail"

  $sourceCollisionTitle = "Already Curated Paper"
  $sourceCollisionName = Get-SafeSourceName $sourceCollisionTitle
  New-Item -ItemType Directory -Path (Join-Path $repo "raw\sources\$sourceCollisionName") -Force | Out-Null
  Assert-Throws {
    & $stagePath -PdfPath $pdf -MineruOutputDir $mineru -Title $sourceCollisionTitle -RepoRoot $repo | Out-Null
  } "duplicate in raw/sources must fail"

  $htmlPdf = Join-Path $tempRoot "not-a-paper.pdf"
  Set-Content -LiteralPath $htmlPdf -Value "<!DOCTYPE html><title>Sign in</title>" -Encoding UTF8
  Assert-Throws {
    & $stagePath -PdfPath $htmlPdf -MineruOutputDir $mineru -Title "HTML Download" -RepoRoot $repo | Out-Null
  } "HTML masquerading as PDF must fail"

  $emptyMineru = Join-Path $tempRoot "empty-mineru"
  New-Item -ItemType Directory -Path $emptyMineru -Force | Out-Null
  Set-Content -LiteralPath (Join-Path $emptyMineru "full.md") -Value "   " -Encoding UTF8
  Assert-Throws {
    & $stagePath -PdfPath $pdf -MineruOutputDir $emptyMineru -Title "Empty Parse" -RepoRoot $repo | Out-Null
  } "empty Markdown must fail"

  $longRepo = Join-Path $tempRoot "long-repo"
  New-TestRepo $longRepo $namingScript
  $longTitle = ((1..40 | ForEach-Object { "LongTitleSegment$_" }) -join " ")
  $longResult = & $stagePath -PdfPath $pdf -MineruOutputDir $mineru -Title $longTitle -RepoRoot $longRepo | ConvertFrom-Json
  Assert-True ($longResult.name.Length -le 180) "long name must respect repository limit"

  Write-Output "PASS PDF and Markdown validation"
  Write-Output "PASS source naming and duplicate gates"
  Write-Output "PASS atomic raw/tmp bundle staging"
}
finally {
  if (Test-Path -LiteralPath $tempRoot) {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
  }
}
