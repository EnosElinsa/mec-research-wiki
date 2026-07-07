---
type: concept
title: "Two-Tier Submodel Partition"
tags: [uav-swarm, federated-learning, model-partitioning, robustness]
related:
  - "[[li-2026-tspf-forest-fire-uav-swarm]]"
  - "[[uav-forest-fire-detection]]"
  - "[[federated-learning]]"
  - "[[split-federated-learning]]"
  - "[[task-redundancy-for-reliability]]"
created: 2026-07-07
updated: 2026-07-07
---

# Two-Tier Submodel Partition

Two-tier submodel partition (TSPF) is a UAV-swarm training pattern where a DNN is partitioned into submodels, selected layers are aggregated inside spatially dispersed UAV groups, and a swarm-level server then combines group submodels into a global model. In [[li-2026-tspf-forest-fire-uav-swarm]], the partition is paired with balanced graph coloring, intragroup data backup, and Dynamic Server Selection so forest-fire detection can continue after some UAVs are destroyed.

It is related to [[federated-learning]] and [[split-federated-learning]], but its distinctive contribution in the corpus is robustness: partitioning reduces full-model communication, while same-group backup preserves data that standard FL would lose after node destruction.
