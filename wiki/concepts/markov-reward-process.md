---
type: concept
title: "Markov Reward Process (MRP)"
tags: [drl, mdp, formulation, stochastic-process]
related:
  - "[[pomdp]]"
  - "[[soft-actor-critic]]"
  - "[[dynamic-qos-constraints]]"
  - "[[niazmand-2025-jopa-dnn-pruning-iiot]]"
created: 2026-05-31
updated: 2026-05-31
---

# Markov Reward Process (MRP)

A generalization of a Markov decision process (MDP) in which the **state transitions are characterized independently of the actions** taken by the agent — the dynamics are driven by an exogenous network/environment process, and the agent's policy affects the **reward** rather than the transition kernel.

This framing is convenient when the underlying network-state evolution (channel gains, task arrivals, criticality levels) is governed by external randomness while the decision variables (offloading, pruning, resource allocation) shape the per-step reward and constraint satisfaction. It lets a DRL agent learn a stationary policy without modeling action-dependent transitions.

In the wiki, [[niazmand-2025-jopa-dnn-pruning-iiot]] transforms a stochastic IIoT optimization into an MRP with per-time-slot delay/accuracy constraints, then solves it with a hybrid-action [[soft-actor-critic|SAC]] agent. Contrast with the action-dependent [[pomdp]] formulations used elsewhere in the corpus.
