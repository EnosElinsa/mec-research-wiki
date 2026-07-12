---
type: concept
title: "Multi-Source Data Fusion"
tags: [data-fusion, perception, uav, its]
related:
  - "[[cooperative-perception]]"
  - "[[uav-enabled-its]]"
  - "[[completion-time-difference]]"
  - "[[xie-2026-uav-multisource-fusion]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[yan-not-in-parse-multibs-isac-uav-trajectory]]"
  - "[[multi-bs-feature-fusion-isac]]"
  - "[[wang-2025-cellular-uav-cooperative-detection]]"
  - "[[ground-air-cooperative-isac-detection]]"
created: 2026-05-29
updated: 2026-07-13
---

# Multi-Source Data Fusion

Combining observations from multiple sensors / agents into a unified output that's more accurate or complete than any single source alone. In MEC, two flavors appear:

- **Spatial fusion** — different agents observe different parts of the scene (e.g. multiple vehicles seeing different occlusion-blocked objects). [[xie-2026-uav-multisource-fusion]] uses a UAV to fuse vehicular observations of "non-connected objects" — things only one vehicle saw.
- **Temporal-aligned fusion** — agents observe overlapping data at multiple times; the control center aligns and combines. [[peng-2024-energy-time-uav-its]] highlights that **completion-time difference** between agents degrades fusion quality.

Fusion has its own optimization shape: synchronization matters; latency matters more than throughput; missing one input degrades the output. Reward functions for fusion-aware MEC therefore include synchronization terms (e.g. variance of finish times) that pure-task-offloading rewards don't have.

[[yan-not-in-parse-multibs-isac-uav-trajectory]] adds a cellular-ISAC sensing variant: [[multi-bs-feature-fusion-isac]] combines delay/Doppler feature vectors from multiple BSs before trajectory association, avoiding both raw coherent signal fusion and late data-only averaging.

[[wang-2025-cellular-uav-cooperative-detection]] instead performs [[ground-air-cooperative-isac-detection]]: a ground BS and one connected UAV independently estimate surrounding UAV states, associate them by normalized position/motion distance, and fuse the matched states with an extended Kalman filter before the next trajectory and beamforming update.
