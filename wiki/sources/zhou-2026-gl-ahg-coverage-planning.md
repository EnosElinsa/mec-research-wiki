---
type: source
modeling_card: required
title: "GL-AHG: A Novel Game-Learning Alternating Hierarchical Genetic Algorithm for UAV-Enabled Coverage Path Planning"
authors: ["Liangke Zhou", "Jie Chen", "Riheng Jia", "Changbing Tang", "Yang Liu", "Minglu Li"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3682715"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, coverage-path-planning, weighted-vertex-cover, game-learning, genetic-algorithm, visual-coverage, energy-aware-routing]
related:
  - "[[path-aware-3d-visual-coverage]]"
  - "[[genetic-algorithm]]"
  - "[[uav-trajectory-control]]"
  - "[[riheng-jia]]"
  - "[[minglu-li]]"
created: 2026-07-13
updated: 2026-07-16
---

# GL-AHG: A Novel Game-Learning Alternating Hierarchical Genetic Algorithm for UAV-Enabled Coverage Path Planning

## Citation

Zhou, L., Chen, J., Jia, R., Tang, C., Liu, Y., & Li, M. (2026). *GL-AHG: A Novel Game-Learning Alternating Hierarchical Genetic Algorithm for UAV-Enabled Coverage Path Planning*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3682715.

## TL;DR

Couples terrain waypoint generation with route energy instead of solving them independently. Energy-derived waypoint weights form a weighted vertex-cover problem addressed by an asymmetric snowdrift/TD learning scheme; an alternating hierarchical genetic algorithm then searches distance-energy routes with a persistent Pareto archive.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-speed UAV with a gimbal-fixed camera, searchlight, or LiDAR must completely cover a smooth three-dimensional terrain surface. Candidate waypoints are generated from overlapping sensing footprints, wind is neglected, and the energy proxy combines flight distance with turning and slope angles; the formulation is geometric rather than radio-access based.

**Problem & objective**: GL-AHG couples minimum weighted vertex cover with multi-objective path planning, first minimizing $\sum_i w_i x_i$ for coverage and then minimizing $\bigl(\mathcal L(s),\mathcal E(s)\bigr)$ over waypoint sequences.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Waypoint cover state | $x_i$ | binary | Whether candidate vertex $V_i$ is retained as a sensing waypoint |
| Vertex strategy | $a_i$ | categorical, $\{C,D\}$ | Covered or uncovered action in the asymmetric snowdrift game |
| Route sequence | $s$ | permutation | Visiting order of generated waypoints |
| Final trade-off weight | $\lambda$ | continuous, $[0,1]$ | Relative energy weight in Pareto-solution selection |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every graph edge has at least one covered endpoint, $x_i+x_j\geq1$ |
| C2 | Sensing footprints satisfy the adopted overlap and complete-area coverage conditions |
| C3 | The route visits every retained representative waypoint |
| C4 | The flight path remains on the terrain-offset surface and avoids cutting through terrain |
| C5 | Dense valley clusters retain a central representative while preserving modeled coverage |

**Algorithm**: Generate terrain-offset candidate waypoints → map incoming path-energy costs to vertex weights → solve weighted vertex cover with asymmetric snowdrift game and TD learning → simplify dense valley clusters → alternate distance-heavy and energy-heavy genetic search → maintain a Pareto archive and select a normalized trade-off route.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhou et al. [x] studied three-dimensional UAV coverage path planning by coupling waypoint generation with route energy. They transformed energy-aware waypoint selection into a weighted vertex-cover problem and used an asymmetric snowdrift game with temporal-difference learning to obtain a covered waypoint set. The subsequent path-planning stage minimizes flight length and energy consumption over waypoint permutations. Their alternating hierarchical genetic algorithm switches between distance-oriented and energy-oriented fitness functions while maintaining and reinjecting a Pareto archive. Simulations on four-peak, eight-peak, and Wucheng terrain models report shorter paths and lower energy consumption than the evaluated representative coverage algorithms.

## Problem framing

Coverage-complete waypoint sets can force excessive turns, slopes, and route length when generated without path cost. GL-AHG pushes a distance-plus-angle energy proxy into waypoint selection, then plans the visiting order for cameras, searchlights, or LiDAR flying over 3-D terrain.

## System model

- A smooth terrain/DEM is represented by a B-spline surface and offset along normals to form the UAV flight surface.
- The gimbal-fixed sensor faces the terrain; sensing footprints use a 30% circular-overlap assumption.
- UAV mass and speed are constant, wind is absent or light/constant, and battery discharge is ideal.
- Energy is a linear proxy over distance and turning/slope angle, not a detailed propulsion model.
- Convex polygons are handled directly; concave regions are assumed decomposable.

## Method

Candidate grid vertices receive the mean energy cost of incoming neighbor moves. A game-learning weighted vertex-cover stage combines an asymmetric snowdrift game, TD-style payoff updates, and a Fermi decision rule so lower-weight endpoints tend to be selected. Dense valley clusters are reduced to a central representative.

The AHG path stage alternates distance-heavy (`0.7L+0.3E`) and energy-heavy (`0.3L+0.7E`) fitness every 100 generations, maintains non-dominated solutions, injects archive elites every 50 generations, and uses order crossover and swap mutation. A final normalized weighted score selects one route.

## Key findings

- Four-peak terrain: GL-AHG reports `1348.3 m` and `250.4 kJ` versus BF's `2029.1 m` and `282.6 kJ`, reductions of `33.6%` and `11.4%`.
- Eight-peak terrain: `2301.4 m` and `447.0 kJ` versus `3453.0 m` and `525.7 kJ`, reductions of `33.4%` and `15.0%`.
- Wucheng DEM simulation: `19043.2 m` and `2648.3 kJ` versus `26889.1 m` and `3816.7 kJ`, reported reductions of `29.2%` and `30.6%`.
- The stated AHG complexity is `O(T(N^2+NM))`; no convergence theorem or runtime-scaling experiment is given.

## Limitations / parse caveats

The real-terrain case is DEM simulation, not flight testing. No repeated-run statistics, runtime, public DEM product, comparator-tuning protocol, obstacle model, or dynamic wind is reported. Valley-cluster reduction lacks a formal coverage criterion. The overlap requirements, two spacing values, one real-terrain Spiral percentage, raw-unit fitness weighting, cosine-law expression, strategy initialization, and Boltzmann parameter contain conflicts or damage; exact formulas should not be normalized from the parse.

## Relation to the corpus

This source extends [[path-aware-3d-visual-coverage]] with an explicit upstream/downstream coupling: route energy becomes a weighted-vertex-cover cost before [[genetic-algorithm|genetic]] route search. It is adjacent UAV sensing and planning, not an MEC offloading formulation.

## Raw artifacts

- Parse: `raw/sources/GL-AHG_a_Novel_Game-Learning_Alternating_Hierarchical_Genetic_Algorithm_for_UAV-Enabled_Coverage_Path_Planning/GL-AHG_a_Novel_Game-Learning_Alternating_Hierarchical_Genetic_Algorithm_for_UAV-Enabled_Coverage_Path_Planning.md`
- Origin PDF: `raw/sources/GL-AHG_a_Novel_Game-Learning_Alternating_Hierarchical_Genetic_Algorithm_for_UAV-Enabled_Coverage_Path_Planning/GL-AHG_a_Novel_Game-Learning_Alternating_Hierarchical_Genetic_Algorithm_for_UAV-Enabled_Coverage_Path_Planning.pdf`
- Figures: `raw/sources/GL-AHG_a_Novel_Game-Learning_Alternating_Hierarchical_Genetic_Algorithm_for_UAV-Enabled_Coverage_Path_Planning/images/`
