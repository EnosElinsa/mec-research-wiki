---
type: concept
title: "Energy-Causality Constraint"
tags: [energy-harvesting, wireless-power-transfer, constraint, scheduling]
related:
  - "[[wang-2018-uav-powered-d2d]]"
  - "[[harvest-transmit-store-scheduling]]"
  - "[[energy-harvesting-mec]]"
  - "[[rf-energy-harvesting]]"
  - "[[wireless-power-transfer]]"
created: 2026-07-14
updated: 2026-07-14
---

# Energy-Causality Constraint

An energy-causality constraint requires cumulative consumed energy through every time step to remain no greater than the initial plus cumulatively harvested energy. It prevents an optimizer from spending future harvested energy before that energy becomes available.

[[wang-2018-uav-powered-d2d]] applies the constraint to cochannel D2D transmitters charged by a fixed UAV. Together with stored energy, it couples every slot to the preceding harvest history and supports the paper's derived harvest-first, transmit-later structure.
