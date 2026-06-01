---
type: source
title: "Resource and Trajectory Optimization for UAV-Relay-Assisted Secure Maritime MEC"
authors: ["Fangwei Lu", "Gongliang Liu", "Weidang Lu", "Yuan Gao", "Jiang Cao", "Nan Zhao", "Arumugam Nallanathan"]
year: 2023
url: "https://doi.org/10.1109/TCOMM.2023.3330884"
venue: "IEEE Transactions on Communications (IEEE TCOM)"
tags: [source, maritime-mec, uav-mobile-relaying, physical-layer-security, cooperative-jamming, uav-trajectory-control, alternating-optimization-sdr-sca, binary-vs-partial-offloading]
related:
  - "[[maritime-mec]]"
  - "[[uav-mobile-relaying]]"
  - "[[physical-layer-security]]"
  - "[[cooperative-jamming]]"
  - "[[friendly-jamming-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[secure-computation-efficiency]]"
  - "[[information-causality-constraint]]"
  - "[[li-2023-secure-marine-iot-jamming]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
  - "[[hu-2019-uav-relay-edge-computing]]"
  - "[[zhan-2020-completion-time-energy-uav-mec]]"
created: 2026-06-02
updated: 2026-06-02
---

# Resource and Trajectory Optimization for UAV-Relay-Assisted Secure Maritime MEC

## Citation

Lu, F., Liu, G., Lu, W., Gao, Y., Cao, J., Zhao, N., & Nallanathan, A. (2023). *Resource and Trajectory Optimization for UAV-Relay-Assisted Secure Maritime MEC*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2023.3330884. (Manuscript received 2 June 2023; revised 17 September 2023; accepted 28 October 2023; date of publication 7 November 2023; date of current version 19 March 2024 → year 2023.)

## TL;DR

Proposes a **secure communication scheme for UAV-relay-assisted maritime MEC** with a **flying (UAV) eavesdropper**. A relay UAV (`UAV_r`) **amplify-and-forwards** maritime-device (MD) computing tasks to a coastal edge server (CES), while an eavesdropping UAV (`UAV_e`) tries to overhear the offloaded data and a **coastal jammer (CJ)** emits friendly jamming to disrupt it (CES knows the jamming signal, `UAV_e` does not). The scheme **maximizes the minimum (max-min) secure computing capacity** of the MDs by jointly optimizing **transmit power, time-slot allocation, local-computation allocation, and the `UAV_r` trajectory**. The non-convex problem is transformed with auxiliary variables and solved by **block coordinate descent (BCD) + successive convex approximation (SCA)**.

## Problem framing

Maritime devices generate explosive data but are compute-limited and usually far from shore, with poor maritime channels — so direct MD↔CES links cannot carry massive offloading. A UAV relay improves the link via mobility, but its **LoS channels make offloaded data easy to eavesdrop**, and a **flying eavesdropper has a far better channel than a fixed ground eavesdropper** (introducing an inter-UAV anti-collision concern absent for ground eavesdroppers). Secure transmission in UAV-relay-assisted maritime MEC was not well studied, motivating a physical-layer-security scheme combining relaying, friendly jamming, and joint resource/trajectory optimization.

## System model

- **Nodes.** `K` MDs, two UAVs (`UAV_r` relay, `UAV_e` eavesdropper), one CES, one CJ. `UAV_r` uses **amplify-and-forward (AF)** relaying; CJ jams `UAV_e`; CES treats CJ's signal as known/friendly (no self-interference), `UAV_e` cannot cancel it.
- **Geometry/channels.** UAVs fly at constant altitude over `N` discrete time slots from fixed initial to final positions, under a per-slot max-displacement (speed) limit and an inter-UAV **collision-avoidance distance** `d_min`. Air-to-sea links use **Rician fading** (large-scale + small-scale), distance-dependent path loss.
- **Protocol.** Each slot is split per-MD by **TDMA** time-slot factor `ξ_k[n]`; each sub-slot has two equal phases — phase 1: MD→`UAV_r` offload (overheard by `UAV_e`, jammed by CJ); phase 2: `UAV_r`→CES AF forward. Secure offloading rate is `(Φ_{k,s} − Φ_{k,e})^+` (legitimate minus eavesdropping rate).
- **Computing.** **Partial offloading**: part computed locally at the MD (CPU-frequency cap, `k_k f^3`-style energy), the rest forwarded to CES; per-MD minimum secure-computing requirement `Q_k` and an average-power budget `P^ave_k` over period `T`.
- **Objective (P1).** `max-min_k` average **secure computing capacity** `Φ̄_{k,sec}` over `{ξ_k[n], p_k[n], p_r[n], l_{k,loc}[n], u_r[n]}`, subject to trajectory, collision, power, time-slot, CPU, and energy-budget constraints. Coupled and non-convex.

## Method

- **Transformation.** Introduce auxiliary variables (`θ`, `θ_{1,k}[n]`, `θ_{2,k}[n]`) to recast the max-min secure-capacity problem (P2) into an equivalent form and drop the `[·]^+` operator (zero achievable by setting powers/local bits to zero).
- **BCD + SCA.** Decompose into subproblems and apply **successive convex approximation** iteratively; a **feasibility check** (solving for `Q^u_k`) adjusts initialization so the per-MD secure-requirement constraints are satisfiable.
- **Complexity.** With `I_1` BCD iterations, the stated per-run complexity is `I_1 · O((KN)^{3.5} log(1/ε))`.

## Key findings

- The proposed scheme is reported to **effectively improve secure computing capability** versus four benchmark approaches (parse); specific margins are figure-derived, treat as indicative.
- **Larger flight period `T` raises the max-min secure computing capacity** because `UAV_r` gets more time to approach MDs and hover longer over each (Figs. 2–4): at `T = 50` s `UAV_r` passes few MDs, at `T = 70` s it covers more with longer per-MD hovering.
- Simulation setup (parse): a 1500 × 2000 m² sea area, five MDs, CES and CJ both fixed at the origin, `UAV_r` flying `[0,0]→[2000,0]`, `UAV_e` flying `[0,750]→[2000,−750]` at constant speed, `V^max_r = 50` m/s, `d_min = 1` m.

## Limitations / future work

Evaluation is **simulation-only**. The eavesdropper UAV flies a **fixed straight-line trajectory at constant speed**, `UAV_r` and CES are assumed to know the CSI of the legitimate/jamming links in advance (e.g. via synthetic aperture radar), CES/CJ are approximated as maritime nodes, and a **single relay + single eavesdropper + single jammer** topology is considered. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **secure maritime MEC** entry combining [[uav-mobile-relaying|UAV mobile relaying]] (AF) with [[physical-layer-security]] against a **flying** eavesdropper. Its **coastal-jammer** design is the single-helper, shore-based analogue of the multi-USV [[cooperative-jamming]] in [[li-2023-secure-marine-iot-jamming]] and the aerial [[friendly-jamming-uav]] elsewhere; its max-min secure objective is kin to the [[secure-computation-efficiency]] maximized in [[michailidis-2024-secure-ris-uav-mec-iot]]. Methodologically it sits in the [[alternating-optimization-sdr-sca|BCD + SCA]] family and shares the relay-plus-MEC-server fusion and trajectory machinery of [[hu-2019-uav-relay-edge-computing]] (and the fixed-wing trajectory + AO + SCA lineage of [[zhan-2020-completion-time-energy-uav-mec]]) within the [[maritime-mec]] track. It uses [[binary-vs-partial-offloading|partial offloading]] and relates to the [[information-causality-constraint]] of UAV relaying.

## Raw artifacts

- `raw/sources/Resource_and_Trajectory_Optimization_for_UAV-Relay-Assisted_Secure_Maritime_MEC/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
