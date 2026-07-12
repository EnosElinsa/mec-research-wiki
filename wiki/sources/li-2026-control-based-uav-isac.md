---
type: source
title: "A Control-Based Design of Beamforming and Trajectory for UAV-Enabled ISAC System"
authors: ["Bin Li", "Hongyun Zhang", "Yue Rong", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3604344"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
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
updated: 2026-07-13
---

# A Control-Based Design of Beamforming and Trajectory for UAV-Enabled ISAC System

## Citation

Li, B., Zhang, H., Rong, Y., & Han, Z. (2026). *A Control-Based Design of Beamforming and Trajectory for UAV-Enabled ISAC System*. **IEEE Transactions on Wireless Communications**, 25, 3469-3484. DOI: 10.1109/TWC.2025.3604344.

## TL;DR

Designs UAV-ISAC beamforming and trajectory with explicit 3-DoF and 6-DoF UAV dynamics instead of treating the UAV as a mass point. The alternating solver uses SCA/SDR for communication and sensing beamforming, then transforms trajectory planning into an optimal-control problem through control parameterization and exact penalties solved by SQP.

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
