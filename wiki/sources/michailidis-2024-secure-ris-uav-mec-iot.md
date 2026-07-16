---
type: source
modeling_card: required
title: "Optimization of Secure Computation Efficiency in UAV-Enabled RIS-Assisted MEC-IoT Networks With Aerial and Ground Eavesdroppers"
authors: ["Emmanouel T. Michailidis", "Maria-Garyfallio Volakaki", "Nikolaos I. Miridakis", "Demosthenes Vouyioukas"]
year: 2024
url: "https://doi.org/10.1109/TCOMM.2024.3372877"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, multi-uav-assisted-mec, intelligent-reflecting-surface, physical-layer-security, secure-computation-efficiency, computation-offloading, fractional-programming-dinkelbach]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[physical-layer-security]]"
  - "[[secure-computation-efficiency]]"
  - "[[secrecy-outage-probability]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[task-offloading]]"
created: 2026-05-31
updated: 2026-07-16
---

# Optimization of Secure Computation Efficiency in UAV-Enabled RIS-Assisted MEC-IoT Networks With Aerial and Ground Eavesdroppers

## Citation

Michailidis, E. T., Volakaki, M.-G., Miridakis, N. I., & Vouyioukas, D. (2024). *Optimization of Secure Computation Efficiency in UAV-Enabled RIS-Assisted MEC-IoT Networks With Aerial and Ground Eavesdroppers*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2024.3372877. (Manuscript received 30 Jul 2023; date of publication 1 Mar 2024; date of current version 19 Jul 2024 → year 2024.)

## TL;DR

A security-aware **partial computation offloading** framework for an MEC-IoT network with both **aerial eavesdroppers (AEs)** and **ground eavesdroppers (GEs)**. Ground nodes (GNs) compute partly locally and offload the rest to a UAV that acts as **both an aerial MEC server and a decode-and-forward relay** to a MEC-enabled access point (AP); a **RIS** near the AP improves the UAV→AP link. The paper derives **secrecy-outage-probability (SOP)** expressions over Nakagami-m fading and maximizes the **minimum secure computation efficiency (SCE)** by jointly optimizing transmit-power allocation, time-slot scheduling, task allocation, and RIS phase shifts, via Dinkelbach + BCD + bisection methods.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ battery-powered ground nodes partially compute tasks locally and use TDMA to offload the remainder to one UAV, which serves as an aerial MEC server and half-duplex decode-and-forward relay to a grid-powered MEC access point through a nearby RIS. Independent non-identical Nakagami-$m$ links include both colluding aerial eavesdroppers and ground eavesdroppers, and the UAV follows a predetermined straight-line path.

**Problem & objective**: Problem P1, a non-convex max-min fractional program, maximizes the minimum secure computation efficiency, $\max_{\mathbf P,\boldsymbol\tau,\mathbf B,\boldsymbol\varphi}\min_k\eta_{\mathrm{SCE},k}$, measured as securely processed bits per weighted energy consumption.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading powers | $\mathbf P$ | continuous, bounded nonnegative | Ground-node and UAV transmit powers |
| Offloading times | $\boldsymbol\tau$ | continuous, slot-bounded | GN-to-UAV and UAV-to-AP transmission durations |
| Task allocation | $\mathbf B$ | continuous, nonnegative bits | Bits computed locally, at the UAV, and at the AP |
| RIS phases | $\boldsymbol\varphi$ | continuous, $[0,2\pi]$ | RIS phase alignment for the AP and ground-eavesdropper links |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 38b-38c | $b_{k,l}[n]+b_{k,U}[n]+b_{k,A}[n]\ge b_{k,\min}[n]$ and every allocated bit count is nonnegative |
| 38d-38e | GN and UAV offloading powers remain within their respective maxima |
| 38f-38h | Transmission and computation durations fit the slot and per-user time shares |
| 38i-38j | Allocated UAV/AP bits do not exceed the GN-to-UAV and UAV-to-AP offloading capacities |
| 38k | RIS phase variables satisfy $0\le\varphi\le2\pi$ |

**Algorithm**: Derive exact and asymptotic secrecy-outage probabilities → apply Dinkelbach transformation to the max-min fractional objective → use block coordinate descent to separate power, time, task, and phase blocks → solve the scalar coupled updates by bisection → iterate to convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Michailidis et al. [x] studied security-aware computation offloading in a UAV-enabled RIS-assisted MEC-IoT network with aerial and ground eavesdroppers. They derived exact, closed-form, and asymptotic secrecy-outage-probability expressions under independent non-identical Nakagami-$m$ fading. They formulated a non-convex max-min problem that maximizes secure computation efficiency by jointly optimizing transmit-power allocation, time-slot scheduling, task allocation, and RIS phase shifts. Their iterative solution combines Dinkelbach, block coordinate descent, bisection, and the derived outage expressions. Numerical results show that secure computation efficiency increases with the number of RIS elements and approaches saturation in the evaluated settings, while higher computation demand or additional eavesdroppers reduces the achieved efficiency.

## Problem framing

IoT computation offloading over wireless is exposed to blockage, fading, and eavesdropping. UAVs improve LoS coverage in hard-to-reach areas and a RIS reshapes the propagation environment for the blockage-prone UAV→AP link, but security must be addressed against unauthorized data leakage. The authors note that prior work studied GEs extensively but rarely both AEs and GEs jointly, and that the joint RIS + UAV + secure-MEC design with both eavesdropper types was unexplored.

## System model

- **Actors.** K static battery-powered GNs; one UAV (aerial MEC server + DF half-duplex relay); a grid-powered MEC-enabled AP; a RIS (with phase errors) on a building near the AP; L_AE AEs and L_GE GEs (worst case: AEs collude via maximum-ratio combining).
- **Offloading.** Per-slot task split b_k = local + UAV + AP bits; TDMA among GNs; energy includes cubic-frequency compute energy at GN/UAV, offloading energy, and rotary-wing UAV **propulsion energy** (see [[rotary-wing-propulsion-energy-model]]).
- **Objective.** Maximize the **minimum SCE** = total computation bits / weighted total energy ([[secure-computation-efficiency]]), subject to power, time-slot, task-allocation, and RIS phase-shift constraints. A 3-D geometric mobility model (distance + velocity vectors) tracks node positions.

## Method

- Derive analytical, closed-form, and asymptotic **SOP** expressions under independent non-identical **Nakagami-m** fading ([[secrecy-outage-probability]]); the asymptotic form assumes a large RIS array.
- Solve the non-convex fractional max-min SCE problem with a **Dinkelbach** transform for the fractional objective ([[fractional-programming-dinkelbach]]) plus **block coordinate descent (BCD)** and **bisection** over the coupled variables. Evaluated in MATLAB 2023b + CVX. The UAV uses a **predetermined straight-line trajectory** (3-D trajectory optimization deferred).

## Key findings

- Results underscore a balance between desired SOP and energy consumption, and confirm the optimized scheme beats benchmarks.
- Positioning the UAV closer to the RIS improves SCE when the UAV→RIS channel is poor; positioning it closer to the GNs helps when the GN→UAV link degrades (Fig. 7).
- SCE improves with more RIS reflecting elements and saturates (the parse notes the target rate is met around 57 elements, and asymptotic SCE curves converge to the analytical ones near ~60 elements); SCE declines as GNs' minimal computing requirement, or the number of AEs/GEs, increases — but a high channel quality and large RIS mitigate that decline (Figs. 8, 10, 11).

## Limitations / future work

The UAV trajectory is **not** optimized (fixed straight-line path); 3-D trajectory optimization is left to future work, with potential to further raise SCE. Multi-UAV deployment is discussed as a future direction (with coordination/interference/migration-overhead challenges). Results are simulation-based; element-count thresholds are read from the figures and are indicative.

## Relation to the corpus

A **secure UAV-RIS-MEC** entry notable for jointly handling **both aerial and ground eavesdroppers** and for an analytical **SOP-over-Nakagami-m** treatment. It joins the corpus's secure-MEC / PLS thread alongside [[yao-2025-secure-isac-dual-eavesdropping]] (dual eavesdropping, ISAC) and [[chen-2024-three-party-hierarchical-game-pls]], and the RIS line ([[wu-2025-iopo-irs-uav-thz-mec]], [[sun-2024-mfris-semantic-antijamming]]). It introduces the [[secure-computation-efficiency]] and [[secrecy-outage-probability]] concepts and reuses [[fractional-programming-dinkelbach]], [[alternating-optimization-sdr-sca]], and the [[rotary-wing-propulsion-energy-model]].

## Raw artifacts

- `raw/sources/Optimization_of_Secure_Computation_Efficiency_in_UAV-Enabled_RIS-Assisted_MEC-IoT_Networks_With_Aerial_and_Ground_Eavesdroppers/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
