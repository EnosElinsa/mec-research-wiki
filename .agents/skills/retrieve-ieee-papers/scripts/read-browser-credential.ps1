param(
  [Parameter(Mandatory)][string]$ExpectedHost,
  [string]$SecretPath = ""
)

$ErrorActionPreference = "Stop"
$approvedHost = "idp.gxu.edu.cn"
if ($ExpectedHost.Trim().ToLowerInvariant() -ne $approvedHost) {
  throw "Credential release denied for unapproved host."
}

. (Join-Path $PSScriptRoot "secret-store.ps1")
if ([string]::IsNullOrWhiteSpace($SecretPath)) { $SecretPath = Get-RetrievalSecretPath }

$password = $null
try {
  $payload = Import-RetrievalSecrets -Path $SecretPath
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
