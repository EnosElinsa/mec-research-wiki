---
type: source
title: "Two-Hop Packet Scheduling, Resource Allocation, and UAV Trajectory Design for Internet of Remote Things in Air–Ground Integrated Network"
authors: ["Shichao Li", "Zhiqiang Yu", "Mianxiong Dong", "Kaoru Ota", "Hongbin Chen", "Ning Zhang", "Chao Yang"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3393444"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, air-ground-integrated-network, packet-scheduling, resource-allocation, maddpg, prioritized-experience-replay, hap, uav-trajectory-control]
related:
  - "[[air-ground-integrated-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[maddpg]]"
  - "[[ddqn]]"
  - "[[hybrid-action-decision-making]]"
  - "[[prioritized-experience-replay]]"
  - "[[uav-trajectory-control]]"
  - "[[li-2025-twohop-airground-drl-offloading]]"
  - "[[wang-2024-hybrid-oma-noma-sagin]]"
created: 2026-05-31
updated: 2026-05-31
---

# Two-Hop Packet Scheduling, Resource Allocation, and UAV Trajectory Design for Internet of Remote Things in Air–Ground Integrated Network

## Citation

Li, S., Yu, Z., Dong, M., Ota, K., Chen, H., Zhang, N., & Yang, C. (2024). *Two-Hop Packet Scheduling, Resource Allocation, and UAV Trajectory Design for Internet of Remote Things in Air–Ground Integrated Network*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3393444. (Manuscript received 31 Jan 2024; date of publication 25 Apr 2024; date of current version 25 Jul 2024.)

## TL;DR

A joint **packet scheduling, resource allocation, and UAV trajectory design** problem for the **Internet of Remote Things (IoRT)** in a two-hop **air-ground integrated network** of UAVs and HAPs. The objective is to **minimize the average packet queue delay from HAP to IoRT devices** while avoiding network congestion. The non-convex problem is reformulated as an **MDP**; because it has **continuous + discrete hybrid action spaces**, the primal action space is split into two sub-action spaces solved with **MADDPG** (continuous) and **multi-agent double DQN (MADDQN)** (discrete) respectively, enhanced with **adaptive prioritized experience replay (PER)** → the hybrid **MADDPG-APER** algorithm.

## Problem framing

Terrestrial networks have limited coverage/capacity for IoRT devices in remote/rural areas. An air-ground integrated network helps: HAPs give high-reliability, large-coverage connection, while UAVs (high mobility, low cost, good LoS) raise the channel capacity between HAP and IoRT devices over a two-hop path. The goal is to reduce end-to-end (e2e) packet delay and avoid congestion of the two-hop network.

## System model

- **Tiers.** HAP → UAVs → IoRT devices (two-hop), in an [[air-ground-integrated-network]] with [[high-altitude-platform-station|HAPs]].
- **Decisions.** Packet scheduling, bandwidth allocation, power control, and UAV trajectory design.
- **Objective.** Minimize the average packet queue delay from HAP to IoRT devices → reformulated as an **MDP** with hybrid (continuous + discrete) action spaces.

## Method

- Separate the primal action space into two sub-action spaces and solve with the basic ideas of:
  - **MADDPG** for the continuous sub-actions ([[maddpg]]).
  - **multi-agent double DQN (MADDQN)** for the discrete sub-actions ([[ddqn]]).
- Introduce **adaptive prioritized experience replay** to improve stability, convergence rate, and learning efficiency, yielding the hybrid **MADDPG-APER** algorithm ([[prioritized-experience-replay]], [[hybrid-action-decision-making]]).

## Key findings

- Simulations show **MADDPG-APER reduces the average packet queue delay** versus benchmark algorithms (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established method; results are simulation-based.

## Relation to the corpus

A **two-hop air-ground DRL** entry that is closely related to — but **distinct from** — the same lead author's [[li-2025-twohop-airground-drl-offloading]] (Li et al. 2025, IEEE IoT-J, JPTORAUTD): that paper targets partial **task offloading** delay with MADDPG-IPER + NV-IPPO; **this** paper (2024) targets **packet-queue delay** from HAP to IoRT devices with MADDPG + MADDQN + adaptive PER (MADDPG-APER) — different objective, action-space split, algorithm, year, and DOI. Shares the Guilin-University-of-Electronic-Technology authorship (Shichao Li, Hongbin Chen) with [[wang-2024-hybrid-oma-noma-sagin]]. Reinforces [[air-ground-integrated-network]], [[maddpg]], and [[prioritized-experience-replay]].

## Raw artifacts

- `raw/sources/Two-Hop_Packet_Scheduling_Resource_Allocation_and_UAV_Trajectory_Design_for_Internet_of_Remote_Things_in_AirGround_Integrated_Network/full.md`
- Original PDF and extracted figures in the same folder.
