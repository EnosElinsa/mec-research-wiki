---
type: concept
title: Two-Timescale Optimization
tags: [optimization, online-control, resource-allocation]
related:
  - "[[sun-2025-tjcct-twotimescale-uav-mec]]"
  - "[[zhao-2026-heuristic-supervised-drl]]"
  - "[[heuristic-supervised-drl]]"
  - "[[uav-trajectory-control]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[tian-2026-coded-cache-repair]]"
created: 2026-05-31
updated: 2026-07-13
---

# Two-Timescale Optimization

A decomposition that splits a coupled control problem into decisions that operate on **different time scales**: fast (short-timescale) decisions that react slot-by-slot, and slow (long-timescale) decisions that change less frequently. The slow variables are optimized over a horizon while the fast variables are solved repeatedly within each long slot, exploiting the fact that some quantities (e.g. UAV position) evolve more slowly or are more costly to change than others (e.g. per-slot resource pricing and offloading association).

## Why MEC research reaches for it

- It matches the natural dynamics of aerial MEC: trajectory control is a slow, energy-coupled decision, while computing-resource allocation and offloading association must respond to fast task arrivals.
- Decoupling the scales keeps each subproblem tractable (often convex or a matching) and supports stability/complexity proofs over the long horizon.

## In this wiki

[[zhao-2026-heuristic-supervised-drl]] uses a two-timescale stochastic-approximation view for [[heuristic-supervised-drl]]: the supervised bridge updates on the fast timescale while the DRL/MARL policy evolves on the slow timescale.

[[sun-2025-tjcct-twotimescale-uav-mec]] (TJCCT) is the anchor: in the **short timescale** it runs a price-incentive model for on-demand computing-resource allocation plus a [[matching-theory-for-resource-allocation|matching]]-mechanism for computation offloading, and in the **long timescale** it runs a convex-optimization method for [[uav-trajectory-control|UAV trajectory control]] — with stability and polynomial complexity proved for the combined scheme. Contrast with the single-timescale [[lyapunov-optimization|drift-plus-penalty]] online approaches elsewhere in the corpus.

[[tian-2026-coded-cache-repair]] reverses the common mobility/resource split: coding and cache placement are slow decisions, while matching and UAV trajectory actions react on the fast timescale.
