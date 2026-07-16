---
type: source
title: "A Multi-Scale Feature Extraction and Fusion U-Net for Pathloss Prediction in UAV-Assisted mmWave Radio Networks"
authors: ["Sajjad Hussain"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3670373"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: not_applicable
tags: [source, uav-communications, channel-model, pathloss-prediction, multi-scale-unet-pathloss-prediction, air-to-ground-channel-model, radio-map-assisted-channel-estimation, low-altitude-intelligent-network]
related:
  - "[[multi-scale-unet-pathloss-prediction]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[yang-2026-generative-radio-map-lae]]"
  - "[[bai-2026-multimodal-uav-vehicle-channel]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Multi-Scale Feature Extraction and Fusion U-Net for Pathloss Prediction in UAV-Assisted mmWave Radio Networks

## Citation

Hussain, S. (2026). *A Multi-Scale Feature Extraction and Fusion U-Net for Pathloss Prediction in UAV-Assisted mmWave Radio Networks*. **IEEE Transactions on Wireless Communications (IEEE TWC)**. DOI: 10.1109/TWC.2026.3670373.

## TL;DR

Introduces a U-Net pathloss predictor for UAV-assisted mmWave networks that uses log-distance, LoS mask, and building mask inputs. The architecture combines multi-scale convolution branches, feature fusion, and an ASPP bottleneck, and the paper adds a vectorized LoS-mask computation pipeline for large-scale dataset generation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hussain [x] studied pathloss prediction for UAV-assisted millimeter-wave radio networks across multiple urban environments and UAV altitudes. The proposed U-Net takes log-distance, line-of-sight mask, and building-occupancy mask inputs and combines multi-scale convolution branches, feature fusion, and an atrous spatial pyramid pooling bottleneck. A vectorized geometric line-of-sight algorithm accelerates mask generation for dense receiver grids. The model was evaluated on an in-house 28 GHz ray-tracing dataset and the RadioMapSeer benchmark, including cross-city, altitude, and noisy-input tests. The reported in-house results include a 3.15 dB RMSE, a 2.37 dB MAE, and a 0.00049 NMSE for the complete model.

## Problem

Accurate pathloss prediction is needed for UAV-assisted mmWave planning, but field measurements are site-specific, ray tracing is costly, and stochastic models miss fine-grained urban variation. The paper focuses on three underexplored issues: cross-environment generalization, robustness to noisy inputs, and sensitivity to UAV altitude.

## System model

- Five urban environments are used: Munich-01, Munich-02, Helsinki, London, and Manhattan.
- Each environment has four UAV transmitter locations and three UAV altitudes: 25 m, 35 m, and 45 m.
- The dataset contains 60 transmitter scenarios and 5,898,240 simulated receiver points on a 256 x 384 receiver grid.
- The UAV operates at 28 GHz with 30 dBm transmit power and an isotropic antenna; receiver height is 1.5 m.
- Inputs are reshaped into 128 x 128 x 3 tensors: log-distance, LoS mask, and building occupancy.

## Method

The model is a fully convolutional encoder-decoder based on U-Net. Each encoder stage uses parallel convolution kernels at multiple scales, then fuses them with a 1 x 1 convolution. The bottleneck uses atrous spatial pyramid pooling to aggregate context across receptive fields.

A vectorized LoS-mask algorithm projects building geometry against transmitter-receiver line segments using tensor operations, avoiding slow per-receiver visibility loops. The model is evaluated on the in-house 28 GHz UAV dataset and on the RadioMapSeer benchmark.

## Key findings

- On the in-house dataset, the proposed model reports RMSE 3.15 dB, MAE 2.37 dB, and NMSE 0.00049.
- Across four independent in-house runs, it reports RMSE 3.26 +/- 0.09 dB, MAE 2.46 +/- 0.07 dB, and NMSE (5.1 +/- 0.22) x 10^-4.
- On RadioMapSeer, it reports RMSE 3.97 dB, MAE 2.03 dB, and NMSE 0.0011.
- Across 25 m, 35 m, and 45 m UAV altitudes, RMSE stays between 3.17 dB and 3.28 dB; the paper reports average reductions of 37% in MAE and 63% in NMSE versus RadioUNet 3-channel.
- Distance-channel noise has negligible impact up to 10% standard deviation, while 10% LoS-mask and building-mask corruption degrade RMSE to 4.54 dB and 4.95 dB.
- Inference averages 0.86 s per transmitter scenario, compared with 0.52 s for the RadioUNet baselines.

## Limitations / future work

The study focuses on large-scale pathloss under stationary channel assumptions. UAV airframe occlusion, airframe shadowing, and channel non-stationarity from mobility or altitude changes are explicitly outside scope. The higher-altitude test at 80 m and 120 m also shows weaker generalization than the 25-45 m range.

## Relation to the corpus

This is a data-driven pathloss-modeling counterpart to [[air-to-ground-channel-model]] and [[blockage-aware-channel-model]]. It is adjacent to [[yang-2026-generative-radio-map-lae]] because both use learned spatial maps for low-altitude channel reasoning, but this paper predicts pathloss from geometry-derived masks rather than estimating CSI from generated radio maps. It also sits near [[bai-2026-multimodal-uav-vehicle-channel]] as a second UAV communication-layer source where sensing or map-derived structure informs channel modeling.

## Raw artifacts

- Parse: `raw/sources/A_Multi-Scale_Feature_Extraction_and_Fusion_U-Net_for_Pathloss_Prediction_in_UAV-Assisted_mmWave_Radio_Networks/A_Multi-Scale_Feature_Extraction_and_Fusion_U-Net_for_Pathloss_Prediction_in_UAV-Assisted_mmWave_Radio_Networks.md`
- Origin PDF: `raw/sources/A_Multi-Scale_Feature_Extraction_and_Fusion_U-Net_for_Pathloss_Prediction_in_UAV-Assisted_mmWave_Radio_Networks/A_Multi-Scale_Feature_Extraction_and_Fusion_U-Net_for_Pathloss_Prediction_in_UAV-Assisted_mmWave_Radio_Networks.pdf`
- Figures: `raw/sources/A_Multi-Scale_Feature_Extraction_and_Fusion_U-Net_for_Pathloss_Prediction_in_UAV-Assisted_mmWave_Radio_Networks/images/`
