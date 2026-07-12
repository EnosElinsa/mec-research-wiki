---
type: concept
title: "Generalized Assignment Problem"
tags: [optimization, combinatorial, np-hard, assignment, load-balancing]
related:
  - "[[matching-theory-for-resource-allocation]]"
  - "[[load-balancing-uav-mec]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[yang-2020-loadbalance-multiuav-iot]]"
  - "[[wu-2026-parallel-cooperative-charging]]"
  - "[[parallel-cooperative-uav-charging]]"
created: 2026-05-31
updated: 2026-07-12
---

# Generalized Assignment Problem

The **generalized assignment problem (GAP)** assigns a set of tasks to a set of agents, where each agent has a capacity (budget) and each task consumes a different amount of that capacity and yields a different profit per agent. The goal is to maximize total profit subject to each task being assigned to exactly one agent and no agent exceeding its capacity. GAP is **NP-hard** and generalizes the (balanced) assignment problem by allowing task-dependent, agent-dependent sizes.

## In this wiki

- [[yang-2020-loadbalance-multiuav-iot]] models IoT-node-to-UAV association as a GAP — UAVs are capacity-limited agents, IoT nodes are tasks with distance/traffic-dependent profit — and solves it with a near-optimal LP-relaxation + bipartite-graph + deterministic-rounding approximation to balance UAV load. It is a capacity-aware cousin of [[matching-theory-for-resource-allocation]] used for [[load-balancing-uav-mec]].
- [[wu-2026-parallel-cooperative-charging]] assigns each UAV to one station/facility, but its [[parallel-cooperative-uav-charging]] objective is not separable by UAV: parallel completion time and a shared station tariff create group costs, so the solution combines set-cover grouping with uniform-machine scheduling rather than using GAP directly.
