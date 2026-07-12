---
type: source
title: "Bi-Level Optimization Framework for Urban Low-Altitude UAV Delivery Ensuring Target Level of Safety"
authors: ["Bo Jiang", "Yichao Li", "Chenglong Li", "Yuan Zheng"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3660878"
venue: ""
tags: [source, uav-delivery, low-altitude-economy, safety, multi-objective-optimization, trajectory-planning]
related:
  - "[[target-level-of-safety]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[uav-trajectory-control]]"
  - "[[urban-air-mobility]]"
created: 2026-07-11
updated: 2026-07-11
---

# Bi-Level Optimization Framework for Urban Low-Altitude UAV Delivery Ensuring Target Level of Safety

## Citation

Jiang, B., Li, Y., Li, C., & Zheng, Y. (2026). *Bi-Level Optimization Framework for Urban Low-Altitude UAV Delivery Ensuring Target Level of Safety*. DOI: 10.1109/TITS.2026.3660878. The local parse exposes the DOI line but not a reliable venue banner, so the venue field is left blank.

## TL;DR

Models urban low-altitude UAV delivery as a coupled task-allocation and trajectory-planning problem. The upper level uses TC-NSGA-III to balance delivery time, ground risk, and workload; the lower level uses RG-FMT* to find collision-free paths whose waypoint risks satisfy a target level of safety (TLS).

## Problem

Urban UAV logistics is not just a shortest-route problem. Heterogeneous UAVs must receive orders, sequence deliveries, avoid obstacles, balance workload, and keep local ground risk below a safety threshold. Weighted-sum methods can trade risk away, but they cannot guarantee that every path segment satisfies TLS.

## System model

- The environment is a 3-D urban grid with buildings and risk values.
- The upper-level task allocation assigns orders to heterogeneous UAVs and delivery sequences.
- The lower-level planner computes trajectories for the assigned tasks, constrained by grid boundaries, obstacles, payload capacity, uniqueness of assignment, and `R(X_k) <= R_TLS` at waypoints.
- Objectives are total delivery time cost, total path ground risk, and workload-balance variance.

## Method

TC-NSGA-III uses dual-layer chromosomes for allocation and path sequence, then evolves a Pareto solution set over the three objectives. RG-FMT* performs risk-aware sampling and fast-marching-tree path search under TLS constraints. The framework cycles between the levels: allocation decisions call trajectory planning for feasible paths and costs, while planned paths feed the allocation objective values.

## Key findings

- Experiments use MATLAB R2019b on an Intel Core i5-12600KF 10-core CPU with 32 GB RAM; the urban grid is 60 by 60 by 12 cells with 10 m cell length.
- Sensitivity analysis selects crossover 0.4 and mutation 0.2; maximum HV 0.5112 occurs at `lambda = -0.08` and `sigma = 0.7`.
- In 50 random start-goal tests with TLS `1 x 10^-7`, RG-FMT* has 100% TLS compliance, risk `1.013 x 10^-5`, length 31.38, and computation time 0.1484 s.
- In framework comparison over 50 runs, the proposed method reports average risk `1.416 x 10^-5`, average time cost 85.78, and workload balance 607.0.
- The urban scenario uses 1000 simulations with order counts from 1 to 100; a demonstration with 10 UAVs and 25 orders uses population 60, crossover 0.4, mutation 0.2, and 80 iterations.
- The conflict example uses a 10 m collision buffer.

## Limitations / parse caveats

The DOI is present, but the parse lacks a venue name. The author line has a corrupted marker after Yuan Zheng, many symbols are mojibake, and several tables have merged or malformed cells. The page records the stable values visible in prose and parsed tables.

## Relation to the corpus

This source extends [[uav-delivery-pickup-dropoff]] from energy/time tradeoffs into safety-constrained logistics. It links [[compliance-aware-uav-trajectory]] to an explicit [[target-level-of-safety]] constraint and adds a many-objective evolutionary allocation case adjacent to [[non-dominated-sorting-genetic-algorithm]].

## Raw artifacts

- `raw/sources/Bi-Level_Optimization_Framework_for_Urban_Low-Altitude_UAV_Delivery_Ensuring_Target_Level_of_Safety/Bi-Level_Optimization_Framework_for_Urban_Low-Altitude_UAV_Delivery_Ensuring_Target_Level_of_Safety.md`
- Original PDF and extracted figures (`images/`) in the same folder.
