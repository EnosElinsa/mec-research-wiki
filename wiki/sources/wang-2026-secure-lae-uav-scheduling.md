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
updated: 2026-07-16
modeling_card: required
---

# Energy-Efficient Secure Aerial Communications for Low-Altitude Economy: Joint UAV Scheduling and Trajectory Optimization

## Citation

Wang, X., Liu, Q., Ning, Z., Qiu, T., Guo, L., & Zhang, Y. (2026). *Energy-Efficient Secure Aerial Communications for Low-Altitude Economy: Joint UAV Scheduling and Trajectory Optimization*. **IEEE Transactions on Wireless Communications**, 25, 14828-14844. DOI: 10.1109/TWC.2026.3680053.

## TL;DR

Studies secure multi-UAV downlink communication for low-altitude economy, where UAVs can switch between communication and jamming roles. The EAIA algorithm maximizes secrecy energy efficiency by jointly optimizing communication/jamming scheduling, transmit power, 3D trajectory, and velocity under imperfect eavesdropper location information.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs provide downlink service to ground users in the presence of uncertain ground eavesdroppers. Each UAV can be scheduled for communication or cooperative jamming and follows a three-dimensional trajectory with propulsion costs.

**Problem & objective**: Problem P1 maximizes secrecy energy efficiency, $\max \frac{\sum_{t,k}R_k^{\mathrm{sec}}(t)}{\sum_{t,m}E_m^{\mathrm{fly}}(t)}$, by jointly scheduling UAV functions and optimizing transmit powers, trajectories, and velocities.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication scheduling | $\lambda_{k,m}[t]$ | binary | Assigns UAV $k$ to serve legitimate user $m$ |
| Jamming scheduling | $\mu_{k,n}[t]$ | binary | Assigns UAV $k$ to jam ground eavesdropper $n$ |
| Communication power | $p_k^S[t]$ | continuous, bounded | Confidential-signal transmit power |
| Jamming power | $p_k^J[t]$ | continuous, bounded | Jamming transmit power |
| UAV trajectory | $(\mathbf q_k[t],z_k[t])$ | continuous, bounded | Horizontal position and altitude |
| UAV velocity | $\mathbf v_k[t]$ | continuous, bounded | Three-dimensional flight velocity |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C3 | Communication and jamming assignments are binary, one-to-one, and give each UAV at most one function per slot |
| C4-C5 | Instantaneous and average communication and jamming powers satisfy their budgets |
| C6 | Each served user satisfies its minimum average secrecy-rate requirement |
| C7 | Pairwise UAV distance remains above the collision-avoidance threshold |
| C8-C11 | Horizontal and vertical speed, acceleration, and altitude remain within flight limits |

**Algorithm**: EAIA alternates among a penalty double-loop scheduler, an SCA-based transmit-power update, and a Dinkelbach and SCA trajectory subproblem. The outer loop repeatedly updates the communication and jamming roles, powers, trajectories, and velocities until the secrecy-energy-efficiency objective stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] investigated secrecy-energy-efficient aerial communication with UAVs that can alternate between user service and cooperative jamming. They maximized aggregate secrecy rate per unit propulsion energy over binary role scheduling, communication and jamming powers, and three-dimensional trajectories under power, rate, collision, and flight constraints. Their EAIA solver combines a penalty double-loop scheduling method, successive convex approximation for power control, and Dinkelbach-based trajectory optimization. The reported experiments showed that EAIA attained the highest secrecy energy efficiency among the compared schemes while retaining latency comparable to fixed-role scheduling. The learned role switches and trajectories remained effective under the examined eavesdropper-location errors and in both two-UAV and four-UAV settings.

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
