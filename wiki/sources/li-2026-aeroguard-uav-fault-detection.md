---
type: source
title: "AeroGuard: Towards Real-Time UAV Fault Detection With Hybrid Models"
authors: ["Teng Li", "Zhili Wei", "Yebo Feng", "Runze Yu", "Zhuo Ma", "Yulong Shen", "Jianfeng Ma", "Yang Liu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3653674"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav, fault-detection, anomaly-detection, hybrid-model, lstm, arx, sprt, z-score, edge-intelligence, real-time-detection, uav-security]
related:
  - "[[hybrid-uav-flight-data-fault-detection]]"
  - "[[edge-intelligence]]"
  - "[[expert-assisted-anomaly-aware-tracking]]"
  - "[[uav-localization-under-jamming]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[uav-enabled-its]]"
created: 2026-07-10
updated: 2026-07-10
---

# AeroGuard: Towards Real-Time UAV Fault Detection With Hybrid Models

## Citation

Li, T., Wei, Z., Feng, Y., Yu, R., Ma, Z., Shen, Y., Ma, J., & Liu, Y. (2026). *AeroGuard: Towards Real-Time UAV Fault Detection With Hybrid Models*. **IEEE Transactions on Mobile Computing**, 25(6), 9075-9088. DOI: 10.1109/TMC.2026.3653674.

## TL;DR

Builds a lightweight real-time UAV fault detector by fusing an LSTM predictor with an ARX predictor, weighting their residuals adaptively, and running Z-score plus SPRT tests over the fused residual stream. The system targets static, bias, drift, and point faults in UAV flight data and is evaluated on public datasets, real UAV logs, outdoor flights, and Raspberry Pi-class devices.

## Problem

UAVs in safety-critical settings face internal faults and external attacks that surface as anomalies in flight data. Knowledge-based, model-based, and pure data-driven detectors each have tradeoffs: limited unseen-fault coverage, dependence on accurate aerodynamics, high compute cost, or narrow fault types. AeroGuard targets onboard multi-fault detection with enough accuracy and latency headroom for real-time UAV operation.

## System model

- Faults are modeled through UAV flight-data streams, mainly attitude-related gyroscope and accelerometer measurements in the parsed experiments.
- The paper studies static, bias, drift, and point faults.
- The threat model includes attackers manipulating sensors, injecting false data, disturbing signals, or compromising software.
- GPS, LiDAR, and barometer streams are discussed as future extensions rather than primary evaluated channels.

## Method

AeroGuard has flight-data extraction, expected-measurement inference, and fault-detection modules. A sliding window of length $D=20$ feeds two predictors: a one-hidden-layer LSTM and an ARX model updated by recursive least squares. Their prediction residuals drive a dynamic weight matrix through an AHP-style pairwise comparison, producing a fused prediction and residual. Z-score detection and sequential probability ratio testing then run in parallel; either test can trigger a fault notification.

## Key findings

- The abstract reports up to 95.8% precision and about 10% improvement over prior work.
- On the ALFA dataset, the parsed result reports 90% accuracy, 87.5% precision, 93.33% recall, and 90.32% F1.
- Across four simulated faults, reported accuracy ranges from 83% to 90%; the GPS-attack experiment reports 80% accuracy.
- AeroGuard is not uniformly best on every sub-metric: the parse notes that LSTM-14 has higher recall on bias faults, while AeroGuard gives stronger drift robustness and more balanced F1.
- Prediction RMSE is mostly below 2 and MAE mostly below 1 in the parsed tables.
- Latency stays under 6 ms on Raspberry Pi platforms; the abstract/conclusion describe sub-5 ms latency, and the longest reported detection time is 0.8 s on lower-compute devices.
- A real-flight dataset covers 334 s at 50 Hz; PX4 injection settings include $\Delta d=15$, $k=0.03$, $m=5$, and $d=-1$.

## Limitations / future work

The PX4 parameter-injection setup cannot fully reproduce hardware-level physics such as motor seizure, actuator wear, or propeller damage. The evaluation also does not cover uncontrolled environmental disturbances such as strong wind gusts. The primary evaluated streams are attitude sensors; GPS, LiDAR, and barometer integration plus adaptive adversaries are left for future work.

## Relation to the corpus

This paper adds [[hybrid-uav-flight-data-fault-detection]] to the wiki's safety and [[edge-intelligence]] vocabulary. It is adjacent to [[expert-assisted-anomaly-aware-tracking]], which detects visual tracking anomalies, and to security-side UAV robustness pages such as [[uav-localization-under-jamming]] and [[multi-domain-uav-anti-jamming]]. Its distinguishing role is onboard flight-data fault detection with real UAV logs and edge-device latency measurements.

## Raw artifacts

- Parse: `raw/sources/AeroGuard_Towards_Real-Time_UAV_Fault_Detection_With_Hybrid_Models/AeroGuard_Towards_Real-Time_UAV_Fault_Detection_With_Hybrid_Models.md`
- Origin PDF: `raw/sources/AeroGuard_Towards_Real-Time_UAV_Fault_Detection_With_Hybrid_Models/AeroGuard_Towards_Real-Time_UAV_Fault_Detection_With_Hybrid_Models.pdf`
- Figures: `raw/sources/AeroGuard_Towards_Real-Time_UAV_Fault_Detection_With_Hybrid_Models/images/`
