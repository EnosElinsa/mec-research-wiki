param(
  [string]$InputRoot = "C:\Users\labs2\Desktop\Papers\TMC_TWC_TITS_TGCN_TPDS",
  [string]$OutputRoot = "C:\Users\labs2\Desktop\Projects\mec-research-wiki\raw\sources",
  [string]$ManifestPath = "C:\Users\labs2\Desktop\Projects\mec-research-wiki\.curation-out\mineru-conversion-manifest.csv",
  [string]$NonMecRoot = "C:\Users\labs2\Desktop\Projects\mec-research-wiki\.curation-out\mineru-non-mec",
  [int]$Limit = 0,
  [string]$StartAfter = "",
  [string]$Model = "pipeline",
  [string]$Language = "en",
  [int]$TimeoutSeconds = 1800
)

$ErrorActionPreference = "Stop"
. "$PSScriptRoot\mec_relevance.ps1"

function Normalize-Title([string]$Text) {
  $name = [IO.Path]::GetFileNameWithoutExtension($Text)
  $name = $name -replace "^[0-9]{1,4}[_\-\s]+", ""
  return (($name.ToLowerInvariant()) -replace "[^a-z0-9]+", "")
}

function Get-SourceTitle([string]$FileName) {
  return (([IO.Path]::GetFileNameWithoutExtension($FileName)) -replace "^[0-9]{1,4}[_\-\s]+", "").Trim()
}

function Get-SafeName([string]$Title) {
  $safe = $Title.Trim()
  $safe = $safe -replace '[<>:"/\\|?*]', "-"
  $safe = $safe -replace "\s+", " "
  $safe = $safe.Trim(" .")
  if ($safe.Length -gt 180) {
    $safe = $safe.Substring(0, 180).Trim(" .")
  }
  if ([string]::IsNullOrWhiteSpace($safe)) {
    throw "Cannot derive a safe output name from title: $Title"
  }
  return $safe
}

function Test-RateLimit([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return $false }
  return $Text -match "(?i)(\b429\b|rate\s*limit|too many requests|限流|请求过多|quota|qps|throttle)"
}

function Ensure-Directory([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Path $Path | Out-Null
  }
}

function Get-ExistingKeys([string]$Root) {
  $keys = @{}
  if (Test-Path -LiteralPath $Root) {
    Get-ChildItem -LiteralPath $Root -Directory | ForEach-Object {
      $key = Normalize-Title $_.Name
      if (-not $keys.ContainsKey($key)) { $keys[$key] = @() }
      $keys[$key] += $_.FullName
    }
  }
  return $keys
}

function Read-Manifest([string]$Path) {
  if (Test-Path -LiteralPath $Path) {
    return @(Import-Csv -LiteralPath $Path)
  }
  return @()
}

function Append-ManifestRow([string]$Path, [object]$Row) {
  $dir = Split-Path -Parent $Path
  Ensure-Directory $dir
  $exists = Test-Path -LiteralPath $Path
  $Row | Export-Csv -LiteralPath $Path -Append -NoTypeInformation -Encoding UTF8
}

function Resolve-OutputDirectory([string]$OutputRoot, [string]$SafeTitle, [string]$Group, [string]$Key) {
  $target = Join-Path $OutputRoot $SafeTitle
  if (-not (Test-Path -LiteralPath $target)) {
    return $target
  }

  $targetKey = Normalize-Title (Split-Path -Leaf $target)
  if ($targetKey -eq $Key) {
    return $target
  }

  $fallback = Join-Path $OutputRoot "$SafeTitle [$Group]"
  if (-not (Test-Path -LiteralPath $fallback)) {
    return $fallback
  }

  $i = 2
  while ($true) {
    $candidate = Join-Path $OutputRoot "$SafeTitle [$Group-$i]"
    if (-not (Test-Path -LiteralPath $candidate)) {
      return $candidate
    }
    $i++
  }
}

function Move-NonMecOutput([string]$OutputDir, [string]$NonMecRoot) {
  if ([string]::IsNullOrWhiteSpace($OutputDir) -or -not (Test-Path -LiteralPath $OutputDir)) {
    return ""
  }

  Ensure-Directory $NonMecRoot
  $leaf = Split-Path -Leaf $OutputDir
  $destination = Join-Path $NonMecRoot $leaf
  if (Test-Path -LiteralPath $destination) {
    $destination = Join-Path $NonMecRoot "$leaf-$((Get-Date).ToString('yyyyMMddHHmmss'))"
  }
  Move-Item -LiteralPath $OutputDir -Destination $destination
  return $destination
}

function Find-MineruMarkdown([string]$TempDir) {
  $markdowns = @(Get-ChildItem -LiteralPath $TempDir -Recurse -File -Filter *.md)
  if ($markdowns.Count -eq 0) { return $null }
  return $markdowns | Sort-Object Length -Descending | Select-Object -First 1
}

function Move-MineruOutput([string]$TempDir, [string]$TargetDir, [string]$TargetTitle) {
  Ensure-Directory $TargetDir
  $md = Find-MineruMarkdown $TempDir
  if ($null -eq $md) {
    throw "MinerU completed but no Markdown file was found under $TempDir"
  }

  $mdParent = $md.Directory.FullName
  Get-ChildItem -LiteralPath $mdParent -Force |
    Where-Object { $_.Name -notin @("mineru.stdout.log", "mineru.stderr.log") } |
    ForEach-Object {
    $destination = Join-Path $TargetDir $_.Name
    if (Test-Path -LiteralPath $destination) {
      Remove-Item -LiteralPath $destination -Recurse -Force
    }
    Move-Item -LiteralPath $_.FullName -Destination $destination
  }

  $currentMd = Join-Path $TargetDir $md.Name
  $targetMd = Join-Path $TargetDir "$TargetTitle.md"
  if ((Test-Path -LiteralPath $currentMd) -and ($currentMd -ne $targetMd)) {
    if (Test-Path -LiteralPath $targetMd) {
      Remove-Item -LiteralPath $targetMd -Force
    }
    Move-Item -LiteralPath $currentMd -Destination $targetMd
  }

  $assetDirs = @("images", "tables", "figures")
  foreach ($assetDir in $assetDirs) {
    $candidate = Join-Path $TargetDir $assetDir
    if (Test-Path -LiteralPath $candidate) {
      continue
    }
  }

  return $targetMd
}

if (-not (Get-Command mineru-open-api -ErrorAction SilentlyContinue)) {
  throw "mineru-open-api was not found in PATH. Install with: npm install -g mineru-open-api"
}

$mineruCommand = Get-Command mineru-open-api -ErrorAction Stop
$mineruScript = Join-Path (Split-Path -Parent $mineruCommand.Source) "node_modules\mineru-open-api\bin\mineru-open-api"
if (-not (Test-Path -LiteralPath $mineruScript)) {
  throw "Cannot locate mineru-open-api node script at $mineruScript"
}

function Quote-ProcessArgument([string]$Argument) {
  if ($null -eq $Argument) { return '""' }
  return '"' + ($Argument -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"'
}

function Invoke-Mineru([string[]]$Arguments, [string]$StdoutLog, [string]$StderrLog) {
  $startInfo = [System.Diagnostics.ProcessStartInfo]::new()
  $startInfo.FileName = "node"
  $startInfo.UseShellExecute = $false
  $startInfo.RedirectStandardOutput = $true
  $startInfo.RedirectStandardError = $true
  $startInfo.CreateNoWindow = $true
  $allArguments = @($mineruScript) + $Arguments
  $startInfo.Arguments = (($allArguments | ForEach-Object { Quote-ProcessArgument $_ }) -join " ")

  $process = [System.Diagnostics.Process]::new()
  $process.StartInfo = $startInfo
  [void]$process.Start()
  $stdout = $process.StandardOutput.ReadToEnd()
  $stderr = $process.StandardError.ReadToEnd()
  $process.WaitForExit()
  Set-Content -LiteralPath $StdoutLog -Value $stdout -Encoding UTF8
  Set-Content -LiteralPath $StderrLog -Value $stderr -Encoding UTF8
  return $process.ExitCode
}

if ([string]::IsNullOrWhiteSpace($env:MINERU_TOKEN)) {
  $userToken = [Environment]::GetEnvironmentVariable("MINERU_TOKEN", "User")
  if (-not [string]::IsNullOrWhiteSpace($userToken)) {
    $env:MINERU_TOKEN = $userToken
  }
}

if ([string]::IsNullOrWhiteSpace($env:MINERU_TOKEN)) {
  throw "MINERU_TOKEN is not set. Set it in the environment before running this script."
}

Ensure-Directory $OutputRoot
Ensure-Directory (Split-Path -Parent $ManifestPath)
Ensure-Directory $NonMecRoot

$existingKeys = Get-ExistingKeys $OutputRoot
$manifest = Read-Manifest $ManifestPath
$completed = @{}
$lastStatusBySource = @{}
foreach ($row in $manifest) {
  if ([string]::IsNullOrWhiteSpace($row.SourcePath)) {
    continue
  }

  $lastStatusBySource[$row.SourcePath] = $row.Status
  if ($row.Status -in @("success", "skipped-existing")) {
    $completed[$row.SourcePath] = $true
  }
}

$pdfs = @(Get-ChildItem -LiteralPath $InputRoot -Recurse -File -Filter *.pdf | Sort-Object FullName)
$bibEntriesByDirectory = @{}
$started = [string]::IsNullOrWhiteSpace($StartAfter)
$processed = 0

foreach ($pdf in $pdfs) {
  if (-not $started) {
    if ($pdf.FullName -eq $StartAfter -or $pdf.Name -eq $StartAfter) {
      $started = $true
    }
    continue
  }

  if ($Limit -gt 0 -and $processed -ge $Limit) {
    Write-Host "Reached limit $Limit. Stopping."
    break
  }

  if ($completed.ContainsKey($pdf.FullName)) {
    Write-Host "SKIP manifest-completed: $($pdf.FullName)"
    continue
  }

  $group = Split-Path $pdf.DirectoryName -Leaf
  $title = Get-SourceTitle $pdf.Name
  $safeTitle = Get-SafeName $title
  $key = Normalize-Title $pdf.Name
  if (-not $bibEntriesByDirectory.ContainsKey($pdf.DirectoryName)) {
    $bibEntriesByDirectory[$pdf.DirectoryName] = Get-BibEntriesByNumber $pdf.DirectoryName
  }
  $isMecRelevant = Test-PdfMecRelevant $pdf $bibEntriesByDirectory[$pdf.DirectoryName]

  if ($existingKeys.ContainsKey($key)) {
    $target = $existingKeys[$key] | Select-Object -First 1
    if (-not $isMecRelevant) {
      $movedTo = Move-NonMecOutput $target $NonMecRoot
      Write-Host "MOVE non-MEC existing: $title"
      Append-ManifestRow $ManifestPath ([pscustomobject]@{
        Timestamp = (Get-Date).ToString("s")
        Status = "skipped-not-mec"
        Group = $group
        Title = $title
        SourcePath = $pdf.FullName
        OutputDir = $movedTo
        Message = "Existing output moved out of raw/sources because it is not MEC-related"
      })
      $completed[$pdf.FullName] = $true
      $existingKeys.Remove($key)
      continue
    }

    Write-Host "SKIP existing: $title"
    Append-ManifestRow $ManifestPath ([pscustomobject]@{
      Timestamp = (Get-Date).ToString("s")
      Status = "skipped-existing"
      Group = $group
      Title = $title
      SourcePath = $pdf.FullName
      OutputDir = $target
      Message = "Existing normalized source directory found"
    })
    $completed[$pdf.FullName] = $true
    continue
  }

  $targetDir = Resolve-OutputDirectory $OutputRoot $safeTitle $group $key
  $targetMd = Join-Path $targetDir "$safeTitle.md"
  if (-not $isMecRelevant) {
    if ($lastStatusBySource.ContainsKey($pdf.FullName) -and $lastStatusBySource[$pdf.FullName] -eq "skipped-not-mec") {
      Write-Host "SKIP non-MEC recorded: $group / $title"
      $completed[$pdf.FullName] = $true
      continue
    }

    Write-Host "SKIP non-MEC: $group / $title"
    Append-ManifestRow $ManifestPath ([pscustomobject]@{
      Timestamp = (Get-Date).ToString("s")
      Status = "skipped-not-mec"
      Group = $group
      Title = $title
      SourcePath = $pdf.FullName
      OutputDir = ""
      Message = "No MEC/edge computing/offloading signal in filename or BibTeX metadata"
    })
    $completed[$pdf.FullName] = $true
    $lastStatusBySource[$pdf.FullName] = "skipped-not-mec"
    continue
  }

  if ((Test-Path -LiteralPath $targetMd) -and ((Get-Item -LiteralPath $targetMd).Length -gt 0)) {
    Write-Host "SKIP target-md-present: $title"
    Append-ManifestRow $ManifestPath ([pscustomobject]@{
      Timestamp = (Get-Date).ToString("s")
      Status = "skipped-existing"
      Group = $group
      Title = $title
      SourcePath = $pdf.FullName
      OutputDir = $targetDir
      Message = "Target Markdown already present"
    })
    $existingKeys[$key] = @($targetDir)
    $completed[$pdf.FullName] = $true
    continue
  }

  $processed++
  $tempDir = Join-Path ([IO.Path]::GetTempPath()) ("mineru-" + [guid]::NewGuid().ToString("N"))
  Ensure-Directory $tempDir
  Write-Host "EXTRACT [$processed]: $group / $title"

  $combinedOutput = ""
  try {
    $args = @(
      "extract",
      $pdf.FullName,
      "-o",
      $tempDir,
      "-f",
      "md",
      "--model",
      $Model,
      "--language",
      $Language,
      "--timeout",
      "$TimeoutSeconds"
    )

    $stdoutLog = Join-Path $tempDir "mineru.stdout.log"
    $stderrLog = Join-Path $tempDir "mineru.stderr.log"
    $exitCode = Invoke-Mineru $args $stdoutLog $stderrLog
    $stdoutText = if (Test-Path -LiteralPath $stdoutLog) { Get-Content -LiteralPath $stdoutLog -Raw } else { "" }
    $stderrText = if (Test-Path -LiteralPath $stderrLog) { Get-Content -LiteralPath $stderrLog -Raw } else { "" }
    $combinedOutput = "$stdoutText`n$stderrText"

    if ($exitCode -ne 0) {
      if (Test-RateLimit $combinedOutput) {
        Append-ManifestRow $ManifestPath ([pscustomobject]@{
          Timestamp = (Get-Date).ToString("s")
          Status = "rate-limited"
          Group = $group
          Title = $title
          SourcePath = $pdf.FullName
          OutputDir = $targetDir
          Message = ($combinedOutput.Trim() -replace "\s+", " ")
        })
        Write-Host "RATE LIMITED. Stopping at: $($pdf.FullName)"
        exit 75
      }
      throw "mineru-open-api failed with exit code $exitCode. $combinedOutput"
    }

    if (Test-RateLimit $combinedOutput) {
      Append-ManifestRow $ManifestPath ([pscustomobject]@{
        Timestamp = (Get-Date).ToString("s")
        Status = "rate-limited"
        Group = $group
        Title = $title
        SourcePath = $pdf.FullName
        OutputDir = $targetDir
        Message = ($combinedOutput.Trim() -replace "\s+", " ")
      })
      Write-Host "RATE LIMITED. Stopping at: $($pdf.FullName)"
      exit 75
    }

    $writtenMd = Move-MineruOutput $tempDir $targetDir $safeTitle
    $targetPdf = Join-Path $targetDir "$safeTitle.pdf"
    Copy-Item -LiteralPath $pdf.FullName -Destination $targetPdf -Force

    $existingKeys[$key] = @($targetDir)
    $completed[$pdf.FullName] = $true
    Append-ManifestRow $ManifestPath ([pscustomobject]@{
      Timestamp = (Get-Date).ToString("s")
      Status = "success"
      Group = $group
      Title = $title
      SourcePath = $pdf.FullName
      OutputDir = $targetDir
      Message = "Markdown: $writtenMd"
    })
  }
  catch {
    $message = $_.Exception.Message
    if (Test-RateLimit ($message + "`n" + $combinedOutput)) {
      Append-ManifestRow $ManifestPath ([pscustomobject]@{
        Timestamp = (Get-Date).ToString("s")
        Status = "rate-limited"
        Group = $group
        Title = $title
        SourcePath = $pdf.FullName
        OutputDir = $targetDir
        Message = (($message + " " + $combinedOutput).Trim() -replace "\s+", " ")
      })
      Write-Host "RATE LIMITED. Stopping at: $($pdf.FullName)"
      exit 75
    }

    Append-ManifestRow $ManifestPath ([pscustomobject]@{
      Timestamp = (Get-Date).ToString("s")
      Status = "failed"
      Group = $group
      Title = $title
      SourcePath = $pdf.FullName
      OutputDir = $targetDir
      Message = ($message -replace "\s+", " ")
    })
    Write-Host "FAILED: $($pdf.FullName)"
    Write-Host $message
  }
  finally {
    if (Test-Path -LiteralPath $tempDir) {
      Remove-Item -LiteralPath $tempDir -Recurse -Force
    }
  }
}

Write-Host "Done. Manifest: $ManifestPath"
