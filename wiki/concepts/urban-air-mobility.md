---
type: concept
title: "Urban Air Mobility (UAM)"
tags: [aerial, 6g, non-terrestrial-network, deployment-scenario]
related:
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[cellular-connected-uav]]"
  - "[[moon-2024-ground-satellite-uam-scheduling]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[target-level-of-safety]]"
  - "[[vitale-2026-density-aware-4d-trajectory]]"
created: 2026-06-03
updated: 2026-07-12
---

# Urban Air Mobility (UAM)

A transportation paradigm in which passenger- or cargo-carrying aircraft operate at low altitude over urban areas for fast, demand-driven point-to-point transport. Unlike a generic [[cellular-connected-uav]] — which is typically tasked with mission data upload or with serving terrestrial users — a UAM aircraft is designed to **hold a planned flight path and velocity** for stable transport, and instead consumes large amounts of **downlink** data for navigation, safety, command-and-control (C2), and multimedia.

These properties shape the communication problem around UAM:

- **Edge-user role in a [[space-air-ground-integrated-network|SAGIN]].** A UAM is served by ground stations (GSs) over a line-of-sight, scatterer-poor GS-to-aircraft channel, or by a satellite over a separate band, making it a distinctive class of edge user for 6G [[non-terrestrial-network|NTN]].
- **Predictable mobility.** Because flight paths and velocities are stable and known, scheduling can be done by **prediction** over a short horizon rather than by reacting to instantaneous channel feedback — avoiding frequent handovers despite high speed.
- **Interference geometry.** When a GS and two UAMs become geometrically aligned, inter-beam and inter-GS interference rise; offloading the high-interference UAMs to a satellite on a different band restores orthogonality for the remaining GS-served users.

In the wiki, [[moon-2024-ground-satellite-uam-scheduling]] frames cooperative ground-satellite downlink scheduling and power allocation for UAM as a sum-rate-maximization problem (link association as a minimum-cost maximum-flow graph problem + SCA power allocation), positioning UAMs as the edge users of a satellite-ground NTN.

[[jiang-2026-bi-level-uav-delivery-safety]] contributes the low-altitude logistics side of UAM: delivery routes and task assignments are accepted only when planned paths respect [[target-level-of-safety]] risk thresholds.
