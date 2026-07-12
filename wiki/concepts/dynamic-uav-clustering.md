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
  - "[[uav-cluster-authentication]]"
  - "[[gong-2026-lp2-casku-uav-clusters]]"
  - "[[guang-2026-hiswta-mcs]]"
created: 2026-05-29
updated: 2026-07-13
---

# Dynamic UAV Clustering

Allowing UAVs to **re-form their swarm membership over time** — e.g. follower UAVs switching which leader they follow — rather than holding fixed clusters, so the swarm can rebalance computing load as task demand and application placement shift across space and time. Fixed clustering leaves some swarms overloaded while others idle; dynamic clustering migrates followers toward where work is.

In the wiki, [[li-2025-stochastic-game-uav-swarm]] makes this its headline novelty (the "Dynamic Clustering Stochastic Game"), letting followers re-associate to leaders each slot; its figures show leader energy traces fluctuating as followers switch. It is a swarm-membership form of [[load-balancing-uav-mec]] within a [[hierarchical-aerial-mec]] (leader/follower) structure, and pairs with [[intra-swarm-task-delegation]].

[[gong-2026-lp2-casku-uav-clusters]] adds the security version of the same membership problem: cluster heads must admit new UAVs, authenticate existing UAVs moving across clusters, and update cluster session keys while preserving anonymity, unlinkability, and forward/backward secrecy.

[[guang-2026-hiswta-mcs]] uses dynamic clustering for sensing-information flow rather than MEC workload placement. Residual energy, consumption, distance, connectivity, and communication quality determine cluster-head selection after task cycles; fuzzy link conditions can trigger head replacement, and an inter-head route carries fused sensing information.
