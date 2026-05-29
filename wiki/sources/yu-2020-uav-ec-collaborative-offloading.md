---
type: source
title: "Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing"
authors: ["Zhe Yu", "Yanmin Gong", "Shimin Gong", "Yuanxiong Guo"]
year: 2020
url: "https://doi.org/10.1109/JIOT.2020.2965898"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, computation-offloading, resource-allocation, sca, edge-cloud-collaboration, energy-latency-tradeoff]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
created: 2026-05-29
updated: 2026-05-29
---

# Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing

## Citation

Yu, Z., Gong, Y., Gong, S., & Guo, Y. (2020). *Joint Task Offloading and Resource Allocation in UAV-Enabled Mobile Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2020.2965898.

## TL;DR

A UAV-enabled MEC system where a UAV and edge clouds (ECs) **collaboratively** serve stationary IoT devices in regions where ECs are inaccessible due to terrestrial signal blockage/shadowing. The paper minimizes the weighted sum of all devices' service delay and UAV energy consumption by jointly optimizing UAV position, communication and computing resource allocation, and task-splitting decisions, solving the non-convex problem with **successive convex approximation (SCA)**.

## Problem framing

Existing MEC fails when users explode in number or facilities are sparse. UAVs improve connectivity for ground IoT via high-altitude LoS. Here the UAV and ECs cooperate (aerial-to-ground links), and the joint position + resource + task-split design is highly non-convex.

## System model

- **Actors.** IoT devices (stationary), one UAV, edge clouds (ECs); the UAV and ECs jointly serve devices.
- **Objective.** Minimize the weighted sum of total device service delay and UAV energy ([[energy-latency-tradeoff]]).
- **Decisions.** UAV position, communication + computing resource allocation, task-splitting ([[binary-vs-partial-offloading]] — splitting).

## Method

- Transform the non-convex problem into an approximated convex form and solve efficiently with an **SCA**-based algorithm ([[alternating-optimization-sdr-sca]]).

## Key findings

- Numerical experiments show the collaborative UAV-EC offloading scheme **largely outperforms baselines that rely solely on UAV or solely on ECs** (the paper's stated headline result).

## Limitations / future work

Stationary IoT devices. Future work: multiple UAVs, and task offloading + UAV swarm placement in multihop MEC scenarios.

## Relation to the corpus

A foundational **UAV-EC collaborative offloading** entry, methodologically close to [[zhang-2019-uav-iot-comp-comm]] (SCA + Lagrangian dual single-UAV) and [[liu-2022-miso-uav-mec-trajectory]] (MISO three-stage). Its UAV+EC cooperation theme foreshadows the hierarchical UAV+HAP track. Reinforces [[alternating-optimization-sdr-sca]] and [[energy-latency-tradeoff]].

## Raw artifacts

- `raw/sources/Joint_Task_Offloading_and_Resource_Allocation_in_UAV-Enabled_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
