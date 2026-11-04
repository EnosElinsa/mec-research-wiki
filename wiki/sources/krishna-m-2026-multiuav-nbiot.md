---
type: source
title: "Performance Analysis of Multi-UAV-Aided NB-IoT Communication System"
authors: ["Siva Rama Krishna M.", "Naveen Mysore Balasubramanya"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3673845"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-16"
modeling_card: required
tags: [source, nb-iot, multi-uav, code-domain-noma, scheduling, latency, energy-efficiency]
related:
  - "[[narrowband-iot]]"
  - "[[code-domain-noma]]"
  - "[[longest-transmission-time-first-uav-grouping]]"
  - "[[non-terrestrial-network]]"
  - "[[air-to-ground-channel-model]]"
  - "[[makespan-minimization]]"
created: 2026-07-14
updated: 2026-11-03
---

# Performance Analysis of Multi-UAV-Aided NB-IoT Communication System

## Citation

Krishna M., S. R., & Balasubramanya, N. M. (2026). *Performance Analysis of Multi-UAV-Aided NB-IoT Communication System*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3673845.

## TL;DR

Models stationary decode-and-forward UAVs as NB-IoT relays for ground-device clusters, then reduces end-to-end collection time and device energy by combining Zadoff-Chu code-domain NOMA with dynamic longest-transmission-time-first grouping.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $M$ stationary decode-and-forward UAVs collect NB-IoT uplink data from ground UEs and forward it to a terrestrial BS. UE-UAV links use the TDL-D LoS model; UAV-BS links are evaluated over TDL-D, EPA, and ETU. On the UAV-BS link, OMA gives each UAV its own NPUSCH slot ($t_i=N_{a,i}t_{\mathrm{UE}}$), while code-domain NOMA with Zadoff-Chu spreading and imperfect SIC lets $N_{\mathrm{UAV}}$ UAVs transmit together.

**Problem & objective**: This is a performance analysis with no formal optimization problem. It derives the average UAV-BS transmission time for OMA, $\mathbb E[t_{\mathrm{OMA}}]=(\sum_i\mathbb E[N_{a,i}])t_{\mathrm{UE}}$ in (5), for static NOMA grouping from (8), and for dynamic grouping, $T^{\mathrm{Dyn}}_{\mathrm{NOMA}}=\lceil\sum_i\mathbb E[N_{a,i}]/N_{\mathrm{UAV}}\rceil t_{\mathrm{UE}}$ in (11), the lower bound $t_{\min}$ in (10). Closed forms follow for discrete-uniform, Poisson, and beta UE-activity distributions, plus end-to-end UE latency and energy.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV groups (pools) | $\mathcal G_k$ / $\mathcal P_n$ | discrete sets of UAVs | UAVs that transmit together under NOMA; fixed in static grouping, formed per realization in dynamic grouping |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| Model rule | Static grouping forms $K=\lceil M/N_{\mathrm{UAV}}\rceil$ predetermined groups; each group lasts $(\max_{i\in\mathcal G_k}N_{a,i})t_{\mathrm{UE}}$ (8) |
| Model rule | Dynamic grouping uses $N_{\mathrm{UAV}}$ pools; total time is $\max_nL_n\,t_{\mathrm{UE}}$ |
| Model rule | Group size $N_{\mathrm{UAV}}$ requires $N_{\mathrm{UAV}}-1$ SIC operations; the evaluation uses $N_{\mathrm{UAV}}=2$ |
| Simulation setting | Link reliability is judged at BLER $10^{-1}$; NOMA supports coverage areas CVA 1 and CVA 2, OMA all three |

**Algorithm**: Static grouping (Algorithm 1) groups consecutive UAVs. Dynamic grouping (Algorithm 2, longest transmission time first) sorts UAVs by active-UE load in descending order, assigns each to the pool with the smallest load $L_n$, and returns $\max_nL_n\,t_{\mathrm{UE}}$, with $O(M\log M)$ complexity.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Krishna and Balasubramanya [x] studied NB-IoT communication in which multiple stationary UAVs relay ground-device traffic to a terrestrial base station. They compared sequential OMA scheduling with Zadoff-Chu code-domain NOMA and proposed static and dynamic UAV grouping for the UAV-to-BS link. The dynamic method sorts UAV loads by longest transmission time first and assigns each UAV to the least-loaded pool to reduce the largest pool load and hence the total transmission time. Closed-form average-transmission-time expressions were derived for discrete-uniform, Poisson, and beta user-activity distributions, and 3GPP-compliant physical-layer simulations covered TDL-D, EPA, and ETU channels. NOMA scheduling with either grouping gives lower latency and UE energy than OMA, with dynamic grouping best, but NOMA meets the $10^{-1}$ BLER target only in the small and medium coverage areas, while OMA supports all three.

## Problem and system model

Ground user equipment cannot reach the base station directly across the modeled 0.86 km2 cell. Stationary UAVs hover at 150 m, receive NB-IoT uplinks from assigned spots, and decode-and-forward the data to the base station. The 180 kHz link model includes NPRACH, NPUSCH, and NPDSCH procedures, TDL-D user-to-UAV channels, and TDL-D/EPA/ETU UAV-to-base-station channels.

Orthogonal access serves users sequentially with TDMA. The non-orthogonal design assigns simultaneous users different Zadoff-Chu spreading codes and applies successive interference cancellation with estimated channels; it is therefore [[code-domain-noma]], not the power-domain model represented by the wiki's general NOMA page.

## Method

Static grouping fixes the UAV pools. Dynamic [[longest-transmission-time-first-uav-grouping]] sorts offered loads in descending order and repeatedly assigns the next load to the currently lightest pool, adapting a longest-processing-time scheduling heuristic to multi-UAV collection. Physical-layer simulations include practical channel estimation and compare scheduled and grant-free random access.

## Key findings

- In the six-UAV example, dynamic grouping completes collection in 11 ms versus 15 ms for static grouping.
- OMA supports all three evaluated coverage requirements, while the NOMA design is limited to the small and medium coverage cases under the tested link budget.
- Dynamic NOMA gives the lowest latency and user-equipment energy across the discrete-uniform, Poisson, and beta load distributions.
- At 50 UAVs, reported grouping-processing time is below 0.125 microseconds for static grouping and 0.375 microseconds for dynamic grouping; these are implementation measurements, not airborne execution results.
- In the grant-free comparison, NOMA needs about 5 dB rather than 0 dB to reach 99% preamble-detection probability and about 3 dB additional SNR to reach BLER 0.1.

## Limitations

The UAVs are quasi-static; deployment, trajectory, and failure recovery remain future work. The main analysis assumes no NPRACH collision among active devices, although a separate collision calculation is provided. Imperfect cancellation limits a code group to two users. The grouping procedure is a heuristic and has no global-optimality proof. The paper uses inconsistent LTTF/LPTF naming, so this page describes the scheduling rule directly and avoids treating either label as a separate guarantee. Results are analytical and simulation-based, with no airborne deployment.

## Relation to the corpus

This source connects [[narrowband-iot]] access mechanics to multi-UAV relay scheduling. Its maximum-pool-completion objective is a specialized [[makespan-minimization]] problem, while its code separation makes it distinct from power-domain aerial NOMA resource-allocation papers.

## Raw artifacts

- Parse: `raw/sources/Performance_Analysis_of_Multi-UAV-Aided_NB-IoT_Communication_System/Performance_Analysis_of_Multi-UAV-Aided_NB-IoT_Communication_System.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
