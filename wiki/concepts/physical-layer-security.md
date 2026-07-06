---
type: concept
title: "Physical Layer Security (PLS)"
tags: [security, secrecy-rate, eavesdropper, beamforming, jamming]
related:
  - "[[friendly-jamming-uav]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[zero-trust-architecture]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[collaborative-beamforming]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
created: 2026-05-29
updated: 2026-07-07
---

# Physical Layer Security (PLS)

A family of secrecy techniques that exploit physical-layer properties — channel randomness, beamforming, artificial noise — to keep messages unreadable by eavesdroppers, **without** relying on cryptographic keys. The canonical metric is **secrecy rate** = legitimate-receiver rate − eavesdropper rate (clipped at 0).

Three common levers:

- **Beamforming nulls** that steer signal away from the eavesdropper.
- **Artificial noise / jamming** that raises the eavesdropper's noise floor more than the legitimate receiver's. See [[friendly-jamming-uav]].
- **Cooperative relays** that mask the source.

In the wiki, [[benaya-2025-aerial-isac-haps]] combines two of these levers: HAPS beamforming nulls steer signal away from eavesdroppers that are identified through [[integrated-sensing-and-communication|ISAC]] sensing, and a friendly-jamming AAV reinforces the secrecy gap.

PLS complements rather than replaces upper-layer crypto. It's particularly useful when key distribution is hard (post-disaster, ad-hoc swarms) or when key-management overhead is unacceptable. [[sun-2024-imssa-uav-secure-cb]] applies PLS through [[collaborative-beamforming]]: a UAV virtual antenna array steers a high-gain mainlobe to legitimate base stations and low-gain sidelobes elsewhere, maximizing the worst-case secrecy rate even when eavesdropper locations are imperfectly known or unknown.

[[wang-2026-secure-lae-uav-scheduling]] applies PLS to low-altitude economy communications by letting UAVs dynamically switch between communication and artificial-noise jamming roles while jointly optimizing power, trajectory, and velocity for secrecy energy efficiency.
