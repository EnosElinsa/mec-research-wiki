---
type: source
title: "Achieving Optimal 3-D Object Visual Coverage With a Single UAV"
authors: ["Hao Gong", "Baoqi Huang", "Bing Jia"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3646339"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-visual-coverage, trajectory-optimization, viewpoint-planning, energy-efficiency, b-spline, rotary-wing-uav]
related:
  - "[[path-aware-3d-visual-coverage]]"
  - "[[uav-trajectory-control]]"
  - "[[b-spline-trajectory]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[energy-latency-tradeoff]]"
created: 2026-07-10
updated: 2026-07-16
modeling_card: required
---

# Achieving Optimal 3-D Object Visual Coverage With a Single UAV

## Citation

Gong, H., Huang, B., & Jia, B. (2026). *Achieving Optimal 3-D Object Visual Coverage With a Single UAV*. **IEEE Transactions on Mobile Computing**, 25(6), 7970-7987. DOI: 10.1109/TMC.2025.3646339.

## TL;DR

Jointly optimizes viewpoint selection and flight trajectory for a single camera-equipped UAV that must visually cover a 3-D object. The paper argues that viewpoint generation has to be path-aware and that path planning should optimize propulsion energy, not just distance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A camera-equipped rotary-wing UAV observes a three-dimensional object from selected viewpoints while flying a smooth, energy-aware route.

**Problem & objective**: Select viewpoints and a feasible trajectory to maximize coverage quality and then minimize propulsion energy, $\max \sum_i J_i$ and $\min E_{\mathrm{prop}}$, subject to coverage, safety, and vehicle limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Viewpoint positions | $P_{\mathrm{os}}=\{p_o^i\}$ | continuous 3-D points | Camera locations used to cover object facets |
| Viewpoint pitch | $P_{\mathrm{it}}=\{\theta^i\}$ | bounded angles | Camera pitch at each viewpoint |
| Viewpoint yaw | $Y=\{\phi^i\}$ | bounded angles | Camera yaw at each viewpoint |
| B-spline controls and timing | $C=\{\xi\},T$ | continuous controls and knots | Smooth SE(3) path and timing variables |
| Viewpoint count | $N$ | positive integer | Number of selected observation poses |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Every object facet is covered by at least one selected viewpoint |
| C2 | Observation distance stays near the desired range and adjacent views satisfy FOV overlap |
| C3 | The UAV maintains the prescribed safe distance from the object and obstacles |
| C4 | Total propulsion energy does not exceed the available budget |
| C5 | Speed, acceleration, attitude, endpoint, and SE(3) kinematic limits are satisfied |

**Algorithm**: Generate a path-aware viewpoint set with informed RRT*-SA, smooth the ordered poses with an SE(3) B-spline, and refine timing and control points by sequential quadratic programming for energy minimization.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gong et al. [x] coupled viewpoint generation with propulsion-aware trajectory design for a camera-equipped UAV covering a three-dimensional object. They optimized viewpoint positions and attitudes, B-spline control points, timing, and viewpoint count under full-facet coverage, adjacent-view overlap, observation-distance, safety, energy, and kinematic constraints. Their hierarchical solver combines path-aware informed RRT*-SA viewpoint generation with SE(3) B-spline smoothing and SQP energy refinement. Across four simulated objects, energy optimization reduced both energy and flight time relative to distance optimization, including 98.19 kJ versus 887.45 kJ for Big Ben and 89.69 kJ versus 882.72 kJ for Christ.

## Problem

Greedy viewpoint generation can cover all object facets but create a flight path that is unnecessarily expensive. Distance-minimizing paths can also be energetically poor because multi-rotor propulsion depends on velocity, acceleration, and time. The paper couples viewpoint-set generation with energy-efficient trajectory planning to reduce both viewpoint count and flight energy.

## System model

- A multi-rotor UAV carries an infrared camera and uses a rough prior mesh of the object, obtained from LiDAR.
- Each viewpoint includes position, pitch, yaw, and the visible object facets.
- Adjacent viewpoints must preserve field-of-view overlap, commonly at thresholds of 60%, 70%, or 80%.
- Constraints include full facet coverage, near-uniform observation distance, safe distance, energy budget, speed/acceleration limits, attitude constraints, and SE(3) kinematics.
- The energy model focuses on propulsion; communication energy is treated as negligible.

## Method

The method first generates a path-aware viewpoint set with overlapping-field-of-view constraints. It then plans an energy-efficient route through those viewpoints using an informed RRT*-SA search with dynamic sampling and simulated-annealing rewiring. A B-spline SE(3) trajectory is smoothed and then refined through sequential quadratic programming for energy minimization.

## Key findings

- Simulation parameters include horizontal FOV 120 degrees, vertical FOV 90 degrees, desired observation distance 15 m, safe distance 5 m, max speed 25 m/s, max acceleration 1.5 m/s^2, 15 B-spline control points, order 6, and energy budget 1000 kJ.
- Objects include Big Ben, Hoa Hakananai'a, Christ, and House; cases are evaluated at overlap thresholds of 60%, 70%, and 80%.
- The abstract reports up to 89.84% energy reduction versus conventional distance-optimized path planning.
- Table III reports Big Ben energy of 98.19 kJ for the energy-based method versus 887.45 kJ for distance optimization, and Christ energy of 89.69 kJ versus 882.72 kJ.
- The energy-optimized paths often use speeds and accelerations more than twice those of distance-optimized paths while still consuming less energy.
- Informed RRT*-SA can generate all qualified viewpoints for Hoa Hakananai'a at 60% overlap; Gau-RRT* fails for Hoa Hakananai'a and Christ at 80% overlap in the parsed results.

## Relation to the corpus

This is adjacent UAV sensing/inspection work rather than MEC. It extends [[uav-trajectory-control]] with path-aware coverage and connects directly to [[b-spline-trajectory]] and [[rotary-wing-propulsion-energy-model]]. It is useful for separating "shortest path" from "lowest propulsion energy" in UAV sensing papers.

## Limitations / extraction notes

The local parse lacks top-level DOI, venue, and year; the bibliographic fields above are title-matched DOI metadata. The experiments are simulation-only. The paper notes internally occluded objects as a remaining challenge, where skeleton or point-cloud analysis and finer viewpoint sampling would be needed.

## Raw artifacts

- Parse: `raw/sources/Achieving_Optimal_3-D_Object_Visual_Coverage_With_a_Single_UAV/Achieving_Optimal_3-D_Object_Visual_Coverage_With_a_Single_UAV.md`
- Origin PDF: `raw/sources/Achieving_Optimal_3-D_Object_Visual_Coverage_With_a_Single_UAV/Achieving_Optimal_3-D_Object_Visual_Coverage_With_a_Single_UAV.pdf`
- Figures: `raw/sources/Achieving_Optimal_3-D_Object_Visual_Coverage_With_a_Single_UAV/images/`
