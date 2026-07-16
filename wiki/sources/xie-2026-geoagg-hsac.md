---
type: source
title: "GeoAgg-HSAC: An RL-Based Framework for Trajectory and Resource Optimization in Mountainous UAV Integrated Localization and Communication Networks"
authors: ["Yaqi Xie", "Li Wang", "Zheng Chang", "Lianming Xu", "Suzhi Bi", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3625295"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, joint-localization-communication, mountainous-uav, graph-contrastive-learning, hybrid-action-sac, terrain-aware-control, emergency-network]
related:
  - "[[terrain-occlusion-aware-graph-state-aggregation]]"
  - "[[joint-localization-and-communication]]"
  - "[[terrain-aware-channel-model]]"
  - "[[graph-neural-network]]"
  - "[[hybrid-action-decision-making]]"
  - "[[soft-actor-critic]]"
  - "[[uav-trajectory-control]]"
  - "[[li-wang]]"
  - "[[lianming-xu]]"
  - "[[zheng-chang]]"
  - "[[zhu-han]]"
created: 2026-07-13
updated: 2026-07-16
---

# GeoAgg-HSAC: An RL-Based Framework for Trajectory and Resource Optimization in Mountainous UAV Integrated Localization and Communication Networks

## Citation

Xie, Y., Wang, L., Chang, Z., Xu, L., Bi, S., & Han, Z. (2026). *GeoAgg-HSAC: An RL-Based Framework for Trajectory and Resource Optimization in Mountainous UAV Integrated Localization and Communication Networks*. **IEEE Transactions on Wireless Communications**, 25, 6507-6522. DOI: 10.1109/TWC.2025.3625295.

## TL;DR

Uses terrain-induced LoS/NLoS patterns to pretrain a graph state encoder, then applies hybrid-action SAC to jointly control multi-UAV 3-D motion, transmit power, and user association for mountainous localization and downlink communication.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAV base stations provide two-way-ranging localization and TDMA downlink service to moving users in mountainous terrain, where occlusion determines LoS availability, channel gain, and localization geometry.

**Problem & objective**: The online mixed-integer control problem maximizes combined communication and localization utility, $\max_{\mathbf v,\mathbf p,\boldsymbol\beta}\frac{1}{T}\sum_t[\bar C_t+\lambda\bar L_t-(\delta_t^q+\delta_t^c+\delta_t^l+\delta_t^e)]$, with penalties for violated safety and service constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV velocity | $\mathbf v_{k,t}$ | Continuous 3-D vector | Move UAV $k$ during the control phase |
| Transmit power | $p_{k,t}^{trans}$ | Continuous, $[P_{\min},P_{\max}]$ | Allocate UAV downlink power |
| User association | $\beta_{i,k,t}$ | Binary, $\{0,1\}$ | Assign user $i$ to UAV $k$ |
| Next UAV position | $\mathbf q_{k,t+1}$ | Continuous above terrain | Position induced by the velocity action |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Per-cycle motion satisfies $\lVert\mathbf q_{k,t+1}-\mathbf q_{k,t}\rVert\leq V_{\max}^UT^{ctrl}$ |
| C2 | UAVs maintain separation and remain in $\Theta=\{(x,y,z):z>h(x,y)\}$ |
| C3 | Propulsion and transmission use no more than the available UAV energy |
| C4 | Each user has one serving UAV, $\sum_k\beta_{i,k,t}=1$ |
| C5 | Power, minimum communication rate, and localization-quality thresholds are respected |

**Algorithm**: GeoAgg pretrains a two-layer BiGAT and Set2Set graph encoder with contrastive learning on terrain-occlusion patterns, then HSAC uses Gaussian continuous heads and Gumbel-Softmax association heads with twin critics, replay, and expert demonstrations.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xie et al. [x] addressed joint UAV trajectory, transmit-power, and user-association control for localization and downlink communication in mountainous terrain. Their objective combines average communication rate and inverse-GDOP localization utility under motion, separation, energy, association, power, rate, localization, and terrain-clearance constraints. GeoAgg maps states with similar terrain occlusions into compact graph embeddings, and HSAC handles the continuous flight and power actions together with discrete associations. The reported simulations show faster convergence, higher average communication rates, and lower GDOP than SAC, PADDPG, and GeoAgg-PDQN in the reconstructed mountain environment.

## Problem framing

Mountain disasters can disable both terrestrial communications and GNSS. A UAV network can restore downlink coverage and provide ranging, but localization favors multiple geometrically diverse LoS measurements while communication, power, interference, flight safety, and terrain clearance compete for the same aerial resources. The resulting continuous-discrete online problem is difficult for conventional optimization and sample-inefficient for unstructured RL.

## System model

- Multiple UAV base stations serve mobile ground users over repeated localization, communication, and control phases; the aircraft are modeled with rotary-wing propulsion energy.
- Two-way ranging supplies distance measurements. At least three valid LoS links enter a GDOP-based localization utility, and a limited history of measurements can be reused.
- UAVs share spectrum, serve associated users through TDMA, and create inter-UAV interference.
- The centralized controller observes estimated positions, LoS states, channel gains, ranging-link counts, and powers, then chooses 3-D velocities, powers, and discrete associations.
- A reconstructed mountain map, ray tracing, and measured air-to-ground gains form the BUPT-UAV-mountain simulation environment.

## Method

[[terrain-occlusion-aware-graph-state-aggregation|GeoAgg]] builds a heterogeneous UAV-user bipartite graph. Two BiGAT layers use channel-weighted attention, Set2Set pools the network, and InfoNCE contrastive pretraining brings states with the same terrain-occlusion pattern closer together. The encoder is frozen before HSAC training; its pooled embedding is concatenated with the complete estimated LoS/NLoS link-state object before entering the policy.

The HSAC actor uses Gaussian heads for velocity/power and Gumbel-Softmax heads for association. Twin critics, adaptive continuous/discrete entropy temperatures, replay, and target networks follow SAC. Greedy altitude, association, and separation demonstrations seed replay and can be selected during early interaction.

## Key findings

- The paper reports average-rate gains of `106.73%` over SAC, `193.24%` over PADDPG, and `43.7%` over GeoAgg-PDQN. Its own baseline naming alternates between SAC and HSAC.
- Reported GDOP "improvements" include `257.66%` over PADDPG; because lower GDOP is better and the aggregation formula is absent, this should not be read as an ordinary percentage reduction.
- A policy trained with maximum user speed `2 m/s` retains at least `90.4%` of that communication rate in the mobility sweep, while average GDOP remains below 2 at `4 m/s`.
- Increasing network size slows convergence, and the paper gives no theorem, global-optimality result, or runtime deadline measurement.

## Limitations / parse caveats

Evaluation uses one reconstructed mountain environment and simulation rather than a field deployment. The controller assumes negligible inter-UAV collection delay and reliable estimates of position, channels, and LoS class. Cross-terrain generalization, localization position error, energy results, controller latency, public data/code, and repeated-run statistics are absent. The GDOP condition, interference-power index, reward/penalty signs, collision terms, InfoNCE expression, and several optimization equations are internally conflicting or parse-damaged.

## Relation to the corpus

This source extends [[joint-localization-and-communication]] from one-rescuer AOA-guided beamforming to multi-user mountainous ranging and control. It combines an exact terrain/link-state representation with [[hybrid-action-decision-making]], but it does not model task offloading or edge execution.

## Raw artifacts

- Parse: `raw/sources/GeoAgg-HSAC_An_RL-Based_Framework_for_Trajectory_and_Resource_Optimization_in_Mountainous_UAV_Integrated_Localization_and_Communication_Networks/GeoAgg-HSAC_An_RL-Based_Framework_for_Trajectory_and_Resource_Optimization_in_Mountainous_UAV_Integrated_Localization_and_Communication_Networks.md`
- Origin PDF: `raw/sources/GeoAgg-HSAC_An_RL-Based_Framework_for_Trajectory_and_Resource_Optimization_in_Mountainous_UAV_Integrated_Localization_and_Communication_Networks/GeoAgg-HSAC_An_RL-Based_Framework_for_Trajectory_and_Resource_Optimization_in_Mountainous_UAV_Integrated_Localization_and_Communication_Networks.pdf`
- Figures: `raw/sources/GeoAgg-HSAC_An_RL-Based_Framework_for_Trajectory_and_Resource_Optimization_in_Mountainous_UAV_Integrated_Localization_and_Communication_Networks/images/`
