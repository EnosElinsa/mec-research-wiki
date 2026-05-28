---
type: concept
title: Heterogeneous UAV Fleet
tags: [uav, heterogeneity, capability]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-05-28
updated: 2026-05-28
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

[[zhang-2025-ssac-mgi-heterogeneous-uav]] is the first source explicitly addressing heterogeneity. Its **SSAC** architecture (shared backbone + per-UAV head) is one solution; alternatives include type-aware attention or capability-conditioned policy heads.

## Open questions

- Optimal heterogeneity *granularity* — how fine-grained should capability typing be?
- Live re-provisioning — can UAVs swap modules / containers / model weights mid-mission?
- Marketplaces — auction-based dynamic pairing of jobs to capable UAVs.
