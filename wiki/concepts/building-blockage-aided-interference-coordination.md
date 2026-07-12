---
type: concept
title: "Building-Blockage-Aided Interference Coordination"
tags: [blockage, interference, uav-communications, trajectory-optimization, urban]
related:
  - "[[heo-not-in-parse-blockage-aided-multiuav-interference]]"
  - "[[blockage-aware-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
created: 2026-07-11
updated: 2026-07-11
---

# Building-Blockage-Aided Interference Coordination

Building-blockage-aided interference coordination deliberately uses urban obstructions to weaken interfering links while preserving line-of-sight service links. The key move is to treat NLoS status as a controllable resource for interference management, not only as a channel impairment.

[[heo-not-in-parse-blockage-aided-multiuav-interference]] models cuboid buildings, classifies signal and interference links as LoS or NLoS by geometric intersection, and jointly optimizes UAV trajectories, scheduling, and transmit power. Desired UAV-GN links are kept LoS, while selected co-channel interference links are made NLoS through offset UAV positions.

This concept is narrower than [[blockage-aware-channel-model]]. A blockage-aware model may simply predict or avoid blocked links; blockage-aided coordination actively exploits the blockage geometry to shape the interference graph.
