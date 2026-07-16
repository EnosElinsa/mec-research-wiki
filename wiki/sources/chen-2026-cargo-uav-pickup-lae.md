---
type: source
title: "Cargo UAVs Pick-Up Systems for Low-Altitude Economy With Communication Quality, Battery Energy, and Time Window Constraints"
authors: ["Mingjian Chen", "Liang Yang", "Jiangling Cao", "Guangxu Zhu", "Weijie Yuan", "Hongbo Jiang", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3647000"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, low-altitude-intelligent-network, cellular-connected-uav, uav-trajectory-control, dueling-dqn, logistics, collision-avoidance]
related:
  - "[[guangxu-zhu]]"
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
  - "[[cao-2026-radio-map-cargo-pickup]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[weijie-yuan]]"
created: 2026-07-06
updated: 2026-07-16
---

# Cargo UAVs Pick-Up Systems for Low-Altitude Economy With Communication Quality, Battery Energy, and Time Window Constraints

## Citation

Chen, M., Yang, L., Cao, J., Zhu, G., Yuan, W., Jiang, H., & Niyato, D. (2026). *Cargo UAVs Pick-Up Systems for Low-Altitude Economy With Communication Quality, Battery Energy, and Time Window Constraints*. **IEEE Transactions on Mobile Computing**, 25(6), 8111-8128. DOI: 10.1109/TMC.2025.3647000.

## TL;DR

Studies cooperative cargo-pickup route planning for cellular-connected UAVs in the low-altitude economy. The proposed CACMO framework combines D3QN trajectory learning, simulated-annealing pickup-sequence planning, and explicit inter-UAV conflict resolution so multiple cargo UAVs can satisfy communication-quality, battery-energy, time-window, and collision-avoidance constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple cargo UAVs depart from and return to a warehouse while visiting pickup points. Each route must maintain cellular coverage, respect battery and payload limits, meet pickup time windows, and keep safe separation from other UAVs.

**Problem & objective**: The mixed-integer trajectory and scheduling problem $P_0$ maximizes weighted customer satisfaction minus completion time, $\max_{\mathbf p_{\mathrm{uav}}(t),O,g_{\mathrm{uav}}(t),V_{\mathrm{uav}}(t)}\;\mu_1S_{\mathrm{us}}-\mu_2T_c$, subject to route, communication, energy, time-window, payload, speed, and collision constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf p_{\mathrm{uav}}(t)$ | continuous 3-D vector | Location of each cargo UAV over time |
| Pickup order | $O$ | discrete permutation | Sequence in which pickup points are served |
| GBS association | $g_{\mathrm{uav}}(t)$ | discrete index | Serving ground base station for each UAV and slot |
| UAV speed | $V_{\mathrm{uav}}(t)$ | continuous, $[0,V_{\max}]$ | Flight speed along the route |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Warehouse departure and return: $\mathbf p_{\mathrm{uav}}(0)=\mathbf p_{\mathrm{uav}}(T_c)=\mathbf d_0$. |
| C2 | Every pickup point is visited: $\mathbf p_q(t)=\mathbf d_k$ for each assigned pickup point. |
| C3 | Horizontal flight region is bounded: $0\le x_{\mathrm{uav}}(t),y_{\mathrm{uav}}(t)\le I$. |
| C4 | Altitude is bounded: $0\le H_{\mathrm{uav}}(t)\le H_{\max}$. |
| C5 | Payload never exceeds capacity: $\sum_{n=1}^{K}w_k\le w_{\max}$. |
| C6 | Speed is bounded: $0\le V_{\mathrm{uav}}(t)\le V_{\max}$. |
| C7 | Cellular outage probability remains below threshold: $\widehat P_{\mathrm{out}}(\mathbf p_n,g_{\mathrm{uav}})\le P_{\mathrm{th}}$. |
| C8 | Flight-energy and inter-UAV collision constraints from (20) and (25)-(26) are satisfied. |

**Algorithm**: Train an online D3QN for communication-aware point-to-point trajectories, use simulated annealing to search pickup sequences from learned pairwise costs, detect route conflicts, add collision penalties and retrain D3QN, then repeat sequence search until all routes are feasible.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied multi-UAV cargo pickup route planning and task scheduling under cellular communication, battery, time-window, payload, and collision constraints. They formulated a weighted objective that maximizes customer satisfaction while minimizing total completion time over UAV trajectories, pickup order, GBS association, and speed. CACMO combines online D3QN trajectory learning, simulated-annealing pickup-sequence search, and alternating collision detection with penalty-based D3QN retraining. Simulations reported 1719 s task completion time, 0.9969 customer satisfaction, and a 70-75% reduction in total weighted cost against representative baselines.

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

This source extends the [[low-altitude-intelligent-network]] thread from network architecture into cargo-UAV logistics. It is closest to the [[cellular-connected-uav]] side of the UAV literature because the UAV is an aerial cellular user that must maintain GBS connectivity, rather than an aerial MEC server serving ground devices. The D3QN component reinforces [[dueling-dqn]] as a trajectory-control backbone, while the collision-aware multi-UAV refinement connects to the broader [[uav-trajectory-control]] vocabulary. [[cao-2026-radio-map-cargo-pickup]] provides the complementary offline [[radio-map-aided-uav-path-planning]] design for one UAV, using A* paths, PSO allocation, and payload-aware speeds instead of local-measurement learning and multi-UAV conflict resolution. Co-author [[dusit-niyato]] links this paper to the wiki's recurring aerial resource-management and generative-AI cluster.

## Raw artifacts

- `raw/sources/Cargo_UAVs_Pick-Up_Systems_for_Low-Altitude_Economy_With_Communication_Quality_Battery_Energy_and_Time_Window_Constraints/Cargo_UAVs_Pick-Up_Systems_for_Low-Altitude_Economy_With_Communication_Quality_Battery_Energy_and_Time_Window_Constraints.md`
- Original PDF and extracted figures (`images/`) in the same folder.
