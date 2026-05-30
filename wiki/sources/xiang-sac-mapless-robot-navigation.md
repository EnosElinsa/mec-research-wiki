---
type: source
title: "Continuous Control with Deep Reinforcement Learning for Mobile Robot Navigation"
authors: ["Jiaqi Xiang", "Qingdong Li", "Xiwang Dong", "Zhang Ren"]
year:
url: ""
venue: ""
tags: [source, soft-actor-critic, continuous-control, robot-navigation, drl, mapless-navigation]
related:
  - "[[soft-actor-critic]]"
  - "[[ddpg]]"
  - "[[ppo]]"
  - "[[uav-trajectory-control]]"
  - "[[fujimoto-2018-td3-actor-critic]]"
  - "[[chen-2025-swipt-mec-sac]]"
created: 2026-05-31
updated: 2026-05-31
---

# Continuous Control with Deep Reinforcement Learning for Mobile Robot Navigation

## Citation

Xiang, J., Li, Q., Dong, X., & Ren, Z. *Continuous Control with Deep Reinforcement Learning for Mobile Robot Navigation*. Venue / year / DOI: **not in parse** (the MinerU parse contains no publication line; authors affiliated with the School of Automation Science and Electrical Engineering and the Beijing Advanced Innovation Center for Big Data and Brain Computing, Beihang University). An IEEE Xplore record exists for this title (document 8996652), but the venue name and year are not stated in the parse, so they are left blank rather than guessed.

## TL;DR

An end-to-end, **mapless** autonomous-navigation method for a mobile robot trained with **Soft Actor-Critic (SAC)** ([[soft-actor-critic]]). The policy takes low-dimensional laser-scan data plus target information (and the previous action and reward) as input and outputs continuous linear and angular velocity. Trained in Gazebo/ROS on a Turtlebot3, it reaches performance comparable to a traditional SLAM + A\* + DWA navigation stack while using only **10-dimensional** sparse laser data (vs 360-dimensional for the classical `move_base` planner).

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
