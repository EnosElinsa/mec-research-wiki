---
type: source
title: "Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC"
authors: ["You Shi", "Changyan Yi", "Ran Wang", "Qiang Wu", "Bing Chen", "Jun Cai"]
year: 2023
url: "https://doi.org/10.1109/TWC.2023.3290005"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, mobile-edge-computing, service-migration, task-migration, two-timescale-optimization, lyapunov-optimization, mixed-integer-nonlinear-programming, seamless-handover]
related:
  - "[[mobile-edge-computing]]"
  - "[[service-migration]]"
  - "[[task-migration]]"
  - "[[two-timescale-optimization]]"
  - "[[lyapunov-optimization]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[seamless-handover]]"
  - "[[lyapunov-guided-drl]]"
  - "[[sun-2025-tjcct-twotimescale-uav-mec]]"
  - "[[ye-2021-ran-slicing-offloading]]"
  - "[[yang-2024-taco-human-digital-twin-edge]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-06-02
updated: 2026-06-02
---

# Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC

## Citation

Shi, Y., Yi, C., Wang, R., Wu, Q., Chen, B., & Cai, J. (2023). *Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3290005. (Manuscript received 23 December 2022; revised 11 April 2023 and 4 June 2023; accepted 22 June 2023; date of publication 5 July 2023; date of current version 13 February 2024 → year 2023.)

## TL;DR

Builds a **two-timescale online resource-management framework for MEC** that, whenever a mobile device (MD) hands over from one edge server (ES) to another, **strikes the balance between service migration and task rerouting**. **Large-timescale** decisions choose the ES to access and whether to migrate the service application or reroute tasks back to the previously hosted ES; **small-timescale** decisions allocate computing and communication resources among MDs with offloading requests each slot. The objective is to **minimize long-term average service delay** under system stability, energy, and caching-capacity constraints. The solution is an **improved Lyapunov-optimization** online algorithm (OASTR) plus an iterative inner algorithm combining **randomized rounding** (large-timescale integer subproblem, JASTO) and **Lagrange-dual** methods (small-timescale resource allocation), proven to reach the **asymptotic optimum**.

## Problem framing

MEC offloading must stay **seamless and cost-efficient** as MDs roam and trigger access handovers. Two remedies exist, each imperfect: **service migration** (move the application to the new ES) can interrupt service and is infeasible when ESs are capacity-limited (migrating an XR application takes 2–10 s versus a 40 ms delay budget); **task rerouting** (send tasks back to the previously hosted ES) avoids migration overhead but adds per-task rerouting delay and energy. The paper argues the two must be **jointly balanced**, which is hard because (i) the joint access/migration/rerouting + resource problem is a **mixed-integer nonlinear program (MINLP)** coupled to each ES's nonlinear caching state; (ii) network dynamics (channel variation, mobility, random task arrivals) force **online** decisions without future statistics; and (iii) handover-triggered decisions change slowly while task-triggered resource allocations must adapt fast — i.e. **asynchronous, different-timescale** decisions, which single-timescale studies cannot capture.

## System model

- **Two-timescale structure.** `T` coarse time frames, each split into `K` fine slots of length `γ`. Large-timescale per-frame decisions: access selection `x^m_i(t)`, service-migration `ϖ_i(t)`, task-rerouting `ϑ_i(t)`. Small-timescale per-slot decisions: offloading `z_i(τ)`, CPU-allocation `ρ_i(τ)`, bandwidth-allocation `α_i(τ)`.
- **Communication.** Rayleigh flat-fading SNR with path-loss exponent `θ ≥ 2`; transmission rate via Shannon; at most one ES per MD and total bandwidth ratio ≤ 1 per ES.
- **Computation/caching.** Local vs edge computing delay/energy; each ES has a caching capacity `C^t_m` for service applications, so it can serve an MD only if it has the matching application, can install it via **migration**, or can **reroute** the task to an ES that has it.
- **Objective (P1).** Minimize long-term **device-wide average execution delay** subject to system (queue) stability, a long-term energy constraint (energy-deficit virtual queues `Q_i`), and caching-capacity constraints — distinguished in the paper's Table I as the only scheme jointly supporting **both** service migration **and** task rerouting with system-wide cost minimization.

## Method

- **Improved Lyapunov.** A modified Lyapunov drift-plus-penalty structure handles the **two-timescale** variables by evenly distributing per-frame migration cost (delay + energy) across the frame's slots, decomposing the long-term problem into per-frame deterministic subproblems.
- **Large timescale — JASTO.** The integer access/migration/rerouting subproblem (P4) is solved by **randomized rounding** (linear relaxation + LP solver), proven asymptotically optimal (Lemma 1); future-frame status is approximated by the previous frame's status.
- **Small timescale — Lagrange dual.** Bandwidth (P6) and CPU (P7) allocations are solved by **Lagrange-dual + KKT**, and the offloading decision updated, iterated to a stationary point (OASTR, Algorithm 2).
- **Guarantees.** Theorem 3 gives an optimality gap `≤ ε + B/V + Λ/VT` (so larger Lyapunov parameter `V` → closer to optimum); Theorem 2 gives complexity `O[T·ν((2M)^{2.055} + 2K)]`; Theorem 4 bounds the energy-deficit-queue backlog (stability).

## Key findings

- The Lyapunov parameter `V` tunes a **delay-vs-energy-stability tradeoff**: increasing `V` drives the achieved delay toward the theoretical optimum `ε` while the energy-deficit queue backlog grows with a `V`-dependent bound (Theorems 3–4).
- OASTR is reported **superior to two benchmarks**: **JMH** (joint migration + resource allocation, single-timescale, no task rerouting) and **O2TL** (two-timescale migration + offloading but equal bandwidth split, no task rerouting). Specific margins are figure-derived; treat exact values as indicative.
- Simulation setup (parse, Table III): `M = 10` ESs, `I = 40` MDs, `K = 10` slots/frame, `W_m = 5` MHz, ES caching `C^max_m = 100` Gb, MD/ES CPU 1/20 GHz, task arrivals `[10,20]` per slot.

## Limitations / future work

Evaluation is **simulation-only**. Migration cost is distributed evenly across a frame's slots to enable the single-timescale Lyapunov decoupling; the authors note (Remark 1) that adding an explicit **MD-side service-interruption / resumption-delay constraint** couples the two timescales tightly and breaks this trick, requiring more advanced tools (e.g. scale-space theory) — left to **future work**. Future-frame dynamics are approximated by the previous frame's observation.

## Relation to the corpus

The corpus's anchor for **service migration vs task rerouting**, grounding both [[service-migration]] and the broader [[two-timescale-optimization]] pattern. Unlike the price-incentive + matching two-timescale UAV-MEC scheme [[sun-2025-tjcct-twotimescale-uav-mec]] or the RAN-slicing + offloading two-timescale loop [[ye-2021-ran-slicing-offloading]] and the accuracy-aware human-digital-twin TACO [[yang-2024-taco-human-digital-twin-edge]], it puts **handover-triggered application migration / task rerouting** on the slow timescale and resource allocation on the fast one, solved via [[lyapunov-optimization|improved Lyapunov]] + randomized rounding + Lagrange dual (a classical online optimizer, contrast the [[lyapunov-guided-drl]] hybrids). Its MINLP framing uses [[mixed-integer-nonlinear-programming]]; its rerouting/migration mechanics complement the in-flight [[task-migration]] of [[zhang-2025-mcma-task-migration]] and the compute-state [[seamless-handover]] notion from LEO settings.

## Raw artifacts

- `raw/sources/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
