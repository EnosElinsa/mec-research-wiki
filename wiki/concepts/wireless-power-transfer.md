---
type: concept
title: Wireless Power Transfer (WPT) for MEC
tags: [wpt, energy-harvesting, mec]
related:
  - "[[mobile-edge-computing]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[hu-2026-latency-hybrid-uav-mec]]"
created: 2026-05-28
updated: 2026-07-07
---

# Wireless Power Transfer (WPT) for MEC

A power-delivery scheme in which a dedicated power station radiates RF energy that is harvested by wireless devices, either to top up onboard batteries or to power immediate operation. Combining WPT with MEC creates **WPT-MEC**: devices harvest energy in part of each time slot, then spend it on local compute or task offloading.

## Why MEC research cares

- **Sustainability** — battery-operated IoT devices are the binding endurance constraint in many MEC scenarios. WPT extends operating life without manual intervention.
- **Optimization knob** — *how long* to harvest vs *how long* to offload becomes a per-slot decision variable. This adds another lever to the joint design space.

## Per-slot resource breakdown (canonical model)

Total slot duration $T$ is split between:

1. **WPT duration $\tau_0$** — power station broadcasts; devices harvest.
2. **Per-device offloading window** $\tau_i$ — only for devices that chose to offload this slot.
3. **Local compute** — happens for devices that chose local; uses the energy harvested in step 1.

Joint optimization picks $\{\tau_0, \tau_1, \ldots, \tau_N, \mathbf x, \mathbf f, \mathbf p\}$ where $\mathbf x$ is the binary offloading vector, $\mathbf f$ is local CPU frequencies, $\mathbf p$ is transmit powers.

[[hu-2026-latency-hybrid-uav-mec]] uses the UAV itself as the RF energy transmitter in a hybrid UAV-GBS MEC system: users harvest energy from the UAV while offloading latency-critical task bits for local, UAV-side, or GBS-side execution.

## Why "long-term" matters

A naive per-slot greedy ignores the energy queue: if you spend the harvest immediately, you starve future-slot tasks that need the buffered energy. The right framing is **long-term energy efficiency** under queue stability — see [[lyapunov-optimization]] and [[zhu-2025-lycnn-drl-wpt-mec]].
