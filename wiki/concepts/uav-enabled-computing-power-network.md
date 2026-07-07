---
type: concept
title: "UAV-Enabled Computing Power Network"
tags: [computing-power-network, uav, stochastic-geometry, task-offloading, low-altitude-economy]
related:
  - "[[deng-2026-uav-cpn-energy]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[task-offloading]]"
  - "[[uav-mobile-relaying]]"
  - "[[low-altitude-intelligent-network]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV-Enabled Computing Power Network

A UAV-enabled Computing Power Network uses a UAV relay to connect users in a request zone to computing nodes distributed over a wider service zone, mitigating the MEC "island effect" where nearby compute is insufficient while farther compute remains available. In [[deng-2026-uav-cpn-energy]], the computing nodes are modeled as a Poisson point process and task-completion probability is derived from the probability that at least one node satisfies both communication and computation latency constraints.

The concept is close to [[uav-mobile-relaying]], but the service being relayed is computing power rather than only data throughput. Its main corpus link is [[stochastic-geometry-network-analysis]], which gives a distribution-level completion-probability expression before per-task scheduling or DRL control enters.
