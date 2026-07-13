---
type: concept
title: "Multi-Armed Bandit Objective Weighting"
tags: [multi-objective, reinforcement-learning, multi-armed-bandit, scalarization]
related:
  - "[[huang-2026-uav-friendly-jamming-transsac]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[soft-actor-critic]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Armed Bandit Objective Weighting

Multi-armed bandit objective weighting treats candidate scalarization weights as arms and learns which trade-off produces the strongest return. It allows a multi-objective controller to adapt its weighted reward rather than fixing one secrecy, energy, delay, or quality preference for every training stage.

In [[huang-2026-uav-friendly-jamming-transsac]], epsilon-greedy arm selection and sample-average updates choose the secrecy-rate and UAV-energy weights used by a transformer-enhanced [[soft-actor-critic]] policy. The method remains a linear scalarization and does not establish full Pareto-front coverage.
