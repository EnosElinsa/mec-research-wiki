---
type: concept
title: "Target Graph Representation"
tags: [graph-neural-network, cooperative-perception, uav-tracking, target-handover]
related:
  - "[[he-2026-lscr-uav-relay-tracking]]"
  - "[[graph-neural-network]]"
  - "[[cooperative-perception]]"
  - "[[uav-enabled-its]]"
created: 2026-07-10
updated: 2026-07-10
---

# Target Graph Representation

Target graph representation encodes a tracked object together with the spatial layout of nearby detected objects. For UAV relay tracking, the graph carries more information than the target's own appearance or absolute location: neighboring targets and inter-target distances provide context that can remain useful when two UAVs view the scene from different angles.

In [[he-2026-lscr-uav-relay-tracking]], Delaunay triangulation constructs the local target graph, edge weights represent distance relationships, and a lightweight GRCN extracts a graph-level embedding. Twin-GRCN then compares two target graph representations to support handover between UAVs with only coordinate-level information transfer.
