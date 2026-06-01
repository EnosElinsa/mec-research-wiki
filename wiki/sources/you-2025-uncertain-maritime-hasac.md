---
type: source
title: "Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels"
authors: ["Jiahao You", "Ziye Jia", "Chao Dong", "Qihui Wu", "Zhu Han"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3581970"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, computation-offloading, lyapunov-optimization, markov-game, heterogeneous-agent-sac, aav]
related:
  - "[[maritime-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[masac]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[stochastic-game]]"
  - "[[task-offloading]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[jia-2022-hierarchical-aerial-matching]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-05-29
updated: 2026-06-02
---

# Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels

## Citation

You, J., Jia, Z., Dong, C., Wu, Q., & Han, Z. (2025). *Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3581970.

## TL;DR

Maritime MEC via cooperation of autonomous aerial vehicles (AAVs) and vessels, minimizing total task execution time under **uncertain** task arrivals. **Lyapunov optimization** converts the long-term constraints into per-slot short-term ones, yielding small-scale problems; the heterogeneity of AAV/vessel actions and resources is then captured as a **Markov game (MG)**, solved by a **heterogeneous-agent soft actor-critic** that sequentially updates the agents' networks.

## Problem framing

Maritime IoT (MIoT) compute demand is rising, and AAVs + vessels can supply MEC. But maritime tasks arrive unpredictably and resource availability varies, making efficient offloading/allocation hard. The objective is to minimize total execution time despite this uncertainty.

## System model

- **Actors.** MIoT devices, AAVs, vessels — a cooperative MEC framework.
- **Uncertainty.** Unpredictable task arrivals and varying computational-resource availability handled via [[lyapunov-optimization]] (long-term → short-term constraints).
- **Heterogeneity.** AAVs and vessels differ in actions and resources → modeled as a Markov game ([[stochastic-game]]).

## Method

- **Lyapunov optimization** to decompose into per-slot small-scale problems.
- Reformulate each as a **Markov game** and solve with a **heterogeneous-agent soft actor-critic** (sequentially updates each agent's neural networks) ([[masac]] / [[heterogeneous-agent-rl]]).

## Key findings

- The algorithm outperforms baselines in convergence, execution time, computation rate, offloaded data, and percentage of task execution across various environmental conditions (qualitative; specific curves in the paper).

## Limitations / future work

Simulation-based. The parse's conclusion does not enumerate explicit limitations beyond the modeled assumptions.

## Relation to the corpus

A **DRL** treatment of maritime offloading that contrasts with the optimization-based [[wang-2025-double-edge-samin]] and game-theoretic [[wang-2024-twotier-satellite-marine]] approaches to the same maritime/AAV-vessel setting. Its Lyapunov-then-MG-then-heterogeneous-SAC pipeline echoes the Lyapunov+MASAC pattern in [[qin-2025-bcuav-masac]] and the heterogeneous-agent angle of [[zhang-2025-ssac-mgi-heterogeneous-uav]]. Shares co-authors Ziye Jia / Chao Dong / Qihui Wu / Zhu Han with [[jia-2022-hierarchical-aerial-matching]]. Reinforces [[maritime-mec]] and [[lyapunov-optimization]].

## Raw artifacts

- `raw/sources/Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels/full.md`
- Original PDF and extracted figures in the same folder.
