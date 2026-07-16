---
type: source
title: "Age of Information Minimization in UAV-Assisted Covert Communication: Trajectory and Beamforming Design"
authors: ["Shima Salar Hosseini", "Paeiz Azmi", "Ali Nazari"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3681697"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, age-of-information, covert-communication, physical-layer-security, noma, uav-trajectory-control, beamforming, alternating-optimization, air-to-ground-channel-model]
related:
  - "[[freshness-aware-covert-uav-communication]]"
  - "[[age-of-information]]"
  - "[[covert-communication]]"
  - "[[noma]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[air-to-ground-channel-model]]"
  - "[[physical-layer-security]]"
  - "[[ma-2024-covert-mmwave-finite-blocklength]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
created: 2026-07-10
updated: 2026-07-16
---

# Age of Information Minimization in UAV-Assisted Covert Communication: Trajectory and Beamforming Design

## Citation

Hosseini, S. S., Azmi, P., & Nazari, A. (2026). *Age of Information Minimization in UAV-Assisted Covert Communication: Trajectory and Beamforming Design*. **IEEE Transactions on Wireless Communications**, 25, 15425-15440. DOI: 10.1109/TWC.2026.3681697.

## TL;DR

Minimizes AoI for UAV-assisted covert communication in the presence of an aerial eavesdropper. A multi-antenna UAV transmitter serves a covert user and a public user through PD-NOMA, using the public flow as cover traffic; trajectory and beamforming are optimized with alternating LP, SCA, and SDR subproblems.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude multi-antenna UAV uses power-domain NOMA to send public updates to Carol and covert updates to Bob while an aerial Eve performs radiometer detection and adapts its position. Bob uses SIC, and public traffic serves as cover for freshness-sensitive covert packets.

**Problem & objective**: Minimize total age of information, $\min_{\mathbf Q,\mathbf W,\boldsymbol\Delta}\sum_n\sum_{k\in\{b,c\}}\Delta_k[n]$, over UAV trajectory, user beamformers, and slotwise freshness variables.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf Q=\{\mathbf q[n]\}$ | continuous 2-D positions | Alice's horizontal path at fixed altitude |
| User beamforming | $\mathbf W=\{\mathbf w_k[n]\}$ | complex continuous | Public and covert transmit beams |
| Age variables | $\boldsymbol\Delta=\{\Delta_k[n]\}$ | continuous, nonnegative | Information age allocated to each user and slot |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Total beamforming power per slot remains within Alice's budget. |
| C2 | NOMA power ordering enables Bob's SIC and allocates stronger received power to the public flow. |
| C3 | Eve's minimum detection error satisfies $\xi^*[n]\geq1-\epsilon$. |
| C4 | Maximum packet age remains below the channel-variation interval. |
| C5 | Achievable public and covert rates deliver their required packet sizes. |
| C6 | Consecutive UAV positions satisfy the maximum-speed distance bound. |

**Algorithm**: First derive Eve's optimal threshold and location for the conservative covertness constraint. Alternate an LP update for AoI, an SCA trajectory update using first-order rate bounds, and an SDR plus SCA beamforming update; use the rank-one recovery result and repeat the three blocks until total AoI converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hosseini et al. [x] studied information freshness in a UAV NOMA downlink where a public flow covers covert packets from an aerial eavesdropper. They minimized aggregate AoI over UAV positions, public and covert beamformers, and freshness variables under power, SIC ordering, covertness, channel-coherence, packet-delivery, and mobility constraints. Their alternating method derives Eve's adverse detector setting, solves AoI by linear programming, updates trajectory by SCA, and updates beamforming by SDR and SCA. Numerical results showed that the optimized path reduced AoI relative to straight and random paths, while tighter covertness and larger covert packets increased the freshness cost.

## Problem

Covert communication hides the existence of a transmission, while AoI measures the freshness of delivered updates. In UAV links, these goals interact: moving closer and beamforming toward the covert user can refresh data faster but can also make detection by an aerial eavesdropper easier. The paper frames the problem as the first UAV-assisted covert-communication design that explicitly minimizes AoI with an aerial eavesdropper.

## System model

- Alice is a UAV with $M$ antennas, serving Bob as the covert user and Carol as the public user.
- Eve is an aerial eavesdropper that can adjust its distance and detection threshold.
- Alice follows a 2-D trajectory at constant altitude over $N$ time slots with a maximum-speed constraint.
- PD-NOMA superimposes public and covert signals; Bob applies SIC.
- The channel model is LoS air-to-ground in the main formulation, with a Rician comparison in experiments.
- Eve uses a radiometer binary hypothesis test.

## Method

The optimization jointly chooses Alice's trajectory, communication beamforming, and AoI-related scheduling under power budget, covert-user fairness, covertness, packet-reception-before-channel-variation, QoS, and maximum-speed constraints. The non-convex problem is decomposed into alternating subproblems: AoI is handled by linear programming, trajectory by SCA, and beamforming by SDR/SCA. The parse states that the relaxed beamforming solution admits a rank-one solution under the paper's theorem, and the numerical implementation uses CVX.

## Key findings

- More antennas and larger transmit-power budgets improve user rates and reduce AoI.
- Increasing the covertness parameter $\epsilon$ increases covert rate, but the public rate decreases enough that total AoI can rise.
- Larger covert packet size increases Bob's allocated slots and Eve's detection-error rate.
- With the covertness constraint, PD-NOMA's rate is only slightly lower than the unconstrained benchmark, while OMA degrades as covert packet size grows.
- Trajectory design gives higher covert rate and lower AoI than straight and random trajectory benchmarks.
- LoS channels yield higher rate and lower AoI than the Rician comparison.
- The moving/tracking aerial Eve benchmark is used as a robust worst-case reference.
- The default simulation places Bob and Carol randomly in a 1 km by 1 km area and uses $M=10$, $H=100$ m, $V_{\max}=30$ m/s, $S_b=45$ Mbit, $S_c=5$ Mbit, $\mu_0=-30$ dB, $B=1$ MHz, $\kappa=3$ dB, $\lambda_0=0.1$ m, and $d_{\min}=25$ m.

## Limitations / future work

The evaluation is numerical and assumes the modeled aerial Eve behavior, channel families, and user placement. The conclusion points to distributed multi-modal foundation models for intelligent 6G network optimization, including AI-driven multi-modal fusion and data parallelism.

## Relation to the corpus

This source connects [[age-of-information]] to [[covert-communication]] through [[freshness-aware-covert-uav-communication]]. It complements [[ma-2024-covert-mmwave-finite-blocklength]], which studies finite-blocklength covert mmWave links against spatially random wardens, and [[wang-2026-secure-lae-uav-scheduling]], which uses UAV communication/jamming role switching for secrecy-energy efficiency. Its public-cover PD-NOMA mechanism also extends the [[noma]] page beyond MEC offloading into covert update freshness.

## Raw artifacts

- Parse: `raw/sources/Age_of_Information_Minimization_in_UAV-Assisted_Covert_Communication_Trajectory_and_Beamforming_Design/Age_of_Information_Minimization_in_UAV-Assisted_Covert_Communication_Trajectory_and_Beamforming_Design.md`
- Origin PDF: `raw/sources/Age_of_Information_Minimization_in_UAV-Assisted_Covert_Communication_Trajectory_and_Beamforming_Design/Age_of_Information_Minimization_in_UAV-Assisted_Covert_Communication_Trajectory_and_Beamforming_Design.pdf`
- Figures: `raw/sources/Age_of_Information_Minimization_in_UAV-Assisted_Covert_Communication_Trajectory_and_Beamforming_Design/images/`
