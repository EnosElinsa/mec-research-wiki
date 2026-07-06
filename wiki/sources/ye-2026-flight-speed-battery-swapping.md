---
type: source
title: "Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing"
authors: ["Dongmei Ye", "Zhengqing Sun", "Weifeng Zhong", "Jiawen Kang", "Xumin Huang", "Dong In Kim", "Shengli Xie", "Chau Yuen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3601743"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, battery-swapping, flight-speed-scheduling, task-offloading, mixed-integer-convex-programming]
related:
  - "[[battery-swapping-uav-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[analytical-target-cascading]]"
  - "[[mixed-integer-nonlinear-programming]]"
created: 2026-07-07
updated: 2026-07-07
---

# Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing

## Citation

Ye, D., Sun, Z., Zhong, W., Kang, J., Huang, X., Kim, D. I., Xie, S., & Yuen, C. (2026). *Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3601743.

## TL;DR

Studies a patrol-inspection UAV that visits task nodes, processes data locally or via a base-station MEC server, and may swap batteries at the base station. The paper jointly optimizes flight-speed selection, battery swapping, and [[task-offloading]] to minimize UAV operational cost, using virtual nodes to build an extended graph and an [[analytical-target-cascading]] heuristic for larger instances.

## Problem

UAV-enabled MEC inspection is not only an offloading problem. Flight speed changes travel time and propulsion energy, offloading changes hovering time and purchased MEC resources, and battery swapping changes both the feasible path and operating cost. Optimizing one of these decisions while fixing the others can either violate the mission deadline or overpay for batteries, bandwidth, or computation.

## System model

A quad-rotor UAV starts from and returns to a base station that provides wireless access, a MEC server, and a battery-swapping station. The UAV visits task nodes under base-station coverage, hovers at each node for data collection and processing, and chooses whether each task is processed locally or offloaded to the MEC server. The base station sells communication bandwidth, computation resource, and replacement batteries. Flight speeds are selected from a discrete set, and battery-swapping choices are represented through virtual nodes in a unidirectional extended graph.

## Method

The paper formulates total operational cost minimization with time, energy, offloading, flight-speed, and battery-swapping constraints. By expanding the route graph with virtual battery states, it reformulates the nonconvex scheduling problem into a tractable mixed-integer convex form for moderate-sized instances. For larger cases, the ATC heuristic coordinates decomposed subproblems while driving shared time and state variables toward consistency.

## Key findings

- The proposed optimizer is reported to reduce total operational cost relative to fixed-speed and fixed-battery-swapping baselines; Table III includes baselines with cost gaps from 13.8% to 199.5%, while some fixed policies become infeasible.
- Tightening the mission deadline changes the preferred operating mode: one reported case shifts from all-local processing at 720 s, to all-offloading at 660 s, to buying more MEC computation and reducing battery swaps at 600 s.
- Battery mass has a non-monotone role. In the reported examples, increasing battery mass from 0.2 to 0.3 reduces swaps from two to one, and at 0.4 eliminates swapping; the heavier battery can reduce overall cost and time when it avoids enough swap overhead.
- The ATC heuristic is reported to drive total inconsistency error close to zero within a few iterations and to keep total time within the deadline in the tested large-scale settings.

## Limitations / future work

The parse frames the base model as a single-base-station setting and notes that it can be extended to multi-base-station scenarios. Evaluation is simulation/optimization based; hardware or field validation is not in parse.

## Relation to the corpus

This source adds an energy-replenishment dimension to the UAV-MEC offloading line. It complements [[task-offloading]] and [[uav-trajectory-control]] by making speed and battery replacement first-class decisions rather than background constraints. The new [[battery-swapping-uav-mec]] concept is distinct from energy harvesting, wireless power transfer, and UAV charging; it models discrete battery replacement at infrastructure.

## Raw artifacts

- `raw/sources/Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing/Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
