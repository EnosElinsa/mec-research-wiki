---
type: concept
title: "Parallel vs Serial Processing in MEC"
tags: [scheduling, heterogeneous, queueing, processor-model]
related:
  - "[[dispersed-computing]]"
  - "[[mobile-edge-computing]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
  - "[[fan-2026-parallel-caching-uav-mec]]"
created: 2026-05-29
updated: 2026-07-07
---

# Parallel vs Serial Processing in MEC

A modeling distinction that matters in **heterogeneous** MEC environments. An edge server with a many-core CPU runs received tasks **in parallel**, sharing CPU frequency among them per a continuous resource-allocation decision. A small IoT device with a single-core CPU and a task queue runs tasks **in series**, one at a time, with priority determining the order.

Why this matters for offloading optimization:

- **Edge cost** is roughly $\sum_i W_i / f_i$ (parallel, with allocated $f_i$ each).
- **IoTD cost** is the sum of waiting + execution times in the queue, which depends on processing order — a combinatorial decision.

[[huang-2025-cmop-dispersed-computing]] explicitly models both styles in the same problem; the queue position becomes part of the decision space.

Most prior MEC sources in the wiki implicitly assume parallel processing everywhere. The serial model makes a real difference when the worker pool includes lightweight devices.

[[fan-2026-parallel-caching-uav-mec]] uses the same distinction from a UAV-server angle: a UAV can overlap receiving task data, computing tasks, and returning results for different mobile devices, so caching/offloading/channel decisions should minimize service duration under parallel execution rather than under a serialized task pipeline.
