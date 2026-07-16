---
type: source
title: "Erasure Coding-Based Cost-Optimized and Latency-Aware Data Storage in UAV-Enabled Edge Systems"
authors: ["Zhaoxiang Huang", "Zhiwen Yu", "Liang Wang", "Huan Zhou", "Erhe Yang", "Bin Guo"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3594283"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-edge-storage, erasure-coding, post-disaster-mec, hierarchical-reinforcement-learning, ddqn, ppo, convlstm]
related:
  - "[[erasure-coded-edge-storage]]"
  - "[[post-disaster-mec]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[ddqn]]"
  - "[[ppo]]"
  - "[[convlstm]]"
  - "[[device-to-device-communication]]"
  - "[[coded-caching]]"
created: 2026-07-07
updated: 2026-07-16
---

# Erasure Coding-Based Cost-Optimized and Latency-Aware Data Storage in UAV-Enabled Edge Systems

## Citation

Huang, Z., Yu, Z., Wang, L., Zhou, H., Yang, E., & Guo, B. (2026). *Erasure Coding-Based Cost-Optimized and Latency-Aware Data Storage in UAV-Enabled Edge Systems*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3594283.

## TL;DR

Introduces **erasure-coded data storage** for UAV-enabled edge systems in disaster or infrastructure-poor settings. Instead of storing full replicas on UAVs, a file is split into $k$ data blocks and $m$ parity blocks, and a user can recover the file from any $k$ coded blocks. The problem jointly chooses coding parameters, block placement across mobile UAVs, and block-access routes to minimize storage cost plus average user access delay. The proposed ME-HDRL framework combines CNN+ConvLSTM trajectory prediction, DDQN UAV agents for data/parity/none placement, a PPO edge agent for access decisions, and an action filter that removes infeasible actions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A vehicle-mounted edge server stores an original file, a mobile UAV network stores erasure-coded data and parity blocks, and moving users recover a file from any $k$ coded blocks. Blocks can arrive from the covering UAV, neighboring UAVs through D2D links, or the remote edge server.

**Problem & objective**: The joint storage and access problem minimizes $\xi\frac{\mathrm{Cost}}{C_{\max}}+(1-\xi)\lim_{\tau\to\infty}\frac{1}{\tau}\sum_{t=1}^{\tau}\sum_{d=1}^{D}\frac{T_d(t)-T_{\min}}{T_{\max}-T_{\min}}$, balancing normalized coded-storage cost and long-term normalized user access delay.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Erasure-code parameters | $(k,m)$ | integer | Numbers of data and parity blocks |
| Block placement | $x_u,b_u$ | binary | Store a data block, parity block, or neither at UAV $u$ |
| Local, D2D, and edge access | $w_d^u,j_d^{u',u},o_d^{s,u}$ | binary or integer count | Sources of the $k$ blocks requested by user $d$ |
| Bandwidth allocation | $h_u,\phi_{u,d},e_{u,i}$ | continuous, $[0,1]$ | Edge, user, and inter-UAV bandwidth shares |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each UAV stores at most one coded block: $x_u+b_u\in\{0,1\}$ |
| C2 | The code uses a feasible recovery threshold: $2\le k\le U$ |
| C3 | Every request obtains exactly the $k$ blocks needed for decoding |
| C4 | A selected local or neighboring UAV must be connected and store the required block |
| C5 | All edge, user, and D2D bandwidth shares are bounded and satisfy aggregate capacity limits |

**Algorithm**: ME-HDRL predicts future user trajectories with a CNN-ConvLSTM model, then solves the two decomposed decisions hierarchically. UAV DDQN agents choose data-block, parity-block, or no-placement actions; a PPO edge agent chooses block sources and bandwidth; and an action filter removes access actions that target unavailable blocks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] introduced erasure-coded storage for a mobile UAV edge system in which users recover files from local, neighboring, or remote-edge blocks. They minimized a weighted combination of normalized storage cost and long-term access delay over coding, placement, retrieval, and bandwidth decisions under recoverability, availability, connectivity, and resource constraints. ME-HDRL combines CNN-ConvLSTM trajectory prediction, DDQN placement agents, a PPO access agent, and an infeasible-action filter. For 121 to 144 MB files, it reduced transmission delay by 58%, 48%, 54%, 37%, and 24% versus EG-CPS, RVA, JSAC24, BD3QN-CC, and HDRL, respectively, while trajectory prediction lowered storage cost by up to 20% versus HDRL.

## Problem framing

UAVs can provide emergency edge storage when terrestrial infrastructure is unavailable, but full replication wastes scarce UAV storage and can increase access delay when the requested data sits far from the user. Erasure coding reduces redundancy cost, yet it makes placement and retrieval harder because the system must ensure that enough coded blocks are reachable through a time-varying, partially connected UAV network.

## System model

- **Scenario.** A disaster-relief area with one vehicle-based edge server, multiple hovering UAVs, and mobile users.
- **Coding.** A source file is split into $k$ data blocks and $m$ parity blocks. The edge server stores all blocks; each UAV stores at most one coded block.
- **Access.** A user retrieves $k$ coded blocks from covering UAVs, adjacent UAVs, or the edge server through UAV relays.
- **Channels.** A2G, A2A, and G2A links are modeled with LoS/NLoS channel terms and bandwidth allocation.
- **Objective.** Minimize a weighted sum of storage cost and normalized average user data-access delay under storage, placement, coding, and connectivity constraints.

## Method

The original problem is a hard MINLP. The paper decomposes it into a data-encoding / placement subproblem and a block-access subproblem. A trajectory-prediction module uses a CNN + ConvLSTM sequence-to-sequence model to forecast future user positions. ME-HDRL then uses multiple DDQN-based UAV agents to decide whether each UAV stores a data block, parity block, or no block, while a PPO-based edge agent decides how users access coded blocks. A shared reward penalizes normalized storage cost and delay, and an action filter accelerates training by masking invalid storage/access choices.

## Key findings

- The action filter nearly doubles training speed in the reported learning curves.
- Raising request probability from 0.65 to 0.9 increases data-access delay by about 44%, illustrating the pressure on coded-block availability.
- At larger file sizes, the proposed method reports storage-cost reductions of up to 20% versus HDRL and larger reductions versus EG-CPS, RVA, JSAC24, and BD3QN-CC baselines.
- At the largest evaluated file size, reported request-delay reductions are 58%, 48%, 54%, 37%, and 24% versus the five baselines.
- Denser UAV networks reduce edge-server fallback traffic; at network density 2.5, storage cost is reported 26% lower than HDRL and transmission delay is substantially lower than sparse settings.

## Limitations / future work

The paper identifies scalability as a remaining issue when the number of UAVs and users grows, especially under fixed UAV storage capacity and limited communication range. Future work points toward more scalable multi-agent systems and richer resource / communication strategy optimization.

## Relation to the corpus

This is the corpus's first **erasure-coded UAV edge-storage** entry. It is adjacent to [[coded-caching]] and [[service-caching-mec]], but the reliability mechanism is coded-block recovery rather than coded cache placement. It strengthens [[post-disaster-mec]] by adding data availability / storage latency to a track otherwise dominated by computation offloading and task aggregation.

## Raw artifacts

- `raw/sources/Erasure Coding-Based Cost-Optimized and Latency-Aware Data Storage in UAV-Enabled Edge Systems/Erasure Coding-Based Cost-Optimized and Latency-Aware Data Storage in UAV-Enabled Edge Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
