---
type: concept
title: "Elastic Task Scheduling"
tags: [scheduling, fault-tolerance, edge-ai, uav-swarm]
related:
  - "[[collaborative-dl-inference]]"
  - "[[task-migration]]"
  - "[[load-balancing-uav-mec]]"
  - "[[sun-2024-asap-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Elastic Task Scheduling

Online rescheduling of distributed work when compute nodes **drop out or rejoin** — re-partitioning and rebalancing the workload so collaborative computing keeps running through churn. It detects connection-status changes (e.g. via heartbeats), updates the active node set and baseline latencies, and re-runs the partition/balance step.

In the wiki, [[sun-2024-asap-uav-swarm]]'s ES algorithm (part of its E2S scheduler) re-runs ECLB+ICLB online when a cluster head or member fails or recovers; rescheduling after a cluster-head cutoff stays under 1 s, and latency returns to baseline after recovery. It provides fault tolerance for [[collaborative-dl-inference]] in volatile swarm networks, and parallels the dynamic-reallocation spirit of [[task-migration]] / [[load-balancing-uav-mec]].
