---
type: concept
title: "CSI-Free Multi-Antenna Wireless Energy Transfer"
tags: [wireless-power-transfer, multi-antenna, csi-free, energy-beamforming]
related:
  - "[[lin-2026-uav-wpucn-time-allocation]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
created: 2026-07-14
updated: 2026-07-14
---

# CSI-Free Multi-Antenna Wireless Energy Transfer

Multi-antenna RF power delivery that avoids estimating instantaneous receiver channels. Instead of adapting a coherent beam to each device, the transmitter can switch antennas, radiate independent signals, reuse one signal across an array, or mechanically sweep an array pattern.

In [[lin-2026-uav-wpucn-time-allocation]], these schemes are practical alternatives to an ideal full-CSI max-min energy-beamforming benchmark for buried devices. They remove CSI acquisition and feedback from the modeled WET phase, but their performance still depends on array hardware power, antenna geometry, propagation statistics, and the chosen sweeping or signal architecture.
