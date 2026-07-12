---
type: concept
title: "Blockage-Aware Channel Model"
tags: [channel-model, blockage, urban, los-nlos]
related:
  - "[[terrain-aware-channel-model]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[building-blockage-aided-interference-coordination]]"
  - "[[heo-not-in-parse-blockage-aided-multiuav-interference]]"
  - "[[ning-2025-channel-aware-irs-uav]]"
  - "[[dynamic-irs-user-association]]"
  - "[[zhao-2026-dt-ddqn-bisd-deployment]]"
created: 2026-05-29
updated: 2026-07-12
---

# Blockage-Aware Channel Model

A general family of channel models that explicitly account for **blockages** (buildings, trees, terrain) between transmitter and receiver, in contrast with statistical pathloss models that treat the environment as a homogeneous attenuator.

Three sub-families:

- **Statistical with elevation-angle LoS-probability** — sigmoid of elevation angle, fast, ignores actual obstacles. Used in [[hsu-2025-drl-hues-hap-noma]], [[bao-2025-ddpg-video-offloading]], and many others in the wiki.
- **Radio-map** — train a predictor on offline measurements; accurate but expensive to deploy and maintain.
- **Geometric** — use map data (3D building geometry, DEM elevation) to deterministically classify LoS/NLoS. The [[terrain-aware-channel-model]] in [[wu-2026-terrain-aware-uav-mec]] is a geometric variant that handles rough topography on top of buildings.

Choice depends on what data is available. Terrain-aware geometric models are increasingly tractable thanks to public DEM datasets, and they avoid the bias of fixed statistical curves.

[[heo-not-in-parse-blockage-aided-multiuav-interference]] adds a multi-UAV communication variant: cuboid buildings classify both desired and interference links as LoS/NLoS, and [[building-blockage-aided-interference-coordination]] deliberately uses NLoS interference links to improve spectral efficiency while keeping desired links LoS.

[[ning-2025-channel-aware-irs-uav]] uses geometric blockage state to trigger reflected support and change [[dynamic-irs-user-association]] jointly with UAV motion.
