---
type: source
title: "Multi-Agent Reinforcement Learning-Based Resource Allocation for UAV Networks"
authors: ["Jingjing Cui", "Yuanwei Liu", "Arumugam Nallanathan"]
year: 2020
url: "https://doi.org/10.1109/TWC.2019.2935201"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 19, no. 2, pp. 729-743"
tags: [source, uav-communications, resource-allocation, stochastic-game, multi-agent-q-learning, power-control]
related:
  - "[[stochastic-game]]"
  - "[[multi-agent-q-learning]]"
  - "[[nash-equilibrium]]"
  - "[[air-to-ground-channel-model]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[yuanwei-liu]]"
  - "[[arumugam-nallanathan]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Multi-Agent Reinforcement Learning-Based Resource Allocation for UAV Networks

## Citation

Cui, J., Liu, Y., & Nallanathan, A. (2020). *Multi-Agent Reinforcement Learning-Based Resource Allocation for UAV Networks*. **IEEE Transactions on Wireless Communications, 19**(2), 729-743. DOI: 10.1109/TWC.2019.2935201.

## TL;DR

Models selfish UAV base stations as independent tabular Q-learning agents. Each chooses one user, subchannel, and discrete power level from a binary local QoS state, without exchanging actions or rewards with other UAVs.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $M$ single-antenna UAV base stations with predefined trajectories serve $L$ single-antenna ground users over $K$ reusable orthogonal subchannels. Each UAV has only local CSI, measures whether its selected link meets a QoS threshold, and acts without exchanging actions or rewards with the other UAVs.

**Problem & objective**: The dynamic allocation is a noncooperative stochastic game in which UAV $m$ maximizes its discounted reward $v_m(t)=\sum_{\tau=0}^{\infty}\delta^{\tau}R_m(t+\tau+1)$. Its instantaneous reward is throughput minus a power cost when $\gamma_m(t)\geq\bar\gamma_m$ and zero otherwise.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Served user | $a_m^l(t)$ | Binary selection | Chooses at most one ground user |
| Subchannel | $c_m^k(t)$ | Binary selection | Chooses at most one of $K$ subchannels |
| Power level | $p_m^j(t)$ | Binary selection among $J$ levels | Chooses one discrete transmit-power level |
| Joint local action | $\theta_m(t)=(a_m(t),c_m(t),p_m(t))$ | Finite action in $\Theta_m$ | Combines user, channel, and power decisions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | One subchannel: $\sum_{k\in\mathcal K}c_m^k(t)\leq1$ |
| C2 | One power level: $\sum_{j\in\mathcal I}p_m^j(t)\leq1$ |
| C3 | One served user: $\sum_{l\in\mathcal L}a_m^l(t)\leq1$ |
| C4 | QoS-qualified reward: $R_m(t)=\frac{W}{K}\log_2(1+\gamma_m(t))-\omega_mP_m(t)$ if $\gamma_m(t)\geq\bar\gamma_m$, and $R_m(t)=0$ otherwise |
| C5 | Local state: $s_m(t)=1$ if $\gamma_m(t)\geq\bar\gamma$ and $s_m(t)=0$ otherwise |

**Algorithm**: Let every UAV independently maintain a zero-initialized Q-table, choose $\theta_m$ with epsilon-greedy exploration, observe the binary QoS state and local reward, update $Q_m(s_m,\theta_m)$ with the one-step temporal-difference rule, and decrease the learning rate as $\alpha_t=1/((t+c_\alpha)\varphi_\alpha)$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cui et al. [x] studied dynamic user, subchannel, and discrete-power selection in multi-UAV downlink networks with predefined trajectories and no inter-UAV information exchange. They formulated a noncooperative stochastic game in which each UAV maximizes discounted throughput-minus-power reward subject to one-user, one-subchannel, one-power-level, and local QoS limits. Their independent-learning MARL algorithm used a binary SINR-threshold state, a zero-initialized Q-table, epsilon-greedy action selection, and a diminishing learning rate. Simulations reported that epsilon 0.5 gave the highest reward in the tested settings, while independent learning outperformed random selection but remained below complete-information Gale-Shapley matching in the reduced user-selection comparison.

## Problem and system model

Single-antenna UAVs follow predefined trajectories above ground users. Orthogonal subchannels may be reused by different UAVs, creating cochannel interference. Each UAV observes local CSI and whether its selected link meets an SINR target. Its reward is throughput minus a transmit-power cost when QoS is met and zero otherwise.

The repeated interaction is formulated as a non-cooperative [[stochastic-game]]. The objective is each UAV's discounted long-term reward, under one-user, one-subchannel, and one-power-level selection limits.

## Method

Every UAV independently runs zero-initialized [[multi-agent-q-learning|Q-learning]] with epsilon-greedy exploration and diminishing learning rates. Other learning UAVs are treated as part of the environment; there is no central critic, parameter sharing, or action/reward exchange. The paper invokes finite-state stochastic-approximation convergence, but simultaneous independent learners make the coupled environment non-stationary, so this does not establish convergence of the full game to a [[nash-equilibrium]].

## Key findings

- The tested settings use 100 m altitude, 75 kHz subchannels, 2 GHz carrier, three power levels up to 23 dBm, and a 3 dB SINR target.
- In the reduced two-UAV, user-selection-only comparison, complete-information Gale-Shapley matching achieves higher average reward than independent learning, while learning exceeds random selection.
- Among tested exploration settings, epsilon 0.5 performs best; this is scenario-specific.
- Faster UAV motion accumulates reward sooner but can lower final reward by leaving the service disk earlier.

## Limitations

Trajectories are fixed, the state is only a binary QoS indicator, and actions permit one user/subchannel/power level per slot. The model assumes every UAV can find a QoS-feasible user, omits propulsion and fixed processing power, and evaluates only simulations with narrow baselines. Nash equilibrium is defined but not demonstrably reached by the independent-learning algorithm.

## Relation to the corpus

This communications-only source is an early independent-learner counterpart to later deep multi-UAV controllers. It differs from CTDE and parameter-sharing designs by accepting non-stationarity in exchange for zero coordination signaling.

## Raw artifacts

- `raw/sources/Multi-Agent_Reinforcement_Learning-Based_Resource_Allocation_for_UAV_Networks/Multi-Agent_Reinforcement_Learning-Based_Resource_Allocation_for_UAV_Networks.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
