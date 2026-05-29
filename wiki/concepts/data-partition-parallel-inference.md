---
type: concept
title: "Data-Partition Parallel Inference"
tags: [distributed-inference, data-parallel, edge-ai]
related:
  - "[[collaborative-dl-inference]]"
  - "[[dnn-model-partition]]"
  - "[[load-balancing-uav-mec]]"
  - "[[sun-2024-asap-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Data-Partition Parallel Inference

Splitting a layer's **input feature map** into segments computed in parallel across multiple nodes, then concatenating the partial results. Because convolution/pooling operators have receptive fields, each segment needs a slightly expanded input range (overlap/halo) and careful padding to preserve boundary correctness.

In the wiki, [[sun-2024-asap-uav-swarm]] applies this *within* a cluster (its ICLB algorithm sizes each member's partition so predicted latencies align), using a "Mapping Range Transforming" step to back-deduce the minimal input range and an online padding strategy for boundaries. It is the intra-cluster complement to [[dnn-model-partition]] (inter-cluster) in ASAP's two-level [[collaborative-dl-inference]], and a fine-grained form of [[load-balancing-uav-mec]].
