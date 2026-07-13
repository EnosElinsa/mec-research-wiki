---
type: concept
title: "Robust UAV Network Slicing"
tags: [network-slicing, robust-optimization, imperfect-csi, uav-network]
related:
  - "[[wei-2026-runs-uav-network-slicing]]"
  - "[[network-slicing]]"
  - "[[chance-constraint]]"
  - "[[csi-estimation-error]]"
  - "[[dynamic-qos-constraints]]"
created: 2026-07-14
updated: 2026-07-14
---

# Robust UAV Network Slicing

Robust UAV network slicing jointly assigns slice-specific radio resources and aerial deployment while explicitly accounting for uncertain demand, user position, and channel state. It extends [[network-slicing]] from nominal service differentiation to decisions that remain feasible within stated uncertainty sets and outage tolerances.

[[wei-2026-runs-uav-network-slicing]] bounds demand and user-location errors by worst cases and converts Gaussian CSI error plus a per-channel SLA [[chance-constraint]] into a deterministic rate condition. Its RUNs solver eliminates altitude in closed form, alternates channel and power blocks inside an augmented-Lagrangian loop, and rounds relaxed channel counts through a constrained knapsack step. The guarantee is stationarity for the relaxed problem under stated conditions, not global optimality of the original mixed-integer formulation.
