---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications: A Proximal Policy Optimization Approach

## Citation

Wang, Y., Farooq, J., Ghazzai, H., & Setti, G. (2025). *Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications: A Proximal Policy Optimization Approach*. **IEEE Transactions on Mobile Computing**, 24(10), 9584-9598. DOI: 10.1109/TMC.2025.3562806.

## TL;DR

Uses [[ppo]] to jointly control 3D UAV positioning and partial computation offloading in a [[multi-uav-assisted-mec]] network with a ground BS. Each UE task can be split among UAV MEC servers and the BS, while UAVs also form access and backhaul links. The objective is low end-to-end latency under UAV computation and energy constraints. Simulations show PPO scaling better than a bi-level optimization baseline and DQN/D3QN variants as the number of UAVs and UE clusters grows.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground UEs generate divisible low-latency tasks for multiple UAV MEC servers and one cellular BS. UAV positions determine access and multi-hop backhaul rates, while each task can be split among the BS and UAVs under computation and battery limits.

**Problem & objective**: A non-convex continuous-control problem jointly positions UAVs and allocates partial offloading to minimize aggregate response latency, $\min \sum_k T_k$, while maintaining feasible access, backhaul, computation, and energy operation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf q_m$ | continuous 3-D position | Deployment or movement of UAV $m$ |
| Task split | $\alpha_{k,m}$ | continuous, $[0,1]$ | Fraction of UE $k$'s task assigned to UAV $m$ |
| BS task split | $\alpha_{k,0}$ | continuous, $[0,1]$ | Fraction of UE $k$'s task assigned to the BS |
| Backhaul route | $r_{m,m'}$ | discrete link/path choice | UAV-to-UAV or UAV-to-BS forwarding path |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Task fractions form a complete split, $\alpha_{k,0}+\sum_m\alpha_{k,m}=1$ |
| C2 | UAV and BS computation loads do not exceed their capacities |
| C3 | UAV computation, transmission, and propulsion energy stay within battery budgets |
| C4 | Access and backhaul routes remain connected and use position-dependent feasible links |
| C5 | UAV positions obey the allowed three-dimensional operating region and separation limits |

**Algorithm**: Encode positions, task loads, and link state in a continuous MDP → output joint UAV-position and task-split actions with clipped PPO updates → construct low-latency backhaul paths → evaluate latency and energy rewards → repeat until the policy converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied joint UAV positioning and computation offloading in a multi-UAV mobile edge computing network for low-latency applications. They modeled divisible user tasks, UAV access links, UAV-to-UAV and UAV-to-base-station backhaul, computation capacity, and UAV energy consumption. A proximal policy optimization controller jointly selects three-dimensional UAV positions and partial task-allocation ratios in a continuous action space. The learned deployment forms connected access and backhaul paths and adapts the task splits to the served user clusters. Simulations show lower response latency than the evaluated DQN and D3QN methods and improved scalability relative to the reported bi-level optimization baseline.

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
