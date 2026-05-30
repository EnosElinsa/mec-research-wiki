---
type: concept
title: "Cross-Entropy Method"
tags: [optimization, metaheuristic, stochastic, combinatorial]
related:
  - "[[monotonic-optimization]]"
  - "[[particle-swarm-optimization]]"
  - "[[differential-evolution]]"
  - "[[li-2023-secure-marine-iot-jamming]]"
created: 2026-05-31
updated: 2026-05-31
---

# Cross-Entropy Method

The **cross-entropy (CE) method** is a stochastic optimization metaheuristic that iteratively samples candidate solutions from a parameterized distribution, keeps the best-performing "elite" samples, and updates the distribution parameters (by minimizing the cross-entropy / KL divergence toward the elite set) so the next round concentrates around promising regions. It suits combinatorial and rare-event problems where gradients are unavailable.

## In this wiki

- [[li-2023-secure-marine-iot-jamming]] uses a **Code-bAsed croSs-Entropy (CASE)** algorithm to search the top-problem (USV positions) in its secure marine-offloading design, calling a [[monotonic-optimization]]-based PAS algorithm to solve the bottom problem at each sampled configuration. It joins the wiki's metaheuristic toolbox alongside [[particle-swarm-optimization]] and [[differential-evolution]].
