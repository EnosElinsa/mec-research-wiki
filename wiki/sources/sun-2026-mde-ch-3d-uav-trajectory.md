---
type: source
title: "3D UAV Trajectory Planning for IoT Data Collection via Matrix-Based Evolutionary Computation"
authors: ["Pei-Fa Sun", "Yujae Song", "Kangyu Gao", "Yukai Wang", "Changjun Zhou", "Sang-Woon Jeon", "Jun Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3722860"
venue: "IEEE Transactions on Mobile Computing, 25(11)"
modeling_card: required
tags: [source, uav-data-collection, 3d-trajectory, differential-evolution, constraint-handling, bezier-curve, terrain-aware]
related:
  - "[[uav-data-collection]]"
  - "[[differential-evolution]]"
  - "[[constraint-violation-evaluation]]"
  - "[[terrain-aware-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-11-02
updated: 2026-11-02
---

# 3D UAV Trajectory Planning for IoT Data Collection via Matrix-Based Evolutionary Computation

## Citation

Sun, P.-F., Song, Y., Gao, K., Wang, Y., Zhou, C., Jeon, S.-W., & Zhang, J. (2026). *3D UAV Trajectory Planning for IoT Data Collection via Matrix-Based Evolutionary Computation*. **IEEE Transactions on Mobile Computing, 25**(11). DOI: 10.1109/TMC.2026.3722860.

## TL;DR

A UAV collects data from ground nodes over 3-D terrain and must minimize flight plus communication energy while meeting each node's data demand. The paper parameterizes a continuous trajectory with Bézier curves and solves the nonconvex constrained problem with MDE-CH, a matrix-based differential evolution with constraint handling that avoids penalty tuning and parallelizes well.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV starts at $\mathbf q_{\mathrm{str}}$, serves $K$ ground nodes at terrain-dependent heights $u_{k,z}=f_z(u_{k,x},u_{k,y})$ in area $\mathcal U$, and ends at $\mathbf q_{\mathrm{end}}$ within $T\le T_{\max}$. Energy combines a 3-D propulsion model and communication energy.

**Problem & objective**: Problem (19): $\min_{\{\mathbf q(t)\}_{t\in[0,T]}}\{E_{\mathrm{fly}}+E_{\mathrm{com}}\}$, jointly with the completion time $T$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Trajectory | $\mathbf q(t)=[q_x(t),q_y(t),q_z(t)]$ | continuous, Bézier-parameterized | UAV position over the mission |
| Completion time | $T$ | $[0,T_{\max}]$ | Mission duration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Endpoints, $\mathbf q(0)=\mathbf q_{\mathrm{str}}$, $\mathbf q(T)=\mathbf q_{\mathrm{end}}$. |
| C3 | Horizontal position in $\mathcal U$. |
| C4 | Altitude above terrain, $q_z(t)\in[f_z(q_x,q_y)+\Delta_z,U_z]$. |
| C5 | Speed, $v(t)\le v_{\max}$. |
| C6-C8 | Per-axis acceleration limits, $\lvert a_i(t)\rvert\le a_{i,\max}$. |
| C9 | Data demand, $Q_k\ge Q_k^{\mathrm{th}}$ for every node. |
| C10 | $0\le T\le T_{\max}$. |

**Algorithm**: Represent the trajectory with Bézier curves to reduce decision variables; MDE-CH runs matrix-form differential evolution with a constraint-handling rule that keeps feasible solutions without penalty parameters.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied UAV-assisted Internet of Things data collection that minimizes total energy consumption while accounting for the UAV's physical capabilities, the heterogeneous data demands of IoT nodes, and three-dimensional terrain. They formulated a continuous three-dimensional temporal-spatial trajectory problem and used Bézier curves to reduce the number of decision variables. To solve the non-convex problem with several types of constraints, they proposed a matrix-based differential evolution with constraint handling, a computation-efficient evolutionary algorithm that ensures feasible solutions without tuning penalty parameters and supports parallel computation. Numerical evaluations show that the algorithm provides a continuous trajectory that efficiently minimizes energy under practical constraints and outperforms the compared methods, including in scenarios with 3D terrain and varying throughput requirements.

## Problem framing

Discretized trajectory optimization becomes expensive in continuous 3-D space with terrain and kinematic limits. A curve parameterization plus evolutionary search keeps the problem small and handles nonconvex constraints directly.

## System model

- Ground nodes sit on terrain described by $f_z$, and the UAV keeps a clearance $\Delta_z$.
- Acceleration limits are stricter than speed limits to keep flight smooth.

## Method

MDE-CH applies differential evolution operations to whole populations in matrix form.

## Key findings

- MDE-CH yields feasible continuous 3-D trajectories with lower energy than compared methods.
- Performance holds with terrain and varied throughput requirements.

## Limitations / future work

The authors suggest joint optimization of UAV and LEO or very-low-Earth-orbit satellite trajectories in 6G non-terrestrial networks.

## Relation to the corpus

An evolutionary approach to [[uav-data-collection]] trajectories, using [[differential-evolution]] with constraint handling related to [[constraint-violation-evaluation]].

## Raw artifacts

- Parse: `raw/sources/3D_UAV_Trajectory_Planning_for_IoT_Data_Collection_via_Matrix-Based_Evolutionary_Computation/3D_UAV_Trajectory_Planning_for_IoT_Data_Collection_via_Matrix-Based_Evolutionary_Computation.md`
- Origin PDF and extracted figures are in the same folder.
