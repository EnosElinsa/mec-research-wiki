function Get-MecRelevanceMatch([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) {
    return ""
  }

  $normalized = $Text.ToLowerInvariant()
  $normalized = $normalized -replace "[\u2010-\u2015]", "-"
  $normalized = $normalized -replace "[^a-z0-9+.-]+", " "
  $normalized = " $($normalized -replace '\s+', ' ') "

  $excludePatterns = @(
    "\bwireless power transfer\b"
  )

  foreach ($pattern in $excludePatterns) {
    if ($normalized -match $pattern) {
      return ""
    }
  }

  $includePatterns = @(
    "\bmec\b",
    "\blow[- ]altitude economy\b",
    "\blow[- ]altitude economy networking\b",
    "\blow[- ]altitude economy networks\b",
    "\bLAE\b".ToLowerInvariant(),
    "\bmobile edge computing\b",
    "\bmulti access edge computing\b",
    "\bmulti-access edge computing\b",
    "\bedge computing\b",
    "\bedge server(s)?\b",
    "\bedge cloud\b",
    "\bedge network(s)?\b",
    "\bedge system(s)?\b",
    "\baerial edge\b",
    "\bedge intelligence\b",
    "\bedge inference\b",
    "\bedge learning\b",
    "\bfederated edge learning\b",
    "\bsplit inference\b",
    "\bcloudlet(s)?\b",
    "\bfog computing\b",
    "\bfog node(s)?\b",
    "\bcomputation offloading\b",
    "\bcomputational offloading\b",
    "\btask offloading\b",
    "\bservice offloading\b",
    "\bdata offloading\b",
    "\boffloading strateg(y|ies)\b",
    "\boffloading optimization\b",
    "\boffloading decision(s)?\b",
    "\bservice placement\b",
    "\bfunction placement\b",
    "\bmodel placement\b",
    "\btask[- ]driven resource management\b",
    "\bsplit federated learning\b",
    "\bsemantic[- ]aware content reuse\b",
    "\btwin migration\b",
    "\bsubmodel partition\b",
    "\bcollaborative inference\b",
    "\bdistributed inference\b"
  )

  foreach ($pattern in $includePatterns) {
    if ($normalized -match $pattern) {
      return $pattern
    }
  }

  return ""
}

function Test-MecRelevant([string]$Text) {
  $match = Get-MecRelevanceMatch $Text
  if (-not [string]::IsNullOrWhiteSpace($match)) {
    return $true
  }
  return $false
}

function Get-BibEntriesByNumber([string]$DirectoryPath) {
  $entries = @{}
  $bib = Get-ChildItem -LiteralPath $DirectoryPath -File -Filter "*.bib" -ErrorAction SilentlyContinue |
    Select-Object -First 1
  if ($null -eq $bib) {
    return $entries
  }

  $content = Get-Content -LiteralPath $bib.FullName -Raw
  $pattern = "(?ms)%\s*(\d+)\.\s*(.*?)(?=^\s*%\s*\d+\.|\z)"
  foreach ($match in [regex]::Matches($content, $pattern)) {
    $number = $match.Groups[1].Value.PadLeft(3, "0")
    $entry = $match.Groups[2].Value
    $entries[$number] = $entry
  }

  return $entries
}

function Get-PaperMetadataText([System.IO.FileInfo]$Pdf, [hashtable]$BibEntriesByNumber) {
  $fileTitle = [IO.Path]::GetFileNameWithoutExtension($Pdf.Name) -replace "^[0-9]{1,4}[_\-\s]+", ""
  $numberMatch = [regex]::Match($Pdf.Name, "^(\d{1,4})[_\-\s]+")
  if ($numberMatch.Success) {
    $number = $numberMatch.Groups[1].Value.PadLeft(3, "0")
    if ($BibEntriesByNumber.ContainsKey($number)) {
      return "$fileTitle`n$($BibEntriesByNumber[$number])"
    }
  }

  return $fileTitle
}

function Test-PdfMecRelevant([System.IO.FileInfo]$Pdf, [hashtable]$BibEntriesByNumber) {
  $text = Get-PaperMetadataText $Pdf $BibEntriesByNumber
  return Test-MecRelevant $text
}
