---
type: concept
title: "RIS-Assisted Directional Jamming"
tags: [covert-communication, cooperative-jamming, uav-mounted-ris, physical-layer-security]
related:
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[covert-communication]]"
  - "[[cooperative-jamming]]"
  - "[[uav-mounted-ris]]"
  - "[[physical-layer-security]]"
created: 2026-07-11
updated: 2026-07-11
---

# RIS-Assisted Directional Jamming

RIS-assisted directional jamming uses a reconfigurable surface to steer a helper jammer's artificial noise toward a warden or eavesdropper without requiring the jammer itself to occupy a favorable direct-link position.

In [[zhang-2026-air-ground-covert-jamming]], the RIS is carried by a decode-and-forward UAV. A terrestrial friendly jammer emits artificial noise, while the UAV-mounted RIS configures reflection coefficients and phase shifts so the jamming energy is focused toward Willie. This differs from ordinary [[cooperative-jamming]] because the helper's geographic exposure is partly decoupled from the surveillance region, and it differs from rate-oriented [[uav-mounted-ris]] work because the RIS is mainly a security-control surface.

The control problem is coupled: UAV motion changes both the relay channel and the jammer-RIS-Willie path, while the RIS must protect Bob's reception and preserve the covertness constraint. The source page solves the static jamming/RIS parameters with SDR, Dinkelbach iterations, and randomization, then wraps them in a DDQN trajectory and scheduling loop.
