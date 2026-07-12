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
created: 2026-07-12
updated: 2026-07-12
---

# Dynamic IRS User Association

Dynamic IRS user association chooses which users receive reflected support as UAV positions and LoS/blockage states change. Unlike a one-IRS/one-user assignment, an [[intelligent-reflecting-surface]] may be partitioned into element groups so it can assist multiple users during the same control interval.

[[ning-2025-channel-aware-irs-uav]] couples the association with UAV movement, geometric LoS judgment, phase alignment, NOMA service, and transmit-power allocation. Its MAPPO agents jointly choose UAV movement and IRS-user association, making reflected-path capacity a time-varying network resource rather than a fixed deployment parameter.
