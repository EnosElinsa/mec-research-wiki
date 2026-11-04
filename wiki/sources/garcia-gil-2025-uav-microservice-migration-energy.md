---
type: source
title: "Microservices Migration: A Pathway to Improved Energy Efficiency in UAV Networks"
authors: ["Santiago García-Gil", "Diego Ramos-Ramos", "Javier Berrocal", "Juan Manuel Murillo", "Jaime Galán-Jiménez"]
year: 2025
url: "https://doi.org/10.1016/j.iot.2024.101463"
venue: "Internet of Things, 30, 101463"
modeling_card: required
tags: [source, uav-networks, microservices, service-migration, energy-efficiency, mixed-integer-linear-programming]
related:
  - "[[service-migration]]"
  - "[[autonomous-uav-swarms]]"
  - "[[container-layered-storage-migration]]"
  - "[[frejo-martin-2025-uav-stateful-microservice-live-migration]]"
  - "[[juan-manuel-murillo]]"
  - "[[jaime-galan-jimenez]]"
created: 2026-08-27
updated: 2026-11-03
---

# Microservices Migration: A Pathway to Improved Energy Efficiency in UAV Networks

## Citation

García-Gil, S., Ramos-Ramos, D., Berrocal, J., Murillo, J. M., & Galán-Jiménez, J. (2025). *Microservices Migration: A Pathway to Improved Energy Efficiency in UAV Networks*. **Internet of Things, 30**, 101463. DOI: 10.1016/j.iot.2024.101463.

## TL;DR

Formulates battery-aware microservice deployment and migration across a computing-enabled UAV swarm as a mixed-integer linear program. Maximizing the minimum remaining battery balances workload and drain, extending simulated rural IoT service lifetime compared with request reassignment alone.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A mesh of computing-enabled UAVs hosts replicated microservices for rural IoT applications. UAVs have finite battery, memory, and CPU capacity, while requests create computation and communication energy demand.

**Problem & objective**: The MILP (6), solved in each time window, selects binary placements $x_{n_i,m_j}$ to maximize the slack $z$, the remaining battery of the UAV with the least battery.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Service placement | $x_{n,m}$ | binary | Whether UAV $n$ hosts microservice $m$ |
| Minimum battery slack | $z$ | continuous | Lowest remaining battery across the fleet |
| Request load (input) | $q_{n_i,m_j}$ | nonnegative | Requests reaching microservice $m_j$ on UAV $n_i$; uplink and downlink traffic $r^u,r^d$ enter the energy model |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| (6b) | Every replica is deployed: $\sum_{n_i}x_{n_i,m_j}=d_{m_j}$ |
| (6c) | RAM: $\sum_{m_j}x_{n_i,m_j}c_{m_j}\le c_{u_i}$ |
| (6d) | CPU: $\sum_{m_j}x_{n_i,m_j}(f_{m_j}+f_{m_j}^rq_{n_i,m_j})\le f_{u_i}$ |
| (6e) | Battery floor to reach the recharging station: $b_{n_i}-E(u_{n_i},r_{n_i}^u,r_{n_i}^d,t)\ge b$ |
| (6f) | Slack is the lowest remaining battery: $b_{n_i}-E(\cdot)\ge z$ |

**Algorithm**: Estimate CPU and network power from Raspberry Pi measurements, compute per-slot energy, and solve the resulting MILP repeatedly to relocate microservices so that the fleet's lowest remaining battery is maximized.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

García-Gil et al. [x] studied energy-aware microservice placement and migration in a computing-enabled UAV swarm supporting rural IoT applications. They built a measured processor and network power model and formulated binary service placement as a mixed-integer linear program. The objective maximizes the minimum remaining UAV battery subject to replica, RAM, CPU, and minimum-energy constraints. Simulations show balanced workload and battery drain and report that migrating microservices is more energy efficient than reallocating requests alone in the evaluated setting. Quality-of-service and service-function-chain constraints, photovoltaic or tethered UAVs, and their different power models remain outside the formulation.

## Problem and system model

IoT applications are decomposed into resource-bounded microservices and placed on UAVs connected by line-of-sight links. Communication, computation, and flight consume battery, and uneven request load can cause one UAV to terminate service early.

## Method

The paper derives CPU, downlink, uplink, and forwarding energy terms from Raspberry Pi 4 measurements. A ten-minute-slot MILP then relocates replicated microservices while satisfying resource and battery thresholds and maximizing fleet battery balance.

## Key findings

- The evaluated network operates for more than nine hours at the reported request load, consuming about 1.06% battery per ten-minute slot.
- The placement becomes infeasible above roughly 36,300 requests per slot in the studied configuration.
- At least 15 UAVs are required for feasibility in the reported scenario, and the worst MILP solve takes 3.6 seconds.

## Limitations / future work

The model omits QoS and service-function-chain constraints. Photovoltaic and tethered UAVs would require different infrastructure costs, mobility assumptions, and power models.

## Relation to the corpus

This source adds battery-balanced application placement to [[service-migration]] and [[autonomous-uav-swarms]]. It focuses on where microservices execute, whereas [[container-layered-storage-migration]] focuses on reducing migration transfer cost.

## Raw artifacts

- Parse: `raw/sources/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md`
- Origin PDF and extracted figures are in the same folder.
