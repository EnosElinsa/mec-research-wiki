---
type: source
modeling_card: required
title: "Transmit-Receive Beamforming for ISAC-Enabled Multi-UAVs System"
authors: ["Jinyu Wang", "Xianchao Zhang", "Yi Wang", "Xue Yao", "Zhiqing Wei", "Fengsong Sun", "Zhiyong Feng"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3594962"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 652-666"
tags: [source, multi-uav, isac, transmit-receive-beamforming, clutter, scnr, trajectory-optimization]
related:
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[uav-trajectory-control]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[wang-2026-robust-anti-uav-isac]]"
  - "[[zhiyong-feng]]"
created: 2026-07-14
updated: 2026-07-16
---

# Transmit-Receive Beamforming for ISAC-Enabled Multi-UAVs System

## Citation

Wang, J., Zhang, X., Wang, Y., Yao, X., Wei, Z., Sun, F., & Feng, Z. (2026). *Transmit-Receive Beamforming for ISAC-Enabled Multi-UAVs System*. **IEEE Transactions on Green Communications and Networking, 10**, 652-666. DOI: 10.1109/TGCN.2025.3594962.

## TL;DR

Coordinates sensing/communication transmit beams, clutter-aware receive filters, and multi-UAV positions to maximize summed sensing SCNR subject to downlink SINR, power, mobility, separation, and flight-region constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs jointly transmit integrated sensing and communication waveforms, receive target echoes in clutter, and serve downlink users. UAV locations, transmit beams, and clutter-aware receive filters jointly determine sensing SCNR and communication SINR.

**Problem & objective**: A non-convex sum-of-ratios problem maximizes aggregate sensing quality, $\max \sum_m\operatorname{SCNR}_m$, under downlink QoS, power, mobility, separation, and flight-region constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Transmit beamformer | $\mathbf w_{m,k}$ | complex continuous vector | Communication or sensing beam sent by UAV $m$ |
| Receive filter | $\mathbf u_m$ | complex continuous vector | Clutter-aware target-echo combiner |
| UAV position | $\mathbf q_m$ | continuous horizontal position | Fixed-altitude UAV deployment or trajectory |
| Fractional/slack variables | $\boldsymbol\xi$ | continuous | Dinkelbach, SDR, and SCA auxiliaries |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every served user meets its downlink SINR requirement |
| C2 | Each UAV's transmit beams satisfy its power budget |
| C3 | UAV positions remain in the allowed flight region |
| C4 | Per-slot motion and prescribed trajectory conditions remain feasible |
| C5 | Pairwise UAV separation remains above the collision threshold |

**Algorithm**: Fix beams and positions and update each receive filter by the generalized-Rayleigh-quotient eigenvector → optimize transmit beams through a Dinkelbach-style fractional reformulation and SDR → update UAV positions with fractional transformation, SCA, slacks, and a trust region → alternate until summed SCNR converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied transmit-receive beamforming and UAV positioning in an ISAC-enabled multi-UAV network with target clutter. They formulated summed sensing-SCNR maximization over transmit beams, receive filters, and UAV positions under downlink SINR, power, mobility, separation, and flight-region constraints. Each receive filter is updated from a generalized Rayleigh quotient for fixed transmit beams and geometry. The transmit block uses a Dinkelbach-style sum-of-ratios reformulation and semidefinite relaxation, while the trajectory block uses fractional transformation and successive convex approximation. Simulations report higher detection and SCNR than the evaluated single-UAV and fixed-hovering baselines, including a sensing gain from mobility in the stated scenario.

## Method and guarantee scope

For fixed transmit beams and geometry, each receive filter is the globally optimal generalized-Rayleigh-quotient eigenvector. The transmit block uses a Dinkelbach-style sum-of-ratios reformulation and SDR; the paper claims rank recovery but also discusses Gaussian randomization when relaxed solutions are not rank one. The trajectory block uses fractional transformation, SCA, slack variables, and a trust region.

The alternating updates are shown to produce a nondecreasing objective under the modeled subproblems. They do not globally solve the original joint non-convex problem.

## Findings

Three-UAV simulations averaged over 1,000 trials report higher detection/SCNR than single-UAV and fixed-hovering baselines. Mobility gives a reported 32% sensing improvement in the tested scenario, and the SCNR curves settle after roughly ten iterations. Sensing performance falls as the required communication SINR rises.

## Limitations

Simulation only; ideal backhaul, perfect pilots/synchronization, known positions, quasi-static CSI, fixed altitude, static clutter, one target, exclusive user association, and perfect Doppler cancellation. The SDR-tightness narrative is internally inconsistent, the trust-region update rule is unusual, and broad SCNR-to-CRB equivalence is asserted without derivation.

## Relation to the corpus

This source extends [[cooperative-isac-transceiver-beamforming]] from fixed multi-cell anti-UAV sensing in [[zhang-2025-cooperative-anti-uav-isac]] toward jointly mobile transmit/receive UAVs. Relative to the robust target-tracking formulation in [[wang-2026-robust-anti-uav-isac]], it emphasizes clutter-aware transceiver coupling and sum sensing SINR rather than worst-case CRB under target-location uncertainty.

## Raw artifacts

- Parse: `raw/sources/Transmit-Receive_Beamforming_for_ISAC-Enabled_Multi-UAVs_System/Transmit-Receive_Beamforming_for_ISAC-Enabled_Multi-UAVs_System.md`
- Original PDF and extracted figures are in the same folder.
