---
type: concept
title: "Multi-Microservice Application Placement"
tags: [microservice-placement, service-migration, mobile-edge-computing, resource-management]
related:
  - "[[service-migration]]"
  - "[[mobile-edge-computing]]"
  - "[[dynamic-space-time-graph-with-virtual-edges]]"
  - "[[adeppady-2026-step-composite-edge]]"
created: 2026-08-27
updated: 2026-08-27
---

# Multi-Microservice Application Placement

Jointly deciding where the microservices composing an edge application are deployed, which instances serve each user, how much CPU and radio resource they receive, and when mobility triggers migration or relocation. The problem must distinguish stateful and stateless services, sharing semantics, application latency, downtime, resource capacities, and quality-version choices.

## In this wiki

[[adeppady-2026-step-composite-edge]] names this optimization problem MAP and solves a local graph representation with STEP. Its DNTG and expanded decision graph encode application chains, user handovers, resource constraints, and additive latency/downtime budgets before minimum-cost path selection.
