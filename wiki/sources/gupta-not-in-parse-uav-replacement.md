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
created: 2026-08-27
updated: 2026-08-27
---

# Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service

## Citation

Gupta, N., Agarwal, S., Mishra, D., & Kumbhani, B. *Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service*. Venue and year are not in the parse.

## TL;DR

When a serving UAV runs low on battery, a charged UAV replaces it from a station. The paper maximizes minimum ground-user throughput by jointly optimizing three-dimensional trajectories and bandwidth/resource allocation with alternating optimization and successive convex approximation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs provide temporary base-station coverage to ground users. A replacement UAV flies from a charging station while the depleted UAV returns, so coverage continuity must be preserved.

**Problem & objective**: Maximize the minimum user throughput, $\max\min_m R_m$, over replacement trajectories and communication-resource allocations.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV position | $\mathbf q_k[n]$ | continuous 3-D | Replacement and serving UAV trajectory |
| Bandwidth share | $\beta_{k,m}[n]$ | continuous | Resource allocated to user $m$ by UAV $k$ |
| Replacement timing | $t_k$ | slot/time | Time at which a charged UAV takes over |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Coverage | Users retain a serving UAV throughout replacement. |
| Mobility | UAV positions, velocity, and replacement flight path are feasible. |
| Resource | Bandwidth shares remain within each UAV's budget. |
| Battery | Depleted UAV returns to charging before unsafe energy exhaustion. |

**Algorithm**: Alternate closed-form or convex bandwidth updates with trajectory updates solved by successive convex approximation until the max-min objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gupta et al. [x] studied UAV replacement as a coverage-continuity problem for a UAV-assisted wireless system. Their max-min throughput objective jointly optimizes three-dimensional multi-UAV trajectories and user resource allocation when a charged UAV replaces an energy-depleted server. The nonconvex formulation is handled by alternating optimization and successive convex approximation. Numerical studies show higher achievable sum rate and fairer throughput than the benchmark replacement strategies. The paper focuses on communication coverage rather than MEC task execution or service-state migration.

## Problem and system model

UAVs act as temporary base stations and serve ground users through line-of-sight channels. Replacement flight and communication allocation must be coordinated so the old UAV can return while the new UAV reaches service position.

## Method

The method alternates resource allocation and trajectory optimization, convexifying nonconvex rate and motion terms around the current iterate.

## Key findings

- Joint trajectory and bandwidth control improves minimum and sum throughput relative to separate optimization baselines.
- The replacement framework preserves service while the depleted UAV returns to charge.
- The iterative SCA/alternating procedure converges in the reported numerical cases.

## Limitations / future work

The evaluation is numerical and does not include application-state migration, obstacle avoidance, or charging-station scheduling.

## Relation to the corpus

This source complements [[battery-swapping-uav-mec]] with a communication-throughput view of UAV replacement and links replacement timing to [[uav-trajectory-control]].

## Raw artifacts

- Parse: `raw/sources/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md`
- Origin PDF and figures are in the same folder.
