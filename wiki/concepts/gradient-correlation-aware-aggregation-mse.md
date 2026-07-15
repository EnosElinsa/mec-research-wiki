---
type: concept
title: "Gradient-Correlation-Aware Aggregation MSE"
tags: [federated-learning, aircomp, aggregation-error, learning-theory]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[dang-2026-uav-fl-energy]]"
  - "[[critical-learning-period]]"
created: 2026-07-14
updated: 2026-07-14
---

# Gradient-Correlation-Aware Aggregation MSE

An [[over-the-air-computation|AirComp]] aggregation-error model that retains cross-device gradient correlation instead of treating local updates as independent. It separates receiver noise, device-selection bias, and correlation-weighted channel mismatch, connecting radio decisions to a bound on federated-learning stationarity.

The result in [[zhong-2026-hierarchical-ota-fl]] is conditional on smoothness, Lipschitz-gradient, and normalized-gradient distribution assumptions. It bounds a gradient-norm stationarity measure rather than proving global minimization of the learning loss.

[[aerial-federated-aggregation-design-space]] contrasts this continuous, theorem-linked communication-error objective with two different controls. [[dang-2026-uav-fl-energy]] minimizes UE computation and communication energy under deadlines and inter-user interference, while [[critical-learning-period]] thresholds evolving learning statistics to change participation and cadence. Energy, MSE, detector thresholds, and accuracy are not numerically comparable.
