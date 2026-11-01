---
type: concept
title: "HAP Solar-Propulsion Energy Balance"
tags: [high-altitude-platform-station, solar-energy-harvesting, propulsion-power, energy-budget]
related:
  - "[[high-altitude-platform-station]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[energy-harvesting-mec]]"
  - "[[javed-2023-hale-haps-noma-flight]]"
  - "[[xing-2026-genai-agent-hap-power-allocation]]"
  - "[[huang-2026-haps-sar-trajectory-resource]]"
  - "[[abderrahim-2024-data-center-hap]]"
  - "[[renga-2022-haps-sustainable-6g]]"
created: 2026-11-02
updated: 2026-11-02
---

# HAP Solar-Propulsion Energy Balance

The energy budget of a long-endurance high-altitude platform, where photovoltaic harvesting by day must pay for propulsion and station keeping, the communication, sensing, or computing payload, and battery charging for the night. Propulsion is usually the largest term and depends on airspeed, altitude, air density, and airframe aerodynamics, so flight parameters and payload power have to be designed together. Harvested power depends on latitude, day of year, and panel efficiency.

## In this wiki

- [[javed-2023-hale-haps-noma-flight]] chooses NOMA power coefficients, altitude, and airspeed to maximize daytime sum rate and then minimizes nighttime propulsion within stored energy.
- [[xing-2026-genai-agent-hap-power-allocation]] corrects the propulsion term for hull-propeller interference before allocating the remaining power to beamforming.
- [[huang-2026-haps-sar-trajectory-resource]] keeps the platform's energy state positive while splitting power among motion, SAR sensing, and backhaul, with solar harvesting as income.
- [[abderrahim-2024-data-center-hap]] uses the same harvesting model with low stratospheric temperature to argue for a flying data center.
- [[renga-2022-haps-sustainable-6g]] looks at the network side: HAPS offloading lets terrestrial base stations sleep and lowers grid energy.

The balance differs from rotary-wing UAV energy models, where hovering is costly and endurance is measured in minutes, and from [[energy-harvesting-mec]], where the harvesting node is usually a ground device.
