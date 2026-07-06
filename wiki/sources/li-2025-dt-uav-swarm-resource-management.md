---
type: source
title: "Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms"
authors: ["Tianyang Li", "Supeng Leng", "Xiwen Liao", "Yan Zhang"]
year: 2025
url: "https://doi.org/10.1109/TITS.2025.3531120"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, digital-twin, uav-swarm, search-and-rescue, task-crowdsourcing, stochastic-network-calculus, multi-agent-drl, resource-management]
related:
  - "[[digital-twin]]"
  - "[[stochastic-network-calculus]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[communication-constrained-marl]]"
created: 2026-07-06
updated: 2026-07-06
---

# Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms

## Citation

Li, T., Leng, S., Liao, X., & Zhang, Y. (2025). *Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms*. **IEEE Transactions on Intelligent Transportation Systems**, 26(4), 5467-5480. DOI: 10.1109/TITS.2025.3531120.

## TL;DR

Builds a **digital-twin-based collaboration architecture** for UAV swarms in search-and-rescue scenarios. Task requirements drive swarm formation: a virtual traffic-flow scheduler uses stochastic network calculus to pre-assess end-to-end delay bounds, while a MADRL-based task-crowdsourcing policy adjusts which UAVs join the swarm. The goal is to satisfy sensing/service requirements without recruiting unnecessary UAVs or repeatedly reconfiguring physical routes.

## Problem

UAV swarms can cover search-and-rescue tasks that a single UAV cannot, but task requirements, sensing performance, UAV mobility, communication routes, and computation resources interact. The paper targets resource management that is **task-driven** rather than merely connectivity-driven: admit UAVs and schedule traffic only when the virtual swarm can satisfy service and delay requirements.

## System model

- **Architecture.** The paper separates realistic task crowdsourcing from virtual traffic-flow scheduling, with four stages: task crowdsourcing, resource scheduling, pre-assessment, and feedback adjustment.
- **Digital twins.** UAV coordinators maintain DT models for physical and virtual swarm members, including routing, positions, sensor performance, transmit power, CPU frequency, channel gains, and statistical/theoretical end-to-end delay.
- **Traffic.** The virtual layer schedules sensing/service flows before physical route changes are committed.

## Method

The task-crowdsourcing component uses MADRL, with imitation learning used to improve learning efficiency. The traffic-flow allocation component uses [[stochastic-network-calculus]] to evaluate theoretical end-to-end delay bounds and to schedule intra-swarm service flows in the virtual layer before applying changes to the physical UAV network.

## Key findings

- The abstract reports that the proposed framework upholds a **90% achievement ratio** for task requirements while keeping UAV costs comparable.
- The results describe swarm sizes of roughly **4-6 members** when the task-requirement achievement ratio is above 90%.
- When enough UAVs are available, the conclusion reports communication-cost reductions of over 80% versus greedy selection and over 50% versus QMIX and IDQN, while maintaining the task-requirement satisfaction target.

## Limitations / future work

The authors note that larger UAV swarms make MADRL convergence more difficult, multi-hop relaying introduces more coupled variables, and stochastic-network-calculus delay estimates become less precise for time-varying multi-hop paths. Future work is framed around evaluation networks for faster adaptation/training and refined models for time-varying multi-hop UAV networks.

## Relation to the corpus

This paper complements the UAV-swarm MEC and collaborative-inference line by focusing on **task admission and traffic scheduling** rather than in-swarm DNN partitioning. It extends [[digital-twin]] from edge synchronization and ISCC control into a swarm-level resource-management role, and it supplies the corpus with a concrete [[stochastic-network-calculus]] example for probabilistic delay assessment in UAV-swarm traffic flows.

## Raw artifacts

- `raw/sources/Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms/Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms.md`
- Original PDF and extracted figures (`images/`) in the same folder.
