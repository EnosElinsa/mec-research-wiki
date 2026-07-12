---
type: concept
title: "Hierarchical Graph Anti-Jamming Control"
tags: [anti-jamming, graph-attention-network, beamforming, uav-deployment, adversarial-learning]
related:
  - "[[tang-2026-gat-antijamming]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[graph-neural-network]]"
  - "[[maddpg]]"
created: 2026-07-13
updated: 2026-07-13
---

# Hierarchical Graph Anti-Jamming Control

A hierarchical learning pattern that delegates interference-aware beamforming to a graph model and spatial/adversarial adaptation to reinforcement learning. In [[tang-2026-gat-antijamming]], a frozen GAT maps desired, interfering, and jammer channels to beamformers inside each outer transition, while two-agent MADDPG controls UAV displacement and jammer power. The paper does not define separate update periods, so this is a two-layer decomposition rather than a documented two-timescale controller.

The hierarchy reduces the outer policy's action dimension, but its equilibrium quality inherits approximation from both layers. Converged rewards and deployment trajectories do not by themselves prove a zero-sum saddle point.
