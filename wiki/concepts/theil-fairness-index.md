---
type: concept
title: Theil Coefficient as a Fairness Index
tags: [fairness, metric, inequality]
related:
  - "[[spatial-equity-index]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Theil Coefficient as a Fairness Index

An entropy-based inequality measure originally from economics:

$$
T = \frac{1}{N} \sum_{i=1}^N \frac{x_i}{\bar x} \ln\frac{x_i}{\bar x}
$$

where $x_i$ is the share of resource (or service count) for unit $i$ and $\bar x$ is the mean. $T = 0$ at perfect equality; larger values indicate more concentration.

## Why MEC papers use it

- **Sensitivity to disparities** — penalizes outliers more sharply than Jain's index.
- **Decomposability** — Theil splits into within-group and between-group inequality, which is useful when you have natural sub-populations (e.g. dense vs sparse regions in [[post-disaster-mec]]).

## Theil vs Jain

| Property | Jain ($f_n$) | Theil ($T$) |
|---|---|---|
| Range | $[1/N, 1]$, maximize | $[0, \ln N]$, minimize |
| Sensitivity to outliers | Moderate | High |
| Decomposability | No | Yes (between-group / within-group) |
| Interpretation | "what fraction of N effectively get equal share" | "entropy distance from equal distribution" |

In this wiki, [[liu-2026-jppo-en-convntm]] uses Jain's-style $f_n$, while [[peng-2025-drudm-cfg]] uses Theil. Cross-paper comparison should normalize before drawing conclusions.

## Caveats

- Theil's value depends on the **partition** — different region definitions give different numbers. Coarse partitions can hide intra-region inequality.
- Single-number summaries lose information about *which* group is under-served. For diagnostic purposes, plot the per-group share as well.
