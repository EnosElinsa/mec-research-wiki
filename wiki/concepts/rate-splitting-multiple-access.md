---
type: concept
title: "Rate-Splitting Multiple Access"
tags: [multiple-access, rsma, beamforming, interference-management, sic, wireless-communication]
related:
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[mihertie-2026-aerial-irs-rsma-ee]]"
  - "[[beyond-diagonal-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[noma]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
created: 2026-07-13
updated: 2026-07-13
---

# Rate-Splitting Multiple Access

In the one-layer rate-splitting multiple access (RSMA) design used by the linked sources, each user's message is divided into common and private parts. The transmitter combines the common parts into one stream decoded by every scheduled user, while private streams remain user-specific. Each receiver decodes and removes the common stream through successive interference cancellation, then decodes its private stream while treating the remaining private streams as noise.

This creates an interference-management continuum between fully treating interference as noise and decoding complete interfering messages as in some [[noma|NOMA]] designs. Beamformers and common-rate allocations determine how much interference is decoded versus tolerated.

[[huroon-2026-bd-ris-rsma-uav]] applies RSMA inside each UAV user group while orthogonalizing groups and assigning [[beyond-diagonal-ris]] clusters. [[mihertie-2026-aerial-irs-rsma-ee]] jointly optimizes common/private precoders, common rates, a [[uav-mounted-ris]], and aerial placement under hardware distortion.
