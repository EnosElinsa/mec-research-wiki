---
type: source
title: "Aerial ISAC: A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced Coverage and Security"
authors: ["Ahmed M. Benaya", "Mohamed S. Hassan", "Mahmoud H. Ismail", "Taha Landolsi"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2025.3551395"
venue: "IEEE Transactions on Green Communications and Networking"
modeling_card: required
tags: [source, isac, haps, full-duplex, physical-layer-security, aav-jammer, beamforming, mec, alternating-optimization]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[high-altitude-platform-station]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[wang-2025-lae-network-survey]]"
created: 2026-05-29
updated: 2026-07-16
---

# Aerial ISAC: A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced Coverage and Security

## Citation

Benaya, A. M., Hassan, M. S., Ismail, M. H., & Landolsi, T. (2025). *Aerial ISAC: A HAPS-Assisted Integrated Sensing, Communications and Computing Framework for Enhanced Coverage and Security*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2025.3551395.

## TL;DR

A **HAPS-mounted full-duplex ISAC base station** simultaneously serves K downlink UEs, senses L ground targets, offloads sensed data to a ground MEC server for processing, and enables a **friendly-jamming AAV (UAV)** to disrupt eavesdroppers identified through the radar process. The authors formulate joint optimization of (1) the BS transmit/receive beamforming, (2) the AAV trajectory, and (3) jamming power, to maximize the communication sum spectral efficiency under radar-rate, secrecy, offloading, and power constraints.

The problem is non-convex; solved by **alternating optimization (AO)** with **semi-definite relaxation (SDR)** + **successive convex approximation (SCA)**. The HAPS hosts the radio front-end; the heavy data processing of the sensed targets is offloaded to a ground MEC server — that's the "computing" part of the framework.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude HAPS carries a full-duplex $N_t$-antenna ISAC base station that serves $K$ single-antenna UEs, senses $L$ quasi-static targets with TDM-ISAC, and offloads part of the sensed workload to a ground MEC server. A single-antenna friendly-jamming AAV flies at fixed altitude $z_U$ over $N$ slots and degrades a sensed eavesdropper while the HAPS-to-ground links follow Rician fading and the AAV-to-ground links are line of sight.

**Problem & objective**: Problem (21) is a non-convex communication-centric program that maximizes average sum communication spectral efficiency, $\max_{\mathbf{W}[n],\mathbf{u}_l[n],\mathbf{Q}}\frac{1}{N}\sum_{n=1}^{N}\sum_{k=1}^{K}R_k[n]$, over transmit beamforming, radar receive beamforming, and the AAV trajectory.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Composite transmit beamforming | $\mathbf{W}[n]$ | Complex matrix | Communication, radar, and offloading beamforming vectors in slot $n$ |
| Radar receive beamforming | $\mathbf{u}_l[n]$ | Complex vector, $\lVert\mathbf{u}_l[n]\rVert^2\leq1$ | Receive beamformer for target $l$ |
| AAV trajectory | $\mathbf{Q}=\{\mathbf{q}[1],\ldots,\mathbf{q}[N]\}$ | Continuous 2D coordinates at fixed $z_U$ | Friendly-jammer horizontal path over the mission |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 21b-21c | ISAC-BS power and receive-vector norm, $P_t[n]\leq p_{\max}$ and $\lVert\mathbf{u}_l[n]\rVert^2\leq1$ |
| 21d-21e | AAV kinematics and endpoints, $\lVert\mathbf{q}[n+1]-\mathbf{q}[n]\rVert^2\leq(\tau v^{\max})^2$, $\mathbf{q}[1]=\mathbf{q}^0$, and $\mathbf{q}[N]=\mathbf{q}^F$ |
| 21f | Eavesdropper security, $\max_{k\in\mathcal{K}}\Gamma_{\mathrm{eve},k}[n]\leq\Gamma_{\min}$ |
| 21g | Per-target radar information rate, $\log_2(1+\Gamma_l[n])\geq R_{\mathrm{req}}$ |
| 21h-21i | Offloading and execution, $R_{\mathrm{off}}[n]\leq R_{\mathrm{rad}}[n]$ and $\xi_{\mathrm{tot}}[n]\leq\xi_{\max}$ |

**Algorithm**: Alternating optimization first solves an SDR/SCA radar receive-beamforming subproblem and recovers $\mathbf{u}_l[n]$ by eigenvalue decomposition, then solves an SCA transmit-beamforming subproblem, and finally solves an SCA AAV-trajectory subproblem. The three blocks are updated with CVX until the objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Benaya et al. [x] studied a non-terrestrial ISAC architecture in which a HAPS-mounted full-duplex base station serves communication users, senses ground targets, and offloads sensed workloads to a ground MEC server. A friendly-jamming AAV follows a controlled trajectory to reduce the decoding SINR of a sensed eavesdropper. They formulated a non-convex program that maximizes average sum communication spectral efficiency by jointly selecting composite transmit beamforming, radar receive beamforming, and the AAV trajectory under transmit-power, radar-rate, security, trajectory, offloading-rate, and workload-latency constraints. Their alternating-optimization algorithm applies semidefinite relaxation and successive convex approximation to the receive-beamforming, transmit-beamforming, and trajectory blocks. Simulations reported about 47% higher communication spectral efficiency for the optimized trajectory than for the initial trajectory at 44 dBm transmit power, and about 20% higher radar estimation information rate than the Rayleigh-quotient receive-beamforming approach at the same power.

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
