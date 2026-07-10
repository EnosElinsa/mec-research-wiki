---
type: concept
title: "FedX Training Acceleration"
tags: [drl, federated-learning, training-acceleration, uav-trajectory-control]
related:
  - "[[huang-2025-fedx-ris-uav-trajectory]]"
  - "[[federated-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[ppo]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-10
updated: 2026-07-10
---

# FedX Training Acceleration

FedX training acceleration is a thread-level federating pattern for RL training. Instead of treating clients as independent devices with private environments, [[huang-2025-fedx-ris-uav-trajectory]] treats parallel worker threads as agents that collect experience, train local models, and aggregate parameters under centralized control.

The paper instantiates FedX as FedSAC and FedPPO for RIS-assisted [[uav-trajectory-control]]. The reusable idea is not privacy-preserving FL itself, but faster RL training for time-sensitive wireless control while preserving the solution quality of the underlying [[soft-actor-critic]] or [[ppo]] solver.
