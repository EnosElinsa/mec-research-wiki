---
type: source
title: "Multi-UAV Navigation for Partially Observable Communication Coverage by Graph Reinforcement Learning"
authors: ["Zhenhui Ye", "Ke Wang", "Yining Chen", "Xiaohong Jiang", "Guanghua Song"]
year: 2023
url: "https://doi.org/10.1109/TMC.2022.3146881"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 22, no. 7, pp. 4056-4069"
tags: [source, multi-uav, communication-coverage, graph-attention, recurrent-network, maximum-entropy-q-learning, partial-observability]
related:
  - "[[graph-attention-fanet]]"
  - "[[maximum-entropy-deep-q-learning]]"
  - "[[graph-neural-network]]"
  - "[[memory-augmented-multi-uav-navigation]]"
  - "[[parameter-sharing-marl]]"
  - "[[ma-pomdp]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
  - "[[jains-fairness-index]]"
  - "[[pytorch]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Multi-UAV Navigation for Partially Observable Communication Coverage by Graph Reinforcement Learning

## Citation

Ye, Z., Wang, K., Chen, Y., Jiang, X., & Song, G. (2023). *Multi-UAV Navigation for Partially Observable Communication Coverage by Graph Reinforcement Learning*. **IEEE Transactions on Mobile Computing, 22**(7), 4056-4069. DOI: 10.1109/TMC.2022.3146881.

## TL;DR

Combines two-hop FANET graph attention, GRU memory, shared discrete-action Q-values, and maximum-entropy action sampling so locally observing UAVs can trade communication coverage, Jain fairness, and movement energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-altitude UAV base stations navigate a planar region to cover static points of interest. Each UAV observes only a bounded local area and exchanges learned embeddings with neighbors connected through a distance-limited flying ad hoc network.

**Problem & objective**: The policy problem maximizes the terminal coverage-fairness-energy score, $\pi^*=\arg\max_\pi \mathrm{CFE}_T$ with $\mathrm{CFE}_T=c_Tf_T/e_T$, where $c_T$ is cumulative coverage, $f_T$ is Jain fairness, and $e_T$ is average movement energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Decentralized navigation policy | $\pi$ | stochastic policy | Maps each UAV's local observation and recurrent history to action probabilities |
| UAV drag action | $a_i(t)$ | discrete, 17 actions | Hover or apply half or full drag in one of eight planar directions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Local execution | UAV $i$ acts from its local observation and recurrent state rather than the global map |
| Local training | Training samples contain only local information, so the global CFE score is unavailable as a training reward |
| FANET adjacency | UAVs exchange embeddings only when their distance is below $D_{\mathrm{Com}}$ |
| Stable coverage | A point is covered only when its horizontal distance to a UAV is below $R_{\mathrm{Cov}}$ |
| Action set | Every movement command belongs to the prescribed 17-action drag set |

**Algorithm**: SDRGN encodes each local observation, aggregates two-hop neighbor information with two graph-attention layers, and carries history through a GRU. A temperature-softmax maximum-entropy policy samples discrete actions and is trained with replay, a target network, and a soft Bellman loss; a local heuristic reward combines exclusive coverage, neighbor coverage, and movement energy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ye et al. [x] formulated partially observable multi-UAV coverage as decentralized policy optimization over cumulative coverage, Jain fairness, and movement energy. Their SDRGN controller combines two-hop graph attention, GRU memory, parameter sharing, and maximum-entropy discrete action sampling. A local heuristic reward enables training without exposing the global coverage-fairness-energy score to individual UAVs. With twenty UAVs, SDRGN achieved the highest reported CFE score of 0.5436 among the listed methods while using less movement energy than the deterministic DRGN variant. Adding recurrent memory to the graph network improved coverage, fairness, and CFE over DGN in the reported ablation. Network-only inference on a Jetson Nano averaged 0.0232 seconds over the measured executions.

## Problem and system model

Fixed-altitude UAV base stations navigate a continuous planar map containing clustered static points of interest. Each UAV observes only a bounded local map and exchanges embeddings with neighbors inside a distance-defined flying ad hoc network. Seventeen drag actions represent hover plus two magnitudes in eight directions.

The terminal score multiplies cumulative coverage and Jain fairness, then divides by average movement-energy index. The local reward instead uses exclusive and neighbor coverage divided by local movement energy, so alignment with the global score is empirical rather than guaranteed.

## Method

DRGN encodes each local observation, applies two [[graph-attention-fanet|FANET graph-attention]] layers for a two-hop information field, and feeds the result plus recurrent state into a GRU. SDRGN converts the discrete Q-values into a temperature-softmax policy, samples actions, and learns with replay, a target network, and a soft Bellman loss through [[maximum-entropy-deep-q-learning]]. Homogeneous UAVs share one policy.

The detailed algorithm centrally collects local experiences, while a fully distributed replay/training variant is described only in prose. Neither variant uses a privileged global critic state.

## Key findings

- With 20 UAVs, SDRGN reports CFE `0.5436 +/- 0.1210`, the highest listed score; its coverage and fairness are slightly below deterministic DRGN while its energy index is lower.
- The paper reports GRU-equipped DRGN improving coverage by 0.018, fairness by 0.038, and CFE by 0.031 over DGN, with 0.017 more energy overhead.
- A policy trained with 20 UAVs is evaluated from 5 to 40 UAVs in the same simulator; exact per-size values are figure-only.
- Graph policies degrade under random communication drops, while the text reports SDRGN remains strongest even at complete edge loss.
- Jetson Nano inference averages `0.0232 +/- 0.0037` s over 500,000 executions; this benchmarks the network only, not an airborne system.

## Limitations

The study is simulation-only and uses geometric distance thresholds rather than fading, interference, capacity, or communication energy. Flight is planar with no obstacles, wind, collision constraints, or continuous dynamics. Points of interest are static and synthetic. The local reward has no global-performance guarantee, the distributed-training variant lacks pseudocode and cost measurements, and scalability is tested only to 40 agents in one simulator.

## Relation to the corpus

This source extends the communication-coverage controller in [[liu-2020-distributed-uav-coverage-navigation]] with learned neighbor selection and temporal memory. It is adjacent to [[memory-augmented-multi-uav-navigation]], but uses recurrent graph embeddings rather than centralized critics over longer observation histories.

## Raw artifacts

- Parse: `raw/sources/Multi-UAV_Navigation_for_Partially_Observable_Communication_Coverage_by_Graph_Reinforcement_Learning/Multi-UAV_Navigation_for_Partially_Observable_Communication_Coverage_by_Graph_Reinforcement_Learning.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
