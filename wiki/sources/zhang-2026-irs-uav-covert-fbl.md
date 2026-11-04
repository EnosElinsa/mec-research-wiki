---
type: source
modeling_card: required
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
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-07-13
updated: 2026-11-03
---

# Joint Trajectory and Beamforming Optimization for IRS-Assisted Multi-Antenna UAV Covert Communications With a Finite Blocklength

## Citation

Zhang, W., Liang, X., Deng, Q., Shu, F., Zhang, Z., Nie, L., & Yan, S. (2026). Joint trajectory and beamforming optimization for IRS-assisted multi-antenna UAV covert communications with a finite blocklength. *IEEE Transactions on Green Communications and Networking, 10*, 426-439. https://doi.org/10.1109/TGCN.2025.3585891

## TL;DR

A fixed-altitude multi-antenna UAV covertly serves Bob while a building-mounted IRS redirects its signal and Willie performs finite-blocklength detection. BCD-SDR alternates relaxed active/passive beamforming with SCA trajectory design; BCD-PDDGP replaces the expensive SDR beamforming blocks with projected-gradient penalty-dual updates.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude multi-antenna transmitter UAV, Alice, covertly communicates with a single-antenna ground receiver, Bob, while a ground warden, Willie, tests for transmission activity. A building-mounted IRS controls the reflected path, direct and cascaded links follow Rician fading, and Bob decodes finite-blocklength packets.

**Problem & objective**: Problem (22) is a nonconvex average covert transmission rate maximization, $\max_{\mathbf Q_a,\mathcal W,\Phi} R=N^{-1}\sum_{\iota=1}^{N}R_b[\iota]$, over the UAV trajectory, active beamforming, and IRS phases.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf Q_a=\{\mathbf o_a[\iota]\}$ | continuous coordinates | Horizontal UAV position in each flight slot |
| UAV transmit beamformer | $\mathcal W=\{\mathbf w[\iota]\}$ | complex continuous vector | Active multi-antenna beamforming toward Bob |
| IRS phase-shift matrix | $\Phi=\{\Theta[\iota]\}$ | unit-modulus complex diagonal matrix | Passive beamforming through per-element IRS phases |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (1) | Mobility: $\lVert\mathbf o_a[1]-\mathbf o_{a,I}\rVert\le V_{\max}\delta_t$, consecutive positions within $V_{\max}\delta_t$, and the prescribed final position |
| (9) | UAV transmit power, $\lVert\mathbf w[\iota]\rVert^2\le P_{a,\max}$ |
| (21) | Covertness at Willie, $\xi^*[\iota]\ge1-\epsilon$, enforced through $\varphi[\iota]\le\bar\varphi$ |
| (22a) | IRS phases $0\le\theta_m[\iota]\le2\pi$ with unit-modulus reflection |

**Algorithm**: Split trajectory, UAV beamforming, and IRS phases into BCD blocks → solve active and passive beamforming by SDR → convexify the trajectory block by SCA → alternate offline LoS trajectory and online instantaneous-CSI beamforming; for lower complexity, replace both SDR blocks with inner projected-gradient augmented-Lagrangian updates and outer penalty-dual updates in BCD-PDDGP.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied IRS-assisted multi-antenna UAV covert communication with a finite blocklength. They formulated average covert transmission rate maximization over the UAV trajectory, UAV transmit beamforming, and IRS phase shifts under mobility, transmit-power, unit-modulus, and covertness constraints. Their BCD-SDR algorithm applies semidefinite relaxation to active and passive beamforming and successive convex approximation to trajectory design. They also developed BCD-PDDGP, which uses projected-gradient penalty-dual updates to reduce the beamforming complexity. Numerical results show that both algorithms converge within three iterations, that BCD-PDDGP attains a covert rate close to BCD-SDR while its complexity grows much more slowly with the number of IRS elements, and that the joint design beats designs without the IRS, with straight flight, or with a single-antenna UAV.

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

Its finite-blocklength Willie test belongs to the activity-hiding branch of [[aerial-observation-control-covertness-surveillance-and-monitoring]]. The DEP/KL constraint does not measure authorized monitoring success, camera coverage, secrecy rate, or track-estimation error.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_and_Beamforming_Optimization_for_IRS-Assisted_Multi-Antenna_UAV_Covert_Communications_With_a_Finite_Blocklength/Joint_Trajectory_and_Beamforming_Optimization_for_IRS-Assisted_Multi-Antenna_UAV_Covert_Communications_With_a_Finite_Blocklength.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
