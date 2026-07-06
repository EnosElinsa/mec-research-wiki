---
type: source
title: "Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain"
authors: ["Zhao Tong", "Shiyan Zhang", "Jing Mei", "Jiayi Sun", "Keqin Li"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3695882"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, uav-mec, uneven-terrain, task-offloading, trajectory-optimization, hierarchical-reinforcement-learning, td3, propulsion-energy]
related:
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[terrain-aware-channel-model]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[td3]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[gao-2024-d3qn-uav-mec-mobile-gt]]"
created: 2026-07-07
updated: 2026-07-07
---

# Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain

## Citation

Tong, Z., Zhang, S., Mei, J., Sun, J., & Li, K. (2026). *Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3695882.

## TL;DR

Studies UAV-assisted MEC over real uneven terrain, with dynamic service coverage, partial task allocation between UAV and BS computing, and UAV propulsion energy. The paper formulates a multi-objective non-convex problem that maximizes service coverage ratio and UAV propulsion energy efficiency under safe-flight constraints. PH-DRL combines a hierarchical network architecture with phased training: a TD3 first level controls 3D UAV flight, while an actor-critic second level decides covered UEs' task-allocation ratios.

## Problem framing

Uneven terrain complicates UAV-MEC in three ways: terrain affects safe 3D flight, terrain-induced height variation affects UAV-UE coverage, and dynamic UE coverage changes the dimensionality of the task-offloading decision. The paper targets remote mountainous areas where fixed infrastructure is limited and a UAV must cruise, hover, collect UE tasks, split them between UAV and BS computing, and manage propulsion energy.

## System model

- A three-layer MEC architecture: UEs on uneven terrain, one UAV with onboard MEC, and one BS connected to the core network.
- UE positions include terrain-induced altitude; the UAV's 3D position changes over time.
- A UE is served only if it is unserved and within UAV coverage, with the UAV higher than the UE.
- UE tasks are uploaded from ground to UAV; each task may be partially computed at the UAV and partially offloaded from UAV to BS.
- The channel uses an elevation-angle-based probabilistic LoS model for the UAV-UE link and a LoS UAV-BS link.
- Terrain elevation constrains the UAV's minimum safe altitude, and the objective includes service coverage ratio and propulsion energy efficiency.

## Method

PH-DRL separates the decision process into two levels:

- **First level:** TD3 controls UAV 3D movement and safe trajectory planning with terrain-aware state observations.
- **Second level:** an actor-critic network is invoked when serviceable UEs are detected and chooses task-allocation ratios.
- **Phased training:** the first phase uses randomized starts and exploration to gather terrain and UE-service experience; the second phase trains the policy with richer experience.
- **Dynamic invocation:** the task-offloading network is activated according to the number of covered UEs, reducing the mismatch between fixed neural-network dimensions and variable service sets.

## Key findings

- PH-DRL and the hierarchical ablation converge around the 300th episode; PH-DRL is more stable and reaches zero default steps earlier in the reported training curves.
- In testing, PH-DRL and H-DRL serve all UEs without violating constraints in the reported case, while other baselines show constraint breaches or poor convergence.
- PH-DRL achieves full UE coverage with about 2 kJ average energy expenditure per served UE in the Fig. 7 discussion.
- Under larger UE counts, PH-DRL maintains 100% service coverage and the highest overall system utility among the compared algorithms, even when its pure propulsion energy efficiency is not always the highest because it serves more remote UEs.
- Load-equal bandwidth allocation for the UAV-to-BS stage consistently beats user-equal allocation in hover energy efficiency.

## Limitations / future work

The evaluation is simulation-based, using paid-platform DEM data for a 500 m by 500 m region. The conclusion states future work will extend to multi-UAV collaboration over uneven terrain and add terrain/environment uncertainty such as user mobility. DOI/venue/year are verified by DOI metadata because the parse does not include a clean DOI line.

## Relation to the corpus

This source is a DRL counterpart to [[wu-2026-terrain-aware-uav-mec]]. Wu et al. build a geometric DEM blocked-region channel model and solve a CMOP with evolutionary methods; Tong et al. use real elevation data in a hierarchical DRL controller and emphasize service coverage plus propulsion efficiency. It also relates to [[gao-2024-d3qn-uav-mec-mobile-gt]], which handles 3D UAV-MEC in an obstacle-aware post-disaster urban setting.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain/Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain.md`
- Origin PDF: `raw/sources/Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain/Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain.pdf`
- Figures: `raw/sources/Energy-Efficient Joint Task Offloading and 3D Trajectory Optimization for UAV-assisted MEC Systems over Uneven Terrain/images/`
