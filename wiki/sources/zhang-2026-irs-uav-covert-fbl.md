---
type: source
title: "Joint Trajectory and Beamforming Optimization for IRS-Assisted Multi-Antenna UAV Covert Communications With a Finite Blocklength"
authors: ["Wei Zhang", "Xiaopeng Liang", "Qian Deng", "Feng Shu", "Zhi Zhang", "Liusong Nie", "Shihao Yan"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3585891"
venue: "IEEE Transactions on Green Communications and Networking (TGCN)"
tags: [source, covert-communication, finite-blocklength, intelligent-reflecting-surface, trajectory-optimization]
related:
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[covert-communication]]"
  - "[[finite-blocklength-urllc]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[penalty-dual-decomposition]]"
  - "[[deng-2025-covert-isac-trajectory]]"
created: 2026-07-13
updated: 2026-07-14
---

# Joint Trajectory and Beamforming Optimization for IRS-Assisted Multi-Antenna UAV Covert Communications With a Finite Blocklength

## Citation

Zhang, W., Liang, X., Deng, Q., Shu, F., Zhang, Z., Nie, L., & Yan, S. (2026). Joint trajectory and beamforming optimization for IRS-assisted multi-antenna UAV covert communications with a finite blocklength. *IEEE Transactions on Green Communications and Networking, 10*, 426-439. https://doi.org/10.1109/TGCN.2025.3585891

## TL;DR

A fixed-altitude multi-antenna UAV covertly serves Bob while a building-mounted IRS redirects its signal and Willie performs finite-blocklength detection. BCD-SDR alternates relaxed active/passive beamforming with SCA trajectory design; BCD-PDDGP replaces the expensive SDR beamforming blocks with projected-gradient penalty-dual updates.

## Problem and system model

Direct and IRS-cascaded UAV links use Rician fading. Bob's rate follows the finite-blocklength normal approximation, while Willie tests transmission versus silence over the same block. The optimizer uses a Pinsker/KL sufficient covertness bound rather than the exact incomplete-gamma detection-error expression.

The objective maximizes average covert rate over horizontal trajectory, UAV beamformers, and unit-modulus IRS phases subject to endpoints, speed, transmit power, and covertness. Propulsion and onboard energy are not modeled.

## Method

BCD-SDR lifts UAV and IRS beamformers, drops rank-one constraints, and uses SVD or Gaussian randomization after solving SDPs. Its trajectory block freezes array responses at the previous path and applies SCA. The path is optimized offline from LoS components; beamforming and phases are then updated online from instantaneous CSI.

BCD-PDDGP uses an augmented-Lagrangian [[penalty-dual-decomposition]] with projected-gradient beam/phase updates and a closed-form slack update. Its phase block scales linearly with IRS size under the paper's assumptions, but the complete algorithm still includes trajectory-solver cost.

## Key findings

- Both algorithms stabilize within three outer iterations for the displayed four-antenna, 50/80-element simulations; this is setting-specific.
- PDDGP approaches SDR's covert rate while its reported complexity grows much more slowly with IRS size.
- More antennas/elements, power, and mission time improve tested covert rate; stricter covertness keeps the path farther from Willie.
- Covert rate is non-monotonic in blocklength because longer blocks reduce coding dispersion but give Willie more observations.

## Limitations

One Bob, one Willie, one IRS, fixed altitude/duration, known terminal positions, and obtainable Willie CSI are assumed. Covertness uses a conservative sufficient bound. SDR recovery and PDDGP are suboptimal; convergence is not global optimality. The parse is formula-damaged, and all evaluation is numerical without propulsion energy or flight experiments. The externally verified final metadata is absent from the parse.

## Relation to the corpus

[[deng-2025-covert-isac-trajectory]] uses sensing signals as cover, while this source couples [[finite-blocklength-urllc]] with an IRS and active/passive beamforming. [[ma-2024-covert-mmwave-finite-blocklength]] is the finite-blocklength covert anchor without trajectory/IRS coupling.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_and_Beamforming_Optimization_for_IRS-Assisted_Multi-Antenna_UAV_Covert_Communications_With_a_Finite_Blocklength/Joint_Trajectory_and_Beamforming_Optimization_for_IRS-Assisted_Multi-Antenna_UAV_Covert_Communications_With_a_Finite_Blocklength.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
