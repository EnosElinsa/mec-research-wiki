---
type: source
title: "Multi-UAV-Assisted MEC in Internet of Vehicles With Combined Multi-Modal Semantic Communication Under Jamming Attacks"
authors: ["Shuai Liu", "Helin Yang", "Mengting Zheng", "Liang Xiao"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3550965"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, semantic-communication, anti-jamming, multi-agent-td3, uav-trajectory-control]
related:
  - "[[vehicular-mec]]"
  - "[[multi-modal-semantic-communication]]"
  - "[[semantic-communication]]"
  - "[[anti-jamming-mec]]"
  - "[[multi-agent-td3]]"
  - "[[uav-trajectory-control]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
  - "[[shao-2024-drl-antijamming-mec]]"
created: 2026-07-07
updated: 2026-11-03
modeling_card: required
---

# Multi-UAV-Assisted MEC in Internet of Vehicles With Combined Multi-Modal Semantic Communication Under Jamming Attacks

## Citation

Liu, S., Yang, H., Zheng, M., & Xiao, L. (2025). *Multi-UAV-Assisted MEC in Internet of Vehicles With Combined Multi-Modal Semantic Communication Under Jamming Attacks*. **IEEE Transactions on Mobile Computing**, 24(8), 7600-7614. DOI: 10.1109/TMC.2025.3550965. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Combines UAV-assisted IoV MEC, [[multi-modal-semantic-communication]], and anti-jamming control. The SC-MA-TD3 policy coordinates UAV trajectories, user associations, and channel selections so UAVs can receive image and text semantic tasks under a jammer while reducing communication/computation delay and preserving semantic accuracy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Image collection points, image-transmission vehicles, text-transmission RSUs, $N$ UAV MEC nodes, and one jammer form a multi-modal IoV network. In each slot every UAV hovers near an associated vehicle, receives one image and one text semantic task over orthogonal channels, and processes them with DeepSC-VQA; image channels have unequal bandwidths and are selected, while text channels are fixed.

**Problem & objective**: Problem P1 (13), non-convex and NP-hard, jointly selects UAV trajectory $L$, channel selection $\rho$, and user association $\delta$ to maximize semantic accuracy and minimize total communication and computation delay $D_t^{\mathrm{sum}}$ (12). The parsed equation is garbled, so the exact objective expression should be checked against the published paper.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $L$ | continuous positions | Hover positions of the UAVs across slots |
| Channel selection | $\rho$ | discrete | Image-task channel chosen by each UAV |
| User association | $\delta$ | binary | Image-transmission and text-transmission user served by each UAV |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Semantic accuracy is at least the threshold $\varpi_{th}$ |
| C2 | Channel selection respects the limited number of channels |
| C3 | Each episode has $T$ time slots |
| C4-C5 | Each UAV associates with one image-transmission user and one text-transmission user per slot |
| C6 | Inter-UAV distance stays above the minimum to avoid collisions |

**Algorithm**: Reformulate P1 as an MDP → SC-MA-TD3 agents choose trajectories, associations, and channels → compute semantic-accuracy and delay rewards → update centralized critics and decentralized actors until the policy converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied multi-UAV-assisted vehicular MEC with combined multi-modal semantic communication under jamming attacks. They formulated a dynamic non-convex control problem that balances semantic accuracy against communication and computation delay while selecting UAV trajectories, modal-user associations, and channels. The problem was reformulated as a Markov decision process and solved with SC-MA-TD3, a multi-agent deterministic policy-gradient method that keeps semantic accuracy in the reward loop. The UAVs receive image and text information, process traffic-condition tasks, and adapt their actions to the jammer and channel state. Simulations report higher semantic accuracy and lower delay than the evaluated semantic and conventional communication baselines.

## Problem framing

IoV applications carry image and text information, but bit-level transmission wastes spectrum and MEC-only designs do not compress semantic payloads. Semantic communication saves channel resources, yet UAV-assisted semantic MEC becomes fragile when a jammer disrupts any modality link. The paper targets the joint delay/semantic-accuracy problem under dynamic jamming.

## System model

The network includes image collection points, image-transmission vehicles, text-transmission RSUs, multiple UAVs, and one jammer. UAVs collect image and text semantic information, add their own aerial perspective, decode semantic tasks, and compute traffic-condition results. The optimization covers UAV trajectories, association between UAVs and modal users, and offloading-channel selection under semantic accuracy and UAV-distance constraints.

## Method

The paper formulates the dynamic non-convex optimization as an MDP and proposes SC-MA-TD3, a multi-agent [[td3]]-style DRL method with semantic communication in the loop. The agent observes jamming/environment state, chooses UAV motion, user association, and channel actions, and learns a policy that balances SINR, semantic accuracy, and delay.

## Key findings

- The contributions section reports semantic accuracy improvements of at least 6.10% and communication/computation delay reductions of 29.07% compared with traditional approaches.
- Fig. 4 reports higher converged reward than SC-D4N, SC-MA-DDPG, fixed-action SC-MA-TD3, and non-semantic baselines.
- Under changing jamming power, the parse reports that SC-MA-TD3 achieves the shortest delays and highest semantic accuracy among compared schemes.
- When the average number of semantic symbols changes, semantic communication saves channel resources; the parsed example reports at least 29.07% delay improvement at `k = 4` versus non-semantic communication.

## Limitations / future work

Evaluation is simulation-based. The conclusion states future work will explore how same-modality users performing different tasks are affected in semantic communication.

## Relation to the corpus

This is the vehicular counterpart to [[sun-2024-mfris-semantic-antijamming]] and [[shao-2024-drl-antijamming-mec]]: all three address hostile channels, but this paper focuses on multi-modal semantic task reception in IoV rather than MF-RIS robust optimization or generic anti-jamming MEC resource management. It strengthens [[vehicular-mec]], [[semantic-communication]], [[anti-jamming-mec]], [[multi-agent-td3]], and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Multi-UAV-Assisted_MEC_in_Internet_of_Vehicles_With_Combined_Multi-Modal_Semantic_Communication_Under_Jamming_Attacks/Multi-UAV-Assisted_MEC_in_Internet_of_Vehicles_With_Combined_Multi-Modal_Semantic_Communication_Under_Jamming_Attacks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
