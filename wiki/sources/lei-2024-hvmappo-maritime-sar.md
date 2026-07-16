---
type: source
title: "Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning"
authors: ["Chengjia Lei", "Shaohua Wu", "Yi Yang", "Jiayin Xue", "Qinyu Zhang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3388499"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
modeling_card: required
tags: [source, maritime-mec, multi-agent-reinforcement-learning, uav-trajectory-control, task-offloading, fault-tolerant-relay-network, search-and-rescue]
related:
  - "[[maritime-mec]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[pomdp]]"
  - "[[gae]]"
  - "[[fault-tolerant-relay-network]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[qi-2024-msar-minmax-latency]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[shaohua-wu]]"
  - "[[qinyu-zhang]]"
created: 2026-06-01
updated: 2026-07-16
---

# Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning

## Citation

Lei, C., Wu, S., Yang, Y., Xue, J., & Zhang, Q. (2024). *Joint Trajectory and Communication Optimization for Heterogeneous Vehicles in Maritime SAR: Multi-Agent Reinforcement Learning*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3388499. (Manuscript received 18 September 2023; date of publication 15 April 2024; date of current version 19 September 2024 → year 2024.)

## TL;DR

A **maritime search-and-rescue (SAR)** system of heterogeneous vehicles — observation UAVs, relay/routing UAVs, and autonomous surface vehicles (ASVs) carrying MEC servers — operating far from shore with no base stations. It **jointly optimizes vehicle trajectories, offloading scheduling, and routing topology** to minimize time + energy consumption while **increasing the fault tolerance of the relay network** (redundant multi-hop paths). The multi-objective problem is recast as a **Dec-POMDP** and solved by multi-agent RL; the proposed **HVMAPPO** (heterogeneous-vehicles multi-agent PPO) uses CTDE plus three stabilizing techniques.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A maritime search-and-rescue team contains observation UAVs, routing UAVs, and autonomous surface vehicles carrying MEC servers. Observation UAVs track drifting targets and may offload image recognition, routing UAVs maintain multi-hop connectivity, and surface vehicles approach and rescue targets under ocean-current disturbance.

**Problem & objective**: The joint policy minimizes $\sum_{t=1}^{T}\left(1+\mu_1E_{\mathrm{tot}}^t-\mu_2\mathcal F_{\mathrm{tot}}^t\right)$, combining mission duration, heterogeneous-vehicle energy, and the negative of relay-network fault tolerance.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Observation-UAV motion | $(v_x,v_y)$ | continuous | Horizontal velocity command for each observation UAV |
| Offloading ratio | $R_{\mathrm{off}}^j$ | continuous, $[0,1]$ | Fraction of observation task offloaded to the ASV MEC server |
| Routing-UAV motion | $(v_x,v_y)$ | continuous | Velocity command shaping the relay topology |
| ASV motion | $(v_x,v_y)$ | continuous | Surface-vehicle rescue trajectory command |
| Joint policy | $\Pi$ | decentralized policy set | Cooperative policies for all heterogeneous vehicles |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every vehicle obeys its type-specific maximum speed and acceleration |
| C2 | Mission completion time satisfies $0\le T\le T_{\max}$ |
| C3 | Routing links remain within the routing-UAV communication range |
| C4 | Aggregate MEC use remains within the available edge-server capacity |
| C5 | Offloading ratios and continuous actions remain in their feasible ranges |

**Algorithm**: HVMAPPO casts the coupled control as a Dec-POMDP and uses centralized training with decentralized execution. Mixed heterogeneous rewards combine observation, rescue, relay fault tolerance, and energy terms; parameter sharing, normalized generalized advantage estimation, Pop-Art value scaling, and PPO clipping stabilize the heterogeneous multi-agent updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lei et al. [x] jointly controlled observation UAVs, relay UAVs, and MEC-equipped surface vehicles for maritime search and rescue without coastal base-station coverage. They minimized mission time and energy while rewarding relay-network fault tolerance over vehicle motion and observation-task offloading under speed, acceleration, horizon, routing-range, and MEC-capacity constraints. HVMAPPO uses a Dec-POMDP, mixed heterogeneous rewards, centralized critics, parameter sharing, normalized advantage estimates, and Pop-Art scaling. Relative to HVIPPO, it improved observation rate by 4% and rescue count by 12%, and relative to centralized PPO it improved those metrics by 9% and 58% while also increasing fault tolerance by 8%.

## Problem framing

Maritime SAR has two defining traits: a harsh ocean environment with scarce/unstable communication (no BS far from coast; GEO satellites high-latency, LEO complex to switch), and targets drifting with currents/wind. Observation UAVs must spread out to cover a large search area, but spreading too far breaks the relay network — a direct tension between **mission immediacy (efficiency)** and **communication reliability (fault tolerance)**. The joint trajectory+communication optimization is NP-hard with hard real-time demands, motivating a learned cooperative policy.

## System model

- **Heterogeneous vehicles.** Observation UAVs (vision/ResNet target detection, offload part to ASV edge servers), routing UAVs (multi-hop relay within range $r_{\text{router}}$), and ASVs (MEC servers + rescue).
- **Ocean environment.** A time-varying stream function models ocean currents that move rescue targets (parameters fixed per the cited model, randomized per episode with Gaussian noise).
- **Observation model.** Camera field-of-view → swept observation area proportional to UAV altitude and flight speed.
- **MEC offloading.** UAV picks an offloading ratio to the ASV edge server; limited MEC load capacity (offloading halted if total requests exceed capacity).
- **Fault tolerance.** Per-observation-UAV redundancy = existing relay paths / possible paths; averaged over UAVs.
- **Energy.** Rotary-wing flight power + computation energy + multi-hop transmission energy.

## Method

The multi-objective problem (minimize time + energy, maximize relay fault tolerance, weighted) is transformed into a **Dec-POMDP** and solved with MARL:

- **HVMAPPO** — multi-agent PPO under **centralized training with decentralized execution (CTDE)**, compared against IPPO (independent learning).
- Three performance/stability techniques: **parameter sharing**, **normalized generalized advantage estimation (GAE)**, and **Pop-Art** (preserving outputs precisely while adaptively rescaling targets).
- A custom **mixed-heterogeneous-reward (MHR)** shaping mixes per-task rewards (observation, relay fault tolerance, rescue, energy) with joint rewards to encourage cooperation among the heterogeneous vehicles.

## Key findings

- HVMAPPO **outperforms the baselines in overall team performance**, achieving a balanced trade-off between efficiency (time + energy) and communication fault tolerance (abstract / contributions; specific curves are in the figures and not asserted here as exact magnitudes).
- The CTDE framing keeps computational complexity from growing with the number of vehicles, which the paper highlights as well-suited to compute-limited UAVs.

## Limitations / future work

MHR reward coefficients are tuned by experimental experience. The captured parse does not enumerate explicit future-work targets in detail → `not in parse`.

## Relation to the corpus

A **maritime MEC** entry joining the corpus's maritime track, but distinctive for combining **offloading with a fault-tolerant multi-hop relay topology** as a co-equal objective. It contrasts with the other maritime search-and-rescue sources — [[qi-2024-msar-minmax-latency]] (min-max latency via linearization + SCA + branch-and-bound) and [[wang-2026-aerial-marine-msar]] (UAV+HAPS+MASS three-tier JCORA via matching + convex + PGD) — by being a **MARL (HVMAPPO/CTDE)** solution that explicitly optimizes relay-network redundancy. It introduces the [[fault-tolerant-relay-network]] concept and reinforces [[mappo]], [[centralized-training-decentralized-execution]], and [[gae]].

## Raw artifacts

- `raw/sources/Joint_Trajectory_and_Communication_Optimization_for_Heterogeneous_Vehicles_in_Maritime_SAR_Multi-Agent_Reinforcement_Learning/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
