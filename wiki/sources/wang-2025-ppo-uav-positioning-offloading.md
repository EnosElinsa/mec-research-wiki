---
type: source
title: "Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications: A Proximal Policy Optimization Approach"
authors: ["Yuhui Wang", "Junaid Farooq", "Hakim Ghazzai", "Gianluca Setti"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3562806"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 24, no. 10, Oct. 2025"
tags: [source, multi-uav-assisted-mec, task-offloading, uav-positioning, ppo, latency-minimization, energy-efficiency]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[ppo]]"
  - "[[load-balancing-uav-mec]]"
  - "[[wang-2022-cat-rat-fmec-trajectory]]"
  - "[[hao-2024-clp-multiuav-priority-offloading]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications: A Proximal Policy Optimization Approach

## Citation

Wang, Y., Farooq, J., Ghazzai, H., & Setti, G. (2025). *Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications: A Proximal Policy Optimization Approach*. **IEEE Transactions on Mobile Computing**, 24(10), 9584-9598. DOI: 10.1109/TMC.2025.3562806.

## TL;DR

Uses [[ppo]] to jointly control 3D UAV positioning and partial computation offloading in a [[multi-uav-assisted-mec]] network with a ground BS. Each UE task can be split among UAV MEC servers and the BS, while UAVs also form access and backhaul links. The objective is low end-to-end latency under UAV computation and energy constraints. Simulations show PPO scaling better than a bi-level optimization baseline and DQN/D3QN variants as the number of UAVs and UE clusters grows.

## Problem framing

UAV MEC is useful where terrestrial edge infrastructure is missing or overloaded, but positioning and offloading are tightly coupled: UAV locations determine access/backhaul latency, while task allocation determines UAV compute load and energy draw. The paper targets low-latency applications such as AR, autonomous driving, live video, emergency response, and smart-city surveillance, where static or heavily discretized methods become brittle in dynamic multi-UAV networks.

## System model

- The network has one cellular BS, multiple UAVs, and ground UEs.
- Each UAV has separate access and backhaul antennas, supporting UAV-UE access and UAV-UAV or UAV-BS backhaul.
- Each UE task has workload, data size, and delay tolerance; the task can be split into proportions assigned to the BS and to individual UAVs.
- Backhaul paths are selected to minimize transmission latency across the UAV network.
- Energy includes UAV computation, data transmission, and propulsion/hovering components, with UAV battery and computation-capacity constraints.
- The model uses air-to-ground and air-to-air path-loss expressions and explicitly ties UAV positions to achievable rates and latency.

## Method

The paper formulates coupled UAV deployment and task allocation as a reinforcement-learning problem with continuous state and action spaces. The PPO controller outputs UAV positioning and offloading decisions, using clipped policy updates for stability. Baselines include a bi-level optimization method, DQN, and D3QN-style value-based learning.

## Key findings

- The learned UAV placement forms a connected backhaul network between the BS and UE clusters, with access UAVs moving toward the clusters and a backhaul UAV bridging them to the BS.
- Task splits stabilize after roughly 800 training episodes in the reported two-cluster scenario; each cluster predominantly offloads to the nearest learned access UAV.
- During testing, task splits stabilize within about 14 steps, showing the learned policy can adapt quickly to the tested network conditions.
- In random-UAV-failure tests, larger fleets recover with less latency disruption; the 4-UAV case has the strongest redundancy after one UAV fails.
- Compared with the bi-level baseline and DQN, PPO reports lower average response latency in more complex multi-cluster settings; the baseline fails to converge once the UAV count becomes large in the reported 4-cluster case.
- PPO stays close to the bi-level baseline on total energy while outperforming DQN, and for four or more UAVs it reports lower total energy than both the baseline and DQN/D3QN variants.

## Limitations / future work

The evaluation is simulation-only. The paper assumes UE positions can be retrieved in real time, uses fixed UE positions in the modeled scenario, and does not validate the policy on hardware. The conclusion names dynamic user mobility, heterogeneous UAV capabilities, distributed learning, energy-efficient strategies, and deployment constraints as future directions.

## Relation to the corpus

This paper is a direct [[ppo]] entry in the [[multi-uav-assisted-mec]] trajectory/offloading family. It complements [[liu-2026-jppo-en-convntm]], which uses a hybrid-action PPO variant with a memory-augmented encoder for high-density mobility, and [[wang-2022-cat-rat-fmec-trajectory]], where RAT combines twin-DQN and matching for flying-MEC trajectory and association. Its distinguishing role is continuous PPO control over both UAV placement and partial offloading, with explicit backhaul connectivity to a BS and failure-resilience evaluation.

## Raw artifacts

- `raw/sources/Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications A Proximal Policy Optimization Approach/Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications A Proximal Policy Optimization Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
