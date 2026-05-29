---
type: concept
title: "Multi-Objective MDP (Vectorial Reward)"
tags: [drl, multi-objective, mdp, formulation]
related:
  - "[[multi-objective-reinforcement-learning]]"
  - "[[pomdp]]"
  - "[[song-2024-mol-aoi-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Multi-Objective MDP (Vectorial Reward)

A Markov Decision Process whose reward is a **vector** $\mathbf{r}_t = (r_t^1, \dots, r_t^m)$ — one component per objective — with an expected vectorial return. It is the formulation device underneath [[multi-objective-reinforcement-learning]]: instead of a scalar value function, the agent reasons about a vector of returns, and solution quality is judged by Pareto dominance.

In the wiki, [[song-2024-mol-aoi-energy]] models the AoI-vs-energy tradeoff as a two-component MOMDP (`r_t^A` for negative AoI increment, `r_t^E` for negative energy), faithfully preserving the conflict rather than pre-collapsing it with fixed weights. Contrast with the single-reward [[pomdp]]/MDP formulations used by most DRL sources in the corpus.
