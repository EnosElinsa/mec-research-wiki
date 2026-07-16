---
type: source
title: "Drone Swarm Path Planning for Mobile Edge Computing in Industrial Internet of Things"
authors: ["Yiming Miao", "Kai Hwang", "Di Wu", "Yixue Hao", "Min Chen"]
year: 2023
url: "https://doi.org/10.1109/TII.2022.3196392"
venue: "IEEE Transactions on Industrial Informatics (IEEE TII)"
tags: [source, uav-mec, path-planning, drone-swarm, energy-efficiency, industrial-iot, computation-offloading]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[load-balancing-uav-mec]]"
  - "[[energy-latency-tradeoff]]"
  - "[[task-offloading]]"
  - "[[air-ground-integrated-network]]"
  - "[[zhang-2024-uav-task-offloading-ddpg]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
created: 2026-05-31
updated: 2026-07-16
modeling_card: required
---

# Drone Swarm Path Planning for Mobile Edge Computing in Industrial Internet of Things

## Citation

Miao, Y., Hwang, K., Wu, D., Hao, Y., & Chen, M. (2023). *Drone Swarm Path Planning for Mobile Edge Computing in Industrial Internet of Things*. **IEEE Transactions on Industrial Informatics**. DOI: 10.1109/TII.2022.3196392. (Date of publication 4 August 2022; date of current version 4 May 2023.)

## TL;DR

A drone-swarm-assisted MEC offloading scheme for smart-city / Industrial IoT that combines **ground-station-controlled global path planning** with **onboard-computer-controlled local path planning** — the **ground-air controlled global and local path planning (GAGLPP)** algorithm. Globally, a swarm scheduling/allocation strategy ranks monitoring areas by **priority, UAV residual energy, and distance to target points** to minimize total flight length and energy. Locally, each UAV computes its optimal communication coverage from user mobility and jointly optimizes local path + computation offloading to maximize the number of offloading services and minimize total task latency. The result is an energy-efficiency-optimized UAV-cluster offloading strategy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A drone swarm with onboard MEC computers serves mobile Industrial-IoT users in multiple monitoring areas. A ground station performs global area/cluster scheduling, while each UAV performs local path planning and offloading; channels are air-to-ground and users move within each coverage region.

**Problem & objective**: GAGLPP hierarchical path-planning and offloading, a mixed discrete-continuous energy-efficiency problem, maximizes the number of offloading services and minimizes path length/task latency, summarized as $\max\mathrm{EE}=\text{served tasks}/\text{flight+communication+compute energy}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Area/cluster assignment | $x_{u,r}$ | binary | UAV $u$ is assigned to monitoring area $r$ |
| Local trajectory | $\mathbf q_u(t)$ | continuous path | UAV route within its assigned area |
| Offloading ratio | $\lambda_{u,i}(t)$ | continuous, $[0,1]$ | Fraction of task $i$ offloaded to UAV $u$ |
| Coverage radius | $R_u(t)$ | continuous, bounded | Communication service radius selected from user mobility |
| Scheduling priority | $\pi_r$ | discrete ordering | Global service order based on priority, energy, and distance |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each monitoring area and user is assigned to a feasible UAV cluster |
| C2 | UAV paths remain within their coverage and motion limits |
| C3 | Offloading ratios and local/remote workload satisfy task conservation |
| C4 | Task completion latency and UAV communication/computation capacity limits hold |
| C5 | Flight, communication, and computation energy stay within UAV budgets |

**Algorithm**: Ground station ranks areas by priority, residual energy, and distance → assign UAV clusters → onboard double-loop optimization updates local coverage/path/offloading → iterate until served-task count, latency, and energy-efficiency objectives stabilize.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Miao et al. [x] studied drone-swarm path planning and computation offloading for Industrial IoT mobile edge computing. They formulated a hierarchical global and local design that schedules UAV clusters across monitoring areas and jointly optimizes local paths, coverage, and task offloading to increase served tasks and energy efficiency while reducing latency. The GAGLPP method ranks areas using priority, residual UAV energy, and distance at the ground station, then runs an onboard iterative path/offloading update for each UAV. Local decisions account for user mobility, communication coverage, computation cost, and task-completion latency. Experiments report more offloading services, shorter path length, and higher energy efficiency than the evaluated comparison approaches.

## Problem framing

Fixed base stations / servers as edge nodes have limited, fixed service scope, channel attenuation over long distances, and high large-scale deployment cost — poor fits for complex terrains (desert, wilderness, ocean) and crowd-gathering monitoring areas. UAVs with onboard computers are low-cost, mobile MEC nodes (and backup base stations when fixed ones are damaged). Prior path-planning-based offloading mostly studies **single-UAV, single-area, multi-user** scenarios and ignores **cluster scheduling across multiple machines and areas** and the **ground-station + onboard** control split used in real UAV practice (e.g. Pixhawk-v4 + QGroundControl). This paper targets that gap.

## System model

- **Control split.** Ground station handles mission division + cluster scheduling (global); onboard computer handles path planning + computation offloading (local) ([[air-ground-integrated-network]]).
- **Global scheduling.** Drone-swarm allocation by monitoring-area priority, UAV residual energy, and distance to target points → minimize global flight length + energy ([[multi-uav-assisted-mec]], [[load-balancing-uav-mec]]).
- **Local planning.** From user mobility, compute each UAV's optimal communication coverage; jointly optimize local path + offloading to maximize offloading-service count and minimize total latency ([[uav-trajectory-control]]).
- **Objective.** Optimize overall **energy efficiency** across flight + communication + computation energy ([[energy-latency-tradeoff]]).

## Method

- **GAGLPP** = a two-level (global + local) path-planning + offloading algorithm.
- An **onboard double-loop iterative optimization** of UAV-swarm energy efficiency maximizes the number of offloading services and minimizes path length, accounting for user mobility, task completion latency, and UAV communication coverage.
- The strategy maximizes energy efficiency and minimizes flight energy + total task latency "by using a small amount of computational energy compensation" (parse contributions).

## Key findings

- Experiments show GAGLPP provides **more offloading services** while achieving **shorter path length** and **greater energy efficiency** than the compared approaches (parse abstract; specific curves in the figures).

## Limitations / future work

Simulation/experiment-based; the parse's contributions do not enumerate explicit limitations beyond the modeled assumptions (ground-station + onboard control, priority-based scheduling).

## Relation to the corpus

A **path-planning-centric, ground-air-controlled** multi-UAV offloading entry that distinguishes itself by the explicit **ground-station (global) + onboard (local)** control hierarchy and a priority/energy/distance scheduling rule, rather than a single joint optimization or end-to-end DRL policy. Its global-flight + local-offloading split complements the DDPG-trajectory + IPSO-offloading decomposition of [[zhang-2024-uav-task-offloading-ddpg]] and the evolutionary path-planning + offloading of [[peng-2022-cmop-uav-path-planning]]. As an **Industrial IoT** complex-terrain deployment, it broadens the corpus's application settings. Reinforces [[uav-trajectory-control]] and [[energy-latency-tradeoff]].

## Raw artifacts

- `raw/sources/Drone_Swarm_Path_Planning_for_Mobile_Edge_Computing_in_Industrial_Internet_of_Things/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
