---
type: concept
title: "Geometric Dilution of Precision"
tags: [localization, metric, sensing-geometry, tdoa]
related:
  - "[[wang-2026-mat-target-tracking]]"
  - "[[tdoa-based-uav-localization]]"
  - "[[joint-localization-and-communication]]"
created: 2026-07-13
updated: 2026-07-13
---

# Geometric Dilution of Precision

Geometric dilution of precision (GDOP) measures how receiver/anchor geometry amplifies ranging or angle-measurement error in a position estimate. A small value indicates well-spread sensing geometry; a large value indicates nearly degenerate geometry, such as collinear receivers. It describes geometric sensitivity rather than realized error and cannot remove biased NLoS measurements.

[[wang-2026-mat-target-tracking]] uses `sqrt(trace((G^T G)^-1))` in both its localization analysis and UAV-swarm reward. The paper's results show why GDOP and realized MAE/RMSE must remain separate: MAT obtains the best mean position errors in several simulations without always obtaining the best GDOP.
