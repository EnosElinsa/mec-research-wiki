---
type: source
modeling_card: not_applicable
title: "Asynchronous UAV Trajectory Monitoring With Multi-BS Feature Fusion in Cellular ISAC"
authors: ["Shaoqiang Yan", "Mei Chen", "Hongliang Luo", "Ping Yang", "Feifei Gao"]
year: ""
url: ""
venue: ""
tags: [source, integrated-sensing-and-communication, networked-isac, multi-bs-sensing, feature-fusion, ofdm-sensing, kalman-filter, uav-trajectory-monitoring]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
  - "[[multi-bs-feature-fusion-isac]]"
  - "[[multi-source-data-fusion]]"
  - "[[uav-trajectory-control]]"
  - "[[mmwave-radar-sensing]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
  - "[[tang-2025-cooperative-isac-lae]]"
  - "[[shaoqiang-yan]]"
  - "[[hongliang-luo]]"
  - "[[ping-yang]]"
  - "[[feifei-gao]]"
created: 2026-07-11
updated: 2026-07-16
---

# Asynchronous UAV Trajectory Monitoring With Multi-BS Feature Fusion in Cellular ISAC

## Citation

Yan, S., Chen, M., Luo, H., Yang, P., & Gao, F. *Asynchronous UAV Trajectory Monitoring With Multi-BS Feature Fusion in Cellular ISAC*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Proposes a cellular ISAC trajectory-monitoring pipeline where multiple base stations fuse feature-level delay and Doppler information to track unauthorized UAVs despite asynchronous observations. The key idea is to avoid strict coherent radar-style synchronization by preprocessing each BS observation and then fusing compact features.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yan et al. [x] studied asynchronous UAV trajectory monitoring through feature fusion across multiple cellular ISAC base stations. Each station estimates angles, compensates timing and carrier-frequency offsets, and extracts delay and Doppler features from local echoes. The fusion stage obtains rough position and velocity estimates, refines them through compressed-sensing feature fusion, and applies a sequential unscented Kalman filter to asynchronous trajectory points. Simulations report lower position and velocity error than the evaluated direct-observation, rough-fusion, data-fusion, and standard-UKF baselines. The paper is a measurement and state-estimation pipeline and does not define an application-level operational decision model with reusable decisions, objective, and constraints.

## Problem

Single-BS ISAC can estimate local target state but struggles to maintain wide-area UAV trajectories. Multi-BS sensing improves coverage, yet neighboring BSs often observe the same UAV at different times. That temporal misalignment makes direct data-level or signal-level fusion fragile.

## System model

- Multiple ISAC BSs are deployed in a hexagonal cellular layout. Communication cells serve ground users and authorized UAVs, while larger sensing areas overlap into cooperative sensing areas.
- Each BS has hybrid-unit and radar-unit UPAs and uses narrowband OFDM sensing signals.
- During a sensing cycle, one BS transmits while all BSs receive reflected echoes, yielding multi-perspective but asynchronous observations.

## Method

The pipeline has three layers. First, single-BS preprocessing estimates angles with local DFT, compensates time offsets and carrier-frequency offsets with a LoS reference and cross-correlation, and extracts time-delay / Doppler feature vectors. Second, multi-BS feature fusion roughly estimates position and velocity, then refines them with compressed-sensing feature fusion. Third, cooperative trajectory tracking associates local and global trajectories and applies a sequential unscented Kalman filter (SUKF) to fuse asynchronous trajectory points.

## Key findings

- Simulations use 28 GHz, 120 kHz subcarrier spacing, 128 subcarriers, 64 OFDM symbols, HU-UPA `8 x 8`, RU-UPA `16 x 16`, and 3GPP UMi propagation.
- LDFT outperforms classical DFT for angle estimation, especially as SNR increases.
- TO/CFO compensation improves distance and radial-velocity estimation under large offsets.
- Feature fusion beats direct observation, rough fusion, and data fusion for both position and velocity estimation; data fusion saturates around SNR 5 while feature fusion continues improving.
- SUKF reduces position RMSE to `(0.1146, 0.1098, 0.0958)` m and velocity RMSE to `(0.1336, 0.1070, 0.1064)` m/s, outperforming direct observations and standard UKF.

## Limitations / future work

The validation is simulation-only in the parse. The preprocessing assumes LoS reference information between BSs. OCR artifacts affect equations and headings, so the page avoids formula-level reconstruction.

## Relation to the corpus

This source deepens [[networked-isac]] beyond handover and shared-resource echo separation. [[zhao-2025-networked-isac-uav-handover]] uses virtual sensing cells and EKF handover logic, while [[wang-2026-stbc-cooperative-isac]] uses STBC echo separation and SINR-weighted fusion. Yan et al. add [[multi-bs-feature-fusion-isac]], where feature-level delay/Doppler fusion and SUKF handle asynchronous multi-BS trajectory observations.

## Raw artifacts

- `raw/sources/Asynchronous_UAV_Trajectory_Monitoring_With_Multi-BS_Feature_Fusion_in_Cellular_ISAC/Asynchronous_UAV_Trajectory_Monitoring_With_Multi-BS_Feature_Fusion_in_Cellular_ISAC.md`
- Original PDF and extracted figures (`images/`) in the same folder.
