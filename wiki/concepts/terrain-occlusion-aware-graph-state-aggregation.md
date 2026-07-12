---
type: concept
title: "Terrain-Occlusion-Aware Graph State Aggregation"
tags: [graph-neural-network, contrastive-learning, terrain, uav, state-representation]
related:
  - "[[xie-2026-geoagg-hsac]]"
  - "[[graph-neural-network]]"
  - "[[terrain-aware-channel-model]]"
  - "[[hybrid-action-decision-making]]"
created: 2026-07-13
updated: 2026-07-13
---

# Terrain-Occlusion-Aware Graph State Aggregation

A learned state representation that groups aerial-network states by terrain-induced LoS/NLoS structure rather than only by Euclidean proximity. [[xie-2026-geoagg-hsac]] constructs a UAV-user bipartite graph, applies channel-weighted graph attention and Set2Set pooling, and contrastively pretrains states whose occlusion patterns match.

The encoder supplies a pooled representation to hybrid-action SAC for trajectory, power, and association control, but the policy input also concatenates the complete estimated LoS/NLoS link-state object. Its physical meaning depends on the ray-traced terrain labels and channel measurements used during pretraining, so transfer across unseen terrain is not established by within-map mobility tests.
