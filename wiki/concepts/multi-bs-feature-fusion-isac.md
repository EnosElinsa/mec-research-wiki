---
type: concept
title: "Multi-BS Feature Fusion for ISAC"
tags: [isac, networked-isac, feature-fusion, trajectory-tracking, sensing]
related:
  - "[[yan-not-in-parse-multibs-isac-uav-trajectory]]"
  - "[[networked-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[multi-source-data-fusion]]"
  - "[[space-time-block-codec]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
created: 2026-07-11
updated: 2026-07-11
---

# Multi-BS Feature Fusion for ISAC

Multi-BS feature fusion estimates a target state from intermediate sensing features gathered by several base stations, rather than fusing raw waveforms or already-finalized position observations. In cellular ISAC, this is attractive because neighboring BSs may use communication-grade OFDM signals, imperfectly synchronized radios, and asynchronous sensing cycles.

[[yan-not-in-parse-multibs-isac-uav-trajectory]] uses delay and Doppler feature vectors as the fusion object. Each BS first estimates angles, compensates TO/CFO offsets, and extracts compact features. The fusion layer then aligns multi-BS geometry and applies compressed-sensing refinement for position/velocity before a sequential UKF handles asynchronous trajectory points.

This sits between two neighboring corpus patterns. [[zhao-2025-networked-isac-uav-handover]] focuses on virtual sensing cells and handover across BSs, while [[wang-2026-stbc-cooperative-isac]] focuses on shared-resource echo separation and SINR-weighted data fusion. Feature fusion is the middle layer: enough information to improve estimation, but not enough raw signal coupling to require full coherent radar-style synchronization.
