---
type: concept
title: "Dynamic QoS Constraints"
tags: [qos, dynamic-constraints, time-varying, iiot, scheduling]
related:
  - "[[qoe-modeling-mec]]"
  - "[[dynamic-constrained-multi-objective-optimization]]"
  - "[[task-priority-in-mec]]"
  - "[[niazmand-2025-jopa-dnn-pruning-iiot]]"
created: 2026-05-31
updated: 2026-05-31
---

# Dynamic QoS Constraints

QoS requirements (e.g. end-to-end **delay** and inference **accuracy**) that **change over time** rather than being fixed per task type. The same task class can carry a higher or lower delay/accuracy bar at different instants, reflecting a changing **criticality level** of the underlying physical process.

This breaks the common stationary-requirement assumption and forces the scheduler to **adapt online** — e.g. by switching among differently-pruned models, re-allocating compute, or changing offloading decisions per slot to track the moving requirement while bounding the **task-dropping rate**.

In the wiki, [[niazmand-2025-jopa-dnn-pruning-iiot]] makes time-varying per-task delay and accuracy requirements first-class: an industrial washing machine's fault-detection task gets stricter accuracy as its mechanical condition degrades, and the SAC policy picks pruned-vs-full models to satisfy the moving bar with <1% dropping. Related to the time-evolving feasible region of [[dynamic-constrained-multi-objective-optimization]] and to [[task-priority-in-mec]].
