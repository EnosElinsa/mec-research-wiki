---
type: source
title: "Pursuit-Evasion Game for UAV Anti-Jamming Communications: An Opponent Modeling Based Reinforcement Learning Approach"
authors: ["Ziyan Yin", "Zhe Wang", "Jun Li", "Long Shi", "Yiyang Ni", "Shi Jin"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3678748"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-14"
tags: [source, uav-anti-jamming, pursuit-evasion, opponent-modeling, fictitious-self-play, recurrent-q-learning]
related:
  - "[[implicit-opponent-modeling]]"
  - "[[unpredictable-uav-trajectory-control]]"
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[fictitious-self-play]]"
  - "[[stochastic-game]]"
  - "[[ddqn]]"
  - "[[dueling-dqn]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[shi-jin]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# Pursuit-Evasion Game for UAV Anti-Jamming Communications: An Opponent Modeling Based Reinforcement Learning Approach

## Citation

Yin, Z., Wang, Z., Li, J., Shi, L., Ni, Y., & Jin, S. (2026). *Pursuit-Evasion Game for UAV Anti-Jamming Communications: An Opponent Modeling Based Reinforcement Learning Approach*. **IEEE Transactions on Mobile Computing**, 1-14. DOI: 10.1109/TMC.2026.3678748.

## TL;DR

Models a communicating UAV and an adaptive mobile jammer as a partially observable pursuit-evasion game, then combines neural fictitious self-play, LSTM history, and dueling double Q-learning so each side can adapt without observing the other's private state or policy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude rotary-wing UAV collects uplink data from ground devices while a mobile ground jammer pursues it. Both agents move simultaneously on a square grid with incomplete knowledge of the opponent's private state.

**Problem & objective**: The UAV solves $\max\mathbb E[\sum_t(\varphi_1\eta(t)-\varphi_2E_{\mathrm{con}}(t))]$, while the jammer solves $\max\mathbb E[\sum_t-\eta(t)]$; their coupled trajectory policies form a partially observable pursuit-evasion game.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory policy | $\pi^u$ | stochastic policy | Maps UAV observation history to movement probabilities |
| Jammer trajectory policy | $\pi^j$ | stochastic policy | Maps jammer observation history to movement probabilities |
| UAV movement | $a^u(t)$ | five discrete actions | Hover or move one grid step in a cardinal direction |
| Jammer movement | $a^j(t)$ | five discrete actions | Hover or move one grid step in a cardinal direction |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 14b-14c | UAV coordinates remain inside the service area |
| 14d | UAV battery satisfies $E(t)\geq E_{\min}$ |
| 15b-15c | Jammer coordinates remain inside the service area |
| Partial observation | The UAV cannot observe jammer position, and the jammer cannot observe UAV energy |
| Action sets | Both agents choose only hover or four cardinal movements |

**Algorithm**: NFSP-D3RN mixes a learned best-response policy with a supervised average policy to approximate fictitious self-play. LSTMs encode observation-action histories, double Q-learning reduces value overestimation, a dueling head separates value and advantage, and FIFO reinforcement replay plus reservoir-sampled supervised replay train the two policies.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yin et al. [x] modeled UAV anti-jamming communication as a partially observable pursuit-evasion game between a data-collecting UAV and a mobile jammer. The UAV maximizes weighted communication rate minus propulsion energy under area and battery constraints, while the jammer minimizes UAV rate through its trajectory. NFSP-D3RN combines neural fictitious self-play, recurrent history encoding, double Q-learning, and a dueling value architecture. With hidden jammer location, UAV cumulative reward improved by 10.89%, 36.82%, and 90.97% over NFSP-D3QN, D3RN, and D3QN, respectively. At a 3 dB SINR threshold, successful communications increased by 17.65%, 25%, and 42.86% over the same baselines. The decentralized controller was also reported to perform comparably to a full-observation MADDPG reference.

## Problem and system model

A fixed-altitude rotary-wing UAV collects uplink data from the nearest ground IoT device while a mobile ground jammer adapts its path. Both actors move simultaneously on a square grid through hover and four cardinal actions. The UAV trades cumulative communication rate against propulsion energy and must retain minimum battery; the jammer minimizes UAV rate and is treated as energy-unconstrained.

The UAV observes its energy, location, and binary SINR-success feedback but not jammer position. The jammer sees both positions and SINR feedback but not UAV energy. A single failed transmission is ambiguous under Nakagami fading, so both policies consume observation/action histories.

## Method

The NFSP-D3RN controller uses [[fictitious-self-play]] to mix a learned best response with a supervised average policy. This provides [[implicit-opponent-modeling]] from interaction history without a centralized critic or opponent-private information. LSTM encodes partial observations, double Q-learning limits overestimation, and a dueling head separates state value from action advantage. FIFO RL replay and reservoir-sampled supervised replay train the two policies.

## Key findings

- With observable jammer location, UAV cumulative reward improves by 5.07%, 15.53%, and 25% over NFSP-D3QN, D3RN, and D3QN.
- With hidden jammer location, the corresponding improvements are 10.89%, 36.82%, and 90.97%.
- At a 3 dB SINR threshold with hidden jammer location, successful communications increase by 17.65%, 25%, and 42.86% over those baselines.
- An anticipatory mixing value of 0.1 gives the highest cumulative reward in the reported setup.
- The decentralized method is reported as comparable to full-observation MADDPG, but the text gives no exact numerical gap.

## Limitations

The evidence is simulation-only: one UAV, one jammer, fixed altitude, grid motion, synthetic channels, and no measured jammer or field flight. Jammer energy and UAV acceleration/deceleration energy are omitted. The information asymmetry is fixed, and hidden-jammer inference relies only on binary success history confounded by fading. The paper invokes NFSP approximate-equilibrium guarantees but does not supply a new proof for the complete recurrent dueling-double architecture.

## Relation to the corpus

This is a communication/data-collection anti-jamming source, not MEC task execution. It complements [[cooperative-uav-pursuit-evasion]] geometrically but studies adversarial radio adaptation rather than cooperative physical capture.

## Comparison boundary

Relative to [[unpredictable-uav-trajectory-control]], this paper hides jammer state and adapts from recurrent history rather than recomputing a current-geometry randomized heading term slot by slot. Relative to [[qi-2026-ocma-ddqn-data-collection]], it models an adaptive mobile opponent rather than an episode-static jammer. Both remain simulation-scoped anti-jamming evidence; see [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- Parse: `raw/sources/Pursuit-Evasion_Game_for_UAV_Anti-Jamming_Communications_An_Opponent_Modeling_Based_Reinforcement_Learning_Approach/Pursuit-Evasion_Game_for_UAV_Anti-Jamming_Communications_An_Opponent_Modeling_Based_Reinforcement_Learning_Approach.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
