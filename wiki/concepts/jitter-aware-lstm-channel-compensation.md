---
type: concept
title: "Jitter-Aware LSTM Channel Compensation"
tags: [uav-communications, jitter, lstm, channel-prediction, coordinated-multipoint]
related:
  - "[[jin-2026-jitter-aware-uav-comp]]"
  - "[[jitter-aware-uav-beamwidth-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[csi-estimation-error]]"
created: 2026-07-13
updated: 2026-07-13
---

# Jitter-Aware LSTM Channel Compensation

Jitter-aware LSTM channel compensation predicts future aerial CSI from onboard attitude and recent channel sequences. Pitch and yaw explain antenna displacement from platform motion; real and imaginary channel samples capture the resulting propagation response. The predicted channel then updates precoding before outdated CSI causes coherent-transmission loss.

[[jin-2026-jitter-aware-uav-comp]] implements J-LSTM for distributed UAV-BS CoMP joint transmission. It differs from [[jitter-aware-uav-beamwidth-control]], which chooses directional beamwidth from a disturbance model: J-LSTM predicts next-symbol CSI for precoding. Its reported gains are based on synthetic jitter/channel data, not measured airborne CSI.
