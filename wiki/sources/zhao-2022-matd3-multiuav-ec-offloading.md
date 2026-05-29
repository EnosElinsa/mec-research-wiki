---
type: source
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
updated: 2026-05-29
---

# Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing

## Citation

Zhao, N., Ye, Z., Pei, Y., Liang, Y.-C., & Niyato, D. (2022). *Multi-Agent Deep Reinforcement Learning for Task Offloading in UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2022.3153316.

## TL;DR

A collaborative MEC system with **multiple UAVs and multiple edge clouds (ECs)** offloading user-equipment (UE) tasks. The goal is to minimize the sum of execution delays and energy consumptions by jointly designing UAV trajectories, computation-task allocation, and communication-resource management. Formulated as an MDP and solved with a cooperative **multi-agent DRL** framework; given the high-dimensional continuous action space, the **twin delayed DDPG (MATD3)** algorithm is used.

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

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning_for_Task_Offloading_in_UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
