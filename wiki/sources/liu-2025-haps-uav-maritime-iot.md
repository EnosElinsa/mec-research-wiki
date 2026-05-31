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
updated: 2026-06-01
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

Two solvers: an enhanced multi-verse optimization with chaos + grey-wolf + discrete update (**EMOMVO-CGD**), and a step-wise classical method (**JCCPAPO**: Gale-Shapley-style association → power allocation → PSO-based UAV placement).

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

- `raw/sources/HAP-UAV-Assisted Maritime IoT Communication Network/full.md`
