---
type: concept
title: "Temporal Spectrum Cartography"
tags: [low-altitude-economy, spectrum-sensing, radio-map, generative-ai]
related:
  - "[[zhao-2026-temporal-spectrum-cartography]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[uav-trajectory-control]]"
  - "[[generative-ai-for-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Temporal Spectrum Cartography

Temporal spectrum cartography reconstructs a sequence of RF power or RSSI maps over space and time rather than a single static radio map. In [[zhao-2026-temporal-spectrum-cartography]], the map is represented as a temporal tensor over a 2D low-altitude grid, with sparse measurements from static sensors and mobile UAV sensors.

The concept differs from ordinary [[spectrum-sensing-channel-selection]] because sensing is not only used to pick an idle channel at one time instant. The goal is to recover a time-varying spectrum field under sparse sensor coverage, then move UAV sensors to locations that reduce future reconstruction error.
