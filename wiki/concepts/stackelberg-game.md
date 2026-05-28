---
type: concept
title: Stackelberg Game (Leader-Follower)
tags: [game-theory, mechanism-design, pricing]
related:
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Stackelberg Game (Leader-Follower)

A sequential-move game where one player (the **leader**) commits to a strategy first, and the remaining players (the **followers**) optimize their responses given the leader's commitment. The leader anticipates the followers' best-response functions when choosing.

Solved by **backward induction**: characterize $\mathbf{a}^*_{\text{follower}}(\mathbf{a}_{\text{leader}})$, substitute into the leader's payoff, then optimize the leader's action.

## Why MEC and wireless papers use it

Network operators or service providers naturally play leader: they set prices, allocations, or QoS tiers. Users / clients / UAVs play follower: they choose how much to consume given the announced terms.

- **Pricing.** Leader (e.g. base station) prices spectrum or compute; followers (UAVs / IoT devices) bid demand.
- **Resource auctioning.** Leader announces auction rules; followers bid.
- **Trust / reputation.** Leader sets the reputation function; followers shape behavior to optimize reputation.

## Equilibrium concepts

- **Stackelberg equilibrium** — the unique optimum under sequential moves. Generally Pareto-improves over Nash equilibria of the simultaneous-move game.
- **Subgame-perfect refinement** — required when followers' choices interact and the followers form a sub-game.

## In this wiki

[[wang-2025-uav-swarm-stackelberg]] is the canonical example: U2B base station as leader (sets price for spectrum access), U2U links as followers (bid power/duration). The Stackelberg layer composes with a [[matching-theory-for-resource-allocation|matching algorithm]] for the assignment side.

Multi-leader Stackelberg variants (multiple competing operators) appear in some adjacent literature but aren't yet curated in this wiki.
