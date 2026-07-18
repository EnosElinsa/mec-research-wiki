[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$PdfPath,

  [Parameter(Mandatory = $true)]
  [string]$MineruOutputDir,

  [Parameter(Mandatory = $true)]
  [string]$Title,

  [string]$Doi = "",

  [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Assert-PdfFile([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    throw "Downloaded PDF is missing: $Path"
  }

  $stream = [IO.File]::OpenRead($Path)
  try {
    if ($stream.Length -lt 5) {
      throw "Downloaded file is too short to be a PDF: $Path"
    }
    $header = New-Object byte[] 5
    if ($stream.Read($header, 0, 5) -ne 5) {
      throw "Could not read the downloaded PDF header: $Path"
    }
    if ([Text.Encoding]::ASCII.GetString($header) -cne "%PDF-") {
      throw "Downloaded file is not a PDF (missing %PDF- header): $Path"
    }
  }
  finally {
    $stream.Dispose()
  }
}

function Get-ParsedMarkdown([string]$OutputDir) {
  if (-not (Test-Path -LiteralPath $OutputDir -PathType Container)) {
    throw "MinerU output directory is missing: $OutputDir"
  }

  $usable = @(
    Get-ChildItem -LiteralPath $OutputDir -Filter "*.md" -File -Recurse |
      Where-Object { -not [string]::IsNullOrWhiteSpace([IO.File]::ReadAllText($_.FullName)) }
  )
  if ($usable.Count -eq 0) {
    throw "MinerU produced no non-empty Markdown file under: $OutputDir"
  }

  $preferred = @($usable | Where-Object { $_.Name -ieq "full.md" })
  if ($preferred.Count -gt 0) {
    return $preferred | Sort-Object @{ Expression = { $_.FullName.Length } }, FullName | Select-Object -First 1
  }

  return $usable | Sort-Object @{ Expression = { $_.Length }; Descending = $true }, FullName | Select-Object -First 1
}

function Find-SourceCollision([string]$Root, [string]$OutputKey) {
  if (-not (Test-Path -LiteralPath $Root -PathType Container)) { return $null }

  foreach ($directory in (Get-ChildItem -LiteralPath $Root -Directory)) {
    if ($directory.Name -eq ".work") { continue }
    if ((Get-OutputSourceKey $directory.Name) -eq $OutputKey) {
      return $directory.FullName
    }
  }
  return $null
}

function Copy-ImageTree([IO.DirectoryInfo]$Source, [string]$Destination) {
  foreach ($file in (Get-ChildItem -LiteralPath $Source.FullName -File -Recurse)) {
    $relative = $file.FullName.Substring($Source.FullName.Length).TrimStart('\', '/')
    $target = Join-Path $Destination $relative
    $targetParent = Split-Path -Parent $target
    New-Item -ItemType Directory -Path $targetParent -Force | Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $target
  }
}

$resolvedRepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$namingScript = Join-Path $resolvedRepoRoot "tools\source_naming.ps1"
if (-not (Test-Path -LiteralPath $namingScript -PathType Leaf)) {
  throw "Repository naming authority is missing: $namingScript"
}
. $namingScript

Assert-PdfFile $PdfPath
$markdown = Get-ParsedMarkdown $MineruOutputDir
$safeName = Get-SafeSourceName $Title
$outputKey = Get-OutputSourceKey $safeName
$sourcesRoot = Join-Path $resolvedRepoRoot "raw\sources"
$tmpRoot = Join-Path $resolvedRepoRoot "raw\tmp"

$sourceCollision = Find-SourceCollision $sourcesRoot $outputKey
if ($sourceCollision) {
  throw "Paper already exists in raw/sources: $sourceCollision"
}
$tmpCollision = Find-SourceCollision $tmpRoot $outputKey
if ($tmpCollision) {
  throw "Paper is already staged in raw/tmp: $tmpCollision"
}

New-Item -ItemType Directory -Path $tmpRoot -Force | Out-Null
$workRoot = Join-Path $tmpRoot ".work"
New-Item -ItemType Directory -Path $workRoot -Force | Out-Null
$workBundle = Join-Path $workRoot ([guid]::NewGuid().ToString("N"))
$finalBundle = Join-Path $tmpRoot $safeName

try {
  New-Item -ItemType Directory -Path $workBundle -Force | Out-Null
  $imagesDestination = Join-Path $workBundle "images"
  New-Item -ItemType Directory -Path $imagesDestination -Force | Out-Null

  $stagedPdf = Join-Path $workBundle ($safeName + ".pdf")
  $stagedMarkdown = Join-Path $workBundle ($safeName + ".md")
  Copy-Item -LiteralPath $PdfPath -Destination $stagedPdf
  Copy-Item -LiteralPath $markdown.FullName -Destination $stagedMarkdown

  $siblingImages = Join-Path $markdown.Directory.FullName "images"
  $imageRoots = if (Test-Path -LiteralPath $siblingImages -PathType Container) {
    @((Get-Item -LiteralPath $siblingImages))
  }
  else {
    @(Get-ChildItem -LiteralPath $MineruOutputDir -Directory -Recurse | Where-Object { $_.Name -ieq "images" })
  }
  foreach ($imageRoot in $imageRoots) {
    Copy-ImageTree $imageRoot $imagesDestination
  }

  if (Test-Path -LiteralPath $finalBundle) {
    throw "Staging destination appeared while preparing the bundle: $finalBundle"
  }
  Move-Item -LiteralPath $workBundle -Destination $finalBundle

  [ordered]@{
    status = "staged"
    name = $safeName
    title = $Title
    doi = $Doi
    directory = $finalBundle
    pdf = (Join-Path $finalBundle ($safeName + ".pdf"))
    markdown = (Join-Path $finalBundle ($safeName + ".md"))
  } | ConvertTo-Json -Compress
}
finally {
  if (Test-Path -LiteralPath $workBundle) {
    Remove-Item -LiteralPath $workBundle -Recurse -Force
  }
}
