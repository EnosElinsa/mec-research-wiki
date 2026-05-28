---
type: concept
title: Spatial Equity Index (f)
tags: [metric, fairness]
related:
  - "[[equilibrium-efficiency-metric]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Spatial Equity Index (f)

A Jain-style fairness measure of how evenly UAVs cover the device population:

$$
f_n = \frac{\big(\sum_d \iota_{d,n}\big)^2}{D \sum_d \iota_{d,n}^2}
$$

where $\iota_{d,n}$ is the cumulative number of times device $d$ has been visited (within the UAV communication range) by any UAV up to time $n$, and $D$ is the device count.

- $f_n = 1$ iff every device has been visited the same number of times.
- $f_n \to 1/D$ if a single device dominates visits.

In [[high-density-mobile-device-scenarios]] this metric is what penalizes a UAV that just camps over the densest cluster.
