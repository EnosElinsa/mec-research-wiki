---
type: source
modeling_card: required
title: "Digital-Twin-Empowered Cluster Formation via Over-the-Air Computation in UAV Swarm Networks"
authors: ["Lu Zhang", "Xuan Li", "Yuhang Zhang", "Yansong Huang", "Haiyan Li", "Zixuan Zhang", "Mugen Peng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3646641"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, digital-twin, aircomp, uav-swarm, cluster-formation, energy-efficiency, bcd]
related:
  - "[[aircomp-aware-uav-device-cluster-formation]]"
  - "[[digital-twin]]"
  - "[[over-the-air-computation]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-12
updated: 2026-07-16
---

# Digital-Twin-Empowered Cluster Formation via Over-the-Air Computation in UAV Swarm Networks

## Citation

Zhang, L., Li, X., Zhang, Y., Huang, Y., Li, H., Zhang, Z., & Peng, M. (2026). *Digital-Twin-Empowered Cluster Formation via Over-the-Air Computation in UAV Swarm Networks*. **IEEE Transactions on Wireless Communications**, 25, 9940-9954. DOI: 10.1109/TWC.2025.3646641.

## TL;DR

Uses a digital-twin control loop to jointly form UAV-to-IoE-device-group clusters, coordinate AirComp receiver scaling and device power, and plan collision-safe UAV trajectories. A four-block BCD solver maximizes aggregated data per UAV-plus-twin energy under AirComp distortion constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-altitude UAVs form time-varying one-to-one service clusters with groups of IoE devices. Devices in a selected group transmit simultaneously through AirComp, while a digital-twin layer periodically updates formation, receiver scaling, device power, and collision-safe UAV trajectories.

**Problem & objective**: The MINLP fractional program maximizes aggregated-data energy efficiency, $\max_{\mathbf Q,\mathbf A,\mathbf P,\boldsymbol\eta}\frac{\sum_{n,l,m}a_{l,m}[n]R_{l,m}[n]}{\sum_{m,n}P_U^m[n]+\phi_p}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV-group formation | $a_{l,m}[n]$ | binary, $\{0,1\}$ | Whether UAV $m$ aggregates group $l$ in slot $n$ |
| Device power | $P_{k,l}[n]$ | continuous, $[0,P_{\max}]$ | AirComp transmit power of device $k$ in group $l$ |
| AirComp scale factor | $\eta_{l,m}[n]$ | continuous, positive | Receive normalization applied by UAV $m$ |
| UAV trajectory | $\mathbf q_m[n]$ | continuous position | Horizontal location of UAV $m$ in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The associated AirComp distortion satisfies $\sum_m a_{l,m}[n]\mathrm{mse}_{l,m,n}\leq\epsilon_l$. |
| C2 | Scale and power satisfy $\eta_{l,m}[n]>0$ and $0\leq P_{k,l}[n]\leq P_{\max}$. |
| C3 | UAV displacement satisfies $\lVert\mathbf q_m[n]-\mathbf q_m[n-1]\rVert\leq V_{\max}\delta_t$. |
| C4 | UAV separation satisfies $\lVert\mathbf q_m[n]-\mathbf q_i[n]\rVert^2\geq d_{\min}^2$. |
| C5 | Each group has at most one UAV and each UAV serves at most one group per slot. |

**Algorithm**: Apply BCD across four blocks: relax and greedily recover binary UAV-device formation, update AirComp scale factors with Dinkelbach fractional programming, update device powers with a square-root substitution and Dinkelbach iteration, and optimize trajectories through SCA with an inner Dinkelbach loop until the global objective stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied digital-twin-empowered UAV-device cluster formation with AirComp for energy-efficient IoE data aggregation. They formulated a mixed-integer nonlinear fractional program that jointly selects binary UAV-group associations, device powers, AirComp receiver scale factors, and UAV trajectories to maximize aggregated-data energy efficiency under distortion, power, speed, collision-separation, and one-to-one formation constraints. Their global iterative optimization decomposes the problem into relaxed formation, Dinkelbach-based AirComp-factor coordination, Dinkelbach-based device-power allocation, and SCA-Dinkelbach trajectory blocks. Simulations report up to 42% higher energy efficiency and 34% higher throughput than the corresponding pre-set AirComp baseline.

## Problem

UAV swarms can aggregate measurements from groups of IoE devices through over-the-air superposition, but mobility, group assignment, coherent-signal distortion, device power, propulsion, and digital-twin update overhead are coupled. The resulting mixed-integer nonlinear fractional program must preserve aggregation quality while avoiding collisions and limiting energy use.

## System model

- Multiple fixed-altitude UAVs serve disjoint IoE device groups over time slots while a digital-twin layer receives delayed physical state and returns optimized policies.
- Devices in one selected group transmit simultaneously; the serving UAV computes an arithmetic average from their superposed signals.
- AirComp MSE includes signal misalignment, inter-cluster interference, and noise. Each selected group must stay below its distortion threshold.
- Binary association permits at most one serving UAV per group and at most one group per UAV in a slot.
- UAV energy follows a rotary-wing speed-dependent propulsion model. Digital-twin overhead grows with swarm/device scale and update frequency.
- Energy efficiency divides total aggregated transmission data by UAV propulsion energy plus twin-update overhead.

## Method

The GIO-BCD solver cycles through four blocks. UDCF-RLP relaxes binary UAV-group assignments and greedily recovers a feasible formation. FPO-ACSF applies [[fractional-programming-dinkelbach|Dinkelbach iteration]] to AirComp receiver scale factors. DB-DPA substitutes the square root of device power and solves another fractional program. SDB-USTD uses SCA/Taylor bounds plus an inner Dinkelbach loop for rate-to-propulsion trajectory design under movement, collision, and MSE constraints.

The objective sequence is argued to be non-decreasing and bounded. This establishes convergence of generated objective values, not global optimality for the original mixed-integer problem; assignment recovery and SCA remain approximation steps.

## Key findings

- At high device-power levels in the three-UAV setting, AirComp cluster formation reaches up to `6x` the throughput of orthogonal-transmission cluster formation.
- As device density varies, the proposed method reaches up to `6.2x` the energy efficiency of the orthogonal-transmission baseline.
- Against static pre-set AirComp, DT-CF-AirComp is reported about `42%` higher in energy efficiency and `34%` higher in throughput.
- DT-CF-OT is reported about `44%` higher in energy efficiency and `245%` higher in throughput than pre-set orthogonal transmission.
- The stated `10-15` global iterations and “few seconds” per cycle are algorithmic feasibility assertions; no processor or measured runtime trace is supplied.

## Limitations / parse caveats

Evaluation is simulation-only. The model assumes fixed altitude and device positions, LoS-dominant reciprocal channels, coherent transmission, perfect synchronization and Doppler compensation, independent normalized device signals, and straight-line motion inside each slot. Twin uncertainty is represented mainly through delayed state and update overhead rather than an explicit estimation-error constraint. The parse contains damaged set/time notation, shifted constraint labels, a missing equation body, and a table label inconsistent with the system definition. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[aircomp-aware-uav-device-cluster-formation]] connects [[digital-twin]] synchronization to physical-layer [[over-the-air-computation]] and swarm mobility. It complements [[huang-2026-aircomp-uav-swarms-afl]], which aggregates learning updates under staleness, by optimizing IoE measurement aggregation and UAV propulsion energy with classical BCD/SCA rather than reinforcement learning.

## Raw artifacts

- Parse: `raw/sources/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks.md`
- Origin PDF: `raw/sources/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks.pdf`
- Figures: `raw/sources/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks/images/`
