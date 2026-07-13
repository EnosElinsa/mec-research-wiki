---
type: concept
title: "Two-Layer Successive Programming"
tags: [optimization, sequential-quadratic-programming, bayesian-optimization]
related:
  - "[[lv-2026-isac-sar-tlsp]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# Two-Layer Successive Programming

A decomposition that assigns relatively smooth, constrained variables to an inner gradient-based solver and leaves highly nonconvex geometry variables to an outer stochastic surrogate optimizer.

In [[lv-2026-isac-sar-tlsp]], segmentwise SQP optimizes communication trajectory, speed, power, and duration at fixed sensing legs, while constrained Gaussian-process Bayesian optimization updates SAR sensing endpoints and velocities. Multi-start and selected non-improving samples improve exploration but do not establish global optimality.
