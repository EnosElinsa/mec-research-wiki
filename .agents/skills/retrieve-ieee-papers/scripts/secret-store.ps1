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

function Get-RetrievalProfileValue([object]$Profile, [string]$Name) {
  if ($null -eq $Profile) { return "" }
  if ($Profile -is [Collections.IDictionary]) { return [string]$Profile[$Name] }
  $property = $Profile.PSObject.Properties[$Name]
  if ($null -eq $property) { return "" }
  return [string]$property.Value
}

function ConvertFrom-RetrievalUtf8Base64([string]$Value) {
  return [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($Value))
}

function Get-LegacyGxuInstitutionProfile {
  return [pscustomobject]@{
    Organization = "Guangxi University"
    CarsiSchoolPlaceholder = (ConvertFrom-RetrievalUtf8Base64 "6K+36L6T5YWl6auY5qChL+acuuaehOWQjeensA==")
    CarsiSearchText = (ConvertFrom-RetrievalUtf8Base64 "5bm/6KW/5aSn5a2m")
    CarsiInstitution = (ConvertFrom-RetrievalUtf8Base64 "5bm/6KW/5aSn5a2m77yIR3VhbmdYaSBVbml2ZXJzaXR577yJ")
    CarsiLoginButtonName = (ConvertFrom-RetrievalUtf8Base64 "55m75b2V")
    CarsiEntityId = "https://idp.gxu.edu.cn/idp/shibboleth"
    CredentialHost = "idp.gxu.edu.cn"
    UsernameLabel = (ConvertFrom-RetrievalUtf8Base64 "55So5oi35ZCN")
    PasswordLabel = (ConvertFrom-RetrievalUtf8Base64 "5a+G56CB")
    LoginButtonName = (ConvertFrom-RetrievalUtf8Base64 "55m75b2V")
    ResourceAccessUrl = "https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:6"
    AttributeReleaseTitle = ""
    AttributeReleaseAcceptControlName = "_eventId_proceed"
    AttributeReleaseRejectControlName = "_eventId_AttributeReleaseRejected"
  }
}

function ConvertTo-RetrievalInstitutionProfile([object]$InstitutionProfile) {
  $required = @(
    "Organization",
    "CarsiSchoolPlaceholder",
    "CarsiSearchText",
    "CarsiInstitution",
    "CarsiLoginButtonName",
    "CredentialHost",
    "UsernameLabel",
    "PasswordLabel",
    "LoginButtonName",
    "ResourceAccessUrl"
  )
  $values = @{}
  foreach ($name in $required) {
    $value = (Get-RetrievalProfileValue -Profile $InstitutionProfile -Name $name).Trim()
    if ([string]::IsNullOrWhiteSpace($value)) {
      throw "IEEE institution profile field is missing: $name"
    }
    $values[$name] = $value
  }

  $credentialHost = $values.CredentialHost
  if (-not $credentialHost.Contains(".") -or $credentialHost.EndsWith(".") -or
      $credentialHost.Contains(":") -or $credentialHost.Contains("/") -or
      $credentialHost.Contains("*") -or
      [Uri]::CheckHostName($credentialHost) -ne [UriHostNameType]::Dns) {
    throw "IEEE credential host must be one exact DNS hostname without scheme, port, path, wildcard, or trailing dot."
  }
  $values.CredentialHost = $credentialHost.ToLowerInvariant()

  $carsiEntityId = (Get-RetrievalProfileValue -Profile $InstitutionProfile -Name "CarsiEntityId").Trim()
  if ([string]::IsNullOrWhiteSpace($carsiEntityId) -and $values.CredentialHost -eq "idp.gxu.edu.cn") {
    $carsiEntityId = "https://idp.gxu.edu.cn/idp/shibboleth"
  }
  $entityUri = $null
  if (-not [Uri]::TryCreate($carsiEntityId, [UriKind]::Absolute, [ref]$entityUri) -or
      $entityUri.Scheme -ne "https" -or
      -not $entityUri.IsDefaultPort -or
      -not [string]::IsNullOrWhiteSpace($entityUri.UserInfo) -or
      -not [string]::IsNullOrWhiteSpace($entityUri.Fragment)) {
    throw "CARSI entity ID must be an HTTPS URL without credentials, a custom port, or a fragment."
  }

  $resourceUri = $null
  if (-not [Uri]::TryCreate($values.ResourceAccessUrl, [UriKind]::Absolute, [ref]$resourceUri) -or
      $resourceUri.Scheme -ne "https" -or
      $resourceUri.DnsSafeHost -ne "ds.carsi.edu.cn" -or
      -not $resourceUri.IsDefaultPort -or
      -not [string]::IsNullOrWhiteSpace($resourceUri.UserInfo) -or
      -not [string]::IsNullOrWhiteSpace($resourceUri.Fragment)) {
    throw "IEEE resource access URL must use the exact ds.carsi.edu.cn HTTPS host without credentials, a custom port, or a fragment."
  }

  $attributeReleaseTitle = (
    Get-RetrievalProfileValue -Profile $InstitutionProfile -Name "AttributeReleaseTitle"
  ).Trim()
  $attributeReleaseAccept = (
    Get-RetrievalProfileValue -Profile $InstitutionProfile -Name "AttributeReleaseAcceptControlName"
  ).Trim()
  $attributeReleaseReject = (
    Get-RetrievalProfileValue -Profile $InstitutionProfile -Name "AttributeReleaseRejectControlName"
  ).Trim()
  if ([string]::IsNullOrWhiteSpace($attributeReleaseAccept) -and
      -not [string]::IsNullOrWhiteSpace($attributeReleaseReject)) {
    throw "An attribute-release reject control requires an accept or continue control."
  }
  foreach ($controlName in @($attributeReleaseAccept, $attributeReleaseReject)) {
    if (-not [string]::IsNullOrWhiteSpace($controlName) -and $controlName -notmatch '^[A-Za-z0-9_-]+$') {
      throw "IEEE attribute-release control names may contain only letters, digits, underscores, and hyphens."
    }
  }

  return [pscustomobject]@{
    Organization = $values.Organization
    CarsiSchoolPlaceholder = $values.CarsiSchoolPlaceholder
    CarsiSearchText = $values.CarsiSearchText
    CarsiInstitution = $values.CarsiInstitution
    CarsiLoginButtonName = $values.CarsiLoginButtonName
    CarsiEntityId = $entityUri.AbsoluteUri
    CredentialHost = $values.CredentialHost
    UsernameLabel = $values.UsernameLabel
    PasswordLabel = $values.PasswordLabel
    LoginButtonName = $values.LoginButtonName
    ResourceAccessUrl = $resourceUri.AbsoluteUri
    AttributeReleaseTitle = $attributeReleaseTitle
    AttributeReleaseAcceptControlName = $attributeReleaseAccept
    AttributeReleaseRejectControlName = $attributeReleaseReject
  }
}

function Export-RetrievalSecrets(
  [object]$InstitutionProfile = (Get-LegacyGxuInstitutionProfile),
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
  $profile = ConvertTo-RetrievalInstitutionProfile -InstitutionProfile $InstitutionProfile

  $parent = Split-Path -Parent $Path
  if ([string]::IsNullOrWhiteSpace($parent)) { throw "Secret path must include a parent directory." }
  if (-not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
  }

  $payload = [pscustomobject]@{
    SchemaVersion = 2
    InstitutionProfile = $profile
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
  if ($null -eq $payload -or [int]$payload.SchemaVersion -notin @(1, 2)) {
    throw "Unsupported retrieval secret schema."
  }
  if ($payload.IeeeCredential -isnot [Management.Automation.PSCredential]) {
    throw "IEEE credential is missing or invalid."
  }
  if ($payload.MinerUToken -isnot [Security.SecureString] -or $payload.MinerUToken.Length -eq 0) {
    throw "MinerU token is missing or invalid."
  }
  if ([int]$payload.SchemaVersion -eq 1) {
    if ($payload.Organization -ne "Guangxi University") {
      throw "Unexpected organization in legacy retrieval secret file."
    }
    return [pscustomobject]@{
      SchemaVersion = 2
      InstitutionProfile = ConvertTo-RetrievalInstitutionProfile (Get-LegacyGxuInstitutionProfile)
      IeeeCredential = $payload.IeeeCredential
      MinerUToken = $payload.MinerUToken
    }
  }
  return [pscustomobject]@{
    SchemaVersion = 2
    InstitutionProfile = ConvertTo-RetrievalInstitutionProfile $payload.InstitutionProfile
    IeeeCredential = $payload.IeeeCredential
    MinerUToken = $payload.MinerUToken
  }
}
