---
type: concept
title: "Active RIS"
tags: [communication, beamforming, metasurface, anti-jamming]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[anti-jamming-mec]]"
  - "[[sun-2024-active-passive-ris-receiver]]"
  - "[[shi-2026-aoi-active-ris-noma-agmec]]"
  - "[[cui-2026-aris-v2x-icac]]"
created: 2026-05-31
updated: 2026-07-10
---

# Active RIS

A reconfigurable intelligent surface whose elements can adjust both the **phase and the amplitude** of incident signals, because each unit is backed by a power amplifier (e.g. tunnel diodes / active loads). Unlike a [[intelligent-reflecting-surface|passive RIS]] (phase-only, no amplification), an active RIS can amplify the desired signal and overcome the severe transmitter-RIS path-loss attenuation — at the cost of consuming power and injecting **dynamic noise**.

In the wiki, [[sun-2024-active-passive-ris-receiver]] cascades a passive RIS layer with an active RIS layer at the user side to build a low-cost large-scale receive array for anti-jamming, exploiting the active layer's amplitude control to concentrate receive power on the Rx antennas while the passive layer nulls jammers. [[shi-2026-aoi-active-ris-noma-agmec]] uses active RIS on the infrastructure side to improve NOMA-assisted air-ground MEC offloading freshness, jointly optimizing active-RIS beamforming with UAV trajectory and task offloading. [[cui-2026-aris-v2x-icac]] extends active RIS into V2X integrated communication and computation, where ARIS phase/amplitude control is optimized with UAV/BS beamforming, vehicle associations, offloading ratios, and computation resources.
