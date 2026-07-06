---
type: concept
title: "Second-Order Cone Programming"
tags: [optimization, convex-optimization, trajectory-planning]
related:
  - "[[linear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[ji-2026-llm-iov-uav-offloading]]"
created: 2026-07-07
updated: 2026-07-07
---

# Second-Order Cone Programming

A convex optimization class whose constraints can include norm cones, typically written as `||Ax + b||_2 <= c^T x + d`. SOCP is useful in wireless and UAV planning when distance, coverage, collision-avoidance, or energy approximations can be written as convex norm constraints after relaxation or linearization.

In [[ji-2026-llm-iov-uav-offloading]], the multi-UAV 3D trajectory subproblem is solved as sequential SOCPs. The paper convexifies horizontal and vertical propulsion-energy terms, uses tangent-based collision-avoidance constraints, and optimizes each UAV trajectory while holding the others fixed. This gives the trajectory stage a transparent convex core before DRL/LLM/LP scheduling handles faster resource and offloading decisions.

SOCP sits next to the corpus's broader convex-decomposition tools, including [[alternating-optimization-sdr-sca]] and [[linear-programming]].
