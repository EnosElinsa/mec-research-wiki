---
type: concept
title: "Erasure-Coded Edge Storage"
tags: [storage, erasure-coding, reliability, mec]
related:
  - "[[coded-caching]]"
  - "[[service-caching-mec]]"
  - "[[post-disaster-mec]]"
  - "[[huang-2026-erasure-coded-uav-storage]]"
created: 2026-07-07
updated: 2026-07-07
---

# Erasure-Coded Edge Storage

Erasure-coded edge storage splits a file into data blocks plus parity blocks so that the file can be reconstructed from any sufficient subset of coded blocks. In UAV or edge systems, this reduces the cost of full replication while preserving availability when some storage nodes are unreachable.

The design question is not just "where should the file be cached?" It also includes how many data/parity blocks to generate, which mobile nodes should store each block, and how users should retrieve enough blocks under changing connectivity. In [[huang-2026-erasure-coded-uav-storage]], this becomes a storage-cost-vs-access-delay problem for a post-disaster UAV edge system, solved with trajectory prediction plus hierarchical RL.

This concept is adjacent to [[coded-caching]] and [[service-caching-mec]], but the failure/recovery semantics are different: coded caching usually exploits multicast or cache-hit structure, while erasure-coded storage is about reconstructability from partial block availability.
