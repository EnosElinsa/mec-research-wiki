---
type: concept
title: "Potential Game"
tags: [game-theory, equilibrium, distributed-optimization]
related:
  - "[[nash-equilibrium]]"
  - "[[stackelberg-game]]"
  - "[[stochastic-game]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[chen-2024-ulse-game]]"
created: 2026-05-29
updated: 2026-05-29
---

# Potential Game

A non-cooperative game whose players' incentive changes are all captured by a single global **potential function** $\Phi$: whenever a player unilaterally changes strategy, the change in its own payoff equals (or has the same sign as) the change in $\Phi$. This structure guarantees the **finite improvement property (FIP)** — any sequence of self-interested improving moves terminates — and therefore the existence of at least one pure-strategy [[nash-equilibrium]].

Potential games are attractive for distributed MEC because best-response dynamics provably converge without central coordination. In the wiki, [[chen-2024-ulse-game]] proves its LUTO-Game (multi-user offloading over UAV/LEO resources) is a potential game with potential function = total system cost, so its distributed JULTO algorithm converges to an NE in a few iterations. Contrast with the leader-follower [[stackelberg-game]] and the multi-state [[stochastic-game]]; efficiency of the resulting equilibrium is measured by an [[equilibrium-efficiency-metric|price of anarchy]].
