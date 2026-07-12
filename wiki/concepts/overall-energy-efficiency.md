---
type: concept
title: "Overall Energy Efficiency"
tags: [metric, energy-efficiency, haps, uav, data-collection, fractional-programming]
related:
  - "[[fan-2026-hap-uav-iort-oee]]"
  - "[[high-altitude-platform-station]]"
  - "[[uav-data-collection]]"
  - "[[information-causality-constraint]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[effective-energy-efficiency]]"
created: 2026-07-12
updated: 2026-07-12
---

# Overall Energy Efficiency

Overall energy efficiency (OEE) is a whole-chain data-per-energy metric for two-hop IoRT collection through UAVs and HAPs. In [[fan-2026-hap-uav-iort-oee]], the numerator is the bottleneck amount successfully carried across IoRT-UAV and UAV-HAP links, while the denominator includes UAV transmit/propulsion energy and HAP propulsion energy.

The ratio couples [[uav-data-collection]], HAP selection, bandwidth, power, and both aerial trajectories, so it is handled through [[fractional-programming-dinkelbach]] plus block-coordinate SCA. It is related to [[effective-energy-efficiency]] by objective form but is not the same metric: OEE measures relayed data, whereas that page's integrated communication-computation use combines broader utility terms.
