---
type: concept
title: Informer for Trajectory / Time-Series Prediction
tags: [transformer, time-series, attention, prediction]
related:
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-05-28
updated: 2026-05-28
---

# Informer for Trajectory / Time-Series Prediction

Informer (Zhou et al., AAAI 2021) is a Transformer variant designed for *long-sequence* time-series forecasting. Two architectural changes vs vanilla Transformer:

- **ProbSparse self-attention** — only the queries with top-$\log L$ KL-divergence vs uniform attention are computed; the rest are filled with the mean. Cuts attention cost from $O(L^2)$ to $O(L \log L)$.
- **Distilling encoder** — alternates self-attention with a 1-D convolutional pooling that halves the sequence length, reducing memory across layers.

Together these let Informer scale to $L = 720$+ sequence lengths on commodity GPUs.

## Why MEC papers use it

For anything where the controller's quality depends on **future context** rather than current observation alone — vehicular trajectories, UAV swarm positions, queue arrival rates — Informer offers the same expressive power as Transformer at meaningfully lower compute. In [[zhang-2025-mcma-task-migration]], the centralized prediction module would be untenable at $O(H^2)$ for $H = 24$ h history × thousands of vehicles; the ProbSparse trick brings it back into reach.

## When *not* to use Informer

- Short horizons ($H < 100$) — the constants in $O(H \log H)$ may make a vanilla Transformer or even an LSTM faster wall-clock.
- Strongly periodic signals where simple Fourier features outperform learned attention.
- Tabular / non-sequential predictions.
