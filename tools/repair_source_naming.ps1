param(
  [string]$InputRoot = "C:\Users\labs2\Desktop\Papers\TMC_TWC_TITS_TGCN_TPDS",
  [string]$OutputRoot = "C:\Users\labs2\Desktop\Projects\mec-research-wiki\raw\sources",
  [string]$ArchiveRoot = "C:\Users\labs2\Desktop\Projects\mec-research-wiki\.curation-out\naming-duplicates"
)

$ErrorActionPreference = "Stop"
. "$PSScriptRoot\source_naming.ps1"

function Ensure-Directory([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Path $Path | Out-Null
  }
}

function Assert-UnderRoot([string]$Path, [string]$Root) {
  $resolvedRoot = (Resolve-Path -LiteralPath $Root).Path.TrimEnd('\')
  $resolvedPath = if (Test-Path -LiteralPath $Path) {
    (Resolve-Path -LiteralPath $Path).Path
  } else {
    $parent = Split-Path -Parent $Path
    $leaf = Split-Path -Leaf $Path
    (Join-Path (Resolve-Path -LiteralPath $parent).Path $leaf)
  }

  if (-not $resolvedPath.StartsWith($resolvedRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Path is outside expected root. Path=$resolvedPath Root=$resolvedRoot"
  }
}

function Move-ToArchive([string]$Path, [string]$ReasonName) {
  Ensure-Directory $ArchiveRoot
  $hashInput = "$ReasonName|$Path|$([guid]::NewGuid().ToString('N'))"
  $bytes = [Text.Encoding]::UTF8.GetBytes($hashInput)
  $md5 = [Security.Cryptography.MD5]::Create()
  $hash = ([BitConverter]::ToString($md5.ComputeHash($bytes))).Replace("-", "").ToLowerInvariant().Substring(0, 12)
  $stamp = Get-Date -Format "yyyyMMddHHmmss"
  $extension = if (Test-Path -LiteralPath $Path -PathType Leaf) { [IO.Path]::GetExtension((Split-Path -Leaf $Path)) } else { "" }
  $destination = Join-Path $ArchiveRoot "$stamp-$hash$extension"
  Move-Item -LiteralPath $Path -Destination $destination
  return $destination
}

function Rename-PrimaryFile([string]$Directory, [string]$TargetBaseName, [string]$Extension) {
  $target = Join-Path $Directory "$TargetBaseName$Extension"
  $files = @(Get-ChildItem -LiteralPath $Directory -File -Filter "*$Extension")
  if ($files.Count -eq 0) { return }

  $targetItem = $files | Where-Object { $_.FullName -eq $target } | Select-Object -First 1
  if ($null -eq $targetItem) {
    $source = $files | Sort-Object Length -Descending | Select-Object -First 1
    Move-Item -LiteralPath $source.FullName -Destination $target
    $files = @(Get-ChildItem -LiteralPath $Directory -File -Filter "*$Extension")
  }

  foreach ($extra in @($files | Where-Object { $_.FullName -ne $target })) {
    $archiveDir = Join-Path $ArchiveRoot $TargetBaseName
    Ensure-Directory $archiveDir
    $archivePath = Join-Path $archiveDir $extra.Name
    if (Test-Path -LiteralPath $archivePath) {
      $archivePath = Join-Path $archiveDir "$([IO.Path]::GetFileNameWithoutExtension($extra.Name))-$((Get-Date).ToString('yyyyMMddHHmmss'))$Extension"
    }
    Move-Item -LiteralPath $extra.FullName -Destination $archivePath
  }
}

function Repair-DirectoryFiles([string]$Directory, [string]$TargetBaseName) {
  Rename-PrimaryFile $Directory $TargetBaseName ".md"
  Rename-PrimaryFile $Directory $TargetBaseName ".pdf"
}

$resolvedOutputRoot = (Resolve-Path -LiteralPath $OutputRoot).Path
Ensure-Directory $ArchiveRoot

$sourceByKey = @{}
foreach ($pdf in Get-ChildItem -LiteralPath $InputRoot -Recurse -File -Filter *.pdf) {
  $title = Get-SourceTitleFromName $pdf.Name
  $key = Get-OutputSourceKey $pdf.Name
  if (-not $sourceByKey.ContainsKey($key)) {
    $sourceByKey[$key] = [pscustomobject]@{
      Title = $title
      SafeName = Get-SafeSourceName $title
      PdfPath = $pdf.FullName
    }
  }
}

$renamed = 0
$fileRenamed = 0
$archived = 0

$dirs = @(Get-ChildItem -LiteralPath $OutputRoot -Directory | Sort-Object Name)
foreach ($dir in $dirs) {
  $key = Get-OutputSourceKey $dir.Name
  if (-not $sourceByKey.ContainsKey($key)) {
    continue
  }

  $record = $sourceByKey[$key]
  $targetPath = Join-Path $resolvedOutputRoot $record.SafeName
  Assert-UnderRoot $dir.FullName $resolvedOutputRoot
  Assert-UnderRoot $targetPath $resolvedOutputRoot

  $currentPath = $dir.FullName
  if ($dir.Name -ne $record.SafeName) {
    if (Test-Path -LiteralPath $targetPath) {
      $targetMd = Join-Path $targetPath "$($record.SafeName).md"
      $targetPdf = Join-Path $targetPath "$($record.SafeName).pdf"
      if ((Test-Path -LiteralPath $targetMd) -and (Test-Path -LiteralPath $targetPdf)) {
        [void](Move-ToArchive $dir.FullName $record.SafeName)
        $archived++
        Repair-DirectoryFiles $targetPath $record.SafeName
        continue
      }

      foreach ($item in Get-ChildItem -LiteralPath $dir.FullName -Force) {
        $destination = Join-Path $targetPath $item.Name
        if (Test-Path -LiteralPath $destination) {
          [void](Move-ToArchive $item.FullName $record.SafeName)
          $archived++
        } else {
          Move-Item -LiteralPath $item.FullName -Destination $destination
        }
      }

      if (@(Get-ChildItem -LiteralPath $dir.FullName -Force).Count -eq 0) {
        Remove-Item -LiteralPath $dir.FullName
      } else {
        [void](Move-ToArchive $dir.FullName $record.SafeName)
        $archived++
      }
      $currentPath = $targetPath
    } else {
      Move-Item -LiteralPath $dir.FullName -Destination $targetPath
      $currentPath = $targetPath
      $renamed++
    }
  }

  $before = @(Get-ChildItem -LiteralPath $currentPath -File -Filter *.md).Name + @(Get-ChildItem -LiteralPath $currentPath -File -Filter *.pdf).Name
  Repair-DirectoryFiles $currentPath $record.SafeName
  $after = @(Get-ChildItem -LiteralPath $currentPath -File -Filter *.md).Name + @(Get-ChildItem -LiteralPath $currentPath -File -Filter *.pdf).Name
  if (($before -join "`n") -ne ($after -join "`n")) {
    $fileRenamed++
  }
}

[pscustomobject]@{
  RenamedDirectories = $renamed
  FileSetsRenamed = $fileRenamed
  ArchivedDuplicates = $archived
  ArchiveRoot = $ArchiveRoot
}
