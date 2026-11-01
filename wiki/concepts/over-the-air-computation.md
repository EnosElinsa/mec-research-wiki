---
type: concept
title: "Over-the-Air Computation (AirComp)"
tags: [edge-inference, federated-learning, beamforming, signal-processing]
related:
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[gradient-correlation-aware-aggregation-mse]]"
  - "[[fu-2025-otae-inference-lae-batching]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
  - "[[collaborative-dl-inference]]"
  - "[[federated-learning]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[qian-2026-federated-bandit-aircomp]]"
  - "[[federated-linear-bandit-learning]]"
  - "[[wen-2025-iscc-air-feel]]"
  - "[[gong-2025-secure-uav-aircomp]]"
  - "[[yao-not-in-parse-hierarchical-airfl-power]]"
created: 2026-05-29
updated: 2026-11-02
---

# Over-the-Air Computation (AirComp)

A technique that exploits the **superposition property** of the wireless multiple-access channel: many devices transmit simultaneously and the channel naturally sums their signals, so the receiver obtains an aggregate function (e.g. a weighted sum of features or gradients) in one transmission instead of decoding each device separately. This fuses communication and computation, drastically cutting aggregation latency.

In [[fu-2025-otae-inference-lae-batching]], AirComp aggregates multi-sensor features at a 6G base station for low-altitude edge inference, with spatial-correlation-aware beamforming to suppress aggregation error. In [[du-2024-distributed-foundation-models-6g]], FL with AirComp expedites gradient aggregation for distributed foundation-model training. AirComp supports [[collaborative-dl-inference]] and [[federated-learning]].

[[huang-2026-aircomp-uav-swarms-afl]] makes AirComp the uplink aggregation primitive for [[aircomp-assisted-asynchronous-fl]] in UAV swarms: selected communication UAVs aggregate sensing-UAV model updates while beamforming and participant scheduling manage aggregation error and model staleness.

[[qian-2026-federated-bandit-aircomp]] aggregates Gram matrices and reward vectors for [[federated-linear-bandit-learning]] rather than gradients. Event-triggered clients transmit simultaneously to a mobile UAV server, while BCD-ADMM trajectory/power control reduces aggregation MSE and the resulting channel perturbation appears in the regret analysis.


Further AirComp designs: [[wen-2025-iscc-air-feel]] couples device sensing, batch size, and AirComp distortion in federated edge learning; [[gong-2025-secure-uav-aircomp]] moves a UAV fusion center and shapes transmit scalers to keep an eavesdropper's MSE high; and [[yao-not-in-parse-hierarchical-airfl-power]] controls device and base-station amplify-and-forward power under inter-cluster interference.
