---
type: concept
title: "Terrain-Aware Channel Model"
tags: [channel-model, dem, blockage, urban, geometric]
related:
  - "[[blockage-aware-channel-model]]"
  - "[[csi-estimation-error]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
created: 2026-05-29
updated: 2026-06-01
---

# Terrain-Aware Channel Model

A geometric channel model that uses **real-world Digital Elevation Model (DEM) data** to predict whether the air-to-ground link between a UAV and a ground user is line-of-sight or blocked, and to estimate the resulting path loss.

The construction in [[wu-2026-terrain-aware-uav-mec]]:

1. Discretize terrain (DEM + buildings) into a 3D mesh.
2. For each user device (UD), sweep vectors from the UD outward to surrounding mesh points to identify the **blocked region** (the half-space where the UD is occluded from the UAV).
3. UAV positions outside the blocked region see LoS; positions inside see NLoS.
4. Path loss = function of Euclidean distance between UAV and the boundary of the blocked region.

Distinct from:

- **Statistical** LoS-probability models (sigmoid of elevation angle) — fast but inaccurate in valleys / behind ridges.
- **Radio-map / measurement-based** models — accurate but require expensive offline data collection.

The terrain-aware model is a deterministic-geometric channel model — distinct from the statistical LoS-probability models used across most aerial-MEC sources in the corpus (see [[blockage-aware-channel-model]]). It also makes UAV destination selection a natural decision variable, since "where to land" depends on the *exact* blocked-region geometry around each candidate destination.
