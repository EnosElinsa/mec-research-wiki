---
type: source
modeling_card: required
title: "Intelligent Reflecting Surface Enhanced Wireless Network via Joint Active and Passive Beamforming"
authors: ["Qingqing Wu", "Rui Zhang"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2936025"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, irs, beamforming, passive-beamforming, sinr, power-minimization, foundational-irs]
related:
  - "[[active-ris]]"
  - "[[qingqing-wu]]"
  - "[[an-2024-multilayer-ris-hap-swipt]]"
  - "[[chu-2024-secure-ris-isac]]"
  - "[[zhu-2024-crb-active-ris-isac]]"
  - "[[ahmed-2026-noma-irs-vehicular]]"
  - "[[fixed-point-irs-passive-beamforming]]"
created: 2026-06-04
updated: 2026-07-16
---

# Intelligent Reflecting Surface Enhanced Wireless Network via Joint Active and Passive Beamforming

## Citation

Wu, Q., & Zhang, R. (2019). *Intelligent Reflecting Surface Enhanced Wireless Network via Joint Active and Passive Beamforming*. **IEEE Transactions on Wireless Communications**, 18(11). DOI: 10.1109/TWC.2019.2936025. (Received 15 May 2019; accepted 12 August 2019; published 23 August 2019; current version 11 November 2019.)

## TL;DR

Foundational IRS paper. Studies an IRS-aided single-cell system (multi-antenna AP + multiple single-antenna users + one IRS). Formulates new **transmit-power minimization** problems solved by jointly optimizing the AP's **active transmit beamforming** and the IRS's **passive reflect beamforming** (phase shifts), subject to per-user SINR constraints. Simulations show that IRS-aided MIMO can match the rate performance of a massive MIMO system with significantly fewer active antennas/RF chains. Provides asymptotic analysis (infinitely large IRS) and deployment insights.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna access point serves multiple single-antenna users through both a direct path and an IRS-reflected path, with active AP beamforming coupled to passive unit-modulus phase shifts.

**Problem & objective**: The joint design minimizes AP transmit power, $\min_{\mathbf W,\boldsymbol\theta}\sum_k\lVert\mathbf w_k\rVert^2$, while meeting each user's SINR target.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AP beamformers | $\mathbf W=\{\mathbf w_k\}$ | complex vectors | Active transmit beams for users |
| IRS phases | $\boldsymbol\theta$ | continuous, $0\leq\theta_n\leq2\pi$ | Passive reflection phase shifts |
| IRS coefficients | $\boldsymbol\Theta$ | unit-modulus diagonal matrix | Reflect beamforming configuration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user meets its SINR target: $\mathrm{SINR}_k\geq\gamma_k$. |
| C2 | IRS phases are bounded: $0\leq\theta_n\leq2\pi$. |
| C3 | IRS coefficients have unit modulus. |
| C4 | Beamforming and phase variables remain coupled through the direct and reflected channels. |

**Algorithm**: Use SDR for phase optimization and SOCP for fixed-phase AP beamforming, or alternate AP beamforming and IRS phase updates in closed form until transmit power converges; apply Gaussian randomization when SDR is not rank one.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu and Zhang [x] establish the joint active and passive beamforming formulation for an IRS-aided multiuser cell. The design minimizes AP transmit power with coupled AP beamformers and unit-modulus IRS phases under per-user SINR targets. Semidefinite relaxation and second-order cone optimization provide a benchmark, while alternating updates offer a lower-complexity convergent method. The paper also derives the quadratic passive-array gain law and shows that IRS-assisted MIMO can match massive-MIMO rate performance with fewer active antennas.

## Problem framing

5G massive MIMO and mmWave approaches improve spectral efficiency but are costly in hardware (RF chains) and energy. IRS — a planar array of passive programmable phase shifters — can shape radio propagation without any transmit RF chains, at low cost and with negligible power consumption. The IRS creates an additional controllable signal path from AP to users, enabling **3D passive beamforming** that augments the AP's active beamforming. The joint active+passive design is the key optimization challenge; without it, the IRS passive gain is not fully exploited.

## System model

- **AP:** `M` active antennas. **IRS:** `N` passive reflecting elements, each with an adjustable phase shift (unit-modulus constraint). **K single-antenna users.**
- **Signal model:** users receive both the direct AP path and the AP→IRS→user reflected path; total received SINR is a function of both active beamforming vectors at the AP and the IRS phase-shift vector.
- **Optimization (P1):** minimize total AP transmit power subject to per-user SINR ≥ γ_k; variables: AP beamforming vectors + IRS phase shifts. Non-convex due to unit-modulus constraint and coupled variables.
- **Approach:** alternating optimization — for fixed IRS phases, AP beamforming is solved as second-order cone programming (SOCP); for fixed AP beamformers, IRS phases are solved via semidefinite relaxation (SDR).

## Key findings

- Simulation results report that joint active+passive beamforming with IRS achieves the **same rate performance as a massive MIMO system** (which has no IRS) while using significantly fewer active antennas and RF chains at the AP (parse Abstract, simulations).
- Asymptotic analysis: with `N` IRS elements, the passive array gain scales quadratically with `N`, meaning even a modest-size IRS can achieve large performance gains (parse Section IV).
- Useful deployment insights: IRS should be placed close to either the AP or the users (not midway) to maximize received power (parse simulation Section V).
- SDR is used as an approximate relaxation for IRS phase-shift optimization, with Gaussian randomization when the relaxed solution is not rank-one; the paper also gives lower-complexity alternating-optimization variants (parse Section III).

## Limitations / future work

Single IRS, single cell. Phase shifts assumed continuous [0,2π]; practical discrete phase-shift architectures not treated here. Perfect CSI assumed throughout.

## Relation to the corpus

Qingqing Wu ([[qingqing-wu]]) is the first author. This is the foundational IRS joint-beamforming paper that underpins the majority of IRS corpus entries — [[an-2024-multilayer-ris-hap-swipt]], [[chu-2024-secure-ris-isac]], [[zhu-2024-crb-active-ris-isac]], [[chhea-2025-irs-uav-swipt-drl]], [[wu-2025-gai-ris-resource-management]], and others all build on the system model and alternating-optimization approach established here. The active vs. passive beamforming comparison establishes [[active-ris]] as a concept in the corpus.

## Raw artifacts

- `raw/sources/Intelligent_Reflecting_Surface_Enhanced_Wireless_Network_via_Joint_Active_and_Passive_Beamforming/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
