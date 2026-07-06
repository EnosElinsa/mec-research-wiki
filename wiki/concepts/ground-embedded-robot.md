---
type: concept
title: "Ground Embedded Robot (GER)"
tags: [post-disaster-mec, low-altitude-economy, task-offloading, ground-robot]
related:
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
  - "[[post-disaster-mec]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-07
updated: 2026-07-07
---

# Ground Embedded Robot (GER)

A ground-side robotic compute node used in low-altitude rescue MEC. In [[tang-2026-hg-maddpg-uav-rescue]], GERs are deployed inside the rescue area and provide computing support to UAVs that collect object-detection tasks while exploring. The UAV can process locally, offload to a selected GER over a U2G link, or use higher-altitude airship support when GER resources are insufficient.

The concept is narrower than a generic edge server: the GER is mobile/robotic ground infrastructure embedded in the disaster scene, and its current compute state affects UAV task-assignment and exploration policy. It connects [[post-disaster-mec]] to [[low-altitude-intelligent-network]] control because UAV exploration, offloading, and energy queues are optimized together.
