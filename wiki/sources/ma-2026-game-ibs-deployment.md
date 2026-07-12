---
type: source
title: "Game-Theoretic Optimization of Multiple Interfering Base Stations Deployment"
authors: ["Xiaomeng Ma", "Mohan Yu", "Haoxuan Xu", "Taohan Sun", "Yangguang Zhao", "Meiguo Gao"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3695955"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, anti-uav, interference-base-station, potential-game, soft-actor-critic, gnss-jamming, communication-jamming]
related:
  - "[[anti-uav-interference-base-station-deployment]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[soft-actor-critic]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-localization-under-jamming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Game-Theoretic Optimization of Multiple Interfering Base Stations Deployment

## Citation

Ma, X., Yu, M., Xu, H., Sun, T., Zhao, Y., & Gao, M. (2026). *Game-Theoretic Optimization of Multiple Interfering Base Stations Deployment*. **IEEE Transactions on Wireless Communications**, 25, 17724-17739. DOI: 10.1109/TWC.2026.3695955.

## TL;DR

Places multiple ground interference base stations to disrupt an unauthorized UAV's GNSS and operator link while limiting leakage into supportive devices. MIAUG is presented as an exact potential game; IBSs-DO enumerates placement combinations and trains a Soft Actor-Critic UAV path policy for each placement to score the jammer-versus-path interaction.

## Problem framing

Anti-UAV systems must choose jammer locations from the defender side, not only model an aircraft resisting attacks. More UAV disruption can also degrade friendly navigation and communication through spectral overlap and sidelobes, so deployment must balance external and internal interference against the UAV's least-interfered feasible path.

## System model

- An unauthorized UAV crosses a rectangular sensitive area toward a destination, using GNSS and an OFDM ground-operator link.
- Fixed IBSs track the UAV with directional main lobes and jam navigation and communication; supportive devices and a global controller must retain service.
- Propagation combines probabilistic LoS/NLoS path loss with Nakagami fading through air, mountains, forests, and buildings.
- The UAV minimizes a composite capture/disruption score while avoiding boundaries/obstacles; IBS positions remain fixed during one flight.
- Placement is discretized for exhaustive search, although the game definition also describes continuous rectangular strategy sets.

## Method

The Multiple IBSs Anti-UAV Game (MIAUG) assigns each IBS a utility combining UAV disruption with supportive-device performance and claims an exact potential function and pure-strategy NE. IBSs-DPPG adds the UAV's minimum-capture path and claims the optimized placement/path pair is an NE.

IBSs-DO enumerates candidate placements. For each, [[soft-actor-critic|SAC]] learns an entropy-regularized UAV trajectory; the resulting capture and supportive-device metrics fill a utility table, whose maximum selects the deployment. The stated complexity is `O(N_1...N_J G K |A|)`.

## Key findings

- For one fixed-start two-IBS experiment, the reported best positions are `(100,800) m` and `(200,750) m`.
- Averaging over ten directional takeoff points changes the reported best pair to `(100,900) m` and `(200,600) m`.
- For three IBSs, the reported best positions are `(400,700) m`, `(100,800) m`, and `(200,100) m`.
- SAC is reported to find lower-capture paths than PPO, Q-learning, Sarsa, B3L, maximum-step, and direct-to-destination baselines, but the parse gives no numerical margin or statistical test.

## Limitations / parse caveats

Exhaustive placement is exponential, IBSs cannot move during a flight, and validation uses synthetic simulation with no named software, data, hardware, seeds, or statistics. Reward weights differ by algorithm and curves are normalized, weakening direct comparisons. The finite-game existence argument is not reconciled with continuous strategy rectangles; potential-function signs conflict; NE existence is conflated with global optimality; uniqueness is claimed without proof; 2-D and 3-D motion descriptions differ; and stated grid endpoints do not match deployment counts. The composite "capture probability" is a communication/navigation disruption score, not observed physical capture.

## Relation to the corpus

[[anti-uav-interference-base-station-deployment]] reverses the usual anti-jamming viewpoint: the optimized system is the jammer network, while the UAV is the path-planning adversary. The potential-game layer is structural; the executed solution remains exhaustive placement around a learned trajectory response.

## Raw artifacts

- Parse: `raw/sources/Game-Theoretic_Optimization_of_Multiple_Interfering_Base_Stations_Deployment/Game-Theoretic_Optimization_of_Multiple_Interfering_Base_Stations_Deployment.md`
- Origin PDF: `raw/sources/Game-Theoretic_Optimization_of_Multiple_Interfering_Base_Stations_Deployment/Game-Theoretic_Optimization_of_Multiple_Interfering_Base_Stations_Deployment.pdf`
- Figures: `raw/sources/Game-Theoretic_Optimization_of_Multiple_Interfering_Base_Stations_Deployment/images/`
