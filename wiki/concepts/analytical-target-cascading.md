---
type: concept
title: "Analytical Target Cascading"
tags: [optimization, decomposition, coordination]
related:
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[two-stage-decomposition]]"
  - "[[ye-2026-flight-speed-battery-swapping]]"
created: 2026-07-07
updated: 2026-07-07
---

# Analytical Target Cascading

Analytical target cascading (ATC) is a decomposition-and-coordination method for large coupled optimization problems. A system-level problem is split into subproblems; shared variables are passed as targets, and consistency penalties drive local decisions toward agreement.

In [[ye-2026-flight-speed-battery-swapping]], ATC is used as a large-scale heuristic for the joint flight-speed, battery-swapping, and offloading problem after the exact mixed-integer convex reformulation becomes expensive. The parse reports that the ATC iterations drive consistency error close to zero and keep mission time within the deadline in the tested settings.
