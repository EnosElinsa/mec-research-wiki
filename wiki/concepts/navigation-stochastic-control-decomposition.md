---
type: concept
title: "Navigation-Stochastic Control Decomposition"
tags: [stochastic-control, model-predictive-control, uav, trajectory-planning]
related:
  - "[[hua-2026-unpredictable-uav-trajectory]]"
  - "[[unpredictable-uav-trajectory-control]]"
  - "[[control-parameterized-uav-trajectory]]"
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[convex-tsp-uav-data-collection]]"
  - "[[implicit-opponent-modeling]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
created: 2026-07-14
updated: 2026-07-14
---

# Navigation-Stochastic Control Decomposition

A motion-control pattern that splits the physical input into a mission-directed navigation term and a random term used for unpredictability or exploration. Finite component bounds may be stated to preserve the total actuator limit, and the stochastic component can be disabled near the terminal set to protect arrival.

[[hua-2026-unpredictable-uav-trajectory]] chooses navigation heading rate through finite-horizon discrete MPC enumeration and chooses the Gaussian stochastic input's mean through a parallel modified-gradient procedure. Because a Gaussian has unbounded support, the paper's finite stochastic-control bounds are not guaranteed without an unstated clipping, truncation, or rejection mechanism. The decomposition is a slotwise heuristic rather than a globally optimal stochastic mission controller.
