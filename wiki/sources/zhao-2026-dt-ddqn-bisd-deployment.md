---
type: source
title: "Deployment Design for Multi-UAV-Assisted IoT Networks: A Digital Twin-Driven Deep Reinforcement Learning Approach"
authors: ["Le Zhao", "Zesong Fei", "Jingxuan Huang", "Xinyi Wang", "Bin Li", "Weijie Yuan"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3596864"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, digital-twin, ddqn, uav-deployment, iot-data-collection, obstacle-avoidance, age-of-information]
related:
  - "[[digital-twin-assisted-online-drl-policy-refresh]]"
  - "[[digital-twin]]"
  - "[[ddqn]]"
  - "[[deep-q-network]]"
  - "[[age-of-information]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[blockage-aware-channel-model]]"
  - "[[weijie-yuan]]"
created: 2026-07-12
updated: 2026-07-13
---

# Deployment Design for Multi-UAV-Assisted IoT Networks: A Digital Twin-Driven Deep Reinforcement Learning Approach

## Citation

Zhao, L., Fei, Z., Huang, J., Wang, X., Li, B., & Yuan, W. (2026). *Deployment Design for Multi-UAV-Assisted IoT Networks: A Digital Twin-Driven Deep Reinforcement Learning Approach*. **IEEE Transactions on Wireless Communications**, 25, 2468-2483. DOI: 10.1109/TWC.2025.3596864.

## TL;DR

Divides a multi-UAV IoT collection mission into balanced service regions, 3-D transfer, and fixed-altitude collection stages. Parallel digital-twin environments train separate DDQN policies, synchronize newly sensed obstacles, halt unsafe actions, and refresh policy parameters when the physical and virtual environments diverge.

## Problem

Multiple UAVs must reach assigned IoT regions and serve all ground nodes quickly in a partially known three-dimensional environment. Buildings are known before flight, but random obstacles are discovered online; radio blockage, discrete maneuvering, transfer time, coverage, and collection progress interact. A static policy trained against the initial map can therefore become unsafe or inefficient as the mission reveals new obstacles.

## System model

- A centralized base station and wired digital-twin server coordinate UAVs serving stationary ground nodes in discretized urban and rural mission areas.
- K-means-based mission division balances ground-node assignments. UAVs first execute a 3-D mission-transfer stage, then a fixed-altitude 2-D mission-maintaining stage for coverage and data collection.
- Each motion action selects `-1`, `0`, or `1` on each axis, yielding 26 three-dimensional directions plus hover during transfer. Forward sensing exposes binary obstacle-threat indicators.
- Air-to-ground links use geometric building blockage for LoS/NLoS classification, spatially correlated shadowing, and Rician/Rayleigh small-scale fading. UAVs use separate bandwidths.
- The objective minimizes total transfer-plus-service time under spatial, action, obstacle, SINR, access-count, mission-duration, and complete-service constraints.

## Method

The transfer [[ddqn|DDQN]] state combines current and target 3-D coordinates, distance features, and a 26-entry threat vector; its reward combines progress with hover, crash, boundary, and step-time penalties. The maintenance controller observes fixed-altitude 2-D position, per-node coverage/service indicators, aggregate [[age-of-information|AoI]], and eight directional threats; its reward emphasizes service completion and penalizes boundary or collision events.

[[digital-twin-assisted-online-drl-policy-refresh]] runs multiple virtual environments to collect replay data and pretrain the two controllers. During execution, sensed obstacle changes are synchronized into the twin, unsafe selected actions can be halted, affected virtual environments are updated, and revised network parameters are returned to the UAVs after retraining. The mission regions themselves are produced through K-means clustering followed by coarse- and fine-cell remapping to balance ground-node counts.

## Key findings

- In simulation, DT-DDQN approaches zero training crashes within 500 episodes while the reported DDQN and QMIX curves do not; no exact reward ordinates are printed.
- The selected service altitudes are `80 m` in the rural setting and `150 m` in the urban setting based on 20 repeated simulations.
- At those altitudes, service-stage duration is reported `60%`/`30%` lower than ACO/scanning in the urban setting and `75%`/`58%` lower in the rural setting.
- With five UAVs, DT-DDQN-BiSD totals `285.3 s` in the rural and `117.9 s` in the urban case. Fully informed ideal PSO-BiSD is faster at `268.2 s` and `104.7 s`, so the proposal does not outperform that upper-bound baseline on mission time.
- Online twin updates add `1.6 MB` and `1.8 MB` beyond state/action synchronization; final stated twin fidelity is `99.72%` and `97.2%` in the rural and urban settings.

## Limitations / parse caveats

All trajectories, timing, fidelity, and communication overhead come from simulation; the named RTX 4090 is training hardware, not a UAV test. Ground nodes are stationary, buildings are pre-known, unknown obstacles are sparse synthetic cells, control links are assumed LoS with sufficient bandwidth, and the maintenance stage is two-dimensional. Battery/propulsion constraints, inter-UAV separation, packet loss, sensing errors, and control-link/model-update latency are absent from the formulation. Moving-obstacle dynamics are not specified in the formulation or simulation setup, although the results prose says newly perceived obstacles can include moving objects. Several extracted equations have sign, action-count, target-network, or AoI-language inconsistencies, so they are not silently repaired. Publication metadata was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

The source applies [[digital-twin]] synchronization to online safety and policy maintenance rather than only state mirroring or offline optimization. It combines [[deep-q-network|value-based control]], [[uav-data-collection]], [[uav-trajectory-control]], and [[blockage-aware-channel-model|blockage-aware radio modeling]], while the ideal-PSO comparison keeps the learned controller's performance claim narrower than the abstract's broad wording.

## Raw artifacts

- Parse: `raw/sources/Deployment_Design_for_Multi-UAV-Assisted_IoT_Networks_A_Digital_Twin-Driven_Deep_Reinforcement_Learning_Approach/Deployment_Design_for_Multi-UAV-Assisted_IoT_Networks_A_Digital_Twin-Driven_Deep_Reinforcement_Learning_Approach.md`
- Origin PDF: `raw/sources/Deployment_Design_for_Multi-UAV-Assisted_IoT_Networks_A_Digital_Twin-Driven_Deep_Reinforcement_Learning_Approach/Deployment_Design_for_Multi-UAV-Assisted_IoT_Networks_A_Digital_Twin-Driven_Deep_Reinforcement_Learning_Approach.pdf`
- Figures: `raw/sources/Deployment_Design_for_Multi-UAV-Assisted_IoT_Networks_A_Digital_Twin-Driven_Deep_Reinforcement_Learning_Approach/images/`
