---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# UAV-Enabled Secure ISAC Against Dual Eavesdropping Threats: Joint Beamforming and Trajectory Design

## Citation

Yao, J., Yang, Z., Yang, Z., Xu, J., & Quek, T. Q. S. (2025). *UAV-Enabled Secure ISAC Against Dual Eavesdropping Threats: Joint Beamforming and Trajectory Design*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2025.3588758.

## TL;DR

A letter on **secure UAV-enabled ISAC**: a UAV serves as an aerial base station communicating with a user and sensing a ground target, while a **dual-functional eavesdropper** tries to intercept both the communication and the sensing signals. The authors maximize the average achievable secrecy rate by jointly designing the UAV trajectory and the transmit information + sensing beamforming, subject to sensing-performance, sensing-security, UAV-power, and flight constraints. The non-convex problem is solved by **alternating optimization (AO) + SCA + SDR**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-wing UAV with a vertical $M$-element ULA flies at constant altitude over a legitimate communication user, a sensing target, and a dual-functional eavesdropper. The UAV sends an information beam and a sensing waveform that also acts as artificial noise during $N$ flight slots.

**Problem & objective**: Problem (P1) maximizes the average achievable secrecy rate, $\max_{\{\mathbf b[n],\mathbf A_s[n],\boldsymbol\rho[n]\}}\frac{1}{N}\sum_{n=1}^{N}R_s[n]$, through joint information beamforming, sensing covariance, and trajectory design.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Information beamformer | $\mathbf b[n]$ | complex continuous | Beam for the legitimate communication signal |
| Sensing covariance | $\mathbf A_s[n]$ | Hermitian PSD | Covariance of the sensing and artificial-noise waveform |
| UAV horizontal position | $\boldsymbol\rho[n]$ | continuous, 2-D trajectory | UAV location in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 13a | UAV starts at $\boldsymbol\rho_I$ and ends at $\boldsymbol\rho_F$ |
| 13b | Slot displacement satisfies $\|\boldsymbol\rho[n+1]-\boldsymbol\rho[n]\|\le V_{\max}$ |
| 13c | Target beampattern gain satisfies $\zeta_t[n]\ge\Gamma_t d_t^2(\boldsymbol\rho[n])$ |
| 13d | Eavesdropper sensing gain satisfies $\zeta_e[n]\le\Gamma_e d_e^2(\boldsymbol\rho[n])$ |
| 13e | Information and sensing power satisfy $\|\mathbf b[n]\|^2+\operatorname{tr}(\mathbf A_s[n])\le P_{\max}$ |

**Algorithm**: Alternating optimization separates beamforming from trajectory updates. With the trajectory fixed, SDR lifts the information beam and SCA convexifies the secrecy-rate objective; with the beams fixed, trust-region SCA updates the UAV trajectory, and the two blocks repeat until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yao et al. [x] studied a UAV-enabled secure ISAC link in which one aerial base station serves a user, senses a target, and faces an eavesdropper that intercepts both functions. They maximized average secrecy rate over the information beam, sensing covariance, and UAV trajectory while enforcing target illumination, sensing-security, transmit-power, and flight constraints. Their alternating solver applies semidefinite relaxation and successive convex approximation to the beamforming block and trust-region successive convex approximation to the trajectory block. Numerical results show that joint trajectory and beamforming design achieves higher secrecy rates than straight-flight or MRT-based alternatives. The reported beampatterns keep the legitimate user and target in high-gain regions while placing the eavesdropper in a low-gain region, illustrating the communication-versus-sensing security tradeoff.

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
