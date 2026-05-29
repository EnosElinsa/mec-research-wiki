---
type: concept
title: "Computational Task Caching"
tags: [caching, scheduling, mec, deferral]
related:
  - "[[service-caching-mec]]"
  - "[[task-migration]]"
  - "[[lyapunov-optimization]]"
  - "[[zhao-2025-traj-offload-cache-migration]]"
created: 2026-05-29
updated: 2026-05-29
---

# Computational Task Caching

Caching **whole computational tasks** (not content/data) at an edge node and **deferring their execution** to a later time slot when compute capacity frees up. Under tight, time-varying UAV compute, caching a task during a demand peak — instead of dropping it or forcing immediate execution — can cut service-denial events and raise long-term throughput, at the cost of added latency and cache-stability bookkeeping.

This is the central, explicitly-novel mechanism of [[zhao-2025-traj-offload-cache-migration]], which adds it as a third option alongside local compute and inter-UAV [[task-migration]], governed by a cache-stability constraint inside a [[lyapunov-optimization]] framework. It is distinct from [[service-caching-mec]] (content/service pre-caching, e.g. caching the *program/model* needed to serve a task) — here it is the *pending task itself* that is cached.
