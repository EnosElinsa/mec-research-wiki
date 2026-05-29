---
type: concept
title: "DNN Model Partition (Split Computing)"
tags: [distributed-inference, model-partition, edge-ai]
related:
  - "[[collaborative-dl-inference]]"
  - "[[data-partition-parallel-inference]]"
  - "[[pipeline-parallel-inference]]"
  - "[[sun-2024-asap-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# DNN Model Partition (Split Computing)

Splitting a deep neural network into sequential **submodels** assigned to different compute nodes, so the activations flow node-to-node down the layer stack (the "split computing" idea, à la Neurosurgeon). The cut point(s) trade communication (sending intermediate feature maps) against per-node compute and memory.

In the wiki, [[sun-2024-asap-uav-swarm]] partitions the model **across UAV clusters** (its ECLB algorithm picks per-cluster cut points to equalize predicted per-cluster latency), then runs the cluster submodels via [[pipeline-parallel-inference]]. It is one half of ASAP's two-level split — complemented by [[data-partition-parallel-inference]] *within* each cluster — and a building block of [[collaborative-dl-inference]].
