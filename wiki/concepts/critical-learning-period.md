---
type: concept
title: "Critical Learning Period"
tags: [federated-learning, learning-dynamics, data-drift, adaptive-scheduling]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[dang-2026-uav-fl-energy]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[gradient-correlation-aware-aggregation-mse]]"
  - "[[multidimensional-contract-matching]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[federated-learning]]"
  - "[[federated-kl-divergence-norm]]"
  - "[[federated-drift-norm]]"
created: 2026-07-14
updated: 2026-07-14
---

# Critical Learning Period

A training interval in which model divergence or data drift rises enough that additional participation, aggregation, or communication is expected to have unusually high learning value. A critical learning period is detected from evolving training statistics rather than assigned to a universal fixed epoch range.

[[li-2026-clp-uav-hpfl]] detects these intervals from relative increases in either [[federated-kl-divergence-norm]] or [[federated-drift-norm]]. It then adapts device participation, UAV revisit frequency, and aggregation timing: high-divergence devices and high-drift clusters receive more attention, while communication and visits can be reduced outside detected periods.

The detector threshold controls a practical tradeoff. In the source, thresholds that are too small over-detect critical periods and add communication or training, while thresholds that are too large miss useful updates and reduce accuracy. The reported behavior is simulation-based and depends on Gaussian parameter and bounded-drift assumptions.

[[aerial-federated-aggregation-design-space]] separates CLP-triggered cadence from three adjacent controls. [[zhong-2026-hierarchical-ota-fl]] and [[hierarchical-over-the-air-federated-learning]] expose a tunable update frequency but do not detect CLPs; [[gradient-correlation-aware-aggregation-mse]] optimizes a communication-error surrogate rather than a detector threshold; and [[dang-2026-uav-fl-energy]] uses offline physical constraints rather than evolving learning state. [[multidimensional-contract-matching]] is an earlier-stage eligibility mechanism based on private service costs, so its incentive and stability guarantees do not transfer to learning performance.
