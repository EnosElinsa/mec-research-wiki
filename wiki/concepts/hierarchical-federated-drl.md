---
type: concept
title: "Hierarchical Federated DRL"
tags: [drl, federated-learning, multi-agent-learning, non-terrestrial-network]
related:
  - "[[seid-2026-mafdrl-tn-ntn-incentive]]"
  - "[[federated-reinforcement-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[maddpg]]"
  - "[[ddpg]]"
created: 2026-07-10
updated: 2026-07-10
---

# Hierarchical Federated DRL

Hierarchical federated DRL combines multi-agent DRL with multi-tier model aggregation. In [[seid-2026-mafdrl-tn-ntn-incentive]], ED, UAV/UCH, and HAP agents make local resource and offloading decisions, while model parameters are aggregated upward through the terrestrial/non-terrestrial hierarchy.

The concept is a specialized form of [[federated-reinforcement-learning]] for [[space-air-ground-integrated-network]] and [[hierarchical-aerial-mec]] settings. Its distinctive feature is that the hierarchy is both a network architecture and a learning architecture: [[maddpg]] handles lower-layer multi-agent control under [[centralized-training-decentralized-execution]], while a [[ddpg]] auctioneer controls the incentive layer.
