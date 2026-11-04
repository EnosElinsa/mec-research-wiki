---
type: source
title: "Multi-UAV Cooperative Trajectory for Servicing Dynamic Demands and Charging Battery"
authors: ["Kai Wang", "Xiao Zhang", "Lingjie Duan", "Jun Tie"]
year: 2023
url: "https://doi.org/10.1109/TMC.2021.3110299"
venue: "IEEE Transactions on Mobile Computing, 22(3)"
modeling_card: required
tags: [source, multi-uav, path-planning, dynamic-demands, charging-station, approximation-algorithm, dynamic-programming, integer-linear-programming]
related:
  - "[[uav-trajectory-control]]"
  - "[[uav-charging-scheduling]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[song-2024-k-coverage-uav-recharging]]"
created: 2026-11-02
updated: 2026-11-03
---

# Multi-UAV Cooperative Trajectory for Servicing Dynamic Demands and Charging Battery

## Citation

Wang, K., Zhang, X., Duan, L., & Tie, J. (2023). *Multi-UAV Cooperative Trajectory for Servicing Dynamic Demands and Charging Battery*. **IEEE Transactions on Mobile Computing, 22**(3). DOI: 10.1109/TMC.2021.3110299.

## TL;DR

A UAV swarm visits hotspots where user demands are released over time with waiting deadlines, and UAVs may detour to charging stations. The paper gives a polynomial-time optimal dynamic program for one UAV, an iterative cooperation algorithm with approximation ratio $1-(1-1/|K|)^{|K|}$ for many UAVs, and, with charging, an ILP on a DAG of UAV states plus an iterative constant-ratio algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A set $K$ of UAVs serves a set $J$ of $n$ user demands at locations $S$. Demand $j$ has release time $r_j$ and waiting deadline $d_j$ and needs service time $q$. Travel distance between locations is $a(s,s')$; UAVs communicate over LoS air-to-ground links. With charging, each UAV has battery capacity $B$, hovering and flying power rates $p_0 \le p_1$, and ground charging stations $C$, where a full recharge from remaining energy $B_t$ takes time $t_c(B_t)$.

**Problem & objective**: Maximize the total number of successfully serviced demands over the horizon by choosing cooperative UAV paths, $\max|J(M(t))|$ over all UAV state sequences.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV state | $U(t)$ | location and time | Where each UAV is at time $t$, including charging stations |
| Path history | $M(t)$ | sequence of states | Historical UAV states that define the trajectory |
| Serviced set | $J(M(t))$ | subset of $J$ | Demands served by time $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Deadline | A demand counts only if a UAV reaches its location within $[r_j,d_j]$ and serves it for $q$. |
| Travel | Moving between $s$ and $s'$ takes time proportional to $a(s,s')$. |
| Battery | Remaining energy never falls below zero; hovering and flying consume energy at fixed rates. |
| Charging | A UAV fully recharges at a station in time $t_c(B_t)$ and may wait there for new demands. |

**Algorithm**: For one UAV, a simplified dynamic program returns the optimal path with complexity polynomial in locations and demands. For $|K|$ UAVs, iterate single-UAV optimization over residual demands, achieving $1-(1-1/|K|)^{|K|}\ge1-1/e$ in the worst case. With charging, build a directed acyclic graph of UAV-state transitions, solve the ILP optimally, or use an iterative algorithm with constant approximation ratio.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied cooperative path planning of a UAV swarm that travels among multiple geographical user locations to service spatio-temporally distributed demands released over a long time horizon. For a single UAV, they simplified the traditional dynamic program and proposed an optimal algorithm whose complexity is polynomial in the numbers of locations and demands. For a large swarm, they presented a fast iterative cooperation algorithm with a provable worst-case approximation ratio and proved that it outperforms the traditional approach of partitioning UAVs to serve separate location clusters. To relax the battery capacity limit, they jointly designed paths over user locations and charging stations, transformed the problem into an integer linear program using a directed acyclic graph of the UAV-state transition diagram, and proposed an iterative algorithm with constant approximation ratio. Simulations validate the theoretical results, with the multi-UAV algorithm achieving an average performance ratio above 96% relative to the optimum.

## Problem framing

UAVs have small service coverage and must fly close to users, and demands appear at different times and places. Partitioning the swarm by location clusters can be arbitrarily poor when demands are uneven.

## System model

- Demands over up to 40 minutes, durations 1 to 20 minutes, 2-minute service time.
- Locations and three charging stations on a 10 km grid with Manhattan distance.
- Battery capacity 30 units; hovering and flying cost 2 and 3 units per minute; charging or swapping takes 3 minutes.

## Method

The single-UAV DP compresses the state to decision points, the multi-UAV algorithm applies it greedily per UAV, and the charging version adds station nodes to the state graph.

## Key findings

- The multi-UAV algorithm's average performance ratio exceeds 96%, close to 1 for small or large swarms.
- With 20 demands at 10 locations, the optimum serves 17 and the charging-aware Algorithm 3 serves 16, a 94% ratio.
- Under noisy demand information, Algorithm 3 keeps an average ratio above 75% of the offline optimum.

## Limitations / future work

Demands are known in advance. The authors plan online algorithms with competitive-ratio guarantees for unknown demands.

## Relation to the corpus

A combinatorial deadline-driven routing view related to [[deadline-constrained-uav-data-collection]] and [[uav-charging-scheduling]], with service applicable to [[multi-uav-assisted-mec]]. A slot-wise assignment counterpart with renewable platforms is [[song-2024-k-coverage-uav-recharging]].

## Raw artifacts

- Parse: `raw/sources/Multi-UAV_Cooperative_Trajectory_for_Servicing_Dynamic_Demands_and_Charging_Battery/Multi-UAV_Cooperative_Trajectory_for_Servicing_Dynamic_Demands_and_Charging_Battery.md`
- Origin PDF and extracted figures are in the same folder.
