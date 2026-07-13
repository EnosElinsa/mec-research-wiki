---
type: concept
title: "Wireless-Powered Underground Communication Network"
tags: [wireless-power-transfer, underground-iot, uav, data-collection]
related:
  - "[[lin-2026-uav-wpucn-time-allocation]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[underground-air-soil-wireless-channel]]"
created: 2026-07-14
updated: 2026-07-14
---

# Wireless-Powered Underground Communication Network

A network in which buried sensing devices harvest RF energy from above-ground infrastructure and spend that energy on an underground-to-air data return link. Soil attenuation, refraction at the air-soil boundary, burial depth, water content, and the cost of channel acquisition make this setting materially different from conventional above-ground WPCNs.

[[lin-2026-uav-wpucn-time-allocation]] combines a terrestrial hybrid access point with a rotary-wing UAV. The HAP charges the UAV, the HAP and UAV power underground devices, the devices upload by TDMA to the UAV, and the UAV returns to offload the collected data. Its time-allocation problem fixes the flight geometry and minimizes modeled UAV energy subject to per-device throughput and complete-offload constraints.
