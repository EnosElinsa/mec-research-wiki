---
type: concept
title: "Space-Air-Ground Integrated Network (SAGIN)"
tags: [sagin, satellite, hap, uav, 6g, architecture]
related:
  - "[[high-altitude-platform-station]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[he-2026-dt-sagimec-lae]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
  - "[[zhao-2026-hcdrl-ga-sagin-sar]]"
  - "[[tun-2025-thz-sag-mec-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-07
---

# Space-Air-Ground Integrated Network (SAGIN)

A network architecture that vertically stacks **satellites** (LEO/MEO/GEO), **aerial platforms** ([[high-altitude-platform-station|HAPS]] and UAVs), and **ground stations** into one integrated communication-and-computation system. Used in 6G visions to extend coverage into oceans, deserts, post-disaster zones, and other places terrestrial infrastructure can't reach.

The three tiers play distinct roles. Satellites give global reach but high propagation delay. HAPS sit at ~20 km, are quasi-stationary for months, and combine wide footprint with stable energy supply. UAVs are flexible and cheap but battery-limited. The control plane decides which tier handles which task — and that's a recurring optimization in the wiki.

In the wiki, [[hsu-2025-drl-hues-hap-noma]] uses the SAGIN frame explicitly to model HAP-as-relay between ground stations and a satellite. [[mao-2025-bcsa-frl]] sits at the LEO-tier of a SAGIN. [[he-2026-dt-sagimec-lae]] makes the SAGIN stack a low-altitude-economy MEC substrate: ISDs offload through a UAV and selected LEO satellite paths while a cloud-side digital twin mirrors the physical layers. [[zhao-2025-probabilistic-semantic-sagin]] uses a satellite-UAV-ground relay chain to study the communication-versus-computation energy tradeoff of [[probabilistic-semantic-communication]]. [[zhao-2026-hcdrl-ga-sagin-sar]] uses the SAGIN tiers as offloading targets in a multi-UAV search-and-rescue setting, adding wind-aware deployment and online trajectory/offloading control. The narrower **air-ground integrated network (IAGN)** in [[jiang-2025-isac-lae-overview]] and [[wang-2025-lae-network-survey]] is a SAGIN minus the satellite layer.
