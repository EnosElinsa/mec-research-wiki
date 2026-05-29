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
created: 2026-05-29
updated: 2026-05-29
---

# Federated Learning (FL)

A distributed machine-learning paradigm where many clients train a shared model on their **local** data and send only model updates (not raw data) to an aggregator, which combines them — classically by **FedAvg** (data-size-weighted averaging) — into a global model. It preserves privacy and cuts data movement, but suffers from data heterogeneity (non-IID clients), stragglers, and communication bottlenecks.

This is the base concept underlying the wiki's prior, narrower [[federated-reinforcement-learning]] and [[blockchain-for-fl-aggregation]] pages. In the wiki, [[han-2024-sagin-fl-handover]] orchestrates FL across a SAGIN — satellites and UAVs act as both aggregators and compute units — adding [[adaptive-inter-layer-data-offloading]], satellite [[seamless-handover]], and a [[privacy-sensitive-data-partitioning]] constraint, with a proven convergence guarantee for non-convex losses. Complements [[mao-2025-bcsa-frl]]'s federated-RL-over-satellites approach.
