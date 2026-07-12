---
type: concept
title: "Control-Assisted UAV Beam Tracking"
tags: [uav, mmwave, beam-tracking, flight-control, prediction]
related:
  - "[[zhang-2026-control-assisted-beam-tracking]]"
  - "[[cellular-connected-uav]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-12
updated: 2026-07-12
---

# Control-Assisted UAV Beam Tracking

Control-assisted UAV beam tracking reuses flight-controller state such as position error, velocity, attitude, and waypoints to predict physical-layer beam direction. It reduces exhaustive sounding by translating control-state regularity into a smaller beam-search interval and an uncertainty estimate.

[[zhang-2026-control-assisted-beam-tracking]] separates attitude-induced and relative-position-induced offsets. A Bayesian DNN predicts the former, while a velocity-based estimator tracks the latter and is periodically corrected by absolute position. The method is specific to the coupling between autonomous mission flight and a narrow BS-UAV mmWave link.
