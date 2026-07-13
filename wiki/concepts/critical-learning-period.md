---
type: concept
title: "Critical Learning Period"
tags: [federated-learning, learning-dynamics, data-drift, adaptive-scheduling]
related:
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
