---
type: source
title: "Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach"
authors: ["Hongyue Kang", "Xiaolin Chang", "Jelena Mišić", "Vojislav B. Mišić", "Junchao Fan", "Yating Liu"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3240173"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, hierarchical-aerial-mec, mappo, multi-agent-drl, task-offloading, resource-allocation, hap, uav]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[pomdp]]"
  - "[[ppo]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[jia-2022-hierarchical-aerial-matching]]"
created: 2026-05-29
updated: 2026-05-29
---

# Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach

## Citation

Kang, H., Chang, X., Mišić, J., Mišić, V. B., Fan, J., & Liu, Y. (2023). *Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3240173.

## TL;DR

A **hierarchical aerial computing** system where both HAPs and UAVs serve ground devices (GDs). UAVs collect GD tasks and may offload part of them up to the HAP to cut processing delay. The joint UAV resource allocation (spectrum, caching, computing) + task offloading problem is cast as a [[pomdp|POMDP]] under resource, energy, and collision-avoidance constraints, and solved with **[[mappo|multi-agent PPO]]** under [[centralized-training-decentralized-execution|CTDE]], with state normalization and action masking to speed training. Objective: maximize the amount of computed tasks while meeting heterogeneous QoS.

## Problem framing

Prior aerial-MEC work ignored UAV→HAP offloading and suffered long HAP↔GD transmission delay. Here UAVs (limited resources, constrained coverage) cooperatively allocate resources to GDs and offload overflow tasks to the HAP, balancing delay against QoS satisfaction.

## System model

- **Tiers.** HAP + multiple UAVs as agents; GDs on the ground generate heterogeneous-QoS tasks.
- **UAV roles.** Collect GD tasks; allocate spectrum, caching, and computing; decide GD association and how much to offload to the HAP.
- **Formulation.** POMDP with constraints on available resources, UAV energy, and collision avoidance; objective = maximize amount of computed tasks subject to QoS.

## Method

- **MAPPO** (multi-agent PPO) under **CTDE**: each UAV acts on local observations for GD association, resource allocation, and task offloading.
- **Training tricks.** State normalization and action masking improve training efficiency.

## Key findings

- Numerical experiments verify both the advantage of the hierarchical (UAV+HAP) architecture and the efficiency of the MAPPO algorithm versus baselines (qualitative; specific reward/QoS curves are in the paper).

## Limitations / future work

UAV trajectory optimization is **not** considered (assumed fixed), and spectrum sensing is assumed perfect. The authors flag trajectory optimization and imperfect spectrum sensing as future work.

## Relation to the corpus

A DRL counterpart in the **hierarchical aerial MEC (UAV+HAP)** track alongside [[nabi-2025-jour-hierarchical-aerial]], [[jia-2025-dro-uav-hap-mec]], and [[bao-2025-ddpg-video-offloading]]. Where [[jia-2022-hierarchical-aerial-matching]] solves the same UAV+HAP offloading with matching theory, this paper uses MAPPO. Reinforces [[hierarchical-aerial-mec]], [[mappo]], and the recurring [[centralized-training-decentralized-execution]] pattern.

## Raw artifacts

- `raw/sources/Cooperative_UAV_Resource_Allocation_and_Task_Offloading_in_Hierarchical_Aerial_Computing_Systems_A_MAPPO-Based_Approach/full.md`
- Original PDF and extracted figures in the same folder.
