---
type: concept
title: "AoI-Aware UAV Altitude and Scheduling Control"
tags: [age-of-information, altitude-control, scheduling, uav-relay, iot]
related:
  - "[[samir-2022-aoi-altitude-scheduling]]"
  - "[[age-of-information]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
  - "[[ppo]]"
  - "[[hybrid-action-decision-making]]"
created: 2026-07-13
updated: 2026-07-13
---

# AoI-Aware UAV Altitude and Scheduling Control

AoI-aware UAV altitude and scheduling control couples vertical relay placement to status-update service. Altitude changes distance and LoS probability on both IoT-to-UAV and UAV-to-base-station links; scheduling decides whether the relay receives a fresher packet or forwards a queued packet, directly changing destination [[age-of-information|AoI]].

[[samir-2022-aoi-altitude-scheduling]] keeps only the newest packet per stream and uses PPO over a discretized action set. A slot performs one transmission or one altitude action, so the learned policy trades channel improvement against immediate update service.
