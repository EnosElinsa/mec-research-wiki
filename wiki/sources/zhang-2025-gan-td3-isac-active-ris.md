---
type: source
modeling_card: required
title: "Generative-Adversarial-Network-Enhanced DRL for ISAC With Double Active RISs"
authors: ["Jifa Zhang", "Min Sheng", "Chengwen Xing", "Junyu Liu", "Nan Zhao", "George K. Karagiannidis"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3527441"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, isac, intelligent-reflecting-surface, generative-adversarial-network, td3, beamforming, drl]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[td3]]"
  - "[[generative-adversarial-network]]"
  - "[[generative-ai-for-mec]]"
  - "[[faisal-2025-cgan-ris-isac-channel]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
  - "[[george-k-karagiannidis]]"
  - "[[chengwen-xing]]"
created: 2026-05-29
updated: 2026-07-16
---

# Generative-Adversarial-Network-Enhanced DRL for ISAC With Double Active RISs

## Citation

Zhang, J., Sheng, M., Xing, C., Liu, J., Zhao, N., & Karagiannidis, G. K. (2025). *Generative-Adversarial-Network-Enhanced DRL for ISAC With Double Active RISs*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3527441.

## TL;DR

Beamforming design for a **double-active-RIS-assisted ISAC** network where direct ISAC-BS→user links may be blocked. Two active RISs build virtual LoS links; the design maximizes the sum of the minimum sensing SINRs across multiple targets over a series of time slots, subject to QoS and transmit-power constraints, by jointly optimizing transmit, reflection, and receive beamforming. The non-convex problem is turned into an MDP and solved with **TD3**; a **GAN is integrated into TD3 (GAN-TD3)** to improve generalization and stability — at the cost of higher complexity and slower convergence.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An ISAC BS serves multiple users and senses multiple targets through two active RISs when direct links are blocked. Amplified reflection creates virtual LoS paths, while transmit, reflection, and receive beams interact across slots.

**Problem & objective**: A dynamic non-convex MDP maximizes summed worst-target sensing SINR, $\max\sum_t\min_j\operatorname{SINR}^{\mathrm{sense}}_j(t)$, under communication QoS and power limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| BS transmit beam | $\mathbf w_k(t)$ | complex continuous vector | User and sensing transmission beam |
| Active-RIS coefficients | $\boldsymbol\phi_r(t)$ | complex bounded vector | Amplifying reflection at RIS $r$ |
| Receive beam | $\mathbf u_j(t)$ | complex continuous vector | Combiner for target $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every user meets the required communication QoS |
| C2 | BS transmit power remains within its budget |
| C3 | Each active RIS satisfies amplitude and amplification-power limits |
| C4 | Receive and reflection coefficients remain in their feasible domains |

**Algorithm**: Cast channel and beam state as an MDP → let TD3 generate continuous transmit, RIS, and receive beam actions → use twin critics and delayed actor updates → train a GAN on action/state experience to enrich policy generalization → combine GAN guidance with TD3 updates → repeat over channel states.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied ISAC beamforming with two active RISs under blocked direct links. They formulated summed minimum sensing-SINR maximization over BS transmit beams, active-RIS reflection coefficients, and receive beams under user-QoS, BS-power, and RIS-amplification constraints. The non-convex dynamic problem is represented as an MDP and first solved with TD3. GAN-TD3 integrates a generative adversarial network with the actor-critic updates to improve policy stability and generalization. Simulations report higher sensing performance than the evaluated TD3 and passive-RIS configurations, with additional complexity and slower convergence.

## Problem framing

ISAC shares spectrum for sensing and communication, but obstacles block BS→user links. Active RISs (which amplify, unlike passive RIS) establish virtual LoS. The dynamic, highly-coupled beamforming optimization is non-convex; DRL handles the dynamics, and a GAN augments the DRL policy for robustness.

## System model

- **Network.** ISAC BS, two **active** RISs, multiple users and sensing targets.
- **Objective.** Maximize the sum of minimum detection SINRs among targets over time slots, under QoS and transmit-power limits.
- **Variables.** Transmit beamforming, reflection beamforming (RIS), receive beamforming.

## Method

- Transform the non-convex problem into an **MDP**.
- **TD3** baseline; **GAN-TD3** integrates a generative adversarial network into TD3 to enhance generalization and stability ([[td3]] + [[generative-adversarial-network]]).

## Key findings

- Simulations show effectiveness of both algorithms and the superiority of active RIS over passive RIS. **GAN-TD3 improves performance and stability over plain TD3, at the cost of higher computational complexity and slower convergence speed** (the paper's stated trade-off).

## Limitations / future work

Simulation-only; GAN-TD3's gains come with higher complexity/slower convergence. The parse does not enumerate further limitations.

## Relation to the corpus

A **generative-AI-enhanced DRL** entry in the ISAC track. It pairs naturally with [[faisal-2025-cgan-ris-isac-channel]] (CGAN for RIS-ISAC channel *estimation*) — together they show GANs entering ISAC at both the estimation and policy-learning layers — and with the diffusion-as-optimizer work [[ye-2025-aigc-diffusion-contract]] and [[peng-2025-drudm-cfg]] under the broader [[generative-ai-for-mec]] umbrella. Reinforces [[td3]], [[intelligent-reflecting-surface]], and introduces [[generative-adversarial-network]].

## Raw artifacts

- `raw/sources/Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs/full.md`
- Original PDF and extracted figures in the same folder.
