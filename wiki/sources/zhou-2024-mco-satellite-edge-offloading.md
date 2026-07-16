---
type: source
modeling_card: required
title: "Mobility-Aware Computation Offloading in Satellite Edge Computing Networks"
authors: ["Jian Zhou", "Qi Yang", "Lu Zhao", "Haipeng Dai", "Fu Xiao"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3359759"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, leo-satellite-edge-computing, task-offloading, mobility-aware-offloading, alternating-direction-method-of-multipliers, leo-satellite-coverage-time, energy-latency-tradeoff, three-tier-cloud-edge-end]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[task-offloading]]"
  - "[[mobility-aware-offloading]]"
  - "[[alternating-direction-method-of-multipliers]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[energy-latency-tradeoff]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[non-terrestrial-network]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[zhang-2024-mhspo-satellite-peer-offloading]]"
  - "[[wang-2024-satellite-terrestrial-computing]]"
  - "[[zhang-2024-coma-satellite-offloading]]"
  - "[[you-2017-meco-resource-allocation]]"
created: 2026-06-02
updated: 2026-07-16
---

# Mobility-Aware Computation Offloading in Satellite Edge Computing Networks

## Citation

Zhou, J., Yang, Q., Zhao, L., Dai, H., & Xiao, F. (2024). *Mobility-Aware Computation Offloading in Satellite Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3359759. (Manuscript received 16 September 2023; revised 28 December 2023; accepted 23 January 2024; date of publication 29 January 2024; date of current version 3 September 2024 → year 2024.)

## TL;DR

Studies **mobility-aware computation offloading (MCO)** in a **satellite edge computing network (SECN)**, taking the **high-speed movement of LEO satellites** explicitly into account — which the authors present as the first such attempt. The three-layer SECN has GEO satellites as the cloud, LEO satellites (each with an MEC server) as edge nodes, and ground users as end-users; a task can be computed locally, on the accessible LEO satellite, on another LEO satellite via inter-satellite (L-L) relays, or on the GEO satellite. The objective minimizes a **weighted sum of network latency and energy consumption**. The problem is **discrete and non-convex** (binary offloading decisions), so it is **relaxed to a continuous convex problem** (proved feasible) and solved by **MCO-A**, an **ADMM-based distributed** algorithm designed to scale to many co-existing users, with a **convergence proof**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-layer satellite edge computing network uses GEO satellites as cloud centers, moving LEO satellites as edge servers connected by ring inter-satellite links, and ground users as end terminals. Each user reaches an accessible LEO over a large-scale plus Rician-fading uplink and can compute locally or route its task to an accessible LEO, another LEO, or a GEO server.

**Problem & objective**: MCO is a discrete non-convex offloading problem that minimizes normalized latency-energy cost, $\min_{\mathbf A}\lambda t'_{\mathrm{total}}+(1-\lambda)e'_{\mathrm{total}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading selection | $a_{i,m}$ | binary | Whether user $i$ selects execution option $m$ |
| Relaxed selection | $a'_{i,m}$ | continuous, $[0,1]$ | Convex relaxation used by the distributed solver |
| Local consensus copy | $\hat a_{i,m}^{k}$ | continuous, $[0,1]$ | Satellite-local copy of the offloading decision |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task selects at most one remote execution node; no remote selection means local execution |
| C2 | Original offloading entries satisfy $a_{i,m}\in\{0,1\}$ |
| C3 | Every LEO respects its computing-resource cap, $\sum_i a_{i,m}x_i\leq Z_m$ |
| C4 | Relaxed variables satisfy $0\leq a'_{i,m}\leq1$ and local ADMM copies agree with the global decision |

**Algorithm**: Model LEO coverage time and four mobility-dependent execution routes → relax binary decisions to a feasible convex program → split global and local variables through ADMM → update satellite-local and consensus variables with primal and dual residual checks → restore one-hot binary offloading by maximum relaxed value.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhou et al. [x] studied mobility-aware computation offloading in a satellite edge computing network with GEO cloud centers, moving LEO edge servers, and ground users. They formulated the MCO problem to minimize a weighted sum of normalized network latency and energy consumption using mobility-aware route costs and heterogeneous LEO computing-resource constraints. Binary choices allow local execution, processing at the accessible LEO, forwarding to another LEO, or offloading to a GEO satellite. The authors relaxed the discrete non-convex formulation into a continuous convex problem and developed MCO-A, a distributed ADMM-based solver with a convergence analysis and binary recovery. Experiments in small-scale and large-scale scenarios report lower latency and energy consumption than the evaluated baseline and state-of-the-art approaches.

## Problem framing

LEO satellites give low-latency edge service but have limited energy/compute/storage, move fast, and cover only a small, **constantly changing** ground area; GEO satellites have large payloads but high, unpredictable latency. Most prior SECN offloading work **assumes the LEO satellite is stationary** — an impractical assumption, because a satellite that processes a task may move away from the user before returning the result, inflating latency and hurting QoE. With many co-existing users contending for scarce LEO resources, the problem is also a scalability challenge. The paper therefore jointly considers **LEO mobility and heterogeneous resource constraints** to find practical offloading strategies that minimize latency and energy.

## System model

- **Three-layer SECN.** GEO layer (one GEO satellite as cloud, treated as static relative to ground); LEO layer (co-orbiting LEO satellites with MEC servers, connected in a ring via L-L inter-satellite links, and to GEO via G-L links); ground layer (users with local compute). Each ground area is covered by at least one LEO satellite; a user's nearest covering satellite is its **accessible** LEO satellite. User mobility is negligible relative to LEO motion and is ignored.
- **Coverage-time model.** Because LEO satellites move fast, the time $t^R_{i,\tilde m}$ that a user $i$ is covered by its accessible satellite is derived geometrically from orbit height, Earth radius, elevation angle, and satellite linear velocity — a hard bound on any offloading decision. The paper analyzes **four LEO-satellite mobility scenarios** affecting offloading.
- **Communication.** Uplink (U-L) rate uses large-scale + Rician fading; inter-satellite (L-L) and GEO-link (G-L) rates are treated as constants.
- **Latency & energy.** Latency decomposes into local, LEO-satellite (transmission + propagation + computation, including multi-hop L-L relays), and GEO-satellite components — propagation latency is **not** negligible given the long distances, though result-feedback transmission is neglected (results are small). Energy has local, LEO, and GEO components ($P \propto f^2$-style local energy, plus transmission energy).
- **Objective.** Minimize the **weighted total network latency + energy** ($\lambda$-weighted) over binary offloading decisions $a_{i,m}$, subject to LEO per-satellite resource caps and coverage-time/feasibility constraints.

## Method

- **Convex relaxation.** The discrete non-convex MCO problem (binary $a_{i,m}$) is converted into a **continuous convex problem** by relaxing the binary variables to $a'_{i,m}$, and the relaxation is **proved feasible**.
- **MCO-A (ADMM, distributed).** To avoid the high complexity of centralized optimization under large-scale co-existing user offloading, the paper designs **MCO-A**, a **distributed algorithm based on the alternating direction method of multipliers (ADMM)**, and **proves its convergence**.
- **Evaluation.** MCO-A is tested in both small-scale and large-scale scenarios against baseline and state-of-the-art approaches.

## Key findings

- MCO-A is reported to achieve **lower network latency and energy consumption, efficiently**, versus baseline and state-of-the-art methods across small- and large-scale experiments. Specific numeric margins are figure-derived; treat exact values as indicative.
- Framed as the **first** SECN offloading work to model the effect of LEO satellites' high-speed movement on the offloading decision (via the coverage-time model and four mobility scenarios).

## Limitations / future work

The evaluation is experimental/simulation-based, and several modeling simplifications are made for tractability (constant L-L and G-L rates, negligible user mobility, neglected result-feedback transmission latency, a single GEO satellite as cloud). The paper contrasts ADMM favorably against RL (longer training, poor large-scale scaling) and game theory (rising complexity, slow Nash-equilibrium attainment), positioning the distributed convex approach as more scalable. Future work is to include more specific factors such as inter-task dependencies, resource-allocation optimization, and collaboration among GEO satellites, and to investigate the latency impact of distributed algorithms.

## Relation to the corpus

A **LEO satellite edge computing** offloading entry distinguished by making **LEO mobility** first-class (its [[leo-satellite-coverage-time]] model and four mobility scenarios) and by using an **ADMM-based distributed** convex solver for large-scale co-existing users rather than DRL or game theory. Its three-layer GEO-cloud / LEO-edge / ground-end design is a satellite instance of [[three-tier-cloud-edge-end]], and it grounds [[alternating-direction-method-of-multipliers]] and [[mobility-aware-offloading]]. It sits beside other satellite-offloading entries: the energy-constrained Lyapunov DOS scheme [[cheng-2025-dos-satellite-edge-computing]], the multi-hop horizontal peer-offloading MHSPO [[zhang-2024-mhspo-satellite-peer-offloading]], the vertical GUE/SUE → BS/LEO offloading of [[wang-2024-satellite-terrestrial-computing]], and the COMA-based distributed-satellite offloading [[zhang-2024-coma-satellite-offloading]]. Its weighted latency-energy objective under a coverage/latency constraint echoes the threshold offloading policy of [[you-2017-meco-resource-allocation]], within the broader [[non-terrestrial-network]] context.

## Raw artifacts

- `raw/sources/Mobility-Aware_Computation_Offloading_in_Satellite_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
