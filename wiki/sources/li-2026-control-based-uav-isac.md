---
type: source
title: "A Control-Based Design of Beamforming and Trajectory for UAV-Enabled ISAC System"
authors: ["Bin Li", "Hongyun Zhang", "Yue Rong", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3604344"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
modeling_card: required
tags: [source, isac, uav-trajectory, beamforming, control-parameterization, alternating-optimization, dynamic-model]
related:
  - "[[control-parameterized-uav-trajectory]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zhu-han]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[wang-2026-robust-anti-uav-isac]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Control-Based Design of Beamforming and Trajectory for UAV-Enabled ISAC System

## Citation

Li, B., Zhang, H., Rong, Y., & Han, Z. (2026). *A Control-Based Design of Beamforming and Trajectory for UAV-Enabled ISAC System*. **IEEE Transactions on Wireless Communications**, 25, 3469-3484. DOI: 10.1109/TWC.2025.3604344.

## TL;DR

Designs UAV-ISAC beamforming and trajectory with explicit 3-DoF and 6-DoF UAV dynamics instead of treating the UAV as a mass point. The alternating solver uses SCA/SDR for communication and sensing beamforming, then transforms trajectory planning into an optimal-control problem through control parameterization and exact penalties solved by SQP.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna quadrotor UAV serves $M$ ground users in the downlink while sensing $J$ points over a finite horizontal flight at fixed altitude. A ULA transmits user streams and a dedicated sensing signal, and the flight is governed by either a 3-DoF translational model or a 6-DoF rigid-body model.

**Problem & objective**: Problems $P_1$ and $P_2$ maximize the average weighted communication sum rate $R_{\mathrm{ave}}=\frac{1}{T}\int_0^T\sum_{m=1}^{M}\rho_m R_m(t)\,dt$ by jointly designing the trajectory and communication and sensing beamforming under the corresponding UAV dynamics.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\boldsymbol p(t)$ | continuous state trajectory | Horizontal UAV position over the flight horizon |
| Communication beamformer | $\boldsymbol w_m(t)$ | complex continuous vector | Beamforming vector for user $m$ |
| Sensing covariance | $\boldsymbol G_d(t)$ | positive semidefinite matrix, $\boldsymbol G_d(t)\succeq\boldsymbol 0$ | Covariance of the dedicated sensing signal |
| Flight control | $\boldsymbol u(t)$ | continuous control input | Force and attitude control variables that drive the selected dynamic model |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 22a | Every sensing point meets its beam-pattern threshold: $\Theta_{r,j}(\boldsymbol p(t),\{\boldsymbol w_m(t)\},\boldsymbol G_d(t))\geq\Theta_j^{\mathrm{th}}$ |
| 22b | Horizontal speed is bounded: $\sqrt{\dot x(t)^2+\dot y(t)^2}\leq V_{\max}$ |
| 22c | The flight begins and ends at prescribed locations: $\boldsymbol p(0)=\boldsymbol p_{\mathrm I}$ and $\boldsymbol p(T)=\boldsymbol p_{\mathrm F}$ |
| Dynamics | States and controls satisfy the selected 3-DoF or 6-DoF differential model throughout the horizon |
| Power | Communication and sensing beams satisfy the UAV transmit-power limit at each time |

**Algorithm**: Alternate two blocks until the increase in $R_{\mathrm{ave}}$ is below $\Gamma^{\mathrm{th}}$: for a fixed trajectory, apply SCA and SDR and solve the resulting semidefinite beamforming problem; for fixed beams, cast the dynamic trajectory block as optimal control, discretize the controls by control parameterization, enforce continuous constraints with an exact penalty, and solve the nonlinear program by SQP.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied joint beamforming and trajectory design for a multi-antenna UAV that provides downlink communication while sensing a target region under explicit 3-DoF and 6-DoF flight dynamics. They formulated average weighted sum-rate maximization over the UAV trajectory, user beamformers, and sensing covariance subject to dynamic, sensing-gain, speed, endpoint, and transmit-power constraints. Their alternating method applies SCA and SDR to the beamforming block and uses control parameterization, an exact penalty, and SQP for the trajectory-control block. Simulations reported that the 6-DoF design produced a trackable planned trajectory and reduced actual communication degradation and sensing-constraint violations, while the 3-DoF design offered a lower-complexity performance tradeoff.

## Problem

Many UAV-enabled ISAC trajectory designs discretize paths and model the UAV only by position and speed. The paper argues that ignoring rotational motion, internal forces, and torques can produce planned paths that a real controller cannot track, causing communication degradation and sensing constraint violations.

## System model

- A multi-antenna quadrotor UAV provides downlink communication to multiple ground users while sensing multiple target points in a region.
- The UAV flies from a fixed initial point to a fixed final point over a finite horizon at fixed altitude.
- A ULA mounted on the UAV transmits user information signals and a dedicated radar signal.
- Two dynamic models are considered: a 3-DoF translational model and a 6-DoF translational-plus-rotational rigid-body model.
- The objective maximizes average weighted communication rate subject to UAV dynamic constraints, sensing beam-pattern-gain requirements, and transmit-power constraints.

## Method

- Alternates between beamforming and trajectory blocks.
- Given a trajectory, applies SCA and SDR to reformulate communication/sensing beamforming as a convex problem.
- Given beamforming vectors and sensing covariance, rewrites trajectory optimization as a state-space optimal-control problem.
- Uses piecewise constant control parameterization plus exact penalty functions for continuous state constraints.
- Solves the resulting static nonlinear program with sequential quadratic programming.

## Key findings

- Planned trajectories from the model-free benchmark, 3-DoF model, and 6-DoF model can look similar, but the actual tracked trajectories differ once PID tracking and UAV dynamics are considered.
- The model-free trajectory can fail to reach the final destination under the 6-DoF tracking model, while the 3-DoF trajectory reaches it with mismatch and the 6-DoF trajectory matches the planned path.
- Actual trajectories for the benchmark and 3-DoF scheme can violate the sensing beam-pattern threshold even when their planned trajectories satisfy it.
- Planned benchmark/3-DoF rates may look higher, but their actual rates fall below the 6-DoF planned/actual trajectory because omitted dynamics degrade tracking.
- The 3-DoF model is presented as a lower-complexity compromise, while the 6-DoF model gives the most faithful practical UAV-control behavior.

## Limitations / future work

The validation is numerical simulation with known user/target positions and modeled UAV dynamics. The parse does not report field deployment, hardware-in-the-loop control, or robustness to sensing-target uncertainty.

## Relation to the corpus

This paper gives the ISAC track a control-theoretic counterpart to DRL trajectory controllers such as [[ye-2026-deeplsc-lae-isac]], [[ye-2026-meta-deepesc-lae-isac]], and [[ye-2026-mode-lae-isac]]. It adds [[control-parameterized-uav-trajectory]] as a concept for trajectory design that treats control inputs and trackability as first-class constraints. It also updates [[zhu-han]]'s roster with a UAV-ISAC control paper distinct from his MEC/offloading sources.

## Raw artifacts

- `raw/sources/A_Control-Based_Design_of_Beamforming_and_Trajectory_for_UAV-Enabled_ISAC_System/A_Control-Based_Design_of_Beamforming_and_Trajectory_for_UAV-Enabled_ISAC_System.md`
- `raw/sources/A_Control-Based_Design_of_Beamforming_and_Trajectory_for_UAV-Enabled_ISAC_System/A_Control-Based_Design_of_Beamforming_and_Trajectory_for_UAV-Enabled_ISAC_System.pdf`
- Extracted figures in `raw/sources/A_Control-Based_Design_of_Beamforming_and_Trajectory_for_UAV-Enabled_ISAC_System/images/`
