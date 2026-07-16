---
type: source
title: "Dynamic UAV Deployment for Differentiated Services: A Multi-Agent Imitation Learning Based Approach"
authors: ["Xiaojie Wang", "Zhaolong Ning", "Song Guo", "Miaowen Wen", "Lei Guo", "H. Vincent Poor"]
year: 2023
url: "https://doi.org/10.1109/TMC.2021.3116236"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 22, no. 4, pp. 2131-2146"
modeling_card: required
tags: [source, multi-uav, uav-deployment, differentiated-services, imitation-learning, opponent-modeling, nash-equilibrium]
related:
  - "[[multi-agent-imitation-learning]]"
  - "[[differentiated-uav-service-market]]"
  - "[[nash-equilibrium]]"
  - "[[stochastic-game]]"
  - "[[generative-adversarial-network]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[maddpg]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[zhaolong-ning]]"
  - "[[xiaojie-wang]]"
  - "[[lei-guo]]"
  - "[[ning-2023-madrl-uav-trajectory-differentiated-services]]"
  - "[[wang-2025-ctmig-task-migration-uav]]"
created: 2026-07-13
updated: 2026-07-16
---

# Dynamic UAV Deployment for Differentiated Services: A Multi-Agent Imitation Learning Based Approach

## Citation

Wang, X., Ning, Z., Guo, S., Wen, M., Guo, L., & Poor, H. V. (2023). *Dynamic UAV Deployment for Differentiated Services: A Multi-Agent Imitation Learning Based Approach*. **IEEE Transactions on Mobile Computing**, 22(4), 2131-2146. DOI: 10.1109/TMC.2021.3116236.

## TL;DR

Models competing UAV owners as a [[differentiated-uav-service-market]] and trains a multi-agent imitation-learning policy from full-information expert demonstrations. Each owner predicts opponents from local observations, changes its service quantity and UAV count, and seeks long-run profit without exchanging actual opponent policies.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $H$ hotspots receive users with differentiated service preferences from $K$ competing UAV owners. Owner $k$ offers quantity $q_{hk}(t)$ at price $p_k(t)$, with each UAV supplying capability $b_k$ and incurring deployment, hovering, and service costs.

**Problem & objective**: User utility is $P_1:\max_{q_{hk}}u(t)=\sum_{h,k}f_{hk}(t)q_{hk}(t)^{\alpha}$, while each owner solves $P_2:\max_{q_{hk},p_k}\Gamma_k=\sum_{t,h}(p_kq_{hk}-c_{hk})$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Service quantity | $q_{hk}(t)$ | nonnegative continuous | Capacity owner $k$ offers in hotspot $h$ |
| Service price | $p_k(t)$ | nonnegative continuous | Price charged for owner $k$ service |
| Deployment count | $\lceil q_{hk}(t)/b_k\rceil$ | integer derived | Number of UAVs needed for the offered quantity |
| Online action | $\Delta q_{hk}(t)$ | bounded continuous | Increment or reduction in offered quantity |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Hotspot budget: $\sum_kp_k(t)q_{hk}(t)\le e_h$ |
| C2 | Differentiation parameter: $0<\alpha<1$ |
| C3 | Quantity nonnegativity: $q_{hk}(t)\ge0$ |
| C4 | Action bound: $-\alpha e_h/(4A_k)\le\Delta q_{hk}(t)\le\alpha e_h/(4A_k)$ |
| C5 | Owner cost: $c_{hk}(t)=(g_0+g_s)\lceil q_{hk}(t)/b_k\rceil+g_cq_{hk}(t)$ |

**Algorithm**: Derive full-information Nash-equilibrium quantities as expert demonstrations, then train decentralized MILU policies with CNN and GAN imitation, an opponent-action predictor, and a policy-gradient/value-network update under partial observations.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] modeled differentiated UAV services as a competition among owners that choose service quantities and prices across user hotspots. The formulation maximizes CES-based user utility under hotspot budgets while each owner maximizes long-term revenue minus deployment, hovering, and service costs. Full-information analysis supplies Nash-equilibrium expert actions, and the MILU learner imitates those actions with decentralized CNN, GAN, opponent-model, and policy-gradient networks. Experiments reported higher user utility and owner profit with faster convergence than multi-agent DRL and optimization baselines, while the framework retains partial-observation operation.

## Problem

Several UAV owners may sell substitutable computation or content-delivery services in the same hotspots, with different capabilities, costs, and prices. User demand and preferences vary over time, while each owner lacks its competitors' policies. The decision is how many UAVs and how much service each owner should provide while users choose among differentiated substitutes under a budget.

## System model

- A network operator observes system demand, while multiple UAV owners independently control sufficient rechargeable/replaced UAV inventories across non-overlapping hotspots.
- Same-owner UAVs in a hotspot form a load-balancing mesh/cloudlet; different owners' UAVs do not communicate. Users choose the nearest UAV offering their preferred service over OFDM.
- Constant-elasticity-of-substitution utility captures user preferences across owners. Users maximize utility under hotspot budgets; each owner maximizes infinite-horizon revenue minus deployment, hover-energy, and service-energy costs.
- A full-information game yields quantity/price equilibrium conditions. The incomplete-information version is a Markov game with local owner observations, service-quantity increments as actions, and owner profit as reward.

## Method

Full-information oracle owners first generate historical expert trajectories containing local observations, each owner's action, and opponents' actions. Each learning owner has a discriminator, opponent model, policy network, and value network. Adversarial occupancy matching distinguishes expert from learned behavior; the opponent model predicts other owners' actions; and entropy-regularized actor-critic updates train the local policy.

During execution, an owner observes locally, predicts opponents, updates its service quantity, and converts that quantity into a UAV count. Actual opponent policies are not exchanged, but the broader pipeline still relies on the network operator for global demand or preference-density estimates.

## Key findings

- At user budgets 2 and 4, the average UAV counts per hotspot are respectively `11/8/5/3` and `22/16/9/4` for Expert/MILU/MDDPG/OMD.
- At substitutability values `0.3` and `0.6`, average user utilities are `0.344/0.318/0.174/0.037` and `9.27/7.93/3.561/1.01` in the same order.
- MILU's average-profit gap to the expert is reported near `10%`; at 4000 iterations, the four policies report `232521/209246/168455/149542`, although units and the distinction between average and accumulated profit are unclear.
- In the three-owner case, Jain-style profit fairness at 2000 iterations is `0.996/0.979/0.74/0.57`. MILU converges in about 700 iterations with two owners and 900 with three, compared with 1200 for MDDPG and 1900 for OMD in the two-owner case.

## Limitations / parse caveats

Evidence is simulation rather than UAV deployment: a Hangzhou map parameterizes hotspot geography, while a 19-video/five-quality trace set parameterizes differentiated video-service qualities. The operator's global demand information qualifies the paper's fully decentralized wording. The parse describes fully connected networks despite abstract-level CNN claims, omits 3-D propagation and trajectory control, and contains inconsistent utility normalizations, average-versus-accumulated profit labels, and damaged theorem/equation symbols. The final publication record is absent from the parse and was verified by exact title through Crossref.

## Relation to the corpus

This is the service-quantity/deployment predecessor to [[ning-2023-madrl-uav-trajectory-differentiated-services]], which instead controls free-space trajectories under changing service preferences. Its [[multi-agent-imitation-learning]] design also complements [[wang-2025-ctmig-task-migration-uav]], where GAIL refines a task-migration policy, but MILU adds strategic opponent prediction and expert equilibrium actions.

## Raw artifacts

- Parse: `raw/sources/Dynamic_UAV_Deployment_for_Differentiated_Services_A_Multi-Agent_Imitation_Learning_Based_Approach/Dynamic_UAV_Deployment_for_Differentiated_Services_A_Multi-Agent_Imitation_Learning_Based_Approach.md`
- Origin PDF: `raw/sources/Dynamic_UAV_Deployment_for_Differentiated_Services_A_Multi-Agent_Imitation_Learning_Based_Approach/Dynamic_UAV_Deployment_for_Differentiated_Services_A_Multi-Agent_Imitation_Learning_Based_Approach.pdf`
- Figures: `raw/sources/Dynamic_UAV_Deployment_for_Differentiated_Services_A_Multi-Agent_Imitation_Learning_Based_Approach/images/`
