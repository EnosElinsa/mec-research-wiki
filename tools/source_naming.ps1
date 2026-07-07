$ErrorActionPreference = "Stop"

function Get-SourceTitleFromName([string]$Name) {
  $leaf = Split-Path -Leaf $Name
  $baseName = if ($leaf -match '(?i)\.(pdf|md|markdown|html|json|docx?|pptx?|xlsx?)$') {
    [IO.Path]::GetFileNameWithoutExtension($leaf)
  } else {
    $leaf
  }
  return (($baseName -replace "^[0-9]{3,4}[_\-\s]+", "").Trim())
}

function Get-NormalizedSourceKey([string]$Text) {
  $title = Get-SourceTitleFromName $Text
  return (($title.ToLowerInvariant()) -replace "[^a-z0-9]+", "")
}

function Get-OutputSourceKey([string]$Text) {
  $safeName = Get-SafeSourceName $Text
  return (($safeName.ToLowerInvariant()) -replace "[^a-z0-9]+", "")
}

function Get-SafeSourceName([string]$Title) {
  $safe = Get-SourceTitleFromName $Title
  $safe = $safe -replace '[\u2010-\u2015]', "-"
  $safe = $safe -replace '[<>:"/\\|?*]', "-"
  $safe = $safe -replace '\s*-\s+', "_"
  $safe = $safe -replace '\s+-\s*', "_"
  $safe = $safe -replace '[\(\)\[\]\{\}]', ""
  $safe = $safe -replace "[,;]+", ""
  $safe = $safe -replace "\.", "_"
  $safe = $safe -replace "\s+", "_"
  $safe = $safe -replace "_+", "_"
  $safe = $safe -replace "_-_", "_"
  $safe = $safe.Trim(" ._")

  if ($safe.Length -gt 180) {
    $safe = $safe.Substring(0, 180).Trim(" ._")
  }

  if ([string]::IsNullOrWhiteSpace($safe)) {
    throw "Cannot derive a safe output name from title: $Title"
  }

  return $safe
}
