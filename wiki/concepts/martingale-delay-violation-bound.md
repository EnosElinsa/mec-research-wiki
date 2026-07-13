---
type: concept
title: "Martingale Delay-Violation Bound"
tags: [queueing, martingale, delay-violation-probability, multi-hop-network]
related:
  - "[[guo-2026-spatiotemporal-information-quality-ugrnet]]"
  - "[[queueing-theory]]"
  - "[[stochastic-network-calculus]]"
  - "[[spatiotemporal-information-quality]]"
  - "[[uav-mobile-relaying]]"
created: 2026-07-14
updated: 2026-07-14
---

# Martingale Delay-Violation Bound

An exponential upper bound on the probability that queueing delay exceeds a threshold, constructed from supermartingales for finite-state Markov arrival and service processes. In a heterogeneous tandem route, per-hop decay terms can be combined after minimizing over allocations of the end-to-end delay threshold rather than keeping only the bottleneck hop or assuming homogeneous service.

[[guo-2026-spatiotemporal-information-quality-ugrnet]] uses critical arrival/service decay parameters for each robot-to-robot, robot-to-UAV, and UAV-to-command-center queue. Its joint decay product is a harmonic aggregation of per-hop decay products, and the resulting bound supplies the temporal term in [[spatiotemporal-information-quality]].

The result is an analytical bound under stationary finite-state Markov models, queue stability, independent arrival and service processes, independent service across hops, and simplified propagation-loss assumptions. It is not a worst-case guarantee for arbitrary traffic or correlated links, and the source gives no approximation-error bound for its MCMC fitting or model mismatch.
