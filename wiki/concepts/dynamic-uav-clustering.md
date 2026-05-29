---
type: concept
title: "Dynamic UAV Clustering"
tags: [uav-swarm, clustering, load-balancing, scheduling]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[load-balancing-uav-mec]]"
  - "[[intra-swarm-task-delegation]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Dynamic UAV Clustering

Allowing UAVs to **re-form their swarm membership over time** — e.g. follower UAVs switching which leader they follow — rather than holding fixed clusters, so the swarm can rebalance computing load as task demand and application placement shift across space and time. Fixed clustering leaves some swarms overloaded while others idle; dynamic clustering migrates followers toward where work is.

In the wiki, [[li-2025-stochastic-game-uav-swarm]] makes this its headline novelty (the "Dynamic Clustering Stochastic Game"), letting followers re-associate to leaders each slot; its figures show leader energy traces fluctuating as followers switch. It is a swarm-membership form of [[load-balancing-uav-mec]] within a [[hierarchical-aerial-mec]] (leader/follower) structure, and pairs with [[intra-swarm-task-delegation]].
