---
type: concept
title: "Service Caching in MEC"
tags: [service-caching, mec, infrastructure]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-05-29
---

# Service Caching in MEC

Pre-deploying the **service program** (executable, libraries, models) for popular tasks at the edge server so a task can be processed locally without first fetching the binary from the cloud. Conceptually similar to CDN caching but for compute artifacts rather than content.

Modeling it requires a binary indicator $\gamma_j \in \{0, 1\}$ for whether task $j$'s service is cached at the local edge. Cached: tiny retrieval cost; uncached: pull from cloud (extra bandwidth + latency). The cache decision itself is a separate, longer-timescale optimization problem (which services to cache); per-task offloading decisions take the cache state as given.

In the wiki, [[peng-2024-energy-time-uav-its]] models the cached/cloud distinction in its UAV-ITS task formulation. None of the other wiki sources currently model service caching explicitly — most assume the service is "always available locally."
