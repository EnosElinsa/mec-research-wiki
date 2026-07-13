---
type: concept
title: "HAPS-UAV ISAC Resource Allocation"
tags: [haps, uav, isac, multi-objective, resource-allocation, nsga-ii]
related:
  - "[[kanani-2026-haps-uav-isac]]"
  - "[[high-altitude-platform-station]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
created: 2026-07-14
updated: 2026-07-14
---

# HAPS-UAV ISAC Resource Allocation

A two-tier aerial ISAC architecture in which UAV access points transmit communication/sensing waveforms and a [[high-altitude-platform-station|HAPS]] coordinates signal processing. [[kanani-2026-haps-uav-isac]] optimizes UAV positions, beamforming, and powers against two separate objectives: target-echo power and worst-user SINR. Weighted-sum GA returns one preference-conditioned solution, while [[non-dominated-sorting-genetic-algorithm|NSGA-II]] exposes a Pareto set of sensing/communication trade-offs.
