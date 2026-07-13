---
type: concept
title: "Wireless Backhaul"
tags: [backhaul, hap, uav, infrastructure]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[zheng-2026-active-search-low-altitude-uav]]"
  - "[[deng-2026-eret-fanet-routing]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[aerial-active-ris-backhaul]]"
  - "[[jeon-2026-ampli-flection-aerial-backhaul]]"
  - "[[mozaffari-not-in-parse-3d-drone-cellular-network]]"
  - "[[hua-2026-ddrl-content-delivery]]"
  - "[[uav-content-caching]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
  - "[[wang-2026-multimodal-uav-coverage-backhaul]]"
  - "[[multi-modal-uav-coverage-backhaul-control]]"
  - "[[su-2026-three-tier-uav-capacity]]"
created: 2026-05-29
updated: 2026-07-13
---

# Wireless Backhaul

The high-capacity link that connects an access node (small cell, UAV base station, MEC server) to a higher-tier core or aggregator, **without** wired fiber. Critical for aerial and maritime deployments where running cable is impossible.

Recurring forms in the wiki:

- **HAP / FSO backhaul for aerial cells** — the HAP tier provides line-of-sight backhaul to an underlying UAV access layer. [[mozaffari-not-in-parse-3d-drone-cellular-network]] uses HAP drones for FSO backhaul to LAP drone-BSs, while [[liu-2025-haps-uav-maritime-iot]] uses HAPS backhaul explicitly in the maritime-IoT setting.
- **HAP-as-backhaul** — the HAPS provides high-bandwidth, line-of-sight backhaul for an underlying UAV layer. Used in [[liu-2025-haps-uav-maritime-iot]] explicitly.
- **UAV-to-infrastructure backhaul** — the aerial access point must preserve a BS or upper-tier link while serving ground users. [[zheng-2026-active-search-low-altitude-uav]] makes this a search constraint by balancing BS-UAV and UAV-user objectives.
- **Aerial active-RIS backhaul** - an airborne active RIS provides the relay-like backhaul path for UAV base stations while optimizing amplification, phase, platform placement, and array partitioning. [[jeon-2026-ampli-flection-aerial-backhaul]] is the corpus anchor for this [[aerial-active-ris-backhaul]] pattern.
- **FANET swarm backhaul / forwarding** — multi-UAV networks need routing behavior that survives topology and traffic changes. [[deng-2026-eret-fanet-routing]] treats route-expiration time as an adaptive knob for moving between route reuse and content-centric discovery.
- **Inter-RSU backhaul** — wired between RSUs, modeled in [[ma-2025-pdqn-vehicular-mec]] as a fixed, small per-hop transmission delay between adjacent RSUs (propagation-dominated, scaled by the number of road segments a relayed task crosses).
- **Cache-miss backhaul** - [[hua-2026-ddrl-content-delivery]] makes the BS-UAV retrieval link part of end-to-end acquisition delay: [[uav-content-caching]] avoids this hop on a hit, while a miss couples cache replacement to UAV position and backhaul rate.

[[wang-2026-multimodal-uav-coverage-backhaul]] turns backhaul into a dynamic UAV role: access points switch among cluster exploration, local user service, and minimum-spanning-tree bridge formation through [[multi-modal-uav-coverage-backhaul-control]]. [[liu-2020-distributed-uav-coverage-navigation]] instead treats peer connectivity as a constraint while UAVs optimize long-term access coverage and movement energy.

A backhaul link's capacity is *upper-tier* infrastructure. It rarely appears as a decision variable, but its value as a constraint shapes the offloading topology — overloaded backhaul forces more local processing.

[[su-2026-three-tier-uav-capacity]] makes UAV-to-BS SDMA backhaul an explicit end-to-end bottleneck and bounds the error of a mean-interference capacity approximation under transmit/receive pointing jitter.
