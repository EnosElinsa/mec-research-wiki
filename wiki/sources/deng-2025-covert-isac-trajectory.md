---
type: source
title: "Joint Beamforming and UAV Trajectory Optimization for Covert Communications in ISAC Networks"
authors: ["Dan Deng", "Wen Zhou", "Xingwang Li", "Daniel Benevides da Costa", "Derrick Wing Kwan Ng", "Arumugam Nallanathan"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3503726"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
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
  - "[[wang-2026-fd-covert-isac]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-07-13
updated: 2026-07-16
---

# Joint Beamforming and UAV Trajectory Optimization for Covert Communications in ISAC Networks

## Citation

Deng, D., Zhou, W., Li, X., da Costa, D. B., Ng, D. W. K., & Nallanathan, A. (2025). *Joint Beamforming and UAV Trajectory Optimization for Covert Communications in ISAC Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3503726.

## TL;DR

Uses an ISAC sensing waveform as cover for a UAV access point's information transmission. Block-coordinate descent alternates semidefinite-relaxed communication/sensing beamforming with SCA trajectory updates to maximize average covert rate while preserving sensing gain and a detection-error constraint at multiple wardens.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude multi-antenna UAV serves one legitimate receiver while illuminating multiple sensing targets and hiding its information signal from multiple wardens. The sensing waveform supplies the masking baseline, and each warden applies received-power detection.

**Problem & objective**: The joint ISAC design maximizes the legitimate user's average achievable covert rate, $\max_{\mathbf w_r,\mathbf w_c,\mathbf q}\mathcal R(\mathbf q)=\frac{1}{N}\sum_{n=1}^{N}\log_2\!\left(1+\frac{\mathbf h_B^H[n]\mathbf W_c[n]\mathbf h_B[n]}{\sigma_b^2}\right)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensing beamformer | $\mathbf w_r[n]$ | complex vector | ISAC sensing waveform in slot $n$ |
| Information beamformer | $\mathbf w_c[n]$ | complex vector | Covert communication beam in slot $n$ |
| UAV horizontal position | $\mathbf q[n]$ | continuous, $\mathbb R^2$ | Fixed-altitude UAV waypoint in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 22a-22b | The trajectory starts and ends at prescribed points and obeys the speed limit, $\lVert\mathbf q[n]-\mathbf q[n+1]\rVert\leq V_mT_s$ |
| 22c | Sensing and information beams share the slot power budget, $\lVert\mathbf w_r[n]\rVert^2+\lVert\mathbf w_c[n]\rVert^2\leq P_m$ |
| 22d | Each sensing target receives at least its required directional gain |
| 22e | At every warden, the information-to-sensing received-power ratio stays below $\mu_{\max}$, enforcing the detection-error requirement |

**Algorithm**: Block-coordinate descent alternates two local solvers. With the path fixed, semidefinite relaxation optimizes communication and sensing covariance matrices and recovers beamformers by singular-value decomposition or Gaussian randomization; with beams fixed, successive convex approximation updates the trajectory inside a trust region until the average covert rate converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Deng et al. [x] used an ISAC sensing waveform to mask information transmission from a fixed-altitude multi-antenna UAV in the presence of multiple wardens and sensing targets. They maximized average covert rate by jointly selecting communication and sensing beamformers and the horizontal UAV trajectory under endpoint, speed, power, sensing-gain, and detection-error constraints. Their block-coordinate method combines semidefinite relaxation and rank recovery for beamforming with successive convex approximation for trajectory updates. In the reported simulations, relaxing the covertness parameter from 0.01 to 0.10 adds about 0.6 bit/s/Hz, while joint optimization exceeds the trajectory-only and beamforming-only baselines by about 5.2 and 1.1 bit/s/Hz.

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

The wardens' received-power decision, the target-directed sensing-gain constraint, and the resulting covert-rate objective occupy the activity-hiding branch of [[aerial-observation-control-covertness-surveillance-and-monitoring]]; they should not be read as authorized interception or trajectory-tracking metrics.

## Raw artifacts

- `raw/sources/Joint_Beamforming_and_UAV_Trajectory_Optimization_for_Covert_Communications_in_ISAC_Networks/Joint_Beamforming_and_UAV_Trajectory_Optimization_for_Covert_Communications_in_ISAC_Networks.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
