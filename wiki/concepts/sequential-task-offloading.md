---
type: concept
title: "Sequential Task Offloading"
tags: [task-offloading, multi-uav, scheduling, dependency]
related:
  - "[[teng-2026-gstrl-sequential-offloading]]"
  - "[[task-offloading]]"
  - "[[interdependent-tasks-dag]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[graph-neural-network]]"
created: 2026-07-07
updated: 2026-07-07
---

# Sequential Task Offloading

Sequential task offloading is an offloading model where a job is decomposed into ordered subtasks and a later subtask can be requested only after its predecessor completes. This differs from one-shot task offloading because the offloading choice for each subtask changes the location, queue, latency, and feasibility of its successors.

[[teng-2026-gstrl-sequential-offloading]] formulates this as sTOP in a dynamic multi-UAV system. It uses a heterogeneous graph for UAV/task topology and LSTM state for predecessor-successor dependencies. The concept overlaps with [[interdependent-tasks-dag]], but the source's core abstraction is a linear task sequence rather than an arbitrary DAG.
