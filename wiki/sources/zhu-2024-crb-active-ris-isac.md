---
type: source
title: "Cramér-Rao Bound Optimization for Active RIS-Empowered ISAC Systems"
authors: ["Qi Zhu", "Ming Li", "Rang Liu", "Qian Liu"]
year: 2024
url: "https://doi.org/10.1109/TWC.2024.3384501"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, active-ris, cramer-rao-bound, beamforming, alternating-optimization-sdr-sca, majorization-minimization, doa-estimation]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[active-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[cramer-rao-bound]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[majorization-minimization]]"
  - "[[collaborative-beamforming]]"
  - "[[chu-2024-secure-ris-isac]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[zhu-2024-sensing-comm-doppler-uav-swarm]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[benaya-2025-aerial-isac-haps]]"
created: 2026-06-02
updated: 2026-06-02
---

# Cramér-Rao Bound Optimization for Active RIS-Empowered ISAC Systems

## Citation

Zhu, Q., Li, M., Liu, R., & Liu, Q. (2024). *Cramér-Rao Bound Optimization for Active RIS-Empowered ISAC Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3384501. (Manuscript received 23 May 2023; revised 18 October 2023 and 8 February 2024; accepted 24 March 2024; date of publication 10 April 2024; date of current version 12 September 2024 → year 2024.)

## TL;DR

A **classical/convex** beamforming design for an **active-RIS-empowered ISAC** system in which a dual-functional base station (BS) communicates with multiple users while sensing a point target that is **blocked from the BS by an obstacle**. Because the ISAC receiver is low-sensitivity and the only path to the target is via the RIS, the echo is weak; an **active RIS** (which amplifies, unlike a passive RIS) is used to overcome the multiplicative-fading path-loss and improve both sensing and communication. The paper derives — for the first time, by its own statement — the **Cramér-Rao bound (CRB)** for target **direction-of-arrival (DoA)** estimation in this active-RIS ISAC setting, then jointly designs the BS transmit precoding and the active RIS reflection beamforming to **minimize that CRB** subject to per-user SINR requirements, BS and active-RIS power budgets, and the RIS amplitude constraint. The non-convex problem is solved with an algorithm combining **alternating optimization (AO)**, **semidefinite relaxation (SDR)**, and **majorization-minimization (MM)**. This is a **physical-layer ISAC** entry, not an MEC offloading paper.

## Problem framing

ISAC merges sensing and communication on a shared waveform/aperture to gain spectral and energy efficiency. A practical obstacle is that ISAC receivers are typically less sensitive than dedicated radar receivers (cost considerations), so a weak echo from an obstructed target yields poor parameter-estimation performance. RIS can build a virtual line-of-sight link around the blockage, but a **passive** RIS suffers the "multiplicative fading" effect (the reflected-link path-loss is the *product* of the two segment path-losses), so its gain is marginal unless the receiver is close to the RIS or the direct link is weak. **Active RIS** mitigates this by integrating reflection-type amplifiers, amplifying the reflected signal at the cost of more power/hardware. Prior active-RIS ISAC work focused on target *detection* (radar SNR); **parameter estimation** (CRB) for active-RIS ISAC was unexplored, which this paper targets.

## System model

- **Nodes.** A dual-functional BS with $N_\mathrm{t}=N_\mathrm{r}=N$ transmit/receive antennas, $K$ single-antenna communication users, and an $M$-element **active RIS**. The target sits in the BS's blind zone (direct BS-target link blocked), so the sensing signal reaches the target only via the RIS and returns along the same path.
- **Transmit signal.** A dual-functional waveform combining precoded communication symbols and radar signals, $\mathbf{x}[l]=\mathbf{W}_\mathrm{c}\mathbf{s}_\mathrm{c}[l]+\mathbf{W}_\mathrm{r}\mathbf{s}_\mathrm{r}[l]$.
- **Active RIS model.** Reflection coefficients $\phi_m=a_m e^{\jmath\varphi_m}$ with amplitude $a_m\in(0,a_\max]$, $a_\max\ge 1$ (amplification); additive noise is injected at the active RIS (AWGN $\mathbf{z}_0,\mathbf{z}_1$). Channels (BS-user, BS-RIS $\mathbf{G}$, RIS-user, RIS-target $\mathbf{h}_\mathrm{r,t}$) are assumed perfectly known.
- **Metrics.** Communication: per-user **SINR**. Sensing: **CRB** for the target DoA $\theta$, obtained as the relevant entry of the inverse **Fisher information matrix (FIM)** of the parameter vector $\boldsymbol{\xi}=[\theta,\Re\{\alpha\},\Im\{\alpha\}]^T$ ($\alpha$ = target RCS).
- **Problem.** Minimize the DoA-estimation CRB over the BS precoding $\mathbf{W}$ and active-RIS reflection vector $\boldsymbol{\phi}$, subject to each user's SINR $\ge\gamma_k$, BS power budget, active-RIS power budget (including the amplified-noise term), and the RIS amplitude constraint.

## Method

- **CRB derivation.** The FIM for $\boldsymbol{\xi}$ is derived from the vectorized echo model; the CRB matrix is the FIM inverse, with the noise covariance $\mathbf{R}_\mathrm{n}$ capturing the RIS-amplified noise. The work notes this active-RIS CRB differs substantially from the passive-RIS case.
- **AO + SDR + MM.** The joint non-convex design is split by **alternating optimization** into the precoding subproblem and the reflection subproblem. **Semidefinite relaxation** handles the precoding (lifting $\mathbf{W}$-related terms to PSD matrices), and **majorization-minimization** surrogates the intractable RIS-reflection objective into tractable per-iteration convex updates. (Scope note: this initial work optimizes CRB for **DoA** estimation only; RCS/range-estimation CRB is left to future work.)
- **Complexity.** The overall per-iteration complexity is analyzed (interior-point solver), dominated by the precoding step at roughly $\mathcal{O}(N^{6.5}K^{6.5}+M^{4.5}+NM^2+MN^2)$.

## Key findings

- **Active RIS provides over 30 dB CRB reduction** for single-target DoA estimation versus a passive-RIS-assisted ISAC system (abstract/intro/conclusion, parse) — a large sensing-accuracy gain.
- The active-RIS ISAC design performs **close to an active-RIS radar-only system**, i.e. supporting communication costs little sensing accuracy, while dramatically beating passive RIS (Figs. 6-7, figure-derived, indicative).
- A clear **communication-vs-sensing trade-off**: as the number of communication users $K$ grows, more resources go to meeting the users' SINR/QoS, so the DoA CRB increases (Fig. 8, figure-derived).
- Across transmit power sweeps the active scheme is consistently superior to passive, with the parse reporting up to **36 dB** CRB improvement at $a_\max=8,\,P_\mathrm{RIS}=10\,$dBm (Fig. 4 discussion, parse).

## Limitations / future work

The model is **simulation-based**, assumes **perfect CSI**, a **single point target**, and a **known target angle/range detection cell** (the DoA w.r.t. the RIS and the RIS-target LoS are treated as known for CRB computation). By the authors' explicit statement, only **DoA-estimation** CRB is optimized in this initial work; CRB for **RCS/range** estimation and the **multi-target** case (where deriving the multi-DoA CRB and the associated beamforming is substantially more complex) are deferred to future work.

## Relation to the corpus

A **physical-layer ISAC** entry that anchors the corpus's [[cramer-rao-bound]] sensing-accuracy thread on the active-RIS side. It complements the **secure** convex-ISAC designs [[chu-2024-secure-ris-isac]] (RIS-ISAC radar-SNR max via AO + SDR + fractional programming + [[majorization-minimization]]) and [[su-2024-sensing-aided-isac-pls]] (sensing-aided PLS minimizing eavesdropper-angle CRB), and the CRLB-minimizing UAV-swarm design [[zhu-2024-sensing-comm-doppler-uav-swarm]] — all sharing the CRB/CRLB-as-objective framing and the [[alternating-optimization-sdr-sca|AO + SDR + SCA]] convex scaffold. It is the **classical-optimization** counterpart to the learning-based [[zhang-2025-gan-td3-isac-active-ris]] (GAN-enhanced TD3 beamforming for *double*-active-RIS ISAC): both exploit [[active-ris]] amplification against blockage, but one solves via convex AO and the other via DRL. Its aerial sibling on the secure side is [[benaya-2025-aerial-isac-haps]].

## Raw artifacts

- `raw/sources/Cramr-Rao_Bound_Optimization_for_Active_RIS-Empowered_ISAC_Systems/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
