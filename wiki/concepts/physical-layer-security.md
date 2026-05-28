---
type: concept
title: "Physical Layer Security (PLS)"
tags: [security, secrecy-rate, eavesdropper, beamforming, jamming]
related:
  - "[[friendly-jamming-uav]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[zero-trust-architecture]]"
  - "[[benaya-2025-aerial-isac-haps]]"
created: 2026-05-29
updated: 2026-05-29
---

# Physical Layer Security (PLS)

A family of secrecy techniques that exploit physical-layer properties — channel randomness, beamforming, artificial noise — to keep messages unreadable by eavesdroppers, **without** relying on cryptographic keys. The canonical metric is **secrecy rate** = legitimate-receiver rate − eavesdropper rate (clipped at 0).

Three common levers:

- **Beamforming nulls** that steer signal away from the eavesdropper.
- **Artificial noise / jamming** that raises the eavesdropper's noise floor more than the legitimate receiver's. See [[friendly-jamming-uav]].
- **Cooperative relays** that mask the source.

In the wiki, [[benaya-2025-aerial-isac-haps]] combines all three: HAPS beamforming nulls eavesdroppers identified through [[integrated-sensing-and-communication|ISAC]] sensing, and a friendly-jamming UAV reinforces the secrecy gap.

PLS complements rather than replaces upper-layer crypto. It's particularly useful when key distribution is hard (post-disaster, ad-hoc swarms) or when key-management overhead is unacceptable.
