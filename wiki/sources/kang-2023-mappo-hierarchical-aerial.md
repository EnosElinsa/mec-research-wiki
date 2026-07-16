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
  - "[[ctde-multi-agent-drl-protocol]]"
created: 2026-05-29
modeling_card: required
updated: 2026-07-16
---

# Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach

## Citation

Kang, H., Chang, X., Mišić, J., Mišić, V. B., Fan, J., & Liu, Y. (2023). *Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3240173.

## TL;DR

A **hierarchical aerial computing** system where both HAPs and UAVs serve ground devices (GDs). UAVs collect GD tasks and may offload part of them up to the HAP to cut processing delay. The joint UAV resource allocation (spectrum, caching, computing) + task offloading problem is cast as a [[pomdp|POMDP]] under resource, energy, and collision-avoidance constraints, and solved with **[[mappo|multi-agent PPO]]** under [[centralized-training-decentralized-execution|CTDE]], with state normalization and action masking to speed training. Objective: maximize the amount of computed tasks while meeting heterogeneous QoS.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In a disaster area, $U$ hovering UAVs collect heterogeneous-QoS computation tasks from $N$ ground devices and either process task fractions locally or offload them to one more powerful HAP; each time slot has task-collection and offloading-and-processing phases.

**Problem & objective**: Problem (10a) maximizes completed task volume $\sum_{n\in\mathcal N}b_{n,u}(t)\,\mathrm{size}_n(t)H_1(t)H_2(t)$, where the step functions accept only tasks meeting delay and cache requirements; the equivalent cooperative reward sums accepted task sizes across devices.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Device association | $b_{n,u}(t)$ | Binary, $\{0,1\}$ | Associates ground device $n$ with UAV $u$ |
| Spectrum share | $f_{n,u}(t)$ | Continuous, $[0,1]$ | Allocates UAV spectrum to device $n$ |
| Cache share | $f_{n,u}^{\mathrm{ca}}(t)$ | Continuous, $[0,1]$ | Allocates UAV cache to device $n$ |
| Computing share | $f_{n,u}^{\mathrm{co}}(t)$ | Continuous, $[0,1]$ | Allocates UAV CPU capacity to device $n$ |
| HAP offloading ratio | $\mathrm{ratio}_u(t)$ | Continuous, $[0,1]$ | Splits collected tasks between UAV and HAP processing |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each ground device associates with at most one UAV |
| C2 | Associated spectrum, cache, and computing shares each sum to at most one |
| C3 | Cumulative UAV energy satisfies $\sum_t e_{\mathrm{total}}(t)\leq E_{\mathrm{UAV}}$ |
| C4 | UAV separation remains above the collision distance |
| C5 | A task contributes reward only when its delay and cache QoS indicators both equal one |

**Algorithm**: The joint problem is cast as a cooperative POMDP whose local action contains association, resource shares, and offloading ratio; MAPPO collects multi-UAV trajectories, trains centralized critics and PPO actors with shuffled replay batches, observation normalization, and action masking, then executes each actor from local observations only.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Kang et al. [x] studied hierarchical aerial computing in which multiple UAVs collect tasks from ground devices and can offload part of each task to a high-altitude platform. They formulated joint association, spectrum, cache, computing, and offloading decisions to maximize the amount of completed task data subject to resource, energy, collision-avoidance, and heterogeneous-QoS conditions. The problem is represented as a cooperative POMDP whose agents observe local device and task information and share a reward equal to successfully completed task size. Their MAPPO solver uses centralized training, decentralized execution, state normalization, and action masking. Numerical results show that combined UAV-HAP computing completed more tasks than UAV-only or HAP-only processing, and MAPPO achieved the highest QoS satisfaction among MAPPO, MADDPG, and random policies.

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
