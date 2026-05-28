---
type: methodology
title: DRL simulation methodology for UAV-MEC under POMDP formulation
tags: [drl, simulation, methodology, pomdp]
related:
  - "[[pomdp]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[en-convntm-beats-baselines]]"
created: 2026-05-28
updated: 2026-05-28
---

# DRL simulation methodology for UAV-MEC under POMDP formulation

The protocol used by [[liu-2026-jppo-en-convntm]] — generally applicable to any DRL-based UAV-MEC paper this wiki may add later.

## Why a POMDP

The agent (joint UAV controller) doesn't see the full system state — it sees a 3-channel grid observation $\mathbf{o}_n$ summarizing positions, energies, and visit-history. The hidden state includes future device positions (governed by a [[gauss-markov-mobility-model|Gauss-Markov process]]) and unobserved per-device queue depths. This is a textbook [[pomdp]].

## Observation construction

Three channels of size matching a discretized world grid:

1. **Channel 1:** per-cell device count, plus per-cell number of total visits by any UAV.
2. **Channel 2:** per-cell UAV remaining energy (at occupied cells); $-1$ at charging stations.
3. **Channel 3:** per-cell visit history $\iota_{d,n}$.

This grid lends itself naturally to a convolutional encoder, which is why the front-end is convolutional (and why [[en-convntm]] is preferred over a non-convolutional NTM).

## Reward shaping

$r_n = \Omega_n - p_{u,n}$, where the penalty $p_{u,n}$ activates when:

- two UAVs come within a danger distance
- a UAV approaches an obstacle
- a UAV's battery drops near depletion

Penalty terms are essential — without them the policy will exploit the unconstrained $\Omega$ landscape to camp dangerously close to dense clusters or hover unsafely close to obstacles.

## Training and evaluation procedure

- **Episodes:** 500 time steps each.
- **Iterations:** 3000, with parallel rollouts of size $\tilde{N} = 8$.
- **Update mini-batch:** segments of length $K = 5$ to break NTM-induced sample correlation.
- **Selection:** the iteration whose model has the highest $\Omega_n$ at the final time step is kept for evaluation.
- **Reporting:** box-plots over multiple simulation runs (with horizontal-axis jitter to avoid overlap of adjacent boxes).

## Hardware

Ubuntu 20.04 with 2× NVIDIA RTX 4090, PyTorch 2.1.0, Matplotlib 3.8.4 for the simulation arena.
