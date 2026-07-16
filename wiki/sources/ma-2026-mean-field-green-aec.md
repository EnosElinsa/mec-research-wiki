---
type: source
title: "Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users: A Mean Field Game Approach"
authors: ["Lianbo Ma", "Dingsige Chen", "Yue-e Zhou", "Jianming Zhao", "Liang Wang", "Qiang He", "Bo Yi", "Min Huang", "Xingwei Wang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3698303"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, aerial-edge-computing, metaverse, mean-field-game, energy-harvesting, task-allocation, lyapunov-optimization, hardware-in-the-loop]
related:
  - "[[mean-field-game]]"
  - "[[energy-harvesting-mec]]"
  - "[[task-offloading]]"
  - "[[load-balancing-uav-mec]]"
  - "[[energy-balancing-uav]]"
  - "[[lyapunov-optimization]]"
  - "[[nash-equilibrium]]"
  - "[[semantic-content-reuse]]"
  - "[[panahi-2026-uav-green-iot-offloading]]"
  - "[[wang-2026-lifelong-semantic-content-reuse]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users: A Mean Field Game Approach

## Citation

Ma, L., Chen, D., Zhou, Y.-e., Zhao, J., Wang, L., He, Q., Yi, B., Huang, M., & Wang, X. (2026). *Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users: A Mean Field Game Approach*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3698303.

## TL;DR

Proposes a green aerial edge computing (GAEC) framework for metaverse users, with computing-enhanced UAVs executing tasks and energy-focused UAVs harvesting ambient energy. A mean field game approximates massive UAV interactions through an individual UAV versus aggregate population state, while Lyapunov optimization sets an energy valuation signal for long-term utility and energy balance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Computing-enhanced UAVs execute metaverse-user tasks while energy-focused UAVs harvest ambient energy and act as energy reservoirs. A dispatcher broadcasts an energy value signal at a large timescale, and each computing UAV makes local task/transmission decisions at a smaller timescale; unprocessed tasks can go to a cloud.

**Problem & objective**: Green aerial edge task allocation, a stochastic mean-field game with Lyapunov control, minimizes long-term task delay and energy cost, $\min\mathbb E[\text{delay}+\text{energy cost}]$, while maintaining battery stability and one-task-per-UAV service constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task assignment | $x_{u,i}(t)$ | binary | Computing UAV $u$ serves task $i$ |
| Local/cloud offloading | $y_i(t)$ | discrete | Task executes locally, at a CE-UAV, or in the cloud |
| Compute/transmit allocation | $f_u(t),p_u(t)$ | continuous, bounded | CPU frequency and communication power at CE-UAV $u$ |
| Energy value signal | $\rho[n]$ | continuous signal | Dispatcher valuation of stored energy |
| Harvesting control | $h_v(t)$ | continuous/discrete | Energy collected by EF-UAV $v$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task is assigned to at most one CE-UAV and each CE-UAV processes at most one task at a time |
| C2 | Local, CE-UAV, and cloud execution choices obey the task-latency limits |
| C3 | CPU and communication allocations remain within UAV capacities |
| C4 | Battery stochastic dynamics stay within nonnegative energy bounds |
| C5 | The Lyapunov energy queue and mean-field population state remain stable |

**Algorithm**: Approximate the large UAV population by a mean-field representative agent → derive the energy valuation with Lyapunov optimization → solve the coupled HJB/ODE coefficients → broadcast $\rho[n]$ and execute local task policies → validate the $\epsilon$-Nash approximation and energy balance on the hardware-in-the-loop testbed.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ma et al. [x] studied energy-efficient task allocation for green aerial edge computing with computing-enhanced and energy-focused UAVs serving metaverse users. They formulated a stochastic long-term task-allocation problem that balances delay, computation/communication energy, and energy harvesting while assigning each task to at most one computing UAV or the cloud. A mean-field game replaces dense UAV interactions with a representative agent against the aggregate energy state, and Lyapunov optimization supplies an energy valuation signal for long-term stability. The resulting policy is analyzed with an epsilon-Nash approximation and implemented with a dispatcher and local UAV decisions. A Raspberry Pi and A100 hardware-in-the-loop testbed reports energy balancing and the predicted decrease of approximation error as the UAV population grows.

## Problem

Metaverse users generate delay-sensitive tasks, but UAV edge nodes have limited and stochastic battery resources. The hard part is not only choosing which tasks to process locally at UAVs, but balancing energy across a large heterogeneous UAV population under stochastic harvesting, task-specific compute/communication costs, and long-term service sustainability.

## System model

- CE-UAVs execute offloaded tasks; EF-UAVs harvest energy and act as energy reservoirs.
- A central dispatcher broadcasts a system-wide energy value signal $\rho[n]$ at the large timescale.
- Each CE-UAV makes local processing and transmission decisions over a smaller continuous timescale using its energy state and the broadcast signal.
- Each task is assigned to at most one CE-UAV, and each CE-UAV processes at most one task at a time.
- Unprocessed tasks are offloaded to a remote cloud server to satisfy latency constraints.
- Battery dynamics are modeled with stochastic differential equations including harvesting inflow, computation/communication consumption, and random energy fluctuations.

## Method

The paper uses an MFG model to replace dense UAV-UAV coupling with a representative-agent problem against the aggregate mean energy state. Lyapunov optimization derives an energy valuation policy that guides the dispatcher and encourages long-term energy stability. The theoretical analysis reports an epsilon-Nash-equilibrium style scalability result with approximation error decreasing as $O(1/\sqrt{U})$ as the number of UAVs grows.

## Key findings

- A Raspberry Pi5/A100 hardware-in-the-loop testbed is used: Raspberry Pi5 devices emulate UAV agents, and an NVIDIA A100 server implements the dispatcher and cloud-server role.
- The closed-form MFG coefficients match numerical ODE solutions in the validation plot.
- The Raspberry Pi testbed follows the predicted $O(1/\sqrt{U})$ approximation-error decay for 50, 100, and 200 UAV-agent configurations.
- The Lyapunov-driven average energy and energy value signal converge over 100 time slots for the linear and logarithmic models tested.
- MFG keeps average UAV energy around 0.75-0.8 and energy variance below 0.05 in steady state, while greedy and no-balancing baselines drop to about 0.3-0.4 average energy with higher variance.
- Utility peaks around energy-balancing weight $\xi=1.0$ in the reported heatmap, and EF-UAV ratio $\gamma=0.4$ gives the best normalized utility among the tested ratios.

## Limitations / future work

The system limits each task to one UAV, so it does not yet support collaborative execution of a single complex task across multiple UAVs. The authors name collaborative task execution through workload decomposition and distribution as future work. The hardware evidence is hardware-in-the-loop emulation rather than real UAV flight.

## Relation to the corpus

This source adds [[mean-field-game]] to the wiki's game-theoretic offloading vocabulary. It complements [[panahi-2026-uav-green-iot-offloading]] by treating green aerial computing as a large-population energy-balancing problem rather than an energy-procurement compensation problem. It is adjacent to [[wang-2026-lifelong-semantic-content-reuse]] because both target metaverse-facing aerial edge services, but Ma et al. focus on task allocation, [[energy-harvesting-mec]], and energy balance rather than semantic caching/reuse.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users A Mean Field Game Approach/Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users A Mean Field Game Approach.md`
- Origin PDF: `raw/sources/Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users A Mean Field Game Approach/Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users A Mean Field Game Approach.pdf`
- Figures: `raw/sources/Energy-Efficient Task Allocation for Green Aerial Edge Computing Based on Metaverse Users A Mean Field Game Approach/images/`
