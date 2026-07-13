---
type: concept
title: UAV Data Collection
tags: [uav, data-collection, iot, data-sink, aerial-communications]
related:
  - "[[lu-2026-aoi-trajectory-channel]]"
  - "[[zhao-2026-uav-irs-data-collection]]"
  - "[[guo-2026-uav-wsn-completion-time]]"
  - "[[wang-2025-sac-tma-mec-dc]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[age-of-information]]"
  - "[[task-offloading]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[liu-2026-spherical-t-ris-bs]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[du-2025-autonomous-intelligent-uav-swarms]]"
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[fan-2026-hap-uav-iort-oee]]"
  - "[[overall-energy-efficiency]]"
  - "[[le-2026-asynchronous-uav-data-collection]]"
  - "[[asynchronous-qmix]]"
  - "uav-assisted-mobile-crowd-sensing"
  - "[[li-2023-energy-constrained-uav-data-collection]]"
  - "[[energy-constrained-uav-data-collection-orienteering]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
  - "[[zhao-2026-dt-ddqn-bisd-deployment]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[fu-2026-dubins-uav-data-collection]]"
  - "[[releasing-collecting-recycling-uav-framework]]"
  - "[[jia-2026-hierarchical-uav-swarms]]"
  - "[[hierarchical-uav-swarm]]"
  - "[[li-2016-energy-balanced-uav-relaying]]"
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[memory-augmented-multi-uav-navigation]]"
  - "[[samir-2022-aoi-altitude-scheduling]]"
created: 2026-05-31
updated: 2026-07-13
---

# UAV Data Collection

A UAV mission pattern where the aircraft acts as a flying **data sink**, flying to (or hovering over) ground IoT devices to collect their sensed data directly over LoS links — reducing device transmit power and preventing data overflow in hard-to-reach areas. It is the **data-gathering** counterpart to UAV-assisted **computation offloading** ([[task-offloading]]): the former maximizes collected data volume, the latter minimizes compute latency/energy.

## Joint MEC + DC

These two missions are usually studied separately and often run on different UAVs — an MEC-UAV doing real-time compute, a DC-UAV gathering freshness-insensitive data — because mixing them can hurt MEC latency and raise energy use, and isolating the data aids privacy. [[wang-2025-sac-tma-mec-dc]] is the corpus's entry that instead **jointly** optimizes a multi-AAV MEC-DC system, trading off MEC latency against collected data volume under co-channel interference, using SAC plus a matching-based user-association strategy.

## Relation to freshness

When the collected data is delay-sensitive, data-collection objectives connect to [[age-of-information]]; in [[wang-2025-sac-tma-mec-dc]] the DC data is explicitly **freshness-insensitive**, so the objective is total volume rather than AoI. [[cai-2026-llm-drl-secure-lae-data]] studies the freshness-sensitive and security-sensitive case, coordinating a data-collection UAV with a jamming UAV under AoI, energy, and eavesdropping constraints.

[[zhao-2026-adaptive-wdc-wet-lae]] adds the dual-service low-altitude version: UAVs collect fresh data from I-devices while also transferring RF energy to E-devices, with AoI and hungry-level-of-energy balanced by an adaptive reward preference rather than a fixed hand-tuned weight.

[[shi-2025-aoi-energy-replenishment-multiuav]] adds the rechargeable-IoT version: UAVs wirelessly charge sensor nodes, collect fresh updates, offload to the BS, and recharge at fixed charging stations, with VDN/QMIX deciding local multi-UAV actions. [[liu-2026-spherical-t-ris-bs]] uses UAV data collection as the application benchmark for a spherical transmissive-RIS base station.

[[you-2019-rician-uav-data-harvesting]] is the channel-model foundation case: a single UAV collects WSN data under outage-aware [[angle-dependent-rician-fading]], jointly optimizing scheduling, horizontal trajectory, and vertical trajectory through BCD/SCA.

[[gao-2023-uav-mcs-uma]] broadens the collection model to uav-assisted-mobile-crowd-sensing: UAVs cover points of interest that human participants miss and calibrate participant sensors when trajectories intersect. [[du-2025-autonomous-intelligent-uav-swarms]] is a survey anchor for the swarm autonomy stack behind data collection, relaying, monitoring, and edge-computing applications.

[[fan-2026-hap-uav-iort-oee]] adds a moving HAP aggregation tier and optimizes [[overall-energy-efficiency]] across both collection hops. [[le-2026-asynchronous-uav-data-collection]] instead studies stochastic remote sensing with unequal action durations and limited inter-UAV communication, using [[asynchronous-qmix]] for event-driven trajectory decisions and local convex bandwidth allocation at hover points.

[[li-2023-energy-constrained-uav-data-collection]] treats collection as [[energy-constrained-uav-data-collection-orienteering]] over depot-returning hover tours, distinguishing full/partial collection and non-overlap guarantees from overlap heuristics. [[wang-2026-glint-aoi-wireless-powered-edge]] adds the wireless-powered freshness case, where multiple UAVs first move and associate sensors, then allocate charging time and update transmissions through [[dual-network-sequential-aoi-control]].

[[fu-2026-dubins-uav-data-collection]] adds a carrier/subordinate architecture through the [[releasing-collecting-recycling-uav-framework]]: a transport UAV releases communication UAVs for obstacle-aware collection tours and later synchronizes airborne recovery.
