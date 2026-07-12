---
type: source
title: "Deep Learning-Based Predictive Bidirectional Beamforming in ISAC-Enabled UAV Networks"
authors: ["Jinghan Xu", "Xiaotian Zhou", "Haixia Zhang", "Yueheng Li"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3664980"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, uav, predictive-beamforming, deep-learning, temporal-attention, mmwave]
related:
  - "[[historical-echo-predictive-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[csi-estimation-error]]"
  - "[[mmwave-radar-sensing]]"
  - "[[cellular-connected-uav]]"
created: 2026-07-12
updated: 2026-07-12
---

# Deep Learning-Based Predictive Bidirectional Beamforming in ISAC-Enabled UAV Networks

## Citation

Xu, J., Zhou, X., Zhang, H., & Li, Y. (2026). *Deep Learning-Based Predictive Bidirectional Beamforming in ISAC-Enabled UAV Networks*. **IEEE Transactions on Wireless Communications**, 25, 12230-12245. DOI: 10.1109/TWC.2026.3664980.

## TL;DR

HECTA-Net predicts the next BS transmit beam and UAV receive beam directly from historical matched-filtered ISAC echoes. CNN, dilated causal TCN, and multi-head time attention capture array-space and motion history without an explicit kinematic tracker or intermediate CSI estimate.

## Problem

A narrow BS-UAV link must track active 3D motion, wind-driven drift, and roll/pitch/yaw changes that rotate the UAV array. EKF beam tracking depends on a prescribed motion model, while historical-CSI predictors inherit channel-estimation error. The design instead learns both ends' beamformers from communication-signal echoes.

## System model

- One ground BS communicates with and senses one UAV through BS transmit/echo-receive UPAs and a ventral UAV receive UPA.
- Each slot contains signal/echo acquisition followed by next-slot beam prediction; the predicted receive vector is signaled to the UAV.
- Position combines intended motion with accumulated Gaussian drift. Attitude combines active rotation and passive Gaussian oscillation.
- Matched filtering extracts historical echo tensors. The supervised objective predicts unit-norm transmit and receive vectors that maximize next-slot achievable rate.

## Method

[[historical-echo-predictive-beamforming|HECTA-Net]] splits complex echoes into real/imaginary channels. Two CNN blocks extract local array features for each historical slot; three residual dilated-causal TCN blocks model long temporal dependencies; four-head attention weights informative slots; and a final normalized complex output produces both beamformers. Offline Adam training minimizes real-plus-imaginary MSE against simulation-derived optimal beam pairs. Online operation is a forward pass with no gradient update.

## Key findings

- At 30 dBm in circular motion, HECTA-Net's communication rate is reported `8.07%` above HCL-Net and `36.93%` above EKF.
- In the higher-randomness random-motion test at `T=650 s`, it is reported `24.1%` above HCL-Net.
- Circular-motion beam-angle error has mean `0.958 degrees`, with 80% below `1.4 degrees`; random-motion mean is `2.6 degrees`, with 80% below `3.4 degrees`.
- Mean online inference latency on an Intel i7-11700K/UHD 750 system is `2.073 ms` for circular motion and `2.891 ms` for random motion.
- Performance approaches the perfect-CSI upper bound in the reported plots, but exact remaining gaps are figure-only.

## Limitations / parse caveats

Evaluation is synthetic with one BS/UAV, modeled LoS propagation, and two constructed mobility families. Labels are simulation-derived optimal beams; cross-environment generalization, blockage, multi-BS cooperation, over-the-air validation, and receive-beam signaling errors/overhead are not evaluated. The current method is communication-centric ISAC: echoes improve the link rather than serve an independent sensing objective. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[historical-echo-predictive-beamforming]] complements [[control-assisted-uav-beam-tracking]]. The control-assisted method uses flight-controller state and a Bayesian DNN; HECTA-Net instead learns bidirectional physical-layer beams end to end from echo history and explicitly includes attitude-driven receive-array rotation.

## Raw artifacts

- Parse: `raw/sources/Deep_Learning-Based_Predictive_Bidirectional_Beamforming_in_ISAC-Enabled_UAV_Networks/Deep_Learning-Based_Predictive_Bidirectional_Beamforming_in_ISAC-Enabled_UAV_Networks.md`
- Origin PDF: `raw/sources/Deep_Learning-Based_Predictive_Bidirectional_Beamforming_in_ISAC-Enabled_UAV_Networks/Deep_Learning-Based_Predictive_Bidirectional_Beamforming_in_ISAC-Enabled_UAV_Networks.pdf`
- Figures: `raw/sources/Deep_Learning-Based_Predictive_Bidirectional_Beamforming_in_ISAC-Enabled_UAV_Networks/images/`
