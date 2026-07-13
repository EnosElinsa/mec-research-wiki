---
type: source
title: "Scalable UAV Multi-Hop Networking via Multi-Agent Reinforcement Learning With Large Language Models"
authors: ["Yanggang Xu", "Jirong Zha", "Weijie Hong", "Xiangmin Yi", "Geng Chen", "Jianfeng Zheng", "Chen-Chun Hsia", "Xinlei Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3669346"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 11173-11190"
tags: [source, uav-swarm, multi-hop-network, emergency-networking, marl, large-language-model, knowledge-distillation]
related:
  - "[[multi-hop-uav-emergency-networking]]"
  - "[[llm-guided-marl-policy-distillation]]"
  - "[[task-oriented-grouped-uav-marl]]"
  - "[[connectivity-preserving-uav-behavioral-loss]]"
  - "[[ppo]]"
  - "[[mappo]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[uav-mobile-relaying]]"
  - "[[xinlei-chen]]"
created: 2026-07-14
updated: 2026-07-14
---

# Scalable UAV Multi-Hop Networking via Multi-Agent Reinforcement Learning With Large Language Models

## Citation

Xu, Y., Zha, J., Hong, W., Yi, X., Chen, G., Zheng, J., Hsia, C.-C., & Chen, X. (2026). *Scalable UAV Multi-Hop Networking via Multi-Agent Reinforcement Learning With Large Language Models*. **IEEE Transactions on Mobile Computing, 25**(7), 11173-11190. DOI: 10.1109/TMC.2026.3669346.

## TL;DR

MRLMN trains decentralized UAV policies for disaster-area multi-hop relaying by combining task-oriented agent groups, relay-aware rewards, a connectivity-preserving auxiliary loss, and soft action targets distilled from offline GPT-4o deployment plans. The LLM is removed at deployment. Simulation results favor MRLMN as area and swarm size grow, but do not isolate the LLM from a simpler heuristic advisor or account for energy, interference, signaling overhead, or real flight constraints.

## Problem and system model

[[multi-hop-uav-emergency-networking]] connects scattered mobile UEs to surviving fixed base stations through a dynamic UAV relay graph. The slotted model contains $U$ UAVs, $M$ UEs, and $G$ base stations. A UAV is connected if it has a qualifying direct base-station link or can reach one through connected UAVs; each UE selects the eligible UAV with maximum data rate, and backhaul uses the fewest-hop qualifying path.

UAV-UE links use probabilistic LoS/NLoS path loss, while UAV-UAV and BS-UAV links use free-space LoS models. Connectivity requires SNR above a threshold. Each UAV moves at fixed speed using nine planar actions: eight directions and hover. Although positions are represented in 3-D, altitude is not controlled.

The main simulation covers about 3.5 km x 3.5 km with about 150 mobile UEs, 18 UAVs, and three base stations. Training runs for 25,000 episodes of 400 slots, uses four UAV groups and five-hidden-layer tanh policy/critic networks, and queries GPT-4o as an offline advisor.

## Method

The base learner is decentralized independent PPO. UAVs exchange a structured summary of node positions, link SNRs, UE rates, and connectivity, and concatenate it with local position and incident-link information.

[[task-oriented-grouped-uav-marl]] sorts UAVs by initial distance to the nearest base station and partitions them by quantiles. Near-base-station groups emphasize relay service and distant groups emphasize UE access. Per-agent rewards combine the team objective, directly served UE rate, and traffic relayed for downstream nodes.

[[connectivity-preserving-uav-behavioral-loss]] adds an auxiliary log-policy loss when a critical near-base-station UAV loses all BS links, steering it toward the BS with highest SNR. This seeks to prevent one relay failure from cascading through the topology.

For [[llm-guided-marl-policy-distillation]], GPT-4o receives a simplified grid, base-station locations, UE counts, connectivity instructions, output constraints, and few-shot examples. A rule-based verifier discards unreachable, out-of-bounds, poorly connected, isolated, or insufficient-coverage plans. Hungarian matching assigns UAVs to accepted grid-center targets, and directional cosine similarities become soft targets over the nine actions. The distillation and behavioral terms augment the PPO objective; cached guidance is refreshed periodically during training, while deployment uses only decentralized MARL policies.

## Key findings

- Over 10 million training steps in the 18-UAV setting, the prose describes MRLMN stabilizing above 0.8 team objective. GVis remains below it, MAPPO and GA2C stabilize between 0.4 and 0.6, and IA2C/MAA2C fluctuate around 0.4.
- As square area grows from 6.76 to 14.44 km2 with 18 UAVs, MRLMN averages about 27% higher UE coverage than GVis, GA2C, and MAPPO. In the largest settings its available-UAV ratio exceeds the best alternative by about 17%.
- With area fixed and UAV count increasing from 12 to 24, the prose reports average gains of 23% in UE coverage, 52% in data rate, and 19% in UAV availability over the compared methods.
- At 14.44 km2 with 18 UAVs, full MRLMN reports 46% connected UEs, 88% available UAVs, and 5.2 Mbps, versus 40%, 82%, and 4.5 Mbps without grouping and reward decomposition. Removing any one of grouping/reward decomposition, LLM distillation, or behavioral constraints causes an average decline of at least 6% in coverage and 10% in rate across the tested UAV counts.
- Increasing independently trained policies from four to 18 raises coverage from 45% to 65%, data rate from 5.1 to 7.4 Mbps, and UAV availability to about 98%, while training time increases from 20 to 40 hours. Each sharing configuration uses three independent runs.
- Fig. 8's snapshots at slots 1, 100, 200, and 400 qualitatively show an emerging multi-hop topology. This is figure-derived evidence and provides no additional comparator values.

## Limitations

Evaluation is simulation-only. Motion is planar and fixed-speed, with no altitude control, acceleration, collision avoidance, battery state, or no-fly zones. UAV-UAV and BS-UAV links assume unobstructed LoS, and fixed bandwidth by link class avoids interference rather than optimizing it. Energy use, load balancing, replacement continuity, and detailed physical-layer control remain future work.

The global structured summary assumes exchange of all node positions, pairwise SNRs, UE rates, and connectivity, but signaling cost, delay, packet loss, staleness, and partition behavior are not quantified. Groups are fixed from initial nearest-BS distance, with no described dynamic regrouping.

The GPT-4o environment is simplified and prompt-sensitive. Exact prompts, few-shot examples, verifier thresholds, query period, and reproducibility artifacts are absent from the parse. The no-LLM ablation supports the combined distillation module, but there is no comparison with a handcrafted advisor producing the same grid targets, so the incremental value of language-model reasoning is not isolated. The complexity claim that $O(U^3)$ Hungarian matching is below $O(U L H^2)$ neural computation is parameter-dependent, not universal.

The algorithm calls $D$ a PPO replay buffer even though PPO is normally on-policy, without explaining how stale samples are excluded. Weijie Hong's biography contains the malformed sentence "He is also Ltd."; the missing position cannot be reconstructed from context.

## Relation to the corpus

This source applies [[ppo]] and [[knowledge-distillation-for-drl]] to topology formation rather than MEC task offloading. It extends [[uav-mobile-relaying]] from local movement or relay selection to a large coordinated emergency network. Recurring author [[xinlei-chen]] also connects the paper to the corpus's UAV control and sensing work.

## Raw artifacts

- Parse: `raw/sources/Scalable_UAV_Multi-Hop_Networking_via_Multi-Agent_Reinforcement_Learning_With_Large_Language_Models/Scalable_UAV_Multi-Hop_Networking_via_Multi-Agent_Reinforcement_Learning_With_Large_Language_Models.md`
- Origin PDF: `raw/sources/Scalable_UAV_Multi-Hop_Networking_via_Multi-Agent_Reinforcement_Learning_With_Large_Language_Models/Scalable_UAV_Multi-Hop_Networking_via_Multi-Agent_Reinforcement_Learning_With_Large_Language_Models.pdf`
- Figures: `raw/sources/Scalable_UAV_Multi-Hop_Networking_via_Multi-Agent_Reinforcement_Learning_With_Large_Language_Models/images/`
