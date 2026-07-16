---
type: source
title: "Quantum Multi-Agent Reinforcement Learning for Cooperative Mobile Access in Space-Air-Ground Integrated Networks"
authors: ["Gyu Seon Kim", "Yeryeong Cho", "Jaehyun Chung", "Soohyun Park", "Soyi Jung", "Zhu Han", "Joongheon Kim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3599683"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 1, pp. 1200-1218"
modeling_card: required
tags: [source, quantum-marl, sagin, cubesat, hale-uav, scheduling, energy-efficiency]
related:
  - "[[quantum-marl-sagin-access]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[non-terrestrial-network]]"
  - "[[multi-agent-q-learning]]"
  - "[[pytorch]]"
  - "[[zhu-han]]"
  - "[[gyu-seon-kim]]"
  - "[[soyi-jung]]"
  - "[[soohyun-park]]"
  - "[[joongheon-kim]]"
created: 2026-07-14
updated: 2026-07-16
---

# Quantum Multi-Agent Reinforcement Learning for Cooperative Mobile Access in Space-Air-Ground Integrated Networks

## Citation

Kim, G. S., Cho, Y., Chung, J., Park, S., Jung, S., Han, Z., & Kim, J. (2026). *Quantum Multi-Agent Reinforcement Learning for Cooperative Mobile Access in Space-Air-Ground Integrated Networks*. **IEEE Transactions on Mobile Computing, 25**(1), 1200-1218. DOI: 10.1109/TMC.2025.3599683.

## TL;DR

Represents each CubeSat/HALE-UAV scheduling bit with one qubit and uses projection-valued measurement inside centralized-critic multi-agent learning, targeting differentiated ground-station capacity and residual-energy preservation in a simulated SAGIN.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple ground stations cooperatively select visible CubeSats and fixed-wing HALE-UAVs for differentiated mobile access in a space-air-ground integrated network. CubeSat links use orbital geometry, channel capacity, QoS, and sun-side or dark-side energy models, while HALE-UAV links use air-to-ground propagation and aerodynamic energy models. Access is controlled by binary device scheduling rather than a separate multiple-access allocation.

**Problem & objective**: The cooperative scheduling problem is formulated as a multi-agent MDP whose policy maximizes expected cumulative reward, $\max_\pi \mathbb E_\pi[\sum_t\gamma^t R_i(t)]$, combining ground-station QoS and capacity with high and balanced residual energy for CubeSats and HALE-UAVs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| CubeSat access schedule | $x_j^i(t)$ | binary, $\{0,1\}$ | Whether ground station $i$ selects CubeSat $j$ in slot $t$ |
| HALE-UAV access schedule | $x_l^i(t)$ | binary, $\{0,1\}$ | Whether ground station $i$ selects HALE-UAV $l$ in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | A ground station can select only CubeSats and HALE-UAVs within its coverage |
| C2 | Scheduling indicators are binary for every visible NTN device |
| C3 | The number of selected NTN devices does not exceed the station's monitoring limit $\bar H_i$ |
| C4 | Differentiated capacity targets cap unnecessary access service for each ground station |
| C5 | Reward terms preserve residual energy and penalize uneven device-energy use |

**Algorithm**: Encode the classical SAGIN state into parameterized quantum circuits, represent the binary scheduling distribution with projection-valued measurements using one qubit per device decision, train decentralized quantum actors with a centralized quantum critic, and update actor-critic parameters until the cooperative reward converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Kim et al. [x] studied cooperative mobile-access scheduling among ground stations, CubeSats, and HALE-UAVs in a space-air-ground integrated network. They formulated a multi-agent decision problem that selects visible non-terrestrial devices to improve differentiated QoS and capacity while preserving and balancing residual energy. Their QMARL scheduler encodes state information in parameterized quantum circuits and uses projection-valued measurement to represent binary CubeSat and HALE-UAV scheduling actions. Decentralized quantum actors are trained with a centralized quantum critic using a reward that combines access performance and device-energy terms. Simulations with orbital and aerodynamic data report higher normalized reward, QoS, capacity, and residual energy than the evaluated conventional MARL, independent Q-learning, DQN, and random schedulers at the largest tested action space.

## Problem and system model

Multiple ground stations cooperatively schedule CubeSats and fixed-wing HALE-UAVs. The reward combines differentiated regional QoS/capacity requirements with residual energy, including CubeSat sun-side photovoltaic charging and HALE aerodynamic/power models. With eight CubeSats and eight HALE-UAVs, each station faces 2^16 binary scheduling combinations.

The experiments use real two-line orbital elements and aerodynamic parameters, but the network and learning loop remain simulation-based.

## Method

[[quantum-marl-sagin-access]] encodes classical state into parameterized quantum circuits and uses basis-level projection-valued measurements to represent probabilities over 2^(M+L) actions with M+L qubits. Each ground station has a quantum actor and training uses a centralized quantum critic. The implementation runs with PyTorch 2.2 and TorchQuantum 0.1.7 on conventional CPU/GPU hardware.

## Key findings

- In the 2^16-action experiment, normalized reward reaches 1.0 and stabilizes after roughly 9,000 epochs; conventional MARL reaches 0.4103, while IQL, DQN, and random scheduling remain lower.
- Against MARL at that scale, the paper reports 87.2% higher QoS, 178% higher capacity, and 99.5% higher residual energy.
- QMARL is not uniformly best at small spaces: conventional MARL slightly exceeds it at 2^1 and 2^4 actions, while QMARL leads at 2^16.
- Ground-station-specific capacity caps raise average residual energy by 46.2% for CubeSats and 38.7% for HALE-UAVs in the reported simulation.

## Limitations

No quantum processor, satellite/UAV deployment, or hardware-in-the-loop network is used. TorchQuantum emulates ideal circuits on an RTX 4090; realistic quantum noise and error correction are explicitly future work. The claimed scalability is demonstrated only through up to 16 binary device decisions and simulation-derived models. Projection measurement compresses the qubit representation of the action distribution, but the policy still represents all scheduling combinations.

## Relation to the corpus

This source adds a quantum-policy representation to [[space-air-ground-integrated-network]] scheduling. It differs from satellite MEC offloading: the controlled object is access assignment and residual energy, not task execution.

## Raw artifacts

- Parse: `raw/sources/Quantum_Multi-Agent_Reinforcement_Learning_for_Cooperative_Mobile_Access_in_Space-Air-Ground_Integrated_Networks/Quantum_Multi-Agent_Reinforcement_Learning_for_Cooperative_Mobile_Access_in_Space-Air-Ground_Integrated_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
