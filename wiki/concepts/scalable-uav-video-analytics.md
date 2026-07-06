---
type: concept
title: "Scalable UAV Video Analytics"
tags: [video-analytics, uav-swarm, distributed-inference, computation-offloading]
related:
  - "[[wang-2026-scalable-multiuav-analytics]]"
  - "[[video-analytics-offloading]]"
  - "[[collaborative-dl-inference]]"
  - "[[interdependent-tasks-dag]]"
  - "[[mappo]]"
created: 2026-07-07
updated: 2026-07-07
---

# Scalable UAV Video Analytics

A UAV-swarm video-analytics pattern where the control architecture changes with swarm size. [[wang-2026-scalable-multiuav-analytics]] uses centralized deployment and task scheduling for small swarms with BS support, but switches to a distributed MAPPO-plus-DAG-partition controller for larger swarms or weaker BS connectivity.

The workload differs from generic [[video-analytics-offloading]] because each ROI classification is represented as a classifier-level [[interdependent-tasks-dag|DAG]] and can be partially processed on one UAV before being handed to another UAV. This makes it a bridge between [[video-analytics-offloading]] and [[collaborative-dl-inference]].
