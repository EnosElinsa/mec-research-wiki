---
type: source
title: "Through the Wall Detection and Localization of Autonomous Mobile Device in Indoor Scenario"
authors: ["Jiacheng Wang", "Hongyang Du", "Dusit Niyato", "Mu Zhou", "Jiawen Kang", "Zehui Xiong", "Abbas Jamalipour"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2023.3322819"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, indoor-localization, channel-state-information, through-the-wall, passive-sensing, isac, smart-warehouse]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[dusit-niyato]]"
  - "[[cramer-rao-bound]]"
  - "[[zehui-xiong]]"
created: 2026-06-04
updated: 2026-07-13
---

# Through the Wall Detection and Localization of Autonomous Mobile Device in Indoor Scenario

## Citation

Wang, J., Du, H., Niyato, D., Zhou, M., Kang, J., Xiong, Z., & Jamalipour, A. (2024). *Through the Wall Detection and Localization of Autonomous Mobile Device in Indoor Scenario*. **IEEE Journal on Selected Areas in Communications**, 42(1). DOI: 10.1109/JSAC.2023.3322819. (Received 15 February 2023; accepted 13 August 2023; published 9 October 2023; current version 19 December 2023.)

## TL;DR

Proposes **T-DeLo**, a CSI-based system for **through-the-wall (TTW) passive detection and localization** of autonomous mobile devices (AMDs, e.g., warehouse robots) using existing WiFi/5G infrastructure. T-DeLo: (1) establishes a reference channel to cancel strong signal interference (SSI) and phase errors; (2) applies a novel **two-dimensional matrix pencil algorithm** to jointly estimate path-length change rate (PLCR) and time-of-flight (ToF) of AMD-induced reflections; (3) uses statistical analysis (detection) and geometric analysis (localization) to track the AMD. Aggregates multiple measurements for robustness at low SNR. Experimental validation in glass-wall and brick-wall scenarios achieves detection accuracy 0.964 / 0.952 and median localization errors 1.65 m / 2.05 m.

## Problem framing

Indoor autonomous mobile devices (warehouse robots, hospital transport) require accurate localization without installing dedicated beacons on the device. Through-the-wall sensing adds a challenge: walls attenuate and scatter signals, and visually-based methods (SLAM) fail in NLoS scenarios. CSI from ambient WiFi/5G links is passive (no modification to the AMD) and can detect the AMD's reflections if the strong direct-path interference is cancelled and the weak reflected components are extracted. The matrix pencil algorithm enables joint ToF and PLCR estimation, which is then used for detection and localization.

## System model

- **Environment:** indoor smart warehouse/factory with glass or brick walls blocking line-of-sight. AMD moves on the floor.
- **Reference channel:** established between two fixed anchors; used to estimate and cancel SSI and phase noise from the measurement channel.
- **Channel model:** residual CSI after SSI cancellation contains AMD-induced reflections characterized by (ToF, PLCR).
- **2D Matrix Pencil Algorithm:** jointly estimates ToF and PLCR by aggregating multiple CSI snapshots — more robust at low SNR than single-snapshot methods.
- **Detection:** statistical hypothesis test on estimated PLCR (AMD moving vs. static).
- **Localization:** geometric analysis using estimated ToF (range) and PLCR (Doppler velocity projection) to compute AMD position.
- **Experimental evaluation:** hardware testbed in glass-wall and brick-wall scenarios.

## Key findings

- T-DeLo achieves **detection accuracy 0.964 (glass wall) / 0.952 (brick wall)** and **median localization error 1.65 m (glass) / 2.05 m (brick)** in real hardware experiments (parse Abstract).
- Multi-measurement aggregation in the matrix pencil algorithm improves robustness under low-SNR TTW conditions significantly compared to single-snapshot estimators (parse Section III + IV).
- SSI cancellation using the reference channel is essential for exposing AMD-reflected signals (parse Section III).

## Limitations / future work

Single AMD tracked at a time. Requires two fixed anchor nodes for reference channel. Localization error of ~2 m may be insufficient for fine-grained robotics positioning. Multi-AMD scenarios left as future work.

## Relation to the corpus

A passive indoor sensing paper at the intersection of **CSI-based localization** and **integrated sensing** — adjacent to the ISAC corpus entries ([[tang-2024-iscc-uav-feel]], [[wen-2024-iscc-edge-ai]]) but focused on through-wall detection rather than communication-sensing joint design. Dusit Niyato ([[dusit-niyato]]) co-authored. The hardware-experimental validation is relatively rare in the corpus (most papers are simulation-only).

## Raw artifacts

- `raw/sources/Through_the_Wall_Detection_and_Localization_of_Autonomous_Mobile_Device_in_Indoor_Scenario/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
