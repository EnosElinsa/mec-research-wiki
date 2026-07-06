---
type: source
title: "Generative Radio Map-Assisted Channel Estimation in Low-Altitude Economy"
authors: ["Bin Yang", "Wei Wang", "Weizheng Zhang", "Wei Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3665545"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-economy, channel-estimation, radio-map, generative-adversarial-network, uav-communications]
related:
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[generative-adversarial-network]]"
  - "[[conditional-gan]]"
  - "[[air-to-ground-channel-model]]"
  - "[[csi-estimation-error]]"
  - "[[low-altitude-intelligent-network]]"
created: 2026-07-07
updated: 2026-07-07
---

# Generative Radio Map-Assisted Channel Estimation in Low-Altitude Economy

## Citation

Yang, B., Wang, W., Zhang, W., & Zhang, W. (2026). *Generative Radio Map-Assisted Channel Estimation in Low-Altitude Economy*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3665545.

## TL;DR

Uses LAE's fixed air corridors and planned UAV routes to build a velocity-aware radio map for channel estimation. The paper measures grid-labeled CSI, fills the map with a continuous vector-conditioned GAN (CVCGAN), and fuses generated radio-map CSI with pilot-based estimates through a CNN integrator. The reported NMSE gains are strongest at high UAV speeds, where pilot-only and generic neural baselines struggle with doubly selective fading.

## Problem framing

Low-altitude-economy UAVs need reliable downlink CSI while moving quickly through urban multipath. Conventional pilot-based estimators face high overhead and accuracy loss under doubly selective fading; generic deep estimators do not use the operational fact that LAE UAVs often fly in assigned air corridors with planned routes. The paper asks whether sensing labels - position and velocity - can supply a reusable channel prior through a radio map.

## System model

The model considers a BS serving UAVs in an assigned LAE air corridor. For tractability the channel-measurement region is represented as a two-dimensional plane at fixed altitude, with UAV locations and radical velocity labels attached to MISO-OFDM CSI samples. UAV positions include Gaussian deviation around nominal paths, and the physical channel is modeled over frequency, antenna, and time dimensions to capture Doppler effects.

## Method

The method has three stages:

- A grid-based channel measurement scheme samples CSI at discrete location and speed labels. In the reported setup the airspace grid yields 21 by 11 measurement points, and the UAV speeds are 5, 10, 15, 20, 25, and 30 m/s.
- CVCGAN extends conditional GAN generation to continuous vector labels by adding a pretrained CSI-to-label estimator and an MSE label-consistency term to the generator objective. WGAN-GP is used for training stability.
- A CNN integrator combines the generated radio-map CSI prior with pilot-based channel estimates, treating the radio-map output as a distributional prior rather than an exact instantaneous estimate.

## Key findings

- The CVCGAN adversarial loss stabilizes after about 10,000 epochs, and the estimator-deception loss stabilizes after about 12,000 epochs.
- At 20 m/s, the radio-map method is reported to outperform LS, ChannelNet, CGAN, RadioUNet, and DNN+LSTM across the 0-30 dB average-SNR range.
- At 30 m/s, benchmark NMSE values remain around 0.1 as SNR increases, while the proposed method improves with SNR and is described as nearly an order of magnitude better.
- In the 15 dB ablation table, the full method reports NMSE 0.016 at 20 m/s and 0.021 at 30 m/s, compared with 0.057/0.107 without CVCGAN and 0.392/0.434 without the integrator.
- Online inference uses only the trained generator and integrator; the paper estimates roughly twice the online complexity of ChannelNet/CGAN/RadioUNet while remaining in the same asymptotic order.

## Limitations / future work

The radio map is scenario-dependent: a map built for one BS service area cannot be transferred directly to a different wireless environment without adaptation or fine-tuning. The paper uses a two-dimensional fixed-altitude simplification, while noting that altitude could be added as another conditioning label for 3D maps. The evaluation is simulation/ray-tracing based rather than flight-tested.

## Relation to the corpus

This is a physical-layer LAE entry rather than MEC offloading. It extends the corpus's [[generative-adversarial-network]] and [[conditional-gan]] thread from RIS/ISAC channel generation into [[radio-map-assisted-channel-estimation]]. It also complements [[air-to-ground-channel-model]] and [[csi-estimation-error]] pages by making UAV sensing labels part of the channel-estimation state.

## Raw artifacts

- `raw/sources/Generative Radio Map-Assisted Channel Estimation in Low-Altitude Economy/Generative Radio Map-Assisted Channel Estimation in Low-Altitude Economy.md`
- Original PDF and extracted figures (`images/`) in the same folder.
