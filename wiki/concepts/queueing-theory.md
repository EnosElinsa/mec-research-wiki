---
type: concept
title: "Queueing Theory"
tags: [analysis, delay, performance-modeling, mec]
related:
  - "[[stochastic-geometry-network-analysis]]"
  - "[[lyapunov-optimization]]"
  - "[[age-of-information]]"
  - "[[zhang-2020-response-delay-uav-swarm]]"
created: 2026-05-31
updated: 2026-05-31
---

# Queueing Theory

**Queueing theory** models systems where jobs (tasks, packets) arrive, wait in a queue, and are served by one or more servers, yielding closed-form expressions for waiting time, queue length, and end-to-end delay as functions of arrival rate, service rate, and scheduling discipline. In MEC it is the natural tool for analyzing **response/computation delay** at edge servers, especially when combined with a spatial model of where the offloading nodes are.

## In this wiki

- [[zhang-2020-response-delay-uav-swarm]] combines queueing theory with [[stochastic-geometry-network-analysis]] to derive the closed-form **optimal response delay** of a MEC-enabled UAV swarm over four delay indicators, modeling VM-multiplexing degradation as an inflated expected service time. It complements the drift-plus-penalty queue-stability view of [[lyapunov-optimization]] and the freshness view of [[age-of-information]].
