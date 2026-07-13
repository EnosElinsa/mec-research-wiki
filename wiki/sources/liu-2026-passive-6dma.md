---
type: source
title: "UAV-Enabled Passive 6D Movable Antennas: Joint Deployment and Beamforming Optimization"
authors: ["Changhao Liu", "Weidong Mei", "Peilan Wang", "Yinuo Meng", "Zhi Chen", "Boyu Ning"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3643647"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 9765-9781"
tags: [source, uav-mounted-ris, passive-6dma, aerial-irs, orientation-control, passive-beamforming, max-min-snr]
related:
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[tilt-aware-aerial-ris-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[passive-six-dimensional-movable-antenna]]"
  - "[[angle-dependent-irs-effective-aperture]]"
  - "[[six-dimensional-aerial-rotatable-antenna-array]]"
  - "[[movable-antenna]]"
  - "[[wang-2026-6dara-cellfree]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Enabled Passive 6D Movable Antennas: Joint Deployment and Beamforming Optimization

## Citation

Liu, C., Mei, W., Wang, P., Meng, Y., Chen, Z., & Ning, B. (2026). *UAV-Enabled Passive 6D Movable Antennas: Joint Deployment and Beamforming Optimization*. **IEEE Transactions on Wireless Communications, 25**, 9765-9781. DOI: 10.1109/TWC.2025.3643647.

## TL;DR

Treats a UAV-mounted passive IRS as a rigid six-degree-of-freedom surface whose 3-D location, three-axis orientation, and reflection phases are jointly controlled. The paper proves a one-axis orientation reduction only for a restricted single-user geometry, then applies coarse/fine deployment search, structured penalty-SCA phase design, and Gibbs exploration to multi-user max-min-SNR optimization.

## Problem framing

A passive aerial IRS relays a multi-antenna base station's common downlink signal to remote single-antenna users when direct BS-user links are absent. Translation changes cascaded path loss, rotation changes the surface's effective aperture, and element phases change passive beamforming gain. The paper jointly optimizes these coupled effects to maximize the minimum user SNR.

## System model

- A fixed-altitude UAV carries a rigid rectangular IRS. The whole surface translates horizontally and rotates through three Euler angles; reflecting elements keep fixed relative positions.
- Far-field LoS BS-IRS and IRS-user channels use free-space inverse-square path gain. The direct BS-user link is excluded.
- [[angle-dependent-irs-effective-aperture]] is modeled as the product of incidence- and reflection-angle cosine terms. The BS and every user must remain in the surface's reflecting half-space.
- IRS coefficients have continuous unit modulus. Rank-one BS-IRS LoS structure makes normalized steering/MRT optimal at the base station, leaving location, orientation, and passive phases as the principal variables.

## Method

For the restricted single-user geometry, the method aligns all reflected paths, reduces three-axis orientation to a y-axis angle, derives that angle in closed form for each horizontal position, and searches the remaining scalar position.

For multiple users, conventional AO alternates a two-dimensional coarse/fine location grid, a three-dimensional coarse/fine orientation grid, and structured passive-phase optimization. The phase vector is factored into horizontal and vertical components; each component is lifted to a PSD matrix, rank one is promoted through a nuclear-minus-spectral-norm penalty, and SCA plus SVD recovery produces an iterative phase design. A Gibbs stage then explores neighboring and random feasible location/orientation states with softmax probabilities and retains the best visited state. This is a structured [[alternating-optimization-sdr-sca|AO/SCA]] approximation, not an exact unrestricted phase solution.

## Guarantee scope

For one user at the specified ground location and with the IRS restricted to the corresponding vertical plane, the paper proves that every three-axis orientation has an equal-SNR two-axis counterpart and that a y-axis-only orientation can do at least as well. It then gives the globally optimal y-axis angle for each fixed scalar position. These reductions do not apply to the general multi-user geometry.

The conventional AO objective is stated to be non-decreasing. The Gibbs-enhanced update retains the best visited feasible state, including the current AO state, which supports the paper's convergence claim. There is no global-optimality guarantee for the general problem, no discretization-error bound for the grid search, and no finite-step theorem that Gibbs exploration reaches the global optimum.

## Key findings

- Joint location and orientation optimization outperforms the location-only and orientation-only baselines in the tested single-user curves; orientation is described as more influential in that setup.
- The Gibbs-enhanced AO method outperforms the tested baselines in the sparse and dense three-user simulations. This is numerical evidence, not a general guarantee.
- With 256 reflecting elements, the theoretical per-user passive gain is reported as 48.2 dB, while all three sparse users receive around 40 dB in the plotted optimized case.
- In the mobility test at 100 m altitude, a common user shift of plus or minus 20 m gives approximately 0.1 dB max-min-SNR loss when phases are refreshed but deployment is stale, and approximately 1 dB when both are stale.
- Against the modeled full-duplex amplify-forward relay at 200 m, the passive scheme outperforms the tested 64-antenna relay over the reported power range; a 256-antenna relay eventually performs better at high power. No crossover power is stated in the parse.

## Limitations

The model assumes fixed altitude, calm conditions or effective gimbal damping, full CSI, compensated user Doppler, continuous lossless phases, and LoS far-field channels. It omits propulsion and orientation energy, hard gimbal-rate and acceleration constraints, collision/no-fly-zone constraints, phase quantization, calibration error, localization error, and control latency. Multi-user evaluation uses three deterministic users, grid quality has no error bound, and the separable horizontal/vertical phase construction may exclude non-separable vectors. Validation is numerical only; the mobility test shifts all users together rather than modeling independent motion.

## Relation to the corpus

This source grounds [[passive-six-dimensional-movable-antenna]] as rigid whole-platform translation and rotation of an [[uav-mounted-ris]], with [[angle-dependent-irs-effective-aperture]] coupling orientation to the reflected link. It is not element-level [[movable-antenna]] because the reflecting elements do not move relative to one another. It is also distinct from the active receive array in [[wang-2026-6dara-cellfree]] and [[six-dimensional-aerial-rotatable-antenna-array]]: here the payload is a passive surface that reflects a base-station signal and additionally controls per-element phases. Relative to [[tilt-aware-aerial-ris-control]], the source emphasizes static or quasi-static deployment, analytical single-user geometry, and grid/AO optimization.

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Passive_6D_Movable_Antennas_Joint_Deployment_and_Beamforming_Optimization/UAV-Enabled_Passive_6D_Movable_Antennas_Joint_Deployment_and_Beamforming_Optimization.md`
- Origin PDF: `raw/sources/UAV-Enabled_Passive_6D_Movable_Antennas_Joint_Deployment_and_Beamforming_Optimization/UAV-Enabled_Passive_6D_Movable_Antennas_Joint_Deployment_and_Beamforming_Optimization.pdf`
- Figures: `raw/sources/UAV-Enabled_Passive_6D_Movable_Antennas_Joint_Deployment_and_Beamforming_Optimization/images/`
