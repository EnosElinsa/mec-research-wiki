---
type: concept
title: "Ground-to-UAV Free-Space Optical Channel"
tags: [fso, air-to-ground, optical-wireless, uav, channel-model]
related:
  - "[[kamatchi-2025-slipt-uav-fso]]"
  - "[[simultaneous-lightwave-information-and-power-transfer]]"
  - "[[fov-aware-optical-uav-reception]]"
  - "[[air-to-ground-channel-model]]"
created: 2026-07-14
updated: 2026-07-14
---

# Ground-to-UAV Free-Space Optical Channel

A ground-to-UAV free-space optical channel models an upward optical link whose received intensity is jointly shaped by atmospheric attenuation, turbulence, beam misalignment, and receiver orientation. [[kamatchi-2025-slipt-uav-fso]] combines Beer-Lambert attenuation, Malaga turbulence, nonzero-boresight pointing error, and field-of-view interruption caused by excessive angle of arrival.

This is an optical counterpart to the broader [[air-to-ground-channel-model]], not a generic UAV channel. The cited formulation assumes a hovering UAV, Gaussian position/orientation deviations, modified-Rayleigh approximations, and quasi-static single-link operation; it is not validated against flight measurements and does not model trajectory-dependent blockage or handover.
