---
type: concept
title: "Covariance-Intersection State Fusion"
tags: [state-estimation, covariance-intersection, distributed-tracking, data-fusion]
related: ["[[fang-2026-cellfree-uav-predictive-beamforming]]", "[[multi-source-data-fusion]]", "[[cell-free-uav-predictive-beamforming]]"]
created: 2026-07-14
updated: 2026-07-14
---

# Covariance-Intersection State Fusion

A conservative method for fusing state estimates whose cross-correlations are unknown. [[fang-2026-cellfree-uav-predictive-beamforming]] sends each AP's UAV state and covariance to a CPU, which combines information matrices with covariance-intersection weights rather than exchanging full CSI or assuming independent estimation errors.
