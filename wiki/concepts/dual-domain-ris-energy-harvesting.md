---
type: concept
title: "Dual-Domain RIS Energy Harvesting"
tags: [ris, energy-harvesting, swipt, time-splitting, element-scheduling]
related:
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[peng-2023-dual-domain-eh-ris]]"
created: 2026-07-13
updated: 2026-07-13
---

# Dual-Domain RIS Energy Harvesting

Dual-domain RIS energy harvesting combines **time splitting** with **spatial element partitioning**. The surface first dedicates an energy-harvesting phase to all elements. During the information phase, selected elements reflect signals toward users while the remaining elements continue [[rf-energy-harvesting|harvesting RF energy]]. This extends time-only [[simultaneous-wireless-information-and-power-transfer|SWIPT]] by exploiting otherwise idle reflecting elements when not every element is needed for communication.

[[peng-2023-dual-domain-eh-ris]] implements the pattern as resource-allocation-based harvest-transmit-store operation on a [[uav-mounted-ris|UAV-mounted RIS]]. Its controller jointly chooses the time split, transmit powers, user-specific element schedules, and continuous phases. The benefit is an additional resource dimension, while the cost is a coupled non-convex problem with binary scheduling and unit-modulus constraints.
