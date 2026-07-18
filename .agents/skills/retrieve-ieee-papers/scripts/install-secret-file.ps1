[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$SourcePath,

  [string]$DestinationPath = "",

  [string]$RepoRoot = "",

  [switch]$Force,

  [switch]$TestMode
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

. (Join-Path $PSScriptRoot "secret-store.ps1")

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $RepoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..\..")).Path
}
$resolvedRepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$allowedRoot = [IO.Path]::GetFullPath((Join-Path $resolvedRepoRoot "raw\tmp\.work")).TrimEnd('\', '/')
$resolvedSource = (Resolve-Path -LiteralPath $SourcePath).Path
$allowedPrefix = $allowedRoot + [IO.Path]::DirectorySeparatorChar
if (-not $resolvedSource.StartsWith($allowedPrefix, [StringComparison]::OrdinalIgnoreCase)) {
  throw "Encrypted provisioning source must be a file under raw/tmp/.work."
}
if (-not (Test-Path -LiteralPath $resolvedSource -PathType Leaf)) {
  throw "Encrypted provisioning source is missing: $resolvedSource"
}

$expectedDestination = [IO.Path]::GetFullPath((Get-RetrievalSecretPath))
if ([string]::IsNullOrWhiteSpace($DestinationPath)) { $DestinationPath = $expectedDestination }
$destination = [IO.Path]::GetFullPath($DestinationPath)
if (-not $TestMode -and
    -not $destination.Equals($expectedDestination, [StringComparison]::OrdinalIgnoreCase)) {
  throw "Encrypted credentials may only be installed at the dedicated LocalAppData secret path: $expectedDestination"
}
if ((Test-Path -LiteralPath $destination) -and -not $Force) {
  throw "Encrypted credential destination already exists. Re-run with -Force to replace it: $destination"
}

$destinationParent = Split-Path -Parent $destination
New-Item -ItemType Directory -Path $destinationParent -Force | Out-Null
$temporaryDestination = "$destination.$([guid]::NewGuid().ToString('N')).tmp"
try {
  Copy-Item -LiteralPath $resolvedSource -Destination $temporaryDestination
  Set-RetrievalSecretAcl -Path $temporaryDestination
  Move-Item -LiteralPath $temporaryDestination -Destination $destination -Force
  Set-RetrievalSecretAcl -Path $destination
  Remove-Item -LiteralPath $resolvedSource -Force

  [ordered]@{
    status = "installed"
    path = $destination
  } | ConvertTo-Json -Compress
}
finally {
  if (Test-Path -LiteralPath $temporaryDestination) {
    Remove-Item -LiteralPath $temporaryDestination -Force
  }
}
