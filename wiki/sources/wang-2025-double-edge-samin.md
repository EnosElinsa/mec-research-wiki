---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Double-Edge-Assisted Computation Offloading and Resource Allocation for Space-Air-Marine Integrated Networks

## Citation

Wang, Z., Lin, B., & Ye, Q. (2025). *Double-Edge-Assisted Computation Offloading and Resource Allocation for Space-Air-Marine Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3561346.

## TL;DR

A computation-offloading scheme for **space-air-marine integrated networks (SAMINs)** where both UAVs and a LEO satellite carry edge servers. Maritime autonomous surface ships (MASSs) can offload partial workloads to UAVs *and* the LEO satellite concurrently via multi-access. The goal is to minimize SAMIN energy consumption under latency constraints by jointly optimizing offloading mode, offloading volume, and the computing-resource allocation of the UAVs and the LEO satellite. Solved by **alternating optimization (AO)** plus a layered decomposition into four sub-problems.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Maritime autonomous surface ships split computation workloads between nearby UAV edge servers and a LEO satellite, using multi-access offloading and separate UAV and satellite compute resources.

**Problem & objective**: The double-edge formulation minimizes total system energy, $\min_{\mathbf a,\mathbf s,\boldsymbol\rho^U,\boldsymbol\rho^L}E^{tot}$, under latency and resource limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading mode | $a_{mn}$ | continuous ratio, $[0,1]$ | Fraction of MASS task sent to UAV or satellite |
| Offloading volume | $s_{mn}$ | continuous, $[0,S_{mn}]$ | Uploaded workload volume |
| UAV compute allocation | $\rho_{mn}^U$ | continuous, nonnegative | Resource assigned by UAV $m$ to task $n$ |
| LEO compute allocation | $\rho_{mn}^L$ | continuous, nonnegative | Resource assigned by the LEO satellite |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Offloading ratio is bounded: $0\leq a_{mn}\leq1$. |
| C2 | Uploaded workload cannot exceed the task: $0\leq s_{mn}\leq S_{mn}$. |
| C3 | Total task and satellite latency meet their limits: $T_{mn}^{tot}\leq T_{mn}^{max}$ and $t_{mn}^L+T_{mn}^L\leq T^{max}$. |
| C4 | MASS-UAV distance is bounded: $\lVert\mathbf q_m-\mathbf q_{mn}\rVert\leq d^{max}$. |
| C5 | UAV and satellite compute capacities are bounded by $\rho_m^{max}$ and $\rho_{max}^L$. |
| C6 | UAV and satellite transmit powers and energy budgets remain within their maxima. |

**Algorithm**: Optimize offloading mode and volume with a multi-round iterative search, then solve UAV and LEO compute allocations with convex or KKT subproblems inside a layered alternating-optimization framework.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] study double-edge computation offloading for maritime devices served concurrently by UAVs and a LEO satellite. Their energy-minimization problem jointly chooses offloading ratios, uploaded volumes, and UAV and satellite compute allocations under workload, latency, distance, capacity, power, and energy constraints. A multi-round iterative search handles offloading mode and volume, while convex and KKT allocation blocks form the layered alternating-optimization solution. Numerical experiments show convergent offloading and resource updates and lower energy than paired, equal-offloading, and other benchmark schemes.

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
