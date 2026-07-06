---
type: concept
title: "Energy Procurement Compensation"
tags: [energy-management, incentive-mechanism, uav-mec]
related:
  - "[[wireless-power-transfer]]"
  - "[[energy-harvesting-mec]]"
  - "[[task-offloading]]"
  - "[[stackelberg-game]]"
  - "[[reverse-auction-incentive]]"
  - "[[panahi-2026-uav-green-iot-offloading]]"
  - "[[wang-2025-airground-laser-mec]]"
created: 2026-07-06
updated: 2026-07-06
---

# Energy Procurement Compensation

Energy procurement compensation treats a UAV-MEC platform as both an energy buyer and a service seller. The UAV pays for externally supplied energy, such as laser power from ground laser beam directors, while receiving revenue for computation offloading service or wireless charging service. The optimization target is therefore not only physical energy consumption, but the net procurement cost after service compensation.

In [[panahi-2026-uav-green-iot-offloading]], the UAV buys laser energy, uses local renewable energy, stores battery energy, and offsets procurement cost by charging IoT devices for COF and [[wireless-power-transfer]] service. This complements [[wang-2025-airground-laser-mec]], where laser charging sustains a UAV's MEC / relay role but service-pricing compensation is not the central modeling object.

This concept sits near market and incentive mechanisms such as [[stackelberg-game]] pricing and [[reverse-auction-incentive]], but the distinctive variable is energy-accounting: procurement cost, conversion losses, service income, and feasible offloading coverage are coupled.
