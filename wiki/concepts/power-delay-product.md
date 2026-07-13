---
type: concept
title: "Power-Delay Product"
tags: [metric, power, delay, neighbor-discovery, energy-efficiency]
related:
  - "[[fan-2026-directional-neighbor-discovery]]"
  - "[[energy-latency-tradeoff]]"
created: 2026-07-13
updated: 2026-07-13
---

# Power-Delay Product

A multiplicative efficiency metric defined as average operating power times completion delay. In [[fan-2026-directional-neighbor-discovery]], node `i` has `C_i = D_i * P_i`, so a policy cannot improve the metric merely by discovering rapidly at extreme radio power or by listening cheaply for an arbitrarily long time.

This differs from a weighted-sum [[energy-latency-tradeoff]]: multiplication fixes no explicit preference coefficient and has units that depend on how delay and power are measured. It is also not total mission energy when propulsion, switching, computation, or other power states are omitted.
