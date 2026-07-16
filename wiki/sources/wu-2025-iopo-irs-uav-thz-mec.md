---
type: source
modeling_card: required
title: "Two-Stage Deep Energy Optimization in IRS-Assisted UAV-Based Edge Computing Systems"
tags:
  - source
  - mobile-edge-computing
  - uav
  - intelligent-reflecting-surface
  - terahertz-communication
  - task-offloading
  - deep-learning
  - energy-optimization
  - two-stage-decomposition
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[terahertz-communication]]"
  - "[[order-preserving-quantization]]"
  - "[[whale-optimization-algorithm]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[two-stage-decomposition]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[ddpg]]"
  - "[[mobile-edge-computing]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
created: 2026-05-29
updated: 2026-07-16
authors:
  - Jianqiu Wu
  - Zhongyi Yu
  - Jianxiong Guo
  - Zhiqing Tang
  - Tian Wang
  - Weijia Jia
year: 2025
url: "https://doi.org/10.1109/TMC.2024.3461719"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 24, no. 1, Jan. 2025"
---

# Two-Stage Deep Energy Optimization in IRS-Assisted UAV-Based Edge Computing Systems

## Citation

Wu, J., Yu, Z., Guo, J., Tang, Z., Wang, T., & Jia, W. (2025). *Two-Stage Deep Energy Optimization in IRS-Assisted UAV-Based Edge Computing Systems*. **IEEE Transactions on Mobile Computing, 24**(1). DOI: 10.1109/TMC.2024.3461719.

## TL;DR
A multi-UAV, multi-user [[mobile-edge-computing]] system running over a [[terahertz-communication]] network is augmented with an [[intelligent-reflecting-surface]] to fight THz blockage and propagation loss. The authors jointly optimize binary task-offloading decisions and IRS phase shifts to minimize the total energy of UAVs and user devices, an NP-hard [[mixed-integer-nonlinear-programming]] problem, and solve it with a two-stage deep-learning framework called **IOPO**. Stage 1 generates an offloading decision via [[order-preserving-quantization]]; stage 2 tunes IRS phases with the [[whale-optimization-algorithm]]. Reported energy drops up to 32.8% versus a [[ddpg]] baseline (3 UAVs, 15 users) while almost always meeting task deadlines.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple users either compute locally or offload to one of several fixed-position UAV MEC servers over a blockage-sensitive THz network aided by one IRS. Per-user deadlines couple binary execution choice, shared uplink rate, UAV workload, computation energy, and RIS phases.

**Problem & objective**: P1 is an NP-hard MINLP that minimizes total device and UAV energy, $\min_{\boldsymbol\beta,\boldsymbol\phi}E_{\mathrm{total}}$, over binary offloading and IRS phase shifts.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading assignment | $\beta_{u,m}$ | binary | User $u$ computes locally or at UAV $m$ |
| IRS phase | $\phi_k$ | continuous, $[0,2\pi]$ | Phase shift of IRS element $k$ |
| Candidate probability | $P_{u,m}$ | continuous, $[0,1]$ | Neural score quantized into offloading candidates |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user selects exactly one mode, $\sum_{m=0}^{M}\beta_{u,m}=1$ |
| C2 | Offloading assignments are binary |
| C3 | Every IRS phase satisfies $0\le\phi_k\le2\pi$ |
| C4 | Local or offloaded execution meets each task deadline $T_u$ |
| C5 | UAV workload determines feasible compute sharing among its assigned users |

**Algorithm**: Predict an offloading-probability matrix with the MLP → apply order-preserving quantization to generate diverse binary candidates → for each candidate solve IRS phases with the whale optimization algorithm → score energy plus overdue penalties → retain the best assignment and update the supervised replay reference.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied energy optimization in an IRS-assisted multi-UAV edge computing system over terahertz links. They formulated an NP-hard mixed-integer nonlinear problem that minimizes user and UAV computation and transmission energy over binary offloading assignments and IRS phase shifts under one-mode, phase-range, and task-deadline constraints. IOPO first predicts assignment probabilities and applies order-preserving quantization to generate feasible binary candidates. For each candidate, a whale optimization algorithm updates the IRS phases, and the lowest-energy deadline-aware pair becomes the training reference. Simulations report lower energy and fewer overdue tasks than the evaluated DDPG, greedy, local-computing, random, and IRS-ablation baselines.

## Problem
UAV-mounted MEC servers provide flexible, well-positioned offloading for mobile devices, and THz bands supply the bandwidth needed for fast-growing data. But THz waves attenuate severely (path loss + molecular absorption) and diffract poorly, so links are blockage-vulnerable. An IRS can reconfigure the propagation channel through per-element phase shifts, restoring coverage and spectral efficiency. Task offloading in an IRS-assisted *multi-UAV* MEC system over THz has been largely unexplored. The paper jointly chooses binary offloading allocations (each user uses one of M UAVs or local compute) and IRS reflector phases to minimize total system energy under per-task latency deadlines, a problem that is NP-hard MINLP. Prior single-stage RL methods that emit decisions and phases at once tend to be suboptimal, motivating a [[two-stage-decomposition]].

## System model
- **Actors:** one IRS, U users each with a User Electronic Device (UED) for local compute, and M UAVs each acting as an MEC server. A base-station central server gathers locations/compute info and runs the decision model.
- **Offloading:** binary, via a U×(M+1) matrix β(n); each user computes locally or offloads to exactly one UAV (Σ_m β_{u,m}=1). Downlink result size is treated as negligible. See [[binary-vs-partial-offloading]].
- **Channel:** THz Shannon rate R_{u,m}=B·log2(1+p|h+ĝ|²/σ²). Direct gain h follows a THz path-loss/molecular-absorption model; IRS cascaded gain ĝ=g·ēᵀΦê with Φ=diag(exp(jφ_k)) the phase-shift matrix. Per-element phase terms derive from reflector geometry on an X-Z plane (K=K_x·K_z elements, first reflector as reference). Base station supplies transmission power p; bandwidth shared among concurrent uploaders; quasi-static flat fading.
- **Energy:** task Ψ_u={D_u, T_u, C_u}. Local: E=t_local·p_u, t_local=C_u/Z_u. Offload: upload E_tran=t_tran·p_u^tran (t_tran=D_u/shared-rate) plus UAV compute E_comp=Σ t_comp·p_m, t_comp=C_u/(Z_m/w_m), workload w_m=max(1,Σ_u β_{u,m}). System energy = Σ_u E_u^total.
- **Assumptions:** UAVs at fixed random positions, 20 m altitude (no trajectory control, no propulsion energy modeled); single base station and single IRS; deadline constraint T_u per user (violations = "overdue").

## Method
The joint problem **P1** = min_{β,φ} E_total subject to binary/one-UAV constraints, phase range 0≤φ_k≤2π, and per-user deadlines is NP-hard MINLP. IOPO applies a [[two-stage-decomposition]]:

- **Stage 1 — offloading decision.** An MLP f_θ (6 hidden layers, Tanh, softmax output, dropout) maps the system feature [f_e(n); f_w(n)] (per-user offloading energy costs + UAV CPU speeds) to a probability matrix P(n). The **OPPO** unit applies [[order-preserving-quantization]] (adapted from DROO's order-preserving method for the multi-UAV/multi-user case) to turn P(n) into H diverse binary candidates, then selects β*(n)=argmin E_total over them (each scored after phase optimization). An overdue penalty (+100 per late user) biases selection toward deadline-feasible decisions, avoiding enumeration of (M+1)^U options.
- **Stage 2 — IRS phases.** Given β*, the non-convex problem **P2** = min_φ E_total is solved with the [[whale-optimization-algorithm]] (W whales, E rounds; spiral / shrink-wrap exploration-vs-exploitation updates), returning φ*(n)=f_WOA(β*).
- **Training.** Supervised; a GREEDY-OC initial reference β̂(n) bootstraps early learning and is upgraded to β* whenever cheaper. Samples ([f_e;f_w], β̂) go into a finite memory buffer; the DNN trains every λ steps with Adam. Overall complexity is polynomial, dominated by network size and iteration count.
- **Simulation setup:** 800 m × 600 m area; UAV CPU 0.08–0.4 GHz, UED CPU 0.04–0.08 GHz; THz 200–400 GHz; IRS = 25 elements (K_x=K_z=5), first element at (4,0,4); tasks 32 B–100 KB; N=200,000 frames, H=20, W=3, E=5, batch 256, dropout 0.1, lr 0.001, λ=10.

## Key findings
- **Energy:** up to **32.8% lower** than [[ddpg]] at 3 UAVs / 15 users (overdue-penalized energy: IOPO 823.32 vs DDPG 1225.47; GREEDY-OC 1011.89; LOCAL 1676.27). IOPO has the lowest energy across all user counts (10/15/20) and UAV counts (3/4/5).
- **Deadlines:** IOPO keeps decisions-with-overdue-users to 0.6%–6.88% while GREEDY/DDPG/RANDOM hit ~100%; only LOCAL and GREEDY-OC match it on no-overdue but waste UAV resources.
- **Near-optimal:** proximity ratio ≈ 1.00 for IOPO on small configs (5,1),(5,2),(7,1),(7,2), beating DDPG (0.73–1.00).
- **OPPO ablation:** with OPPO 1247.98 vs without 1408.36 (20 users, 3 UAVs); OPPO found 127,966 improved decisions over 200,000 iterations, cutting energy from 1384.57 to 1247.98.
- **Initial reference & IRS:** the GREEDY-OC reference lowers energy across configs; removing the IRS or using zero/random phases reduces transmission speed and raises energy, most when resources are scarce. A smaller DNN (1 layer/64 units) underperforms the 6-layer/256-unit network.

## Limitations
Simulation-only; the authors propose future validation with real THz transmission, practical UAV energy losses, and real workloads. UAV positions are fixed/random (no [[uav-trajectory-control]]) and propulsion energy is not modeled, so only computation and transmission energy count. Single base station and single IRS; binary (not partial) offloading. Exhaustive optimal baselines exist only for tiny systems (≤7 users, ≤2 UAVs); larger systems need many more iterations to approach optimum. The "wireless-powered MEC" framing in the abstract is not backed by a device-side energy-harvesting model — transmission power comes from the base station.

## Relation to the corpus
This is the corpus's entry point for [[intelligent-reflecting-surface]] and [[terahertz-communication]] in UAV-based MEC, and a clear application of [[two-stage-decomposition]]: a learned offloading stage feeding a metaheuristic phase-optimization stage. Its [[order-preserving-quantization]] decision generator shares the DROO lineage seen in [[zhu-2025-lycnn-drl-wpt-mec]], and it uses [[ddpg]] as its main one-stage baseline, linking it to DDPG-based offloading work such as [[bao-2025-ddpg-video-offloading]]. As [[multi-uav-assisted-mec]] with energy-minimizing [[task-offloading]], it sits alongside [[wu-2026-terrain-aware-uav-mec]] and [[jia-2025-dro-uav-hap-mec]], differing mainly in its THz/IRS channel focus and its [[whale-optimization-algorithm]] solver for the continuous phase sub-problem. Note its [[whale-optimization-algorithm]] is the continuous variant, distinct from the wiki's existing [[binary-whale-optimization]] page.

## Raw artifacts
- `raw/sources/Two-Stage_Deep_Energy_Optimization_in_IRS-Assisted_UAV-Based_Edge_Computing_Systems/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
