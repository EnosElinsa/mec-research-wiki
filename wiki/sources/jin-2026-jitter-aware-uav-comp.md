---
type: source
title: "Multi-UAV CoMP Transmission Based on UAV Jitter Characteristics: Analysis and Optimization"
authors: ["Wanyang Jin", "Changhao Du", "Jiacheng Wang", "Shuai Wang", "Gaofeng Pan", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3588241"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 978-993"
tags: [source, coordinated-multipoint, uav-jitter, channel-modeling, lstm, channel-prediction]
related:
  - "[[jitter-aware-lstm-channel-compensation]]"
  - "[[jitter-aware-uav-beamwidth-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[csi-estimation-error]]"
  - "[[jiacheng-wang]]"
  - "[[shuai-wang]]"
  - "[[gaofeng-pan]]"
  - "[[dusit-niyato]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-UAV CoMP Transmission Based on UAV Jitter Characteristics: Analysis and Optimization

## Citation

Jin, W., Du, C., Wang, J., Wang, S., Pan, G., & Niyato, D. (2026). *Multi-UAV CoMP Transmission Based on UAV Jitter Characteristics: Analysis and Optimization*. **IEEE Transactions on Wireless Communications, 25**, 978-993. DOI: 10.1109/TWC.2025.3588241.

## TL;DR

Derives channel correlation and approximate CoMP capacity under pitch/yaw jitter, then predicts next-symbol CSI from attitude and channel sequences with J-LSTM to compensate joint-transmission precoding.

## Problem and system model

UAV clusters form distributed UAV base stations that jointly transmit to ground users over shared time/frequency resources. Pitch and yaw move an omnidirectional antenna offset from the platform center, changing LoS and multipath distances. A sinusoidal random-jitter/Rician model yields channel autocorrelation; Gamma approximations and bounds characterize useful power, inter-user interference, and achievable capacity.

## Method

The analytical model shows how jitter amplitude, frequency, carrier frequency, and antenna offset reduce temporal correlation. [[jitter-aware-lstm-channel-compensation]] uses two 64-unit LSTM layers to predict next-symbol CSI from pitch, yaw, and real/imaginary channel sequences. It is compared with an unrealistic perfect-future-correlation AR predictor and a practical delayed AR predictor.

## Key findings

- With two UAV-BSs, ten UAVs each, and two users, jitter loss is about 2 bit/s/Hz at 20 dB and 6 degrees, but almost 9 bit/s/Hz at 30 dB.
- Training converges after about 6000 iterations and reports test MSE 0.0087 on generated data.
- At 30 dB, perfect AR and J-LSTM improve capacity by at least 4 bit/s/Hz; J-LSTM's plotted gain exceeds 8 bit/s/Hz at 10 degrees.
- Against delayed AR, estimation accuracy improves by more than 3.8% at 10 degrees and nearly 7% at 14 degrees.

## Limitations

Evaluation uses synthetic channels and numerical simulations, not airborne measurements. The model assumes ideal LoS information exchange among UAV-BSs, common antenna offsets, prescribed jitter distributions, and simplified scatterer geometry. Complexity is lower than AR only under stated parameter inequalities. Power allocation, UAV mobility, heterogeneous global optimization, and field testing remain future work; several extracted equations are corrupted.

## Relation to the corpus

This source treats jitter as CSI aging for CoMP joint transmission, distinct from [[jitter-aware-uav-beamwidth-control]], where angular disturbance selects a directional beamwidth. Both expose high-SNR performance limits caused by platform motion.

## Raw artifacts

- `raw/sources/Multi-UAV_CoMP_Transmission_Based_on_UAV_Jitter_Characteristics_Analysis_and_Optimization/Multi-UAV_CoMP_Transmission_Based_on_UAV_Jitter_Characteristics_Analysis_and_Optimization.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
