---
type: source
modeling_card: not_applicable
title: "Generative AI for Integrated Sensing and Communication: Insights From the Physical Layer Perspective"
authors: ["Jiacheng Wang", "Hongyang Du", "Dusit Niyato", "Jiawen Kang", "Shuguang Cui", "Xuemin (Sherman) Shen", "Ping Zhang"]
year: ""
url: "https://doi.org/10.1109/MWC.013.2300485"
venue: "IEEE Wireless Communications"
tags:
  - source
  - generative-ai
  - integrated-sensing-and-communication
  - physical-layer
  - diffusion-model
  - channel-estimation
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[generative-ai-for-mec]]"
  - "[[generative-diffusion-model]]"
  - "[[generative-adversarial-network]]"
  - "[[conditional-gan]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[csi-estimation-error]]"
  - "[[du-2024-gdm-network-optimization-tutorial]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
  - "[[faisal-2025-cgan-ris-isac-channel]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
created: 2026-05-31
updated: 2026-07-16
---

# Generative AI for Integrated Sensing and Communication: Insights From the Physical Layer Perspective

## Citation

Wang, J., Du, H., Niyato, D., Kang, J., Cui, S., Shen, X. (Sherman), & Zhang, P. *Generative AI for Integrated Sensing and Communication: Insights From the Physical Layer Perspective*. **IEEE Wireless Communications**. DOI: 10.1109/MWC.013.2300485. (Year **not in parse** — the parse has no manuscript-date / volume line.)

## TL;DR
A **magazine overview** of how generative AI (GAI) supports **integrated sensing and communication (ISAC)**, focused on the **physical layer**. It reviews five GAI model families (GANs, normalizing flows, VAEs, diffusion models, Transformers) and their potential support across ISAC's physical, network, and application layers, then analyzes GAI-enhanced physical-layer technologies (channel estimation, CSI compression, signal detection, beamforming) from both sensing and communication perspectives. A **case study** presents a diffusion-based **signal spectrum generator (SSG)** for near-field direction-of-arrival (DoA) estimation when antenna spacing exceeds half the wavelength, achieving a mean square error of **~1.03°**.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] survey how generative models can support sensing and communication functions in the ISAC physical layer. They compare GANs, normalizing flows, VAEs, diffusion models, and Transformers, then discuss channel estimation, CSI compression, signal detection, and beamforming use cases. A near-field signal spectrum generator case study applies diffusion modeling to direction-of-arrival estimation when antenna spacing exceeds the half-wavelength limit. The article is an overview and case study rather than an application-specific decision or control optimization.

## Problem framing
GAI models excel at understanding and modeling complex data distributions, generating new data resembling training data — useful beyond content generation for wireless systems. Integrating GAI into wireless is still limited, especially for emerging near-field communications and **ISAC**. ISAC couples communication and sensing modules with conflicting physical-layer demands — e.g. reliable communication in multipath fading wants **large** antenna spacing for independent signals, while DoA sensing wants spacing **≤ half wavelength** to avoid ambiguities. These tensions, plus resource-allocation complexity across modules, motivate a thorough look at GAI's role in ISAC, especially at the physical layer.

## Scope surveyed
- **Five GAI models** with principles + advantages/disadvantages + potential ISAC support (parse Table 1):
  - **GANs** — generator vs discriminator; parallel generation, end-to-end, but hard to train (Nash equilibrium) and hyperparameter-sensitive.
  - **NFs** — invertible transforms; tractable likelihood; sensitive to base distribution, struggle with discrete data.
  - **VAEs** — encode/decode via latent space; good for high-dimensional/distributed data; posterior collapse risk.
  - **DFMs (diffusion)** — add-noise-then-denoise; flexible, supports per-step probability; low sampling rate (many steps).
  - **Transformers** — self-attention; long-range dependencies + parallelism; hard to interpret, limited variable-size handling.
- **GAI support across ISAC layers:** physical (channel estimation, signal detection/enhancement, beamforming, CSI compression, NOMA, secure transceiver, synchronization); network (resource allocation, scheduling/offloading, incentive mechanisms); application (ISAC data generation/repair/augmentation, distribution modeling, feature extraction, denoising/dimensionality reduction).
- **Physical-layer deep-dive** (beamforming, signal detection) and how GAI-enhanced PHY supports communication + sensing, including a CSI-compression example reporting normalized MSE **−7.05 dB** vs **−2.46 dB** for a deep-learning CS-CsiNet baseline at compression ratio 1/64 (parse, from-sensing-perspective section).

## Key findings (case study)
- **SSG (signal spectrum generator):** a **diffusion-model**-based method tackling **near-field DoA estimation** with **uniform linear arrays whose antenna spacing exceeds half the wavelength** — the regime that normally causes ambiguities.
- Reported **mean square error ≈ 1.03°** in DoA estimation, confirming SSG's effectiveness and, more broadly, that integrating GAI into the ISAC physical layer is worthwhile.

## Limitations / future work
Magazine overview + a single illustrative case study (not a comprehensive benchmark); year not in parse. GAI hurdles noted generically (e.g. diffusion's low sampling rate; GAN training instability). The case study targets one specific near-field DoA setting.

## Relation to the corpus
A **GAI-for-ISAC** overview anchor, complementing the methodological tutorial [[du-2024-gdm-network-optimization-tutorial]] (overlapping Du/Niyato/Kang/Wang authors) and the broader GAI-for-wireless survey [[khoramnejad-2025-gai-wireless-optimization-survey]]. Its physical-layer, generative-channel theme directly frames the corpus's concrete GAN-/diffusion-for-ISAC works: [[faisal-2025-cgan-ris-isac-channel]] ([[conditional-gan]] channel estimation) and [[zhang-2025-gan-td3-isac-active-ris]] (GAN-TD3 beamforming). Sits beside the ISAC overviews [[meng-2024-uav-isac-overview]] and [[jiang-2025-isac-lae-overview]] in the [[integrated-sensing-and-communication]] track, and references the diffusion-contract incentive work [[ye-2025-aigc-diffusion-contract|[2]]] in its intro. Authors with corpus entity pages include [[jiacheng-wang]], [[dusit-niyato]], and [[jiawen-kang]].

## Raw artifacts
- `raw/sources/Generative_AI_for_Integrated_Sensing_and_Communication_Insights_From_the_Physical_Layer_Perspective/full.md`
- Original PDF and extracted figures in the same folder.
