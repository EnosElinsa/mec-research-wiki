---
type: source
title: "Energy Minimization in UAV-Enabled Cargo Pickup Systems: A Radio Map-Aided Hierarchical Optimization Framework"
authors: ["Jiangling Cao", "Shi Peng", "Dingcheng Yang", "Qinghua Wu", "Tiankui Zhang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3639674"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
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
updated: 2026-07-14
---

# Energy Minimization in UAV-Enabled Cargo Pickup Systems: A Radio Map-Aided Hierarchical Optimization Framework

## Citation

Cao, J., Peng, S., Yang, D., Wu, Q., & Zhang, T. (2026). *Energy Minimization in UAV-Enabled Cargo Pickup Systems: A Radio Map-Aided Hierarchical Optimization Framework*. **IEEE Transactions on Intelligent Transportation Systems**, 27(3), 3669-3684. DOI: 10.1109/TITS.2025.3639674.

## TL;DR

Minimizes propulsion energy for one cellular-connected cargo UAV that must collect all known parcels over multiple warehouse-return trips. UPSEEO first thresholds a preconstructed expected-SNR map and uses A* to compute communication-feasible all-pairs paths. PSO then chooses trip partitioning and pickup order, while each segment's speed is derived from payload-dependent energy per distance.

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
