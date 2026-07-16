---
type: source
title: "Integrated Sensing and Communication for Energy-Efficient Low-Altitude Economy Based on Meta Deep Reinforcement Learning"
authors: ["Xiaowen Ye", "Xianxin Song", "Yi Wu", "Liqun Fu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3678893"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-economy, isac, meta-deep-reinforcement-learning, td3, uav-trajectory-control, energy-efficiency]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[meta-deep-reinforcement-learning]]"
  - "[[episodic-experience-replay]]"
  - "[[td3]]"
  - "[[uav-trajectory-control]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# Integrated Sensing and Communication for Energy-Efficient Low-Altitude Economy Based on Meta Deep Reinforcement Learning

## Citation

Ye, X., Song, X., Wu, Y., & Fu, L. (2026). *Integrated Sensing and Communication for Energy-Efficient Low-Altitude Economy Based on Meta Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3678893.

## TL;DR

Extends LAE-oriented ISAC control from communication sum-rate to **energy efficiency**. A ground base station (GBS) simultaneously serves authorized UAVs and senses an unauthorized moving target; the controller jointly optimizes GBS beamforming and UAV trajectories over a flight period. The paper proposes **DeepESC**, a TD3-style DRL controller with constrained action selection and episode-level replay, then adds **Meta-DeepESC** so the policy adapts faster to unseen flight-period lengths with fewer samples.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna ground base station communicates with authorized cargo UAVs and senses an unauthorized moving target. Authorized UAVs follow fixed-altitude missions over a finite number of slots while total energy includes GBS signaling and UAV propulsion.

**Problem & objective**: Problem (3) maximizes expected communication-centric energy efficiency, $\max_{\mathbf W_c,\mathbf W_s,\mathbf u}\mathbb E[\sum_{t=1}^{T}R_{\mathrm{total}}(t)/E_{\mathrm{total}}(t)]$, through joint beamforming and trajectory control.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beamforming | $\mathbf W_c(t)$ | complex continuous | GBS downlink beams for authorized UAVs |
| Sensing beamforming | $\mathbf W_s(t)$ | complex continuous | GBS probing beams for target monitoring |
| UAV movement direction | $\mathbf a_u(t)$ | continuous angles | Per-slot headings for all authorized UAVs |
| UAV trajectory | $\mathbf u_m(t)$ | continuous positions | Horizontal trajectory of UAV $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 3b | Expected average target sensing SNR is at least $\Gamma_{\min}$ |
| 3c | Constant-speed motion satisfies $\|\mathbf u_m(t+1)-\mathbf u_m(t)\|_2=v_m\Delta_t$ |
| 3d | Each UAV starts and finishes at its prescribed mission locations |
| 3e-3f | UAV-to-UAV and UAV-to-target separation remains at least $D_{\min}$ |
| 3g | Communication and sensing beam powers jointly remain below $P_{\max}$ |

**Algorithm**: DeepESC uses a TD3 actor and twin critics, constrained action selection, and prioritized episode-level replay for the long-horizon MDP. Meta-DeepESC meta-trains across flight-period tasks with dynamic task weighting and smoothed meta-parameters, then adapts the learned initialization to an unseen mission length with a small number of new samples.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ye et al. [x] optimized communication-centric energy efficiency in a ground-based LAE ISAC system with authorized UAVs and an unauthorized target. The formulation jointly selects communication beams, sensing beams, and UAV trajectories under sensing-SNR, mission, collision, and transmit-power constraints. DeepESC combines TD3, constrained action selection, and prioritized episode-level replay, while Meta-DeepESC adds meta-training and rapid adaptation across flight-period lengths. In the reported four-UAV and forty-slot setting, Meta-DeepESC achieved energy efficiency of 5.84e-3 bits per hertz per joule and average sensing SNR of 1.66 dB against a 1.50 dB target. It exceeded DDPGE by more than 7.37% in energy efficiency across the examined UAV-count sweep and remained the strongest method across the tested CSI delays. The reported inference time was approximately 0.6 ms, and meta-learning improved convergence and generalization to unseen flight periods.

## Problem framing

In a low-altitude-economy airspace, authorized UAVs need communication and navigation support while unauthorized targets must be sensed. The hard part is that energy-efficient communication, average sensing-SNR requirements, UAV mission completion, collision avoidance, and transmit-power limits interact over an entire episode rather than a single slot.

## System model

- One multi-antenna GBS at the origin transmits to multiple single-antenna authorized UAVs and receives radar echoes from a low-altitude target.
- Authorized UAVs fly at preset altitude and transport cargo from source to destination positions over a finite flight period divided into slots.
- Decision variables include GBS beamforming and authorized-UAV horizontal trajectories.
- Constraints cover average sensing SNR, task/mission completion, inter-UAV collision avoidance, and maximum GBS transmit power.

## Method

- **Episode-task MDP.** The state/action design targets long-term flight-period constraints rather than only instantaneous rewards.
- **DeepESC.** A TD3-based controller with a constrained action-selection policy. The policy uses scaling and current UAV locations to refine exploration noise so sampled actions remain closer to sensing, mission, collision, and power feasibility.
- **Episodic experience replay.** Experiences are stored and sampled as complete episode sets, with uncertainty-aware priority and recent sets sampled more actively.
- **Meta-DeepESC.** Meta-learning is added through dynamic task weighting and meta-parameter smoothing so training across sampled flight periods yields a policy that can adapt quickly when the flight period changes.

## Key findings

- In the 4-UAV, 40-slot sensing table, Meta-DeepESC reports average sensing SNR of 1.66 dB against a 1.50 dB target, while comparison variants either match less robustly or miss the target.
- The best reported hyperparameter row reaches energy efficiency of `5.84 x 10^-3` bits/Hz/J with 1.66 dB average sensing SNR.
- The conclusion reports higher energy efficiency than DDPG/exploration baselines, constraint satisfaction across the tested cases, faster convergence for Meta-DeepESC, and better generalization across flight periods.
- Inference is reported around 0.6 ms, while an optimization solver baseline takes about 0.1 s per iteration in the authors' setup.

## Limitations / future work

Evaluation is simulation-based. The authors state that the simulation environment is built from mathematical communication/sensing models, with LOS channel and signal models derived from real-world data, but the controller is not flight-tested. Future directions named in the parse include adding a Value-of-Service reward, federated training for scalable task sampling and gradient aggregation, and a real-time collision-avoidance monitor that can override the learned controller.

## Relation to the corpus

This is the energy-efficiency successor to [[ye-2026-deeplsc-lae-isac]], which optimized communication sum-rate in a similar LAE ISAC setting. It reinforces [[integrated-sensing-and-communication]], [[low-altitude-intelligent-network]], and [[uav-trajectory-control]], while adding [[meta-deep-reinforcement-learning]] and [[episodic-experience-replay]] to the DRL-method vocabulary. It also complements [[wang-2026-secure-lae-uav-scheduling]]: both optimize LAE UAV control under sensing/security constraints, but this source uses a Meta-TD3 controller over energy-efficient ISAC rather than a classical secrecy-energy-efficiency decomposition.

## Raw artifacts

- `raw/sources/Integrated Sensing and Communication for Energy-Efficient Low-Altitude Economy Based on Meta Deep Reinforcement Learning/Integrated Sensing and Communication for Energy-Efficient Low-Altitude Economy Based on Meta Deep Reinforcement Learning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
