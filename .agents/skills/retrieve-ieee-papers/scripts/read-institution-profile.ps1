param(
  [string]$SecretPath = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false)
. (Join-Path $PSScriptRoot "secret-store.ps1")
if ([string]::IsNullOrWhiteSpace($SecretPath)) { $SecretPath = Get-RetrievalSecretPath }

$payload = Import-RetrievalSecrets -Path $SecretPath
$profile = $payload.InstitutionProfile
[ordered]@{
  organization = $profile.Organization
  carsiSchoolPlaceholder = $profile.CarsiSchoolPlaceholder
  carsiSearchText = $profile.CarsiSearchText
  carsiInstitution = $profile.CarsiInstitution
  carsiLoginButtonName = $profile.CarsiLoginButtonName
  carsiEntityId = $profile.CarsiEntityId
  credentialHost = $profile.CredentialHost
  usernameLabel = $profile.UsernameLabel
  passwordLabel = $profile.PasswordLabel
  loginButtonName = $profile.LoginButtonName
  resourceAccessUrl = $profile.ResourceAccessUrl
  attributeReleaseTitle = $profile.AttributeReleaseTitle
  attributeReleaseAcceptControlName = $profile.AttributeReleaseAcceptControlName
  attributeReleaseRejectControlName = $profile.AttributeReleaseRejectControlName
} | ConvertTo-Json -Compress
