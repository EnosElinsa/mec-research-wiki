---
type: concept
title: "Heterogeneous-Agent Reinforcement Learning"
tags: [drl, multi-agent, markov-game]
related:
  - "[[you-2025-uncertain-maritime-hasac]]"
  - "[[masac]]"
  - "[[stochastic-game]]"
  - "[[centralized-training-decentralized-execution]]"
created: 2026-05-29
updated: 2026-05-29
---

# Heterogeneous-Agent Reinforcement Learning

A multi-agent RL setting where agents differ in action spaces, capabilities, or resources, so they cannot share a single homogeneous policy. Heterogeneous-agent algorithms (e.g. heterogeneous-agent soft actor-critic) typically update agents' networks **sequentially** with guarantees that monotonically improve a joint objective, addressing the non-stationarity of concurrent learning.

In [[you-2025-uncertain-maritime-hasac]], AAVs and vessels have heterogeneous actions/resources, so the per-slot problem (after Lyapunov decomposition) is modeled as a Markov game ([[stochastic-game]]) and solved by a heterogeneous-agent soft actor-critic that sequentially updates each agent's neural networks. It generalizes homogeneous multi-agent methods like [[masac]].
