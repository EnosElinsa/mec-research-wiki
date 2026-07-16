---
type: source
title: "System Cost Optimization-Based Task Offloading for UAV-Assisted LEO Satellite Networks"
authors: ["Elhadj Moustapha Diallo", "Rong Chai", "Amayika Kakati", "Chao Yang", "Mohamed Basher Omer", "Linji Ye", "Chengchao Liang", "Qianbin Chen"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3654247"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1980-1993"
modeling_card: required
tags: [source, leo-satellite-edge-computing, space-air-ground-integrated-network, task-offloading, uav-trajectory-control, mobile-edge-computing, mixed-integer-nonlinear-programming]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[linear-programming]]"
  - "[[chen-2024-ulse-game]]"
  - "[[zhang-2024-coma-satellite-offloading]]"
  - "[[rong-chai]]"
  - "[[qianbin-chen]]"
created: 2026-07-07
updated: 2026-07-16
---

# System Cost Optimization-Based Task Offloading for UAV-Assisted LEO Satellite Networks

## Citation

Diallo, E. M., Chai, R., Kakati, A., Yang, C., Omer, M. B., Ye, L., Liang, C., & Chen, Q. (2026). *System Cost Optimization-Based Task Offloading for UAV-Assisted LEO Satellite Networks*. **IEEE Transactions on Green Communications and Networking**, 10, 1980-1993. DOI: 10.1109/TGCN.2026.3654247. The local parse title has "Ofloading"; DOI/venue/page metadata were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Optimizes task offloading in a UAV-assisted LEO satellite network where IoT devices send tasks to UAVs and UAVs either compute locally or offload to LEO satellites. The paper minimizes a weighted system cost combining dropped-task penalty and energy consumption by jointly optimizing IoT task transmission, UAV trajectory, transmit power, and offloading/computing schedules.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Static IoT devices send deadline-constrained tasks to multiple fixed-altitude UAVs, which either compute locally or forward tasks to moving LEO satellites. A central controller schedules collection, execution, and forwarding before transmission and drops tasks predicted to miss their deadlines.

**Problem & objective**: The mixed-integer nonlinear program minimizes a weighted sum of task-drop cost and flight, transmission, and execution energy, $\min C=\omega_1\sum_k(1-\gamma_k)\eta_k^d+\omega_2E$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| IoT-to-UAV transmission | $\lambda_{k,n,t}$ | binary, $\{0,1\}$ | Whether device $k$ uploads its task to UAV $n$ in slot $t$ |
| UAV offloading or local execution | $x_{k,n,m,t}$ | binary, $\{0,1\}$ | Whether UAV $n$ executes locally for $m=0$ or forwards task $k$ to satellite $m$ |
| Satellite execution | $y_{k,n,m,t}$ | binary, $\{0,1\}$ | Whether satellite $m$ executes task $k$ from UAV $n$ in slot $t$ |
| UAV transmit power | $P_{k,n,m,t}$ | continuous, $0\leq P_{k,n,m,t}\leq P_n^{\max}$ | Power used for UAV-to-satellite forwarding |
| UAV position | $\mathbf q_{n,t}^{u}$ | continuous, $\mathbb R^2$ | Horizontal position of UAV $n$ in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C3 | Each UAV collects, processes, or forwards at most one task per slot, and each satellite executes at most one task per slot |
| C4-C6 | Collection precedes UAV or satellite execution, and a dropped task is neither transmitted nor executed |
| C7 | UAV forwarding power is bounded, $0\leq P_{k,n,m,t}\leq P_n^{\max}$ |
| C8-C11 | Each hop finishes within one slot and meets the task's minimum transmission rate |
| C12 | Slot-to-slot UAV movement obeys the speed limit, $\lVert\mathbf q_{n,t+1}^{u}-\mathbf q_{n,t}^{u}\rVert\leq\nu_n^{\max}\tau$ |
| C13 | UAVs maintain collision separation, $\lVert\mathbf q_{n,t}^{u}-\mathbf q_{n',t}^{u}\rVert^2\geq d_{\min}^2$ |

**Algorithm**: Alternating optimization splits the MINLP into four blocks. A relaxed linear program selects IoT transmissions, SCA convexifies UAV trajectories, Lagrange-dual updates allocate forwarding power, and a virtual-time-axis heuristic schedules local or satellite execution by task urgency; the blocks repeat until system cost converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Diallo et al. [x] studied deadline-aware task execution in a UAV-assisted LEO network where IoT tasks are collected by UAVs and then computed onboard or forwarded to satellites. They minimized a weighted sum of task-drop penalties and flight, transmission, and execution energy over collection schedules, offloading and execution decisions, UAV powers, and trajectories. Their alternating solution combines a relaxed linear program, successive convex approximation, Lagrange-dual power updates, and a virtual-time-axis scheduling heuristic. Across 500 simulation trials, the method converges in a small number of outer iterations and reports lower system cost and task-dropping rate than the three cited baselines as device load and infrastructure resources vary.

## Problem

IoT devices in remote or infrastructure-poor areas can generate computation-intensive tasks that exceed local resources. UAVs can collect tasks and relay work to LEO satellites, but the joint task scheduling, resource allocation, UAV trajectory, and task-dropping decision is a nonconvex mixed-integer problem. The paper explicitly includes the cost of dropping tasks predicted to miss their deadlines.

## System model

The model contains multiple LEO satellites, multiple UAVs, and multiple static IoT devices over slotted time. UAVs fly at a fixed altitude, collect tasks from IoT devices over free-space LoS links, and may either compute tasks locally or offload them over UAV-satellite links. Each task has data size, computation intensity, and deadline parameters. System cost combines UAV flight energy, task transmission/execution energy, and weighted task-drop cost.

## Method

The original MINLP is decomposed into four subproblems:

- IoT task-transmission scheduling is relaxed and solved as a linear program.
- UAV trajectory is handled through successive convex approximation and first-order Taylor convexification.
- Power allocation is solved with Lagrange-dual updates.
- Task offloading and computing scheduling use a virtual-time-axis heuristic that prioritizes tighter task deadlines.

The alternating iteration-based algorithm repeats the four blocks until convergence.

## Key findings

- MATLAB/STK simulations over 500 independent trials report convergence within a small number of iterations; the parse reports about six iterations for the three-UAV setting and about nine for the five-UAV setting.
- System cost increases as the number of IoT devices grows and decreases when more UAVs are deployed.
- Increasing satellite computing capability reduces system cost by making satellite offloading more attractive.
- The proposed method reports lower system cost than the compared baselines from the paper's references [29], [33], and [36].
- The proposed method has the lowest task-dropping rate in the reported IoT-count sweep.

## Limitations / future work

The parse assumes direct UAV-satellite links. The conclusion names relay-UAV multi-hop transmission as future work when direct UAV-satellite links are unavailable. The model also uses static IoT devices and single-antenna UAVs/satellites; the paper notes mobility and multi-antenna beamforming as future extensions.

## Relation to the corpus

This source extends the wiki's [[leo-satellite-edge-computing]] and [[space-air-ground-integrated-network]] track from satellite-edge scheduling into UAV-assisted LEO task dropping and energy control. It is close to [[chen-2024-ulse-game]] and [[zhang-2024-coma-satellite-offloading]] on LEO/SAGIN offloading, but it stays in a classical decomposition pipeline rather than a game or CTDE multi-agent RL formulation.

## Raw artifacts

- `raw/sources/System_Cost_Optimization-Based_Task_Offloading_for_UAV-Assisted_LEO_Satellite_Networks/System_Cost_Optimization-Based_Task_Offloading_for_UAV-Assisted_LEO_Satellite_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
