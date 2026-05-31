---
type: source
title: "Deep Reinforcement Learning Based Latency Minimization for Mobile Edge Computing With Virtualization in Maritime UAV Communication Network"
authors: ["Ying Liu", "Junjie Yan", "Xiaohui Zhao"]
year: 2022
url: "https://doi.org/10.1109/TVT.2022.3141799"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, uav-mec, latency-minimization, virtual-machine-multiplexing, deep-reinforcement-learning, ddpg, deep-q-network, trajectory-control]
related:
  - "[[maritime-mec]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[virtual-machine-multiplexing]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[deep-q-network]]"
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[zhang-2020-response-delay-uav-swarm]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-05-31
updated: 2026-05-31
---

# Deep Reinforcement Learning Based Latency Minimization for Mobile Edge Computing With Virtualization in Maritime UAV Communication Network

## Citation

Liu, Y., Yan, J., & Zhao, X. (2022). *Deep Reinforcement Learning Based Latency Minimization for Mobile Edge Computing With Virtualization in Maritime UAV Communication Network*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2022.3141799.

## TL;DR

Minimizes communication + computation latency in a **two-layer maritime UAV-MEC network**: a centralized **top-UAV (T-UAV)** carrying the MEC server above a group of distributed **bottom-UAVs (B-UAVs)**. The MEC server uses **virtual-machine (VM) multiplexing** to run multiple tasks in parallel, accounting for I/O interference that slows each VM. The non-convex, multiply-constrained latency-minimization is reformulated as a **Markov decision process** and solved with a **DQN** (discrete/small spaces) and a **DDPG** (continuous/large spaces) to jointly optimize the T-UAV trajectory and the number of VMs.

## Problem framing

Maritime communication is hard (long distances, unstable channels, sparse infrastructure), and computation-intensive maritime applications need low latency. UAV-enabled MEC supplies flexible, LoS-friendly compute over the sea. A core implementation technology is VM multiplexing, but sharing one physical machine causes I/O interference that degrades each VM's compute speed — and prior work mostly studied parallel computing of **equal**-sized tasks, not the realistic case of **different**-sized tasks across VMs. The paper minimizes latency under this interference while jointly optimizing trajectory and VM count.

## System model

- **Two layers.** Maritime users offload latency-sensitive tasks to B-UAVs; when a B-UAV's edge server saturates (long queue), the T-UAV above offloads B-UAV tasks per an offloading-decision strategy and performs parallel VM computing.
- **Latency components.** Offloading + parallel computing + downloading (download time of results is treated as negligible vs offloading).
- **Virtualization.** A degradation factor D > 0 captures the percentage increase in expected service time when a VM is multiplexed with others; tasks have **different** data amounts across VMs ([[virtual-machine-multiplexing]], [[parallel-vs-serial-processing]]).
- **Formulation.** Non-convex with practical constraints → cast as an **MDP** over T-UAV trajectory and number of VMs participating in parallel computing.

## Method

- **DQN algorithm.** Easy to implement, suited to discrete or low-dimensional action spaces.
- **DDPG algorithm.** Handles large-dimensional/continuous action spaces, avoiding the quantization error of DQN.
- Both minimize system latency by finding optimal T-UAV flight trajectories and the VM count for parallel computing.

## Key findings

- Versus a baseline of **hovering at the center with no parallel computing**, the DDPG algorithm reduces total average latency by **more than 37%** and the DQN algorithm by **31%** (verbatim from the conclusion).
- **DDPG outperforms DQN** for the joint trajectory + VM-configuration problem because it selects continuous actions without quantization error — at the cost of heavier computation.
- DRL-based optimization is more robust to problem modeling (insensitive to convexity of models/constraints) but needs more compute / stronger hardware.

## Limitations / future work

Simulation-only, using random user requests and simplified channel conditions. Stated future work: intelligent reception and DRL-based transmission prediction to actively anticipate user requests and time-varying channels for better trajectory and resource allocation. DOI date of publication 11 Jan 2022 / date of current version 2 May 2022 → year 2022.

## Relation to the corpus

A **maritime UAV-MEC + DRL** entry distinctive for its **VM-virtualization / I/O-interference** angle on parallel computing — a layer most corpus MEC papers abstract away. Its two-layer T-UAV / B-UAV architecture parallels the MEC-enabled UAV-swarm structure of [[zhang-2020-response-delay-uav-swarm]] (top-UAV MEC over bottom-UAVs), and it sits in the maritime track alongside [[liu-2025-haps-uav-maritime-iot]] and the broader [[maritime-mec]] cluster. Reinforces [[virtual-machine-multiplexing]], [[parallel-vs-serial-processing]], [[deep-q-network]], and [[ddpg]]. (First author Ying Liu, Jilin University — distinct from the Yi Liu of [[liu-2020-cooperative-uav-mec-power-iot]] and the Yangbo/Lihan Liu entities.)

## Raw artifacts

- `raw/sources/Deep_Reinforcement_Learning_Based_Latency_Minimization_for_Mobile_Edge_Computing_With_Virtualization_in_Maritime_UAV_Communication_Network/full.md`
- Original PDF and extracted figures in the same folder.
