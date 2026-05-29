---
type: concept
title: "Multi-Objective Reinforcement Learning (MORL)"
tags: [drl, multi-objective, pareto]
related:
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[evolutionary-reinforcement-learning]]"
  - "[[ppo]]"
  - "[[dynamic-constrained-multi-objective-optimization]]"
  - "[[song-2024-mol-aoi-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Multi-Objective Reinforcement Learning (MORL)

RL that optimizes a **vector** of objectives rather than a single scalar reward, producing a set of Pareto-nondominated policies so a decision-maker can later pick the policy matching a current preference. This avoids the usual fixed-weight linear scalarization, which collapses conflicting objectives into one number and breaks when preferences shift.

Common scaffolding: define a [[multi-objective-mdp-vectorial-reward|multi-objective MDP]], decompose the preference space into weight vectors, train one policy per weight (often with [[ppo]] or value-based learners), and maintain a nondominated archive across them.

In the wiki, [[song-2024-mol-aoi-energy]]'s **MOL-AET** is the anchor: it trains multi-objective PPO individuals over uniformly spread preference weights and then refines the Pareto set with [[evolutionary-reinforcement-learning|evolutionary operators]]. MORL is the learning-based counterpart to the evolutionary [[dynamic-constrained-multi-objective-optimization]] / CMOEA family used across the Peng/Huang lineage.
