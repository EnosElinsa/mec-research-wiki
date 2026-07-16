---
type: source
title: "Spatiotemporal-Attention-Based Channel Prediction for UAV-RIS-Assisted LEO Satellite MIMO Communications"
authors: ["Mingyi Wang", "Yizhou Peng", "Ruofei Ma", "Gongliang Liu", "Weixiao Meng", "Carla Fabiana Chiasserini", "Roberto Garello"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3630206"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 7252-7267"
tags: [source, channel-prediction, spatiotemporal-attention, transformer, partial-csi, beamspace, uav-mounted-ris, leo-satellite]
related:
  - "[[spatiotemporal-attention-channel-prediction]]"
  - "[[masked-csi-reconstruction-pretraining]]"
  - "[[dft-beamspace-channel-compression]]"
  - "[[partial-csi-outage-patterns]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[transformer-encoder]]"
  - "[[carla-fabiana-chiasserini]]"
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[moon-2024-ground-satellite-uam-scheduling]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[mahboob-2024-ai-ntn-survey]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: not_applicable
---

# Spatiotemporal-Attention-Based Channel Prediction for UAV-RIS-Assisted LEO Satellite MIMO Communications

## Citation

Wang, M., Peng, Y., Ma, R., Liu, G., Meng, W., Chiasserini, C. F., & Garello, R. (2026). *Spatiotemporal-Attention-Based Channel Prediction for UAV-RIS-Assisted LEO Satellite MIMO Communications*. **IEEE Transactions on Wireless Communications, 25**, 7252-7267. DOI: 10.1109/TWC.2025.3630206.

## TL;DR

Predicts future satellite-RIS-user MIMO channel tensors with global/local attention over individual antenna-time tokens. Masked reconstruction prepares the model for missing historical snapshots, while dominant DFT-beam tokens reduce the otherwise prohibitive attention cost of large arrays.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] developed a spatiotemporal-attention model for predicting satellite, UAV-RIS, and user MIMO channel tensors under rapid mobility. Their architecture expands antenna-time coefficients into tokens, combines global and local attention, and uses masked reconstruction pretraining to tolerate missing historical snapshots. A dominant DFT-beam representation reduces attention cost by retaining only the strongest complex beam coefficients and their indices. At a twenty-step horizon, the reported full-CSI NMSE was approximately -19.4 dB, compared with approximately -16.4 dB for the next-best LSTM baseline. Retaining nine beams in the small-array case reduced computation from 6.06 to 1.52 GMac while changing NMSE from -19.40 to -19.35 dB. A single-user MRT experiment also showed higher spectral efficiency with predicted CSI than with stale CSI at both five-step and twenty-step horizons.

## Problem

Fast satellite, UAV-RIS, and user motion causes large Doppler and rapid channel aging, while feedback may contain contiguous outages, random outages, or deliberate undersampling. Treating each time snapshot as one token can hide spatial dependencies among antennas and subchannels, but expanding every coefficient into a token makes global attention expensive. The paper addresses prediction accuracy, missing-CSI robustness, and model scaling together.

## System model

- One LEO satellite with a UPA serves ground users directly and through a passive RIS carried by a moving UAV. Users have multi-antenna receivers.
- The synthetic channel generator combines ECEF geometry and attitude, ISS TLE/SGP4 satellite motion, Dubins UAV motion, Gauss-Markov user mobility, free-space and ITU-R losses, 3GPP UMi-LoS CDL fading, Rician components, and ray-level Doppler.
- The carrier is 27 GHz with 100 MHz bandwidth. Satellite speed is `7.4-7.6 km/s`; the stated maximum Doppler is `6.8 x 10^5 Hz`.
- Each snapshot concatenates real and imaginary parts of the satellite-RIS, RIS-user, and direct satellite-user matrices. The prediction input contains `c` historical snapshots and the target contains `g` future snapshots.
- [[partial-csi-outage-patterns]] covers contiguous missing time steps, randomly missing time steps, and equidistant intentional undersampling, alone or combined.

## Method

The [[spatiotemporal-attention-channel-prediction]] model represents each antenna/subchannel coefficient at each time as a token. Its encoder combines global self-attention across all tokens with local attention over smaller temporal/antenna neighborhoods. A causal decoder uses masked self-attention and global/local cross-attention to predict future coefficients without future-token leakage.

For partial CSI, [[masked-csi-reconstruction-pretraining]] first masks historical time snapshots and minimizes reconstruction error only over masked values. The pretrained embedding and encoder then initialize supervised future-channel prediction. The reported experiments use snapshot-level zero filling even though parts of the paper describe entry-level masking.

To scale to larger arrays, [[dft-beamspace-channel-compression]] transforms each sublink, retains its `P` strongest complex beams, and encodes magnitude, phase, and normalized beam indices. Predictions are placed back into those bins and inverse transformed after omitted bins are set to zero. This is approximate dominant-beam reconstruction, not lossless inversion.

## Key findings

- In the full-CSI experiment, Figure 6 approximately gives the proposed model NMSEs of `-22.0`, `-19.4`, and `-16.6 dB` at 2, 20, and 26 prediction steps. At 20 steps, the next-best LSTM is approximately `-16.4 dB`.
- For 20-step prediction, Table IV reports 568.51K parameters and 6100 MMAC for spatiotemporal attention, compared with 1.27M/62.66 MMAC for LSTM and 528.93K/9.04 MMAC for temporal-only attention. The accuracy gain therefore carries a large pre-compression compute cost.
- In the small-array case, retaining `P=9` beams changes NMSE from `-19.40` to `-19.35 dB` while reducing cost from `6.06` to `1.52 GMac`. In the large-array case, `P=26` gives `-19.24 dB` at `12.63 GMac`; the full-domain accuracy is not reported.
- Figure 9 labels the proposed model around `-16.0 dB` under 75% continuous outage, `-17.1 dB` under 75% random outage, and `-18.2 dB` under 75% equidistant sparsity. Some labels are low-resolution and should be treated as figure-derived.
- At 10 dB SNR with single-user MRT, Table VII reports `3.15` and `2.49 bps/Hz` for 5- and 20-step predicted CSI, compared with `2.67` and `1.94 bps/Hz` for stale CSI; perfect CSI gives `3.46 bps/Hz` at both horizons.

## Limitations

All data are generated by one simulator stack; there are no measured satellite/UAV-RIS channels, orbital trials, hardware-in-the-loop tests, confidence intervals, or cross-environment evaluations. The outage experiments zero-fill whole historical snapshots without an explicit mask indicator. Quantization, delayed feedback, coefficient-level corruption, asynchronous loss, and noisy nonzero errors are not separated.

Global attention is quadratic in the expanded antenna-time sequence. Reported Jetson inference times are calculated from assumed TFLOPS rather than measured on-device runs, and the eight-H100 training cost is not quantified. The large-array full-domain NMSE is absent, so compression accuracy at that scale has no direct uncompressed reference. The end-use rate experiment removes the RIS and multiuser setting, demonstrating predicted-CSI utility only on a single-user direct satellite link. No error bound, generalization guarantee, convergence theorem, code release, or complete training recipe is provided.

## Relation to the corpus

[[fang-2026-cellfree-uav-predictive-beamforming]] predicts LoS state with distributed EKF and covariance fusion, whereas this source learns full satellite/RIS/user coefficient tensors. [[moon-2024-ground-satellite-uam-scheduling]] predicts motion to reduce handovers rather than forecasting CSI. [[pan-2025-uav-ris-energy-efficient-comm]] optimizes UAV-RIS placement, phases, and beamforming; the present paper treats RIS motion and channels as generated inputs and does not optimize phases or trajectories.

## Raw artifacts

- Parse: `raw/sources/Spatiotemporal-Attention-Based_Channel_Prediction_for_UAV-RIS-Assisted_LEO_Satellite_MIMO_Communications/Spatiotemporal-Attention-Based_Channel_Prediction_for_UAV-RIS-Assisted_LEO_Satellite_MIMO_Communications.md`
- Origin PDF: `raw/sources/Spatiotemporal-Attention-Based_Channel_Prediction_for_UAV-RIS-Assisted_LEO_Satellite_MIMO_Communications/Spatiotemporal-Attention-Based_Channel_Prediction_for_UAV-RIS-Assisted_LEO_Satellite_MIMO_Communications.pdf`
- Figures: `raw/sources/Spatiotemporal-Attention-Based_Channel_Prediction_for_UAV-RIS-Assisted_LEO_Satellite_MIMO_Communications/images/`
