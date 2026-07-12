---
type: source
title: "Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing"
authors: ["Zhaolong Ning", "Yuxuan Yang", "Xiaojie Wang", "Lei Guo", "Xinbo Gao", "Song Guo", "Guoyin Wang"]
year: 2023
url: "https://doi.org/10.1109/TMC.2021.3129785"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, uav-mec, task-offloading, server-deployment, stochastic-game, nash-equilibrium, dynamic-environment]
related:
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[stochastic-game]]"
  - "[[nash-equilibrium]]"
  - "[[potential-game]]"
  - "[[wang-2019-todetas-deployment-scheduling]]"
  - "[[pervez-2024-acm-multiuav-mec]]"
  - "[[zhaolong-ning]]"
created: 2026-07-07
updated: 2026-07-13
---

# Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing

## Citation

Ning, Z., Yang, Y., Wang, X., Guo, L., Gao, X., Guo, S., & Wang, G. (2023). *Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2021.3129785.

## TL;DR

Models a multi-UAV MEC network in which users decide whether to compute locally or offload to a UAV-MEC server, while UAVs choose hovering locations as mobile edge-server deployment decisions. The paper decomposes the system-wide computation-cost minimization into two stochastic games: one for user offloading and one for UAV location selection. Probability-based learning algorithms seek pure-strategy Nash equilibria for the two games, and a chess-like asynchronous update alternates between them.

## Problem framing

The paper argues that offloading and server deployment are tightly coupled: changing UAV locations changes user channel conditions and therefore offloading choices, while user offloading choices determine UAV computation load. It targets a dynamic environment in which users generate tasks with time-varying probabilities and the objective is to reduce a system-wide computation cost combining delay and energy terms.

## System model

- Multiple UEs and multiple UAVs operate over a discretized service area; each UAV hovers at one candidate location and acts as a UAV-MEC server.
- Each UE either computes locally or chooses one UAV for edge computing.
- UE tasks arrive probabilistically at each period, with per-UE task-generation probability.
- UE cost combines transmission/computation delay and energy; UAV cost combines average processing delay and edge-computing energy for the UEs it serves.
- A UAV availability response mechanism rejects overload by assigning zero computation capability to some UEs when a UAV's data threshold is exceeded, causing those UEs to fall back to local computing.

## Method

The optimization is split into two game layers:

- **UE computation-offloading game:** with UAV locations fixed, users select local computing or a UAV server. The paper shows the UE game is equivalent to a weighted potential game.
- **UAV location-selection game:** with user strategies fixed, UAVs select hovering locations. The paper transforms this game into an exact potential game.
- **Learning algorithms:** UEPSSL and UAVPSSL update strategy-selection probabilities using received rewards and are proved to converge to pure-strategy NE under the stated dynamic-game assumptions.
- **Chess-like asynchronous update:** alternates UE and UAV updates, accepting strategy profiles only when the system-wide computation cost improves.

## Key findings

- The proposed learning algorithms converge in the simulation setting, while a short-sighted updating baseline does not converge under the dynamic environment because it reacts to instantaneous utilities.
- In the Melbourne-CBD data-driven scenario, UAV-MEC with adaptive deployment lowers the system-wide computation cost relative to fixed edge-server placement; the parse reports a roughly 50% reduction against the fixed-EC baseline in its Fig. 9 discussion.
- The UAV-MEC result grows more gently with the number of UEs than the fixed-EC baseline, which the paper uses as evidence of robustness under scaling.
- Increasing UAV data thresholds reduces cost until the threshold is high enough to satisfy all UEs' edge-computing requests; beyond that point additional threshold does not improve performance in the studied scenario.

## Limitations / future work

The model discretizes UAV hovering locations and omits signaling overhead, bandwidth overhead, and downlink result transmission. The parse uses simulation over a real-world Melbourne CBD data source but does not report hardware deployment. Publication venue/year are verified by DOI metadata because the parse itself does not include a clean venue line.

## Relation to the corpus

This source adds a game-theoretic server-deployment counterpart to the UAV-MEC offloading line. It is closer to [[pervez-2024-acm-multiuav-mec]] than to pure DRL trajectory papers: both put game-theoretic offloading inside a broader optimization loop. It also complements [[wang-2019-todetas-deployment-scheduling]], which handles UAV deployment with differential evolution and task scheduling, by making deployment and offloading mutually reactive through stochastic games.

## Raw artifacts

- Parse: `raw/sources/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing.md`
- Origin PDF: `raw/sources/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing.pdf`
- Figures: `raw/sources/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing/images/`
