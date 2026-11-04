---
type: source
title: "A Novel Deep Q-Learning-Based Air-Assisted Vehicular Caching Scheme for Safe Autonomous Driving"
authors: ["Junling Shi", "Liang Zhao", "Xingwei Wang", "Weiliang Zhao", "Ammar Hawbani", "Min Huang"]
year: 2021
url: "https://doi.org/10.1109/TITS.2020.3018720"
venue: "IEEE Transactions on Intelligent Transportation Systems, 22(7)"
modeling_card: required
tags: [source, uav-content-caching, vehicular-networks, airship, deep-q-network, autonomous-driving, cache-placement]
related:
  - "[[uav-content-caching]]"
  - "[[vehicular-mec]]"
  - "[[deep-q-network]]"
  - "[[high-altitude-platform-station]]"
created: 2026-11-02
updated: 2026-11-02
---

# A Novel Deep Q-Learning-Based Air-Assisted Vehicular Caching Scheme for Safe Autonomous Driving

## Citation

Shi, J., Zhao, L., Wang, X., Zhao, W., Hawbani, A., & Huang, M. (2021). *A Novel Deep Q-Learning-Based Air-Assisted Vehicular Caching Scheme for Safe Autonomous Driving*. **IEEE Transactions on Intelligent Transportation Systems, 22**(7). DOI: 10.1109/TITS.2020.3018720.

## TL;DR

UAVs cache driving-safety content for vehicles, and an airship schedules a UAV that holds the content when a vehicle's resident UAV does not. DAVC uses deep Q-learning on historical requests to place content so that request probability of cached items is high and UAV scheduling, a proxy for energy, is low, under per-UAV cache limits and no duplicate copies.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-layer architecture with an airship, $N_u$ UAVs, and vehicles. Each UAV $i$ caches $A_i$ items of equal size $\theta$ up to limit $L_i$. A vehicle asks its resident UAV; if it lacks the content, the airship schedules the UAV holding it.

**Problem & objective**: A bi-objective cache placement: $\max\sum_{i=1}^{N_u}\sum_{j=1}^{N_c}P_{ij}$ (request probability of cached content) and $\min\sum_{i=1}^{N_u}S_i$ (scheduling probability, linked to UAV energy).

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Cache placement | $\mathbf C_i$ | set of contents per UAV | Which content items UAV $i$ caches |
| Cached count | $A_i$ | integer, $\theta A_i\le L_i$ | Number of items cached at UAV $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (8) | Cache capacity, $H_i=\theta A_i\le L_i$. |
| (9) | No redundancy, $Nc_j\le1$ copy of each content across UAVs. |
| Probabilities | $P_{ij}=R_{ij}/\sum_iR_i$ from history; $S_i=\mu\,ST_i/\sum_iST_i$ from scheduling counts. |

**Algorithm**: DQN learns cache placements from historical requests, with a reward combining request and scheduling probabilities; DAVC adds adaptive adjustments to DQN for the caching task.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Shi et al. [x] addressed driving safety-related content demands of vehicle users, noting that distributed vehicular content caching suffers from high response delay and a low response ratio because of poor traffic conditions and building obstructions. They adopted UAVs to assist safety-related content caching and designed a caching scheme that guarantees users' content demands while reducing UAV energy consumption under limited UAV power and storage. They introduced a three-layered content response architecture in which an airship schedules UAVs, built a multi-objective mathematical model of the caching problem, and applied deep Q-learning to solve it by learning from historical content requests. Experiments on a real map with generated vehicle traces show that the scheme outperforms its counterparts in content hit ratio, response delay, scheduling probability, and packet buffering time.

## Problem framing

Vehicles cannot cache everything they need, and ground infrastructure may be blocked. Sparse UAVs have line-of-sight but small caches, so placement determines how often extra UAV flights are needed.

## System model

- Requests carry content, requester, area, and timestamp.
- Each content has only one copy among UAVs.

## Method

DQN with experience replay; most best policies appear within the first 20% of training time.

## Key findings

- DAVC improves content hit ratio, response delay, scheduling probability, and buffering time relative to compared schemes.

## Limitations / future work

The authors note open issues such as the large size of high-precision safety content.

## Relation to the corpus

An early learned placement design for [[uav-content-caching]] in [[vehicular-mec]], with an airship tier related to [[high-altitude-platform-station]].

## Raw artifacts

- Parse: `raw/sources/A_Novel_Deep_Q-Learning-Based_Air-Assisted_Vehicular_Caching_Scheme_for_Safe_Autonomous_Driving/A_Novel_Deep_Q-Learning-Based_Air-Assisted_Vehicular_Caching_Scheme_for_Safe_Autonomous_Driving.md`
- Origin PDF and extracted figures are in the same folder.
