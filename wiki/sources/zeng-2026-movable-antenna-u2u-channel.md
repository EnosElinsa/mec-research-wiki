---
type: source
modeling_card: required
title: "Modeling and Analysis of Movable Antenna Aided MIMO Wideband UAV-to-UAV Channels for Low-Altitude Economy Networks"
authors: ["Linzhou Zeng", "Xuewen Liao", "Zhangfeng Ma", "Ruichen Zhang", "Dusit Niyato", "Hao Jiang", "Cheng-Xiang Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3649584"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 2026"
tags: [source, low-altitude-economy, movable-antenna, mimo, channel-modeling, uav-to-uav, non-terrestrial-network]
related:
  - "[[movable-antenna]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[near-field-communications]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mozaffari-2019-drone-antenna-array]]"
  - "[[dusit-niyato]]"
created: 2026-07-07
updated: 2026-07-16
---

# Modeling and Analysis of Movable Antenna Aided MIMO Wideband UAV-to-UAV Channels for Low-Altitude Economy Networks

## Citation

Zeng, L., Liao, X., Ma, Z., Zhang, R., Niyato, D., Jiang, H., & Wang, C.-X. (2026). *Modeling and Analysis of Movable Antenna Aided MIMO Wideband UAV-to-UAV Channels for Low-Altitude Economy Networks*. **IEEE Transactions on Wireless Communications**, 25, 10257-10273. DOI: 10.1109/TWC.2025.3649584. (DOI/venue/year verified against the title-matched Crossref/IEEE DOI record; the parse header itself does not print the DOI.)

## TL;DR

Builds a wideband UAV-to-UAV MIMO channel model for low-altitude economy networks with movable antennas at both transmitter and receiver. The paper proposes a 3D arbitrary-elevation two-concentric-cylinders reference model, derives closed-form space-time-frequency correlation, space-Doppler PSD, and power space-delay spectrum, then uses the closed-form correlation gradient to optimize movable-antenna positions for ergodic-capacity improvement.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A wideband MIMO UAV-to-UAV link has movable elements at both transmitter and receiver within bounded three-dimensional regions. A two-concentric-cylinder geometry models LoS, single-bounce, and double-bounce components while both UAVs move.

**Problem & objective**: A non-convex antenna-positioning problem maximizes ergodic-capacity surrogates, $\max_{\mathbf r_T,\mathbf r_R}\log\det\mathbf R_T+\log\det\mathbf R_R$, using closed-form spatial correlation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Transmit-element positions | $\mathbf r_{T,m}$ | continuous 3-D positions | Movable antennas on the transmitting UAV |
| Receive-element positions | $\mathbf r_{R,n}$ | continuous 3-D positions | Movable antennas on the receiving UAV |
| Momentum states | $\mathbf v_T,\mathbf v_R$ | continuous vectors | Gradient-ascent momentum for position updates |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every element stays inside its bounded movement region |
| C2 | Pairwise antenna spacing remains above the mechanical minimum |
| C3 | Spatial correlation matrices follow the derived wideband U2U channel model |
| C4 | Position updates are projected back to the feasible region |

**Algorithm**: Derive space-time-frequency correlation from the two-cylinder model → form transmit and receive spatial correlation matrices → differentiate the log-determinant capacity surrogate with respect to element positions → update positions by momentum gradient ascent → project region and spacing violations → alternate transmitter and receiver updates until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng et al. [x] studied movable-antenna-assisted wideband MIMO UAV-to-UAV channels for low-altitude economy networks. They developed a three-dimensional arbitrary-elevation two-concentric-cylinder model with LoS, single-bounce, and double-bounce components. Closed-form space-time-frequency correlation, space-Doppler power spectrum, and power space-delay spectrum characterize the moving link. A momentum gradient-ascent method then optimizes transmit and receive element positions to improve a log-determinant ergodic-capacity surrogate under movement-region and minimum-spacing constraints. Numerical results report capacity gains over fixed UPA, UCA, and ULA layouts and agreement between the analytical model, simulations, and the cited measurement data.

## Problem framing

Reliable UAV-to-UAV links are important for low-altitude economy networking, but U2U channels are highly dynamic and three-dimensional. Existing U2U geometry-based stochastic models often target fixed antennas or narrowband channels, and existing movable/fluid antenna correlation models often assume simpler Jakes/Clarke-style scattering. The paper addresses wideband, 3D, non-isotropic U2U scattering with mechanically movable MIMO antenna elements.

## System model

- A wideband U2U MIMO system has $M_T$ transmit movable antennas and $M_R$ receive movable antennas.
- Antennas can move within bounded 3D regions centered at the Tx and Rx.
- The reference model includes LoS, single-bounced Tx-side, single-bounced Rx-side, and double-bounced components from two concentric cylindrical scattering regions.
- Both Tx and Rx may move, so the correlation functions include velocity-dependent terms.

## Method

The paper derives closed-form channel statistics from the arbitrary-elevation two-concentric-cylinders model: STF-CF, SD-PSD, and PSDS. It validates the model by comparing theoretical PSDS with prior measurement data and by showing deterministic/simulation models align with the analytical correlation expression. For antenna positioning, it maximizes the log-determinants of transmit/receive spatial correlation matrices under movement-region and minimum-spacing constraints using a gradient-ascent algorithm with momentum.

## Key findings

- The theoretical PSDS agrees well with prior UAV air-to-air measurement data in the reported comparison, supporting the wideband model's utility.
- Optimized movable antennas migrate toward the boundary of the feasible 3D volume, reflecting the benefit of exploiting spatial diversity under finite movement regions.
- The reported capacity-ratio analysis shows movable antennas outperform fixed UPA/UCA/ULA layouts in the tested settings, with gains especially valuable under tighter spatial constraints.
- Medium SNR values (10-20 dB in the reported analysis) yield peak relative gains before capacity saturates at higher SNR.
- Fixed-volume movement preserves performance better than vertical-line or horizontal-line movement under tight mechanical constraints.
- The model predicts that antenna counter-movements can compensate for UAV motion over short intervals until the movement volume boundary is reached.

## Limitations / future work

Future work may jointly optimize ergodic and outage performance, extend the model to airframe shadowing, validate with real UAV trajectories, and investigate more general scattering conditions.

## Relation to the corpus

This is a physical-layer/channel-modeling LAE entry, not a computation-offloading paper. It introduces [[movable-antenna]] to the corpus and connects UAV-to-UAV communications to the broader reconfigurable-antenna and MIMO vocabulary represented by [[extremely-large-scale-mimo]], [[near-field-communications]], and [[mozaffari-2019-drone-antenna-array]]. Co-author [[dusit-niyato]] links the channel-modeling source to the recurring generative-AI and aerial-edge author cluster, but the paper itself is about U2U wideband propagation and antenna-position optimization rather than MEC control.

## Raw artifacts

- `raw/sources/Modeling and Analysis of Movable Antenna Aided MIMO Wideband UAV-to-UAV Channels for Low-Altitude Economy Networks/Modeling and Analysis of Movable Antenna Aided MIMO Wideband UAV-to-UAV Channels for Low-Altitude Economy Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
