---
type: source
title: "Joint Trajectory and Beamforming Optimization for UAV-ISAC Secure Communications"
authors: ["Zhaolong Ning", "Yuzhen Zhang", "Xiaojie Wang", "Lei Guo", "Dusit Niyato", "Yan Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3681639"
venue: "IEEE Transactions on Wireless Communications (TWC)"
tags: [source, integrated-sensing-and-communication, physical-layer-security, robust-beamforming, trajectory-optimization]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[physical-layer-security]]"
  - "[[cramer-rao-bound]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[zhaolong-ning]]"
  - "[[dusit-niyato]]"
  - "[[xiaojie-wang]]"
  - "[[lei-guo]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Joint Trajectory and Beamforming Optimization for UAV-ISAC Secure Communications

## Citation

Ning, Z., Zhang, Y., Wang, X., Guo, L., Niyato, D., & Zhang, Y. (2026). Joint trajectory and beamforming optimization for UAV-ISAC secure communications. *IEEE Transactions on Wireless Communications, 25*, 15216-15231. https://doi.org/10.1109/TWC.2026.3681639

## TL;DR

One multi-antenna UAV divides each slot between sensing passive ground eavesdroppers and securely serving one legitimate user. A triple-layer penalty-SCA/SCA/SDR framework jointly controls scheduling, sensing time, 3-D trajectory, and communication/sensing beamformers under CRB-derived channel uncertainty.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna UAV serves $K$ legitimate ground users while sensing and jamming $M$ passive eavesdroppers. Slot $i$ is split into sensing fraction $\eta[i]$ and communication fraction $1-\eta[i]$; legitimate CSI is known and eavesdropper CSI has a CRB-derived bounded error.

**Problem & objective**: Maximize the average worst-case secrecy rate $R_{\mathrm{sec}}=\frac{1}{N}\sum_i\left[R_k^C[i]-\max_mR_m^E[i]\right]^+$ over scheduling, sensing time, trajectory, and communication and sensing beams.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User scheduling | $u_k[i]$ | binary | Whether user $k$ is served in slot $i$ |
| Sensing fraction | $\eta[i]$ | continuous, $0\le\eta[i]\le1$ | Sensing duration ratio |
| UAV trajectory | $\mathbf q^B[i],z^B[i]$ | continuous 3-D | Horizontal position and altitude |
| Communication beam | $\mathbf w_k[i]$ | complex vector | Information beam for user $k$ |
| Sensing/jamming beam | $\mathbf r_m[i]$ | complex vector | Beam aimed at eavesdropper $m$ |
| Lifted beam matrices | $\mathbf W_k[i],\mathbf R_m[i]$ | positive semidefinite relaxations | SDR forms of beam outer products |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Per-slot transmit power: $\sum_k u_k[i]\|\mathbf w_k[i]\|^2+\sum_m\|\mathbf r_m[i]\|^2\le P^{\max}$ |
| C2 | Sensing CRB bounds: $\xi_m[i]\le\xi^{\max}$ and $\psi_m[i]\le\psi^{\max}$ |
| C3 | One scheduled user: $u_k[i]\in\{0,1\}$ and $\sum_k u_k[i]\le1$ |
| C4 | Legitimate-user QoS: $R_k^C[i]\ge R_C^{\min}$ |
| C5 | Eavesdropper leakage bound: $R_m^E[i]\le R_E^{\max}$ |
| C6 | Horizontal and vertical speed limits: $\lVert\mathbf q^B[i+1]-\mathbf q^B[i]\rVert\le V_L^{\max}\tau$ and $\lvert z^B[i+1]-z^B[i]\rvert\le V_Z^{\max}\tau$ |
| C7 | Altitude band: $z^{\min}\le z^B[i]\le z^{\max}$ |
| C8 | Per-slot UAV energy: $E^I[i]+E^F[i]\le E^{\max}$ |

**Algorithm**: Alternate three layers: penalty-based SCA for binary scheduling and sensing time, SCA for the 3-D trajectory, and robust beamforming with matrix lifting, the S-procedure for bounded channel uncertainty, SDR, and iterative rank-one recovery.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ning et al. [x] formulate secure UAV-ISAC design with one multi-antenna UAV, legitimate users, and passive eavesdroppers observed through radar sensing. The problem maximizes average worst-case secrecy rate while jointly optimizing user scheduling, sensing time, trajectory, information beams, and sensing or jamming beams under power, CRB, QoS, speed, altitude, and energy constraints. Their solution alternates penalty SCA for scheduling and sensing time, SCA for trajectory, and robust SDR beamforming with bounded channel uncertainty. In a 500 m square simulation, the secrecy rate rises from about 2.3 to 5.0 bit/s/Hz in the first iterations and stabilizes after roughly six iterations, while lower channel-error bounds outperform larger-error settings.

## Problem and system model

Legitimate channels are perfectly known; a trusted authority identifies eavesdroppers. Sensing echoes estimate eavesdropper range and angle, whose [[cramer-rao-bound|CRBs]] define a conservative bounded channel-error set. The same sensing beams also jam eavesdropping links.

The objective maximizes average secrecy rate subject to power, sensing-accuracy, user/eavesdropper-rate, speed, altitude, endpoint, scheduling, and per-slot UAV-energy constraints.

## Method

Penalty-based SCA relaxes binary scheduling and sensing time. A second SCA block updates the 3-D path. Robust communication/sensing beamforming uses worst-case reformulation, matrix lifting, SDR, LMIs, bisection, and iterative rank-one recovery without Gaussian randomization.

The outer loop monotonically increases a bounded objective from a feasible initialization. This proves objective convergence, not global optimality or stationarity of the original NP-hard problem; the abstract correctly calls the solution suboptimal despite stronger wording elsewhere.

## Key findings

- Figure-derived secrecy rate rises from roughly 2.3 to 5.0 bit/s/Hz within four iterations and stabilizes near six in the displayed setup.
- More candidate users improve optimized scheduling flexibility; larger channel-error bounds reduce secrecy.
- The path descends to the minimum altitude through middle slots, then climbs to the required endpoint altitude.
- Proposed variants outperform fixed-ground-station ISAC and trajectory/power-only UAV-ISAC baselines in simulations, without a headline percentage.

## Limitations

The trusted authority, perfect legitimate CSI, known passive-eavesdropper identities, static ground nodes, independent Gaussian sensing errors, and conservative normalized uncertainty radius are strong assumptions. The uncertainty set is a modeling construction rather than a calibrated real-channel confidence guarantee. The study omits clutter, multipath, node mobility, measured channel errors, and flight validation.

## Relation to the corpus

This paper unifies [[integrated-sensing-and-communication]], robust [[physical-layer-security]], and 3-D UAV motion on one platform. It differs from [[deng-2025-covert-isac-trajectory]], which hides transmission existence, by maximizing secrecy while directly estimating and jamming eavesdropper channels.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_and_Beamforming_Optimization_for_UAV-ISAC_Secure_Communications/Joint_Trajectory_and_Beamforming_Optimization_for_UAV-ISAC_Secure_Communications.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
