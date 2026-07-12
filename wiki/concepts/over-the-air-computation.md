---
type: concept
title: "Over-the-Air Computation (AirComp)"
tags: [edge-inference, federated-learning, beamforming, signal-processing]
related:
  - "[[fu-2025-otae-inference-lae-batching]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
  - "[[collaborative-dl-inference]]"
  - "[[federated-learning]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[qian-2026-federated-bandit-aircomp]]"
  - "[[federated-linear-bandit-learning]]"
created: 2026-05-29
updated: 2026-07-13
---

# Over-the-Air Computation (AirComp)

A technique that exploits the **superposition property** of the wireless multiple-access channel: many devices transmit simultaneously and the channel naturally sums their signals, so the receiver obtains an aggregate function (e.g. a weighted sum of features or gradients) in one transmission instead of decoding each device separately. This fuses communication and computation, drastically cutting aggregation latency.

In [[fu-2025-otae-inference-lae-batching]], AirComp aggregates multi-sensor features at a 6G base station for low-altitude edge inference, with spatial-correlation-aware beamforming to suppress aggregation error. In [[du-2024-distributed-foundation-models-6g]], FL with AirComp expedites gradient aggregation for distributed foundation-model training. AirComp supports [[collaborative-dl-inference]] and [[federated-learning]].

[[huang-2026-aircomp-uav-swarms-afl]] makes AirComp the uplink aggregation primitive for [[aircomp-assisted-asynchronous-fl]] in UAV swarms: selected communication UAVs aggregate sensing-UAV model updates while beamforming and participant scheduling manage aggregation error and model staleness.

[[qian-2026-federated-bandit-aircomp]] aggregates Gram matrices and reward vectors for [[federated-linear-bandit-learning]] rather than gradients. Event-triggered clients transmit simultaneously to a mobile UAV server, while BCD-ADMM trajectory/power control reduces aggregation MSE and the resulting channel perturbation appears in the regret analysis.
