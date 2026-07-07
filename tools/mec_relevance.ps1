function Get-MecRelevanceMatch([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) {
    return ""
  }

  $normalized = $Text.ToLowerInvariant()
  $normalized = $normalized -replace "[\u2010-\u2015]", "-"
  $normalized = $normalized -replace "[^a-z0-9+.-]+", " "
  $normalized = " $($normalized -replace '\s+', ' ') "

  $networkContextPatterns = @(
    "\bmec\b",
    "\bedge\b",
    "\bcloud\b",
    "\bfog\b",
    "\bcomput(ing|ation)\b",
    "\boffloading\b",
    "\bcommunication(s)?\b",
    "\bnetwork(s|ing)?\b",
    "\bresource(s)?\b",
    "\bservice(s)?\b",
    "\bsensing\b",
    "\bisac\b",
    "\binternet of things\b",
    "\biot\b",
    "\biov\b",
    "\bvehicular\b",
    "\blow[- ]altitude\b",
    "\blow[- ]altitude economy\b",
    "\blae\b",
    "\bsagin\b",
    "\bntn\b",
    "\bhap\b",
    "\bsatellite\b",
    "\bmaritime\b",
    "\bmarine\b",
    "\bair[- ]ground\b",
    "\baerial[- ]terrestrial\b"
  )

  $optimizationContextPatterns = @(
    "\boptimization\b",
    "\ballocation\b",
    "\bscheduling\b",
    "\bdeployment\b",
    "\bplacement\b",
    "\bbeamforming\b",
    "\btrajectory\b",
    "\brouting\b",
    "\bhandover\b",
    "\bthroughput\b",
    "\blatency\b",
    "\bdelay\b",
    "\bqos\b",
    "\benergy efficiency\b",
    "\bcost\b",
    "\breliability\b"
  )

  $cvPatterns = @(
    "\byolo\b",
    "\bvision[- ]based\b",
    "\bobject detection\b",
    "\bvehicle detection\b",
    "\bpavement crack\b",
    "\bpavement distress\b",
    "\broad detection\b",
    "\brail fastener\b",
    "\bcatenary support components detection\b",
    "\baerial imagery\b",
    "\bdetector\b",
    "\bdetection with robustness\b"
  )

  $securityProtocolPatterns = @(
    "\bauthentication\b",
    "\bkey agreement\b",
    "\bpuf[- ]based\b",
    "\bphysical attacks\b",
    "\battack(s)? on a uav system\b"
  )

  $pureControlPatterns = @(
    "\bobstacle avoidance\b",
    "\battitude(s)?\b",
    "\bcable[- ]suspended load(s)?\b",
    "\bconsensus control\b",
    "\benclosing control\b",
    "\bflocking\b",
    "\bcollision avoidance\b",
    "\bcoverage path planning\b",
    "\bpickup[- ]drop[- ]off\b",
    "\bpick[- ]up system(s)?\b",
    "\bcargo pickup\b",
    "\buav[- ]enabled delivery\b"
  )

  $pureHardwarePatterns = @(
    "\bneural processing unit(s)?\b",
    "\bnpu(s)?\b",
    "\bsoft preemptive real[- ]time scheduling\b"
  )

  $generalWirelessPhyPatterns = @(
    "\bbase station(s)?\b",
    "\binterfering base stations\b",
    "\bantenna array(s)?\b",
    "\bwireless communication(s)?\b",
    "\bbeam[- ]delay alignment\b",
    "\bnear[- ]field\b",
    "\bmimo\b",
    "\bris\b",
    "\birs\b",
    "\bchannel\b"
  )

  foreach ($pattern in $pureHardwarePatterns) {
    if ($normalized -match $pattern) {
      return ""
    }
  }

  $includePatterns = @(
    "\bmec\b",
    "\blow[- ]altitude economy\b",
    "\blow[- ]altitude economy networking\b",
    "\blow[- ]altitude economy networks\b",
    "\blae\b",
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

  $hasNetworkContext = $false
  foreach ($pattern in $networkContextPatterns) {
    if ($normalized -match $pattern) {
      $hasNetworkContext = $true
      break
    }
  }

  $hasOptimizationContext = $false
  foreach ($pattern in $optimizationContextPatterns) {
    if ($normalized -match $pattern) {
      $hasOptimizationContext = $true
      break
    }
  }

  foreach ($pattern in $securityProtocolPatterns) {
    if ($normalized -match $pattern) {
      return ""
    }
  }

  foreach ($pattern in $cvPatterns) {
    if ($normalized -match $pattern) {
      if (-not ($hasNetworkContext -and $hasOptimizationContext)) {
        return ""
      }
    }
  }

  foreach ($pattern in $pureControlPatterns) {
    if ($normalized -match $pattern) {
      if (-not ($hasNetworkContext -and $hasOptimizationContext)) {
        return ""
      }
    }
  }

  $hasUavLowAltitudeOrVerticalContext = $normalized -match "\buav(s)?\b|\bunmanned aerial\b|\bdrone(s)?\b|\baerial\b|\blow[- ]altitude\b|\blae\b|\bsagin\b|\bntn\b|\bsatellite\b|\bhap\b|\biot\b|\binternet of things\b|\biov\b|\bvehicular\b|\bmaritime\b|\bmarine\b|\bair[- ]ground\b|\bspace[- ]air[- ]ground\b"
  if (-not $hasUavLowAltitudeOrVerticalContext) {
    foreach ($pattern in $generalWirelessPhyPatterns) {
      if ($normalized -match $pattern) {
        return ""
      }
    }
  }

  return "default-keep"
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
