---
type: source
title: "HAP-UAV-Assisted Hierarchical Aerial Computing Framework for Video Offloading: A Deep Reinforcement Learning Approach"
authors: ["Yifei Bao", "Jinghui Zhang", "Yi Cheng", "Dengyin Zhang", "Rongguo Fu"]
year: 2025
url: "https://doi.org/10.1007/s40747-025-02106-1"
venue: "Complex & Intelligent Systems (Springer)"
modeling_card: required
tags: [source, hap, uav, video-offloading, video-transcoding, ddpg, qoe, post-disaster, hierarchical-aerial-mec]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[ddpg]]"
  - "[[video-analytics-offloading]]"
  - "[[video-transcoding-tradeoff]]"
  - "[[qoe-modeling-mec]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-07-16
---

# HAP-UAV-Assisted Hierarchical Aerial Computing Framework for Video Offloading: A Deep Reinforcement Learning Approach

## Citation

Bao, Y., Zhang, J., Cheng, Y., Zhang, D., & Fu, R. (2025). *HAP-UAV-Assisted Hierarchical Aerial Computing Framework for Video Offloading: A Deep Reinforcement Learning Approach*. **Complex & Intelligent Systems** (Springer). DOI: 10.1007/s40747-025-02106-1.

> **Metadata note:** the parse carries the title, the dates (received 23 May 2025 / accepted 12 Sep 2025 / published online 24 Oct 2025 → year 2025), and "© The Author(s) 2025", but **no DOI line** (only reference DOIs). Venue (**Complex & Intelligent Systems**, Springer) and DOI `10.1007/s40747-025-02106-1` were **web-confirmed** against the Springer record, not taken from the parse.

## TL;DR

A post-disaster scenario where ground camera equipments (CEs) feed video to nearby UAVs, and UAVs split each video chunk between local DNN inference and offloading to a HAPS for inference. Because the UAV → HAPS link is bandwidth-limited at tens of kilometers altitude, **video must be transcoded to a lower bitrate** before offloading — but lower bitrate degrades inference accuracy. The system jointly optimizes:

- offloading ratio η_u(i) ∈ [0,1] per UAV,
- transcoding indicator ε_u(i) ∈ {0,1} and ratio ε_u(i) ∈ [ε_min, 1),
- HAP computation resource allocation φ_u(i) per UAV.

The objective is a **QoE function** combining task delay (transmission + computation) with the average video bitrate after transcoding (proxy for inference accuracy). Solved as an MDP with **DDPG** for continuous control.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In each processing round, ground camera equipments send equal-size video chunks to their pre-associated UAVs over orthogonal CE-to-UAV links. Multiple UAVs follow fixed circular trajectories, split collected video between local inference and one stationary HAP, optionally transcode the HAP-bound fraction, and equally share the HAP uplink bandwidth.

**Problem & objective**: Problem (20), a non-convex mixed-integer program, maximizes cumulative quality of experience, $\max \sum_{i\in\mathcal{I}}\mathrm{QoE}(i)$, where $\mathrm{QoE}(i)=Q(i)-\alpha T^{\mathrm{sys}}(i)$, over offloading, transcoding, and HAP computation allocation decisions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading ratio | $\eta_u(i)$ | Continuous, $[0,1]$ | Fraction of UAV $u$'s collected video offloaded to the HAP in round $i$ |
| Transcoding switch | $\epsilon_u(i)$ | Binary, $\{0,1\}$ | Whether UAV $u$ transcodes its HAP-bound video |
| Transcoding ratio | $\varepsilon_u(i)$ | Continuous, $[\varepsilon_{\min},1)$ | Bitrate ratio applied to transcoded video |
| HAP computation allocation | $\varphi_u(i)$ | Continuous, $[0,1]$ | Fraction of HAP computation capacity assigned to UAV $u$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 20b | Offloading domain, $0\leq\eta_u(i)\leq1$ |
| 20c-20d | Transcoding domains, $\epsilon_u(i)\in\{0,1\}$ and $\varepsilon_{\min}\leq\varepsilon_u(i)<1$ |
| 20e-20f | HAP allocation feasibility, $0\leq\varphi_u(i)\leq1$ and $\sum_{u\in\mathcal{U}}\varphi_u(i)=1$ |
| 20g | Per-UAV battery budget, $\sum_{i\in\mathcal{I}}E_u(i)\leq E$ |

**Algorithm**: The system is written as an MDP with state $\mathcal{S}=\{\mathbf{q}_m^{\mathrm{D}}(i),\mathbf{q}_u^{\mathrm{U}}(i),\mathcal{M}_u(i)\}$, action $\mathcal{A}=\{\eta_u(i),\epsilon_u(i),\varepsilon_u(i),\varphi_u(i)\}$, and reward $r_i=Q(i)-\alpha T^{\mathrm{sys}}(i)$. DDPG selects continuous controls with exploration noise, stores transitions in replay memory, updates the critic from bootstrapped target values, updates the actor by deterministic policy gradients, and softly updates both target networks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bao et al. [x] studied video-analytics offloading in a post-disaster hierarchical aerial computing system with ground camera equipments, multiple UAVs, and one HAP. Each UAV collects video chunks, selects the fraction processed locally or offloaded to the HAP, and may transcode the offloaded fraction before the long-distance UAV-to-HAP transmission. They formulated a non-convex mixed-integer problem that maximizes cumulative QoE, defined by video quality minus a weighted system-delay term, subject to decision-domain, HAP computation-allocation, and UAV-energy constraints. The authors transformed the problem into an MDP and trained a DDPG actor-critic with replay memory and target networks. Simulations reported that DDPG achieved the highest accumulated reward among DDPG, actor-critic, and DQN, while the proposed hierarchical system attained the lowest delay among the evaluated computing configurations. In the reported comparison, a 10.6% reduction in average video bitrate produced an 18.2% improvement in total delay relative to using the original bitrate.

## Why this matters

This is the wiki's first **video-analytics workload** entry. Earlier offloading sources treat tasks as opaque (input-bytes, CPU-cycles, deadline). This paper introduces:

1. **Workload-aware compression.** The data being offloaded is *lossy-compressible*, and compression directly affects the downstream model's accuracy. None of [[liu-2026-jppo-en-convntm]], [[peng-2025-drudm-cfg]], [[zhu-2025-lycnn-drl-wpt-mec]] etc. have this knob.
2. **Three-way tradeoff.** Delay, video quality, and compute resources — not just delay vs energy. The QoE function explicitly bakes the bitrate-accuracy curve into the reward.
3. **Vanilla DDPG suffices.** Continuous offloading + transcoding ratios are pure continuous actions; DDPG fits cleanly. No need for the hybrid-action machinery of [[liu-2026-jppo-en-convntm|j-PPO]] or [[ma-2025-pdqn-vehicular-mec|P-DQN]].

## Method

- **State.** Per-round per-UAV: collected video volume D_u(i), UAV-HAP channel gain proxy, residual energy.
- **Action.** {η_u(i), ε_u(i), ε̄_u(i), φ_u(i)} per UAV.
- **Reward.** −(α·delay + β·(1 − transcoded_bitrate / original_bitrate)) — small Greek-letter weights tune the tradeoff.
- **Algorithm.** DDPG with target networks; OU-noise exploration.

## Findings

- Adaptive transcoding **dominates** fixed-rate transmission. Rather than transcoding everything to a fixed low bitrate, the policy raises bitrate when the channel is good and the offloaded fraction is small.
- DDPG outperforms the AC and DQN baselines used in the paper. DQN explicitly fails to converge because the continuous action space is intractable for value-iteration; AC trains but is unstable in the dynamic disaster environment. (No PPO baseline in the paper — the wiki's [[ddpg-vs-jppo]] comparison should be read as cross-source, not internal to this paper.)
- The QoE-shaped reward avoids the "always offload" failure mode that pure-delay rewards trigger when compute on the HAP is cheap.

## Limitations

- Single HAP, fixed UAV trajectories — no joint trajectory + offloading optimization.
- The bitrate→accuracy curve is fitted offline; in real disaster scenes the curve shifts with content (e.g. low-light, smoke). No online adaptation.
- DNN inference cost ζ·(ε·η·D)^ξ is empirical; the exponent ξ may not generalize across model families.
- Simulation only; no field trial in actual disaster conditions.

## Cross-link with related sources

- **Video-analytics workload class:** new for the wiki. Distinct from the *cooperative perception* workload in [[xie-2026-uav-multisource-fusion]] (which fuses raw observations, not bitrate-controlled video).
- **Hierarchical UAV+HAP MEC:** alongside [[peng-2025-drudm-cfg]], [[nabi-2025-jour-hierarchical-aerial]], [[wang-2026-aerial-marine-msar]], [[jia-2025-dro-uav-hap-mec]].
- **Solver:** vanilla DDPG, comparison-relevant to [[ddpg-vs-jppo]].

## Raw artifacts

- `raw/sources/HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement/full.md`
