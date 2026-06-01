---
type: source
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
updated: 2026-06-02
---

# Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks

## Citation

Wang, Q., Chen, X., & Qi, Q. (2024). *Energy-Efficient Design of Satellite-Terrestrial Computing in 6G Wireless Networks*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2023.3334813. (Manuscript received 11 April 2023; revised 7 September and 14 November 2023; accepted 15 November 2023; date of publication 20 November 2023; date of current version 19 March 2024 → year 2024.)

## TL;DR

A joint design for **satellite-terrestrial computing** in 6G, where multiple terrestrial base stations (BSs) and LEO satellites — both equipped with MEC servers — cooperatively serve **ground user equipments (GUEs)** and **space user equipments (SUEs)**. The goal is to **minimize the weighted total energy consumption while meeting per-task delay requirements**, by jointly optimizing **offloading selection** (which BS/satellite serves a task), **receive beamforming**, and **resource allocation** (transmit power + MEC compute resources). The resulting NP-hard problem is decomposed into three subproblems and solved by an **alternating-optimization (AO)** algorithm: a **relaxation-mapping** method for offloading selection, and a combination of **closed-form solutions, convex approximation, and semidefinite relaxation (SDR)** for beamforming and resource allocation. Theory and simulation report fast convergence and superior performance over benchmarks.

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
