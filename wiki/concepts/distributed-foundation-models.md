---
type: concept
title: "Distributed Foundation Models"
tags: [foundation-models, 6g, distributed-training, multi-modal]
related:
  - "[[du-2024-distributed-foundation-models-6g]]"
  - "[[pipeline-parallel-inference]]"
  - "[[data-partition-parallel-inference]]"
  - "[[federated-learning]]"
  - "[[over-the-air-computation]]"
created: 2026-05-29
updated: 2026-05-29
---

# Distributed Foundation Models

The training and serving of large multi-modal foundation models (FMs) across many distributed, heterogeneous devices rather than a single centralized GPU cluster — motivated by FMs' exploding parameter sizes/energy costs and by the dispersal of fresh multi-modal data across wireless devices.

[[du-2024-distributed-foundation-models-6g]] organizes the design space along three axes: **pipeline parallelism** (compress activations/gradients, allocate communication resources), **data parallelism** ([[federated-learning]] + [[over-the-air-computation]] for fast gradient aggregation), and **multi-modal learning** (fuse NLP and CV). The challenges — non-IID heterogeneous data, unstable wireless links, straggler devices — distinguish it from homogeneous GPU-cluster training, and connect it to [[pipeline-parallel-inference]] and [[data-partition-parallel-inference]].
