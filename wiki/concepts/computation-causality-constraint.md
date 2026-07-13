---
type: concept
title: "Computation Causality Constraint"
tags: [mobile-edge-computing, task-offloading, causality, scheduling]
related:
  - "[[xie-2021-uav-wpt-tutorial]]"
  - "[[task-offloading]]"
  - "[[energy-causality-constraint]]"
  - "[[information-causality-constraint]]"
created: 2026-07-14
updated: 2026-07-14
---

# Computation Causality Constraint

A cumulative scheduling condition that prevents an edge server from executing task bits before they have been offloaded and prevents result transmission before the corresponding computation has finished. Deadline formulations also require all admitted input bits to be executed and all output bits to be returned by the mission end.

[[xie-2021-uav-wpt-tutorial]] shows why this constraint materially complicates UAV-enabled wireless-powered MEC: WPT, offloading, aerial execution, result downloading, and flight all share time and energy. The tutorial formulates the full causal problem but does not solve it; the trajectory structures it surveys apply directly only after computation causality is simplified or omitted.
