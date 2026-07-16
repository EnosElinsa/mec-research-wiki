---
type: source
title: "Cooperative Learning-Based Joint UAV and Human Courier Scheduling for Emergency Medical Delivery Service"
authors: ["Jiawei Chen", "Pengfu Wan", "Gangyan Xu"]
year: ""
url: ""
venue: ""
tags: [source, uav, delivery, medical-logistics, deep-reinforcement-learning, vehicle-routing, pickup-delivery]
related:
  - "[[cooperative-uav-human-courier-delivery]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[cooperative-uav-taxi-delivery]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[transformer-encoder]]"
  - "[[gao-2026-air-ground-instant-delivery]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
created: 2026-07-12
updated: 2026-07-16
modeling_card: required
---

# Cooperative Learning-Based Joint UAV and Human Courier Scheduling for Emergency Medical Delivery Service

## Citation

Chen, J., Wan, P., & Xu, G. *Cooperative Learning-Based Joint UAV and Human Courier Scheduling for Emergency Medical Delivery Service*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Jointly assigns urgent medical pickup-delivery orders to UAVs and human couriers and routes both fleets under different capacities, speeds, costs, and service rules. An attention-based cooperative DRL policy uses a shared encoder, separate UAV/courier decoders, feasibility masks, and a vehicle coordinator to produce near-real-time schedules.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Emergency medical orders pair a pharmacy or hospital pickup with a delivery point and soft deadline. Heterogeneous UAVs and human couriers start and end at assigned depots; couriers may consolidate orders, whereas each UAV completes one pickup-delivery pair before accepting another.

**Problem & objective**: The multi-depot capacitated pickup-and-delivery problem with soft deadlines minimizes transportation cost and lateness penalties, $\min\sum_{k\in\mathcal K}\sum_{(i,j)\in\mathcal A}w^kd_{ij}x_{ij}^k+\sum_{i\in\mathcal D}\xi_i e_i$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Route arc | $x_{ij}^{k}$ | Binary, $\{0,1\}$ | Indicates that vehicle $k$ traverses arc $(i,j)$ |
| Arrival time | $a_i^k$ | Continuous, nonnegative | Arrival time of vehicle $k$ at point $i$ |
| Vehicle load | $Q_i^k$ | Continuous, $0\leq Q_i^k\leq C^k$ | Load after vehicle $k$ serves point $i$ |
| Delivery lateness | $e_i$ | Continuous, $e_i\geq0$ | Amount by which delivery $i$ exceeds its deadline |
| MDP action | $a_t=(k_t^i,x_t^j)$ | Finite feasible pair | Selects one vehicle and its next point |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every pickup is served once: $\sum_{k\in\mathcal K}\sum_{j\in\mathcal V}x_{ij}^{k}=1$ |
| C2 | Paired pickup and delivery use the same vehicle, with depot departure, depot return, and route-flow balance enforced by (3)-(9) |
| C3 | Pickup precedes delivery: $a_i^k\leq a_{i+n}^k$ |
| C4 | Capacity: $Q_j^k+(1-x_{ij}^k)M_2\geq Q_i^k+q_j$ and $Q_i^k\leq C^k$ |
| C5 | UAV service rule: constraints (16)-(18) force a UAV to complete its current request before another pickup |
| C6 | Soft deadline: $e_i\geq a_i^k-l_i$ and $e_i\geq0$ |

**Algorithm**: Reformulate routing as an MDP, encode depots and paired nodes with heterogeneous multi-head attention, apply separate UAV and courier decoders with precedence, capacity, and vehicle-specific masks, combine compatibilities through a vehicle coordinator, train with REINFORCE and an exponential moving-average baseline, and use greedy decoding at inference.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied joint UAV and human-courier scheduling for emergency medical pickup-and-delivery service with heterogeneous capacities, speeds, costs, and service rules. They minimized distance-based transportation cost plus soft-deadline penalties under paired-service, depot, route-flow, precedence, capacity, and UAV one-order-at-a-time constraints. Their cooperative DRL method used a shared attention encoder, vehicle-specific decoders and feasibility masks, a vehicle coordinator, and REINFORCE training with an exponential baseline. In the H4U5-PDP160 generalization test, it reported an objective of 1262.60 in $1.00\times10^{-3}$ s, compared with 3320.10 in 1259.33 s for OR-Tools and 2785.22 in $1.52\times10^{-3}$ s for Mixed-DRL.

## Problem

Emergency medical-resource sharing creates short-deadline pharmacy/hospital transfers. Human couriers can consolidate several orders but face traffic and higher modeled cost; UAVs are faster and cheaper in the experiments but carry less and serve one request at a time. Assignment and routing must therefore be optimized together under pickup-before-delivery, capacity, depot, and lateness constraints.

## System model

- The problem is a multi-depot capacitated pickup-and-delivery problem with soft deadlines and heterogeneous vehicles (MCPDPSD).
- Each order has paired pickup/delivery points, quantity, and a deadline. Every vehicle starts and ends at its assigned depot and makes one trip.
- The objective combines distance-based transportation cost with lateness penalties; overdue medical deliveries continue rather than becoming infeasible.
- Couriers may consolidate orders, while a UAV must complete its current pickup-delivery pair before starting another.

## Method

The deterministic routing problem is cast as an MDP whose action selects both a vehicle and its next point. A multi-head-attention encoder represents depots and paired pickup/delivery nodes. Type-specific decoder networks apply different feasibility masks for UAVs and couriers, and a vehicle coordinator combines their compatibility scores into one joint action distribution. Training uses REINFORCE with an exponential-moving-average baseline; inference is greedy.

## Key findings

- Random instances use deadlines of 20-180 minutes, request quantities 20-40, five-minute service times, and distinct UAV/courier capacity, speed, and cost settings.
- In the parsed H4U5-PDP160 generalization row (1,440 nodes; 20-instance average), Cooperative-DRL reports objective 1262.60 in `1.00e-3 s`, versus OR-Tools 3320.10 in 1259.33 s and Mixed-DRL 2785.22 in `1.52e-3 s`.
- The Shenzhen case uses 12 hospitals, 60 retained pharmacies, and Amap-derived road routes. Requests and deadlines remain generated, so this is route-informed evaluation rather than live dispatch.
- In the parsed H2U3-PDP80 Shenzhen row (400 nodes; 20-instance average), Cooperative-DRL reports 2337.66 in `1.36e-3 s`, versus OR-Tools 5957.45 in 2800.01 s and Mixed-DRL 3495.01 in `1.65e-3 s`.
- CPLEX does not return a feasible/optimal value within 3,600 s for the reported Shenzhen cases.

## Limitations / parse caveats

Most evaluation instances are synthetic. The Shenzhen experiment uses real geography and routes but generated orders, and it is not an operational deployment. Travel is deterministic; online arrivals, traffic uncertainty, weather, battery/charging, no-fly zones, obstacle avoidance, medical handling constraints, and multi-trip dispatch are outside the model. Exact-solver comparisons are time-capped, and several small-instance table cells are OCR-misaligned. Publication year, venue, DOI, and article URL are not in the parse and remain blank.

## Relation to the corpus

[[cooperative-uav-human-courier-delivery]] extends [[uav-delivery-pickup-dropoff]] from UAV-only trajectory logistics to heterogeneous assignment and routing. It is adjacent to [[cooperative-uav-taxi-delivery]], but couriers consolidate medical orders under soft deadlines rather than contributing opportunistic taxi capacity.

## Raw artifacts

- Parse: `raw/sources/Cooperative_Learning-Based_Joint_UAV_and_Human_Courier_Scheduling_for_Emergency_Medical_Delivery_Service/Cooperative_Learning-Based_Joint_UAV_and_Human_Courier_Scheduling_for_Emergency_Medical_Delivery_Service.md`
- Origin PDF: `raw/sources/Cooperative_Learning-Based_Joint_UAV_and_Human_Courier_Scheduling_for_Emergency_Medical_Delivery_Service/Cooperative_Learning-Based_Joint_UAV_and_Human_Courier_Scheduling_for_Emergency_Medical_Delivery_Service.pdf`
- Figures: `raw/sources/Cooperative_Learning-Based_Joint_UAV_and_Human_Courier_Scheduling_for_Emergency_Medical_Delivery_Service/images/`
