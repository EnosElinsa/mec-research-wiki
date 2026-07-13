---
type: source
title: "Control-Assisted Beam Prediction and Tracking for UAV Millimeter Wave Communications"
authors: ["Jianjun Zhang", "Yongming Huang", "Jiaheng Wang", "Christos Masouros", "Xiaohu You"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3668082"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-communication, mmwave, beam-tracking, flight-control, bayesian-learning, hardware-evidence]
related:
  - "[[yongming-huang]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[cellular-connected-uav]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[hussain-2026-unet-uav-mmwave-pathloss]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[christos-masouros]]"
created: 2026-07-12
updated: 2026-07-14
---

# Control-Assisted Beam Prediction and Tracking for UAV Millimeter Wave Communications

## Citation

Zhang, J., Huang, Y., Wang, J., Masouros, C., & You, X. (2026). *Control-Assisted Beam Prediction and Tracking for UAV Millimeter Wave Communications*. **IEEE Transactions on Wireless Communications**, 25, 13121-13135. DOI: 10.1109/TWC.2026.3668082.

## TL;DR

Uses position error, velocity, attitude, and waypoint information already available from the UAV flight-control loop to predict and track a narrow mmWave beam during autonomous mission flight. A Bayesian DNN predicts attitude-induced offsets, while a low-complexity kinematic estimator tracks position-induced offsets and narrows or skips beam sweeping.

## Problem

High mobility and perturbations make narrow BS-UAV mmWave beams difficult to align. Repeated full sweeping consumes transmission time, accurate dynamics are difficult to maintain, and purely data-driven predictors can require large fresh training sets.

## System model

- A point-to-point BS-UAV analog-beamforming link operates over a LoS-dominant single-path channel.
- The multicopter follows preloaded waypoints in mission-flight mode under a PX4-like double-loop PID controller.
- Each 100 ms slot contains prediction, beam sweeping, and data transmission.
- Beam offset is split into attitude-induced Type I and relative-position-induced Type II components.
- Effective achievable rate accounts for both beam quality and beam-sounding overhead.

## Method

The controller analysis separates each flight leg into acceleration, near-uniform motion, and deceleration. A fully connected DNN with a Bayesian linear output layer predicts Type-I offsets and uncertainty intervals from control state. A velocity-based kinematic estimator predicts Type-II offsets and is periodically corrected by absolute position updates. The tracker then sweeps only the confidence interval and may omit local sweeping when uncertainty is small.

## Key findings

- The evaluated DNN has layers of 128, 256, 256, and 24 neurons; the approximate roll/pitch beam width is 4 degrees.
- Position and velocity examples update at 1 Hz and 50 Hz. The Gazebo case uses four targets and 45 m altitude; the real F450 setup includes a 600 m flight segment.
- In the reported Gazebo comparisons, CTRL has the best prediction-success accuracy and effective achievable rate against SBL and GPR, but exact curve magnitudes are not stated in text.
- With more than 64 training trajectories, the textual figure analysis reports CTRL ahead across the tested SNR region; with 16 trajectories it remains best in the low-SNR region.
- Data from a real F450 UAV with Pixhawk/PX4 and an RK3506 ARM processor show a similar effective-rate ordering to simulation.

## Limitations / parse caveats

The real-UAV evidence validates flight-state collection and embedded prediction, not an over-the-air mmWave radio testbed; the feedback link is Sub-6G LoRa. The model assumes autonomous waypoint flight, fixed yaw, a LoS-dominant single path, and approximately constant velocity/attitude away from waypoint transitions. Figure 15 is labeled effective achievable rate in its caption while adjacent prose calls it prediction-success accuracy, so no exact figure values are transcribed. The parse contains the DOI; year, venue, volume, and pages were verified against its exact Crossref record.

## Relation to the corpus

[[control-assisted-uav-beam-tracking]] connects flight-control telemetry directly to physical-layer alignment, unlike [[hussain-2026-unet-uav-mmwave-pathloss]], which predicts spatial path loss from maps. It gives a concrete hardware-evidence case for the control/communication coupling surveyed in [[javaid-2023-collaborative-uav-communication-control]].

## Raw artifacts

- Parse: `raw/sources/Control-Assisted_Beam_Prediction_and_Tracking_for_UAV_Millimeter_Wave_Communications/Control-Assisted_Beam_Prediction_and_Tracking_for_UAV_Millimeter_Wave_Communications.md`
- Origin PDF: `raw/sources/Control-Assisted_Beam_Prediction_and_Tracking_for_UAV_Millimeter_Wave_Communications/Control-Assisted_Beam_Prediction_and_Tracking_for_UAV_Millimeter_Wave_Communications.pdf`
- Figures: `raw/sources/Control-Assisted_Beam_Prediction_and_Tracking_for_UAV_Millimeter_Wave_Communications/images/`
