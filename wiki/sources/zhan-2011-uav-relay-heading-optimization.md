---
type: source
modeling_card: required
title: "Wireless Relay Communications with Unmanned Aerial Vehicles: Performance and Optimization"
authors: ["Pengcheng Zhan", "Kai Yu", "A. Lee Swindlehurst"]
year: 2011
url: "https://doi.org/10.1109/TAES.2011.5937283"
venue: "IEEE Transactions on Aerospace and Electronic Systems (IEEE TAES)"
tags: [source, uav-mobile-relaying, heading-control, ergodic-normalized-transmission-rate, seamless-handover, uav-communications]
related:
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[seamless-handover]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[hu-2019-uav-relay-edge-computing]]"
  - "[[zhao-2019-uav-emergency-disasters]]"
  - "[[lu-2023-uav-relay-secure-maritime-mec]]"
created: 2026-06-02
updated: 2026-07-16
---

# Wireless Relay Communications with Unmanned Aerial Vehicles: Performance and Optimization

## Citation

Zhan, P., Yu, K., & Swindlehurst, A. L. (2011). *Wireless Relay Communications with Unmanned Aerial Vehicles: Performance and Optimization*. **IEEE Transactions on Aerospace and Electronic Systems**, 47(3), 2068–2085. DOI: 10.1109/TAES.2011.5937283. (Manuscript received 3 August 2009; revised 9 February and 2 August 2010; released for publication 20 August 2010. IEEE Log No. T-AES/47/3/941781.)

## TL;DR

Studies a **tactical** hierarchical network where multiple **UAVs act as relays** connecting distributed ground access points (APs) to a remote base station (BTS) in a single hop, on the AP→UAV **uplink**. To quantify link performance the paper defines the **ergodic normalized transmission rate (ENTR)** for each AP–UAV link and derives a closed-form expression in terms of the channel correlation-matrix eigenvalues. It shows the ENTR can be approximated as a **sinusoid plus an offset** in the UAV **heading angle**, which yields a **closed-form optimal UAV heading** that maximizes the sum uplink rate subject to a per-AP minimum-rate constraint. Because the network is mobile, it also develops an adaptive **handoff algorithm** to re-assign APs to relays as the topology evolves, plus a procedure to deploy new UAVs when the current ones cannot meet QoS.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple multi-antenna UAV relays connect distributed multi-antenna ground access points to a remote base station in a tactical single-hop uplink. AP transmissions are orthogonal, and spatially correlated MIMO rates vary with UAV heading.

**Problem & objective**: A heading-control problem maximizes network ENTR, $\max_{\psi_u}\sum_{k\in\mathcal A_u}R_{k,u}(\psi_u)$, subject to minimum AP rates and reachable turning angles.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV heading | $\psi_u$ | continuous angle | Next movement direction of relay $u$ |
| AP-UAV association | $x_{k,u}$ | binary | Relay serving access point $k$ |
| Handoff decision | $h_{k,u\to v}$ | binary | Reassignment of AP $k$ between relays |
| New-relay position | $\mathbf q_{mathrm{new}}$ | continuous position | Deployment target when current relays are infeasible |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every served AP has ENTR above its QoS threshold |
| C2 | Heading remains inside the turning-radius reachable region |
| C3 | Each AP is assigned to one feasible UAV relay |
| C4 | Handoffs preserve link availability during topology change |
| C5 | A new relay is deployed when no current heading/association is feasible |

**Algorithm**: Approximate each link ENTR as a sinusoid plus offset in heading → sum the sinusoids and compute the unconstrained closed-form maximizing angle → intersect link-allowable and reachable heading regions → choose the best feasible heading → trigger RSS-style AP handoffs as links evolve → deploy and steer a new relay if QoS remains infeasible.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhan et al. [x] studied performance optimization for multi-UAV wireless relays serving distributed ground access points. They derived an ergodic normalized transmission-rate metric for spatially correlated MIMO links and approximated each link's rate as a sinusoid in UAV heading. The resulting heading controller maximizes total uplink rate under per-access-point QoS and turning-radius constraints, with a closed-form unconstrained direction and feasible-region correction. An adaptive handoff algorithm reassigns access points as links evolve, and a deployment step adds a relay when the current fleet cannot meet QoS. Simulations report close agreement of the sinusoidal approximation and higher rate or fewer relay deployments than the evaluated unoptimized-heading and no-handoff cases.

## Problem framing

UAVs can be quickly deployed as relays to extend coverage and improve connectivity, especially where nodes are scattered or terrain/buildings degrade direct links. Prior UAV-relay work focused on routing, physical-layer beamforming/OSTBC, connectivity optimization, or delay-tolerant carry-and-forward. This paper differs in its network assumptions, its performance criterion (ENTR), and a **closed-loop UAV heading-control** process to optimize it. It targets a tactical scenario: distributed APs in a remote area communicating with a BTS, with a team of multi-antenna UAVs establishing the links; transmissions are assumed orthogonal/interference-free (valid when the number of APs is not too large, consistent with hierarchical funneling of ground traffic).

## System model

- **Topology.** Multi-user uplink: each AP has `M_a` transmit antennas, each UAV relay has `N_a` receive antennas; APs transmit orthogonally (no inter-user interference); UAVs relay AP traffic to a BTS in a single hop.
- **Channel.** A spatially-correlated MIMO model accounting for different correlation levels at APs and UAVs (e.g. Lee's channel model in simulation); adaptive modulation + space-time coding.
- **Performance metric.** The **ENTR** per AP–UAV link, derived in closed form from the channel correlation-matrix eigenvalues; the **SER** for each AP–UAV link is also analyzed.
- **Optimization.** Find the UAV **heading** maximizing the total network ENTR subject to each AP-link rate exceeding a threshold; constraints include the UAV's per-step turning radius (reachable heading region). When no feasible heading meets all minimum-rate requirements, additional UAVs are needed.

## Method

- **Sinusoidal approximation.** Under mild conditions, each link's rate `R_k(heading)` is approximated as a sinusoid plus offset; the total network throughput is therefore also sinusoidal-plus-constant, giving a **closed-form optimal heading** (absent turning-radius limits) and a "link allowable region" / "reachable region" formulation when limits apply.
- **Adaptive handoff.** As mobile APs/UAVs change link strengths, an RSS-style **handoff algorithm** (modified for UAV motion constraints) periodically reassigns APs to relays to improve network ENTR.
- **New-relay deployment.** When the current UAV configuration cannot host all APs at the required QoS, the paper addresses where to deploy a new UAV relay and how to command its motion.

## Key findings

- The **sinusoidal approximation** accurately matches the simulated total uplink rate as a function of UAV heading.
- Optimizing the UAV's heading yields a meaningful rate gain — the parse cites a **~20 kbit/s** difference in a two-AP example simply from choosing a better heading, enough to support an additional voice user under common standards.
- The **handoff algorithm** reduces the need to deploy additional relays: in the simulation, appropriate handoff events eliminate a relay deployment that the no-handoff network required as AP positions evolved. (Demonstrated via a simple simulation example.)

## Limitations / future work

The authors explicitly list relaxable simplifying assumptions: a **relatively small number of APs** (enabling the orthogonal, interference-free, no-bandwidth-limit assumption) — larger networks would need interference mitigation (frequency reuse, beamforming) and a **bandwidth-aware** handoff (avoid switching an AP to an already-loaded UAV); the **initial UAV deployment** is treated simply, ignoring arrival delay and path planning; and **UAV–UAV links** are assumed error-free with no relaying overhead, so additional motion constraints would be needed to keep the UAV relay network connected. Evaluation is **simulation-only**.

## Relation to the corpus

The **earliest** UAV-communications source in the corpus (2011) and an early **UAV mobile-relaying** anchor alongside [[zeng-2016-throughput-relaying]] — but where Zeng et al. optimize a single relay's *trajectory + power* under an information-causality constraint, Zhan et al. optimize the relay **heading** in closed form via the ENTR sinusoid and add a topology-adaptive **handoff** ([[seamless-handover|handover]]) mechanism for a *multi-UAV, multi-AP* tactical network. It predates the corpus's UAV-relay-with-MEC fusions ([[hu-2019-uav-relay-edge-computing]], [[lu-2023-uav-relay-secure-maritime-mec]]) and the post-disaster UAV-relaying framework [[zhao-2019-uav-emergency-disasters]], situating it as a communication-layer relaying foundation rather than an MEC offloading paper.

## Raw artifacts

- `raw/sources/Wireless_Relay_Communications_with_Unmanned_Aerial_Vehicles_Performance_and_Optimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
