---
type: source
title: "Joint Trajectory Planning and Task Offloading in UAV-Assisted Inspection Networks: A Transformer-Based Approach"
authors: ["Ruibin Guo", "Wei Quan", "Xinyu Huang", "Yuming Zhang", "Mingyuan Liu", "Dong Yang", "Hongke Zhang", "Xuemin Shen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3636717"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 5, May 2026"
tags: [source, uav-assisted-inspection, railway-inspection, task-offloading, uav-trajectory-control, transformer, reinforce]
related:
  - "[[transformer-encoder]]"
  - "[[uav-enabled-its]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[dueling-dqn]]"
  - "[[ant-colony-optimization]]"
  - "[[jia-2026-ufsp-rail-inspection]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint Trajectory Planning and Task Offloading in UAV-Assisted Inspection Networks: A Transformer-Based Approach

## Citation

Guo, R., Quan, W., Huang, X., Zhang, Y., Liu, M., Yang, D., Zhang, H., & Shen, X. (2026). *Joint Trajectory Planning and Task Offloading in UAV-Assisted Inspection Networks: A Transformer-Based Approach*. **IEEE Transactions on Mobile Computing**, 25(5), 6383-6397. DOI: 10.1109/TMC.2025.3636717.

## TL;DR

Introduces an AGI-oriented Transformer (AoT) for UAV-assisted railway inspection. A UAV leaves a hive, visits sensor clusters, gathers inspection task requirements, decides whether each task runs on the sensor, UAV, or hive edge server, and returns to recharge. AoT uses a shared encoder-only [[transformer-encoder]] with specialized MLP output heads for trajectory planning and task offloading, trained with REINFORCE-style optimization. The parse reports shorter trajectories and lower offloading cost than heuristic, recurrent, and value-based baselines.

## Problem

Railway inspections combine heterogeneous tasks: camera-based object recognition, rain/humidity monitoring for landslide risk, and LiDAR or infrastructure modeling for bridges and related assets. These tasks differ in data volume, computation intensity, and urgency. The UAV must jointly decide where to fly and where computation happens while carrying limited onboard compute, storage, battery, and model capacity.

## System model

- The architecture has a hive, one rotary-wing UAV, and clustered ground sensors.
- The hive recharges the UAV and acts as an edge cloud server.
- The UAV acts as both relay and MEC server, deciding trajectory and task-offloading location.
- Each task can be processed at the sensor, the UAV, or the hive; hive execution requires UAV forwarding.
- The UAV visits virtual access points for sensor clusters and returns to the hive after the inspection cycle.
- The objective minimizes a weighted sum of total inspection latency and total energy consumption.

## Method

AoT uses one shared encoder to process either cluster-location tokens or task-feature tokens. The encoded representation is routed to a trajectory-planning head or task-offloading head. The trajectory problem is transformed into a TSP-hybrid implicit MDP, while task offloading is treated as an offloading MDP. Output heads are MLPs rather than full Transformer decoders, reducing parameters for UAV deployment.

## Key findings

- For 20, 30, 40, and 50 clusters, AoT reports trajectory lengths of 4245.18 m, 4874.85 m, 5646.72 m, and 6023.02 m, respectively.
- In the 45-cluster comparison, AoT reports a 5869.52 m trajectory versus 7093.39 m for Greedy, 7075.64 m for BO_ACO, and 8154.82 m for ABC; the paper describes this as 28.02% shorter than ABC, 14.87% shorter than BO_ACO, and 17.25% shorter than Greedy.
- In larger trajectory-planning tests, increasing training from 500 to 1000 epochs reduces the 80-cluster path from 8295.17 m to 7648.61 m; 100-cluster tests produce 9236.00 m and 9145.47 m paths for batch sizes 12 and 16.
- For task offloading, AoT reaches an average reward around -85 by about episode 300, while the LSTM encoder converges around episode 400 and D3QN/DDQN stabilize below -95.
- The best reported learning rate is 1e-3, with average reward -84.21 and the smallest error bars among the compared settings.
- With a UAV computation-energy budget of 180 J, AoT offloads 56.2% of tasks to the UAV, compared with 54.4% for BO_ACO, 32.1% for LSTM, 30.6% for GRU, and 28.1% for RNN.

## Limitations / future work

The evaluation is simulation-based. The authors note that AoT can produce only near-optimal trajectories as cluster counts grow; the parse specifically notes local loops beyond 40 clusters and identifies Transformer memory demand as a bottleneck. Future work targets more specialized output heads for additional tasks.

## Relation to the corpus

This paper links the rail/ITS branch of the wiki to Transformer-based offloading. It complements [[jia-2026-ufsp-rail-inspection]], which focuses on decentralized multi-UAV rail-line inspection under imperfect information, while this paper focuses on a single UAV/hive inspection workflow and a lightweight shared-encoder model. It also extends the [[uav-enabled-its]] concept beyond vehicle-carried drones by adding railway sensor inspection with joint [[uav-trajectory-control]] and [[task-offloading]].

## Raw artifacts

- `raw/sources/Joint Trajectory Planning and Task Offloading in UAV-Assisted Inspection Networks A Transformer-Based Approach/Joint Trajectory Planning and Task Offloading in UAV-Assisted Inspection Networks A Transformer-Based Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
