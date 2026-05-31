---
type: concept
title: "Trust Region Policy Optimization (TRPO / HATRPO)"
tags: [drl, policy-gradient, multi-agent, monotonic-improvement]
related:
  - "[[ppo]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[mappo]]"
  - "[[beta-policy-drl]]"
  - "[[liu-2024-hatrpo-ucb-cb]]"
created: 2026-06-01
updated: 2026-06-01
---

# Trust Region Policy Optimization (TRPO / HATRPO)

A policy-gradient method that constrains each policy update to stay within a **trust region** — measured by the KL-divergence between the new and old policies — so that the update has a **monotonic improvement guarantee** rather than the unbounded steps that can collapse vanilla policy gradient. [[ppo|PPO]] is the better-known first-order approximation of the same idea (clipped surrogate instead of an explicit KL constraint); TRPO keeps the constraint explicit and solves the constrained update via a surrogate objective plus a backtracking line search.

**Heterogeneous-Agent TRPO (HATRPO)** lifts TRPO to the multi-agent setting ([[heterogeneous-agent-rl]]): agents update their policies **sequentially**, and the per-agent surrogate plus KL-penalty terms compose into a joint monotonic-improvement bound for the whole team — without requiring the agents to share a homogeneous policy. The update order can be permuted each iteration.

## In this wiki

- [[liu-2024-hatrpo-ucb-cb]] takes conventional HATRPO as its backbone and proposes **HATRPO-UCB** for UAV collaborative beamforming, adding observation enhancement, an agent-specific global state for the critic, and a [[beta-policy-drl|Beta-distribution]] actor (in place of the Gaussian) to match the finite action ranges. It is the corpus's trust-region MADRL anchor, sitting alongside the [[mappo|MAPPO]] / [[ppo|PPO]] family.
