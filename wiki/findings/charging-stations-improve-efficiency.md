---
type: finding
title: Adding charging stations monotonically improves UAV-MEC performance
source: "[[liu-2026-jppo-en-convntm]]"
confidence: medium
replicated: null
tags: [uav, energy, infrastructure]
related:
  - "[[energy-expenditure-coefficient]]"
  - "[[uav-count-inverted-u-energy]]"
  - "[[uav-charging-scheduling]]"
created: 2026-05-28
updated: 2026-05-28
---

# Adding charging stations monotonically improves UAV-MEC performance

In [[liu-2026-jppo-en-convntm]] Fig. 5, holding UAV count at 2 and varying charging stations from 1 to 5:

- $\Omega_n$ (equilibrium efficiency) — improves
- $\psi_n$ (data collection) — improves
- $f_n$ (fairness) — improves
- $\kappa_n$ (energy expenditure) — *decreases* (better)

## Why

UAVs always pick the nearest available station, so adding stations shortens recharge detours and keeps UAVs closer to their data-collection zones. The marginal benefit shrinks as stations become abundant relative to fleet size — i.e. there's still a sub-linear return.

## Together with [[uav-count-inverted-u-energy]]

These two findings argue for **co-design**: pick fleet size and station count together, not independently. The optimal UAV count under-budgeted on stations is smaller than the optimal count with abundant stations.
