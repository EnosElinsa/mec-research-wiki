---
type: source
title: "HAP-UAV-Assisted Maritime IoT Communication Network"
authors: ["Lingling Liu", "Chong Shen", "Feng Shu", "Feng Wang", "Shujing Li", "Tony Q. S. Quek"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3596169"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, maritime, hap, uav, unicast-multicast, backhaul, multi-objective, multi-verse-optimizer, noma-multicast]
related:
  - "[[maritime-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[unicast-multicast-cooperation]]"
  - "[[wireless-backhaul]]"
  - "[[noma]]"
  - "[[multi-verse-optimizer]]"
  - "[[wang-2026-aerial-marine-msar]]"
created: 2026-05-29
updated: 2026-11-03
modeling_card: required
---

# HAP-UAV-Assisted Maritime IoT Communication Network

## Citation

Liu, L., Shen, C., Shu, F., Wang, F., Li, S., & Quek, T. Q. S. (2025). *HAP-UAV-Assisted Maritime IoT Communication Network*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3596169.

## TL;DR

A maritime communication architecture (UMABMCN) where:

- Multiple **UAVs** provide **multicast** services to vessels (broadcast content like weather, traffic, sports) — limited by the worst-channel vessel in each multicast group (intra-group bottleneck).
- A single **HAP** provides **unicast** services to specific vessels (per-vessel content) and serves as a **wireless backhaul** for UAVs (HAP-to-UAV link with larger bandwidth).
- Vessels use NOMA-style SIC: decode multicast first, then unicast.

The authors formulate a **three-objective MOP**: (1) maximize sum B2V access rate, (2) maximize HAP-to-UAV backhaul rate, (3) minimize UAV energy consumption — all subject to BS-vessel association, UAV power, and UAV placement constraints.

Two solvers: an enhanced multi-verse optimization with chaos + grey-wolf + discrete update (**EMOMVO-CGD**), and a step-wise classical method (**JCCPAPO**: communication-connection optimization → power allocation → PSO-based UAV placement).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In the UMABMCN, one HAP gives H2V unicast service and multiple UAVs give U2V multicast service to $V$ maritime vessels, and the HAP also provides H2U backhaul links to the UAVs. Each vessel associates with one base station $s$ (the HAP, $s=0$, or a UAV), and air-to-sea and HAP-to-UAV channels are modeled separately.

**Problem & objective**: UMCMOP (P1), a constrained multi-objective MINLP: $\min_{\mathcal X} F = \{-f_1, -f_2, f_3\}$ with $\mathcal X = [\mathcal L, \mathcal P, \Theta]$, where $f_1$ is the B2V sum access rate, $f_2$ the H2U sum backhaul rate, and $f_3 = \sum_{u} E_u^f$ the UAV movement energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV positions | $\mathcal L = [x_1^U,\dots,x_u^U,y_1^U,\dots,y_u^U]$ | continuous 2-D | Horizontal UAV coordinates |
| Transmit powers | $\mathcal P = [p_0, p_1, \dots, p_u]$ | continuous, bounded | HAP and UAV transmit powers |
| Access relationships | $\Theta = [\epsilon_{s,1},\dots,\epsilon_{s,V}]$ | binary | Vessel $v$ associates with base station $s$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 (22b-22c) | UAV coordinates lie in $[X_{\min}, X_{\max}]$ and $[Y_{\min}, Y_{\max}]$. |
| C3 (22d) | UAV transmit power, $P_{\min} \le p_{u,v} \le P_{\max}$. |
| C4 (22e) | Peak power per base station, $0 \le \sum_v \epsilon_{s,v} p_{s,v} \le \hat P_s$. |
| C5 (22f) | Each vessel associates with at most one base station, $\sum_{s=0}^{U} \epsilon_{s,v} \le 1$. |
| C6 (22g) | Association variables are binary. |

**Algorithm**: EMOMVO-CGD, an enhanced multi-objective multi-verse optimizer with chaos, grey-wolf, and discrete updates, searches the mixed decision space and keeps Pareto solutions. The step-wise JCCPAPO alternative first optimizes vessel-base-station connections, then UAV transmit powers, then UAV placement by PSO.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied a HAP-UAV-assisted maritime IoT communication network that combines UAV multicast, HAP unicast, and HAP-to-UAV wireless backhaul. They formulated a mixed multi-objective problem that maximizes vessel access rate and HAP-to-UAV backhaul rate while minimizing UAV movement energy under placement, power, and association constraints. They proposed EMOMVO-CGD, an enhanced multi-verse optimizer with chaos, grey-wolf, and discrete updates for the mixed decision space. They also proposed JCCPAPO, a step-wise method that decomposes the problem into communication-connection optimization, power allocation, and PSO-based UAV placement. Simulations show that both methods improve the vessel sum access rate and the backhaul rate and reduce UAV energy relative to the benchmarks.

## Why this matters

This is a **communication-layer foundations** paper for the wiki's maritime track — the layer beneath the maritime MEC paper [[wang-2026-aerial-marine-msar]]. Where Wang et al. compute *what to do with the bits*, this paper decides *how the bits get delivered*.

Three observations worth tracking:

1. **Unicast + multicast hybrid** is a workload pattern not yet present elsewhere in the wiki. Multicast caps the multicast group at the worst channel, so UAV placement is dominated by serving the laggard vessel — different from unicast-only placements.
2. **HAP as backhaul** rather than HAP as compute. Most prior wiki entries put compute on the HAP. This one uses the HAP purely as a relay-tier transport pipe.
3. **Multi-verse optimizer** is a metaheuristic the wiki hasn't seen before — chaos for exploration, grey-wolf for exploitation, discrete-update for binary association variables. Not obviously better than [[binary-whale-optimization|BWOA]]; the paper doesn't compare against BWOA.

## Findings

- Across two cases (60 vessels / 20 UAVs and 70 vessels / 30 UAVs), EMOMVO-CGD attains the best sum backhaul rate (objective f₂) among all benchmarks, while the classical step-wise JCCPAPO attains the best sum B2V access rate (objective f₁); the two achieve similar UAV energy (f₃). Benchmarks in the parse are the evolutionary MOJS / MOSMA / MOEA/D / conventional MOMVO and the ablation variants C-C-O / P-A-O / P-O / Fixed C-P-P (no NSGA-II in the parse). The per-objective values live in Tables II–III and are indicative.
- The split is read as f₁ having convex structure (favoring the decomposition-based JCCPAPO) and f₂ being clearly non-convex (favoring the global-search EMOMVO-CGD).
- JCCPAPO (the classical step-wise scheme) is competitive and useful as a fast, interpretable benchmark.

## Limitations

- No computation offloading — pure communication paper. Pairs with [[wang-2026-aerial-marine-msar]] for the full stack.
- Single HAP, no inter-HAP coordination.
- Vessels are treated as quasi-static within a slot.

## Cross-link with related sources

- **Maritime track:** alongside [[wang-2026-aerial-marine-msar]]. Together, they cover the wiki's maritime communication + maritime MEC stack.
- **HAP-as-backhaul:** distinct architectural role from HAP-as-compute ([[peng-2025-drudm-cfg]], [[wang-2026-aerial-marine-msar]]) and HAP-as-relay-with-NOMA ([[hsu-2025-drl-hues-hap-noma]]). All three roles are now in the corpus and worth a `hap-roles-in-mec` synthesis.
- **NOMA-multicast:** complements the [[noma]] usage in [[hsu-2025-drl-hues-hap-noma]] and [[qin-2025-bcuav-masac]].

## Raw artifacts

- `raw/sources/HAP-UAV-Assisted_Maritime_IoT_Communication_Network/HAP-UAV-Assisted_Maritime_IoT_Communication_Network.md`
