---
type: source
title: "Cargo UAVs Pick-Up Systems for Low-Altitude Economy With Communication Quality, Battery Energy, and Time Window Constraints"
authors: ["Mingjian Chen", "Liang Yang", "Jiangling Cao", "Guangxu Zhu", "Weijie Yuan", "Hongbo Jiang", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3647000"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-intelligent-network, cellular-connected-uav, uav-trajectory-control, dueling-dqn, logistics, collision-avoidance]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[dueling-dqn]]"
  - "[[deep-q-network]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[gao-2024-d3qn-uav-mec-mobile-gt]]"
  - "[[dusit-niyato]]"
created: 2026-07-06
updated: 2026-07-12
---

# Cargo UAVs Pick-Up Systems for Low-Altitude Economy With Communication Quality, Battery Energy, and Time Window Constraints

## Citation

Chen, M., Yang, L., Cao, J., Zhu, G., Yuan, W., Jiang, H., & Niyato, D. (2026). *Cargo UAVs Pick-Up Systems for Low-Altitude Economy With Communication Quality, Battery Energy, and Time Window Constraints*. **IEEE Transactions on Mobile Computing**, 25(6), 8111-8128. DOI: 10.1109/TMC.2025.3647000.

## TL;DR

Studies cooperative cargo-pickup route planning for cellular-connected UAVs in the low-altitude economy. The proposed CACMO framework combines D3QN trajectory learning, simulated-annealing pickup-sequence planning, and explicit inter-UAV conflict resolution so multiple cargo UAVs can satisfy communication-quality, battery-energy, time-window, and collision-avoidance constraints.

## Problem framing

Cargo UAV logistics needs more than a shortest path. The UAVs must stay connected to terrestrial ground base stations, avoid energy depletion, meet user pickup time windows, and avoid each other in dense task areas. The paper argues that prior cargo-UAV logistics work usually handles only part of this constraint set, often assumes a known radio map, or omits multi-UAV collision avoidance.

The resulting optimization is a non-convex multi-objective trajectory and task-scheduling problem: minimize task completion time while maximizing user satisfaction under communication outage, energy, time-window, and safe-separation constraints.

## System model

- Multiple UAVs depart from and return to a central warehouse while visiting fixed pickup points.
- Cellular connectivity is constrained by ground base stations, sectorized antennas, LoS/NLoS path loss, building blockage, and SIR/outage probability.
- User service quality is represented through hard/soft time windows and a satisfaction function.
- UAV energy includes flight and payload effects; a UAV may return for battery replacement when needed.
- A minimum inter-UAV separation constraint is enforced outside the warehouse shield zone.

## Method

- A D3QN module learns communication-aware point-to-point trajectories from local link-quality measurements, avoiding poor-coverage regions without requiring an a priori radio map.
- A simulated-annealing module solves the pickup sequence over the D3QN-derived pairwise trajectory costs, incorporating time-window and energy feasibility.
- CACMO alternates between sequence planning and conflict-free refinement: detected trajectory conflicts feed a collision penalty into retraining until safe multi-UAV routes are obtained.
- The objective converts task time and satisfaction into a weighted cost, so operators can tune the time-vs-satisfaction priority.

## Key findings

- Under the representative operating setting in the abstract and Table III, CACMO reports 1719 s completion time and 0.9969 customer satisfaction.
- The abstract reports a 70-75% reduction in total weighted cost versus representative baselines while maintaining zero communication outage and safe inter-UAV separation.
- Lower outage-probability thresholds force routes away from poor-coverage regions and can lengthen paths, exposing the connectivity-vs-time trade-off.
- Increasing battery capacity reduces warehouse-return frequency, lowers time cost, and improves time-window satisfaction until the route has enough energy flexibility.
- Table III shows the tunable objective behavior: as the satisfaction/time weight ratio increases, satisfaction rises from 0.8234 to 1.0 while completion time rises from 1455.0 s to 1753.5 s.

## Limitations / future work

The authors state that the paper does not address 3D trajectory optimization. They name obstacle avoidance, flight safety across different altitudes, and mobile users with dynamic pickup requests as future extensions.

## Relation to the corpus

This source extends the [[low-altitude-intelligent-network]] thread from network architecture into cargo-UAV logistics. It is closest to the [[cellular-connected-uav]] side of the UAV literature because the UAV is an aerial cellular user that must maintain GBS connectivity, rather than an aerial MEC server serving ground devices. The D3QN component reinforces [[dueling-dqn]] as a trajectory-control backbone, while the collision-aware multi-UAV refinement connects to the broader [[uav-trajectory-control]] vocabulary. Co-author [[dusit-niyato]] links it to the wiki's recurring aerial resource-management and generative-AI cluster.

## Raw artifacts

- `raw/sources/Cargo_UAVs_Pick-Up_Systems_for_Low-Altitude_Economy_With_Communication_Quality_Battery_Energy_and_Time_Window_Constraints/Cargo_UAVs_Pick-Up_Systems_for_Low-Altitude_Economy_With_Communication_Quality_Battery_Energy_and_Time_Window_Constraints.md`
- Original PDF and extracted figures (`images/`) in the same folder.
