---
type: concept
title: "Block Successive Upper-Bound Minimization"
tags: [optimization, nonconvex, decomposition]
related:
  - "[[two-stage-decomposition]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[tun-2025-thz-sag-mec-resource-allocation]]"
  - "[[heo-not-in-parse-blockage-aided-multiuav-interference]]"
  - "[[pham-2026-vnf-control-loop]]"
  - "[[routing-vnf-scaling-control-loop]]"
created: 2026-07-07
updated: 2026-07-13
---

# Block Successive Upper-Bound Minimization

Block Successive Upper-Bound Minimization (BSUM) is a decomposition method for non-convex or non-smooth optimization. It partitions variables into blocks, builds a tractable upper-bound surrogate for one block while holding the others fixed, minimizes that surrogate, and cycles through the blocks. Under suitable surrogate conditions, the iterations converge to a stationary point.

In [[tun-2025-thz-sag-mec-resource-allocation]], BSUM solves the UAV task-offloading subproblem after binary forwarding variables are relaxed. It is the fourth block in a larger BCD-style solver: device offloading, THz sub-band/power control, UAV deployment, and UAV task forwarding.

BSUM sits near [[alternating-optimization-sdr-sca]] in the corpus because both are classical decomposition tools used when direct mixed-integer non-convex optimization is too hard.

[[heo-not-in-parse-blockage-aided-multiuav-interference]] is adjacent in the same decomposition family: it cycles scheduling, trajectory, channel-state, and power-control subproblems with SCA/PCCP-style convexification and BCD, although it does not name BSUM as the headline method.
