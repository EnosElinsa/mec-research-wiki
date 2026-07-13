---
type: concept
title: "Traffic-Aware Asynchronous UAV Control"
tags: [multi-uav, asynchronous-control, traffic-aware, scheduling, relaying]
related:
  - "[[spatial-temporal-graph-attention-traffic-clustering]]"
  - "[[graph-neural-network]]"
  - "[[ppo]]"
  - "[[uav-trajectory-control]]"
  - "[[chen-2026-traffic-aware-asynchronous-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Traffic-Aware Asynchronous UAV Control

A multi-UAV control pattern where each UAV independently allocates time among motion, data collection, inter-UAV handoff, and downlink delivery according to traffic buffers and current topology. Asynchrony lets different UAVs serve different pipeline stages within the same global slot.

[[chen-2026-traffic-aware-asynchronous-control]] represents UAVs and traffic clusters as a dynamic graph, uses a GNN plus GRU to encode changing relationships, and applies PPO to trajectories, access schedules, relay links, and per-mode durations.

The method is a learned heuristic. Empirical training convergence and throughput gains do not establish convergence to the max-min throughput optimum.
