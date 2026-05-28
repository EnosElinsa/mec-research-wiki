---
type: source
title: "Multi-Agent Deep Reinforcement Learning With Trajectory Prediction for Task Migration-Assisted Computation Offloading"
authors: ["Xinyi Zhang", "Chunyang Wang", "Yanmin Zhu", "Jian Cao", "Tong Liu"]
year: 2025
url: ""
venue: ""
tags: [vehicular-mec, task-migration, multi-agent, drl, trajectory-prediction, informer, ctde]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[task-migration]]"
  - "[[vehicular-mec]]"
  - "[[informer-trajectory-prediction]]"
  - "[[ma-pomdp]]"
  - "[[masac]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Multi-Agent DRL With Trajectory Prediction for Task Migration-Assisted Computation Offloading

## Citation

Zhang, X., Wang, C., Zhu, Y., Cao, J., & Liu, T. (2025). *Multi-Agent Deep Reinforcement Learning With Trajectory Prediction for Task Migration-Assisted Computation Offloading*.

## TL;DR

Targets [[vehicular-mec|vehicular MEC]] where high vehicle mobility produces *spatio-temporal load imbalance* across edge servers — some servers overload as a vehicle cluster passes through, others idle. **Task migration** (forwarding work from overloaded to underloaded servers) is the mechanism, but naive migration policies suffer from *hysteresis*: by the time you decide to migrate, the vehicle has moved.

The solution stack — **MCMA** (Mobility-aware Cooperative Multi-Agent DRL):

1. **[[informer-trajectory-prediction|Informer]]-based multi-step trajectory prediction** for all vehicles (centralized, $O(H\log H)$ via ProbSparse self-attention).
2. **Two-stage decision framework**: (a) coarse-grained migration decisions, (b) fine-grained offloading + resource allocation.
3. **MA-DRL** with [[centralized-training-decentralized-execution|CTDE]] — each edge server is an agent with partial observation, sharing global info during training only. Compatible with MADDPG, MAPPO, MATD3, Qmix, COMA backbones.

Evaluated on synthetic (Grid3×3, Net4) and realistic (Pasubio, Aurelio Costa) traffic traces, with up to 32k vehicles and 18 servers.

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

- **Stage 1 (coarse):** discrete migration target (which peer server) — naturally Q-style.
- **Stage 2 (fine):** continuous resource allocation per migrated task — naturally policy-gradient style.

The two-stage split keeps each stage's action space small, easing learning. CTDE applies to both stages.

## Findings

- MCMA reduces average task latency vs MADDPG-only and migration-without-prediction baselines, on both synthetic and real-world traces.
- Per-server load imbalance index drops — workloads spread more evenly.
- Two-stage architecture is **base-model-agnostic** — paper demonstrates compatibility with multiple MARL backbones.
- ProbSparse cuts per-step cost from $O(H^2)$ to $O(H\log H)$, making the centralized prediction tractable for tens-of-thousands of vehicles.

## Limitations / future work

- Trajectory prediction is centralized — single point of failure / privacy concern for large-scale IoV.
- Vehicle-to-vehicle (V2V) collaboration not modeled — only vehicle-server and server-server channels.
- Synthetic traces are grid-like; realistic urban deployments may stress the prediction further.

## Cross-link with related sources

- Same MA-POMDP framing as [[peng-2025-drudm-cfg]] and [[qin-2025-bcuav-masac]]; uses CTDE.
- Trajectory prediction is the distinctive ingredient — most other curated sources react to current observations only. This is the first source in the wiki to use *anticipated* trajectories as a control input. Likely to recur in the **vehicular** and **low-altitude economy** papers later in the queue.
- Compare with [[liu-2026-jppo-en-convntm]]'s [[en-convntm]] which encodes long history — Zhang et al. instead predicts the *future*; both pay $O(H \log H)$-ish cost but for different ends.

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning_With_Trajectory_Prediction_for_Task_Migration-Assisted_Computation_Offloading/full.md`
