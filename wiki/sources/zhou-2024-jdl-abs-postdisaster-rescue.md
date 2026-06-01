---
type: source
title: "Delay-Aware UAV Computation Offloading and Communication Assistance for Post-Disaster Rescue"
authors: ["Chengyi Zhou", "Junyu Liu", "Kaige Qu", "Min Sheng", "Jiandong Li", "Weihua Zhuang"]
year: 2024
url: "https://doi.org/10.1109/TWC.2024.3479709"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, post-disaster-mec, computation-offloading, lyapunov-optimization, actor-critic, two-timescale-optimization, trajectory-design]
related:
  - "[[post-disaster-mec]]"
  - "[[mobile-edge-computing]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[two-timescale-optimization]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[edge-user-allocation]]"
  - "[[air-to-ground-channel-model]]"
  - "[[zhang-2019-stochastic-offloading-uav-mec]]"
  - "[[yang-2022-stochastic-uav-mec-lyapunov]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-06-01
updated: 2026-06-02
---

# Delay-Aware UAV Computation Offloading and Communication Assistance for Post-Disaster Rescue

## Citation

Zhou, C., Liu, J., Qu, K., Sheng, M., Li, J., & Zhuang, W. (2024). *Delay-Aware UAV Computation Offloading and Communication Assistance for Post-Disaster Rescue*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3479709. (Received 14 Jan 2024; revised 16 May and 9 Sep 2024; accepted 28 Sep 2024; date of publication 21 Oct 2024; date of current version 12 Dec 2024. Corresponding author: Junyu Liu.)

## TL;DR

A UAV-mounted **aerial base station (ABS)** in a post-disaster rescue scenario simultaneously serves ground users (GUs) with communication and computes sensing-related tasks, partially offloading them to a more powerful **macro base station (MBS)**. The work **minimizes task computation queuing delay** while ensuring GU communication rate, by jointly optimizing **ABS-GU association, task offloading ratio, and ABS trajectory** under ABS flight-energy constraints. The long-term stochastic **mixed-integer nonlinear program (MINLP)** is solved by a **joint DRL + Lyapunov optimization (JDL)** algorithm, with a distinctive twist: the **critic module uses model-based successive convex approximation (SCA)** to evaluate the actor's association action, instead of a model-free critic DNN.

## Problem framing

When terrestrial infrastructure is damaged, ABSs restore emergency communication and provide situational awareness by sensing the rescue environment, but their onboard battery and compute are limited, so real-time sensing tasks (e.g., image processing) cannot be fully handled locally. The MBS is more capable and can take partially offloaded tasks, but tasks queue behind predecessors, producing a **task queuing delay**. Three coupled difficulties arise: (1) GUs are non-uniformly and unpredictably distributed and the count under an ABS varies as it flies, so association must track user distribution and mobility; (2) the ABS-MBS channel is time-varying with ABS motion, complicating offloading decisions; (3) the ABS must get close to GUs for throughput yet close to the MBS for low offloading delay — conflicting trajectory pulls under an energy budget.

## System model

- **Actors.** Multiple ABSs ($A_j$), MBSs ($M_g$), and GUs ($U_i$); each ABS flies a designed trajectory while serving associated GUs and offloading a fraction of its sensing-task data to an MBS.
- **Queues.** Per-ABS local computation queue $Q_j^L$, offloaded-task transmission queue $Q_j^O$, and offloaded-task computation queue at the MBS $Q_j^S$ — the queuing delays the objective targets.
- **Constraints.** Maximum GU association number per slot, minimum inter-ABS safe distance $D_{\min}$, max/min ABS speed and acceleration, and a maximum ABS flight-energy budget $E_{\max}$ ([[air-to-ground-channel-model]] governs ABS-GU and ABS-MBS links).
- **Objective.** Minimize the long-term task computation queuing delay subject to a GU communication-rate guarantee, formulated as a stochastic [[mixed-integer-nonlinear-programming|MINLP]].

## Method

- **JDL = Lyapunov + actor-critic DRL.** [[lyapunov-optimization|Lyapunov optimization]] decouples the long-term stochastic MINLP into a series of per-slot deterministic MINLPs.
- **Actor** is a DNN that learns the **ABS-GU association** from all GUs' channel gains and all ABSs' task queuing delays.
- **Critic** evaluates the actor's association action by **analytically solving** a joint trajectory-planning + task-offloading problem via [[alternating-optimization-sdr-sca|SCA]] — a model-based critic rather than a model-free value DNN.
- **Two timescales** ([[two-timescale-optimization]]): trajectory planning is optimized on a **large timescale**, task offloading on a **small timescale**, to reduce computational complexity.

## Key findings

- JDL's learned trajectory planning **reduces queuing delay versus a fixed circular-trajectory benchmark** (the paper uses a 2.5 km-radius circular ABS path as the benchmark): moving the ABS shortens ABS-GU and ABS-MBS distances, raising the offloading transmission rate so more task data can be offloaded to the MBS (Fig. 13, parse).
- Against the **SDQN** (separated-DQN) baseline, JDL attains lower queuing delay across a cycle and is more robust to changes in the number of GUs, because mapping the actor output to a generated action set decouples the model structure from the association count (Figs. 12, 14; figure-read curves, indicative).
- JDL trained in one measured-channel scenario and executed in another (JDL-Cir-change) still reduces queuing delay versus SDQN-Cir, supporting fast real-time inference as the environment changes; lower queuing delay also corresponds to higher CSI accuracy for delay-sensitive monitoring (Figs. 14–16, qualitative).

## Limitations / future work

The authors flag (stated) extending to **online resource management** that accounts for the **uncertainty of user mobility** and **time-variant ABS computation demand** under wireless channel dynamics. Reported magnitudes are read from MinerU-parsed figures/tables and should be treated as indicative.

## Relation to the corpus

A **post-disaster UAV-MEC** entry ([[post-disaster-mec]]) that joins Lyapunov-based stochastic UAV-MEC optimization with an actor-critic DRL policy — pairing the model-based convex machinery of [[zhang-2019-stochastic-offloading-uav-mec]] and [[yang-2022-stochastic-uav-mec-lyapunov]] with a learned association policy. Its **SCA-in-the-critic** design is the distinguishing trait versus pure model-free DRL post-disaster work such as [[peng-2025-drudm-cfg]] (urgency-aware admission via generative DRL). The ABS-GU association subproblem connects to [[edge-user-allocation]], and the two-timescale split echoes [[two-timescale-optimization]].

## Raw artifacts

- `raw/sources/Delay-Aware_UAV_Computation_Offloading_and_Communication_Assistance_for_Post-Disaster_Rescue/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
