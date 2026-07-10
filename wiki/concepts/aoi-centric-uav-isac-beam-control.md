---
type: concept
title: "AoI-Centric UAV-ISAC Beam Control"
tags: [age-of-information, isac, uav-trajectory-control, beamforming, soft-actor-critic]
related:
  - "[[bai-2026-aoi-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[age-of-information]]"
  - "[[soft-actor-critic]]"
  - "[[uav-trajectory-control]]"
  - "[[dynamic-target-prioritization-metric]]"
created: 2026-07-10
updated: 2026-07-10
---

# AoI-Centric UAV-ISAC Beam Control

AoI-centric UAV-ISAC beam control makes delivered sensing-update freshness the main objective of integrated sensing and communication. A UAV must decide where to fly, which users/targets to prioritize, and how to form sensing and communication beams so that users receive timely target-state updates rather than merely high-rate downlink service or accurate sensing in isolation.

In [[bai-2026-aoi-uav-isac]], SAC outputs UAV-motion actions plus beam-priority logits and an activation threshold. Kalman target prediction, regularized zero-forcing precoding, and waveform post-processing convert those policy outputs into physical ISAC beams. The concept extends [[integrated-sensing-and-communication]] toward [[age-of-information]] and is adjacent to [[dynamic-target-prioritization-metric]], which also adds freshness to UAV sensing/target-tracking decisions.
