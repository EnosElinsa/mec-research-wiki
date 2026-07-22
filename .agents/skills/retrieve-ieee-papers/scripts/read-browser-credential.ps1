param(
  [Parameter(Mandatory)][string]$ExpectedHost,
  [string]$SecretPath = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [Text.UTF8Encoding]::new($false)
. (Join-Path $PSScriptRoot "secret-store.ps1")
if ([string]::IsNullOrWhiteSpace($SecretPath)) { $SecretPath = Get-RetrievalSecretPath }

$password = $null
try {
  $payload = Import-RetrievalSecrets -Path $SecretPath
  $expected = $ExpectedHost.Trim()
  if ($expected.EndsWith(".") -or
      $expected.ToLowerInvariant() -ne $payload.InstitutionProfile.CredentialHost.ToLowerInvariant()) {
    throw "Credential release denied for unapproved host."
  }
  $password = ConvertFrom-RetrievalSecureString $payload.IeeeCredential.Password
  [pscustomobject]@{
    username = $payload.IeeeCredential.UserName
    password = $password
  } | ConvertTo-Json -Compress
}
finally {
  $password = $null
  $payload = $null
}
