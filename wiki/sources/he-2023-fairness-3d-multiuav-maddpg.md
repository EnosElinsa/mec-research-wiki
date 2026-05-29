---
type: source
title: "Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System"
authors: ["Yejun He", "Youhui Gan", "Haixia Cui", "Mohsen Guizani"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3241087"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, multi-uav-assisted-mec, maddpg, fairness, trajectory-optimization, task-offloading, energy-efficiency]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
  - "[[energy-balancing-uav]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System

## Citation

He, Y., Gan, Y., Cui, H., & Guizani, M. (2023). *Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3241087.

## TL;DR

A 3-D dynamic multi-UAV-assisted MEC system in which ground devices (GDs) with real-time mobility and task updates select a target UAV for offloading. The authors formulate communication, computation, and flight energy as objectives **based on fairness among UAVs**, analytically derive the optimal GD selectivity and offloading strategy per slot, then learn the multi-UAV 3-D trajectories with **MADDPG**. They minimize total system energy while ensuring inter-UAV fairness.

## Problem framing

GDs have limited compute/energy, and multiple UAVs must share the load fairly. The paper separates the decision into (a) which UAV a GD offloads to and how much (selectivity + offloading strategy, derived analytically) and (b) how UAVs move in 3-D over a horizon (learned).

## System model

- **Actors.** Multiple UAVs at 3-D positions; mobile GDs with task updates each slot.
- **Objectives.** Communication, computation, and flight energy, framed for fairness among UAVs.
- **Per-slot result.** Optimal GD selectivity and offloading strategy obtained by theoretical analysis/derivation (with extreme-value/differentiability arguments shown in the appendix).

## Method

- **Per slot t:** closed-form/derived offloading strategy and UAV selection for each GD.
- **Over horizon T:** model UAV trajectories as a sequence of joint location updates and solve with **MADDPG** (multi-agent DDPG) for the cooperative trajectory problem ([[multi-agent-td3]] family / [[centralized-training-decentralized-execution]]).

## Key findings

- Simulations show minimum total system energy (communication + computation + flight) **under the fairness premise**, and validate the rationality/effectiveness of the algorithm (qualitative; specific energy curves in the paper).

## Limitations / future work

Future work: multi-UAV communications across multiple cells and more novel trajectory designs.

## Relation to the corpus

Adds a **fairness-among-UAVs** angle to the multi-UAV trajectory + offloading track, complementing the energy-balancing fairness of [[huang-2023-mu-aec-task-energy]] and [[nabi-2025-jour-hierarchical-aerial]], and the safety-constrained heterogeneous-fleet trajectory work [[zhang-2025-ssac-mgi-heterogeneous-uav]]. Methodologically it shares the MADDPG/MATD3 cooperative-trajectory pattern with [[zhao-2022-matd3-multiuav-ec-offloading]] and [[chang-2022-marl-multiuav-trajectory]]. Reinforces [[energy-balancing-uav]] and [[jains-fairness-index]].

## Raw artifacts

- `raw/sources/Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System/full.md`
- Original PDF and extracted figures in the same folder.
