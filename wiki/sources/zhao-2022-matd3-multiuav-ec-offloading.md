---
type: source
modeling_card: required
title: "Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing"
authors: ["Nan Zhao", "Zhiyang Ye", "Yiyang Pei", "Ying-Chang Liang", "Dusit Niyato"]
year: 2022
url: "https://doi.org/10.1109/TWC.2022.3153316"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav-assisted-mec, multi-agent-drl, matd3, task-offloading, trajectory-design, edge-cloud-collaboration]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-agent-td3]]"
  - "[[td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[energy-latency-tradeoff]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[chang-2022-marl-multiuav-trajectory]]"
created: 2026-05-29
updated: 2026-11-03
---

# Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing

## Citation

Zhao, N., Ye, Z., Pei, Y., Liang, Y.-C., & Niyato, D. (2022). *Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2022.3153316.

## TL;DR

A collaborative MEC system with **multiple UAVs and multiple edge clouds (ECs)** offloading user-equipment (UE) tasks. The goal is to minimize the sum of execution delays and energy consumptions by jointly designing UAV trajectories, computation-task allocation, and communication-resource management. Formulated as an MDP and solved with a cooperative **multi-agent DRL** framework; given the high-dimensional continuous action space, the **twin delayed DDPG (MATD3)** algorithm is used.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: UAVs $n$ act as relays and edge servers for UEs $m$ in hotspots and cooperate with terrestrial edge clouds (ECs) $k$. Each UE task is partitioned between the UAV and the ECs over G2A and A2G links, and the UAVs move in three dimensions.
**Problem & objective**: Problem (27) minimizes the total system cost $\sum_nU_n(t)$ with $U_n(t)=w_1E_n(t)+w_2T_n(t)$ (26), over UAV positions, task partition ratios, and UAV transmit power.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\boldsymbol\omega_n(t)$ | continuous 3-D | Location of UAV $n$ |
| Task partition at the UAV | $\gamma_{m0}^n(t)$ | continuous, $[0,1]$ | Share of UE $m$'s task computed at UAV $n$ |
| Task partition to ECs | $\gamma_{mk}^n(t)$ | continuous, $[0,1]$ | Share forwarded to EC $k$ |
| UAV transmit power | $P_n^t(t)$ | continuous, $[0,P_{\max}]$ | A2G forwarding power |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (27b)-(27d) | Partition shares in $[0,1]$ that sum to one, $\gamma_{m0}^n+\sum_k\gamma_{mk}^n=1$ |
| (27e) | UAV power $0\le P_n^t(t)\le P_{\max}$ |
| (27f) = (4)-(10) | Horizontal and vertical step limits, area bounds, and minimum separation between UAVs |
**Algorithm**: Re-model (27) as a multi-agent MDP. Each UAV runs a MATD3 actor on local observations, while centralized twin critics use clipped double-Q targets, target-policy smoothing, delayed actor updates, and replay.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied task offloading in collaborative multi-UAV and multi-edge-cloud mobile edge computing. They formulated weighted energy and delay minimization over UAV positions, task partition ratios between UAVs and edge clouds, and UAV transmit power under partition, power, and UAV movement constraints, then re-modeled it as a multi-agent MDP. Each UAV executes a local continuous actor while centralized twin critics train on joint state and actions. MATD3 uses clipped double targets, delayed actor updates, target-policy smoothing, and replay to stabilize the high-dimensional policy. Simulations report lower total system cost than MADDPG, MATD3 with fixed height or fixed power, edge-cloud-only offloading, and random schemes.

## Problem framing

UAVs serve as assisted edge clouds for large-scale, sparsely-distributed UEs, but have limited compute/energy. With multiple UAVs and ECs cooperating, the joint trajectory + task-allocation + resource-management problem is non-convex and high-dimensional.

## System model

- **Actors.** Multiple UAVs (assisted ECs) + multiple ECs serving UEs collaboratively.
- **Objective.** Minimize sum of execution delays + energy consumptions ([[energy-latency-tradeoff]]).
- **Decisions.** UAV trajectories, computation-task allocation, communication-resource management → MDP.

## Method

- A cooperative **multi-agent DRL** framework under CTDE; **MATD3** (twin delayed DDPG) handles the high-dimensional continuous action space ([[multi-agent-td3]], [[td3]]).

## Key findings

- The multi-UAV multi-EC offloading method adapts to UE mobility and changing communication/computation resources and task dynamics, and significantly reduces total system cost versus other optimization approaches (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established framework.

## Relation to the corpus

A core **MATD3 cooperative multi-UAV MEC** entry that sits with [[he-2023-fairness-3d-multiuav-maddpg]] (MADDPG, fairness) and [[chang-2022-marl-multiuav-trajectory]] (MARL trajectory/resource) in the multi-agent UAV-trajectory family, and shares the UAV+EC collaboration theme with [[yu-2020-uav-ec-collaborative-offloading]]. Reinforces [[multi-agent-td3]] and [[centralized-training-decentralized-execution]].

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing.md`
- Original PDF and extracted figures in the same folder.
