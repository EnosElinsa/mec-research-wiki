---
type: source
title: "Two-Level-Attention-Based Continuous Trajectory Design and Computation Offloading for Multi-UAV Cooperative Target Search"
authors: ["Haowen Zhu", "Junpeng Hui", "Zehua Guo"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3614596"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 3, pp. 3196-3214, Mar. 2026"
tags: [source, multi-uav-target-search, computation-offloading, mappo, attention, beta-policy, curriculum-learning, uav-charging]
related:
  - "[[attention-based-uav-target-search]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[beta-policy-drl]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-charging-scheduling]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[video-analytics-offloading]]"
created: 2026-07-07
updated: 2026-07-07
---

# Two-Level-Attention-Based Continuous Trajectory Design and Computation Offloading for Multi-UAV Cooperative Target Search

## Citation

Zhu, H., Hui, J., & Guo, Z. (2026). *Two-Level-Attention-Based Continuous Trajectory Design and Computation Offloading for Multi-UAV Cooperative Target Search*. **IEEE Transactions on Mobile Computing**, 25(3), 3196-3214. DOI: 10.1109/TMC.2025.3614596. DOI evidence appears in the local parse and was cross-checked against title-matched DOI metadata.

## TL;DR

Studies cooperative UAV target search in 3D continuous space, where UAVs choose flight, charging, image offloading, CPU-frequency allocation, and transmit power to reduce map uncertainty and improve target detection. HAB-MAPPO combines heuristic offloading/resource allocation with MAPPO, two-level attention, Beta-distribution continuous actions, a safe-flight controller, and curriculum learning for larger swarms.

## Problem

Many UAV-swarm search methods use fixed-altitude or discrete 2D motion and ignore how offloading location and compute-resource allocation affect search success. The paper asks how to jointly control 3D motion, charging, offloading, CPU frequency, and transmit power under partial observability, collision avoidance, energy limits, and search-time constraints.

## System model

The search area is gridded, and each UAV flies in 3D continuous space with altitude-dependent field of view and sensor fidelity. In each time slot, a flying subslot updates the UAV position, and an offloading subslot is used either for target search or laser charging. During search, the UAV camera captures an observation area, segments it into sub-observation images, and computes each image locally or offloads it to a BS. Completed recognition updates a Bayesian target-probability map; information entropy measures residual search uncertainty.

## Method

The joint problem, JOT-COFP, maximizes target-detection utility and environment-search efficiency over five decision groups: trajectory, charging, offloading, CPU-frequency allocation, and transmit-power allocation. HAB-MAPPO reduces the mixed action space by splitting the problem:

- MAPPO learns trajectory and charging actions under CTDE;
- HODRA heuristically decides image offloading and resource allocation from current position/channel state;
- a safe-flying controller enforces boundary and altitude safety without relying only on reward penalties;
- actor/critic networks use attention to handle local neighbor observations and variable swarm sizes;
- [[beta-policy-drl|Beta-policy]] sampling avoids truncation bias for bounded continuous actions;
- curriculum learning transfers policies from smaller to larger UAV swarms.

## Key findings

- Simulations report 27%-64% objective-function improvement versus existing MADRL and optimization methods.
- At 800000 training steps, HAB-MAPPO attains information uncertainty 0.28 and target-discovery proportion 0.76, with reported uncertainty reductions of 30% versus AM-MAPPO and 42% versus the discrete-action baseline; the parse truncates the final 64% comparison line but the abstract/contribution states the 27%-64% range.
- Under maximum sensor confidence 0.9, HAB-MAPPO reaches uncertainty 0.35 and target-discovery proportion 0.78; compared with Wo-priority, BLO, LBO, FO, and RO, it reduces uncertainty by 11%, 19%, 26%, 30%, and 61% and improves discovered targets by 8%, 14%, 20%, 44%, 78%, and 500% as reported in the parse.
- HODRA maintains about 80% task-offloading success in the reported task-offloading metric figure, while selecting energy-efficient local/BS execution and resource allocations.
- Adaptive charging extends search time: at 200 W laser charging power, the proposed algorithm gives 26% longer UAV search time than fixed charging in the parse.
- Two-level attention enables cross-scale transfer; direct deployment of an 8-UAV trained policy in the 11-UAV scenario reduces initial uncertainty by 56% versus orthogonal initialization, and fine-tuning reduces it from 0.4 to 0.3.

## Limitations / future work

The conclusion says the current framework focuses on static targets. Future work will extend it to dynamic targets through a hierarchical search-to-monitor process: first locating moving ground targets, then maintaining persistent tracking and monitoring.

## Relation to the corpus

This source creates [[attention-based-uav-target-search]] as a target-search counterpart to generic [[task-offloading]] and [[uav-trajectory-control]]. It is close to [[tang-2026-hg-maddpg-uav-rescue]] in low-altitude search behavior, but its novelty is the attention/MAPPO offloading-control architecture rather than rescue-area assignment and diffusion-enhanced MADDPG.

## Raw artifacts

- `raw/sources/Two-Level-Attention-Based Continuous Trajectory Design and Computation Offloading for Multi-UAV Cooperative Target Search/Two-Level-Attention-Based Continuous Trajectory Design and Computation Offloading for Multi-UAV Cooperative Target Search.md`
- Original PDF and extracted figures (`images/`) in the same folder.
