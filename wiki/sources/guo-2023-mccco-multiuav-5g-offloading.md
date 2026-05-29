---
type: source
title: "Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond"
authors: ["Hongzhi Guo", "Yutao Wang", "Jiajia Liu", "Chang Liu"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3277801"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav-assisted-mec, task-offloading, resource-allocation, partial-offloading, software-defined-networking, load-balancing]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[interdependent-tasks-dag]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[load-balancing-uav-mec]]"
  - "[[network-slicing]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond

## Citation

Guo, H., Wang, Y., Liu, J., & Liu, C. (2023). *Multi-UAV Cooperative Task Offloading and Resource Allocation in 5G Advanced and Beyond*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3277801.

## TL;DR

A **software-defined-networking-enhanced cooperative multiple-UAV-enabled aerial computing (MUEAC)** system. Cooperation among UAVs overcomes single-UAV limits (small coverage, scarce resources) and balances load; for divisible, data-dependent tasks, **partial offloading** makes scheduling more flexible than binary. The authors minimize the processing delay of divisible tasks under task-data-dependency and UAV-energy constraints, proposing the **MCCCO** (multi-UAV cooperative communication and computing optimization) scheme.

## Problem framing

5G-Advanced/beyond IoT apps (autonomous driving, face detection) are compute-intensive and latency-sensitive; remote areas lack terrestrial infrastructure. Single UAV-enabled aerial computing (SUEAC) is limited, so multiple UAVs (MUEAC) cooperate to use resources fully and balance load. Divisible tasks with data dependencies favor partial offloading.

## System model

- **Actors.** Multiple cooperating UAVs (SDN-enhanced) serving ground devices; models D2D communication, A2A communication, and task interdependency, with a detailed task-execution process from ground devices to UAVs ([[interdependent-tasks-dag]]).
- **Objective.** Minimize task processing delay under task-data-dependency and UAV-energy constraints; achieve load balancing on UAV energy.
- **Offloading.** Partial ([[binary-vs-partial-offloading]]).

## Method

- **MCCCO** scheme optimizing the ground D2D association strategy and computation-task offloading strategy to minimize processing delay and balance UAV energy load.

## Key findings

- Experiments show MCCCO achieves better task-processing-delay reduction and load balancing on UAV energy than traditional multi-UAV schemes (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established scheme.

## Relation to the corpus

A **cooperative multi-UAV partial-offloading** entry emphasizing task interdependency (DAG) and load balancing, complementing the priority-aware cooperative work [[hao-2024-clp-multiuav-priority-offloading]] and the energy-balancing multi-objective study [[huang-2023-mu-aec-task-energy]]. Reinforces [[interdependent-tasks-dag]], [[binary-vs-partial-offloading]], and [[load-balancing-uav-mec]]; introduces [[network-slicing]]/SDN-enhanced framing.

## Raw artifacts

- `raw/sources/Multi-UAV_Cooperative_Task_Offloading_and_Resource_Allocation_in_5G_Advanced_and_Beyond/full.md`
- Original PDF and extracted figures in the same folder.
