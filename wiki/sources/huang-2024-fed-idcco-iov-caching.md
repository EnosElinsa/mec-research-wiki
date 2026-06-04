---
type: source
title: "Joint Data Caching and Computation Offloading in UAV-Assisted Internet of Vehicles via Federated Deep Reinforcement Learning"
authors: ["Jiwei Huang", "Man Zhang", "Jiangyuan Wan", "Ying Chen", "Ning Zhang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3429507"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, vehicular-mec, data-caching, federated-learning, drl, internet-of-vehicles]
related:
  - "[[vehicular-mec]]"
  - "[[task-offloading]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
created: 2026-06-04
updated: 2026-06-04
---

# Joint Data Caching and Computation Offloading in UAV-Assisted Internet of Vehicles via Federated Deep Reinforcement Learning

## Citation

Huang, J., Zhang, M., Wan, J., Chen, Y., & Zhang, N. (2024). *Joint Data Caching and Computation Offloading in UAV-Assisted Internet of Vehicles via Federated Deep Reinforcement Learning*. **IEEE Transactions on Vehicular Technology**, 73(11). DOI: 10.1109/TVT.2024.3429507. (Received 9 October 2023; accepted 18 June 2024; published 18 July 2024; current version 7 November 2024.)

## TL;DR

In UAV-assisted IoV, UAVs hover above traffic intersections, serving vehicles with limited computing and storage alongside macro base stations (MBSs). The paper jointly optimizes dynamic **data caching** and **computation offloading** to minimize average task processing delay and maximize UAV cache hit ratio. A DRL-based algorithm (IDCCO) addresses the large-scale dynamic state/action space. A **federated learning (FL)** distributed training mechanism trains DRL locally on each UAV and aggregates parameters at the MBS — preserving vehicle privacy and accelerating convergence vs. centralized training. Results show superiority over baselines in delay, cache hit ratio, and training speed.

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
