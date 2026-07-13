---
type: concept
title: "PCRB-Guided Pilot-Length Optimization"
tags: [posterior-crb, pilot-overhead, resource-allocation, uav-tracking]
related: ["[[fang-2026-cellfree-uav-predictive-beamforming]]", "[[cramer-rao-bound]]", "[[cell-free-uav-predictive-beamforming]]"]
created: 2026-07-14
updated: 2026-07-14
---

# PCRB-Guided Pilot-Length Optimization

A resource-control pattern that turns predicted estimation uncertainty into a minimum training requirement. [[fang-2026-cellfree-uav-predictive-beamforming]] expresses UAV position PCRB as a monotone function of pilot length, selects the shortest feasible pilot by integer bisection, and allocates association/power using the remaining frame resources.
