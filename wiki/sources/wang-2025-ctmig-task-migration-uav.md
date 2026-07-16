---
type: source
modeling_card: required
title: "Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks"
authors: ["Liang Wang", "Bingnan Shen", "Lianbo Ma", "Yao Zhang", "Yingnan Zhao", "Hongzhi Guo", "Zhiwen Yu", "Bin Guo"]
year: 2025
url: "https://doi.org/10.1109/TSC.2025.3576644"
venue: "IEEE Transactions on Services Computing (IEEE TSC)"
tags: [source, uav-mec, task-migration, imitation-learning, ppo, generative-adversarial-imitation-learning, dynamic-mec]
related:
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[mou-2025-adm-dt-migration]]"
  - "[[shi-2023-two-timescale-migration-rerouting]]"
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[multi-agent-imitation-learning]]"
created: 2026-06-04
updated: 2026-07-16
---

# Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks

## Citation

Wang, L., Shen, B., Ma, L., Zhang, Y., Zhao, Y., Guo, H., Yu, Z., & Guo, B. (2025). *Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks*. **IEEE Transactions on Services Computing**, 18(4). DOI: 10.1109/TSC.2025.3576644. (Received 8 January 2025; accepted 27 May 2025; published 4 June 2025; current version 8 August 2025.)

## TL;DR

Studies a multi-UAV MEC network where mobile users (MUs) offload tasks to UAVs, but as MUs and network conditions change, the initially selected UAV may no longer be optimal, necessitating **task migration** from one UAV to another. Focuses on large-result tasks (video editing, reconnaissance) where the downlink result delivery delay is non-trivial (A2G download rate drops sharply with distance). Formulates a joint **task offloading + migration** (CTMiG) problem minimizing total latency. Proposes **ILCTS**: imitation learning combining an improved PPO policy (generates expert data) with **Generative Adversarial Imitation Learning (GAIL)** for online policy refinement. Achieves superior training accuracy and average latency over RL and heuristic baselines.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile users generate hard- or soft-deadline tasks in a dynamic multi-UAV MEC network; an SDN controller chooses an initial serving UAV and may migrate a partially executed task over more stable inter-UAV links.

**Problem & objective**: CTMiG minimizes average realized task latency, $\min_{\{y_{i,j}^t\}}\frac{1}{M}\sum_i\mathcal L_i$, while satisfying task deadlines and UAV capacity.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Serving-UAV assignment | $y_{i,j}^t$ | binary | Assign MU $i$ to UAV $j$ at slot $t$ |
| MDP action | $a_t^i$ | discrete, $\{0,1,\ldots,U\}$ | Keep the current UAV or switch to a target UAV |
| Policy action distribution | $\pi(a_t^i\mid s_t^i)$ | probability over actions | Learned offloading or migration policy |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Assignment is binary: $y_{i,j}^t\in\{0,1\}$. |
| C2 | Each MU selects one serving UAV: $\sum_jy_{i,j}^t=1$. |
| C3 | UAV workload is bounded: $\sum_i y_{i,j}^t\mu_i\leq1/\varpi_j$. |
| C4 | Hard tasks meet $\mathcal L_i\leq dl_i$; soft tasks meet $\mathcal L_i\leq dl_i+\Delta t_i$. |
| C5 | Soft-task migration can be deferred when $\Psi_i^t\geq\varsigma$ and estimated latency remains within the relaxed deadline. |

**Algorithm**: Train an improved PPO policy offline to generate expert trajectories, then refine online with GAIL in the ILCTS generator-discriminator loop; the policy acts on task, UAV-resource, and channel state features.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] formulate dynamic multi-UAV MEC task serving as joint offloading and migration for large-result tasks. The CTMiG objective minimizes average latency with binary one-UAV assignments, capacity limits, and separate hard and soft deadline constraints. ILCTS first trains an improved PPO expert and then uses GAIL to refine online offloading or migration actions from task, UAV, and channel state. The reported experiments show lower average latency and better training accuracy than PPO alone, DQN, and heuristic policies.

## Problem framing

Most UAV-MEC works assume result sizes are negligible and channels are stable. This paper relaxes both: (i) large results make downlink delay significant; (ii) A2G transmission rate drops sharply with distance (14 Mbps to 2 Mbps as distance increases from 300 to 325 meters, per the paper's Fig. 1 discussion), while A2A (inter-UAV) channels are more stable. When an MU moves far from its serving UAV, migrating partially-computed tasks to a closer UAV (via A2A links) can reduce total delay. The policy must jointly decide initial offloading and ongoing migration in response to environmental dynamics.

## System model

- **Multiple UAVs** with MEC servers, communicating via A2A links. **Multiple mobile users** with continuously arriving tasks.
- **A2G channel:** distance-dependent, high variability (empirically measured, parse Section I).
- **A2A channel:** lower path-loss variation than A2G.
- **Task model:** each task has a data size and compute requirement; partial results may be migrated mid-execution to a different UAV.
- **ILCTS algorithm:** (1) improved PPO trained first to generate expert demonstrations; (2) GAIL uses the expert data as reference and explores new policies via online learning to continuously improve beyond the expert.
- **Objective:** minimize average total task processing + delivery latency for all MUs.

## Key findings

- ILCTS achieves **superior training accuracy and lower average latency** compared to baseline DRL methods (PPO alone, DQN, heuristic greedy) in dynamic multi-UAV networks (parse abstract + Section VI).
- GAIL's online exploration enables the agent to improve beyond the PPO expert, especially in novel/dynamic scenarios not covered by expert demonstrations (parse Section IV-V).
- Migration via stable A2A links effectively mitigates the large-result delivery delay when MUs move away from their serving UAV (parse motivation + Section I).

## Limitations / future work

The paper is simulation-based. UAV trajectory optimization is not included: UAVs remain stationary at predefined positions, while MUs move continuously; only offloading + migration decisions are optimized.

## Relation to the corpus

Extends the task-migration literature ([[mou-2025-adm-dt-migration]], [[shi-2023-two-timescale-migration-rerouting]]) to the UAV-MEC setting with explicit A2A migration paths. The GAIL approach (combining PPO + imitation learning) is a novel solver family not seen in other corpus sources. The large-result-delivery framing distinguishes this from papers that treat downlink as negligible.

## Raw artifacts

- Parse: `raw/sources/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/full.md`
- Origin PDF: `raw/sources/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/48fff01b-84b5-45c8-b1cb-1065a9ac9683_origin.pdf`
- Figures: `raw/sources/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/images/`
