---
type: concept
title: "Near-Field Communications"
tags: [near-field, xl-mimo, physical-layer, channel-modeling, 6g]
related:
  - "[[extremely-large-scale-mimo]]"
  - "[[wang-2024-xl-mimo-tutorial]]"
  - "[[bui-2025-noma-near-far-offloading]]"
  - "[[selective-near-field-area]]"
  - "[[bai-adaptive-near-field-xl-mimo-multi-uav]]"
created: 2026-06-02
updated: 2026-07-11
---

# Near-Field Communications

The communication regime that arises when the array aperture is large enough (as in [[extremely-large-scale-mimo|XL-MIMO]]) that users fall within the array's near field, so the wavefront across the array is **spherical** rather than planar. This invalidates the far-field planar-wave assumption used in conventional massive MIMO and changes channel modeling, performance analysis, beamforming, and applications.

Key consequences surveyed in [[wang-2024-xl-mimo-tutorial]]:

- **Channel modeling** must use spherical-wave models (uniform / non-uniform spherical wave for discrete antennas, Green's-function models for continuous apertures), with explicit distance boundaries / EM regions separating near- and far-field behavior.
- **Signal processing** needs near-field-specific schemes — e.g. polar-domain channel estimation and **near-field beam focusing** (focusing energy at a point rather than steering a far-field beam) — because far-field schemes mismatch the near-field channel.
- New opportunities include near-field beam focusing and near-field wireless energy transfer.

A physical-layer concept that now also appears inside MEC offloading. [[bui-2025-noma-near-far-offloading]] uses near-field spherical-wave channel modeling for users inside the UAV array's Rayleigh distance, while far-field users keep the planar-wave model; the distinction affects NOMA offloading, transmit power, and UAV compute allocation.

[[bai-adaptive-near-field-xl-mimo-multi-uav]] extends the channel-modeling side to XL-MIMO UPA-to-multi-UAV links at mmWave and low-THz frequencies. Its [[selective-near-field-area]] applies spherical-wave modeling only inside the region where near-field effects are material, trading accuracy against simulation complexity.
