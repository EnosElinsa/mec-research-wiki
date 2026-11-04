---
type: source
title: "Cost Optimization of UAV Swarm Network for Persistent Emergency Communication"
authors: ["Changtong Liu", "Xin Xin", "Yueyue Dai", "Du Xu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3649278"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, uav-swarm, emergency-communication, persistent-service, mobile-relaying, ant-colony-optimization]
related:
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[post-disaster-mec]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-substitution-relaying]]"
  - "[[ant-colony-optimization]]"
  - "[[fixed-wing-propulsion-energy-model]]"
created: 2026-07-12
updated: 2026-11-03
modeling_card: required
---

# Cost Optimization of UAV Swarm Network for Persistent Emergency Communication

## Citation

Liu, C., Xin, X., Dai, Y., & Xu, D. (2026). *Cost Optimization of UAV Swarm Network for Persistent Emergency Communication*. **IEEE Transactions on Green Communications and Networking**, 10, 1734-1748. DOI: 10.1109/TGCN.2025.3649278.

## TL;DR

Minimizes the number of fixed-wing UAVs needed to keep disaster-area access points continuously connected to a remote base/charging station. USP-NFRP combines periodic replacement loops, dynamically reconfigured tree backhaul, and max-min ant-system path planning so relay roles need not remain fixed throughout a mission.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A swarm $\mathcal M$ of homogeneous UAVs gives persistent multi-hop connectivity from target areas $\mathcal K$ to one base station at $B$, which is also the charging station. A link between nodes $p,q \in \mathcal T = \mathcal M \cup \{\text{station}\}$ exists when their horizontal distance is at most the relay range $D$, and flight power follows $P_f = c_1V^3 + c_2/V$.

**Problem & objective**: Problem (10) minimizes the fleet size, $\min |\mathcal M|$, jointly over access assignments, trajectories, and the backhaul topology.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Access assignment | $\alpha_{k,m}(t)$ | binary | UAV $m$ serves target area $k$ at time $t$ |
| Link selection | $\mu_{p,q}(t)$ | binary | Backhaul link between nodes $p$ and $q$ is used |
| UAV trajectory | $L_m(t)$ | continuous 2-D | Horizontal position of UAV $m$ |
| Fleet size | $\lvert\mathcal M\rvert = \sum_{r\in R} M_r$ | integer | Total UAVs, summed over periodic rotation paths $r$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (11)-(12) | Each UAV serves at most one target area, and each area is served by exactly one UAV at all times. |
| (13) | A link can be used only within range, $\mu_{p,q}(t) \le z_{p,q}(t)$. |
| (14)-(15) | At least one UAV links to the station, and every served area has a backhaul link. |
| (16)-(17) | Active links form a connected tree without cycles. |
| (18) | Residual energy covers the return flight, $E_m(t) \ge \frac{\lVert L_m(t)-B\rVert}{V}(P_c+P_f)$. |

**Algorithm**: The periodic rotation path (PRP) method builds rotation paths and computes each path's feasible replacement interval $\Delta t_r$ by linear programming, which fixes the UAVs $M_r$ per path. The dynamic tree backhaul link (DTBL) method keeps the tree connected as relay roles move, and the max-min ant system planner (MMAS-PP) searches paths and task sequences for the smallest feasible fleet.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied persistent emergency communication with a multi-hop UAV swarm and non-fixed relay points. They formulated a combinatorial fleet-planning problem that minimizes the number of fixed-wing UAVs while maintaining connected tree backhaul, target coverage, relay-range, energy-return, and periodic replacement constraints. The USP-NFRP scheme builds periodic rotation paths, uses dynamic tree backhaul links to repair connectivity when relay roles move, and applies an MMAS-PP max-min ant-system planner to select paths and schedules. A linear program determines each path's feasible replacement interval before the global candidate search. Simulations report up to 30.9% fewer UAVs than baselines that include a genetic-algorithm vehicle-routing strategy and the theoretical lower bound of direct replacement.

## Problem

Seven isolated target areas need persistent service through a multi-hop aerial backhaul to one distant, co-located base and charging station. Limited endurance forces UAV replacement, but fixing every relay point can waste aircraft. The joint association, trajectory, topology, and energy problem is a continuous-time combinatorial MINLP whose cost proxy is fleet size.

## System model

- Homogeneous fixed-wing UAVs fly at fixed altitude and constant speed, serve at most one target each, and form an acyclic connected tree back to the station.
- A bidirectional link exists when node separation is at most relay range `D`; the model does not include fading, interference, traffic, or link capacity.
- Propulsion and constant communication power consume energy, and each UAV must always retain enough energy to return. Recharge at the station is modeled as instantaneous restoration to full capacity.
- Decision variables cover target association, continuous trajectories, selected relay links, and indirectly the minimum fleet size.

## Method

The Periodic Rotation Path method builds closed station-to-station loops through access and relay tasks. UAVs on each path depart at that path's fixed interval and synchronously take over the next role; a small linear program maximizes each path's feasible replacement interval. The paper's comparison with direct replacement is conditional on the stated path-feasibility cases, not a universal dominance proof.

Dynamic Tree Backhaul Link logic tests whether nodes affected by a moving non-fixed relay can reconnect through a stable segment or other relays; otherwise that relay role becomes fixed. MMAS-PP then uses max-min ant-system pheromones, interval-change heuristics, fixed/non-fixed candidate states, and DTBL feasibility checks to build rotation paths. The reported overall complexity is `O(N^3)`, with connectivity checking identified as the scalability bottleneck.

## Key findings

- In the `20 km x 20 km` synthetic scenario with `D=8 km` and `T_max=60 min`, USP-NFRP uses 38 UAVs, versus 52 for PHRR and 55 for GA-VRP: reductions of `26.9%` and `30.9%`.
- Across tested relay ranges/endurance values, the paper reports an average `21.6%` fleet reduction, ranging from `11.7%` to `30.9%` versus baselines.
- The illustrated `D=8 km` plan maintains one rotation path with 10 UAVs, and the simulated topology trace retains a spanning tree without access-point-to-station disruption.

## Limitations / parse caveats

The study uses synthetic geometry, seven targets, homogeneous UAVs, deterministic distance-threshold links, constant communication power, and instantaneous recharge. Circular flight approximates hovering, while takeoff, acceleration, charge time, stochastic failures, throughput, and QoS are omitted. The paper scopes practical cubic complexity to roughly `N <= 50` and only proposes partitioned/incremental checks beyond that. Quantitative results come from simulation narrative, not field deployment. Publication metadata is absent from the parse and was verified through the exact-title Crossref record.

## Relation to the corpus

[[persistent-emergency-uav-swarm-service]] joins [[uav-substitution-relaying]] with route-level role rotation and tree-topology repair. Unlike one-link [[uav-mobile-relaying]], the design minimizes the fleet needed for a persistent multi-hop emergency network. It extends the infrastructure side of [[post-disaster-mec]] without modeling computation offloading.

## Raw artifacts

- Parse: `raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md`
- Origin PDF: `raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.pdf`
- Figures: `raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/images/`
