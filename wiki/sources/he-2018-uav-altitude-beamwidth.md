---
type: source
title: "Joint Altitude and Beamwidth Optimization for UAV-Enabled Multiuser Communications"
authors: ["Haiyun He", "Shuowen Zhang", "Yong Zeng", "Rui Zhang"]
year: 2018
url: "https://doi.org/10.1109/LCOMM.2017.2772254"
venue: "IEEE Communications Letters (IEEE LCOMM)"
modeling_card: required
tags: [source, uav-base-station, altitude-optimization, beamwidth-optimization, drone-cell-3d-placement, air-to-ground-channel-model]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[mozaffari-2016-efficient-multi-uav-coverage]]"
  - "[[yong-zeng]]"
created: 2026-06-04
updated: 2026-07-16
---

# Joint Altitude and Beamwidth Optimization for UAV-Enabled Multiuser Communications

## Citation

He, H., Zhang, S., Zeng, Y., & Zhang, R. (2018). *Joint Altitude and Beamwidth Optimization for UAV-Enabled Multiuser Communications*. **IEEE Communications Letters**, 22(2). DOI: 10.1109/LCOMM.2017.2772254. (Received 9 September 2017; accepted 6 November 2017; published 10 November 2017; current version 9 February 2018.)

## TL;DR

Studies a UAV equipped with a **directional antenna of adjustable beamwidth** flying above a large area with K uniformly distributed ground terminals (GTs). Proposes a **fly-hover-and-communicate** protocol where GTs are partitioned into hexagonal clusters; the UAV hovers above each cluster center and serves all GTs in that cluster. Jointly optimizes the UAV's altitude H and antenna beamwidth Θ to maximize throughput across three multiuser models: **downlink multicasting (MC), downlink broadcasting (BC), and uplink multiple access (MAC)**. Shows the optimal (H, Θ) pair critically depends on the communication model — not a single universal setting.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV with a tunable directional antenna serves uniformly distributed ground terminals by flying among hexagonal cluster centers and hovering to communicate. The rural air-to-ground channel is pure LoS with inverse-square path gain; downlink broadcasting and uplink multiple access use equal-bandwidth FDMA, while downlink multicasting sends one common message.

**Problem & objective**: Joint altitude and half-beamwidth design minimizes multicast completion time through $\max_{H,\Theta}\widetilde R_{\mathrm{MC}}(H,\Theta)$ and maximizes $\widetilde R_{\mathrm{BC}}(H,\Theta)$ or $\widetilde R_{\mathrm{MAC}}(H,\Theta)$ for the two independent-message models.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV altitude | $H$ | continuous, $H_{\min}\leq H\leq H_{\max}$ | Hovering altitude shared across all served clusters |
| Antenna half-beamwidth | $\Theta$ | continuous, $\Theta_{\min}\leq\Theta\leq\Theta_{\max}<\pi/2$ | Tunable azimuth and elevation half-power beamwidth |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Altitude range | $H$ remains within obstacle- and regulation-defined limits $[H_{\min},H_{\max}]$ |
| Beamwidth range | The antenna supports only $\Theta\in[\Theta_{\min},\Theta_{\max}]$ |
| Main-lobe coverage | The ground coverage radius and cell size obey $\bar r=H\tan\Theta$ and $A_s=3\sqrt3\,\bar r^2/2$ |
| Service protocol | Every cluster is visited and its terminals receive the model-specific common or independent data |

**Algorithm**: Substitute the directional gain, LoS pathloss, terminal density, and coverage radius into the three rate expressions; use monotonic analysis to set $H_{\mathrm{MC}}^*=H_{\max}$ and $H_{\mathrm{BC}}^*=H_{\min}$ and to show that MAC throughput is altitude-independent; then perform a one-dimensional search over the feasible beamwidth for each communication model.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

He et al. [x] studied joint UAV altitude and directional-antenna beamwidth design for fly-hover-and-communicate multiuser service. They derived separate throughput objectives for downlink multicasting, FDMA downlink broadcasting, and FDMA uplink multiple access under LoS propagation and bounded altitude and beamwidth. Their analysis sets the multicast altitude to its maximum, the broadcast altitude to its minimum, shows altitude independence for the uplink model, and obtains the remaining beamwidth by one-dimensional search. Numerical results matched the analytical broadcasting and uplink rates and reported an uplink-optimal half-beamwidth of approximately 1.3195 radians when feasible.

## Problem framing

Prior UAV communication work assumes omnidirectional or fixed-beamwidth antennas. With a tunable-beamwidth directional antenna, two design freedoms are available simultaneously: (i) altitude (more altitude → larger LoS coverage area but higher path loss); (ii) beamwidth (wider beam → more GTs in main lobe but lower per-GT antenna gain). The altitude–beamwidth tradeoff differs fundamentally depending on whether the UAV multicasts common data, broadcasts independent data via FDMA, or receives uplink FDMA transmissions.

## System model

- **UAV** at altitude H with a directional antenna (equal azimuth/elevation half-power beamwidth 2Θ). Coverage radius r̄ = H·tan(Θ).
- **GTs:** K uniformly distributed in a large area A (density ρ = K/A), each equipped with an omnidirectional antenna.
- **Channel:** pure LoS (rural area assumed); channel power gain h(r) = β₀/(H² + r²).
- **Hexagonal tessellation:** area partitioned into N hexagonal cells (each with circumradius r̄); UAV hovers above each cluster center to serve its GTs.
- **Three models:**
  - **MC:** single common message to all GTs in cluster; throughput = rate achievable at the worst GT (min-rate MC).
  - **BC:** independent messages per GT via FDMA; total throughput = sum of per-GT rates.
  - **MAC:** each GT sends independent message via FDMA uplink; total throughput = sum of per-GT rates.

## Key findings

- Optimal altitude and beamwidth **differ significantly across the three communication models** (MC vs BC vs MAC), because the signal-power vs. coverage-area tradeoff manifests differently for each model (parse abstract + simulations).
- For multicasting, a narrower beam and higher altitude (focusing power on a single high-gain GT in the cluster center) can outperform wide-beam coverage depending on density and cluster structure.
- For broadcasting/MAC, a wider beam and lower altitude (covering more GTs per cluster visit, maximizing frequency reuse) tends to be optimal.
- The fly-hover-and-communicate protocol achieves practical system operation while enabling tractable joint optimization.

## Limitations / future work

Assumes pure LoS (no LoS probability model) and omnidirectional GTs. The hexagonal cell partition is fixed; dynamic cluster sizes are not explored. UAV trajectory between cluster centers is not optimized (fly-time overhead is treated as overhead, not co-optimized).

## Relation to the corpus

From the Zeng/Zhang group (NUS) — same authors as [[zeng-2019-uav-comm-tutorial-5g]] and [[zhan-2018-uav-wsn-data-collection]]. Extends the [[drone-cell-3d-placement]] line ([[al-hourani-2014-optimal-lap-altitude]], [[mozaffari-2016-efficient-multi-uav-coverage]]) by introducing the **beamwidth** degree of freedom and multi-model throughput analysis. The communication-model-dependent optimal altitude finding distinguishes this from the purely coverage-focused prior work.

## Raw artifacts

- `raw/sources/Joint_Altitude_and_Beamwidth_Optimization_for_UAV-Enabled_Multiuser_Communications/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
