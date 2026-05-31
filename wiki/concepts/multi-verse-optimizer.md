---
type: concept
title: "Multi-Verse Optimizer (MVO)"
tags: [metaheuristic, multi-objective, swarm-intelligence]
related:
  - "[[binary-whale-optimization]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[liang-2024-hmecmop-uav-cb]]"
created: 2026-05-29
updated: 2026-06-01
---

# Multi-Verse Optimizer (MVO)

A metaheuristic inspired by the multiverse cosmological theory. Three operators model "white holes" (best-fitness universes propagate solutions), "black holes" (other universes absorb), and "wormholes" (random tunneling toward the current best). Easy to implement, decent on smooth landscapes, weaker on highly non-convex ones.

Used in [[liu-2025-haps-uav-maritime-iot]] in an enhanced form (EMOMVO-CGD) — chaos for exploration, grey-wolf for exploitation, discrete-update for binary association variables. Also used in [[liang-2024-hmecmop-uav-cb]] as an **improved multiobjective** MVO (IMOMVO) with a vertical-and-horizontal renewal strategy + nearest-neighbor procedure, to solve a mixed continuous/discrete (positions + excitation weights + BS-communication order) hovering-vs-motion-energy MOP for UAV collaborative beamforming. Comparable to [[binary-whale-optimization|BWOA]] used in [[jia-2025-dro-uav-hap-mec]] — different metaphors, same role: a swarm-based metaheuristic for non-convex MOPs after a convex inner subproblem has been peeled off.

Treat metaheuristics like MVO and BWOA as "use when convex relaxation isn't available and DRL would be overkill" — they're cheap, no training, no convergence guarantees but reasonable empirical performance on the wiki's UAV-MEC instances.
