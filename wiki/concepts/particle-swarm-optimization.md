---
type: concept
title: "Particle Swarm Optimization (PSO)"
tags: [optimization, swarm-intelligence, metaheuristic]
related:
  - "[[guo-2026-dual-objective-multiuav-isac]]"
  - "[[wang-2025-acbft-uav-consensus]]"
  - "[[zhang-2024-uav-task-offloading-ddpg]]"
  - "[[albakhrani-2025-moalf-uav-mec]]"
  - "[[zhao-2026-heuristic-supervised-drl]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[zang-2026-uav-ev-priority-cav-speed]]"
  - "[[speed-coordinated-robust-optimization-control]]"
  - "[[heuristic-supervised-drl]]"
  - "[[whale-optimization-algorithm]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
  - "[[hua-2026-ddrl-content-delivery]]"
  - "[[uav-content-caching]]"
created: 2026-05-29
updated: 2026-07-13
---

# Particle Swarm Optimization (PSO)

A population-based metaheuristic in which candidate solutions ("particles") move through the search space guided by their own best-known position and the swarm's best-known position, balancing exploration and exploitation. It is simple, derivative-free, and handles non-convex/combinatorial objectives, which makes it popular as a sub-solver inside larger MEC schemes.

[[zhao-2026-heuristic-supervised-drl]] uses PSO as the upper-tier trajectory planner in a [[heuristic-supervised-drl]] loop, with a supervised bridge predicting candidate plan quality before MARL execution. [[beishenalieva-2026-secrecy-aware-uav-path-planning]] uses PSO as the lower-tier slot scheduler after a policy-gradient UAV controller chooses secure mobility and power actions. [[zang-2026-uav-ev-priority-cav-speed]] uses a dual-layer PSO for [[speed-coordinated-robust-optimization-control]], with the inner layer searching worst-case human lane-change timing and the outer layer choosing CAV speed-control decisions.

In this wiki PSO appears as: the chain-ordering optimizer in [[wang-2025-acbft-uav-consensus]]; an **improved PSO (IPSO)** for offloading decisions in [[zhang-2024-uav-task-offloading-ddpg]]; and **adaptive PSO (APSO)** as one ingredient of the integrated framework in [[albakhrani-2025-moalf-uav-mec]]. It sits alongside other metaheuristics like the [[whale-optimization-algorithm]] and [[multi-verse-optimizer]].

[[hua-2026-ddrl-content-delivery]] uses PSO at a different control layer: particles tune the popularity, object-size, and request-frequency weights of a [[uav-content-caching]] replacement score, while PPO handles UAV movement and transmission decisions.
