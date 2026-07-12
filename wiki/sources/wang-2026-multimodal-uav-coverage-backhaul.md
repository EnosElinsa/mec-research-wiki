---
type: source
title: "Dynamic Multi-Modal UAV Control for Optimized Coverage and Backhaul Connectivity in Spatially Unstructured and Dispersed User Environments"
authors: ["Yuhui Wang", "Junaid Farooq", "Juntao Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3606778"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, multi-uav, communication-coverage, wireless-backhaul, distributed-control, flocking, network-resilience]
related:
  - "[[multi-modal-uav-coverage-backhaul-control]]"
  - "[[wireless-backhaul]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-13
updated: 2026-07-13
---

# Dynamic Multi-Modal UAV Control for Optimized Coverage and Backhaul Connectivity in Spatially Unstructured and Dispersed User Environments

## Citation

Wang, Y., Farooq, J., & Chen, J. (2026). *Dynamic Multi-Modal UAV Control for Optimized Coverage and Backhaul Connectivity in Spatially Unstructured and Dispersed User Environments*. **IEEE Transactions on Mobile Computing**, 25(2), 2320-2334. DOI: 10.1109/TMC.2025.3606778.

## TL;DR

Uses local flocking, potential fields, and distributed tree formation to switch UAV mobile access points among exploration, user service, and bridge roles. The controller covers irregular user clusters, maintains inter-cluster backhaul, and reallocates surviving UAVs after random failures.

## Problem

UAV access networks in remote or emergency regions must cover users whose exact locations are unknown and spatially dispersed, while preserving an air-to-air backhaul between separated clusters. Static placement and one-mode flocking can either leave coverage gaps or concentrate too many UAVs on connectivity.

## System model

- Ground mobile devices form geographic clusters on a two-dimensional plane. UAV mobile access points use omnidirectional antennas, observe only nearby users, and exchange information with communication neighbors.
- Air-to-air links use a range-limited, interference-aware SINR model with Nakagami fading; the [[air-to-ground-channel-model]] uses probabilistic LoS/NLoS loss and inter-UAV interference.
- User coverage is the fraction associated with a UAV at sufficient SINR. Backhaul connectivity is measured by the graph Laplacian's Fiedler value, which is positive for a connected UAV graph.
- Exact user positions are unavailable, but cluster centers or concentration areas are assumed known for mode selection.

## Method

[[multi-modal-uav-coverage-backhaul-control]] switches each UAV among three roles: exploration toward an uncovered cluster, minimum-spanning-tree bridge formation, and static service near a locally estimated user centroid. Coverage and served-user thresholds determine mode changes.

The control law combines inter-UAV attraction/repulsion, velocity consensus and load balancing, plus role-specific goal or bridge potentials. A smooth log-sum-exp minimum fuses coverage and connectivity objectives. The continuous-time Lyapunov analysis shows the aggregate potential is non-increasing and converges to an initialization-dependent local equilibrium; discrete-time execution requires sufficiently small steps.

## Key findings

- Simulations use communication range `24 m`, minimum inter-UAV distance `20 m`, altitude `20 m`, transmit power `10 W`, and service capacity 80 users per UAV.
- Across 50-100 UAVs, peak coverage reaches `98.5%` with 90 UAVs. The highest reported post-convergence Fiedler value is `0.021` with 100 UAVs.
- Random failures occur at 55 s. Coverage remains approximately `85%` at a `30%` failure rate, while higher failure rates weaken inter-cluster connectivity.
- With only 50 UAVs, failure rates above `40%` prevent full connectivity recovery.
- Fewer than 65 UAVs cannot connect all four user clusters; connectivity rises sharply from 65-80 UAVs and then more slowly through 120.

## Limitations / parse caveats

Evidence is simulation-only. Mode thresholds are fixed, exact cluster centers are assumed known, and convergence is local and initialization-dependent. The prose describes a local coverage ratio for switching, whereas the displayed algorithms update and test a network-wide ratio; the page therefore does not resolve the trigger's scope. The parse also conflicts on total user population (500 total, 500 per cluster, or 100 per cluster), on a 30 s versus 40 s convergence time, and on which inter-UAV spacings were tested. The displayed centroid update does not visibly include the neighbor-centroid term described in prose, so no stronger average-consensus claim is made. The parse lacks publication metadata and identifies a distinct ICC 2022 preliminary version; the final 2026 TMC record was verified through the exact-title Crossref entry.

## Relation to the corpus

This source complements [[wang-2025-ppo-uav-positioning-offloading]], by the same Yuhui Wang/Junaid Farooq pair, with distributed non-learning control for irregular coverage, [[wireless-backhaul]], and failure recovery. It also differs from [[zheng-2026-active-search-low-altitude-uav]], which searches for unknown users while treating a backhaul constraint, rather than switching UAVs among persistent coverage and bridge roles.

## Raw artifacts

- Parse: `raw/sources/Dynamic_Multi-Modal_UAV_Control_for_Optimized_Coverage_and_Backhaul_Connectivity_in_Spatially_Unstructured_and_Dispersed_User_Environments/Dynamic_Multi-Modal_UAV_Control_for_Optimized_Coverage_and_Backhaul_Connectivity_in_Spatially_Unstructured_and_Dispersed_User_Environments.md`
- Origin PDF: `raw/sources/Dynamic_Multi-Modal_UAV_Control_for_Optimized_Coverage_and_Backhaul_Connectivity_in_Spatially_Unstructured_and_Dispersed_User_Environments/Dynamic_Multi-Modal_UAV_Control_for_Optimized_Coverage_and_Backhaul_Connectivity_in_Spatially_Unstructured_and_Dispersed_User_Environments.pdf`
- Figures: `raw/sources/Dynamic_Multi-Modal_UAV_Control_for_Optimized_Coverage_and_Backhaul_Connectivity_in_Spatially_Unstructured_and_Dispersed_User_Environments/images/`
