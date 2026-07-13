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
  - "[[deep-q-network]]"
  - "[[uav-trajectory-control]]"
  - "[[zhou-2021-delay-sagin-task-scheduling]]"
  - "[[tiankui-zhang]]"
  - "[[yuanwei-liu]]"
  - "[[arumugam-nallanathan]]"
created: 2026-07-14
updated: 2026-07-14
---

# Trajectory Optimization for UAV Emergency Communication With Limited User Equipment Energy: A Safe-DQN Approach

## Citation

Zhang, T., Lei, J., Liu, Y., Feng, C., & Nallanathan, A. (2021). *Trajectory Optimization for UAV Emergency Communication With Limited User Equipment Energy: A Safe-DQN Approach*. **IEEE Transactions on Green Communications and Networking, 5**(3), 1236-1247. DOI: 10.1109/TGCN.2021.3068333.

## TL;DR

Trains a Lyapunov-filtered DQN trajectory policy for one emergency UAV base station, maximizing uploaded data while constraining expected user-energy cost and filtering actions whose next grid point lies inside a modeled obstacle.

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

## Raw artifacts

- Parse: `raw/sources/Trajectory_Optimization_for_UAV_Emergency_Communication_With_Limited_User_Equipment_Energy_A_Safe-DQN_Approach/Trajectory_Optimization_for_UAV_Emergency_Communication_With_Limited_User_Equipment_Energy_A_Safe-DQN_Approach.md`
- Original PDF and extracted figures are in the same folder.
