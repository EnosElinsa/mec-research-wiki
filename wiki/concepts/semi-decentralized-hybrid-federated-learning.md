---
type: concept
title: "Semi-Decentralized Hybrid Federated Learning"
tags: [federated-learning, d2d, uav, asynchronous-aggregation, distributed-training]
related:
  - "[[chen-2026-sdhfl-completion-time]]"
  - "[[federated-learning]]"
  - "[[device-to-device-communication]]"
  - "[[decentralized-federated-learning]]"
  - "[[lyapunov-optimization]]"
created: 2026-07-12
updated: 2026-07-12
---

# Semi-Decentralized Hybrid Federated Learning

Semi-decentralized hybrid federated learning combines local peer-to-peer model consensus with a retained global aggregator. Devices first exchange updates inside geographic D2D clusters; a higher-tier coordinator then aggregates selected cluster models asynchronously, reducing long-range communication without removing global coordination.

In [[chen-2026-sdhfl-completion-time]], a UAV aggregates one cluster per global round while other clusters continue local training. Cluster selection, UAV speed, device computation, power, and subcarriers are jointly controlled for completion time and queue stability. This differs from [[decentralized-federated-learning]], where aggregation is server-free across the full network.
