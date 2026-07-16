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
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-06-01
updated: 2026-07-16
modeling_card: required
---

# Joint Optimization of Trajectory and Jamming Power for Multiple UAV-Aided Proactive Eavesdropping

## Citation

Guo, D., Tang, L., Zhang, X., & Liang, Y.-C. (2024). *Joint Optimization of Trajectory and Jamming Power for Multiple UAV-Aided Proactive Eavesdropping*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3311484. (Manuscript received 1 August 2022; date of publication 4 September 2023; date of current version 4 April 2024 → year 2024.)

## TL;DR

A **wireless information surveillance** scenario where a legitimate party uses **multiple full-duplex UAVs** to eavesdrop on **multiple suspicious links**, each formed by a mobile suspicious UAV transmitter and its fixed ground destination. The legitimate UAVs simultaneously act as silent eavesdroppers and emit **cognitive jamming** to the suspicious destinations (forcing the suspicious source to lower its rate so the monitor can decode), while planning trajectories to improve their eavesdropping channels. The sequential decision problem is an MDP; the key trick is to **decompose** it into (1) a non-learning optimal jamming-power solver per state and (2) an RL-optimized **moving policy**, with **decentralized per-UAV** control for flight safety.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple full-duplex UAV monitors track moving suspicious UAV-to-ground links while receiving intercepted signals and transmitting cooperative jamming.

**Problem & objective**: Jointly choose motion and jamming to maximize long-run eavesdropping reward, $\max \liminf_{T\to\infty}\frac{1}{T}\sum_t r_t$, where $r_t$ combines eavesdropping rate and collision penalties.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV motion | $v_n(t)$ | discrete feasible velocity set | Movement action of monitor $n$ at slot $t$ |
| Jamming power | $p_n^m(t)$ | continuous nonnegative | Power sent by monitor $n$ toward suspicious link $m$ |
| Joint control policy | $\pi_n$ | decentralized policy | Maps each UAV's observation to its motion action |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Each motion action belongs to the feasible velocity set $\mathcal{V}$ |
| C2 | Jamming powers are nonnegative, $p_n^m(t)\geq0$ |
| C3 | Each monitor obeys its total jamming-power budget |
| C4 | The eavesdropping rate must meet the suspicious-link rate for successful decoding |
| C5 | Monitor trajectories preserve collision-avoidance and flight-safety separation |

**Algorithm**: Solve jamming powers with successive convex approximation, then train decentralized parameter-shared MAPPO movement policies in the resulting multi-agent decision process.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guo et al. [x] considered multiple full-duplex UAVs that cooperatively monitor moving suspicious UAV-to-ground links while transmitting jamming signals. They maximize long-run eavesdropping rate with collision penalties over per-UAV motion and per-link jamming powers, subject to velocity, power-budget, and successful-decoding constraints. The solution computes jamming power with successive convex approximation and trains decentralized movement policies with parameter-shared MAPPO. Simulations show the SCA power allocation approaches simplified exhaustive search, while MAPPO matches centralized PPO for two monitors and four links and reaches 1.4 bit/s/Hz in fewer than 2000 episodes for the larger case where centralized PPO requires about 4000.

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

The authorized interception role—and its distinction from activity hiding, camera observation, and trajectory-state tracking—is positioned in [[aerial-observation-control-covertness-surveillance-and-monitoring]].

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping/Joint_Optimization_of_Trajectory_and_Jamming_Power_for_Multiple_UAV-Aided_Proactive_Eavesdropping.md`
- Original PDF and extracted figures (`images/`) in the same folder.
