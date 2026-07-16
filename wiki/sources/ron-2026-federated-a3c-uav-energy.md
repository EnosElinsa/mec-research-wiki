---
type: source
modeling_card: required
title: "Intelligent Energy Efficiency and Service Reliability Optimization for UAV-Aided Terrestrial Networks"
authors: ["Dara Ron", "Jung-Ryun Lee"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3601729"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, uav-relay, federated-learning, a3c, energy-efficiency, service-reliability, dynamic-spectrum-sharing, resource-allocation]
related:
  - "[[hierarchical-federated-a3c]]"
  - "[[hierarchical-federated-drl]]"
  - "[[federated-reinforcement-learning]]"
  - "[[federated-learning]]"
  - "[[device-association]]"
  - "[[energy-latency-tradeoff]]"
  - "[[jung-ryun-lee]]"
created: 2026-07-13
updated: 2026-07-16
---

# Intelligent Energy Efficiency and Service Reliability Optimization for UAV-Aided Terrestrial Networks

## Citation

Ron, D., & Lee, J.-R. (2026). *Intelligent Energy Efficiency and Service Reliability Optimization for UAV-Aided Terrestrial Networks*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2025.3601729.

> **Metadata grounding note.** DOI, venue, and year are absent from the parse and were verified through the exact-title Crossref record.

## TL;DR

Uses a two-level federated multi-agent A3C framework to control ground-user and UAV transmit powers, UAV hover positions, bandwidth fractions, and UAV associations in a 12.2-12.7 GHz UAV-relay network. The intended objective is low ground-user/UAV computation-plus-transmission energy while keeping federated-learning round-trip delay within a reliability threshold.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground users upload data and local federated-learning models through selected UAV relays to a terrestrial base station over licensed FR3 dynamic spectrum, with computation and transmission energy tracked at users and UAVs.

**Problem & objective**: The mixed-integer nonlinear formulation minimizes long-run average energy, written as $\min \overline{E}_{GU+UAV}$, while keeping model round-trip delay reliable.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| GU transmit power | $P_{m,t}$ | continuous, bounded | Ground-user uplink power |
| UAV transmit power | $\bar P_{n,t}$ | continuous, bounded | UAV forwarding and feedback power |
| UAV position | $\varphi_{n,t}$ | continuous, bounded 3-D coordinate | UAV hover position |
| Bandwidth share | $\zeta_{n,t}$ | continuous, $(0,1)$ | Fraction assigned to UAV $n$ |
| UAV association | $\vartheta_{m,n,t}$ | binary | Selects one serving UAV for user $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Round-trip delay reliability keeps the model exchange within the threshold: $\Pr\{T_{m,t}\leq T_{th}\}$ meets the required service reliability. |
| C2 | Ground-user power bounds: $P_{min}\leq P_{m,t}\leq P_{max}$. |
| C3 | UAV power bounds: $\bar P_{min}\leq\bar P_{n,t}\leq\bar P_{max}$. |
| C4 | UAV position remains in the feasible flight region. |
| C5 | Bandwidth shares form a simplex: $\sum_n\zeta_{n,t}=1$. |
| C6 | Each ground user selects one UAV: $\vartheta_{m,n,t}\in\{0,1\}$ and $\sum_n\vartheta_{m,n,t}=1$. |

**Algorithm**: Model the controls as a federated multi-agent UMDP; each A3C agent observes delay and energy, emits quantized power, position, bandwidth, and association actions, and aggregates actor and critic parameters first at UAVs and then at the base station.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ron and Lee [x] formulate UAV-relay federated learning as joint energy and service-reliability control. The mixed-integer nonlinear model selects user and UAV powers, UAV positions, bandwidth shares, and associations while constraining round-trip delay, power, geometry, bandwidth, and association. Their two-level federated A3C scheme uses user agents and hierarchical model aggregation to approximate the coupled control problem. At the reported 30-action setting, the federated design reaches 99.06% reliability versus 88.3% for multi-agent DQN and reduces energy by up to 35.11%.

## Problem framing

Remote ground users send both information and local learning models through UAV relays to a terrestrial base station. The same control choices determine interference, model-delivery delay, and battery use. The resulting mixed-integer nonlinear problem couples continuous powers/positions/bandwidth with discrete association and a probabilistic round-trip-delay constraint.

## System model

- Ground users upload information plus local model parameters to associated UAVs; each UAV aggregates a sub-global model and forwards it to the terrestrial base station, which aggregates and returns the global model.
- A slot has uplink and downlink phases in licensed FR3 dynamic spectrum sharing.
- Energy equations include user computation/uplink transmission and UAV aggregation/forwarding/downlink transmission. They do **not** include UAV propulsion or hovering energy.
- Reliability is the probability that the full model round trip, including local/sub-global/global computation and transport, meets a 1 s threshold.

## Method

Each ground user is an A3C agent. Continuous controls are quantized, and the joint action selects user/UAV power, UAV Cartesian hover position, bandwidth fraction, and association. Local actor/critic parameters are averaged at the UAV, then UAV sub-global models are averaged at the base station. The reward multiplies negative energy by a round-trip-delay violation indicator; this is the paper's unconstrained UMDP surrogate, not an exact proof that every original reliability constraint is satisfied.

## Key findings

- The reported learning curves stabilize after about 50 episodes in the simulated configuration.
- At 30 actions, the paper reports **99.06%** service reliability for the federated A3C design versus **88.3%** for multi-agent DQN.
- The conclusion reports up to **35.11%** lower energy consumption than DQN.

## Limitations / interpretation

All evidence is simulation-based; an O-RAN/real-network testbed is left for future work. The method discretizes a very large Cartesian action space and reports a critic output size of 7,593,750 neurons. Its complexity estimate assumes NVIDIA A100-class processors on UAVs and the base station and excludes communication, aggregation, memory, and system overhead. The parse gives inconsistent quantization counts (15 levels in the parameter table versus five in the network-description prose). It also alternates between minimizing energy and “maximizing energy efficiency,” and equation (17)'s violation-indicator reward becomes zero when delay is feasible, so the stated energy/reliability interpretation should not be read as a formal equivalence without qualification. The paper's replay-memory/batch implementation is also not canonical on-policy A3C.

## Relation to the corpus

The distinctive contribution is [[hierarchical-federated-a3c]]: the relay hierarchy doubles as a model-aggregation hierarchy. It is adjacent to [[hierarchical-federated-drl]] but uses ground-user A3C agents for communication controls rather than a terrestrial/non-terrestrial offloading and incentive stack.

## Raw artifacts

- `raw/sources/Intelligent_Energy_Efficiency_and_Service_Reliability_Optimization_for_UAV-Aided_Terrestrial_Networks/Intelligent_Energy_Efficiency_and_Service_Reliability_Optimization_for_UAV-Aided_Terrestrial_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
