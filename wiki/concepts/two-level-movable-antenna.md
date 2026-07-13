---
type: concept
title: "Two-Level Movable Antenna"
tags: [movable-antenna, uav-swarm, mimo, near-field-communications, low-altitude-economy]
related:
  - "[[lu-2026-uav-swarm-two-level-ma]]"
  - "[[movable-antenna]]"
  - "[[near-field-communications]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[collaborative-beamforming]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[wan-2026-movable-antenna-multiuav-mimo]]"
created: 2026-07-07
updated: 2026-07-13
---

# Two-Level Movable Antenna

A two-level movable antenna system uses mobility at two scales: first, the UAV swarm's 3D positions act as a large movable array; second, each UAV's onboard antenna elements can move locally within a bounded array. In [[lu-2026-uav-swarm-two-level-ma]], these two position layers are jointly optimized with receive beamforming to maximize the minimum uplink user rate in a low-altitude economy network.

This extends [[movable-antenna]] from per-platform element repositioning to swarm-level geometry control. It also overlaps with [[collaborative-beamforming]], but the paper's core decision is physical placement for rate balancing under near-field LoS channels rather than excitation-weight design for a fixed virtual antenna array.

[[wan-2026-movable-antenna-multiuav-mimo]] uses the same macro/micro distinction for independent UAV transmitters: whole-UAV positions and local array elements are selected from hierarchical dictionaries while WMMSE updates uplink precoders and BS combiners.
