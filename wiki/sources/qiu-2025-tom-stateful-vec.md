---
type: source
title: "TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System"
authors: ["Qijie Qiu", "Lingjie Li", "Zhijiao Xiao", "Qiuzhen Lin", "Lijia Ma", "Zhong Ming"]
year: 2025
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, uav-enabled-vec, service-migration, task-offloading, uav-trajectory, dynamic-multi-objective-optimization, evolutionary-algorithm]
related:
  - "[[service-migration]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[vehicular-mec]]"
  - "[[age-of-information]]"
created: 2026-08-27
updated: 2026-08-27
---

# TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System

## Citation

Qiu, Q., Li, L., Xiao, Z., Lin, Q., Ma, L., & Ming, Z. (2025). *TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System*. Venue and DOI are not in the parse.

## TL;DR

TOM jointly controls UAV trajectories, vehicle offloading, and parallel stateful-service migration in a dynamic UAV-enabled vehicular edge system. A dynamic multifactorial evolutionary algorithm minimizes UAV flight cost, vehicle energy, migration time, and age of information while adapting its population after environmental changes.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAV edge servers follow moving vehicles that generate partially offloadable tasks and depend on stateful services whose runtime context must migrate when hosting changes.

**Problem & objective**: Jointly minimize the dynamic objective vector $\mathbf F=(F_{\mathrm{flight}},F_{\mathrm{energy}},F_{\mathrm{migration}},F_{\mathrm{AoI}})$ over UAV motion, offloading ratios, and service migration plans.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV trajectory | $\mathbf q_k(t)$ | continuous position | Position of UAV $k$ over time |
| Offloading ratio | $\theta_i(t)$ | continuous, $[0,1]$ | Fraction of vehicle $i$'s task offloaded |
| Service host | $h_i(t)$ | discrete UAV index | UAV hosting vehicle $i$'s stateful service |
| Migration plan | $\pi_t$ | ordering / grouping | Parallel service-transfer schedule |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Mobility | UAV positions and displacement obey the modeled flight limits. |
| Offloading | Each ratio satisfies $0\leq\theta_i(t)\leq1$. |
| Capacity | Computation and communication loads remain within UAV resources. |
| State continuity | Hosting changes incur live-migration time and preserve stateful service continuity. |

**Algorithm**: Initialize solutions through random, inherited, and K-means seeds; evolve linked optimization tasks through dynamic multifactorial evolution and custom mutation; schedule compatible service migrations in parallel; and trigger environmental adaptation when vehicle and network state change.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qiu et al. [x] jointly studied trajectory planning, computation offloading, and stateful-service migration in UAV-enabled vehicular edge computing. They formulated a dynamic multi-objective problem over UAV flight cost, vehicle energy consumption, service migration time, and age of information. TOM uses a dynamic multifactorial evolutionary algorithm with heuristic initialization, customized mutation, parallel migration scheduling, and environmental adaptation. Simulations on real-world mobility datasets report better multi-objective performance than the compared peer methods. The study is simulation-based and leaves obstacle avoidance and inter-UAV collaboration for future work.

## Problem and system model

Vehicle movement changes wireless links and useful UAV positions, while service hosting and offloading determine computation load. Stateful applications add migration time and continuity requirements that cannot be represented by restarting stateless tasks.

## Method

The approach encodes motion, offloading, and hosting decisions in a shared evolutionary population. Knowledge transfer between factor tasks accelerates search, a migration-specific routine parallelizes compatible transfers, and an adaptation trigger reacts to environmental change.

## Key findings

- TOM outperforms the reported state-of-the-art multi-objective baselines on real-world mobility datasets.
- The service migration strategy reduces migration time by exploiting parallel transfers.
- Ablation results attribute additional gains to environmental adaptation under changing vehicle distributions.

## Limitations / future work

The evaluation is simulation-based. UAV obstacle avoidance and collaborative UAV strategies are explicitly left for future research.

## Relation to the corpus

TOM connects [[service-migration]], [[task-offloading]], [[uav-trajectory-control]], and [[age-of-information]] in one stateful vehicular formulation. It is an evolutionary counterpart to learned migration and trajectory control in [[feng-2026-prediction-service-migration]].

## Raw artifacts

- Parse: `raw/sources/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md`
- Origin PDF and extracted figures are in the same folder.
