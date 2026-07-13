---
type: source
title: "Secrecy Rate Maximization for IRS-Enabled UAV-ISAC Systems via Phase Shifting Adjustment and Resource Allocation"
authors: ["Yuxin Guo", "Xiangdong Jia", "Mangang Xie", "Yue Li"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3578453"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), 10, 289-299"
tags: [source, secure-irs-uav-isac, integrated-sensing-and-communication, intelligent-reflecting-surface, physical-layer-security, artificial-noise, robust-optimization, trajectory-optimization]
related:
  - "[[secure-irs-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[physical-layer-security]]"
  - "[[artificial-noise-aided-physical-layer-security]]"
  - "[[closed-form-irs-phase-alignment]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[csi-estimation-error]]"
  - "[[robust-ris-assisted-uav-secrecy]]"
  - "[[uav-trajectory-control]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[chu-2024-secure-ris-isac]]"
  - "[[li-2021-robust-ris-uav-secrecy]]"
  - "[[jing-2024-isac-trajectory-localization]]"
created: 2026-07-14
updated: 2026-07-14
---

# Secrecy Rate Maximization for IRS-Enabled UAV-ISAC Systems via Phase Shifting Adjustment and Resource Allocation

## Citation

Guo, Y., Jia, X., Xie, M., & Li, Y. (2026). *Secrecy Rate Maximization for IRS-Enabled UAV-ISAC Systems via Phase Shifting Adjustment and Resource Allocation*. **IEEE Transactions on Green Communications and Networking, 10**, 289-299. DOI: 10.1109/TGCN.2025.3578453.

## TL;DR

Jointly optimizes a UAV-mounted IRS's continuous phases and trajectory with base-station beamforming and artificial noise to maximize multiuser secrecy rate while meeting a radar-SNR requirement. Alternating closed-form phase alignment, transformed beamforming, SCA trajectory updates, and worst-case robust extensions produce locally convergent designs under perfect and bounded-error CSI; the evidence is simulation-only and several notation and formulation inconsistencies limit finer claims.

## Problem

An IRS carried by a UAV can reshape both communication and sensing paths, but secrecy, sensing quality, active beamforming, passive phase control, artificial noise, and mobility compete for the same spatial and power resources. The paper studies this [[secure-irs-uav-isac]] design under perfect CSI and under bounded channel and target-angle uncertainty.

## System model

- One `J`-antenna ISAC base station serves `K` legitimate ground users in the presence of one ground eavesdropper and senses one stationary aerial target. A fixed-altitude UAV carries an `M`-element passive UPA IRS and follows constrained horizontal start/end positions and per-slot displacement.
- Each slot is divided by `beta`: the first subslot senses the target, and the second sends communications plus artificial noise (AN). IRS amplitudes are one and phases are continuous.
- Direct BS-user/eavesdropper channels use Rician fading; ground-air and air-air links are LoS-dominant. The effective communication channel combines direct and BS-IRS-ground paths under quasi-static flat fading.
- The BS signal combines `K` user beamformers and AN. Their total power is capped. AN is represented by a scalar variance/power term rather than a fully specified spatial covariance.
- A clutter-free model combines direct and IRS-assisted target responses. Sensing quality is accumulated radar SNR at the BS.
- Perfect-CSI problem P1 maximizes one half of the time/user sum of legitimate rate minus eavesdropping rate over IRS phases, beamforming/AN, and trajectory, subject to sensing-SNR, phase, power, endpoint, and mobility constraints.
- Imperfect-CSI problem P2 maximizes worst-case sum secrecy rate under norm/Frobenius-bounded errors on direct, IRS-ground, and BS-IRS links plus bounded target-angle uncertainty.

## Method

For perfect CSI, alternating optimization uses three blocks:

1. The IRS block applies a closed-form geometric LoS phase rule that adds intended-user alignment and subtracts eavesdropper alignment. The paper presents it as an effective suboptimal rule, not a globally optimal joint phase solution.
2. The active-beamforming block introduces rate auxiliaries and a quadratic/fractional transform, adds an AN-power reward `chi sigma_a^2`, linearizes the sensing constraint by SCA, and solves the convex surrogate with CVX. This is the quadratic-transform branch related to [[fractional-programming-dinkelbach]], not a Dinkelbach iteration in this block.
3. The trajectory block introduces distance and eavesdropper-rate slacks and uses first-order SCA/Taylor bounds for rates, geometry, and sensing before solving with CVX.

Algorithm 1 alternates these updates until relative secrecy-rate change falls below `epsilon` or the iteration limit is reached. The objective is argued to be non-decreasing and bounded, establishing convergence of the sequence but not global optimality. The paper gives complexity as `O(MN + L Nbar K + L(KN)^3.5)`; `Nbar` is not cleanly defined in the parse.

For imperfect CSI, phase alignment adds angular-error compensation. Robust beamforming uses the S-procedure and Schur complement to turn infinitely many bounded-error quadratic constraints into LMIs. Robust trajectory design combines triangle/Cauchy-Schwarz bounds, local trajectory approximations, slack variables, and SCA. These are worst-case local robust updates, not a global robust optimum.

## Key findings

- **Exact prose-supported result:** the perfect-CSI alternating curves stabilize after approximately two iterations. The paper also states that `M = 64` outperforms `M = 16`.
- **Prose-supported trends:** secrecy rate increases with transmit power, BS antenna count, and IRS element count, and decreases as the sensing threshold `mu` rises because sensing consumes resources otherwise available to communication.
- Under imperfect CSI, all tested error settings converge. Secrecy rate increases with power and antenna count but remains slightly below ideal CSI; the paper states that gains become gradual above `P > 14 W`.
- The beampattern discussion reports narrower/stronger mainlobes and lower sidelobes with more antennas, with AN further suppressing non-target radiation. These are qualitative figure/prose findings; no exact dB gain is stated.
- The abstract and contribution text claim improved secrecy rate and positioning accuracy, but the simulation section evaluates sensing primarily through radar SNR and beampatterns and does not tabulate a positioning-error metric.
- **Parsed Table I values:** BS power 12 W, target height 60 m, `M = 16`, reference path loss `L0 = -20 dB` at 1 m, noise `-80 dBm`, `K = 4`, flight time `T = 50`, path-loss exponent 2, IRS spacing `lambda/2`, minimum radar SNR 3 dB, and iteration tolerance `10^-4`.
- The parse associates `N = 6` with antenna/user rows even though the model defines `J` as antenna count and `N` as slot count. It is therefore retained as an unresolved table/notation defect, not reported as an exact antenna or slot value.
- Random IRS phases, no AN, a fixed straight-line UAV trajectory, and random active beamforming are the simulation baselines. The figures are not converted here into exact secrecy-rate margins.

## Limitations / future work

The design assumes one IRS-UAV, one eavesdropper, one stationary target, fixed-altitude 2-D motion, passive unit-amplitude continuous phases, quasi-static channels, LoS-dominant aerial links, a clutter-free sensing model, centralized optimization, and simulation-only validation. It omits phase quantization, UAV attitude/jitter, IRS control latency, pilot and control overhead, uncertainty calibration, and hardware experiments.

Perfect CSI is an upper-bound case. The robust design depends on deterministic bounded-error sets and local approximations. The closed-form phase rule is not proven globally optimal for the joint secrecy/sensing objective, and AO/SCA/CVX provides only local monotonic convergence. AN uses a scalar power model rather than a spatial covariance design. Moreover, the positive AN reward changes the optimized beamforming surrogate from pure secrecy rate unless interpreted as an algorithmic regularizer.

The contribution text says user-SINR constraints are enforced, but displayed P1 has no explicit minimum user-SINR constraint. The model defines `J` antennas and `N` slots, while the simulation prose and figures reuse `N` for antenna count. The coefficient `psi_m = delta_m exp(j phi_m)` is incorrectly described as a phase in `[0,2pi]`; that interval belongs to `phi_m`. Robust-trajectory equations (41)-(44) are severely corrupted in the parse, and Table I includes OCR defects such as `d0 = 1 n`. These defects preclude fine-grained claims from those expressions.

The citation year is 2026 because the journal header is volume 10, 2026, pages 289-299. The manuscript was received, accepted, published online, and marked current version in 2024-2025; this chronology is unusual but is not treated as a parse error.

## Relation to the corpus

[[chu-2024-secure-ris-isac]] is the closest fixed-RIS secure-ISAC optimization anchor, but it maximizes radar output SNR with communication/eavesdropping constraints rather than moving an IRS-UAV to maximize secrecy rate. [[li-2021-robust-ris-uav-secrecy]] supplies the bounded-error, S-procedure, and robust UAV-RIS secrecy lineage with a building-mounted RIS and no sensing target. [[jing-2024-isac-trajectory-localization]] links sensing/localization with trajectory control without this mobile-IRS secrecy architecture.

The paper makes AN an explicit security resource through [[artificial-noise-aided-physical-layer-security]] and combines it with [[closed-form-irs-phase-alignment]], [[uav-trajectory-control]], and [[robust-ris-assisted-uav-secrecy]]. Its secrecy-rate results should not be numerically compared with propulsion-normalized SEE: the objective units, energy accounting, access protocol, and sensing obligations differ.

## Raw artifacts

- Parse: `raw/sources/Secrecy_Rate_Maximization_for_IRS-Enabled_UAV-ISAC_Systems_via_Phase_Shifting_Adjustment_and_Resource_Allocation/Secrecy_Rate_Maximization_for_IRS-Enabled_UAV-ISAC_Systems_via_Phase_Shifting_Adjustment_and_Resource_Allocation.md`
- Origin PDF: `raw/sources/Secrecy_Rate_Maximization_for_IRS-Enabled_UAV-ISAC_Systems_via_Phase_Shifting_Adjustment_and_Resource_Allocation/Secrecy_Rate_Maximization_for_IRS-Enabled_UAV-ISAC_Systems_via_Phase_Shifting_Adjustment_and_Resource_Allocation.pdf`
- Figures: `raw/sources/Secrecy_Rate_Maximization_for_IRS-Enabled_UAV-ISAC_Systems_via_Phase_Shifting_Adjustment_and_Resource_Allocation/images/`
