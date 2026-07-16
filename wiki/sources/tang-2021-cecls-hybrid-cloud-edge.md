---
type: source
title: "Computation Offloading in LEO Satellite Networks With Hybrid Cloud and Edge Computing"
authors: ["Qingqing Tang", "Zesong Fei", "Bin Li", "Zhu Han"]
year: 2021
url: "https://doi.org/10.1109/JIOT.2021.3056569"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
modeling_card: required
tags:
  - source
  - leo-satellite-edge-computing
  - computation-offloading
  - three-tier-cloud-edge-end
  - alternating-direction-method-of-multipliers
  - binary-vs-partial-offloading
  - leo-satellite-coverage-time
  - energy-latency-tradeoff
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[alternating-direction-method-of-multipliers]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[task-offloading]]"
  - "[[zhu-han]]"
  - "[[zhou-2024-mco-satellite-edge-offloading]]"
  - "[[zhang-2023-three-tier-satellite-offloading]]"
  - "[[wang-2024-satellite-terrestrial-computing]]"
  - "[[xie-2025-stin-delay-offloading]]"
created: 2026-06-03
updated: 2026-07-16
---

# Computation Offloading in LEO Satellite Networks With Hybrid Cloud and Edge Computing

## Citation
Qingqing Tang, Zesong Fei, Bin Li, Zhu Han, "Computation Offloading in LEO Satellite Networks With Hybrid Cloud and Edge Computing," *IEEE Internet of Things Journal*, 2021. DOI: 10.1109/JIOT.2021.3056569. (Manuscript received 2 Jan 2021; accepted 27 Jan 2021; date of publication 2 Feb 2021; date of current version 21 May 2021 → year 2021. Corresponding author: Zesong Fei. Beijing Institute of Technology + Nanjing University of Information Science and Technology + University of Houston / Kyung Hee University.)

## TL;DR
This paper proposes a **hybrid cloud and edge computing LEO satellite (CECLS)** network with a **three-tier** computation architecture — ground users, LEO-satellite MEC servers, and terrestrial cloud servers reachable through the satellites. It minimizes the **sum energy consumption of ground users** subject to each LEO satellite's **coverage-time** and **computation-capability** constraints, where each user's single, non-partitionable task is computed locally, at a LEO satellite, or at the cloud. The resulting discrete nonconvex (binary) problem is relaxed to a **linear program** via binary-variable relaxation and solved with a **distributed ADMM** algorithm that recovers binary decisions, achieving near-optimal energy with low complexity.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground users execute one indivisible computation task locally, at a LEO satellite MEC server, or at a terrestrial cloud reached through that satellite. Satellite contact time and onboard computing capacity limit the feasible offloading assignments.

**Problem & objective**: Problem (13) minimizes total ground-user energy, $\min_{\mathbf a,\mathbf b}\sum_i E_i$, including local CPU energy and uplink transmission energy, by selecting one execution tier for every user.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Satellite-edge offloading | $a_{i,m}$ | binary, $\{0,1\}$ | User $i$ sends its task to LEO satellite $m$ for execution |
| Cloud offloading | $b_{i,m}$ | binary, $\{0,1\}$ | User $i$ sends its task through satellite $m$ to the cloud |
| Local execution | $1-\sum_m(a_{i,m}+b_{i,m})$ | implied binary choice | User $i$ executes locally when no offloading option is selected |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 13b | Satellite compute capacity, $\sum_i a_{i,m}X_i\leq Z_m$ |
| 13c | At most one offloading destination per user, $\sum_m(a_{i,m}+b_{i,m})\leq1$ |
| 13d | Satellite or cloud processing finishes within satellite coverage time $T_m$ |
| 13e | Both offloading variables are binary |

**Algorithm**: Binary variables are relaxed to $[0,1]$, producing a convex linear program. Local copies and consensus constraints make the problem separable across satellites, after which distributed ADMM updates local variables, global variables, and dual variables before a recovery algorithm maps the relaxed solution back to binary assignments.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Tang et al. [x] proposed a three-tier computation architecture linking ground users, LEO satellite MEC servers, and terrestrial cloud servers. They minimized total user energy by choosing local, satellite-edge, or cloud execution for each indivisible task under satellite computing-capacity and coverage-time constraints. The binary nonconvex formulation was relaxed to a linear program and decomposed into a consensus form solved by distributed ADMM, followed by binary decision recovery. The authors established convergence for the relaxed convex problem and reported per-iteration complexity lower than the centralized interior-point alternative. In the evaluated user-count and elevation-angle sweeps, the ADMM solution closely matched the centralized offloading scheme and used less energy than satellite-or-local and local-only baselines.

## Problem framing
LEO satellite networks provide global coverage where terrestrial infrastructure is absent (mountains, oceans, disaster zones), but the long satellite-to-ground propagation delay strains real-time computation. Sinking MEC servers onto LEO satellites lets ground users offload directly to satellites, cutting end-to-end delay. The paper argues prior satellite-MEC work considered only **two-tier** networks (terrestrial/users + LEO satellites) and ignored the abundant **cloud** servers; and that work optimizing user energy ignored the **limited computation capability and coverage time** that characterize LEO satellites. It positions the three-tier cooperation of users, LEO edge nodes, and cloud as previously unstudied.

## System model
- **Network (Fig. 1):** M LEO satellites (each carrying a MEC server, e.g. a lightweight Docker platform) and I ground users in remote areas; satellites connect to terrestrial cloud servers over backhaul links and share information over inter-satellite links (ISLs), whose transfer delay is treated as negligible.
- **Coverage-time model:** a geometric earth/orbit relation (elevation angle θ, geocentric angle γ, orbit height h, satellite speed v_s) yields the maximum communication arc length L and the longest contact time T = L/v_s — this caps how long a user can use a given satellite (see [[leo-satellite-coverage-time]]).
- **Communication:** users share spectrum (mutual interference); uplink rate from user i to satellite m via the satellite-to-terrestrial link uses a Shannon expression with shadowed-Rician + large-scale fading channel gain. Downlink result-return delay is ignored (results ≪ input size).
- **Offloading decision:** binary vectors `a_{i,m}` (offload to satellite m) and `b_{i,m}` (offload to cloud via satellite m); each user takes at most one decision (Σ(a+b) ≤ 1), and total CPU-cycle demand on a satellite cannot exceed its capacity Z_m.
- **Computation models:** local (time X_i/f_i^L, energy ε(f_i^L)²X_i); LEO-satellite (propagation + transmission + compute delay, transmit energy p_i·D_i/R_{i,m}); cloud (adds a backhaul delay D_i/r). Offloading energy is the same whether the task lands at the satellite or the cloud (the user only pays for the uplink transmission).
- **Problem (13):** minimize total user energy over the binary offloading vectors subject to satellite compute caps (13b), one-decision-per-user (13c), and a coverage-time deadline on satellite/cloud processing (13d) — a **mixed discrete and nonconvex** (NP-hard) program.

## Method
- **Binary relaxation → LP:** the binary variables are relaxed to the continuous interval, transforming the discrete nonconvex problem into a linear program whose convexity the paper analyzes.
- **Distributed ADMM:** an [[alternating-direction-method-of-multipliers|ADMM]]-based distributed algorithm approximates the optimal solution with low computational complexity, plus a recovery procedure that maps the continuous solution back to binary offloading decisions. The paper also discusses convergence of the scheme.

## Key findings
Grounded in the abstract and contributions (magnitudes are figure-derived and treated as indicative):
- The proposed ADMM scheme **effectively reduces the total energy consumption of ground users** and is reported to outperform the benchmark algorithms in the simulations.
- Making use of the cloud tier (in addition to local + LEO-edge computing) gives users more offloading opportunities than the two-tier baselines summarized in the paper's comparison table.
- Explicitly honoring each LEO satellite's coverage-time and compute-capability limits is presented as what distinguishes the formulation from energy-only two-tier prior work.

## Limitations / future work
- Results are simulation-based; no on-orbit validation.
- Inter-satellite-link transfer delay is assumed negligible, simplifying multi-hop cooperation across the constellation.
- Tasks are atomic (non-partitionable) and each user has a single task, so partial offloading and multi-task scheduling are out of scope.
- The relaxation-then-rounding recovery is a suboptimal heuristic; the gap to the true binary optimum is not characterized analytically.

## Relation to the corpus
This is a satellite-edge offloading entry that sits with the corpus's other LEO-edge offloading designs. Architecturally it is a [[three-tier-cloud-edge-end|user/edge/cloud]] design with [[leo-satellite-edge-computing|LEO edge]] servers — the same three-tier split studied by [[zhang-2023-three-tier-satellite-offloading]] (UE/LEO-edge/ground-cloud partial offloading) — but here tasks are atomic and the solver is a binary-relaxation **LP + distributed ADMM**, which puts it alongside [[zhou-2024-mco-satellite-edge-offloading]] (also ADMM-distributed, but mobility-aware) rather than the DRL-based [[xie-2025-stin-delay-offloading]] or the receive-beamforming convex pipeline of [[wang-2024-satellite-terrestrial-computing]]. Its explicit [[leo-satellite-coverage-time|coverage-time]] deadline is the modeling feature it shares with the satellite track at large. Co-author [[zhu-han]] connects it to the corpus's broader aerial/edge optimization cluster.

## Raw artifacts
- Parse: `raw/sources/Computation_Offloading_in_LEO_Satellite_Networks_With_Hybrid_Cloud_and_Edge_Computing/full.md`
- Origin PDF: `raw/sources/Computation_Offloading_in_LEO_Satellite_Networks_With_Hybrid_Cloud_and_Edge_Computing/e05be22d-ce46-416b-8a40-8217f45f7995_origin.pdf`
- Figures: `raw/sources/Computation_Offloading_in_LEO_Satellite_Networks_With_Hybrid_Cloud_and_Edge_Computing/images/`
