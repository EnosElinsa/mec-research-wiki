---
type: concept
title: "Federated Drift Norm"
tags: [federated-learning, data-drift, gradient-drift, critical-learning-period]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[critical-learning-period]]"
  - "[[federated-learning]]"
  - "[[federated-kl-divergence-norm]]"
created: 2026-07-14
updated: 2026-07-14
---

# Federated Drift Norm

A federated statistic for detecting temporal change in local learning conditions through gradient and loss variation. It summarizes how much the value of revisiting a device cluster has changed, allowing communication and aggregation schedules to react to nonstationary data rather than using uniform revisit intervals.

[[li-2026-clp-uav-hpfl]] bounds temporal gradient variation, approximates one-step loss change with a first-order Taylor argument, and aggregates device loss changes with sample-size weights. A relative increase above a threshold identifies a [[critical-learning-period]]; high-drift clusters are then revisited more often, while low-drift clusters may defer UAV visits.

The statistic is an approximation, not a direct guarantee of future accuracy improvement. Its interpretation depends on bounded, slowly varying gradients and the local first-order loss model, and the source validates the resulting schedule only in simulation.

In [[aerial-federated-aggregation-design-space]], [[zhong-2026-hierarchical-ota-fl]] supplies the complementary statistic: same-round cross-device gradient correlation shapes analog aggregation error, whereas this norm tracks temporal change to schedule later visits. Their magnitudes are not comparable.
