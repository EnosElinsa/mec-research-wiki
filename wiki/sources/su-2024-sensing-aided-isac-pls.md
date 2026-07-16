---
type: source
modeling_card: required
title: "Sensing-Assisted Eavesdropper Estimation: An ISAC Breakthrough in Physical Layer Security"
authors: ["Nanchi Su", "Fan Liu", "Christos Masouros"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3306029"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, physical-layer-security, cramer-rao-bound, secrecy-rate, artificial-noise, beamforming]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[physical-layer-security]]"
  - "[[cramer-rao-bound]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[wang-gai-isac-physical-layer]]"
  - "[[fan-liu]]"
  - "[[christos-masouros]]"
  - "[[lu-2026-icsn-beamforming]]"
created: 2026-05-31
updated: 2026-07-16
---

# Sensing-Assisted Eavesdropper Estimation: An ISAC Breakthrough in Physical Layer Security

## Citation

Su, N., Liu, F., & Masouros, C. (2024). *Sensing-Assisted Eavesdropper Estimation: An ISAC Breakthrough in Physical Layer Security*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3306029. (Manuscript received 15 Oct 2022; date of publication 23 Aug 2023; date of current version 11 Apr 2024.)

## TL;DR

A **sensing-aided physical-layer-security (PLS)** scheme for ISAC systems. A well-known limitation of PLS is needing information about potential eavesdroppers (Eves); the paper uses the **sensing** functionality of ISAC to estimate Eves' directions. The dual-functional base station first emits an **omnidirectional waveform** to detect Eves via the **combined Capon and approximate maximum likelihood (CAML)** technique, then formulates a **weighted optimization** that simultaneously maximizes the **secrecy rate** (aided by **artificial noise, AN**) and minimizes the **Cramér-Rao Bound (CRB)** of targets'/Eves' estimation. Because the secrecy-rate expression is a function of estimation accuracy, sensing and security improve each other across iterations until convergence.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A dual-functional base station serves cooperative users while sensing potential eavesdroppers that are also radar targets. An initial omnidirectional waveform and CAML estimation provide uncertain Eve directions; subsequent artificial-noise-aided secure beamforming balances secrecy rate and sensing accuracy through a widened beampattern.

**Problem & objective**: A weighted non-convex ISAC/PLS program maximizes secrecy rate while minimizing eavesdropper-estimation CRB, $\max\;R_s-\lambda\operatorname{CRB}$, subject to a wide-main-beam beampattern and transmit-power constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beamformer | $\mathbf W_c$ | complex continuous matrix | Confidential-data precoder |
| Artificial-noise covariance | $\mathbf W_{AN}$ | positive semidefinite matrix | AN used to reduce Eve's secrecy rate |
| Sensing beamformer | $\mathbf W_s$ | complex continuous matrix | Radar/sensing waveform design |
| Main-beam width | $\Delta\theta$ | continuous, accuracy-bounded | Angular coverage chosen from the prior CRB |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Total transmit covariance satisfies the BS power budget |
| C2 | The sensing beampattern covers the CRB-derived Eve angular uncertainty region |
| C3 | Covariance matrices are positive semidefinite and beamforming ranks are feasible |
| C4 | Confidential-user quality and artificial-noise/secrecy expressions remain valid |

**Algorithm**: Emit an omnidirectional probe → estimate Eve directions with CAML and compute the CRB → alternate FIM/CRB beamforming and secrecy-rate/AN optimization → solve the weighted fractional block with fractional programming → widen the sensing beam from the updated uncertainty → repeat until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Su et al. [x] studied sensing-assisted physical-layer security in an integrated sensing and communication base-station system. The base station first emits an omnidirectional waveform and uses combined Capon and approximate maximum likelihood estimation to obtain potential eavesdropper directions. It then solves a weighted design that maximizes secrecy rate with artificial noise while minimizing the Cramér-Rao bound of target and Eve estimation under beampattern and transmit-power constraints. An alternating optimization procedure updates Fisher-information and secrecy-rate blocks, with fractional programming used for the weighted problem. Numerical results show that secrecy rate increases as the estimation CRB decreases for both single-Eve and multi-Eve cases.

## Problem framing

In mmWave ISAC, the shared spectrum + broadcast nature of transmission makes security hard: Rician channels couple the LoS communication channel to the sensing channel (breaking the i.i.d. legitimate-vs-eavesdrop-channel assumption of classical PLS), and confidential data embedded in radar probing signals is susceptible to interception by the very targets being illuminated. PLS conventionally needs Eve channel/location knowledge — which is exactly what sensing can supply.

## System model

- **Actors.** A dual-functional access point / base station (communication + radar), cooperative communication users (CUs, whose locations are known), and potential eavesdroppers (Eves) that are also sensing targets.
- **Stage 1 — detection.** Emit an omnidirectional waveform; receive echoes from CUs and Eves; remove known CU angles to obtain Eve angle estimates, with accuracy measured by the **CRB** ([[cramer-rao-bound]]).
- **Stage 2 — secure beamforming.** Formulate a weighted problem to minimize the CRB of targets/Eves and maximize the secrecy rate, subject to a wide-main-beam beampattern constraint (width set by estimation accuracy) and a transmit-power budget.
- **Robustness.** Eve-location uncertainty is handled by widening the sensing beampattern's main beam to cover the angular region where an Eve may appear, indicated by the previous iteration's CRB.

## Method

- **CAML** (combined Capon + approximate maximum likelihood) for Eve angle estimation.
- An **alternating optimization** algorithm that iteratively maximizes the determinant of the **Fisher Information Matrix (FIM)** and the secrecy rate with the aid of AN; the secrecy rate is updated as Eve-angle estimation accuracy improves ([[alternating-optimization-sdr-sca]] family).
- A **fractional programming (FP)** algorithm to solve the weighted optimization problem, verified for both single-Eve and multi-Eve detection ([[fractional-programming-dinkelbach]]).
- Analytical lower bound on CRB and upper bound on secrecy rate are derived.

## Key findings

- Numerical results show the secrecy rate is **enhanced as the CRB decreases**, in both single-Eve and multi-Eve scenarios — i.e. better sensing accuracy yields better security, the paper's central "mutual benefit" claim (specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work; the study is a (non-UAV) terrestrial ISAC base-station design, evaluated by simulation.

## Relation to the corpus

A **sensing-aided PLS** anchor for the wiki's ISAC/security thread, distinct from the UAV-mounted secure-ISAC work [[yao-2025-secure-isac-dual-eavesdropping]] (which optimizes a UAV trajectory + beamforming against a dual-functional eavesdropper). Here there is no UAV — the novelty is using radar sensing to *estimate the eavesdropper* and feeding that into PLS. Framed conceptually by the UAV-ISAC overview [[meng-2024-uav-isac-overview]] and the GAI-for-ISAC physical-layer survey [[wang-gai-isac-physical-layer]]. Introduces and reinforces [[cramer-rao-bound]] as the sensing figure of merit, alongside [[physical-layer-security]] and [[integrated-sensing-and-communication]].

## Raw artifacts

- `raw/sources/Sensing-Assisted_Eavesdropper_Estimation_An_ISAC_Breakthrough_in_Physical_Layer_Security/Sensing-Assisted_Eavesdropper_Estimation_An_ISAC_Breakthrough_in_Physical_Layer_Security.md`
- Original PDF and extracted figures in the same folder.
