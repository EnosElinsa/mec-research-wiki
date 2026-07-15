---
type: concept
title: "Federated KL-Divergence Norm"
tags: [federated-learning, kl-divergence, model-divergence, critical-learning-period]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[critical-learning-period]]"
  - "[[federated-learning]]"
  - "[[federated-drift-norm]]"
created: 2026-07-14
updated: 2026-07-14
---

# Federated KL-Divergence Norm

A federated model-divergence statistic that compares participating local model distributions with the current global model distribution. Under a mean-field Gaussian approximation, the statistic aggregates parameter-wise Gaussian KL divergences from selected devices to the global model and can expose rounds in which local and global learning states separate sharply.

[[li-2026-clp-uav-hpfl]] marks a [[critical-learning-period]] when the statistic's relative round-to-round increase reaches a threshold. The detector is used to prioritize device participation during high-divergence periods rather than to replace the federated optimization objective.

This norm inherits the assumptions of the distributional approximation. The source treats neural-network parameters as independent Gaussians, and its equation is an unweighted sum even though the surrounding prose calls it a weighted average; the unweighted equation is the grounded definition available in the local paper.

[[aerial-federated-aggregation-design-space]] contrasts this parameter-distribution detector with the gradient moments and same-round cross-device correlation used by [[zhong-2026-hierarchical-ota-fl]] to design an analog estimator.
