---
type: source
title: "A Tutorial on Extremely Large-Scale MIMO for 6G: Fundamentals, Signal Processing, and Applications"
authors: ["Zhe Wang", "Jiayi Zhang", "Hongyang Du", "Dusit Niyato", "Shuguang Cui", "Bo Ai", "Mérouane Debbah", "Khaled B. Letaief", "H. Vincent Poor"]
year: 2024
url: "https://doi.org/10.1109/COMST.2023.3349276"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
tags: [source, survey, tutorial, extremely-large-scale-mimo, near-field-communications, 6g, signal-processing, physical-layer]
related:
  - "[[extremely-large-scale-mimo]]"
  - "[[near-field-communications]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[physical-layer-security]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[terahertz-communication]]"
  - "[[wang-gai-isac-physical-layer]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
  - "[[mahboob-2024-ai-ntn-survey]]"
created: 2026-06-02
updated: 2026-06-02
---

# A Tutorial on Extremely Large-Scale MIMO for 6G: Fundamentals, Signal Processing, and Applications

## Citation

Wang, Z., Zhang, J., Du, H., Niyato, D., Cui, S., Ai, B., Debbah, M., Letaief, K. B., & Poor, H. V. (2024). *A Tutorial on Extremely Large-Scale MIMO for 6G: Fundamentals, Signal Processing, and Applications*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2023.3349276. (Manuscript received 14 July 2023; revised 9 November 2023; accepted 13 December 2023; date of publication 2 January 2024; date of current version 23 August 2024 → year 2024.)

## TL;DR

A **comprehensive survey / tutorial on extremely large-scale MIMO (XL-MIMO)** as a 6G enabler. XL-MIMO deploys a much larger antenna count and array aperture than conventional massive MIMO (mMIMO) to gain spectral efficiency and spatial degrees of freedom, which pushes operation into the **near-field** regime where spherical-wave (rather than planar-wave) propagation and new electromagnetic effects dominate. The survey introduces four hardware designs — ULA-based, UPA-based with patch antennas, UPA-based with point antennas, and continuous-aperture (CAP)-based XL-MIMO — reviews near-field channel modeling (LoS / NLoS / hybrid), surveys low-complexity and deep-learning-empowered signal processing (channel estimation, beamforming), and outlines applications and future directions.

This is the wiki's **XL-MIMO / near-field physical-layer anchor**. It is a communications-physical-layer reference, not an MEC paper.

## Problem framing

6G targets a ~100× peak-rate increase (toward Tb/s), ~10× lower latency, and higher reliability than 5G, motivating new physical-layer technologies. XL-MIMO extends mMIMO by an order of magnitude more antennas in a compact space, but this raises two coupled challenges the survey organizes around: (1) the **extremely large antenna count** brings high signal-processing complexity plus EM effects absent in mMIMO (spatial non-stationarity, severe mutual coupling, polarization); and (2) the large aperture makes users fall in the **near field**, so conventional far-field channel models and signal processing become mismatched.

## Scope surveyed

- **Hardware designs** (Section II): four general XL-MIMO architectures — ULA-based, UPA-based (patch / point antennas), and CAP-based — with the discrete-aperture approaches following compact sub-half-wavelength antenna packing and CAP approximating a spatially-continuous aperture via metamaterials. The survey compares antenna spacing, antenna characteristics, scenarios, and carrier frequencies, and relates the designs to holographic MIMO, large intelligent surfaces (LIS), and extremely large-scale antenna arrays (ELAA).
- **Channel modeling** (Section III): EM characteristics (spherical-wave, spatial non-stationarity, polarization), distance boundaries / EM regions, and LoS / NLoS / hybrid near-field channel models, with modeling guidelines.
- **Signal processing** (Section IV): low-complexity near-field **channel estimation** and **beamforming** schemes, plus **deep-learning-empowered** processing — emphasized to promote practical implementation.
- **Applications & future directions** (Sections V–VI): physical-layer security enhancement, [[integrated-sensing-and-communication|ISAC]], and IoT as application scenarios; AI-aided resource allocation, energy efficiency / green communication, and semantic communication as future directions.

## Key findings

As a survey/tutorial it reports no original benchmarks. Its contributions (its own stated framing) are: unifying four XL-MIMO hardware designs and their relationships; a thorough near-field channel-modeling tutorial with distance-boundary / EM-region summaries; a review of low-complexity and deep-learning signal-processing schemes aimed at practical implementation; and an application + future-direction map. It positions itself against prior XL-MIMO reviews (which it argues focus on a single design such as holographic MIMO, or on a single perspective) by offering a more holistic hardware-design comparison.

## Limitations / future work

A survey, so no controlled experiments of its own. The CAP-based (continuous-aperture / metamaterial) realization is flagged as immature — only a few works model and implement it — and near-field signal processing, mutual-coupling handling, and practical low-complexity implementation are named as open problems. The future directions it lists (AI-aided resource allocation, energy efficiency / green communication, semantic communication) are forward-looking rather than validated.

## Relation to the corpus

A **physical-layer 6G anchor** that complements the wiki's other PHY-leaning references rather than the MEC offloading core. Its near-field / ISAC / PLS framing connects to the generative-AI ISAC physical-layer overview [[wang-gai-isac-physical-layer]] (a shared Hongyang Du / Dusit Niyato author neighborhood). It sits beside the GAI-for-wireless survey [[khoramnejad-2025-gai-wireless-optimization-survey]] and the AI-empowered NTN survey [[mahboob-2024-ai-ntn-survey]] as a foundational-survey reference, and its [[active-ris|RIS]]/[[terahertz-communication|THz]] context overlaps the corpus's RIS-ISAC and THz-MEC threads. The lead author **Hongyang Du** recurs widely across the corpus with differing affiliations and is intentionally not yet promoted to an entity page; [[dusit-niyato]] is a confirmed entity.

## Raw artifacts

- `raw/sources/A_Tutorial_on_Extremely_Large-Scale_MIMO_for_6G_Fundamentals_Signal_Processing_and_Applications/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
