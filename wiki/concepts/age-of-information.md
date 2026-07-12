---
type: concept
title: "Age of Information (AoI)"
tags: [metrics, freshness, data-collection, iot]
related:
  - "[[aoi-energy-tradeoff]]"
  - "[[qoe-modeling-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[song-2024-mol-aoi-energy]]"
  - "[[shi-2026-aoi-active-ris-noma-agmec]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[wu-not-in-parse-aoi-sampling-buffering-routing]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[guo-2026-aoi-uav-mcs-contract]]"
  - "[[aoi-aware-contract-incentives]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[hazarika-2026-dynamo-uav-vehicle-tracking]]"
  - "[[dynamic-target-prioritization-metric]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[bai-2026-aoi-uav-isac]]"
  - "[[freshness-aware-covert-uav-communication]]"
  - "[[aoi-centric-uav-isac-beam-control]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
created: 2026-05-29
updated: 2026-07-12
---

# Age of Information (AoI)

A **data-freshness** metric: the time elapsed since the generation of the most recently received/collected update from a source. Distinct from latency or throughput — AoI penalizes *stale* information even if individual packets arrive quickly, which matters for monitoring, control, and autonomous-driving applications where decisions depend on the freshest sensor data.

In a UAV data-collection setting, a device's AoI resets when the UAV collects its task and grows otherwise (up to a tolerable maximum beyond which data is invalid). In the wiki, [[song-2024-mol-aoi-energy]] makes total AoI a first-class objective, trading it against UAV energy in the [[aoi-energy-tradeoff]], while [[shi-2026-aoi-active-ris-noma-agmec]] minimizes AoI in active-RIS and NOMA-assisted air-ground MEC through joint offloading, RIS beamforming, and UAV trajectory control. [[shi-2025-aoi-energy-replenishment-multiuav]] applies AoI to rechargeable multi-UAV IoT data collection, coupling UAV wireless power transfer to sensor nodes with UAV charging-station scheduling and value-decomposition MARL. [[wu-not-in-parse-aoi-sampling-buffering-routing]] shifts the freshness target inside a fully airborne leader-follower UAV swarm, where follower UAVs jointly learn when to sample, which buffered packets to forward or discard, and how to route fresh packets through a FANET. [[zhou-2026-a2g-madrl-air-ground-vcs]] uses sensing capability-aware AoI for air-ground vehicular crowdsensing, weighting freshness by non-uniform PoI data and coupling it to latency-weighted collection ratio. [[liao-2026-aoi-ris-uav-usv-mec]] applies average AoI to RIS-assisted UAV-USV maritime MEC, [[cai-2026-llm-drl-secure-lae-data]] uses AoI as a secure LAE data-collection objective, and [[zhao-2026-adaptive-wdc-wet-lae]] balances AoI against energy-device hungry-level-of-energy in WDC/WET service control. [[guo-2026-aoi-uav-mcs-contract]] uses AoI as the freshness target in [[aoi-aware-contract-incentives]] for UAV-assisted mobile crowdsensing. [[hosseini-2026-aoi-covert-uav]] adds [[freshness-aware-covert-uav-communication]], where public-cover PD-NOMA and UAV beamforming shape covert update freshness, and [[bai-2026-aoi-uav-isac]] adds [[aoi-centric-uav-isac-beam-control]] for UAV-ISAC target-state updates.

[[hazarika-2026-dynamo-uav-vehicle-tracking]] shows the limit of using AoI alone for fast vehicle tracking: the [[dynamic-target-prioritization-metric]] keeps elapsed update time but adds trajectory deviation, prediction uncertainty, SINR, and distance-aware quality. AoI remains the corpus's freshness-oriented complement to delay-based [[qoe-modeling-mec]], and it tightly couples to [[uav-trajectory-control]].

[[wang-2026-glint-aoi-wireless-powered-edge]] adds a nonlinear energy-harvesting constraint to the freshness loop. Its [[dual-network-sequential-aoi-control]] first resolves multi-UAV mobility and sensor association, then schedules WPT duration and sensor updates from the resulting coverage and battery state.
