---
type: concept
title: "Split Federated Learning (SFL)"
tags: [federated-learning, split-learning, distributed-ml, foundation-models, edge-ai]
related:
  - "[[federated-learning]]"
  - "[[distributed-foundation-models]]"
  - "[[dnn-model-partition]]"
  - "[[pipeline-parallel-inference]]"
  - "[[zhou-2026-cpsfl-uav-foundation-models]]"
created: 2026-07-06
updated: 2026-07-06
---

# Split Federated Learning (SFL)

A distributed-training pattern that combines [[federated-learning]] with model partitioning. Each client keeps raw data local and runs the client-side part of the model, while a server runs the server-side part; federated aggregation updates the distributed model without centralizing the raw data. The split lowers client compute and memory load, but introduces smashed-data upload, gradient download, split-point selection, and straggler-management problems.

In the wiki, [[zhou-2026-cpsfl-uav-foundation-models]] applies SFL to LoRA fine-tuning of foundation models in UAV networks. Its CPSFL design treats downlink gradient transmission as the bottleneck and pipelines it through priority scheduling and intra-round asynchronous training, linking SFL to [[distributed-foundation-models]], [[dnn-model-partition]], and wireless resource allocation.
