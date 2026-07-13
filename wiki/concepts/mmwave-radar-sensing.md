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
  - "[[uav-backscatter-identification]]"
  - "[[zeng-2026-fmcw-isibc-lae]]"
  - "[[xu-2026-hecta-predictive-beamforming]]"
  - "[[historical-echo-predictive-beamforming]]"
  - "[[chen-2026-pointrl-uav-isac]]"
created: 2026-05-29
updated: 2026-07-14
---

# mmWave Radar Sensing

Millimeter-wave (FMCW) radar used for onboard perception: it estimates a target's **distance** (from the intermediate-frequency beat frequency), **velocity** (Doppler phase shift across chirps), and **angle** (phase difference across receive antennas). Compact and robust to lighting/weather, it complements vision sensors for situational awareness.

In the wiki, [[gao-2024-sagin-perception-offloading]] mounts mmWave radar on UAVs to sense ground-device distance/speed/direction, fuses it ([[multi-source-data-fusion]]) with [[yolov7-object-detection|YOLOv7]] type recognition, and feeds the result into the DRL state — the core of its [[perception-aided-offloading]] contribution. Conceptually adjacent to the sensing side of [[integrated-sensing-and-communication]].

[[zeng-2026-fmcw-isibc-lae]] uses FMCW sensing from a ground base station toward low-altitude UAVs, then recovers both radar parameters and backscatter identity symbols from the reflected signal.

[[xu-2026-hecta-predictive-beamforming]] uses matched-filtered communication-signal echoes for a different sensing role: a CNN-TCN-attention model consumes the echo tensor as history and predicts both ends of the next BS-UAV beam, rather than explicitly outputting range, velocity, or angle.

[[chen-2026-pointrl-uav-isac]] uses full vehicle point clouds as the state for [[radar-point-cloud-driven-uav-isac]], jointly selecting UAV motion and communication power rather than reducing the radar output to a point estimate.
