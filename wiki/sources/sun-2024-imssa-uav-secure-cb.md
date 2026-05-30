---
type: source
title: "UAV-Enabled Secure Communications via Collaborative Beamforming With Imperfect Eavesdropper Information"
authors: ["Geng Sun", "Xiaoya Zheng", "Zemin Sun", "Qingqing Wu", "Jiahui Li", "Yanheng Liu", "Victor C. M. Leung"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3273293"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-swarm, physical-layer-security, collaborative-beamforming, multi-objective, salp-swarm-algorithm, secure-communications]
related:
  - "[[collaborative-beamforming]]"
  - "[[physical-layer-security]]"
  - "[[salp-swarm-algorithm]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[li-2024-emodrl-ground-space-cb]]"
created: 2026-05-31
updated: 2026-05-31
---

# UAV-Enabled Secure Communications via Collaborative Beamforming With Imperfect Eavesdropper Information

## Citation

Sun, G., Zheng, X., Sun, Z., Wu, Q., Li, J., Liu, Y., & Leung, V. C. M. (2024). *UAV-Enabled Secure Communications via Collaborative Beamforming With Imperfect Eavesdropper Information*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3273293. (Date of publication 5 May 2023; date of current version 6 March 2024. Corresponding authors: Zemin Sun, Qingqing Wu. A small part appeared at IEEE ISCC 2022, DOI 10.1109/ISCC55528.2022.9912883.)

## TL;DR

A group of UAVs forms a **UAV-enabled virtual antenna array (UVAA)** and uses **collaborative beamforming (CB)** to transmit toward a cluster of remote base stations, while resisting **multiple known eavesdroppers with imperfect (inaccurately detected) location information and unknown eavesdroppers**. The authors formulate a **secure communication multi-objective optimization problem (SCMOP)** — maximize the worst-case secrecy rate, minimize the maximum sidelobe level (SLL), and minimize UAV flight energy — by jointly optimizing each UAV's 3-D position and excitation-current weight, plus BS selection. The non-convex, NP-hard problem is solved by an **improved multi-objective salp swarm algorithm (IMSSA)**.

## Problem framing

UAV-enabled communications are easily wiretapped because the air-ground channel is line-of-sight dominated. [[physical-layer-security|Physical-layer security]] (PLS) avoids encryption by exploiting channel characteristics, but two challenges arise for UAVs: deploying many antennas on a single UAV is impractical (limited resources), and trajectory-based PLS needs perfect eavesdropper CSI/location, which fails when detection is imperfect or eavesdroppers are unknown. [[collaborative-beamforming|CB]] via a UVAA addresses the antenna-count problem — many UAVs jointly form a high-gain mainlobe toward the receiver and low-gain sidelobes elsewhere. The paper states it is, to the authors' knowledge, the first to **simultaneously** treat known eavesdroppers with imperfect location information **and** unknown eavesdroppers in CB-enabled UAV secure communications, distinguishing it from the authors' prior work (ref. [12]) which assumed perfectly-detected known-eavesdropper locations.

## System model

- **Actors.** A UVAA of UAV elements transmits toward a cluster of base stations; multiple known eavesdroppers (imperfect location info) and unknown eavesdroppers attempt to wiretap ([[air-to-ground-channel-model]]).
- **Decision variables.** Each UAV's 3-D location and excitation-current weight (continuous parts), and the BS selection (discrete part B). Solution dimension grows with the number of UAVs, making the SCMOP a **large-scale** optimization problem (Proposition 3).
- **Objectives (SCMOP).** (1) maximize the **worst-case secrecy rate**; (2) minimize the **maximum sidelobe level (SLL)**; (3) minimize UAV **flight energy consumption**. The paper proves the SCMOP is **non-convex and NP-hard**, with trade-offs among the objectives (Proposition 4).

## Method

- **IMSSA** — an improved multi-objective salp swarm algorithm ([[salp-swarm-algorithm]]) with three tailored operators:
  1. **Circle map-based (chaotic) solution initialization** for a more uniform initial population.
  2. **Discrete solution update operator** to handle the discrete BS-selection dimension that conventional MSSA cannot.
  3. **Migration and adaptive mutation operator** (inspired by biogeography-based optimization) to improve solution quality and diversity over iterations.
- **Complexity.** Proposition 5 gives computational complexity $\mathcal{O}(N_f \cdot N_{pop}^2)$ (objectives × population-size squared).
- **Type.** Swarm-intelligence multi-objective evolutionary optimizer producing a Pareto archive (not a DRL method).

## Key findings

- IMSSA solves the SCMOP effectively and **outperforms the benchmark optimizers** — MOPSO, NSGA-II, MODE, the conventional MSSA, and IMODACH (parse simulation section; specific Pareto/metric curves in the figures).
- Optimized UAV heights tend to be higher than initial heights (higher LoS probability → lower path loss), and IMSSA's optimized UAV locations are more **compact** than the baselines', which the paper argues enhances UVAA communication performance (Figs. 5–6, qualitative).
- A **multi-hop relay** scheme is introduced to verify the reasonability of the UVAA system, and **two benchmark schemes** of the SCMOP are introduced to demonstrate the necessity of the formulated problem.
- An **experimental implementation using a Raspberry Pi** is reported to demonstrate the practicality of the CB-based secure-communication approach in real-world scenarios (the parse describes a hardware implementation; detailed quantitative results are figure-derived and indicative).

## Limitations / future work

Primarily simulation-based with a small-scale hardware demonstration (Raspberry Pi); the parsed conclusion does not enumerate explicit limitations. Reported magnitudes read from MinerU-parsed tables/figures (e.g., the per-direction rate table) should be treated as indicative.

## Relation to the corpus

A **collaborative-beamforming + physical-layer-security** entry from the Jilin-University/NTU [[geng-sun]] cluster, joining the wiki's CB thread — [[sun-2025-emoppo-vlh-aerial-cb]] (aerial CB to a mobile user via evolutionary MORL), [[li-2024-emodrl-ground-space-cb]] (ground-space CB), and [[li-2024-emssa-uav-swarm-vaa]] (UAV-swarm IoT VAA, also a salp-swarm optimizer). Where [[zhang-2024-gdmtd3-aerial-secure-cb]] solves a related *secure* CB problem with a diffusion-enhanced TD3 DRL policy, this paper uses a **swarm-intelligence (IMSSA)** optimizer and is distinctive in modeling **imperfect / unknown eavesdropper** information. It reinforces [[collaborative-beamforming]], [[physical-layer-security]], and [[salp-swarm-algorithm]], and shares the Geng Sun / Zemin Sun / Jiahui Li / Qingqing Wu / Victor C. M. Leung author cluster.

## Raw artifacts

- `raw/sources/UAV-Enabled_Secure_Communications_via_Collaborative_Beamforming_With_Imperfect_Eavesdropper_Information/full.md`
- Original PDF (`b0b407e8-9ff7-4831-a73e-9d790e1b975a_origin.pdf`) and extracted figures (`images/`) in the same folder.
