---
type: source
title: "Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability"
authors: ["Sergio Frejo-Martín", "Andrés García-López", "Juan Manuel Murillo", "Jaime Galán-Jiménez"]
year: 2025
url: "https://doi.org/10.1109/ISCC65549.2025.11325941"
venue: "2025 IEEE Symposium on Computers and Communications (ISCC)"
modeling_card: not_applicable
tags: [source, stateful-migration, live-migration, uav-replacement, microservices, digital-twin, containers]
related:
  - "[[stateful-edge-microservice-migration]]"
  - "[[container-layered-storage-migration]]"
  - "[[digital-twin]]"
  - "[[garcia-gil-2025-uav-microservice-migration-energy]]"
  - "[[juan-manuel-murillo]]"
  - "[[jaime-galan-jimenez]]"
created: 2026-11-02
updated: 2026-11-02
---

# Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability

## Citation

Frejo-Martín, S., García-López, A., Murillo, J. M., & Galán-Jiménez, J. (2025). *Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability*. **2025 IEEE Symposium on Computers and Communications (ISCC)**. DOI: 10.1109/ISCC65549.2025.11325941.

## TL;DR

UAVs in an ad hoc network must be replaced when their batteries run low, which interrupts the microservices they host. The paper proposes an architecture for pre-copy live migration of stateful containerized microservices during replacement, coordinated by a digital twin, a swarm management function, and a central image server for storage layers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Frejo-Martín et al. [x] addressed service disruption in UAV-assisted networks, where limited flight time forces frequent node replacements that interrupt the microservices hosted on the UAVs. They introduced a model for live migration of stateful microservices that uses pre-copy mechanisms and containerized environments to minimize service downtime and preserve state. The architecture includes a digital twin for real-time monitoring, a swarm management function for orchestrating UAV replacements, and a central image server for managing storage layers. By combining these elements, the model aims at seamless handovers that enable reliable deployment of state-sensitive applications such as real-time data analysis and edge computing. The authors identify service downtime, network overhead, and energy consumption as the metrics for future performance evaluation.

## Scope and method

The paper describes an architecture and migration workflow without an optimization model or a quantitative evaluation.

## Key findings

- Pre-copy live migration with containerized state preservation can keep microservices running across UAV replacements.
- State preservation introduces network overhead that needs further optimization.

## Limitations / future work

The authors plan to evaluate downtime, network overhead, and energy consumption.

## Relation to the corpus

Applies [[stateful-edge-microservice-migration]] to UAV replacement, alongside the energy-oriented migration study [[garcia-gil-2025-uav-microservice-migration-energy]] from the same university.

## Raw artifacts

- Parse: `raw/sources/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md`
- Origin PDF and extracted figures are in the same folder.
