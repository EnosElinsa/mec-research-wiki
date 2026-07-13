---
type: source
title: "Joint Beamforming and UAV Trajectory Optimization for Covert Communications in ISAC Networks"
authors: ["Dan Deng", "Wen Zhou", "Xingwang Li", "Daniel Benevides da Costa", "Derrick Wing Kwan Ng", "Arumugam Nallanathan"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3503726"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav, isac, covert-communication, beamforming, trajectory-optimization, sdr, sca]
related:
  - "[[sensing-signal-assisted-covertness]]"
  - "[[covert-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[xingwang-li]]"
  - "[[derrick-wing-kwan-ng]]"
  - "[[arumugam-nallanathan]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Beamforming and UAV Trajectory Optimization for Covert Communications in ISAC Networks

## Citation

Deng, D., Zhou, W., Li, X., da Costa, D. B., Ng, D. W. K., & Nallanathan, A. (2025). *Joint Beamforming and UAV Trajectory Optimization for Covert Communications in ISAC Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3503726.

## TL;DR

Uses an ISAC sensing waveform as cover for a UAV access point's information transmission. Block-coordinate descent alternates semidefinite-relaxed communication/sensing beamforming with SCA trajectory updates to maximize average covert rate while preserving sensing gain and a detection-error constraint at multiple wardens.

## System and objective

- A fixed-altitude, multi-antenna UAV serves one legitimate receiver, illuminates multiple sensing targets, and faces several passive noncooperative wardens.
- Wardens perform received-power binary detection. The paper derives the optimal threshold and rewrites the minimum detection-error requirement as an upper bound on the information-to-sensing received-power ratio.
- The optimization maximizes average achievable covert rate over information and sensing covariance matrices plus the horizontal UAV path, subject to endpoint, speed, transmit-power, sensing-gain, and covertness constraints.

## Method

The beamforming block uses SDR independently in each slot. The communication covariance can be recovered at rank one, while a higher-rank sensing covariance may require Gaussian randomization. The trajectory block uses first-order convex approximations and a trust region. The alternating objective is monotone under the paper's local surrogate construction, but this is a local non-convex method and does not establish global optimality.

## Key findings

- The reported algorithm stabilizes after roughly four outer iterations in the default simulation.
- Its trajectory reaches the exhaustive-search stationary optimum, flies at maximum speed for eight slots, hovers for 24, then returns over eight slots.
- Relaxing the covertness parameter from 0.01 to 0.10 increases average covert rate by about **0.6 bit/s/Hz**.
- Joint optimization exceeds the trajectory-only and beamforming-only baselines by about **5.2** and **1.1 bit/s/Hz**, respectively, in the reported comparison.

## Limitations / interpretation

Evidence is simulation-only. The model assumes fixed altitude, static terminals and targets, pure LoS propagation, perfect legitimate CSI, and known warden/target locations; it omits propulsion energy and small-scale fading. The simulation prose also mixes `-3 dBW` and `-3 dBm` for transmit power, so power-dependent figures should not be silently reconciled. The covertness metric is the paper's equal-prior sum of false-alarm and missed-detection probabilities, not an operational field guarantee.

## Relation to the corpus

Unlike [[ambient-interference-aided-covertness]], this paper deliberately shapes the ISAC sensing signal as the masking baseline. It is also a direct [[alternating-optimization-sdr-sca]] instance coupling physical-layer covariance design with [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Joint_Beamforming_and_UAV_Trajectory_Optimization_for_Covert_Communications_in_ISAC_Networks/Joint_Beamforming_and_UAV_Trajectory_Optimization_for_Covert_Communications_in_ISAC_Networks.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
