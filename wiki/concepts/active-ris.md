---
type: concept
title: "Active RIS"
tags: [communication, beamforming, metasurface, anti-jamming]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[anti-jamming-mec]]"
  - "[[sun-2024-active-passive-ris-receiver]]"
created: 2026-05-31
updated: 2026-05-31
---

# Active RIS

A reconfigurable intelligent surface whose elements can adjust both the **phase and the amplitude** of incident signals, because each unit is backed by a power amplifier (e.g. tunnel diodes / active loads). Unlike a [[intelligent-reflecting-surface|passive RIS]] (phase-only, no amplification), an active RIS can amplify the desired signal and overcome the severe transmitter-RIS path-loss attenuation — at the cost of consuming power and injecting **dynamic noise**.

In the wiki, [[sun-2024-active-passive-ris-receiver]] cascades a passive RIS layer with an active RIS layer at the user side to build a low-cost large-scale receive array for anti-jamming, exploiting the active layer's amplitude control to concentrate receive power on the Rx antennas (lower power-scattering ratio) while the passive layer nulls jammers. The paper reports the cascaded receive power and asymptotic SINR scale as N_A²·N_P² and N_A·N_P, versus (N_P + N_A)² and (N_P + N_A) for a single-layer active RIS.
