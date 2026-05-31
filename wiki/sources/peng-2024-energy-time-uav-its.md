---
type: source
title: "Joint Energy and Completion Time Difference Minimization for UAV-Enabled Intelligent Transportation Systems: A Constrained Multi-Objective Optimization Approach"
authors: ["Chaoda Peng", "Zexiong Wu", "Xumin Huang", "Yuan Wu", "Jiawen Kang", "Qiong Huang", "Shengli Xie"]
year: 2024
url: "https://doi.org/10.1109/TITS.2024.3395993"
venue: "IEEE Transactions on Intelligent Transportation Systems"
tags: [source, uav, its, multi-source-fusion, cmop, evolutionary-algorithm, time-balancing, service-caching]
related:
  - "[[uav-enabled-its]]"
  - "[[multi-source-data-fusion]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[completion-time-difference]]"
  - "[[service-caching-mec]]"
  - "[[cmoea-d-cdp]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-06-01
---

# Joint Energy and Completion Time Difference Minimization for UAV-Enabled Intelligent Transportation Systems

## Citation

Peng, C., Wu, Z., Huang, X., Wu, Y., Kang, J., Huang, Q., & Xie, S. (2024). *Joint Energy and Completion Time Difference Minimization for UAV-Enabled Intelligent Transportation Systems: A Constrained Multi-Objective Optimization Approach*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2024.3395993.

## TL;DR

A control center dispatches multiple UAVs to monitor traffic at distinct ground locations. Each UAV gathers surveillance data and either processes it locally or offloads to an edge server. The **fusion** of all UAVs' processing results at the control center is sensitive to **temporal misalignment** — if UAVs finish at very different times, the fusion is degraded.

So the CMOP balances:

- **G₁:** total UAV energy consumption.
- **G₂:** total **pairwise completion-time difference** among employed UAVs (a synchronization objective, not a makespan).

Solved with the **CMOEA/D-CDP** framework plus an **improved genetic operator** (data-type aware) and a **repairing constraint-handling technique**.

## Why this matters

The completion-time-difference objective is the original contribution. Most prior wiki sources optimize **mean** or **max** delay; this paper argues that for **multi-source fusion** the **variance** of completion times matters more. That observation is very portable:

- Federated learning round synchronization ([[mao-2025-bcsa-frl]]).
- Multi-vehicle cooperative perception ([[xie-2026-uav-multisource-fusion]]).
- Multi-UAV interdependent task scheduling ([[huang-2023-mu-aec-task-energy]]).

In all those settings, "everyone finish around the same time" is a hidden constraint that's worth pulling explicit.

This paper is also a **lineage** entry in the Peng/Huang group's **CMOP-evolutionary** thread — see [[peng-2022-cmop-uav-path-planning]] for the seed.

## Method outline

- **Decision variables.** Binary task association y_{i,j} (UAV i ↔ task j); binary offloading x_i (local vs edge); UAV computing speeds f_i^L; edge CPU allocation f_i^O; UAV flight speed v_i.
- **Service caching.** Tasks may need a service program. If cached on the edge server (γ_j = 1), retrieval is fast; else fetched from the cloud (extra time r_ES). This is a wiki-first **service-caching** modeling.
- **Genetic operator.** Distinguishes binary, integer, and continuous variables, applying the right crossover/mutation per type.
- **Constraint repair.** Infeasible offspring are surgically repaired (rather than simply discarded).

## Findings

- The repair-CHT + data-type-aware operator beats stock CMOEA/D-CDP baselines on inverted-generational distance and hypervolume.
- Time-difference reduction comes mostly from **balancing offloading** (slow local UAVs offload; fast UAVs run local) — *not* from balancing flight time.
- Energy and time-difference do conflict: pushing all UAVs to offload reduces variance but spikes edge-server energy.

## Limitations

- Static UAV start positions; no trajectory replanning during the mission.
- Synchronization objective uses pairwise differences; could be reformulated as variance for cleaner gradient information (open methodological question).
- I ≥ J assumption — more UAVs than tasks. The reverse case is the interesting one for crowded-deployment scenarios and isn't addressed.

## Cross-link with related sources

- **Lineage:** [[peng-2022-cmop-uav-path-planning]] (seed) → this paper (multi-UAV + time difference) → [[huang-2025-cmop-dispersed-computing]] (reliability via redundancy) → [[wu-2026-terrain-aware-uav-mec]] (terrain awareness) → [[huang-2023-mu-aec-task-energy]] (interdependent tasks).
- **Synchronization-as-objective** is a recurring pattern: see also [[mao-2025-bcsa-frl]]'s round-synchronization in BCSA-FRL.
- **Service caching** is introduced here for the wiki — could be revisited in any future ground-MEC source with caching.

## Raw artifacts

- `raw/sources/Joint_Energy_and_Completion_Time_Difference_Minimization_for_UAV-Enabled_Intelligent_Transportation_Systems_A_Constrained_Multi-Objective_Optimization_Approach/full.md`
