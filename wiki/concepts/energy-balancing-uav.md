---
type: concept
title: "Energy Balancing Across UAVs"
tags: [fairness, energy, multi-uav, swarm]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[load-balancing-uav-mec]]"
  - "[[huang-2023-mu-aec-task-energy]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[zhang-2026-distributed-jscc-uav-video]]"
  - "[[li-2016-energy-balanced-uav-relaying]]"
  - "[[energy-balanced-cooperative-uav-relaying]]"
created: 2026-05-29
updated: 2026-07-13
---

# Energy Balancing Across UAVs

A scheduling objective that minimizes the **disparity** in energy expended across a UAV swarm, rather than the total energy consumed. The goal: keep all UAVs alive about as long as each other so the swarm degrades gracefully — one UAV dying early mid-mission is more disruptive than the swarm reaching end-of-life together.

In the wiki, [[huang-2023-mu-aec-task-energy]] makes this an explicit CMOP objective alongside makespan: an **energy-balancing index** $G_2 = \sum_j \left((TE_j - \overline{TE})/\psi\right)^2$ — the sum of squared normalized deviations of each UAV's total energy $TE_j$ from the swarm mean $\overline{TE}$ (ψ a reference value; Eq. 13), minimized to prevent the sudden departure of high-drain UAVs.

Different from **load balancing** ([[load-balancing-uav-mec]]) — load balancing equalizes *current* compute load; energy balancing equalizes *cumulative* energy expended. They're correlated but not identical (a UAV with a more efficient chip can run higher load with less energy). [[nabi-2025-jour-hierarchical-aerial]] sits on the load-balancing side: it adds a per-UAV **load** term (computed cycles ÷ compute capacity, Eq. 25a) to its SAC reward — equalizing instantaneous load rather than cumulative energy.

[[li-2016-energy-balanced-uav-relaying]] uses the min-max form for radio forwarding: it allocates decoded packets, rates, and powers so the most heavily drained relay is reduced. Its metric excludes propulsion energy, so it establishes packet-scheduling balance rather than whole-aircraft energy balance.
