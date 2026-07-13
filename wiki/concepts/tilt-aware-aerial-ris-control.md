---
type: concept
title: "Tilt-Aware Aerial RIS Control"
tags: [uav-mounted-ris, intelligent-reflecting-surface, uav-trajectory-control, beamforming]
related:
  - "[[liu-2026-passive-6dma]]"
  - "[[angle-dependent-irs-effective-aperture]]"
  - "[[li-2026-aerial-ris-trajectory-phase]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-trajectory-control]]"
  - "[[soft-actor-critic]]"
  - "[[prioritized-experience-replay]]"
created: 2026-07-10
updated: 2026-07-14
---

# Tilt-Aware Aerial RIS Control

Tilt-aware aerial RIS control treats the orientation of a UAV-mounted RIS as part of the communication-control problem, not just the UAV's position and RIS phase shifts. When a quadrotor accelerates, decelerates, or changes direction, its Euler angles alter the incidence and reflection angles seen by the RIS; the reflected beam can therefore lose gain even if the waypoint and phase-shift plan looks feasible in a position-only model.

In [[li-2026-aerial-ris-trajectory-phase]], the ARIS gain depends on incidence/reflection geometry, and the SAC-PER controller chooses attitude-related actions and sub-surface phase shifts while BS beamforming is handled by ZF plus water-filling. The concept is a RIS-specific extension of [[uav-trajectory-control]]: the flight policy must preserve both mobility feasibility and orientation-dependent reflection quality.
