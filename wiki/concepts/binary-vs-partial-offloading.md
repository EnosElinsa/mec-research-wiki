---
type: concept
title: Binary vs Partial Task Offloading
tags: [task-offloading, design-choice]
related:
  - "[[task-offloading]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Binary vs Partial Task Offloading

Two formulations of the offloading decision that recur across MEC papers:

| Aspect | Binary | Partial |
|---|---|---|
| Decision per task | $x \in \{0, 1\}$ — fully local or fully offloaded | $\lambda \in [0, 1]$ — fraction offloaded |
| Reflects | Indivisible tasks (e.g. legacy binaries, transactions) | Data-parallel tasks (e.g. neural-net inference, matrix ops) |
| Resulting program | Mixed-Integer Nonlinear Program (MINLP) | Continuous nonlinear program (often non-convex but tractable) |
| Combinatorial complexity | $2^N$ for $N$ devices | continuous, smooth |
| DRL fit | DQN family, hybrid actor (continuous part for $\tau, p$, discrete for $x$) | Continuous actor (DDPG, SAC, PPO) |

## When to pick which

- **Binary** when tasks are strictly indivisible — e.g. database transactions, signed firmware blobs, blockchain transactions. Also chosen when the optimization advantage of dividing the task is dominated by signaling overhead.
- **Partial** when tasks decompose naturally — sensor preprocessing, ML inference layers, frame-by-frame video. The optimization problem becomes far more tractable.

## In this wiki

- **Binary:** [[zhu-2025-lycnn-drl-wpt-mec]] (LSEM uses $x_i(k) \in \{0,1\}$).
- **Partial:** [[liu-2026-jppo-en-convntm]] (uses $\lambda_{u,d,n} \in [0,1]$).

Both are valid and the choice is application-driven, not algorithmic. When comparing across papers, keep this axis in mind — a binary scheme can't be benchmarked apples-to-apples against a partial scheme without normalizing.
