---
type: source
title: "Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism"
authors: ["Zexiong Wu", "Qiqi Xie", "Zhuoran Wang", "Xumin Huang", "Chaoda Peng", "Yuan Wu"]
year: 2026
url: "https://doi.org/10.1109/TVT.2025.3604250"
venue: "IEEE Transactions on Vehicular Technology"
tags: [source, uav, mec, urban, terrain-aware-channel, dem, b-spline-trajectory, multi-tasking-evolutionary, task-adaptive, cmop]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[terrain-aware-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[b-spline-trajectory]]"
  - "[[multi-tasking-evolutionary-algorithm]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[uav-trajectory-control]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-06-01
---

# Terrain-Aware UAV-Enabled MEC in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism

## Citation

Wu, Z., Xie, Q., Wang, Z., Huang, X., Peng, C., & Wu, Y. (2026). *Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3604250.

## TL;DR

UAV-MEC in dense urban environments where buildings *and* terrain elevation block air-to-ground signals. Two innovations:

1. **Terrain-aware channel model.** Builds on real-world Digital Elevation Model (DEM) data. For each user device, a *blocked region* is constructed by sweeping vectors from the UD outward to surrounding terrain mesh points; UAV positions inside that region see NLoS, outside see LoS. This captures rough topography that the standard sigmoid-LoS-probability model ignores.
2. **Joint optimization of UAV trajectory + destination + resource allocation** as a CMOP, with a **multi-tasking CMOEA** featuring a **task-adaptive mechanism** that retains historically-effective genetic operators per individual.

Objectives: G₁ = safe-flight metric (sum of inverse distances to nearby terrain meshes within a safety distance); G₂ = task completion time. Constraints encode altitude bounds, turning angle limits, and "above terrain" inequalities derived from triangulated mesh normals.

## Why this matters

This is the **terrain-aware** continuation of the Peng/Huang lineage seeded by [[peng-2022-cmop-uav-path-planning]]. Two specific advances over the seed:

- The seed paper uses a **synthetic terrain** (parameterized sinusoidal surfaces). This paper uses **real DEM data**. The blocked-region construction is geometric and explainable, where prior wiki entries either assumed simple statistical pathloss or required radio-map measurements ([[blockage-aware-channel-model]]).
- The single-population CMOEA in the seed evolves into a **multi-tasking** CMOEA here, where multiple co-evolving subtasks share an adaptively-selected pool of genetic operators. This is a methodologically distinct branch from the **dual-population** scheme in [[huang-2025-cmop-dispersed-computing]].

The **destination optimization** point is also new: previous trajectory-design papers fix the start and end positions and optimize the middle. Here the end position itself is a decision variable, because moving the destination by even a few meters in a dense city can be the difference between safe and crashed.

## Method highlights

- **Channel model.** DEM → 3D mesh; for each UD, identify the relevant mesh points and construct an LoS/NLoS *blocked region* via geometric sweep. UAV-to-UD path loss is then a function of the Euclidean distance from the UAV to that region.
- **B-spline trajectory.** λ control points; smooth path with low decision dimensionality.
- **Multi-tasking + task-adaptive.** Multiple related subtasks (different terrain configurations) co-evolve. A bandit-like mechanism tracks which genetic operators worked well historically and biases assignment for new individuals.

## Findings

- Terrain-aware channel model gives substantially more accurate path-loss predictions than statistical models in urban DEM scenarios — especially in valleys and behind ridges.
- The destination-as-decision-variable degree of freedom shortens both the safe path and the offloading time vs fixed-destination baselines.
- Multi-tasking CMOEA beats single-task CMOEA on both objectives.

## Limitations

- DEM data must be available — not always true in disaster scenarios where the terrain itself just changed.
- Quasi-stationary UDs; real urban users move (vehicles, pedestrians).
- Computational cost is high (multi-tasking population × evolutionary generations) — not real-time.

## Cross-link with related sources

- **Lineage:** [[peng-2022-cmop-uav-path-planning]] (seed) → [[peng-2024-energy-time-uav-its]] → [[huang-2025-cmop-dispersed-computing]] → [[huang-2023-mu-aec-task-energy]] → **this paper** (terrain-aware channel + destination optimization).
- **Channel modeling contrast:** statistical LoS probability ([[hsu-2025-drl-hues-hap-noma]], [[bao-2025-ddpg-video-offloading]]) vs DEM-geometric (this paper) vs measured-radio-map ([[jiang-2025-isac-lae-overview]] MBCM).
- **Trajectory class:** B-spline path planning, alongside [[peng-2022-cmop-uav-path-planning]]; contrast with the per-slot trajectory updates in [[liu-2026-jppo-en-convntm]].

## Raw artifacts

- `raw/sources/Terrain-Aware_UAV-Enabled_Mobile_Edge_Computing_in_Urban_Environments_A_Constrained_Multi-Objective_Approach_With_Task-Adaptive_Mechanism/full.md`
