---
type: source
modeling_card: not_applicable
title: "UAV Trajectory Monitoring for Integrated Sensing and Communications System"
authors: ["Shaoqiang Yan", "Hongliang Luo", "Ping Yang", "Jianwei Zhao", "Feifei Gao"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3598799"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, 2026"
tags: [source, integrated-sensing-and-communication, uav-trajectory-monitoring, ofdm-sensing, target-association, unscented-kalman-filter]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-monitoring]]"
  - "[[phase-rotated-dft-motion-parameter-estimation]]"
  - "[[position-gated-velocity-nearest-neighbor-association]]"
  - "[[mmwave-radar-sensing]]"
  - "[[yan-not-in-parse-multibs-isac-uav-trajectory]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[wang-2026-fd-covert-isac]]"
  - "[[huang-2026-intelligent-jamming-maritime]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
  - "[[shaoqiang-yan]]"
  - "[[hongliang-luo]]"
  - "[[ping-yang]]"
  - "[[feifei-gao]]"
created: 2026-07-14
updated: 2026-07-16
---

# UAV Trajectory Monitoring for Integrated Sensing and Communications System

## Citation

Yan, S., Luo, H., Yang, P., Zhao, J., & Gao, F. (2026). *UAV Trajectory Monitoring for Integrated Sensing and Communications System*. **IEEE Transactions on Wireless Communications**, 25, 2733-2747. DOI: 10.1109/TWC.2025.3598799. Published online 21 August 2025; assigned to the final 2026 volume.

## TL;DR

Presents a single-base-station [[integrated-sensing-and-communication|ISAC]] framework for discovering non-cooperative UAVs, estimating six motion parameters, associating observations across sensing cycles, and predicting subsequent target states for beam tracking. Its distinctive pipeline combines phase-rotated DFT estimation, inter-array spatial registration, position-gated velocity nearest-neighbor association, and interacting multiple-model unscented Kalman filtering. The reported accuracy and complete-trajectory results are simulation evidence rather than deterministic guarantees.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yan et al. [x] studied non-cooperative UAV trajectory monitoring with a single integrated sensing and communication base station. The pipeline applies moving-target indication, FFT and CA-CFAR detection, phase-rotated DFT parameter refinement, and coordinate registration across array sectors. Position-gated velocity nearest-neighbor association links observations to trajectories, and an interacting multiple-model unscented Kalman filter fuses constant-velocity, constant-acceleration, and coordinated-spiral estimates. Simulations report lower position and velocity RMSE and better crossing-trajectory association than the evaluated DFT, observation, and association baselines. The paper is a sensing, association, and state-estimation study and does not expose an application-level operational decision model for a Modeling Quick-Use Card.

## Problem

Target detection or state estimation alone does not preserve a complete UAV trajectory. An ISAC system must also associate each new observation with an existing track, handle targets whose paths approach or cross, initialize newly discovered trajectories, and predict where tracking beams should point in the next sensing cycle. The paper addresses this end-to-end [[uav-trajectory-monitoring]] problem for a single BS with multiple sensing arrays.

## System model

- One OFDM ISAC BS has three array sectors, each with a hybrid unit that handles communication and transmits sensing signals and a radar unit that receives echoes. The paired arrays are modeled as co-located and parallel.
- Each fixed-duration sensing cycle combines wide-beam rough scanning, narrow-beam fine scanning for newly detected targets, narrow-beam tracking for established trajectories, and an idle interval when required to keep the cycle length fixed.
- Echoes contain dynamic-target returns, static clutter, and additive white Gaussian noise. Adjacent-symbol subtraction suppresses clutter under static-channel and equal-reference-symbol assumptions.
- Each target is represented by distance, horizontal and pitch angles, radial velocity, and two angular velocities. Array-local estimates are transformed into a common Cartesian position-and-velocity frame.
- The tracking state contains 3-D position, velocity, and acceleration. Candidate dynamics are constant velocity, constant acceleration, and coordinated spiral motion.

## Method

The BS first uses moving-target indication, a two-dimensional FFT range-Doppler spectrum, and CA-CFAR detection to identify dynamic targets. [[phase-rotated-dft-motion-parameter-estimation|PRDFT]] then locates coarse spectral bins and searches a bounded phase-rotation grid to refine distance and angle estimates; virtual-velocity estimates and least-squares plane fitting recover radial and angular velocities.

After coordinate registration, [[position-gated-velocity-nearest-neighbor-association|WGVDNN]] applies a covariance-weighted position gate and resolves plausible matches by minimum Euclidean velocity difference. An unmatched detection must be associated across two consecutive cycles before a trajectory is initialized. An interacting multiple-model unscented Kalman filter then mixes constant-velocity, constant-acceleration, and coordinated-spiral models, updates their probabilities, fuses their state estimates, and predicts the next position and velocity for association and beam tracking.

## Key findings

- The simulation configuration uses a 30 GHz carrier, 240 kHz subcarrier spacing, 256 subcarriers, 64 OFDM symbols, `64 x 64` hybrid-unit UPAs, and `128 x 128` radar-unit UPAs.
- Across the plotted SNR range, PRDFT is reported to approach ESPRIT accuracy and substantially outperform ordinary DFT. The paper gives PRDFT distance-estimation complexity as `O(M log M + M + GM)` for `G` phase-grid points, compared with `O(M^3)` for the cited ESPRIT-style method; this is a complexity comparison, not an accuracy theorem.
- In the 1000-slot cross-array coordinated-spiral simulation, IMMUKF reduces position RMSE from `(0.2966, 0.3123, 0.2967)` m for observations to `(0.0968, 0.1022, 0.0839)` m, and velocity RMSE from `(0.1172, 0.1159, 0.1172)` m/s to `(0.0464, 0.0509, 0.0332)` m/s.
- In the constructed crossing-trajectory experiment, position-only WGNN misassociates targets, whereas WGVDNN correctly associates all three tested trajectory pairs.
- The multi-model experiment identifies the highest-probability motion model in the simulated CA, coordinated-spiral, and CV segments, but model changes are detected with delay and CV/CA probabilities can be similar.
- The multi-target experiment maintains previously discovered tracks while adding later-appearing targets and reconstructs complete trajectories for the eight simulated flight attitudes.

## Limitations / future work

The evaluation is simulation-only and the paper provides no theorem guaranteeing complete monitoring, correct association at every intersection, or delay-free motion-model identification. The single-BS model assumes co-located parallel array pairs, sufficiently distant targets, static clutter across adjacent symbols, equal adjacent reference symbols, independent symbol noise, and small target displacement within an OFDM frame. New trajectories require two consecutive detections, and IMMUKF is restricted to three motion models. Multi-BS cooperation is identified as an extension rather than evaluated here.

## Relation to the corpus

This paper is the single-BS counterpart to [[yan-not-in-parse-multibs-isac-uav-trajectory]], which fuses asynchronous delay and Doppler features from multiple BSs and uses sequential UKF tracking. It also complements [[zhao-2025-networked-isac-uav-handover]], where cooperative BSs manage sensing coverage and handover. Unlike [[uav-trajectory-control]] sources that optimize the sensing UAV's own path, this paper estimates and maintains the trajectories of non-cooperative target UAVs. Its 30 GHz OFDM pipeline is adjacent to [[mmwave-radar-sensing]], while remaining distinct from the narrower FMCW examples on that concept page.

The tracked object and output differ from camera-service monitoring in [[zhan-2026-star-ris-aerial-monitoring]], authorized suspicious-payload decoding in [[lin-2026-fc-ris-surveillance]], and Willie's activity detection in [[wang-2026-fd-covert-isac]]. [[huang-2026-intelligent-jamming-maritime]] predicts an unobserved Eve position for a secrecy controller, whereas this source measures, associates, and filters non-cooperative tracks. See [[aerial-observation-control-covertness-surveillance-and-monitoring]].

## Raw artifacts

- Parse: `raw/sources/UAV_Trajectory_Monitoring_for_Integrated_Sensing_and_Communications_System/UAV_Trajectory_Monitoring_for_Integrated_Sensing_and_Communications_System.md`
- Origin PDF: `raw/sources/UAV_Trajectory_Monitoring_for_Integrated_Sensing_and_Communications_System/UAV_Trajectory_Monitoring_for_Integrated_Sensing_and_Communications_System.pdf`
- Figures: `raw/sources/UAV_Trajectory_Monitoring_for_Integrated_Sensing_and_Communications_System/images/`
