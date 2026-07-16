---
type: source
title: "Joint Trajectory Planning and Channel Selection for AoI Minimization in Multi-UAV-Assisted IoT Networks"
authors: ["Zhuo Lu", "Qihui Wu", "Ziye Jia", "Chen Fei", "Jianzhao Zhang", "Fuhui Zhou", "Kai-Kit Wong"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3658601"
venue: "IEEE Transactions on Wireless Communications (TWC)"
tags: [source, age-of-information, multi-uav, channel-selection, multi-agent-reinforcement-learning]
related:
  - "[[age-of-information]]"
  - "[[soft-actor-critic]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-data-collection]]"
  - "[[qihui-wu]]"
  - "[[ziye-jia]]"
  - "[[fuhui-zhou]]"
  - "[[kai-kit-wong]]"
modeling_card: required
created: 2026-07-13
updated: 2026-07-16
---

# Joint Trajectory Planning and Channel Selection for AoI Minimization in Multi-UAV-Assisted IoT Networks

## Citation

Lu, Z., Wu, Q., Jia, Z., Fei, C., Zhang, J., Zhou, F., & Wong, K.-K. (2026). Joint trajectory planning and channel selection for AoI minimization in multi-UAV-assisted IoT networks. *IEEE Transactions on Wireless Communications, 25*, 11161-11175. https://doi.org/10.1109/TWC.2026.3658601

## TL;DR

Multiple UAV base stations jointly choose 3-D motion and wireless channels while collecting IoT uploads in the presence of ground jammers and same-channel UAV interference. ITPCS-DC uses SAC-style maximum-entropy multi-agent actor-critic training to reduce a transmission-duration freshness proxy, path length, switching cost, and collision risk.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $U$ rotary-wing UAV base stations collect uploads from $G$ IoT devices over $C<U$ channels in the presence of $J$ ground jammers; uplink and downlink share each selected channel through TDMA, with probabilistic LoS/NLoS path loss and interference from co-channel UAVs and jammers.

**Problem & objective**: Minimize the paper's upload-duration freshness proxy, $\min_{\{u_{i,j}(t)\},\{c_{i,j}(t)\}}\sum_{i\in U}\sum_{j\in G}\sum_t\mathcal A_{i,j}(t)$, where $\mathcal A_{i,j}(t)=Q_{j,i}(t)/R_{j,i}(t)$ and $Q_{j,i}(t+1)=Q_{j,i}(t)-R_{j,i}(t)\delta_t$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $u_{i,j}(t)$ | continuous 3-D position | Position of UAV $i$ while serving IoT device $j$ |
| Channel choice | $c_{i,j}(t)$ | discrete, nonzero channel index | Channel selected by UAV $i$ for device $j$ |
| Velocity action | $a_i^p(t)$ | continuous 3-D action | Actor output controlling UAV motion |
| Switching action | $a_i^c(t)$ | discrete action | Actor output controlling channel switching |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Initial positions are fixed, $u_{i,j}(0)=u_{i,j}^0$. |
| C2 | Constant-speed motion is enforced, $\|u_{i,j}(t+1)-u_{i,j}(t)\|=V\delta_t$. |
| C3 | UAV separation is safe, $\|u_{i,j}(t)-u_{n,l}(t)\|\geq\delta_d$. |
| C4 | Every selected channel is valid and nonzero, $c_{i,j}(t)\neq0$, and successful uploads satisfy the SINR threshold $S_{j,i}(t)\geq\kappa_{g,u}$. |

**Algorithm**: Model the problem as a multi-agent MDP, let each decentralized actor output velocity and channel actions, train centralized value and Q networks with replay and SAC-style entropy regularization, apply soft target updates, and execute the learned policies independently at each UAV.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lu et al. [x] studied multi-UAV IoT data collection with ground jammers, same-channel UAV interference, and fewer channels than UAVs. They formulated joint 3-D trajectory and channel-selection optimization to minimize an upload-duration freshness proxy based on remaining data divided by instantaneous rate, while penalizing distance, switching, and collision risk. They modeled the problem as a multi-agent MDP and solved it with ITPCS-DC, using decentralized actors, centralized value and Q networks, replay, entropy regularization, and soft target updates. In simulations, ITPCS-DC achieved the lowest reported proxy AoI, trajectory length, and switching cost, and its average reward was up to 13.17% higher than the compared methods.

## Problem and system model

The model contains multiple rotary-wing UAVs, ground IoT devices, jammers, and fewer channels than UAVs. Downlink control and uplink data share each selected channel through TDMA. Probabilistic LoS/NLoS path loss is used without small-scale fading.

Although the paper first introduces conventional elapsed-time [[age-of-information]], its optimization evaluates `remaining upload volume / instantaneous rate`. This is a transmission-duration freshness proxy, not a packet-generation and reception-age recursion.

## Method

Each UAV is one agent. Observations contain all UAV, device, and jammer positions; peer/jammer channel choices; and remaining upload volumes, supplied through GPS and information exchange. Actions combine continuous 3-D velocity with an underspecified switch/no-switch channel decision.

ITPCS-DC uses decentralized actors, centralized value/Q networks during training, replay, entropy-regularized policies, and soft target updates. It is best described as SAC-style maximum-entropy actor-critic rather than canonical MASAC because the architecture does not use the wiki's twin-Q MASAC structure.

## Key findings

- In the three-UAV/three-device/one-jammer simulation, the last-10,000-episode average reward is -87,728.80 versus -92,686 for MADDPG, -96,593.66 for MAPPO, and -101,037.52 for DDPG.
- At 10 Mbit per device, reported freshness-proxy values are 463, 464, 467, and 472 respectively; the parse gives no unit.
- Reported channel-switching cost reductions are 16.11%, 26.85%, and 41.77% against MADDPG, MAPPO, and DDPG.
- Tests with three to six UAVs favor ITPCS-DC, but do not establish large-swarm scalability.

## Limitations

The channel-action mapping does not explain downward switching, wraparound, or arbitrary choice among channels. The actor's stated softmax output is not reconciled with signed continuous velocity. "Decentralized" execution still depends on globally exchanged state. Interference equations in the parse omit an explicit same-channel indicator, and path length substitutes for propulsion/battery energy. Evidence is simulation-only with fixed seeds and no repeated-seed variance or field validation.

## Relation to the corpus

This source connects [[age-of-information]], anti-jamming channel selection, and [[uav-trajectory-control]]. It differs from [[shi-2025-aoi-energy-replenishment-multiuav]] by omitting battery dynamics and from [[chen-2026-maddpg-uav-swarm-antijamming]] by centering the upload-time freshness proxy and channel switching.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_Planning_and_Channel_Selection_for_AoI_Minimization_in_Multi-UAV-Assisted_IoT_Networks/Joint_Trajectory_Planning_and_Channel_Selection_for_AoI_Minimization_in_Multi-UAV-Assisted_IoT_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
