---
type: source
modeling_card: required
title: "Joint Trajectory, RIS, and Computation Offloading Optimization via Decentralized Model-Based PPO in Urban Multi-UAV Mobile Edge Computing"
authors: ["Liangshun Wu", "Jianbo Du", "Junsuo Qu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3679344"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), early access, 2026"
tags: [source, multi-uav-assisted-mec, intelligent-reflecting-surface, model-based-marl, ppo, task-offloading, uav-trajectory-control, anti-jamming]
related:
  - "[[model-based-marl]]"
  - "[[ppo]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[blockage-aware-channel-model]]"
  - "[[communication-constrained-marl]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
created: 2026-07-07
updated: 2026-11-03
---

# Joint Trajectory, RIS, and Computation Offloading Optimization via Decentralized Model-Based PPO in Urban Multi-UAV Mobile Edge Computing

## Citation

Wu, L., Du, J., & Qu, J. (2026). *Joint Trajectory, RIS, and Computation Offloading Optimization via Decentralized Model-Based PPO in Urban Multi-UAV Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3679344.

## TL;DR

Builds a decentralized [[model-based-marl]] controller for urban RIS-assisted multi-UAV MEC. Each UAV jointly controls trajectory, offloading, and RIS phase recommendations using local and k-hop neighbor observations. A lightweight RIS controller aggregates the UAV phase proposals. The key algorithmic move is local dynamics learning plus short-horizon branched rollouts inside [[ppo]], improving sample efficiency and stability without requiring a centralized critic.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multi-antenna UAVs $u\in\mathcal U$ act as computing nodes and relays for moving single-antenna UEs $k\in\mathcal K$, forwarding tasks to a ground AP with an MEC server. Direct UE-AP and UE-RIS links are blocked, a building-mounted RIS reflects UAV signals to the AP, and a ground jammer interferes with UAV and RIS links.
**Problem & objective**: Problem (33) maximizes energy efficiency over $N$ slots, $\max_z\frac{\sum_n\sum_k(l_{u,k}^{loc}[n]+l_{u,k}^o[n])}{\sum_nE[n]}$, the processed bits over total UE and UAV energy (32).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV velocity and acceleration | $\mathbf V_u[n],\mathbf A_u[n]$ | continuous | Kinematic controls of UAV $u$ |
| RIS phases | $\boldsymbol\Theta[n]=\mathrm{diag}(e^{j\theta_1},\ldots,e^{j\theta_M})$ | continuous, $\theta_m\in[0,2\pi)$ | Reflection coefficients |
| Time allocation | $\tau_{u,k}^o[n],\tau_{u,k}^R[n]$ | continuous, $\ge0$ | Offloading and relaying time for UE $k$ via UAV $u$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1, C3 | Kinematics $\mathbf q_u[n+1]=\mathbf q_u[n]+\mathbf V_u[n]\delta_t+\frac12\mathbf A_u[n]\delta_t^2$, $\mathbf V_u[n+1]=\mathbf V_u[n]+\mathbf A_u[n]\delta_t$ |
| C2a-C2b | Fixed start and end points; 3-D flight region |
| C4a-C4b, C5 | Per-slot displacement and speed within $V_{\max}$; the end point stays reachable |
| C6-C7 | RIS phases in $[0,2\pi)$ with diagonal unit-modulus $\boldsymbol\Theta[n]$ |
| C8-C10 (35)-(36) | Nonnegative times, zero boundary times, and $\sum_u\sum_k(\tau^o+\tau^R)\le\delta_t$ |
| C11-C12 (37) | Peak and average UAV transmit power |
| C13-C16 (38) | Relay causality, UAV and AP computing within $F_u^{\max}\delta_t$ and $F_a^{\max}\delta_t$, and each UE's total task $L_k$ completed |
**Algorithm**: Each UAV agent observes local and $k$-hop neighbor states with LSTM-based fusion, acts with a decentralized PPO policy, submits an RIS phase proposal that a lightweight RIS controller aggregates, learns a local dynamics model, and adds short-horizon branched model rollouts to real data for policy and value updates without a centralized critic.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied decentralized model-based control of trajectory, RIS phases, and computation offloading in urban multi-UAV mobile edge computing. Each UAV observes local and k-hop neighbor state, selects movement and offloading actions, and sends phase recommendations to a lightweight RIS aggregator. Local learned dynamics models generate short-horizon branched rollouts for PPO policy and value updates without a centralized critic. The objective maximizes energy efficiency under task, communication, computation, RIS, mobility, and jamming conditions. Simulations report convergence nearly as fast as centralized PPO and higher throughput and energy efficiency than the decentralized DPPO and I3CNet baselines.

## Problem

Urban multi-UAV MEC faces building blockage, partial observability, rapidly changing user demand, and expensive inter-UAV information exchange. RIS can restore reflected paths, especially for mmWave/THz-like blockage-sensitive deployments, but RIS phase control, UAV movement, and computation offloading become coupled. The paper targets a decentralized controller that approaches centralized PPO performance while using only limited local coordination.

## System model

- Multiple multi-antenna UAVs serve as both computing nodes and decode-and-forward relays.
- Single-antenna UEs offload tasks to UAVs; tasks can be processed onboard or forwarded to a ground AP with an MEC server.
- A building-mounted RIS uses a uniform rectangular array; direct UE-to-RIS/AP links are blocked or attenuated.
- The RIS phase at each slot is obtained by aggregating phase recommendations from UAV agents.
- The model includes UAV kinematics, RIS-assisted UAV-AP channels, UE-UAV and UAV-AP Rician links, task offloading/relay variables, UE/UAV/AP computing, UAV propulsion energy, and a ground jammer.
- The objective is system energy efficiency under limited observability and sample-efficiency constraints.

## Method

The proposed MB-DRL framework gives each UAV a local policy/value pair and a learned local transition model. Agents observe local state plus k-hop neighborhood information, sample actions from their PPO policies, propose RIS phases, and then use both real interactions and model-generated short-horizon branches for policy/value updates. Baselines include centralized PPO (CPPO), decentralized PPO (DPPO), IC3Net, and reimplemented model-free SOTA competitors under the same environment.

## Key findings

- CPPO remains the upper bound because it has full-state observability, but the proposed decentralized model-based method converges close to CPPO and outperforms DPPO and IC3Net in the reported reward curves.
- The model-based version converges faster and more smoothly than the model-free decentralized version, attributed to short-horizon branched rollouts reducing value-estimation variance.
- CDF comparisons report that the proposed method has the best tradeoff among decentralized schemes for throughput, data rate, and energy efficiency, while approaching centralized performance.
- Ablations show both k-hop neighborhood communication and branched model rollouts matter; removing either degrades energy efficiency and throughput.
- Trajectory plots show smoother and more directed UAV motion than DPPO and IC3Net, with fewer erratic turns under partial observability.
- Increasing neighborhood size improves coordination in congested scenarios, while increasing rollout branch count/length improves energy efficiency until marginal gains diminish beyond four branches.

## Limitations / future work

The evaluation is simulation-only and assumes full CSI for system optimization. The paper's future-work list includes jointly learning neighborhood aggregation and event-triggered communication, uncertainty-aware rollout horizons and branch counts, tighter decentralized convergence guarantees, and jammer-aware trajectory/RIS beam adaptation.

## Relation to the corpus

This source extends the wiki's RIS-MEC line beyond classical BCD/SCA formulations such as [[qin-2023-ris-uav-mec-ee]]. It also complements [[communication-constrained-marl]] and [[ctde-multi-agent-drl-protocol]] by providing a fully decentralized, model-based alternative to centralized critics: local k-hop observations plus learned short-horizon models rather than global-state training.

## Raw artifacts

- `raw/sources/Joint_Trajectory_RIS_and_Computation_Offloading_Optimization_Via_Decentralized_Model-Based_PPO_in_Urban_Multi-UAV_Mobile_Edge_Computing/Joint_Trajectory_RIS_and_Computation_Offloading_Optimization_Via_Decentralized_Model-Based_PPO_in_Urban_Multi-UAV_Mobile_Edge_Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
