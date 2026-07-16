---
type: source
modeling_card: required
title: "Energy and Latency Efficient Joint Communication and Computation Optimization in a Multi-UAV-Assisted MEC Network"
authors: ["Farhan Pervez", "Ajmery Sultana", "Cungang Yang", "Lian Zhao"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3291692"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags:
  - source
  - multi-uav-assisted-mec
  - computation-offloading
  - potential-game
  - alternating-optimization-sdr-sca
  - energy-latency-tradeoff
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[energy-latency-tradeoff]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[two-stage-decomposition]]"
  - "[[edge-user-allocation]]"
  - "[[chen-2024-ulse-game]]"
  - "[[guo-2023-mccco-multiuav-5g-offloading]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
  - "[[bai-2024-delay-aware-cooperative-edge-cloud]]"
created: 2026-05-31
updated: 2026-07-16
---

# Energy and Latency Efficient Joint Communication and Computation Optimization in a Multi-UAV-Assisted MEC Network

## Citation

Pervez, F., Sultana, A., Yang, C., & Zhao, L. (2024). *Energy and Latency Efficient Joint Communication and Computation Optimization in a Multi-UAV-Assisted MEC Network*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3291692. (Date of publication 11 Jul 2023; date of current version 12 Mar 2024 → year 2024 per the current-version convention.)

## TL;DR
A multi-UAV + terrestrial-BS MEC network where multiple UAV-MEC servers and one BS-MEC server serve ground users. The objective is to minimize a **weighted energy-and-latency cost** by jointly optimizing **task offloading + MEC server selection**, **offloading/downloading transmit power**, **UAV trajectory**, and **CPU-frequency allocation**. The non-convex MINLP is solved by a **three-layer Alternative Cost Minimization (ACM)** algorithm: a **[[potential-game]]** for offloading/server selection (proven to have a Nash Equilibrium), **geometric water-filling (GWF)** for power + **[[alternating-optimization-sdr-sca|SCA]]** for trajectory, and **gradient descent** for CPU frequency, iterated via alternating optimization. A segment-by-segment trajectory split cuts computation time. ACM beats local/MEC/random baselines and ~10–12% beats two prior joint-optimization methods.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ ground users either compute locally or fully offload to one of $M-1$ rotary-wing UAV-MEC servers or one terrestrial BS-MEC server over time-varying multiple-access links. UAV access links are LoS-dominant, the user-to-BS link includes Rayleigh fading, UAVs move horizontally at fixed altitude, and UAV backhaul uses assumed reliable FSO links.

**Problem & objective**: A non-convex MINLP jointly minimizes weighted energy and execution latency, $\min\sum_k(\sigma_k^E E_k+\sigma_k^{\psi}T_k)$, over offloading/server selection, uplink and downlink power, UAV trajectories, and server CPU allocation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Execution/server choice | $d_{k,m}$ | binary | Local execution or the selected UAV/BS MEC server for user $k$ |
| Uplink/downlink power | $p_{k,m}^{\mathrm{UL}},p_{m,k}^{\mathrm{DL}}$ | continuous, power-bounded | Task-upload and result-download transmit powers |
| UAV trajectory | $\mathbf a_m[t]$ | continuous horizontal position | Location of UAV-MEC server $m$ in slot $t$ |
| CPU allocation | $f_{k,m}$ | continuous, nonnegative | Server computing frequency allocated to user $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task is executed locally or fully offloaded to exactly one MEC server |
| C2 | User and server transmit powers satisfy their respective limits |
| C3 | Per-server CPU allocations do not exceed available computing capacity |
| C4 | UAV positions, speeds, and prescribed trajectory endpoints remain feasible |
| C5 | Upload, execution, and download rates determine feasible latency and energy under co-channel interference |

**Algorithm**: Solve offloading and server selection as a best-response potential game → allocate upload/download power by geometric water filling → update segmented UAV trajectories with SCA → optimize CPU frequencies by gradient descent → alternate the three layers until the weighted cost converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Pervez et al. [x] studied joint communication and computation optimization in a multi-UAV-assisted MEC network with one terrestrial BS-MEC server. They formulated a non-convex mixed-integer problem that minimizes a weighted sum of user energy and latency by jointly selecting local or MEC execution, transmit powers, UAV trajectories, and CPU frequencies. Their Alternative Cost Minimization method solves offloading and server selection as a potential game, applies geometric water filling to power allocation, updates segmented trajectories with successive convex approximation, and allocates CPU frequency by gradient descent. The three layers are alternated until the system cost converges. Simulations report convergence in about nine iterations and cost reductions of approximately 12% and 10% against the two evaluated joint-optimization methods under the stated settings.

## Problem
UAV-assisted MEC adds mobility and LoS-favorable channels over fixed ground servers, but most prior multi-UAV-MEC work optimizes either communication **or** computation parameters, and the joint minimization of a **weighted linear sum of energy + latency** across a multi-UAV multi-user system "has not been sufficiently discussed." The paper formulates task computation in a multi-access environment (one BS-MEC server + multiple UAV-MEC servers, total `M` servers = `M−1` UAVs + 1 BS, serving `K` ground users over time-varying channels) as a constrained optimization minimizing each user's weighted energy + time-latency cost; users can compute locally or **fully offload** to one MEC server.

## System model
- **Actors:** `K` single-antenna ground users; `M−1` rotary-wing UAV-MEC servers (constant altitude, free to move horizontally over horizon `Γ`, divided into `T` slots) + 1 BS-MEC server; UAVs connected to the network via FSO links (no backhaul failures).
- **Comms:** wireless interference model; free-space-path-loss channel gain (high LoS probability for UAV links); small-scale Rayleigh fading for the user-BS link; Doppler assumed perfectly compensated.
- **Compute:** each task = (CPU cycles/bit, data size `u_k`); local CPU cycles/bit `ν_k`, server `ω_m`; offloaded tasks computed at the server and results returned downlink.
- **Decision variables:** offloading + server-selection `d` (`K×(M+1)`), offloading/downloading power, UAV trajectory `a_m[t]`, CPU-frequency allocation — formulated as a **[[mixed-integer-nonlinear-programming]]** problem minimizing weighted energy (`σ_k^E`) + latency (`σ_k^ψ`) cost.

## Method
- **Three-layer ACM (alternating optimization):**
  1. **Offloading + MEC server selection** via a **game-theoretic** approach: the user game `Ω` is shown to be a (best-response) **[[potential-game]]** with potential function `Υ`, guaranteeing existence of a **[[nash-equilibrium]]**; the best-response `Ξ_k(α_{−k})` gives the offloading/server-selection profile.
  2. **Power allocation** (offloading at user + downloading computed bits) via **geometric water-filling (GWF)**, avoiding nonlinear KKT resolution; **UAV trajectory** via **[[alternating-optimization-sdr-sca|SCA]]** with a **segment-by-segment** split (divide the flight into shorter timeframe segments) to reduce computation time.
  3. **CPU-frequency allocation** via **gradient descent**.
- The three layers are iterated (alternating optimization) until the weighted cost converges; **ACM-s** is a single-iteration variant.

## Key findings
- ACM and ACM-s achieve **lower total cost** (energy + latency) than baselines **LC** (all-local), **MC** (all-offload-to-nearest-server), and **RC** (random) across user counts (parse, Figs. 3–4); delay reduction is more pronounced than energy reduction (the energy cost matrix also includes UAV hovering power).
- The algorithm **converges in ~9 iterations** (10/50/100-user scenarios) to a stable average system cost (parse, Fig. 4b).
- System cost **rises with more Gbits to compute** and **falls as more UAV-MEC servers** are added (faster, lower-energy execution) — but redundant idle UAVs only add hovering-energy cost; 3-D altitude optimization is flagged as further leverage (parse, Fig. 5).
- Versus two prior joint-optimization methods (a Lagrange-duality + SCA method and an alternating two-subproblem SCA method), ACM achieves **~12%** and **~10%** cost reduction respectively, under identical parameters (parse, Fig. 6), attributed to the layered GTD + GWF + gradient-descent decomposition.

## Limitations / future work
Simulation-only (numerical results). 2-D horizontal trajectory at fixed altitude — full **3-D** (altitude + horizontal) optimization noted as future leverage. Binary **full** offloading only (no partial offloading). FSO UAV backhaul assumed failure-free; Doppler assumed perfectly compensated. Communication resources can become scarce and raise cost when the user count/load is very high.

## Relation to the corpus
A **classical/convex multi-UAV-MEC** source whose offloading/server-selection layer is a **[[potential-game]]** — the same equilibrium tool used by [[chen-2024-ulse-game]] (UAV-LEO offloading) and [[he-2019-euagame-user-allocation]] ([[edge-user-allocation]]), here embedded inside an alternating-optimization solver rather than standing alone. Its GWF + SCA + gradient-descent **[[alternating-optimization-sdr-sca]]** pipeline and weighted [[energy-latency-tradeoff]] objective align it with [[liu-2022-miso-uav-mec-trajectory]] and [[bai-2024-delay-aware-cooperative-edge-cloud]]; the multi-UAV cooperative-offloading framing parallels [[guo-2023-mccco-multiuav-5g-offloading]]. Sits in the broader [[multi-uav-assisted-mec]] / [[task-offloading]] landscape.

## Raw artifacts
- `raw/sources/Energy_and_Latency_Efficient_Joint_Communication_and_Computation_Optimization_in_a_Multi-UAV-Assisted_MEC_Network/full.md`
- Original PDF and extracted figures in the same folder.
