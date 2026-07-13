---
type: source
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
updated: 2026-07-14
---

# Transmit-Receive Beamforming for ISAC-Enabled Multi-UAVs System

## Citation

Wang, J., Zhang, X., Wang, Y., Yao, X., Wei, Z., Sun, F., & Feng, Z. (2026). *Transmit-Receive Beamforming for ISAC-Enabled Multi-UAVs System*. **IEEE Transactions on Green Communications and Networking, 10**, 652-666. DOI: 10.1109/TGCN.2025.3594962.

## TL;DR

Coordinates sensing/communication transmit beams, clutter-aware receive filters, and multi-UAV positions to maximize summed sensing SCNR subject to downlink SINR, power, mobility, separation, and flight-region constraints.

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
