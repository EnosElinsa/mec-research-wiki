---
type: concept
title: "Historical-Echo Predictive Beamforming"
tags: [isac, uav, predictive-beamforming, deep-learning, temporal-attention]
related:
  - "[[xu-2026-hecta-predictive-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[csi-estimation-error]]"
  - "[[mmwave-radar-sensing]]"
  - "[[cellular-connected-uav]]"
  - "[[jiang-2026-sensing-assisted-uav-tracking]]"
created: 2026-07-12
updated: 2026-07-13
---

# Historical-Echo Predictive Beamforming

Historical-echo predictive beamforming learns a future communication beam directly from radar-like echoes of earlier communication signals. It bypasses a separate CSI-estimation or kinematic-tracking stage, letting the model absorb spatial array structure, temporal motion, and sensing noise jointly.

[[xu-2026-hecta-predictive-beamforming]] predicts both the BS transmit vector and UAV receive vector. HECTA-Net combines CNN spatial features, dilated causal TCN history, and multi-head time attention, then normalizes complex outputs to the beamforming constraints. UAV attitude matters because array rotation changes the receive direction even when position prediction is accurate.

This is communication-centric [[integrated-sensing-and-communication|ISAC]]: sensing echoes are used to maintain the link, not to optimize a separate sensing target. It complements [[control-assisted-uav-beam-tracking]], which predicts beam direction from flight-control state rather than echo history.
