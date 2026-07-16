---
type: source
title: "Hammurabi: Establish Cooperative Order From Pre-Trained Policies in Multi-UAV Networks"
authors: ["Dezhi Chen", "Hongchuan He", "Qi Qi", "Jingyu Wang", "Rongxin Han", "Bo He", "Zirui Zhuang", "Qianlong Fu", "Jianxin Liao", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TPDS.2026.3654605"
venue: "IEEE Transactions on Parallel and Distributed Systems (IEEE TPDS)"
modeling_card: required
tags: [source, multi-uav, cooperative-marl, pretrained-policy, markov-social-dilemma, inequality-aversion, area-coverage]
related:
  - "[[pretrained-policy-cooperation-shaping]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[jains-fairness-index]]"
  - "[[parameter-sharing-marl]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[qi-qi]]"
  - "[[zhu-han]]"
created: 2026-07-13
updated: 2026-07-16
---

# Hammurabi: Establish Cooperative Order From Pre-Trained Policies in Multi-UAV Networks

## Citation

Chen, D., He, H., Qi, Q., Wang, J., Han, R., He, B., Zhuang, Z., Fu, Q., Liao, J., & Han, Z. (2026). *Hammurabi: Establish Cooperative Order From Pre-Trained Policies in Multi-UAV Networks*. **IEEE Transactions on Parallel and Distributed Systems**, 37(3), 744-761. DOI: 10.1109/TPDS.2026.3654605.

*Metadata note:* The local parse supplies the DOI but not the final issue record; the exact-title Crossref DOI record supplies volume 37, issue 3, and pages 744-761.

## TL;DR

Diagnoses whether rule-pretrained multi-UAV policies behave cooperatively or defectively, classifies their interaction through a Markov social dilemma and Schelling diagram, then fine-tunes shared MARL policies with inequality-aversion reward shaping.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ UAVs provide communication coverage over $K$ points of interest (PoIs) during $T$ time slots. Each UAV observes nearby PoIs and neighboring UAVs, chooses a flight direction and normalized speed, and spends rotary-wing propulsion energy while covering users.

**Problem & objective**: The area-coverage control seeks to maximize coverage and fairness while improving energy efficiency, summarized by $\max(\bar c_T,f_T,\zeta_T)$ where $\bar c_T$ is average PoI coverage, $f_T$ is the coverage fairness index, and $\zeta_T=f_T\bar c_T/\Delta E_T$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV flight direction | $\omega_{t,i}$ | continuous, $(0,2\pi]$ | Direction selected by UAV $i$ at slot $t$ |
| UAV normalized speed | $v_{t,i}$ | continuous, $[0,1]$ | Speed fraction of the maximum UAV speed |
| Shared policy | $\pi_i$ | stochastic policy | Mapping from local observations to movement actions |
| Reward mechanism | $r_{I,t,i}$ | real-valued | Inequality-aversion reward used to shape cooperation |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Flight speed is bounded by the platform maximum: $0\le v_{t,i}\le v_{\max}$. |
| C2 | PoI coverage is binary per slot: $c_{t,k}=1$ only when a UAV covers PoI $k$ and its channel is active. |
| C3 | Coverage fairness is evaluated over all PoIs: $f_T=\frac{(\sum_k c_k)^2}{K\sum_k c_k^2}$. |
| C4 | Rotary-wing energy is bounded over the mission: $\int_0^T(P_F(v(t))+P_H+P_C)\,dt\le E_{\mathrm{limit}}$. |
| C5 | UAVs start from the access point and return after the coverage mission. |

**Algorithm**: Generate initial policies from ACS-First or F-First expert trajectories, pre-train a shared policy, use a Schelling diagram to diagnose public-goods-game behavior, construct inequality-aversion rewards from accumulated agent returns, and continue DDPG, SAC, TD3, or PPO training toward a cooperative Nash equilibrium.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied multi-UAV area coverage for intelligent transportation, where each UAV selects movement actions to balance PoI coverage, fairness, and propulsion energy. They defined coverage and fairness indices together with an energy-efficiency objective and constrained speed, mission energy, and start-return operation. Hammurabi pre-trains shared policies from expert trajectories, diagnoses social-dilemma behavior with Schelling diagrams, and adds inequality-aversion rewards before continuing standard DRL updates. In the reported six-UAV case, the mechanism improved energy efficiency by 25.89%, average coverage score by 16.16%, and fairness by 16.64% over the stated baselines.

## Problem framing

System-level rewards align a fleet but give weak individual credit, while agent-level rewards can encourage free-riding. Rule demonstrations solve cold start but impose the demonstrator's cooperative or selfish bias. Hammurabi treats that bias as a game-structure problem rather than assuming pretraining is always beneficial.

## System model

- Homogeneous UAVs cover PoIs over a finite mission, starting and ending at an access point with local observation and communication ranges.
- Actions are continuous heading and speed; reward metrics combine coverage, Jain-style coverage fairness, and rotary-wing energy.
- The default simulation has six UAVs, 100 PoIs, 256 slots, 250 m coverage radius, and 500 m inter-UAV communication range.
- Centralized training produces a shared policy deployed for local inference on each UAV.

## Method

[[pretrained-policy-cooperation-shaping|Hammurabi]] pretrains from ACS-First and F-First rule trajectories. It labels them relatively defect-oriented and cooperative, constructs Schelling diagrams over policy mixtures, and classifies the six-UAV interaction as following a public-goods-game trend.

Inequality-aversion shaping penalizes advantageous and disadvantageous differences in cumulative agent reward before fine-tuning parameter-shared DDPG, SAC, TD3, or PPO policies. The theory frames a finite-state Nash-Q update under GLIE, infinite visitation, bounded rewards, and stage games whose equilibria are global optima or saddle points.

## Key findings

- Against ACS-First, IA-based DRL reports `25.89%` higher energy efficiency, `16.16%` higher average coverage, and `16.64%` higher fairness.
- The full table is mixed: fairness is `9.92%` below F-First and `2.67%` below F-First pretraining, so the method is not better than every baseline on every metric.
- The paper reports benefit across four DRL backbones and tests changed fleet size, coverage radius, PoI count, and irregular topology, without quantitative uncertainty or a generalization gap.
- Its Nash convergence theorem does not directly prove convergence of the neural continuous-action actor-critic implementations.

## Limitations / parse caveats

The evaluation is simulation-only and lacks code, simulator, seeds, hardware, run counts, and complete training hyperparameters. Cooperative/defective policy labeling remains manual. The theorem assumes finite states and infinite visitation, while the application uses continuous ungridded observations/actions and only approximate GLIE. Baseline citations, energy accounting, the ACS/F-First footnote, topology dimensions, and several formulas are inconsistent or parse-damaged.

## Relation to the corpus

This source deepens [[expert-guided-warm-start-rl]] by asking what social behavior a demonstrator transfers, then selecting reward shaping from the diagnosed game. It is useful for multi-agent credit assignment and cooperative aerial control, but it does not model MEC task offloading or compute allocation.

## Raw artifacts

- Parse: `raw/sources/Hammurabi_Establish_Cooperative_Order_From_Pre-Trained_Policies_in_Multi-UAV_Networks/Hammurabi_Establish_Cooperative_Order_From_Pre-Trained_Policies_in_Multi-UAV_Networks.md`
- Origin PDF: `raw/sources/Hammurabi_Establish_Cooperative_Order_From_Pre-Trained_Policies_in_Multi-UAV_Networks/Hammurabi_Establish_Cooperative_Order_From_Pre-Trained_Policies_in_Multi-UAV_Networks.pdf`
- Figures: `raw/sources/Hammurabi_Establish_Cooperative_Order_From_Pre-Trained_Policies_in_Multi-UAV_Networks/images/`
