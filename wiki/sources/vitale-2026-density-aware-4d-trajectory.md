---
type: source
modeling_card: required
title: "Density-Aware 4-D Trajectory Planning for Urban Air Traffic With Different QoS Levels"
authors: ["Christian Vitale", "Charalambos Menelaou", "Panayiotis Kolios", "Stelios Timotheou", "Christos G. Panayiotou", "Georgios Ellinas"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3694259"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, urban-air-mobility, trajectory-planning, air-traffic-management, chance-constraint, robust-mpc, miqcp]
related:
  - "[[reservation-based-density-aware-4d-uav-planning]]"
  - "[[urban-air-mobility]]"
  - "[[uav-trajectory-control]]"
  - "[[chance-constraint]]"
  - "[[target-level-of-safety]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[charalambos-menelaou]]"
  - "[[stelios-timotheou]]"
  - "[[theocharides-2026-uav-traffic-estimation]]"
created: 2026-07-12
updated: 2026-11-03
---

# Density-Aware 4-D Trajectory Planning for Urban Air Traffic With Different QoS Levels

## Citation

Vitale, C., Menelaou, C., Kolios, P., Timotheou, S., Panayiotou, C. G., & Ellinas, G. (2026). *Density-Aware 4-D Trajectory Planning for Urban Air Traffic With Different QoS Levels*. **IEEE Transactions on Intelligent Transportation Systems**, 27(7), 7787-7804. DOI: 10.1109/TITS.2026.3694259.

## TL;DR

Coordinates urban UAV traffic through centralized cube-and-time reservations and distributed uncertainty-aware local control. A reverse-time graph planner selects the latest feasible departure and 4-D route for each QoS request, while robust MPC converts probabilistic separation constraints into a conservative MIQCP inside each airspace cube.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Urban airspace is split into cubes with a maximum number of simultaneous UAVs; a central planner reserves cube-time slots for UAV requests with two arrival-time QoS levels, and admissibility $\psi_i^m(k)$ marks cubes still below capacity. Inside each cube, every UAV follows its reservation with model-predictive control under linear-Gaussian motion and predicted neighbor states.

**Problem & objective**: The inter-cube OIPP problem $(\mathrm P_1)$ in (6) picks departure time $s^m$ and cube path $p^h$ to minimize $J_T=k_{des}^m-k_{0^h}(s^m)$, i.e., the latest departure that still arrives by $k_{des}^m$. Inside a cube, the Intra-Cube Planner (15), an MIQCP, minimizes the number of slots spent in the cube $\sum_tb_t^m$ plus a big-$M$ penalty on separation slacks $\zeta_t^{i,m}$.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Departure time | $s^m$ | discrete slot in $\mathcal H$ | Departure of UAV $m$ |
| Cube path | $p^h$ | discrete path in $G(\mathcal V,\mathcal E)$ | Cube sequence from $O^m$ to $D^m$ |
| Control input | $\mathbf u_{k+t}^m$ | continuous, $\lvert\mathbf u\rvert\le\mathbf u_{MAX}$ | MPC force inside the cube |
| In-cube indicator | $b_t^m$ | binary, non-increasing | UAV $m$ is still inside the cube at step $t$ |
| Separation slack | $\zeta_t^{i,m}$ | continuous, $\ge0$ | Relaxation of the safe distance to neighbor $i$ |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (6a) | Cube dynamics (3)–(5): traversal time is finite only through admissible cubes, so density limits hold |
| (6b) | Arrival by the desired time: $k_{L^h}(s^m)\le k_{des}^m$ |
| (15b)–(15d) | Leave the cube by the reserved exit slot; $b_t^m$ binary and non-increasing |
| (15e)–(15i) | Mean dynamics (6) and staying within the cube until exit through its face |
| (15j)–(15k) | Control-rate $\lvert\mathbf u_{k+t}-\mathbf u_{k+t-1}\rvert\le\Delta\mathbf u$ and speed $\le\mathbf v_{MAX}$ (with the force bound) |
| (15m)–(15n) | Expected positions keep the sphere-based safe distance $d_{k+t}^{i,m}$ minus slack $\zeta_t^{i,m}\ge0$, a sufficient condition for the chance constraint (10l)–(10m) |

**Algorithm**: Algorithm 1 (ICPP) sorts requests by QoS and desired arrival time, solves OIPP for each with a reverse-time search (Algorithm 2) that returns the latest feasible departure and path, and updates reservations and admissibility. Each UAV then runs the Intra-Cube Planner in every cube, enclosing Gaussian confidence ellipsoids in spheres to turn the separation chance constraint into a deterministic distance.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Vitale et al. [x] studied density-aware four-dimensional trajectory planning for urban UAV traffic with different arrival-time QoS levels. A central reverse-time graph planner reserves cube-time resources and selects the latest feasible route, while each UAV uses robust model-predictive control to follow the reservation under stochastic separation constraints. The local controller solves a mixed-integer quadratically constrained problem with force, speed, control-rate, and safety-slack variables. Gaussian confidence ellipsoids are conservatively enclosed by spheres to obtain a sufficient chance-constraint condition. Against a time-dependent A* baseline, the proposed method reduces mean arrival-time gap from 336.35 to 202.79 at capacity one (3,000 requests) and from 56.90 to 39.18 at capacity ten (6,500 requests), with slightly longer mean travel time at capacity one.

## Problem

Dense [[urban-air-mobility|urban air mobility]] must reconcile requested arrival times with finite local airspace capacity and collision risk under uncertain motion. Planning only geometric routes does not reserve when a UAV occupies each region, while a fully centralized continuous controller scales poorly and requires detailed state exchange. The paper separates strategic space-time scheduling from local trajectory execution.

## System model

- AirMatrix+ partitions a three-dimensional urban airspace into equal cubes connected by an adjacency graph. Each cube accepts at most a configured number of simultaneous reservations.
- A central traffic manager receives each UAV's origin, destination, desired arrival time, and one of two QoS classes: close-to-requested arrival or early-arrival tolerance.
- The UAV state contains 3-D position and velocity; a 3-D force is applied under linear dynamics with i.i.d. zero-mean Gaussian acceleration disturbance.
- Each UAV executes its reserved inter-cube route locally and exchanges predicted state means and covariances only with relevant nearby UAVs.

## Method

[[reservation-based-density-aware-4d-uav-planning]] first orders requests by QoS and desired arrival time. Its inter-cube path planner builds a reverse-time directed acyclic graph from the requested destination time, filters cube-time nodes by existing reservations, and returns the latest feasible departure and admissible route. For each request, given the reservations already committed by previously processed requests, Algorithm 2 is optimal for the OIPP in the discretized space-time domain and has pseudopolynomial complexity `O((k_des^m-s_*^m)|E|)`.

Within each cube, stochastic MPC controls a UAV toward the reserved exit face and time while respecting force, speed, control-rate, and no-return constraints. Gaussian confidence ellipsoids are conservatively enclosed by spheres, yielding a sufficient barycenter-separation condition for the pairwise [[chance-constraint|chance constraint]]. The resulting MIQCP minimizes cube residence time plus heavily weighted safety slack.

## Key findings

- In simulations with 6,500 requests, three vertical layers, and nine `160 m` cubes per layer, capacity `C=10` is selected from an empirical congestion sweep; it is scenario-specific rather than a universal capacity result.
- At the capacity-specific maximum-demand cases for `C=5`, `C=7`, and `C=9`, ICPP extends the planned flight times of approximately `8%` of non-priority UAVs. Across the reported simulations, the configured minimum separation of `20 m` remains respected.
- Against the modified time-dependent `A*` Metropolis baseline, mean arrival-time deviation falls from `336.35 s` to `202.79 s` at `C=1` (`N=3,000`, `7 s` nominal traversal) and from `56.90 s` to `39.18 s` at `C=10` (`N=6,500`, `14 s` nominal traversal). Mean travel time and mean path length are similar between methods.
- The conservative separation derivation bounds loss-of-separation probability by the requested risk threshold when the original constraint is feasible without positive safety slack.

## Limitations / parse caveats

Evidence is MATLAB/Gurobi simulation only. The model assumes linear-Gaussian dynamics, exact current-state estimates, fixed percentile-based cube reservation durations, timely local prediction exchange, and a predetermined update order. Safety slack permits temporary relaxation when strict separation is infeasible, so the probability guarantee is conditional. The parse misspells “Traffic” and “Different” in the title, damages parts of the notation table, and inconsistently labels the proposed method `ICTP` in one table; the corrected title and publication metadata were verified through the exact-title Crossref record, while technical claims come only from the parse.

## Relation to the corpus

The source adds strategic airspace reservation to [[uav-trajectory-control]] and [[compliance-aware-uav-trajectory]]. Its explicit probabilistic separation bound links [[chance-constraint]] planning to the operational risk vocabulary in [[target-level-of-safety]], while its QoS classes concern arrival timing rather than radio-resource QoS.

## Raw artifacts

- Parse: `raw/sources/Density-Aware_4-D_Trajectory_Planning_for_Urban_Air_Traffic_With_Different_QoS_Levels/Density-Aware_4-D_Trajectory_Planning_for_Urban_Air_Traffic_With_Different_QoS_Levels.md`
- Origin PDF: `raw/sources/Density-Aware_4-D_Trajectory_Planning_for_Urban_Air_Traffic_With_Different_QoS_Levels/Density-Aware_4-D_Trajectory_Planning_for_Urban_Air_Traffic_With_Different_QoS_Levels.pdf`
- Figures: `raw/sources/Density-Aware_4-D_Trajectory_Planning_for_Urban_Air_Traffic_With_Different_QoS_Levels/images/`
