---
type: concept
title: "Hybrid UAV Flight-Data Fault Detection"
tags: [uav, fault-detection, anomaly-detection, edge-intelligence, safety]
related:
  - "[[li-2026-aeroguard-uav-fault-detection]]"
  - "[[edge-intelligence]]"
  - "[[expert-assisted-anomaly-aware-tracking]]"
  - "[[uav-localization-under-jamming]]"
  - "[[multi-domain-uav-anti-jamming]]"
created: 2026-07-10
updated: 2026-07-10
---

# Hybrid UAV Flight-Data Fault Detection

Hybrid UAV flight-data fault detection combines a data-driven predictor with a lightweight system-model predictor, then uses their residuals to detect abnormal flight behavior. The point is onboard robustness: pure neural prediction can adapt to nonlinear patterns but may be data-hungry, while a compact autoregressive model is cheaper and more interpretable but less flexible.

In [[li-2026-aeroguard-uav-fault-detection]], AeroGuard fuses LSTM and ARX expected-measurement predictions through residual-driven adaptive weights, then applies Z-score and SPRT tests. The concept sits near [[edge-intelligence]] because detection must run within UAV compute/latency budgets, and near [[expert-assisted-anomaly-aware-tracking]] because both pages treat UAV safety as anomaly detection over operational signals rather than only communication-rate optimization.
