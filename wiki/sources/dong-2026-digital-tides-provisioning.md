---
type: source
title: "Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks"
authors: ["Wen-Yu Dong", "Song Zhao", "Rui-Si Han", "Qi Bi", "Sheng Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3688690"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-logistics, mobile-edge-computing, fluid-dynamics, information-flux, infrastructure-provisioning, energy-efficiency]
related:
  - "[[information-flux-triggered-infrastructure-activation]]"
  - "[[mobile-edge-computing]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[effective-energy-efficiency]]"
created: 2026-07-13
updated: 2026-07-13
---

# Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks

## Citation

Dong, W.-Y., Zhao, S., Han, R.-S., Bi, Q., & Chen, S. (2026). *Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3688690.

## TL;DR

Models periodic logistics-UAV demand as a compressible fluid and activates ground MEC infrastructure from information flux rather than local density alone. The outward flux signal reaches its threshold ahead of the demand wavefront, creating a guard ring that can absorb radio and container startup latency while an asymmetric holding rule avoids premature shutdown during contraction.

## Problem

Periodic logistics swarms expand from and return to distribution hubs, moving computational demand across a low-altitude network. Density-triggered base-station activation reacts only when the wavefront arrives, so sleeping radio sectors and MEC containers can miss mission-critical workload during setup. Always-on infrastructure avoids that outage but wastes energy through the low-demand part of each logistics cycle.

## System model

- A two-dimensional urban service region contains one logistics hub and fixed-altitude UAV demand whose aggregate density expands and contracts radially.
- Ground base stations form a homogeneous PPP. Their terrestrial sectors remain active for command/control, while orthogonal up-tilted low-altitude sectors and colocated [[mobile-edge-computing|MEC]] servers can sleep.
- A common setup latency covers radio wake-up and MEC container or VM cold start.
- Total load and spatial spread follow sinusoidal functions, producing a time-varying Gaussian workload density. Solving its continuity equation gives a radial velocity field and information flux `Phi = lambda v`.
- Coverage and energy analysis use quasi-static packet intervals, Rayleigh fading, power-law path loss, and a finite time-varying active region.

## Method

[[information-flux-triggered-infrastructure-activation]] uses an outward-flux or load threshold during expansion. Because flux grows with both density and radial velocity, its boundary can precede the density wavefront. During contraction, the flux trigger is disabled and active cells remain on until density falls below a lower holding threshold.

Each base station evaluates local density and expansion-phase flux without neighbor coordination, giving stated `O(M)` complexity for `M` base stations. The analysis derives phase-dependent activation radii, finite-region coverage, served workload, energy consumption, period-average energy efficiency, a guard-ring reliability condition, and an upper bound on the flux threshold for a specified startup latency. A polynomial outage barrier converts the continuous-time reliability-constrained ratio into a QoS-penalized effective-energy-efficiency surrogate.

## Key findings

- The analytical phase-lead result gives `||Phi||/lambda = r dot(sigma)/sigma`, whose radial derivative is positive during expansion.
- Hardware-tier wavefront outage is eliminated when the guard-ring width covers the wavefront displacement during setup, approximately `v_wf(t) tau_boot`; this does not guarantee successful SINR coverage.
- Simulations average 50,000 Monte Carlo runs over a `20 km x 20 km` region with a default `300 s` setup latency.
- At `t=0.6 h`, the reported proactive guard ring is about `8.25 km`; at `r=14.5 km`, flux triggers about five minutes before density.
- The reactive and snapshot-oracle policies serve `79.6%` and `82.8%` of demand, the fixed robust margin serves about `99.0%`, and the flux-aware policy serves `99.1%` while attaining the highest reported effective energy efficiency.
- In the expansion comparison, the reactive boundary lags by roughly `1-2 km` and reaches about `15%` service unavailability, while the calibrated flux-aware strategy reduces it to near zero.

## Limitations / parse caveats

The derivation assumes a cohesive high-density swarm, radial Gaussian demand, sinusoidal load/spread, a homogeneous-PPP infrastructure, local-homogeneity coverage approximation, accurate macroscopic velocity estimates, and uniform startup latency. Abrupt route changes or chaotic individual motion can erase the flux lead; planned corridors, clustered deployments, noisy estimates, and heterogeneous startup times need revised models. Several proofs are deferred to a supplement absent from the parse. One section reports roughly `15%` peak reactive unavailability while the conclusion says roughly `20%`; the page retains the section-specific value rather than reconciling them. Some table entries and equations are OCR-damaged. The parse supplies the DOI and accepted TMC venue; the 2026 year and current `1-15` pages were verified through the exact-title Crossref record.

## Relation to the corpus

This source adds macroscopic demand advection to the corpus's [[low-altitude-intelligent-network]] and [[stochastic-geometry-network-analysis]] vocabulary. Its `effective energy efficiency` is a distinct [[effective-energy-efficiency]] instantiation: raw served-workload-per-energy is multiplied by an outage penalty rather than by the communication/computation utility used in the active-RIS V2X source.

## Raw artifacts

- Parse: `raw/sources/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks.md`
- Origin PDF: `raw/sources/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks.pdf`
- Figures: `raw/sources/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks/images/`
