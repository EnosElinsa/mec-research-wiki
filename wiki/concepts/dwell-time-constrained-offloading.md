---
type: concept
title: "Dwell-Time-Constrained Offloading"
tags: [task-offloading, mobility, vehicular-mec, constraint, aerial-mec]
related:
  - "[[vehicular-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[task-offloading]]"
  - "[[zhang-2026-dwell-time-aerial-vec]]"
created: 2026-07-06
updated: 2026-07-06
---

# Dwell-Time-Constrained Offloading

**Dwell-time-constrained offloading** treats limited contact or coverage duration as a feasibility constraint for task execution. A mobile user can offload to a nearby aerial or non-terrestrial server only if upload, computation, and any return/downlink stage finish before the user leaves the server's coverage region.

## In this wiki

- [[zhang-2026-dwell-time-aerial-vec]] applies this idea to multi-layer aerial vehicular edge computing. A vehicle may offload to a UAV only if the task can complete before the vehicle exits the UAV coverage area; otherwise the HAP tier acts as a broader-coverage fallback.

## Relation to coverage time

The constraint is conceptually close to [[leo-satellite-coverage-time]], where a fast-moving satellite creates a finite service window. In aerial VEC, the finite window is created by high-speed vehicles moving through UAV coverage.
