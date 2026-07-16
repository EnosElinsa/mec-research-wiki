---
type: source
modeling_card: required
title: "Federated Linear Bandit Learning via UAV Aided Over-the-Air Computation"
authors: ["Junkai Qian", "Yuning Jiang", "Yudi Zhang", "Xin Liu", "Ting Wang", "Yuanming Shi", "Colin N. Jones"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3651589"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, federated-linear-bandit, linucb, over-the-air-computation, uav-trajectory-control, admm, regret]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[federated-linear-bandit-learning]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[alternating-direction-method-of-multipliers]]"
  - "[[uav-trajectory-control]]"
  - "[[yuanming-shi]]"
created: 2026-07-13
updated: 2026-07-16
---

# Federated Linear Bandit Learning via UAV Aided Over-the-Air Computation

## Citation

Qian, J., Jiang, Y., Zhang, Y., Liu, X., Wang, T., Shi, Y., & Jones, C. N. (2026). *Federated Linear Bandit Learning via UAV Aided Over-the-Air Computation*. **IEEE Transactions on Mobile Computing**, 25(6), 9284-9299. DOI: 10.1109/TMC.2026.3651589.

## TL;DR

Combines event-triggered federated LinUCB with analog AirComp aggregation at a mobile UAV server. A BCD-ADMM optimizer jointly controls device powers, receive normalization, and UAV horizontal trajectory to reduce aggregation MSE, while the regret analysis makes channel noise part of the online-learning guarantee.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ mobile IoT devices run federated LinUCB with one single-antenna UAV server flying at fixed altitude. On event-triggered rounds, clients simultaneously upload Gram-matrix and reward-vector statistics through noisy fading multiple-access AirComp; accurate CSI, tight synchronization, error-free downlink broadcast, and quasi-static intra-slot channels are assumed.

**Problem & objective**: The communication problem is a non-convex time-averaged AirComp design, $\min_{\boldsymbol\alpha,\boldsymbol\eta,\mathbf q}\frac1T\sum_{t=1}^T\mathrm{MSE}_t$, jointly optimizing device transmission, UAV receive normalization, and horizontal trajectory while the learning layer minimizes cumulative group pseudo-regret.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Device transmission factor | $\alpha_{i,t}$ | continuous, power-constrained | Analog scaling used by device $i$ in slot $t$ |
| Receive normalization | $\eta_t$ | continuous, positive | UAV post-processing factor for the aggregated signal |
| UAV trajectory | $\mathbf q_t$ | continuous horizontal position | UAV server location in slot $t$ |
| Bandit action | $\theta_{i,t}$ | discrete candidate action | LinUCB action selected by device $i$ from its confidence bound |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every device satisfies per-slot peak and horizon-average transmit-power limits |
| C2 | Receive normalization remains positive and is shared by the simultaneous AirComp upload |
| C3 | UAV displacement satisfies $\lVert\mathbf q_t-\mathbf q_{t-1}\rVert\le V_{\max}\Delta t$ |
| C4 | UAV initial/final locations and horizontal flight-region limits are respected |
| C5 | Synchronization occurs only when the determinant-ratio information-gain trigger fires |

**Algorithm**: Run event-triggered federated LinUCB → aggregate cached statistics by AirComp → alternate a closed-form normalization update, KKT/binary-search transmission update, and trajectory QCQP → solve the trajectory block by ADMM projection and quadratic updates → repeat BCD until the average aggregation MSE converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qian et al. [x] studied federated contextual linear bandit learning through UAV-aided over-the-air computation. Their event-triggered federated LinUCB method aggregates client Gram matrices and reward vectors over noisy fading channels at a mobile UAV server. They formulated a non-convex problem that minimizes time-averaged AirComp mean-square error by jointly optimizing device transmission factors, receive normalization, and UAV trajectory under peak, average-power, and mobility constraints. The BCD-ADMM solution alternates closed-form normalization, KKT and binary-search signal-quality updates, and an ADMM trajectory QCQP. Theoretical analysis gives the stated regret upper bound, and simulations report lower pseudo-regret than the evaluated static-UAV, fixed-power, hover-with-power-control, and BCD-SCA baselines.

## Problem framing

Mobile IoT clients need a shared contextual-bandit model without centralizing raw observations. Orthogonal uploads scale poorly with client count, but noisy AirComp distorts the Gram matrices and reward vectors that drive confidence bounds. A UAV server can improve geometry for moving client clusters, provided its mobility and radio variables are optimized together.

## System model

- `N` mobile devices share one fixed unknown `d`-dimensional linear reward parameter over `T` rounds.
- One single-antenna UAV server flies at fixed altitude and optimizes only its horizontal trajectory.
- Devices send analog sufficient-statistic updates over a fading multiple-access channel; UAV downlink broadcasts are assumed error-free.
- Per-slot peak and time-average device powers constrain AirComp; accurate CSI and tight synchronization are assumed without overhead.
- Device clusters follow predesigned mobile paths, and channels are quasi-static inside each slot.

## Method

[[federated-linear-bandit-learning|Federated LinUCB]] broadcasts global Gram/reward statistics, combines them with local caches, and selects upper-confidence-bound actions. A determinant-ratio information-gain trigger initiates synchronization; otherwise devices keep collecting locally. Triggered clients simultaneously upload cached statistics through [[over-the-air-computation|AirComp]].

The communication layer minimizes average aggregation MSE by BCD. Receive normalization has a closed form; signal-quality/power updates use KKT conditions and binary search; the trajectory block becomes a convex weighted-distance QCQP solved by [[alternating-direction-method-of-multipliers|ADMM]] projections and a quadratic trajectory update.

## Key findings

- Under the stated synchronization/noise conditions, the paper gives regret order `O(sigma sqrt(N T d) log(gamma_max/gamma_min + T L^2/(d gamma_min)))`, summarized as `O(sqrt(T) log T)` for fixed channel noise.
- Simulations use a `400 m x 400 m` region, `N = 50`, `d = 30`, 500 slots, 100 m altitude, and 20 m/s maximum UAV speed.
- BCD-ADMM reports the lowest pseudo-regret among static-UAV, fixed-power, hover-with-power-control, and BCD-SCA baselines; the parse states no numerical margin.
- BCD-SCA and BCD-ADMM give the lowest parameter-estimation MSE, while the optimized UAV follows moving device clusters more closely than the static baseline.

## Limitations / future work

The model assumes accurate CSI, tight synchronization, error-free downlink, fixed altitude, quasi-static intra-slot channels, and one shared stationary parameter. It omits UAV propulsion energy and formal privacy guarantees. Evaluation is synthetic, and the centralized `O(NT^2 + T^3)` trajectory work per inner iteration may bottleneck at massive scale. CSI/synchronization overhead, energy-aware mobility, intra-slot variation, and lighter decentralized solvers remain open.

## Relation to the corpus

This source separates federated online decision learning from gradient-based [[federated-learning]]. Unlike [[aircomp-assisted-asynchronous-fl]], clients aggregate bandit sufficient statistics on event-triggered rounds, and communication noise enters a regret bound rather than a model-convergence metric.

[[aerial-federated-aggregation-design-space]] therefore treats this as an event-triggered AirComp design with a regret guarantee, not as another accuracy- or training-loss result.

## Raw artifacts

- Parse: `raw/sources/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation.md`
- Origin PDF: `raw/sources/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation.pdf`
- Figures: `raw/sources/Federated_Linear_Bandit_Learning_via_UAV_Aided_Over-the-Air_Computation/images/`
