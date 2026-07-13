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
updated: 2026-07-14
---

# Energy-Constrained Satellite Edge Computing for Satellite-Terrestrial Integrated Networks

## Citation

Cheng, L., Feng, G., Sun, Y., Qin, S., Wang, F., & Quek, T. Q. S. (2025). *Energy-Constrained Satellite Edge Computing for Satellite-Terrestrial Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3483203. (Date of publication 17 Oct 2024; date of current version 14 Feb 2025 → year 2025 per the current-version convention. An earlier version appeared at ICC 2022, DOI 10.1109/ICC45855.2022.9838943.)

## TL;DR
Proposes **DOS** (dynamic offloading strategy), an online [[leo-satellite-edge-computing]] offloading scheme for satellite-terrestrial integrated networks (STINs) that minimizes overall **task completion time** under the LEO satellite's **long-term energy constraint**. The key realism is modeling LEO satellites' **time-varying energy** (solar harvest + eclipse periods) and **stochastic, location-dependent task arrivals**. Using [[lyapunov-optimization]], the long-term stochastic problem is converted into per-slot deterministic problems, each decomposed into convex subproblems for joint task offloading + computing + communication resource allocation. DOS is proven near-optimal and beats four baselines on completion time and task dropping rate.

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
