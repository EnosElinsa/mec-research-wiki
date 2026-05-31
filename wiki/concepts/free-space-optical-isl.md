---
type: concept
title: "Free-Space Optical Inter-Satellite Link (FSO ISL)"
tags: [leo-satellite, inter-satellite-link, optical-communication, non-terrestrial-network]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[walker-star-constellation]]"
  - "[[non-terrestrial-network]]"
  - "[[mao-2024-fso-leo-hierarchical-routing]]"
created: 2026-06-01
updated: 2026-06-01
---

# Free-Space Optical Inter-Satellite Link (FSO ISL)

An **inter-satellite link (ISL)** carried over a **laser (free-space optical)** beam rather than radio frequency (RF). FSO offers very high bandwidth (demonstrated single-wavelength links into the Tbps range), which is why it is the expected ISL technology for dense LEO constellations. The trade-off is operational: a laser's strong directionality means a link can only be established when two satellites have **geometric visibility** *and* a free **Acquisition, Pointing, and Tracking (APT) terminal** — and each satellite carries only a limited number of APT terminals. So, unlike RF, FSO ISLs cannot be set up as rapidly or flexibly, and the set of available links is dynamic.

In the wiki, [[mao-2024-fso-leo-hierarchical-routing]] makes this constraint first-class: its routing strategy must be **adaptive to the number of FSO ISLs** (bounded by APT terminals + visibility), and it analyzes how the APT-terminal count affects network performance. Intra-orbit FSO ISLs are relatively stable (satellites on the same orbit move together) while inter-orbit ones change spatially and temporally. The FSO ISL is also noted in passing as a natural multi-hop offloading substrate on the [[leo-satellite-edge-computing]] page, and the constellation geometry that determines visibility is the [[walker-star-constellation]].
