---
type: concept
title: "Sparrow Search Algorithm"
tags: [swarm-intelligence, metaheuristic, optimization, uav-deployment]
related:
  - "[[particle-swarm-optimization]]"
  - "[[salp-swarm-algorithm]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Sparrow Search Algorithm

A swarm-intelligence metaheuristic that evolves a population of candidate solutions through producer, scrounger, and warning/anti-predation roles. In this wiki it appears as a UAV-deployment optimizer rather than a full MEC offloading controller.

[[li-2026-isac-vec-beamforming-deployment]] uses an improved SSA with refraction-based learning to optimize UAV deployment positions in an ISAC-enhanced UAV-assisted VEC system. The beamforming block is then handled by SCA and first-order Taylor convexification, so SSA is an embedded deployment sub-solver inside a larger block-coordinate optimization pipeline.

This places sparrow search near [[particle-swarm-optimization]] and [[salp-swarm-algorithm]] in the corpus's swarm-metaheuristic family, but its role here is narrower: mixed, non-convex UAV placement under communication/sensing/energy tradeoffs. The acronym is intentionally avoided in page titles because salp swarm is already abbreviated SSA in this wiki.
