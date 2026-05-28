---
type: concept
title: "Integrated Sensing and Communication (ISAC)"
tags: [isac, dual-function, beamforming, 6g]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[high-altitude-platform-station]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[jiang-2025-isac-lae-overview]]"
created: 2026-05-29
updated: 2026-05-29
---

# Integrated Sensing and Communication (ISAC)

A 6G design pattern in which the **same RF hardware and waveform** simultaneously serves communication users and senses targets via radar-style echo processing. The motivation is dual: cut hardware cost in half by sharing front ends, and extract sensing information (target position, velocity, RCS) from signals that are already in the air for communication.

Two competing design philosophies appear in the wiki:

- **Dual-function waveform** — beamforming matrix splits energy across communication and sensing streams. See [[benaya-2025-aerial-isac-haps]] for a HAPS-mounted full-duplex example.
- **Time-division multiplexing (TDM-ISAC)** — alternate slots between sensing and communication, simpler to implement.

ISAC complicates [[physical-layer-security]] because the sensing operation can leak information to an eavesdropper that's also being tracked. [[benaya-2025-aerial-isac-haps]] uses an aerial friendly jammer to neutralize this leak.

For a high-level survey of ISAC in the LAE context, see [[jiang-2025-isac-lae-overview]] and [[wang-2025-lae-network-survey]].
