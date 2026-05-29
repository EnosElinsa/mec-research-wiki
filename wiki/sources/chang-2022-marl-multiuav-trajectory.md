---
type: source
title: "Trajectory Design and Resource Allocation for Multi-UAV Networks: Deep Reinforcement Learning Approaches"
authors: ["Zheng Chang", "Hengwei Deng", "Li You", "Geyong Min", "Sahil Garg", "Georges Kaddoum"]
year: 2022
url: "https://doi.org/10.1109/TNSE.2022.3171600"
venue: "IEEE Transactions on Network Science and Engineering (IEEE TNSE)"
tags: [source, multi-uav-assisted-mec, aerial-base-station, trajectory-design, resource-allocation, multi-agent-drl, user-association]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
created: 2026-05-29
updated: 2026-05-29
---

# Trajectory Design and Resource Allocation for Multi-UAV Networks: Deep Reinforcement Learning Approaches

## Citation

Chang, Z., Deng, H., You, L., Min, G., Garg, S., & Kaddoum, G. (2022). *Trajectory Design and Resource Allocation for Multi-UAV Networks: Deep Reinforcement Learning Approaches*. **IEEE Transactions on Network Science and Engineering**. DOI: 10.1109/TNSE.2022.3171600.

## TL;DR

DRL-based trajectory design + resource allocation for a **multi-UAV communications** system where UAVs act as aerial base stations providing ubiquitous coverage. The objective is to maximize system utility over all served ground users (GUs) through a joint user-association, power-allocation, and trajectory-design problem. The authors propose a machine-learning strategic resource-allocation algorithm (combining RL + deep learning) and a **multi-agent DRL** scheme for distributed implementation without prior knowledge of network dynamics.

## Problem framing

Future mobile systems need ubiquitous connectivity over billions of devices; UAVs as flexible, low-cost aerial base stations help. The joint user-association + power-allocation + trajectory problem has a high-dimensional state space, motivating learning-based solutions, including a decentralized variant.

## System model

- **Actors.** Multiple UAVs as aerial base stations serving ground users.
- **Objective.** Maximize system utility over all served GUs.
- **Decisions.** User association, power allocation, trajectory design.

## Method

- A **machine-learning-based strategic resource-allocation algorithm** combining reinforcement learning and deep learning to design the optimal policy of all UAVs.
- A **multi-agent DRL** scheme for decentralized implementation without a-priori knowledge of network dynamics ([[multi-agent-td3]] family / [[centralized-training-decentralized-execution]]).

## Key findings

- Extensive simulations demonstrate advantages of the proposed schemes over baselines (qualitative; specific utility curves in the paper).

## Limitations / future work

Future work: improve multi-UAV system performance via energy-efficiency and delay optimization within the framework.

## Relation to the corpus

A **multi-UAV-as-base-station** trajectory/resource DRL entry — note this is a *communications* (coverage/utility) framing rather than compute offloading, distinguishing it from the offloading-centric [[zhao-2022-matd3-multiuav-ec-offloading]] and [[he-2023-fairness-3d-multiuav-maddpg]], with which it shares the multi-agent UAV-trajectory machinery. Reinforces [[multi-agent-td3]] and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches/full.md`
- Original PDF and extracted figures in the same folder.
