---
type: source
title: "Trajectory Optimization for UAV Emergency Communication With Limited User Equipment Energy: A Safe-DQN Approach"
authors: ["Tiankui Zhang", "Jiayi Lei", "Yuanwei Liu", "Chunyan Feng", "Arumugam Nallanathan"]
year: 2021
url: "https://doi.org/10.1109/TGCN.2021.3068333"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 5, no. 3, pp. 1236-1247"
tags: [source, emergency-communication, safe-reinforcement-learning, deep-q-network, uav-trajectory, user-energy]
related:
  - "[[safe-reinforcement-learning]]"
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[distributed-tabular-q-learning-uav-collision-avoidance]]"
  - "[[navigation-stochastic-control-decomposition]]"
  - "[[connectivity-preserving-uav-behavioral-loss]]"
  - "[[bernstein-safe-approximation]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[deep-q-network]]"
  - "[[uav-trajectory-control]]"
  - "[[zhou-2021-delay-sagin-task-scheduling]]"
  - "[[tiankui-zhang]]"
  - "[[yuanwei-liu]]"
  - "[[arumugam-nallanathan]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# Trajectory Optimization for UAV Emergency Communication With Limited User Equipment Energy: A Safe-DQN Approach

## Citation

Zhang, T., Lei, J., Liu, Y., Feng, C., & Nallanathan, A. (2021). *Trajectory Optimization for UAV Emergency Communication With Limited User Equipment Energy: A Safe-DQN Approach*. **IEEE Transactions on Green Communications and Networking, 5**(3), 1236-1247. DOI: 10.1109/TGCN.2021.3068333.

## TL;DR

Trains a Lyapunov-filtered DQN trajectory policy for one emergency UAV base station, maximizing uploaded data while constraining expected user-energy cost and filtering actions whose next grid point lies inside a modeled obstacle.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV acts as an aerial base station and collects uplink data from fixed users in a post-disaster area containing circular obstacle regions. Users access the UAV through OFDMA, and each air-to-ground channel follows the 3GPP probabilistic LoS and NLoS path-loss model with AWGN.

**Problem & objective**: Trajectory problem (P1), equivalently CMDP (P2), maximizes expected cumulative uploaded bits, $\max_{\pi\in\Delta}W_\pi(s_0)$, subject to $E_\pi(s_0)\leq e_0$ and obstacle avoidance.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Trajectory policy | $\pi(\cdot\mid s)$ | stochastic policy | Action probabilities at a UAV position and upload-progress state |
| UAV motion action | $a_m$ | discrete, 5 actions | Move forward, backward, left, right, or hover in slot $m$ |
| UAV trajectory | $l_U(m)$ | discrete grid position | Horizontal UAV location induced by the action sequence |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 7a | Each user's cumulative energy satisfies $\sum_me_k(m)\leq e_0$ |
| 7a double-prime | The CMDP uses the sufficient surrogate $\sum_m\max_ke_k(m)\leq e_0$ |
| 7b | Slot displacement obeys $\|l_U(m+1)-l_U(m)\|=\delta_tv$ |
| 7c | Every selected grid point lies outside the obstacle set, $l_U(m)\notin\Omega$ |
| 13 | The learned policy satisfies expected cumulative cost $E_\pi(s_0)\leq e_0$ |

**Algorithm**: Convert the trajectory problem to a CMDP; construct a Lyapunov function from a feasible benchmark policy and derive a statewise safe-policy set; learn reward and cost Q-functions plus the benchmark-policy network with prioritized replay and target networks; solve the small policy linear program; remove actions whose next point lies in an obstacle before execution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied UAV trajectory optimization for emergency communication with limited user-equipment energy and flight obstacles. They formulated a constrained Markov decision process that maximizes long-term uplink throughput subject to an expected cumulative energy limit and obstacle avoidance. Their safe-DQN method constructs a Lyapunov-based safe policy set, learns reward and cost action values, and filters illegal motion actions before execution. Simulations report convergence to approximately 50 Mbps within 1,000 episodes at the selected learning rate. The proposed method reports higher uplink throughput and energy efficiency than the fixed-flight-trajectory and shortest-flight-distance baselines across the evaluated service durations and user counts.

## Model and method

One fixed-altitude UAV serves fixed post-disaster users through OFDMA over a finite horizon. Users have equal initial data, fixed transmit power, and cumulative energy budgets. The paper replaces all per-user energy inequalities by an exact maximum-over-users constraint, then uses the stricter sum of per-slot maximum user energy as a sufficient surrogate.

A constrained MDP uses UAV position and uploaded-data totals as state, five discrete motion actions, uploaded bits as reward, and maximum slot energy as cost. Learned reward/cost Q-functions and a benchmark-policy network feed a small LP that selects an action distribution satisfying an estimated Lyapunov safety inequality. Prioritized replay and target networks train the policy.

## Guarantee scope and findings

The exact Lyapunov construction supports an expected cumulative-cost statement for the surrogate CMDP. The implementation replaces its function and policies with neural approximations, so the paper does not prove sample-path energy safety, convergence, or global trajectory optimality. Its obstacle filter checks the next point rather than continuous segment-circle intersection.

Simulation reports the highest energy efficiency among two baselines and higher throughput at several horizon/user-count settings, while also using more absolute user energy. Throughput rises and then falls with altitude in the tested scenario.

## Limitations

Simulation only; one UAV, fixed users, equal data, fixed power, constant nominal speed/altitude, known circular obstacles, and no measured disaster channel. Hovering conflicts with the written fixed-displacement constraint, the return-to-start requirement is not visible in the formal problem, and the conservative surrogate is later called equivalent without proof.

## Relation to the corpus

This source complements [[zhou-2021-delay-sagin-task-scheduling]] by applying [[safe-reinforcement-learning]] to aerial motion rather than task scheduling. It is also a useful boundary case for [[uav-trajectory-control]]: the Lyapunov filter constrains an expected learned cost, while geometric obstacle handling remains a separate one-step action filter.

## Comparison boundary

The comparison with [[hsu-2022-collision-avoidance-trajectory]] and [[distributed-tabular-q-learning-uav-collision-avoidance]] is an enforcement-locus contrast: this source filters a next point and an expected surrogate, whereas Hsu's table changes heading from local sensing. [[navigation-stochastic-control-decomposition]] and [[connectivity-preserving-uav-behavioral-loss]] address different control layers, and [[bernstein-safe-approximation]] supplies a probabilistic Gaussian rate construction rather than a collision or sample-path guarantee. See [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- Parse: `raw/sources/Trajectory_Optimization_for_UAV_Emergency_Communication_With_Limited_User_Equipment_Energy_A_Safe-DQN_Approach/Trajectory_Optimization_for_UAV_Emergency_Communication_With_Limited_User_Equipment_Energy_A_Safe-DQN_Approach.md`
- Original PDF and extracted figures are in the same folder.
