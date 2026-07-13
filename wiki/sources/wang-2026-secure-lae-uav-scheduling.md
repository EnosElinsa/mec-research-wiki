---
type: source
title: "Energy-Efficient Secure Aerial Communications for Low-Altitude Economy: Joint UAV Scheduling and Trajectory Optimization"
authors: ["Xiaojie Wang", "Qianwen Liu", "Zhaolong Ning", "Tie Qiu", "Lei Guo", "Yan Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3680053"
venue: "IEEE Transactions on Wireless Communications"
tags: [source, low-altitude-economy, secure-communications, physical-layer-security, uav-scheduling, trajectory-optimization, secrecy-energy-efficiency, dinkelbach, sca]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[cooperative-jamming]]"
  - "[[uav-trajectory-control]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[guo-2024-multiuav-proactive-eavesdropping]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[xu-2021-secure-uav-mec-dual-uav]]"
  - "[[zhaolong-ning]]"
  - "[[xiaojie-wang]]"
  - "[[lei-guo]]"
  - "[[secrecy-energy-efficiency]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
created: 2026-07-07
updated: 2026-07-13
---

# Energy-Efficient Secure Aerial Communications for Low-Altitude Economy: Joint UAV Scheduling and Trajectory Optimization

## Citation

Wang, X., Liu, Q., Ning, Z., Qiu, T., Guo, L., & Zhang, Y. (2026). *Energy-Efficient Secure Aerial Communications for Low-Altitude Economy: Joint UAV Scheduling and Trajectory Optimization*. **IEEE Transactions on Wireless Communications**, 25, 14828-14844. DOI: 10.1109/TWC.2026.3680053.

## TL;DR

Studies secure multi-UAV downlink communication for low-altitude economy, where UAVs can switch between communication and jamming roles. The EAIA algorithm maximizes secrecy energy efficiency by jointly optimizing communication/jamming scheduling, transmit power, 3D trajectory, and velocity under imperfect eavesdropper location information.

## Problem

Low-altitude UAV communications are exposed to ground eavesdroppers, and many PLS designs maximize secrecy rate without accounting for propulsion energy or incomplete eavesdropper CSI. This paper targets the secrecy-rate versus propulsion-energy tradeoff by optimizing UAV functional roles, powers, trajectories, and velocities together.

## System model

- Multiple UAVs serve legitimate ground users while ground eavesdroppers try to intercept the transmission.
- A UAV can be selected as a communication UAV for a legitimate user or as a jamming UAV for a ground eavesdropper in each time slot.
- Eavesdropper positions are uncertain and modeled with bounded location error regions.
- Channels use Rician fading with path loss determined by UAV-user/eavesdropper geometry.
- Secrecy rate is the legitimate-user rate minus the maximum eavesdropping rate, clipped at zero.
- UAV energy is dominated by a rotary-wing propulsion model using horizontal and vertical velocity terms; communication energy is neglected relative to propulsion energy in the parse.

## Method

The non-convex secrecy-energy-efficiency maximization is decomposed into three subproblems. UAV communication/jamming scheduling is solved with a penalty-based double-loop algorithm for binary role variables; power allocation is handled by SCA; trajectory and velocity optimization use a Dinkelbach-driven hierarchical iterative algorithm with SCA. The overall Efficient Alternating Iteration Algorithm (EAIA) converges to a suboptimal solution.

## Key findings

- EAIA achieves higher secrecy energy efficiency than the SUS, MPS, FRS, and MARS comparison schemes while keeping comparable latency to FRS.
- Optimized trajectories show UAVs approaching legitimate users for communication and switching to jamming near eavesdroppers to protect other UAV transmissions.
- Lower minimum altitude improves SEE because UAVs get more room to approach users; larger eavesdropper location-error radius reduces SEE because security constraints become tighter.
- SEE and sum secrecy rate increase with mission duration, but MARS sacrifices SEE because it prioritizes secrecy rate and incurs more movement energy.
- In both two-UAV and four-UAV scenarios, EAIA maintains the best SEE in the reported comparisons; all four UAVs in the multi-UAV case perform dual communication/jamming functions.

## Limitations / future work

This is a secure communications paper, not a computation-offloading MEC paper. It is simulation-based and uses a simplified Rician K-factor assumption for the urban environment. The paper states that more refined channel models are a future direction.

## Relation to the corpus

This source extends the [[physical-layer-security]] and [[friendly-jamming-uav]] track into low-altitude-economy secure communication. It differs from [[xu-2021-secure-uav-mec-dual-uav]], which studies secure UAV-MEC computation with a server UAV and jammer UAV, because Wang et al. focus on communication [[secrecy-energy-efficiency]] and allow UAV roles to switch dynamically. [[li-2026-secrecy-ee-uav-ris-iov]] optimizes the same metric under a different threat and energy boundary: one untrusted relay, vehicle-generated jamming, UAV-RIS assistance, and communication power without UAV propulsion. This source is also adjacent to [[guo-2024-multiuav-proactive-eavesdropping]] and [[yao-2025-secure-isac-dual-eavesdropping]] as another multi-UAV security optimization with explicit trajectory and jamming decisions.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient Secure Aerial Communications for Low-Altitude Economy Joint UAV Scheduling and Trajectory Optimization/Energy-Efficient Secure Aerial Communications for Low-Altitude Economy Joint UAV Scheduling and Trajectory Optimization.md`
- Origin PDF: `raw/sources/Energy-Efficient Secure Aerial Communications for Low-Altitude Economy Joint UAV Scheduling and Trajectory Optimization/Energy-Efficient Secure Aerial Communications for Low-Altitude Economy Joint UAV Scheduling and Trajectory Optimization.pdf`
- Figures: `raw/sources/Energy-Efficient Secure Aerial Communications for Low-Altitude Economy Joint UAV Scheduling and Trajectory Optimization/images/`
