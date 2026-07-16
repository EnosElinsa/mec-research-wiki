---
type: source
title: "Energy-Efficient Cooperative Relaying for Unmanned Aerial Vehicles"
authors: ["Kai Li", "Wei Ni", "Xin Wang", "Ren Ping Liu", "Salil S. Kanhere", "Sanjay Jha"]
year: 2016
url: "https://doi.org/10.1109/TMC.2015.2467381"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 15, no. 6, pp. 1377-1386"
modeling_card: required
tags: [source, cooperative-uav-relaying, energy-balancing, packet-scheduling, rate-adaptation, wireless-sensor-network, integer-programming]
related:
  - "[[energy-balanced-cooperative-uav-relaying]]"
  - "[[uav-mobile-relaying]]"
  - "[[energy-balancing-uav]]"
  - "[[air-ground-integrated-network]]"
  - "[[uav-data-collection]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[zhan-2011-uav-relay-heading-optimization]]"
created: 2026-07-13
updated: 2026-07-16
---

# Energy-Efficient Cooperative Relaying for Unmanned Aerial Vehicles

## Citation

Li, K., Ni, W., Wang, X., Liu, R. P., Kanhere, S. S., & Jha, S. (2016). *Energy-Efficient Cooperative Relaying for Unmanned Aerial Vehicles*. **IEEE Transactions on Mobile Computing**, 15(6), 1377-1386. DOI: 10.1109/TMC.2015.2467381. Final bibliographic fields were verified by exact-title Crossref match because the parse omits them.

## TL;DR

Balances packet-forwarding energy across cooperative UAV relays in a two-hop sensor-to-base-station link. An exact integer min-max scheduler is used for small cases; EPLA alternates packet-load balancing with modulation/rate increases to meet a BER-constrained TDMA deadline at much lower runtime.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Remote sensors broadcast packets to a cooperative UAV relay fleet, and the UAVs immediately forward successfully decoded packets to a base station in a TDMA frame. The base station observes second-hop SNR, then assigns disjoint packets, modulation levels, and corresponding transmit powers while the relays follow predetermined trajectories.

**Problem & objective**: The integer scheduler minimizes $\max_i\sum_{s\subseteq\mathbb S_i}\sum_{\rho_i=1}^{M}x_{i,s,\rho_i}\delta_i(t)\frac{2^{\rho_i}-1}{\rho_i}$, the largest forwarding-energy expenditure among the cooperative UAVs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Packet-relay-modulation assignment | $x_{i,s,\rho_i}$ | binary | Whether UAV $i$ forwards packet $s$ using modulation level $\rho_i$ |
| Modulation level | $\rho_i$ | discrete, $\{1,\ldots,M\}$ | Rate selected for UAV $i$ |
| UAV transmit power | $\Gamma_i(t)$ | continuous, derived | Power needed by the chosen rate and SNR to meet the BER target |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Required transmit power does not exceed $P_{\max}$ |
| C2 | A packet assigned to one UAV uses exactly one modulation level |
| C3 | Every packet decoded by at least one UAV is forwarded exactly once |
| C4 | All scheduled transmissions fit the TDMA forwarding duration $T$ |
| C5 | The rate-dependent power is selected to satisfy the target BER $\epsilon$ |

**Algorithm**: The exact method reformulates the min-max integer program as one minimization problem per candidate maximum-energy UAV and selects the best result. EPLA provides the real-time alternative by repeatedly moving packets from the highest-energy relay to lower-energy relays, then increasing the modulation of the UAV that most reduces transmission time until the TDMA deadline is feasible.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] balanced forwarding energy across cooperative UAV relays that carry sensor packets to a base station over a two-hop TDMA link. They minimized the maximum per-relay transmit energy over packet assignment and modulation under BER, transmit-power, unique-forwarding, and slot-duration constraints. EPLA alternates packet-load balancing with rate adaptation and was roughly four orders of magnitude faster than exact scheduling with five UAVs. With 20 UAVs, it extended lifetime by 33% and increased network yield by 15% relative to the low-transmit-power baseline while saving 50% energy.

## Problem

Remote sensors broadcast over lossy air links to battery-limited UAVs, which immediately relay decoded packets to a base station. A scheduler that repeatedly favors good channels can exhaust a subset of relays early, while equal allocation wastes energy on poor channels. The paper minimizes the largest relay forwarding-energy use while preserving packet success and slot feasibility.

## System model

- One hundred sensors use prescheduled TDMA; cooperative UAVs report decoded packets and first-hop reception quality, while the base station measures each UAV's second-hop SNR.
- The base station assigns disjoint packets, modulation levels, and powers to UAVs so every decoded packet is forwarded exactly once before a `10 ms` slot deadline.
- UAVs follow predetermined circular trajectories at 50 m altitude and 10 m/s. Links use free-space large-scale loss, independent Rayleigh fading, and within-frame block fading.
- The optimized energy is relay transmit energy only; propulsion, hovering, base-station energy, and sensor energy are outside the objective.

## Method

The exact formulation converts a min-max integer scheduler into one problem for each possible maximum-energy relay and keeps the best solution. EPLA first assigns feasible packets at low modulation, repeatedly transfers load from the highest-energy to the lowest-energy relay, and then raises selected modulation levels when the total forwarding time still exceeds the slot. Energy balancing and rate adaptation alternate until the deadline is met.

## Key findings

- For five UAVs, the exact scheduler averages `129.1360 s` and EPLA `0.0664 s`; the resulting ratio is about `1945x`. This conflicts with the paper's separate three-order and four-order descriptions.
- At 20 UAVs, the prose reports EPLA lifetime as `33%`, `60%`, and `66.7%` longer than Low TxPower, Average, and Random allocation. Here lifetime is the paper's nonstandard `max_i T_i`, the time until all UAV batteries are exhausted rather than time to first relay failure; the plotted gains also imply EPLA, not the named baseline, is the percentage denominator.
- At 20 UAVs, the paper reports `15%/30%/38%` higher network yield and `50%/75%/78%` lower forwarding energy against the same three baselines.
- With ten UAVs, the longest simulated lifetime occurs at a 500 m trajectory radius; the preferred circle center is 1.0-1.2 km from the base station.

## Limitations / parse caveats

Scheduling is centralized and assumes timely reception reports, base-station second-hop SNR estimates, equal packet sizes, fixed sensor power, TDMA, uniform circular flight, and no reporting errors. The results are simulation-only and omit propulsion energy even when changing trajectory geometry. Network lifetime is defined as time until all relay batteries are exhausted rather than first-relay failure, the lifetime percentages use an unconventional denominator, the success-probability equation is missing a likely minus sign, the network-yield figure axis conflicts with its 20-UAV prose, and no approximation ratio or formal iteration bound is given.

## Relation to the corpus

Unlike [[zeng-2016-throughput-relaying]], which jointly designs a mobile relay trajectory and powers under information causality, this source freezes flight paths and optimizes cooperative packet assignment, modulation, and forwarding power. It therefore anchors [[energy-balanced-cooperative-uav-relaying]] rather than trajectory-first relaying.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_Cooperative_Relaying_for_Unmanned_Aerial_Vehicles/Energy-Efficient_Cooperative_Relaying_for_Unmanned_Aerial_Vehicles.md`
- Origin PDF: `raw/sources/Energy-Efficient_Cooperative_Relaying_for_Unmanned_Aerial_Vehicles/Energy-Efficient_Cooperative_Relaying_for_Unmanned_Aerial_Vehicles.pdf`
- Figures: `raw/sources/Energy-Efficient_Cooperative_Relaying_for_Unmanned_Aerial_Vehicles/images/`
