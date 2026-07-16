---
type: source
title: "Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing"
authors: ["Liang Wang", "Kezhi Wang", "Cunhua Pan", "Wei Xu", "Nauman Aslam", "Lajos Hanzo"]
year: 2021
url: "https://doi.org/10.1109/TCCN.2020.3027695"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
modeling_card: required
tags: [source, multi-uav-assisted-mec, multi-agent-drl, maddpg, trajectory-design, fairness-metrics, energy-latency-tradeoff, uav-trajectory-control]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[maddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[jains-fairness-index]]"
  - "[[wang-2022-cat-rat-fmec-trajectory]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[cunhua-pan]]"
  - "[[nauman-aslam]]"
created: 2026-05-31
updated: 2026-07-16
---

# Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing

## Citation

Wang, L., Wang, K., Pan, C., Xu, W., Aslam, N., & Hanzo, L. (2021). *Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2020.3027695. (Manuscript received April 18, 2020; date of publication September 29, 2020; date of current version March 8, 2021 → year 2021.)

## TL;DR

A multi-UAV-aided MEC framework where several UAVs with distinct trajectories fly over a target area to serve ground UEs. The paper **jointly optimizes geographical fairness among UEs, fairness of each UAV's UE-load, and overall UE energy consumption** — a mixed integer/continuous problem. A **multi-agent DRL** trajectory-control algorithm (one agent per UAV) using **MADDPG** manages each UAV's trajectory independently; given the trajectories, a **low-complexity approach** then sets UE offloading decisions. It reports advantages over traditional algorithms in UE-serving fairness, UE-load fairness, and energy consumption.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ UEs and $M$ fixed-altitude UAVs operate for $T$ slots. Each UE executes locally or offloads to one UAV while each UAV chooses a horizontal direction and travel distance.

**Problem & objective**: The mixed-variable objective $P_1=\max\sum_t\frac{f_t^u f_t^e}{\sum_{n,m}z_{n,m,t}E_{n,m,t}}$ rewards UAV-load fairness and UE geographical fairness while reducing UE energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Execution association | $z_{n,m,t}$ | binary | UE $n$ uses local mode $m=0$ or UAV $m$ in slot $t$ |
| Heading | $\alpha_{m,t}$ | continuous, $0\le\alpha_{m,t}\le2\pi$ | Horizontal movement direction of UAV $m$ |
| Travel distance | $d_{m,t}$ | continuous, $0\le d_{m,t}\le d^{\max}$ | UAV displacement in slot $t$ |
| CPU allocation | $f_{n,m,t}$ | continuous, nonnegative | Optional resource used in task completion and energy |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Binary association: $z_{n,m,t}\in\{0,1\}$ |
| C2 | One execution place per UE: $\sum_mz_{n,m,t}=1$ |
| C3 | Area bounds: $0\le X_{m,t}\le X^{\max}$ and $0\le Y_{m,t}\le Y^{\max}$ |
| C4 | Movement bounds: $0\le\alpha_{m,t}\le2\pi$ and $0\le d_{m,t}\le d^{\max}$ |
| C5 | Collision avoidance: $R_{m,m',t}\ge R^u$ |
| C6-C7 | Coverage and deadline: $z_{n,m,t}R_{n,m,t}\le R^{\max}$ and $z_{n,m,t}T_{n,m,t}\le T^{\max}$ |

**Algorithm**: Multi-agent MADDPG uses centralized training with decentralized execution for trajectory control; after trajectories are fixed, a low-complexity offloading and association step selects UE execution modes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] designed a multi-UAV MEC controller that combines geographical fairness among served UEs, fairness of UE loads across UAVs, and total UE energy. The formulation couples binary execution associations with continuous headings, travel distances, resource allocations, coverage, separation, and deadline constraints. A dedicated MADDPG agent controls each UAV under centralized training and decentralized execution, followed by a low-complexity offloading step for fixed trajectories. Simulations reported better fairness and energy performance than traditional trajectory baselines, while the model exposes the tradeoff between balanced service and battery use.

## Problem framing

UAVs as flexible aerial servers can establish LoS links and adapt position to dynamic environments. The objective explicitly combines two fairness notions — **geographical fairness** over served UEs and **UE-load fairness** across UAVs — with **UE energy minimization**, producing a high-dimensional mixed-variable problem unsuited to exhaustive/conventional methods. A decentralized, per-UAV agent design is motivated by the curse of dimensionality.

## System model

- **Actors.** Multiple UAVs (one DRL agent each) serving ground UEs.
- **Objective.** Jointly maximize geographical fairness of served UEs and UAV UE-load fairness while minimizing total UE energy consumption.
- **Variables.** Integer (e.g., associations/offloading) plus continuous (trajectory) variables.

## Method

- **MADDPG**-based trajectory-control algorithm: each UAV is controlled by a dedicated agent, trained under CTDE ([[centralized-training-decentralized-execution]]), building on the DQN→Double-DQN→DDPG lineage the parse reviews.
- **Low-complexity offloading step.** Given fixed UAV trajectories, a separate low-complexity approach optimizes UE offloading decisions (a trajectory-then-offloading decomposition).

## Key findings

- The proposed solution achieves "considerable performance over other traditional algorithms" on all three axes — UE-serving fairness, per-UAV UE-load fairness, and total UE energy (stated qualitatively in the parse; specific curves in the figures, not asserted here as exact).

## Limitations / future work

The parse leaves constrained UAV computing resources outside the low-complexity offloading step and notes that a matching algorithm could extend the model to that more practical setting. No explicit quantitative future-work targets are grounded in the captured parse.

## Relation to the corpus

A **MADDPG multi-UAV trajectory** entry by the Northumbria/QMUL/Southeast group ([[kezhi-wang]] corresponding). It is the **same research group** as [[wang-2022-cat-rat-fmec-trajectory]] (CAT/RAT, single twin-DQN agent) but is a **distinct earlier paper** — different venue (TCCN vs TMC), different DOI, a *multi-agent* MADDPG design, and an explicit **dual-fairness + energy** objective rather than pure energy minimization. Its dual fairness formulation links it to the [[fairness-metrics-in-mec]] hub and [[jains-fairness-index]], and it sits with [[he-2023-fairness-3d-multiuav-maddpg]] and [[seid-2021-madrl-multiuav-iot-edge]] in the MADDPG multi-UAV family.

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning-Based_Trajectory_Planning_for_Multi-UAV_Assisted_Mobile_Edge_Computing/full.md`
- Original PDF (`e5d7b673-bd11-43f2-8872-4ceddac8e9b5_origin.pdf`) and extracted figures (`images/`) in the same folder.
