---
type: source
title: "ISAC From the Sky: UAV Trajectory Design for Joint Communication and Target Localization"
authors: ["Xiaoye Jing", "Fan Liu", "Christos Masouros", "Yong Zeng"]
year: 2024
url: "https://doi.org/10.1109/TWC.2024.3396571"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, target-localization, multi-stage-trajectory, bandwidth-allocation, cramer-rao-bound, energy-constraint]
related:
  - "[[multi-stage-estimate-design-sense-trajectory]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[joint-localization-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
  - "[[fan-liu]]"
  - "[[christos-masouros]]"
  - "[[yong-zeng]]"
created: 2026-07-13
updated: 2026-07-13
---

# ISAC From the Sky: UAV Trajectory Design for Joint Communication and Target Localization

## Citation

Jing, X., Liu, F., Masouros, C., & Zeng, Y. (2024). *ISAC From the Sky: UAV Trajectory Design for Joint Communication and Target Localization*. **IEEE Transactions on Wireless Communications**, 23(10), 12857-12872. DOI: 10.1109/TWC.2024.3396571.

*Metadata note:* The parse supplies the DOI and 2024 publication history but omits the journal record; the exact-title Crossref record supplies the venue, volume, issue, and pages above.

## TL;DR

Closes an estimate-design-sense loop for one energy-limited UAV that transmits to ground users and localizes initially unknown static targets. Each stage uses accumulated ranges to update target positions, then redesigns waypoints, hover points, velocities, and bandwidth for the next stage.

## Problem framing

An airborne ISAC platform can reuse one waveform for communication and target ranging, but communication data and localization accuracy compete for trajectory geometry and energy. Because target locations are initially uncertain, a trajectory optimized once against coarse coordinates can be poorly formulated.

## System model

- One single-transmit/single-receive rotary-wing UAV serves `M` known communication users and localizes `K` static ground targets in a `1500 m x 1500 m` region.
- The UAV flies at `200 m` altitude, continuously transmits, and senses ranges at regularly spaced hover points.
- Communication performance is minimum accumulated data across users; sensing performance is maximum coordinate CRB across targets.
- The stage objective normalizes communication-data increase and CRB decrease with weight `eta`, under speed, region, energy, and bandwidth constraints.
- Propulsion dominates the energy model; transmission energy is ignored.

## Method

[[multi-stage-estimate-design-sense-trajectory|MSTD]] begins with coarse coordinates from three sensing points near the charging base. For each stage, a log-sum-exp-smoothed objective guides a feasible ascent/SCA waypoint update, a convex bandwidth block is solved in CVX, and the UAV executes communication and hover-point ranging.

All accumulated ranges then feed a grid-search maximum-likelihood coordinate estimator. The next stage is redesigned from the updated target estimates until remaining energy cannot support another regular stage; a final shorter stage uses the residual budget.

## Key findings

- Optimized bandwidth allocation adds at least `0.5 Gbits` over equal bandwidth under the same-total-energy comparison.
- At `eta=0.1`, the reported CRB is nearly ten times the value at `eta=0.9`; reducing `eta` from `0.9` to `0.1` increases transmitted data by about `0.6 Gbits`.
- ISAC is reported to outperform two separate single-function UAVs when both architectures receive the same total energy, but no exact cross-architecture percentage is stated.
- Coordinate MSE is evaluated over 100 Monte Carlo runs; CRB and MSE improve over stages but no confidence interval is given.

## Limitations / parse caveats

The numerical model is single-UAV, fixed-altitude, LoS, static-target, and simulation-only. CRB is loose because range-to-coordinate mapping is nonlinear and hover geometry is deliberately correlated; the paper says this tightness problem is unresolved. MLE uses an unspecified grid, and echo association has no gate, conflict rule, or measured error rate.

Moving-target and multi-UAV variants are conceptual extensions rather than evaluated results. The parse has a missing bandwidth subproblem, a soft-min sign issue, damaged CRB/MLE equations, and an incompatible line-search table value. The solver seeks local improvement only.

## Relation to the corpus

This paper makes localization estimates part of the next trajectory formulation, deepening [[joint-localization-and-communication]] beyond one-shot geometry. It also extends the foundational energy-aware UAV trajectory line represented by [[yong-zeng]] and [[rotary-wing-propulsion-energy-model]].

## Raw artifacts

- Parse: `raw/sources/ISAC_From_the_Sky_UAV_Trajectory_Design_for_Joint_Communication_and_Target_Localization/ISAC_From_the_Sky_UAV_Trajectory_Design_for_Joint_Communication_and_Target_Localization.md`
- Origin PDF: `raw/sources/ISAC_From_the_Sky_UAV_Trajectory_Design_for_Joint_Communication_and_Target_Localization/ISAC_From_the_Sky_UAV_Trajectory_Design_for_Joint_Communication_and_Target_Localization.pdf`
- Figures: `raw/sources/ISAC_From_the_Sky_UAV_Trajectory_Design_for_Joint_Communication_and_Target_Localization/images/`
