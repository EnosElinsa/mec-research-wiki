param(
  [string]$Path = "",
  [switch]$Force
)

$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "secret-store.ps1")

if ([string]::IsNullOrWhiteSpace($Path)) { $Path = Get-RetrievalSecretPath }
if ((Test-Path -LiteralPath $Path) -and -not $Force) {
  throw "Secret file already exists. Re-run with -Force to replace it: $Path"
}

$usernameSecure = Read-Host "Guangxi University username" -AsSecureString
$password = Read-Host "Guangxi University password" -AsSecureString
$mineruToken = Read-Host "MinerU API token" -AsSecureString
$username = $null
try {
  $username = ConvertFrom-RetrievalSecureString $usernameSecure
  if ([string]::IsNullOrWhiteSpace($username)) { throw "Username cannot be empty." }
  $credential = [Management.Automation.PSCredential]::new($username.Trim(), $password)
  Export-RetrievalSecrets -IeeeCredential $credential -MinerUToken $mineruToken -Path $Path
  Write-Output "Encrypted retrieval secrets stored at: $Path"
}
finally {
  $username = $null
  $credential = $null
}
