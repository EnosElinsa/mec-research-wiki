---
type: concept
title: "Geometric Disk Cover (GDC)"
tags: [coverage, deployment, np-hard, optimization, aerial-base-station]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[lyu-2017-spiral-mbs-placement]]"
  - "[[zhang-2026-omnidirectional-monitoring-deployment]]"
created: 2026-06-02
updated: 2026-07-12
---

# Geometric Disk Cover (GDC)

The combinatorial problem of covering a set of `K` points (e.g. ground terminals) in the plane with the **minimum number of disks of a given fixed radius `r`**, such that every point lies inside at least one disk. It is NP-hard in general. The closely-related **p-center** problem instead fixes the *number* of disks `p` and minimizes the covering *radius* — so GDC can be solved as a sequence of p-center problems with increasing `p` until the radius drops to `r`.

Why it shows up in aerial networking: when UAV-mounted base stations have a fixed ground coverage radius (a fixed-altitude LoS link with an SNR threshold), "how few UAVs do I need, and where?" is exactly GDC. The exact **core-sets** method has running time exponential in `K`, so practical work uses heuristics: a **strip-based** partition (fast but lossy, since points in different strips can't share a disk) or clustering like [[weighted-kmeans-uav-deployment]].

## In this wiki

[[lyu-2017-spiral-mbs-placement]] casts minimum-count UAV-MBS coverage as GDC and solves it with a polynomial-time **spiral** heuristic: place base stations sequentially around the convex-hull perimeter of the still-uncovered terminals and nudge each inward, tracing an inward spiral until all terminals are covered. It nearly matches the core-sets optimum on small instances while running far faster, and beats strip-based and K-means placement. GDC is the **count-minimization** complement to the single-UAV **3-D placement** problem of [[drone-cell-3d-placement]] / [[bor-yaliniz-2016-3d-abs-placement]] (which uses [[mixed-integer-nonlinear-programming|MINLP]] over altitude + location for one drone-cell).
