---
type: concept
title: "Minimum-Connection-Time Trajectory"
tags: [uav-trajectory, reliability, connection-time, multicast, optimization]
related:
  - "[[random-linear-network-coding-multicast]]"
  - "[[virtual-base-station-waypoint-design]]"
  - "[[linear-programming]]"
  - "[[zeng-2018-uav-multicasting-completion-time]]"
created: 2026-07-14
updated: 2026-07-14
---

# Minimum-Connection-Time Trajectory

A trajectory abstraction that replaces a probabilistic communication requirement with a minimum duration spent inside each receiver's connection region. Once the regions and required durations are known, path geometry and speed allocation can be optimized without repeatedly evaluating packet-level reliability.

[[zeng-2018-uav-multicasting-completion-time]] obtains the duration by lower-bounding RLNC recovery probability with a binomial tail and then applying a Gaussian approximation. For a fixed sampled path, an LP assigns traversal times subject to every terminal's minimum connection duration.

The exact binomial lower-bound problem is conservative and model-dependent: its feasibility guarantees the original recovery target under the assumed independent fading, but the converse need not hold. The final duration threshold additionally uses a Gaussian approximation with no error bound, so feasibility of that approximate duration formulation is not itself an exact reliability guarantee.
