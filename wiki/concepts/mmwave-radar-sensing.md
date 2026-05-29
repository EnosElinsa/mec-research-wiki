---
type: concept
title: "mmWave Radar Sensing"
tags: [sensing, perception, isac, radar]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[multi-source-data-fusion]]"
  - "[[perception-aided-offloading]]"
  - "[[yolov7-object-detection]]"
  - "[[gao-2024-sagin-perception-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# mmWave Radar Sensing

Millimeter-wave (FMCW) radar used for onboard perception: it estimates a target's **distance** (from the intermediate-frequency beat frequency), **velocity** (Doppler phase shift across chirps), and **angle** (phase difference across receive antennas). Compact and robust to lighting/weather, it complements vision sensors for situational awareness.

In the wiki, [[gao-2024-sagin-perception-offloading]] mounts mmWave radar on UAVs to sense ground-device distance/speed/direction, fuses it ([[multi-source-data-fusion]]) with [[yolov7-object-detection|YOLOv7]] type recognition, and feeds the result into the DRL state — the core of its [[perception-aided-offloading]] contribution. Conceptually adjacent to the sensing side of [[integrated-sensing-and-communication]].
