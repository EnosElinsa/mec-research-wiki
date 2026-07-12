---
type: source
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
updated: 2026-07-13
---

# GL-AHG: A Novel Game-Learning Alternating Hierarchical Genetic Algorithm for UAV-Enabled Coverage Path Planning

## Citation

Zhou, L., Chen, J., Jia, R., Tang, C., Liu, Y., & Li, M. (2026). *GL-AHG: A Novel Game-Learning Alternating Hierarchical Genetic Algorithm for UAV-Enabled Coverage Path Planning*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3682715.

## TL;DR

Couples terrain waypoint generation with route energy instead of solving them independently. Energy-derived waypoint weights form a weighted vertex-cover problem addressed by an asymmetric snowdrift/TD learning scheme; an alternating hierarchical genetic algorithm then searches distance-energy routes with a persistent Pareto archive.

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
