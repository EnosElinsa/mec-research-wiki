---
type: source
modeling_card: required
title: "Aerial Reliable Collaborative Communications for Terrestrial Mobile Users via Evolutionary Multi-Objective Deep Reinforcement Learning"
authors: ["Geng Sun", "Jian Xiao", "Jiahui Li", "Jiacheng Wang", "Jiawen Kang", "Dusit Niyato", "Shiwen Mao"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3536093"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, aav-communications, collaborative-beamforming, multi-objective-reinforcement-learning, evolutionary-reinforcement-learning, ppo, virtual-antenna-array]
related:
  - "[[collaborative-beamforming]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[evolutionary-reinforcement-learning]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[ppo]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[song-2022-emorl-tcto-uav]]"
  - "[[li-2024-emodrl-ground-space-cb]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
created: 2026-05-31
updated: 2026-07-16
---

# Aerial Reliable Collaborative Communications for Terrestrial Mobile Users via Evolutionary Multi-Objective Deep Reinforcement Learning

## Citation

Sun, G., Xiao, J., Li, J., Wang, J., Kang, J., Niyato, D., & Mao, S. (2025). *Aerial Reliable Collaborative Communications for Terrestrial Mobile Users via Evolutionary Multi-Objective Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3536093.

## TL;DR

Multiple autonomous aerial vehicles (AAVs) form a **virtual antenna array (UVAA)** and use **collaborative beamforming (CB)** to transmit to a **terrestrial mobile user**, under interference from non-associated BSs and time-varying channels. The work formulates a **long-term multi-objective optimization problem (MOP)** — maximize total achievable transmission rate, minimize AAV swarm flight energy — over excitation-current weights and AAV positions, and transforms it into a multi-objective Markov decision process solved by **EMOPPO-VLH**: an evolutionary multi-objective PPO with a **vectorized value function**, **LSTM** networks, and a **hyper-sphere-based task selection** method.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple autonomous aerial vehicles form a virtual antenna array and collaboratively beamform to a mobile terrestrial user under interference from non-associated base stations. AAV positions and excitation currents change over a time-varying Gaussian-Markov channel, and flight energy trades off against achievable rate.

**Problem & objective**: A long-term multi-objective MOP maximizes total transmission rate and minimizes AAV flight energy, $\max(R_{\mathrm{sum}},-E_{\mathrm{flight}})$, over excitation weights and AAV positions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AAV positions | $\mathbf q_i(t)$ | continuous 3-D positions | UVAA geometry over time |
| Excitation currents | $w_i(t)$ | complex continuous | Collaborative-beamforming amplitudes and phases |
| Policy preference | $\mathbf w$ | continuous objective-weight vector | Pareto preference used by each policy task |
| Movement action | $a_t$ | discrete/continuous | Position update selected by the learned policy |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | AAV positions remain in the flight region and obey mobility/energy limits |
| C2 | Excitation currents satisfy power and beamforming normalization limits |
| C3 | The UVAA maintains a feasible link to the mobile user under interference |
| C4 | Vector rewards and policy tasks remain within the multi-objective preference domain |

**Algorithm**: Transform the long-term MOP into a vector-reward MOMDP → warm up a primary policy population → train vectorized-value PPO with LSTM state features → select tasks by hyper-sphere diversity → evolve policy tasks and update the external Pareto archive → return nondominated rate-energy policies.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied reliable collaborative communications from a mobile terrestrial user to a multi-AAV virtual antenna array. They formulated a long-term multi-objective problem that maximizes transmission rate and minimizes AAV flight energy through excitation-current and position control under time-varying channels and interference. EMOPPO-VLH transforms the problem into a vector-reward MDP and combines vectorized-value PPO, LSTM temporal features, warm-up learning, hyper-sphere task selection, and evolutionary policy updates. The external archive retains a diverse nondominated policy set for different rate-energy preferences. Simulations report improved inverted generational distance and hypervolume over the evaluated evolutionary and multi-objective reinforcement-learning baselines across system scales.

## Problem framing

A single AAV's onboard energy and transmit power limit its range; CB across a UVAA amplifies received power (∝ the square of the number of AAV elements) to extend distance and resist interference. But the AAVs' stochastic 3-D positions disrupt the beam pattern, and improving the pattern means flying (extra energy). With mobile ground users (pedestrians, robots, vehicles) and no advance knowledge of their future locations, offline optimization fails — motivating a real-time multi-objective online method. The rate-vs-energy objectives trade off over time, making this a long-term MOP.

## System model

- **Actors.** Multiple AAVs forming a UVAA → one terrestrial **mobile** user; interference from non-associated BSs; time-varying channels.
- **User mobility.** Modeled with a memory-based random walk, the **Gaussian-Markov** mobility model ([[gauss-markov-mobility-model]]), to better match real movement.
- **Objectives.** Maximize total achievable rate; minimize overall AAV flight energy (a long-term MOP, NP-hard).
- **Variables.** AAV excitation-current weights and positions.
- **Formulation.** Transformed into a multi-objective MDP (MOMDP) with a [[multi-objective-mdp-vectorial-reward|vectorized reward]].

## Method

- **EMOPPO-VLH.** Extends single-objective [[ppo]] with a **vectorized value function** to handle multiple objectives; integrates **LSTM** networks to capture short-term (multi-path fading) and long-term (user mobility) temporal dependencies; and adds a **hyper-sphere-based task selection** method to improve Pareto-set diversity.
- **Two stages.** A **warm-up stage** generates a high-quality primary population, then an **evolutionary stage** (task-population update, hyper-sphere task selection, offspring acquisition, external Pareto archive update) optimizes the selected tasks via an LSTM-MOPPO learner ([[evolutionary-reinforcement-learning]] + [[multi-objective-reinforcement-learning]]).

> Note: the parse's algorithm name is **EMOPPO-VLH** in the title/abstract/algorithm sections; one sentence in the introduction calls it "MOPPO-PLE" (an apparent in-paper naming inconsistency). This page uses EMOPPO-VLH, the dominant name in the parse.

## Key findings

- EMOPPO-VLH generates a diverse set of high-quality non-dominated policies and outperforms benchmark algorithms across different scales, assessed by inverted generational distance (IGD) and hypervolume (qualitative; specific scores in the paper).
- Additional simulations show scalability and robustness under varying system parameters and unexpected circumstances; user mobility does not degrade the method's effectiveness.

## Limitations / future work

The parse has a discussion section but does not enumerate a consolidated limitations list; evaluation is simulation-based.

## Relation to the corpus

A close sibling of the wiki's existing evolutionary-multi-objective-RL entry [[song-2022-emorl-tcto-uav]] (EMORL-TCTO) and of the same group's ground-space companion [[li-2024-emodrl-ground-space-cb]] — all use an evolutionary mechanism around a (multi-objective) PPO learner to emit a Pareto set in one run. It shares the Geng Sun / Jiahui Li / Jiacheng Wang / Dusit Niyato cluster and the **collaborative-beamforming UVAA** model with the secure-CB source [[zhang-2024-gdmtd3-aerial-secure-cb]], but targets reliable rate-vs-energy CB to a mobile user rather than secrecy. Introduces [[collaborative-beamforming]] as new vocabulary; reinforces [[multi-objective-reinforcement-learning]] and [[evolutionary-reinforcement-learning]].

## Raw artifacts

- `raw/sources/Aerial_Reliable_Collaborative_Communications_for_Terrestrial_Mobile_Users_via_Evolutionary_Multi-Objective_Deep_Reinforcement_Learning/full.md`
- Original PDF and extracted figures in the same folder.
