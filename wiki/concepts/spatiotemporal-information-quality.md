---
type: concept
title: "Spatiotemporal Information Quality"
tags: [information-quality, delay-reliability, spatial-completeness, uav-data-collection]
related:
  - "[[guo-2026-spatiotemporal-information-quality-ugrnet]]"
  - "[[martingale-delay-violation-bound]]"
  - "[[uav-data-collection]]"
  - "[[queueing-theory]]"
  - "[[stochastic-network-calculus]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Spatiotemporal Information Quality

A joint quality cost that combines temporal delivery reliability with spatial coverage fidelity. A weighted delay-violation probability bound represents temporal risk, while a Wasserstein distance between collected and required sensing distributions represents spatial mismatch; lower values indicate better quality in both terms.

[[guo-2026-spatiotemporal-information-quality-ugrnet]] controls this tradeoff through each ground robot's sensing task-completion ratio. Collecting more regions reduces spatial mismatch but raises arrival load and the [[martingale-delay-violation-bound]], so the simulated cost can attain an interior minimum rather than favoring complete collection unconditionally.

The formulation assumes that target and collected spatial distributions are available and uses simplified queue, link, routing, and regional-assignment models. The source supplies no optimization algorithm, convexity result, convergence proof, or UAV trajectory variable; its tested minima come from parameter sweeps and do not establish a general real-time path-planning method.
