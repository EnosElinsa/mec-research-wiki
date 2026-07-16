---
type: source
modeling_card: required
title: "Energy Oriented Three-Tier Computation Offloading Scheme in Maritime Edge Computing Network"
authors: ["Hongxia Zhang", "Shiyu Xi", "Bodong Shang", "Peiying Zhang", "Sheng Wu", "Chunxiao Jiang"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3526213"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, leo-satellite-edge-computing, computation-offloading, minlp, three-tier, energy-efficiency]
related:
  - "[[maritime-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[zhang-2024-dlrl-maritime-usv]]"
created: 2026-05-29
updated: 2026-07-16
---

# Energy Oriented Three-Tier Computation Offloading Scheme in Maritime Edge Computing Network

## Citation

Zhang, H., Xi, S., Shang, B., Zhang, P., Wu, S., & Jiang, C. (2025). *Energy Oriented Three-Tier Computation Offloading Scheme in Maritime Edge Computing Network*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3526213.

## TL;DR

A **three-tier maritime edge computing** system where a LEO satellite and an offshore base station (OBS) provide communication/computing to maritime wireless devices (MWDs). It minimizes system energy under latency constraints by optimizing association, task partitioning, transmission power, and computing-resource allocation. Formulated as a **MINLP**, decomposed into four sub-problems with tailored solvers. Reported headline result: **39.3% system-energy savings** versus benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Maritime wireless devices process divisible tasks locally and through a three-tier architecture comprising an offshore base station and LEO satellites. A selected LEO provides the device uplink and can compute one task part or forward another part to the offshore base station.

**Problem & objective**: The mixed-integer nonlinear program jointly minimizes weighted local, LEO, and offshore-base-station energy, $\min_{\mathbf A,\mathbf P_k,\mathbf P_m,\mathbf L_S,\mathbf L_B,\mathbf F_S,\mathbf F_B}\sum_{k\in\mathcal K}e_k$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| LEO association | $a_{k,m}$ | binary, $\{0,1\}$ | Whether maritime device $k$ associates with satellite $m$ |
| Device and LEO powers | $p_k,p_m$ | continuous, nonnegative | Uplink and satellite-to-OBS transmit powers |
| Task partition | $l_k^S,l_k^B$ | continuous, nonnegative | Task bits computed at the LEO and at the OBS |
| LEO compute allocation | $f_{k,m}^S$ | continuous, nonnegative | Satellite CPU capacity assigned to device $k$ |
| OBS compute allocation | $f_k^B$ | continuous, nonnegative | Offshore-base-station CPU capacity assigned to device $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each device associates with at most one LEO: $\sum_m a_{k,m}\leq1$. |
| C2 | Transmit powers satisfy $p_k\leq P_k^{\max}$ and $p_m\leq P_m^{\max}$. |
| C3 | Offloaded partitions cannot exceed the task: $l_k^S+l_k^B\leq L_k$. |
| C4 | Aggregate satellite and OBS allocations satisfy their CPU-capacity limits. |
| C5 | Local, satellite, and OBS completion times each satisfy $t_k^L,t_k^S,t_k^B\leq T_k$. |

**Algorithm**: Relax and solve association with a slack variable, optimize transmission powers by quadratic transformation and a difference-of-convex procedure, derive feasible task-partition bounds and solve the convex partition block, update LEO and OBS computing resources by Lagrangian dual coordinate iteration, and alternate the four blocks to convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied energy-oriented computation offloading in a three-tier maritime edge computing system where LEO satellites and an offshore base station provide communication and computing services to maritime wireless devices. They formulated a MINLP that minimizes system energy by jointly optimizing satellite association, task partitioning, transmission power, and LEO and offshore computing-resource allocation under power, workload, capacity, and latency constraints. Their iterative solution uses a slack-variable association block, quadratic transformation and a difference-of-convex power block, convex task partitioning, and Lagrangian-dual computing-resource allocation. Simulation results report a 39.3% reduction in system energy consumption relative to the evaluated benchmark schemes.

## Problem framing

Large-scale MWDs run computation-intensive, resource-sensitive maritime IoT tasks, but have limited compute and energy. A LEO+OBS three-tier architecture supplies offshore compute; the challenge is to transmit and process tasks energy-efficiently under deadlines.

## System model

- **Tiers.** MWDs (device) → OBS (edge) → LEO satellite, a maritime [[three-tier-cloud-edge-end]] structure.
- **Decision variables.** Association variable, task partitioning, transmission power, computing-resource allocation.
- **Objective.** Minimize system energy consumption subject to latency constraints — a non-convex [[mixed-integer-nonlinear-programming|MINLP]].

## Method

Decompose the MINLP into four sub-problems:
1. **Association** — slack-variable method → convex.
2. **Transmission power** (MWDs + LEO) — quadratic transformation + difference-of-convex algorithm.
3. **Task partitioning** — derive upper/lower bounds on offloaded task size, then standard convex method.
4. **Joint computing-resource allocation** (LEO + OBS) — Lagrangian dual + coordinate transformation.

An iterative algorithm jointly optimizes all four to minimize system energy.

## Key findings

- The proposed algorithm **saves 39.3% of system energy consumption** compared to benchmark schemes (the paper's stated headline number).

## Limitations / future work

Simulation-based. Future work: complexity analysis, scaling/deployment factors (e.g., spectrum resources), dynamic satellite-marine scenarios, and UAV-assisted maritime edge computing.

## Relation to the corpus

A **maritime MEC** entry that, unlike the double-edge UAV+LEO scheme of [[wang-2025-double-edge-samin]], uses a LEO+OBS three-tier architecture and a fully optimization-based MINLP decomposition. Complements the DRL maritime work [[zhang-2024-dlrl-maritime-usv]] and the HAP-UAV maritime IoT study [[liu-2025-haps-uav-maritime-iot]]. Shares co-author Chunxiao Jiang with several aerial/space sources. Reinforces [[mixed-integer-nonlinear-programming]] and [[three-tier-cloud-edge-end]].

## Raw artifacts

- `raw/sources/Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network/Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network.md`
- Original PDF and extracted figures in the same folder.
