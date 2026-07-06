---
type: concept
title: "Service Migration in MEC"
tags: [mec, service-migration, handover, mobility, resource-management]
related:
  - "[[task-migration]]"
  - "[[seamless-handover]]"
  - "[[two-timescale-optimization]]"
  - "[[mobile-edge-computing]]"
  - "[[shi-2023-two-timescale-migration-rerouting]]"
  - "[[feng-2026-prediction-service-migration]]"
created: 2026-06-02
updated: 2026-07-07
---

# Service Migration in MEC

Moving a long-lived **service application** (the program/state an edge server must host to serve a device's tasks) from one edge server to another when a device hands over between access points. Migration keeps edge service continuous for a roaming device, but it is not free: edge servers are capacity-limited and cannot host every application, and migrating a large application incurs a setup delay that can cause **service interruption** (e.g. migrating an XR application can take seconds against a tens-of-milliseconds delay budget).

Distinct from neighboring mechanisms:

- **Task migration** ([[task-migration]]) — forwards a single in-flight *task* between servers, not the whole service binding.
- **Task rerouting** — leaves the application where it is and instead sends the roaming device's new tasks *back* to its previously-hosted server; it avoids the migration overhead but pays per-task rerouting delay and energy.
- **Compute-state handover** ([[seamless-handover]]) — hands over in-progress computation state (e.g. a partially-trained model) between LEO satellites.

The recurring research question is **when to migrate vs reroute**: migration suits service-delay-tolerant / task-delay-sensitive workloads, rerouting suits the opposite. Because handover-triggered migration/rerouting changes slowly while resource allocation changes fast, the problem is a natural fit for [[two-timescale-optimization]].

## In this wiki

[[shi-2023-two-timescale-migration-rerouting]] is the anchor: it jointly balances **service migration and task rerouting** for MEC handovers in a two-timescale online framework (slow: access selection + migration/rerouting; fast: computing/communication resource allocation), minimizing long-term average service delay via an improved [[mobile-edge-computing|MEC]] Lyapunov algorithm with randomized rounding and Lagrange-dual inner solvers. [[feng-2026-prediction-service-migration]] moves the mechanism into multi-UAV vehicular MEC, where stacked-LSTM vehicle prediction, [[lyapunov-optimization]], and MADDPG coordinate when a service instance should migrate between UAV MEC servers.
