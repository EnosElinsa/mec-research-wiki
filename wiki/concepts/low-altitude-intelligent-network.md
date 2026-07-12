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
  - "[[huang-2026-offgrid-lae-imager]]"
  - "[[zeng-2026-movable-antenna-u2u-channel]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[ye-2026-mode-lae-isac]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[trajectory-privacy]]"
  - "[[wu-2026-service-oriented-segmented-trajectory]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
  - "[[zhao-2026-temporal-spectrum-cartography]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[gong-2026-lp2-casku-uav-clusters]]"
  - "[[deng-2026-uav-cpn-energy]]"
  - "[[lu-2026-uav-swarm-two-level-ma]]"
  - "[[liu-2026-spherical-t-ris-bs]]"
  - "[[spherical-transmissive-ris]]"
  - "[[belgiovine-not-in-parse-multidt-abs-deployment]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[target-level-of-safety]]"
  - "[[yang-2025-hcdrl-pursuit-evasion]]"
  - "[[cooperative-uav-pursuit-evasion]]"
created: 2026-05-28
updated: 2026-07-12
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

Recent corpus entries use the low-altitude frame for vertical integration, secure communication, robust control, channel estimation, low-carbon optimization, LLM-assisted control, sensing-aware trajectory control, and physical-layer modeling: [[he-2026-dt-sagimec-lae]] adds a DT-assisted UAV/LEO/cloud SAGIMEC architecture for low-altitude economy workloads; [[wang-2026-blockchain-lae-fl-mappo]] models blockchain-assisted FL/MAPPO offloading and caching across UEs, task UAVs, service UAVs, and a BS; [[wang-2026-secure-lae-uav-scheduling]] studies secure LAE communications with UAVs switching between communication and jamming roles; [[jia-2026-dro-lawn-trajectory]] treats uncertain task-size distributions in a UAV/HAP low-altitude wireless network; [[yang-2026-generative-radio-map-lae]] exploits planned air corridors for radio-map-assisted CSI estimation; [[huang-2026-offgrid-lae-imager]] reconstructs sparse low-altitude aerial images from cooperative ISAC CSI; [[wang-2026-stbc-cooperative-isac]] uses shared-resource multi-BS cooperative ISAC for UAV sensing at cell edges; [[zeng-2026-movable-antenna-u2u-channel]] models movable-antenna UAV-to-UAV wideband channels; [[wen-2026-hybridrag-low-carbon-lae]] uses HybridRAG and diffusion-enhanced SAC for low-carbon LAE MEC formulation and control; [[cai-2026-llm-drl-secure-lae-data]] uses an LLM-enhanced DRL loop for secure LAE data collection; [[wu-2026-service-oriented-segmented-trajectory]] adds service-oriented high-rise UAV-MEC with [[trajectory-privacy]]; and the DeepLSC / Meta-DeepESC pair ([[ye-2026-deeplsc-lae-isac]], [[ye-2026-meta-deepesc-lae-isac]]) treats LAE ISAC as a flight-period DRL control problem over GBS beamforming plus UAV trajectories.

The LAE sensing-control line also includes [[ye-2026-mode-lae-isac]], which uses [[mixture-of-experts-drl]] for multi-objective communication/sensing tradeoffs, [[zhao-2025-networked-isac-uav-handover]], which uses multi-BS [[networked-isac]] for unauthorized-UAV tracking and sensing-cell handover, [[zhao-2026-temporal-spectrum-cartography]], which reconstructs temporal RF power maps from sparse static/mobile sensing, and [[gong-2026-safe-economic-lae-trajectory]], which grounds [[compliance-aware-uav-trajectory]] planning under obstacles, no-fly zones, residential speed limits, landing, and energy constraints. The rescue/offloading side includes [[tang-2026-hg-maddpg-uav-rescue]], where UAVs coordinate with [[ground-embedded-robot|ground embedded robots]] and airship support for low-altitude post-disaster exploration. [[zhao-2026-adaptive-wdc-wet-lae]] adds adaptive WDC/WET service balancing for heterogeneous IoT devices, [[gong-2026-lp2-casku-uav-clusters]] adds authentication and session-key continuity for dynamic UAV clusters, [[deng-2026-uav-cpn-energy]] turns UAV relaying into computing-power-network service expansion, and [[lu-2026-uav-swarm-two-level-ma]] treats UAV swarm positions plus onboard arrays as a [[two-level-movable-antenna]] system.

[[liu-2026-spherical-t-ris-bs]] adds a low-altitude infrastructure variant: a [[spherical-transmissive-ris]] base-station architecture is evaluated in a UAV data-collection scenario with uplink cellular users, where the surface geometry is meant to reduce angle-sensitive gain loss across 3-D aerial directions.

[[belgiovine-not-in-parse-multidt-abs-deployment]] and [[jiang-2026-bi-level-uav-delivery-safety]] add planning infrastructure for LAE operations: the former uses multiple digital twins to place airborne base stations before mission deployment, while the latter enforces [[target-level-of-safety]] in heterogeneous UAV delivery scheduling and routing.

[[yang-2025-hcdrl-pursuit-evasion]] adds a counter-UAV control case through [[cooperative-uav-pursuit-evasion]]. Its low-altitude network provides the application frame, but the evaluated pursuit model assumes ideal communication and does not optimize radio resources.

## Open architectural questions

- How to vertically integrate LAIN with terrestrial 5G/6G, HAPS, and LEO?
- What's the right control plane — fully centralized, hierarchical, or federated?
- Spectrum policy — exclusive licensing vs dynamic sharing vs unlicensed.
- Safety / collision avoidance as a coordination problem.
