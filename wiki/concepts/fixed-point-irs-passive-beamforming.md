---
type: concept
title: "Fixed-Point IRS Passive Beamforming"
tags: [intelligent-reflecting-surface, passive-beamforming, fixed-point-iteration, unit-modulus, alternating-optimization]
related:
  - "[[ahmed-2026-noma-irs-vehicular]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[noma]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[wu-2019-irs-joint-beamforming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Fixed-Point IRS Passive Beamforming

Fixed-point IRS passive beamforming iteratively updates a reflecting-phase vector from a local objective surrogate and projects every entry back onto the unit circle. It converts a continuous unit-modulus phase block into repeated low-cost updates, usually inside an alternating loop with transmit beamforming or power allocation.

[[ahmed-2026-noma-irs-vehicular]] linearizes the NOMA sum-capacity problem around feasible SINR points, applies projected fixed-point phase updates for the passive IRS, and alternates them with convex UAV power allocation. The reported capacity of the joint proposed algorithm stabilizes after two or three alternating iterations in the two-vehicle simulations; this does not isolate the convergence rate of the inner phase loop.

The projection preserves passive phase feasibility but does not establish a global optimum. The method therefore belongs to the local [[alternating-optimization-sdr-sca|alternating/convex-approximation]] family and contrasts with SDR-based passive-beamforming formulations such as [[wu-2019-irs-joint-beamforming]].
