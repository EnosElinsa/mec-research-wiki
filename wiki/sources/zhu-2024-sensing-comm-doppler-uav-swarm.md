---
type: source
title: "Sensing-Communication Co-Design for UAV Swarm-Assisted Vehicular Network in Perspective of Doppler"
authors: ["Qian Zhu", "Rongke Liu", "Zijie Wang", "Qirui Liu", "Changwen Chen"]
year: 2024
url: "https://doi.org/10.1109/TVT.2023.3315868"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, integrated-sensing-and-communication, uav-swarm, vehicular-mec, cramer-rao-bound, differential-evolution, doppler]
related:
  - "[[rongke-liu]]"
  - "[[qian-zhu]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[differential-evolution]]"
  - "[[uav-enabled-its]]"
  - "[[vehicular-mec]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[jiang-2025-isac-lae-overview]]"
modeling_card: required
created: 2026-05-31
updated: 2026-07-16
---

# Sensing-Communication Co-Design for UAV Swarm-Assisted Vehicular Network in Perspective of Doppler

## Citation

Zhu, Q., Liu, R., Wang, Z., Liu, Q., & Chen, C. (2024). *Sensing-Communication Co-Design for UAV Swarm-Assisted Vehicular Network in Perspective of Doppler*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3315868. (Manuscript received 7 Apr 2023; date of publication 15 Sep 2023; date of current version 13 Feb 2024.)

## TL;DR

A **sensing-communication co-design** scheme for **UAV-swarm-assisted vehicular networks** that explicitly accounts for **Doppler**. Doppler is essential for multidimensional sensing (especially velocity estimation) but causes SNR loss in communication. The paper establishes mathematical models for the effect of Doppler on communication and on sensing, analyzes how UAV link selection affects ground-vehicle (GV) sensing-communication performance, and minimizes the GVs' **maximum Cramér-Rao lower bound (CRLB)** for sensing estimates under an **SNR-loss constraint** (the communication-vs-sensing trade-off). The non-convex problem is solved by a **differential-evolution (DE)-based** algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A formation-controlled UAV swarm provides joint TDOA/FDOA sensing and OFDM downlink communication to moving ground vehicles in an urban canyon; Doppler in the dynamic air-to-ground links improves position and velocity sensing but causes communication SNR loss.

**Problem & objective**: Problem P1, a non-convex min-max subset-selection problem, minimizes $\max_{k\in\mathcal K}[\mathrm{CRLB}(\mathbf u_k)+\mathrm{CRLB}(\dot{\mathbf u}_k)]$ subject to Doppler-induced SNR-loss and geometry limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV subset selection | $\mathbf V=[\mathcal V_1,\ldots,\mathcal V_K]^T$ | Discrete index matrix, five UAVs per GV | Aerial anchors selected to serve each ground vehicle |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV horizontal coordinates remain within $v_{\min}\le v_{x,y}^i\le v_{\max}$ |
| C2 | Inter-UAV distances satisfy $\delta_{\mathrm{thr}}^{\mathrm{safe}}\le\|\mathbf v_i-\mathbf v_j\|\le\delta_{\mathrm{thr}}^{\mathrm{UAV}}$ |
| C3 | Selected UAV-GV link distances do not exceed $\delta_{\mathrm{thr}}^{\mathrm{dis}}$ |
| C4 | Selected UAV-GV relative velocities do not exceed $\delta_{\mathrm{thr}}^{\mathrm{vel}}$ |
| C5 | Average Doppler SNR loss satisfies $M_0^{-1}\sum_i Dnf_{\mathbf v_{k_i}\leftrightarrow\mathbf u_k}\le Dnf_{\mathrm{thr}}$ |

**Algorithm**: Differential evolution, encode all GVs' UAV subsets as each individual, initialize a feasible population, evaluate CRLB and constraint-penalty fitness, apply mutation and crossover, retain fitter individuals, and return the best subset matrix.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhu et al. [x] studied Doppler-oriented sensing-communication co-design for UAV-swarm-assisted vehicular networks. They modeled Doppler-induced OFDM SNR loss together with TDOA/FDOA position and velocity estimation and optimized the UAV links selected for each ground vehicle. The resulting non-convex problem minimizes the maximum sum of position and velocity CRLBs under deployment, safety, relative-motion, and SNR-loss constraints. A differential-evolution algorithm encodes the selected UAV subsets as individuals and iteratively applies fitness evaluation, mutation, crossover, and selection. Numerical results report sensing-accuracy improvements above 30% while maintaining communication and communication gains above 20% without reducing sensing capability.

## Problem framing

Intelligent vehicle networks are often deployed in harsh environments (urban canyons, isolated areas) where GNSS degrades under NLoS propagation. UAVs, with high mobility and flexible deployment, can assist GVs. Prior UAV-assisted vehicular work designs localization/communication separately, often **ignoring Doppler or assuming it perfectly eliminated**, yielding unstable or impractical dynamic models. There has been no unified theoretical framework specifying the communication-vs-sensing trade-off under Doppler — the gap this paper targets.

## System model

- **Actors.** A UAV swarm providing sensing + communication for ground vehicles (GVs).
- **Doppler models.** Separate mathematical models for Doppler's effect on communication (SNR loss) and on sensing (velocity estimation via FDOA-type information that also tightens position accuracy).
- **Link selection.** Analysis of how UAV-to-GV link selection trades off the two functionalities.
- **Objective.** Minimize the maximum CRLB ([[cramer-rao-bound]]) across GVs subject to an SNR-loss constraint.

## Method

- An efficient **differential-evolution (DE)-based algorithm** finds a sub-optimal solution to the complicated non-convex min-max-CRLB problem ([[differential-evolution]]).

## Key findings

- Numerical results show the co-design scheme improves **sensing accuracy by more than 30%** while ensuring communication, and outperforms by **over 20% in communication** without sacrificing sensing capacity, versus state-of-the-art methods (figures quoted verbatim from the abstract; specific curves in the paper).

## Limitations / future work

Results are simulation-based. The authors point to follow-up research on resource utilization and energy efficiency of UAV swarms under the proposed co-design scheme.

## Relation to the corpus

An **ISAC co-design** entry that, unlike the secrecy-focused [[su-2024-sensing-aided-isac-pls]], targets the **Doppler-driven sensing-vs-communication trade-off** for UAV-swarm vehicular sensing. Shares the CRB/CRLB sensing figure of merit with [[su-2024-sensing-aided-isac-pls]] and the DE optimizer with several evolutionary UAV works. Conceptually framed by the UAV-ISAC overview [[meng-2024-uav-isac-overview]] and the ISAC-for-LAE overview [[jiang-2025-isac-lae-overview]]. Reinforces [[integrated-sensing-and-communication]], [[cramer-rao-bound]], and [[uav-enabled-its]]. (Sensing/communication only — no MEC offloading in this paper.)

## Raw artifacts

- `raw/sources/Sensing-Communication_Co-Design_for_UAV_Swarm-Assisted_Vehicular_Network_in_Perspective_of_Doppler/full.md`
- Original PDF and extracted figures in the same folder.
