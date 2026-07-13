---
type: concept
title: "Partial-Space Adaptive Play"
tags: [game-theory, potential-game, stochastic-search, uav-deployment]
related:
  - "[[du-2026-hierarchical-coalition-deployment]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
created: 2026-07-13
updated: 2026-07-13
---

# Partial-Space Adaptive Play

A stochastic finite-game update that samples only a subset of a player's alternative actions, evaluates their utilities, and selects among them with a softmax response. Restricting the evaluated action space reduces each update's cost while the inverse-temperature or learning factor controls exploration versus concentration on high-utility actions.

In [[du-2026-hierarchical-coalition-deployment]], UAV placements are the actions and total ground-user utility is the potential. The claimed best-equilibrium behavior is asymptotic and conditional on a sufficiently large learning factor and a well-defined utility for every placement; it is not a finite-time global-optimality guarantee.
