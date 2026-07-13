---
type: concept
title: "NOMA Amplify-and-Forward UAV Relaying"
tags: [noma, uav-relay, amplify-and-forward, beamforming, trajectory-optimization]
related:
  - "[[li-2026-noma-uav-relay-planning]]"
  - "[[imperfect-sic-residual-interference]]"
  - "[[noma]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-13
updated: 2026-07-13
---

# NOMA Amplify-and-Forward UAV Relaying

NOMA amplify-and-forward UAV relaying uses a mobile aerial relay to amplify a received multiuser signal and forward it to power-domain NOMA users. The end-to-end rate depends on both hops, relay noise amplification, beamforming, NOMA power coefficients, SIC quality, relay gain, and the UAV's changing geometry.

[[li-2026-noma-uav-relay-planning]] studies the case with no direct base-station-to-user link. It jointly optimizes multi-antenna beamforming, power control, relay amplification, and trajectory to maximize the minimum accumulated user rate, with [[imperfect-sic-residual-interference]] included in the user SINR model.

This concept specializes [[uav-mobile-relaying]] and [[noma]]. Unlike buffered decode-and-forward formulations with information-causality constraints, AF immediately forwards a scaled noisy signal. The cited source solves the resulting coupling through [[alternating-optimization-sdr-sca]], so its result is a locally constructed feasible design rather than a global optimum guarantee.
