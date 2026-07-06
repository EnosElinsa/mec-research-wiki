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
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[wu-2026-secure-split-offloading-ci]]"
created: 2026-05-29
updated: 2026-07-07
---

# Whale Optimization Algorithm (WOA)

A bio-inspired swarm metaheuristic that mimics humpback-whale bubble-net hunting. Candidate solutions ("whales") update their positions via two phases: **encircling/shrinking** (exploitation, moving toward the best agent) and **spiral** bubble-net updates, with a stochastic switch between exploration (random search agent) and exploitation. It operates over **continuous** search spaces.

In the wiki, [[wu-2025-iopo-irs-uav-thz-mec]] uses WOA as the stage-2 solver for continuous IRS phase shifts (given a fixed offloading decision from stage 1). [[liao-2026-aoi-ris-uav-usv-mec]] uses an enhanced WOA for RUAV trajectory optimization inside an AoI-aware RIS-assisted UAV-USV MEC controller. [[wu-2026-secure-split-offloading-ci]] uses a discrete WOA variant for early-exit and DNN-partition selection in secure collaborative inference. Note this is the **continuous** variant, distinct from the wiki's existing [[binary-whale-optimization]] page (used for 0/1 decisions in [[jia-2025-dro-uav-hap-mec]]).
