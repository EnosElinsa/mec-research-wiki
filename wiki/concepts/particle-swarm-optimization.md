---
type: concept
title: "Particle Swarm Optimization (PSO)"
tags: [optimization, swarm-intelligence, metaheuristic]
related:
  - "[[wang-2025-acbft-uav-consensus]]"
  - "[[zhang-2024-uav-task-offloading-ddpg]]"
  - "[[albakhrani-2025-moalf-uav-mec]]"
  - "[[whale-optimization-algorithm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Particle Swarm Optimization (PSO)

A population-based metaheuristic in which candidate solutions ("particles") move through the search space guided by their own best-known position and the swarm's best-known position, balancing exploration and exploitation. It is simple, derivative-free, and handles non-convex/combinatorial objectives, which makes it popular as a sub-solver inside larger MEC schemes.

In this wiki PSO appears as: the chain-ordering optimizer in [[wang-2025-acbft-uav-consensus]]; an **improved PSO (IPSO)** for offloading decisions in [[zhang-2024-uav-task-offloading-ddpg]]; and **adaptive PSO (APSO)** as one ingredient of the integrated framework in [[albakhrani-2025-moalf-uav-mec]]. It sits alongside other metaheuristics like the [[whale-optimization-algorithm]] and [[multi-verse-optimizer]].
