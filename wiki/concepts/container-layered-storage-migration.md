---
type: concept
title: "Container Layered-Storage Migration"
tags: [container-migration, docker, layered-storage, service-handoff, edge-computing]
related:
  - "[[stateful-edge-microservice-migration]]"
  - "[[service-migration]]"
  - "[[mobile-edge-computing]]"
  - "[[ma-2019-layered-container-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# Container Layered-Storage Migration

Using a container image's immutable base layers as shared state between source and destination hosts, so a migration transfers only the writable layer and changed runtime data. The approach reduces WAN transfer volume but still requires synchronization, layer-ID matching, checkpoint/restore, and a handoff procedure for active users.

## In this wiki

[[ma-2019-layered-container-migration]] demonstrates the pattern with Docker layered storage, dirty-memory pre-dumps, compression, and pipelined transfer. It complements [[stateful-edge-microservice-migration]], where COAT preserves a transport connection and PAM models stateful migration time.
