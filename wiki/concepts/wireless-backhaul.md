---
type: concept
title: "Wireless Backhaul"
tags: [backhaul, hap, uav, infrastructure]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-05-29
updated: 2026-05-29
---

# Wireless Backhaul

The high-capacity link that connects an access node (small cell, UAV base station, MEC server) to a higher-tier core or aggregator, **without** wired fiber. Critical for aerial and maritime deployments where running cable is impossible.

Two flavors in the wiki:

- **HAP-as-backhaul** — the HAPS provides high-bandwidth, line-of-sight backhaul for an underlying UAV layer. Used in [[liu-2025-haps-uav-maritime-iot]] explicitly.
- **Inter-RSU backhaul** — wired between RSUs, modeled in [[ma-2025-pdqn-vehicular-mec]] as a fixed-rate link.

A backhaul link's capacity is *upper-tier* infrastructure. It rarely appears as a decision variable, but its value as a constraint shapes the offloading topology — overloaded backhaul forces more local processing.
