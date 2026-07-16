---
type: source
title: "STAR-RIS Enabled Air-Ground Near-Field ISAC"
authors: ["Qiulei Huang", "Zhaohui Song", "Zehui Xiong", "Guanjun Xu", "Nan Zhao", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3602989"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 3260-3271"
modeling_card: required
tags: [source, star-ris, near-field-communications, integrated-sensing-and-communication, uav, beamforming, successive-convex-approximation, semidefinite-relaxation]
related:
  - "[[star-ris]]"
  - "[[semi-passive-star-ris]]"
  - "[[near-field-star-ris-isac]]"
  - "[[radar-mutual-information-rate]]"
  - "[[near-field-communications]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[full-space-star-ris-uav-trajectory]]"
  - "[[zehui-xiong]]"
  - "[[dusit-niyato]]"
  - "[[meng-2026-star-ris-uav-energy]]"
  - "[[chen-2026-pointrl-uav-isac]]"
created: 2026-07-14
updated: 2026-07-16
---

# STAR-RIS Enabled Air-Ground Near-Field ISAC

## Citation

Huang, Q., Song, Z., Xiong, Z., Xu, G., Zhao, N., & Niyato, D. (2026). *STAR-RIS Enabled Air-Ground Near-Field ISAC*. **IEEE Transactions on Wireless Communications, 25**, 3260-3271. DOI: 10.1109/TWC.2025.3602989.

## TL;DR

Jointly optimizes an aerial base station's beamforming, horizontal hovering location, and a large semi-passive STAR-RIS's transmission/reflection coefficients for near-field communication and target sensing. A weighted objective combines indoor and outdoor user rates with radar mutual information rate; block coordinate descent, semidefinite relaxation, and successive convex approximation produce a convergent local alternating method. Simulations show the expected communication-sensing tradeoffs, near-field focusing gains, and modest scenario-specific gains over a transmission-only RIS benchmark.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna UAV serves as a mobile base station for outdoor users on the reflection side and indoor users plus one sensing target on the transmission side of a semi-passive STAR-RIS. Multiuser beamforming supplies communication and sensing signals. Direct UAV-to-outdoor-user and UAV-to-STAR-RIS links use far-field Rician channels, while STAR-RIS-to-user, target, and sensing-array links use spherical-wave near-field channels.

**Problem & objective**: Problem (25) is a coupled nonconvex weighted-sum-rate maximization, $\max \mu_1\sum_k R_{o,k}+\mu_2\sum_l R_{i,l}+\mu_3R_t$, that balances outdoor communication, indoor communication, and radar mutual information rate.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV beamforming | $\mathbf w_{o,k},\mathbf w_{i,l}$ | complex continuous vectors | Precoding for outdoor and indoor users |
| STAR-RIS reflection | $\mathbf\Theta_r$ | complex continuous diagonal matrix | Reflection amplitudes and phases |
| STAR-RIS transmission | $\mathbf\Theta_t$ | complex continuous diagonal matrix | Transmission amplitudes and phases |
| UAV hovering location | $\mathbf q_b$ | continuous 2D position | Horizontal position of the aerial base station |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The UAV maintains the minimum separation from the STAR-RIS plane |
| C2 | Radar mutual information rate meets its sensing threshold |
| C3 | Every indoor and outdoor user satisfies its minimum communication rate |
| C4 | Total UAV transmit power does not exceed $P_{max}$ |
| C5 | Each STAR-RIS element obeys continuous transmission-reflection energy splitting and phase constraints |
| C6 | Location updates stay inside the feasible region and the SCA trust radius |

**Algorithm**: Apply block coordinate descent to separate beamforming, STAR-RIS coefficients, and UAV location, lift beamformers and use SDR plus SCA, convexify the STAR-RIS SINR and MIR bounds with auxiliary variables, update location through trust-region SCA while refreshing small-scale fading, and alternate the three blocks until the weighted sum rate converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] studied STAR-RIS-enabled air-ground near-field integrated sensing and communication with a UAV base station and a semi-passive surface. They formulated a nonconvex weighted-sum-rate maximization over UAV beamforming, STAR-RIS reflection and transmission coefficients, and the UAV hovering location while enforcing communication, sensing, power, geometry, and surface constraints. Their alternating method decomposes the coupled problem into three blocks through block coordinate descent. Semidefinite relaxation and successive convex approximation are used to obtain tractable beamforming, surface, and location updates. Simulations report communication-sensing tradeoffs, near-field focusing behavior, and higher weighted sum rate than the evaluated transmission-only, separated-surface, and random-beamforming designs.

## Problem framing

Conventional RIS serves only one half-space, while large STAR-RIS apertures can support users on both sides but make plane-wave far-field models inaccurate. At the same time, multi-hop STAR-RIS sensing suffers severe path loss. The paper combines a mobile UAV base station, spherical-wave near-field links, and active sensing elements mounted on the STAR-RIS to balance air-ground communication and target sensing.

## System model

- A UAV with an `N_b`-element ULA acts as the mobile base station. It serves outdoor users on the STAR-RIS reflection side and indoor users plus one sensing target on the transmission side.
- A `(2M_x+1) x (2M_z+1)` passive array uses per-element energy splitting to transmit and reflect simultaneously. An `N_s = 2M_x+1` active sensing ULA on the transmission side creates a [[semi-passive-star-ris]] that processes target echoes locally and reduces multi-hop sensing loss.
- UAV-to-outdoor-user direct links and the UAV-to-STAR-RIS link use far-field Rician models. STAR-RIS-to-user, target, and sensor links use element-wise spherical-wave distances and phases.
- The near-field model adds a distance-domain degree of freedom: same-angle terminals can be separated by range, and sensing can recover angle and distance. This is the core of [[near-field-star-ris-isac]].
- Communication uses SINR-based indoor/outdoor rates. Sensing uses [[radar-mutual-information-rate]] from the target echo.

## Method

The objective maximizes

`mu_1 * sum(R_outdoor) + mu_2 * sum(R_indoor) + mu_3 * R_target`,

with nonnegative weights summing to one. Constraints cover a minimum UAV-to-surface-plane separation, target MIR, per-user QoS, total transmit power, and continuous STAR-RIS amplitudes/phases with unit energy splitting.

Block coordinate descent alternates among three variable blocks. The beamforming block lifts vectors to Hermitian matrices, applies first-order SCA to difference-of-concave rates, and uses SDR with eigenvalue recovery. The STAR-RIS block introduces SINR/MIR lower-bound variables, linearizes quadratic-over-linear terms, and relaxes the energy-split equality to an inequality argued to bind at the optimum. The location block freezes small-scale fading during each update, imposes a trust radius, linearizes distance and rate terms, solves the convex approximation with CVX, and then refreshes small-scale fading. The bounded, nondecreasing weighted sum rate establishes convergence of the alternating sequence, not global optimality.

## Key findings

- Lowering the outdoor-user weight moves the UAV toward the STAR-RIS because indoor communication and sensing rely on the surface path. More BS antennas have a similar effect after the outdoor direct links saturate.
- Reflection allocation rises with outdoor-user weight while transmission allocation falls. Simulated average transmission/reflection coefficients sum to one, supporting the active-bound assumption used in the relaxed STAR-RIS subproblem.
- Optimized beams focus on users and the target and favor the higher-weight group. The paper reports stronger indoor near-field focusing because outdoor channels are dominated by far-field Rician direct links.
- Increasing the indoor weight from 0.1 to 0.8 increases indoor sum rate. Larger `N_b` and `M_r` increase weighted sum rate through array gain.
- **Figure-derived (Fig. 9):** at `P_max = 0.5 W`, approximate weighted sum rates are 23.5 for the proposed method, 23.0 for transmission-only RIS, 21.4 for separate half-reflection/half-transmission RISs, and 12.5 bit/s/Hz for random beamforming. At `P_max = 1.2 W`, the corresponding visual readings are about 25.5, 25.3, 23.7, and 14.0 bit/s/Hz. These are plot reads, not prose-stated values.
- The proposed method is highest across the plotted power range, but transmission-only RIS nearly matches it because the illustrated indoor users and target share the transmission side while outdoor users retain strong direct UAV links. The small gap is specific to that geometry and weighting.

## Limitations / future work

Validation is simulation-only and assumes available channel knowledge and exact user/target locations. The design fixes UAV altitude at 100 m and optimizes one horizontal hover point, omitting trajectory, propulsion energy, mobility within a frame, sensing uncertainty, control latency, and flight experiments. The near-/far-field partition depends on the chosen aperture, wavelength, and geometry. The location update freezes small-scale fading within each convex step, so the result is a local approximation dependent on initialization and trust radius.

The optimized STAR-RIS coefficients are continuous. Discrete phase and amplitude degradation are discussed through a nearest-pattern remark, but no hardware-loss benchmark is reported. Power, calibration, coupling, processing load, and cost of the active sensor array are omitted. Complexity grows with 3.5-power terms in antenna, user, and STAR-RIS dimensions; the default `M_r = 1681` is large, yet no wall-clock runtime is provided.

The paper also contains internal notation inconsistencies. Equation (2) and related constraints repeat the reflection phase `theta_r` where one term should apparently be transmission phase `theta_t`. Problem constraint (25f) includes a sensing beam `w_t`, although the transmitted-signal model, variable list, and later beamforming power constraint omit a separately defined sensing beam; later surrogates reintroduce it. Several equations are corrupted in the Markdown parse. Finally, the claim that the relaxed energy-split inequality always binds is supported by empirical observation rather than a formal proof in the parse.

## Relation to the corpus

This paper extends [[star-ris]] and [[integrated-sensing-and-communication]] into a large-aperture, distance-aware air-ground design. Its [[semi-passive-star-ris]] sensors distinguish it from purely passive full-space surfaces, while [[radar-mutual-information-rate]] makes the sensing contribution explicit in the weighted objective. It complements [[meng-2026-star-ris-uav-energy]], which emphasizes STAR-RIS/UAV energy optimization, and [[chen-2026-pointrl-uav-isac]], which uses radar point clouds for UAV control. The connection to [[full-space-star-ris-uav-trajectory]] is neighboring rather than equivalent because this paper keeps the UAV on one side and optimizes a single hover point. Coauthors [[zehui-xiong]] and [[dusit-niyato]] connect it to the corpus's broader aerial-network and ISAC literature.

## Raw artifacts

- `raw/sources/STAR-RIS_Enabled_Air-Ground_Near-Field_ISAC/STAR-RIS_Enabled_Air-Ground_Near-Field_ISAC.md`
- `raw/sources/STAR-RIS_Enabled_Air-Ground_Near-Field_ISAC/STAR-RIS_Enabled_Air-Ground_Near-Field_ISAC.pdf`
- Extracted figures in `raw/sources/STAR-RIS_Enabled_Air-Ground_Near-Field_ISAC/images/`.

## Metadata notes

The Markdown parse supplies the title and author order but omits the final journal header. Volume, pages, DOI, and 2026 issue metadata are taken from the embedded first-page PDF header. The article was published online in September 2025, with a December 2025 current-version date; an earlier WCSP 2024 version has a different DOI and is not the journal citation used here.
