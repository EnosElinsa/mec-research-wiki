---
type: source
title: "Hammurabi: Establish Cooperative Order From Pre-Trained Policies in Multi-UAV Networks"
authors: ["Dezhi Chen", "Hongchuan He", "Qi Qi", "Jingyu Wang", "Rongxin Han", "Bo He", "Zirui Zhuang", "Qianlong Fu", "Jianxin Liao", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TPDS.2026.3654605"
venue: "IEEE Transactions on Parallel and Distributed Systems (IEEE TPDS)"
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
updated: 2026-07-13
---

# Hammurabi: Establish Cooperative Order From Pre-Trained Policies in Multi-UAV Networks

## Citation

Chen, D., He, H., Qi, Q., Wang, J., Han, R., He, B., Zhuang, Z., Fu, Q., Liao, J., & Han, Z. (2026). *Hammurabi: Establish Cooperative Order From Pre-Trained Policies in Multi-UAV Networks*. **IEEE Transactions on Parallel and Distributed Systems**, 37(3), 744-761. DOI: 10.1109/TPDS.2026.3654605.

*Metadata note:* The local parse supplies the DOI but not the final issue record; the exact-title Crossref DOI record supplies volume 37, issue 3, and pages 744-761.

## TL;DR

Diagnoses whether rule-pretrained multi-UAV policies behave cooperatively or defectively, classifies their interaction through a Markov social dilemma and Schelling diagram, then fine-tunes shared MARL policies with inequality-aversion reward shaping.

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
