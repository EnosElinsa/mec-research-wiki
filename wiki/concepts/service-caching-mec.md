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
  - "[[fan-2026-parallel-caching-uav-mec]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
  - "[[secure-caching-uav-mec]]"
  - "[[hu-2026-ertatd3-secure-caching]]"
  - "[[wu-2025-security-aware-multiuav-service-placement]]"
  - "[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]]"
  - "[[action-masked-hierarchical-drl]]"
created: 2026-05-29
updated: 2026-07-11
---

# Service Caching in MEC

Pre-deploying the **service program** (executable, libraries, models) for popular tasks at the edge server so a task can be processed locally without first fetching the binary from the cloud. Conceptually similar to CDN caching but for compute artifacts rather than content.

Modeling it requires a binary indicator $\gamma_j \in \{0, 1\}$ for whether task $j$'s service is cached at the local edge. Cached: tiny retrieval cost; uncached: pull from cloud (extra bandwidth + latency). The cache decision itself is a separate, longer-timescale optimization problem (which services to cache); per-task offloading decisions take the cache state as given.

[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]] is a nearby secure content-delivery case rather than MEC offloading: UAVs cache requested files at the long timescale, while [[action-masked-hierarchical-drl]] handles short-timescale secure association, deployment, and beamforming.

In the wiki, [[peng-2024-energy-time-uav-its]] models the cached/cloud distinction in its UAV-ITS task formulation (the binary $\gamma_j$ indicator above). Service/content caching also appears in the cache-enabled UAV-MEC sources: [[gao-2024-service-experience-cache-uav]] (each UAV caches a subset of services, chosen by a priority-based placement heuristic), [[zhao-2024-caching-service-placement-uav]] (joint content caching + service placement via Gibbs sampling), [[fan-2026-parallel-caching-uav-mec]] (content caching tied to computation offloading and channel allocation under parallel execution), [[hu-2026-ertatd3-secure-caching]] (general task-result caching plus privacy-preserving partial caching for private vehicular tasks), and [[wu-2025-security-aware-multiuav-service-placement]] (service-program placement under secure offloading and UAV-jammer constraints), and at satellite scale in [[mao-2024-ntn-hierarchical-caching-cav]] (hierarchical content caching). This is distinct from caching the *pending task itself* — see [[computational-task-caching]] — and from [[secure-caching-uav-mec]], which adds privacy constraints to what can be cached.
