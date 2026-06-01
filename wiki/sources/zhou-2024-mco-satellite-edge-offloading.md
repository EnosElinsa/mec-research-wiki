---
type: source
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
updated: 2026-06-02
---

# Mobility-Aware Computation Offloading in Satellite Edge Computing Networks

## Citation

Zhou, J., Yang, Q., Zhao, L., Dai, H., & Xiao, F. (2024). *Mobility-Aware Computation Offloading in Satellite Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3359759. (Manuscript received 16 September 2023; revised 28 December 2023; accepted 23 January 2024; date of publication 29 January 2024; date of current version 3 September 2024 → year 2024.)

## TL;DR

Studies **mobility-aware computation offloading (MCO)** in a **satellite edge computing network (SECN)**, taking the **high-speed movement of LEO satellites** explicitly into account — which the authors present as the first such attempt. The three-layer SECN has GEO satellites as the cloud, LEO satellites (each with an MEC server) as edge nodes, and ground users as end-users; a task can be computed locally, on the accessible LEO satellite, on another LEO satellite via inter-satellite (L-L) relays, or on the GEO satellite. The objective minimizes a **weighted sum of network latency and energy consumption**. The problem is **discrete and non-convex** (binary offloading decisions), so it is **relaxed to a continuous convex problem** (proved feasible) and solved by **MCO-A**, an **ADMM-based distributed** algorithm designed to scale to many co-existing users, with a **convergence proof**.

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

The evaluation is experimental/simulation-based, and several modeling simplifications are made for tractability (constant L-L and G-L rates, negligible user mobility, neglected result-feedback transmission latency, a single GEO satellite as cloud). The paper contrasts ADMM favorably against RL (longer training, poor large-scale scaling) and game theory (rising complexity, slow Nash-equilibrium attainment), positioning the distributed convex approach as more scalable. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **LEO satellite edge computing** offloading entry distinguished by making **LEO mobility** first-class (its [[leo-satellite-coverage-time]] model and four mobility scenarios) and by using an **ADMM-based distributed** convex solver for large-scale co-existing users rather than DRL or game theory. Its three-layer GEO-cloud / LEO-edge / ground-end design is a satellite instance of [[three-tier-cloud-edge-end]], and it grounds [[alternating-direction-method-of-multipliers]] and [[mobility-aware-offloading]]. It sits beside other satellite-offloading entries: the energy-constrained Lyapunov DOS scheme [[cheng-2025-dos-satellite-edge-computing]], the multi-hop horizontal peer-offloading MHSPO [[zhang-2024-mhspo-satellite-peer-offloading]], the vertical GUE/SUE → BS/LEO offloading of [[wang-2024-satellite-terrestrial-computing]], and the COMA-based distributed-satellite offloading [[zhang-2024-coma-satellite-offloading]]. Its weighted latency-energy objective under a coverage/latency constraint echoes the threshold offloading policy of [[you-2017-meco-resource-allocation]], within the broader [[non-terrestrial-network]] context.

## Raw artifacts

- `raw/sources/Mobility-Aware_Computation_Offloading_in_Satellite_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
