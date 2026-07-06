---
type: concept
title: "Heuristic-Supervised DRL"
tags: [drl, heuristic-optimization, two-timescale-optimization, supervised-learning]
related:
  - "[[zhao-2026-heuristic-supervised-drl]]"
  - "[[two-timescale-optimization]]"
  - "[[particle-swarm-optimization]]"
  - "[[ppo]]"
  - "[[ctde-multi-agent-drl-protocol]]"
created: 2026-07-07
updated: 2026-07-07
---

# Heuristic-Supervised DRL

Heuristic-supervised DRL couples a heuristic planner, a DRL controller, and an online supervised predictor in one feedback loop. The heuristic planner searches slow strategic variables, the DRL controller executes fast operational decisions, and the supervised predictor estimates candidate plan quality from recent execution feedback so the planner does not need full rollouts for every candidate.

In [[zhao-2026-heuristic-supervised-drl]], this pattern is called HSD and is analyzed as a two-timescale stochastic approximation: the supervised bridge tracks the evolving lower-tier policy on a faster timescale, while the DRL/MARL policy evolves more slowly. The UAV-MEC instantiation uses [[particle-swarm-optimization]] for trajectory planning and MARL for resource allocation.
