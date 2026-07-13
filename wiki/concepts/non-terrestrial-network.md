---
type: concept
title: "Non-Terrestrial Network (NTN)"
tags: [ntn, satellite, uav, architecture, 6g]
related:
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[service-caching-mec]]"
  - "[[three-dimensional-frequency-reuse]]"
  - "[[prabhath-not-in-parse-3d-space-spectrum-utilization]]"
  - "[[huang-2026-uav-friendly-jamming-transsac]]"
created: 2026-05-29
updated: 2026-07-13
---

# Non-Terrestrial Network (NTN)

A network architecture composed of airborne and spaceborne nodes — LEO satellites, HAPs, and UAVs — that provide seamless, ubiquitous coverage where terrestrial infrastructure is absent or unreliable. NTNs are a building block of the broader [[space-air-ground-integrated-network]] vision.

In [[mao-2024-ntn-hierarchical-caching-cav]], an NTN of LEO satellites and UAVs provides hierarchical content caching for connected automated vehicles; caching-satellite selection is posed as a weighted minimum-vertex-cover problem (solved by delay-motivated ant colony optimization) and caching capacity managed by multi-agent DRL. NTN-hosted edge computing connects to [[leo-satellite-edge-computing]] and [[service-caching-mec]].

[[prabhath-not-in-parse-3d-space-spectrum-utilization]] is adjacent to NTN planning rather than edge computing: its 3-D frequency-reuse and SUE framework is written for UAV-enabled cellular networks and explicitly frames extension to space-air-ground integrated networks as future adaptation work.

[[morshed-2026-active-ris-uav-noma-mappo]] studies a compact terrestrial/non-terrestrial instance: a serving BS and interfering BS communicate with mobile NOMA users through one UAV-mounted active RIS, with subsystem-specific actors coordinated by [[decentralized-active-ris-uav-noma-control]].
