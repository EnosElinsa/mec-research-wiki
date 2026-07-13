---
type: concept
title: "Simultaneous Wireless Information and Power Transfer (SWIPT)"
tags: [swipt, wireless-power-transfer, energy-harvesting, power-splitting]
related:
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[high-altitude-platform-station]]"
  - "[[an-2024-multilayer-ris-hap-swipt]]"
  - "[[chen-2025-swipt-mec-sac]]"
  - "[[dual-domain-ris-energy-harvesting]]"
  - "[[peng-2023-dual-domain-eh-ris]]"
  - "[[lu-2026-multiuav-iscpt]]"
created: 2026-06-02
updated: 2026-07-13
---

# Simultaneous Wireless Information and Power Transfer (SWIPT)

**SWIPT** lets a single radio signal carry **information and energy at the same time**, so the same ambient transmission both communicates with and recharges energy-constrained devices. A common receiver design is **power splitting (PS)**, which divides the received signal into two streams — an **information stream** for decoding and a **power stream** for [[rf-energy-harvesting|energy harvesting]] — with a tunable PS ratio governing the trade-off between rate and harvested energy.

SWIPT is closely related to [[wireless-power-transfer]] (where a dedicated source pushes energy) but distinguished by reusing the **information-bearing** signal for energy. Its main practical limit is that energy-transfer efficiency falls off sharply with distance because of large-scale fading, which makes long-range deployments (satellite, HAP) challenging without aperture/array gain.

In the wiki, [[an-2024-multilayer-ris-hap-swipt]] enables SWIPT over the extreme long-distance link of a [[high-altitude-platform-station|HAP]] network using a **multi-layer refracting [[intelligent-reflecting-surface|RIS]]-assisted receiver** and PS-based information/energy splitting, optimizing the PS ratios alongside the precoder and RIS coefficients under a non-linear EH constraint. [[chen-2025-swipt-mec-sac]] applies SWIPT in a UAV-assisted MEC setting solved with an improved soft-actor-critic. [[peng-2023-dual-domain-eh-ris]] adds [[dual-domain-ris-energy-harvesting]], combining the slot split with element-level reflection/harvesting partitioning on a UAV-mounted surface. The concept complements [[backscatter-communication]] in the corpus's energy-sustainability track.
