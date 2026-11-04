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
updated: 2026-11-03
---

# TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System

## Citation

Qiu, Q., Li, L., Xiao, Z., Lin, Q., Ma, L., & Ming, Z. (2025). *TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System*. Venue and DOI are not in the parse.

## TL;DR

TOM jointly controls UAV trajectories, vehicle offloading, and parallel stateful-service migration in a dynamic UAV-enabled vehicular edge system. A dynamic multifactorial evolutionary algorithm minimizes UAV flight cost, vehicle energy, migration time, and age of information while adapting its population after environmental changes.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAV edge servers follow moving vehicles that generate partially offloadable tasks and depend on stateful services whose virtual-machine memory must migrate when hosting changes; parallel migration is limited by inter-UAV distance and bandwidth.

**Problem & objective**: Problem $\mathbb P0$ (16) is a dynamic multi-objective problem, $\min_{L_j,\theta_i,PSG}\{FC,EC,AoI,MT\}$, minimizing UAV flight cost, vehicle energy consumption, age of information, and service migration time.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV trajectory | $L_j$ | continuous positions | Trajectory decision of UAV $j$ |
| Offloading ratio | $\theta_i$ | continuous, $[0,1]$ | Fraction of vehicle $i$'s task offloaded |
| Parallel service groups | $PSG$ | grouping / ordering | Service-migration decision that groups compatible migrations in parallel |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| (17) | $\theta_i\in[0,1]$ |
| (18)-(19) | Storage and computational resources of each UAV are not exceeded |
| (20) | Local plus edge delay is within the task's maximum admissible delay $\psi_i$ |
| (21) | Per-slot UAV travel distance is at most $\Delta t\times\nu^{uav}$ |
| (22) | Each vehicle is within the service range of its nearest UAV |

**Algorithm**: Initialize solutions through random, Circle-map, and K-means seeds; evolve linked optimization tasks through dynamic multifactorial evolution and custom mutation; schedule compatible service migrations in parallel; and trigger environmental adaptation when vehicle and network state change.

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
