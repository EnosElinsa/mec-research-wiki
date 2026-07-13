---
type: concept
title: "Symmetric Double-Nested Array"
tags: [sparse-array, nested-array, coarray, degrees-of-freedom]
related:
  - "[[min-2026-sparse-bistatic-nearfield-isac]]"
  - "[[sparse-xl-mimo]]"
  - "[[fourth-order-bistatic-virtual-array]]"
  - "[[extremely-large-scale-mimo]]"
created: 2026-07-14
updated: 2026-07-14
---

# Symmetric Double-Nested Array

A one-dimensional sparse array composed of a compact central uniform subarray and two symmetrically placed sparse outer subarrays. The nested spacings enlarge the difference coarray while preserving a compact center, yielding more virtual sensing degrees of freedom than an equal-element compact ULA.

For the parameterization used by [[min-2026-sparse-bistatic-nearfield-isac]], the sensing degrees of freedom are `M_2(M_1+1)+(M_1-1)`, compared with `M-1` for its equal-element compact ULA. The source combines this geometry with a [[fourth-order-bistatic-virtual-array]] to suppress near-field phase coupling and resolve sparse-array ambiguities.

The degree-of-freedom expression is an array-geometry result, not a guarantee of localization accuracy or identifiability under arbitrary noise. Physical-array processing can retain grating lobes, and the source does not test mutual coupling, placement error, calibration drift, or a hardware realization.
