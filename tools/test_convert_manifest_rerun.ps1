$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$convertScript = Join-Path $PSScriptRoot "convert_with_mineru.ps1"
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) ("mineru-convert-test-" + [guid]::NewGuid().ToString("N"))

try {
  $inputRoot = Join-Path $tempRoot "input"
  $groupRoot = Join-Path $inputRoot "TITS"
  $outputRoot = Join-Path $tempRoot "sources"
  $nonMecRoot = Join-Path $tempRoot "non-mec"
  $manifestPath = Join-Path $tempRoot "manifest.csv"

  New-Item -ItemType Directory -Path $groupRoot, $outputRoot, $nonMecRoot | Out-Null
  $pdfPath = Join-Path $groupRoot "001_YOLO-RAW Advancing UAV Detection With Robustness to Adverse Weather Conditions.pdf"
  Set-Content -LiteralPath $pdfPath -Value "fake pdf placeholder" -Encoding ASCII

  [pscustomobject]@{
    Timestamp = (Get-Date).ToString("s")
    Status = "skipped-not-mec"
    Group = "TITS"
    Title = "YOLO-RAW Advancing UAV Detection With Robustness to Adverse Weather Conditions"
    SourcePath = $pdfPath
    OutputDir = ""
    Message = "Already recorded as not MEC-related"
  } | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding UTF8

  & powershell -NoProfile -ExecutionPolicy Bypass -File $convertScript `
    -InputRoot $inputRoot `
    -OutputRoot $outputRoot `
    -ManifestPath $manifestPath `
    -NonMecRoot $nonMecRoot `
    -Limit 1 | Out-Host

  $rows = @(Import-Csv -LiteralPath $manifestPath)
  $skipRows = @($rows | Where-Object { $_.SourcePath -eq $pdfPath -and $_.Status -eq "skipped-not-mec" })
  if ($skipRows.Count -ne 1) {
    throw "Expected one skipped-not-mec row after rerun, found $($skipRows.Count)"
  }

  Write-Host "PASS skipped-not-mec rows are not duplicated on rerun"
}
finally {
  if (Test-Path -LiteralPath $tempRoot) {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
  }
}
