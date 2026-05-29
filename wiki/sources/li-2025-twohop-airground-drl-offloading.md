---
type: source
title: "Two-Hop Partial Task Offloading and Resource Allocation in Air-Ground Integrated Mobile Edge Computing Network: A DRL-Based Method"
authors: ["Shichao Li", "Bingji Lu", "Laha Ale", "Hongbin Chen", "Fangqing Tan", "Jingyue Huang"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3548088"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, air-ground-integrated-network, partial-offloading, resource-allocation, maddpg, ippo, prioritized-experience-replay, hap, uav]
related:
  - "[[air-ground-integrated-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[multi-agent-td3]]"
  - "[[ppo]]"
  - "[[prioritized-experience-replay]]"
  - "[[uav-trajectory-control]]"
  - "[[wang-2024-hybrid-oma-noma-sagin]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-05-29
---

# Two-Hop Partial Task Offloading and Resource Allocation in Air-Ground Integrated Mobile Edge Computing Network: A DRL-Based Method

## Citation

Li, S., Lu, B., Ale, L., Chen, H., Tan, F., & Huang, J. (2025). *Two-Hop Partial Task Offloading and Resource Allocation in Air-Ground Integrated Mobile Edge Computing Network: A DRL-Based Method*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3548088.

## TL;DR

A joint partial-task-offloading, resource-allocation, and UAV-trajectory-design problem in an **air-ground integrated MEC** network for Internet of Remote Things (IoRT), where UAVs and HAPs execute tasks. The objective is to minimize total offloading delay across all IoRT devices. The non-convex problem is cast as an MDP, decomposed into two sub-problems solved with **MADDPG** (trajectory + power control) and **IPPO** (offloading + resource allocation), enhanced with **prioritized experience replay** and a noise value, yielding MADDPG-IPER, NV-IPPO, and the overall JPTORAUTD algorithm.

## Problem framing

MEC + air-ground integrated networks give widespread coverage for IoRT, with UAVs and HAPs executing tasks two hops away. As IoRT-device and UAV counts grow, the MDP's complexity grows, motivating problem decomposition and convergence-improving tricks.

## System model

- **Tiers.** IoRT devices → UAVs → HAPs (two-hop execution) ([[high-altitude-platform-station]]).
- **Offloading.** Partial ([[binary-vs-partial-offloading]]).
- **Objective.** Minimize total task-offloading delay of all IoRT devices → MDP.

## Method

- Decompose into:
  - **UAV trajectory + IoRT power control:** based on **MADDPG**, improved with enhanced prioritized experience replay → **MADDPG-IPER** ([[multi-agent-td3]], [[prioritized-experience-replay]]).
  - **Partial offloading + resource allocation:** based on **independent PPO (IPPO)**, with a noise value → **NV-IPPO** ([[ppo]]).
- Combine into the **JPTORAUTD** algorithm.

## Key findings

- Simulations show JPTORAUTD reduces total offloading delay versus benchmark algorithms (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established method.

## Relation to the corpus

A **two-hop air-ground DRL offloading** entry that combines MADDPG + IPPO across decomposed sub-problems, alongside the MAPPO hierarchical work [[kang-2023-mappo-hierarchical-aerial]] and the SCA+DQN SAGIN work [[wang-2024-hybrid-oma-noma-sagin]] (shared co-authors Hongbin Chen / Fangqing Tan). Reinforces [[air-ground-integrated-network]], [[prioritized-experience-replay]], and the partial-offloading framing.

## Raw artifacts

- `raw/sources/Two-Hop_Partial_Task_Offloading_and_Resource_Allocation_in_AirGround_Integrated_Mobile_Edge_Computing_Network_A_DRL-Based_Method/full.md`
- Original PDF and extracted figures in the same folder.
