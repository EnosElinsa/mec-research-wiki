---
type: concept
title: "Integrated Sensing and Communication (ISAC)"
tags: [isac, dual-function, beamforming, 6g]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[huang-2026-offgrid-lae-imager]]"
  - "[[hou-2025-pbia-air-iscc-uav-its]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[ye-2026-mode-lae-isac]]"
  - "[[networked-isac]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
  - "[[li-2026-control-based-uav-isac]]"
  - "[[control-parameterized-uav-trajectory]]"
created: 2026-05-29
updated: 2026-07-10
---

# Integrated Sensing and Communication (ISAC)

A 6G design pattern in which the **same RF hardware and waveform** simultaneously serves communication users and senses targets via radar-style echo processing. The motivation is dual: cut hardware cost in half by sharing front ends, and extract sensing information (target position, velocity, RCS) from signals that are already in the air for communication.

Two competing design philosophies appear in the wiki:

- **Dual-function waveform** — beamforming matrix splits energy across communication and sensing streams. See [[benaya-2025-aerial-isac-haps]] for a HAPS-mounted full-duplex example.
- **Time-division multiplexing (TDM-ISAC)** — alternate slots between sensing and communication, simpler to implement.

ISAC complicates [[physical-layer-security]] because the sensing operation can leak information to an eavesdropper that's also being tracked. [[benaya-2025-aerial-isac-haps]] uses an aerial friendly jammer to neutralize this leak.

For a high-level survey of ISAC in the LAE context, see [[jiang-2025-isac-lae-overview]] and [[wang-2025-lae-network-survey]]. The corpus now also has LAE control instances: [[ye-2026-deeplsc-lae-isac]] uses DDPG to jointly control GBS beamforming and UAV trajectories for sum-rate under sensing constraints, while [[ye-2026-meta-deepesc-lae-isac]] shifts the objective to energy efficiency and adds meta-learning for flight-period adaptation. [[ye-2026-mode-lae-isac]] turns that LAE line into a multi-objective communication/sensing controller using [[mixture-of-experts-drl]], and [[zhao-2025-networked-isac-uav-handover]] moves from single-cell ISAC links to multi-BS [[networked-isac]] tracking and sensing-cell handover. In VEC, [[li-2026-isac-vec-beamforming-deployment]] uses ISAC metrics to jointly shape UAV deployment and beamforming for temporary road hot spots.

[[huang-2026-offgrid-lae-imager]] adds a cooperative cellular-ISAC imaging view: multiple BSs use raw CSI to reconstruct sparse low-altitude aerial images and mitigate off-grid errors with physics-embedded learning. [[hou-2025-pbia-air-iscc-uav-its]] extends the same sensing/communication substrate into Air-ISCC, where UAV swarms also compute IoTD tasks in ITS scenarios.

[[wang-2026-stbc-cooperative-isac]] adds the shared-resource physical-layer version: multi-BS cooperative ISAC uses robust inter-BS nulling, a [[space-time-block-codec]], and SINR-weighted data fusion to sense low-altitude UAVs near cell edges without allocating fully orthogonal resources.

[[li-2026-control-based-uav-isac]] adds a control-theoretic UAV-ISAC design: communication/sensing beamforming is optimized with SCA/SDR, while the UAV trajectory is represented through 3-DoF or 6-DoF dynamics and [[control-parameterized-uav-trajectory|control parameterization]] so planned sensing constraints remain meaningful for actual flight.
