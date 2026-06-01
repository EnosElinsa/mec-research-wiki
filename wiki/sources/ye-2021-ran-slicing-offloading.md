---
type: source
title: "Joint RAN Slicing and Computation Offloading for Autonomous Vehicular Networks: A Learning-Assisted Hierarchical Approach"
authors: ["Qiang Ye", "Weisen Shi", "Kaige Qu", "Hongli He", "Weihua Zhuang", "Xuemin Shen"]
year: 2021
url: "https://doi.org/10.1109/OJVT.2021.3089083"
venue: "IEEE Open Journal of Vehicular Technology (IEEE OJVT)"
tags: [source, vehicular-mec, network-slicing, computation-offloading, two-timescale-optimization, multi-agent-q-learning, load-balancing-uav-mec, network-function-virtualization]
related:
  - "[[vehicular-mec]]"
  - "[[network-slicing]]"
  - "[[network-function-virtualization]]"
  - "[[task-offloading]]"
  - "[[two-timescale-optimization]]"
  - "[[multi-agent-q-learning]]"
  - "[[load-balancing-uav-mec]]"
  - "[[dynamic-qos-constraints]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[duan-2023-moto-smallcell-offloading]]"
  - "[[sun-2025-tjcct-twotimescale-uav-mec]]"
created: 2026-06-02
updated: 2026-06-02
---

# Joint RAN Slicing and Computation Offloading for Autonomous Vehicular Networks: A Learning-Assisted Hierarchical Approach

## Citation

Ye, Q., Shi, W., Qu, K., He, H., Zhuang, W., & Shen, X. (2021). *Joint RAN Slicing and Computation Offloading for Autonomous Vehicular Networks: A Learning-Assisted Hierarchical Approach*. **IEEE Open Journal of Vehicular Technology**. DOI: 10.1109/OJVT.2021.3089083. (Received 29 May 2021; accepted 7 June 2021; date of publication 14 June 2021; date of current version 1 July 2021 → year 2021. Presented in part at IEEE ICC 2021.)

## TL;DR

A **two-timescale** framework that jointly optimizes **RAN slicing** and **computation task offloading** for a **cloud-enabled autonomous vehicular network (C-AVN)**, aiming to maximize both communication and computing resource utilization with diverse QoS guarantees. On the **small timescale** (milliseconds), task scheduling is a stochastic optimization for long-term network-wide **computation load balancing** with **minimal task-offloading variations**, solved by **cooperative multi-agent deep Q-learning (MA-DQL) with fingerprint** to learn stationary, stably-converging offloading policies. On the **large timescale** (hours), given the offloading decisions, **RAN slicing** (radio-resource slicing ratios across base stations) is a **convex** program maximizing aggregate network utility with **statistical (delay-violation) QoS**. The two are coupled in a **hierarchical** joint-optimization loop solved iteratively, and simulations report gains over state-of-the-art schemes.

## Problem framing

Autonomous vehicles (AVs) generate sensing-driven computing tasks (object detection, data fusion, localization) that can overwhelm on-board processing, so tasks are offloaded over C-V2X to multi-tier edge servers. Two coupled issues arise: (i) determining a **task-offloading policy** that balances network-wide computation load over **sequential** scheduling slots (solving one-shot optimizations per millisecond slot is intractable, and offloading *switching cost* between slots matters); and (ii) how **radio-resource allocation** affects offloading — if slicing can't meet per-task rate/latency/reliability needs, load can't be balanced. The paper explicitly characterizes the impact of radio-resource slicing on computation load balancing so that **both** communication and computing utilization are maximized — a joint view prior work largely left separate.

## System model

- **Network.** A two-tier uplink C-AVN: one macro-cell base station (MBS $S_0$) underlaid by n small-cell base stations (SBSs $S_1,\dots,S_n$); set $\mathcal{B}=\{S_0,\dots,S_n\}$. A two-layer edge-computing infrastructure attaches a main server (to the MBS) over n local servers (to the SBSs), hosting virtualized radio functions (BBUs, RRC) on an **NFV** platform; an **SDN-enabled RAN slicing controller** in the main server partitions a pooled radio resource into per-BS slices. The road under the MBS is partitioned into Z zones; AVs in a zone share an offloading decision per slot.
- **Task model.** Two offloadable autonomous-driving task types (object detection, data fusion) of fixed size H bits with latency bound D = scheduling-slot duration T and a minimum frame-rate (LDM update) requirement; task generation is Bernoulli with activation probability p. The transmission time dominates (processing + result-return delays are negligible).
- **Communication.** Shannon-rate uplink with pre-configured MBS/SBS resources $W_m, W_s$; SBSs reuse resources under controlled inter-cell interference (SINR/SNR per zone), with path loss, log-normal shadowing, and Rayleigh fading. A fluid-flow mobility model links AV density to mean velocity per zone.
- **Objectives.** Small timescale: minimize a weighted sum of the **load-imbalance cost** (max instantaneous computation level across servers) and the **offloading-switching cost** between consecutive slots. Large timescale: maximize aggregate network utility from radio-resource slicing under **statistical QoS** (delay-violation probability bound $\varepsilon$).

## Method

- **Small-timescale task scheduling (MDP → MA-DQL).** The load-balancing-with-minimal-variation problem is formulated as a constrained MDP (communication-latency + computation-capacity constraints). With a large problem size and unknown state-transition probabilities, the paper uses **cooperative multi-agent deep Q-learning with fingerprint** (each BS is an agent; the fingerprint augments local observations to stabilize multi-agent learning) to learn stationary task-offloading policies with stabilized convergence.
- **Large-timescale RAN slicing (convex).** Given offloading decisions, the radio-resource slicing ratios $\gamma_k$ at BSs are optimized by a **convex optimization program** maximizing overall communication-resource utilization with statistical QoS provisioning.
- **Hierarchical joint optimization.** Because the two timescales are correlated (slicing affects load balancing), a **learning-assisted hierarchical** algorithm iterates between them to jointly maximize communication and computing resource utilization.

## Key findings

- Simulations are reported to show the proposed framework outperforming benchmark schemes in **communication and computing resource utilization with QoS guarantees** and in **adaptation to AV traffic-load variations**. Specific numeric margins are figure-derived; treat exact values as indicative.

## Limitations / future work

The evaluation is simulation-based, and several modeling assumptions are made for tractability (zone-uniform offloading decisions, dominant transmission delay, a specific inter-small-cell interference structure). Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **vehicular MEC** entry that is distinctive in the corpus for coupling **RAN slicing** (radio-resource virtualization/slicing) with computation offloading across **two timescales**, rather than optimizing offloading alone. Its NFV/SDN slicing layer connects to the satellite-ground VNF-selection work [[zhang-2025-vnf-sgin-dql]] and grounds [[network-slicing]] / [[network-function-virtualization]]; its computation-load-balancing objective relates to [[load-balancing-uav-mec]] and the small-cell load-balancing offloading of [[duan-2023-moto-smallcell-offloading]]. The cooperative multi-agent Q-learning backbone grounds [[multi-agent-q-learning]], and the explicit two-timescale (fast scheduling / slow slicing) structure parallels the two-timescale UAV-MEC scheme [[sun-2025-tjcct-twotimescale-uav-mec]] (see [[two-timescale-optimization]]). Among vehicular-MEC neighbors it sits beside the P-DQN offloading of [[ma-2025-pdqn-vehicular-mec]] and the task-migration MCMA scheme [[zhang-2025-mcma-task-migration]].

## Raw artifacts

- `raw/sources/Joint_RAN_Slicing_and_Computation_Offloading_for_Autonomous_Vehicular_Networks_A_Learning-Assisted_Hierarchical_Approach/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
