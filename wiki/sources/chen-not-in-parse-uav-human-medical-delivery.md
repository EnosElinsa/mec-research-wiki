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
updated: 2026-07-12
---

# Cooperative Learning-Based Joint UAV and Human Courier Scheduling for Emergency Medical Delivery Service

## Citation

Chen, J., Wan, P., & Xu, G. *Cooperative Learning-Based Joint UAV and Human Courier Scheduling for Emergency Medical Delivery Service*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Jointly assigns urgent medical pickup-delivery orders to UAVs and human couriers and routes both fleets under different capacities, speeds, costs, and service rules. An attention-based cooperative DRL policy uses a shared encoder, separate UAV/courier decoders, feasibility masks, and a vehicle coordinator to produce near-real-time schedules.

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
