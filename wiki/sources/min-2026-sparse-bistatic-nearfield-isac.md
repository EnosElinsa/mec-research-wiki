---
type: source
title: "Sparse XL-MIMO Bi-Static Near-Field ISAC for Low-Altitude UAV Swarm"
authors: ["Hongqi Min", "Yong Zeng", "Xinrui Li", "Suzhi Bi", "Jie Xu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3702759"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 18562-18578"
tags: [source, integrated-sensing-and-communication, sparse-xl-mimo, near-field, bistatic-sensing, uav-swarm, localization]
related:
  - "[[sparse-xl-mimo]]"
  - "[[fourth-order-bistatic-virtual-array]]"
  - "[[symmetric-double-nested-array]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[near-field-communications]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[joint-localization-and-communication]]"
  - "[[yong-zeng]]"
  - "[[suzhi-bi]]"
  - "[[jie-xu]]"
  - "[[jiang-2026-ray-antenna-array]]"
  - "[[huang-2026-star-ris-nearfield-isac]]"
  - "[[bai-adaptive-near-field-xl-mimo-multi-uav]]"
created: 2026-07-14
updated: 2026-07-14
---

# Sparse XL-MIMO Bi-Static Near-Field ISAC for Low-Altitude UAV Swarm

## Citation

Min, H., Zeng, Y., Li, X., Bi, S., & Xu, J. (2026). *Sparse XL-MIMO Bi-Static Near-Field ISAC for Low-Altitude UAV Swarm*. **IEEE Transactions on Wireless Communications, 25**, 18562-18578. DOI: 10.1109/TWC.2026.3702759.

## TL;DR

Uses a sparse extremely large-scale transmit array and fourth-order cumulants to separate angle from near-field range in bistatic OFDM-ISAC. The resulting virtual arrays support joint AoD/AoA estimation and closed-form 3D UAV localization while the enlarged physical aperture also improves downlink spatial separation.

## Problem

Compact half-wavelength arrays have limited aperture for resolving low-altitude UAV targets, while sparse arrays introduce grating lobes and near-field steering couples angle to range. A bistatic deployment adds another pairing problem because departure and arrival angles must be associated before 3D localization. The paper asks how a sparse array can increase sensing degrees of freedom without retaining that angle-range coupling.

## System model

- A spatially separated ISAC transmitter and sensing receiver use linear arrays to serve single-antenna downlink users and sense multiple low-altitude UAVs in the upper half-space.
- One precoded OFDM waveform carries user data and known sensing streams. Communication data are reused for sensing, and the known sensing streams are assumed removable at users.
- Sensing returns contain target-dependent AoD/AoA steering, bistatic delay, Doppler, fluctuating complex RCS, and noise. Communication channels are multipath.
- The transmitter uses a 23-element [[symmetric-double-nested-array]] in the main experiment: a compact central ULA with two sparse outer ULAs. The receiver normally uses a three-element compact ULA.
- Near-field steering retains a quadratic angle-range phase term through a second-order spherical-distance approximation. The same precoder is used across subcarriers and OFDM symbols.

## Method

The receiver first correlates known transmitted symbols to separate delay clusters and removes the full-rank precoder. It then forms a fourth-order cumulant matrix. Conjugate products cancel the quadratic near-field phase while doubling difference-coarray indices, producing the [[fourth-order-bistatic-virtual-array|fourth-order virtual manifolds]] used for joint sensing.

After permutation and selection of consecutive virtual-coarray segments, two-dimensional spatial smoothing restores rank for coherent target returns. An EVD and two-dimensional Bartlett spectrum estimate paired AoD/AoA values. A separate physical-array covariance and one-dimensional MUSIC search estimate transmitter-side near-field range; OFDM delay supplies bistatic range. The angle and range cones are then intersected in closed form, with the positive-altitude solution retained under the paper's nonparallel-array geometry.

The work does not formulate a joint resource or trajectory optimization problem. Communication is evaluated with normalized MRT, ZF, and MMSE precoders, while dedicated sensing vectors occupy the communication precoder's null space.

## Key findings

- The [[symmetric-double-nested-array]] analysis gives sensing DoF `M_2(M_1+1)+(M_1-1)`, compared with `M-1` for an equal-element compact ULA. This is an array-geometry result, not a general estimation-error guarantee.
- With five delay clusters, the reported delay RMSE is below `3.76 x 10^-10 s`, corresponding to `0.1128 m` range error.
- At half-wavelength element spacing, the fourth-order coarray's doubled spacing leaves angular ambiguity for the tested near-field targets. At quarter-wavelength spacing, the proposed method resolves both near- and far-field targets.
- Figure 8 indicates an AoD RMSE around `1.5-1.8 x 10^-3 rad` from 0 to 30 dB in one setup, but the fourth-order method is worse at very low SNR. These are approximate plot readings and reflect the noise sensitivity of higher-order statistics.
- Figure 9 approximately places sparse-array MMSE/ZF sum spectral efficiency at `36-37 bps/Hz` at 20 dB, versus roughly `6-9 bps/Hz` for the compact-array curves. The paper reports no numerical 3D localization RMSE despite visually close estimated and ground-truth points.

## Limitations

The evidence is analytical and Monte Carlo simulation only. There is no array prototype, flight test, measured RCS/channel data, calibration study, runtime, or hardware-energy evaluation. The pipeline assumes known transmitted symbols, precoder, array locations, and array orientations; synchronization error, carrier offset, channel-estimation error, target-count uncertainty, and association failures are omitted. Mutual coupling, sparse-array calibration errors, platform attitude, multipath target echoes, and model mismatch are also absent.

Fourth-order processing requires many snapshots and is more noise-sensitive than second-order processing. The two-dimensional angle search and large EVDs are computationally expensive. Unique 3D localization depends on near-field range information and the stated nonparallel orientation; parallel one-dimensional arrays are geometrically degenerate. The parse also contains inconsistent precoder dimensions and damaged equations, so this page does not silently repair the source's formula-level notation.

## Relation to the corpus

This source extends [[integrated-sensing-and-communication]] and [[extremely-large-scale-mimo]] with a sparse bistatic sensing pipeline rather than a trajectory or beam-resource optimizer. [[jiang-2026-ray-antenna-array]] also studies low-altitude UAV-swarm OFDM-ISAC with [[yong-zeng]], but uses a switch-selected radial receive array and far-field-style angle/delay/Doppler processing. [[huang-2026-star-ris-nearfield-isac]] jointly optimizes hover position, beamforming, and STAR-RIS coefficients, while [[bai-adaptive-near-field-xl-mimo-multi-uav]] focuses on near-field channel statistics rather than target localization.

## Raw artifacts

- Parse: `raw/sources/Sparse_XL-MIMO_Bi-Static_Near-Field_ISAC_for_Low-Altitude_UAV_Swarm/Sparse_XL-MIMO_Bi-Static_Near-Field_ISAC_for_Low-Altitude_UAV_Swarm.md`
- Origin PDF: `raw/sources/Sparse_XL-MIMO_Bi-Static_Near-Field_ISAC_for_Low-Altitude_UAV_Swarm/Sparse_XL-MIMO_Bi-Static_Near-Field_ISAC_for_Low-Altitude_UAV_Swarm.pdf`
- Figures: `raw/sources/Sparse_XL-MIMO_Bi-Static_Near-Field_ISAC_for_Low-Altitude_UAV_Swarm/images/`
