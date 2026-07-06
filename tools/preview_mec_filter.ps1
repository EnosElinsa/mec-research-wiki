param(
  [string]$InputRoot = "C:\Users\labs2\Desktop\Papers\TMC_TWC_TITS_TGCN_TPDS"
)

$ErrorActionPreference = "Stop"
. "$PSScriptRoot\mec_relevance.ps1"

$bibEntriesByDirectory = @{}
$rows = foreach ($pdf in Get-ChildItem -LiteralPath $InputRoot -Recurse -File -Filter *.pdf | Sort-Object FullName) {
  if (-not $bibEntriesByDirectory.ContainsKey($pdf.DirectoryName)) {
    $bibEntriesByDirectory[$pdf.DirectoryName] = Get-BibEntriesByNumber $pdf.DirectoryName
  }
  $title = [IO.Path]::GetFileNameWithoutExtension($pdf.Name) -replace "^[0-9]{1,4}[_\-\s]+", ""
  [pscustomobject]@{
    Group = Split-Path $pdf.DirectoryName -Leaf
    Title = $title
    IsMec = Test-PdfMecRelevant $pdf $bibEntriesByDirectory[$pdf.DirectoryName]
    Path = $pdf.FullName
  }
}

"summary_by_group:"
$rows | Group-Object Group,IsMec | Sort-Object Name | Select-Object Name,Count | Format-Table -AutoSize

"kept_by_group:"
$rows | Where-Object IsMec | Group-Object Group | Sort-Object Name | Select-Object Name,Count | Format-Table -AutoSize

"skipped_by_group:"
$rows | Where-Object { -not $_.IsMec } | Group-Object Group | Sort-Object Name | Select-Object Name,Count | Format-Table -AutoSize

"kept_samples:"
$rows | Where-Object IsMec | Select-Object -First 80 Group,Title | Format-Table -AutoSize

"skipped_samples:"
$rows | Where-Object { -not $_.IsMec } | Select-Object -First 80 Group,Title | Format-Table -AutoSize
