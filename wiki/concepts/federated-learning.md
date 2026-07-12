---
type: concept
title: "Federated Learning (FL)"
tags: [distributed-ml, privacy, aggregation, fedavg]
related:
  - "[[federated-reinforcement-learning]]"
  - "[[seamless-handover]]"
  - "[[adaptive-inter-layer-data-offloading]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
  - "[[li-2026-tspf-forest-fire-uav-swarm]]"
  - "[[two-tier-submodel-partition]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[contract-theoretic-fl-incentives]]"
  - "[[zhao-2026-uav-fl-inspection-incentives]]"
  - "[[chen-2026-sdhfl-completion-time]]"
  - "[[semi-decentralized-hybrid-federated-learning]]"
  - "[[fu-2026-uav-fl-user-grouping]]"
created: 2026-05-29
updated: 2026-07-13
---

# Federated Learning (FL)

[[zhao-2026-uav-fl-inspection-incentives]] adds the incentive/client-selection side of UAV FL: [[contract-theoretic-fl-incentives]] build a candidate UAV pool and then select high-contribution clients for federated intelligent inspection under communication, sensing, computation, and battery costs.

A distributed machine-learning paradigm where many clients train a shared model on their **local** data and send only model updates (not raw data) to an aggregator, which combines them — classically by **FedAvg** (data-size-weighted averaging) — into a global model. It preserves privacy and cuts data movement, but suffers from data heterogeneity (non-IID clients), stragglers, and communication bottlenecks.

This is the base concept underlying the wiki's narrower [[federated-reinforcement-learning]] and [[blockchain-for-fl-aggregation]] pages. In the wiki, [[han-2024-sagin-fl-handover]] orchestrates FL across a SAGIN — satellites and UAVs act as both aggregators and compute units — adding [[adaptive-inter-layer-data-offloading]], satellite [[seamless-handover]], and a [[privacy-sensitive-data-partitioning]] constraint, with a proven convergence guarantee for non-convex losses. Complements [[mao-2025-bcsa-frl]]'s federated-RL-over-satellites approach.

[[wang-2026-blockchain-lae-fl-mappo]] applies FL in a low-altitude UAV-MEC stack: service UAVs train local models, the BS aggregates the global model, and MAPPO uses the learned policy layer for offloading, caching, and resource allocation.

[[li-2026-tspf-forest-fire-uav-swarm]] adds a robust UAV-swarm variant: [[two-tier-submodel-partition]] aggregates selected layers inside spatially dispersed UAV groups and then combines group submodels at swarm level, while intragroup backup keeps training data available after UAV destruction.

[[huang-2026-aircomp-uav-swarms-afl]] focuses on asynchronous FL rather than split/submodel partitioning. It uses communication UAVs as AirComp aggregators for sensing-UAV updates and applies layer-wise cosine-similarity filtering to reduce stale-model damage during UAV-swarm learning.

[[chen-2026-sdhfl-completion-time]] adds [[semi-decentralized-hybrid-federated-learning]]: devices reach D2D model consensus inside geographic clusters, while a UAV asynchronously aggregates selected cluster models and jointly controls mobility and communication resources for completion time.

[[fu-2026-uav-fl-user-grouping]] groups interfering clients with DBSCAN, links participation/data volume to an expected-global-loss bound, and jointly controls UAV trajectory, hover time, UE power, and local data for energy-efficient synchronous aggregation.
