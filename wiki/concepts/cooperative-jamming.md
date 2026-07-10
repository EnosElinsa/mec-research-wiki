---
type: concept
title: "Cooperative Jamming"
tags: [security, jamming, physical-layer-security, secrecy]
related:
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[ris-assisted-directional-jamming]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[noma]]"
  - "[[li-2023-secure-marine-iot-jamming]]"
created: 2026-05-31
updated: 2026-07-11
---

# Cooperative Jamming

**Cooperative jamming** is a physical-layer-security technique in which helper nodes deliberately transmit interfering (jamming) signals to degrade an eavesdropper's reception while legitimate communication proceeds. Unlike a dedicated jammer, the helpers are existing network nodes (relays, receivers, or idle devices) reused as cooperative jammers, which improves the secrecy rate without extra hardware. The optimization typically allocates jamming power across helpers (and their positions) to maximize the legitimate-vs-eavesdropper channel gap.

## In this wiki

- [[li-2023-secure-marine-iot-jamming]] schedules **USVs** to first set up a high-quality NOMA uplink to a HAP and then reuse them as **cooperative jammers** against an eavesdropper during HAP offloading, jointly optimizing each USV's jamming power with positions, uploading duration, workload, and HAP transmit power to minimize energy. It is the multi-helper, ground-vehicle counterpart of the aerial [[friendly-jamming-uav]] used in [[benaya-2025-aerial-isac-haps]]; both serve [[physical-layer-security]].
- [[zhang-2026-air-ground-covert-jamming]] adds [[ris-assisted-directional-jamming]]: a terrestrial jammer does not need a direct favorable path to Willie because a UAV-mounted RIS redirects the jamming signal. This makes the jamming role part of a covert relay/RIS/trajectory design rather than a fixed helper-node placement assumption.
