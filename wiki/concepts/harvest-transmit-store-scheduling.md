---
type: concept
title: "Harvest-Transmit-Store Scheduling"
tags: [energy-harvesting, scheduling, wireless-power-transfer, energy-causality]
related:
  - "[[wang-2018-uav-powered-d2d]]"
  - "[[energy-causality-constraint]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[device-to-device-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Harvest-Transmit-Store Scheduling

Harvest-transmit-store scheduling lets wireless devices collect dedicated RF energy, retain unused energy across slots, and later spend it on payload transmission. The scheduler trades additional charging time against the reduced number of information slots while enforcing cumulative [[energy-causality-constraint|energy causality]].

In [[wang-2018-uav-powered-d2d]], Lagrangian analysis yields a common binary mode per slot and a single switch: all harvesting slots precede all transmission slots. Successive difference-of-convex power updates and a discrete golden-section search produce a suboptimal schedule for mutually interfering D2D pairs.
