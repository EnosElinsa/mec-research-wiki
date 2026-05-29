---
type: concept
title: "Evolutionary Reinforcement Learning"
tags: [drl, evolutionary, hybrid, exploration]
related:
  - "[[multi-objective-reinforcement-learning]]"
  - "[[ppo]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[song-2024-mol-aoi-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Evolutionary Reinforcement Learning

Hybridizing gradient-based RL with gradient-free evolutionary operators applied **directly at the policy-network parameter level** (e.g. uniform crossover + Gaussian mutation on network weights). The motivation: gradient descent exploits locally but gets trapped in local optima, while evolutionary algorithms explore globally but are sample-inefficient in high dimensions — combining them gets the best of both.

In the wiki, [[song-2024-mol-aoi-energy]]'s MOL-AET runs an "evolutionary phase" after PPO training: crossover/mutation on policy-network parameters of each learning individual and its matched nondominated peer, refining the Pareto archive and escaping premature convergence. It is a bridge between the corpus's DRL track ([[ppo]]) and its evolutionary track ([[constrained-multi-objective-evolutionary-algorithm]]), and a methodological cousin of [[multi-objective-reinforcement-learning]].
