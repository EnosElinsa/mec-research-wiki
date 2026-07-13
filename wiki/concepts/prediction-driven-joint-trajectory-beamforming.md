---
type: concept
title: "Prediction-Driven Joint Trajectory and Beamforming"
tags: [trajectory-prediction, beamforming, uav, deep-reinforcement-learning]
related:
  - "[[sensing-assisted-predictive-beamforming]]"
  - "[[uav-trajectory-control]]"
  - "[[m2llm-state-representation-for-drl]]"
  - "[[yin-2026-m2llm-trajectory-beamforming]]"
created: 2026-07-14
updated: 2026-07-14
---

# Prediction-Driven Joint Trajectory and Beamforming

A control pipeline that predicts future user motion before jointly choosing an aerial platform's path and transmit beams. Prediction compensates for sensing and processing delay, while joint control avoids committing to a trajectory before beam decisions are considered.

In [[yin-2026-m2llm-trajectory-beamforming]], multimodal user-path forecasts become the state for centralized DDPG over each UAV's direction, speed, and beamformer. The approach is compared with real-time-state control and a separated trajectory/beam-tracking baseline.

The pipeline is related to [[sensing-assisted-predictive-beamforming]] but uses a learned multimodal environment representation instead of a model-based state estimator. Its performance evidence is empirical and does not guarantee optimal joint control.
