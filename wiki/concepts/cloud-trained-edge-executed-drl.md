---
type: concept
title: "Cloud-Trained, Edge-Executed DRL"
tags: [deep-reinforcement-learning, cloud-edge, online-control, model-refresh]
related:
  - "[[alsenwi-2026-ris-uav-energy-efficiency]]"
  - "[[uav-mounted-ris]]"
  - "[[digital-twin-assisted-online-drl-policy-refresh]]"
created: 2026-07-14
updated: 2026-07-14
---

# Cloud-Trained, Edge-Executed DRL

Cloud-trained, edge-executed DRL separates expensive policy training from latency-sensitive control. A central server trains or refreshes the model from accumulated transitions, while an edge node runs the deployed policy for online decisions and returns new observations and rewards for later updates.

In [[alsenwi-2026-ris-uav-energy-efficiency]], the cloud trains an actor-critic policy and the BS-side edge server selects UAV position, RIS coefficients, and BS precoding online. Periodic feedback supports retraining, but the paper does not quantify cloud-edge latency, communication overhead, or policy-refresh stability. The pattern is therefore an execution architecture rather than evidence that the learned controller itself is distributed.
