---
type: concept
title: "Stochastic Network Calculus"
tags: [network-calculus, latency-bound, qos, uav-swarm, traffic-scheduling]
related:
  - "[[digital-twin]]"
  - "[[communication-constrained-marl]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[li-2025-dt-uav-swarm-resource-management]]"
created: 2026-07-06
updated: 2026-07-06
---

# Stochastic Network Calculus

**Stochastic network calculus (SNC)** is an analytical framework for deriving probabilistic backlog and delay bounds for traffic flows traversing uncertain service processes. Instead of simulating every route realization, it characterizes arrivals and service with stochastic envelopes or moment-generating-function-style bounds, then estimates whether a flow can satisfy an end-to-end latency target.

## In this wiki

- [[li-2025-dt-uav-swarm-resource-management]] uses SNC inside a digital-twin layer for UAV swarms. The virtual swarm pre-schedules sensing/service traffic paths and assesses theoretical end-to-end delay bounds before admitting UAVs or changing the physical multi-hop route.

## Why it matters

For UAV-swarm MEC, SNC provides a conservative admission/scheduling check between purely learned control and purely empirical simulation. The same paper also flags the limitation: in large, time-varying multi-hop UAV networks, SNC delay estimates become less precise and need refined modeling.
