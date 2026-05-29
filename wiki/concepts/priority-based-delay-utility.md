---
type: concept
title: "Priority-Based Delay Utility"
tags: [qoe, task-priority, utility, scheduling]
related:
  - "[[task-priority-in-mec]]"
  - "[[qoe-modeling-mec]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
  - "[[hao-2025-priority-aware-task-driven-co]]"
created: 2026-05-29
updated: 2026-05-29
---

# Priority-Based Delay Utility

An **asymmetric utility function** that encodes task priority into how delay is rewarded, instead of using preemptive scheduling (which starves low-priority tasks). High-priority tasks get a logarithmic on-time reward and a hard penalty for missing the deadline; low-priority tasks get a fixed on-time reward and an exponentially decaying (but non-zero) utility when late — so they are deprioritized without being starved.

In the wiki, [[hao-2024-clp-multiuav-priority-offloading]] uses this as the per-task utility inside its "system gain" objective, letting a single reward capture delay, energy, and priority. It is the utility-shaping mechanism behind [[task-priority-in-mec]] and a close relative of the priority utility in [[hao-2025-priority-aware-task-driven-co]] (same lead author); it connects to [[qoe-modeling-mec]] through the experience-vs-deadline framing.
