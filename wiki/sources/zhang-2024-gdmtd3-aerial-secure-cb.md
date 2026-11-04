---
type: source
modeling_card: required
title: "Multi-Objective Aerial Collaborative Secure Communication Optimization via Generative Diffusion Model-Enabled Deep Reinforcement Learning"
authors: ["Chuang Zhang", "Geng Sun", "Jiahui Li", "Qingqing Wu", "Jiacheng Wang", "Dusit Niyato", "Yuanwei Liu"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3502685"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-swarm, physical-layer-security, collaborative-beamforming, generative-diffusion-model, td3, multi-objective]
related:
  - "[[physical-layer-security]]"
  - "[[generative-diffusion-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[td3]]"
  - "[[friendly-jamming-uav]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
  - "[[yuanwei-liu]]"
created: 2026-05-29
updated: 2026-11-03
---

# Multi-Objective Aerial Collaborative Secure Communication Optimization via Generative Diffusion Model-Enabled Deep Reinforcement Learning

## Citation

Zhang, C., Sun, G., Li, J., Wu, Q., Wang, J., Niyato, D., & Liu, Y. (2024). *Multi-Objective Aerial Collaborative Secure Communication Optimization via Generative Diffusion Model-Enabled Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3502685.

## TL;DR

A UAV swarm forms a virtual antenna array and uses **collaborative beamforming (CB)** to send sensitive surveillance data to a remote base station while resisting mobile eavesdroppers. The authors formulate an **aerial secure communication and energy efficiency multi-objective problem (ASCEE-MOP)** — maximize secrecy rate, minimize swarm flight energy — by jointly optimizing UAV excitation-current weights and positions. The non-convex, NP-hard, dynamic problem is solved by **GDMTD3**, a generative-diffusion-model-enhanced TD3.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A swarm of $K$ UAVs forms a virtual antenna array and uses collaborative beamforming to send surveillance data to a remote base station while mobile eavesdroppers try to decode it. UAV positions and excitation currents shape the beam, the secrecy rate, and flight energy.
**Problem & objective**: ASCEE-MOP P1 (20) is a two-objective problem, $\max_{\boldsymbol I,\boldsymbol q}\left(\sum_nR_{SE}[n],-\sum_nE[n]\right)$, maximizing the total secrecy rate and minimizing total flight energy.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV positions | $\boldsymbol q=\{\boldsymbol q_k[n]\}$ | continuous 3-D | Swarm geometry in slot $n$ |
| Excitation currents | $\boldsymbol I=\{I_k^U[n]\}$ | continuous, $[0,1]$ | Normalized excitation weight of UAV $k$ in the virtual array |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (20b) | Excitation current $0\le I_k^U[n]\le1$ |
| (20c)-(20e) | Position bounds in $x$, $y$, and $z$ |
| (20f) | Speed $0\le v_k^U[n]\le V_{\max}$ |
| (20g) | Pairwise separation $\lVert\boldsymbol q_{k_1}[n],\boldsymbol q_{k_2}[n]\rVert\ge D_{\min}^U$ |
**Algorithm**: Reformulate P1 as an MDP with the weighted reward $r[n]=\omega_1r_{SE}[n]+\omega_2r_E[n]-r_P[n]$ (21), and train GDMTD3, which replaces the TD3 actor with a generative diffusion model that produces continuous position and excitation-current actions by reverse denoising (noise schedule (32)), with twin critics and delayed updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied multi-objective aerial collaborative secure communication with a UAV swarm acting as a virtual antenna array. They formulated ASCEE-MOP to maximize secrecy rate and minimize swarm flight energy over UAV positions and excitation-current weights under excitation-current, flight-region, speed, and separation constraints. GDMTD3 integrates a generative diffusion action model with twin-delayed deep deterministic policy gradients. The diffusion process generates continuous high-dimensional swarm and beamforming actions from the current secure-communication state. Simulations report higher secrecy rate and lower flight energy than four deployment policies and five DRL benchmarks.

## Problem framing

Integrating UAVs into next-gen wireless requires high-rate, long-range *secure* communication against eavesdropping. A UAV swarm acting as a virtual antenna array can beamform to a remote BS, but optimizing the beam (current weights + UAV positions) for secrecy while saving flight energy is a hard, dynamic multi-objective problem.

## System model

- **Actors.** UAV swarm (virtual antenna array) → remote base station (RBS), with mobile eavesdroppers.
- **Objective (ASCEE-MOP).** Maximize system secrecy rate; minimize swarm flight energy ([[physical-layer-security]], [[multi-objective-mdp-vectorial-reward]]).
- **Variables.** Excitation-current weights and positions of the UAVs.

## Method

- **GDMTD3:** integrates a **generative diffusion model** into TD3 to capture the high-dimensional probabilistic distributions needed for optimal policy decisions ([[diffusion-model-as-optimizer]], [[td3]]).

## Key findings

- Simulations show GDMDRL beats various deployment policies on both secrecy rate and swarm flight energy, and GDMTD3 outperforms several advanced DRL benchmarks on the ASCEE-MOP (qualitative; specific curves in the paper).

## Limitations / future work

Simulation-based; the parse's conclusion does not enumerate explicit limitations.

## Relation to the corpus

A **generative-diffusion-as-policy** entry that joins the GDM thread with [[ye-2025-aigc-diffusion-contract]] and [[peng-2025-drudm-cfg]] (and the survey [[khoramnejad-2025-gai-wireless-optimization-survey]]), but applies it to UAV-swarm **physical-layer security** via collaborative beamforming rather than offloading. Connects to the UAV-swarm thread ([[wang-2025-uav-swarm-stackelberg]], [[sun-2024-asap-uav-swarm]], [[li-2025-stochastic-game-uav-swarm]]) and the secrecy/jamming thread ([[shao-2024-drl-antijamming-mec]]). Shares the Geng Sun / Jiahui Li / Qingqing Wu / Dusit Niyato cluster. Reinforces [[generative-diffusion-model]] and [[physical-layer-security]].

## Raw artifacts

- `raw/sources/Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning/Multi-Objective_Aerial_Collaborative_Secure_Communication_Optimization_via_Generative_Diffusion_Model-Enabled_Deep_Reinforcement_Learning.md`
- Original PDF and extracted figures in the same folder.
