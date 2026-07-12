---
type: source
title: "Dynamic Trajectory Optimization and Power Control for Hierarchical UAV Swarms in 6G Aerial Access Network"
authors: ["Ziye Jia", "Jia He", "Lijun He", "Min Sheng", "Junyu Liu", "Qihui Wu", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3603432"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 3349-3362"
tags: [source, hierarchical-uav-swarm, uav-data-collection, multi-objective-optimization, trajectory-control, power-control, whale-optimization]
related:
  - "[[hierarchical-uav-swarm]]"
  - "[[uav-data-collection]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[whale-optimization-algorithm]]"
  - "[[energy-latency-tradeoff]]"
  - "[[ziye-jia]]"
  - "[[qihui-wu]]"
  - "[[zhu-han]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
created: 2026-07-13
updated: 2026-07-13
---

# Dynamic Trajectory Optimization and Power Control for Hierarchical UAV Swarms in 6G Aerial Access Network

## Citation

Jia, Z., He, J., He, L., Sheng, M., Liu, J., Wu, Q., & Han, Z. (2026). *Dynamic Trajectory Optimization and Power Control for Hierarchical UAV Swarms in 6G Aerial Access Network*. **IEEE Transactions on Wireless Communications**, 25, 3349-3362. DOI: 10.1109/TWC.2025.3603432. The parsed early-access copy reports online publication in September 2025; the final Crossref record assigns the 2026 volume.

## TL;DR

A fixed fleet is divided into [[hierarchical-uav-swarm|hierarchical UAV swarms]] whose head UAVs coordinate tail UAVs for two-hop ground-user data collection. K-means/Voronoi predeployment fixes swarm locations and user associations, then an improved non-dominated-sorting whale optimizer jointly selects tail-UAV routes and ground/relay transmit powers over UAV energy, user energy, and delay objectives.

## Problem

One UAV cannot efficiently collect delay-sensitive data over a large remote area. The paper asks how to divide a fixed multi-UAV fleet into swarms, deploy their head UAVs, assign users and tail UAVs, and jointly control routes and powers without collapsing UAV energy, ground-user energy, and transmission delay into one metric.

## System model

- Each swarm has one stationary head UAV acting as an aerial base station and an optimized number of tail UAVs that collect data and relay it to the head.
- A tail UAV follows a successive-hover-and-fly route from its head UAV, serving users at hover points before the air-to-air relay hop. OFDMA removes modeled intra-hop interference, and communication during flight is disabled.
- User delay combines ground-to-air upload and air-to-air relay time. Energy includes user transmission, tail-UAV relay/hover/flight consumption, and head-UAV hovering until the slowest tail completes.
- The three objectives are total swarm energy, average ground-user energy, and average ground-user delay under fleet, rate, association, capacity, delay, position, route, and power constraints.

## Method

The predeployment stage clusters users into as many groups as there are tail UAVs, forms a Voronoi diagram from cluster centers, selects swarm sites from Voronoi intersections, allocates tail UAVs, and derives Fermat/geometric-median hover points. This fixes deployment, fleet allocation, and user-hover associations.

The remaining route-and-power problem is solved with INS-WOA. Candidate solutions are ranked by non-dominated sorting and crowding distance; whale encircling, spiral, and random-search updates explore transmit powers, while a greedy objective-change score builds each tail UAV's hover-point order. The output is a Pareto set rather than a claimed global optimum.

## Key findings

- Simulations use a synthetic `2000 x 2000 x 120 m^3` region with three head UAVs, eight tail UAVs, and up to three tail UAVs per swarm; no trace or hardware data are used.
- As user count increases, average user energy remains near `0.02 J` and is reported as `30%` lower than MOGWO and NSGA-II.
- For a 60-user compromise solution, `80%` of users transmit at `0-0.5 W`; the user-energy-focused solution places `70%` below `0.25 W`, while the delay-focused solution places `60%` above `0.75 W`.
- The compromise solution is not the best-delay point: it deliberately sacrifices transmission delay to reduce UAV and user energy.

## Limitations / parse caveats

The method is centralized and simulation-only, requires fixed user coordinates and global fleet information, and freezes deployment/association before route and power optimization. The model omits an explicit obstacle or collision constraint, assumes common tail-UAV speed, ignores air-to-air NLoS fading, and forces every user through the fixed fleet. The abstract's `50%` complexity-reduction claim has no named baseline in the parsed results. The delay cap is `0.4 s` in the parameter table but `0.5 s` in prose, and several equations/algorithm symbols are OCR-damaged.

## Relation to the corpus

This source uses an intra-swarm head/tail communication hierarchy, distinct from the UAV-HAPS compute tiers in [[hierarchical-aerial-mec]]. It extends [[uav-data-collection]] and [[uav-mobile-relaying]] with a multi-objective fleet/deployment stage and sits beside [[jia-2025-dro-uav-hap-mec]] as a WOA-family aerial optimizer, but it does not model MEC task execution.

## Raw artifacts

- Parse: `raw/sources/Dynamic_Trajectory_Optimization_and_Power_Control_for_Hierarchical_UAV_Swarms_in_6G_Aerial_Access_Network/Dynamic_Trajectory_Optimization_and_Power_Control_for_Hierarchical_UAV_Swarms_in_6G_Aerial_Access_Network.md`
- Origin PDF: `raw/sources/Dynamic_Trajectory_Optimization_and_Power_Control_for_Hierarchical_UAV_Swarms_in_6G_Aerial_Access_Network/Dynamic_Trajectory_Optimization_and_Power_Control_for_Hierarchical_UAV_Swarms_in_6G_Aerial_Access_Network.pdf`
- Figures: `raw/sources/Dynamic_Trajectory_Optimization_and_Power_Control_for_Hierarchical_UAV_Swarms_in_6G_Aerial_Access_Network/images/`
