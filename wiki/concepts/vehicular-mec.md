---
type: concept
title: Vehicular MEC (V-MEC / VEC)
tags: [iov, mec, vehicular, mobility]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-migration]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[zhang-2026-dwell-time-aerial-vec]]"
created: 2026-05-28
updated: 2026-07-06
---

# Vehicular MEC (V-MEC / VEC)

MEC where the user devices are vehicles — connected, semi-autonomous, or autonomous — moving at sustained high speed through a network of roadside / cellular edge servers. Distinguishing properties vs static-IoT MEC:

- **Sustained mobility** — vehicles cross multiple server coverage areas during a single task's lifetime.
- **Spatio-temporal load imbalance** — server loads are highly correlated with rush-hour patterns and traffic flow geometry.
- **Strict latency budgets** — autonomous-driving and ADAS workloads have hard real-time deadlines.
- **Predictable mobility (relative to UAVs)** — vehicles follow road graphs, so trajectory prediction becomes both feasible and valuable.

## Common architectural responses

- **[[task-migration]]** — when a server overloads, forward the queued tasks to a less-loaded peer. The challenge is anticipating the imbalance.
- **Trajectory prediction** — use historical traces to estimate future server-coverage transitions, allowing pre-emptive migration. See [[informer-trajectory-prediction]] in [[zhang-2025-mcma-task-migration]].
- **CTDE multi-agent control** — each server is an agent under [[ma-pomdp]] framing; centralized critic + decentralized actor.
- **Aerial fallback tiers** — UAVs and [[high-altitude-platform-station|HAPS]] can cover sparse or overloaded roads, but high-speed vehicles introduce [[dwell-time-constrained-offloading]] as a feasibility constraint; see [[zhang-2026-dwell-time-aerial-vec]].

## Open questions

- How to handle **asymmetric mobility** — some vehicles park, some cross the network in minutes.
- How to integrate V-MEC with [[multi-uav-assisted-mec|UAV]] / [[high-altitude-platform-station|HAPS]] tiers when ground servers are insufficient.
- Privacy implications of centralized trajectory prediction.
