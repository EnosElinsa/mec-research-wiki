---
type: source
title: "Handover Protocol Learning for LEO Satellite Networks: Access Delay and Collision Minimization"
authors: ["Ju-Hyung Lee", "Chanyoung Park", "Soohyun Park", "Andreas F. Molisch"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3342975"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, leo-satellite-edge-computing, seamless-handover, deep-reinforcement-learning, non-terrestrial-network, protocol-learning]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[leo-handover-protocol]]"
  - "[[seamless-handover]]"
  - "[[non-terrestrial-network]]"
  - "[[impala]]"
  - "[[ppo]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[walker-star-constellation]]"
  - "[[soohyun-park]]"
created: 2026-06-01
updated: 2026-07-16
---

# Handover Protocol Learning for LEO Satellite Networks: Access Delay and Collision Minimization

## Citation

Lee, J.-H., Park, C., Park, S., & Molisch, A. F. (2024). *Handover Protocol Learning for LEO Satellite Networks: Access Delay and Collision Minimization*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3342975. (Manuscript received 30 July 2023; date of publication 21 December 2023; date of current version 12 July 2024 → year 2024.)

## TL;DR

A DRL-based **handover (HO) protocol** for **regenerative-type LEO satellite networks**, called **DHO**, that **skips the Measurement Report (MR)** step of the conventional 3GPP-NR HO procedure. After training on a pre-determined LEO orbital pattern, the serving-satellite agent uses its predictive capability to send the HO Request to a target satellite without waiting for the MR — eliminating the long uplink propagation delay (and power) incurred during the MR phase. DHO minimizes **access delay** and **collision rate** while keeping a high HO success rate, and is trained with the distributed **IMPALA** actor-learner algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground user equipment must hand over from a serving regenerative LEO satellite to a target satellite before the serving link disappears. At each of $N$ handover opportunities, the serving satellite can wait or send a handover request for each user to a candidate satellite on another orbital plane, with limited target resource blocks and random-access preambles creating collisions.

**Problem & objective**: DHO minimizes $\sum_{n=1}^{N}\left(D[n]+\nu C[n]\right)$, the horizon sum of average access delay and weighted collision rate, by controlling per-user handover requests and target-satellite selection.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Handover action | $a_j[n]$ | multi-discrete, $\{0,1,\ldots,K-1\}$ | Wait or request a target orbital plane for user $j$ in slot $n$ |
| One-hot action vector | $\mathbf a_j[n]$ | binary vector | Encoded wait or target-satellite decision |
| Joint handover action | $\mathbf a[n]$ | stacked multi-discrete action | Decisions for all ground users at opportunity $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Exactly one wait-or-target action is selected per user: $\sum_{k=0}^{K-1}a_k=1$ |
| C2 | A handover cannot select another satellite on the serving satellite's orbital plane |
| C3 | Satellite positions evolve according to the predetermined discrete orbital model |
| C4 | A target admits no more requests than its available resource blocks |
| C5 | Successful random access requires a non-colliding preamble after admission |

**Algorithm**: DHO removes the Measurement Report step and learns the request and target decisions with IMPALA. Parallel actors interact with independent LEO handover environments, upload trajectories to a central learner, and use V-trace targets with truncated importance weights to correct actor-policy lag before updated parameters are redistributed.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lee et al. [x] learned per-user handover timing and target-satellite selection for massive access in regenerative LEO satellite networks. Their objective minimizes access delay plus a weighted collision rate under orbital evolution, single-target selection, resource-block admission, and random-access contention. DHO removes the uplink Measurement Report and trains a multi-discrete policy with distributed IMPALA and V-trace correction. With sufficient resource blocks, DHO achieved 6.8 times lower access delay than conventional handover and 5.02 times lower delay than a random policy, while adapting its request rate when resources became scarce.

## Problem framing

LEO mega-constellations face **massive access** and unique HO challenges: long propagation delay (one-way ~1.6–6 ms over 500–2000 km), large coverage areas, and limited satellite resources. Applying terrestrial HO protocols is suboptimal because the MR sent from a ground UE to a LEO satellite becomes outdated, consumes high uplink power, and is unreliable. With dense, highly-correlated ground UEs (e.g., simultaneous A3 events in a street canyon), simultaneous HO requests cause collisions and long access delays. The paper targets the **preparation phase** of the HO process to remove the MR bottleneck.

## System model

- **Network.** $K$ orbital planes, $|\mathcal{T}_k|=I$ LEO satellites per plane in uniform circular motion ([[walker-star-constellation]]-style geometry), serving ground UEs in an area; serving-SAT acts as serving-gNB, neighboring SATs are target-gNBs.
- **HO opportunities.** $N$ discrete HO slots in an interval $T$; at each slot a UE/agent chooses an action $a_j[n]\in\{0,1,\dots,K-1\}$ (which target-SAT, or wait), no HO to a same-plane SAT.
- **Collisions.** Two kinds — NACK from insufficient resource blocks (RBs) at the target-SAT, and PRACH preamble collisions (two-step RA from 5G-NR Release 16).
- **Metrics.** Collision rate and access delay (and HO success rate), with an explicit access-delay-vs-collision-rate trade-off studied.

## Method

A **DRL-based protocol redesign**: the serving-gNB agent predicts the UE's signal information and issues the HO Request without an MR, collapsing the preparation phase. Training uses **IMPALA** (importance-weighted actor-learner architecture) — an off-policy distributed algorithm with parallel actor-learners and **V-trace** truncated-importance-sampling targets — chosen for stable training over large state/action spaces. The paper also evaluates other DRL algorithms (DQN, A3C, PPO) for comparison (Appendix B).

## Key findings

- DHO achieves up to **6.86× lower access delay than the conventional HO protocol and 4.18× lower than heuristic methods** (abstract / introduction; the paper attributes the detailed numbers to its Tables IV–V).
- It outperforms the legacy HO protocol across diverse conditions in access delay, collision rate, and HO success rate, at lower power (MR skipped).
- The trained policy's behavior is interpreted to explain the gains and its adaptability across scenarios.

## Limitations / future work

The primary focus is fixed VSAT-type UEs (mobile handheld UEs noted as needing minor adjustments). The captured parse does not enumerate explicit future-work targets → `not in parse`. DHO presumes training on a known/pre-determined orbital pattern.

## Relation to the corpus

A **LEO-satellite networking** entry centered on the HO procedure itself, distinct from the corpus's compute-state handover work [[han-2024-sagin-fl-handover]] (which hands over partially-trained models/data across satellites for federated learning). Here the "handover" is the connection HO and the contribution is **protocol learning** (skipping the MR) rather than offloading; it anchors the new [[leo-handover-protocol]] concept and links to [[seamless-handover]], [[leo-satellite-edge-computing]], and the [[impala]] / [[ppo]] DRL backbones. (Networking-focused, not a computation-offloading paper.)

## Raw artifacts

- `raw/sources/Handover_Protocol_Learning_for_LEO_Satellite_Networks_Access_Delay_and_Collision_Minimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
