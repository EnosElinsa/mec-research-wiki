---
type: source
title: "Computation Offloading in Resource-Constrained Multi-Access Edge Computing"
authors: ["Kexin Li", "Xingwei Wang", "Qiang He", "Jielei Wang", "Jie Li", "Siyu Zhan", "Guoming Lu", "Schahram Dustdar"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3383041"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags:
  - source
  - mobile-edge-computing
  - computation-offloading
  - multi-agent-reinforcement-learning
  - communication-constrained-marl
  - qoe-modeling-mec
  - lyapunov-optimization
  - binary-vs-partial-offloading
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[communication-constrained-marl]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[qoe-modeling-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[soft-actor-critic]]"
  - "[[maddpg]]"
  - "[[chen-2022-qoe-game-end-edge-cloud]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
created: 2026-06-03
updated: 2026-06-03
---

# Computation Offloading in Resource-Constrained Multi-Access Edge Computing

## Citation
Kexin Li, Xingwei Wang, Qiang He, Jielei Wang, Jie Li, Siyu Zhan, Guoming Lu, Schahram Dustdar, "Computation Offloading in Resource-Constrained Multi-Access Edge Computing," *IEEE Transactions on Mobile Computing*, 2024. DOI: 10.1109/TMC.2024.3383041. (Manuscript received 6 Nov 2023; revised 23 Jan 2024; accepted 18 Mar 2024; date of publication 29 Mar 2024; date of current version 3 Oct 2024 → year 2024. Corresponding authors: Xingwei Wang; Qiang He. University of Electronic Science and Technology of China + Northeastern University (Shenyang) + Hubei University + TU Wien.)

## TL;DR
For multi-terminal-device (TD) MEC where the wireless medium is **shared and bandwidth-constrained** — e.g. firefighting robots or UAVs that must coordinate offloading — this paper proposes **Scheduled Multi-agent Deep Reinforcement Learning (SMDRL)**. Each TD learns to **encode messages**, **select actions**, and **schedule itself** from received messages, while a **TopK** mechanism lets only the most important TDs broadcast, keeping coordination low-communication. A **virtual energy(-deficit) queue** decouples a long-term per-device energy cap, turning the long-term QoE-maximization (service delay + energy) into a per-slot MDP. The scheme is shown to reach near-optimal QoE while respecting communication and energy constraints.

## Problem framing
Real MEC applications need teamwork among TDs, but real-world settings are resource-constrained: network connectivity can weaken or drop, and when many TDs share the medium, coordination is hard. Centralized MIP/DRL offloading (e.g. DROO-style, SAC-based) needs to ship large amounts of data to a central server, causing uplink congestion and stripping TDs of local-feature/interaction awareness. Multi-agent DRL (e.g. MADDPG) handles distributed decisions but typically **ignores the cost of the shared communication medium** and assumes free inter-agent messaging — unrealistic when bandwidth is scarce. The paper targets the under-studied problem of computation offloading in **multi-access** MEC with **bandwidth constraints**, where agents must exchange concise but significant information and arbitrate medium access to avoid collisions.

## System model
- **Topology (Fig. 1):** M edge nodes (EN), each an access-point/base-station + edge server with compute f_m and bandwidth B_m; N terminal devices (TDs), each with compute g_n and an **energy cap** e_n^c (motivated by small-battery wearables/medical devices).
- **Tasks:** TD n generates a task with probability λ_n^t per slot, described by data size c_n^t, required CPU cycles z_n^t, and delay tolerance d_n^{t,max}; tasks are **atomic** (binary offloading — local or to one EN).
- **Computation/communication:** local delay z_n^t/g_n and energy ρ_n·z_n^t; EN-side delay z_n^t/f_m and energy ρ_m·z_n^t; uplink over a flat Rayleigh channel divided into orthogonal sub-channels of size b Hz, transmission rate from a Shannon expression with bandwidth-allocation factors, transmission energy c_n^t·ϱ_{m,n}/r_{m,n}^t. Return data is ignored.
- **Constraints:** offloading strategy is binary and mutually exclusive (local xor offload); completion delay ≤ d_n^{t,max}; the **long-term average energy** of each TD must stay ≤ its cap e_n^c; per-EN allocated bandwidth ≤ B_m.
- **Reformulation:** a **virtual energy-deficit queue** Q_n^{t+1} = max{0, Q_n^t + E_n^t − e_n^c} converts the long-term energy constraint into a per-slot drift term, yielding a real-time QoE-maximization objective P1 weighting Q_n^t·E_n^t and delay T_n^t.

## Method
- **MDP + multi-agent learning:** the per-slot offloading is cast as an MDP (state/action/reward over task + TD + EN messages) and solved by SMDRL with **centralized training, distributed execution** (see [[centralized-training-decentralized-execution]]).
- **Learned communication:** the actor network is redesigned to **encode** information for exchange; agents learn what to send and how to act on received messages (a [[communication-constrained-marl|communication-constrained MARL]] design).
- **TopK scheduling:** only the K most-significant TDs broadcast their messages each round, arbitrating the shared medium so coordination works under tight bandwidth — the paper proves the method still reaches close-to-optimal performance under limited communication.

## Key findings
Grounded in the abstract and contributions (specific magnitudes are figure-derived, treated as indicative):
- SMDRL attains **near-optimal QoE** (service delay + energy) while staying within the TDs' communication and energy constraints.
- The TopK low-communication mechanism is reported to retain close-to-optimal performance even when inter-agent communication is restricted.
- The scheme is reported to outperform representative centralized and multi-agent baselines at determining the offloading strategy.

## Limitations / future work
- Results are simulation-based; no hardware deployment despite the robot/UAV framing.
- Tasks are atomic (binary offloading only); partial offloading and task dependencies are out of scope.
- The channel is modeled as flat Rayleigh with returning-data delay ignored, a simplification of real multi-access wireless conditions.
- The number of broadcasting agents K is a design knob whose sensitivity is explored empirically rather than derived.

## Relation to the corpus
This is a multi-agent-DRL offloading entry whose distinctive angle is treating the **inter-agent communication channel itself as a constrained resource** — learned message encoding + TopK scheduling — rather than assuming free coordination, which sets it apart from the corpus's other MADRL offloading work such as [[zhao-2022-matd3-multiuav-ec-offloading]]. Its **QoE** objective (delay + energy) connects it to [[qoe-modeling-mec]] and the potential-game QoE offloading of [[chen-2022-qoe-game-end-edge-cloud]], while its **virtual energy-deficit queue** is the same [[lyapunov-optimization|Lyapunov-style]] long-term-constraint decoupling recurring across the corpus. The learned-communication idea is captured in the new [[communication-constrained-marl]] concept page.

## Raw artifacts
- Parse: `raw/sources/Computation_Offloading_in_Resource-Constrained_Multi-Access_Edge_Computing/full.md`
- Origin PDF: `raw/sources/Computation_Offloading_in_Resource-Constrained_Multi-Access_Edge_Computing/4cb00723-7605-4068-82a9-b4f936db0089_origin.pdf`
- Figures: `raw/sources/Computation_Offloading_in_Resource-Constrained_Multi-Access_Edge_Computing/images/`
