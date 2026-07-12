---
type: concept
title: "Hierarchical UAV Swarm"
tags: [uav-swarm, hierarchy, head-uav, relay, data-collection]
related:
  - "[[jia-2026-hierarchical-uav-swarms]]"
  - "[[autonomous-uav-swarms]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[uav-data-collection]]"
  - "[[uav-mobile-relaying]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[guang-2026-hiswta-mcs]]"
created: 2026-07-13
updated: 2026-07-13
---

# Hierarchical UAV Swarm

A hierarchical UAV swarm assigns persistent coordination roles inside one fleet. A head UAV can act as an aerial base station or collection sink, while subordinate or tail UAVs move through the service area, gather data, and relay it upward. This functional split supports cooperative large-area coverage and can reduce data delay, while introducing fleet-allocation, bottleneck, and completion-time coupling at the head.

[[jia-2026-hierarchical-uav-swarms]] uses stationary head UAVs and successive-hover-and-fly tail UAVs. Deployment determines how many tail UAVs each head receives and which users they serve; route and power optimization then balances head/tail energy, user energy, and two-hop delay.

[[guang-2026-hiswta-mcs]] makes the hierarchy dynamic: sensing UAVs join clusters, members report to heads, heads fuse and exchange information, and weak heads can be replaced. It couples that communication hierarchy with approximate Shapley-value task allocation to reduce energy imbalance across repeated sensing cycles.

This is an intra-swarm communication hierarchy, not automatically a [[hierarchical-aerial-mec]] stack. The latter places computation across different aerial tiers such as UAVs and HAPS, whereas a hierarchical swarm may perform collection and relaying without any MEC execution model.
