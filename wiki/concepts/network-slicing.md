---
type: concept
title: "Network Slicing"
tags: [architecture, resource-virtualization, sagin, economics]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[traffic-aware-offloading]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[ammar-2026-oran-maritime-slicing]]"
  - "[[wei-2026-runs-uav-network-slicing]]"
  - "[[robust-uav-network-slicing]]"
created: 2026-05-29
updated: 2026-07-14
---

# Network Slicing

Virtualizing physical communication and computing resources into independently-managed, rentable **slices** that can be provisioned on demand for different tenants or service classes. An Infrastructure Provider (InP) owns the physical resources and sells slices; an Edge Service Provider (ESP) rents and dynamically resizes slices to serve users, earning revenue from completed tasks.

In the wiki, [[chen-2024-thoas-traffic-aware-sagin]] makes slicing first-class for SAGIN: it splits the network into Communication Access Platforms (subchannel slices) and Computation Offloading Platforms (VM slices), and adjusts slices only when the expected profit gain exceeds the **service-interruption cost** of re-slicing. This couples tightly with [[traffic-aware-offloading]] (predict load, then size slices) and the [[hierarchical-aerial-mec]] tier structure.

[[wei-2026-runs-uav-network-slicing]] adds [[robust-uav-network-slicing]] for an aerial radio-access network: slice channel counts, powers, and UAV deployment are optimized under bounded demand/location uncertainty and Gaussian CSI error. Its structured RUNs solver is optimization-based rather than a learned slicing policy.
