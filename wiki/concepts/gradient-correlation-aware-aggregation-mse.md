---
type: concept
title: "Gradient-Correlation-Aware Aggregation MSE"
tags: [federated-learning, aircomp, aggregation-error, learning-theory]
related:
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
created: 2026-07-14
updated: 2026-07-14
---

# Gradient-Correlation-Aware Aggregation MSE

An [[over-the-air-computation|AirComp]] aggregation-error model that retains cross-device gradient correlation instead of treating local updates as independent. It separates receiver noise, device-selection bias, and correlation-weighted channel mismatch, connecting radio decisions to a bound on federated-learning stationarity.

The result in [[zhong-2026-hierarchical-ota-fl]] is conditional on smoothness, Lipschitz-gradient, and normalized-gradient distribution assumptions. It bounds a gradient-norm stationarity measure rather than proving global minimization of the learning loss.
