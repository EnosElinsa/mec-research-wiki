---
type: concept
title: "Price of Anarchy (PoA)"
tags: [game-theory, metric, equilibrium, optimization]
related:
  - "[[nash-equilibrium]]"
  - "[[potential-game]]"
  - "[[game-theoretic-offloading-formulations]]"
  - "[[chen-2022-qoe-game-end-edge-cloud]]"
created: 2026-06-02
updated: 2026-06-02
---

# Price of Anarchy (PoA)

A worst-case efficiency metric for game-theoretic systems: the ratio between the objective value at the **worst Nash Equilibrium** and the value of the **centralized optimal** solution. It quantifies how much performance can be lost when self-interested players settle into an equilibrium instead of being centrally coordinated. A PoA close to 1 means selfish equilibria are nearly as good as the optimum; a PoA far from 1 means decentralization is costly.

Why decentralized MEC offloading papers care: recasting offloading as a game (so each device optimizes its own delay/energy/QoE) buys distributed, low-complexity solutions and a [[nash-equilibrium]] existence guarantee — but without a PoA bound there is no promise the equilibrium is any good. Bounding the PoA turns "it converges" into "it converges to something provably near-optimal in the worst case."

## In this wiki

[[chen-2022-qoe-game-end-edge-cloud]] defines the PoA as the ratio of the worst-NE sum-QoE to the centralized-optimal sum-QoE and derives a **lower bound** on it for its end-edge-cloud offloading [[potential-game]] (MUTO-Game), alongside an iteration-count convergence bound. The closely-related UAV-LEO offloading game [[chen-2024-ulse-game]] uses the same worst-NE-vs-optimum framing as its [[equilibrium-efficiency-metric]]. PoA is one of the comparison axes in [[game-theoretic-offloading-formulations]].
