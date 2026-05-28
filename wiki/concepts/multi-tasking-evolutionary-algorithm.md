---
type: concept
title: "Multi-Tasking Evolutionary Algorithm"
tags: [evolutionary, transfer-learning, multi-task, knowledge-sharing]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[dual-population-evolutionary-algorithm]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Multi-Tasking Evolutionary Algorithm

An evolutionary scheme where multiple related optimization tasks are solved **simultaneously** in a single population. Useful genetic material learned on one task can be reused for related tasks via crossover, which speeds up convergence on each.

In MEC, this is useful when the same UAV-MEC problem must be solved across **multiple environmental contexts** (e.g. multiple terrain configurations or multiple user distributions). [[wu-2026-terrain-aware-uav-mec]] adds a **task-adaptive mechanism** that retains historically-effective genetic operators per individual and biases their assignment by track record — a bandit-style operator selection on top of multi-tasking.

Distinct from **multi-objective** EAs (which find Pareto fronts within one task) and from **dual-population** schemes (which split one task across two populations). All three address exploration-exploitation but at different granularities.
