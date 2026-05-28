---
type: concept
title: "Completion-Time Difference"
tags: [synchronization, fusion, makespan, scheduling]
related:
  - "[[multi-source-data-fusion]]"
  - "[[makespan-minimization]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-05-29
---

# Completion-Time Difference

A scheduling objective that minimizes the **variance** (or sum of pairwise differences) of completion times across agents — the goal is to have everyone finish around the same time, not as fast as possible.

Why this is different from minimizing makespan: makespan = max completion time; minimizing it pulls all agents toward the same maximum, but doesn't penalize stragglers if a few agents finish quickly. Variance/diff penalizes stragglers and over-eager finishers symmetrically.

Why it matters: in [[multi-source-data-fusion|multi-source fusion]] (e.g. [[peng-2024-energy-time-uav-its]]), the fusion algorithm needs **temporally aligned** outputs. A 30-second gap between agents introduces stale-data problems. Federated learning has the same issue at synchronization rounds (see [[mao-2025-bcsa-frl]]).

Conflicts with energy minimization: pushing slow agents to finish faster usually means using more compute resource, hence more energy. So variance and energy are typically conflicting CMOP objectives.
