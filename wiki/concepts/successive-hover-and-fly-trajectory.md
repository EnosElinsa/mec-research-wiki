---
type: concept
title: "Successive Hover-and-Fly Trajectory"
tags: [uav-trajectory, wpt, convex-optimization]
related:
  - "[[uav-trajectory-control]]"
  - "[[wireless-power-transfer]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
created: 2026-06-01
updated: 2026-06-01
---

# Successive Hover-and-Fly Trajectory

A structured UAV-trajectory primitive for problems whose **speed-unconstrained** optimum is a set of fixed **hovering locations** with optimal time allocations. The UAV successively **hovers** at each of those locations for a prescribed duration and **flies at maximum speed** between them along the shortest path that visits all of them — so the total flying time (pure overhead) is minimized. It is motivated by the multi-location-hovering solution of the relaxed problem and serves both as a near-optimal design in its own right and as a good initialization for a [[alternating-optimization-sdr-sca|successive-convex-programming (SCP)]] refinement.

## In this wiki

- [[xu-2018-uav-wpt-trajectory]] introduces the successive hover-and-fly trajectory for UAV-enabled [[wireless-power-transfer|WPT]] max-min (min-energy) energy delivery. It is proved optimal for $K=2$ energy receivers and asymptotically optimal for $K>2$ as the charging duration grows large (the flying-time overhead becomes negligible). An SCP-based algorithm, initialized by this trajectory, refines it to a locally optimal solution. The structure generalizes to other UAV [[uav-trajectory-control|trajectory-design]] problems where serving distributed ground nodes reduces to visiting a discrete set of good hovering spots.
