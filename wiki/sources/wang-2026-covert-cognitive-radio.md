---
type: source
modeling_card: required
title: "UAV-Assisted Covert Transmission for Cooperative Cognitive Radio Networks"
authors: ["Qunshu Wang", "Chengwen Xing", "Nan Zhao", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3591810"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 1594-1608"
tags: [source, covert-communication, finite-blocklength, cooperative-cognitive-radio, primary-signal-assisted-covertness, uav-trajectory]
related:
  - "[[covert-communication]]"
  - "[[finite-blocklength-urllc]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[physical-layer-security]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[cooperative-cognitive-radio]]"
  - "[[primary-signal-assisted-covertness]]"
  - "[[wang-2026-fd-covert-isac]]"
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[huang-2026-intelligent-jamming-maritime]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
  - "[[qunshu-wang]]"
  - "[[chengwen-xing]]"
  - "[[dusit-niyato]]"
created: 2026-07-14
updated: 2026-07-16
---

# UAV-Assisted Covert Transmission for Cooperative Cognitive Radio Networks

## Citation

Wang, Q., Xing, C., Zhao, N., & Niyato, D. (2026). *UAV-Assisted Covert Transmission for Cooperative Cognitive Radio Networks*. **IEEE Transactions on Wireless Communications, 25**, 1594-1608. DOI: 10.1109/TWC.2025.3591810.

## TL;DR

A decode-and-forward UAV relays a primary user's short packet while superposing a covert secondary signal. Joint power and trajectory design preserves primary quality of service and uses the useful primary signal as interference that masks the secondary transmission from multiple wardens.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude decode-and-forward UAV receives a short primary packet, then forwards the primary signal while superposing a covert secondary message. A primary receiver, secondary receiver, and multiple wardens observe finite-blocklength air-to-ground links with probabilistic LoS/NLoS fading.

**Problem & objective**: A non-convex finite-blocklength design maximizes time-average secondary effective throughput, $\max \frac{1}{N}\sum_{n=1}^{N}R_{\mathrm s}^{\mathrm{eff}}[n]$, under primary quality of service, per-warden covertness, power, and UAV-mobility constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Primary forwarding power | $p_{mathrm p}[n]$ | continuous, nonnegative | UAV power allocated to the relayed primary signal |
| Covert transmit power | $p_{mathrm s}[n]$ | continuous, nonnegative | UAV power allocated to the secondary signal |
| UAV trajectory | $\mathbf q[n]$ | continuous horizontal position | Fixed-altitude UAV location in slot $n$ |
| Auxiliary rate/slack variables | $\boldsymbol\xi[n]$ | continuous | SCA surrogates for throughput and covertness terms |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Total UAV power satisfies $p_{\mathrm p}[n]+p_{\mathrm s}[n]\le P_{\max}$ |
| C2 | The forwarded primary effective throughput exceeds its per-slot QoS threshold |
| C3 | Every warden satisfies the KL/Pinsker sufficient covertness condition |
| C4 | UAV motion satisfies prescribed endpoints and per-slot displacement limits |
| C5 | Finite-blocklength decoding-error and bottleneck-rate definitions remain feasible |

**Algorithm**: Derive finite-blocklength effective throughputs and a KL-based covertness surrogate → fix the trajectory and solve power allocation with slack variables and SCA → fix powers and solve the trajectory block with first-order lower bounds → alternate the convex subproblems until the objective value converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied UAV-assisted covert transmission in a cooperative cognitive radio network with finite-blocklength packets and multiple wardens. A decode-and-forward UAV relays the primary signal and superposes a covert secondary message, allowing the primary waveform to mask the secondary transmission. They formulated time-average secondary effective-throughput maximization under primary quality-of-service, transmit-power, trajectory, and per-warden covertness constraints. Their block-coordinate method alternates power allocation and horizontal trajectory updates, with slack variables and successive convex approximation used in both blocks. Simulations show higher covert throughput than the evaluated fixed-power, fixed-trajectory, shorter-duration, and non-UAV baselines over the tested settings.

## Problem

The paper maximizes the time-average finite-blocklength effective throughput of the secondary link while maintaining per-slot primary-user quality of service, a UAV power budget, mobility constraints, and covertness against every warden. The objective retains the paper's equation-defined bottleneck between primary-receiver and secondary-receiver effective throughputs; the parse is inconsistent about describing the corresponding end-to-end data path.

## System model

One single-antenna UAV flies at fixed altitude between prescribed endpoints. In phase one, a primary transmitter sends a short packet to the UAV; in phase two, the UAV forwards the decoded primary signal and superposes a covert signal for the secondary receiver. Multiple single-antenna wardens use received-power detection to distinguish primary-only forwarding from primary-plus-covert transmission.

The links use finite blocklengths and elevation-dependent probabilistic LoS/NLoS [[air-to-ground-channel-model|air-ground channels]]. PT-UAV is assumed LoS, UAV-warden links are NLoS Rayleigh, and the expected NLoS contributions to the UAV-SR and UAV-PR rates are neglected. Covertness is enforced in every slot and for every warden through a Pinsker/KL sufficient condition, while the relayed primary throughput must exceed a fixed threshold.

## Method

The paper derives finite-blocklength rates, effective throughputs, the wardens' minimum detection error, and a stricter KL-divergence covertness surrogate. A block-coordinate algorithm alternates power allocation and horizontal [[uav-trajectory-control|trajectory]] updates. Slack variables, monotonicity arguments, and first-order lower bounds turn each block into a CVX-solvable SCA subproblem.

## Guarantee scope and findings

The alternating updates produce a nondecreasing, upper-bounded objective sequence under the paper's approximated subproblems. This supports convergence of the objective values, not global optimality or a stationary-point guarantee for the original non-convex problem. The KL constraint is sufficient for the stated detection-error lower bound only under the assumed Gaussian signaling, fading, and detector model.

In simulation, joint power/trajectory optimization outperforms fixed-power, fixed-trajectory, shorter-duration, and non-UAV baselines, without an exact percentage gain stated in the prose. Throughput improves with longer flight time and looser covertness tolerance, and declines with more wardens, higher decoding error, or a stricter primary-QoS threshold over the tested ranges. Increasing covert power or blocklength increases modeled KL divergence, whereas increasing forwarded primary-signal power reduces it.

## Limitations

The model assumes fixed UAV altitude, known fixed warden locations, single-antenna nodes, finite fixed blocklengths, prescribed Gaussian/Rayleigh channel and detector models, and no propulsion-energy constraint. Several equations and symbols are OCR-damaged, and the parse contains inconsistent transmitter/receiver labels. The paper identifies battery-aware design, lower-complexity algorithms, and distributed large-scale or real-time methods as future work.

## Relation to the corpus

This source joins [[covert-communication]] and [[cooperative-cognitive-radio]]: unlike dedicated jamming, [[primary-signal-assisted-covertness]] reuses a signal that also serves the primary link. [[wang-2026-fd-covert-isac]] instead combines a sensing waveform with full-duplex receiver jamming, while [[zhang-2026-irs-uav-covert-fbl]] couples finite-blocklength covertness to active/passive beamforming. All three use alternating local optimization, but only this paper couples covert throughput to a primary relay-QoS constraint.

Its observation objective is the reverse of [[lin-2026-fc-ris-surveillance]]: the primary waveform should make unauthorized activity detection harder, whereas Lin's aerial surface should make authorized suspicious-signal decoding easier. [[huang-2026-intelligent-jamming-maritime]] also controls interference against an adversarial observer, but its separate jammer suppresses Eve's payload rate rather than hiding whether a transmission exists. These role boundaries are mapped in [[aerial-observation-control-covertness-surveillance-and-monitoring]].

## Raw artifacts

- Parse: `raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks.md`
- Origin PDF: `raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks.pdf`
- Figures: `raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/images/`
