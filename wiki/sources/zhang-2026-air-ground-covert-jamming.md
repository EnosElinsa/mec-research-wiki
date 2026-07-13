---
type: source
title: "Air-Ground Cooperative Covert Transmission: A Jamming Dynamic Management and Security Enhancement Approach"
authors: ["Yunyang Zhang", "Bohang Wang", "Weijie Yuan", "Nanchi Su", "Yuanhao Cui", "Guoru Ding"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3673234"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, covert-communication, physical-layer-security, cooperative-jamming, uav-mounted-ris, uav-mobile-relaying, finite-blocklength-urllc, ddqn, energy-efficiency]
related:
  - "[[weijie-yuan]]"
  - "[[ris-assisted-directional-jamming]]"
  - "[[covert-communication]]"
  - "[[cooperative-jamming]]"
  - "[[physical-layer-security]]"
  - "[[uav-mounted-ris]]"
  - "[[uav-mobile-relaying]]"
  - "[[finite-blocklength-urllc]]"
  - "[[ddqn]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[effective-energy-efficiency]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[ma-2024-covert-mmwave-finite-blocklength]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
created: 2026-07-11
updated: 2026-07-14
---

# Air-Ground Cooperative Covert Transmission: A Jamming Dynamic Management and Security Enhancement Approach

## Citation

Zhang, Y., Wang, B., Yuan, W., Su, N., Cui, Y., & Ding, G. (2026). *Air-Ground Cooperative Covert Transmission: A Jamming Dynamic Management and Security Enhancement Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3673234.

## TL;DR

Designs a friendly-jamming covert air-ground link where a decode-and-forward UAV carrying an RIS relays Alice's covert data and redirects a terrestrial jammer toward Willie. Static RIS/power optimization is embedded in a [[ddqn|DDQN]] trajectory and user-scheduling controller to maximize effective-throughput energy efficiency under covertness and propulsion-energy constraints.

## Problem framing

Low-altitude covert transmission must hide the existence of a link, not only protect message content. Prior UAV covert work often optimizes the desired signal first, assumes convenient friendly-jammer placement, or leaves a dedicated jammer exposed. This paper instead uses a mobile UAV-mounted RIS to turn a terrestrial jammer into directional cover, reducing the jammer's dependence on direct geography while preserving Bob's link.

## System model

- Alice is an aerial hovering transmitter; a single-antenna decode-and-forward UAV relays to one of `K` ground Bobs.
- The UAV carries an `N`-element RIS that redirects artificial noise from a terrestrial friendly jammer toward Willie.
- Alice-UAV uses finite-blocklength decoding; UAV-related links use Rician fading; the RIS model keeps first-order reflected signals.
- Willie observes the Alice-UAV and UAV-Bob hops and performs a likelihood-ratio test; covertness is imposed through a Pinsker/KL-divergence upper-bound constraint.
- The service region is discretized into cells and time slots, with UAV horizontal/vertical motion and propulsion energy modeled explicitly.

## Method

- Static optimization decomposes UAV transmit power, RIS phase shifts, and RIS reflection coefficients.
- The static solver uses a closed-form feasible power boundary, semidefinite relaxation, Dinkelbach iterations, and Gaussian randomization.
- The dynamic controller uses DDQN with UAV position, historical channel information, and user demand in the state; actions select horizontal/vertical movement and the scheduled Bob.
- The reward combines effective-throughput energy efficiency with penalties for mission/service-area violations.

## Key findings

- Joint RIS/jammer optimization makes effective throughput increase with jammer power, while the disabled-RIS benchmark shows that a geographically constrained standalone jammer is ineffective.
- Adding RIS elements helps only when the RIS/jamming parameters are globally coordinated; more elements alone do not guarantee better covert throughput.
- Relaxing the covertness tolerance increases throughput, and the proposed scheme remains better than the reported benchmarks under the paper's simulation settings.
- DDQN produces a more direct trajectory than the GA benchmark and better reported propulsion-energy and energy-efficiency CDF behavior.
- The prose does not state exact percentage gains; figure-derived values should remain indicative.

## Limitations / future work

The evaluation is simulation-only and assumes one Willie, first-order RIS reflections, modeled Rician channels, and discrete grid movement. The paper names covert channel estimation and multiple mobile, intelligent wardens with adaptive detection as future directions.

## Relation to the corpus

This source extends the wiki's [[covert-communication]] branch from public-cover traffic ([[hosseini-2026-aoi-covert-uav]]) and finite-blocklength mmWave covertness ([[ma-2024-covert-mmwave-finite-blocklength]]) toward [[ris-assisted-directional-jamming]]. Its UAV-mounted RIS role is different from communication-rate RIS placement in [[pan-2025-uav-ris-energy-efficient-comm]]: here, the RIS mainly steers a friendly jammer's signal while the UAV also acts as a relay and trajectory-controlled security asset.

## Raw artifacts

- `raw/sources/Air-Ground_Cooperative_Covert_Transmission_A_Jamming_Dynamic_Management_and_Security_Enhancement_Approach/Air-Ground_Cooperative_Covert_Transmission_A_Jamming_Dynamic_Management_and_Security_Enhancement_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.

## Metadata notes

The parsed Markdown contains the title and technical text but is silent on DOI/year in its text body. DOI, venue, and year were verified through the local PDF header/footer and exact-title DOI lookup; all technical claims above are grounded in the local parse.
