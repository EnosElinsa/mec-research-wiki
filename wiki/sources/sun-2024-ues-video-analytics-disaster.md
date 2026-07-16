---
type: source
modeling_card: required
title: "Optimal Task Offloading and Trajectory Planning Algorithms for Collaborative Video Analytics With UAV-Assisted Edge in Disaster Rescue"
authors: ["Hui Sun", "Xiuye Zhang", "Bo Zhang", "Kewei Sha", "Weisong Shi"]
year: 2024
url: "https://doi.org/10.1109/TVT.2023.3344281"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, post-disaster-mec, video-analytics-offloading, ddqn, differential-evolution, uav-trajectory-control, task-offloading, energy-latency-tradeoff]
related:
  - "[[post-disaster-mec]]"
  - "[[video-analytics-offloading]]"
  - "[[ddqn]]"
  - "[[differential-evolution]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[zhou-2024-jdl-abs-postdisaster-rescue]]"
created: 2026-06-01
updated: 2026-07-16
---

# Optimal Task Offloading and Trajectory Planning Algorithms for Collaborative Video Analytics With UAV-Assisted Edge in Disaster Rescue

## Citation

Sun, H., Zhang, X., Zhang, B., Sha, K., & Shi, W. (2024). *Optimal Task Offloading and Trajectory Planning Algorithms for Collaborative Video Analytics With UAV-Assisted Edge in Disaster Rescue*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3344281. (Manuscript received 5 July 2023; accepted 12 December 2023; date of publication 19 December 2023; date of current version 16 May 2024, so the wiki year is 2024.)

## TL;DR

A **UAV-assisted-edge video-analytics** system for **disaster rescue** that explicitly targets the **battery constraints of smart cameras (ECs)**, which prior work neglects. A **UAV-mounted edge server (UES)** operates in discrete, variable-length time slots, alternating between flying to a new offloading point and hovering to serve nearby ECs. Two nested optimizations: a **differential-evolution-based task-offloading** algorithm minimizes per-slot EC computing overhead (local optimization), and a **double deep Q-learning (DDQN)** trajectory-planning algorithm minimizes long-term energy/overhead and **extends the EC-system lifetime** (global optimization). Reported results: the offloading algorithm is more accurate and converges faster than four state-of-the-art strategies, and the trajectory algorithm **doubles the system's lifetime** while cutting energy and total overhead.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV-mounted edge server visits disaster-region offloading points and serves heterogeneous battery-powered smart cameras performing video analytics. Each variable-length slot contains a flight phase and a hover phase; binary camera offloading, channel assignment, and UES resource allocation determine local overhead and the camera-network lifetime.

**Problem & objective**: The nested design minimizes per-slot camera computing overhead and maximizes the long-term camera-system lifetime, represented by $\min O_{\mathrm{slot}}$ locally and $\max T_{\mathrm{lifetime}}$ globally under latency and battery constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Camera offloading | $x_i(t)$ | binary | Local execution or offload of camera $i$'s analytics task |
| Channel assignment | $c_i(t)$ | discrete | UES channel assigned to camera $i$ |
| UES compute allocation | $f_i(t)$ | continuous, capacity-bounded | Virtual-machine resource assigned to camera $i$ |
| UES trajectory | $\mathbf q(t)$ | discrete region/point action | Offloading point selected by the UES |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | At most one camera uses a UES virtual machine in each slot |
| C2 | Offloaded and locally processed data satisfy the per-slot latency cap |
| C3 | Camera battery energy and UES flight/hover energy remain feasible |
| C4 | Channel interference and UES computing capacity limit simultaneous offloading |
| C5 | UES trajectory stays within the disaster region and serves reachable cameras |

**Algorithm**: Solve the per-slot binary offloading/channel/resource block with improved differential evolution → use a DDQN MDP for long-term UES movement and lifetime reward → nest the local optimizer inside each trajectory step → update the UES policy from energy, overhead, and camera-battery feedback.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied collaborative video analytics with a UAV-assisted edge server in disaster rescue. They jointly considered binary camera offloading, channel and UES-resource allocation, and UES trajectory planning, minimizing local computing overhead and extending the camera-system lifetime under latency and battery constraints. An improved differential-evolution method solves the per-slot offloading and resource block, while a DDQN controller plans long-term UES movement from the resulting energy and overhead feedback. The two optimizers are nested hierarchically across local and global timescales. Simulations report faster and more accurate offloading convergence than four comparison strategies and a stated doubling of system lifetime with lower energy and total overhead.

## Problem framing

In disasters, smart cameras doing video analytics may lose mains power and run on batteries while network infrastructure is disrupted. Offloading video-analytics tasks to a UES extends EC lifetime, but a UES has limited range and compute and so can only serve a subset of ECs at a time. Most prior UES work optimizes UES or device energy without accounting for **EC battery constraints**; yet the EC network's lifetime (time until any one EC's battery is depleted) is what matters for sustained rescue, and ECs are heterogeneous (different data volumes, compute, remaining energy). The two needs, global trajectory planning that considers EC conditions and regional task offloading that picks ECs and allocates UES resources, are coupled but distinct, so the paper models and solves them separately.

## System model

- **Actors.** A disaster area divided into subareas/regions; in each region one UES serves a set of heterogeneous ECs. Focus is on collaborative processing between one UES and its ECs.
- **Time structure.** Variable-length time slots; per slot the UES first flies to an offloading point then hovers to assist ECs. $S$ virtual machines (VMs) on the UES, one EC per VM per slot; a slot ends when all served ECs' analytics complete. A latency cap $T_\text{max}$ enforces real-time processing.
- **Offloading.** A **0-1 (binary) offloading** decision per EC (local execution vs offload to a UES VM); ECs decide based on battery, distance to UES, and channel interference. Output data is small and its feedback latency/overhead is ignored.
- **Models.** Communication model with $K$ channels (interference among ECs on the same channel) and log-distance path loss; execution-time and energy models for local vs offloaded tasks (using measured per-task execution rate/power across heterogeneous task types, e.g. Haar cascades, OpenCV DNNs, Dlib MMOD, YOLOv3); UES flying and hovering energy.
- **Objectives.** Local: minimize per-slot EC computing overhead. Global: extend EC-system lifetime (modeled as a Markov decision process for the UES movement).

## Method

- **Task offloading**: an **improved differential-evolution** algorithm ([[differential-evolution]]) solves the per-slot offloading decision, UES channel allocation, and UES resource allocation.
- **Trajectory planning**: the UES movement is formulated as an **MDP** and solved with a **double deep Q-learning (DDQN)** algorithm ([[ddqn]]) that optimizes energy consumption, feedback reward, and total system overhead, prioritizing assistance to ECs with lower remaining energy.
- The two algorithms are nested hierarchically (regional offloading inside global trajectory planning) and complement each other to extend the EC-system lifetime.

## Key findings

- The DE-based **offloading** algorithm shows **high accuracy and fast convergence** versus four other state-of-the-art strategies (parse).
- The DDQN **trajectory-planning** algorithm **doubles the system's lifetime** while reducing energy consumption and total system overhead (abstract/parse; the "doubling" is the paper's stated headline, with specific curves in the experiment figures).

## Limitations / future work

The study focuses on one UES per region with a 0-1 offloading model and ignores result-feedback latency. The parse does not enumerate an explicit future-work list: `not in parse`.

## Relation to the corpus

A **post-disaster + video-analytics** entry that pairs the two workload/scenario threads: it joins the post-disaster track ([[zhou-2024-jdl-abs-postdisaster-rescue]], [[raivi-2024-jdaco-postdisaster-iot]]) and grounds the [[video-analytics-offloading]] concept alongside [[bao-2025-ddpg-video-offloading]] (UAV+HAP video offload with transcoding). Its distinctive objective is the **EC-network lifetime** (battery-aware), and its solver pairing of **differential evolution** for offloading + **DDQN** for trajectory is a notable hybrid in the corpus. Reinforces [[post-disaster-mec]], [[task-offloading]], and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Optimal_Task_Offloading_and_Trajectory_Planning_Algorithms_for_Collaborative_Video_Analytics_With_UAV-Assisted_Edge_in_Disaster_Rescue/full.md`
- Original PDF (`51a417ff-e883-4afc-9179-ca7f3c146ed3_origin.pdf`) and extracted figures (`images/`) in the same folder.
