---
type: concept
title: "S-Procedure for CSI Uncertainty"
tags: [robust-optimization, csi-uncertainty, semidefinite-programming, lmi]
related:
  - "[[yao-2026-secure-maritime-sutn]]"
  - "[[norm-bounded-csi-robust-optimization]]"
  - "[[csi-estimation-error]]"
created: 2026-07-14
updated: 2026-07-14
---

# S-Procedure for CSI Uncertainty

A robust-optimization device that, under the applicable S-lemma or generalized S-procedure regularity conditions, converts a semi-infinite quadratic implication over norm-bounded channel errors into a finite linear matrix inequality with an auxiliary nonnegative multiplier. When those conditions do not establish equivalence, the resulting LMI is a sufficient conservative restriction. The technique is commonly paired with Schur complements and semidefinite programming in robust beamforming.

[[yao-2026-secure-maritime-sutn]] uses generalized S-procedure and sign-definiteness transformations inside its fixed-trajectory beamforming block. Solving the resulting SDP handles that convexified block; it does not establish global optimality for the original jointly nonconvex beamforming-and-trajectory problem.
