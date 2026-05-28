---
type: concept
title: "Task Redundancy for Reliability"
tags: [reliability, redundancy, fault-tolerance, dispersed-computing]
related:
  - "[[dispersed-computing]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
created: 2026-05-29
updated: 2026-05-29
---

# Task Redundancy for Reliability

When individual processors are unreliable (per-task failure probability $\varphi_j$), the same task can be run on $k$ independent processors in parallel; the **task succeeds** if at least one (or a quorum, depending on verification) succeeds. The success probability becomes $1 - \prod_{j} \varphi_j$, which falls geometrically with $k$.

In [[huang-2025-cmop-dispersed-computing]] this is the central reliability mechanism: each task is duplicated across enough IoTDs that the resulting success probability meets the per-task reliability requirement $\bar R_i$. The cost: redundant executions consume more bandwidth, more compute, and more monetary charge — so reliability and charge are conflicting objectives.

Different from the **voting-based** correctness check in [[ccvm-correction-voting]] / [[mao-2025-bcsa-frl]]: voting handles **adversarial** failures (Byzantine-style malicious workers), redundancy handles **stochastic** failures.
