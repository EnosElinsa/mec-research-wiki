$ErrorActionPreference = "Stop"

. "$PSScriptRoot\source_naming.ps1"

$cases = @(
  @{
    Name = "uses underscores between words"
    Title = "Energy-Efficient UAV Communication With Trajectory Optimization"
    Expected = "Energy-Efficient_UAV_Communication_With_Trajectory_Optimization"
  },
  @{
    Name = "treats spaced hyphens as separators"
    Title = "Integrated Sensing- Computation- and Communication for UAV-Assisted Federated Edge Learning"
    Expected = "Integrated_Sensing_Computation_and_Communication_for_UAV-Assisted_Federated_Edge_Learning"
  },
  @{
    Name = "removes parentheses without breaking acronyms"
    Title = "Age of Information (AoI)-Aware Joint Optimization"
    Expected = "Age_of_Information_AoI-Aware_Joint_Optimization"
  },
  @{
    Name = "strips numeric PDF prefixes"
    Title = "001_UAV-Assisted MEC System With Mobile Ground Terminals"
    Expected = "UAV-Assisted_MEC_System_With_Mobile_Ground_Terminals"
  },
  @{
    Name = "does not strip 3-D as a numeric prefix"
    Title = "3-D Self-Tracking of UAV Based on Minor Subspace Majorization-Minimization Iteration"
    Expected = "3-D_Self-Tracking_of_UAV_Based_on_Minor_Subspace_Majorization-Minimization_Iteration"
  },
  @{
    Name = "does not treat decimal title text as an extension"
    Title = "Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications Using Rate Splitting Multiple Access"
    Expected = "Energy-Efficient_Transmission_Strategy_for_UAV-RIS_2_0_Assisted_Communications_Using_Rate_Splitting_Multiple_Access"
  }
)

$failures = 0
foreach ($case in $cases) {
  $actual = Get-SafeSourceName $case.Title
  if ($actual -ne $case.Expected) {
    Write-Host "FAIL $($case.Name): expected=$($case.Expected) actual=$actual"
    $failures++
  } else {
    Write-Host "PASS $($case.Name)"
  }
}

$decimalKey = Get-NormalizedSourceKey "Energy-Efficient Transmission Strategy for UAV-RIS 2.0 Assisted Communications"
if ($decimalKey -ne "energyefficienttransmissionstrategyforuavris20assistedcommunications") {
  Write-Host "FAIL decimal normalized key: actual=$decimalKey"
  $failures++
} else {
  Write-Host "PASS decimal normalized key"
}

$longTitle = "Joint Optimization of UAV Trajectory and Number of Reflecting Elements for UAV-Mounted Intelligent Reflecting Surface-Assisted Data Collection in Wireless Sensor Networks Under Transmission Prior"
$longOutputKey = Get-OutputSourceKey $longTitle
if ($longOutputKey.Length -gt 180) {
  throw "Output key should be based on truncated safe output names"
}
if ($longOutputKey -ne (Get-OutputSourceKey (Get-SafeSourceName $longTitle))) {
  Write-Host "FAIL output key is not stable between source title and safe name"
  $failures++
} else {
  Write-Host "PASS output key stability"
}

if ($failures -gt 0) {
  throw "$failures source naming tests failed"
}

Write-Host "All source naming tests passed."
