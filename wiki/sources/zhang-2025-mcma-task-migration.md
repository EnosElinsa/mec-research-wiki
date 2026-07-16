---
type: source
modeling_card: required
title: "Multi-Agent Deep Reinforcement Learning With Trajectory Prediction for Task Migration-Assisted Computation Offloading"
authors: ["Xinyi Zhang", "Chunyang Wang", "Yanmin Zhu", "Jian Cao", "Tong Liu"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3539945"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, vehicular-mec, task-migration, multi-agent, drl, trajectory-prediction, informer, ctde]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[task-migration]]"
  - "[[vehicular-mec]]"
  - "[[informer-trajectory-prediction]]"
  - "[[ma-pomdp]]"
  - "[[masac]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[discrete-continuous-two-stage-decomposition]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[ctde-multi-agent-drl-protocol]]"
created: 2026-05-28
updated: 2026-07-16
---

# Multi-Agent DRL With Trajectory Prediction for Task Migration-Assisted Computation Offloading

## Citation

Zhang, X., Wang, C., Zhu, Y., Cao, J., & Liu, T. (2025). *Multi-Agent Deep Reinforcement Learning With Trajectory Prediction for Task Migration-Assisted Computation Offloading*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3539945.

## TL;DR

Targets [[vehicular-mec|vehicular MEC]] where high vehicle mobility produces *spatio-temporal load imbalance* across edge servers — some servers overload as a vehicle cluster passes through, others idle. **Task migration** (forwarding work from overloaded to underloaded servers) is the mechanism, but naive migration policies suffer from *hysteresis*: by the time you decide to migrate, the vehicle has moved.

The solution stack — **MCMA** (Mobility-aware Cooperative Multi-Agent DRL):

1. **[[informer-trajectory-prediction|Informer]]-based multi-step trajectory prediction** for all vehicles (centralized, $O(H\log H)$ via ProbSparse self-attention).
2. **Two-stage decision framework**: (a) discrete task-migration-assisted offloading decisions via **MAPPO**, (b) continuous bandwidth + compute resource allocation via **MADDPG**.
3. **MA-DRL** with [[centralized-training-decentralized-execution|CTDE]] — each edge server is an agent with partial observation, sharing global info during training only. The framework is base-model-agnostic: beyond the adopted MAPPO + MADDPG, the paper notes it also admits MADDQN, Qmix, MATD3, and COMA backbones.

Evaluated on synthetic (Grid3×3, Net4) and realistic (Pasubio, Aurelio Costa) traffic traces, with up to 32k vehicles and 18 servers.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple MEC servers collocated with base stations cover non-overlapping road intersections. Mobile vehicles execute tasks locally, offload them to the serving server, or migrate them through multi-hop links between base stations while sharing wireless bandwidth and edge computing capacity.

**Problem & objective**: The NP-hard constrained sequential problem minimizes total task completion latency, $\min_{\mathbf a^o,\mathbf a^{r_b},\mathbf a^{r_c}}\sum_{t=1}^{T}L^t$, and is represented as a multi-agent POMDP.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Execution and migration choice | $a_{i,j,k}^{o,t}$ | binary, $\{0,1\}$ | Select local execution, the serving server, or remote server $k$ for vehicle task $(i,j)$ |
| Bandwidth share | $a_{i,j}^{r_b,t}$ | continuous, $(0,1]$ | Fraction of serving-BS bandwidth allocated to the task |
| Computing share | $a_{i,j}^{r_c,t}$ | continuous, $(0,1]$ | Fraction of destination-server computing capacity allocated to the task |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task has exactly one execution choice: $\sum_{k=1}^{N+1}a_{i,j,k}^{o,t}=1$. |
| C2 | Resource shares are bounded: $a_{i,j}^{r_b,t},a_{i,j}^{r_c,t}\in(0,1]$. |
| C3 | Allocated radio bandwidth cannot exceed the serving BS budget: $\sum_j B_{i,j}^{t}\leq B_i$. |
| C4 | Computing allocated to tasks placed at server $k$ cannot exceed $f_k$. |

**Algorithm**: Predict multi-step vehicle trajectories centrally with Informer, feed the forecasts to the servers, use MAPPO for discrete offloading and migration, use MADDPG for continuous bandwidth and computing allocation, and train both stages cooperatively under CTDE.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] investigated task migration-assisted computation offloading in multi-edge vehicular networks where high mobility creates spatio-temporal load imbalances. They formulated joint computation offloading, task migration, and resource allocation as a POMDP that minimizes total task completion latency under one-choice, bandwidth, and computing-capacity constraints. Their MCMA approach uses an Informer-based multi-step vehicular trajectory prediction module, followed by a two-stage cooperative multi-agent decision framework with MAPPO for offloading and migration and MADDPG for bandwidth and computing-resource allocation. Experiments on synthetic and realistic traffic scenarios show that MCMA consistently attains lower latency and task failure rate than the evaluated heuristic and DRL-based methods while balancing edge and vehicle resource utilization.

## Problem framing

Vehicles move at high speed across an edge-server topology. Each task arrival could be:

- **Locally executed** at the source vehicle.
- **Offloaded** to its current serving server.
- **Migrated** from a loaded server to a less-loaded peer.

Cast as **[[ma-pomdp|MA-POMDP]]** because each server only sees vehicles within its coverage. Joint objective: minimize task latency under server resource constraints, balanced across servers (to avoid spatio-temporal pile-ups).

## Method (Section IV)

### Trajectory prediction (centralized)

- Sliding-window history of length $H$ → predicted future positions of length $B$.
- Input embeds local position + hierarchical time stamps (minute/hour/day) — captures both daily and weekly traffic regularities.
- Encoder uses ProbSparse self-attention + distilling (Informer's signature efficiencies).
- Centralized at training time, but at deployment the predictions are broadcast to all servers — only one prediction module exists.

### Two-stage decision (decentralized)

- **Stage 1 (discrete):** task-migration-assisted offloading — which server (current, or a peer to migrate to) executes each task. Discrete action space, solved with **MAPPO**.
- **Stage 2 (continuous):** bandwidth + compute resource allocation per task. Continuous action space, solved with **MADDPG**, conditioned on the stage-1 offloading decision (concatenated into its observation).

Both stages are policy-gradient/actor-critic (no value-iteration / Q-style stage); the split keeps each stage's action space homogeneous (all-discrete vs all-continuous), easing learning. CTDE applies to both stages.

## Findings

- MCMA achieves lower task completion latency and task failure rate than both heuristic strategies (VE/EO/PO-x/RE) and state-of-the-art DRL methods (M-DRL, AB-MAPPO, MADDQN, MATD3), across synthetic and realistic traces (relative margins are figure-derived/indicative).
- Ablations (w/o-{m&p}, w/o-{a}, w/o-{co}) confirm each component helps: disabling task migration + prediction, adaptive resource allocation, or inter-agent cooperation each degrades performance.
- Per-server load is balanced more evenly (lower load-imbalance) — workloads spread across servers.

## Limitations / future work

- Trajectory prediction is centralized — single point of failure / privacy concern for large-scale IoV.
- Vehicle-to-vehicle (V2V) collaboration not modeled — only vehicle-server and server-server channels.
- Synthetic traces are grid-like; realistic urban deployments may stress the prediction further.

## Cross-link with related sources

- Same MA-POMDP framing as [[peng-2025-drudm-cfg]] and [[qin-2025-bcuav-masac]]; uses CTDE.
- Trajectory prediction is the distinctive ingredient — most other curated sources react to current observations only. This is the corpus's clearest example of using *anticipated* trajectories as a control input, a pattern that also fits the **vehicular** and **low-altitude economy** tracks.
- Compare with [[liu-2026-jppo-en-convntm]]'s [[en-convntm]] which encodes long history — Zhang et al. instead predicts the *future*; both pay $O(H \log H)$-ish cost but for different ends.

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning_With_Trajectory_Prediction_for_Task_Migration-Assisted_Computation_Offloading/Multi-Agent_Deep_Reinforcement_Learning_With_Trajectory_Prediction_for_Task_Migration-Assisted_Computation_Offloading.md`
