---
type: source
title: "Hierarchical Aerial Computing for Internet of Things via Cooperation of HAPs and UAVs"
authors: ["Ziye Jia", "Qihui Wu", "Chao Dong", "Chau Yuen", "Zhu Han"]
year: 2022
url: "https://doi.org/10.1109/JIOT.2022.3151639"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, hierarchical-aerial-mec, hap, uav, matching-theory, task-offloading, integer-programming]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[task-offloading]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[you-2025-uncertain-maritime-hasac]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
---

# Hierarchical Aerial Computing for Internet of Things via Cooperation of HAPs and UAVs

## Citation

Jia, Z., Wu, Q., Dong, C., Yuen, C., & Han, Z. (2022). *Hierarchical Aerial Computing for Internet of Things via Cooperation of HAPs and UAVs*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2022.3151639.

## TL;DR

A **hierarchical aerial computing** framework of HAPs + UAVs that serves terrestrial IoT in disaster/remote areas. Two offloading schemes: IoT→UAV (computed at UAV) and IoT→UAV→HAP (relayed and computed at HAP). The objective — maximize total successfully-computed IoT data under IoT delay requirements and UAV/HAP resource constraints — is an integer program (intractable). The authors solve IoT→UAV offloading with **matching game theory** (with an externality-elimination mechanism), IoT→HAP offloading with a **heuristic**, and add an adjustment algorithm to fully use aerial resources.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Terrestrial IoT devices offload binary tasks to nearby UAV edge servers or relay them through UAVs to a higher-capacity HAP.

**Problem & objective**: Select IoT-to-UAV and UAV-to-HAP offloading decisions to maximize successfully computed data, $\max_{x,\beta,y,\gamma}\sum_i\sum_u\sum_h\sigma_i(\beta_u^i+\gamma_h^i)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| IoT-to-UAV association | $x_u^i$ | binary | Connect IoT task $i$ to UAV $u$ |
| UAV computation choice | $\beta_u^i$ | binary | Compute task $i$ at UAV $u$ |
| UAV-to-HAP relay | $y_h^{i,u}$ | binary | Forward task $i$ from UAV $u$ to HAP $h$ |
| HAP computation choice | $\gamma_h^i$ | binary | Compute task $i$ at HAP $h$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Each IoT task connects to at most one UAV, $\sum_u x_u^i\leq1$ |
| C2 | UAV computation and relay choices conserve the selected IoT-to-UAV flow |
| C3 | Each UAV serves no more than its IoT quota |
| C4 | HAP computation requires a corresponding UAV relay |
| C5 | IoT, UAV, and HAP energy budgets and each IoT delay deadline are satisfied |

**Algorithm**: Build many-to-one matching preferences, iteratively eliminate externalities and blocking pairs, move overloaded tasks from UAVs to the HAP with a heuristic, and use an adjustment pass to fill residual UAV capacity.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Jia et al. [x] formulated hierarchical aerial computing in which IoT tasks are either computed by a matched UAV or relayed to a higher-capacity HAP. They maximize successfully computed data over binary association, computation, and relay decisions under one-UAV matching, quota, flow, energy, and delay constraints. The solution combines many-to-one matching with externality elimination, a heuristic UAV-to-HAP offloading stage, and an adjustment pass for residual resources. In simulations, the combined MEHA scheme stays close to the exhaustive optimum while using much lower complexity, and the cooperative UAV plus HAP mode serves more IoT data and users than UAV-only or HAP-only alternatives.

## Problem framing

6G IoT in remote/disaster regions needs MEC, and HAPs+UAVs can supply aerial compute. Treating every offloading decision via exhaustive search is prohibitive, so tractable matching/heuristic algorithms are needed that still approach the optimum.

## System model

- **Tiers.** HAPs (high-altitude, large coverage) + UAVs (low-altitude, collect IoT tasks); ground IoT devices.
- **Offloading schemes.** (1) IoT→UAV→compute-at-UAV; (2) IoT→UAV→relay→HAP→compute-at-HAP.
- **Objective.** Maximize total successfully-computed IoT data subject to IoT delay and UAV/HAP resource constraints — an integer programming problem.

## Method

- **IoT→UAV:** [[matching-theory-for-resource-allocation|matching game]]-based algorithm, with an **externality-elimination mechanism** handling the inter-device interplay in matching.
- **UAV→HAP:** a heuristic offloading algorithm.
- **Adjustment algorithm** to make best use of aerial resources; complexity analyzed.

## Key findings

- Numerical results show the algorithms efficiently achieve near-optimal performance versus exhaustive search, and the IoT-UAV-HAP scheme's advantages and parameter sensitivities are analyzed (qualitative; specific curves in the paper).

## Limitations / future work

Future work flagged: dynamic networks with varying traffic load and channel-utilization metrics.

## Relation to the corpus

An early, **matching-theoretic** anchor for the **hierarchical aerial MEC (UAV+HAP)** track that the wiki's later DRL ([[kang-2023-mappo-hierarchical-aerial]]), Gale-Shapley ([[nabi-2025-jour-hierarchical-aerial]]), and DRO ([[jia-2025-dro-uav-hap-mec]]) entries build on. Reinforces [[matching-theory-for-resource-allocation]] and [[hierarchical-aerial-mec]]. Shares co-authors Ziye Jia / Chao Dong / Qihui Wu / Zhu Han with the maritime cooperative-MEC paper [[you-2025-uncertain-maritime-hasac]].

## Raw artifacts

- `raw/sources/Hierarchical_Aerial_Computing_for_Internet_of_Things_via_Cooperation_of_HAPs_and_UAVs/full.md`
- Original PDF and extracted figures in the same folder.
