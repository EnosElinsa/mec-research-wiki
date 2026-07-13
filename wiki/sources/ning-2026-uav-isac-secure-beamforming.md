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
updated: 2026-07-13
---

# Joint Trajectory and Beamforming Optimization for UAV-ISAC Secure Communications

## Citation

Ning, Z., Zhang, Y., Wang, X., Guo, L., Niyato, D., & Zhang, Y. (2026). Joint trajectory and beamforming optimization for UAV-ISAC secure communications. *IEEE Transactions on Wireless Communications, 25*, 15216-15231. https://doi.org/10.1109/TWC.2026.3681639

## TL;DR

One multi-antenna UAV divides each slot between sensing passive ground eavesdroppers and securely serving one legitimate user. A triple-layer penalty-SCA/SCA/SDR framework jointly controls scheduling, sensing time, 3-D trajectory, and communication/sensing beamformers under CRB-derived channel uncertainty.

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
