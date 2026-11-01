---
type: source
title: "Latency Minimization Oriented Radio and Computation Resource Allocations for 6G V2X Networks With ISCC"
authors: ["Peng Liu", "Xinyi Wang", "Zesong Fei", "Yuan Wu", "Jie Xu", "Arumugam Nallanathan"]
year: 2025
url: "https://doi.org/10.1109/TCOMM.2025.3616242"
venue: "IEEE Transactions on Communications"
modeling_card: required
tags: [source, integrated-sensing-computation-communication, v2x, vehicular-mec, branch-and-bound, receive-beamforming, max-min-fairness]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[vehicular-mec]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[jie-xu]]"
  - "[[yuan-wu]]"
  - "[[arumugam-nallanathan]]"
created: 2026-11-02
updated: 2026-11-02
---

# Latency Minimization Oriented Radio and Computation Resource Allocations for 6G V2X Networks With ISCC

## Citation

Liu, P., Wang, X., Fei, Z., Wu, Y., Xu, J., & Nallanathan, A. (2025). *Latency Minimization Oriented Radio and Computation Resource Allocations for 6G V2X Networks With ISCC*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2025.3616242.

## TL;DR

Vehicles use one ISAC signal to sense targets and to offload sensing echoes to multi-antenna roadside BSs for MEC processing. The paper minimizes the maximum sensing-task completion latency across vehicles under detection-probability constraints by jointly choosing sub-bands, vehicle power, local and edge CPU allocation, and BS receive beamforming, using alternating optimization with branch-and-bound and SCA.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple multi-antenna BSs with MEC servers serve $K$ single-antenna vehicles over $L$ orthogonal sub-bands. Each vehicle transmits an ISAC signal for target detection and data offloading, and may compute part of its task locally with power $\kappa f_{L,k}^3$.

**Problem & objective**: Problem (19), a MINLP: $\min_{\mathbf A,\mathbf p,\mathbf u,\mathbf f_L,\mathbf f_M}\max_kT_k$, the worst-case task completion latency.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sub-band allocation | $a_{lk}$ | binary | Sub-band $l$ assigned to vehicle $k$ |
| Transmit power | $p_k$ | continuous | Vehicle ISAC transmit power |
| Receive beamforming | $\mathbf u_k$ | $\lVert\mathbf u_k\rVert=1$ | BS combiner for vehicle $k$ |
| Local computation | $f_{L,k}$ | $[0,F_l]$ | Vehicle CPU frequency |
| Edge computation | $f_{m,k}$ | $\sum_kf_{m,k}\le\hat F_m$ | MEC CPU share at BS $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (19a) | Detection, sensing SINR $\gamma_k\ge\Gamma_d$. |
| (19b)-(19c) | Binary sub-band assignment, at most one sub-band per vehicle. |
| (19d) | Edge CPU budget, $\sum_kf_{m,k}\le\hat F_m$. |
| (19e) | Local CPU range, $0\le f_{L,k}\le F_l$. |
| (19f) | Vehicle power budget, $p_k+\kappa f_{L,k}^3\le P_{\max}$. |
| (19g) | Unit-norm receive beamformer. |

**Algorithm**: Alternate among blocks: sub-band allocation by branch-and-bound, transmit power by SCA, and receive beamforming and computation allocation in closed form.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] investigated an integrated sensing, communication, and computing enabled V2X system with multiple multi-antenna base stations serving single-antenna vehicles, in which vehicles perform ISAC to sense the environment and simultaneously offload the sensing data to roadside base stations over orthogonal sub-bands. Focusing on fairly minimizing the sensing completion latency while ensuring detection probability constraints, they jointly optimized sub-band allocation, transmit power control at vehicles, receive beamforming at base stations, and computation resources at the MEC servers. To solve the resulting mixed-integer nonlinear program, they proposed an alternating optimization algorithm that determines sub-band allocation by branch-and-bound, optimizes power control by successive convex approximation, and derives receive beamforming and computation allocation in closed form. Simulation results show that the joint design significantly reduces the maximum task completion latency among vehicles compared with optimizing radio or computation resources alone. A reduced-complexity variant cuts runtime by 92% with about 12% performance loss.

## Problem framing

Sensing and offloading share one waveform and one power budget, and local computing draws from the same budget, so radio and computation decisions are coupled.

## System model

- Detection probability depends on the sensing SINR.
- Latency combines offloading, edge processing, and local processing.

## Method

Alternating optimization with BnB, SCA, and closed-form beamforming and CPU updates.

## Key findings

- Joint radio and computation allocation lowers maximum latency compared with separate designs.
- With 48 vehicles, over 99% achieve a sensing SINR above 25 dB under the proposed sub-band allocation.
- Fewer iterations and relaxations reduce runtime by 92% at a 12% performance cost.

## Limitations / future work

Vehicles use orthogonal sub-bands, so interference among vehicles is not modeled.

## Relation to the corpus

A V2X instance of [[integrated-sensing-computation-communication]] within [[vehicular-mec]].

## Raw artifacts

- Parse: `raw/sources/Latency_Minimization_Oriented_Radio_and_Computation_Resource_Allocations_for_6G_V2X_Networks_With_ISCC/Latency_Minimization_Oriented_Radio_and_Computation_Resource_Allocations_for_6G_V2X_Networks_With_ISCC.md`
- Extracted figures are in the same folder; no companion PDF is present.
