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
created: 2026-05-29
updated: 2026-07-10
---

# Wireless Backhaul

The high-capacity link that connects an access node (small cell, UAV base station, MEC server) to a higher-tier core or aggregator, **without** wired fiber. Critical for aerial and maritime deployments where running cable is impossible.

Two flavors in the wiki:

- **HAP-as-backhaul** — the HAPS provides high-bandwidth, line-of-sight backhaul for an underlying UAV layer. Used in [[liu-2025-haps-uav-maritime-iot]] explicitly.
- **UAV-to-infrastructure backhaul** — the aerial access point must preserve a BS or upper-tier link while serving ground users. [[zheng-2026-active-search-low-altitude-uav]] makes this a search constraint by balancing BS-UAV and UAV-user objectives.
- **FANET swarm backhaul / forwarding** — multi-UAV networks need routing behavior that survives topology and traffic changes. [[deng-2026-eret-fanet-routing]] treats route-expiration time as an adaptive knob for moving between route reuse and content-centric discovery.
- **Inter-RSU backhaul** — wired between RSUs, modeled in [[ma-2025-pdqn-vehicular-mec]] as a fixed, small per-hop transmission delay between adjacent RSUs (propagation-dominated, scaled by the number of road segments a relayed task crosses).

A backhaul link's capacity is *upper-tier* infrastructure. It rarely appears as a decision variable, but its value as a constraint shapes the offloading topology — overloaded backhaul forces more local processing.
