---
type: concept
title: "Integrated Periodic Sensing and Communication"
tags: [integrated-sensing-and-communication, periodic-sensing, scheduling, uav]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[adaptive-td-isac-sensing-period]]"
  - "[[uav-trajectory-control]]"
  - "[[meng-2023-uav-ipsac-throughput]]"
  - "[[meng-2026-uav-isac-corrections]]"
created: 2026-07-14
updated: 2026-07-14
---

# Integrated Periodic Sensing and Communication

An ISAC schedule where communication runs throughout a mission while each target is sensed at a prescribed frequency, rather than forcing sensing into every communication slot. A frame defines the sensing period; target-slot selection, communication scheduling, beamforming, and platform motion determine how the sensing requirement trades against rate.

In [[meng-2023-uav-ipsac-throughput]], every target is selected exactly once per frame and at most one target is sensed per slot. Longer frames reduce sensing frequency and enlarge the communication design space. [[meng-2026-uav-isac-corrections]] repairs two convexification steps in that paper's solver.

This differs from [[adaptive-td-isac-sensing-period]], which optimizes the sensing interval itself. Here the frame length is a requirement or sweep parameter, while the algorithm decides where sensing occurs inside each frame.
