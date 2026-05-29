---
type: source
title: "On a Hierarchical Content Caching and Asynchronous Updating Scheme for Non-Terrestrial Network-Assisted Connected Automated Vehicles"
authors: ["Bomin Mao", "Yangbo Liu", "Hongzhi Guo", "Yijie Xun", "Jiadai Wang", "Jiajia Liu", "Nei Kato"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3460063"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, non-terrestrial-network, content-caching, connected-automated-vehicles, ant-colony-optimization, multi-agent-drl, leo-satellite]
related:
  - "[[non-terrestrial-network]]"
  - "[[service-caching-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[ant-colony-optimization]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
  - "[[zhao-2025-traj-offload-cache-migration]]"
created: 2026-05-29
updated: 2026-05-29
---

# On a Hierarchical Content Caching and Asynchronous Updating Scheme for Non-Terrestrial Network-Assisted Connected Automated Vehicles

## Citation

Mao, B., Liu, Y., Guo, H., Xun, Y., Wang, J., Liu, J., & Kato, N. (2024). *On a Hierarchical Content Caching and Asynchronous Updating Scheme for Non-Terrestrial Network-Assisted Connected Automated Vehicles*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3460063.

## TL;DR

Content caching for **connected automated vehicles (CAVs)** served by **non-terrestrial networks (NTNs)** of LEO satellites and UAVs (for collaborative viewing, traffic sensing, metaverse entertainment in remote areas). Treating all LEO satellites as caching nodes causes content duplication and interference, so the authors use **Delay-Motivated Ant Colony Optimization (DM-ACO)** to select caching satellites with reduced propagation delay, then a **Multi-Agent DRL-based Hierarchical Caching and Asynchronous Updating (MADRL-HCAU)** strategy to manage LEO/UAV caching capacity with customized QoS.

## Problem framing

NTNs give seamless coverage for CAVs, but heterogeneous caching hardware, varying communication environments, and frequent dynamics complicate caching policy. Two issues: (1) using every LEO as a cache wastes storage and degrades transmission via interference; (2) providing customized QoS via intra-/inter-layer cooperative caching is open.

## System model

- **Tiers.** LEO satellites + UAVs (NTN) caching for ground CAVs ([[non-terrestrial-network]], [[leo-satellite-edge-computing]]).
- **Caching-satellite selection** posed as a weighted minimum-vertex-cover (WMVC) problem minimizing system propagation delay.

## Method

- **DM-ACO:** delay-motivated ant colony optimization selects caching LEO satellites to reduce propagation delay ([[ant-colony-optimization]]).
- **MADRL-HCAU:** multi-agent DRL hierarchical caching + asynchronous updating manages LEO/UAV caching capacity, providing customized CAV services and dispensing peak traffic ([[centralized-training-decentralized-execution]]).

## Key findings

- Simulations show the scheme accelerates caching refresh and content downloading, reduces packet drop, and improves cache hit ratio (CHR) and average transmission delay versus popularity-aware and traditional LIFO caching (qualitative; specific curves in the paper).

## Limitations / future work

The authors note MADRL-HCAU's robust scalability to SAGINs (treating RSUs/BSs as fixed gravity-free UAVs) as a future direction.

## Relation to the corpus

A **caching over non-terrestrial networks** entry that complements the UAV caching/service-placement work [[zhao-2024-caching-service-placement-uav]] and the caching/migration study [[zhao-2025-traj-offload-cache-migration]], extending caching into the LEO/NTN + vehicular space. Introduces [[non-terrestrial-network]] and [[ant-colony-optimization]] to the corpus and reinforces [[service-caching-mec]].

## Raw artifacts

- `raw/sources/On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles/full.md`
- Original PDF and extracted figures in the same folder.
