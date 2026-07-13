---
type: concept
title: "Sensing-Assisted Predictive Beamforming"
tags: [isac, predictive-beamforming, tracking, outage]
related:
  - "[[yin-2026-m2llm-trajectory-beamforming]]"
  - "[[prediction-driven-joint-trajectory-beamforming]]"
  - "[[jiang-2026-sensing-assisted-uav-tracking]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[historical-echo-predictive-beamforming]]"
  - "[[cellular-connected-uav]]"
created: 2026-07-13
updated: 2026-07-14
---

# Sensing-Assisted Predictive Beamforming

Sensing-assisted predictive beamforming predicts a mobile user's direction from a motion model, prior state estimate, and control input, then uses communication-signal echoes to refine that prediction before allocating the remaining slot to data transmission. It couples sensing duration, tracking uncertainty, beam alignment, and communication reliability.

[[jiang-2026-sensing-assisted-uav-tracking]] sends one beam toward an EKF-predicted UAV state, updates that state from angle/range echoes, and sends a second beam toward the estimate. Its outage-capacity formulation differs from [[historical-echo-predictive-beamforming]], which learns beams directly from echo histories, and [[control-assisted-uav-beam-tracking]], which uses flight-control telemetry.
