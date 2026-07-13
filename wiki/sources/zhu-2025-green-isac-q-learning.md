---
type: source
title: "Resource Allocation for UAV Swarm-Assisted Green ISAC Networks via Multi-Agent RL"
authors: ["Qian Zhu", "Rongke Liu", "Qirui Liu", "Changwen Chen"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3487995"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 9, no. 3, pp. 1354-1367"
tags: [source, integrated-sensing-and-communication, uav-swarm, resource-allocation, multi-agent-q-learning, cramer-rao-bound, energy-efficiency]
related:
  - "[[improved-fast-base-station-selection]]"
  - "[[crlb-initialized-q-table]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[tdoa-based-uav-localization]]"
  - "[[multi-agent-q-learning]]"
  - "[[overall-energy-efficiency]]"
  - "[[qian-zhu]]"
  - "[[rongke-liu]]"
  - "[[zhu-2024-sensing-comm-doppler-uav-swarm]]"
created: 2026-07-14
updated: 2026-07-14
---

# Resource Allocation for UAV Swarm-Assisted Green ISAC Networks via Multi-Agent RL

## Citation

Zhu, Q., Liu, R., Liu, Q., & Chen, C. (2025). *Resource Allocation for UAV Swarm-Assisted Green ISAC Networks via Multi-Agent RL*. **IEEE Transactions on Green Communications and Networking, 9**(3), 1354-1367. DOI: 10.1109/TGCN.2024.3487995.

## TL;DR

Uses low-CRLB UAV-anchor geometry to initialize selected entries of independent tabular Q-learners, coupling periodic TDOA positioning information with per-slot ground-terminal and transmit-power selection.

## Problem and system model

A swarm of moving low-altitude UAVs provides downlink communication and TDOA positioning to stationary ground terminals in an isolated area without reliable GNSS or terrestrial service. UAVs follow known straight-line horizontal trajectories at fixed altitude and speed. A ground base station stores UAV positions and issues schedules, while each UAV acts as an independent resource-allocation agent.

Each UAV selects at most one terminal and one discrete power level per slot. Its communication reward is throughput divided by transmit energy when an SINR threshold is met, and zero otherwise. Positioning uses at least four UAV anchors and scores geometry by the inverse trace of the Fisher-information inverse, expressed as a positioning [[cramer-rao-bound|CRLB]]. The optimization combines these periodic sensing-prior scores with communication energy-efficiency rewards.

## Method

[[improved-fast-base-station-selection]] groups candidate UAV anchors around rotated reference azimuths and searches one candidate per group for the minimum-CRLB subset. [[crlb-initialized-q-table|CRLB-initialized Q-tables]] assign inverse-CRLB values to QoS-satisfied actions that pair selected anchors with the corresponding terminal; other entries start at zero, and the prior is refreshed as geometry changes.

Distributed [[multi-agent-q-learning]] then lets each UAV choose a terminal-power action with epsilon-greedy exploration from a two-state table. The stated update retains the larger of the current value and Bellman target, so values cannot decrease; it is not the standard learning-rate-weighted Q-learning update.

## Key findings

- The motivating Fig. 4 example gives nearly equal communication rates of about 0.87 Mbit/s for two UAV subsets but positioning errors of 9 m and 17 m, showing that communication-equivalent allocations can have different sensing geometry. These are figure-derived values described in the text.
- Improved FBSS produces positioning error around 5.42 m in the displayed Fig. 7 scenario relative to original FBSS and random selection; this is a single simulation setting, not a general bound.
- In Fig. 8, D-Q reward flattens after roughly 900 slots for tested epsilon values 0.2, 0.5, and 0.9. In the single Fig. 9 run, prior-informed learning converges after roughly 800 slots while the no-prior case does not; the paper itself treats one run as weak evidence.
- Over 100 Monte Carlo runs at epsilon 0.2, the text reports an 11.9% network energy-efficiency improvement from sensing-prior initialization. Figure-derived distributions span 1.6-10.8 times 10^5 with the prior and 0.2-11.6 times 10^5 without it.
- In the same experiment, per-terminal positioning errors span 5.6-37.8 m with improved FBSS and 13.2-52.1 m for the benchmark. Eight of ten terminals improve by 24%-96%, while GT-4 and GT-10 do not; the paper summarizes average sensing accuracy as improving by at least about 20%.
- Against naive random decisions, Fig. 12 reports energy-efficiency gains from 5.82% to 174.56%, a 50% probability of exceeding 49.6%, and an average gain above 40%. This headline communication comparison is against random actions, not a modern MARL baseline.

## Limitations

The evaluation is simulation-only and assumes clear LoS links, compensated synchronization error, known trajectories and UAV positions, stationary terminals, known measurement covariance, and a QoS-feasible terminal for every UAV. The energy metric includes transmit power but omits propulsion, sensing, processing, and fixed circuitry, so it is not whole-platform [[overall-energy-efficiency]].

The two-state tabular model does not represent channel history or richer network state, and its action space grows with terminal and power choices. Independent-learner nonstationarity and convergence are not analyzed; the nonstandard monotone update has no convergence proof. The division between centrally issued schedules and distributed learning is also not fully specified. No flight tests, runtime study, synchronization/CSI sensitivity analysis, or comparison with modern multi-agent RL is provided.

## Relation to the corpus

This source connects [[tdoa-based-uav-localization]] and [[integrated-sensing-and-communication]] to communication resource learning through a sensing-derived table prior. It extends the authors' UAV-swarm ISAC line in [[zhu-2024-sensing-comm-doppler-uav-swarm]] and differs from communication-only independent learning by making anchor geometry affect action initialization.

## Raw artifacts

- Parse: `raw/sources/Resource_Allocation_for_UAV_Swarm-Assisted_Green_ISAC_Networks_via_Multi-Agent_RL/Resource_Allocation_for_UAV_Swarm-Assisted_Green_ISAC_Networks_via_Multi-Agent_RL.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
