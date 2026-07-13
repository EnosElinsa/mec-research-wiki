---
type: source
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
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[qunshu-wang]]"
  - "[[chengwen-xing]]"
  - "[[dusit-niyato]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Assisted Covert Transmission for Cooperative Cognitive Radio Networks

## Citation

Wang, Q., Xing, C., Zhao, N., & Niyato, D. (2026). *UAV-Assisted Covert Transmission for Cooperative Cognitive Radio Networks*. **IEEE Transactions on Wireless Communications, 25**, 1594-1608. DOI: 10.1109/TWC.2025.3591810.

## TL;DR

A decode-and-forward UAV relays a primary user's short packet while superposing a covert secondary signal. Joint power and trajectory design preserves primary quality of service and uses the useful primary signal as interference that masks the secondary transmission from multiple wardens.

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

## Raw artifacts

- Parse: `raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks.md`
- Origin PDF: `raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks.pdf`
- Figures: `raw/sources/UAV-Assisted_Covert_Transmission_for_Cooperative_Cognitive_Radio_Networks/images/`
