---
type: concept
title: "Regenerating Codes"
tags: [coded-caching, erasure-coding, distributed-storage, cache-repair]
related:
  - "[[tian-2026-coded-cache-repair]]"
  - "[[coded-caching]]"
  - "[[erasure-coded-edge-storage]]"
  - "[[uav-content-caching]]"
created: 2026-07-13
updated: 2026-07-13
---

# Regenerating Codes

Regenerating codes repair a failed distributed-storage node by downloading partial information from multiple surviving nodes instead of reconstructing the entire file at a central server. Their design trades per-node storage against repair bandwidth: minimum-storage regenerating (MSR) codes minimize stored data, while minimum-bandwidth regenerating (MBR) codes minimize repair traffic.

[[tian-2026-coded-cache-repair]] uses MDS, MSR, and MBR families in a UAV cache network. A requester needs at least `k` fragments to recover a file, while a replacement UAV contacts at least `d` valid UAVs to repair one lost fragment. Code family and parameters therefore affect both download and repair success under changing UAV availability.
