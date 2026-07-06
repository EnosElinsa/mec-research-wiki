---
type: concept
title: "Friendly-Jamming UAV"
tags: [security, jamming, uav, secrecy, pls]
related:
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
created: 2026-05-29
updated: 2026-07-07
---

# Friendly-Jamming UAV

An aerial node that deliberately transmits noise-like or interfering signals **toward eavesdroppers** to lower their effective receive SINR while leaving legitimate receivers' SINR mostly intact. UAVs are well-suited because they can re-position to maximize the eavesdropper-channel-vs-victim-channel gap.

The optimization variables are typically jamming power, jamming waveform, and **UAV trajectory**. Trajectory matters more than power: bringing the jammer 5 m closer to the eavesdropper (and not the user) often beats doubling jamming power.

Used in [[benaya-2025-aerial-isac-haps]] alongside HAPS beamforming and ISAC-based eavesdropper localization. The UAV trajectory there is jointly optimized with the HAPS beamformer via alternating optimization.

In [[wang-2026-secure-lae-uav-scheduling]], the same UAV fleet can switch between communication-UAV and jamming-UAV roles across slots, so friendly jamming becomes a scheduling and trajectory decision rather than a fixed helper assignment.

A friendly jammer is a pure helper, distinct from an *adversarial* jammer (which is a threat to be mitigated). Both share the math; only the labels differ.
