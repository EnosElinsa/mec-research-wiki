---
type: concept
title: "Networked ISAC"
tags: [isac, sensing, cooperation, handover]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[seamless-handover]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[tang-2025-cooperative-isac-lae]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
  - "[[yan-not-in-parse-multibs-isac-uav-trajectory]]"
  - "[[multi-bs-feature-fusion-isac]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[wang-2025-cellular-uav-cooperative-detection]]"
  - "[[ground-air-cooperative-isac-detection]]"
  - "[[wang-2026-robust-anti-uav-isac]]"
  - "[[spatially-separated-uav-isac-role-scheduling]]"
created: 2026-07-07
updated: 2026-07-13
---

# Networked ISAC

An ISAC architecture where multiple base stations or access points cooperate for sensing and communication instead of treating each cell independently. In [[zhao-2025-networked-isac-uav-handover]], three neighboring BS sectors form a virtual sensing cell: one primary BS transmits and all three BSs receive echoes, then a centralized EKF fuses the estimates for UAV tracking. [[wang-2026-stbc-cooperative-isac]] handles a different networked-ISAC problem: neighboring BSs share the same time-frequency resources, suppress LoS inter-BS interference, decode space-time block coded echoes, and fuse target estimates by range-profile SINR. [[yan-not-in-parse-multibs-isac-uav-trajectory]] adds [[multi-bs-feature-fusion-isac]], where asynchronous BS observations are fused at the delay/Doppler feature level and then tracked with SUKF. The concept is distinct from a single-BS ISAC link because sensing responsibility can be handed over across BSs or virtual sensing cells.

[[zhang-2025-cooperative-anti-uav-isac]] adds [[cooperative-isac-transceiver-beamforming]]: fixed cellular BSs jointly suppress clutter and inter-cell interference while meeting downlink SINR constraints, with centralized and primal-decomposition distributed implementations.

The cooperating nodes can also be mobile or heterogeneous. [[wang-2025-cellular-uav-cooperative-detection]] fuses estimates from a ground BS and connected sensing UAV, while [[wang-2026-robust-anti-uav-isac]] assigns moving UAVs to spatially separated transmit and receive roles for robust target tracking.
