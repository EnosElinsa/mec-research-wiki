---
type: concept
title: "Longest-Transmission-Time-First UAV Grouping"
tags: [scheduling, load-balancing, multi-uav, makespan, heuristic]
related:
  - "[[krishna-m-2026-multiuav-nbiot]]"
  - "[[makespan-minimization]]"
created: 2026-07-14
updated: 2026-07-14
---

# Longest-Transmission-Time-First UAV Grouping

A greedy multi-UAV load-balancing rule that orders device loads by descending transmission time and assigns each one to the currently lightest UAV pool. [[krishna-m-2026-multiuav-nbiot]] uses this longest-processing-time-style heuristic to reduce the maximum pool completion time under non-uniform NB-IoT traffic. The rule is computationally light but is not proven globally optimal in that source.
