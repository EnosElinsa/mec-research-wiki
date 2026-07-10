---
type: concept
title: "Selective Near-Field Area (SNA)"
tags: [near-field, xl-mimo, channel-modeling, complexity-reduction]
related:
  - "[[near-field-communications]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[terahertz-communication]]"
  - "[[bai-adaptive-near-field-xl-mimo-multi-uav]]"
created: 2026-07-11
updated: 2026-07-11
---

# Selective Near-Field Area (SNA)

A channel-modeling device for XL-MIMO UPAs: define a near-field region around the array and use spherical-wave calculations only for UAVs, clusters, or reflection points inside that region. Outside it, a plane-wave approximation is used to reduce computation.

In [[bai-adaptive-near-field-xl-mimo-multi-uav]], the SNA radius follows Rayleigh-distance logic for the UPA aperture. The point is not to deny near-field physics; it is to apply the expensive spherical-wave model only where it changes the channel enough to matter. That makes it a practical bridge between [[near-field-communications]] accuracy and the computational burden of simulating multi-UAV, low-THz, XL-MIMO channels.
