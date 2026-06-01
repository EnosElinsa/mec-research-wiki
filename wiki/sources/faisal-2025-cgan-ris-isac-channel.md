---
type: source
title: "Conditional Generative Adversarial Networks for Channel Estimation in RIS-Assisted ISAC Systems"
authors: ["Alice Faisal", "Ibrahim Al-Nahhal", "Kyesan Lee", "Octavia A. Dobre", "Hyundong Shin"]
year: 2025
url: "https://doi.org/10.1109/TCOMM.2025.3541047"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, isac, intelligent-reflecting-surface, channel-estimation, generative-adversarial-network, deep-learning]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[conditional-gan]]"
  - "[[csi-estimation-error]]"
  - "[[generative-ai-for-mec]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
created: 2026-05-29
updated: 2026-06-01
---

# Conditional Generative Adversarial Networks for Channel Estimation in RIS-Assisted ISAC Systems

## Citation

Faisal, A., Al-Nahhal, I., Lee, K., Dobre, O. A., & Shin, H. (2025). *Conditional Generative Adversarial Networks for Channel Estimation in RIS-Assisted ISAC Systems*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2025.3541047.

## TL;DR

Applies **conditional GANs (CGANs)** to channel estimation in a **[[intelligent-reflecting-surface|RIS]]-assisted [[integrated-sensing-and-communication|ISAC]]** system. A generator learns the mapping from observed pilots to the true channel while a discriminator's feedback sharpens it adversarially, improving estimation accuracy and stability over conventional deep-learning estimators. Two variants are proposed — CE-CGAN and SE-CGAN — with complexity analyzed against a benchmark.

## Problem framing

RIS improves ISAC by shaping the propagation environment, but accurate channel estimation is essential for reliable deployment. Conventional deep-learning estimators struggle to model the complex dynamics of RIS-assisted ISAC channels. The paper poses channel estimation as a learning problem solvable by adversarial training.

## System model / method

- **CGAN framework.** Two networks trained adversarially: the generator maps observed data to channel estimates; the discriminator provides feedback that the generator uses to refine its output.
- **Variants.** CE-CGAN keeps complexity comparable to existing DL methods while improving accuracy; SE-CGAN reportedly improves both performance and computational complexity over the existing estimation model.

## Key findings

- Numerical simulations show the CGAN approach improves estimation performance across different SNR conditions and system dimensions versus conventional DL techniques.
- CE-CGAN's complexity is comparable to existing DL methods at better accuracy; SE-CGAN improves on both fronts (qualitative claims; exact NMSE/complexity curves are in the paper).

## Limitations / future work

Simulation-only. The authors flag multi-target scenarios with user/target mobility and wideband deployments as future directions.

## Relation to the corpus

Extends the wiki's **generative-AI-for-wireless** thread into channel estimation, complementing [[zhang-2025-gan-td3-isac-active-ris]] (GAN-enhanced DRL for ISAC beamforming with active RIS) — both pair a GAN with ISAC/RIS but at different layers (estimation vs. policy learning). Connects to the ISAC line ([[benaya-2025-aerial-isac-haps]], [[jiang-2025-isac-lae-overview]]) and to [[intelligent-reflecting-surface]] / [[generative-ai-for-mec]]. Introduces [[conditional-gan]] to the corpus.

## Raw artifacts

- `raw/sources/Conditional_Generative_Adversarial_Networks_for_Channel_Estimation_in_RIS-Assisted_ISAC_Systems/full.md`
- Original PDF and extracted figures in the same folder.
