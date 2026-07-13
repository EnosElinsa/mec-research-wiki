---
type: source
title: "Wireless Communication for Low-Altitude Economy With UAV Swarm Enabled Two-Level Movable Antenna System"
authors: ["Haiquan Lu", "Yong Zeng", "Shaodan Ma", "Bin Li", "Shi Jin", "Rui Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3689048"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 16463-16479, 2026"
tags: [source, low-altitude-economy, movable-antenna, uav-swarm, near-field-communications, mimo]
related:
  - "[[shi-jin]]"
  - "[[two-level-movable-antenna]]"
  - "[[movable-antenna]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[near-field-communications]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[collaborative-beamforming]]"
  - "[[uav-trajectory-control]]"
  - "[[yong-zeng]]"
created: 2026-07-07
updated: 2026-07-14
---

# Wireless Communication for Low-Altitude Economy With UAV Swarm Enabled Two-Level Movable Antenna System

## Citation

Lu, H., Zeng, Y., Ma, S., Li, B., Jin, S., & Zhang, R. (2026). *Wireless Communication for Low-Altitude Economy With UAV Swarm Enabled Two-Level Movable Antenna System*. **IEEE Transactions on Wireless Communications**, 25, 16463-16479. DOI: 10.1109/TWC.2026.3689048.

## TL;DR

Treats the UAV swarm itself as a first-level movable antenna system and each UAV's local movable array as a second-level movable antenna. The paper maximizes the minimum uplink user rate by jointly optimizing UAV swarm placement, local antenna positions, and receive beamforming under safety and array-spacing constraints.

## Problem

Movable-antenna work often optimizes element positions inside a fixed platform, while UAV swarms have another mobility layer: each UAV can relocate in 3D. The paper asks how to exploit both swarm-level UAV placement and local per-UAV antenna movement for low-altitude economy communications.

## System model

The system has a UAV swarm with multiple UAVs serving multiple single-antenna ground users on the uplink. Each UAV carries a linear movable-antenna array. UAV positions are constrained to a 3D region with safe inter-UAV distance; local antenna elements move along bounded arrays with spacing constraints. The user-to-UAV channel uses line-of-sight near-field spherical wavefronts for the swarm-level geometry, while each local array uses a uniform-plane-wave approximation.

## Method

The paper formulates max-min achievable rate over UAV placement, local antenna positions, and receive beamforming. For special single-antenna cases, it derives structural results: with one user, SNR is independent of array geometry; with two users under UPW, a uniform sparse array can remove inter-user interference. For general cases, it alternates between MMSE receive beamforming and SCA-based placement/position updates. It also discusses synchronization and position-error compensation through channel estimation.

## Key findings

- The single-antenna algorithm produces non-decreasing minimum rate and approaches the inter-user-interference-free upper bound in the parsed experiments.
- For two users, the proposed geometry achieves interference-free communication and zero SNR loss in the reported comparison, outperforming circular-array geometries with MMSE, ZF, or MRC receivers.
- For three users, the proposed scheme remains close to the interference-free upper bound and outperforms circular MMSE and distributed-MIMO baselines as transmit power increases.
- In the multi-antenna setting with two UAVs and four local elements per UAV, two-level movable antennas outperform circular fixed-position arrays and placement-optimized fixed-position arrays.
- Expanding the local movable region improves minimum rate until the interference-free upper bound becomes limiting.
- Error compensation with synchronization and position errors reports performance comparable to the no-error case in the parsed experiment.

## Limitations / future work

The paper names channel modeling with array misalignment/orientation jitter and multipath, energy consumption and latency, flight-control/safety mechanisms, and IRS integration as future research directions.

## Relation to the corpus

This source extends [[movable-antenna]] from a UAV-to-UAV channel model in [[zeng-2026-movable-antenna-u2u-channel]] to a LAE swarm-communication design problem. It also connects to [[collaborative-beamforming]], but the control variable is physical UAV/antenna placement for rate balancing rather than virtual-array excitation weights for remote communication or secrecy.

## Raw artifacts

- `raw/sources/Wireless Communication for Low-Altitude Economy With UAV Swarm Enabled Two-Level Movable Antenna System/Wireless Communication for Low-Altitude Economy With UAV Swarm Enabled Two-Level Movable Antenna System.md`
- Original PDF and extracted figures (`images/`) in the same folder.
