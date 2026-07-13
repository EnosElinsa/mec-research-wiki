---
type: concept
title: "Robust UAV Position and Power Optimization"
tags: [uav-relay, robust-optimization, chance-constraint, power-allocation, deployment]
related:
  - "[[li-2026-full-duplex-noma-uav-relay]]"
  - "[[full-duplex-noma-uav-relay]]"
  - "[[bernstein-safe-approximation]]"
  - "[[chance-constraint]]"
created: 2026-07-14
updated: 2026-07-14
---

# Robust UAV Position and Power Optimization

Robust UAV position and power optimization jointly chooses an expected 3-D relay location and user-specific relay powers while treating the realized UAV position as random. Reliability constraints require user rates and relay-link ordering to hold with prescribed probabilities.

In [[li-2026-full-duplex-noma-uav-relay]], a [[bernstein-safe-approximation]] converts Gaussian-error chance constraints into deterministic sufficient conditions. Block-coordinate descent alternates SCA position and power subproblems. The monotone objective sequence supports convergence of the iterative approximation, not global optimality of the original nonconvex design.
