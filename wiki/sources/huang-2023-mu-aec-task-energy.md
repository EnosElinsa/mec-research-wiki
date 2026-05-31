---
type: source
title: "Joint Interdependent Task Scheduling and Energy Balancing for Multi-UAV-Enabled Aerial Edge Computing: A Multiobjective Optimization Approach"
authors: ["Xumin Huang", "Chaoda Peng", "Yuan Wu", "Jiawen Kang", "Weifeng Zhong", "Dong In Kim", "Long Qi"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3288379"
venue: "IEEE Internet of Things Journal"
tags: [source, mu-aec, interdependent-tasks, dag, makespan, energy-balancing, cmop, evolutionary-algorithm, local-search]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[interdependent-tasks-dag]]"
  - "[[makespan-minimization]]"
  - "[[energy-balancing-uav]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[local-search-evolutionary]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
created: 2026-05-29
updated: 2026-06-01
---

# Joint Interdependent Task Scheduling and Energy Balancing for Multi-UAV-Enabled Aerial Edge Computing

## Citation

Huang, X., Peng, C., Wu, Y., Kang, J., Zhong, W., Kim, D. I., & Qi, L. (2023). *Joint Interdependent Task Scheduling and Energy Balancing for Multi-UAV-Enabled Aerial Edge Computing: A Multiobjective Optimization Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3288379.

## TL;DR

A user partitions an application into a **directed acyclic graph (DAG)** of interdependent tasks (e.g. face recognition: capture → detect → preprocess → extract → classify). A **leader UAV** in a swarm of J UAVs centrally assigns each task to a UAV (with a process order) and chooses each task's CPU frequency. The CMOP minimizes:

- **G₁** — **makespan** (latest task finish time across UAVs), respecting the DAG dependencies.
- **G₂** — **energy-balancing index** (a measure of variance in per-UAV energy consumption).

Solved with a constrained decomposition-based MOEA augmented by:

- **Local search** that consults the objective values to guide neighborhood moves.
- **Improved genetic operator** that respects task-dependency order during crossover/mutation.

## Why this matters

This paper is the **interdependent-task** entry in the Peng/Huang **CMOP-evolutionary** lineage. Until this point in the wiki, every offloading source treated tasks as independent (each task's destination is decided in isolation). Here:

- The DAG forces a **process order** per UAV: task k on UAV j cannot start until all its predecessors finish, including those on other UAVs (which adds intermediate-data transmission time).
- Multicast intermediate data between UAVs complicates the cost model — when a precedent task has m successors on different UAVs, the source UAV multicasts at γ/m per stream.
- **Energy balancing**, not energy minimization, is the per-UAV objective. This avoids a fairness failure mode in which one UAV is always assigned the cheapest tasks and dies first.

These choices make this paper a strong candidate for the **canonical reference for DAG-aware UAV-MEC** in the wiki — there isn't another in the corpus yet.

## Method outline

- **Decision variable.** Integer x_{i,j} = k > 0: task i is assigned to UAV j with processing order k. x_{i,j} = 0 ⇒ UAV j does not run task i.
- **Constraint.** Process orders must respect DAG: 𝒮_j(k) ∉ pred(𝒮_j(k − 1)) ∀k.
- **Objectives.**
  - G₁ = max_j FT_j (makespan).
  - G₂ = Σ_j ((TE_j − mean(TE)) / ψ)² (energy-balancing index — sum of squared normalized deviations of each UAV's total energy TE_j from the swarm mean, ψ a reference value; Eq. 13).
- **Algorithm.** CMOEA/D-CDP augmented with the local-search and DAG-respecting genetic operator.

## Findings

- Against the CMOEA/D-CDP, PPS, and ToP baselines on three task-graph instances (general, mesh, tree), the proposed algorithm attains lower mean **IGD** and higher mean **HV** — i.e. a better-converged and better-distributed Pareto front trading makespan (G₁) against the energy-balancing index (G₂) (parse Table I, Fig. 5).
- The energy-balancing objective is motivated as preventing the *sudden departure* of high-drain UAVs (fairness across the swarm); the paper optimizes the G₂ balancing index rather than reporting an explicit energy-depletion-timing margin → such a margin is `not in parse`.

## Limitations

- A single user with one DAG per scheduling round. Multi-user contention is left to future work.
- The leader UAV is assumed perfectly trusted and to know all UAVs' capabilities and current state. No partial-observability variant.
- Communication topology between UAVs is symmetric and constant; reality is more dynamic.

## Cross-link with related sources

- **Lineage:** [[peng-2022-cmop-uav-path-planning]] (seed) → [[peng-2024-energy-time-uav-its]] → [[huang-2025-cmop-dispersed-computing]] → **this paper** (DAG awareness) → [[wu-2026-terrain-aware-uav-mec]] (terrain awareness).
- **DAG-aware** scheduling is a wiki-first; pairs with the broader **dependent task** discussion in synthesis pages.
- **Energy balancing** as an explicit objective (rather than a constraint or implicit fairness term) is also picked up in [[nabi-2025-jour-hierarchical-aerial]]'s ESAC reward — different mechanism, same goal.

## Raw artifacts

- `raw/sources/Joint_Interdependent_Task_Scheduling_and_Energy_Balancing_for_Multi-UAV-Enabled_Aerial_Edge_Computing_A_Multiobjective_Optimization_Approach/full.md`
