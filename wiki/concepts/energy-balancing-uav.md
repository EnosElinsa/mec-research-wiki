---
type: concept
title: "Energy Balancing Across UAVs"
tags: [fairness, energy, multi-uav, swarm]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[load-balancing-uav-mec]]"
  - "[[huang-2023-mu-aec-task-energy]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-05-29
---

# Energy Balancing Across UAVs

A scheduling objective that minimizes the **disparity** in remaining energy across a UAV swarm, rather than the total energy consumed. The goal: keep all UAVs alive about as long as each other so the swarm degrades gracefully — losing one UAV early is far more disruptive than losing all UAVs at once.

Two formulations appear in the wiki:

- **Energy-balancing index** (sum of pairwise differences) — [[huang-2023-mu-aec-task-energy]] uses this in a CMOP alongside makespan.
- **Variance / max-min penalty in DRL reward** — [[nabi-2025-jour-hierarchical-aerial]] adds a load-balancing term to the SAC reward.

Different from **load balancing** ([[load-balancing-uav-mec]]) — load balancing equalizes *current* compute load; energy balancing equalizes *cumulative* energy expended. They're correlated but not identical (a UAV with a more efficient chip can run higher load with less energy).
