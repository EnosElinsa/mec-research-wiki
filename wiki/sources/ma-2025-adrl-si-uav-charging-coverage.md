---
type: source
title: "Efficient Charging Coverage Strategy of UAV Based on Improved Deep Reinforcement Learning"
authors: ["Haixu Ma", "Wenbo Liu", "Guang Yang", "Huihui Sun", "Dongming Qu", "Hongfei Yang"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3556754"
venue: "IEEE Transactions on Vehicular Technology, 74(8)"
modeling_card: required
tags: [source, uav-charging, charging-coverage, fairness, ddpg, particle-swarm-optimization, constrained-pareto-dominance]
related:
  - "[[uav-charging-scheduling]]"
  - "[[jains-fairness-index]]"
  - "[[ddpg]]"
  - "[[particle-swarm-optimization]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[yang-2026-udi-docking-point-charging]]"
created: 2026-11-02
updated: 2026-11-02
---

# Efficient Charging Coverage Strategy of UAV Based on Improved Deep Reinforcement Learning

## Citation

Ma, H., Liu, W., Yang, G., Sun, H., Qu, D., & Yang, H. (2025). *Efficient Charging Coverage Strategy of UAV Based on Improved Deep Reinforcement Learning*. **IEEE Transactions on Vehicular Technology, 74**(8). DOI: 10.1109/TVT.2025.3556754.

## TL;DR

UAV base stations cover moving users and must return to a charging station before their energy runs out. ADRL-SI guides DDPG agents with multi-objective particle swarm optimization (MOPSO) under constrained Pareto dominance and adds a survival incentive that forces a low-energy UAV toward the station, so low-energy UAVs recharge near the station while high-energy UAVs serve edge users.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ UAV-BSs at positions $p_i=(p_{ix},p_{iy},p_{iz})$ serve $M$ randomly moving users in a 2-D area over $T$ slots. Coverage radius is $R=\xi p_z$, altitude lies in $[f_l,f_h]$, and a charging station sits at $S$. A user's coverage score is $c_m=T_m/T$ and fairness is Jain's index $f_c$.

**Problem & objective**: $P^*=\arg\max_P F$ with $F=\frac{f_c\sum_m c_m}{M f_I}$, where the scheduling index $f_I$ rewards sending UAVs with low residual energy and short distance to the station first.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV positions | $P=\{p_1,\dots,p_N\}$ | continuous, altitude in $[f_l,f_h]$ | Coverage deployment per slot |
| Movement per slot | $\triangle D_i$ | bounded by $d_{max}$ | Distance travelled by UAV $i$ in a slot |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Safety | All UAVs remain safe, $n_s=\sum_i\rho_i=N$ with $\rho_i=1$ if $e_i\ge\Upsilon e_{i,back}$. |
| Residual energy | $e_i=E_i$ minus energy spent on travelled distance. |
| Altitude | $p_{iz}\in[f_l,f_h]$, with connectivity distance $2f_h$. |

**Algorithm**: ADRL-SI. MOPSO with constrained Pareto dominance generates assisting actions whose use probability decays over training. DDPG actors and critics learn the deployment policy, and the survival-incentive mechanism triggers return to the station once residual energy falls below the threshold.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ma et al. [x] studied charging coverage, where multiple UAVs serving mobile users must adaptively recharge while maintaining service fairness and minimizing the replacement consumption of UAVs. They designed a multi-objective charging coverage problem based on the constrained Pareto dominance principle. They proposed an assisted deep reinforcement learning model based on a survival incentive, in which multi-objective particle swarm optimization assists different agents in learning and the survival incentive mechanism secures the UAVs with minimum residual energy. Simulation results show that the proposed method improves user service level, UAV energy efficiency, adaptive charging security, and system convergence compared with current DRL-based methods. For a coverage range ratio of 1.1, it improves the average coverage score, fairness index, and energy efficiency by 11.5%, 11.6%, and 33.3% over the earlier ADRL method.

## Problem framing

Round-trip charging stations are reliable but interrupt service and cost energy when distant UAVs return. The paper therefore wants replacement to happen near the station, with high-energy UAVs taking over marginal users.

## System model

- 200 users in a 200-unit square area moving with step 0.4; the station is at the midpoint of one side.
- Maximum initial energy is twice the maximum return energy, with heterogeneous initial energies.
- Charge factor $\Upsilon=1.5$ and altitudes $f_l=20$, $f_h=40$ units.

## Method

Actor and critic networks have hidden layers of 400, 200, 100, 64, and 32 units with ReLU. MOPSO uses 100 particles. The survival-incentive check adds only a residual-energy condition, so complexity stays close to ADRL.

## Key findings

- At coverage range ratio 1.1, ADRL-SI reaches average coverage score 0.29, fairness 0.48, and energy efficiency 0.08, versus 0.26, 0.43, and 0.06 for ADRL.
- ADRL-SI also keeps the most UAVs in the safe-energy state among the eight compared methods.
- ADRL-SI, ADRL, and PER-DQN consistently lead, which the authors attribute to higher-quality training experience.

## Limitations / future work

Communication and relaying details are outside the model. The authors plan more advanced DRL models and integration with 5G or edge computing.

## Relation to the corpus

A learned station-return policy within [[uav-charging-scheduling]] that weights [[jains-fairness-index]], compared with infrastructure-based charging in [[yang-2026-udi-docking-point-charging]] and continuous service in [[persistent-emergency-uav-swarm-service]].

## Raw artifacts

- Parse: `raw/sources/Efficient_Charging_Coverage_Strategy_of_UAV_Based_on_Improved_Deep_Reinforcement_Learning/Efficient_Charging_Coverage_Strategy_of_UAV_Based_on_Improved_Deep_Reinforcement_Learning.md`
- Origin PDF and extracted figures are in the same folder.
