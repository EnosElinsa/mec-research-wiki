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
created: 2026-08-27
updated: 2026-08-27
---

# Stateful Edge-Microservice Migration

Migrating an edge microservice together with the runtime state needed to continue a user's session. The state may include CPU context, memory pages, network sockets, open files, or application-specific session data. Unlike stateless relocation, a stateful migration must preserve this state and therefore incurs transfer and service-disruption costs.

## In this wiki

[[calagna-2024-robust-stateful-migration]] provides the detailed COAT connection-preservation architecture and PAM timing model for Podman/CRIU migration. [[calagna-2026-cormo-ran]] applies stateful xApp migration and O-RAN Shared Data Layer alternatives to near-RT RIC energy-aware orchestration. [[container-layered-storage-migration]] addresses a complementary optimization by avoiding redundant Docker base-layer transfers.
