$ErrorActionPreference = "Stop"

. "$PSScriptRoot\mec_relevance.ps1"

$cases = @(
  @{
    Name = "keeps explicit MEC title"
    Text = "Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks"
    Expected = $true
  },
  @{
    Name = "keeps mobile edge computing title"
    Text = "Cooperative Drone-Vehicle Mobile Edge Computing for Low-Altitude Economy"
    Expected = $true
  },
  @{
    Name = "keeps computation offloading title"
    Text = "Cost-Aware UAV-Enabled Computation Offloading for Green Internet of Things"
    Expected = $true
  },
  @{
    Name = "keeps task offloading title"
    Text = "Deep Reinforcement Learning-Based Task Offloading With Edge Servers"
    Expected = $true
  },
  @{
    Name = "keeps edge inference title"
    Text = "UAV-Assisted Edge Inference With Integrated Sensing, Communication, and Computation"
    Expected = $true
  },
  @{
    Name = "keeps task-driven resource management in UAV swarms"
    Text = "Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms"
    Expected = $true
  },
  @{
    Name = "keeps coded caching in UAV-assisted edge networks"
    Text = "Coded Caching Enabled D2D Content Delivery in UAV-Assisted Marine Edge Networks"
    Expected = $true
  },
  @{
    Name = "keeps split federated learning for foundation models"
    Text = "Communication-Pipelined Split Federated Learning for Foundation Model Fine-Tuning in UAV Networks"
    Expected = $true
  },
  @{
    Name = "keeps wireless powered edge networks"
    Text = "Decentralized Learning-Driven AoI Optimization in UAV-Assisted Wireless Powered Edge Networks"
    Expected = $true
  },
  @{
    Name = "keeps semantic content reuse in UAV-assisted metaverse"
    Text = "Deep Lifelong Learning for Adaptive Semantic-Aware Content Reuse in UAV-Assisted Metaverse"
    Expected = $true
  },
  @{
    Name = "keeps data storage in UAV-enabled edge systems"
    Text = "Erasure Coding-Based Cost-Optimized and Latency-Aware Data Storage in UAV-Enabled Edge Systems"
    Expected = $true
  },
  @{
    Name = "keeps vehicle twin migration with workload prediction"
    Text = "Hierarchical Control Multi-Agent DRL for Vehicle Twin Migration with Workload Prediction in UAV-Assisted Vehicular Metaverses"
    Expected = $true
  },
  @{
    Name = "keeps federated edge learning with computation"
    Text = "Integrated Sensing, Computation, and Communication for UAV-Assisted Federated Edge Learning"
    Expected = $true
  },
  @{
    Name = "keeps low-altitude economy service balance"
    Text = "Toward Adaptive IoT Service Balance in Low-Altitude Economy: Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer"
    Expected = $true
  },
  @{
    Name = "keeps UAV communication trajectory optimization"
    Text = "Energy-Efficient UAV Communication With Trajectory Optimization"
    Expected = $true
  },
  @{
    Name = "keeps UAV wireless power transfer"
    Text = "UAV-Enabled Wireless Power Transfer: A Tutorial Overview"
    Expected = $true
  },
  @{
    Name = "keeps ISAC tracking with UAV context"
    Text = "A Predictive UAV Framework for Tracking Fast-Moving Vehicles in Dynamic Environments Integrated Sensing and Communication"
    Expected = $true
  },
  @{
    Name = "keeps maritime network resource allocation"
    Text = "An Online Double Auction Mechanism for Dynamic Resource Allocation in Maritime Networks; keywords = task scheduling"
    Expected = $true
  },
  @{
    Name = "keeps computing power networks with edge context"
    Text = "Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization; keywords = edge computing"
    Expected = $true
  },
  @{
    Name = "skips pure delivery trajectory planning"
    Text = "3D Trajectory and Pickup-Drop-Off Strategy for UAV-Enabled Delivery"
    Expected = $false
  },
  @{
    Name = "skips pure authentication"
    Text = "A PUF-Based Lightweight Authentication Scheme for UAV-Assisted Internet of Vehicles"
    Expected = $false
  },
  @{
    Name = "skips TPDS NPU scheduling"
    Text = "Workload-Aware Performance Model Based Soft Preemptive Real-Time Scheduling for Neural Processing Units"
    Expected = $false
  },
  @{
    Name = "skips pure YOLO detection"
    Text = "YOLO-RAW: Advancing UAV Detection With Robustness to Adverse Weather Conditions"
    Expected = $false
  },
  @{
    Name = "skips pure pavement crack detection"
    Text = "Hybrid CNN-Mamba Network and Air-Ground Platform for Pavement Crack Evaluation"
    Expected = $false
  },
  @{
    Name = "skips pure road detection"
    Text = "Efficient Road Detection and Tracking for Unmanned Aerial Vehicle"
    Expected = $false
  },
  @{
    Name = "skips pure coverage path planning"
    Text = "A Clustering-Based Coverage Path Planning Method for Autonomous Heterogeneous UAVs"
    Expected = $false
  },
  @{
    Name = "skips physical attacks overview"
    Text = "Physical Attacks on a UAV System: Overview and Emerging Methods"
    Expected = $false
  },
  @{
    Name = "skips pure obstacle avoidance control"
    Text = "Memory-Based Deep Reinforcement Learning for Obstacle Avoidance in UAV With Limited Environment Knowledge"
    Expected = $false
  },
  @{
    Name = "skips pure payload transport review"
    Text = "Multirotor UAVs Transporting Cable-Suspended Loads: A Literature Review"
    Expected = $false
  },
  @{
    Name = "skips general base-station PHY without UAV context"
    Text = "Game-Theoretic Optimization of Multiple Interfering Base Stations Deployment"
    Expected = $false
  },
  @{
    Name = "keeps UAV-aided covert satellite communication"
    Text = "Uncertain Location Transmitter and UAV-Aided Warden-Based LEO Satellite Covert Communication Systems"
    Expected = $true
  },
  @{
    Name = "keeps if keywords provide MEC signal"
    Text = "Efficient Resource Management for UAV Communications; keywords = mobile edge computing; task offloading"
    Expected = $true
  }
)

$failures = 0
foreach ($case in $cases) {
  $result = Test-MecRelevant $case.Text
  if ($result -ne $case.Expected) {
    Write-Host "FAIL $($case.Name): expected=$($case.Expected) actual=$result"
    $failures++
  } else {
    Write-Host "PASS $($case.Name)"
  }
}

if ($failures -gt 0) {
  throw "$failures MEC relevance tests failed"
}

Write-Host "All MEC relevance tests passed."
