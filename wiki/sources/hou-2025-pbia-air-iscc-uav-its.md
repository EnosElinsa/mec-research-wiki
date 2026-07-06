---
type: source
title: "Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems"
authors: ["Peng Hou", "Hongbin Zhu", "Zhihui Lu", "Shin-Chia Huang", "Yang Yang", "Hongfeng Chai"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3492028"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), 9(3), 2025"
tags: [source, integrated-sensing-computation-communication, uav-enabled-its, multi-uav, ppo, deep-reinforcement-learning, resource-allocation]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-enabled-its]]"
  - "[[ppo]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[device-association]]"
  - "[[qin-2025-urllc-noma-uav-iscc]]"
  - "[[zhao-2026-mappo-jscc-aec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems

## Citation

Hou, P., Zhu, H., Lu, Z., Huang, S.-C., Yang, Y., & Chai, H. (2025). *Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems*. **IEEE Transactions on Green Communications and Networking**, 9(3), 1414-1428. DOI: 10.1109/TGCN.2024.3492028. (The parse gives DOI, publication date 5 Nov 2024, and current version 21 Aug 2025; volume/issue/pages/venue verified against the title-matched Crossref/IEEE DOI record.)

## TL;DR

Introduces an Air-ISCC framework for UAV-swarm-enabled ITS where UAVs sense the environment, communicate with IoTDs, and compute offloaded tasks. The paper jointly optimizes time-slot scheduling, sensing/communication power, computing-resource allocation, and service association to maximize service success while minimizing UAV energy. PBIA, a PPO-based DRL algorithm with parallel training, learns UAV-swarm service policies.

## Problem framing

ITS emergency and traffic scenarios need sensing, communication, and computation at the same time. A single UAV has limited sensing range, communication rate, computing capacity, and energy, while a UAV swarm has to coordinate multidimensional resources and avoid inefficient competition among IoTDs. The paper turns this coupled Air-ISCC design into a sequential decision-making problem.

## System model

- The network has a UAV swarm and terrestrial IoTDs in a Manhattan-style ITS area.
- Communication/sensing links between IoTDs and the master eNodeB can be blocked by terrain or traffic accidents.
- UAVs carry antenna arrays, radar sensing units, computing resources, and storage.
- Each time slot is split by TDM: the first sub-slot senses environment/target information, and the second provides communication and computation service for offloaded IoTD tasks.
- Service decisions include sensing time, sensing power, UAV-IoTD association, and CPU-resource allocation.

## Method

The optimization target combines service success and UAV energy consumption. The paper models state, action, and reward for an MDP and proposes PBIA, a Proximal Policy Optimization based Air-ISCC algorithm. A parallel DRL training scheme lets multiple workers collect experience from Air-ISCC environments and send updates through a server-side PPO training loop before deployment on the control UAV.

## Key findings

- PBIA learns a stable service policy and converges faster than the DDPG and REINFORCE baselines in the reported reward curves.
- In 100 testing episodes, Table III reports PBIA average success rate 97.58% +/- 6.47%, average reward 279.527 +/- 19.716, and the best load-balance metric, 0.863 +/- 0.439.
- Across varying IoTD counts, the paper reports PBIA success-rate gains of 16.32% to 61.44% over baselines, and load-balancing improvements of 50.09% to 72.23%.
- PBIA remains effective as IoTD speeds, UAV counts, and energy-weighting factors vary, although the parse notes reduced stability as IoTD movement speed increases.

## Limitations / future work

The conclusion states that the study restricts UAV mobility; multi-UAV trajectory optimization in dynamic ITS environments is identified as future work.

## Relation to the corpus

This source expands [[integrated-sensing-computation-communication]] from single-UAV/FEEL and HAP-assisted AEC settings into a UAV-swarm ITS service system. It is closer to [[uav-enabled-its]] than to generic vehicular offloading: UAVs provide sensing, communication, and compute services for moving IoTDs in emergency/traffic scenes. Methodologically, PBIA reinforces the [[ppo]] lineage and complements [[zhao-2026-mappo-jscc-aec]] and [[qin-2025-urllc-noma-uav-iscc]] as ISCC/ISAC-MEC control entries.

## Raw artifacts

- `raw/sources/Learning-Based Over-the-Air Integrated Sensing- Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems/Learning-Based Over-the-Air Integrated Sensing- Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
