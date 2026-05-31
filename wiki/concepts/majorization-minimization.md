---
type: concept
title: "Majorization-Minimization (MM)"
tags: [optimization, convex, surrogate]
related:
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[monotonic-optimization]]"
  - "[[chu-2024-secure-ris-isac]]"
created: 2026-06-01
updated: 2026-06-01
---

# Majorization-Minimization (MM)

An iterative optimization framework that replaces a hard (often non-convex) objective or constraint with a **surrogate** that locally bounds it — a majorizer for minimization, a minorizer for maximization — typically built from a first-order Taylor expansion, then optimizes the easy surrogate and repeats, guaranteeing monotonic improvement. Successive convex approximation (SCA) is a closely related instance; MM is a generalization of the surrogate idea used across the corpus's convex-optimization pipelines (see [[alternating-optimization-sdr-sca]]).

In this wiki, [[chu-2024-secure-ris-isac]] uses MM (with a first-order Taylor surrogate that lower-bounds the non-convex RIS-reflection term), alongside SDR and Dinkelbach [[fractional-programming-dinkelbach|fractional programming]], to update the RIS reflection coefficients in its secure RIS-ISAC beamforming design.
