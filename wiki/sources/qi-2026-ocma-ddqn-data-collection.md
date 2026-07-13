---
type: source
title: "Robust and Energy-Efficient Multi-UAV Trajectory Planning for Data Collection: A Game-Theoretic and Deep Reinforcement Learning Approach"
authors: ["Nan Qi", "Hua Jiang", "Sa Xiao", "Daolong Wu", "Fuhui Zhou", "Chunguo Li", "Shi Jin"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3695901"
venue: "IEEE Transactions on Green Communications and Networking, vol. 10, pp. 3086-3101"
tags: [source, multi-uav, data-collection, trajectory-planning, ddqn, potential-game, intermittent-connectivity, lstm, anti-jamming, energy-efficiency]
related:
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[lstm-interruption-compensation]]"
  - "[[experience-value-circles]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[ddqn]]"
  - "[[potential-game]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[fuhui-zhou]]"
  - "[[shi-jin]]"
created: 2026-07-14
updated: 2026-07-14
---

# Robust and Energy-Efficient Multi-UAV Trajectory Planning for Data Collection: A Game-Theoretic and Deep Reinforcement Learning Approach

## Citation

Qi, N., Jiang, H., Xiao, S., Wu, D., Zhou, F., Li, C., & Jin, S. (2026). *Robust and Energy-Efficient Multi-UAV Trajectory Planning for Data Collection: A Game-Theoretic and Deep Reinforcement Learning Approach*. **IEEE Transactions on Green Communications and Networking, 10**, 3086-3101. DOI: 10.1109/TGCN.2026.3695901.

## TL;DR

Combines an exact-potential-game cooperation model with distributed DDQN for fixed-altitude multi-UAV data collection under directional jamming and intermittent links. UAVs exchange maps and replay experience according to distance-dependent value circles, while an online LSTM predicts neighbor actions during short disconnections. The reported gains are simulation results for up to four UAVs and do not establish robustness to long outages, changing jammers, or real flight dynamics.

## Problem and system model

- Multiple fixed-altitude UAVs collect data from ground base stations in a gridded airspace containing buildings or no-fly zones and directional jammers.
- Each UAV chooses among four cardinal moves, hovering, and landing. A move spans four one-second communication slots, and TDMA separates data collection from inter-UAV exchange.
- Hybrid LoS/NLoS path loss, shadowing, and jammer interference determine the link rate. A UAV selects the base station with the highest rate and collects data only when the rate threshold is met.
- Each agent observes a compressed relative global map and a cropped local map containing task nodes, jammers, obstacles, the landing zone, its position, and remaining battery.
- Jammer positions, powers, beamwidths, and counts are randomized at the start of an episode but remain fixed during that episode.

The bilateral interaction game defines each UAV's utility as collected-data reward minus propulsion energy and pairwise cooperation cost. Symmetric pairwise costs make it an exact [[potential-game]], so a pure-strategy Nash equilibrium exists. In the learned implementation, movement, collection, cooperation, collision, landing, and remaining-energy terms form the DDQN reward.

## Method

[[opportunistic-cooperative-multi-uav-ddqn]] uses independent replay buffers and policy/target networks. Connected neighbors share explored-grid information and experience; [[experience-value-circles]] set the exchange probability from inter-UAV distance so that very close observations are treated as redundant and very distant experience as less useful relative to communication cost.

When a link is interrupted, [[lstm-interruption-compensation]] predicts the neighbor's next action from an eight-step history of previous actions, normalized coordinates, and a flattened $5 \times 5$ local map. Each agent trains a two-layer, 64-unit LSTM online within an episode. A prediction is used only when its Softmax confidence exceeds 0.95; otherwise the agent retains the last valid neighbor state. DDQN training is performed offline, distributed execution uses local forward inference, and the LSTM continues adapting within each episode.

## Key findings

- Cooperative methods converge after about 2,500 episodes in Fig. 8. The paper reports about **31% higher converged reward** than non-cooperative DDQN in the abstract and Fig. 9 discussion.
- Fig. 9 reports post-convergence collection ratios of **0.923** for OCMA-DDQN-LSTM, **0.911** for its Dueling-DQN variant, **0.908** for adapted MADDPG, and **0.897** for adapted MAPPO. These are figure-derived simulation results, not measured flight performance.
- Figs. 9-10 indicate that the proposed method lands with more than 10% battery remaining and approaches zero collision resets after convergence. Both claims are figure-derived and depend on the paper's reward and grid-reset definitions.
- Fig. 11 reports approximately **80% prediction accuracy for the first two steps after disconnection**. The paper relates this short horizon to movement remaining inside the observed $5 \times 5$ local map; it does not show that accuracy persists through long outages.
- Fig. 13 supports the tested experience-circle thresholds $d_1=100$ m and $d_2=200$ m. Larger $d_2$ raises sharing and communication cost, while larger $d_1$ lowers sharing frequency; these are sensitivity results for the simulated setting.
- Fig. 14(b) shows **95%-99%** collection ratios with three and four UAVs only when total base-station data is also increased to 90 and 120 bit/Hz. Fig. 14(d) shows approximately **80%** at 50 W jammer power with two 60-degree jammers. These figure-derived values do not isolate swarm size from task-load scaling.

The energy calculations give about 168.49 W for hovering, 160.65 W at 2.5 m/s, 642.6 J of propulsion per four-second move, and 40 J for static communication and computation. The reported 0.28 ms Jetson Nano inference latency is estimated from FLOPs rather than measured on deployed hardware.

## Limitations

Motion is deterministic and grid-discrete in two dimensions at fixed altitude; the main scenario omits continuous heading, acceleration, altitude control, and smooth flight dynamics. Jammers do not move or change within an episode. The short-outage predictor assumes stale neighbor history remains informative, and the paper acknowledges degradation under longer interruptions or rapidly changing interference.

Evaluation is simulation-only and covers at most four UAVs while increasing task load with swarm size. It does not measure communication overhead, decentralized scaling, hardware inference latency, or algorithm energy. The 0.95 confidence threshold has no reported ablation.

The parse also contains unresolved inconsistencies: the scenario describes eight base stations but gives a ten-entry initial-data vector; the jammer-distance term in one SINR equation appears to reuse a base-station distance; another utility equation is malformed; and action ordering differs between sections. Algorithm 1 says the LSTM predicts grid exploration, whereas the detailed model predicts neighbor actions and positions. The adapted CTDE baselines' missing-information handling is not specified in enough detail to independently establish comparator fairness.

## Relation to the corpus

This source combines [[uav-data-collection]], [[uav-trajectory-control]], and [[ddqn]] with an explicit game-theoretic price for cooperation. Its distinctive contribution is not generic multi-agent learning, but distance-conditioned sharing plus confidence-filtered short-outage prediction. The propulsion accounting follows [[rotary-wing-propulsion-energy-model]]. Recurring authors [[fuhui-zhou]] and [[shi-jin]] connect it to the corpus's broader UAV optimization and intelligent-wireless work.

## Raw artifacts

- Parse: `raw/sources/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach.md`
- Origin PDF: `raw/sources/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach.pdf`
- Figures: `raw/sources/Robust_and_Energy-Efficient_Multi-UAV_Trajectory_Planning_for_Data_Collection_A_Game-Theoretic_and_Deep_Reinforcement_Learning_Approach/images/`
