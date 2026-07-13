---
type: source
title: "Optimization of Urban Emergency Multimodal Transportation Scheduling With UAV-Ground Traffic Coordination"
authors: ["Hanqing Xia", "Ming Zhang", "Zechao Ma", "Mengju Cui", "Chao Yan"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3626994"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, no. 1, pp. 692-708"
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
updated: 2026-07-13
---

# Optimization of Urban Emergency Multimodal Transportation Scheduling With UAV-Ground Traffic Coordination

## Citation

Xia, H., Zhang, M., Ma, Z., Cui, M., & Yan, C. (2026). *Optimization of Urban Emergency Multimodal Transportation Scheduling With UAV-Ground Traffic Coordination*. **IEEE Transactions on Intelligent Transportation Systems, 27**(1), 692-708. DOI: 10.1109/TITS.2025.3626994.

## TL;DR

Coordinates UAVs riding and charging on buses with dynamically recruited taxis, then uses learned taxi availability/travel times and a non-overlapping coverage-gain greedy selector to improve citywide emergency coverage and hovering endurance.

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
