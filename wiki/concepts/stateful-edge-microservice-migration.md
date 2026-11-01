---
type: concept
title: "Stateful Edge-Microservice Migration"
tags: [stateful-migration, edge-microservices, container-migration, service-continuity]
related:
  - "[[service-migration]]"
  - "[[task-migration]]"
  - "[[container-layered-storage-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
  - "[[calagna-2026-cormo-ran]]"
  - "[[frejo-martin-2025-uav-stateful-microservice-live-migration]]"
  - "[[hu-2026-seer-on-demand-container-migration]]"
created: 2026-08-27
updated: 2026-11-02
---

# Stateful Edge-Microservice Migration

Migrating an edge microservice together with the runtime state needed to continue a user's session. The state may include CPU context, memory pages, network sockets, open files, or application-specific session data. Unlike stateless relocation, a stateful migration must preserve this state and therefore incurs transfer and service-disruption costs.

## In this wiki

[[calagna-2024-robust-stateful-migration]] provides the detailed COAT connection-preservation architecture and PAM timing model for Podman/CRIU migration. [[calagna-2026-cormo-ran]] applies stateful xApp migration and O-RAN Shared Data Layer alternatives to near-RT RIC energy-aware orchestration. [[container-layered-storage-migration]] addresses a complementary optimization by avoiding redundant Docker base-layer transfers.

[[frejo-martin-2025-uav-stateful-microservice-live-migration]] applies pre-copy live migration to UAV replacement with a digital twin and swarm manager, and [[hu-2026-seer-on-demand-container-migration]] transfers only the snapshot files predicted to be read after resumption, cutting migration traffic in low-bandwidth edges.
