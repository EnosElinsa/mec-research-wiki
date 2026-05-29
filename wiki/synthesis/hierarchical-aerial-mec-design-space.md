---
type: synthesis
title: "The hierarchical aerial MEC (UAV+HAP) design space"
tags: [synthesis, hierarchical-aerial-mec, hap, uav, comparison]
related:
  - "[[peng-2025-drudm-cfg]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[two-stage-decomposition]]"
  - "[[load-balancing-uav-mec]]"
  - "[[csi-estimation-error]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
created: 2026-05-29
updated: 2026-05-29
---

# The hierarchical aerial MEC (UAV+HAP) design space

The wiki's **hierarchical aerial MEC** track is now five sources strong, and they make different design choices on every axis: backbone, decomposition, channel model, objective stack, HAP role. This page walks through those axes and highlights where the design space partitions cleanly vs where it doesn't.

## Roster

| Source | Backbone family | HAP role | Decomposition | Notable knob |
|---|---|---|---|---|
| [[peng-2025-drudm-cfg]] | MA-DRL with [[adaptive-entropy-priority-replay\|AEP]] | HAS-style aerial server (multi-UAV under one HAP) | Joint MA-POMDP | **Fairness reward** ([[theil-fairness-index]]) for post-disaster |
| [[nabi-2025-jour-hierarchical-aerial]] | ESAC (SAC + PER) | Compute server (after UAV partial offload) | **Two-stage** (Gale-Shapley → SAC) | Load-balancing penalty in reward |
| [[bao-2025-ddpg-video-offloading]] | DDPG | Compute server (after video transcode) | Joint single-agent | **Video transcoding** decision in action space |
| [[jia-2025-dro-uav-hap-mec]] | None (classical) | Compute server (overflow tier) | Primal decomp + WKD pre-stage | **DRO + CVaR** under uncertain CSI |
| [[wang-2026-aerial-marine-msar]] | None (classical) | Compute server alongside MASS tier | Two-stage matching + convex | **Three-tier** (UAV + MASS + HAP) |

## Architectural patterns

### HAP-as-compute (4 of 5)

Most sources put the HAP at the top of the offloading hierarchy as a deeper compute tier than UAVs — bigger battery, larger payload, slower link. UAVs collect data and relay it upward when their local compute is saturated. The implicit model: HAP energy is unbounded, latency to HAP is the only friction.

[[hsu-2025-drl-hues-hap-noma]] (in the SAGIN track, not strictly hierarchical-aerial-MEC) disagrees with this assumption — the HAP there is energy-constrained and runs out. Worth keeping that counterexample in mind when reading the four sources here.

### HAP-as-coordinator vs HAP-as-pure-server

A subtle split:

- **Coordinator** — HAP sees all traffic and runs a global optimizer ([[peng-2025-drudm-cfg]]'s HAS centralizes admission + allocation).
- **Pure server** — HAP just executes offloaded compute; the coordinator is somewhere else ([[nabi-2025-jour-hierarchical-aerial]]'s GU coordinator, [[jia-2025-dro-uav-hap-mec]]'s primal decomposition).

The split matters because coordinator-HAP designs scale worse — every offloading decision has to traverse the HAP — but interactive-control designs require it.

### Hub-and-spoke vs additional sea-surface tier

[[wang-2026-aerial-marine-msar]] is the only source with a **third compute tier** (MASSs as sea-surface servers between UAVs and HAP). The matching-based server selection there has to weigh proximity (MASS) against capacity (HAP), which is genuinely a different optimization shape than the others. Future urban-mobility analogs (RSU + UAV + HAP, e.g.) would likely re-discover this pattern.

## Solver-family split

Three of five (`bao-2025`, `nabi-2025`, `peng-2025`) use DRL; two (`jia-2025`, `wang-2026`) use classical / metaheuristic methods. The split correlates with what they care most about:

- **DRL** wins when the optimization is **online, recurring, scalar-reward** with stable channel statistics. Train once, deploy fast.
- **Classical** wins when **provable robustness** matters ([[jia-2025-dro-uav-hap-mec]]'s DRO under uncertain CSI), or when the structure is **highly decomposable** ([[wang-2026-aerial-marine-msar]]'s clean four-subproblem split).

[[two-stage-decomposition]] cuts across both — `nabi-2025` (DRL second stage), `jia-2025` (classical second stage with BWOA on the binary), `wang-2026` (classical both stages). The two-stage frame seems to be the most portable design pattern in the track.

## Common objective shapes

Every source minimizes some weighted combination of latency + energy. They differ on what *else* enters the objective:

| Source | Latency | Energy | Other |
|---|---|---|---|
| [[peng-2025-drudm-cfg]] | ✓ | ✓ | Theil fairness |
| [[nabi-2025-jour-hierarchical-aerial]] | ✓ | ✓ | UAV-load variance ([[load-balancing-uav-mec]]) |
| [[bao-2025-ddpg-video-offloading]] | ✓ | (implicit) | **Video bitrate** ([[qoe-modeling-mec]]) |
| [[jia-2025-dro-uav-hap-mec]] | ✓ (chance constraint) | ✓ (sole objective: total energy) | (none) |
| [[wang-2026-aerial-marine-msar]] | ✓ | ✓ | (none beyond CO weighted sum) |

Nothing surprising in the latency + energy core. The third-axis choices are workload-specific: fairness for disaster relief, load balance for swarm longevity, bitrate for video analytics. None of the third-axis choices transfers cleanly across workloads.

## What the design space does NOT settle

### When to put trajectory in the action space

Three of five sources hold UAV positions *fixed* during the planning window: [[bao-2025-ddpg-video-offloading]] (UAVs fly fixed circular paths), [[nabi-2025-jour-hierarchical-aerial]] (static UAV positions), and [[wang-2026-aerial-marine-msar]] (UAV positions and MASS positions both static-per-slot). One source ([[peng-2025-drudm-cfg]]) puts UAV trajectory directly in the DRL action vector (flight angle θ, flight speed ϑ). [[jia-2025-dro-uav-hap-mec]] is in between: it computes a *one-shot UAV deployment* (placement) via Weighted K-means before the per-slot offloading optimization, but the UAVs are quasi-stationary after deployment — so it has placement, not trajectory.

The argument for joint trajectory: UAV position determines channel quality, which determines optimal offloading, which determines optimal trajectory — the loop is real. The argument for fixed trajectory: in many deployments (post-disaster, search-and-rescue) the trajectory is operationally constrained and not a free decision variable anyway.

The wiki has no head-to-head on the same scenario, so this stays open.

### How HAP latency is modeled

Three sources treat the HAP transmission link as a static rate $r_h$ (no fading, no overhead). One ([[jia-2025-dro-uav-hap-mec]]) accepts that the *G2U* link has CSI uncertainty but *U2H* link is deterministic. None models *atmospheric* effects (rain, ducting) on the HAP link, despite this being a real concern at 20 km altitude.

If a future source documents materially different HAP-link dynamics (e.g. weather-dependent rate variations), the latency models above will need refresh.

### Interaction between security and the hierarchical stack

Only [[benaya-2025-aerial-isac-haps]] and [[qin-2025-bcuav-masac]] put physical-layer security on this kind of stack — and neither is in this synthesis's main roster (Benaya is ISAC, Qin is multi-agent UAV-MEC, neither is hierarchical-aerial-MEC strictly). The hierarchical-aerial-MEC track currently has **no source** that puts security/trust on the UAV → HAP path. That's a real gap given how much sensitive data flows through the HAP tier.

## Practical guidance distilled from the five sources

If you're designing a hierarchical-aerial-MEC system and choosing between the canonical patterns:

1. **Start with two-stage decomposition.** Gale-Shapley or many-to-one matching for user-UAV / UAV-HAP association; then optimize the continuous resource allocations conditional on the matching. This is the most reliable scaffold.
2. **Default to DRL only for the continuous stage.** The discrete stage benefits from the determinism of classical methods. [[nabi-2025-jour-hierarchical-aerial]] is the cleanest demonstration of this pattern.
3. **Add a third objective only when it's load-bearing for the use case.** Latency + energy is the universal core. Adding fairness for disaster relief, load balance for swarm longevity, bitrate for video — pick at most one beyond the core, and tie it to a real operational concern.
4. **Don't assume HAP energy is unbounded.** The five-source roster does, but [[hsu-2025-drl-hues-hap-noma]] shows the assumption breaks at HAP scale. If your deployment is multi-day or solar-powered, model HAP energy explicitly.
5. **If CSI uncertainty is operationally real, don't paper over it.** Either go DRO ([[jia-2025-dro-uav-hap-mec]]) or pre-measure ([[wang-2026-aerial-marine-msar]] for shipping routes). Pretending CSI is exact is a recipe for QoS violations at deployment time.

## Open questions

- **Three-tier extension.** [[wang-2026-aerial-marine-msar]] adds MASSs. The terrestrial analog (RSU + UAV + HAP) and the dense-urban analog (small cell + UAV + HAP) are unstudied in the wiki. Would the matching-based server selection re-emerge naturally?
- **Online tuning of the HAP-vs-UAV split.** All five sources fix the offloading-tier-selection rule by training once. A continual-learning variant that tracks demand drift would be welcome; the wiki has no example.
- **Joint trajectory + offloading + DRO.** [[jia-2025-dro-uav-hap-mec]] handles the latter two, [[peng-2025-drudm-cfg]] handles the former two, no source handles all three. The intersection is operationally important and methodologically open.

## See also

- [[drl-backbones-across-uav-mec-sources]] — DRL-track view, with the two DRL entries above analyzed alongside the rest of the corpus.
- [[cmop-evolutionary-uav-mec-lineage]] — non-DRL, non-classical UAV-MEC track. Almost no overlap with this hierarchical-aerial-MEC track yet — the lineage focuses on UAV-only or aerial-marine, not UAV+HAP.
- [[drl-vs-evolutionary-vs-classical-solvers]] — cross-corpus solver-family synthesis.
- [[two-stage-decomposition]] — the recurring solver pattern in this track.
