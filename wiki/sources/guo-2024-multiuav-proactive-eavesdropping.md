---
type: source
title: "Joint Optimization of Trajectory and Jamming Power for Multiple UAV-Aided Proactive Eavesdropping"
authors: ["Delin Guo", "Lan Tang", "Xinggan Zhang", "Ying-Chang Liang"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3311484"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, proactive-eavesdropping, uav-trajectory-control, physical-layer-security, multi-agent-reinforcement-learning, friendly-jamming-uav]
related:
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[wireless-information-surveillance]]"
  - "[[proactive-eavesdropping]]"
  - "[[uav-trajectory-control]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[cooperative-jamming]]"
  - "[[ma-pomdp]]"
  - "[[pomdp]]"
  - "[[shao-2024-drl-antijamming-mec]]"
created: 2026-06-01
updated: 2026-07-14
---

# Joint Optimization of Trajectory and Jamming Power for Multiple UAV-Aided Proactive Eavesdropping

## Citation

Guo, D., Tang, L., Zhang, X., & Liang, Y.-C. (2024). *Joint Optimization of Trajectory and Jamming Power for Multiple UAV-Aided Proactive Eavesdropping*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3311484. (Manuscript received 1 August 2022; date of publication 4 September 2023; date of current version 4 April 2024 → year 2024.)

## TL;DR

A **wireless information surveillance** scenario where a legitimate party uses **multiple full-duplex UAVs** to eavesdrop on **multiple suspicious links**, each formed by a mobile suspicious UAV transmitter and its fixed ground destination. The legitimate UAVs simultaneously act as silent eavesdroppers and emit **cognitive jamming** to the suspicious destinations (forcing the suspicious source to lower its rate so the monitor can decode), while planning trajectories to improve their eavesdropping channels. The sequential decision problem is an MDP; the key trick is to **decompose** it into (1) a non-learning optimal jamming-power solver per state and (2) an RL-optimized **moving policy**, with **decentralized per-UAV** control for flight safety.

## Problem framing

Passive eavesdropping only works when the eavesdropping channel beats the suspicious channel — often false. **Proactive eavesdropping via jamming** degrades the suspicious channel to enable reliable decoding. Prior UAV-eavesdropping work used silent UAVs (trajectory only), single UAVs (can't cover multiple links), or assumed fixed suspicious node locations. This paper is, per its claim, the first to study **jamming-assisted multi-UAV eavesdropping against multiple UAV-enabled (mobile) suspicious links**.

## System model

- **Actors.** $N$ legitimate full-duplex UAV eavesdroppers (each with separate jamming + receiving antennas) vs. $M$ suspicious links (mobile suspicious UAV $S_m$ → fixed destination $D_m$), FDMA across links.
- **Channels.** UAV-to-UAV air-to-air dominated by LoS; air-to-ground (jammer/source → destination) Rician.
- **Decoding.** Eavesdropping succeeds when the legitimate party's joint-decoding rate exceeds the suspicious link rate; a central console fuses the $E_n$ observations and runs the RL.
- **Constraint.** Per-UAV total jamming power budget; collision-avoidance / flight safety motivates decentralized control.

## Method

The problem is modeled as a (multi-agent) MDP and solved by a **two-phase decoupled** approach, proven to retain optimality:

1. **Jamming-power allocation** — a non-learning **optimal solver** computes the jamming powers under each system state (handling the eavesdropping-constraint feasibility that is hard to embed in an RL policy).
2. **Moving policy** — RL optimizes each UAV's movement action; an **individual (decentralized) policy** is learned per UAV rather than a centralized joint policy, because large-action-space training is harder and a blocked/jammed control signal could down a centrally-controlled UAV.

## Key findings

- With jamming assistance, the scheme effectively guarantees the eavesdropping rate and **eavesdropping success rate** on multiple suspicious links while deploying **fewer eavesdropping UAVs** (qualitative; specific simulation curves are in the figures and not asserted here as exact magnitudes).
- The decoupled optimization is shown to preserve optimality versus solving the joint MDP directly.

## Limitations / future work

Suspicious users are assumed unaware of being monitored (no countermeasures). The captured parse does not enumerate explicit future-work targets → `not in parse`.

## Relation to the corpus

A **proactive-eavesdropping / surveillance** entry (physical-layer-security-adjacent, not MEC). It contributes the new [[proactive-eavesdropping]] concept and connects to the wiki's UAV-jamming threads — [[friendly-jamming-uav]] and [[cooperative-jamming]] — though here jamming serves *legitimate surveillance* rather than protecting a friendly link. Its decompose-then-RL structure (closed-form power solver + learned trajectory) echoes the hybrid solver pattern seen across the DRL track, and its decentralized multi-agent MDP framing links to [[ma-pomdp]] / [[pomdp]]. (Surveillance/PLS anchor, not a computation-offloading paper.)

## Raw artifacts

- `raw/sources/Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
