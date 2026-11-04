---
type: source
title: "Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service"
authors: ["Nishant Gupta", "Satyam Agarwal", "Deepak Mishra", "Brijesh Kumbhani"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, uav-replacement, service-continuity, uav-trajectory, resource-allocation, successive-convex-approximation]
related:
  - "[[battery-swapping-uav-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[gupta-2022-energy-aware-outage-trajectory]]"
  - "[[li-2026-two-timescale-uav-replacement-hap]]"
  - "[[nishant-gupta]]"
  - "[[deepak-mishra]]"
  - "[[satyam-agarwal]]"
  - "[[ye-2023-seamless-service-handover-uav-mec]]"
  - "[[uav-energy-replenishment-and-service-continuity]]"
created: 2026-08-27
updated: 2026-11-03
---

# Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service

## Citation

Gupta, N., Agarwal, S., Mishra, D., & Kumbhani, B. *Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service*. Venue and year are not in the parse.

## TL;DR

When a serving UAV runs low on battery, a charged UAV replaces it from a station. The paper maximizes minimum ground-user throughput by jointly optimizing the three-dimensional trajectories of the two UAVs and the bandwidth allocation with alternating optimization and successive convex approximation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Two rotary-wing UAVs serve $K$ ground users over FDMA downlinks with a probabilistic LoS channel. The energy-depleted UAV $U_1$ flies from the service location $\mathbf X_F$ to the charging station $\mathbf X_I$ within $N_f \le N$ slots, while the charged UAV $U_2$ flies from $\mathbf X_I$ to $\mathbf X_F$ to take over.

**Problem & objective**: Maximize the minimum user throughput over the replacement flight, $\max_{\mathbf B,\mathbf T}\min_k R_k$ with $R_k = \sum_{n=1}^{N_f} r_{k,1}[n] + \sum_{n=1}^{N} r_{k,2}[n]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV trajectory | $\mathbf T = \{\mathbf X_m[n]\}$, with horizontal $\mathbf q_m[n]$ and altitude $z_m[n]$ | continuous 3-D | Positions of $U_1$ and $U_2$ in slot $n$ |
| Bandwidth allocation | $\mathbf B = \{b_{k,m}[n]\}$ | continuous, $\ge 0$ | Bandwidth given to user $k$ by UAV $m$ in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Endpoints | $\mathbf X_1[0]=\mathbf X_F$, $\mathbf X_1[N_f]=\mathbf X_I$, $\mathbf X_2[0]=\mathbf X_I$, $\mathbf X_2[N]=\mathbf X_F$ |
| Speed | $v_m[n] \le V_{\max}$ |
| Collision avoidance | $\lVert \mathbf X_m[n]-\mathbf X_j[n]\rVert^2 \ge D_{\min}^2$ for $m \ne j$ |
| Residual energy | $\sum_{n=1}^{N_f} e_1[n] \le E_{\text{left}}$ for the depleted UAV, using the rotary-wing propulsion model |
| Minimum rate | $r_{k,1}[n] + r_{k,2}[n] \ge R_{th}$ for every user and slot |
| Bandwidth budget | $\sum_{k}\sum_{m} b_{k,m}[n] = B$ |

**Algorithm**: Alternating optimization: bandwidth allocation by linear programming for fixed trajectories, then horizontal and vertical trajectory updates by successive convex approximation for fixed bandwidth, repeated until the objective improvement falls below a tolerance.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gupta et al. [x] studied UAV replacement as a coverage-continuity problem for a UAV-assisted wireless system. Their max-min throughput objective jointly optimizes three-dimensional multi-UAV trajectories and user resource allocation when a charged UAV replaces an energy-depleted server. The nonconvex formulation is handled by alternating optimization and successive convex approximation. Numerical studies show higher achievable sum rate and fairer per-user throughput than straight and ellipsoidal trajectory benchmarks. The paper focuses on communication coverage rather than MEC task execution or service-state migration.

## Problem and system model

UAVs act as temporary base stations and serve ground users through probabilistic LoS/NLoS channels. Replacement flight and communication allocation must be coordinated so the old UAV can return while the new UAV reaches service position.

## Method

The method alternates resource allocation and trajectory optimization, convexifying nonconvex rate and motion terms around the current iterate.

## Key findings

- Joint trajectory and bandwidth control improves minimum and sum throughput relative to separate optimization baselines.
- The replacement framework preserves service while the depleted UAV returns to charge.
- The iterative SCA/alternating procedure converges in the reported numerical cases.

## Limitations / future work

The evaluation is numerical and does not include application-state migration, obstacle avoidance, or charging-station scheduling.

## Relation to the corpus

This source complements [[battery-swapping-uav-mec]] with a communication-throughput view of UAV replacement and links replacement timing to [[uav-trajectory-control]]. The same authors' single-UAV outage study [[gupta-2022-energy-aware-outage-trajectory]] treats the on-board energy budget as a trajectory constraint rather than a trigger for replacement, and [[li-2026-two-timescale-uav-replacement-hap]] studies replacement inside hierarchical aerial computing.

## Raw artifacts

- Parse: `raw/sources/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md`
- Origin PDF and figures are in the same folder.