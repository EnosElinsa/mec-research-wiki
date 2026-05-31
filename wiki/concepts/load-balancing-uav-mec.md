---
type: concept
title: "Load Balancing in UAV-MEC"
tags: [fairness, load, swarm, uav, mec]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[energy-balancing-uav]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-06-01
---

# Load Balancing in UAV-MEC

Equalizing the **current compute load** across a UAV swarm so no single UAV becomes a bottleneck. A common penalty term in the optimization objective (or constraint) for multi-UAV-MEC.

Why this differs from [[energy-balancing-uav|energy balancing]]: load balancing addresses *throughput* (no UAV is overloaded *now*); energy balancing addresses *longevity* (no UAV runs out *first*). Both can be active in the same system, with different time horizons.

[[nabi-2025-jour-hierarchical-aerial]] adds a per-UAV load term (computed cycles ÷ compute capacity, Eq. 25a) to its reward and reports that the **average load per UAV** stays below its learning/heuristic baselines as the GU count grows (e.g. 0.30 vs 0.32–0.44 for GOUA+SAC/PPO/DDPG/HA at 30 GUs, Fig. 8). The matching algorithm (Gale-Shapley-inspired) used in its discrete stage also helps by capping the number of GUs each UAV can accept based on capacity.
