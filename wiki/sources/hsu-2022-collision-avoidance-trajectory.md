---
type: source
title: "Reinforcement Learning-Based Collision Avoidance and Optimal Trajectory Planning in UAV Communication Networks"
authors: ["Yu-Hsin Hsu", "Rung-Hung Gau"]
year: 2022
url: "https://doi.org/10.1109/TMC.2020.3003639"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), 21(1), 306-320"
modeling_card: required
tags: [source, uav-trajectory-control, uav-data-collection, collision-avoidance, reinforcement-learning, convex-optimization, traveling-salesman-problem]
related:
  - "[[convex-tsp-uav-data-collection]]"
  - "[[distributed-tabular-q-learning-uav-collision-avoidance]]"
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[hua-2026-unpredictable-uav-trajectory]]"
  - "[[unpredictable-uav-trajectory-control]]"
  - "[[navigation-stochastic-control-decomposition]]"
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-data-collection]]"
  - "[[autonomous-uav-swarms]]"
  - "[[air-to-ground-channel-model]]"
  - "[[safe-reinforcement-learning]]"
  - "[[zhan-2018-uav-wsn-data-collection]]"
created: 2026-07-14
updated: 2026-07-16
---

# Reinforcement Learning-Based Collision Avoidance and Optimal Trajectory Planning in UAV Communication Networks

## Citation

Hsu, Y.-H., & Gau, R.-H. (2022). *Reinforcement Learning-Based Collision Avoidance and Optimal Trajectory Planning in UAV Communication Networks*. **IEEE Transactions on Mobile Computing, 21**(1), 306-320. DOI: 10.1109/TMC.2020.3003639.

## TL;DR

Separates multi-UAV mission planning into a planned data-collection route and an online collision-avoidance layer. [[convex-tsp-uav-data-collection|Convex-TSP]] constructs a short piecewise-linear return route through the heterogeneous communication disks of assigned IoT devices, while [[distributed-tabular-q-learning-uav-collision-avoidance|distributed tabular Q-learning]] changes each UAV's heading from local relative observations when nearby UAVs are detected.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-altitude UAVs deliver goods on outbound paths and collect data from assigned heterogeneous IoT devices on return paths. Device transmit powers and SNR targets induce different communication disks, while unknown paths of other UAVs require local sensing and online collision avoidance.

**Problem & objective**: Plan the shortest feasible return curve, $\min_{\tilde\gamma}\int_0^1\lVert\dot{\tilde\gamma}(\tau)\rVert_2\,d\tau$, that intersects every assigned communication disk, then choose online heading changes that preserve separation while tracking the planned route.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Device visiting order | $\boldsymbol\alpha$ | permutation | Order in which a UAV covers assigned IoT devices |
| Visiting point | $\mathbf v_k$ | continuous 2-D point | Point selected inside device $k$'s communication disk |
| Planned return path | $\tilde\gamma$ | piecewise-linear curve | Route from delivery point back to distribution center |
| Collision-avoidance action | $a$ | discrete heading change | Online direction adjustment at fixed speed |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The return path starts at the delivery point and ends at the distribution center. |
| C2 | For every assigned device, $d(\tilde\gamma,\mathbf w_k)\leq R_k$. |
| C3 | UAVs fly at the prescribed fixed altitude and constant speed. |
| C4 | Pairwise separation satisfies $\lVert\mathbf q_m(t)-\mathbf q_n(t)\rVert_2\geq d_{\min}$. |
| C5 | Sensing radius satisfies $d_{\mathrm{sen}}\geq2Vt_{\mathrm{sensor}}+d_{\min}$. |
| C6 | When three or more neighbors make the tabular state unbounded, an identifier-based altitude rule supplies fallback separation. |

**Algorithm**: Solve an auxiliary no-return TSP for device order, then solve a convex two-segment problem for a point inside each communication disk and repeatedly refine neighboring bridge points until path improvement is negligible. Train a distributed tabular Q-learning controller offline from goal-relative and obstacle-relative states, and during flight apply its heading action when nearby UAVs are sensed while otherwise following the planned path.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hsu and Gau [x] separated multi-UAV goods delivery and IoT collection into planned return trajectories and local collision-avoidance control. They minimized each return-path length over device order and visiting points inside heterogeneous communication disks, while online heading choices enforce fixed-speed, sensing-range, endpoint, data-coverage, and pairwise-separation conditions. Convex-TSP combines a no-return traveling-salesman order with convex visiting-point refinement, and distributed tabular Q-learning deviates from the plan when neighboring UAVs are detected. In 100-device networks with two to ten UAVs, Convex-TSP reduced average return length by at least 25% relative to random disk cover and circumcircle baselines, while learned paths avoided collisions with only modest route-length increase.

## Problem and system model

Each UAV carries goods from a distribution center to a delivery destination and collects data from its assigned ground IoT devices on the return flight. Other UAV trajectories are not known in advance, so collision avoidance must operate from local sensing rather than a globally coordinated route plan.

The UAVs fly at constant speed. Altitude groups are separated by more than the minimum collision distance, and UAVs within the studied group share a fixed altitude. Radar or lidar provides a sensing radius; the time-slotted safety condition requires that sensing cover the distance traveled during sensor delay plus the minimum separation margin.

For data collection, the paper uses a fixed-altitude LoS free-space [[air-to-ground-channel-model]]. Device transmit power and SNR requirements determine device-specific horizontal communication disks. The planned return path must start at the delivery point, end at the distribution center, and enter every assigned disk; the actual path may depart from that plan to avoid another UAV.

## Method

The [[convex-tsp-uav-data-collection]] procedure first adds the fixed endpoints and a virtual city to an auxiliary no-return TSP so that the resulting order starts at the delivery point, visits the devices, and terminates at the distribution center. Given that order, it solves a convex subproblem for a point inside each device's communication disk that minimizes the lengths of the adjacent route segments. A refinement loop repeatedly updates the bridging points using their current neighbors until the path-length improvement falls below a threshold or the iteration limit is reached. The simulations use Google Optimization Tools for the TSP and CVXPY for the convex subproblems.

The [[distributed-tabular-q-learning-uav-collision-avoidance]] controller quantizes the UAV's goal-relative heading and each detected obstacle's relative distance, bearing, and direction. Its discrete action changes heading while speed remains fixed. The reward combines unsafe-separation penalties, progress toward the destination, and heading-alignment penalties. To bound the table, a state represents at most two obstacles; detection of three or more adjacent UAVs invokes an identifier-based altitude-change rule instead. Training is offline, and deployment looks up the learned action from a sorted state table.

## Key findings

- Across 100 random topologies with 10-20 IoT devices, the route-refinement procedure is reported to converge within 20 iterations in almost all trials. This is simulation evidence, not a worst-case convergence guarantee.
- In the tested 10-network collision-avoidance setup, success-probability sequences converged within 1,000 training episodes for exploration probabilities 0.01, 0.05, and 0.1. Success means completing an episode without collision in that simulator; it does not establish a formal [[safe-reinforcement-learning|safety guarantee]].
- Figure 9(a) shows the proposed planner with the lowest average return-route length among the four tested methods. Exact curve values are figure-derived and are not reported as precise measurements in the text.
- In the fixed-altitude experiment with heterogeneous device radii, Fig. 10 reports the lowest average route length for convex-TSP when the maximum communication radius is at least 100 m. The circumcircle method is slightly better when all radii are equal, so the advantage depends on radius heterogeneity.
- For simulated 100-device networks with 2-10 UAVs and radii drawn from {50, 100, 150, 200, 250, 300} m, Fig. 11's accompanying prose reports at least a 25% reduction in average route length per UAV versus random-GDC and circumcircle baselines. This percentage is tied to that plotted scenario.
- In one four-UAV mission, Table 3 reports planned/actual lengths of 1434.975/1473.536, 1896.011/1931.823, 1338.174/1350.598, and 1909.327/1931.844 m. These are exact entries for one simulated topology, not averages.

## Limitations

Evaluation is analytical and simulation-based, without a flight or hardware experiment. The model fixes speed, uses common altitude within a group, assumes deterministic LoS/free-space data links, and assigns devices to UAVs in advance. Route planning optimizes finite piecewise-linear paths separately for each UAV rather than jointly optimizing association, routes, and collision avoidance.

The tabular state represents no more than two obstacles and handles denser encounters through a separate altitude rule. The demonstrated collision-free trajectories therefore do not constitute a universal safety proof. The paper identifies deep Q-learning, joint forward/return route design, and joint trajectory/collision-avoidance optimization as future work.

## Relation to the corpus

This source combines [[uav-data-collection]] route design with local [[uav-trajectory-control]] during multi-UAV encounters. It complements [[zhan-2018-uav-wsn-data-collection]], but adds heterogeneous communication neighborhoods, fixed distinct route endpoints, and a decentralized collision-avoidance layer.

## Comparison boundary

Its local tabular heading lookup is empirically distinct from Zhang's expected-cost/next-point filter ([[zhang-2021-safe-dqn-emergency]]), Hua's deliberate stochastic motion ([[hua-2026-unpredictable-uav-trajectory]]), and Qi's opportunistic DDQN exchange ([[qi-2026-ocma-ddqn-data-collection]]). [[unpredictable-uav-trajectory-control]] and [[navigation-stochastic-control-decomposition]] preserve a mission component while modifying motion, but this paper's simulator success is not a formal collision guarantee. See [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- Parse: `raw/sources/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks.md`
- Origin PDF: `raw/sources/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks.pdf`
- Figures: `raw/sources/Reinforcement_Learning-Based_Collision_Avoidance_and_Optimal_Trajectory_Planning_in_UAV_Communication_Networks/images/`
