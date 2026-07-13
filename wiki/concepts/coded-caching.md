---
type: concept
title: "Coded Caching"
tags: [caching, content-delivery, d2d, maritime]
related:
  - "[[huang-2026-coded-caching-uav-marine]]"
  - "[[device-to-device-communication]]"
  - "[[service-caching-mec]]"
  - "[[computational-task-caching]]"
  - "[[maritime-mec]]"
  - "[[tian-2026-coded-cache-repair]]"
created: 2026-07-06
updated: 2026-07-13
---

# Coded Caching

A content-caching technique that encodes a file into redundant blocks and distributes those blocks across multiple cache nodes. A requester can reconstruct the file after retrieving enough coded blocks, rather than relying on one node to transmit the full file. In mobile or intermittently connected networks, this increases block availability and lets nearby devices serve part of the request through [[device-to-device-communication|D2D]] links.

In the wiki, [[huang-2026-coded-caching-uav-marine]] uses MDS-coded chunks across AUVs in a UAV-assisted [[maritime-mec|marine edge network]]. The UAV stores complete files, while AUVs cache coded chunks and exchange them over underwater acoustic D2D links. This is distinct from [[service-caching-mec]], which pre-places executable services/models for compute tasks, and from [[computational-task-caching]], which buffers pending tasks for later execution.

[[tian-2026-coded-cache-repair]] adds cache-node failure and fragment repair: MDS, MSR, or MBR parameters are chosen jointly with placement, matching, and UAV movement.
