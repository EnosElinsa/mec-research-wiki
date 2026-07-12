---
type: concept
title: Mobile Edge Computing (MEC)
tags: [edge-computing, latency, 5g, 6g]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[dong-2026-digital-tides-provisioning]]"
created: 2026-05-28
updated: 2026-07-13
---

# Mobile Edge Computing (MEC)

A computing paradigm that pushes compute and storage to the radio-access edge so latency-sensitive workloads can be served close to the data source. Originally proposed in the context of 5G to bypass the round-trip to centralized clouds.

In the IoT setting, MEC servers (or [[multi-uav-assisted-mec|airborne UAV-MEC nodes]]) host the offloaded compute. Devices choose, per task, how much of the workload to offload via $\lambda_{u,d,n}$ vs run locally — see [[task-offloading]].

## Trade-off model used in this wiki

For a single offloaded task, the cost function decomposes into:

- transmission delay/energy (uplink)
- compute delay/energy (server-side)
- transmit-back delay/energy (downlink, results)
- local-compute delay/energy (the unoffloaded fraction)

Energy is approximated with the standard $\eta f^3 T$ cubic-frequency rule for both ends. See `wiki/sources/liu-2026-jppo-en-convntm.md` for the full equations.

## Key references

- Hu et al. (2015) — early MEC architectures for task offloading [13]
- Mao et al. (2017) — communication-perspective survey [11]
- Zeng et al. (2016) — UAV + wireless intersection [14]
