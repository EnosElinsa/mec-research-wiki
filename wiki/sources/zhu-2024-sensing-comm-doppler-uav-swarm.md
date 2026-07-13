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
  - "[[integrated-sensing-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[differential-evolution]]"
  - "[[uav-enabled-its]]"
  - "[[vehicular-mec]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[jiang-2025-isac-lae-overview]]"
created: 2026-05-31
updated: 2026-07-13
---

# Sensing-Communication Co-Design for UAV Swarm-Assisted Vehicular Network in Perspective of Doppler

## Citation

Zhu, Q., Liu, R., Wang, Z., Liu, Q., & Chen, C. (2024). *Sensing-Communication Co-Design for UAV Swarm-Assisted Vehicular Network in Perspective of Doppler*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3315868. (Manuscript received 7 Apr 2023; date of publication 15 Sep 2023; date of current version 13 Feb 2024.)

## TL;DR

A **sensing-communication co-design** scheme for **UAV-swarm-assisted vehicular networks** that explicitly accounts for **Doppler**. Doppler is essential for multidimensional sensing (especially velocity estimation) but causes SNR loss in communication. The paper establishes mathematical models for the effect of Doppler on communication and on sensing, analyzes how UAV link selection affects ground-vehicle (GV) sensing-communication performance, and minimizes the GVs' **maximum Cramér-Rao lower bound (CRLB)** for sensing estimates under an **SNR-loss constraint** (the communication-vs-sensing trade-off). The non-convex problem is solved by a **differential-evolution (DE)-based** algorithm.

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
