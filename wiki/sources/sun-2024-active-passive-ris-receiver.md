---
type: source
modeling_card: required
title: "Active-Passive Cascaded RIS-Aided Receiver Design for Jamming Nulling and Signal Enhancing"
authors: ["Yifu Sun", "Yonggang Zhu", "Kang An", "Zhi Lin", "Cheng Li", "Derrick Wing Kwan Ng", "Jiangzhou Wang"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3325813"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, reconfigurable-intelligent-surface, anti-jamming, receiver-architecture, robust-beamforming, csi-uncertainty, physical-layer-security]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[active-ris]]"
  - "[[anti-jamming-mec]]"
  - "[[physical-layer-security]]"
  - "[[csi-estimation-error]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-05-31
updated: 2026-11-03
---

# Active-Passive Cascaded RIS-Aided Receiver Design for Jamming Nulling and Signal Enhancing

## Citation

Sun, Y., Zhu, Y., An, K., Lin, Z., Li, C., Ng, D. W. K., & Wang, J. (2024). *Active-Passive Cascaded RIS-Aided Receiver Design for Jamming Nulling and Signal Enhancing*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3325813.

## TL;DR

Proposes an **active-passive cascaded [[intelligent-reflecting-surface|RIS]]-aided receiver architecture** so that a large-scale antenna array can be deployed cheaply at the user side for anti-jamming communications. A passive RIS layer (N_P units) is cascaded with an [[active-ris|active RIS]] layer (N_A units), stacked in front of the receive antennas. Under imperfect (angular) jammer CSI, the paper formulates a **worst-case achievable-rate maximization** problem and solves the non-convex/NP-hard design with a low-complexity framework yielding semi-closed-form solutions. The authors state this is the first work to exploit an active-passive cascaded RIS at the user side for receiver design.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna base station transmits to a user whose receiver cascades a passive RIS layer, an active RIS layer and a small digital antenna array. $M$ jammers attack the link, their angular CSI is imperfect within the uncertainty set $\Delta_{\mathrm J}$, and the active layer amplifies signals but adds dynamic noise $\sigma_z^2$.

**Problem & objective**: Problem (6) maximizes the worst-case achievable rate $\max_{\mathbf w_{\mathrm B},\mathbf P,\boldsymbol\Xi,\mathbf v_{\mathrm U}}\min_{\Delta_{\mathrm J}}R_{\mathrm U}(\mathbf w_{\mathrm B},\mathbf P,\boldsymbol\Xi,\mathbf v_{\mathrm U})$.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| BS precoder | $\mathbf w_{\mathrm B}$ | complex vector, cluster-power bounded | Downlink transmit beamformer |
| Passive RIS coefficients | $\mathbf P$ | diagonal, unit modulus | Phase-only coefficients of the passive layer |
| Active RIS coefficients | $\boldsymbol\Xi$ | diagonal, amplitude $\le\alpha_{n_1,\max}$ | Amplitudes and phases of the active layer |
| Rx digital decoder | $\mathbf v_{\mathrm U}$ | complex vector | Receive combining at the user |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 (5) | Per-cluster BS power, $\mathbf w_{\mathrm B}^H\mathbf E_c\mathbf w_{\mathrm B}\le p_{\mathrm B,c}$ for $c=1,\dots,C$; $C=1$, $\mathbf E_c=\mathbf I$ gives the total power constraint |
| C2 | Worst-case active-RIS amplification power, $\max_{\Delta_{\mathrm J}}(\lVert\boldsymbol\Xi\tilde{\mathbf w}_{\mathrm B}\rVert^2+\sigma_z^2\lVert\boldsymbol\Xi\rVert_F^2)\le P_{\mathrm{R,max}}$ |
| C3 | Active amplification factor, $\lvert[\boldsymbol\Xi]_{n_1,n_1}\rvert\le\alpha_{n_1,\max}$ with $\alpha_{n_1,\max}>1$ |
| C4 | Passive unit modulus, $\lvert[\mathbf P]_{n_2,n_2}\rvert=1$ |
| Model rule | The rate is evaluated for the worst jammer angle error in $\Delta_{\mathrm J}$ |

**Algorithm**: A Pareto-dual scheme turns C1 into a tractable form through Lagrange duality and Pareto optimization and gives a semi-closed-form BS precoder. The passive coefficients come from a unified unit-modulus zero-forcing (UM-ZF) design that nulls jamming, with feasibility conditions on the number of passive units. The active coefficients come from alternating majorization-minimization (AMM) or conventional/modified cyclic coordinate descent (C/M-CCD), which handle the fractional objective created by the active-RIS noise.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied anti-jamming receiver design with a passive RIS cascaded with an active RIS at the user side. They formulated a worst-case achievable-rate maximization problem under imperfect angular jammer CSI, jointly designing the BS precoder, passive phases, active gains and phases, and receive combiner. Their low-complexity framework uses Lagrange duality and Pareto optimization for the BS precoder, unit-modulus zero-forcing for the passive layer, and AMM or C/M-CCD updates for the active layer, all in semi-closed form. The analysis derives receive-power and asymptotic-SINR scaling laws for the two-layer architecture. Numerical results report a higher achievable rate than fully digital, phase-array, and single-layer active RIS receivers, even with a 30 dBm amplification budget, at power consumption far below the digital and phase-array designs.

## Problem framing

Massive-MIMO anti-jamming works well but deploying hundreds of antennas at a user is impractical (hardware cost, power). A passive-RIS reflector suffers severe path loss; an active-RIS reflector amplifies the signal but injects dynamic noise and consumes large power at the user. The paper seeks a cost- and energy-efficient receiver that combines both, while remaining robust to **imperfect angular CSI** of the jammers ([[csi-estimation-error]]) and avoiding the high complexity and FPGA-unfriendliness of CVX/SDR-based robust solvers.

## System model

- **Actors.** A base station (transmit precoder, general power constraints), the user equipped with the cascaded RIS receiver, and M jammers (the simulations use M = 2) with imperfect angular CSI.
- **Architecture.** Passive RIS (N_P units, phase-only) cascaded with active RIS (N_A units, phase + amplitude) vertically stacked before the Rx antennas; a digital decoder follows.
- **Performance analysis.** Derives a power-scaling law: the proposed architecture's receive power and asymptotic SINR scale as N_A^2·N_P^2 and N_A·N_P respectively, versus (N_P + N_A)^2 and (N_P + N_A) for a single-layer active RIS — giving additional, separately-controllable degrees of freedom.

## Method

A low-complexity optimization framework that decomposes the joint design:

- **BS precoder.** Lagrange dual + Pareto optimization theory transform the general power constraints into a tractable form yielding an optimal semi-closed-form precoder.
- **Passive RIS coefficients.** A discretization method converts the jammers' imperfect CSI into a robust form; a new anti-jamming criterion yields two **jamming-nulling feasibility conditions** and a unified unit-modulus zero-forcing (UM-ZF) scheme with a semi-closed-form solution.
- **Active RIS coefficients.** Three efficient algorithms based on alternating majorization-minimization (AMM) and conventional/modified cyclic coordinate descent (C/M-CCD) trade complexity against performance; all are proven to converge to a limited KKT point.

## Key findings

- The cascaded architecture accurately nulls toward the jammers while aligning the mainlobe with the target even under angular uncertainty; received SINR at the BS direction is ~0 dB versus ~−10 dB for the single-layer and fully-digital architectures, while all architectures sit near −50 dB toward the jammer (verbatim from the simulation discussion).
- Power-scattering ratio (PSR): the proposed cascaded architecture concentrates power on the Rx antennas with a PSR of **32.8%**, which the paper reports as 2.78 times lower than the single-layer active RIS architecture's PSR of **75.9%** (verbatim).
- Numerical simulations show superior performance at lower complexity than the fully-digital receiver and the SDR method.

## Limitations / future work

Simulation-only; the parse does not enumerate explicit future work. *Not an MEC paper* — it is curated as a physical-layer **anti-jamming / RIS receiver** anchor. An earlier version appeared at IEEE ICC 2023 (Rome). DOI date of publication 25 Oct 2023 / date of current version 12 Jun 2024 → year 2024.

## Relation to the corpus

A physical-layer **anti-jamming + RIS** anchor that complements the MEC-side anti-jamming and RIS work. It shares the **worst-case / imperfect-CSI robust optimization** stance of [[sun-2024-mfris-semantic-antijamming]] (multi-functional RIS semantic anti-jamming) and the broader [[anti-jamming-mec]] thread, and adds a receiver-side architecture to the corpus's [[intelligent-reflecting-surface]] / [[active-ris]] coverage. Reinforces [[csi-estimation-error]], [[physical-layer-security]], and the [[alternating-optimization-sdr-sca]] solver family it explicitly contrasts against.

## Raw artifacts

- `raw/sources/Active-Passive_Cascaded_RIS-Aided_Receiver_Design_for_Jamming_Nulling_and_Signal_Enhancing/Active-Passive_Cascaded_RIS-Aided_Receiver_Design_for_Jamming_Nulling_and_Signal_Enhancing.md`
- Original PDF and extracted figures in the same folder.
