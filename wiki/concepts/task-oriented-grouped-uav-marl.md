---
type: concept
title: "Task-Oriented Grouped UAV MARL"
tags: [marl, uav-swarm, role-grouping, relay, emergency-network]
related:
  - "[[xu-2026-mrlmn-llm-multihop]]"
  - "[[multi-hop-uav-emergency-networking]]"
  - "[[llm-guided-marl-policy-distillation]]"
  - "[[connectivity-preserving-uav-behavioral-loss]]"
  - "[[autonomous-uav-swarms]]"
  - "[[collaborative-uav-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Task-Oriented Grouped UAV MARL

Task-oriented grouped UAV MARL partitions swarm agents by expected network role and assigns group-dependent reward emphasis or constraints. In emergency relaying, UAVs nearer surviving base stations can prioritize backhaul continuity while farther UAVs prioritize direct user service, reducing role ambiguity without requiring a command hierarchy.

[[xu-2026-mrlmn-llm-multihop]] forms quantile groups from each UAV's initial distance to the nearest base station and combines team utility with direct-service and relayed-rate rewards. The grouping is static in the parsed method, so it may become stale as UAVs, users, and connectivity move; the source does not evaluate dynamic regrouping or prove that distance is the best role descriptor.
