---
type: source
title: "Reinforcement Learning With Conformal Symplectic Optimization for Aerial RIS-Aided Secure Communication"
authors: ["Zhongming Feng", "Qiling Gao", "Haoran Zha", "Yun Lin", "Yuanwei Liu", "Dusit Niyato", "Marco Di Renzo"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3670412"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 13560-13574"
tags: [source, aerial-ris, physical-layer-security, secrecy-energy-efficiency, imperfect-csi, td3, uav-trajectory-control, phase-error, attention]
related:
  - "[[phase-aware-relativistic-adaptive-descent]]"
  - "[[environment-state-interactive-attention]]"
  - "[[uav-mounted-ris]]"
  - "[[physical-layer-security]]"
  - "[[secrecy-energy-efficiency]]"
  - "[[csi-estimation-error]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[td3]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
  - "[[li-2026-aerial-ris-trajectory-phase]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[yuanwei-liu]]"
  - "[[dusit-niyato]]"
  - "[[marco-di-renzo]]"
created: 2026-07-14
updated: 2026-07-14
---

# Reinforcement Learning With Conformal Symplectic Optimization for Aerial RIS-Aided Secure Communication

## Citation

Feng, Z., Gao, Q., Zha, H., Lin, Y., Liu, Y., Niyato, D., & Di Renzo, M. (2026). *Reinforcement Learning With Conformal Symplectic Optimization for Aerial RIS-Aided Secure Communication*. **IEEE Transactions on Wireless Communications, 25**, 13560-13574. DOI: 10.1109/TWC.2026.3670412.

## TL;DR

Proposes IA-CSORL, a cooperating two-agent [[td3|TD3]] framework for a [[uav-mounted-ris]] under mobile users, imperfect CSI, GPS error, and jitter-induced RIS phase error. One agent uses [[phase-aware-relativistic-adaptive-descent|PRAD]] for BS/RIS beamforming; the other uses [[environment-state-interactive-attention|ESIA]] to fuse UAV position history with communication and mobility features for trajectory control.

## Problem and system model

A multi-antenna BS serves single-antenna mobile users in the presence of potential single-antenna eavesdroppers. Direct BS-to-ground links are blocked, and an RIS mounted on a fixed-altitude rotorcraft UAV supplies the reflected links. The joint design controls UAV motion, BS beamforming, and RIS phases under secrecy-QoS, BS-power, phase, flight-region, and displacement constraints.

The channel model combines time-varying 3-D Saleh-Valenzuela/Rician links with [[csi-estimation-error]]. UAV GPS error is Gaussian, and jitter perturbs each RIS element's ideal phase according to a zero-mean von Mises distribution. Propulsion energy follows a [[rotary-wing-propulsion-energy-model]] with blade-profile, induced-power, and parasitic-drag terms. The performance metrics are sum secrecy rate (SSR) and [[secrecy-energy-efficiency]] (SSR divided by propulsion energy).

The paper contains an unresolved CSI-factor inconsistency that should be preserved. Equations (12)-(13) use

$$
\mathbf{O}=\sqrt{\kappa_o}\,\hat{\mathbf{O}}+\sqrt{1-\kappa_o}\,\Delta\mathbf{O},\qquad
\mathbf{h}_i=\sqrt{\kappa_i}\,\hat{\mathbf{h}}_i+\sqrt{1-\kappa_i}\,\Delta\mathbf{h}_i,
$$

which gives more weight to the estimated channel as $\kappa$ increases. The accompanying prose instead says $\kappa=0$ is perfect estimation and $\kappa=1$ is completely unreliable. The source does not reconcile these opposite directions.

## Method

IA-CSORL decomposes control between two cooperating TD3 agents. Agent 1 selects BS beamforming and the next RIS phase matrix. Its [[phase-aware-relativistic-adaptive-descent|PRAD]] optimizer maps parameter updates to a dissipative conformal Hamiltonian system, applies conformal-symplectic discretization and relativistic step limiting, scales RIS-phase gradients by a von-Mises correction factor, and adapts first-order momentum from successive gradient changes.

Agent 2 selects UAV displacement. [[environment-state-interactive-attention|ESIA]] uses current UAV position as the query, CSI/user positions/UAV velocity as environment features, and those features plus the previous UAV position as values. Scaled dot-product attention produces the trajectory agent's interaction-enhanced state.

Both agents use the same shaped reward:

$$
r_n=\tanh\!\left(\sum_q R_q^{\mathrm{secret}}-c_1p_m-c_2p_r-c_3p_g-c_4p_e\right),
$$

where the penalties cover secrecy-QoS, transmit-power, mobility, and normalized propulsion-energy terms. This is not the stated SEE ratio objective. It is a learning surrogate introduced because direct ratio optimization was reported to encourage denominator reduction early in training; its behavior depends on manually selected penalty weights and normalization.

## Key findings

- In Fig. 4, all compared methods are reported to converge within 1,500 episodes. IA-CSORL stabilizes around episode 1,000 at an average reward of roughly 40, compared with approximately 25 for the PRAD-only variant, 20 for the ESIA-only variant, and 8 for TDDRL after 2,000 episodes. These are approximate figure readings. The paper's "global equilibrium" interpretation of the reward curves is not a proof of global optimality; its convergence analysis states convergence to a stable local minimum.
- Fig. 5 qualitatively shows IA-CSORL tracking users, avoiding the eavesdropper, and remaining relatively close to the BS, while TDDRL crosses the $y=-40$ m boundary. This single simulated trajectory does not establish general constraint satisfaction.
- Under phase-error scaling 0.5, Fig. 6 reports 4.5 bit/s/Hz SSR with 48 RIS elements, while conventional TTD3 requires 64 elements for a similar value. The proposed method and its ablations reach around 60 bit/s/Hz/kJ SEE at 48 elements, while TTD3 requires 64. These values are figure-derived, and the dashed curves summarize the top three points rather than full-distribution averages.
- With 32 RIS elements and controlled perturbations of ideal phases, Fig. 7 reports that PRAD improves SSR by 1.34 bit/s/Hz and nearly doubles SEE over the Adam-based ESIA comparison at error scaling $\epsilon=0.1$; at $\epsilon=1.5$, it retains a reported 12% SSR gain. These claims apply to that simulation and ablation setup.
- At a GPS-position standard deviation of 3 m and 64 RIS elements, Fig. 8 reports approximately 60 bit/s/Hz/kJ SEE for IA-CSORL and about 42 for the PRAD-only variant. Both are approximate figure-derived values; attributing the gap to ESIA's filtering is the authors' mechanism interpretation.

## Limitations

Evaluation is numerical, with no RIS prototype, over-the-air test, or UAV flight experiment. The main setup uses one BS, two users, one eavesdropper, fixed UAV altitude, constant user speed and heading, and scenario-specific channel and energy parameters. Eavesdropper location uncertainty is represented indirectly through imperfect CSI rather than an explicit location-uncertainty set.

The shaped SSR-minus-penalties reward is not algebraically equivalent to SEE, making the learned policy sensitive to penalty design. The convergence argument supports a stable local minimum, while stronger "global equilibrium" language appears only in the interpretation of simulation curves. Remaining challenges named by the paper include real-time channel estimation, precise RIS control under hardware limits, UAV energy efficiency, and lightweight scalable learning; it proposes quantum-inspired experience replay as future work.

## Relation to the corpus

This source extends [[physical-layer-security]] and [[secrecy-energy-efficiency]] to joint aerial-RIS beamforming and trajectory control under CSI, phase, and positioning errors. [[li-2026-aerial-ris-trajectory-phase]] also couples aerial-RIS phases and UAV motion but emphasizes attitude/tilt and sum rate. [[li-2026-secrecy-ee-uav-ris-iov]] studies secrecy energy efficiency in a distinct untrusted-relay IoV setting, while [[zhang-2024-gdmtd3-aerial-secure-cb]] provides an adjacent TD3-family design for aerial secure beamforming and trajectory control. The two-agent method inherits its actor-critic basis from [[fujimoto-2018-td3-actor-critic]].

## Raw artifacts

- Parse: `raw/sources/Reinforcement_Learning_With_Conformal_Symplectic_Optimization_for_Aerial_RIS-Aided_Secure_Communication/Reinforcement_Learning_With_Conformal_Symplectic_Optimization_for_Aerial_RIS-Aided_Secure_Communication.md`
- Origin PDF: `raw/sources/Reinforcement_Learning_With_Conformal_Symplectic_Optimization_for_Aerial_RIS-Aided_Secure_Communication/Reinforcement_Learning_With_Conformal_Symplectic_Optimization_for_Aerial_RIS-Aided_Secure_Communication.pdf`
- Figures: `raw/sources/Reinforcement_Learning_With_Conformal_Symplectic_Optimization_for_Aerial_RIS-Aided_Secure_Communication/images/`
