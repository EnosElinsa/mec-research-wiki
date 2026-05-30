---
type: concept
title: Markov Approximation
tags: [optimization, online-algorithm, combinatorial-optimization]
related:
  - "[[dai-2024-uav-vehicular-offloading-lyapunov]]"
  - "[[lyapunov-optimization]]"
  - "[[task-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Markov Approximation

A framework for solving hard combinatorial network-optimization problems by constructing a **Markov chain over the discrete configuration space** whose stationary distribution concentrates on near-optimal configurations. A log-sum-exp (Gibbs) approximation of the original combinatorial objective yields transition rates that, when simulated, let the system converge to close-to-optimal solutions without enumerating the exponential configuration set.

## Why MEC research reaches for it

- Offloading-association and scheduling decisions are combinatorial; Markov approximation gives a principled, distributed-friendly way to search them online.
- It pairs naturally with [[lyapunov-optimization]]: Lyapunov decouples the long-term constraint into per-slot problems, and Markov approximation then solves each per-slot combinatorial subproblem.

## In this wiki

[[dai-2024-uav-vehicular-offloading-lyapunov]] uses it as the per-slot solver: after Lyapunov decoupling of the long-term UAV-energy constraint, it constructs a Markov-chain-based search to find close-to-optimal UAV-assisted offloading strategies, with a theoretical analysis of the optimality gap.
