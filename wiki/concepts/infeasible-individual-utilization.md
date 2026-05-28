---
type: concept
title: "Infeasible Individual Utilization"
tags: [evolutionary, constraint-handling, exploration]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[cmoea-d-cdp]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
created: 2026-05-29
updated: 2026-05-29
---

# Infeasible Individual Utilization

A constraint-handling technique that **deliberately retains** some infeasible individuals in the population — the ones with strong objective values — instead of discarding them all. The retained infeasibles seed exploration of regions near the Pareto front but on the wrong side of a constraint, which is exactly where the optimum often sits.

A typical implementation uses a parameter $\alpha \in [0, 1]$ to control the retained fraction per generation: $\alpha = 1$ early on (explore freely), then decay $\alpha$ toward 0 (force feasibility) — see [[peng-2022-cmop-uav-path-planning]] for a clean instance.

Distinct from but compatible with **repair-based** constraint handling, which transforms infeasibles into feasibles directly — see [[peng-2024-energy-time-uav-its]] and [[huang-2025-cmop-dispersed-computing]] for that variant.
