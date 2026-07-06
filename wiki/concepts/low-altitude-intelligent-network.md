---
type: concept
title: Low-Altitude Intelligent Network (LAIN / Low-Altitude Economy)
tags: [uav, low-altitude-economy, 6g, network-architecture]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[he-2026-dt-sagimec-lae]]"
  - "[[jia-2026-dro-lawn-trajectory]]"
created: 2026-05-28
updated: 2026-07-06
---

# Low-Altitude Intelligent Network (LAIN / Low-Altitude Economy)

The networking layer that supports the rapidly emerging **low-altitude economy** — UAVs, eVTOLs, drone delivery, urban air mobility, low-altitude IoT — operating below ~1000 m altitude in a dense, intelligent, often multi-operator regime.

Distinguishing characteristics vs general UAV networks:

- **Density.** Many UAVs per cubic kilometer in urban / industrial zones; spectrum is the binding constraint.
- **Diverse missions.** Cargo, surveillance, agriculture, communication relay, MEC offloading — each with different latency / bandwidth / reliability profiles.
- **Multi-operator.** Public and private fleets share airspace and infrastructure.
- **Vertical integration.** Couples to ground 5G/6G, [[high-altitude-platform-station|HAPS]], [[leo-satellite-edge-computing|LEO]] tiers.

## Why MEC research cares

LAINs are the natural deployment substrate for [[multi-uav-assisted-mec|UAV-MEC]] in real-world urban environments. Spectrum sharing schemes like [[wang-2025-uav-swarm-stackelberg]] are foundational — without efficient spectrum coordination, UAV-MEC compute offloading becomes bandwidth-starved.

Recent corpus entries use the low-altitude frame for both vertical integration and robust control: [[he-2026-dt-sagimec-lae]] adds a DT-assisted UAV/LEO/cloud SAGIMEC architecture for low-altitude economy workloads, while [[jia-2026-dro-lawn-trajectory]] treats uncertain task-size distributions in a UAV/HAP low-altitude wireless network.

## Open architectural questions

- How to vertically integrate LAIN with terrestrial 5G/6G, HAPS, and LEO?
- What's the right control plane — fully centralized, hierarchical, or federated?
- Spectrum policy — exclusive licensing vs dynamic sharing vs unlicensed.
- Safety / collision avoidance as a coordination problem.
