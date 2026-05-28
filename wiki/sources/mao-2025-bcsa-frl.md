---
type: source
title: "A Blockchain-Enabled Cold Start Aggregation Scheme for Federated Reinforcement Learning-Based Task Offloading in Zero Trust LEO Satellite Networks"
authors: ["Bomin Mao", "Yangbo Liu", "Zixiang Wei", "Hongzhi Guo", "Yijie Xun", "Jiadai Wang", "Jiajia Liu", "Nei Kato"]
year: 2025
url: "https://doi.org/10.1109/JSAC.2025.3560003"
venue: "IEEE Journal on Selected Areas in Communications (JSAC)"
tags: [leo-satellite, mec, frl, federated-learning, blockchain, zero-trust, task-offloading, ddqn]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[zero-trust-architecture]]"
  - "[[federated-reinforcement-learning]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[ddqn]]"
  - "[[ccvm-correction-voting]]"
  - "[[csra-cold-start-reputation-aggregation]]"
  - "[[fl-poisoning-attacks]]"
  - "[[bcsa-frl-tolerates-up-to-half-malicious-satellites]]"
created: 2026-05-28
updated: 2026-05-28
---

# A Blockchain-Enabled Cold Start Aggregation Scheme for FRL-Based Task Offloading in Zero Trust LEO Satellite Networks

## Citation

Mao, B., Liu, Y., Wei, Z., Guo, H., Xun, Y., Wang, J., Liu, J., & Kato, N. (2025). *A Blockchain-Enabled Cold Start Aggregation Scheme for Federated Reinforcement Learning-Based Task Offloading in Zero Trust LEO Satellite Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2025.3560003.

Authors are with Northwestern Polytechnical University (Cybersecurity / R&D / Yangtze River Delta Institute) and Tohoku University.

## TL;DR

Proposes **BCSA-FRL**: a federated reinforcement-learning task-offloading scheme for [[leo-satellite-edge-computing|LEO satellite edge computing]] under a [[zero-trust-architecture|zero-trust]] threat model. Uses two new mechanisms layered onto an FRL pipeline backed by [[ddqn|Double DQN]]:

1. [[ccvm-correction-voting|CCVM]] — a Constrained Correction Voting Mechanism that down-weights satellites that consistently vote against block commission, defeating malicious-voting attacks on the consensus layer.
2. [[csra-cold-start-reputation-aggregation|CSRA]] — a Cold Start Reputation Aggregation scheme that sharply penalizes a satellite's FL aggregation weight when an attack is detected, then *gradually* recovers the weight as the replay buffer flushes the poisoned samples.

Tolerates up to ~50% malicious satellites with negligible performance loss; degrades gracefully beyond that majority threshold. See [[bcsa-frl-tolerates-up-to-half-malicious-satellites]].

## Problem framing

Service providers running 6G workloads on LEO constellations may rent satellites from multiple operators, breaking the implicit trust assumption used by classical [[federated-reinforcement-learning|FRL]] aggregation. Three concrete attack vectors:

- **Malicious voting** — bad satellites vote $V_F$ on every other satellite's model update, blocking convergence at the blockchain consensus layer.
- **Replay buffer poisoning** — passively bad: the satellite's RL replay buffer is corrupted, so its sub-model gradually drifts.
- **Model parameter poisoning** — actively bad: malicious satellite uploads random / biased weights during aggregation.

Goal: minimize the average task processing delay $\bar D_{c_i}$ — composed of transmission, queuing, and compute time — under any mix of these attackers.

Cast as an MDP with:

- **State:** inter-satellite distances $D$, current load $L(t, s_k)$, transmission rates $\mathcal R_{s_k \to s_{k'}}$, plus per-task compute requirement $R_{c_i}$ and delay threshold $D_{c_i}$.
- **Action:** which satellite within two hops to offload to.
- **Reward:** exponential ratio $r^{t,+} - r^{t,-}$ over completed-vs-failed task counts in window $\Delta T$.

## System / channel model

- **Path loss:** free-space + shadowing variant — $PL_{NOR}(d) = PL_F(d_0) + 10n\log_{10}(d/d_0) + X_\sigma$.
- **Link rate:** Shannon over $PL_{NOR}$.
- **Latency:** transmission ($\alpha S_{c_i} / \mathcal R$) + queuing ($\sum \beta_{i'} R_{c_i} / \mathcal C_{s_k}$) + compute ($R_{c_i} / \mathcal C_{s_k}$).
- **Task arrivals:** Poisson($\vartheta$) per time interval.

## Method

The full pipeline (BCSA-FRL) is a semi-distributed FRL framework over [[ddqn|DDQN]] agents (online + target nets), where global aggregation is mediated by a permissioned blockchain instead of a trusted central server.

### CCVM — Constrained Correction Voting

Each satellite's vote weight in the smart-contract consensus is corrected by a factor that decreases the more often it casts $V_F$ unilaterally. Effect: a satellite that *always* votes negative (the malicious-voting profile) sees its influence on block commission collapse, while occasional disagreements from honest satellites are not penalized.

### CSRA — Cold Start Reputation Aggregation

The trick: classical reputation schemes update reputation smoothly, so a recovering satellite still drags the global model. CSRA does a hard knockdown when an attack is detected, then **slowly** ramps the weight back up — matching the natural cleaning rate of the local replay buffer. This stops a "just-recovered" sub-model from dominating aggregation while its experience stream is still partially poisoned.

### Algorithm sketch

For each round of FRL:

1. Each satellite trains its local DDQN online network on its replay buffer.
2. Satellites broadcast model parameters; peers verify and emit $V_T$ / $V_F$ votes.
3. CCVM weights the votes; consensus decides commit / pre-commit / reject.
4. CSRA computes per-satellite aggregation weights (sharp drop under attack, slow recovery).
5. Aggregated global model is broadcast back; each satellite syncs its online net.
6. Target net periodically synced from online net (DDQN).

## Findings

- [[bcsa-frl-tolerates-up-to-half-malicious-satellites]] — BCSA-FRL keeps drop rate ≈5% and average delay ≈6 ms with up to 50% malicious satellites. FedAvg-FRL (the baseline) degrades sharply across the same range.
- **vs traditional offloading.** At task load 150: BCSA-FRL = 6.16% drop / 5.95 ms avg delay, vs Avg-Task-Burden = 20.05% / 7.40 ms, vs Random = 40.54% / 9.31 ms. At load 450: BCSA-FRL = 8.29% / 6.08 ms (still dominant).
- **CCVM ablation.** Without CCVM under combined malicious-voting + data-poisoning attack, reward converges to <10. With CCVM, reward converges to ~25.
- Beyond 50% malicious majority, the consensus mechanism itself fails — system stalls in rollback. Authors note >50% malicious is uncommon in practice.

## Limitations / future work

- Above-50% majority breaks the framework.
- No analysis of the smart-contract gas / blockchain compute overhead vs offloading latency budget.
- Validity of *committed* models is taken on consensus alone; the authors flag stronger model-validity verification as next work.

## Raw artifacts

- `raw/sources/A_Blockchain-Enabled_Cold_Start_Aggregation_Scheme_for_Federated_Reinforcement_Learning-Based_Task_Offloading_in_Zero_Trust_LEO_Satellite_Networks/full.md`
- Original PDF and extracted figures in the same folder.
