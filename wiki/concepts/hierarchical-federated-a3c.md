---
type: concept
title: "Hierarchical Federated A3C"
tags: [federated-learning, a3c, multi-agent-learning, uav-relay, resource-allocation]
related:
  - "[[ron-2026-federated-a3c-uav-energy]]"
  - "[[hierarchical-federated-drl]]"
  - "[[federated-reinforcement-learning]]"
  - "[[federated-learning]]"
created: 2026-07-13
updated: 2026-07-13
---

# Hierarchical Federated A3C

Hierarchical federated A3C distributes actor-critic agents at end devices and aggregates their parameters through more than one network tier. In [[ron-2026-federated-a3c-uav-energy]], ground users train local actor/critic models for power, UAV position, bandwidth, and relay association; each UAV averages a sub-global model, and a terrestrial base station averages those UAV models globally.

This is a specific [[federated-reinforcement-learning]] architecture. It differs from the broader [[hierarchical-federated-drl]] corpus example, whose hierarchy spans terrestrial and non-terrestrial offloading/incentive controllers: here the UAVs primarily relay data and provide an intermediate model-aggregation tier for A3C resource control.
