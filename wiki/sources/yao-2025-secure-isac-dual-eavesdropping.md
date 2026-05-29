---
type: source
title: "UAV-Enabled Secure ISAC Against Dual Eavesdropping Threats: Joint Beamforming and Trajectory Design"
authors: ["Jianping Yao", "Zeyu Yang", "Zai Yang", "Jie Xu", "Tony Q. S. Quek"]
year: 2025
url: "https://doi.org/10.1109/LWC.2025.3588758"
venue: "IEEE Wireless Communications Letters (IEEE LWC)"
tags: [source, isac, physical-layer-security, uav, beamforming, trajectory-design, secrecy-rate]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[qcqp-sdr-probabilistic-mapping]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
created: 2026-05-29
updated: 2026-05-29
---

# UAV-Enabled Secure ISAC Against Dual Eavesdropping Threats: Joint Beamforming and Trajectory Design

## Citation

Yao, J., Yang, Z., Yang, Z., Xu, J., & Quek, T. Q. S. (2025). *UAV-Enabled Secure ISAC Against Dual Eavesdropping Threats: Joint Beamforming and Trajectory Design*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2025.3588758.

## TL;DR

A letter on **secure UAV-enabled ISAC**: a UAV serves as an aerial base station communicating with a user and sensing a ground target, while a **dual-functional eavesdropper** tries to intercept both the communication and the sensing signals. The authors maximize the average achievable secrecy rate by jointly designing the UAV trajectory and the transmit information + sensing beamforming, subject to sensing-performance, sensing-security, UAV-power, and flight constraints. The non-convex problem is solved by **alternating optimization (AO) + SCA + SDR**.

## Problem framing

ISAC shares hardware/spectrum for communication and sensing, but a dual-functional eavesdropper threatens both. The challenge is to keep the communication secret *and* the sensing secure while still meeting sensing-performance requirements, using the UAV's mobility and beamforming.

## System model

- **Actors.** A UAV (aerial dual-functional BS), a communication user, a ground sensing target, and a dual-functional eavesdropper (intercepts info + sensing).
- **Objective.** Maximize average achievable secrecy rate.
- **Constraints.** Sensing performance, sensing security, UAV power, flight constraints.
- **Variables.** UAV trajectory, transmit information beamforming, sensing beamforming.

## Method

- **Alternating optimization (AO)** combined with **successive convex approximation (SCA)** and **semidefinite relaxation (SDR)** to handle the non-convex problem ([[alternating-optimization-sdr-sca]], [[qcqp-sdr-probabilistic-mapping]]).

## Key findings

- Numerical results validate the approach, achieving a high secrecy rate while meeting the required sensing and security constraints (qualitative; specific curves in the paper).

## Limitations / future work

The authors flag: multiple users in complex dynamic environments, real-time adaptive algorithms, robust optimization for CSI uncertainty, realistic UAV mobility/energy constraints, multiple antennas, and global-optimality solutions.

## Relation to the corpus

A **secure ISAC** entry combining physical-layer security with UAV trajectory + beamforming, framed by the UAV-ISAC overview [[meng-2024-uav-isac-overview]] (shared co-authors Jie Xu). It complements the HAPS ISAC framework [[benaya-2025-aerial-isac-haps]] and the UAV-swarm secure-beamforming work [[zhang-2024-gdmtd3-aerial-secure-cb]] — using classical AO/SCA/SDR rather than DRL. Reinforces [[physical-layer-security]] and [[integrated-sensing-and-communication]].

## Raw artifacts

- `raw/sources/UAV-Enabled_Secure_ISAC_Against_Dual_Eavesdropping_Threats_Joint_Beamforming_and_Trajectory_Design/full.md`
- Original PDF and extracted figures in the same folder.
