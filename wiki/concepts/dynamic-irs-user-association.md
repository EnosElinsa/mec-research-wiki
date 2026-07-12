---
type: concept
title: "Dynamic IRS User Association"
tags: [intelligent-reflecting-surface, user-association, multi-uav, blockage, resource-allocation]
related:
  - "[[ning-2025-channel-aware-irs-uav]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[mappo]]"
  - "[[noma]]"
  - "[[blockage-aware-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[hu-2026-segmented-irs-cpn]]"
created: 2026-07-12
updated: 2026-07-13
---

# Dynamic IRS User Association

Dynamic IRS user association chooses which users receive reflected support as UAV positions and LoS/blockage states change. Unlike a one-IRS/one-user assignment, an [[intelligent-reflecting-surface]] may be partitioned into element groups so it can assist multiple users during the same control interval. [[hu-2026-segmented-irs-cpn]] applies the same partitioning idea to IRS rows and couples their allocation to per-user UAV computing capacity and task delay.

[[ning-2025-channel-aware-irs-uav]] couples the association with UAV movement, geometric LoS judgment, phase alignment, NOMA service, and transmit-power allocation. Its MAPPO agents jointly choose UAV movement and IRS-user association, making reflected-path capacity a time-varying network resource rather than a fixed deployment parameter.
