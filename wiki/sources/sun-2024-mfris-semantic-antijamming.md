---
type: source
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
updated: 2026-07-13
---

# Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks

## Citation

Sun, Y., Lin, Z., An, K., Li, D., Li, C., Zhu, Y., Ng, D. W. K., Al-Dhahir, N., & Wang, J. (2024). *Multi-Functional RIS-Assisted Semantic Anti-Jamming Communication and Computing in Integrated Aerial-Ground Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3459028. (Received 15 February 2024; date of publication 12 September 2024; date of current version 22 November 2024, so the wiki year is 2024. An earlier version was presented in part at WCSP, Hefei, China, 2024.)

## TL;DR

A framework of **multi-functional reconfigurable intelligent surface (MF-RIS)**-aided **semantic anti-jamming** communication and computing for an MEC-assisted **integrated aerial-ground network (MEC-IAGN)**. A semantic transceiver provides robustness + data compression, and the MF-RIS customizes the full-space environment via **signal reflection, refraction, amplification, and energy harvesting** (overcoming the half-space coverage, multiplicative fading, and battery reliance of conventional RIS). The paper maximizes a **semantic computation rate** under jamming attacks and **imperfect jammer CSI**, subject to an energy-partition (offloading) constraint, semantic-similarity requirement, semantic-rate target, and MF-RIS self-sustainability. Imperfect CSI is converted to a **worst-case** form via discretization; the problem is solved by a fast-converging **monotonic optimization + decoupling second-order cone programming (MO-DSOCP)** algorithm (global optimum), plus a low-complexity suboptimal **generalized power iteration (GPI)** scheme.

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

- `raw/sources/Multi-Functional_RIS-Assisted_Semantic_Anti-Jamming_Communication_and_Computing_in_Integrated_Aerial-Ground_Networks/full.md`
- Original PDF (`0a6fff1e-ad88-455d-b6a7-6b9286e0d7f9_origin.pdf`) and extracted figures (`images/`) in the same folder.
