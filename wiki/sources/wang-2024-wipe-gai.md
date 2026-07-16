---
type: source
modeling_card: required
title: "A Unified Framework for Guiding Generative AI With Wireless Perception in Resource Constrained Mobile Edge Networks"
authors: ["Jiacheng Wang", "Hongyang Du", "Dusit Niyato", "Jiawen Kang", "Zehui Xiong", "Deepu Rajan", "Shiwen Mao", "Xuemin Shen"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3377226"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, generative-ai, aigc, wireless-perception, diffusion-model-as-optimizer, mobile-aigc-network, resource-allocation, edge-computing]
related:
  - "[[wireless-perception]]"
  - "[[generative-ai-for-mec]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[mobile-aigc-network]]"
  - "[[aigc-service-provider]]"
  - "[[reverse-auction-incentive]]"
  - "[[wang-gai-isac-physical-layer]]"
  - "[[du-2024-d2sac-aigc-asp-selection]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[xu-2024-mobile-aigc-survey]]"
  - "[[jiacheng-wang]]"
  - "[[dusit-niyato]]"
  - "[[jiawen-kang]]"
  - "[[xuemin-shen]]"
  - "[[zehui-xiong]]"
created: 2026-06-02
updated: 2026-07-16
---

# A Unified Framework for Guiding Generative AI With Wireless Perception in Resource Constrained Mobile Edge Networks

## Citation

Wang, J., Du, H., Niyato, D., Kang, J., Xiong, Z., Rajan, D., Mao, S., & Shen, X. (2024). *A Unified Framework for Guiding Generative AI With Wireless Perception in Resource Constrained Mobile Edge Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3377226. (Manuscript received 2 September 2023; revised 8 January 2024; accepted 1 March 2024; date of publication 14 March 2024; date of current version 3 October 2024 → year 2024.)

## TL;DR

**WiPe-GAI** — a framework that uses **wireless perception to guide generative AI (GAI)** for AI-generated-content (AIGC) services in resource-constrained mobile edge networks, with virtual-character generation as the running example. Two coupled pieces: (1) a **sequential multi-scale perception (SMSP)** algorithm that builds a CSI feature matrix from wireless signals and feeds a trained network to predict the user's **skeleton** (posture), which then guides the GAI model to generate a matching virtual character; and (2) a **pricing-based incentive mechanism** whose **optimal pricing strategy is produced by a diffusion model**, maximizing user utility while keeping the virtual service provider (VSP) willing to participate. The paper reports experiments showing accurate skeleton prediction and pricing strategies that beat existing solutions in user utility while ensuring VSP participation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A mobile-edge virtual service provider runs wireless perception and generative-AI character generation for a user, with CSI-derived skeleton quality, image quality, limited compute resources, and a price paid per unit of service quality.

**Problem & objective**: The incentive problem maximizes user utility, $\max_{v_r,I_b,\chi_s,\chi_{ag}}U_{us}(v_r,I_b,\chi_s,\chi_{ag})$, while inducing a utility-maximizing provider response.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| QoS price | $v_r$ | continuous, nonnegative | User payment per quality unit |
| Basic fee | $I_b$ | continuous, nonnegative | Fixed payment to the provider |
| Perception compute | $\chi_s$ | continuous, nonnegative | Resources allocated to wireless perception |
| AIGC compute | $\chi_{ag}$ | continuous, nonnegative | Resources allocated to character generation |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Provider resources are chosen as a utility best response: $(\chi_s',\chi_{ag}')\in\arg\max U_{vsp}$. |
| C2 | Total provider compute is bounded: $\chi_s'+\chi_{ag}'\leq E_t$. |
| C3 | Provider participation requires $U_{vsp}(\chi_s',\chi_{ag}',v_r,I_b)\geq U_{th}$. |
| C4 | User utility is $U_{us}=(v_m-v_r)Q_t-I_b$, with $Q_t$ combining perception and AIGC quality. |

**Algorithm**: Extract CSI features and skeletons with sequential multi-scale perception, generate virtual characters from the inferred pose, and train a conditional diffusion model with Q-learning to produce pricing actions; the provider then solves its resource response by convex optimization.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] propose WiPe-GAI, which uses wireless CSI perception to guide virtual-character generation at a mobile edge provider. The paper also formulates a pricing and resource-allocation problem that maximizes user utility through a QoS price, basic fee, and provider compute split under a provider best response, capacity bound, and participation threshold. A sequential multi-scale perception pipeline supplies the skeleton, while a conditional diffusion model with Q-learning generates pricing strategies and convex optimization completes the provider response. Experiments report accurate skeleton and character generation together with user utility gains over existing pricing solutions while preserving provider participation.

## Problem framing

GAI models are unstable: random seeds and the difficulty of conveying user posture through text prompts mean generated characters may not match the actual user, forcing repeated requests that waste edge resources and degrade VSP quality of service. Guiding GAI with side information helps, but the VSP's edge compute is limited, so a second problem is how to **incentivize** the VSP to participate. WiPe-GAI addresses both: wireless perception (instead of cameras) supplies the guidance — improving privacy and coverage via the ubiquity of wireless signals — and a pricing payment plan between user and VSP supplies the incentive.

## System model

- **Actors.** A user requesting AIGC service and a **virtual service provider (VSP)** deployed at the mobile edge that runs perception + GAI generation, mediated by a pricing-based incentive.
- **Perception inputs.** OFDM-modulated signals between wireless APs; CSI matrices over antennas × subcarriers, with AoA and ToF jointly estimated (2D MUSIC) to localize the user and weight links by proximity (Fresnel-zone-motivated).
- **Service flow.** (A) user requests; (B) diffusion model generates the optimal pricing strategy under current conditions; (C) if the resulting utility meets the VSP threshold, the VSP runs SMSP → skeleton prediction → GAI virtual-character generation.
- **Incentive model.** User pays a per-unit-QoS price plus a base fee; VSP has a unit compute cost and a utility threshold; the optimization seeks a price that maximizes user utility while keeping VSP utility above threshold.

## Method

- **SMSP (sequential multi-scale perception).** Large-scale perception localizes the user from CSI (link-distance scoring weights more-informative links); small-scale perception then analyzes per-link signal-fluctuation variance using the user's estimated direction. The two scales cooperate by sharing results to build a more informative CSI feature matrix for skeleton prediction by a trained neural network.
- **Skeleton-guided GAI.** The predicted skeleton plus the user prompt conditions the GAI model (the parse describes a ControlNet-style encoder / trainable-copy / zero-convolution structure) to generate the virtual character.
- **Diffusion-based pricing.** A **diffusion model generates the optimal pricing strategy** (a [[diffusion-model-as-optimizer]] instance) by learning to denoise toward high-utility strategies conditioned on current conditions such as the unit cost of computing resources.

## Key findings

- WiPe-GAI accurately predicts the user skeleton and generates a corresponding virtual character (the paper's stated experimental result).
- The diffusion-based pricing method yields **greater user utility than existing methods** while still ensuring the VSP's participation, improving overall framework efficiency (the paper's stated result). Specific numeric margins are reported in the parse's figures rather than as headline numbers, so treat exact gains as indicative.
- Wireless-perception guidance is argued to improve privacy (less camera exposure) and coverage (signal ubiquity) relative to image/video-guided AIGC.

## Limitations / future work

A simulation/experimental study around a single virtual-character use case; the paper does not claim deployment at scale. The perception accuracy depends on AP geometry and channel-coherence assumptions, and the incentive analysis is scoped to the user–VSP pair. Generalization beyond the gaming/AR virtual-character scenario is not established in the parse.

## Relation to the corpus

A **generative-AI MEC** entry that pairs the diffusion-as-optimizer pattern with a **wireless-perception** front end, distinguishing it from the corpus's other diffusion-for-decisions work: [[du-2024-d2sac-aigc-asp-selection]] (diffusion selects AIGC service providers), [[ye-2025-aigc-diffusion-contract]] (diffusion generates [[contract-theory]] items), and [[peng-2025-drudm-cfg]] (classifier-free-guided diffusion for MEC). Its physical-layer perception sensibility connects to [[wang-gai-isac-physical-layer]], and it sits under the AIGC-services umbrella surveyed in [[xu-2024-mobile-aigc-survey]] ([[mobile-aigc-network]]). Shares the Jiacheng Wang / Hongyang Du / Dusit Niyato / Jiawen Kang / Xuemin Shen author neighborhood ([[jiacheng-wang]], [[dusit-niyato]], [[jiawen-kang]], [[xuemin-shen]] are confirmed entities; Hongyang Du remains intentionally un-promoted).

## Raw artifacts

- `raw/sources/A_Unified_Framework_for_Guiding_Generative_AI_With_Wireless_Perception_in_Resource_Constrained_Mobile_Edge_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
