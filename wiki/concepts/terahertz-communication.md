---
type: concept
title: "Terahertz (THz) Communication"
tags: [communication, channel, spectrum, mmwave]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[blockage-aware-channel-model]]"
  - "[[noma]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[tun-2025-thz-sag-mec-resource-allocation]]"
  - "[[song-2026-thz-multiuav-mec]]"
  - "[[bai-adaptive-near-field-xl-mimo-multi-uav]]"
created: 2026-05-29
updated: 2026-07-11
---

# Terahertz (THz) Communication

Wireless communication in the THz band (roughly 0.1–10 THz; the wiki's source uses 200–400 GHz). THz offers enormous bandwidth for data-hungry applications, but suffers **severe propagation attenuation** — high free-space path loss plus frequency-selective **molecular absorption** — and poor diffraction, making links highly **blockage-vulnerable** and short-range.

These properties motivate pairing THz with an [[intelligent-reflecting-surface]] to engineer reflected paths around blockages. In the wiki, [[wu-2025-iopo-irs-uav-thz-mec]] models THz UAV-MEC links with a path-loss + molecular-absorption channel and adds an IRS to restore spectral efficiency. Related to the [[blockage-aware-channel-model]] concern that recurs across aerial-MEC channel modeling.

[[tun-2025-thz-sag-mec-resource-allocation]] uses THz for short-range device-to-UAV access in a MEC-enabled SAG network, with mmWave backhaul among UAVs and LEO satellites. [[song-2026-thz-multiuav-mec]] uses THz links for direct IoT-MEC and IoT-UAV-MEC relay paths, adding molecular absorption, blockage probability, and MEC queueing delay to the relay/deployment/resource-allocation problem.

[[bai-adaptive-near-field-xl-mimo-multi-uav]] uses 0.35 THz as a low-THz comparison point for XL-MIMO UPA-to-multi-UAV channel modeling; its parse reports faster decorrelation than the 28 GHz case, making CSI refresh and beam tracking more demanding.
