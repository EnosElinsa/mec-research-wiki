---
type: source
title: "Networked ISAC-Based UAV Tracking and Handover Toward Low-Altitude Economy"
authors: ["Chuanbin Zhao", "Yuan Feng", "Hongliang Luo", "Feifei Gao", "Fan Liu", "Shi Jin"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3562396"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, low-altitude-economy, isac, uav-tracking, handover, networked-isac]
related:
  - "[[networked-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[seamless-handover]]"
  - "[[tang-2025-cooperative-isac-lae]]"
  - "[[huang-2026-offgrid-lae-imager]]"
  - "[[fan-liu]]"
created: 2026-07-07
updated: 2026-07-13
---

# Networked ISAC-Based UAV Tracking and Handover Toward Low-Altitude Economy

## Citation

Zhao, C., Feng, Y., Luo, H., Gao, F., Liu, F., & Jin, S. (2025). *Networked ISAC-Based UAV Tracking and Handover Toward Low-Altitude Economy*. **IEEE Transactions on Wireless Communications**, 24(9), 7670-7685. DOI: 10.1109/TWC.2025.3562396. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Defines a [[networked-isac]] tracking architecture for unauthorized UAVs in LAE. Three neighboring BS sectors form a virtual sensing cell: one primary BS transmits the sensing signal, all three BSs receive echoes, MUSIC estimates per-BS angle/range/velocity, and a centralized EKF fuses estimates for multi-UAV tracking. The paper adds PBS and VSC handover strategies so tracking continues under blockage and cell-boundary movement.

## Problem framing

LAE needs to monitor unauthorized or noncooperative UAVs, but single-BS sensing has limited range and can fail when UAVs move across cells or suffer blockage. Multi-BS networked sensing can extend coverage and improve observability, but it needs rules for which BS transmits, how estimates are fused, and how sensing responsibility changes while a UAV moves.

## System model

The paper uses mmWave OFDM ISAC BSs with sectorized antenna groups. Three adjacent sectors from neighboring BSs form a virtual sensing cell. The PBS sends sensing signals; the PBS and two SBSs receive echoes, remove static clutter, estimate horizontal/elevation angle, distance, and radial velocity, and forward estimates to a data center for fusion.

## Method

MUSIC estimates target parameters from the networked OFDM sensing signals. A centralized EKF fuses the three BSs' estimates and uses one-step prediction to distinguish and track multiple UAVs. A PBS handover algorithm switches the transmitting BS within a VSC according to SNR/blockage, while a VSC handover algorithm uses a boundary buffer zone where two adjacent VSCs alternately track the UAV.

## Key findings

- In the multi-UAV tracking experiment without blockage, the parse reports average RMSEs across ten trajectory sets of 0.35 m, 0.39 m, and 0.43 m for x/y/z, and 0.98 m/s, 1.27 m/s, and 0.51 m/s for velocity components.
- The parse reports that single-BS tracking fails for 3D velocity because a single BS observes only radial velocity, while multi-BS tracking remains observable.
- Under blockage, one blocked SBS or a blocked PBS has limited effect because two BSs remain available; simultaneous blockage of two SBSs degrades velocity estimation.
- During VSC handover, the parsed example reports full-process RMSEs of 0.32 m, 0.37 m, 0.52 m, 1.12 m/s, 1.46 m/s, and 0.67 m/s for x/y/z/vx/vy/vz.

## Limitations / future work

The paper is simulation-based. No explicit future-work agenda is stated in the conclusion beyond using the results as reference for networked ISAC-based UAV tracking and handover in LAE.

## Relation to the corpus

This source complements cooperative LAE sensing entries such as [[tang-2025-cooperative-isac-lae]] and [[huang-2026-offgrid-lae-imager]]. It is not MEC offloading; its role is a physical-layer/sensing anchor for multi-BS [[integrated-sensing-and-communication]] and LAE airspace monitoring. It also broadens the handover vocabulary from LEO compute-state handover in [[seamless-handover]] to sensing-cell handover for UAV tracking.

## Raw artifacts

- `raw/sources/Networked_ISAC-Based_UAV_Tracking_and_Handover_Toward_Low-Altitude_Economy/Networked_ISAC-Based_UAV_Tracking_and_Handover_Toward_Low-Altitude_Economy.md`
- Original PDF and extracted figures (`images/`) in the same folder.
