---
type: concept
title: "Beyond-Diagonal Reconfigurable Intelligent Surface"
tags: [ris, beyond-diagonal-ris, group-connected, metasurface, wireless-communication]
related:
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[fully-connected-ris]]"
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[rate-splitting-multiple-access]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
created: 2026-07-13
updated: 2026-07-14
---

# Beyond-Diagonal Reconfigurable Intelligent Surface

A beyond-diagonal RIS (BD-RIS, also called RIS 2.0) allows electrical coupling among surface cells, so its scattering matrix is not restricted to the independent diagonal phase shifts used by a conventional [[intelligent-reflecting-surface]]. A group-connected architecture partitions cells into smaller coupled clusters, trading richer wave transformations against additional inter-cell circuitry and configuration cost.

[[huroon-2026-bd-ris-rsma-uav]] fixes a group-connected BD-RIS to a building facade and assigns at most one surface cluster to each assisted UAV group. Its optimizer jointly handles discrete cluster assignment, unitary scattering matrices, [[rate-splitting-multiple-access]], UAV motion, and transmit precoding.

BD-RIS does not imply an active amplifier or an airborne surface. The cited design is passive and ground-mounted; its distinction from [[uav-mounted-ris]] is both the surface topology and the deployment location.

[[lin-2026-fc-ris-surveillance]] uses the fully connected subtype, whose ideal symmetric-unitary scattering matrix couples all elements, on a UAV-borne surface for legitimate monitoring.
