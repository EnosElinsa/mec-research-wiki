---
type: concept
title: "Unpredictable UAV Trajectory Control"
tags: [uav, trajectory-control, anti-jamming, stochastic-control]
related:
  - "[[hua-2026-unpredictable-uav-trajectory]]"
  - "[[uav-trajectory-control]]"
  - "[[navigation-stochastic-control-decomposition]]"
  - "[[anti-jamming-mec]]"
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[yin-2026-uav-antijamming-nfsp]]"
  - "[[implicit-opponent-modeling]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
created: 2026-07-14
updated: 2026-07-14
---

# Unpredictable UAV Trajectory Control

Trajectory control that deliberately injects stochastic motion so an observer has greater difficulty predicting the UAV's next state, while mission guidance still drives it toward data-collection and terminal goals.

[[hua-2026-unpredictable-uav-trajectory]] evaluates unpredictability through one-step Kalman position-prediction error and balances it against jamming and control surrogates. Higher simulated prediction error is not a formal security guarantee against adaptive, nonlinear, or method-aware attackers.
