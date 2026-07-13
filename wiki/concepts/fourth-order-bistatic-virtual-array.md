---
type: concept
title: "Fourth-Order Bistatic Virtual Array"
tags: [bistatic-sensing, virtual-array, fourth-order-cumulant, near-field-localization]
related:
  - "[[min-2026-sparse-bistatic-nearfield-isac]]"
  - "[[sparse-xl-mimo]]"
  - "[[symmetric-double-nested-array]]"
  - "[[near-field-communications]]"
  - "[[joint-localization-and-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Fourth-Order Bistatic Virtual Array

A bistatic sensing construction that forms fourth-order cumulants from transmitter- and receiver-array observations. Conjugate products cancel the quadratic near-field phase terms used in the source model and create difference-coarray virtual manifolds at both ends, allowing angular variables to be estimated before a separate near-field range search.

[[min-2026-sparse-bistatic-nearfield-isac]] applies the construction to a sparse XL-MIMO transmitter and a spatially separated sensing receiver. It selects consecutive virtual-coarray portions, applies two-dimensional spatial smoothing to coherent equivalent sources, estimates paired departure and arrival angles, and then combines angle and range estimates for 3D UAV localization.

The construction is not a noise-independent ambiguity cure. Fourth-order statistics require many snapshots and become sensitive at low SNR; the source also assumes known transmitted symbols, invertible precoding, known array poses, a second-order spherical-distance approximation, and nonparallel bistatic geometry for unique upper-half-space localization.
