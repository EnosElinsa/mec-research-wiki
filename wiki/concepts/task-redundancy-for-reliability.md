---
type: concept
title: "Task Redundancy for Reliability"
tags: [reliability, redundancy, fault-tolerance, dispersed-computing]
related:
  - "[[dispersed-computing]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
  - "[[li-2026-tspf-forest-fire-uav-swarm]]"
  - "[[two-tier-submodel-partition]]"
created: 2026-05-29
updated: 2026-07-07
---

# Task Redundancy for Reliability

When individual processors are unreliable (per-task failure probability $\varphi_j$), the same task can be run on $k$ independent processors in parallel; the **task succeeds** if at least one of them succeeds. The success probability is $P = 1 - \prod_{j} \varphi_j$, so the *joint failure* probability $\prod_{j} \varphi_j$ falls geometrically with $k$ — driving $P$ toward 1.

In [[huang-2025-cmop-dispersed-computing]] this is the central reliability mechanism: each task is duplicated across enough IoTDs that the resulting success probability meets the per-task reliability requirement $\bar R_i$. The cost: redundant executions consume more bandwidth, more compute, and more monetary charge — so reliability and charge are conflicting objectives.

Different from the **voting-based** correctness check in [[ccvm-correction-voting]] / [[mao-2025-bcsa-frl]]: voting handles **adversarial** failures (Byzantine-style malicious workers), redundancy handles **stochastic** failures.

[[li-2026-tspf-forest-fire-uav-swarm]] is related but not identical: it uses intragroup data backup to preserve destroyed UAVs' training data in a forest-fire-detection swarm, rather than running the same computing task redundantly on multiple processors.
