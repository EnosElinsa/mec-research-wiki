---
type: concept
title: "Freshness-Aware Covert UAV Communication"
tags: [age-of-information, covert-communication, physical-layer-security, noma, uav-trajectory-control]
related:
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[age-of-information]]"
  - "[[covert-communication]]"
  - "[[noma]]"
  - "[[uav-trajectory-control]]"
  - "[[physical-layer-security]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-10
updated: 2026-07-10
---

# Freshness-Aware Covert UAV Communication

Freshness-aware covert UAV communication couples low-probability-of-detection transmission with Age of Information. The transmitter has to deliver updates while keeping a warden or aerial eavesdropper uncertain about whether a covert transmission occurred, so the trajectory and beamforming choices affect both detection risk and update staleness.

In [[hosseini-2026-aoi-covert-uav]], a multi-antenna UAV serves a covert user and a public user with PD-NOMA. The public signal acts as cover traffic, while the optimizer jointly chooses UAV trajectory, beamforming, and AoI-related decisions using LP, SCA, and SDR subproblems. This concept links [[covert-communication]] to [[age-of-information]] and [[noma]] instead of treating covert throughput as the only metric.
