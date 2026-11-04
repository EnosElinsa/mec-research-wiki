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
updated: 2026-11-03
modeling_card: required
---

# Drone Swarm Path Planning for Mobile Edge Computing in Industrial Internet of Things

## Citation

Miao, Y., Hwang, K., Wu, D., Hao, Y., & Chen, M. (2023). *Drone Swarm Path Planning for Mobile Edge Computing in Industrial Internet of Things*. **IEEE Transactions on Industrial Informatics**. DOI: 10.1109/TII.2022.3196392. (Date of publication 4 August 2022; date of current version 4 May 2023.)

## TL;DR

A drone-swarm-assisted MEC offloading scheme for smart-city / Industrial IoT that combines **ground-station-controlled global path planning** with **onboard-computer-controlled local path planning** — the **ground-air controlled global and local path planning (GAGLPP)** algorithm. Globally, a swarm scheduling/allocation strategy ranks monitoring areas by **priority, UAV residual energy, and distance to target points** to minimize total flight length and energy. Locally, each UAV computes its optimal communication coverage from user mobility and jointly optimizes local path + computation offloading to maximize the number of offloading services and minimize total task latency. The result is an energy-efficiency-optimized UAV-cluster offloading strategy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A ground station dispatches $U$ UAVs with onboard computers to $M$ circular monitoring areas of radius $r$, each holding mobile devices (MDs) that move under a Gauss-Markov mobility model. Global path planning at the ground station assigns the closest UAV to each area in order of area priority $\delta_m$ (ranked by user count). Inside an area, the onboard computer plans $I$ waypoints and serves accessed MDs over air-to-ground links with bandwidth $B$ shared equally among accessed devices. A UAV is recalled when its remaining energy cannot cover the return flight $E_u^{Ba}$.

**Problem & objective**: $\mathbf P:\max_{\delta_m,\mu_n,I,T}\eta$ in (16), with the energy-efficiency model $\eta=E_u^{\mathrm{total}}/T_{ta}^{\mathrm{total}}$ as written in the parse, where $E_u^{\mathrm{total}}=E_u^{\mathrm{Gl}}+\sum_{i=1}^{I}E_u^{Ta}+E_u^{\mathrm{Lo}}$ sums global flight, offloading-service and local flight/hover energy and $T_{ta}^{\mathrm{total}}$ is total task completion latency. Check the published paper for the direction of the ratio. P is split into P1 (24), which minimizes total task latency subject to C1–C5 and C7, and P2 (26), which minimizes total UAV energy subject to C1–C4, C6 and C7.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Area priority / assignment order | $\delta_m$ | discrete, $\{1,\dots,M\}$ | Priority used by the ground station to assign UAVs to areas |
| Channel access / offloaded share | $\mu_{n,i}$ | written $[0,1]$; $\mu_n=1$ means access | Whether MD $n$ offloads at waypoint $i$; offloaded data $\mu_{n,i}b_{n,i}$ |
| Waypoint set | $I$ | discrete | Number and positions $P_{u,i}$ of local-path waypoints |
| Timing | $T$ | continuous | Time variables listed under the max in (16); not separately defined in the parse |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 (17) | $\mu_{n,i}=[0,1]$ |
| C2 (18) | $\sum_{n=1}^{N}\mu_{n,i}\leq N$ |
| C3 (19) | Offloading-service time does not exceed the MD's local computing time, $T_{u,n,i}^{Ta}\leq T_{Q^n}^{d}$ |
| C4 (20) | Service time at a waypoint fits the leg duration, $T_{u,i}^{Ta}\leq T_{u,i+1,i}^{lo}$ |
| C5 (21) | Total latency lies between the offloading transmission-plus-UAV-computing time and the MD local computing time $C\sum_n b_{n,i}/f_d$ |
| C6 (22) | $0\leq E_u^{\mathrm{total}}\leq E_u^{\mathrm{In}}-E_{u,i}^{Ba}$, keeping return-flight energy |
| C7 (23) | Each waypoint stays within the area, $\sqrt{(X_{u,i}-x_m)^2+(Y_{u,i}-y_m)^2}\leq r$ |

**Algorithm**: Theorem 1 shows that $\mu_{n,i}=1$ if and only if the UAV–MD distance is at most $D_{u,n,i}^{\max}$ in (30). Algorithm 1 (dynamic waypoint planning based on user mobility) places each waypoint to cover as many predicted MD positions as possible within $D_{u,n,i}^{\max}$ for P1. Algorithm 2 (GAGLPP) repeats over waypoints: global flight energy from (4)–(5), service time and energy from (11)–(12), MD positions from (7), the next waypoint from Algorithm 1 and leg energy from (15), until $i=I$; it then returns $\eta$ if $E_u^{\mathrm{total}}\leq E_u^{\mathrm{In}}-E_{u,i}^{Ba}$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Miao et al. [x] studied drone-swarm path planning and computation offloading for Industrial IoT mobile edge computing. They formulated a UAV energy-efficiency problem over area priority, device channel access, waypoints, and timing, subject to service-time, leg-duration, latency, return-energy, and area constraints, and split it into latency-minimization and energy-minimization subproblems. In their GAGLPP algorithm, the ground station assigns the closest UAV to areas in order of priority, and each UAV places waypoints from predicted device positions so that as many devices as possible fall within the maximum offloading distance. Device positions follow a Gauss-Markov mobility model, and a device offloads only when offloading is faster than local computing. Against diameter, circle, and RL-based path planning, GAGLPP served more devices, gave lower total task latency, and kept energy efficiency in $[4.5,5.5]$; its path was shorter only up to seven waypoints and became longer than diameter path planning beyond that.

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

- `raw/sources/Drone_Swarm_Path_Planning_for_Mobile_Edge_Computing_in_Industrial_Internet_of_Things/Drone_Swarm_Path_Planning_for_Mobile_Edge_Computing_in_Industrial_Internet_of_Things.md`
- Original PDF and extracted figures (`images/`) in the same folder.
