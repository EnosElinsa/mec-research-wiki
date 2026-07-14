---
type: concept
title: "Cell-Free UAV Predictive Beamforming"
tags: [cell-free-massive-mimo, uav-tracking, predictive-beamforming, channel-prediction]
related:
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[covariance-intersection-state-fusion]]"
  - "[[pcrb-guided-pilot-length-optimization]]"
  - "[[beam-delay-alignment-transmission]]"
  - "[[six-dimensional-aerial-rotatable-antenna-array]]"
  - "[[team-mmse-receive-combining]]"
  - "[[statistical-user-position-uav-deployment]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
created: 2026-07-14
updated: 2026-07-14
---

# Cell-Free UAV Predictive Beamforming

A ground-AP architecture that predicts mobile UAV channels from distributed kinematic estimates instead of retraining full CSI every slot. [[fang-2026-cellfree-uav-predictive-beamforming]] uses first-slot pilots, AP-local EKFs, CPU covariance fusion, LoS channel reconstruction, and zero-forcing beams across the remaining frame.
