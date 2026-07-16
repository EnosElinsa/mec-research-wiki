---
type: source
modeling_card: required
title: "Energy Efficient Resource Allocation in UAV-Enabled Mobile Edge Computing Networks"
authors: ["Zhaohui Yang", "Cunhua Pan", "Kezhi Wang", "Mohammad Shikh-Bahaei"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2927313"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav-assisted-mec, resource-allocation, task-offloading, edge-user-allocation, sum-power-minimization, location-optimization]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[edge-user-allocation]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[drone-cell-3d-placement]]"
  - "[[guo-2023-mccco-multiuav-5g-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[cunhua-pan]]"
created: 2026-06-01
updated: 2026-07-16
---

# Energy Efficient Resource Allocation in UAV-Enabled Mobile Edge Computing Networks

## Citation

Yang, Z., Pan, C., Wang, K., & Shikh-Bahaei, M. (2019). *Energy Efficient Resource Allocation in UAV-Enabled Mobile Edge Computing Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2019.2927313. (Manuscript received 20 February 2019; date of publication 16 July 2019; date of current version 10 September 2019; year 2019.)

## TL;DR

A multiple-UAV MEC network where ground UEs either compute locally or offload (binary, one UAV per UE) to a rotary-wing UAV server. The paper minimizes the **sum power of both UEs and UAVs** — communication, execution, and (critically) UAV **propulsion/mechanical power** — by jointly optimizing **user association**, **power control**, **computation-capacity allocation**, and **UAV location planning** (3-D position, altitude, and antenna half-power beamwidth) under per-task latency and per-UAV coverage/battery constraints. The nonconvex problem is solved by an iterative three-subproblem algorithm, with a **fuzzy c-means clustering** initializer to find a feasible starting point.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ ground UEs with binary local or offloaded tasks are served by $M$ hovering rotary-wing UAV MEC servers. Directional antenna beamwidth, altitude, coverage, LoS uplinks, CPU allocation, and propulsion power jointly determine system power and latency.

**Problem & objective**: A non-convex mixed allocation and placement problem minimizes total UE and UAV power, $\min P_{\mathrm{UE}}+P_{\mathrm{UAV}}$, including communication, computation, and UAV mechanical power.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UE-UAV association | $a_{i,j}$ | binary | UE $i$ computes locally or at UAV $j$ |
| UE transmit power | $p_i$ | continuous, bounded | Offloading power of UE $i$ |
| CPU allocation | $f_{i,j}$ | continuous, nonnegative | UAV CPU capacity assigned to UE $i$ |
| UAV position and altitude | $\mathbf q_j,H_j$ | continuous, bounded | Three-dimensional UAV placement |
| Antenna half-beamwidth | $\theta_j$ | continuous, bounded | Directional coverage angle of UAV $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each UE selects local computation or exactly one UAV |
| C2 | Local or offloaded execution meets the common latency limit |
| C3 | UE and UAV communication or computing power stay within budgets |
| C4 | Per-UAV CPU allocation and associated-UE count remain within capacity |
| C5 | Associated UEs lie in directional coverage, $R_{ij}\le H_j\tan\theta_j$ |

**Algorithm**: Initialize feasible UAV clusters with fuzzy c-means → approximate association cardinality by iteratively reweighted $\ell_1$ minimization and update associations → solve CPU allocation in closed form → search each UAV's position, altitude, and beamwidth in one dimension → alternate the three blocks until sum power converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yang et al. [x] studied energy-efficient resource allocation in multi-UAV mobile edge computing networks with binary task offloading. They formulated joint UE and UAV power minimization over user association, transmit power, computing capacity, three-dimensional UAV placement, and antenna beamwidth under latency, coverage, power, and capacity constraints. Their IACL algorithm approximates association cardinality by iteratively reweighted $\ell_1$ optimization, solves computing allocation in closed form, and updates placement and beamwidth by one-dimensional search. Fuzzy c-means clustering supplies a feasible initialization. Simulations report lower sum power than the evaluated fixed-altitude, fixed-beamwidth, and equal-computation-capacity baselines and performance close to exhaustive search in the tested small cases.

## Problem framing

Prior UAV-MEC work (the parse cites its references [39]–[41]) minimized only the total power of UEs and considered a **single** UAV, ignoring the UAV's own significant mechanical/propulsion power. This paper argues that, because UAVs are themselves power-constrained and propulsion power dominates, the objective should be the joint sum power of UEs and UAVs in a **multi-UAV** network, while also optimizing each UAV's altitude and directional-antenna beamwidth.

## System model

- **Actors.** $N$ UEs and $M$ rotary-wing hovering UAVs with directional antennas of adjustable half-power beamwidth $\theta_j$. Each UE has a task $U_i=(F_i,D_i,T)$ (CPU cycles, data size, shared latency requirement).
- **Offloading.** Binary — each UE executes locally or offloads to exactly one UAV ([[binary-vs-partial-offloading]]); the association indicator $a_{ij}$ enters an $\ell_0$-norm term for the number of associated UEs.
- **Channel.** LoS-dominated uplink with antenna gain inside the beamwidth cone; UAVs with overlapping coverage use orthogonal frequencies (no inter-UAV interference).
- **Power.** UE transmit + local-execution (CPU $\kappa f^\nu$) power; UAV computing power $s_j f_j^{w_j}$ plus a propulsion term $Q_j$ active whenever a UAV serves ≥1 UE.
- **Objective.** Weighted sum-power minimization subject to latency, UAV coverage ($R_{ij}\le H_j\tan\theta_j$), UE/UAV max-power, UAV compute-capacity, and max-associated-UE constraints.

## Method

An iterative joint-optimization algorithm (the parse labels the full scheme **IACL**) decomposing the nonconvex problem into three subproblems solved in turn:

1. **User association** — the nonsmooth $\ell_0$-norm is approximated by a sequence of weighted $\ell_1$-norm minimizations via **compressive sensing**, giving a closed-form update each iteration.
2. **Computation-capacity allocation** — decoupled into small problems with a **closed-form optimal** solution.
3. **Location planning** — optimal UAV position/altitude/beamwidth obtained by a **one-dimensional search**.

A **fuzzy c-means (FCM) clustering**-based algorithm supplies an initial feasible solution (the feasible set is nonconvex, so even a starting point is nontrivial).

## Key findings

- The proposed IACL converges quickly — about **three iterations** suffice in the convergence figure, where the initial solution (using all UAVs, high aggregate propulsion power) above 1000 W drops to roughly 420 W as the algorithm reduces the number of used UAVs (figure-read magnitudes; indicative, not asserted as exact).
- IACL beats the fixed-altitude/beamwidth **SCAFAH** baseline and the equal-capacity **ECC** baseline, and approaches the exhaustive **EXH** scheme, with the gap to EXH small at long latency (qualitative comparisons from the parse; specific curves are in the figures).
- Sum power decreases with the allowed maximal latency and increases with task data size, with IACL's growth slower than SCAFAH's thanks to its altitude/beamwidth optimization.

## Limitations / future work

The conclusion leaves UAV-enabled MEC networks where **UAVs are served as UEs** as future work. Offloading is binary and channels are assumed LoS-dominated with orthogonal-frequency UAVs (no inter-UAV interference).

## Relation to the corpus

A foundational **multi-UAV-MEC resource-allocation** entry whose distinguishing move is folding **UAV propulsion power** and **antenna beamwidth/altitude** into a joint sum-power objective. It complements the cooperative partial-offloading scheme [[guo-2023-mccco-multiuav-5g-offloading]] and the single-UAV Lagrangian/SCA design [[zhang-2019-uav-iot-comp-comm]], and its altitude/coverage placement connects to [[drone-cell-3d-placement]] and the clustering-based deployment idea in [[weighted-kmeans-uav-deployment]]. Shares co-author [[kezhi-wang]] with the Northumbria UAV-MEC group's trajectory papers.

## Raw artifacts

- `raw/sources/Energy_Efficient_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
