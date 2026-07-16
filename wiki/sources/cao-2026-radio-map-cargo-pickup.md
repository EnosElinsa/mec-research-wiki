---
type: source
title: "Energy Minimization in UAV-Enabled Cargo Pickup Systems: A Radio Map-Aided Hierarchical Optimization Framework"
authors: ["Jiangling Cao", "Shi Peng", "Dingcheng Yang", "Qinghua Wu", "Tiankui Zhang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3639674"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, cargo-uav, logistics, radio-map, cellular-connected-uav, trajectory-planning, energy-minimization, particle-swarm-optimization]
related:
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[particle-swarm-optimization]]"
  - "[[energy-latency-tradeoff]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[dingcheng-yang]]"
  - "[[tiankui-zhang]]"
created: 2026-07-13
updated: 2026-07-16
---

# Energy Minimization in UAV-Enabled Cargo Pickup Systems: A Radio Map-Aided Hierarchical Optimization Framework

## Citation

Cao, J., Peng, S., Yang, D., Wu, Q., & Zhang, T. (2026). *Energy Minimization in UAV-Enabled Cargo Pickup Systems: A Radio Map-Aided Hierarchical Optimization Framework*. **IEEE Transactions on Intelligent Transportation Systems**, 27(3), 3669-3684. DOI: 10.1109/TITS.2025.3639674.

## TL;DR

Minimizes propulsion energy for one cellular-connected cargo UAV that must collect all known parcels over multiple warehouse-return trips. UPSEEO first thresholds a preconstructed expected-SNR map and uses A* to compute communication-feasible all-pairs paths. PSO then chooses trip partitioning and pickup order, while each segment's speed is derived from payload-dependent energy per distance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One cargo UAV starts and ends every trip at a warehouse, collects one known parcel from each fixed pickup point, and cruises horizontally at a fixed altitude after vertical ascent. A physical-map-derived expected-SNR grid captures cellular coverage, and a payload-dependent rotary-wing propulsion model accounts for horizontal and ascent energy while communication and descent energy are neglected.

**Problem & objective**: Problem P0 is a mixed-integer nonlinear program that minimizes total propulsion energy, $\mathrm{P0}:\min_{\mathcal Q,\Pi,\mathcal V}E_{\mathrm{total}}$, over trajectories, pickup allocation and order, and flight speeds.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectories | $\mathcal Q$ | continuous paths, later discretized to feasible grids | Flight path for every warehouse and pickup-point segment |
| Trip allocation and pickup order | $\Pi=\{\Pi_1,\ldots,\Pi_K\}$ | discrete sequences | Partition of pickup points into warehouse-return trips and their visit order |
| Flight speeds | $\mathcal V$ | continuous, $0\leq\|\mathbf v_k(t)\|\leq V_{\max}$ | Payload-dependent speed along each segment |
| Parcel pickup indicator | $I_{k,m}(t)$ | binary, $\{0,1\}$ | Whether parcel $m$ is collected during trip $k$ at time $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 4 and 28c | Every trip starts and ends at the warehouse, $\pi_{k,0}=\pi_{k,M_k}=0$ and $\mathbf q_k(0)=\mathbf q_k(T_k)=(x_0,y_0,0)$ |
| 6-7 | Pickup is binary and each parcel is collected exactly once, $I_{k,m}(t)\in\{0,1\}$ and $\sum_k\int_0^{T_k}I_{k,m}(t)dt=1$ |
| 8 | Payload stays legal, $W_k(t)\leq W_{\max}$ |
| 16 and 29e | Communication remains feasible, $\bar\gamma(\mathbf q_i^j(t))\geq\gamma_{th}$ along every path |
| 23 | Each trip respects onboard energy, $E_k(t)\leq E_{\max}$ |
| 28a-28b | Motion follows $\dot{\mathbf q}_k(t)=\mathbf v_k(t)$ with $0\leq\|\mathbf v_k(t)\|\leq V_{\max}$ |

**Algorithm**: UPSEEO thresholds the expected-SNR map into a binary feasible grid and runs eight-neighbor A* for every ordered warehouse and pickup-point pair to build trajectory and distance matrices. PSO then searches the trip partition and pickup order, while each segment speed is derived from $\arg\min_{0\leq\|\mathbf v\|\leq V_{\max}}P_{\mathrm{hor}}(\|\mathbf v\|,W)/\|\mathbf v\|$ and assignments violating payload or energy limits are rejected.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cao et al. [x] studied propulsion-energy minimization for a cellular-connected cargo UAV that collects known parcels over one or more warehouse-return trips under coverage, payload, and onboard-energy limits. They formulated a mixed-integer nonlinear problem over flight trajectories, pickup allocation and order, and payload-dependent speed to minimize total vertical and horizontal propulsion energy while every parcel is collected exactly once. The UPSEEO framework thresholds a physical-map-derived expected-SNR map, computes all-pairs communication-feasible paths with eight-neighbor A*, and then uses PSO for trip allocation while deriving each segment's speed from minimum energy per distance. Simulations report about 5.0% to 50.0% lower total energy than the comparison frameworks, including 20.749 kJ for the reported 1431.84 m path carrying 10 N.

## Problem framing

Shortest cargo routes can cross urban coverage holes, and the energy-minimizing speed changes as parcels accumulate. Limited payload and onboard energy may also force several warehouse-return trips. The paper therefore separates communication-safe path construction from route allocation and speed selection instead of solving one monolithic trajectory problem.

## System model

- One UAV serves fixed pickup points with known parcel weights from a central warehouse. Every trip starts and ends at the warehouse, every parcel is collected once, and payload and onboard-energy limits hold per trip.
- The UAV ascends and descends above the warehouse or pickup points, then cruises horizontally at one fixed altitude. Full 3-D trajectory optimization is not performed.
- A physical-map-derived channel-gain map supplies expected SNR from terrestrial base stations. At each grid point the UAV associates with the base station providing the largest expected SNR.
- A grid is communication-feasible only when expected SNR exceeds a threshold. OFDM is assumed to suppress interference from non-associated base stations.
- The propulsion model depends on speed and carried payload. Communication energy is ignored relative to propulsion, and descent is treated as approximately unpowered autorotation.

## Method

The [[radio-map-aided-uav-path-planning|radio-map path-planning]] stage thresholds the SNR map into a binary feasible grid. Eight-neighbor A* then computes the shortest feasible path and distance between every ordered warehouse/pickup pair, producing reusable trajectory and distance matrices.

The allocation stage uses [[particle-swarm-optimization|PSO]] particles to encode trip partitioning and pickup order. Once a particle fixes the payload on each segment, speed is derived by minimizing payload-dependent propulsion energy per distance. Fitness combines vertical and horizontal energy, with infeasible payload or energy assignments rejected. Thus PSO searches allocation, while speed is determined conditionally rather than being an independent particle coordinate.

## Key findings

- For one 1431.84 m warehouse-to-pickup path carrying 10 N, UPSEEO reports 20.749 kJ at its optimized speed, below the compared Dijkstra fixed-speed, DRL fixed-speed, RRT fixed-speed, and DRL optimized-speed variants.
- Across the tested pickup-point counts, the prose reports approximately 5.0%-50.0% lower energy consumption than the comparison frameworks.
- Increasing payload and onboard energy reduces the number of required warehouse-return trips in the stated examples: from eight trips at 20 N/120 kJ to six with 30 N payload, five after raising energy to 200 kJ, and four with 40 N payload.
- The altitude table reports a first-decrease-then-increase total energy trend: 653.60 kJ at 50 m, a minimum listed 645.47 kJ at 60 m, and 670.40 kJ at 90 m. Better LoS coverage shortens horizontal detours, but ascent energy grows.
- Minimum horizontal power is reported near 20-25 m/s for the tested 50 N UAV, whereas minimum energy per meter occurs near 25-30 m/s; payload shifts the optimum.

## Limitations / future work

Planning uses a static expected-SNR map and omits instantaneous channel variation and base-station handover delay. Constructing the map requires an accurate physical map, and the grid-resolution accuracy/computation tradeoff is deferred. The design has one UAV, known static requests, fixed-altitude 2-D paths, ignored communication energy, negligible descent energy, and no explicit obstacle/no-fly-zone constraint beyond blockage encoded in the radio map. PSO has no global-optimality guarantee. Future work covers dynamic channels, handovers, full 3-D paths, and heterogeneous multi-UAV pickup.

## Relation to the corpus

This source belongs to the adjacent UAV-logistics branch rather than MEC offloading. It adds a communication-map-driven route layer to [[uav-delivery-pickup-dropoff]]. [[chen-2026-cargo-uav-pickup-lae]] instead learns point-to-point connectivity-aware trajectories from local measurements, then uses simulated annealing and explicit inter-UAV conflict resolution. [[lee-2026-uav-delivery-time-energy]] optimizes pickup/drop-off indicators and continuous 3-D trajectories under no-fly zones. The present paper is distinguished by an offline expected-SNR map, all-pairs A* paths, PSO trip allocation, and payload-aware speed derivation.

## Raw artifacts

- Parse: `raw/sources/Energy_Minimization_in_UAV-Enabled_Cargo_Pickup_Systems_A_Radio_Map-Aided_Hierarchical_Optimization_Framework/Energy_Minimization_in_UAV-Enabled_Cargo_Pickup_Systems_A_Radio_Map-Aided_Hierarchical_Optimization_Framework.md`
- Origin PDF: `raw/sources/Energy_Minimization_in_UAV-Enabled_Cargo_Pickup_Systems_A_Radio_Map-Aided_Hierarchical_Optimization_Framework/Energy_Minimization_in_UAV-Enabled_Cargo_Pickup_Systems_A_Radio_Map-Aided_Hierarchical_Optimization_Framework.pdf`
- Figures: `raw/sources/Energy_Minimization_in_UAV-Enabled_Cargo_Pickup_Systems_A_Radio_Map-Aided_Hierarchical_Optimization_Framework/images/`
