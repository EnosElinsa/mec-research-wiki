---
type: source
title: "Resource Allocation and Trajectory Optimization for QoE Provisioning in Energy-Efficient UAV-Enabled Wireless Networks"
authors: ["Fanzi Zeng", "Zhenzhen Hu", "Zhu Xiao", "Hongbo Jiang", "Siwang Zhou", "Wenping Liu", "Daibo Liu"]
year: 2020
url: "https://doi.org/10.1109/TVT.2020.2986776"
venue: "IEEE Transactions on Vehicular Technology, 69(7)"
modeling_card: required
tags: [source, uav-base-station, qoe, energy-efficiency, trajectory-optimization, dinkelbach, block-coordinate-descent]
related:
  - "[[qoe-modeling-mec]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[uav-trajectory-control]]"
  - "[[3gpp-uav-los-probability-model]]"
  - "[[zhu-xiao]]"
created: 2026-11-02
updated: 2026-11-02
---

# Resource Allocation and Trajectory Optimization for QoE Provisioning in Energy-Efficient UAV-Enabled Wireless Networks

## Citation

Zeng, F., Hu, Z., Xiao, Z., Jiang, H., Zhou, S., Liu, W., & Liu, D. (2020). *Resource Allocation and Trajectory Optimization for QoE Provisioning in Energy-Efficient UAV-Enabled Wireless Networks*. **IEEE Transactions on Vehicular Technology, 69**(7). DOI: 10.1109/TVT.2020.2986776.

## TL;DR

A UAV base station serves ground users with uneven QoE requirements under limited energy, power, and spectrum. The paper jointly optimizes user scheduling, 3-D trajectory, transmit power, and bandwidth to maximize energy efficiency while meeting QoE, using Dinkelbach's transform and block coordinate descent, and reports 12.5% higher energy efficiency than throughput maximization.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV serves $M$ ground users, allocating bandwidth $b_m(t)$ and power $p_m(t)$ to scheduled users. The ground-to-air link has LoS probability $P_{m,LoS}(t)=b_1(\frac{180}{\pi}\theta_m(t)-15)^{b_2}$ depending on elevation angle and environment. A 3-D rotary-wing flight energy model adds a climb term to the level-flight power, and transmit power adds communication energy.

**Problem & objective**: Maximize $EE(\{\lambda_m\},\{b_m\},\{\mathbf q\},\{p_m\})=R/E$, transmitted bits per unit of UAV propulsion and communication energy, subject to each user's QoE rate; a mixed-integer nonconvex fractional program.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Scheduling | $\lambda_m(t)$ | binary | User $m$ is served at time $t$ |
| Bandwidth | $b_m(t)$ | $\sum_m\lambda_mb_m\le BW$ | Bandwidth for user $m$ |
| Power | $p_m(t)$ | $\sum_m\lambda_mp_m\le p_{\max}$ | Transmit power for user $m$ |
| Trajectory | $\mathbf q(t)$ | continuous 3-D | UAV position |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (1a) | UAV speed, $\lVert\dot q(t)\rVert\le v_{\max}$. |
| (1b) | QoE rate, $R_m(t)\ge R^m_{th}$ for scheduled users. |
| Scheduling | Every user is scheduled at least once, $\int_0^T\lambda_m(t)dt\ge1$. |
| (5) | Bandwidth and power budgets, $\sum_m\lambda_m(t)b_m(t)\le BW$, $\sum_m\lambda_m(t)p_m(t)\le p_{\max}$. |

**Algorithm**: Transform the fractional objective into subtractive form with Dinkelbach's method, then split into four subproblems (scheduling, trajectory, power, bandwidth) optimized alternately by block coordinate descent in a two-loop algorithm.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng et al. [x] studied a UAV-enabled aerial base station that provides wireless service to ground users with different quality-of-experience requirements, which are randomly and unevenly distributed. Given limited UAV coverage, onboard energy, transmission power, and spectrum, they jointly optimized user communication scheduling, UAV trajectory, transmit power, and bandwidth allocation to maximize energy efficiency while satisfying user QoE. The mixed-integer non-convex problem is solved in two steps: the objective is first transformed into a tractable form, and the problem is then divided into four subproblems solved by an iterative algorithm based on Dinkelbach's method and block coordinate descent. Simulation results show that the method achieves higher energy efficiency than the baselines, 12.5% higher than an approach that only maximizes throughput.

## Problem framing

Uniform service wastes energy when user demands differ. Matching scheduling and resources to each user's QoE lets the UAV meet demand with less flight.

## System model

- The 3-D energy model accounts for vertical flight, which costs more than level flight.
- Scenarios with sufficient and insufficient UAV energy are studied.

## Method

The outer loop updates the Dinkelbach parameter; the inner loop runs block coordinate descent over the four subproblems.

## Key findings

- Energy efficiency is 12.5% higher than with throughput maximization only.
- An optimal level-flight altitude exists under sufficient energy.

## Limitations / future work

The model uses one UAV.

## Relation to the corpus

Applies [[fractional-programming-dinkelbach]] to QoE-aware UAV service, related to [[qoe-modeling-mec]] and [[uav-trajectory-control]].

## Raw artifacts

- Parse: `raw/sources/Resource_Allocation_and_Trajectory_Optimization_for_QoE_Provisioning_in_Energy-Efficient_UAV-Enabled_Wireless_Networks/Resource_Allocation_and_Trajectory_Optimization_for_QoE_Provisioning_in_Energy-Efficient_UAV-Enabled_Wireless_Networks.md`
- Origin PDF and extracted figures are in the same folder.
