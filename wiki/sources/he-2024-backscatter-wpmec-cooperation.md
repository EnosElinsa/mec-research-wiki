---
type: source
title: "Energy Efficiency Maximization of Backscatter-Assisted Wireless-Powered MEC With User Cooperation"
authors: ["Yejun He", "Xinying Wu", "Zhou He", "Mohsen Guizani"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3243161"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, mobile-edge-computing, wireless-power-transfer, backscatter-communication, computation-offloading, fractional-programming-dinkelbach, convex-optimization]
related:
  - "[[mobile-edge-computing]]"
  - "[[wireless-power-transfer]]"
  - "[[backscatter-communication]]"
  - "[[rf-energy-harvesting]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[task-offloading]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[liu-2020-wpt-cooperative-uav-mec]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[chen-2025-swipt-mec-sac]]"
created: 2026-06-02
updated: 2026-06-02
---

# Energy Efficiency Maximization of Backscatter-Assisted Wireless-Powered MEC With User Cooperation

## Citation

He, Y., Wu, X., He, Z., & Guizani, M. (2024). *Energy Efficiency Maximization of Backscatter-Assisted Wireless-Powered MEC With User Cooperation*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3243161. (Manuscript received 23 September 2022; revised 16 December 2022; accepted 27 January 2023; date of publication 7 February 2023; date of current version 8 January 2024 → year 2024.)

## TL;DR

A **wireless-powered MEC (WPMEC)** scheme that combines **backscatter communication (BackCom)** and **active communication (AC)** with **user cooperation (UC)** to maximize **user energy efficiency (EE)**. The system has a **source node (SN)**, a **helper**, and a **hybrid access point (HAP)** integrated with MEC servers. Because the SN→HAP link is poor, the helper acts as a **relay** for the SN's computing tasks; both nodes can offload via either the passive (BackCom) or active (AC) mode. The paper maximizes the **user-centric** EE (excluding HAP energy) by jointly optimizing the backscatter reflection coefficient, AC transmit power, system time, and task allocation under minimum-computation-bits, channel-capacity, and energy constraints. A **fractional-programming (Dinkelbach-style)** transform plus variable substitution converts the non-convex problem to a convex one with **semi-closed-form** optimal solutions.

## Problem framing

WPMEC devices have small batteries; a HAP broadcasts RF energy that users harvest (energy harvesting) to power local computing and offloading. But a **double near-far effect** penalizes remote users (they harvest less yet must spend more to offload), motivating **user cooperation** where a near user relays a far user's data. Separately, **BackCom** offers low-energy passive transmission (modulating/reflecting an incident signal while harvesting energy for circuit power), while **AC** under harvest-then-transmit (HTT) gives a higher rate at higher energy — so combining them trades off EH against throughput. Prior work studied general WPMEC and backscatter-assisted WPMEC, but the **cooperation-assisted** WPMEC with integrated BackCom + AC, and specifically a **user-centric EE** objective, was under-explored.

## System model

- **Topology.** SN, helper, and a HAP with integrated MEC servers; the helper relays for the SN because of the poor SN→HAP link. Distances in the simulation: SN–helper 12 m, SN–HAP 30 m, helper–HAP 20 m; path-loss model $d^{-\alpha}$.
- **Transmission modes.** Each node can offload via **BackCom** (passive reflect-and-modulate, harvesting energy for circuit consumption) or **AC** (harvest-then-transmit). The time and the backscatter reflection coefficient split resources between the two modes.
- **Objective.** Maximize **user EE** (computation performance per user energy, deliberately excluding the grid-connected HAP's energy) by jointly optimizing the BackCom reflection coefficient, AC transmit power, system-time allocation, and task allocation, subject to minimum-computation-bits, channel-capacity, and energy(-causality) constraints.

## Method

- **Fractional transform.** The EE-maximization (a fractional objective) is transformed into an equivalent non-convex problem via a **fractional program** (Dinkelbach-style), then into a **convex** problem by **variable substitution** and convex-optimization techniques.
- **Closed-form structure.** Semi-closed-form expressions for the optimal solution are derived (including a mode-selection result: e.g., the SN chooses AC in certain regimes, with analogous conclusions for the helper).
- An **energy-efficiency maximization algorithm** then solves the convex problem; the paper reports it is computation-efficient.

## Key findings

- The proposed UC scheme with integrated BackCom + AC **significantly improves user EE** versus benchmark schemes (the paper compares against four alternatives) — its stated headline result.
- The scheme is **adaptive to the backscatter-vs-active trade-off**: above a backscatter-rate threshold (the parse cites $\zeta > -16$ dB) it allocates more time to BackCom, and at low $\zeta$ ($< -22$ dB) it works almost entirely in AC mode — so it is more flexible than fixed-mode baselines.
- EE behavior versus the minimum-computation-bits requirement $L_{min}$ is characterized (most schemes consume more energy as $L_{min}$ grows; the proposed scheme retains the highest EE). Specific margins are figure-derived; treat exact values as indicative.

## Limitations / future work

A small three-node (SN + helper + HAP) cooperation topology, evaluated by simulation; relies on a tractable EH/circuit model and known channels. Explicit future-work targets are `not in parse`.

## Relation to the corpus

A **wireless-powered MEC / energy** entry that extends the WPT-MEC anchor [[zhou-2018-uav-wireless-powered-mec]] and the idle-helper cooperative WPT-MEC of [[liu-2020-wpt-cooperative-uav-mec]] with a **backscatter + active hybrid** transmission design and a **user-centric EE** objective. Its Dinkelbach fractional-programming solver is the pattern in [[fractional-programming-dinkelbach]], and it sits beside the DRL-based WPT-MEC of [[zhu-2025-lycnn-drl-wpt-mec]] and the SWIPT-MEC of [[chen-2025-swipt-mec-sac]] in the energy-efficiency-and-WPT track. It introduces the corpus's [[backscatter-communication]] concept.

## Raw artifacts

- `raw/sources/Energy_Efficiency_Maximization_of_Backscatter-Assisted_Wireless-Powered_MEC_With_User_Cooperation/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
