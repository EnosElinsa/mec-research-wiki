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
created: 2026-07-07
updated: 2026-07-07
---

# Networked ISAC

An ISAC architecture where multiple base stations or access points cooperate for sensing and communication instead of treating each cell independently. In [[zhao-2025-networked-isac-uav-handover]], three neighboring BS sectors form a virtual sensing cell: one primary BS transmits and all three BSs receive echoes, then a centralized EKF fuses the estimates for UAV tracking. The concept is distinct from a single-BS ISAC link because sensing responsibility can be handed over across BSs or virtual sensing cells.
