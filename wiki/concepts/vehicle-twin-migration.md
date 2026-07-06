---
type: concept
title: "Vehicle Twin Migration"
tags: [digital-twin, vehicular-mec, service-migration, metaverse]
related:
  - "[[chen-2026-hc-mappo-vehicle-twin-migration]]"
  - "[[digital-twin]]"
  - "[[task-migration]]"
  - "[[service-migration]]"
  - "[[vehicular-mec]]"
  - "[[mou-2025-adm-dt-migration]]"
created: 2026-07-07
updated: 2026-07-07
---

# Vehicle Twin Migration

Vehicle twin migration moves or pre-migrates the service state for a vehicle's digital twin across edge servers as the physical vehicle moves. It is a vehicular-metaverse specialization of [[service-migration]] and [[task-migration]]: the migrated object is not just a single computation result, but a latency-sensitive virtual representation that must stay synchronized with a mobile vehicle.

[[chen-2026-hc-mappo-vehicle-twin-migration]] adds UAV-assisted support for this concept: RSU workload prediction decides when terrestrial infrastructure is likely to overload, and UAVs act as mobile edge servers that can serve vehicles or relieve RSUs. [[mou-2025-adm-dt-migration]] is the closest existing corpus neighbor, focusing on adaptive digital-twin migration in vehicular edge networks without the same UAV-routing layer.
