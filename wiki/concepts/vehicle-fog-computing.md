---
type: concept
title: "Vehicle Fog Computing (VFC)"
tags: [fog-computing, vehicular, edge-computing, post-disaster]
related:
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
  - "[[wei-2026-airfogsim-uav-vfc]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[vehicular-mec]]"
  - "[[post-disaster-mec]]"
created: 2026-05-29
updated: 2026-07-06
---

# Vehicle Fog Computing (VFC)

A fog-computing paradigm that pools the idle computation resources of nearby vehicles into a distributed compute layer at the network edge, complementing MEC servers. It is useful where infrastructure is scarce or overloaded — for example, post-disaster rescue, where ground vehicles can host fog nodes.

In [[sun-2024-mvtora-postdisaster-vfc]], VFC forms the lowest tier of a three-layer (vehicle-fog / UAV-client / UAV-edge) post-disaster architecture; VFC resource allocation is solved by an evolutionary-computation hybrid while UAV-MEC allocation is solved by convex optimization. [[wei-2026-airfogsim-uav-vfc]] contributes reusable simulation infrastructure for UAV-integrated VFC, including traffic, mobility, communication, computation, security/privacy, blockchain, and scheduling modules. VFC extends the [[vehicular-mec]] and [[three-tier-cloud-edge-end]] threads toward [[post-disaster-mec]].
