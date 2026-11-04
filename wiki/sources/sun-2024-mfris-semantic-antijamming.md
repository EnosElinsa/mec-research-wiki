---
type: source
modeling_card: required
title: "Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks"
authors: ["Yifu Sun", "Zhi Lin", "Kang An", "Dong Li", "Cheng Li", "Yonggang Zhu", "Derrick Wing Kwan Ng", "Naofal Al-Dhahir", "Jiangzhou Wang"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3459028"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, anti-jamming-mec, intelligent-reflecting-surface, semantic-communication, air-ground-integrated-network, robust-optimization, monotonic-optimization, physical-layer-security]
related:
  - "[[anti-jamming-mec]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[multi-functional-ris]]"
  - "[[semantic-communication]]"
  - "[[air-ground-integrated-network]]"
  - "[[monotonic-optimization]]"
  - "[[csi-estimation-error]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[naofal-al-dhahir]]"
created: 2026-05-31
updated: 2026-11-03
---

# Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks

## Citation

Sun, Y., Lin, Z., An, K., Li, D., Li, C., Zhu, Y., Ng, D. W. K., Al-Dhahir, N., & Wang, J. (2024). *Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3459028. (Received 15 February 2024; date of publication 12 September 2024; date of current version 22 November 2024, so the wiki year is 2024. An earlier version was presented in part at WCSP, Hefei, China, 2024.)

## TL;DR

A framework of **multi-functional reconfigurable intelligent surface (MF-RIS)**-aided **semantic anti-jamming** communication and computing for an MEC-assisted **integrated aerial-ground network (MEC-IAGN)**. A semantic transceiver provides robustness + data compression, and the MF-RIS customizes the full-space environment via **signal reflection, refraction, amplification, and energy harvesting** (overcoming the half-space coverage, multiplicative fading, and battery reliance of conventional RIS). The paper maximizes a **semantic computation rate** under jamming attacks and **imperfect jammer CSI**, subject to an energy-partition (offloading) constraint, semantic-similarity requirement, semantic-rate target, and MF-RIS self-sustainability. Imperfect CSI is converted to a **worst-case** form via discretization; the problem is solved by a fast-converging **monotonic optimization + decoupling second-order cone programming (MO-DSOCP)** algorithm (global optimum), plus a low-complexity suboptimal **generalized power iteration (GPI)** scheme.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An aerial platform (AP) computes part of its task onboard and offloads the rest to $K$ ground base stations (GBSs) by semantic communication. A multi-functional RIS (MF-RIS) splits space into reflected and refracted halves, amplifies signals, and harvests energy for self-sustainability. $R$ single-antenna jammers attack the GBSs, and their CSI is imperfect within an uncertainty set $\Delta$.

**Problem & objective**: Problem (13) maximizes the worst-case total semantic computation rate $\max\min_{\Delta}\bar S(\gamma_k,\mathcal Y)$ over the receive decoders $\mathbf v_k$, transmit precoders $\mathbf w_k$, MF-RIS coefficient matrices $\boldsymbol\Phi_{\mathrm R},\boldsymbol\Phi_{\mathrm T}$, and energy partition $\mathcal Y$; $\bar S$ adds the offloaded semantic rate and the local computing rate.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Transmit precoders | $\mathbf w_k$ | complex vectors | AP beamformers for offloading to GBS $k$ |
| Receive decoders | $\mathbf v_k$ | unit-norm complex vectors | GBS combining vectors |
| MF-RIS coefficients | $\boldsymbol\Phi_{\mathrm R},\boldsymbol\Phi_{\mathrm T}$ | amplitudes $\alpha_{\iota,n}$, phases, mode $\varsigma_n\in\{0,1\}$ | Reflection/refraction with amplification; $\varsigma_n=1$ for reflect/refract mode, 0 for energy harvesting |
| Energy partition | $\mathcal Y$ | continuous, $[0,1]$ | Share $\mathcal YE_{\max}$ of AP energy used for offloading, the rest for local computing |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 | Worst-case semantic similarity, $\min_\Delta\xi(\gamma_k,\mathcal Y)\ge\xi_{\mathrm{th}}$ |
| C2 | Worst-case semantic computation rate, $\min_\Delta S_k(\gamma_k,\mathcal Y)\ge S_{\mathrm{th}}$ |
| C3 | Offloading power, $\sum_k\lVert\mathbf w_k\rVert^2\le\mathcal YE_{\max}/T$ |
| C4, C5 | $\lVert\mathbf v_k\rVert^2=1$; binary mode $\varsigma_n\in\{0,1\}$ |
| C6, C7 | $\alpha_{\mathrm R,n},\alpha_{\mathrm T,n}\in[0,\alpha_{\max}]$ with $\alpha_{\mathrm R,n}+\alpha_{\mathrm T,n}\le\alpha_{\max}$; element modulus $\lvert[\boldsymbol\Phi_{\iota(k)}]_{n,n}\rvert=\varsigma_n\sqrt{\alpha_{\iota(k),n}}$ |
| C8, C9 | $\mathcal Y\in[0,1]$; MF-RIS self-sustainability, $\min_\Delta P_{\mathrm H}\ge P_{\mathrm{Tot}}$ |

**Algorithm**: A discretization method turns the imperfect jammer CSI into a worst-case instance. The globally optimal MO-DSOCP algorithm applies monotonic optimization with box reduction over the semantic-rate region and checks feasibility with decoupling second-order cone programming. A lower-complexity alternative designs the precoder by generalized power iteration (GPI) and the remaining variables by heuristics.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied semantic anti-jamming communication and computing with a multi-functional RIS in an integrated aerial-ground network. They formulated a robust semantic computation-rate maximization problem with reflection, refraction, amplification, energy harvesting, semantic similarity, and offloading variables under imperfect jammer CSI. A worst-case discretization converts the CSI uncertainty into a deterministic instance. The globally optimal solution uses monotonic optimization with decoupling second-order cone programming and sequential partitioning, while generalized power iteration provides a lower-complexity alternative. Simulations show MF-RIS above passive STAR-RIS, no RIS, and bit-level MEC with MF-RIS, but below an active STAR-RIS with ideal power supply; MO-DSOCP also beat the BRB-SCA and PA-DSOCP monotonic-optimization baselines.

## Problem framing

MEC-IAGN for 6G faces three bottlenecks: computation-intensive tasks, an uncontrollable propagation environment, and malicious **jamming** attacks. Conventional remedies (heterogeneous APs, massive antennas, wider/higher-frequency bands) carry prohibitive cost and extra bandwidth/energy. The paper argues prior semantic-MEC work is limited to single-antenna scenarios and prior RIS-MEC work uses bit-level (non-semantic) transmission, motivating the **first** MF-RIS-aided *semantic* MEC-IAGN under jamming.

## System model

- **Architecture.** Integrated aerial-ground network with a semantic transceiver and an MF-RIS supporting reflection/refraction/amplification/energy-harvesting; computation offloading governed by an **energy-partition parameter**.
- **Adversary.** Malicious jammer with **imperfect CSI**, handled via worst-case robust optimization.
- **Objective.** Maximize semantic computation rate (local + offloaded) subject to: semantic-similarity requirement, semantic-rate target, MF-RIS self-sustainability, and the energy-partition constraint.
- **Structure.** Quasi-convex objective with **MINLP** constraints over tightly-coupled variables.

## Method

- **Worst-case transformation.** A discretization method converts imperfect jammer CSI into a worst-case instance.
- **MO-DSOCP (optimal).** A fast-converging **monotonic optimization** algorithm combined with decoupling second-order cone programming, using a sequential partitioning scheme to obtain a globally optimal solution with fewer feasibility evaluations.
- **GPI (suboptimal, low complexity).** A generalized power iteration derives a semi-closed-form transmit precoder, with heuristic design of the remaining variables, trading a little performance for much lower complexity.

## Key findings

- Numerical simulations show the proposed MF-RIS-aided semantic framework and algorithms are superior to various benchmarks (stated qualitatively in the parse; specific magnitudes are in the figures and not asserted here as exact).

## Limitations / future work

No explicit quantitative future-work targets are grounded in the captured parse: `not in parse`.

## Relation to the corpus

A **security + RIS + semantic** entry that bridges several corpus threads. It extends the [[anti-jamming-mec]] theme beyond the DRL-based [[shao-2024-drl-antijamming-mec]] with a **robust-optimization** (worst-case CSI) treatment, connecting to [[csi-estimation-error]] and [[jia-2025-dro-uav-hap-mec]] (uncertain-CSI robustness). It grounds new [[multi-functional-ris]] and [[semantic-communication]] concept pages and the [[monotonic-optimization]] technique, while reinforcing [[intelligent-reflecting-surface]] and [[air-ground-integrated-network]]. Its convex-pipeline flavor (SOCP, semi-closed-form precoder) parallels the corpus's AO+SDR+SCA secure-beamforming sources.

## Raw artifacts

- `raw/sources/Multi-Functional_RIS-Assisted_Semantic_Anti-Jamming_Communication_and_Computing_in_Integrated_Aerial-Ground_Networks/Multi-Functional_RIS-Assisted_Semantic_Anti-Jamming_Communication_and_Computing_in_Integrated_Aerial-Ground_Networks.md`
- Original PDF (`0a6fff1e-ad88-455d-b6a7-6b9286e0d7f9_origin.pdf`) and extracted figures (`images/`) in the same folder.
