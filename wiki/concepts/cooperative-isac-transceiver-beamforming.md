---
type: concept
title: "Cooperative ISAC Transceiver Beamforming"
tags: [isac, cooperative-sensing, beamforming, scnr, distributed-optimization]
related:
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fractional-programming-dinkelbach]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cooperative ISAC Transceiver Beamforming

Cooperative ISAC transceiver beamforming coordinates multiple cellular base stations' sensing and downlink beams so target echoes can be strengthened while inter-cell interference, clutter, residual self-interference, user SINR, and per-BS power limits are handled jointly.

[[zhang-2025-cooperative-anti-uav-isac]] maximizes anti-UAV sensing SCNR with alternating receive/transmit updates. Its centralized solver uses global CSI; its primal-decomposition variant exchanges interference multipliers and solves local convex subproblems. This is a [[networked-isac]] beam-design problem, distinct from the corpus's virtual-array meaning of [[collaborative-beamforming]].
