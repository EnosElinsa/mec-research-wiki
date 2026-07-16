---
type: source
modeling_card: required
title: "Situation-Aware Hybrid Sensing and Position Control for UAV-Assisted ISAC Systems"
authors: ["Ling Lyu", "Qirui Luo", "Yanpeng Dai", "Nan Cheng", "Cailian Chen", "Xinping Guan", "Xuemin Shen"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3661956"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 12197-12213"
tags: [source, integrated-sensing-and-communication, uav-relay, event-triggered-sensing, beam-alignment, position-control, energy-efficiency, fractional-programming]
related:
  - "[[situation-aware-hybrid-isac-sensing]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[li-2026-control-based-uav-isac]]"
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[meng-2026-uav-isac-corrections]]"
  - "[[lu-2026-icsn-beamforming]]"
  - "[[ling-lyu]]"
  - "[[yanpeng-dai]]"
  - "[[nan-cheng]]"
  - "[[xuemin-shen]]"
created: 2026-07-14
updated: 2026-07-16
---

# Situation-Aware Hybrid Sensing and Position Control for UAV-Assisted ISAC Systems

## Citation

Lyu, L., Luo, Q., Dai, Y., Cheng, N., Chen, C., Guan, X., & Shen, X. (2026). *Situation-Aware Hybrid Sensing and Position Control for UAV-Assisted ISAC Systems*. **IEEE Transactions on Wireless Communications, 25**, 12197-12213. DOI: 10.1109/TWC.2026.3661956.

## TL;DR

Coordinates sensing, transmit power, beam alignment, and UAV position control for a half-duplex industrial relay. The remote center senses periodically while receiving AGV data, then triggers sensing from a communication-rate threshold while receiving relayed data; in either phase, the controller reserves propulsion-expensive position correction for severe beam misalignment and otherwise adjusts only the UAV antenna angle.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An automatic guided vehicle sends industrial sensory data to a remote center through one half-duplex decode-and-forward UAV. An orthogonal two-phase relay frame carries the AGV-to-UAV hop and then the UAV-to-center hop; LoS-dominant flat-fading links include free-space path loss and directional-beam misalignment, while the center performs periodic or event-triggered sensing and the UAV applies antenna-angle or position control.

**Problem & objective**: Problem $\mathcal P_0$, a mixed-integer nonlinear fractional program, maximizes end-to-end energy efficiency, $\max D^{\mathrm{end}}/P^{\mathrm{tot}}$ with $D^{\mathrm{end}}=\min\{D_{\mathrm I},D_{\mathrm{II}}\}$, over communication power, sensing beamforming, and the phase division point.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AGV transmit power | $P_{c,k}$ | continuous, nonnegative and power-bounded | Communication power in Phase I |
| UAV transmit power | $P_{u,k}$ | continuous, nonnegative and power-bounded | Relay communication power in Phase II |
| Phase-I sensing beamformer | $\mathbf w_{m,k}$ | complex continuous vector | Remote-center beam for sensing the AGV and UAV |
| Phase-II sensing beamformer | $\mathbf v_k$ | complex continuous vector | Remote-center beam for sensing the UAV |
| Phase division point | $k_{\mathrm{th}}$ | integer slot index | Separates AGV transmission from UAV forwarding |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Phase-I and Phase-II sensing beampattern errors satisfy the prescribed sensing-accuracy limits |
| C3-C4 | Sensing-beam transmit powers do not exceed the remote-center budget $P_l$ |
| C5 | Phase-I sensing interference satisfies the stated cancellation condition |
| C6 | UAV communication power obeys its maximum transmit-power limit |
| C7 | Phase-II forwarded data does not exceed the data available from Phase I |
| C8-C9 | $k_{\mathrm{th}}$ is an integer slot and the sensing/control activation factors are binary |

**Algorithm**: Decompose $\mathcal P_0$ by relay phase → solve Phase I with golden-section Dinkelbach iterations and penalty-based SCA for rank-one beamforming → enumerate the finite phase division points → solve Phase II with a quadratic transform and rank-one reconstruction → retain the best feasible energy-efficiency value.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lyu et al. [x] studied situation-aware sensing and position control for an industrial UAV-assisted integrated sensing and communication relay. They formulated a mixed-integer nonlinear problem that maximizes end-to-end energy efficiency by jointly optimizing AGV and UAV transmit powers, remote-center sensing beamformers, and the phase division point. Their hybrid pattern activates Phase-II sensing from a communication-rate condition and selects antenna-angle control or combined position and angle control from the sensed beam overlap. The solution decomposes the two relay phases, applies golden-section Dinkelbach and penalty-based successive convex approximation in Phase I, and uses a quadratic transform with rank-one reconstruction in Phase II. Simulations report data-volume gains of 15.33%, 17.64%, 34.43%, and 59.48% over the evaluated PAAC-5, PAAC-10, ETMC, and No-control schemes at the stated 20 m horizontal distance, together with fewer sensing activations than the fixed-period schemes.

## Problem

An automatic guided vehicle (AGV) sends industrial sensory data through a decode-and-forward UAV to a remote center (RC). Position uncertainty can misalign the directional AGV and UAV antennas, reducing relay throughput, but frequent sensing and UAV repositioning consume sensing-transmit and propulsion energy. The paper seeks high end-to-end energy efficiency by adapting when the RC senses and whether misalignment should be corrected by antenna rotation alone or by combined antenna and position control.

## System model

- A 100-slot frame is divided at integer slot `k_th`. In Phase I, the AGV transmits to the UAV while the RC periodically senses both platforms. In Phase II, the UAV forwards to the RC, which senses only the UAV and uses an omnidirectional communication antenna.
- The relay is half-duplex decode-and-forward, so delivered data is limited by the smaller data volume across the two phases. Communication links are LoS-dominant flat-fading links with free-space path loss and antenna-misalignment loss; multipath fading is neglected.
- The RC uses a sensing ULA and communication antenna. Phase I forms a dual-main-lobe sensing beampattern for the AGV and UAV, whereas Phase II forms a single-target UAV beampattern.
- UAV position and antenna pitch follow separate linear discrete-time control models. The model holds azimuth fixed and neglects horizontal disturbances in angle control. Position correction incurs rotary-wing propulsion power.
- Energy efficiency is delivered end-to-end data volume divided by total frame power, including AGV/UAV communication, active RC sensing, and UAV propulsion when position control is selected.

## Method

The original mixed-integer nonlinear program jointly selects Phase-I AGV power, Phase-II UAV power, RC sensing beamformers, and `k_th`. Sensing and control indicators are generated by the prescribed trigger and mode-selection rules rather than presented as independent policy variables. Constraints cover sensing beampattern accuracy, RC sensing and UAV transmit-power budgets, sensing-interference cancellation, phase data balance, binary activations, and positive-semidefinite rank-one beamforming matrices.

[[situation-aware-hybrid-isac-sensing]] combines phase-dependent schedules. Phase I always senses both targets. If horn-beam displacement exceeds the beam radius, the UAV uses position plus antenna-angle control; otherwise it uses angle control alone. In Phase II, the RC propagates a state estimate while sensing is inactive and triggers a new observation when the UAV-to-RC rate falls below a model-derived threshold. Zero projected beam overlap invokes position plus angle control, while partial overlap invokes angle-only correction.

The solver decomposes the two relay phases. For Phase I, a golden-section/Dinkelbach outer procedure handles the rate-to-power ratio, while semidefinite lifting, a shrinking rank penalty, and SCA produce QSDPs solved with CVX/MOSEK. This layer yields an overall suboptimal solution. For Phase II, a finite search over `k_th` is combined with a Shen-Yu quadratic transform; inactive-sensing slots require only convex power allocation, while active slots also optimize a lifted beamformer. The paper constructs a globally optimal rank-one solution for the stated Phase-II beamforming subproblem, but this guarantee does not extend to the original MINLP.

## Key findings

- The delivered-data sweep peaks at `k_th=39`, which the remaining experiments use.
- At horizontal AGV-UAV distance `20 m`, the proposed method reports data-volume gains of `15.33%`, `17.64%`, `34.43%`, and `59.48%` over source-defined PAAC-5, PAAC-10, ETMC, and No-control comparators, respectively.
- Energy efficiency rises and then plateaus with UAV power because Phase I eventually becomes the relay bottleneck. The proposed event-triggered design uses fewer sensing activations than the fixed-period PAAC comparators.
- Algorithm 1's interval is nearly closed after about 10 outer iterations. The paper reports convergence for the penalty-SCA and Phase-II procedures but gives inconsistent statements about whether initialization can change the final value.
- Among tested activation probabilities `0.4` through `0.8`, the reported best energy/transmission balance occurs at `0.6`. This is a discrete simulation result, not a general optimum.
- Higher UAV altitude reduces both delivered data and energy efficiency. Beampattern plots qualitatively show two target lobes in Phase I, one in Phase II, and low leakage in undesired directions.

## Limitations

The evaluation is simulation-only, with one AGV, one UAV relay, and one RC. It omits flight and radio experiments, multi-UAV or multi-AGV scheduling, queues, retransmissions, packet loss, latency, finite battery constraints, and control-link overhead. Channels exclude multipath, blockage dynamics, Doppler, hardware impairments, and estimation error. The AGV route and speed are fixed, and the trigger is not tested under sensing delay, missed observations, estimator mismatch, or feedback error.

Several source details require caution. The parsed `P0` display is unusable, two model equations contain possible notation or dimensional errors, and simulation prose sometimes calls the RC an AP. The text and Fig. 12(b) use inconsistent AGV-UAV distance sets, while the activation-probability discussion gives conflicting verbal trends. The overall algorithm is described as suboptimal despite a global rank-one-recovery result for one Phase-II subproblem.

## Relation to the corpus

This paper extends [[integrated-sensing-and-communication]] with a deterministic, phase-aware trigger and [[control-assisted-uav-beam-tracking]]. [[li-2026-control-based-uav-isac]] models richer flight dynamics and trajectory feasibility, while this source emphasizes switching between angle-only and position-plus-angle correction. [[wu-2026-sensing-error-uav-scheduling]] learns multi-UAV schedules under localization error, and [[meng-2026-uav-isac-corrections]] studies periodic sensing and phase/resource allocation. Its optimization stack also connects the sensing-control design to [[fractional-programming-dinkelbach]] and [[rotary-wing-propulsion-energy-model]]. Confirmed recurring authors include [[ling-lyu]], [[yanpeng-dai]], [[nan-cheng]], and [[xuemin-shen]].

## Raw artifacts

- Parse: `raw/sources/Situation-Aware_Hybrid_Sensing_and_Position_Control_for_UAV-Assisted_ISAC_Systems/Situation-Aware_Hybrid_Sensing_and_Position_Control_for_UAV-Assisted_ISAC_Systems.md`
- Origin PDF: `raw/sources/Situation-Aware_Hybrid_Sensing_and_Position_Control_for_UAV-Assisted_ISAC_Systems/Situation-Aware_Hybrid_Sensing_and_Position_Control_for_UAV-Assisted_ISAC_Systems.pdf`
- Figures: `raw/sources/Situation-Aware_Hybrid_Sensing_and_Position_Control_for_UAV-Assisted_ISAC_Systems/images/`
