---
type: concept
title: "Deadline-Constrained UAV Data Collection"
tags: [uav, data-collection, deadlines, admission-control]
related:
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[uav-data-collection]]"
  - "[[age-of-information]]"
  - "[[branch-reduce-and-bound]]"
  - "[[transformer-weighted-a-star-trajectory-planning]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[many-to-one-pickup-and-delivery]]"
  - "[[dynamic-programming-battery-station-insertion]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Deadline-Constrained UAV Data Collection

UAV collection in which each device has a data-generation time, a hard expiry time, and a cumulative upload requirement. A device is admitted only when its complete requirement can be served inside that lifetime, making trajectory, spectrum allocation, and admission decisions inseparable.

[[samir-2020-time-constrained-data-collection]] maximizes the number of admitted devices and then optionally shortens the route while preserving that set. Unlike [[age-of-information|AoI]] minimization, the objective counts complete on-time uploads rather than continuously penalizing staleness.
