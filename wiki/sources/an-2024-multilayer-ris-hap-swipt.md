---
type: source
title: "Exploiting Multi-Layer Refracting RIS-Assisted Receiver for HAP-SWIPT Networks"
authors: ["Kang An", "Yifu Sun", "Zhi Lin", "Yonggang Zhu", "Wanli Ni", "Naofal Al-Dhahir", "Kai-Kit Wong", "Dusit Niyato"]
year: 2024
url: "https://doi.org/10.1109/TWC.2024.3394214"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, high-altitude-platform-station, simultaneous-wireless-information-and-power-transfer, intelligent-reflecting-surface, robust-offloading, csi-estimation-error, majorization-minimization]
related:
  - "[[high-altitude-platform-station]]"
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[rf-energy-harvesting]]"
  - "[[csi-estimation-error]]"
  - "[[robust-offloading]]"
  - "[[majorization-minimization]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
  - "[[sun-2024-active-passive-ris-receiver]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
  - "[[kai-kit-wong]]"
  - "[[naofal-al-dhahir]]"
created: 2026-06-02
updated: 2026-07-16
---

# Exploiting Multi-Layer Refracting RIS-Assisted Receiver for HAP-SWIPT Networks

## Citation

An, K., Sun, Y., Lin, Z., Zhu, Y., Ni, W., Al-Dhahir, N., Wong, K.-K., & Niyato, D. (2024). *Exploiting Multi-Layer Refracting RIS-Assisted Receiver for HAP-SWIPT Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3394214. (Manuscript received 24 October 2023; revised 4 March 2024; accepted 22 April 2024; date of publication 3 May 2024; date of current version 11 October 2024 → year 2024. An earlier version appeared at IEEE GLOBECOM 2023, Kuala Lumpur.)

## TL;DR

A new receiver architecture — a **multi-layer refracting RIS-assisted receiver** — to enable **SWIPT** (simultaneous wireless information and power transfer) in **high-altitude-platform (HAP)** networks, where extreme long-distance links cause severe large-scale fading and energy scarcity. The multi-layer refracting RIS at the receiver concurrently delivers information and energy while exploiting the RIS's degrees of freedom and avoiding both the "double-fading" penalty of RIS-reflectors and the dynamic-noise penalty of single-layer active RIS. The paper formulates a **worst-case sum-rate maximization** under **imperfect (angular) CSI**, information-rate requirements, and an energy-harvesting constraint, then solves it with a **scalable, toolbox-free robust optimization** framework yielding **semi-closed-form** solutions: CSI discretization + a **LogSumExp-dual** scheme for the HAP transmit precoder + a **modified cyclic coordinate descent (M-CCD)** for the block-wise RIS coefficients + closed-form power-splitting ratios and receive decoder.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A quasi-stationary HAP communicates with $K$ battery-powered mobile terminals through a receiver-side multi-layer refracting RIS with $A$ layers and coefficient matrices $\Xi_{ka}$. Each terminal uses power splitting for simultaneous information decoding and energy harvesting, and the HAP transmit precoders face angular CSI uncertainty $\Delta$.

**Problem & objective**: The robust problem $\max_{\mathbf w_k,\boldsymbol\Xi_{ka},\mathbf v_k,\gamma_k}\min_{\Delta}\sum_{k=1}^{K}R_{\mathrm{ID},k}$ maximizes worst-case sum achievable rate while satisfying information-rate, harvested-power, transmit-power, and unit-modulus requirements.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| HAP transmit precoder | $\mathbf w_k$ | continuous complex vector | Precoder for terminal $k$ |
| Power-splitting ratio | $\gamma_k$ | continuous, $0\le\gamma_k\le1$ | Fraction used for information decoding versus harvesting |
| RIS coefficient matrix | $\boldsymbol\Xi_{ka}$ | complex unit-modulus diagonal matrix | Layer-$a$ refracting coefficients for terminal $k$ |
| Receive decoder | $\mathbf v_k$ | continuous complex vector, $\lVert\mathbf v_k\rVert=1$ | Digital decoder at terminal $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Worst-case information rate meets QoS: $\min_{\Delta}R_{\mathrm{ID},k}\ge\Gamma_k,\ \forall k$ |
| C2 | Worst-case harvested power is sufficient: $\min_{\Delta}\zeta_{\mathrm{EH},k}\ge\varsigma_{\max},\ \forall k$ |
| C3 | HAP transmit power is bounded: $\sum_{k=1}^{K}\lVert\mathbf w_k\rVert^2\le P_{\max}$ |
| C4 | RIS units are passive unit modulus: $\lvert[\boldsymbol\Xi_{ka}]_{n,n}\rvert=1,\ \forall k,a,n$ |
| C5 | Decoder normalization holds: $\lVert\mathbf v_k\rVert=1,\ \forall k$ |

**Algorithm**: Discretize the angular CSI uncertainty, use the LogSumExp inequality and dual variables with multi-dimensional bisection for the HAP precoders, update each RIS block by M-CCD with Dinkelbach and bisection parameters, obtain closed-form power-splitting ratios and decoders, and repeat the four block updates until the outer stopping criterion is met.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

An et al. [x] studied a receiver-side multi-layer refracting RIS architecture for SWIPT over long-distance HAP links. They formulated a worst-case sum-rate maximization over HAP precoders, power-splitting ratios, RIS coefficient matrices, and receive decoders under imperfect angular CSI, per-user rate and harvested-power requirements, transmit power, unit-modulus, and decoder-normalization constraints. Their robust solver discretizes CSI, applies a LogSumExp-dual precoder update, uses M-CCD for block-wise RIS coefficients, and obtains closed-form power-splitting ratios and decoders. Simulations reported convergence within about 15 iterations and higher sum rates than single-layer passive or active RIS and digital-receiver baselines, with the gap increasing as per-layer RIS units grow.

## Problem framing

HAPs (aerial base stations at 20–50 km) give wide coverage and low latency for remote areas, but their battery-powered ground devices are hard to recharge, so SWIPT is attractive — except energy-transfer efficiency collapses over the long HAP link's large-scale fading. Large arrays could compensate but are too costly/bulky at both ends. **RIS** can manipulate the channel cheaply, yet existing RIS roles do not fit HAP-SWIPT: RIS-**reflectors** suffer a severe **double-fading** effect over the dozens-of-km link; **active** RIS would need impractical power to overcome the large-scale fading; and prior **multi-layer RIS** work targeted the **transmitter** side, requiring multi-user beamforming coordination at the RIS. A new **receiver-side** RIS architecture is needed, plus a **scalable** solver, since conventional toolbox-based convex relaxations scale poorly with constraints/antennas and are hard to run on the energy-constrained HAP's limited (e.g., FPGA) hardware.

## System model

- **Architecture.** A multi-layer refracting RIS placed at the **receiver** of a HAP-SWIPT link, refracting (penetrating) signal across layers to amplify the desired signal **without** introducing the dynamic noise of active RIS. The HAP uses a transmit precoder; the receiver uses **power splitting (PS)** to divide the received signal into an information stream (decoding) and an energy stream (harvesting).
- **Uncertainty.** Imperfect **angular** CSI, handled in the **worst case** via a CSI-uncertainty bound $\Delta=\theta_U-\theta_L$.
- **Objective.** Maximize the **worst-case sum achievable rate** by jointly designing the transmit precoder, the PS ratios, the multi-layer refracting RIS coefficient matrices, and the receive digital decoder, subject to per-user rate requirements and a **non-linear energy-harvesting** constraint. The authors note this is harder than prior single-layer RIS-SWIPT power-minimization or linear-EH sum-rate problems.

## Method

- **Robust reformulation.** A **discretization** method converts the imperfect angular CSI into a robust (worst-case) form.
- **LogSumExp-dual (precoder).** The **LogSumExp** inequality smooths the non-smooth objective and EH constraints; dual variables fold the EH constraints into the objective as a Rayleigh-quotient subproblem, and a multi-dimensional **bisection** search over the duals yields a semi-closed-form precoder — framed as a more general / efficient generalized power iteration (GPI).
- **M-CCD (RIS coefficients).** Lagrange + Dinkelbach parameters cast the RIS subproblem in quadratic form; a **modified cyclic coordinate descent** updates KKT-optimal closed-form solutions block-wise **without** majorization (contrasted against MM + gradient projection), trading off SWIPT performance and complexity.
- **Closed forms** for the PS ratios and the receive decoder. Convergence/optimality of the LogSumExp-dual and M-CCD steps are proven (Propositions 2–3); overall optimality, convergence, and complexity are analyzed (Algorithm I).

## Key findings

- The proposed framework **converges rapidly** (all algorithms within ~15 iterations per the parse) and achieves **superior sum rate with lower complexity** than state-of-the-art RIS schemes (e.g., SCA-MM, ZF-MCCD baselines); the performance gap **grows** as the per-layer RIS-unit count $N_E$ increases, reflecting the architecture's potential-gain scaling $\propto (\prod_a \hat\rho N_{E,a})^2$.
- The **multi-layer** RIS-receiver outperforms passive/active single-layer RIS-receivers and digital receivers: single-layer **active** RIS only beats single-layer passive when total units stay below a threshold (the parse cites $N_{Tot}<468$) because of its added dynamic noise, whereas the multi-layer architecture amplifies the desired signal **without** that dynamic-noise penalty.
- RIS makes HAP-SWIPT practical where digital receivers cannot: a digital receiver fails to realize SWIPT for small $N_E$ (parse: $<6\times6$), and deploying $>36$ digital antennas at the device is impractical, while RIS facilitates large arrays. Specific numbers are figure-derived; treat exact values as indicative.

## Limitations / future work

A physical-layer SWIPT design (not an MEC offloading scheme); evaluated by numerical simulation with a worst-case angular-CSI model and a non-linear EH model. The HAP channel parameters reuse a referenced model. Explicit future-work targets are `not in parse`.

## Relation to the corpus

A **HAP / RIS / SWIPT physical-layer** anchor (not an MEC offloading paper) that complements the energy track's RF-harvesting HAP work [[hsu-2025-drl-hues-hap-noma]] from the link-design side, and shares the worst-case-CSI **RIS-receiver** lineage and several authors with [[sun-2024-active-passive-ris-receiver]] and [[sun-2024-mfris-semantic-antijamming]]. Its robust-optimization machinery (worst-case CSI, M-CCD, Dinkelbach) connects to [[robust-offloading]], [[majorization-minimization]], and [[fractional-programming-dinkelbach]]. It introduces the corpus's [[simultaneous-wireless-information-and-power-transfer]] concept and grounds [[high-altitude-platform-station]] from the SWIPT angle.

## Raw artifacts

- `raw/sources/Exploiting_Multi-Layer_Refracting_RIS-Assisted_Receiver_for_HAP-SWIPT_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
