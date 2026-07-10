---
type: concept
title: "Effective Energy Efficiency"
tags: [metric, energy-efficiency, communication-computation, resource-allocation]
related:
  - "[[cui-2026-aris-v2x-icac]]"
  - "[[vehicular-mec]]"
  - "[[active-ris]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[energy-latency-tradeoff]]"
created: 2026-07-10
updated: 2026-07-10
---

# Effective Energy Efficiency

Effective energy efficiency is a system-level ratio metric for integrated communication and computation systems. In [[cui-2026-aris-v2x-icac]], it combines network energy cost with communication and computation utilities, so the optimizer is not only minimizing energy or maximizing rate but balancing task offloading, local computation, communication links, and ARIS/UAV power consumption.

The metric is handled with [[fractional-programming-dinkelbach]] inside a BCD resource-allocation loop. It is the ARIS/V2X counterpart to energy-efficiency objectives elsewhere in the corpus, but its numerator explicitly includes both communication and computation utility.
