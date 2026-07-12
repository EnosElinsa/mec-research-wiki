---
type: source
title: "Deploying UAVs and Surveillance Cameras for Continuous Omnidirectional Monitoring"
authors: ["Haihan Zhang", "Haipeng Dai", "Yuben Qu", "Chaocan Xiang", "Yongxi Sui", "Shiju Zhao", "Zhenzhe Zheng", "Guihai Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3642129"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-deployment, surveillance-camera, visual-coverage, submodular-maximization, path-planning, field-test]
related:
  - "[[continuous-omnidirectional-monitoring]]"
  - "[[path-aware-3d-visual-coverage]]"
  - "[[geometric-disk-cover]]"
  - "[[uav-trajectory-control]]"
  - "[[yuben-qu]]"
created: 2026-07-12
updated: 2026-07-12
---

# Deploying UAVs and Surveillance Cameras for Continuous Omnidirectional Monitoring

## Citation

Zhang, H., Dai, H., Qu, Y., Xiang, C., Sui, Y., Zhao, S., Zheng, Z., & Chen, G. (2026). *Deploying UAVs and Surveillance Cameras for Continuous Omnidirectional Monitoring*. **IEEE Transactions on Mobile Computing**, 25(5), 6720-6739. DOI: 10.1109/TMC.2025.3642129.

## TL;DR

Jointly selects camera rentals and UAV position, orientation, path, and departure time to maximize continuous monitoring across every horizontal viewing direction of target objects. The JUMP pipeline reduces the continuous strategy space, plans shortest paths around no-fly zones, and applies approximation-guaranteed submodular selection; a ten-UAV field test supports the geometric deployment results.

## Problem

Directional cameras can see only part of an object's circumference at any moment. Fixed cameras offer persistent coverage but are budget-limited, while UAVs can reposition but spend time and energy traveling around no-fly regions. For each target and horizontal viewing direction, the objective unions monitoring intervals contributed by all selected devices, normalizes by task duration, and then averages over directions and targets; overlapping simultaneous views are counted once.

## System model

- The task contains target objects, camera-equipped UAVs, and fixed candidate surveillance cameras that can be rented under a budget.
- Circular no-fly zones surround objects. UAVs depart from a common source, follow shortest obstacle-avoiding paths at constant speed, and hover at selected positions and orientations for the duration permitted after reserving energy for outbound and return travel.
- Fixed cameras remain active for the full task. Both device types use a sector field-of-view model over a two-dimensional projection.
- [[continuous-omnidirectional-monitoring]] averages normalized unioned monitoring time over every target and every sampled horizontal direction, avoiding double counting when devices overlap.

## Method

JUMP discretizes time and viewing direction with a bounded utility loss. Camera orientations are reduced to event angles at which objects enter or leave a field of view. UAV placements are reduced by enumerating coverage sets induced by up to three objects and partitioning their feasible regions into monitoring-equivalent subareas.

For each candidate UAV area, a visible-tangents graph and enhanced `A*` search generate shortest paths around overlapping circular obstacles and feasible departure times. The reduced problem is then expressed as monotone submodular maximization under one partition matroid and two knapsack constraints. A thresholded value-density greedy algorithm achieves a stated `1/[6(1+epsilon)]` approximation for the reduced problem, improving to `1/[4(1+epsilon)]` when camera costs are equal; after discretization, the corresponding complete-problem ratios are stated as `1/6-epsilon_1` and `1/4-epsilon_1`.

## Key findings

- Across nine simulation sweeps, prose-stated average improvements over the adapted DUET baseline range from `13%` to `44%`; larger gains against weaker random, grid, and coordinate baselines reach `1446%` in one sweep.
- The physical test uses ten Mavic Air 2 UAVs, twenty candidate camera nodes with Sony Alpha a6000 cameras, and twenty cylindrical targets divided into twenty directions.
- Field-test monitoring utilities are JUMP `0.73`, DUET `0.59`, GCDO `0.20`, and GCGO `0.51`, corresponding to `1.23x`, `3.65x`, and `1.43x` the three baselines.
- NP-hardness follows from a two-dimensional unit-disk-cover special case; the approximation ratios are theoretical results, while the utility comparisons are simulation or field evidence.

## Limitations / parse caveats

The evaluated model projects geometry to two dimensions, assumes static objects and no-fly zones, steady UAV altitude, constant average speed, binary geometric visibility, and a simple movement/hover energy model. Recognition accuracy, scene occlusion, video quality, communication latency, and the discussion's dynamic aerodynamic extension are not evaluated in the reported experiments. Simulation points average 30 random topologies, but the field section gives no repeated-trial count or confidence interval. The parse loses some area dimensions and corrupts formulas and a field-results table; only explicitly printed parameters and final utility values are retained. Publication metadata was verified through the DOI's exact-title Crossref record.

## Relation to the corpus

This source extends visual coverage beyond viewpoint generation in [[path-aware-3d-visual-coverage]] by optimizing coverage duration and all horizontal viewing directions across heterogeneous fixed and mobile cameras. Its unit-disk-cover hardness argument connects to [[geometric-disk-cover]], while obstacle-aware path and departure-time selection sit under [[uav-trajectory-control]]. Co-author [[yuben-qu]] also appears in the corpus's UAV-swarm collaborative-inference systems.

## Raw artifacts

- Parse: `raw/sources/Deploying_UAVs_and_Surveillance_Cameras_for_Continuous_Omnidirectional_Monitoring/Deploying_UAVs_and_Surveillance_Cameras_for_Continuous_Omnidirectional_Monitoring.md`
- Origin PDF: `raw/sources/Deploying_UAVs_and_Surveillance_Cameras_for_Continuous_Omnidirectional_Monitoring/Deploying_UAVs_and_Surveillance_Cameras_for_Continuous_Omnidirectional_Monitoring.pdf`
- Figures: `raw/sources/Deploying_UAVs_and_Surveillance_Cameras_for_Continuous_Omnidirectional_Monitoring/images/`
