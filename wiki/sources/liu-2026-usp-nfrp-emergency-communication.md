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
updated: 2026-07-16
modeling_card: required
---

# Cost Optimization of UAV Swarm Network for Persistent Emergency Communication

## Citation

Liu, C., Xin, X., Dai, Y., & Xu, D. (2026). *Cost Optimization of UAV Swarm Network for Persistent Emergency Communication*. **IEEE Transactions on Green Communications and Networking**, 10, 1734-1748. DOI: 10.1109/TGCN.2025.3649278.

## TL;DR

Minimizes the number of fixed-wing UAVs needed to keep disaster-area access points continuously connected to a remote base/charging station. USP-NFRP combines periodic replacement loops, dynamically reconfigured tree backhaul, and max-min ant-system path planning so relay roles need not remain fixed throughout a mission.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fleet of homogeneous fixed-wing UAV relays provides persistent multi-hop emergency connectivity from several target areas to one remote base and charging station. Links are distance-threshold bidirectional links without fading/interference, and UAVs periodically rotate through relay roles.

**Problem & objective**: Persistent emergency swarm planning, a continuous-time combinatorial MINLP, minimizes fleet size, $\min M$, while maintaining a connected tree, target coverage, relay-range connectivity, energy-return feasibility, and periodic replacement schedules.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Target association | $a_{m,k}$ | binary | UAV/rotation path serves target area $k$ |
| Relay links | $e_{i,j}$ | binary | Selected backhaul edge between UAV roles/nodes |
| UAV trajectories | $\mathbf q_m(t)$ | continuous path | Flight path for fixed or rotating relay roles |
| Rotation interval | $\Delta_k$ | continuous, positive | Period between successive UAV takeovers on path $k$ |
| Fleet size | $M$ | integer | Number of UAVs required for persistent service |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The selected relay graph is connected and acyclic, linking every target to the station |
| C2 | Every link length stays within the relay range $D$ |
| C3 | UAVs follow fixed-altitude, fixed-speed paths and retain enough energy to return |
| C4 | Rotation intervals and path schedules permit seamless role replacement |
| C5 | Each UAV serves at most one target/relay role at a time and recharge restores the modeled energy state |

**Algorithm**: Construct periodic rotation paths and solve each path's feasible interval by linear programming → test dynamic tree backhaul links → use MMAS-PP max-min ant-system path planning with interval-change heuristics → retain feasible connected plans with minimum fleet size.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied persistent emergency communication with a multi-hop UAV swarm and non-fixed relay points. They formulated a combinatorial fleet-planning problem that minimizes the number of fixed-wing UAVs while maintaining connected tree backhaul, target coverage, relay-range, energy-return, and periodic replacement constraints. The USP-NFRP scheme builds periodic rotation paths, uses dynamic tree backhaul links to repair connectivity when relay roles move, and applies an MMAS-PP max-min ant-system planner to select paths and schedules. A linear program determines each path's feasible replacement interval before the global candidate search. Simulations report lower fleet size than direct-replacement, genetic, and other path-planning baselines in the stated synthetic emergency scenarios.

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
