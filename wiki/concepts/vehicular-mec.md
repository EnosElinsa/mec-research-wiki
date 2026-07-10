---
type: concept
title: Vehicular MEC (V-MEC / VEC)
tags: [iov, mec, vehicular, mobility]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-migration]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[zhang-2026-dwell-time-aerial-vec]]"
  - "[[li-2025-energy-latency-uav-vec]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[vehicle-twin-migration]]"
  - "[[chen-2026-hc-mappo-vehicle-twin-migration]]"
  - "[[ji-2026-llm-iov-uav-offloading]]"
  - "[[hu-2026-ertatd3-secure-caching]]"
  - "[[ren-2026-security-aware-vec-td3]]"
  - "[[feng-2026-prediction-service-migration]]"
  - "[[cui-2026-aris-v2x-icac]]"
created: 2026-05-28
updated: 2026-07-10
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
- **Federated-learning participant control** — when vehicles train local models, the VEC system must select participants that can finish before leaving coverage and allocate UAV bandwidth / compute resources; see [[li-2025-energy-latency-uav-vec]].
- **ISAC-aware UAV support** — when temporary road hot spots need both coverage and sensing, UAV deployment and beamforming can be optimized jointly; see [[li-2026-isac-vec-beamforming-deployment]].

[[chen-2026-hc-mappo-vehicle-twin-migration]] adds [[vehicle-twin-migration]] as a vehicular-metaverse service-continuity problem: predicted RSU workload drives pre-migration, and UAVs act as mobile edge servers when terrestrial RSUs overload. [[li-2026-isac-vec-beamforming-deployment]] adds the sensing side of UAV-assisted VEC by coupling deployment to communication capacity, radar mutual information / CRB-style sensing quality, and UAV energy. [[cui-2026-aris-v2x-icac]] adds active-RIS-assisted V2X integrated communication and computation, optimizing vehicle associations, ARIS reflection, UAV/BS beamforming, offloading ratios, and compute allocation under an [[effective-energy-efficiency]] metric. [[ji-2026-llm-iov-uav-offloading]] adds an LLM-assisted resource-scheduling variant for dense IoV: SOCP handles 3D UAV coverage, DRL and an LLM macro-scheduler allocate power/RBs, and LP sets task offloading ratios. [[hu-2026-ertatd3-secure-caching]] adds secure result caching for UAV-assisted vehicular tasks, [[ren-2026-security-aware-vec-td3]] adds TD3-controlled security-aware offloading against a passive eavesdropper, and [[feng-2026-prediction-service-migration]] uses stacked-LSTM vehicle prediction to reduce unnecessary multi-UAV service migrations.

## Open questions

- How to handle **asymmetric mobility** — some vehicles park, some cross the network in minutes.
- How to integrate V-MEC with [[multi-uav-assisted-mec|UAV]] / [[high-altitude-platform-station|HAPS]] tiers when ground servers are insufficient.
- Privacy implications of centralized trajectory prediction.
