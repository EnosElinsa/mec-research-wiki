---
type: concept
title: "Decentralized Active-RIS UAV-NOMA Control"
tags: [active-ris, uav, noma, mappo, ctde, resource-allocation]
related:
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[active-ris]]"
  - "[[uav-mounted-ris]]"
  - "[[noma]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
created: 2026-07-12
updated: 2026-07-12
---

# Decentralized Active-RIS UAV-NOMA Control

Decentralized active-RIS UAV-NOMA control assigns physically distinct network decisions to separate cooperating agents: the BS chooses NOMA power allocation, the UAV controls platform motion, and the active RIS controls per-element gain and phase. This avoids one actor spanning the full mixed action space while preserving a shared system objective during training.

[[morshed-2026-active-ris-uav-noma-mappo]] implements the pattern with [[mappo]] and [[centralized-training-decentralized-execution|CTDE]]. A shared critic sees the global state during offline training, while three local actors execute independently. Their common reward balances sum rate, energy efficiency, [[jains-fairness-index|Jain fairness]], outage, and airspace feasibility.

The decomposition is architectural rather than fully distributed learning: training still needs global information and a shared critic. Its practical benefit is parallel low-millisecond inference after training; its evidence remains a single-UAV/RIS simulation with perfect CSI/SIC and simplified propulsion.
