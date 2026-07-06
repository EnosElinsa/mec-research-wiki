---
type: concept
title: "Linear Programming"
tags: [optimization, convex-optimization, resource-allocation]
related:
  - "[[second-order-cone-programming]]"
  - "[[two-stage-decomposition]]"
  - "[[generalized-assignment-problem]]"
  - "[[ji-2026-llm-iov-uav-offloading]]"
created: 2026-07-07
updated: 2026-07-07
---

# Linear Programming

A convex optimization model with a linear objective and linear equality/inequality constraints. In MEC papers it often appears after harder variables are fixed: once trajectory, association, or resource blocks are known, continuous task proportions or time/energy allocations can become an LP.

In [[ji-2026-llm-iov-uav-offloading]], LP determines task offloading ratios among local, UAV, and BS execution. The framework solves an LP after the DRL resource allocation to estimate failed and surplus tasks, lets the LLM adjust resource scheduling, then solves a second LP to obtain final offloading proportions.

This makes LP part of a [[two-stage-decomposition|decomposition]] chain rather than the whole solver: SOCP handles trajectory, DRL/LLM handles resource scheduling, and LP handles the continuous task-splitting ratios.
