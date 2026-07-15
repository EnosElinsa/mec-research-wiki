---
type: concept
title: "Simultaneous-Interference UAV Federated Learning"
tags: [federated-learning, uav, interference, energy-efficiency, resource-allocation]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[dang-2026-uav-fl-energy]]"
  - "[[federated-learning]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Simultaneous-Interference UAV Federated Learning

A UAV-FL design in which participating users upload local models at the same time and frequency and their rates retain inter-user interference. In [[dang-2026-uav-fl-energy]], this access model is coupled with local CPU frequency and accuracy, user power, mixed LoS/NLoS [[air-to-ground-channel-model|A2G channels]], and rotary-wing 3-D placement and flight energy. Alternating inner approximations minimize user computation-plus-communication energy under training-deadline and safe-return constraints.

[[aerial-federated-aggregation-design-space]] uses [[zhong-2026-hierarchical-ota-fl]] and [[hierarchical-over-the-air-federated-learning]] as the direct physical-layer contrast: their receiver wants a superposed gradient sum, while this design treats simultaneous signals as interference in separately decoded rates. [[li-2026-clp-uav-hpfl]] supplies the orthogonal-access contrast through OFDMA and learning-state-driven scheduling.
