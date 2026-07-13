---
type: source
title: "Sensing-Error-Aware UAV Scheduling Based on Generative Diffusion-Driven MADRL for ISAC-Enabled Multi-UAV Systems"
authors: ["Yihao Wu", "Hanxiao Yu", "Yiqing Zhou", "Ningzhe Shi", "Qing Cai", "Jinglin Shi"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3638787"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 9782-9798"
tags: [source, integrated-sensing-and-communication, multi-uav, sensing-error, generative-diffusion, madrl, scheduling, resource-allocation]
related:
  - "[[sensing-error-aware-communication-rate]]"
  - "[[diffusion-augmented-madrl-replay]]"
  - "[[adaptive-td-isac-sensing-period]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[generative-diffusion-model]]"
  - "[[deep-q-network]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[wang-2026-rmaddpg-dda-uav-isac-vehicular]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[zhu-2025-green-isac-q-learning]]"
  - "[[guo-2026-dual-objective-multiuav-isac]]"
  - "[[meng-2026-uav-isac-corrections]]"
created: 2026-07-14
updated: 2026-07-14
---

# Sensing-Error-Aware UAV Scheduling Based on Generative Diffusion-Driven MADRL for ISAC-Enabled Multi-UAV Systems

## Citation

Wu, Y., Yu, H., Zhou, Y., Shi, N., Cai, Q., & Shi, J. (2026). *Sensing-Error-Aware UAV Scheduling Based on Generative Diffusion-Driven MADRL for ISAC-Enabled Multi-UAV Systems*. **IEEE Transactions on Wireless Communications, 25**, 9782-9798. DOI: 10.1109/TWC.2025.3638787.

## TL;DR

Maps localization error into an expected air-to-ground communication rate and uses that metric to coordinate multi-UAV placement, user association, bandwidth, and sensing frequency. A diffusion model augments MADQN replay with synthetic error-bearing transitions, while simulated annealing selects the integer spacing between sensing frames.

## Problem

In time-division UAV ISAC, localization errors mispoint communication beams and make schedules based on sensed positions overestimate link quality. Sensing more frequently improves position information but consumes communication time. The paper formulates this coupling directly rather than treating sensing accuracy and communication rate as independent objectives.

## System model

- At least three fixed-altitude UAVs, each carrying an `M`-element ULA, serve mobile single-antenna users. UAVs reuse spectrum and create inter-UAV interference; users attached to one UAV use OFDMA.
- Users follow a [[gauss-markov-mobility-model]]. Air-to-ground channels combine probabilistic LoS/NLoS loss with array steering.
- Communication and sensing are time divided. A positive integer sensing period `alpha` places sensing slots every `alpha` frames, so smaller values reserve more time for sensing.
- Beamforming uses sensed user directions. A circular position-error region induces an angular-error interval; the analysis assumes uniform angular error and integrates the resulting rate distribution to obtain the [[sensing-error-aware-communication-rate|sensing-error-aware expected rate]].
- Policies observe sensed positions, while evaluation computes actual rate from true user positions.

## Method

The joint problem maximizes average aggregate sensing-error-aware rate over nonsensing slots by selecting the sensing period, horizontal UAV positions, binary user associations, and bandwidth allocations. Constraints cover per-UAV bandwidth, user average-rate QoS, localization MSE, horizontal region and motion limits, and the integer sensing period. Altitude, transmit power, antenna count, and beamformer structure are fixed.

For fixed `alpha`, each UAV is a MADQN agent whose state contains all sensed user positions and its previous channel matrix. Its action includes UAV position, association, and bandwidth, and its local reward sums associated users' expected rates. [[diffusion-augmented-madrl-replay]] trains a fully connected diffusion model on complete transition tuples and mixes generated and real replay samples at ratio `rho`; the MADQN, not the diffusion model, still chooses actions. For fixed scheduling policies, [[adaptive-td-isac-sensing-period]] uses simulated annealing to propose and accept neighboring integer periods. The two blocks are iterated.

## Key findings

- At localization `MSE=100 m^2`, rate degradation is `2.8%` for GD-MADRL+SA, versus `11.4%` for MADRL+SA, `11.1%` for MADRL+Fixed, `10.6%` for epsilon-Greedy+Fixed, and `13.5%` for MAPDQN+Fixed.
- The paper reports up to `30%` communication-rate improvement over the cited sensing-error-unaware methods; it does not identify a single operating point or denominator for that headline claim.
- Over the reported 10-second moving-user trace, GD-MADRL+SA improves average rate by `23.5%`, `28.1%`, `31.6%`, and `49.1%` over MADRL+Fixed, epsilon-Greedy+Fixed, MAPDQN+Fixed, and Uniform, respectively.
- GD-MADRL reward stabilizes after about 200 episodes, and `rho=0.5` gives the highest rate in the diffusion-ratio experiment.
- With 100 users and `40 m^2` sensing MSE, gains taper after more than six UAVs; Uniform slightly exceeds MAPDQN beyond seven UAVs.

## Limitations

Results are simulation-only, without flight tests, measured sensing-error distributions, runtime, overhead measurements, confidence intervals, or released code. Every agent observes all sensed user positions, but the communication needed for that global observation and coordinated learning is omitted. The circular-error-to-uniform-angle model does not cover arbitrary biased or correlated localization errors. The paper describes continuous position and bandwidth actions but uses value-based MADQN without explaining discretization or feasibility projection. It also provides no physical-consistency filter for diffusion-generated transition tuples, and the cost of retraining or updating GD-MADRL inside simulated annealing is absent. Propulsion energy, collision avoidance, acceleration, no-fly zones, and backhaul/control links are not modeled.

## Relation to the corpus

The source joins [[integrated-sensing-and-communication]] with localization-aware scheduling and generative replay. [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] and [[qin-2023-symmetry-augmented-uav-isac]] also use multi-agent learning for multi-UAV ISAC, but neither derives the same error-averaged rate objective. [[zhu-2025-green-isac-q-learning]] uses localization CRB in value-based UAV selection, while [[guo-2026-dual-objective-multiuav-isac]] keeps communication rate and sensing accuracy as separate objectives. Here, diffusion augments replay data; it is not an action policy or direct network optimizer.

## Raw artifacts

- Parse: `raw/sources/Sensing-Error-Aware_UAV_Scheduling_Based_on_Generative_Diffusion-Driven_MADRL_for_ISAC-Enabled_Multi-UAV_Systems/Sensing-Error-Aware_UAV_Scheduling_Based_on_Generative_Diffusion-Driven_MADRL_for_ISAC-Enabled_Multi-UAV_Systems.md`
- Origin PDF: `raw/sources/Sensing-Error-Aware_UAV_Scheduling_Based_on_Generative_Diffusion-Driven_MADRL_for_ISAC-Enabled_Multi-UAV_Systems/Sensing-Error-Aware_UAV_Scheduling_Based_on_Generative_Diffusion-Driven_MADRL_for_ISAC-Enabled_Multi-UAV_Systems.pdf`
- Figures: `raw/sources/Sensing-Error-Aware_UAV_Scheduling_Based_on_Generative_Diffusion-Driven_MADRL_for_ISAC-Enabled_Multi-UAV_Systems/images/`
