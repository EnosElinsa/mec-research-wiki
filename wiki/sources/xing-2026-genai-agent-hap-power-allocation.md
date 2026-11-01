---
type: source
title: "Generative AI Agent Empowered Power Allocation for HAP Propulsion and Communication Systems"
authors: ["Xiaoyu Xing", "Dingyi Lu", "Peng Yang", "Zehui Xiong", "Xianbin Cao", "Tony Q. S. Quek"]
year: 2026
url: "https://doi.org/10.1109/TCCN.2026.3683194"
venue: "IEEE Transactions on Cognitive Communications and Networking, 12"
modeling_card: required
tags: [source, high-altitude-platform-station, propulsion-power, beamforming, energy-efficiency, generative-ai, llm-agent]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hap-solar-propulsion-energy-balance]]"
  - "[[llm-assisted-resource-allocation]]"
  - "[[generative-ai-for-mec]]"
  - "[[zehui-xiong]]"
  - "[[tony-q-s-quek]]"
created: 2026-11-02
updated: 2026-11-02
---

# Generative AI Agent Empowered Power Allocation for HAP Propulsion and Communication Systems

## Citation

Xing, X., Lu, D., Yang, P., Xiong, Z., Cao, X., & Quek, T. Q. S. (2026). *Generative AI Agent Empowered Power Allocation for HAP Propulsion and Communication Systems*. **IEEE Transactions on Cognitive Communications and Networking, 12**. DOI: 10.1109/TCCN.2026.3683194. Part of the work was presented at the 2025 IEEE/CIC International Conference on Communications in China.

## TL;DR

A HAP's limited energy is split between propulsion and communication, and surrogate propulsion models that ignore hull-propeller interference misjudge the communication budget. Guided by an interactive generative AI agent, the authors build a propulsion model including that interference, then maximize a weighted sum of energy efficiency and QoS satisfaction ratio through beamforming with the Q3E algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An airship-type HAP serves $K$ ground users with multi-antenna downlink beams $\mathbf b_k$ over bandwidth $B_w$. Total power covers propulsion, modeled with hull-propeller aerodynamic interference, and communication power $P_{\mathrm{tot}}$. Rates use expected SINR under the channel model, upper-bounded with Jensen's inequality.

**Problem & objective**: $\mathcal P$: $\max_{\{\mathbf b_k\},\mathcal Q}\ \omega EE+(1-\omega)\frac{|\mathcal Q|}{|K|}$, weighting energy efficiency against the fraction of QoS-satisfied users.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Beamformers | $\mathbf b_k$ | complex vectors | Downlink beam for user $k$ |
| Satisfied set | $\mathcal Q$ | subset of users | Users whose QoS requirement is met |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (23b) | QoS for satisfied users, $R_k\ge r_k$ for $k\in\mathcal Q$. |
| (23c) | $\mathcal Q\subseteq K$. |
| (23d) | Communication power budget, $\sum_k\lVert\mathbf b_k\rVert_2^2\le P_{\mathrm{tot}}$. |

**Algorithm**: The generative AI agent assists in deriving the propulsion power model and formulating the problem. Q3E replaces rates with Jensen upper bounds and trains an artificial neural network under the constraints without supervised datasets to output beamformers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xing et al. [x] studied power allocation for high altitude platforms, whose limited energy must be split between propulsion and communications. Noting that most prior HAP studies ignore propulsion power or rely on surrogates that miss hull-propeller interference, they designed an interactive generative AI-empowered HAP power allocation agent. With the agent's assistance, they developed a propulsion power consumption model that accounts for aerodynamic interference between the hull and the propeller, and formulated a beamforming problem that improves user QoS and the energy efficiency of the HAP communication system. A QoS-enhanced energy-efficient beamforming algorithm was proposed to solve the problem. Simulation results show that the propulsion model reduces the average deviation by 84.3% compared with a benchmark model and that the beamforming algorithm achieves the highest QoS satisfaction ratio among the evaluated baselines.

## Problem framing

Propulsion dominates HAP energy use, so an inaccurate propulsion model distorts the communication budget and the beamforming that depends on it. Aerodynamics, propulsion efficiency, and communication performance are therefore coupled.

## System model

- Propulsion power derives from aerodynamic principles and numerical analysis of hull-propeller interference.
- Communication power is optimized under a fixed budget left after propulsion.

## Method

Rates are approximated with Jensen's inequality, and a constrained neural network training procedure solves the nonconvex beamforming problem.

## Key findings

- The propulsion model's maximum deviation stays below 6%, and within 5% above 3 m/s, compared with over 20% for an earlier model.
- At $V_0=25$ m/s, the model error falls from 8367.3 W to 85.32 W.
- Q3E is about 35% to 45% higher in QoS satisfaction at 90 to 150 W and about 8% to 10% higher at 300 W or above, while a sum-rate baseline plateaus near 66%.

## Limitations / future work

The evaluation concerns one HAP and one hull-propeller configuration.

## Relation to the corpus

Feeds a refined propulsion term into [[hap-solar-propulsion-energy-balance]] and illustrates [[llm-assisted-resource-allocation]] in a [[high-altitude-platform-station]] setting.

## Raw artifacts

- Parse: `raw/sources/Generative_AI_Agent_Empowered_Power_Allocation_for_HAP_Propulsion_and_Communication_Systems/Generative_AI_Agent_Empowered_Power_Allocation_for_HAP_Propulsion_and_Communication_Systems.md`
- Origin PDF and extracted figures are in the same folder.
