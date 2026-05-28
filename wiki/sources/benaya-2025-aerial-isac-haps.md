---
type: source
title: "Aerial ISAC: A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced Coverage and Security"
authors: ["Ahmed M. Benaya", "Mohamed S. Hassan", "Mahmoud H. Ismail", "Taha Landolsi"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2025.3551395"
venue: "IEEE Transactions on Green Communications and Networking"
tags: [isac, haps, full-duplex, physical-layer-security, aav-jammer, beamforming, mec, alternating-optimization]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[high-altitude-platform-station]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[wang-2025-lae-network-survey]]"
created: 2026-05-29
updated: 2026-05-29
---

# Aerial ISAC: A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced Coverage and Security

## Citation

Benaya, A. M., Hassan, M. S., Ismail, M. H., & Landolsi, T. (2025). *Aerial ISAC: A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced Coverage and Security*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2025.3551395.

## TL;DR

A **HAPS-mounted full-duplex ISAC base station** simultaneously serves K downlink UEs, senses L ground targets, offloads sensed data to a ground MEC server for processing, and enables a **friendly-jamming AAV (UAV)** to disrupt eavesdroppers identified through the radar process. The authors formulate joint optimization of (1) the BS transmit/receive beamforming, (2) the AAV trajectory, and (3) jamming power, to maximize the communication sum spectral efficiency under radar-rate, secrecy, offloading, and power constraints.

The problem is non-convex; solved by **alternating optimization (AO)** with **semi-definite relaxation (SDR)** + **successive convex approximation (SCA)**. The HAPS hosts the radio front-end; the heavy data processing of the sensed targets is offloaded to a ground MEC server — that's the "computing" part of the framework.

## Why this matters for MEC

This is the wiki's first **non-DRL ISAC** entry. The MEC role is unusual:

- The HAPS *generates* sensing data (echoes from targets).
- The HAPS *cannot* process it on board because of its energy/payload budget.
- Ground MEC server is the *consumer* of an offloaded sensing workload, not a per-user offloading task.

This inverts the typical "user task → aerial MEC" pipeline that dominates the rest of the corpus. It belongs alongside [[xie-2026-uav-multisource-fusion]] in the **sensing-as-workload** family.

## Method

- **System.** HAPS at fixed altitude z_H with N_t Tx + N_t Rx antennas (TDM-ISAC, one target per slot, one UE per slot). Channels: Rician fading on HAPS-to-ground links; pure LoS on AAV-to-ground.
- **Variables.** Composite beamformer W = [W_c, W_r] (communication + radar streams), radar receive vector u_l, AAV trajectory Q, jamming power p_J.
- **Constraints.** Radar estimation rate ≥ threshold; eavesdropper SINR ≤ threshold; AAV speed ≤ v_max; HAPS Tx power ≤ P_t.
- **Algorithm.** AO over four blocks (Tx beamforming, Rx beamforming, jamming power, AAV trajectory), each block solved via SDR or SCA. Convergence: a few AO iterations.

## Findings

- Joint trajectory + receive-beamforming optimization beats baselines that fix either (non-optimized AAV trajectory; Rayleigh-quotient receive vector).
- Friendly jamming via AAV is effective only when the AAV can position to maximize the eavesdropper-channel-to-victim-channel gap — a trajectory-design problem, not just a power-control problem.

## Limitations

- TDM-ISAC: one target + one UE per slot. Concurrent multi-target sensing is left to future work.
- Quasi-static target assumption (Doppler neglected).
- Eavesdropper CSI assumed known. Robust beamforming under imperfect CSI is the natural extension (and where [[jia-2025-dro-uav-hap-mec]]-style DRO would help).
- DL/ML for ISAC is explicitly excluded — the authors argue training data is too scarce. A defensible position; worth contrasting with the DRL-heavy corpus elsewhere.

## Cross-link with related sources

- **Architecture umbrella:** [[wang-2025-lae-network-survey]] flags ISAC as a pillar of LAE; this paper is a concrete instance.
- **Sensing-as-workload:** alongside [[xie-2026-uav-multisource-fusion]], although that one uses evolutionary multi-objective optimization rather than convex AO.
- **Solver class:** AO + SDR + SCA — first appearance in the wiki of this classic non-DRL toolchain. Worth contrasting with the j-PPO / MASAC / MADDPG patterns that dominate.

## Raw artifacts

- `raw/sources/Aerial ISAC A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced/full.md`
