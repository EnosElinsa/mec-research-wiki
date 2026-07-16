---
type: source
title: "Optimization of Urban Emergency Multimodal Transportation Scheduling With UAV-Ground Traffic Coordination"
authors: ["Hanqing Xia", "Ming Zhang", "Zechao Ma", "Mengju Cui", "Chao Yan"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3626994"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, no. 1, pp. 692-708"
modeling_card: required
tags: [source, urban-emergency, uav-bus-taxi, multimodal-transportation, spatiotemporal-coverage, greedy-selection]
related:
  - "[[uav-bus-taxi-emergency-response]]"
  - "[[non-overlapping-coverage-gain-greedy]]"
  - "[[urban-air-mobility]]"
  - "[[cooperative-uav-taxi-delivery]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[vehicle-fog-computing]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-16
---

# Optimization of Urban Emergency Multimodal Transportation Scheduling With UAV-Ground Traffic Coordination

## Citation

Xia, H., Zhang, M., Ma, Z., Cui, M., & Yan, C. (2026). *Optimization of Urban Emergency Multimodal Transportation Scheduling With UAV-Ground Traffic Coordination*. **IEEE Transactions on Intelligent Transportation Systems, 27**(1), 692-708. DOI: 10.1109/TITS.2025.3626994.

## TL;DR

Coordinates UAVs riding and charging on buses with dynamically recruited taxis, then uses learned taxi availability/travel times and a non-overlapping coverage-gain greedy selector to improve citywide emergency coverage and hovering endurance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An urban grid is evaluated over time slots while UAVs ride and recharge on buses, recruit taxis for rendezvous or relay travel, and respond through four flight and ground-transport cases.

**Problem & objective**: Bus selection maximizes joint emergency coverage utility, $P_0=\max_{\mathbb B_S}\sum_{(g_r,t)}\mathcal C_{\mathbb B_S}^{\mathrm{Union}}(g_r,t)$, under a recruitment budget, while each case utility combines delay, hover duration, and relay cost.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Selected bus set | $\mathbb B_S$ | Binary subset, $\mathbb B_S\subseteq\mathbb B$ | Choose buses carrying UAV teams |
| Response case | $\mathrm{Case}_i$ | Discrete, $i\in\{1,2,3,4\}$ | Select the flight and taxi mode for a response |
| Taxi recruitment and rendezvous | $\mathcal T,\,g_r$ | Discrete grid assignments | Select relay taxis and meeting or emergency grids |
| Coverage utility | $\mathcal C^{\mathrm{Union}}$ | Continuous, $[0,1]$ | Utility contributed to each spatiotemporal grid |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Total recruitment cost respects the budget, $R\leq B$ |
| C2 | Each response has positive hover duration, $T_h^{\mathrm{Case}_i}>0$ |
| C3 | Response delay stays within the limit, $T_{\mathrm{delay}}^{\mathrm{Case}_i}\leq T_e^{\max}$ |
| C4 | Relay cost stays within the limit, $C_{\mathrm{relay}}^{\mathrm{Case}_i}\leq C_{\mathrm{relay}}^{\max}$ |
| C5 | The selected bus count is bounded, $\lvert\mathbb B_S\rvert\leq K$ |

**Algorithm**: Two MLP predictors estimate free-taxi counts and grid travel times from trajectory data, then NOCG-Greedy repeatedly selects the bus with the largest uncovered joint coverage gain until the budget or bus-count limit is reached.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xia et al. [x] modeled urban emergency response as multimodal coordination among UAVs, buses, and relay taxis over spatiotemporal grids. The optimization selects bus teams and one of four response cases to maximize joint coverage utility while bounding recruitment cost, delay, hover feasibility, relay cost, and fleet size. Taxi availability and travel time are predicted with MLP models, and NOCG-Greedy adds buses by their non-overlapping coverage gain. Experiments report full citywide coverage with a limited team count, high hovering endurance and energy utilization, and lower infrastructure cost than bus-only and heuristic alternatives.

## Problem and system model

UAVs normally ride buses and respond to unpredictable urban emergencies through four modes: fly both ways, ride a taxi outbound, ride a taxi back, or ride taxis both ways. Each mode trades arrival delay, hovering duration, reserve energy, taxi cost, and the moving rendezvous point with the original bus.

The city is divided into spatial grids and time slots. Bus trajectories are assumed known; unoccupied-taxi counts and travel times are learned from historical trajectories. Vehicle edge devices estimate each bus-UAV team's response utility before a central emergency controller assigns tasks.

## Method

[[uav-bus-taxi-emergency-response]] models flight/hover energy and distance-priced taxi recruitment for the four modes. Two fully connected MLP tasks with Leaky-ReLU and Huber loss predict free-taxi counts and inter-grid travel time.

Bus selection is NP-hard by reduction to set cover. [[non-overlapping-coverage-gain-greedy|NOCG-Greedy]] repeatedly selects the bus with greatest utility over uncovered spatiotemporal grids under a vehicle budget, with stated complexity `O(Kmn)`.

## Key findings

- Shenzhen datasets include more than 13,000 buses, 14,000 taxis, 30 million bus records, 140 million taxi records, and 5,400 congestion events.
- In modeled citywide coverage, 30 bus-UAV teams achieve 100% spatiotemporal coverage for at least five minutes per grid.
- For 1,200 synthetic emergency events, UBT-ST reports average coverage 98.7%, average hovering time 2,105 s, and energy-utilization ratio 87.1%; its arrival delay is not the lowest.
- At 95% coverage, UBT-ST uses five buses in the cost experiment and reports infrastructure cost 281,200 RMB versus 74.799 million RMB for the bus-only baseline.
- On the collected congestion events, 40 buses complete all monitored tasks; centralized emergency stations can reach covered central events faster but complete fewer tasks.

## Limitations

The vehicle traces are real, but UAV missions, taxi compliance, takeoff/landing, energy, and emergency execution are modeled rather than field-tested. The design assumes 100% recruited-taxi compliance, known future bus trajectories, available rooftop landing, reliable vehicle connectivity, and taxis close enough to pickup/drop-off grids. Euclidean grid-center distances and fixed energy coefficients simplify routing, weather, traffic, payload, conflict, and charging effects. The greedy method has no approximation guarantee for the continuous utility objective.

The byline's Chao Yan is a NUAA civil-aviation Ph.D. student and is distinct from the existing source's NUAA automation associate professor with the same name; no entity merge is made.

## Relation to the corpus

This source extends [[cooperative-uav-taxi-delivery]] from parcel logistics to emergency monitoring and reserve-energy management. It is adjacent to [[persistent-emergency-uav-swarm-service]], but uses public vehicles as mobile charging/relay platforms rather than rotating dedicated UAV replacements.

## Raw artifacts

- Parse: `raw/sources/Optimization_of_Urban_Emergency_Multimodal_Transportation_Scheduling_With_UAV-Ground_Traffic_Coordination/Optimization_of_Urban_Emergency_Multimodal_Transportation_Scheduling_With_UAV-Ground_Traffic_Coordination.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
