---
type: source
modeling_card: required
title: "Adaptive Event-Triggered Fuzzy State Observer Control for Surface-Air Vehicles Subject to the Harbor-Approaching Operation"
authors: ["Guoqing Zhang", "Haoyu Zhao", "Jiqiang Li", "Weidong Zhang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3705994"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, uav-usv, event-triggered-control, fuzzy-observer, path-following, harbor-approach, trajectory-control]
related:
  - "[[event-triggered-fuzzy-state-observer]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[control-parameterized-uav-trajectory]]"
  - "[[maritime-mec]]"
created: 2026-07-10
updated: 2026-07-16
---

# Adaptive Event-Triggered Fuzzy State Observer Control for Surface-Air Vehicles Subject to the Harbor-Approaching Operation

## Citation

Zhang, G., Zhao, H., Li, J., & Zhang, W. (2026). *Adaptive Event-Triggered Fuzzy State Observer Control for Surface-Air Vehicles Subject to the Harbor-Approaching Operation*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2026.3705994.

## TL;DR

Proposes a harbor-approach guidance and control scheme for a heterogeneous USV-UAV system. Guidance uses an exponential time-varying velocity law for logical virtual ship / logical virtual aircraft path following; control uses an adaptive event-triggered fuzzy state observer to estimate unmeasured states, adapt the triggering gain, reduce update load, and prove semi-global uniformly ultimately bounded stability.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A heterogeneous surface-air vehicle system combines a 3-DOF underactuated USV and a 6-DOF UAV for harbor-approach path following under nonlinear dynamics, unmeasured states, and bounded wind and wave disturbances. A logical virtual ship generates a decelerating reference, and a logical virtual aircraft maps the horizontal position and yaw reference to the UAV at constant altitude.

**Problem & objective**: The nonlinear event-triggered control design drives USV and UAV tracking and observation errors to a bounded neighborhood while reducing control transmissions, with SGUUB certified by $\dot V_4\le-\varrho_1V_4+\varrho_2$ for $\varrho_1,\varrho_2>0$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Harbor velocity profile | $\kappa_1,\ldots,\kappa_5$ | continuous design parameters | Shape the exponential deceleration reference $u_{sl}(t)$ |
| Vehicle control inputs | $\tau_1,\tau_2,\tau_3$ | continuous vectors | UAV translational and attitude inputs plus USV surge and yaw inputs |
| Trigger threshold | $d_{(\cdot)}$ | continuous, $(0,1)$ | Determines when a held control signal is refreshed |
| Adaptive trigger gain | $\hat{\mathbf g}_i$ | continuous matrix | Compensates the event-triggered signal-amplitude ratio |
| Fuzzy parameter estimate | $\hat{\mathbf W}_i$ | continuous matrix | Approximates unknown nonlinear vehicle dynamics |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | USV and UAV states obey $\dot{\eta}_i=J_i\nu_i$ and $\dot{\nu}_i=F_i+M_i^{-1}R_i\tau_i+D_i$ |
| C2 | Environmental disturbances are bounded, $\lVert D_i\rVert_F\le D_{iM}$ |
| C3 | The underactuated USV has no lateral propulsion input and bounded sway velocity |
| C4 | Events satisfy $\lvert a_{(\cdot)}(t_\iota)-\tau_{(\cdot)}(t)\rvert>d_{(\cdot)}\lvert\tau_{(\cdot)}(t)\rvert$ with $d_{(\cdot)}\in(0,1)$ |
| C5 | Positive-definite controller and observer gains make all quadratic Lyapunov coefficients negative and ensure SGUUB |

**Algorithm**: Generate the LVS exponential velocity reference → map it to LVA reference states → estimate unmeasured states with fuzzy observers → filter virtual controls with dynamic surface control → update fuzzy and trigger gains by adaptive laws → transmit only at threshold events and apply the backstepping control input → verify the composite Lyapunov bound.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied cooperative harbor-approach path following for a heterogeneous USV-UAV system with unmeasured states and external disturbances. They designed an exponential time-varying velocity function for the logical virtual ship to produce a velocity-changing navigation reference. Their adaptive event-triggered fuzzy state observer estimates the hybrid vehicle states and unknown signal-amplitude gain, while backstepping and dynamic surface control generate the vehicle inputs. Lyapunov analysis establishes semi-global uniformly ultimately bounded stability for the closed-loop signals. Numerical results report accurate path following, longer triggering intervals, and approximately 30% to 60% reductions in mean control input and input variation relative to the evaluated controller.

## Problem

Harbor approach requires scheduled deceleration rather than constant-speed path following. The paper argues that constant-velocity guidance can cause premature slowdown or overspeed near the harbor. Control is also difficult because the surface-air system combines underactuated USV dynamics, 6-DOF UAV dynamics, unmeasured states, external wind/wave disturbances, nonlinearities, and communication/control-update pressure.

## System model

- The platform combines a 6-DOF UAV and a 3-DOF USV.
- UAV state covers position and attitude; USV state covers surface position and yaw.
- The USV is underactuated, with no lateral propulsion and bounded sway velocity.
- Guidance maps a logical virtual aircraft to a logical virtual ship: the UAV keeps constant altitude while horizontal position and yaw follow the surface reference.
- The parsed velocity law is $u_{sl}(t)=k_1\exp(k_2t+k_3\sin(k_4t))+k_5$.

## Method

The controller uses an adaptive event-triggered mechanism with trigger threshold $d \in (0,1)$ and an adaptive fuzzy triggered-ratio gain. Fuzzy logic systems approximate nonlinear dynamics, a state observer estimates unmeasured states and fuzzy parameters, and backstepping with dynamic surface control reduces virtual-control derivative complexity. The Lyapunov analysis gives a bound of the form $\dot V \leq -\rho_1 V + \rho_2$, supporting SGUUB stability.

## Key findings

- The parsed simulation parameters include $[k_1,k_2,k_3,k_4,k_5]=[2,-3e{-}3,0.3,5e{-}3,2]$.
- Initial actual USV/UAV positions are around $[-10,10,0]$ m, the initial translational/surge speed is 4 m/s, and the reference yaw is 47.1 degrees.
- Compared with the cited baseline [41], the text reports about 30-60% lower mean control input and input variation.
- The paper reports improved positional tracking accuracy, slightly increased attitude error, and qualitatively longer trigger intervals / lower triggering frequency.

## Relation to the corpus

This is a control-adjacent surface-air vehicle paper, not a MEC offloading formulation. It is useful beside [[uav-usv-cooperative-mec]] because the corpus's UAV-USV pages mostly optimize service, RIS assistance, AoI, or offloading, while this source exposes the low-level guidance/control burden that those architectures abstract away. It also complements [[control-parameterized-uav-trajectory]] by making dynamics and event-triggered updates central to the feasibility story.

## Limitations / extraction notes

The evaluation is simulation-only. The conclusion calls for physical-platform validation, more complex multi-agent tasks, and real communication imperfections. The local parse contains OCR/formula corruption in several equations, so only text-supported numerical summaries are recorded.

## Raw artifacts

- Parse: `raw/sources/Adaptive_Event-Triggered_Fuzzy_State_Observer_Control_for_Surface-Air_Vehicles_Subject_to_the_Harbor-Approaching_Operation/Adaptive_Event-Triggered_Fuzzy_State_Observer_Control_for_Surface-Air_Vehicles_Subject_to_the_Harbor-Approaching_Operation.md`
- Origin PDF: `raw/sources/Adaptive_Event-Triggered_Fuzzy_State_Observer_Control_for_Surface-Air_Vehicles_Subject_to_the_Harbor-Approaching_Operation/Adaptive_Event-Triggered_Fuzzy_State_Observer_Control_for_Surface-Air_Vehicles_Subject_to_the_Harbor-Approaching_Operation.pdf`
- Figures: `raw/sources/Adaptive_Event-Triggered_Fuzzy_State_Observer_Control_for_Surface-Air_Vehicles_Subject_to_the_Harbor-Approaching_Operation/images/`
