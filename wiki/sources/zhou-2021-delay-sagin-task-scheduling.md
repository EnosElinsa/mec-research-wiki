---
type: source
modeling_card: required
title: "Deep Reinforcement Learning for Delay-Oriented IoT Task Scheduling in SAGIN"
authors: ["Conghao Zhou", "Wen Wu", "Hongli He", "Peng Yang", "Feng Lyu", "Nan Cheng", "Xuemin Shen"]
year: 2021
url: "https://doi.org/10.1109/TWC.2020.3029143"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, sagin, iot, uav, leo-satellite, task-scheduling, task-offloading, constrained-mdp, deep-q-network, safe-rl]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[task-offloading]]"
  - "[[safe-reinforcement-learning]]"
  - "[[deep-q-network]]"
  - "[[cheng-2019-sagin-iot-offloading-rl]]"
  - "[[huang-2026-amappo-satellite-edge]]"
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[xuemin-shen]]"
  - "[[nan-cheng]]"
created: 2026-07-06
updated: 2026-07-16
---

# Deep Reinforcement Learning for Delay-Oriented IoT Task Scheduling in SAGIN

## Citation

Zhou, C., Wu, W., He, H., Yang, P., Lyu, F., Cheng, N., & Shen, X. (2021). *Deep Reinforcement Learning for Delay-Oriented IoT Task Scheduling in SAGIN*. **IEEE Transactions on Wireless Communications**, 20(2), 911-925. DOI: 10.1109/TWC.2020.3029143.

## TL;DR

An early SAGIN task-scheduling paper where a rotary-wing UAV collects delay-oriented IoT tasks and decides whether to process them locally, offload to a nearby BS, or offload to a LEO satellite. The key method is DOTS, a deep risk-sensitive RL scheduler that uses separate Q-functions for delay cost and energy-risk, then adjusts a weight parameter to satisfy a UAV energy-capacity constraint.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A rotary-wing UAV follows a predefined route, collects stochastic IoT tasks, executes them locally, or forwards them to an available terrestrial BS or an always-accessible LEO constellation. Separate BS and satellite interfaces avoid cross-tier interference; UAV-BS links use location-dependent air-to-ground path loss, and the UAV-satellite link includes Weibull rain attenuation and propagation delay.

**Problem & objective**: P1 is an uncertain integer nonlinear scheduling problem recast as an energy-constrained MDP that minimizes long-run processing delay, $\min_{\pi}\lim_{T\to\infty}\frac{1}{T}\mathbb E_\pi[\sum_{t=1}^{T}C_t]$, subject to the UAV energy capacity.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading destination | $\alpha_t$ | categorical | Nearby BS, LEO constellation, or no new forwarding |
| Number of offloaded tasks | $\beta_t$ | integer, $0\leq\beta_t\leq\beta^{\max}$ | Tasks moved from the computing queue to forwarding |
| Scheduling policy | $\pi(a\mid s)$ | stochastic policy | State-dependent choice of $a_t=(\alpha_t,\beta_t)$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Destination belongs to the location-dependent available set $\mathcal L_t$ |
| C2 | Offloaded task count respects the forwarding limit and current queue backlog |
| C3 | A busy forwarding interface admits no new tasks, giving $\alpha_t=-1$ and $\beta_t=0$ |
| C4 | Expected time-average UAV energy consumption does not exceed capacity $\varepsilon$ |
| C5 | Computing and forwarding queues remain within their finite capacities |

**Algorithm**: Form the CMDP state from location, forwarding status, computing backlog, and cumulative energy → learn separate delay-cost and energy-risk Q-functions with target networks and replay → mask unavailable actions → combine cost and risk values → adjust the outer risk weight until the energy constraint is satisfied.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhou et al. [x] studied delay-oriented IoT task scheduling in a space-air-ground integrated network where a UAV processes tasks locally or offloads them to a nearby base station or a LEO satellite constellation. They formulated an uncertain integer nonlinear problem as an energy-constrained Markov decision process that minimizes time-averaged task-processing delay under a UAV energy-capacity constraint. The proposed DOTS scheme represents each action by an offloading destination and number of offloaded tasks. Its deep risk-sensitive reinforcement-learning algorithm learns separate Q-functions for delay cost and energy risk, masks unavailable actions, and adjusts their weighting across episodes. Simulations report up to a 30% processing-delay reduction over probabilistic configuration methods while satisfying the UAV energy constraint.

## Problem

IoT devices in remote or hard-to-cover regions need low-latency task processing, but a UAV collector has limited onboard computation and battery energy. BSs offer high computing capacity only when the UAV is in coverage; LEO satellites offer persistent coverage but non-negligible propagation delay. The paper minimizes long-term task delay while satisfying an average UAV energy constraint.

## System model

- **Architecture:** a UAV flies along a predefined trajectory, collects IoT tasks, and can schedule tasks to itself, one nearby BS, or the LEO satellite constellation.
- **Queues:** the UAV maintains a computing queue and a forwarding queue; new tasks may be dropped if the computing queue is full.
- **Offloading actions:** each epoch chooses an offloading destination and the number of tasks to forward, subject to available BS/satellite links and queue state.
- **Delay model:** task delay includes remote computing delay, local computing / queueing delay, and transmission delay; satellite offloading also includes propagation delay.
- **Energy model:** cumulative UAV energy includes communication and local computing energy; propulsion energy is treated as constant for the predefined trajectory.

## Method

The paper formulates delay-oriented task scheduling as a constrained MDP with state variables for UAV location, forwarding status, computing backlog, and cumulative energy. DOTS defines a cost Q-function for delay and a risk Q-function for energy-capacity violation. A weighted Q-function combines cost and risk; the outer loop adjusts the risk weight according to whether the episode exceeds the energy budget, and the inner loop trains DNN approximators with experience replay and a filter layer for unavailable actions.

## Key findings

- The abstract reports up to **30%** task-processing-delay reduction compared with probabilistic configuration baselines while satisfying the UAV energy constraint.
- In the simulations, DOTS learns to use BS offloading when the UAV is under BS coverage and satellite offloading as a complementary option outside BS coverage.
- The reported convergence plots show average delay and average energy consumption stabilizing after training under multiple UAV energy-capacity settings.
- Compared with random probabilistic configuration and sampling-based probabilistic configuration, DOTS achieves lower time-averaged delay while keeping energy near the specified constraint.

## Limitations / future work

The paper uses a predefined UAV trajectory and simulation-based evaluation; it does not jointly optimize the UAV path. The conclusion states that future work will investigate task scheduling based on cooperation of multiple UAVs in SAGIN.

## Relation to the corpus

This is a core bridge between [[cheng-2019-sagin-iot-offloading-rl]] and later SAGIN sources such as [[huang-2026-amappo-satellite-edge]]. It shares the [[space-air-ground-integrated-network]] architecture and [[leo-satellite-edge-computing]] offloading tier, but its distinctive contribution is constrained / risk-sensitive deep Q-learning for delay-oriented UAV task scheduling. It also gives a compact early example of [[safe-reinforcement-learning]] in MEC: the energy constraint is handled through an explicit risk Q-function rather than only a reward penalty.

## Raw artifacts

- `raw/sources/Deep Reinforcement Learning for Delay-Oriented IoT Task Scheduling in SAGIN/Deep Reinforcement Learning for Delay-Oriented IoT Task Scheduling in SAGIN.md`
- Original PDF and extracted figures (`images/`) in the same folder.
