---
type: source
title: "Joint Transceiver and Trajectory Design for Secure UAV-Enabled Over-the-Air Computation"
authors: ["Yuxia Gong", "Jianping Yao", "Jie Xu", "Yi Fang", "Guojun Han", "Tony Q. S. Quek"]
year: 2025
url: "https://doi.org/10.1109/LWC.2025.3626954"
venue: "IEEE Wireless Communications Letters"
modeling_card: required
tags: [source, over-the-air-computation, physical-layer-security, uav-trajectory, eavesdropper, successive-convex-approximation]
related:
  - "[[over-the-air-computation]]"
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[jianping-yao]]"
  - "[[jie-xu]]"
  - "[[yi-fang]]"
  - "[[guojun-han]]"
  - "[[tony-q-s-quek]]"
created: 2026-11-02
updated: 2026-11-02
---

# Joint Transceiver and Trajectory Design for Secure UAV-Enabled Over-the-Air Computation

## Citation

Gong, Y., Yao, J., Xu, J., Fang, Y., Han, G., & Quek, T. Q. S. (2025). *Joint Transceiver and Trajectory Design for Secure UAV-Enabled Over-the-Air Computation*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2025.3626954.

## TL;DR

A UAV acts as a mobile fusion center that aggregates ground-sensor data by AirComp while an eavesdropper listens. The letter minimizes the UAV's average computation MSE over receiver coefficients, sensor transmit scalers, and trajectory, while keeping the eavesdropper's MSE above a threshold, using alternating optimization with SCA.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ ground sensors transmit simultaneously to a UAV flying from $\mathbf q_S$ to $\mathbf q_E$ over $M$ slots. An eavesdropper (EVE) applies its own receive coefficient $a_e[m]$ to estimate the same aggregate.

**Problem & objective**: (P0): $\min_{a_0[m],b_k[m],\mathbf q[m]}\frac1M\sum_m\mathrm{MSE}_0(a_0[m],b_k[m],\mathbf q[m])$, the average AirComp MSE at the UAV.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV receiver coefficient | $a_0[m]$ | complex scalar | Receive scaling at the UAV in slot $m$ |
| Sensor transmitter scaler | $b_k[m]$ | $b_k^2[m]\le P_{\max}$ | Transmit scaling of sensor $k$ |
| Trajectory | $\mathbf q[m]$ | continuous | UAV position in slot $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (13b) | EVE secrecy, $\min_{a_e[m]}\mathrm{MSE}_e(a_e[m],b_k[m],\mathbf q[m])\ge\xi$. |
| (13c) | Sensor power, $b_k^2[m]\le P_{\max}$. |
| (13d) | UAV mobility, $\lVert\mathbf q[m+1]-\mathbf q[m]\rVert\le L$. |
| (13e) | Endpoints, $\mathbf q[0]=\mathbf q_S$ and $\mathbf q[M+1]=\mathbf q_E$. |

**Algorithm**: Transform the EVE MSE constraint for given variables, then alternately optimize the UAV receiver coefficient, the sensor scalers, and the trajectory, using SCA for the nonconvex trajectory step.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gong et al. [x] investigated a secure UAV-enabled over-the-air computation network in which a UAV acts as a mobile fusion center to aggregate data from multiple ground sensors while an eavesdropper attempts to intercept the transmitted signals. To ensure secure and efficient computation, they jointly optimized the UAV's receiver coefficients, the sensors' transmitter scaling factors, and the UAV trajectory to minimize the mean square error at the UAV. The problem is subject to an MSE constraint at the eavesdropper, a maximum transmit power constraint, and UAV trajectory constraints. Given its nonconvexity, an efficient algorithm combining alternating optimization with successive convex approximation is proposed. Numerical results show that the scheme outperforms benchmark approaches, including straight-line trajectories, constant-power transmission, and designs that ignore the eavesdropper.

## Problem framing

AirComp's superposed signal can be overheard. Moving the fusion center and shaping transmit scalers can keep the legitimate aggregate accurate while degrading the eavesdropper's estimate.

## System model

- Single-antenna sensors, UAV, and EVE with slot-wise channels depending on UAV position.
- Security is measured by the eavesdropper's minimum achievable MSE.

## Method

Alternating optimization across receiver, transmitter, and trajectory blocks, with SCA for the trajectory.

## Key findings

- The joint design with a fly-hover-fly trajectory achieves lower MSE than a straight-line trajectory.
- The design outperforms constant-power and eavesdropper-unaware benchmarks.

## Limitations / future work

The authors suggest multiple UAVs and multi-antenna transceivers as extensions.

## Relation to the corpus

Combines [[over-the-air-computation]] with [[physical-layer-security]] and [[uav-trajectory-control]]; the same group studies hierarchical AirComp power control in [[yao-not-in-parse-hierarchical-airfl-power]].

## Raw artifacts

- Parse: `raw/sources/Joint_Transceiver_and_Trajectory_Design_for_Secure_UAV-Enabled_Over-the-Air_Computation/Joint_Transceiver_and_Trajectory_Design_for_Secure_UAV-Enabled_Over-the-Air_Computation.md`
- Extracted figures are in the same folder; no companion PDF is present.
