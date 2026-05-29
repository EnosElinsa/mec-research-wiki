---
type: concept
title: "Bargaining Game"
tags: [game-theory, incentive-mechanism, pricing]
related:
  - "[[sun-2023-bargain-match-vec]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[stackelberg-game]]"
  - "[[nash-equilibrium]]"
created: 2026-05-29
updated: 2026-05-29
---

# Bargaining Game

A cooperative game-theoretic model in which two (or more) parties negotiate how to split a surplus, with a solution concept (e.g. the Nash bargaining solution) that is Pareto-efficient and satisfies fairness/axiomatic properties. In MEC it is used to set resource prices and trading terms between resource providers and consumers.

In the wiki, [[sun-2023-bargain-match-vec]] uses a bargaining-based incentive model for intra-server resource allocation (paired with a matching method for inter-server offloading), and [[wang-2024-twotier-satellite-marine]] models the MASS↔LEO-satellite offloading interaction as a bargaining game (paired with a [[stackelberg-game]] for the AUV↔MASS tier). Bargaining contrasts with the leader-follower [[stackelberg-game]] and the symmetric-competition [[potential-game]].
