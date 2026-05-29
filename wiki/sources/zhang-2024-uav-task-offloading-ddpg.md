---
type: source
title: "UAV-Assisted Task Offloading in Edge Computing"
authors: ["Junna Zhang", "Guoxian Zhang", "Xinxin Wang", "Xiaoyan Zhao", "Peiyan Yuan", "Hu Jin"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3488210"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, task-offloading, resource-allocation, particle-swarm-optimization, ddpg, trajectory-optimization]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[ddpg]]"
  - "[[particle-swarm-optimization]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# UAV-Assisted Task Offloading in Edge Computing

## Citation

Zhang, J., Zhang, G., Wang, X., Zhao, X., Yuan, P., & Jin, H. (2024). *UAV-Assisted Task Offloading in Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3488210.

## TL;DR

A UAV-assisted task-offloading mechanism (**UTOM**) that deploys UAVs as mobile edge servers in complex terrains (forest, desert) to avoid large-scale fixed-server deployment. It minimizes the weighted sum of latency and energy consumption by jointly optimizing resource allocation, offloading decisions, and UAV trajectory, decomposing the non-convex problem into three sub-problems solved by convex optimization (resource), an **improved particle swarm optimization (IPSO)** (offloading), and **DDPG** (trajectory).

## Problem framing

Task offloading frees resource-constrained IoT devices, but fixed base-station edge servers have limited range and high deployment cost. UAVs as mobile edge servers cover complex terrains; the joint resource + offloading + trajectory design is non-convex.

## System model

- **Actors.** UAV(s) as mobile edge servers; IoT devices offloading tasks.
- **Objective.** Minimize weighted sum of latency + energy consumption ([[energy-latency-tradeoff]]).
- **Decisions.** Resource allocation, offloading decision, UAV trajectory.

## Method

- Decompose into three sub-problems:
  1. **Resource allocation:** Lagrange multiplier method + KKT conditions (convex).
  2. **Offloading decision:** improved particle swarm optimization (IPSO) ([[particle-swarm-optimization]]).
  3. **UAV trajectory:** **DDPG** ([[ddpg]]).

## Key findings

- Simulation experiments show UTOM efficiently reduces the weighted sum of latency and energy consumption (qualitative; specific curves in the paper).

## Limitations / future work

The authors flag: extend to **multi-UAV** systems for many IoT devices (a single UAV may not meet demand), and jointly use UAVs + edge servers to improve overall performance.

## Relation to the corpus

A **hybrid convex + IPSO + DDPG** single-UAV offloading entry that combines classical optimization, swarm optimization, and DRL across decomposed sub-problems — a methodological middle ground between the pure-optimization [[zhang-2019-uav-iot-comp-comm]] / [[yu-2020-uav-ec-collaborative-offloading]] and the pure-DRL multi-UAV works. Reinforces [[ddpg]], [[particle-swarm-optimization]], and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/UAV-Assisted_Task_Offloading_in_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
