---
type: source
title: "Semantic Communication in Satellite-Borne Edge Cloud Network for Computation Offloading"
authors: ["Guhan Zheng", "Qiang Ni", "Keivan Navaie", "Haris Pervaiz"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3365879"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, semantic-communication, leo-satellite-edge-computing, computation-offloading, federated-learning, bargaining-game, mixed-integer-nonlinear-programming, privacy-sensitive-data-partitioning]
related:
  - "[[semantic-communication]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[non-terrestrial-network]]"
  - "[[task-offloading]]"
  - "[[federated-learning]]"
  - "[[bargaining-game]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[privacy-sensitive-data-partitioning]]"
  - "[[dnn-model-partition]]"
  - "[[mobile-edge-computing]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[mahboob-2024-ai-ntn-survey]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-06-01
updated: 2026-06-01
---

# Semantic Communication in Satellite-Borne Edge Cloud Network for Computation Offloading

## Citation

Zheng, G., Ni, Q., Navaie, K., & Pervaiz, H. (2024). *Semantic Communication in Satellite-Borne Edge Cloud Network for Computation Offloading*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3365879. (Manuscript received 8 July 2023; accepted 15 December 2023; date of publication 26 February 2024; date of current version 9 May 2024 → year 2024. An earlier version appeared at the IEEE ICC 2022 DDINS Workshop, DOI 10.1109/ICCWorkshops53468.2022.9814494.)

## TL;DR

A framework integrating **semantic communication (SemCom)** into a **LEO satellite-borne edge cloud (SEC)** for terrestrial users' computation offloading (**SemCom-SEC**), with semantic coders deployed on both **terrestrial-station-terminals (TSTs)** and **satellites**. It splits the problem into two scenarios: (1) **in-maintenance** (coders need updating) — solved by an adaptive **pruning-split federated learning (PSFed)** method that preserves coder integrity while cutting training cost and privacy risk; and (2) **in-service** (trained coders process tasks) — where minimizing users' **delay + energy** subject to **privacy** and **fairness** is cast as an incomplete-information **MINLP** and solved by a **computational task processing scheduling (CTPS)** mechanism built on the **Rubinstein bargaining game**.

## Problem framing

Users in remote/disaster areas lack terrestrial edge infrastructure; LEO satellites offer lower latency than GEO/MEO, and **SEC** (compute on board the LEO satellite) halves propagation delay versus offloading to a remote core cloud. But offloading large tasks to SEC demands high transmission rate against a hard **spectrum** limit, motivating SemCom (transmit only task-relevant semantic information, raising spectral efficiency and robustness to variable satellite links). Integrating SemCom into SEC raises two new problems the paper targets: (1) **updating the goal-oriented ML semantic coders** in real time under SEC mobility, low service-interruption tolerance, energy, and **privacy** constraints — existing distributed-learning frameworks (users + terrestrial edge only) do not translate to the multi-party SEC setting; and (2) SemCom shifts load from communication to **computation**, so users need new **task-processing strategies** that jointly weigh access modality, processing entity, delay, energy, and privacy.

## System model

- **Architecture.** Terrestrial users without terrestrial edge access; tasks can be processed **locally**, at the **LEO SEC**, or at the **core cloud**. Users reach the SEC **directly** (C-band user-satellite link) or **indirectly** through a **TST** (C-band user→TST in an OFDMA setting + Ka-band TST→SEC). Semantic coders sit on both TSTs and satellites.
- **In-maintenance objective.** Update deployed semantic coders with low training delay/energy and preserved privacy.
- **In-service objective.** Minimize users' processing **delay + energy** subject to **privacy** and **fairness**, formulated as an **incomplete-information MINLP** (privacy hides information from other parties).

## Method

- **PSFed (in-maintenance).** An adaptive **pruning-split federated learning** approach: it adaptively "splits" and "prunes" the semantic coders for federated aggregation under each user's personalized conditions, but — unlike conventional split/prune models — the **coder model components remain intact after updating**. Prunes uploaded TST encoder parameters by importance to cut training communication cost; shown to guarantee training convergence speed and accuracy while improving privacy.
- **CTPS (in-service).** A two-step mechanism: (1) a **Rubinstein bargaining game** transforms the incomplete-information MINLP (privacy-induced) into a complete-information problem; (2) the converted MINLP is decomposed and solved via the **Lagrangian dual decomposition** method.

## Key findings

- Versus a general learning approach for semantic-coder updating in SEC, **PSFed saves 40.50% of communication resources on average and reduces privacy risk by 51.43%**, while **training accuracy and convergence speed remain almost the same** (conclusion, verbatim figures).
- The PSFed + game-theoretic CTPS combination **outperforms baseline solutions**, reducing delay and energy consumption while enhancing privacy (abstract).

## Limitations / future work

Simulation-based. The parse does not enumerate an explicit future-work list → `not in parse`.

## Relation to the corpus

The corpus's **semantic-communication-for-satellite-offloading** entry, joining the [[semantic-communication]] concept (previously grounded only by the multi-functional-RIS anti-jamming source [[sun-2024-mfris-semantic-antijamming]]) to the [[leo-satellite-edge-computing]] / [[non-terrestrial-network]] thread. It complements the energy-constrained satellite offloading of [[cheng-2025-dos-satellite-edge-computing]] and the double-edge UAV+LEO design [[wang-2025-double-edge-samin]], and instantiates several of the AI-NTN research thrusts catalogued in [[mahboob-2024-ai-ntn-survey]] (computational offloading, distributed/federated learning, security/privacy). Its **PSFed** ties [[federated-learning]] and [[dnn-model-partition]] together, while **CTPS** brings the [[bargaining-game]] to bear on a privacy-aware [[mixed-integer-nonlinear-programming]] offloading problem.

## Raw artifacts

- `raw/sources/Semantic_Communication_in_Satellite-Borne_Edge_Cloud_Network_for_Computation_Offloading/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
