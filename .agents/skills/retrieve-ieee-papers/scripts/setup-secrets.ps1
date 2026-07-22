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

$organization = Read-Host "Institution display name"
$carsiSchoolPlaceholder = Read-Host "CARSI institution-search placeholder"
$carsiSearchText = Read-Host "CARSI search text"
$carsiInstitution = Read-Host "Exact CARSI institution option"
$carsiLoginButtonName = Read-Host "CARSI login button name"
$carsiEntityId = Read-Host "Exact CARSI IdP entity ID (HTTPS URL)"
$credentialHost = Read-Host "Exact institutional IdP hostname (no scheme or path)"
$usernameLabel = Read-Host "Username field label"
$passwordLabel = Read-Host "Password field label"
$loginButtonName = Read-Host "Institution login button name"
$resourceAccessUrl = Read-Host "CARSI post-login IEEE resource access URL"
$attributeReleaseTitle = Read-Host "Optional exact attribute-release page title"
$attributeReleaseAcceptControlName = Read-Host "Optional exact attribute-release accept control name"
$attributeReleaseRejectControlName = Read-Host "Optional exact attribute-release reject control name"
$usernameSecure = Read-Host "Institution username" -AsSecureString
$password = Read-Host "Institution password" -AsSecureString
$mineruToken = Read-Host "MinerU API token" -AsSecureString
$username = $null
try {
  $username = ConvertFrom-RetrievalSecureString $usernameSecure
  if ([string]::IsNullOrWhiteSpace($username)) { throw "Username cannot be empty." }
  $credential = [Management.Automation.PSCredential]::new($username.Trim(), $password)
  $institutionProfile = [ordered]@{
    Organization = $organization
    CarsiSchoolPlaceholder = $carsiSchoolPlaceholder
    CarsiSearchText = $carsiSearchText
    CarsiInstitution = $carsiInstitution
    CarsiLoginButtonName = $carsiLoginButtonName
    CarsiEntityId = $carsiEntityId
    CredentialHost = $credentialHost
    UsernameLabel = $usernameLabel
    PasswordLabel = $passwordLabel
    LoginButtonName = $loginButtonName
    ResourceAccessUrl = $resourceAccessUrl
    AttributeReleaseTitle = $attributeReleaseTitle
    AttributeReleaseAcceptControlName = $attributeReleaseAcceptControlName
    AttributeReleaseRejectControlName = $attributeReleaseRejectControlName
  }
  Export-RetrievalSecrets -InstitutionProfile $institutionProfile -IeeeCredential $credential -MinerUToken $mineruToken -Path $Path
  Write-Output "Encrypted retrieval secrets stored at: $Path"
}
finally {
  $username = $null
  $credential = $null
  $institutionProfile = $null
}
