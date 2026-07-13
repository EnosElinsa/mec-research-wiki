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
  - "[[jie-xu]]"
  - "[[cheng-zhan]]"
  - "[[kaifeng-song]]"
  - "[[rongfei-fan]]"
  - "[[han-hu]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Enabled Aerial Monitoring Aided by STAR-RIS: A Stochastic Optimization Framework

## Citation

Zhan, C., Hu, L., Song, K., Fan, R., Hu, H., & Xu, J. (2026). *UAV-Enabled Aerial Monitoring Aided by STAR-RIS: A Stochastic Optimization Framework*. **IEEE Transactions on Wireless Communications, 25**, 8769-8783. DOI: 10.1109/TWC.2025.3645801.

## TL;DR

Controls a monitoring UAV's trajectory, active beamforming, and a building-mounted STAR-RIS to maximize long-term average sum throughput under a propulsion-energy budget and stochastic target motion. A virtual energy queue converts the long-horizon problem into per-slot control, while WMMSE/PDD and sequential convex approximation handle the coupled communication and trajectory blocks.

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

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework.md`
- Origin PDF: `raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework.pdf`
- Figures: `raw/sources/UAV-Enabled_Aerial_Monitoring_Aided_by_STAR-RIS_A_Stochastic_Optimization_Framework/images/`
