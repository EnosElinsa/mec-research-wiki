[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$Title,

  [string]$Doi = "",

  [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")).Path
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$resolvedRepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$namingScript = Join-Path $resolvedRepoRoot "tools\source_naming.ps1"
if (-not (Test-Path -LiteralPath $namingScript -PathType Leaf)) {
  throw "Repository naming authority is missing: $namingScript"
}
. $namingScript

$safeName = Get-SafeSourceName $Title
$outputKey = Get-OutputSourceKey $safeName
$roots = @(
  [pscustomobject]@{ Label = "raw/sources"; Path = (Join-Path $resolvedRepoRoot "raw\sources") },
  [pscustomobject]@{ Label = "raw/tmp"; Path = (Join-Path $resolvedRepoRoot "raw\tmp") }
)

foreach ($root in $roots) {
  if (-not (Test-Path -LiteralPath $root.Path -PathType Container)) { continue }
  foreach ($directory in (Get-ChildItem -LiteralPath $root.Path -Directory)) {
    if ($directory.Name -eq ".work") { continue }
    if ((Get-OutputSourceKey $directory.Name) -eq $outputKey) {
      [ordered]@{
        status = "existing"
        name = $safeName
        doi = $Doi
        sourceRoot = $root.Label
        path = $directory.FullName
      } | ConvertTo-Json -Compress
      return
    }
  }
}

[ordered]@{
  status = "missing"
  name = $safeName
  doi = $Doi
  sourceRoot = ""
  path = ""
} | ConvertTo-Json -Compress
