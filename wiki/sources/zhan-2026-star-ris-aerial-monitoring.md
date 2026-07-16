---
type: source
title: "UAV-Enabled Aerial Monitoring Aided by STAR-RIS: A Stochastic Optimization Framework"
authors: ["Cheng Zhan", "Lu Hu", "Kaifeng Song", "Rongfei Fan", "Han Hu", "Jie Xu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3645801"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 8769-8783"
tags: [source, star-ris, aerial-monitoring, stochastic-optimization, lyapunov-optimization, uav-trajectory, beamforming]
related:
  - "[[star-ris]]"
  - "[[lyapunov-optimization]]"
  - "[[penalty-dual-decomposition]]"
  - "[[weighted-minimum-mean-square-error]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[wireless-information-surveillance]]"
  - "[[yan-2026-uav-trajectory-monitoring]]"
  - "[[uav-trajectory-monitoring]]"
  - "[[fully-connected-ris]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
  - "[[jie-xu]]"
  - "[[cheng-zhan]]"
  - "[[kaifeng-song]]"
  - "[[rongfei-fan]]"
  - "[[han-hu]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# UAV-Enabled Aerial Monitoring Aided by STAR-RIS: A Stochastic Optimization Framework

## Citation

Zhan, C., Hu, L., Song, K., Fan, R., Hu, H., & Xu, J. (2026). *UAV-Enabled Aerial Monitoring Aided by STAR-RIS: A Stochastic Optimization Framework*. **IEEE Transactions on Wireless Communications, 25**, 8769-8783. DOI: 10.1109/TWC.2025.3645801.

## TL;DR

Controls a monitoring UAV's trajectory, active beamforming, and a building-mounted STAR-RIS to maximize long-term average sum throughput under a propulsion-energy budget and stochastic target motion. A virtual energy queue converts the long-horizon problem into per-slot control, while WMMSE/PDD and sequential convex approximation handle the coupled communication and trajectory blocks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude multi-antenna UAV monitors moving targets with panoramic cameras and broadcasts processed video to indoor and outdoor single-antenna users through a passive energy-splitting STAR-RIS. Users share the downlink through multiuser beamforming, target motion follows a Gauss-Markov model, and the modeled UAV-to-user channels are cascaded through the STAR-RIS with reliable CSI.

**Problem & objective**: Multi-stage stochastic problem (P1) maximizes long-term average sum throughput, $\max\lim_{L\to\infty}L^{-1}\sum_{l=1}^{L}\sum_{k=1}^{K}R_k[l]$, subject to monitoring, mobility, hardware, transmit-power, and average propulsion-energy constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf{q}_v[l]$ | continuous, planar position | Monitoring UAV position in slot $l$ |
| Active beamformer | $\mathbf{w}_k[l]$ | complex continuous | UAV transmit beam for user $k$ |
| STAR-RIS amplitudes | $\beta_{t,n}[l],\beta_{r,n}[l]$ | continuous, $[0,1]$ | Transmission and reflection amplitudes of element $n$ |
| STAR-RIS phases | $\phi_{t,n}[l],\phi_{r,n}[l]$ | continuous, $[0,2\pi)$ | Transmission and reflection phase shifts of element $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 10 | UAV transmit power is bounded, $\operatorname{Tr}(\mathbf{W}[l]\mathbf{W}^{\mathrm H}[l])\leq p^{\max}$ |
| 11 | Per-slot displacement obeys $\|\mathbf{q}_v[l+1]-\mathbf{q}_v[l]\|\leq v_{\mathrm{uav}}^{\max}\delta$ |
| 12 | The UAV remains within the monitoring radius, $\|\mathbf{q}_v[l]-\bar{\mathbf{q}}_u[l]\|\leq d^{\max}$ |
| 13 | Long-term average propulsion energy satisfies $\bar E^{\mathrm{fl}}\leq\bar E_{\max}^{\mathrm{fl}}$ |
| 14 | Element amplitudes satisfy $\beta_{t,n}^2[l]+\beta_{r,n}^2[l]=1$ |
| 15 | Coupled phases satisfy $\cos(\phi_{t,n}[l]-\phi_{r,n}[l])=0$ |

**Algorithm**: Lyapunov optimization creates a virtual propulsion-energy queue and converts (P1) into per-slot problem (P2); WMMSE and penalty dual decomposition update active beamforming and STAR-RIS coefficients; sequential parametric convex approximation updates the UAV trajectory; alternating optimization completes the slot before the virtual queue is advanced.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhan et al. [x] studied STAR-RIS-aided UAV-enabled aerial monitoring in which one UAV tracks moving targets and broadcasts monitored information to indoor and outdoor users. They formulated a multi-stage stochastic optimization problem that maximizes long-term average throughput by jointly optimizing transmit beamforming, UAV trajectory, and STAR-RIS configuration under monitoring and energy constraints. A Lyapunov-based online framework introduces a virtual energy queue and transforms the long-horizon problem into deterministic per-slot subproblems. The resource block is solved with weighted minimum mean-square error and penalty dual decomposition, while sequential parametric convex approximation handles the trajectory block. Simulations report convergence within approximately ten iterations for five STAR-RIS elements and throughput gains of 18.98% and 23.77% over geometric-center tracking at 80 and 120 elements, respectively.

## Problem framing

A UAV records randomly moving targets, processes panoramic video into VR content, and broadcasts it to indoor and outdoor users through a STAR-RIS. Target motion changes the monitoring geometry, cascaded channels, and propulsion cost over time. The paper therefore maximizes long-term average sum throughput while constraining the UAV's monitoring distance, mobility, transmit power, STAR-RIS coefficients, and average propulsion energy.

## System model

- One fixed-altitude UAV carries an antenna array and panoramic cameras; target speed and direction follow a [[gauss-markov-mobility-model]].
- Single-antenna users occupy the transmission and reflection sides of one passive, lossless STAR-RIS operating in energy-splitting mode. The modeled UAV-user links are cascaded through the STAR-RIS, with reliable CSI assumed.
- The UAV must remain within a prescribed distance of the moving targets' geometric center. Its per-slot displacement and transmit power are bounded.
- Each STAR-RIS element has coupled transmission/reflection amplitudes whose squared values sum to one, and the two phases differ by one of the modeled quadrature values.
- A rotary-wing flight-power model supplies propulsion energy. Communication and computation energy are omitted, and VR preprocessing/rendering is outside the optimization.

## Method

The [[lyapunov-optimization|Lyapunov]] layer introduces a virtual queue for the average propulsion-energy constraint and minimizes a per-slot drift-plus-penalty upper bound. For a fixed trajectory, sum-rate optimization is recast through [[weighted-minimum-mean-square-error|WMMSE]]. Duplicated STAR-RIS variables isolate the hardware coupling, and [[penalty-dual-decomposition|PDD]] with block-coordinate updates handles active beamforming and STAR-RIS coefficients.

For fixed active and passive beamforming, the trajectory block uses slack variables and first-order convex bounds for propulsion and rate terms. This sequential parametric convex approximation is solved iteratively, and the two blocks alternate as an [[alternating-optimization-sdr-sca|AO/SCA]] procedure before the virtual queue is updated for the next slot.

## Guarantee scope

Queue stability is stated to imply satisfaction of the long-term average energy constraint; the implication is conditional on stability. The drift theorem supplies a finite per-slot upper bound but does not prove global optimality. The paper characterizes the PDD block as converging to a KKT/stationary solution as equality residuals vanish. No parse-visible theorem establishes global optimality for the complete per-slot alternating method or the original stochastic problem; its convergence plots are empirical.

## Key findings

- In the reported simulation at 0.1 W transmit power, the five-element STAR-RIS case converges in approximately ten iterations; larger tested surfaces take more iterations but attain higher throughput.
- The optimized transmission/reflection phase differences converge to the quadrature values required by the modeled STAR-RIS constraint.
- The prose reports average UAV speeds of 7.91 m/s for the proposed method and 10.03 m/s for the random-STAR-RIS baseline in the plotted scenario.
- With eight UAV antennas and 0.1 W transmit power, the reported throughput improvements over the GCO baseline are approximately 18.98% at 80 STAR-RIS elements and 23.77% at 120 elements. These percentages are simulation-specific.
- The proposed method outperforms the tested GCO, fixed-active-beamforming, reflecting/transmitting partition, and random-configuration baselines in the reported sweeps. Absolute values not stated in the prose are not inferred from figures.

## Limitations

The study assumes reliable CSI, fixed UAV altitude, known Gauss-Markov target dynamics, a passive lossless STAR-RIS, and constant within-slot positions. It models only cascaded STAR-RIS communication and propulsion energy, and reduces panoramic coverage to distance from the targets' geometric center. Hardware loss, phase quantization, CSI acquisition overhead, direct links, motion-model mismatch, and the adequacy of the geometric-center proxy are not experimentally evaluated. Evidence comes from one synthetic urban geometry and its benchmark set.

## Relation to the corpus

This source connects [[star-ris]] with online [[uav-trajectory-control]] under a long-term energy constraint. Its communication block combines [[weighted-minimum-mean-square-error]] and [[penalty-dual-decomposition]], while its trajectory block occupies the SCA branch of [[alternating-optimization-sdr-sca]] rather than using SDR. The stochastic control layer complements other UAV/RIS optimization pages by coupling target monitoring geometry to a virtual propulsion-energy queue.

Here monitoring means panoramic-camera capture plus video delivery. [[lin-2026-fc-ris-surveillance]] and [[wireless-information-surveillance]] instead concern authorized decoding of suspicious radio content, while [[yan-2026-uav-trajectory-monitoring]] and [[uav-trajectory-monitoring]] estimate and maintain non-cooperative target tracks from echoes. The ideal non-diagonal [[fully-connected-ris]] used by Lin is also architecturally distinct from this paper's transmitting/reflecting surface. See [[aerial-observation-control-covertness-surveillance-and-monitoring]].

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework.md`
- Origin PDF: `raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework.pdf`
- Figures: `raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/images/`
