---
type: source
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
created: 2026-05-29
updated: 2026-06-01
---

# Generative-Adversarial-Network-Enhanced DRL for ISAC With Double Active RISs

## Citation

Zhang, J., Sheng, M., Xing, C., Liu, J., Zhao, N., & Karagiannidis, G. K. (2025). *Generative-Adversarial-Network-Enhanced DRL for ISAC With Double Active RISs*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3527441.

## TL;DR

Beamforming design for a **double-active-RIS-assisted ISAC** network where direct ISAC-BS→user links may be blocked. Two active RISs build virtual LoS links; the design maximizes the sum of the minimum sensing SINRs across multiple targets over a series of time slots, subject to QoS and transmit-power constraints, by jointly optimizing transmit, reflection, and receive beamforming. The non-convex problem is turned into an MDP and solved with **TD3**; a **GAN is integrated into TD3 (GAN-TD3)** to improve generalization and stability — at the cost of higher complexity and slower convergence.

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

- Simulations show effectiveness of both algorithms and the superiority of active RIS over passive RIS. **GAN-TD3 beats plain TD3 in convergence speed and stability, at the cost of higher computational complexity** (the paper's stated trade-off).

## Limitations / future work

Simulation-only; GAN-TD3's gains come with higher complexity/slower convergence. The parse does not enumerate further limitations.

## Relation to the corpus

A **generative-AI-enhanced DRL** entry in the ISAC track. It pairs naturally with [[faisal-2025-cgan-ris-isac-channel]] (CGAN for RIS-ISAC channel *estimation*) — together they show GANs entering ISAC at both the estimation and policy-learning layers — and with the diffusion-as-optimizer work [[ye-2025-aigc-diffusion-contract]] and [[peng-2025-drudm-cfg]] under the broader [[generative-ai-for-mec]] umbrella. Reinforces [[td3]], [[intelligent-reflecting-surface]], and introduces [[generative-adversarial-network]].

## Raw artifacts

- `raw/sources/Generative-Adversarial-Network-Enhanced_DRL_for_ISAC_With_Double_Active_RISs/full.md`
- Original PDF and extracted figures in the same folder.
