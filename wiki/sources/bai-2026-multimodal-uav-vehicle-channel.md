---
type: source
title: "A Multi-Modal Intelligent Channel Model for 6G Multi-UAV-to-Multi-Vehicle Communications"
authors: ["Lu Bai", "Mengyuan Lu", "Ziwei Huang", "Xiang Cheng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3630319"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: not_applicable
tags: [source, uav-communications, vehicular-networks, channel-model, multi-modal-intelligent-channel-modeling, integrated-sensing-and-communication, low-altitude-intelligent-network, urban-air-mobility]
related:
  - "[[multi-modal-intelligent-channel-modeling]]"
  - "[[air-to-ground-channel-model]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[uav-enabled-its]]"
  - "[[urban-air-mobility]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[yang-2026-generative-radio-map-lae]]"
  - "[[zeng-2026-movable-antenna-u2u-channel]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Multi-Modal Intelligent Channel Model for 6G Multi-UAV-to-Multi-Vehicle Communications

## Citation

Bai, L., Lu, M., Huang, Z., & Cheng, X. (2026). *A Multi-Modal Intelligent Channel Model for 6G Multi-UAV-to-Multi-Vehicle Communications*. **IEEE Transactions on Wireless Communications (IEEE TWC)**. DOI: 10.1109/TWC.2025.3630319.

## TL;DR

Builds a LiDAR-aided multi-UAV-to-multi-vehicle channel model for 6G low-altitude transportation communications. The model introduces terrestrial traffic density (TTD) and aerial traffic density (ATD), constructs the MUMV-CSCI simulation dataset, distinguishes static, terrestrial-dynamic, and aerial-dynamic scatterers, and derives time-space-frequency channel statistics validated against ray-tracing data.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bai et al. [x] studied multi-UAV-to-multi-vehicle channel modeling for 6G low-altitude transportation communications in suburban forking-road scenarios. They built the MUMV-CSCI dataset by aligning AirSim LiDAR sensing, Wireless InSite channel simulation, and SUMO trajectories under terrestrial and aerial traffic-density conditions. The model classifies static, terrestrial-dynamic, and aerial-dynamic scatterers and derives time-space-frequency correlation, time stationary interval, and Doppler power spectral density statistics. Simulation results matched ray-tracing results, with the dataset containing 96,000 LiDAR point clouds and 553,500 communication links.

## Problem

Repeating independent single-UAV channel models cannot represent a shared propagation environment across many UAV-to-vehicle links. RF-only channel data also struggles to distinguish static scatterers from terrestrial and aerial moving scatterers. The paper addresses this by aligning sensing data from LiDAR point clouds with electromagnetic channel information.

## System model

- Multiple UAV transmitters communicate with multiple vehicle receivers.
- Each terminal is assumed to have mmWave communication equipment, one antenna, and LiDAR.
- The integrated CIR decomposes each link into LoS, ground-reflection, and NLoS components.
- The dataset uses a suburban forking-road scenario, 28 GHz carrier frequency, 2 GHz bandwidth, and UAV heights of 10-15 m.
- Density settings cover 3/8/15 UAVs and 8/15/25 vehicles for low, medium, and high ATD/TTD cases.

## Method

The paper aligns AirSim physical scenes with Wireless InSite electromagnetic simulations using SUMO-generated trajectories. It generates 1500 dynamic suburban scenarios, extracts LiDAR point clouds and CIR matrices, and uses sensing data to classify scatterers into static, terrestrial dynamic, and aerial dynamic groups.

The proposed model fits distributions for scatterer number, distance, angle, and power-delay behavior under different density conditions. It then models non-stationarity and consistency across time, space, and frequency using scatterer survival, birth, visibility regions, and twin-cluster matching. The derived statistics include TSF-CF, TSI, and DPSD.

## Key findings

- The MUMV-CSCI dataset contains 96,000 LiDAR point clouds and 553,500 communication links: 45,000/337,500 at high density, 34,500/180,000 at medium density, and 16,500/36,000 at low density.
- Dynamic-scatterer count distributions grow with TTD and ATD.
- Dynamic scatterers have smaller normalized distance parameters than static scatterers.
- Dynamic scatterers show larger angular variance than static scatterers, and aerial-dynamic scatterers show larger angular variance than terrestrial-dynamic scatterers.
- Aerial-dynamic path power is more sensitive to delay than static or terrestrial-dynamic scatterer power.
- Time ACF and TSI decrease as TTD and ATD increase.
- The high-density simulated DPSD is reported as closest to the high-density ray-tracing DPSD; the parse does not provide a numerical fit-error metric.

## Limitations / future work

The dataset is simulation-based because no real-world RF-plus-sensing multi-UAV-to-multi-vehicle dataset is available in the paper's framing. TTD and ATD are varied jointly; independent density variation is left for future analysis. Real-world data collection and validation are also deferred.

## Relation to the corpus

This is an adjacent physical-layer channel-modeling source rather than an MEC offloading paper. It complements [[yang-2026-generative-radio-map-lae]] and [[radio-map-assisted-channel-estimation]] by using LiDAR and ray tracing to parameterize channels instead of generating radio maps for CSI completion. It also links [[integrated-sensing-and-communication]] to the corpus's low-altitude transportation vocabulary through [[uav-enabled-its]] and [[urban-air-mobility]].

## Raw artifacts

- Parse: `raw/sources/A_Multi-Modal_Intelligent_Channel_Model_for_6G_Multi-UAV-to-Multi-Vehicle_Communications/A_Multi-Modal_Intelligent_Channel_Model_for_6G_Multi-UAV-to-Multi-Vehicle_Communications.md`
- Origin PDF: `raw/sources/A_Multi-Modal_Intelligent_Channel_Model_for_6G_Multi-UAV-to-Multi-Vehicle_Communications/A_Multi-Modal_Intelligent_Channel_Model_for_6G_Multi-UAV-to-Multi-Vehicle_Communications.pdf`
- Figures: `raw/sources/A_Multi-Modal_Intelligent_Channel_Model_for_6G_Multi-UAV-to-Multi-Vehicle_Communications/images/`
