---
type: source
title: "Multi-Agent Deep Reinforcement Learning Based UAV Trajectory Optimization for Differentiated Services"
authors: ["Zhaolong Ning", "Yuxuan Yang", "Xiaojie Wang", "Qingyang Song", "Lei Guo", "Abbas Jamalipour"]
year: 2023
url: "https://doi.org/10.1109/TMC.2023.3312276"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, multi-uav-assisted-mec, uav-trajectory-control, task-offloading, nash-equilibrium, stochastic-game, maddpg, centralized-training-decentralized-execution]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[nash-equilibrium]]"
  - "[[stochastic-game]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[game-theoretic-offloading-formulations]]"
  - "[[chang-2022-marl-multiuav-trajectory]]"
  - "[[peng-2020-maddpg-uav-vehicular]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[bi-2025-sg-mapg]]"
  - "[[zhaolong-ning]]"
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[differentiated-uav-service-market]]"
created: 2026-06-02
updated: 2026-07-13
---

# Multi-Agent Deep Reinforcement Learning Based UAV Trajectory Optimization for Differentiated Services

## Citation

Ning, Z., Yang, Y., Wang, X., Song, Q., Guo, L., & Jamalipour, A. (2023). *Multi-Agent Deep Reinforcement Learning Based UAV Trajectory Optimization for Differentiated Services*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3312276. (Manuscript received 16 December 2022; revised 17 June 2023; accepted 1 September 2023; date of publication 5 September 2023; date of current version 4 April 2024 → year 2023.)

## TL;DR

Achieves **distributed trajectory control of multiple UAVs** in a UAV-assisted MEC network with **multiple service providers (SPs)** offering **differentiated services**, where ground users have **non-binary, time-varying service preferences** (each user prefers each service type with a probability summing to 1). The objective minimizes the **short-term computational cost of ground users** and the **long-term computational cost of UAVs** simultaneously, under incomplete information. The authors first analyze the interaction among SPs as a game on **complete** information, proving the **existence and uniqueness of the Nash Equilibrium (NE)**, then formulate a **Markov game** and propose a **multi-agent DRL** trajectory-optimization algorithm in which each SP executes its UAV's flying action from **local observations only** (no knowledge of other SPs' policies or users' preferences). The paper claims convergence, efficiency, scalability, and robustness over representative baselines.

## Problem framing

Most prior UAV-assisted MEC work simplifies the setting — single UAV, single SP, single service type, deterministic user offloading, cluster-based (rather than free-space) trajectories, complete system information, or a single-agent DRL controller — none of which matches a realistic multi-SP deployment. Two realities motivate this work: (i) users' service choices are **uncertain** and better modeled as probabilistic, time-varying preferences than as binary selections; and (ii) multiple commercial SPs (the paper cites Huawei/Nokia/Qualcomm 5G UAV services and the 5G PPP architecture white paper) each deploy their own UAVs to serve differentiated services over the same area. The goal is **decentralized** multi-UAV trajectory control under these conditions, where each SP plans from local observations.

## System model

- **Network.** $N$ ground users and $M$ SPs; each SP deploys one UAV (an aerial MEC server providing a specific service type) over a rectangular target area. A network operator (e.g. a BS) can observe global state and relay user requirements to SPs. Time is slotted; each user generates one task per slot.
- **Preferences & tasks.** User $i$'s service preference $l_{ij}(t) \in [0,1]$ for type $j$ (summing to 1 over types) is **non-binary** and time-varying; $l_{ij}(t)=1$ means fully offload to UAV $j$, and an interior value means a probabilistic offload. Task $\mathcal I_i(t) = \{D_i(t), F_i(t), \mathbf l_i(t)\}$ (data size, CPU cycles, preference vector).
- **Communication / computing / flying.** Uplink rate uses a LoS air-to-ground model $\propto \alpha P_i(t)/(H_j(t)^2 + R_{ij}(t)^2)$; inter-user interference is neglected (OFDMA/OMA justification). UAV compute energy $\propto \eta_j (f^C_j)^{\beta_j}$ with $\beta_j$ typically 3; result backhaul is neglected (negligible). UAVs move within bounded coordinates; recharging is not modeled (citing long-endurance hybrid-powered UAVs).
- **Objectives.** A **short-term** user computational-cost minimization and a **long-term** UAV computational-cost minimization, pursued simultaneously under incomplete information.

## Method

- **Game-theoretic analysis (complete information).** The interaction among SPs is studied as a game; the paper establishes the **existence conditions and proves the uniqueness of the Nash Equilibrium**, and solves the user and UAV cost-minimization problems at NE.
- **Markov game + multi-agent DRL (incomplete information).** The problem is recast as a **Markov game**, and a multi-agent DRL algorithm controls the trajectories of UAVs owned by different SPs **distributively**, requiring only **local observations** for each UAV's flying-action execution. Trajectories are **free-space** (continuous direction + distance), not cluster-based, and are re-planned per period as user preference patterns change. Convergence of the proposed algorithm is analyzed.

## Key findings

- Theoretical analysis and performance evaluation are reported to demonstrate **convergence, efficiency, scalability, and robustness**, with the proposed algorithm achieving the **lowest overall computational cost** versus representative algorithms. Specific numeric margins are figure-derived; treat exact values as indicative.
- Positions itself as the **first** study to realize distributed multi-UAV trajectory control in **multi-SP** scenarios with probabilistic, time-varying service preferences.

## Limitations / future work

The model neglects inter-user interference (leaning on OFDMA/OMA), neglects result backhaul, and does not model UAV recharging (assuming long-endurance UAVs, with recharging algorithms left as composable add-ons). The evaluation is simulation-based. Explicit future-work statements beyond these are `not in parse`.

## Relation to the corpus

A **multi-UAV-assisted MEC** entry distinctive for combining a **game-theoretic NE analysis** (complete information) with a **Markov-game multi-agent DRL** decentralized controller (incomplete information), and for its **non-binary, probabilistic user service preferences** across **multiple competing SPs** — a setting most multi-UAV-MEC papers omit. Its decentralized, local-observation execution is a [[centralized-training-decentralized-execution]]-style design and grounds [[stochastic-game]] (Markov game) and [[nash-equilibrium]]. It sits alongside the MADDPG multi-UAV trajectory works [[chang-2022-marl-multiuav-trajectory]], [[peng-2020-maddpg-uav-vehicular]], and the fairness-aware [[he-2023-fairness-3d-multiuav-maddpg]], and its NE/game framing connects to the hierarchical Stackelberg-game UAV-MEC scheme [[bi-2025-sg-mapg]]; the game-formulation contrast is catalogued in [[game-theoretic-offloading-formulations]].

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning_Based_UAV_Trajectory_Optimization_for_Differentiated_Services/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
