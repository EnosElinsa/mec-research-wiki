---
type: concept
title: "Secure Caching in UAV-MEC"
tags: [caching, privacy, vehicular-mec, uav-mec]
related:
  - "[[service-caching-mec]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[vehicular-mec]]"
  - "[[hu-2026-ertatd3-secure-caching]]"
created: 2026-07-07
updated: 2026-07-07
---

# Secure Caching in UAV-MEC

Secure caching separates reusable edge-side task artifacts from privacy-sensitive user-specific results. General task outputs or intermediate components can be cached at the UAV edge server, while private final processing remains local to the vehicle or user device.

In [[hu-2026-ertatd3-secure-caching]], this split is used for cache-enabled UAV-assisted [[vehicular-mec]]. General tasks can cache full results at the UAV. Private tasks cache only sectional intermediate results, then perform final personalized computation locally, connecting [[service-caching-mec]] to [[privacy-sensitive-data-partitioning]].
