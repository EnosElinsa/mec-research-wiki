---
type: concept
title: "Whale Optimization Algorithm (WOA)"
tags: [optimization, metaheuristic, continuous, swarm-intelligence]
related:
  - "[[binary-whale-optimization]]"
  - "[[self-adaptive-global-best-harmony-search]]"
  - "[[multi-verse-optimizer]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
created: 2026-05-29
updated: 2026-06-03
---

# Whale Optimization Algorithm (WOA)

A bio-inspired swarm metaheuristic that mimics humpback-whale bubble-net hunting. Candidate solutions ("whales") update their positions via two phases: **encircling/shrinking** (exploitation, moving toward the best agent) and **spiral** bubble-net updates, with a stochastic switch between exploration (random search agent) and exploitation. It operates over **continuous** search spaces.

In the wiki, [[wu-2025-iopo-irs-uav-thz-mec]] uses WOA as the stage-2 solver for continuous IRS phase shifts (given a fixed offloading decision from stage 1). Note this is the **continuous** variant, distinct from the wiki's existing [[binary-whale-optimization]] page (used for 0/1 decisions in [[jia-2025-dro-uav-hap-mec]]).
