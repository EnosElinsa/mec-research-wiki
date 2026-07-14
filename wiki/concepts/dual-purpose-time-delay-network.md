---
type: concept
title: "Dual-Purpose True-Time-Delay Network"
tags: [true-time-delay, beam-split, synchronization, hybrid-beamforming]
related:
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[beam-delay-alignment-transmission]]"
  - "[[wideband-asynchronous-cell-free-massive-mimo]]"
created: 2026-07-14
updated: 2026-07-14
---

# Dual-Purpose True-Time-Delay Network

A hybrid-array hardware pattern that reuses the same analog true-time-delay modules for wideband beam-split calibration and inter-path symbol synchronization. Reuse can avoid a second digital-delay bank, but practical value depends on delay range, quantization, insertion loss, calibration, selector complexity, and switching latency.

[[hong-2026-beam-delay-alignment]] proposes this architecture with one-to-more selection so one RF-chain user signal can feed several path-specific delay/phase-shifter sets. Its performance is evaluated in simulation without a hardware prototype or component-loss model.
