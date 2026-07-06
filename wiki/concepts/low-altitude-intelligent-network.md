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
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[yang-2026-generative-radio-map-lae]]"
  - "[[wen-2026-hybridrag-low-carbon-lae]]"
created: 2026-05-28
updated: 2026-07-07
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

Recent corpus entries use the low-altitude frame for vertical integration, secure communication, robust control, channel estimation, and low-carbon optimization: [[he-2026-dt-sagimec-lae]] adds a DT-assisted UAV/LEO/cloud SAGIMEC architecture for low-altitude economy workloads; [[wang-2026-blockchain-lae-fl-mappo]] models blockchain-assisted FL/MAPPO offloading and caching across UEs, task UAVs, service UAVs, and a BS; [[wang-2026-secure-lae-uav-scheduling]] studies secure LAE communications with UAVs switching between communication and jamming roles; [[jia-2026-dro-lawn-trajectory]] treats uncertain task-size distributions in a UAV/HAP low-altitude wireless network; [[yang-2026-generative-radio-map-lae]] exploits planned air corridors for radio-map-assisted CSI estimation; and [[wen-2026-hybridrag-low-carbon-lae]] uses HybridRAG and diffusion-enhanced SAC for low-carbon LAE MEC formulation and control.

## Open architectural questions

- How to vertically integrate LAIN with terrestrial 5G/6G, HAPS, and LEO?
- What's the right control plane — fully centralized, hierarchical, or federated?
- Spectrum policy — exclusive licensing vs dynamic sharing vs unlicensed.
- Safety / collision avoidance as a coordination problem.
