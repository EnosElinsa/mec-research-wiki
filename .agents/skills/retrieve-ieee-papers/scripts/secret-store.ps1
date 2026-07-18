$ErrorActionPreference = "Stop"

function Get-RetrievalSecretPath([string]$LocalAppData = $env:LOCALAPPDATA) {
  if ([string]::IsNullOrWhiteSpace($LocalAppData)) {
    throw "LOCALAPPDATA is unavailable; cannot resolve the DPAPI secret path."
  }
  return (Join-Path $LocalAppData "Codex\secrets\retrieve-ieee-papers.clixml")
}

function ConvertFrom-RetrievalSecureString([Security.SecureString]$Value) {
  if ($null -eq $Value) { throw "Secure value is missing." }
  $pointer = [IntPtr]::Zero
  try {
    $pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($Value)
    return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer)
  }
  finally {
    if ($pointer -ne [IntPtr]::Zero) {
      [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer)
    }
  }
}

function Set-RetrievalSecretAcl([string]$Path) {
  $identity = [Security.Principal.WindowsIdentity]::GetCurrent().Name
  $icacls = Join-Path $env:SystemRoot "System32\icacls.exe"
  if (-not (Test-Path -LiteralPath $icacls)) {
    throw "icacls.exe is unavailable; cannot restrict the secret file ACL."
  }
  & $icacls $Path "/inheritance:e" "/grant:r" "${identity}:(F)" | Out-Null
  if ($LASTEXITCODE -ne 0) {
    throw "Failed to restrict the secret file ACL."
  }
}

function Export-RetrievalSecrets(
  [Management.Automation.PSCredential]$IeeeCredential,
  [Security.SecureString]$MinerUToken,
  [string]$Path = (Get-RetrievalSecretPath)
) {
  if ($null -eq $IeeeCredential -or [string]::IsNullOrWhiteSpace($IeeeCredential.UserName)) {
    throw "IEEE institutional credential is missing."
  }
  if ($null -eq $MinerUToken -or $MinerUToken.Length -eq 0) {
    throw "MinerU token is missing."
  }
  if ([string]::IsNullOrWhiteSpace($Path)) { throw "Secret path is missing." }

  $parent = Split-Path -Parent $Path
  if ([string]::IsNullOrWhiteSpace($parent)) { throw "Secret path must include a parent directory." }
  if (-not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
  }

  $payload = [pscustomobject]@{
    SchemaVersion = 1
    Organization = "Guangxi University"
    IeeeCredential = $IeeeCredential
    MinerUToken = $MinerUToken
  }
  $temporaryPath = "$Path.$([guid]::NewGuid().ToString('N')).tmp"
  try {
    $payload | Export-Clixml -LiteralPath $temporaryPath
    Set-RetrievalSecretAcl -Path $temporaryPath
    Move-Item -LiteralPath $temporaryPath -Destination $Path -Force
    Set-RetrievalSecretAcl -Path $Path
  }
  finally {
    if (Test-Path -LiteralPath $temporaryPath) {
      Remove-Item -LiteralPath $temporaryPath -Force
    }
  }
}

function Import-RetrievalSecrets([string]$Path = (Get-RetrievalSecretPath)) {
  if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    throw "DPAPI secret file is missing: $Path"
  }
  $payload = Import-Clixml -LiteralPath $Path
  if ($null -eq $payload -or [int]$payload.SchemaVersion -ne 1) {
    throw "Unsupported retrieval secret schema."
  }
  if ($payload.Organization -ne "Guangxi University") {
    throw "Unexpected organization in retrieval secret file."
  }
  if ($payload.IeeeCredential -isnot [Management.Automation.PSCredential]) {
    throw "IEEE credential is missing or invalid."
  }
  if ($payload.MinerUToken -isnot [Security.SecureString] -or $payload.MinerUToken.Length -eq 0) {
    throw "MinerU token is missing or invalid."
  }
  return $payload
}
