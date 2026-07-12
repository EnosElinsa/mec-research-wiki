---
type: source
title: "Enhancing Secrecy Energy Efficiency in UAV-RIS Assisted Mobile IoV Networks Through DRL"
authors: ["Jiawei Li", "Dawei Wang", "Hongbo Zhao", "Yi Jin", "Yixin He", "Fuhui Zhou", "Zhongxiang Wei", "Victor C. M. Leung"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3594691"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, internet-of-vehicles, physical-layer-security, uav-mounted-ris, untrusted-relay, secrecy-energy-efficiency, ddpg, fractional-programming]
related:
  - "[[secrecy-energy-efficiency]]"
  - "[[physical-layer-security]]"
  - "[[uav-mounted-ris]]"
  - "[[cooperative-jamming]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[majorization-minimization]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[ddpg]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[uav-trajectory-control]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[fuhui-zhou]]"
  - "[[victor-c-m-leung]]"
created: 2026-07-13
updated: 2026-07-13
---

# Enhancing Secrecy Energy Efficiency in UAV-RIS Assisted Mobile IoV Networks Through DRL

## Citation

Li, J., Wang, D., Zhao, H., Jin, Y., He, Y., Zhou, F., Wei, Z., & Leung, V. C. M. (2026). *Enhancing Secrecy Energy Efficiency in UAV-RIS Assisted Mobile IoV Networks Through DRL*. **IEEE Transactions on Wireless Communications**, 25, 2092-2108. DOI: 10.1109/TWC.2025.3594691.

## TL;DR

Protects mobile vehicular communication against an amplify-and-forward relay that may eavesdrop while forwarding. A UAV-mounted RIS assists both hops, the target vehicle transmits artificial interference during the first hop, and an alternating solver combines Dinkelbach/CCCP power updates, MM-based two-hop RIS phases, and a firefly-warm-started DDPG trajectory policy to maximize secrecy energy efficiency.

## Problem framing

Relays extend coverage but become internal eavesdroppers when they are not trusted. Mobility of both the vehicle and UAV also introduces Doppler phase changes, while maximizing secrecy rate alone can spend excessive power. The paper therefore optimizes the secure-rate-to-power ratio across relay forwarding, vehicle jamming, RIS reflection, and UAV movement.

## System model

- One remote base station communicates with one mobile target vehicle through an untrusted half-duplex amplify-and-forward ground relay and a passive [[uav-mounted-ris|UAV-mounted RIS]].
- During the first hop, the base station sends confidential data and the target vehicle sends a jamming signal toward the relay. During the second hop, the relay forwards the first-hop signal while the base station sends a new message through the RIS; the vehicle cancels its own jamming and applies successive interference cancellation.
- Separate continuous phase matrices control the RIS in the two hops. Direct and RIS-assisted paths include Rician/Rayleigh components and mobility-induced Doppler phases.
- Independent decisions are base-station and vehicle powers, relay amplification, both RIS phase matrices, and the UAV's slotwise 3-D trajectory.
- The [[secrecy-energy-efficiency]] denominator includes base-station, relay, and vehicle transmit power. UAV propulsion and avionics energy are excluded under an assumption of continuous, sufficient solar supply.

## Method

The non-convex problem is separated into three alternating blocks:

- **Power and relay amplification:** [[fractional-programming-dinkelbach|Dinkelbach's method]] converts the fractional objective; DC/CCCP updates optimize transmit powers, and Newton iteration updates the relay amplification factor.
- **Two-hop RIS phases:** an [[majorization-minimization|MM]] surrogate and semidefinite relaxation update the two phase matrices, followed by Gaussian randomization to recover feasible phase vectors.
- **UAV trajectory:** a firefly algorithm first searches coordinate samples. Those samples seed the [[ddpg|DDPG]] replay buffer, after which the actor-critic policy learns continuous 3-D movement. This is an instance of [[expert-guided-warm-start-rl|heuristic-guided warm-starting]], although the heuristic supplies replay samples rather than a demonstrated policy.

The resulting controller alternates these blocks; it does not guarantee a globally optimal trajectory.

## Key findings

- The abstract and conclusion report secrecy-energy-efficiency gains of 33.3% over DDPG-only and 64.2% over the FA-based scheme.
- The contribution section separately reports a 13.7% gain over the no-interference scheme, isolating the benefit of vehicle-generated jamming.
- The simulations report a non-monotone dependence on base-station power: additional power can also strengthen relay eavesdropping. For one reported curve, secrecy energy efficiency falls beyond 18 dBm.
- Increasing RIS size helps only up to a point in the tested setting; the prose reports a decline after more than 32 elements because reflected energy also strengthens the relay-side path.
- FA-generated replay samples reduce the poor initial exploration observed in DDPG-only and lead to faster convergence in the reported simulations.

## Limitations / future work

The design is simulation-based and returns a sub-optimal solution. Its energy-efficiency denominator omits UAV propulsion and avionics energy under an idealized continuous-solar-supply assumption. The formulation writes a per-slot secrecy-energy-efficiency ratio while jointly optimizing a multi-slot trajectory, so aggregate versus per-slot interpretation requires care. Doppler is modeled, but closed-loop real-time Doppler compensation is future work. The parse also contains conflicting fixed-vehicle coordinates, inconsistent MM/CCCP terminology, and damaged channel/formula rendering; those disputed details are not used here.

## Relation to the corpus

This is a physical-layer vehicular-communication source rather than a computation-offloading paper. It extends [[physical-layer-security]] to an internal eavesdropper that must still forward traffic, and its power/RIS/trajectory decomposition is a hybrid instance of [[alternating-optimization-sdr-sca]]. It complements [[wang-2026-secure-lae-uav-scheduling]], where multiple UAVs switch between communication and jamming roles and propulsion energy enters the secrecy-efficiency objective. It is also adjacent to [[pan-2025-uav-ris-energy-efficient-comm]], but adds an untrusted relay, vehicle jamming, Doppler-aware channels, and a secrecy rather than ordinary communication-efficiency objective.

## Raw artifacts

- Parse: `raw/sources/Enhancing_Secrecy_Energy_Efficiency_in_UAV-RIS_Assisted_Mobile_IoV_Networks_Through_DRL/Enhancing_Secrecy_Energy_Efficiency_in_UAV-RIS_Assisted_Mobile_IoV_Networks_Through_DRL.md`
- Origin PDF: `raw/sources/Enhancing_Secrecy_Energy_Efficiency_in_UAV-RIS_Assisted_Mobile_IoV_Networks_Through_DRL/Enhancing_Secrecy_Energy_Efficiency_in_UAV-RIS_Assisted_Mobile_IoV_Networks_Through_DRL.pdf`
- Figures: `raw/sources/Enhancing_Secrecy_Energy_Efficiency_in_UAV-RIS_Assisted_Mobile_IoV_Networks_Through_DRL/images/`
