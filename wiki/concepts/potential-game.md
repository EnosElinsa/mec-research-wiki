---
type: concept
title: "Potential Game"
tags: [game-theory, equilibrium, distributed-optimization]
related:
  - "[[du-2026-hierarchical-coalition-deployment]]"
  - "[[nash-equilibrium]]"
  - "[[stackelberg-game]]"
  - "[[stochastic-game]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[chen-2024-ulse-game]]"
  - "[[li-2026-cdto-inland-waterways]]"
  - "[[li-2026-jscfg-uav-grouping]]"
  - "[[joint-switch-coalition-formation-game]]"
  - "[[ma-2026-game-ibs-deployment]]"
  - "[[qi-2026-ocma-ddqn-data-collection]]"
created: 2026-05-29
updated: 2026-07-14
---

# Potential Game

A non-cooperative game whose players' incentive changes are all captured by a single global **potential function** $\Phi$: whenever a player unilaterally changes strategy, the change in its own payoff equals (or has the same sign as) the change in $\Phi$. In a finite-strategy potential game, this structure gives the **finite improvement property (FIP)**: any sequence of unilateral strict improvements terminates at a pure-strategy [[nash-equilibrium]]. Continuous-strategy games require additional compactness, continuity, or response-dynamics conditions; a potential function alone does not provide the same finite-step guarantee.

Potential games are attractive for distributed MEC because finite best-response or better-response dynamics can converge without central coordination. In the wiki, [[chen-2024-ulse-game]] proves its LUTO-Game (multi-user offloading over UAV/LEO resources) is a potential game with potential function = total system cost, so its distributed JULTO algorithm converges to an NE in a few iterations. [[li-2026-cdto-inland-waterways]] uses an exact-potential-game formulation inside cluster-based distributed task offloading for inland-waterway USVs, then couples it with graph-based multi-agent learning for D2D link decisions. Contrast with the leader-follower [[stackelberg-game]] and the multi-state [[stochastic-game]]; efficiency of the resulting equilibrium is measured by an [[equilibrium-efficiency-metric|price of anarchy]].

[[ma-2026-game-ibs-deployment]] claims an exact potential game for multiple anti-UAV interference base stations, then evaluates discretized deployments against a learned UAV trajectory response. Its parse contains potential-sign, finite-versus-continuous strategy, and equilibrium/global-optimum inconsistencies, so the claimed structure should not be read as proof that the exhaustive-plus-SAC solution is unique or globally optimal.
