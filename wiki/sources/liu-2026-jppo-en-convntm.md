---
type: source
title: "Multi-UAV Path Planning for Mobile Edge Computing with High-Density Mobile Devices"
authors: ["Lihan Liu", "Hongrui Miao", "Chunhui Qu", "Zhuwei Wang", "Haijun Zhang", "Zhidu Li"]
year: 2026
url: ""
venue: ""
tags: [uav, mec, drl, ppo, ntm, path-planning, high-density, smart-city]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[high-density-mobile-device-scenarios]]"
  - "[[j-ppo]]"
  - "[[en-convntm]]"
  - "[[stn]]"
  - "[[ppo]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[pomdp]]"
  - "[[hybrid-action-decision-making]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[uav-charging-scheduling]]"
  - "[[en-convntm-beats-baselines]]"
  - "[[charging-stations-improve-efficiency]]"
  - "[[uav-count-inverted-u-energy]]"
created: 2026-05-28
updated: 2026-05-28
---

# Multi-UAV Path Planning for Mobile Edge Computing with High-Density Mobile Devices

## Citation

Liu, L., Miao, H., Qu, C., Wang, Z., Zhang, H., & Li, Z. (2026). *Multi-UAV Path Planning for Mobile Edge Computing with High-Density Mobile Devices*. (Authors affiliated with Beijing Wuzi University, University of Tennessee Knoxville, Chinese Academy of Sciences (AIR), Beijing University of Technology, USTB, and CQUPT.)

## TL;DR

Proposes [[j-ppo-en-convntm]], a deep reinforcement learning framework for jointly planning multi-UAV trajectories, task-offloading ratios, and charging decisions in dense, mobile IoT environments. Combines [[j-ppo]] (a PPO variant supporting hybrid continuous/discrete actions) with [[en-convntm]] (a Convolutional Neural Turing Machine extended with a [[stn|spatial transformer network]] and 3-D external memory). Reports significant gains over four [[j-ppo-baselines|j-PPO baselines]] and four mainstream DRL algorithms on the [[equilibrium-efficiency-metric]].

## Problem framing

The authors target a gap in [[multi-uav-assisted-mec]]: prior work assumes static or low-mobility users, so existing solutions degrade in [[high-density-mobile-device-scenarios]] (urban centers, large events). They cast the joint problem as a [[pomdp]] over:

- continuous UAV positions $Q_{u,n}$
- continuous offloading ratios $\lambda_{u,d,n} \in [0,1]$ per (UAV, device) pair
- a discrete charging indicator $\xi_{u,n} \in \{0,1\}$ per UAV

Optimization objective is the multi-objective [[equilibrium-efficiency-metric]] $\Omega_n = \psi_n f_n / \kappa_n$, combining data-collection coefficient $\psi_n$, [[spatial-equity-index]] $f_n$, and [[energy-expenditure-coefficient]] $\kappa_n$. Constraints bound per-step UAV displacement and enforce non-negative residual energy.

## System model (Section III)

| Submodel | Key assumption | Reference |
|---|---|---|
| IoT mobility | [[gauss-markov-mobility-model]] for speed and direction | [[hp-mobility-models]] |
| Channel | LoS UAV→ground, OFDMA, no inter-device interference | [5], [32] |
| Compute | Local + offloaded split, cubic-frequency energy model | standard MEC |
| Charging | UAV hovers at station, adds $q\xi_{u,n} E_{u,n}^{\max}$ per step | [10] |
| Flight | Constant cruise speed $v_u$, fixed altitude $h_u$ | [33] |

## Method (Section IV)

The framework, named **j-PPO+EN-ConvNTM**, has two cooperating modules:

1. **[[en-convntm]]** — input observation $\mathbf{o}_n$ is a 3-channel grid (devices/visit-counts, UAV-energies/charging-stations, device-visit-history). It passes through a [[stn]], then into a [[ntm|Neural Turing Machine]] variant with a 3-D external memory and an *enhancement* operation that uses attention to amplify operationally-significant features.
2. **[[j-ppo]]** — extends [[ppo]] with a hybrid clipped objective that mixes the continuous-action probability ratio (UAV trajectory) and the discrete-action ratio (offloading + charging) via a weight $c_3$. Actor/critic share parameters; loss adds a value-function term and an entropy bonus.

The full training loop (Algorithm 1) runs $\tilde{N}$ episodes per iteration of $N$ time steps, samples hybrid actions, computes [[gae|GAE]] advantages, then updates over segmented mini-batches of length $K$ to break sample correlation introduced by sequential NTM access.

## Experiments (Section V)

- **Setup.** PyTorch 2.1.0; 2× RTX 4090 (Ubuntu 20.04). 256 mobile IoT devices in 160 m × 160 m. 3000 training iterations. $h_u=35$ m, $v_u=10$ m/s, $\eta_u=0.1$, $\eta_d=1$, $q=0.25$, $\gamma=0.99$, $l_r=2.5\times10^{-4}$, $K=5$, $M=400$.
- **Hyperparameters.** Best $\Omega$ at $c_1=0.1$, $c_2=0.01$, $c_3=0.5$. See [[finding-optimal-loss-entropy-weight-coefs]].
- **Baselines (within the j-PPO family):** j-PPO, j-PPO+ConvNTM, j-PPO+ConvLSTM, j-PPO+NeuralMap.
- **Cross-DRL baselines:** DDPG, A2C, TD3, DQN.

## Findings

- [[en-convntm-beats-baselines]] — j-PPO+EN-ConvNTM dominates all four j-PPO ablations on $\Omega$, with the gap widening as the number of UAVs grows (e.g. +21.21% vs j-PPO+ConvNTM at 5 UAVs).
- [[neuralmap-loses-spatial-info]] — j-PPO+NeuralMap underperforms by up to 76.2% on $\Omega$ at 2 UAVs because compressing 3-D observations to 1-D vectors collides UAV identities.
- [[uav-count-inverted-u-energy]] — energy-expenditure coefficient $\kappa_n$ follows an inverted-U as UAV count increases at fixed charging-station count.
- [[charging-stations-improve-efficiency]] — adding charging stations monotonically improves $\Omega$, $\psi$, $f$ and reduces $\kappa$.
- [[hybrid-action-beats-pure-drl]] — DDPG/TD3/DQN/A2C all struggle vs j-PPO+EN-ConvNTM because they target either purely continuous or purely discrete action spaces.

## Theory notes

- Convergence: under smooth reward and compact policy space, sublinear bound $\mathbb{E}[\|\theta_k - \theta^*\|^2] \le F/k$ (cited from [34]).
- Linear-MDP complexity: $O(d_{sa}^2 N_h^3 / \varepsilon^2)$.

## Limitations / future work

The authors note results are simulation-only, and call out hardware constraints and uplink interference as open issues for real-world deployment. See [[query-real-world-validation-of-jppo-en-convntm]].

## Raw artifacts

- `raw/sources/Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/full.md` — parsed text
- `raw/sources/Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/9de84584-c0e5-4b27-b085-5256cd556869_origin.pdf` — original PDF
- `raw/sources/Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/images/` — extracted figures
