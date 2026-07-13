---
type: concept
title: "Improved Fast Base Station Selection"
tags: [isac, uav-swarm, localization, cramer-rao-bound, anchor-selection]
related:
  - "[[zhu-2025-green-isac-q-learning]]"
  - "[[crlb-initialized-q-table]]"
  - "[[tdoa-based-uav-localization]]"
  - "[[cramer-rao-bound]]"
created: 2026-07-14
updated: 2026-07-14
---

# Improved Fast Base Station Selection

Improved fast base station selection (FBSS) chooses a geometrically diverse subset of UAV anchors for TDOA localization. For each ground terminal, it takes the minimum-elevation UAV as a reference, groups candidates around several reference azimuths, enumerates one candidate per group, and selects the subset with the smallest positioning CRLB. Rotating the reference line and repeating the search reduces sensitivity to one angular partition.

In [[zhu-2025-green-isac-q-learning]], the selected subset supplies sensing prior information to resource-allocation agents. The method is a heuristic geometry search rather than a globally optimal subset solver; its reported positioning gains come from simulation under known UAV positions and Gaussian measurement error.
