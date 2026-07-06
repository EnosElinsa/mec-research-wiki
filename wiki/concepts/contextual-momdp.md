---
type: concept
title: "Contextual Multi-Objective MDP"
tags: [drl, multi-objective, context, pareto]
related:
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[energy-latency-tradeoff]]"
  - "[[yang-2025-generalizable-pareto-offloading]]"
created: 2026-07-07
updated: 2026-07-07
---

# Contextual Multi-Objective MDP

A contextual multi-objective MDP augments the usual state, action, transition, and vector-reward structure with a context variable that changes how the policy should behave. In MEC offloading, the context can include user preference weights, the number of edge servers, and server CPU frequencies.

The benefit is generalization: a single policy can be conditioned on the context instead of training one policy per preference vector or one policy per deployment. [[yang-2025-generalizable-pareto-offloading]] uses this framing for delay-vs-energy MEC offloading, with a Discrete-SAC policy that takes both preference and server-configuration context as inputs and approximates the Pareto frontier across them.
