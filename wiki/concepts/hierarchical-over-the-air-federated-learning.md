---
type: concept
title: "Hierarchical Over-the-Air Federated Learning"
tags: [federated-learning, aircomp, hierarchical-aggregation, uav]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[gradient-correlation-aware-aggregation-mse]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[dang-2026-uav-fl-energy]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[simultaneous-interference-uav-federated-learning]]"
  - "[[critical-learning-period]]"
  - "[[tree-structured-weight-synthesis]]"
created: 2026-07-14
updated: 2026-07-14
---

# Hierarchical Over-the-Air Federated Learning

A mobile parameter server collects simultaneous analog gradient updates in partial aggregates at several positions, then aligns and combines those aggregates before a global model update. The hierarchy trades more frequent learning updates against wireless aggregation error, flight time, and computation.

[[zhong-2026-hierarchical-ota-fl]] jointly controls UAV trajectory, device selection, and receiver scaling using a [[gradient-correlation-aware-aggregation-mse]]. Its global aggregation frequency is a separate tunable design setting evaluated across fixed and dynamic schedules, not an AO variable. The scheme differs from [[huang-2026-aircomp-uav-swarms-afl]], which uses asynchronous swarm aggregation and layer-wise staleness filtering rather than trajectory-segmented partial aggregation.

The comparison in [[aerial-federated-aggregation-design-space]] keeps three other hierarchies separate. [[li-2026-clp-uav-hpfl]] uses digital device-UAV-server averaging and learning-state-triggered periods; [[simultaneous-interference-uav-federated-learning]] and [[dang-2026-uav-fl-energy]] preserve simultaneous uploads as interference rather than an in-channel sum; and [[tree-structured-weight-synthesis]] periodically averages complete classifier coefficients at a ground authority rather than aligning noisy gradient aggregates.
