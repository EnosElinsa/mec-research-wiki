---
type: concept
title: Heterogeneous UAV Fleet
tags: [uav, heterogeneity, capability]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[fu-2026-dubins-uav-data-collection]]"
  - "[[releasing-collecting-recycling-uav-framework]]"
  - "[[li-2026-jscfg-uav-grouping]]"
  - "[[joint-switch-coalition-formation-game]]"
  - "[[zhang-2019-fast-uav-deployment]]"
  - "[[fast-heterogeneous-uav-deployment]]"
created: 2026-05-28
updated: 2026-07-13
---

# Heterogeneous UAV Fleet

A multi-UAV system where UAVs differ along one or more axes:

- **Service-type capability** — which workloads the UAV can serve (vision, NLP, transactions, sensor preprocessing, etc.).
- **Compute capacity** — CPU/GPU profile, memory, accelerator presence.
- **Energy capacity** — battery size, recharge rate.
- **Mobility profile** — top speed, ceiling, hover endurance.
- **Sensor suite** — what the UAV can perceive and report back.

Most foundational UAV-MEC papers (e.g. [[liu-2026-jppo-en-convntm]]) assume a homogeneous fleet — every UAV is interchangeable. Real deployments are not like this.

## Why heterogeneity matters

- **Job-UAV compatibility constraint.** Not every UAV can serve every job. The matching becomes a constrained assignment problem rather than free pairing.
- **Specialization trade-offs.** Equipping every UAV with everything wastes payload. Specialization is more efficient in expectation but raises coordination costs.
- **Trajectory implications.** A UAV that can only serve type-A jobs must travel farther on average to find type-A demand than a generalist would, which inflates flight-energy.

## In this wiki

[[zhang-2025-ssac-mgi-heterogeneous-uav]] is the source built explicitly around fleet heterogeneity. Its **SSAC** (Shared Soft Actor-Critic) architecture shares the policy networks across all UAVs and extracts *dimension-invariant* features, so UAVs that differ in service type and resource capacity learn a unified policy; alternatives include type-aware attention or capability-conditioned policy heads.

[[jiang-2026-bi-level-uav-delivery-safety]] adds a logistics-control case: heterogeneous UAVs differ in delivery capacity and route feasibility, so task allocation and safety-constrained trajectory planning must be solved together instead of assuming interchangeable vehicles.

[[fu-2026-dubins-uav-data-collection]] makes heterogeneity architectural: a fast carrier releases and recovers slower communication UAVs. [[li-2026-jscfg-uav-grouping]] instead groups functional UAV types around ordered mission requirements through a [[joint-switch-coalition-formation-game]].

[[zhang-2019-fast-uav-deployment]] adds coverage-service heterogeneity: speed, operating altitude, radius, and origin determine how quickly a given fleet can cover a target area. Its exact and approximation results show that heterogeneity affects not only assignment quality but also performance bounds and tractability.

## Open questions

- Optimal heterogeneity *granularity* — how fine-grained should capability typing be?
- Live re-provisioning — can UAVs swap modules / containers / model weights mid-mission?
- Marketplaces — auction-based dynamic pairing of jobs to capable UAVs.
