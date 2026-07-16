---
type: source
modeling_card: required
title: "Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems"
authors: ["Zhe Zhang", "Ju Jiang", "Keck Voon Ling", "Xinhua Wang", "Wen-An Zhang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3667967"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, low-altitude-economy, uav-enabled-its, multi-uav, task-allocation, path-planning, potential-game, a-star]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[uav-enabled-its]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[uav-trajectory-control]]"
  - "[[collision-avoidance-mgi]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-07-06
updated: 2026-07-16
---

# Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems

## Citation

Zhang, Z., Jiang, J., Ling, K. V., Wang, X., & Zhang, W.-A. (2026). *Cooperative Task Allocation and Path Planning for Multi-UAVs in Low-Altitude Urban Intelligent Transportation Systems*. **IEEE Transactions on Intelligent Transportation Systems**, 27(4), 4112-4124. DOI: 10.1109/TITS.2026.3667967.

## TL;DR

A distributed multi-UAV mission-planning framework for low-altitude urban intelligent transportation systems (LU-ITS). The paper couples two decisions that are often separated: which UAVs should execute each emergency-rescue or cargo-delivery task, and how each UAV should fly collision-free paths through a constrained urban low-altitude environment. Task allocation is modeled as an evolutionary [[potential-game]] solved by an Improved Log-linear Learning Algorithm (ILLA); path planning is solved by a Constraint-Based Multilayer Bidirectional Adaptive A-Star (CBMBA A-Star) search. Simulations report higher task reward and shorter execution / runtime than the listed baselines.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple communicating UAVs cooperatively execute emergency-rescue or last-mile delivery tasks in low-altitude urban airspace with buildings, no-fly zones, and changing threats. A high-level potential game assigns multi-UAV tasks, and a low-level graph search enforces kinematic and collision-avoidance feasibility.

**Problem & objective**: The high-level combinatorial potential-game model maximizes global mission utility, $\max J=\sum_{T_j\in\mathcal T}[B(T_j)-F(T_j)-G(T_j)]=\sum_i\sum_jU_i(T_j,\mathcal A_{T_j})x_{ij}$, before collision-free path construction.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task assignment | $x_{ij}$ | binary | Whether UAV $a_i$ executes task $T_j$ |
| Game strategy | $s_i$ | discrete task and position state | Task choice and relative position selected by UAV $i$ |
| UAV translational control | $u_i(t)$ | continuous, bounded | Acceleration used by the low-level kinematic model |
| UAV angular controls | $u_{\psi_i}(t),u_{\theta_i}(t),u_{\vartheta_i}(t)$ | continuous, bounded | Yaw, roll, and pitch angular rates |
| Search node and step | $k,L_i$ | discrete node and positive step | Successive path node and adaptive graph-search distance |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each UAV is assigned to at most one task, $\sum_jx_{ij}\le1$ |
| C2 | Assigned UAV payloads collectively satisfy each task's required load vector |
| C3 | Flight range, speed, altitude, response time, and angular-rate limits follow Eqs. (1) and (7) |
| C4 | Planned paths avoid buildings, no-fly zones, and bandit threats |
| C5 | UAV pairs maintain minimum safe separation and feasible turning angles |
| C6 | Low-level path planning rejects a high-level assignment if no executable kinematic path exists |

**Algorithm**: Define task reward, path cost, load cost, and the potential function → let neighboring UAVs update task strategies with ILLA and a time-varying Boltzmann parameter → converge to the optimal Nash-equilibrium set → run multilayer bidirectional CBMBA A-Star for each assignment → enforce turning, separation, obstacle, and threat constraints → adapt the search step for online replanning.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied cooperative task allocation and path planning for multiple UAVs in low-altitude urban intelligent transportation systems. They modeled task allocation as a network evolutionary potential game that maximizes task rewards minus path and payload costs under assignment, payload, flight-range, speed, altitude, and attitude-rate limits. Their Improved Log-linear Learning Algorithm uses derived Boltzmann parameters and converges to the optimal Nash equilibrium with probability one. A Constraint-Based Multilayer Bidirectional Adaptive A-Star algorithm then generates collision-free paths under urban obstacles, no-fly zones, turning constraints, and dynamic threats. Simulations for emergency rescue and last-mile delivery report an 11.67% task-reward increase, a 37.41% task-execution-time reduction, and a 61.02% runtime reduction relative to the stated baseline method.

## Problem

Low-altitude urban traffic applications need coordinated UAV fleets, not isolated single-UAV routes. Emergency rescue and last-mile delivery tasks can require multiple UAVs, while paths must respect minimum safe separation, turning-angle limits, speed bounds, obstacles, and bandit threats. The paper targets a distributed decision process where UAVs exchange neighborhood state and iteratively update strategies until reaching a stable task-allocation / path-planning solution.

## System model

- **Scenario:** LU-ITS missions for traffic emergency rescue and last-mile cargo transportation / delivery.
- **Agents:** multiple UAVs that communicate with neighboring UAVs and update state iteratively.
- **Tasks:** each task has mission reward, demand, and execution constraints; some tasks require cooperative assignment by multiple UAVs.
- **Constraints:** safe separation, turning-angle limits, velocity bounds, load / path costs, and urban threats / obstacles.
- **Objective:** maximize mission reward while accounting for path and load costs, then generate feasible collision-free paths for the assigned UAVs.

## Method

The task-allocation part is an evolutionary potential game. The paper analytically derives the potential function and proves a Nash equilibrium exists. ILLA then uses derived Boltzmann parameters so the algorithm converges to the optimal Nash equilibrium with probability one.

The path-planning part is CBMBA A-Star: a graph-search planner that combines constraint handling, multilayer search, bidirectional search, and adaptive replanning to generate optimal collision-free UAV paths in the low-altitude urban environment.

## Key findings

- The abstract reports that the proposed approach improves task reward by **11.67%**, reduces task execution time by **37.41%**, and decreases run time by **61.02%** against the baseline method.
- **Traffic emergency rescue case:** 20 UAVs and 3 tasks. Table II reports ILLA task reward 36578.95, higher than LLA, BRLA, and CBBA; Table III reports CBMBA A-Star path cost 14529.28 m and runtime 21.43 s, lower runtime than A-Star and DE.
- **Last-mile cargo transportation case:** 40 UAVs and 5 tasks. Table IV reports ILLA reward 69862.14 and lower execution time than LLA and CBBA; the text reports reward improvements of 13.57%, 15.64%, and 11.35% over three baselines.
- **Dynamic replanning:** when threats change, CBMBA A-Star's path cost increases by only 2.43% in the reported case; the D-Star and MSFDE baselines show larger runtime / turning-node increases.

## Limitations / future work

The validation is simulation-based. The paper models communication among neighboring UAVs, but does not present a field deployment or real-time network-stack experiment. The task and path constraints are rich for LU-ITS, yet real urban air-traffic regulations, weather, sensing uncertainty, and heterogeneous vehicle dynamics are outside the reported evaluation.

## Relation to the corpus

This is the corpus's clearest low-altitude ITS source where [[potential-game]] task allocation is paired with explicit path planning and collision avoidance. It extends [[low-altitude-intelligent-network]] from architectural / spectrum questions toward operational fleet planning, and complements [[chen-2026-cargo-uav-pickup-lae]] by adding cooperative task allocation and path search rather than cellular-connected pickup routing. It also links the game-theoretic line ([[chen-2024-ulse-game]], [[li-2025-stochastic-game-uav-swarm]]) with the trajectory / path-planning line represented by [[uav-trajectory-control]] and [[collision-avoidance-mgi]].

## Raw artifacts

- `raw/sources/Cooperative_Task_Allocation_and_Path_Planning_for_Multi-UAVs_in_Low-Altitude_Urban_Intelligent_Transportation_Systems/Cooperative_Task_Allocation_and_Path_Planning_for_Multi-UAVs_in_Low-Altitude_Urban_Intelligent_Transportation_Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
