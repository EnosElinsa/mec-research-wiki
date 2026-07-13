---
type: concept
title: "Hierarchical Over-the-Air Federated Learning"
tags: [federated-learning, aircomp, hierarchical-aggregation, uav]
related:
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[gradient-correlation-aware-aggregation-mse]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
created: 2026-07-14
updated: 2026-07-14
---

# Hierarchical Over-the-Air Federated Learning

A mobile parameter server collects simultaneous analog model updates in partial aggregates at several positions, then aligns and combines those aggregates before a global model update. The hierarchy trades more frequent learning updates against wireless aggregation error, flight time, and computation.

[[zhong-2026-hierarchical-ota-fl]] jointly controls UAV trajectory, device selection, receiver scaling, and global aggregation frequency using a [[gradient-correlation-aware-aggregation-mse]]. It differs from [[huang-2026-aircomp-uav-swarms-afl]], which uses asynchronous swarm aggregation and layer-wise staleness filtering rather than trajectory-segmented partial aggregation.
