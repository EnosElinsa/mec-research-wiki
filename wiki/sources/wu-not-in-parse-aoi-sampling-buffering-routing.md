---
type: source
title: "AoI-Aware Joint Sampling-Buffering-Routing Optimization for Autonomous UAV Swarms via a MARL Approach"
authors: ["Haoxu Wu", "Shaohua Wu", "Aimin Li", "Siqi Meng", "Qinyu Zhang"]
year: ""
url: ""
venue: ""
modeling_card: required
tags: [source, age-of-information, autonomous-uav-swarms, fanet, mappo, curriculum-learning, ma-pomdp, uav-data-collection, routing]
related:
  - "[[age-of-information]]"
  - "[[autonomous-uav-swarms]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[mappo]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-data-collection]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[shaohua-wu]]"
  - "[[qinyu-zhang]]"
created: 2026-07-11
updated: 2026-07-16
---

# AoI-Aware Joint Sampling-Buffering-Routing Optimization for Autonomous UAV Swarms via a MARL Approach

## Citation

Wu, H., Wu, S., Li, A., Meng, S., & Zhang, Q. *AoI-Aware Joint Sampling-Buffering-Routing Optimization for Autonomous UAV Swarms via a MARL Approach*. The local parse gives the title and author line but does not expose reliable publication year, venue, or DOI metadata; those fields are left blank rather than inferred.

## TL;DR

Builds an all-aerial monitoring architecture where a leader UAV collects updates and follower UAVs act both as sensing platforms and multi-hop relays. The paper minimizes information staleness by jointly learning sampling, buffer scheduling, and routing decisions with an AoI-aware framework called AASBR and a curriculum-based multi-head MAPPO variant called COMH-MAPPO.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A leader UAV collects fresh packets from follower UAV sensors that also relay packets through a dynamic multi-hop FANET, with bounded buffers and partial local observations.

**Problem & objective**: The AASBR problem minimizes long-term network staleness, $P_1=\min_{\Pi}\lim_{t\to\infty}\frac{1}{t}\sup_{\mathbf u}\mathbb E_\Pi[\sum_t\sum_i\Delta_i(t)]$, while jointly choosing sampling, buffer, and routing policies.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sampling decision | $s_i(t)$ | Binary, $\{0,1\}$ | Generate one fresh packet or wait |
| Next-hop selection | $j$ | Discrete, $j\in\mathcal N_r(i)$ | Select a feasible neighbor or the leader |
| Buffered-packet selection | $pkt_k$ | Discrete, $pkt_k\in B_i(t)$ | Select the packet to transmit |
| Joint policy | $\Pi$ | Stochastic, $\Pi=\{\pi_i\}$ | Map local observations to coupled decisions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Buffer occupancy stays feasible, $0\leq B_i(t)\leq B_i^{\max}$ |
| C2 | Sampling fraction is bounded, $0\leq\sum_t s_i(t)/T_{\max}\leq1$ |
| C3 | At most one outgoing packet is selected per slot, $b_i^{out}(t)=1$ when transmitting |
| C4 | Forwarding uses a current neighbor and an available packet, $j\in\mathcal N_r(i)$ and $pkt_k\in B_i(t)$ |

**Algorithm**: AASBR is solved with COMH-MAPPO, whose separate routing, buffer, and sampling heads use availability masks, centralized training with decentralized execution, and curriculum phases that progressively integrate the coupled decisions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] formulated fully airborne monitoring as a joint sampling, buffer scheduling, and multi-hop routing problem for minimizing long-term Age of Information. The policy chooses a sampling indicator, a feasible neighbor, and a packet from the local buffer while respecting storage and per-slot sampling constraints. Their AASBR framework is solved by COMH-MAPPO, which separates the coupled actions into masked policy heads and trains them through a staged curriculum. The reported simulations show lower average and peak AoI together with improved latency, packet delivery ratio, and throughput than the evaluated MARL and ablation baselines.

## Problem

Remote maritime, disaster, battlefield, and complex-terrain monitoring may not have deployable ground sensors or reliable terrestrial infrastructure. In a fully airborne UAV swarm, data freshness depends on more than link latency: follower UAVs must decide when to sample, which packets to keep or discard in limited buffers, and which relay path should carry fresh packets through a dynamic FANET topology.

## System model

- The system uses a leader-follower UAV swarm. The leader UAV is the sink / aerial collector; each follower UAV senses environmental data, stores packets in a local buffer, and forwards data through multi-hop relay paths.
- The operating region is a bounded 3D volume and the paper models follower UAV mobility with a 3D Gauss-Markov model.
- Each follower UAV has partial local observations, including its position, neighbor connectivity, packet/buffer state, and AoI-related state.
- The objective is to minimize average multi-source AoI at the leader while preserving network-level delivery behavior.

## Method

The paper formulates joint sampling-buffering-routing as a Dec-POMDP. AASBR decomposes the control surface into three coupled decisions: age-aware sampling, intelligent buffer scheduling, and adaptive routing. COMH-MAPPO then assigns separate policy heads to the sampling, buffer, and routing subtasks while using curriculum learning to move from easier fixed-generation behavior toward the full joint policy.

## Key findings

- The abstract reports more than 48% average-AoI improvement over MARL baselines and more than 15% improvement over ablation benchmarks.
- In the detailed table, COMH-MAPPO reaches average AoI `3.84 +/- 0.33`, average peak AoI `16.32 +/- 1.28`, end-to-end latency `1.51 +/- 0.11` time slots, PDR `79.5% +/- 4.2%`, and throughput `9.80 +/- 0.52` packets per time slot.
- The paper reports COMH-MAPPO converging to average AoI 3.84, ablation benchmarks below 7.0, and generic MARL benchmarks around 10.
- In the sampling ablation, the learned sampling rate stabilizes around 0.76, while aggressive full-time sampling degrades AoI through congestion and packet loss.
- Robustness experiments show AoI degrades as follower UAV velocity and network size increase, but COMH-MAPPO keeps lower AoI than the benchmark methods.

## Limitations / future work

The parse has OCR artifacts in punctuation and formulas, so the page relies on stable prose, table values, and stated comparisons. The paper is simulation-based. Future-work text calls out heterogeneous sensor modality selection, energy optimization, larger and more diverse swarms, channel-aware robustness, secure communication against eavesdropping/jamming, joint AoI-energy trajectory planning, and real-world field validation.

## Relation to the corpus

This source extends [[age-of-information]] from UAV data collection and WDC/WET service balancing into fully airborne FANET monitoring. It complements [[shi-2025-aoi-energy-replenishment-multiuav]], which uses VDN/QMIX for UAV charging and sensor-node collection, by focusing instead on follower UAVs as both sensing nodes and relays. Methodologically, it adds a curriculum and multi-head variant of [[mappo]] under [[centralized-training-decentralized-execution]] / [[ma-pomdp]], and it strengthens the [[autonomous-uav-swarms]] and [[stateless-geographic-fanet-routing]] neighborhood without turning the source into an MEC offloading paper.

## Raw artifacts

- `raw/sources/AoI-Aware_Joint_Sampling-Buffering-Routing_Optimization_for_Autonomous_UAV_Swarms_via_a_MARL_Approach/AoI-Aware_Joint_Sampling-Buffering-Routing_Optimization_for_Autonomous_UAV_Swarms_via_a_MARL_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
