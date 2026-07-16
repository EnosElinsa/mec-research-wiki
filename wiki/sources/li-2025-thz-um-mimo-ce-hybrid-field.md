---
type: source
title: "Hybrid Near- and Far-Field THz UM-MIMO Channel Estimation: A Sparsifying Matrix Learning-Aided Bayesian Approach"
authors: ["Yuanjian Li", "A. S. Madhukumar"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3514141"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, thz, um-mimo, channel-estimation, compressed-sensing, bayesian-learning, dictionary-learning, near-field, 6g]
related:
  - "[[near-field-communications]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[cramer-rao-bound]]"
created: 2026-06-04
updated: 2026-07-16
modeling_card: not_applicable
---

# Hybrid Near- and Far-Field THz UM-MIMO Channel Estimation: A Sparsifying Matrix Learning-Aided Bayesian Approach

## Citation

Li, Y., & Madhukumar, A. S. (2025). *Hybrid Near- and Far-Field THz UM-MIMO Channel Estimation: A Sparsifying Matrix Learning-Aided Bayesian Approach*. **IEEE Transactions on Wireless Communications**, 24(3). DOI: 10.1109/TWC.2024.3514141. (Received 12 June 2024; accepted 3 December 2024; published 17 December 2024; current version 12 March 2025.)

## TL;DR

Addresses the channel estimation (CE) problem for THz ultra-massive MIMO (UM-MIMO) systems where **both near-field and far-field propagation paths coexist** — a scenario that makes existing compressed-sensing CE frameworks ineffective because angular- or polar-domain sparsifying dictionaries alone cannot capture the hybrid-field channel. Proposes a **dictionary learning (DL)-aided Bayesian CSCE** solution: a **batch-delayed online DL (BD-ODL)** algorithm learns an adaptive sparsifying matrix; a **Bayesian learning (BL)-enabled CSCE** framework exploits the resulting sparsity. Also derives the Bayesian Cramér-Rao bound (BCRB) as an MSE lower bound and performs complexity analysis. Achieves significant NMSE improvement over LS, MMSE, and CS baselines with rapid convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li and Madhukumar [x] developed a hybrid near-field and far-field THz UM-MIMO channel-estimation model with molecular absorption, reflection attenuation, and compressed pilots. Their BD-ODL dictionary learner and Bayesian CSCE recovery exploit channel sparsity, while the BCRB provides an MSE lower bound for ill-posed estimation. Numerical comparisons against LS, MMSE, FOCUSS, UAMP-SBL, FISTA, and other sparse estimators show large NMSE gains and convergence within about ten EM iterations. This contribution is a physical-layer estimation method rather than an application-specific control or resource-allocation decision model.

## Problem framing

THz UM-MIMO (array-of-subarrays, AoSA, with thousands of antennas) is a key 6G technology for near-Tbps data rates. The Rayleigh distance at THz (proportional to array aperture²/wavelength) can be hundreds of meters, so near-field spherical-wavefront effects coexist with far-field planar-wavefront paths in the same channel sample — a **hybrid-field** scenario. Existing CSCE methods use either angular-domain (far-field only) or polar-domain (near-field only) sparsifying matrices, neither of which correctly represents hybrid-field channels, causing performance loss. Additionally, the PC hybrid AoSA architecture compresses received pilots, making CE an ill-posed recovery problem. The paper adds molecular absorption and reflection attenuation to the channel model for physical realism.

## System model

- **Uplink THz UM-MIMO CE** at a BS with UPA-based AoSA (N_SA subarrays × N_RE REs per subarray = A total antennas). Single-antenna UEs.
- **Hybrid combining (HC) architecture:** partially-connected (PC) structure; each SA has one RF chain + dedicated phase shifters. High-dimensional channel recovered from compressed pilot measurements.
- **Channel model:** hybrid-field paths (near-field SW + far-field PW), molecular absorption loss, reflection attenuation, and spreading loss — a more physically realistic model than pure Rayleigh/SV models.
- **BD-ODL:** iterative algorithm that learns a dictionary (sparsifying matrix) from batched channel samples; designed for online update as channel statistics evolve.
- **BL-CSCE:** exploits learned dictionary sparsity via expectation-maximization (EM)-based Bayesian recovery; handles ill-posed (underdetermined) CE.
- **BCRB:** derived as MSE lower bound for BL-aided CE in this hybrid-field setting.

## Key findings

- Proposed DL-aided Bayesian CSCE achieves **significant NMSE improvement** over LS, MMSE, FOCUSS, AMP-SBL, and FISTA baselines (parse abstract + contributions + Section IV).
- Empirically converges within ~10 iterations, demonstrating rapid convergence (parse contribution point 2 / Section IV).
- Existing angular-domain CSCE methods lose sparsity in hybrid-field channels due to the "energy spread effect"; the learned dictionary eliminates this loss (parse Section I-B, Table I).
- The BCRB provides a tight lower bound for the proposed approach in ill-posed scenarios (parse contribution point 1).

## Limitations / future work

UPA-based AoSA architecture assumed; other antenna configurations not treated. Parse does not give explicit NMSE numbers; references simulation figures. The BD-ODL algorithm's computational overhead for very large arrays is noted in the complexity analysis but not compared to online baselines in detail.

## Relation to the corpus

A physical-layer THz channel estimation anchor for [[near-field-communications]] and [[extremely-large-scale-mimo]] — the two physical-layer concepts that underpin 6G systems also appearing in [[wang-2024-xl-mimo-tutorial]] corpus entries. The BCRB methodology connects to [[cramer-rao-bound]] as used in ISAC sensing papers. Distinct from MEC offloading papers but provides the channel-model foundation for THz-band MEC systems like [[wu-2025-iopo-irs-uav-thz-mec]].

## Raw artifacts

- `raw/sources/Hybrid_Near-_and_Far-Field_THz_UM-MIMO_Channel_Estimation_A_Sparsifying_Matrix_Learning-Aided_Bayesian_Approach/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
