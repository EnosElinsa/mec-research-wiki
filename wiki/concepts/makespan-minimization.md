---
type: concept
title: "Makespan Minimization"
tags: [scheduling, makespan, dag, classical-objective]
related:
  - "[[interdependent-tasks-dag]]"
  - "[[completion-time-difference]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Makespan Minimization

Makespan = the latest finish time across all tasks (or all UAVs). Minimizing makespan ensures the *whole batch* finishes as quickly as possible — important when a downstream consumer waits for the full output (a fusion node, a render, a model-aggregation round).

Distinct from average completion time (which treats stragglers softly) and from [[completion-time-difference]] (which targets variance, not maximum). Each shape captures a different operational concern:

- Makespan: deadline-driven batches.
- Average completion: throughput-driven streams.
- Time difference: synchronization-driven fusion.

In the wiki, [[huang-2023-mu-aec-task-energy]] uses makespan as one of its two CMOP objectives (paired with energy balancing), respecting the DAG dependencies of the task graph. The makespan computation reduces to a longest-path traversal of the DAG with edge weights = transmission + computation time per task.
