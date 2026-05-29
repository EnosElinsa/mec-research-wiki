---
type: source
title: "Double-Edge-Assisted Computation Offloading and Resource Allocation for Space-Air-Marine Integrated Networks"
authors: ["Zhen Wang", "Bin Lin", "Qiang Ye"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3561346"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, space-air-marine, computation-offloading, resource-allocation, leo-satellite, uav, alternating-optimization]
related:
  - "[[maritime-mec]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[you-2025-uncertain-maritime-hasac]]"
  - "[[wang-2024-twotier-satellite-marine]]"
created: 2026-05-29
updated: 2026-05-29
---

# Double-Edge-Assisted Computation Offloading and Resource Allocation for Space-Air-Marine Integrated Networks

## Citation

Wang, Z., Lin, B., & Ye, Q. (2025). *Double-Edge-Assisted Computation Offloading and Resource Allocation for Space-Air-Marine Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3561346.

## TL;DR

A computation-offloading scheme for **space-air-marine integrated networks (SAMINs)** where both UAVs and a LEO satellite carry edge servers. Maritime autonomous surface ships (MASSs) can offload partial workloads to UAVs *and* the LEO satellite concurrently via multi-access. The goal is to minimize SAMIN energy consumption under latency constraints by jointly optimizing offloading mode, offloading volume, and the computing-resource allocation of the UAVs and the LEO satellite. Solved by **alternating optimization (AO)** plus a layered decomposition into four sub-problems.

## Problem framing

Maritime IoT (MASSs with cameras, LiDAR, mmWave radar, IMU, GPS) generates large volumes of data needing real-time processing offshore, where ground infrastructure is absent. A "double-edge" (UAV + LEO) architecture provides over-the-air compute, but offloading mode, volume, and resource split must be optimized jointly to save energy under deadlines.

## System model

- **Actors.** MASSs (devices); UAVs with edge servers; one LEO satellite with an edge server.
- **Offloading.** Partial, multi-access — workload split across UAVs and LEO concurrently ([[binary-vs-partial-offloading]]).
- **Objective.** Minimize total SAMIN energy consumption subject to latency constraints.

## Method

- Formulate the energy-minimization problem, then **decompose via AO + a layered approach** into four sub-problems: offloading mode, offloading volume, UAV resource allocation, and LEO resource allocation; solve to obtain the (sub)optimal solutions ([[alternating-optimization-sdr-sca]]).

## Key findings

- Simulations validate effectiveness and efficiency versus benchmark algorithms (qualitative; specific energy-vs-parameter curves are in the paper).

## Limitations / future work

Optimization-based, static treatment. The authors flag AI/RL or predictive-analytics for dynamic resource allocation, and advanced (stochastic) MASS mobility models for collaborative trajectory planning, as future work.

## Relation to the corpus

Strengthens the **maritime MEC** track ([[wang-2026-aerial-marine-msar]], [[liu-2025-haps-uav-maritime-iot]], [[zhang-2024-dlrl-maritime-usv]], [[zhang-2025-three-tier-maritime-offloading]]) and the **SAGIN/satellite-offloading** thread. Its AO-decomposition contrasts with the DRL ([[you-2025-uncertain-maritime-hasac]]) and game-theoretic ([[wang-2024-twotier-satellite-marine]]) treatments of the same maritime-offloading problem — note all three share Bin Lin / Qiang Ye co-authorship. Reinforces [[alternating-optimization-sdr-sca]].

## Raw artifacts

- `raw/sources/Double-Edge-Assisted_Computation_Offloading_and_Resource_Allocation_for_Space-Air-Marine_Integrated_Networks/full.md`
- Original PDF and extracted figures in the same folder.
