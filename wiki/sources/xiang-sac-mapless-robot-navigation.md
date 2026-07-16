---
type: source
title: "Continuous Control with Deep Reinforcement Learning for Mobile Robot Navigation"
authors: ["Jiaqi Xiang", "Qingdong Li", "Xiwang Dong", "Zhang Ren"]
year:
url: ""
venue: ""
modeling_card: required
tags: [source, soft-actor-critic, continuous-control, robot-navigation, drl, mapless-navigation]
related:
  - "[[soft-actor-critic]]"
  - "[[ddpg]]"
  - "[[ppo]]"
  - "[[uav-trajectory-control]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
  - "[[chen-2025-swipt-mec-sac]]"
created: 2026-05-31
updated: 2026-07-16
---

# Continuous Control with Deep Reinforcement Learning for Mobile Robot Navigation

## Citation

Xiang, J., Li, Q., Dong, X., & Ren, Z. *Continuous Control with Deep Reinforcement Learning for Mobile Robot Navigation*. Venue / year / DOI: **not in parse** (the MinerU parse contains no publication line; authors affiliated with the School of Automation Science and Electrical Engineering and the Beijing Advanced Innovation Center for Big Data and Brain Computing, Beihang University). An IEEE Xplore record exists for this title (document 8996652), but the venue name and year are not stated in the parse, so they are left blank rather than guessed.

## TL;DR

An end-to-end, **mapless** autonomous-navigation method for a mobile robot trained with **Soft Actor-Critic (SAC)** ([[soft-actor-critic]]). The policy takes low-dimensional laser-scan data plus target information (and the previous action and reward) as input and outputs continuous linear and angular velocity. Trained in Gazebo/ROS on a Turtlebot3, it reaches performance comparable to a traditional SLAM + A\* + DWA navigation stack while using only **10-dimensional** sparse laser data (vs 360-dimensional for the classical `move_base` planner).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A Turtlebot3 navigates a mapless Gazebo/ROS arena from sparse laser scans and relative target information, with the previous action and reward retained in the state. The paper defines no wireless multiple-access scheme or channel model.

**Problem & objective**: An entropy-regularized continuous-control MDP learns a collision-avoiding target-reaching policy, $\max_{\pi}\mathbb E_{\tau\sim\pi}[\sum_t\gamma^t(R(s_t,a_t,s_{t+1})+\alpha H(\pi(\cdot\mid s_t)))]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Linear velocity | $v_t$ | continuous, $[0,0.2]$ m/s | Forward speed commanded at step $t$ |
| Angular velocity | $\omega_t$ | continuous, $[-1,1]$ rad/s | Turning command at step $t$ |
| Navigation policy | $\pi_\theta(a_t\mid s_t)$ | stochastic continuous policy | Maps laser, target, previous-action, and previous-reward state to velocity commands |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The squashed and clipped policy enforces $v_t\in[0,0.2]$ m/s and $\omega_t\in[-1,1]$ rad/s |
| C2 | Collision incurs reward $-100$, reaching the target gives $+500$, and every nonterminal step incurs $-3$ plus distance-progress reward |
| C3 | The policy acts only from the 10-dimensional laser scan, target geometry, previous action, and previous reward collected in $s_t$ |

**Algorithm**: Observe $s_t$ → sample a squashed-Gaussian velocity action from SAC → execute the command and record reward and next state → store the transition in replay → update LSTM value and twin-Q networks and the entropy-regularized actor → deploy the learned mapless policy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xiang et al. [x] introduced a mapless mobile-robot navigation policy based on Soft Actor-Critic with sparse laser observations. The state combines laser data, target geometry, the previous action, and the previous reward, while the continuous action controls linear and angular velocity. LSTM value and Q networks provide temporal memory, and a shaped reward encourages progress while penalizing collisions and long episodes. The simulated Turtlebot3 study reports navigation performance comparable to a classical SLAM, A*, and DWA stack, while leaving sim-to-real transfer open.

## Problem framing

Traditional autonomous navigation splits into SLAM-based localization/mapping and path planning (A\*, RRT, dynamic window approach), but depends heavily on high-precision sensors and obstacle maps and gives the robot no intelligent understanding of the navigation task. With indoor localization (e.g., UWB) now cheap, the paper targets a **mapless** navigation method that learns the control policy directly. (This is not an MEC paper; it is a foundational DRL-method/robotics entry that grounds the corpus's SAC vocabulary.)

## System model

- **Agent.** A mobile robot whose state $s_t = (l_t, p_t, a_{t-1}, r_{t-1})$ combines laser-scan data $l_t$, target relative position/angle $p_t$, the last action, and the last reward.
- **Action.** Two-dimensional continuous velocity — linear velocity clipped to $[0, 0.2]$ m/s, angular velocity to $[-1, 1]$ — from a squashed Gaussian (tanh) policy.
- **Reward.** +500 on reaching the target, −100 on collision, otherwise −3 per step plus $k\cdot(d_{t-1}-d_t)$ (progress toward target).

## Method

- **Algorithm.** [[soft-actor-critic|SAC]] — off-policy, entropy-regularized, maximum-entropy actor-critic with the clipped double-Q trick and an inherent target-smoothing benefit from policy stochasticity.
- **Networks.** Policy, value $V_\psi$, and twin Q-networks $Q_{\phi_1}, Q_{\phi_2}$. The value and Q networks use **LSTM** hidden layers (512 units ×3) so the model carries memory of previous observations; the policy uses dense layers emitting mean and standard deviation.
- **Exploration trick.** Uniform-random actions for the first few steps, then sampling from the SAC policy.
- **Setup.** Gazebo + ROS, Turtlebot3 in a 5×5 m² arena with 8 obstacles; 1300 episodes max, replay buffer 50000, batch 128, $\gamma=0.99$, learning rates 0.0003 (Adam); trained in ~3 hours on an RTX 2070.

## Key findings

- The SAC agent learns collision-free mapless navigation and converges to a positive mean reward after early collisions (parse Fig. 4).
- The **LSTM** value/Q networks raise mean reward faster than fully-connected equivalents (an in-paper ablation, parse Fig. 4).
- Against the classical `move_base` (gmapping SLAM + amcl + A\* global + DWA local), the RL policy completes a 7-target route comparably, despite using only 10-dimensional laser data vs `move_base`'s 360-dimensional input (parse Figs. 7-8); the classical trajectory is smoother in some places.

## Limitations / future work

The authors flag **sim-to-real transfer** — good results in the virtual environment, but applying the learned policy to the real world remains future work. The reported success rate plateaus around 0.7 in training (parse Fig. 5).

## Relation to the corpus

A **foundational SAC / continuous-control** entry, analogous to how [[fujimoto-2018-td3-actor-critic]] anchors the TD3 lineage. It grounds the [[soft-actor-critic]] backbone that the corpus's MEC papers build on — e.g. the improved SAC of [[chen-2025-swipt-mec-sac]] and the multi-agent [[masac|MASAC]] of [[qin-2025-bcuav-masac]] / [[you-2025-uncertain-maritime-hasac]] — and its LSTM-augmented value function echoes the memory-augmented encoders used in UAV-MEC ([[liu-2026-jppo-en-convntm]]). The mapless laser-to-velocity control is conceptually adjacent to learned [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Continuous_Control_with_Deep_Reinforcement_Learning_for_Mobile_Robot_Navigation/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
