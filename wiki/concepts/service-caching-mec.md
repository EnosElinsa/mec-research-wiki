---
type: concept
title: "Service Caching in MEC"
tags: [service-caching, mec, infrastructure]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[computational-task-caching]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[gao-2024-service-experience-cache-uav]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
created: 2026-05-29
updated: 2026-06-01
---

# Service Caching in MEC

Pre-deploying the **service program** (executable, libraries, models) for popular tasks at the edge server so a task can be processed locally without first fetching the binary from the cloud. Conceptually similar to CDN caching but for compute artifacts rather than content.

Modeling it requires a binary indicator $\gamma_j \in \{0, 1\}$ for whether task $j$'s service is cached at the local edge. Cached: tiny retrieval cost; uncached: pull from cloud (extra bandwidth + latency). The cache decision itself is a separate, longer-timescale optimization problem (which services to cache); per-task offloading decisions take the cache state as given.

In the wiki, [[peng-2024-energy-time-uav-its]] models the cached/cloud distinction in its UAV-ITS task formulation (the binary $\gamma_j$ indicator above). Service/content caching also appears in the cache-enabled UAV-MEC sources: [[gao-2024-service-experience-cache-uav]] (each UAV caches a subset of services, chosen by a priority-based placement heuristic) and [[zhao-2024-caching-service-placement-uav]] (joint content caching + service placement via Gibbs sampling), and at satellite scale in [[mao-2024-ntn-hierarchical-caching-cav]] (hierarchical content caching). This is distinct from caching the *pending task itself* — see [[computational-task-caching]].
