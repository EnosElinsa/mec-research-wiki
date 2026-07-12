---
type: source
title: "Joint Multi-Domain Resource Allocation and Trajectory Optimization in UAV-Assisted Maritime IoT Networks"
authors: ["Li Ping Qian", "Hongsen Zhang", "Qian Wang", "Yuan Wu", "Bin Lin"]
year: 2022
url: "https://doi.org/10.1109/JIOT.2022.3201017"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, maritime-mec, noma, computation-offloading, uav-trajectory-control, ddpg, energy-latency-tradeoff, fixed-wing-propulsion-energy-model]
related:
  - "[[maritime-mec]]"
  - "[[noma]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[ddpg]]"
  - "[[energy-latency-tradeoff]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[two-stage-decomposition]]"
  - "[[wang-2024-maritime-eh-jcora]]"
  - "[[dai-2023-hybrid-noma-fdma-marine]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[lyu-2023-noma-marine-emergency-offloading]]"
  - "[[wang-2026-noma-marine-data-computation]]"
  - "[[qian-wang]]"
  - "[[liping-qian]]"
  - "[[bin-lin]]"
  - "[[yuan-wu]]"
created: 2026-06-02
updated: 2026-07-13
---

# Joint Multi-Domain Resource Allocation and Trajectory Optimization in UAV-Assisted Maritime IoT Networks

## Citation

Qian, L. P., Zhang, H., Wang, Q., Wu, Y., & Lin, B. (2022). *Joint Multi-Domain Resource Allocation and Trajectory Optimization in UAV-Assisted Maritime IoT Networks*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2022.3201017. (Manuscript received 21 May 2022; revised 10 July 2022; accepted 15 August 2022; date of publication 23 August 2022; date of current version 22 December 2022 → year 2022.)

## TL;DR

A **NOMA-based UAV-assisted Maritime IoT (M-IoT)** MEC system in which **unmanned surface vehicles (USVs)** offload computation-intensive tasks via uplink power-domain **NOMA** (with SIC at the UAV) to a hovering **UAV-mounted MEC server**. The paper **minimizes total energy consumption** — USV transmission + USV/UAV computation + UAV propulsion — by jointly optimizing each USV's **offloaded workload ratio**, **transmit power**, **UAV compute-resource allocation**, and the **UAV trajectory**, subject to per-USV latency. The problem is mixed-discrete and non-convex (and NP-hard, since the trajectory part is TSP-equivalent), so it is solved by **vertical decomposition** into a **two-layered** algorithm: a top layer that learns the UAV trajectory via **deep deterministic policy gradient (DDPG)**, and an underlying layer that solves the multidomain resource allocation in closed form via the **Lagrange-multiplier** method. NOMA-enabled offloading is shown to reduce overall energy versus baselines.

## Problem framing

M-IoT (environmental, biological, tactical, aquaculture monitoring) increasingly uses USVs as floating IoT devices, but USVs have inflexible energy replenishment and limited spectrum, and offloading to distant onshore MEC incurs heavy transmission energy while local computing incurs heavy compute energy. A UAV acting as a **portable MEC unit** close to the USVs reduces both; NOMA lets many USVs share the same time-frequency resource in the power domain to relieve spectrum scarcity. The authors note that **total-energy minimization** for UAV-assisted M-IoT — across the joint power/time/computation/spatial domains — had not been studied, and that, unlike fixed terrestrial IoT, **drifting USVs** force the UAV to repeatedly update their locations before each decision.

## System model

- **Nodes.** One UAV (powerful MEC server, flying at fixed altitude H over duration T split into M slots) and N USVs $\mathcal{N}=\{1,\dots,N\}$, each able to compute simple tasks locally and assumed to report GPS locations to the UAV before each decision.
- **Communication.** Air-to-ocean LoS channel $h_{nm}=h_0/(\|U_m-q_{nm}\|^2+H^2)$; uplink **power-domain NOMA** with SIC ordered by descending channel gain (USVs with higher gain decoded first; lower-gain signals are co-channel interference).
- **Computation.** Each USV n has $B_n$-bit tasks split by offload ratio $\gamma_n\in[0,1]$; local compute time/energy use the per-cycle count $s_n$ and effective switched capacitance $l_n$ (energy $\propto C_{sn}^2$), and the UAV allocates compute resource $C_{an}$ (total $\le C_{\max}$) with energy $\propto C_{an}^2$.
- **UAV energy.** Propulsion energy uses a fixed-wing-style model $\hat{E}_f=\sum_m (\rho_1 v_m^3 + \rho_2/v_m)$ with $v_m$ derived from successive UAV positions.
- **Objective (OECM).** Minimize $\hat{E}_c + \sum_n (E_{tn}+E_{cn}) + \hat{E}_f$ (UAV compute + USV transmit/compute + UAV propulsion) subject to the offload-ratio bounds, NOMA-rate / offloaded-bits coupling, UAV velocity cap, USV power caps, and per-USV maximum execution latency $T_{\max}$. **Theorem 1** establishes NP-hardness (the trajectory subproblem is TSP-equivalent).

## Method

- **Equivalent transformation.** Problem (OECM) is reparameterized via per-USV SINR variables $x_{nm}$ into the tractable form (OECM-E), exposing the **hidden convexity** of the resource-allocation part under a fixed trajectory.
- **Vertical / two-layered decomposition.** The problem is split by domain: the **underlying layer** solves the multidomain resource allocation (offload ratio, transmit power, UAV compute allocation) in **closed form** via the **Lagrange dual method** and a gradient-descent idea, given the trajectory; the **top layer** optimizes the **UAV trajectory** with a **DDPG** agent built on top of the resource-allocation solver. The two layers alternate.

## Key findings

- Simulations validate the two-layered algorithm and show that **NOMA-enabled computation offloading reduces overall energy consumption** versus existing algorithms. A tunable **trade-off between time complexity and optimality** is observed by varying simulation parameters. Specific numeric margins are figure-derived; treat exact values as indicative.

## Limitations / future work

The evaluation is simulation-based; CSI/locations are assumed available (USVs report GPS before decisions). The paper notes it concludes with a discussion of future directions, but explicit future-work targets are otherwise `not in parse`.

## Relation to the corpus

A **maritime MEC** entry that pairs **uplink power-domain NOMA** offloading with a **DDPG-learned UAV trajectory** and a **closed-form Lagrangian** resource allocator — a clean instance of the [[two-stage-decomposition]] pattern (learn the hard combinatorial trajectory, solve the convex resource allocation analytically). It sits in the Dalian-Maritime-University / University-of-Macau maritime line with the energy-harvesting JCORA scheme [[wang-2024-maritime-eh-jcora]] and the hybrid NOMA/FDMA multi-access offloading [[dai-2023-hybrid-noma-fdma-marine]]; across those neighboring sources it shares [[liping-qian]], [[bin-lin]], and [[yuan-wu]]. It shares [[qian-wang]] as well as those three authors with [[wang-2026-noma-marine-data-computation]], which keeps the NOMA energy objective but replaces mobile-USV partial offloading with mandatory fixed-sensor data collection, UAV computation, and TD3 joint control. This source also complements the HAP-UAV maritime-IoT network [[liu-2025-haps-uav-maritime-iot]] and NOMA marine emergency offloading [[lyu-2023-noma-marine-emergency-offloading]]. Its [[fixed-wing-propulsion-energy-model]] propulsion term and **partial (ratio) offloading** ground [[fixed-wing-propulsion-energy-model]] and [[binary-vs-partial-offloading]], while NOMA-SIC offloading grounds [[noma]].

## Raw artifacts

- `raw/sources/Joint_Multi-Domain_Resource_Allocation_and_Trajectory_Optimization_in_UAV-Assisted_Maritime_IoT_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
