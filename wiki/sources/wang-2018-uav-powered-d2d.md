---
type: source
modeling_card: required
title: "Resource Allocation for Energy Harvesting-Powered D2D Communication Underlaying UAV-Assisted Networks"
authors: ["Haichao Wang", "Jinlong Wang", "Guoru Ding", "Le Wang", "Theodoros A. Tsiftsis", "Prabhat Kumar Sharma"]
year: 2018
url: "https://doi.org/10.1109/TGCN.2017.2767203"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 2, no. 1, pp. 14-24, 2018"
tags: [source, device-to-device, wireless-power-transfer, rf-energy-harvesting, energy-causality, resource-allocation, dc-programming]
related:
  - "[[harvest-transmit-store-scheduling]]"
  - "[[energy-causality-constraint]]"
  - "[[haichao-wang]]"
  - "[[device-to-device-communication]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[mozaffari-2016-uav-underlaid-d2d]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
created: 2026-07-14
updated: 2026-11-03
---

# Resource Allocation for Energy Harvesting-Powered D2D Communication Underlaying UAV-Assisted Networks

## Citation

Wang, H., Wang, J., Ding, G., Wang, L., Tsiftsis, T. A., & Sharma, P. K. (2018). *Resource Allocation for Energy Harvesting-Powered D2D Communication Underlaying UAV-Assisted Networks*. **IEEE Transactions on Green Communications and Networking**, 2(1), 14-24. DOI: 10.1109/TGCN.2017.2767203.

## TL;DR

Optimizes multiple mutually interfering D2D pairs with no persistent energy source while a fixed UAV supplies RF energy. Under a finite-horizon harvest-transmit-store model, Lagrangian analysis yields an exclusive per-slot mode and a single switch from harvesting to transmission. Successive difference-of-convex power updates and a discrete golden-section search then produce a suboptimal schedule that respects cumulative energy causality.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ mutually interfering D2D pairs share one band underlaying a UAV-assisted network. A fixed UAV at height $H$ radiates RF power $p_0$; in each of $T$ slots the D2D transmitters harvest $E_n(t)=(1-\tau(t))\eta p_0g_n$ and transmit for fraction $\tau(t)$, with probabilistic LoS/NLoS UAV links.
**Problem & objective**: Problem (9) maximizes the average sum throughput $\frac1T\sum_t\tau(t)\sum_n\log_2(1+\gamma_n(t))$ over $\{\tau(t)\},\{p_n(t)\}$ s.t. C1–C3; after Theorem 1 it becomes the mixed-integer problem (19) over $\{p_n(t)\}$ and the harvest/transmit switch slot $k$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Transmission time fraction | $\tau(t)$ | continuous, $[0,1]$ (binary at the optimum) | Share of slot $t$ used for D2D transmission |
| Switch slot | $k$ | integer, $\{1,\dots,T-1\}$ | Last harvesting slot in (19) |
| D2D transmit power | $p_n(t)$ | continuous, nonnegative | Power of D2D transmitter $n$ in slot $t$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 (9) | Energy causality: $\sum_{k=1}^t\tau(k)p_n(k)\le\sum_{k=1}^tE_n(k),\ \forall t,n$ |
| C2 (9) | Time: $0\le\tau(t)\le1,\ \forall t$ |
| C3 (9) | Power: $p_n(t)\ge0,\ \forall t,n$ |
| (19) | After Theorem 1: $\sum_{t=k+1}^Tp_n(t)\le\sum_{t=1}^k\eta p_0g_n$, $p_n(t)\ge0$, $k\in\{1,\dots,T-1\}$ |
**Algorithm**: Lagrangian relaxation of (9) shows each slot is exclusively harvest or transmit and (Theorem 1) all harvesting slots precede transmission → for fixed $k$, solve the power subproblem (20) by D.C. programming with linearized interference (Algorithm 2) → search $k$ with a floor-adjusted golden-section method (27).

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied resource allocation for RF-energy-harvesting D2D pairs under a fixed UAV power source. They formulated a finite-horizon throughput-maximization problem with mutually interfering D2D links and cumulative energy-causality constraints. Lagrangian analysis proves an exclusive harvest-or-transmit mode in each slot and a single switch from harvesting to transmission. For a fixed switch time, successive difference-of-convex power updates optimize the throughput, and a discrete golden-section search selects the switch. Simulations report higher throughput than an equal-time-allocation (ETA) benchmark across UAV heights and UAV transmit powers, and an average throughput that is almost insensitive to the horizon length $T$.

## Problem

Low-power D2D or sensor transmitters must harvest energy before sending data, but simultaneous same-band D2D links interfere. Allocating more of a finite horizon to harvesting increases available energy while reducing transmission time. The paper jointly chooses the common harvest/transmit schedule and each transmitter's power to maximize average sum throughput without consuming energy before it is available.

## System model

One UAV at a fixed horizontal position and altitude supplies dedicated RF energy to `N` D2D transmitter-receiver pairs. All pairs reuse the same allocated spectrum and transmit simultaneously during information slots, so each receiver's SINR includes interference from every other D2D transmitter. Ground links use distance-based path loss with random fading, while UAV-to-device links use an elevation-dependent probabilistic LoS/NLoS [[air-to-ground-channel-model]].

Across `T` normalized slots, each transmitter can harvest, store, and later use energy. A cumulative [[energy-causality-constraint]] requires consumed energy through every slot to remain no greater than energy harvested through that slot. The objective maximizes time-average aggregate throughput over slot modes and nonnegative D2D powers.

## Method

The paper partially dualizes the cumulative energy constraints to decompose the horizon. Lemma 1 shows that the relaxed per-slot time variable is binary: a slot exclusively harvests or transmits. Theorem 1 then establishes a single-switch [[harvest-transmit-store-scheduling]] structure in which slots `1..k` harvest and slots `k+1..T` transmit.

For a fixed integer switch time, throughput is written as a difference of concave log-sum terms. The interference-only term is linearized to form a tight concave lower bound, and successive convex power problems generate a non-decreasing convergent sequence. A floor-adjusted golden-section procedure searches the discrete switch time, invoking the power optimizer at each objective evaluation. The resulting [[mixed-integer-nonlinear-programming|mixed-integer nonlinear program]] is solved suboptimally; the connection to [[alternating-optimization-sdr-sca]] is the successive convex approximation, not SDR.

## Key findings

- The harvest-first, transmit-later single-switch schedule is a model-derived structural result, not a simulation observation.
- Figure 2 shows the expected tradeoff: additional harvest time initially improves throughput through greater stored energy, but eventually reduces it by leaving too few transmission slots. This is a qualitative figure-derived result.
- Across the UAV-height and power cases plotted in Fig. 3, the proposed optimized schedule outperforms equal half-harvest/half-transmit allocation. The parse states no exact margin.
- The simulated effect of UAV altitude is non-monotonic because increased LoS probability competes with greater distance and path loss. This is scenario-specific; the baseline altitude is 100 m.
- Theorem 2 and Fig. 4 state that normalized optimal throughput is almost unchanged across different horizon lengths under the paper's time-scaling argument. "Almost" is essential because the scaled switch time may not be an integer.
- The reported gain over equal time allocation grows with the number of D2D pairs, while harvesting-efficiency gains become more distinct at larger D2D path-loss exponents. Both trends are figure-derived under the paper's simulation settings.

## Limitations

Validation is simulation-only. The UAV remains fixed, and the paper leaves mobile energy-source trajectory optimization for future work. Harvesting uses a linear constant-efficiency model even though the source notes receiver activation thresholds and power-dependent conversion efficiency. All D2D pairs share one spectrum band and one common slot mode; pair-specific asynchronous scheduling is not modeled.

The successive lower-bound power routine and discrete golden-section search provide no global-optimality guarantee. The horizon-scaling result relies on normalized slots and admits a non-integral scaled switch. Dynamic channel or position evolution, online uncertainty, nonlinear harvesting, and flight energy are outside the model. The parse calls the formulation `MINIP`; this page maps it to the corpus's conventional [[mixed-integer-nonlinear-programming|MINLP]] vocabulary without changing the source wording.

## Relation to the corpus

[[harvest-transmit-store-scheduling]] and [[energy-causality-constraint]] capture the paper's central temporal structure, while [[device-to-device-communication]], [[wireless-power-transfer]], and [[rf-energy-harvesting]] describe its communication and energy roles. [[mozaffari-2016-uav-underlaid-d2d]] studies UAV/D2D spectrum coexistence rather than using the UAV solely as an energy source. [[zhou-2018-uav-wireless-powered-mec]] applies UAV-supplied energy to computation and offloading with trajectory control, and [[xie-2023-wireless-powered-short-packet-uav]] uses TDMA finite-blocklength links and an energy-efficiency objective. First author [[haichao-wang]] also links this result to later UAV relay and deployment work.

## Raw artifacts

- Parse: `raw/sources/Resource_Allocation_for_Energy_Harvesting-Powered_D2D_Communication_Underlaying_UAV-Assisted_Networks/Resource_Allocation_for_Energy_Harvesting-Powered_D2D_Communication_Underlaying_UAV-Assisted_Networks.md`
- Origin PDF: `raw/sources/Resource_Allocation_for_Energy_Harvesting-Powered_D2D_Communication_Underlaying_UAV-Assisted_Networks/Resource_Allocation_for_Energy_Harvesting-Powered_D2D_Communication_Underlaying_UAV-Assisted_Networks.pdf`
- Figures: `raw/sources/Resource_Allocation_for_Energy_Harvesting-Powered_D2D_Communication_Underlaying_UAV-Assisted_Networks/images/`
