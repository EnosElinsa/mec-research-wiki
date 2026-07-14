---
type: concept
title: "Beam-Delay Alignment Transmission"
tags: [cell-free-massive-mimo, wideband, beamforming, time-delay]
related:
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[wideband-asynchronous-cell-free-massive-mimo]]"
  - "[[semi-synchronized-path-set]]"
  - "[[dual-purpose-time-delay-network]]"
created: 2026-07-14
updated: 2026-07-14
---

# Beam-Delay Alignment Transmission

A distributed wideband transmission method that aligns each selected user-path component in both direction and arrival time. A path with delay $\tau_{lkp}$ is transmitted with compensating delay $\tau_k^{\max}-\tau_{lkp}$ so useful multipath components reach user $k$ at a common symbol reference.

[[hong-2026-beam-delay-alignment]] applies BDAT to terrestrial cell-free APs serving UAV users. Delay alignment differs from phase-only beam steering: paths whose residual timing mismatch exceeds the cyclic-prefix tolerance can still create inter-carrier and inter-symbol interference unless they are suppressed or excluded.
