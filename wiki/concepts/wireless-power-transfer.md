---
type: concept
title: Wireless Power Transfer (WPT) for MEC
tags: [wpt, energy-harvesting, mec]
related:
  - "[[mobile-edge-computing]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[hu-2026-latency-hybrid-uav-mec]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[wu-2026-parallel-cooperative-charging]]"
  - "[[parallel-cooperative-uav-charging]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
created: 2026-05-28
updated: 2026-07-12
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

[[zhao-2026-adaptive-wdc-wet-lae]] uses UAV WET as a service-balancing objective in a low-altitude IoT network. E-devices harvest RF energy under a nonlinear EH model, while I-devices require WDC freshness; the controller adapts the WDC/WET preference instead of fixing the scalarization weight.

[[shi-2025-aoi-energy-replenishment-multiuav]] uses UAV-to-sensor wireless energy transfer as the first stage of each fresh-data-collection slot: a UAV charges an associated sensor node, the node uses that harvested energy to upload an update, and the UAV later recharges at a fixed charging station.

[[wu-2026-parallel-cooperative-charging]] uses RF transfer in the opposite direction: provider-operated facilities recharge UAV batteries. The contribution is [[parallel-cooperative-uav-charging]] across shared-cost station groups and parallel facility queues rather than harvest/offload time allocation.

Two trajectory-control cases expose opposite WPT directions. [[wang-2026-wutf-fair-communication]] lets ground towers replenish UAV base stations while [[wireless-powered-uav-fair-service-control]] balances user fairness against flight energy. [[wang-2026-glint-aoi-wireless-powered-edge]] instead lets UAVs charge sensor batteries before fresh-data upload, with [[dual-network-sequential-aoi-control]] separating mobility/association from charging and transmission scheduling.

## Why "long-term" matters

A naive per-slot greedy ignores the energy queue: if you spend the harvest immediately, you starve future-slot tasks that need the buffered energy. The right framing is **long-term energy efficiency** under queue stability — see [[lyapunov-optimization]] and [[zhu-2025-lycnn-drl-wpt-mec]].
