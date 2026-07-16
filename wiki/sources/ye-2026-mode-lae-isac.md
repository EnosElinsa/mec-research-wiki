---
type: source
title: "Multi-Objective ISAC for Low-Altitude Economy Based on Multi-Task Deep Reinforcement Learning With Mixture of Experts"
authors: ["Xiaowen Ye", "Hengyi Lin", "Xianxin Song", "Yi Wu", "Liqun Fu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3693366"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-economy, isac, multi-objective-optimization, mixture-of-experts-drl, ddpg, uav-trajectory-control]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[mixture-of-experts-drl]]"
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[ye-2026-meta-deepesc-lae-isac]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# Multi-Objective ISAC for Low-Altitude Economy Based on Multi-Task Deep Reinforcement Learning With Mixture of Experts

## Citation

Ye, X., Lin, H., Song, X., Wu, Y., & Fu, L. (2026). *Multi-Objective ISAC for Low-Altitude Economy Based on Multi-Task Deep Reinforcement Learning With Mixture of Experts*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3693366. DOI/venue/year are parse-visible and title-matched to Crossref/IEEE metadata.

## TL;DR

Extends the LAE ISAC line from a fixed communication- or energy-centric objective to a Pareto-style communication/sensing tradeoff. A GBS serves authorized UAVs and senses an unauthorized mobile target; MODE wraps [[ddpg]] in a multi-task [[mixture-of-experts-drl]] architecture so one controller can adapt across objective-preference weights without retraining from scratch.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna ground base station communicates with authorized UAVs and senses an unauthorized moving target. Authorized UAVs fly fixed-altitude missions while communication and sensing compete for transmit power and spatial degrees of freedom.

**Problem & objective**: Problem (6) jointly maximizes expected communication sum-rate and target sensing SNR, $\max(\mathbb E[\sum_tR_{\mathrm{total}}(t)],\mathbb E[\sum_t\Gamma_{\mathrm{tar}}(t)])$, with preference $b\in[0,1]$ scalarizing the two returns.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beamforming | $\mathbf W_c(t)$ | complex continuous | Downlink beams for authorized UAVs |
| Sensing beamforming | $\mathbf W_s(t)$ | complex continuous | Target probing beams |
| UAV movement direction | $\mathbf a_u(t)$ | continuous angles | Per-slot headings of authorized UAVs |
| UAV trajectory | $\mathbf u_k(t)$ | continuous positions | Horizontal trajectory of UAV $k$ |
| Objective preference | $b$ | continuous, $[0,1]$ | Weight on communication versus sensing return |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 6b | Constant-speed motion satisfies $\|\mathbf u_k(t+1)-\mathbf u_k(t)\|_2=v_k\Delta_t$ |
| 6c | Every authorized UAV starts and finishes at prescribed mission locations |
| 6d-6e | UAV-to-UAV and UAV-to-target distances remain at least $D_{\min}$ |
| 6f | Communication and sensing beam powers jointly remain below $P_{\max}$ |
| Preference | The scalar return is $\sum_l[b,1-b]^T\mathbf r(l+1)$ |

**Algorithm**: MODE models each preference weight as a related task and uses DDPG for continuous beamforming and heading actions. A shared mixture-of-experts actor-critic uses learned gating across tasks, constrained action selection enforces motion and power structure, and hybrid replay trains from complete episode sets stored in preference-specific buffers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ye et al. [x] formulated LAE ISAC control as a two-objective problem that trades expected communication sum-rate against target sensing SNR. The ground base station jointly selects communication beams, sensing beams, and authorized-UAV trajectories under mission, collision, speed, and transmit-power constraints. MODE combines continuous-control DDPG with a multi-task mixture-of-experts network, constrained action selection, and episode-level hybrid replay. A preference weight conditions one trained controller to produce different communication-sensing tradeoffs without retraining a separate policy for every weight. At preference weight 0.6, MODE began with 18.82% higher sum-rate and 35.52% higher sensing SNR than the no-warm-start variant and required 68.81% fewer time slots to converge. Across the evaluated preference and flight-period sweeps, it produced more Pareto-efficient outcomes and outperformed the listed ablations and actor-critic baseline on both objectives.

## Problem framing

LAE-oriented terrestrial ISAC must simultaneously keep authorized UAVs connected and sense unauthorized UAVs. Prior LAE ISAC work in the parse is framed as optimizing one objective under constraints, while practical deployment needs a tunable tradeoff between communication sum-rate and sensing SNR over a whole flight mission.

## System model

The system has one GBS, multiple authorized UAVs with mission-completion and collision-avoidance constraints, and one unauthorized mobile target. The decision variables are the GBS communication/sensing beamforming matrices and the authorized-UAV trajectories. The optimization maximizes expected communication sum-rate and expected sensing SNR over a finite flight mission under maximum GBS transmit power and UAV feasibility constraints.

## Method

The paper reformulates the two-objective problem as an episode multi-objective MDP by introducing a reward vector and an objective-preference weight. MODE uses DDPG for continuous beamforming/trajectory variables, adds a shared-gating/shared-expert MoE network for multiple preference-weight tasks, and trains with hybrid experience replay that samples whole episode experience sets across task-specific buffers.

## Key findings

- The parse reports that MODE achieves more Pareto-efficient solutions than MODE-c, MODE-w, MODE-o, and actor-critic baselines.
- At objective-preference weight `b = 0.6`, MODE starts around 18.82% higher in sum-rate and 35.52% higher in sensing SNR than the variant without multi-task MoE warm-starting, and needs 68.81% fewer time slots to converge than that variant.
- Across preference weights from 0.2 to 0.8, MODE is reported to exceed MODE-o, MODE-c, and AC by more than 12.38%, 7.13%, and 24.11% in sum-rate and by more than 13.58%, 8.96%, and 24.23% in sensing SNR.
- Across tested flight-period lengths, MODE is reported to exceed MODE-o, MODE-c, and AC by more than 12.00%, 6.84%, and 21.90% in sum-rate and by more than 14.59%, 9.17%, and 27.11% in sensing SNR.

## Limitations / future work

Evaluation is simulation-based. The conclusion states future work should move beyond a single-GBS scenario toward network-level LAE ISAC with multiple GBSs and sensing metrics such as detection probability and CRB rather than relying only on sensing SNR.

## Relation to the corpus

This paper is a direct neighbor of [[ye-2026-deeplsc-lae-isac]] and [[ye-2026-meta-deepesc-lae-isac]]: all three use LAE-oriented GBS beamforming plus authorized-UAV trajectory control, but this source makes the communication/sensing objective preference explicit and reusable through [[mixture-of-experts-drl]]. It strengthens [[integrated-sensing-and-communication]], [[low-altitude-intelligent-network]], and [[uav-trajectory-control]] while adding a multi-objective learning counterpart to the corpus's classical Pareto and DRL sources.

## Raw artifacts

- `raw/sources/Multi-Objective ISAC for Low-Altitude Economy Based on Multi-Task Deep Reinforcement Learning With Mixture of Experts/Multi-Objective ISAC for Low-Altitude Economy Based on Multi-Task Deep Reinforcement Learning With Mixture of Experts.md`
- Original PDF and extracted figures (`images/`) in the same folder.
