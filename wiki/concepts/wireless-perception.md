---
type: concept
title: "Wireless Perception"
tags: [wireless-sensing, csi, generative-ai, edge-computing]
related:
  - "[[generative-ai-for-mec]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[wang-2024-wipe-gai]]"
  - "[[wang-gai-isac-physical-layer]]"
created: 2026-06-02
updated: 2026-06-02
---

# Wireless Perception

Sensing the physical world — locations, postures, gestures, presence — by processing wireless signals (CSI, mmWave radar, WiFi, RFID) rather than cameras. The appeal is privacy (no camera exposure) and coverage (signals are ubiquitous and penetrate where cameras cannot).

In [[wang-2024-wipe-gai]], wireless perception is used to **guide generative AI**: a sequential multi-scale perception (SMSP) algorithm builds a CSI feature matrix and predicts a user's **skeleton** (posture), which then conditions a GAI model to generate a matching virtual character — addressing the instability of prompt-only GAI in AIGC services. The perception chain jointly estimates angle-of-arrival and time-of-flight from CSI (e.g. 2D MUSIC) and weights links by proximity to the user (Fresnel-zone motivated).

Wireless perception is closely related to the sensing half of [[integrated-sensing-and-communication|ISAC]]; the generative-AI-from-physical-layer-signals view also appears in [[wang-gai-isac-physical-layer]].
