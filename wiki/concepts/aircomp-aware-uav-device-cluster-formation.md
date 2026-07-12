---
type: concept
title: "AirComp-Aware UAV-Device Cluster Formation"
tags: [aircomp, uav-swarm, cluster-formation, digital-twin, energy-efficiency]
related:
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[digital-twin]]"
  - "[[over-the-air-computation]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-12
updated: 2026-07-12
---

# AirComp-Aware UAV-Device Cluster Formation

AirComp-aware UAV-device cluster formation assigns mobile UAV aggregators to ground-device groups while accounting for superposition distortion. Association cannot be separated from receiver scaling, device power, and trajectory because all four determine signal alignment, inter-cluster interference, propulsion energy, and which group can meet its MSE threshold.

[[zhang-2026-dt-aircomp-cluster-formation]] implements the pattern through a [[digital-twin]] feedback loop and four-block BCD solver. Each slot permits at most one UAV per group and one group per UAV; binary association recovery is followed by AirComp scaling, device-power allocation, and collision-safe trajectory optimization.

The pattern assumes coherent simultaneous transmission and a distortion model compatible with [[over-the-air-computation]]. Multipath beyond the LoS-dominant model, synchronization error, correlated or non-normalized sensing signals, or multi-group-per-UAV operation require revised channel/MSE or association models rather than direct reuse of the same formation rule.
