---
type: concept
title: "Adaptive Inter-Layer Data Offloading"
tags: [offloading, sagin, federated-learning, load-balancing]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[federated-learning]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[makespan-minimization]]"
  - "[[han-2024-sagin-fl-handover]]"
created: 2026-05-29
updated: 2026-05-29
---

# Adaptive Inter-Layer Data Offloading

Per-round optimization of **how many data samples** are offloaded across the space, air, and ground layers of a SAGIN, adapting to satellites' time-varying compute power and bounded coverage time. Unlike conventional task/computation offloading (move a task to a server), here it is **training data** that moves between tiers to balance per-round federated-learning latency.

In the wiki, [[han-2024-sagin-fl-handover]] formulates two directional regimes — offload space→air/ground when satellites are resource-poor, air/ground→space when they are resource-rich — capped by each device's [[privacy-sensitive-data-partitioning|non-sensitive data fraction]], and solves the resulting [[makespan-minimization]]-style latency problem with hierarchical nested bisection search. It is the data-movement analogue of the corpus's [[task-offloading]] and a [[load-balancing-uav-mec]]-style idea applied to FL across SAGIN tiers.
