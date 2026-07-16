---
type: source
modeling_card: not_applicable
title: "Generative AI for Secure Physical Layer Communications: A Survey"
authors: ["Changyuan Zhao", "Hongyang Du", "Dusit Niyato", "Jiawen Kang", "Zehui Xiong", "Dong In Kim", "Xuemin Shen", "Khaled B. Letaief"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2024.3438379"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, generative-ai, physical-layer-security, survey, gan, vae, diffusion-model, authentication, anomaly-detection]
related:
  - "[[generative-diffusion-model]]"
  - "[[variational-autoencoder]]"
  - "[[dusit-niyato]]"
  - "[[xuemin-shen]]"
  - "[[jiawen-kang]]"
  - "[[huynh-2024-gai-physical-layer-survey]]"
  - "[[liang-2025-gai-semcom-survey]]"
  - "[[zehui-xiong]]"
  - "[[khaled-ben-letaief]]"
created: 2026-06-04
updated: 2026-07-16
---

# Generative AI for Secure Physical Layer Communications: A Survey

## Citation

Zhao, C., Du, H., Niyato, D., Kang, J., Xiong, Z., Kim, D. I., Shen, X., & Letaief, K. B. (2025). *Generative AI for Secure Physical Layer Communications: A Survey*. **IEEE Transactions on Cognitive Communications and Networking**, 11(1). DOI: 10.1109/TCCN.2024.3438379. (Received 19 February 2024; accepted 13 July 2024; published 5 August 2024; current version 7 February 2025.)

## TL;DR

A survey focused specifically on **GAI's role in physical layer security (PLS)** — distinct from the broader GAI-for-PHY survey [[huynh-2024-gai-physical-layer-survey]]. Covers GANs, autoencoders (AEs), variational autoencoders (VAEs), and diffusion models (DMs) applied to five PLS dimensions: **communication confidentiality, authentication, availability, resilience**, and **integrity**. Highlights that traditional AI (supervised/DRL) struggles in PLS because evolving threats and channel non-stationarity require adaptive generative modeling. Identifies future directions in multi-scenario deployment, resource-efficient GAI, and secure semantic communication.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] surveyed generative artificial intelligence for secure physical-layer communications. They organized applications across confidentiality, authentication, availability, resilience, and integrity and reviewed GANs, autoencoders, variational autoencoders, and diffusion models. The survey discussed synthetic adversarial data, adaptive channel modeling, anti-jamming training, signal recovery, RF authentication, and anomaly detection. It identified multi-scenario deployment, resource-efficient generative models, and secure semantic communication as future directions. The article is a survey and does not introduce one application-specific decision model with reusable decisions and constraints.

## Problem framing

Physical layer security exploits channel characteristics (fading, noise, interference) to protect data without relying solely on upper-layer cryptography. Traditional ML models are trained in static environments, limiting adaptability when channel conditions or attack patterns shift. GAI models learn underlying data distributions without labeled supervision, enabling them to adapt to unseen conditions, generate synthetic attack data for adversarial training, and model channel behaviors accurately. This survey fills the gap between general AI-for-communications surveys and the specific PLS use case.

## System model

Taxonomic / survey structure rather than a single system model. Five PLS dimensions:

1. **Confidentiality** — preventing eavesdroppers from decoding signals; GAI-generated waveforms/precoding strategies.
2. **Authentication** — verifying transmitter identity from RF fingerprints and channel features; GAN/VAE for data augmentation + classifier training.
3. **Availability** — defending against jamming/DoS; GAN-based jammer simulation for robust policy training.
4. **Resilience** — recovering from attacks or channel disruptions; diffusion-model-aided signal recovery/denoising.
5. **Integrity** — detecting tampering/anomalies in transmitted data; VAE/GAN-based anomaly detection.

GAI model families covered: GANs (adversarial generation), AEs (compact representation + reconstruction), VAEs (probabilistic latent space), Diffusion Models (iterative denoising).

## Key findings

- GAI excels in PLS because it can **generate synthetic adversarial samples** for data-scarce scenarios (authentication, intrusion detection) and **adapt to changing channel statistics** without retraining from scratch (parse Sections I, III–VII).
- Each GAI family has distinct strengths: GANs for data augmentation + jamming simulation; VAEs for anomaly detection + channel distribution modeling; diffusion models for signal recovery (parse Sections III–VII).
- Traditional AI models trained on labeled data from specific environments degrade rapidly under novel attack patterns or channel conditions — a gap GAI's unsupervised/self-supervised learning addresses (parse Section I-A).
- Future directions include resource-efficient GAI for energy/latency-constrained edge PLS, and secure GAI-assisted semantic communication (parse Section VIII).

## Limitations / future work

Pure survey — no new algorithm or simulation results. Scope is physical layer only; application-layer (cryptographic) security is out of scope.

## Relation to the corpus

One of two survey anchors for GAI + physical-layer security in the corpus; the other is [[huynh-2024-gai-physical-layer-survey]] which covers a broader GAI-for-PHY scope (modulation, channel estimation, JSCC, etc.). This paper's tighter PLS focus complements [[ma-2024-covert-mmwave-finite-blocklength]], [[su-2024-sensing-aided-isac-pls]], and the covert/secrecy corpus. NTU/Dusit Niyato ([[dusit-niyato]]) cluster + Waterloo/Xuemin Shen ([[xuemin-shen]]) both co-authored.

## Raw artifacts

- `raw/sources/Generative_AI_for_Secure_Physical_Layer_Communications_A_Survey/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
