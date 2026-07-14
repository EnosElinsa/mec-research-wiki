---
type: source
title: "UAV Trajectory Planning for Data Collection from Time-Constrained IoT Devices"
authors: ["Moataz Samir", "Sanaa Sharafeddine", "Chadi M. Assi", "Tri Minh Nguyen", "Ali Ghrayeb"]
year: 2020
url: "https://doi.org/10.1109/TWC.2019.2940447"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 19, no. 1, pp. 34-46"
tags: [source, uav-data-collection, deadline-constrained-data-collection, trajectory-optimization, resource-allocation, branch-reduce-and-bound, successive-convex-approximation]
related:
  - "[[deadline-constrained-uav-data-collection]]"
  - "[[branch-reduce-and-bound]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[samir-2022-aoi-altitude-scheduling]]"
  - "[[moataz-samir]]"
  - "[[sanaa-sharafeddine]]"
  - "[[chadi-assi]]"
  - "[[ali-ghrayeb]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV Trajectory Planning for Data Collection from Time-Constrained IoT Devices

## Citation

Samir, M., Sharafeddine, S., Assi, C. M., Nguyen, T. M., & Ghrayeb, A. (2020). *UAV Trajectory Planning for Data Collection from Time-Constrained IoT Devices*. **IEEE Transactions on Wireless Communications, 19**(1), 34-46. DOI: 10.1109/TWC.2019.2940447.

The article was published online on 17 September 2019 and assigned to the January 2020 issue, whose current-version date is 8 January 2020.

## TL;DR

A single UAV jointly plans its trajectory and uplink bandwidth allocation to maximize how many IoT devices complete their uploads between device-specific data-generation times and hard deadlines. A customized [[branch-reduce-and-bound]] method supplies a small-instance global benchmark, while successive convex approximation provides the scalable but locally optimal route and allocation used in larger simulations.

## Problem

Time-sensitive IoT data becomes irrelevant after its deadline, so maximizing aggregate collected bits can still leave many uploads incomplete. The paper formulates [[deadline-constrained-uav-data-collection]] as admission plus trajectory and radio-resource optimization: a device counts as served only when its cumulative service within its own generation-to-deadline window reaches its required amount. After maximizing the served set, a secondary problem shortens the route while preserving service to that set.

This is wireless data collection, not computation offloading. The model does not choose local versus edge execution, CPU frequencies, offloading ratios, or computing-server assignments.

## System model

- One UAV flies for a fixed slotted mission at fixed altitude, with bounded horizontal displacement and optional prescribed start and end locations.
- Each ground device has a known position, generation slot, deadline, and minimum service amount.
- Orthogonal uplink access divides each slot's bandwidth among admitted devices; allocations sum to at most one.
- Devices transmit at constant power. The offline route uses a path-loss-only [[air-to-ground-channel-model]] because future instantaneous CSI is unavailable, while online allocation can use currently observed CSI.
- Binary admission variables select the served devices; cumulative service constraints count rate only during each device's valid lifetime.

## Method

The primary formulation is a non-convex [[mixed-integer-nonlinear-programming|mixed-integer nonlinear program]]. The exact route introduces nonnegative rate slack variables and an equivalent monotonic formulation, then branches and reduces rate/resource hyper-rectangles while tightening upper and lower objective bounds. The resulting BRB algorithm is stated to find the global optimum of the formulated served-device problem to its stopping tolerance, but its repeated feasibility solves make it practical only for small instances.

For larger instances, binary admission is relaxed and non-convex service terms are replaced by iterative convex lower approximations. This SCA algorithm is explicitly suboptimal: convergence of the convexification process does not transfer BRB's global-optimality scope. A per-slot convex allocator then uses observed CSI to repair service deficits before deadlines where remaining time and bandwidth permit. A separate `SCA-distance` stage minimizes route length for the already selected device set.

## Key findings

- A three-device, 15-slot example shows slow BRB bound convergence and motivates using BRB as an optimum benchmark rather than the large-network solver.
- Reported sweeps show that looser deadlines increase the served percentage, while larger service requirements and network size reduce it under limited flight time and spectrum.
- Applying a path-loss-designed route under stronger fading can leave selected devices below their required service. In the shown 12-device test, the online CSI-aware allocator repairs the deficits for the reported path-loss, Rician `K=3`, and Rayleigh `K=0` cases; this is a simulation result, not a universal guarantee.
- `SCA-distance` removes route backtracking and reduces simulated propulsion energy in the shown scenario, but under a strong-fading realization it can fail to serve every selected device, exposing a route-efficiency versus fading-robustness tradeoff.
- The joint trajectory/resource methods outperform distance-based, deadline-based, and, except under very tight deadlines, static-UAV baselines in the reported simulations. OCR-damaged counts and percentages are not reproduced.

## Limitations / future work

The evaluation is simulation-only. The model assumes one UAV, fixed altitude and mission duration, known device positions and timing requirements, constant device power, orthogonal access, and no joint UAV/device energy budget in the primary objective. Future instantaneous CSI is unavailable to route planning, and online resource correction cannot guarantee deadline satisfaction when later service opportunities are insufficient. The paper identifies multi-UAV operation, NOMA, and explicit UAV/IoT energy consumption as future directions.

## Relation to the corpus

This source gives [[uav-data-collection]] a hard-deadline admission formulation distinct from the AoI objective in [[samir-2022-aoi-altitude-scheduling]] and the outage-aware max-min harvesting objective in [[you-2019-rician-uav-data-harvesting]]. [[chang-2026-data-offloading-energy-constraints]] cites it but changes the mission structure: all pickups and deliveries become mandatory, battery stations enter the route, and completion time replaces served-device count.

## Raw artifacts

- Parse: `raw/sources/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices.md`
- Origin PDF: `raw/sources/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices.pdf`
- Figures: `raw/sources/UAV_Trajectory_Planning_for_Data_Collection_from_Time-Constrained_IoT_Devices/images/`
