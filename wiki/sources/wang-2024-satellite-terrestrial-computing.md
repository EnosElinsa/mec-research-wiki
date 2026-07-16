---
type: source
modeling_card: required
title: "Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks"
authors: ["Qi Wang", "Xiaoming Chen", "Qiao Qi"]
year: 2024
url: "https://doi.org/10.1109/TCOMM.2023.3334813"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, leo-satellite-edge-computing, satellite-terrestrial-computing, computation-offloading, beamforming-design, noma, alternating-optimization, non-terrestrial-network]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[task-offloading]]"
  - "[[noma]]"
  - "[[free-space-optical-isl]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zhang-2024-mhspo-satellite-peer-offloading]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[ao-sdr-sca-convex-pipeline]]"
created: 2026-06-02
updated: 2026-07-16
---

# Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks

## Citation

Wang, Q., Chen, X., & Qi, Q. (2024). *Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2023.3334813. (Manuscript received 11 April 2023; revised 7 September and 14 November 2023; accepted 15 November 2023; date of publication 20 November 2023; date of current version 19 March 2024 → year 2024.)

## TL;DR

A joint design for **satellite-terrestrial computing** in 6G, where multiple terrestrial base stations (BSs) and LEO satellites — both equipped with MEC servers — cooperatively serve **ground user equipments (GUEs)** and **space user equipments (SUEs)**. The goal is to **minimize the weighted total energy consumption while meeting per-task delay requirements**, by jointly optimizing **offloading selection** (which BS/satellite serves a task), **receive beamforming**, and **resource allocation** (transmit power + MEC compute resources). The resulting NP-hard problem is decomposed into three subproblems and solved by an **alternating-optimization (AO)** algorithm: a **relaxation-mapping** method for offloading selection, and a combination of **closed-form solutions, convex approximation, and semidefinite relaxation (SDR)** for beamforming and resource allocation. Theory and simulation report fast convergence and superior performance over benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple terrestrial base stations and LEO satellites carry MEC servers for single-antenna ground and space user equipments, with NOMA uplinks, receive beamforming, inter-satellite optical links, and indivisible tasks.

**Problem & objective**: The MINLP minimizes weighted total energy under task delays, $\min_{\alpha,\beta,\gamma,\mathbf w,\mathbf v,\mathbf p,\mathbf q,\mathbf f}\sum_k\rho_k^g(E_k^{g-g}+E_k^{g-s})+\sum_l\rho_l^sE_l^{s-s}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| GUE offloading selection | $\alpha_{k,m},\beta_{k,n}$ | binary | Select a terrestrial BS or LEO satellite for GUE $k$ |
| SUE offloading selection | $\gamma_{l,n}$ | binary | Select a LEO satellite for SUE $l$ |
| Receive beamforming | $\mathbf w_{k,m},\mathbf v_{k,n}$ | complex vectors, unit norm | BS and satellite receive beamformers |
| Transmit powers | $p_k,q_l$ | continuous, nonnegative and bounded | GUE and SUE powers |
| MEC resources | $f_{k,m}^{gro},f_{k,n}^{sat-g},f_{l,n}^{sat-s}$ | continuous, nonnegative | Compute allocation at BSs and satellites |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Per-task delay bounds: $T_k^{g-g}+T_k^{g-s}\leq Z_k^g$ and $T_l^{s-s}\leq Z_l^s$. |
| C2 | BS and satellite compute capacities are not exceeded. |
| C3 | Offloading indicators are binary and each GUE chooses at most one BS or satellite; each SUE chooses one satellite. |
| C4 | User transmit powers obey $0\leq p_k\leq P_k^{max}$ and $0\leq q_l\leq Q_l^{max}$. |
| C5 | Receive beamformers are normalized: $\lVert\mathbf w_{k,m}\rVert^2=\lVert\mathbf v_{k,n}\rVert^2=1$. |

**Algorithm**: Alternate offloading selection, beamforming, and resource-allocation subproblems; use relaxation mapping and branch-and-bound for binary selection, closed-form or convex approximations for powers and resources, and SDR with SCA for beamforming.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] formulate satellite-terrestrial MEC as a joint offloading, beamforming, and resource-allocation problem for ground and space users. The MINLP minimizes weighted energy under per-task delays, server capacities, one-node selection, power budgets, and unit-norm receive beamformers. Their alternating-optimization pipeline combines relaxation mapping, branch-and-bound, convex approximation, and semidefinite relaxation across the coupled subproblems. The algorithm converges within about five iterations in the reported setting and consumes less weighted energy than the five comparison algorithms over the tested delay range.

## Problem framing

5G/terrestrial MEC covers only a small fraction of the globe; oceans, deserts, and remote regions lack access. LEO satellites with onboard MEC servers can both extend coverage and add compute when terrestrial servers are overloaded in dense areas. Prior satellite-terrestrial work focuses largely on the communication link (channel modeling, NOMA, RIS, mmWave) or on terrestrial offloading; what is missing is a unified framework that coordinates wireless **and** computing resources across multiple node types, accounts for **inter-satellite communication and space resource sharing**, and serves both ground and space terminals. This paper targets that gap.

## System model

- **Nodes.** M BSs (each with $N_t^g$ antennas) and N LEO satellites (each with $N_t^s$ antennas), both carrying MEC servers; K single-antenna GUEs and L single-antenna SUEs. Each GUE/SUE has one **indivisible** task offloaded to a server (binary offloading-selection variables $\alpha_{k,m}, \beta_{k,n}, \gamma_{l,n}$). A GUE picks at most one BS or LEO satellite; an SUE selects one satellite from an N-option cluster.
- **Three-stage offloading.** Uplink raw-data transmission → decoding + MEC computation → result return (the return stage's delay/energy is neglected since result data is small).
- **Channels.** Terrestrial-to-terrestrial (Rayleigh small-scale + distance path loss, **NOMA uplink with SIC** and receive beamforming); terrestrial-to-satellite (LEO channel with large-scale fading, rain attenuation, satellite antenna gain, Doppler — NOMA + Doppler compensation + SIC); satellite-to-satellite (**free-space optical (FSO)** inter-satellite link). CSI is assumed available and constant within a slot, fading independently across slots.
- **Computing model.** Per-task execution time and energy split into transmission, propagation (for the long satellite links), and computation components; MEC compute energy uses the standard $\propto f^2$ frequency model with a chip-architecture energy coefficient.
- **Objective.** Minimize $\sum_k \rho_k^g (E_k^{g\text{-}g}+E_k^{g\text{-}s}) + \sum_l \rho_l^s E_l^{s\text{-}s}$ (weighted total energy) subject to per-task delay bounds and per-server compute-capacity constraints.

## Method

- **Decomposition.** The NP-hard joint problem is split into three subproblems — offloading selection, beamforming design, and resource allocation — solved iteratively by **alternating optimization** until the objective converges (Algorithm 1).
- **Offloading selection.** Exhaustive search is intractable, so the 0-1 selection variables are relaxed to $[0,1]$ and recovered by a **relaxation-mapping** method that trades optimality for lower complexity.
- **Beamforming.** Reformulated via auxiliary variables and **SDR** ($\mathbf{W}_{k,m}=\mathbf{w}_{k,m}\mathbf{w}_{k,m}^H$) into a convex form.
- **Resource allocation.** Power and compute-resource allocation handled by **closed-form solutions and convex-approximation** techniques.
- The framework is positioned as suitable for **dynamic** satellite-terrestrial networks: topology/channels are treated as static within a slot and re-solved per slot.

## Key findings

- Both **theoretical analysis and simulation** confirm **fast convergence** of the proposed AO algorithm and **superior performance** (lower weighted total energy under the delay constraints) versus benchmark schemes — the paper's stated results. Specific numeric margins are figure-derived, so treat exact values as indicative.

## Limitations / future work

CSI is assumed perfectly known and slot-static; tasks are indivisible (no partial offloading); result-return cost is neglected. The evaluation is simulation-based. Explicit future-work targets beyond the proposed framework are `not in parse`.

## Relation to the corpus

A **satellite-terrestrial / SAGIN computing** entry that, unlike the horizontal [[zhang-2024-mhspo-satellite-peer-offloading|multi-hop peer offloading]] and the energy-constrained single-tier [[cheng-2025-dos-satellite-edge-computing]], frames a **vertical** GUE/SUE→BS/LEO offloading problem with explicit **receive beamforming** and **NOMA-SIC** uplinks. Its AO + SDR + convex-approximation solver is the classical-optimization pattern catalogued in [[ao-sdr-sca-convex-pipeline]], and its double-tier (terrestrial + LEO) compute substrate parallels [[wang-2025-double-edge-samin]]. It shares the [[free-space-optical-isl]] inter-satellite substrate with the satellite track and grounds [[leo-satellite-edge-computing]] / [[non-terrestrial-network]] from the energy-minimization-with-beamforming angle.

## Raw artifacts

- `raw/sources/Energy-Efficient_Design_of_Satellite-Terrestrial_Computing_in_6G_Wireless_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
