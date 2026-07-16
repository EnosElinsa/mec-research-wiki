---
type: source
title: "Interference-Aware UAV Path Planning on Grid SINR Maps with Event-Triggered Updates"
authors: ["Lantu Guo", "Mengchen Yao", "Han Zhang", "Weiqing Mu", "Yun Lin"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3667780"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, cellular-connected-uav, path-planning, sinr-map, event-triggered-update, uncertainty-quantification, mixture-of-experts, d3qn]
related:
  - "[[uncertainty-triggered-radio-map-update]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[mixture-of-experts-drl]]"
  - "[[dueling-dqn]]"
  - "[[cellular-connected-uav]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Interference-Aware UAV Path Planning on Grid SINR Maps with Event-Triggered Updates

## Citation

Guo, L., Yao, M., Zhang, H., Mu, W., & Lin, Y. (2026). *Interference-Aware UAV Path Planning on Grid SINR Maps with Event-Triggered Updates*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3667780.

> **Metadata grounding note.** The parse contains no DOI/venue/year line. Those fields were verified through the exact-title Crossref record.

## TL;DR

Couples cellular-UAV navigation with bandwidth-aware SINR-map maintenance. UT-Grid uses MC-dropout variance to request a server-to-UAV map refresh only in uncertain regions, while a Top-1 sparse MoE-D3QN plans from local/global SINR grids and UAV position with one active expert per decision.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A cellular-connected UAV navigates a bounded urban grid with mobile interferers while maintaining a SINR map whose refreshes consume downlink bandwidth.

**Problem & objective**: Choose the UAV path, association, and map-refresh decisions to minimize flight time plus weighted outage duration, $\min T+\mu\bar T_{\mathrm{out}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV trajectory | $u(t)$ | feasible grid motion or position sequence | Position selected by the navigation policy |
| Base-station selection | $b(t)$ | discrete element of $\{1,\ldots,M\}$ | Serving cell used at step $t$ |
| Map refresh event | $z_t$ | binary trigger | Request a new global or local SINR map at step $t$ |
| Trigger threshold | $\tau$ | positive configuration scalar | Uncertainty and error threshold controlling refresh frequency |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | The UAV starts and ends at the prescribed grid locations |
| C2 | Every motion action stays inside the bounded airspace and avoids collisions |
| C3 | The serving base station is selected from the available set and follows the link model |
| C4 | Refresh events obey the uncertainty and reconstruction-error trigger |
| C5 | Inference and map communication remain within the prescribed bandwidth and active-parameter budget |

**Algorithm**: Reconstruct SINR maps with a U-Net, estimate uncertainty with 20 MC-dropout passes, trigger UT-Grid refreshes when uncertainty and error exceed $\tau$, and plan motion with a Top-1 mixture-of-experts D3QN.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guo et al. [x] co-designed SINR-map maintenance and connectivity-aware navigation for a cellular UAV moving among mobile urban interferers. Their formal objective minimizes flight time plus weighted expected outage duration over the UAV path and base-station selection under endpoint, airspace, and association constraints. UT-Grid triggers map refreshes from MC-dropout uncertainty, while a Top-1 mixture-of-experts D3QN selects motion from local and global SINR grids with one active expert per step. At threshold 5, the method reports 0.11 updates per step and 84.58% destination reaching, compared with 0.33 updates and 86.27% for three-step periodic refresh, while the eight-expert planner uses 326.5K active parameters and 0.43 ms reported latency.

## Problem framing

Static radio maps become stale around moving interferers, but periodic refreshes spend downlink bandwidth even when the map remains reliable. The paper minimizes flight time plus weighted expected outage duration while treating map freshness as an event-triggered communication decision. The planner must also fit a constrained inference budget.

## System model

- One cellular-connected UAV moves at constant speed through a bounded urban grid among fixed base stations, buildings, and mobile road interferers.
- Strongest-SINR association is implicit in the reconstructed map. The RL action changes UAV position; base-station association is not a separate action.
- A ground station reconstructs the SINR map with a pretrained U-Net from uploaded sensing data. It sends coarse global and fine local maps back to the UAV when the trigger fires.
- Reward combines goal/collision terminal terms, a time-step penalty, and outage probability derived from the current map.

## Method

[[uncertainty-triggered-radio-map-update|UT-Grid]] keeps dropout active for 20 inference passes and uses predictive variance at the UAV's location as its trigger statistic. Threshold tau is the update-budget knob. MoE-D3QN encodes local/global maps with CNN branches, concatenates a position embedding, routes the shared feature to one of several experts, and applies dueling value/advantage heads with Double-DQN target selection.

## Key findings

- With threshold tau=5, the base simulation reports **0.11 updates/step**, return **-113.18**, reaching probability **84.58%**, and mean path length **160.35**. Periodic refresh every 3 steps reports 0.33, -27.84, 86.27%, and 156.17, respectively.
- Thus tau=5 uses about one third of the update traffic while reaching 84.58% versus 86.27%; the paper summarizes this as retaining about 98% of the navigation success with 67% less update traffic.
- The 8-expert Top-1 model reports 2.106M total but 326.5K active parameters, 96.36M FLOPs, 0.43 ms latency, and 84.58% reaching probability. Larger expert configurations attain higher raw success, so eight experts are a cost/performance choice rather than the best success rate.
- Top-4 routing raises reaching probability from 84.58% to 86.14% but increases reported latency from 0.43 to 0.93 ms.

## Limitations / interpretation

Results come from a PyTorch urban simulator on an RTX 4080/i9 host, not onboard flight hardware. The U-Net, map trigger, interference motion, and communication channel remain simulated; one UAV, fixed threshold, constant speed, and strongest-SINR association limit scope. Desktop inference timing does not establish embedded latency or energy. The conclusion's phrase “preserves 84.58% of success rate” confuses the absolute 84.58% success rate with the roughly 98% retention relative to periodic-3. Map traffic direction is server-to-UAV downlink after UAV sensing uploads.

## Relation to the corpus

Extends [[radio-map-aided-uav-path-planning]] from an offline feasibility map to an online freshness/traffic tradeoff, and extends [[mixture-of-experts-drl]] from objective-conditioned actor-critic control to sparse value-based navigation.

## Raw artifacts

- `raw/sources/Interference-Aware_UAV_Path_Planning_on_Grid_SINR_Maps_with_Event-Triggered_Updates/Interference-Aware_UAV_Path_Planning_on_Grid_SINR_Maps_with_Event-Triggered_Updates.md`
- Original PDF and extracted figures (`images/`) in the same folder.
