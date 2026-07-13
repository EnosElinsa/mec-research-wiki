---
type: concept
title: "Control-Assisted UAV Beam Tracking"
tags: [uav, mmwave, beam-tracking, flight-control, prediction]
related:
  - "[[lyu-2026-situation-aware-uav-isac]]"
  - "[[zhang-2026-control-assisted-beam-tracking]]"
  - "[[cellular-connected-uav]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[xu-2026-hecta-predictive-beamforming]]"
  - "[[historical-echo-predictive-beamforming]]"
  - "[[jiang-2026-sensing-assisted-uav-tracking]]"
created: 2026-07-12
updated: 2026-07-14
---

# Control-Assisted UAV Beam Tracking

[[lyu-2026-situation-aware-uav-isac]] selects antenna-angle correction for moderate horn-beam misalignment and adds propulsion-expensive UAV position correction only when overlap is lost or displacement is severe. The source couples this mode switch to periodic/event-triggered sensing rather than learning a free trajectory.

Control-assisted UAV beam tracking reuses flight-controller state such as position error, velocity, attitude, and waypoints to predict physical-layer beam direction. It reduces exhaustive sounding by translating control-state regularity into a smaller beam-search interval and an uncertainty estimate.

[[zhang-2026-control-assisted-beam-tracking]] separates attitude-induced and relative-position-induced offsets. A Bayesian DNN predicts the former, while a velocity-based estimator tracks the latter and is periodically corrected by absolute position. The method is specific to the coupling between autonomous mission flight and a narrow BS-UAV mmWave link.

[[xu-2026-hecta-predictive-beamforming]] provides the complementary echo-only design. [[historical-echo-predictive-beamforming]] learns both transmit and receive vectors from prior ISAC echoes and models attitude-driven receive-array rotation without using flight-controller telemetry as network input.
