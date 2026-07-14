---
type: concept
title: "Phase-Rotated DFT Motion-Parameter Estimation"
tags: [isac, dft, parameter-estimation, target-tracking]
related:
  - "[[yan-2026-uav-trajectory-monitoring]]"
  - "[[uav-trajectory-monitoring]]"
  - "[[mmwave-radar-sensing]]"
created: 2026-07-14
updated: 2026-07-14
---

# Phase-Rotated DFT Motion-Parameter Estimation

A spectral-refinement method that first identifies a coarse DFT/IDFT peak and then searches a bounded phase-rotation grid to reduce off-bin leakage. Applied across OFDM subcarriers, symbols, and array dimensions, it can refine range, angle, and velocity-related parameters without the cubic matrix decomposition of subspace estimators.

[[yan-2026-uav-trajectory-monitoring]] uses PRDFT to estimate target distance, horizontal and pitch angles, radial velocity, and two angular velocities. Its reported accuracy and complexity are simulation and implementation-model results, not a universal estimator guarantee.
