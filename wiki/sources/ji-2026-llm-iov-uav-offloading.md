---
type: source
title: "Joint Optimization of Trajectory Control, Resource Allocation, and Task Offloading for Multi-UAV-Assisted IoV"
authors: ["Maoxin Ji", "Qiong Wu", "Pingyi Fan", "Cui Zhang", "Nan Cheng", "Wen Chen", "Khaled B. Letaief"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3700664"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, uav-enabled-its, uav-trajectory-control, llm-assisted-resource-allocation, second-order-cone-programming, linear-programming, task-offloading]
related:
  - "[[vehicular-mec]]"
  - "[[uav-enabled-its]]"
  - "[[uav-trajectory-control]]"
  - "[[llm-assisted-resource-allocation]]"
  - "[[second-order-cone-programming]]"
  - "[[linear-programming]]"
  - "[[two-stage-decomposition]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[dai-2024-uav-vehicular-offloading-lyapunov]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint Optimization of Trajectory Control, Resource Allocation, and Task Offloading for Multi-UAV-Assisted IoV

## Citation

Ji, M., Wu, Q., Fan, P., Zhang, C., Cheng, N., Chen, W., & Letaief, K. B. (2026). *Joint Optimization of Trajectory Control, Resource Allocation, and Task Offloading for Multi-UAV-Assisted IoV*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3700664.

## TL;DR

Studies multi-UAV and base-station-assisted IoV offloading in dense urban environments. The solution decomposes the nonconvex joint problem into 3D UAV trajectory planning by [[second-order-cone-programming|SOCP]], communication-resource scheduling by DRL plus [[llm-assisted-resource-allocation|LLM macro-scheduling]], and task-splitting ratios by [[linear-programming|LP]]. The LLM is not trained as the main controller; it intervenes as an event-triggered semantic scheduler for long-tail failed or surplus tasks, while reward decoupling keeps DRL training tied to the original DRL action.

## Problem framing

Dense urban IoV creates blocked links, high mobility, and bursty task demand. Ground BS resources can saturate, while UAVs can improve line-of-sight coverage only if their 3D positions and resource allocations follow vehicle dynamics. Pure convex optimization is transparent but costly for the full coupled problem; pure MADRL is less interpretable and can degrade under long-tail load spikes. The paper combines solvers so each subproblem uses a method suited to its structure.

## System model

- Vehicles can process locally, offload to UAVs, or offload to a base station.
- UAVs move in 3D with horizontal and vertical energy models, altitude-dependent coverage, collision avoidance, speed, displacement, and separation constraints.
- Resource decisions include resource blocks and transmit power; offloading variables are continuous proportions split among local, UAV, and BS execution.
- Task delay combines transmission, computing, and FIFO queueing delay at UAVs and the BS.
- The objective minimizes normalized delay, energy consumption, and delay-exceeding penalties under coverage, bandwidth, power, queue, and task-partition constraints.

## Method

- **Trajectory stage.** The UAV trajectory subproblem is convexified into sequential SOCPs using load-aware coverage objectives, convexified propulsion-energy terms, and tangent-based collision-avoidance constraints.
- **Resource stage.** A DRL agent generates initial RB/power schedules; an LP then estimates task completion and identifies long-tail failures.
- **LLM macro-scheduler.** A Qwen3-235B-A22B-style MoE LLM is prompted to reallocate resources for failed or surplus tasks. KV caching precomputes static prompt content, and deterministic constraint checking removes invalid actions.
- **Task stage.** Given trajectory and resource allocation, offloading ratios are solved by LP; after an LLM adjustment, a second LP solve gives final task ratios.
- **Reward decoupling.** The DRL replay buffer stores rewards coupled to the original DRL action, not the post-LLM intervention, to avoid biased policy gradients.

## Key findings

- The CVX/SOCP trajectory stage outperforms LVM and MADQN trajectory baselines under the paper's trajectory metric; fixed-altitude constraints narrow the gap, highlighting the importance of altitude control.
- The proposed and DRL-resource-without-LLM variants have the lowest average delay, but the LLM version trades a small delay increase for better fairness and task-success behavior.
- LP-based task allocation has the strongest impact on delay, while MADDPG-based allocation struggles to enforce queue capacity constraints under load.
- The proposed method significantly improves task success rate as load increases by reallocating resources for failed and surplus tasks.
- Under energy-focused weighting, the LP strategy shifts more workload toward UAVs and avoids the BS except for vehicles outside UAV coverage; under high load, all resources are fully used and delay/energy weighting has little remaining effect.

## Limitations / future work

The framework is evaluated in simulation with Python, CVXPY/linprog, and an open-source LLM. The LLM is assumed to run at a grid-powered BS with edge AI accelerators, so its energy cost is decoupled from UAV energy. Future work named in the conclusion includes heterogeneous UAV-swarm coordination and multi-modal LLMs for complex urban semantic-environment perception.

## Relation to the corpus

This is a [[vehicular-mec]] / [[uav-enabled-its]] source that extends the vehicular track from DRL and Lyapunov offloading into LLM-aided scheduling. It complements [[li-2026-isac-vec-beamforming-deployment]], which uses UAV deployment and beamforming for ISAC-enhanced vehicular coverage, and [[dai-2024-uav-vehicular-offloading-lyapunov]], which uses Lyapunov plus Markov approximation for UAV-assisted VEC delay. Its reusable method vocabulary is captured by [[llm-assisted-resource-allocation]], [[second-order-cone-programming]], and [[linear-programming]].

## Raw artifacts

- `raw/sources/Joint Optimization of Trajectory Control- Resource Allocation- and Task Offloading for Multi-UAV-Assisted IoV/Joint Optimization of Trajectory Control- Resource Allocation- and Task Offloading for Multi-UAV-Assisted IoV.md`
- Original PDF and extracted figures (`images/`) in the same folder.
