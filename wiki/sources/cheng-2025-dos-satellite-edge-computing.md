---
type: source
title: "Energy-Constrained Satellite Edge Computing for Satellite-Terrestrial Integrated Networks"
authors: ["Lei Cheng", "Gang Feng", "Yao Sun", "Shuang Qin", "Feng Wang", "Tony Q. S. Quek"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3483203"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags:
  - source
  - leo-satellite-edge-computing
  - space-air-ground-integrated-network
  - lyapunov-optimization
  - computation-offloading
  - energy-efficiency
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[non-terrestrial-network]]"
  - "[[lyapunov-optimization]]"
  - "[[task-offloading]]"
  - "[[mobile-edge-computing]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[energy-latency-tradeoff]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[chen-2024-ulse-game]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[zhang-2025-three-tier-maritime-offloading]]"
  - "[[gang-feng]]"
  - "[[shuang-qin]]"
  - "[[wei-2026-runs-uav-network-slicing]]"
created: 2026-05-31
updated: 2026-07-16
modeling_card: required
---

# Energy-Constrained Satellite Edge Computing for Satellite-Terrestrial Integrated Networks

## Citation

Cheng, L., Feng, G., Sun, Y., Qin, S., Wang, F., & Quek, T. Q. S. (2025). *Energy-Constrained Satellite Edge Computing for Satellite-Terrestrial Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3483203. (Date of publication 17 Oct 2024; date of current version 14 Feb 2025 → year 2025 per the current-version convention. An earlier version appeared at ICC 2022, DOI 10.1109/ICC45855.2022.9838943.)

## TL;DR
Proposes **DOS** (dynamic offloading strategy), an online [[leo-satellite-edge-computing]] offloading scheme for satellite-terrestrial integrated networks (STINs) that minimizes overall **task completion time** under the LEO satellite's **long-term energy constraint**. The key realism is modeling LEO satellites' **time-varying energy** (solar harvest + eclipse periods) and **stochastic, location-dependent task arrivals**. Using [[lyapunov-optimization]], the long-term stochastic problem is converted into per-slot deterministic problems, each decomposed into convex subproblems for joint task offloading + computing + communication resource allocation. DOS is proven near-optimal and beats four baselines on completion time and task dropping rate.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A satellite-terrestrial integrated network serves remote user devices through a LEO satellite equipped with an edge server and connected to a terrestrial cloud through a gateway. Divisible tasks may be processed locally, at the satellite edge, or in the cloud, while the satellite battery evolves with computation and transmission consumption, solar harvesting, and eclipse periods.

**Problem & objective**: Problem P0 is a long-term stochastic mixed-integer optimization, $\min\frac{1}{T}\sum_{t=0}^{T-1}\mathbb E[\sum_{n=1}^{N(t)}\gamma_n(t)]$, where $\gamma_n(t)=d_n(t)+\beta x_n^d(t)$ includes parallel task-completion time and the re-execution delay for a dropped task.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task portions | $x_n^l(t),x_n^e(t),x_n^c(t)$ | Continuous, $[0,1]$ | Fractions processed locally, at the LEO edge, and in the cloud |
| Drop decision | $x_n^d(t)$ | Binary, $\{0,1\}$ | Indicates that task $n$ is blocked and dropped |
| UD and satellite compute | $z_n^D(t),z_n^S(t)$ | Continuous bounded rates | Allocates local and satellite CPU resources |
| UD and satellite transmit power | $p_n^D(t),p_n^S(t)$ | Continuous bounded power | Allocates ground-satellite and feeder-link power |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Partition or drop: $x_n^l(t)+x_n^e(t)+x_n^c(t)+x_n^d(t)=1$ |
| C2 | Deadline: $d_n(t)\leq\tau_a^{\max}$ |
| C3 | Satellite energy evolution: $E^S(t+1)=E^S(t)-e^S(t)+e^{S,h}(t)$ with $e^S(t)\leq E^{S,\max}(t)$ |
| C4 | UD energy: $e_n^D(x_n(t),z_n(t),p_n(t))\leq E^{D,\max}(t)$ |
| C5 | Compute and power are zero when their route is unused and otherwise satisfy (25e)-(25h) |

**Algorithm**: Form the virtual satellite-energy queue $\widehat E^S(t)=E^S(t)-\phi$, minimize the per-slot drift-plus-penalty upper bound $V\gamma(t)-\widehat E^S(t)e^S(t)$, decompose each one-slot problem into task-offloading, local resource-allocation, and edge resource-allocation convex subproblems, iterate them to convergence, and then update the physical energy queue.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cheng et al. [x] studied dynamic computation offloading in a satellite edge computing assisted satellite-terrestrial integrated network with solar harvesting, eclipse periods, and stochastic task arrivals. They minimized long-term average task completion time by jointly selecting local, LEO-edge, cloud, or drop portions and allocating computation and transmission resources under task-delay, user-energy, and satellite-energy constraints. Their DOS method used a perturbed energy queue and Lyapunov drift-plus-penalty transformation, followed by iterative convex task-offloading and resource-allocation subproblems in every slot. The analysis reported an $O(1/V)$ optimality gap, and simulations showed the lowest completion time across all tested environmental settings and the lowest dropping rate among the compared strategies.

## Problem
Satellite edge computing (SEC) sinks edge servers into LEO satellites to extend computation services where terrestrial networks are absent or compromised (disaster recovery, remote IoT, IoV monitoring). But LEO mobility creates two challenges absent in terrestrial MEC: (1) onboard compute/transmission capability is limited by a **dynamic energy supply** — solar panels + battery cells, with prolonged eclipse (darkness) periods of no energy input; and (2) **stochastic task arrivals within coverage** and time-varying channel conditions that change as the satellite moves. Prior SEC work mostly assumes sufficient/constant energy, allocates only one resource type, or ignores location-dependent task arrivals. The paper formulates a joint task-offloading + computation + communication resource allocation problem to minimize **overall task completion time** subject to the satellite's long-term energy evolution; the problem is NP-hard and future-dependent.

## System model
- **Tiers:** terrestrial user devices (UDs) → **LEO satellite edge server** → cloud computing center. A task can be processed locally, at the LEO edge server, or at the cloud.
- **Energy:** LEO satellite harvested energy from a power-supply model (absorption power `p_H`, sun-incidence angle `α_s`), with explicit **eclipse** periods of zero harvest; a perturbation index `φ` (perturbed energy level) governs the Lyapunov energy queue. Effective switched capacitance `κ = 10⁻²⁴`.
- **Comms:** UDs transmit uplink via **C band (6 GHz, 20 MHz)**; satellite backhauls via **Ku band (12 GHz, 200 MHz)**; max transmit power 24 dBm (UD) / 46 dBm (satellite); noise PSD `σ₀ = −174 dBm/Hz`.
- **Compute:** UD `0.1 Gcycles/s` (battery 5 mJ), LEO edge `4 Gcycles/s`, cloud `10 Gcycles/s`.
- **Orbit (sim):** polar-orbiting LEO at **1700 km**, orbital period **120 min** divided into **200 slots**; task arrival ~10 tasks/slot; problems solved with Gurobi 9 in Python 3.7.6.

## Method
- **Formulation:** long-term task-completion-time minimization under a long-term energy constraint (problem `P₁`), NP-hard and future-dependent.
- **DOS via hierarchical decomposition:** [[lyapunov-optimization]] transforms the long-term stochastic problem into multiple **one-slot** real-time problems parameterized by current state (minimizing a drift-plus-penalty upper bound with tuning factor `V`); each one-slot problem is further decomposed and transformed into multiple **convex** optimization problems for joint offloading + compute + communication resource allocation.
- **Theory:** DOS proven to converge to **near-optimality within polynomial time**; the `[V, E^{S,max}]` pair trades performance against energy discharge depth (a classic Lyapunov `[O(1/V), O(V)]`-style tradeoff).

## Key findings
- DOS achieves the **lowest** average task completion time and task **dropping rate** under all swept values, versus four baselines: **GE** (greedy on edge), **OPT** (random power/compute + optimal offloading), **GS** (greedy on satellite), and **DFO** (dynamic full offloading).
- Completion time **decreases with `V`** and converges to the `P₁` optimum, confirming the asymptotic optimality; energy discharge depth **increases ~linearly with `V`** — e.g. only **5.72% performance improvement needs >1.88× more energy** for `V = 0.05` vs `V = 0.2` (parse, Fig. 4).
- The satellite leans on local + cloud computing during eclipse (low energy) and shifts a larger task fraction to LEO edge computing under sunlight (parse, Fig. 3c offloading-selection).
- With additional terrestrial-UD assistance, DOS's task completion time is **reduced by 37.4% on average vs GE**; OPT and DFO fail to exploit harvested energy (their completion time can even rise as more energy is offered).

## Limitations / future work
Simulation-only (single polar-orbiting LEO satellite; values from numerical experiments). The model omits fixed nominal-operation energy for clarity (stated as easily generalizable). A single satellite is modeled — inter-satellite cooperation/handover across a constellation is outside this formulation. The `V`/`E^{S,max}` trade-off must be tuned per satellite configuration.

## Relation to the corpus
Strengthens the **SAGIN / satellite-offloading** track ([[space-air-ground-integrated-network]]) alongside [[chen-2024-ulse-game]] (UAV-LEO potential game), [[qin-2025-matd3-noma-queue-sagin]] (NOMA queue-aware SAGIN), [[zhai-2023-fedleo-decentralized-fl]] (decentralized FL over LEO), and [[wang-2025-double-edge-samin]] (double-edge UAV+LEO). Methodologically it is a **Lyapunov + convex decomposition** online scheme — the same `[O(1/V), O(V)]` machinery used in [[qin-2025-matd3-noma-queue-sagin]] and [[zhu-2025-lycnn-drl-wpt-mec]], here driven by the distinctive **satellite energy-harvesting / eclipse** dynamic rather than UAV battery limits. Its LEO energy-and-coverage realism complements [[leo-satellite-coverage-time]]. [[tony-q-s-quek]] also co-authors it.

## Raw artifacts
- `raw/sources/Energy-Constrained_Satellite_Edge_Computing_for_Satellite-Terrestrial_Integrated_Networks/full.md`
- Original PDF and extracted figures in the same folder.
