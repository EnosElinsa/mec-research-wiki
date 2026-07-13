---
type: concept
title: "RF Energy Harvesting"
tags: [energy-harvesting, wireless-power, hap, sustainability]
related:
  - "[[guo-2026-uav-wsn-completion-time]]"
  - "[[wireless-power-transfer]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
created: 2026-05-29
updated: 2026-07-13
---

# RF Energy Harvesting

Conversion of ambient radio-frequency signals into usable DC energy for storage in a battery or capacitor. Lets energy-constrained nodes (UAVs, IoT sensors, [[high-altitude-platform-station|HAPS]]) extend operational lifetime by scavenging from existing transmissions rather than requiring dedicated charging infrastructure.

The harvested power is roughly $\eta \cdot P_{tx} \cdot |h|^2$ for incident power $P_{tx}|h|^2$ and conversion efficiency $\eta$ (typically 10–60% in current hardware). Two practical design knobs: time-sharing between transmission and harvesting (per-slot $\alpha$ in [[hsu-2025-drl-hues-hap-noma]]), and antenna placement to maximize incident power.

Distinct from [[wireless-power-transfer]] (a dedicated charger pushes energy on purpose) — RF harvesting *opportunistically* scavenges from signals sent for other purposes (uplink data, base-station broadcasts, etc.).

[[wang-2026-glint-aoi-wireless-powered-edge]] uses a dedicated-WPT rather than ambient-scavenging instance of the same RF-to-DC receiver process. Its sensor model includes sensitivity and saturation limits, and harvested energy gates whether a fresh update can be transmitted.
