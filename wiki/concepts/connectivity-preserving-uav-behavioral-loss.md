---
type: concept
title: "Connectivity-Preserving UAV Behavioral Loss"
tags: [marl, uav, connectivity, auxiliary-loss, emergency-network]
related:
  - "[[xu-2026-mrlmn-llm-multihop]]"
  - "[[multi-hop-uav-emergency-networking]]"
  - "[[task-oriented-grouped-uav-marl]]"
  - "[[llm-guided-marl-policy-distillation]]"
  - "[[collaborative-uav-communication]]"
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[distributed-tabular-q-learning-uav-collision-avoidance]]"
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
created: 2026-07-14
updated: 2026-07-14
---

# Connectivity-Preserving UAV Behavioral Loss

A connectivity-preserving UAV behavioral loss adds supervised action pressure after an agent loses every base-station link. It supplements delayed team rewards with an immediate directional signal intended to restore base-station reachability before one disconnection cascades through a multi-hop aerial network.

[[xu-2026-mrlmn-llm-multihop]] applies the loss to critical near-base-station UAVs that lose all base-station links, steering them toward the highest-SNR base station with distance-dependent weight. This is a shaping mechanism rather than a connectivity guarantee: it assumes reliable link-state knowledge and does not account for blockage, delayed information, collisions, energy limits, or infeasible recovery geometry.
