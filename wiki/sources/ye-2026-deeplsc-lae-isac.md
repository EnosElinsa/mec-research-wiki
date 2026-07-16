---
type: source
title: "Integrated Sensing and Communications for Low-Altitude Economy: A Deep Reinforcement Learning Approach"
authors: ["Xiaowen Ye", "Yuyi Mao", "Xianghao Yu", "Shu Sun", "Liqun Fu", "Jie Xu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3583950"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, low-altitude-economy, isac, deep-reinforcement-learning, ddpg, uav-trajectory-control]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[episodic-experience-replay]]"
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[jie-xu]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# Integrated Sensing and Communications for Low-Altitude Economy: A Deep Reinforcement Learning Approach

## Citation

Ye, X., Mao, Y., Yu, X., Sun, S., Fu, L., & Xu, J. (2026). *Integrated Sensing and Communications for Low-Altitude Economy: A Deep Reinforcement Learning Approach*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3583950.

## TL;DR

Models a terrestrial LAE ISAC system where a GBS communicates with authorized UAVs and senses an unauthorized mobile target. The goal is to maximize expected communication sum-rate over a flight period by jointly optimizing GBS beamforming and UAV trajectories under average sensing-SNR, flight-mission, collision-avoidance, and transmit-power constraints. The proposed **DeepLSC** controller is a DDPG-based DRL method with constrained noise exploration, hierarchical experience replay, and symmetric experience augmentation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna ground base station serves authorized UAVs while sensing an unauthorized moving target. Each authorized UAV must fly from a fixed origin to a fixed destination during a finite slotted mission.

**Problem & objective**: Problem (14) maximizes expected cumulative communication sum-rate, $\max_{\mathbf W_c,\mathbf W_s,\mathbf u}\mathbb E[\sum_{t=1}^{T}R_{\mathrm{total}}(t)]$, through joint communication beamforming, sensing beamforming, and UAV trajectory control.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beamforming | $\mathbf W_c(t)$ | complex continuous | GBS downlink beams for authorized UAVs |
| Sensing beamforming | $\mathbf W_s(t)$ | complex continuous | GBS probing beams for the target |
| UAV movement direction | $\mathbf a_u(t)$ | continuous angles | Per-slot headings that generate authorized-UAV trajectories |
| UAV trajectory | $\mathbf u_m(t)$ | continuous positions | Horizontal position of UAV $m$ in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1 | Constant-speed motion, $\|\mathbf u_m(t+1)-\mathbf u_m(t)\|_2=v_m\Delta_t$ |
| 2 | Every UAV starts at $\mathbf u_m^I$ and reaches $\mathbf u_m^F$ at slot $T$ |
| 3-4 | UAV-to-UAV and UAV-to-target distances remain at least $D_{\min}$ |
| 14c | Expected average target sensing SNR satisfies $\mathbb E[\frac1T\sum_t\mathrm{SNR}_{\mathrm{Tar}}(t)]\geq\Gamma_{\min}$ |
| 14d | Communication and sensing beam powers jointly remain below $P_{\max}$ |

**Algorithm**: DeepLSC converts the constrained flight-period problem into an episode MDP and uses DDPG for continuous beamforming and movement directions. Constrained noise exploration filters sampled actions toward power and mission feasibility, hierarchical replay trains on complete episodes, symmetric index permutations augment experience, and soft target updates stabilize the actor and critic.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ye et al. [x] considered terrestrial LAE ISAC in which a ground base station communicates with authorized UAVs and senses a mobile unauthorized target. They maximized expected flight-period communication sum-rate over communication beams, sensing beams, and UAV trajectories under sensing-SNR, mission, collision, and transmit-power constraints. DeepLSC combines a DDPG backbone with constrained exploration, episode-level replay, symmetric experience augmentation, and soft target updates. Across the reported two-to-five-UAV sweep, DeepLSC satisfied both the average sensing-SNR and flight-mission constraints while several ablations or actor-critic baselines violated at least one constraint. It exceeded constrained-experience-replay and weighted variants by more than 11.68% in sum-rate across the tested flight-period lengths. The method also retained an advantage in the reported twenty-UAV and twenty-antenna scenario.

## Problem framing

The GBS must support authorized UAVs and monitor an unknown target at the same time. Because target mobility is not assumed known in advance, the policy must make long-horizon trajectory/beamforming decisions from observed state rather than solving a deterministic planned trajectory.

## System model

- One GBS with transmit/receive antennas serves multiple single-antenna authorized UAVs.
- Authorized UAVs move from initial to final locations during a finite flight period, while the GBS senses an unauthorized low-altitude target.
- The objective is expected communication sum-rate, with constraints on average sensing SNR, UAV mission completion, inter-UAV collision avoidance, and maximum GBS transmit power.

## Method

- **Episode-task MDP.** The source names the long-horizon flight problem an episode task.
- **DeepLSC.** A DDPG backbone controls beamforming and UAV trajectory.
- **Constrained noise exploration.** A scaling factor and real-time UAV locations keep exploratory actions closer to feasible power, sensing, and flight regions.
- **Hierarchical experience replay.** All experiences generated within an episode jointly train the neural network, preserving episode-level temporal structure.
- **Symmetric experience augmentation.** Permuting indexes of symmetric variables enriches experience sets without changing the physical problem.

## Key findings

- For 2-5 UAVs, DeepLSC is reported to satisfy both average sensing-SNR and flight-mission constraints, while several ablations or actor-critic baselines violate at least one constraint in the larger cases.
- The paper reports DeepLSC-CER sum-rate gaps that grow with the number of UAVs, from 14.43 bps/Hz to 21.42 bps/Hz across the 2-5 UAV sweep.
- In a larger 20-UAV / 20-GBS-antenna scenario, DeepLSC remains better than the tested baselines, and the complexity is described as increasing linearly with the UAV count.
- Across flight-period sweeps, DeepLSC reports more than 11.68% sum-rate gain over constrained-experience-replay and weighted variants in all tested setups.

## Limitations / future work

The parse presents simulation evidence and algorithmic ablations rather than hardware or flight validation. The target model and propagation assumptions are those of the mathematical simulator; transfer to real LAE airspace is not directly tested.

## Relation to the corpus

This is a LAE-specific [[integrated-sensing-and-communication]] control source that turns sensing-aware UAV motion into a DRL episode task. It is the communication-sum-rate predecessor to [[ye-2026-meta-deepesc-lae-isac]], which keeps the same LAE ISAC flavor but shifts the objective to energy efficiency and adds meta-learning. Co-author [[jie-xu]] links it to the CUHK-Shenzhen ISAC cluster already represented by [[meng-2024-uav-isac-overview]], [[yao-2025-secure-isac-dual-eavesdropping]], and [[wen-2024-iscc-edge-ai]].

## Raw artifacts

- `raw/sources/Integrated Sensing and Communications for Low-Altitude Economy A Deep Reinforcement Learning Approach/Integrated Sensing and Communications for Low-Altitude Economy A Deep Reinforcement Learning Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
