---
type: concept
title: "Secure IRS-UAV ISAC"
tags: [isac, uav-mounted-ris, physical-layer-security, artificial-noise, robust-optimization]
related:
  - "[[guo-2026-irs-uav-isac-secrecy]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-mounted-ris]]"
  - "[[physical-layer-security]]"
  - "[[artificial-noise-aided-physical-layer-security]]"
  - "[[robust-ris-assisted-uav-secrecy]]"
  - "[[closed-form-irs-phase-alignment]]"
created: 2026-07-14
updated: 2026-07-14
---

# Secure IRS-UAV ISAC

Secure IRS-UAV ISAC uses a UAV-mounted reflecting surface as a mobile propagation-control layer for [[integrated-sensing-and-communication]]. UAV motion, IRS phases, active beams, and artificial noise can be coordinated to strengthen legitimate links and sensing while suppressing an eavesdropper.

[[guo-2026-irs-uav-isac-secrecy]] instantiates this architecture with a passive [[uav-mounted-ris]], a sensing subslot, and a communication-plus-noise subslot. It maximizes sum secrecy rate subject to an accumulated sensing-SNR requirement and also considers bounded channel and target-angle errors, connecting the design to [[robust-ris-assisted-uav-secrecy]].

This is an architecture pattern rather than a general security guarantee. The supporting design assumes one fixed-altitude IRS-UAV, continuous unit-amplitude phases, centralized channel knowledge, one stationary target, and one eavesdropper; its robust solutions remain local and simulation-based, with no phase quantization, attitude jitter, control overhead, or hardware validation.
