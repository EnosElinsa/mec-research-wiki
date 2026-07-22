$ErrorActionPreference = "Stop"

function Assert-True([bool]$Condition, [string]$Message) {
  if (-not $Condition) { throw "ASSERT TRUE FAILED: $Message" }
}

function Assert-Equal($Actual, $Expected, [string]$Message) {
  if ($Actual -ne $Expected) {
    throw "ASSERT EQUAL FAILED: $Message expected=[$Expected] actual=[$Actual]"
  }
}

function Assert-Throws([scriptblock]$Action, [string]$Message) {
  $threw = $false
  try { & $Action } catch { $threw = $true }
  if (-not $threw) { throw "ASSERT THROWS FAILED: $Message" }
}

function Invoke-CapturedPowerShell([string]$ScriptPath, [string[]]$Arguments) {
  function ConvertTo-NativeArgument([string]$Value) {
    if ($Value -notmatch '[\s"]') { return $Value }
    $escaped = [regex]::Replace($Value, '(\\*)"', '$1$1\"')
    $escaped = [regex]::Replace($escaped, '(\\+)$', '$1$1')
    return '"' + $escaped + '"'
  }

  $startInfo = [Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = "powershell"
  $startInfo.UseShellExecute = $false
  $startInfo.CreateNoWindow = $true
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $nativeArguments = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $ScriptPath) + $Arguments
  $startInfo.Arguments = (($nativeArguments | ForEach-Object { ConvertTo-NativeArgument $_ }) -join " ")

  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  [void]$process.Start()
  $stdout = $process.StandardOutput.ReadToEnd()
  $stderr = $process.StandardError.ReadToEnd()
  $process.WaitForExit()
  return [pscustomobject]@{
    ExitCode = $process.ExitCode
    Stdout = $stdout
    Stderr = $stderr
  }
}

$scriptsRoot = Split-Path -Parent $PSScriptRoot
$secretStorePath = Join-Path $scriptsRoot "secret-store.ps1"
$bridgePath = Join-Path $scriptsRoot "read-browser-credential.ps1"
$profileBridgePath = Join-Path $scriptsRoot "read-institution-profile.ps1"
$installPath = Join-Path $scriptsRoot "install-secret-file.ps1"
if (-not (Test-Path -LiteralPath $secretStorePath)) {
  throw "Expected implementation file is missing: $secretStorePath"
}
if (-not (Test-Path -LiteralPath $bridgePath)) {
  throw "Expected implementation file is missing: $bridgePath"
}
if (-not (Test-Path -LiteralPath $profileBridgePath)) {
  throw "Expected implementation file is missing: $profileBridgePath"
}
if (-not (Test-Path -LiteralPath $installPath)) {
  throw "Expected implementation file is missing: $installPath"
}

. $secretStorePath

$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("retrieve-ieee-secret-test-" + [guid]::NewGuid().ToString("N"))
$localAppData = Join-Path $tempRoot "LocalAppData"
$secretPath = Join-Path $localAppData "Codex\secrets\retrieve-ieee-papers.clixml"

try {
  New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
  $password = ConvertTo-SecureString "synthetic-password" -AsPlainText -Force
  $token = ConvertTo-SecureString "synthetic-token" -AsPlainText -Force
  $credential = [Management.Automation.PSCredential]::new("synthetic-user", $password)
  $institution = [pscustomobject]@{
    Organization = "Example University"
    CarsiSchoolPlaceholder = "Institution name"
    CarsiSearchText = "Example University"
    CarsiInstitution = "Example University (Example)"
    CarsiLoginButtonName = "Continue"
    CarsiEntityId = "https://login.example.edu/idp/shibboleth"
    CredentialHost = "login.example.edu"
    UsernameLabel = "Account"
    PasswordLabel = "Passcode"
    LoginButtonName = "Sign in"
    ResourceAccessUrl = "https://ds.carsi.edu.cn/resource/gotoResource.php?id=resource:example-ieee"
    AttributeReleaseTitle = ""
    AttributeReleaseAcceptControlName = ""
    AttributeReleaseRejectControlName = ""
  }

  Assert-Equal (Get-RetrievalSecretPath $localAppData) $secretPath "default path"
  Export-RetrievalSecrets -InstitutionProfile $institution -IeeeCredential $credential -MinerUToken $token -Path $secretPath
  Assert-True (Test-Path -LiteralPath $secretPath) "secret file should exist"
  Assert-True (-not (Get-Acl -LiteralPath $secretPath).AreAccessRulesProtected) "trusted parent ACL inheritance must remain enabled for the Codex sandbox"

  $serialized = Get-Content -Raw -LiteralPath $secretPath
  Assert-True (-not $serialized.Contains("synthetic-password")) "password must be encrypted"
  Assert-True (-not $serialized.Contains("synthetic-token")) "token must be encrypted"

  $payload = Import-RetrievalSecrets -Path $secretPath
  Assert-Equal $payload.SchemaVersion 2 "schema version"
  Assert-Equal $payload.InstitutionProfile.Organization "Example University" "organization"
  Assert-Equal $payload.InstitutionProfile.CarsiEntityId $institution.CarsiEntityId "CARSI entity ID"
  Assert-Equal $payload.InstitutionProfile.CredentialHost "login.example.edu" "credential host"
  Assert-Equal $payload.IeeeCredential.UserName "synthetic-user" "username"
  Assert-Equal (ConvertFrom-RetrievalSecureString $payload.MinerUToken) "synthetic-token" "token round trip"

  $invalidPath = Join-Path $tempRoot "invalid.clixml"
  [pscustomobject]@{ SchemaVersion = 3 } | Export-Clixml -LiteralPath $invalidPath
  Assert-Throws { Import-RetrievalSecrets -Path $invalidPath } "schema mismatch must fail"
  Assert-Throws { Import-RetrievalSecrets -Path (Join-Path $tempRoot "missing.clixml") } "missing file must fail"

  $rejected = Invoke-CapturedPowerShell $bridgePath @("-ExpectedHost", "login.example.edu.evil.example", "-SecretPath", $secretPath)
  Assert-True ($rejected.ExitCode -ne 0) "unapproved host must fail"
  Assert-Equal $rejected.Stdout "" "unapproved host must not emit stdout"

  $approved = Invoke-CapturedPowerShell $bridgePath @("-ExpectedHost", "login.example.edu", "-SecretPath", $secretPath)
  Assert-Equal $approved.ExitCode 0 "approved host should succeed"
  $json = $approved.Stdout | ConvertFrom-Json
  Assert-Equal $json.username "synthetic-user" "bridge username"
  Assert-Equal $json.password "synthetic-password" "bridge password"

  $profileResult = Invoke-CapturedPowerShell $profileBridgePath @("-SecretPath", $secretPath)
  Assert-Equal $profileResult.ExitCode 0 "profile bridge should succeed"
  $profileJson = $profileResult.Stdout | ConvertFrom-Json
  Assert-Equal $profileJson.organization "Example University" "profile bridge organization"
  Assert-Equal $profileJson.carsiEntityId $institution.CarsiEntityId "profile bridge CARSI entity ID"
  Assert-Equal $profileJson.resourceAccessUrl $institution.ResourceAccessUrl "profile bridge resource route"

  $legacyPath = Join-Path $tempRoot "legacy-v1.clixml"
  [pscustomobject]@{
    SchemaVersion = 1
    Organization = "Guangxi University"
    IeeeCredential = $credential
    MinerUToken = $token
  } | Export-Clixml -LiteralPath $legacyPath
  $legacy = Import-RetrievalSecrets -Path $legacyPath
  Assert-Equal $legacy.SchemaVersion 2 "legacy schema should normalize in memory"
  Assert-Equal $legacy.InstitutionProfile.CarsiEntityId "https://idp.gxu.edu.cn/idp/shibboleth" "legacy Guangxi CARSI entity ID"
  Assert-Equal $legacy.InstitutionProfile.CredentialHost "idp.gxu.edu.cn" "legacy Guangxi host"

  $repoRoot = Join-Path $tempRoot "repo"
  $provisioningRoot = Join-Path $repoRoot "raw\tmp\.work"
  New-Item -ItemType Directory -Path $provisioningRoot -Force | Out-Null
  $provisioningPath = Join-Path $provisioningRoot "provision.clixml"
  Export-RetrievalSecrets -IeeeCredential $credential -MinerUToken $token -Path $provisioningPath
  $installedPath = Join-Path $tempRoot "installed\retrieve-ieee-papers.clixml"
  $installResult = & $installPath -SourcePath $provisioningPath -DestinationPath $installedPath -RepoRoot $repoRoot -Force -TestMode | ConvertFrom-Json
  Assert-Equal $installResult.status "installed" "encrypted payload install status"
  Assert-True (Test-Path -LiteralPath $installedPath -PathType Leaf) "installed encrypted payload"
  Assert-True (-not (Test-Path -LiteralPath $provisioningPath)) "temporary encrypted payload must be removed"
  Assert-Equal (Import-RetrievalSecrets -Path $installedPath).SchemaVersion 2 "installed payload remains decryptable"

  $outsidePath = Join-Path $tempRoot "outside.clixml"
  Export-RetrievalSecrets -IeeeCredential $credential -MinerUToken $token -Path $outsidePath
  Assert-Throws {
    & $installPath -SourcePath $outsidePath -DestinationPath (Join-Path $tempRoot "rejected.clixml") -RepoRoot $repoRoot -Force -TestMode | Out-Null
  } "installer source must remain under raw/tmp/.work"

  $repoDestinationSource = Join-Path $provisioningRoot "repo-destination.clixml"
  Export-RetrievalSecrets -IeeeCredential $credential -MinerUToken $token -Path $repoDestinationSource
  Assert-Throws {
    & $installPath -SourcePath $repoDestinationSource `
      -DestinationPath (Join-Path $repoRoot "raw\tmp\credential.clixml") `
      -RepoRoot $repoRoot `
      -Force | Out-Null
  } "production installer must reject a credential destination inside the repository"
  Assert-True (Test-Path -LiteralPath $repoDestinationSource -PathType Leaf) "rejected install must preserve its source payload"

  Write-Output "PASS DPAPI secret storage"
  Write-Output "PASS exact-host credential gate"
  Write-Output "PASS encrypted-payload installation boundary"
}
finally {
  if (Test-Path -LiteralPath $tempRoot) {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
  }
}
