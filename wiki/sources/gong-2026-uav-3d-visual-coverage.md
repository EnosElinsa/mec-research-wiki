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
updated: 2026-11-03
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

**Problem & objective**: Problem (P1) (18) is decomposed into (P1.1), which picks viewpoint positions and attitudes to maximize the summed coverage-distance quality $\sum_iJ(\mathbf p_o^{i-1},\mathbf p_o^i,\theta^i,\varphi^i)$ s.t. (6)–(8), and (P1.2), which minimizes the segment energy $\sum_iE_{i,i+1}$ over B-spline controls $\mathbb C$ and timing $\mathbb T$ s.t. (13)–(14) and (18a)–(18d).

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
| (6) | Full coverage: the deduplicated union of facets seen by all viewpoints equals all $q$ object facets |
| (7) | Uniform observation distance: $\lvert\lVert\mathbf p_o^i-\mathbf c_o^i\rVert-d_o\rvert\le\beth$ |
| (8) | Adjacent-view FOV overlap: $O_{i,i+1}^c\ge O_{\min}^c$ |
| (13) | Safe distance from the object along each segment: $\widetilde{Dist}(\mathbf S_{i,i+1}(t),\mathcal F)\ge d_s$ |
| (14) | Energy budget: $E_O\le E_{\max}$ |
| (18a)–(18d) | Speed $\le v_{\max}$, acceleration $\le a_{\max}$, and pitch/yaw continuity at viewpoints (constraints of (P1.2); garbled in the parse, so check the published paper) |

**Algorithm**: Generate a path-aware viewpoint set with informed RRT*-SA, smooth the ordered poses with an SE(3) B-spline, and refine timing and control points by sequential quadratic programming for energy minimization.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gong et al. [x] coupled viewpoint generation with propulsion-aware trajectory design for a camera-equipped UAV covering a three-dimensional object. They optimized viewpoint positions and attitudes, B-spline control points, timing, and viewpoint count under full-facet coverage, adjacent-view overlap, observation-distance, safety, energy, and kinematic constraints. Their hierarchical solver combines path-aware informed RRT*-SA viewpoint generation with SE(3) B-spline smoothing and SQP energy refinement. Across four simulated objects, energy-based optimization reduced both energy and flight time relative to distance-based and energy-line-based optimization, including 98.19 kJ versus 887.45 kJ for Big Ben and 89.69 kJ versus 882.72 kJ for Christ.

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
