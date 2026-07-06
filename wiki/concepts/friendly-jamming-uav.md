---
type: concept
title: "Friendly-Jamming UAV"
tags: [security, jamming, uav, secrecy, pls]
related:
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[wu-2026-secure-split-offloading-ci]]"
  - "[[wu-2025-security-aware-multiuav-service-placement]]"
created: 2026-05-29
updated: 2026-07-07
---

# Friendly-Jamming UAV

An aerial node that deliberately transmits noise-like or interfering signals **toward eavesdroppers** to lower their effective receive SINR while leaving legitimate receivers' SINR mostly intact. UAVs are well-suited because they can re-position to maximize the eavesdropper-channel-vs-victim-channel gap.

The optimization variables are typically jamming power, jamming waveform, and **UAV trajectory**. Trajectory matters more than power: bringing the jammer 5 m closer to the eavesdropper (and not the user) often beats doubling jamming power.

Used in [[benaya-2025-aerial-isac-haps]] alongside HAPS beamforming and ISAC-based eavesdropper localization. The UAV trajectory there is jointly optimized with the HAPS beamformer via alternating optimization.

In [[wang-2026-secure-lae-uav-scheduling]], the same UAV fleet can switch between communication-UAV and jamming-UAV roles across slots, so friendly jamming becomes a scheduling and trajectory decision rather than a fixed helper assignment.

[[cai-2026-llm-drl-secure-lae-data]] uses a dedicated jamming UAV alongside a data-collection UAV in low-altitude economy networking, with LLM-enhanced DRL balancing secrecy, AoI, and UAV energy.

Newer secure-offloading entries reuse the same aerial helper role in different workloads: [[beishenalieva-2026-secrecy-aware-uav-path-planning]] protects ITS sensing/offloading data against malicious UAVs, [[wu-2026-secure-split-offloading-ci]] protects intermediate feature data in collaborative inference, and [[wu-2025-security-aware-multiuav-service-placement]] protects service-placement-aware computation offloading.

A friendly jammer is a pure helper, distinct from an *adversarial* jammer (which is a threat to be mitigated). Both share the math; only the labels differ.
