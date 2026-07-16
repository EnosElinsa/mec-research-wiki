---
type: source
title: "Joint Optimization on Trajectory and Velocity for Minimum Completion Time in UAV-Enabled Wireless-Powered WSN"
authors: ["Jing Guo", "Feihang Qiu", "Lei Lei", "Xu Zhang"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3654603"
venue: "IEEE Transactions on Green Communications and Networking (TGCN)"
modeling_card: required
tags: [source, wireless-power-transfer, uav-data-collection, trajectory-optimization, completion-time]
related:
  - "[[fly-while-communication]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[b-spline-trajectory]]"
  - "[[genetic-algorithm]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
  - "[[zhan-2018-uav-wsn-data-collection]]"
created: 2026-07-13
updated: 2026-07-16
---

# Joint Optimization on Trajectory and Velocity for Minimum Completion Time in UAV-Enabled Wireless-Powered WSN

## Citation

Guo, J., Qiu, F., Lei, L., & Zhang, X. (2026). Joint optimization on trajectory and velocity for minimum completion time in UAV-enabled wireless-powered WSN. *IEEE Transactions on Green Communications and Networking, 10*, 1829-1840. https://doi.org/10.1109/TGCN.2026.3654603

## TL;DR

For one energy-limited rotary-wing UAV serving batteryless sensors, this paper combines energy-based sensor clustering, GA visit ordering, a GA-tuned B-spline path, and segmentwise velocity control to minimize mission completion time while powering and collecting data from sensors during flight.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One energy-limited rotary-wing UAV flies at fixed altitude, broadcasts RF energy to static batteryless sensor nodes, receives their data through TDMA, and returns to its departure point. The air-to-ground gain follows an inverse-square distance model and the sensors use linear RF energy harvesting while the UAV communicates during flight.

**Problem & objective**: Discretized problem P0 jointly designs clustering and visit order, a B-spline path, and segment velocities to solve $\min_{\{\theta\},\{q_m[k]\},\{\nu_m[k]\}}T^f+T^s$, the sum of fly-only and fly-while-communication time.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Cluster and visit-order parameters | $\theta$ | discrete permutation and clustering choices | Sensor grouping, cluster-head selection, and order of visitation |
| UAV waypoint | $q_m[k]$ | continuous 2-D position | B-spline trajectory point at discrete instant $k$ |
| Segment velocity | $\nu_m[k]$ | continuous, $0\leq\lVert\nu_m[k]\rVert\leq V_{\max}$ | UAV speed on fly-only or communication segment |
| Communication indicator | $\varphi_{n,k}$ | binary, $\{0,1\}$ | Whether sensor $n$ is powered and served at instant $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Mobility | $\lVert q_m[k+1]-q_m[k]\rVert/\delta_k\leq V_{\max}$ and $q_m[k_T]=q_m[0]$ |
| Service range | $\varphi_{n,k}=1$ only when $\lVert q_m^{\mathrm{tr}}[k]-O_n\rVert\leq D_{\mathrm{tr}}$ |
| Data demand | Every sensor satisfies $\sum_k\varphi_{n,k}R_{n,m}[k]\geq S_n$ |
| Energy budget | UAV propulsion plus RF-transfer energy satisfies $E_m^u+E_{pt}\leq\varepsilon$ |

**Algorithm**: Compute the RF activation radius and cluster adjacent sensors; use a genetic algorithm to order cluster heads as a traveling-salesman tour; initialize a B-spline with those heads and use a second genetic search over affine deformation and spline order with distance, smoothness, and energy fitness; segment the resulting path into fly-only and communication portions; then solve the convex P3 velocity block under throughput and onboard-energy limits.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guo et al. [x] studied completion-time minimization for an energy-limited UAV that powers batteryless sensor nodes and collects their data while flying. They formulated a joint trajectory and velocity problem with speed, return-point, communication-range, sensor-throughput, and onboard-energy constraints. Their solution clusters sensors by RF activation range, orders cluster heads with a genetic algorithm, smooths the route with a genetically tuned B-spline, and optimizes velocities separately on flight and communication segments. Simulations reported average completion-time reductions of 43 percent relative to fly-hover communication and 15 percent relative to the Bezier-curve baseline.

## Problem and system model

The UAV flies at fixed altitude, broadcasts RF energy, receives TDMA sensor uploads, and returns to its departure point. Sensors are static and known; inverse-square channel gain and linear energy harvesting determine service regions. The UAV may cover adjacent nodes along the same [[fly-while-communication]] segment.

The objective minimizes fly-only plus communication-flight time subject to sensor throughput, UAV speed, return, communication-range, and onboard-energy constraints. The energy budget includes RF transmit and speed-dependent [[rotary-wing-propulsion-energy-model|propulsion]] energy but excludes takeoff, landing, and acceleration losses.

## Method

An activation-radius rule clusters sensors and a [[genetic-algorithm]] orders cluster heads as a TSP. Cluster heads initialize a [[b-spline-trajectory]], whose affine deformation and spline order are searched using a weighted fitness over distance, smoothness, and propulsion energy. The final stage divides the path into fly-only and communication segments and optimizes segment speeds.

The paper states that its final velocity block is convex, but the cited equation numbers do not match the extracted formulation. The overall framework includes two GA stages and a non-guaranteed cluster-head choice, so it is heuristic rather than globally optimal.

## Key findings

- The paper reports average simulated completion-time reductions of **43%** versus fly-hover communication and **15%** versus its Bezier-path baseline.
- Higher communication demand moves the path toward sensors and lowers speed on communication segments.
- More onboard energy permits higher average speed and shorter completion time in the tested setup.
- The B-spline path can be slightly longer than the Bezier path while reducing communication time by staying closer to sensors.

## Limitations

Evidence is simulation-only. The model has one UAV, fixed/known sensors, fixed altitude, linear harvesting, simplified propagation, and no blockage, fading uncertainty, nonlinear rectifier behavior, or interference. Complexity claims use locally ambiguous notation and remain paper-attributed. Multi-UAV coordination and real-time replanning are future work.

## Relation to the corpus

[[xu-2018-uav-wpt-trajectory]] provides the foundational UAV-WPT trajectory problem, while [[zhan-2018-uav-wsn-data-collection]] studies wake-up scheduling and sensor energy. This paper contributes the [[fly-while-communication]] operating mode with B-spline path and velocity design under an onboard UAV energy budget.

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_on_Trajectory_and_Velocity_for_Minimum_Completion_Time_in_UAV-Enabled_Wireless-Powered_WSN/Joint_Optimization_on_Trajectory_and_Velocity_for_Minimum_Completion_Time_in_UAV-Enabled_Wireless-Powered_WSN.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
