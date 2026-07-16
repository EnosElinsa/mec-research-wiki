---
type: source
title: "Resource Allocation Scheme in STAR-RIS-Assisted NOMA Systems Based on UAV Energy Supply"
authors: ["Shuyu Meng", "Xue Wang", "Xiaoying Sun", "Yixuan Zou", "Yuanwei Liu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3615641"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 4966-4981, 2026"
tags: [source, star-ris, noma, wireless-power-transfer, rf-energy-harvesting, resource-allocation, block-coordinate-descent, sum-rate]
related:
  - "[[uav-energy-supplied-star-ris-noma]]"
  - "[[star-ris]]"
  - "[[noma]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[meng-2026-fullspace-star-ris-secure]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
  - "[[yuanwei-liu]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# Resource Allocation Scheme in STAR-RIS-Assisted NOMA Systems Based on UAV Energy Supply

## Citation

Meng, S., Wang, X., Sun, X., Zou, Y., & Liu, Y. (2026). *Resource Allocation Scheme in STAR-RIS-Assisted NOMA Systems Based on UAV Energy Supply*. **IEEE Transactions on Wireless Communications**, 25, 4966-4981. DOI: 10.1109/TWC.2025.3615641.

## TL;DR

Studies uplink NOMA for users whose direct base-station links are blocked. A fixed STAR-RIS supplies transmitted and reflected paths, while a UAV following a predetermined route transfers RF energy to the users and surface. A block-coordinate-descent loop alternates STAR-RIS coefficient design, user-power allocation, and harvest/transmit time allocation to maximize multi-slot sum-rate.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed $K$-element STAR-RIS assists $M$ ground users whose direct BS links are blocked, while a UAV on a predetermined route supplies RF energy. Users transmit simultaneously by uplink power-domain NOMA, and the BS decodes in descending effective-channel-gain order.

**Problem & objective**: UAV-energy-supplied STAR-RIS NOMA resource allocation, a non-convex continuous optimization, maximizes multi-slot sum-rate, $\max\sum_{m,t}R_m(t)$, subject to user/surface energy causality, time, power, minimum-rate, interference, and STAR-RIS feasibility constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| STAR-RIS coefficients | $\boldsymbol\alpha_t,\boldsymbol\beta_t$ | continuous amplitudes/phases | Transmission/reflection configuration in slot $t$ |
| User powers | $p_m(t)$ | continuous, bounded | NOMA uplink transmit powers |
| Energy/information durations | $\tau_m(t),T_E(t)$ | continuous, nonnegative | User transmission and UAV WET time allocation |
| Auxiliary transform | $\eta_t$ | continuous | Fractional/sum-rate transform variable |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | User cumulative energy and STAR-RIS circuit energy remain feasible |
| C2 | NOMA users meet minimum-rate requirements and SIC/interference expressions |
| C3 | UAV WET and user information durations fit each slot |
| C4 | User powers obey per-slot limits and the STAR-RIS energy-splitting model |
| C5 | RIS reflection/transmission coefficients satisfy unit-modulus and surface constraints |

**Algorithm**: Lift STAR-RIS coefficients and solve a penalty-SCA SDR → apply the auxiliary/Dinkelbach-labelled power transform and convex power updates → solve energy/information durations with the stated game-theoretic utility → alternate all three BCD blocks until sum-rate improvement is below the stopping tolerance.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Meng et al. [x] studied resource allocation in a STAR-RIS-assisted uplink NOMA system supplied by a UAV. They formulated a non-convex sum-rate maximization that jointly designs STAR-RIS transmission/reflection coefficients, user powers, and energy/information time allocation under user and surface energy causality, minimum-rate, and interference constraints. The UAV follows a predetermined route and wirelessly powers users and the surface before simultaneous NOMA transmission. Their block-coordinate-descent solver uses penalty-SCA SDR for the RIS block, an auxiliary fractional transform for powers, and a game-theoretic time-allocation update. Simulations report higher average sum-rate than the selected surface, time-splitting, and optimization baselines in the evaluated settings.

## Problem

STAR-RIS extends service to users on both sides of a surface, but uplink NOMA couples their rates through interference and successive interference cancellation. Supplying the users and STAR-RIS from a UAV introduces an additional tradeoff because charging consumes time otherwise available for data. The optimization jointly handles full-space propagation, user and surface energy causality, rate requirements, interference overhead, and the per-slot energy/information time split.

## System model

The network contains one base station, one fixed `K`-element STAR-RIS, `M` ground users, and one UAV. Direct user-to-BS links are blocked. The UAV flies at fixed altitude on a predetermined multi-slot path and transmits at constant power during each slot's energy phase; the paper assumes that the UAV recharges from solar energy. Users then transmit simultaneously through uplink power-domain [[noma|NOMA]], and the BS applies SIC in decreasing effective-channel-gain order.

The STAR-RIS uses energy splitting with independently controlled transmission and reflection amplitudes and phases. The main model assumes full CSI and linear RF-energy conversion. Constraints cover cumulative user energy, STAR-RIS circuit energy, time allocation, surface feasibility, user power, minimum rates, and modeled interference overhead.

## Method

With power and time fixed, the STAR-RIS block lifts coefficient vectors into positive-semidefinite matrices and combines an SDR formulation with a penalty/SCA treatment of the rank-one condition. With surface coefficients and time fixed, the power block uses the paper's Dinkelbach-labelled auxiliary transform and iterative convex optimization. Its displayed square-root-over-denominator update resembles a quadratic transform, so the source's label is retained without asserting a broader equivalence.

For fixed surface and power variables, a game-theoretic utility updates the energy and information durations under stated concavity conditions. The outer BCD loop alternates all three blocks until the sum-rate change falls below `10^-3`. The paper argues monotonic improvement but presents the result as a suboptimal solution to the non-convex problem, not a global optimum.

## Key findings

- The abstract reports a 43.64% average sum-rate improvement over the selected comparison schemes. This is a simulation-reported aggregate; the statement does not specify the exact averaging set.
- For 10 users, the proposed BCD routine is reported to converge in 28 iterations on average. The time-allocation routine is separately reported to reach 0.5% utility-deviation accuracy within 35 iterations in its scaled simulation.
- The Fig. 6 discussion reports 48.47% average sum-rate improvement over random time splitting and 37.83% over the paper's SDR+KOA comparison. These are figure-associated, setting-specific results, and some baseline labels are damaged in the parse.
- For 50-70 STAR-RIS elements, the Fig. 9 discussion reports about 19.76% average sum-rate improvement over fixed/random surface designs. This is a simulation-specific figure result.
- The simulated system performs best around a UAV altitude of 24-32 m and declines above 32 m under the reported parameters. This interval is not a general deployment rule.
- With increasing element count, the reported NOMA sum-rate grows faster than TDMA; with increasing user count, it approaches twice the TDMA value in the plotted setup. These are qualitative figure trends rather than universal ratios.

## Limitations

Evaluation is simulation-only. The UAV path and altitude are predetermined, and propulsion energy, flight-battery dynamics, and trajectory optimization are absent. The main derivation assumes full CSI; imperfect CSI is evaluated through a sensitivity experiment rather than a robust joint optimization. The model also assumes independent STAR-RIS phase control, linear constant-efficiency harvesting, and solar replenishment of the UAV.

No global-optimality guarantee is established. Several percentages are author-reported readings associated with figures, and the MinerU parse damages some equation references and baseline labels. Hardware-practical coupled STAR-RIS phases and nonlinear rectifier behavior remain outside the formulation.

## Relation to the corpus

[[uav-energy-supplied-star-ris-noma]] captures the paper's coupling of [[star-ris]], [[noma]], [[wireless-power-transfer]], and [[rf-energy-harvesting]]. The optimization belongs to [[alternating-optimization-sdr-sca]] and uses the source-labelled [[fractional-programming-dinkelbach]] step. [[mohammadi-2026-star-ris-uav-mec-noma]] and [[xiao-2025-star-ris-bidirectional-uav-mec]] optimize MEC energy or offloading, whereas this source maximizes communication sum-rate with a fixed terrestrial STAR-RIS. [[meng-2026-fullspace-star-ris-secure]] focuses secrecy and UAV trajectory, and [[xie-2023-wireless-powered-short-packet-uav]] provides a TDMA finite-blocklength WPT contrast. Author [[yuanwei-liu]] connects this work to the broader STAR-RIS corpus.

## Raw artifacts

- Parse: `raw/sources/Resource_Allocation_Scheme_in_STAR-RIS-Assisted_NOMA_Systems_Based_on_UAV_Energy_Supply/Resource_Allocation_Scheme_in_STAR-RIS-Assisted_NOMA_Systems_Based_on_UAV_Energy_Supply.md`
- Origin PDF: `raw/sources/Resource_Allocation_Scheme_in_STAR-RIS-Assisted_NOMA_Systems_Based_on_UAV_Energy_Supply/Resource_Allocation_Scheme_in_STAR-RIS-Assisted_NOMA_Systems_Based_on_UAV_Energy_Supply.pdf`
- Figures: `raw/sources/Resource_Allocation_Scheme_in_STAR-RIS-Assisted_NOMA_Systems_Based_on_UAV_Energy_Supply/images/`
