---
type: source
title: "Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems"
authors: ["Zhe Zhang", "Ju Jiang", "Keck Voon Ling", "Xinhua Wang", "Wen-An Zhang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3667967"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, low-altitude-economy, uav-enabled-its, multi-uav, task-allocation, path-planning, potential-game, a-star]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[uav-enabled-its]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[uav-trajectory-control]]"
  - "[[collision-avoidance-mgi]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-07-06
updated: 2026-07-06
---

# Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems

## Citation

Zhang, Z., Jiang, J., Ling, K. V., Wang, X., & Zhang, W.-A. (2026). *Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems*. **IEEE Transactions on Intelligent Transportation Systems**, 27(4), 4112-4124. DOI: 10.1109/TITS.2026.3667967.

## TL;DR

A distributed multi-UAV mission-planning framework for low-altitude urban intelligent transportation systems (LU-ITS). The paper couples two decisions that are often separated: which UAVs should execute each emergency-rescue or cargo-delivery task, and how each UAV should fly collision-free paths through a constrained urban low-altitude environment. Task allocation is modeled as an evolutionary [[potential-game]] solved by an Improved Log-linear Learning Algorithm (ILLA); path planning is solved by a Constraint-Based Multilayer Bidirectional Adaptive A-Star (CBMBA A-Star) search. Simulations report higher task reward and shorter execution / runtime than the listed baselines.

## Problem

Low-altitude urban traffic applications need coordinated UAV fleets, not isolated single-UAV routes. Emergency rescue and last-mile delivery tasks can require multiple UAVs, while paths must respect minimum safe separation, turning-angle limits, speed bounds, obstacles, and bandit threats. The paper targets a distributed decision process where UAVs exchange neighborhood state and iteratively update strategies until reaching a stable task-allocation / path-planning solution.

## System model

- **Scenario:** LU-ITS missions for traffic emergency rescue and last-mile cargo transportation / delivery.
- **Agents:** multiple UAVs that communicate with neighboring UAVs and update state iteratively.
- **Tasks:** each task has mission reward, demand, and execution constraints; some tasks require cooperative assignment by multiple UAVs.
- **Constraints:** safe separation, turning-angle limits, velocity bounds, load / path costs, and urban threats / obstacles.
- **Objective:** maximize mission reward while accounting for path and load costs, then generate feasible collision-free paths for the assigned UAVs.

## Method

The task-allocation part is an evolutionary potential game. The paper analytically derives the potential function and proves a Nash equilibrium exists. ILLA then uses derived Boltzmann parameters so the algorithm converges to the optimal Nash equilibrium with probability one.

The path-planning part is CBMBA A-Star: a graph-search planner that combines constraint handling, multilayer search, bidirectional search, and adaptive replanning to generate optimal collision-free UAV paths in the low-altitude urban environment.

## Key findings

- The abstract reports that the proposed approach improves task reward by **11.67%**, reduces task execution time by **37.41%**, and decreases run time by **61.02%** against the baseline method.
- **Traffic emergency rescue case:** 20 UAVs and 3 tasks. Table II reports ILLA task reward 36578.95, higher than LLA, BRLA, and CBBA; Table III reports CBMBA A-Star path cost 14529.28 m and runtime 21.43 s, lower runtime than A-Star and DE.
- **Last-mile cargo transportation case:** 40 UAVs and 5 tasks. Table IV reports ILLA reward 69862.14 and lower execution time than LLA and CBBA; the text reports reward improvements of 13.57%, 15.64%, and 11.35% over three baselines.
- **Dynamic replanning:** when threats change, CBMBA A-Star's path cost increases by only 2.43% in the reported case; the D-Star and MSFDE baselines show larger runtime / turning-node increases.

## Limitations / future work

The validation is simulation-based. The paper models communication among neighboring UAVs, but does not present a field deployment or real-time network-stack experiment. The task and path constraints are rich for LU-ITS, yet real urban air-traffic regulations, weather, sensing uncertainty, and heterogeneous vehicle dynamics are outside the reported evaluation.

## Relation to the corpus

This is the corpus's clearest low-altitude ITS source where [[potential-game]] task allocation is paired with explicit path planning and collision avoidance. It extends [[low-altitude-intelligent-network]] from architectural / spectrum questions toward operational fleet planning, and complements [[chen-2026-cargo-uav-pickup-lae]] by adding cooperative task allocation and path search rather than cellular-connected pickup routing. It also links the game-theoretic line ([[chen-2024-ulse-game]], [[li-2025-stochastic-game-uav-swarm]]) with the trajectory / path-planning line represented by [[uav-trajectory-control]] and [[collision-avoidance-mgi]].

## Raw artifacts

- `raw/sources/Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems/Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
