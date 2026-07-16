---
type: source
title: "Joint Data Caching and Computation Offloading in UAV-Assisted Internet of Vehicles via Federated Deep Reinforcement Learning"
authors: ["Jiwei Huang", "Man Zhang", "Jiangyuan Wan", "Ying Chen", "Ning Zhang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3429507"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
modeling_card: required
tags: [source, uav-mec, vehicular-mec, data-caching, federated-learning, drl, internet-of-vehicles]
related:
  - "[[vehicular-mec]]"
  - "[[task-offloading]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
created: 2026-06-04
updated: 2026-07-16
---

# Joint Data Caching and Computation Offloading in UAV-Assisted Internet of Vehicles via Federated Deep Reinforcement Learning

## Citation

Huang, J., Zhang, M., Wan, J., Chen, Y., & Zhang, N. (2024). *Joint Data Caching and Computation Offloading in UAV-Assisted Internet of Vehicles via Federated Deep Reinforcement Learning*. **IEEE Transactions on Vehicular Technology**, 73(11). DOI: 10.1109/TVT.2024.3429507. (Received 9 October 2023; accepted 18 June 2024; published 18 July 2024; current version 7 November 2024.)

## TL;DR

In UAV-assisted IoV, UAVs hover above traffic intersections, serving vehicles with limited computing and storage alongside macro base stations (MBSs). The paper jointly optimizes dynamic **data caching** and **computation offloading** to minimize average task processing delay and maximize UAV cache hit ratio. A DRL-based algorithm (IDCCO) addresses the large-scale dynamic state/action space. A **federated learning (FL)** distributed training mechanism trains DRL locally on each UAV and aggregates parameters at the MBS — preserving vehicle privacy and accelerating convergence vs. centralized training. Results show superiority over baselines in delay, cache hit ratio, and training speed.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One macro base station stores the complete content library, while fixed-hover UAVs at road intersections provide limited cache and MEC capacity to moving vehicles. Each vehicle generates a data-intensive task whose input can be sent either to its serving UAV or to the macro base station, and a UAV cache hit avoids fetching the requested data from the macro base station.

**Problem & objective**: The joint caching, offloading, and computing problem minimizes $\frac{1}{T}\sum_{t=1}^{T}\left[\sum_{u=1}^{U}\lambda\left(1-H_u^t\right)+\sum_{n=1}^{N}T_n(t)\right]$, combining cache misses and task-processing delay.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Cache placement | $x_{u,f}^{t}$ | binary | Whether UAV $u$ caches data item $f$ in slot $t$ |
| Offloading choice | $a_n(t)$ | binary | Whether vehicle task $n$ is processed by the UAV or macro base station |
| UAV compute share | $\gamma_{u,n}(t)$ | continuous, $[0,1]$ | Fraction of UAV $u$ computing capacity assigned to task $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Compute shares are normalized and bounded: $\sum_n\gamma_{u,n}(t)=1$ and $0\le\gamma_{u,n}(t)\le1$ |
| C2 | Cached items fit the UAV storage budget: $\sum_f x_{u,f}^{t}s_f\le S_u$ |
| C3 | Every admitted task finishes within the slot duration: $T_n(t)\le\tau$ |
| C4 | Caching and offloading decisions are binary: $x_{u,f}^{t},a_n(t)\in\{0,1\}$ |

**Algorithm**: IDCCO represents cache placement, offloading, and compute allocation in a TD3 actor, learns from replay with twin critics and delayed policy updates, and updates each UAV from local observations. Fed-IDCCO lets UAVs train locally, upload model parameters rather than vehicle data, and periodically applies weighted federated averaging at the macro base station before broadcasting the global parameters.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] jointly controlled content caching, UAV-versus-MBS task offloading, and UAV compute slicing in a fixed-hover UAV-assisted Internet of Vehicles. They minimized a weighted sum of cache misses and processing delay under compute-share, cache-capacity, per-slot delay, and binary-decision constraints. IDCCO uses TD3 for the mixed control problem, while Fed-IDCCO trains local UAV agents and averages their weights at the MBS without uploading raw vehicle data. Fed-IDCCO converged faster than centralized IDCCO and reduced average delay by 25.1%, 27.6%, 30.7%, and 60.1% versus LRU, FIFO, LFU, and random caching across cache-capacity tests.

## Problem framing

Urban MBS coverage is disrupted by dense buildings; traffic hotspots (intersections) create burst demand. UAVs with MEC servers and limited cache capacity supplement MBSes with LoS links. Tasks are data-intensive (codes, databases, AI models); if a requested data item is already cached on the UAV, download from MBS is avoided. Jointly optimizing which data to cache (given limited UAV storage) and where to compute (local vehicle, UAV, or MBS) under dynamic content popularity and vehicle mobility is the core challenge. Centralized learning requires sharing raw vehicle data, raising privacy concerns; FL avoids this.

## System model

- **1 MBS** (stores all data; always available) + **U UAVs** (limited cache, MEC server, hover above intersections) + **N vehicles** continuously generating data-intensive tasks.
- **Caching:** each UAV caches a subset of data items; cache hit when requested data is already present (no MBS download needed).
- **Offloading:** vehicle sends task to UAV or MBS depending on load, coverage, and cache state.
- **Fed-IDCCO:** each UAV trains its local DRL model using local task/environmental observations → uploads model parameters (not raw data) to MBS for federated averaging → UAVs download updated global parameters.
- **Objectives:** minimize average task processing delay; maximize UAV cache hit ratio.

## Key findings

- Fed-IDCCO achieves **lower average task processing delay and higher cache hit ratio** compared to baseline algorithms (pure DRL without FL, heuristic caching, random offloading) in dynamic IoV scenarios (parse Section IV).
- FL-based distributed training **accelerates DRL convergence** compared to centralized approaches while protecting user privacy (parse contribution 3 / Section IV).
- The combined caching + offloading design outperforms separate optimization of each (parse experiment comparisons).

## Limitations / future work

UAV positions are fixed at intersection hover-points (no trajectory optimization). Content popularity dynamics are DRL-learned but not explicitly modeled. FL aggregation overhead at MBS not quantified in the parse.

## Relation to the corpus

Combines UAV-MEC caching (shared with [[mao-2024-ntn-hierarchical-caching-cav]], [[gao-2024-service-experience-cache-uav]]) with federated learning for privacy-preserving distributed training — a combination distinct from the corpus's other IoV papers. The FL + DRL pattern for cooperative MEC connects to [[zhai-2023-fedleo-decentralized-fl]] (which uses FL for LEO satellite networks).

## Raw artifacts

- `raw/sources/Joint_Data_Caching_and_Computation_Offloading_in_UAV-Assisted_Internet_of_Vehicles_via_Federated_Deep_Reinforcement_Learning/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
