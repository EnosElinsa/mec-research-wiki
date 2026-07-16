---
type: source
title: "Generative AI for Physical Layer Communications: A Survey"
authors: ["Nguyen Van Huynh", "Jiacheng Wang", "Hongyang Du", "Dinh Thai Hoang", "Dusit Niyato", "Diep N. Nguyen", "Dong In Kim", "Khaled B. Letaief"]
year: 2024
url: "https://doi.org/10.1109/TCCN.2024.3384500"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
modeling_card: not_applicable
tags: [source, survey, generative-ai-for-mec, physical-layer-security, intelligent-reflecting-surface, semantic-communication, variational-autoencoder, generative-adversarial-network]
related:
  - "[[generative-ai-for-mec]]"
  - "[[generative-adversarial-network]]"
  - "[[variational-autoencoder]]"
  - "[[generative-diffusion-model]]"
  - "[[conditional-gan]]"
  - "[[physical-layer-security]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[semantic-communication]]"
  - "[[du-2024-gdm-network-optimization-tutorial]]"
  - "[[wang-gai-isac-physical-layer]]"
  - "[[xu-2024-mobile-aigc-survey]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
  - "[[khaled-ben-letaief]]"
created: 2026-06-02
updated: 2026-07-16
---

# Generative AI for Physical Layer Communications: A Survey

## Citation

Van Huynh, N., Wang, J., Du, H., Hoang, D. T., Niyato, D., Nguyen, D. N., Kim, D. I., & Letaief, K. B. (2024). *Generative AI for Physical Layer Communications: A Survey*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2024.3384500. (Manuscript received 9 December 2023; revised 1 March 2024; accepted 23 March 2024; date of publication 3 April 2024; date of current version 7 June 2024 → year 2024.)

## TL;DR

A comprehensive survey of how **generative AI (GAI)** can support **physical-layer communications**, organized around five GAI model families — **GANs, variational autoencoders (VAEs), normalizing flows, diffusion models, and transformers** — and the physical-layer problems they address: modulation/signal classification, channel equalization/modeling/estimation, physical-layer security (PLS), intelligent reflecting surfaces (IRS), beamforming, joint source-channel coding (JSCC), CSI feedback, and radio-map / channel-delay estimation. The survey contrasts GAI with traditional (discriminative) AI, arguing GAI's distinctive value is in **capturing complex data distributions**, **cross-dimensional data transformation**, and **repairing/enhancing data**, and closes with open issues (security/privacy, model-driven GAI, resource-efficient learning, real-time adaptation).

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huynh et al. [x] surveyed generative artificial intelligence for physical-layer communications. They reviewed generative adversarial networks, variational autoencoders, normalizing flows, diffusion models, and transformers and compared their operating principles, strengths, and limitations. The survey organized applications across channel modeling, estimation and signal detection, physical-layer security, intelligent reflecting surfaces, beamforming, joint source-channel coding, CSI feedback, radio-map estimation, and channel-delay estimation. It synthesized how the reviewed methods use distribution learning, cross-dimensional transformation, and data repair or enhancement in physical-layer tasks. The authors identified security and privacy, model-driven generative AI, resource-efficient learning, and real-time adaptation as future research directions.

## Problem framing

The physical layer converts higher-layer digital data into channel-ready signals (encoding, modulation, propagation) and inverts the process at the receiver, while also handling channel access, equalization, and multiplexing. Classical model-based methods struggle when systems include effects that are hard to express analytically; discriminative deep learning (DNNs, RNNs, CNNs, autoencoders) helps but is reported to falter on channels unseen during training. The survey's thesis is that GAI overcomes these limits by generating extra channel samples and analyzing data distributions, making it well suited to emerging technologies such as IRS, cell-free, ISAC, and extremely large-scale MIMO — areas where GAI is reported to be underexplored.

## System model

This is a survey, so there is no single system model. It structures the field along two axes: **(i) GAI model families** — GANs (generator/discriminator adversarial game toward Nash equilibrium), VAEs (probabilistic encoder/latent/decoder), normalizing flows (invertible transformations mapping simple to complex distributions), diffusion models (forward noising / reverse denoising, stable training on incomplete data), and transformers (self-attention for sequential data); and **(ii) physical-layer application areas** — modulation and signal classification, channel equalization/modeling/estimation, PLS, IRS, beamforming, JSCC, CSI feedback, and radio-map / channel-delay estimation. Strengths and weaknesses of each model family are tabulated, as are the drawbacks of traditional-AI approaches versus the proposed GAI approach per problem.

## Method

As a survey, the contribution is taxonomy and analysis rather than a new algorithm:

- **GAI fundamentals.** Principles, strengths, weaknesses, and differences of the five model families, with emphasis on the data-generation properties relevant to the physical layer.
- **Problem-by-problem review.** For each physical-layer problem, the survey identifies where traditional AI falls short and how a GAI model addresses it (e.g., GANs and VAEs are the most common families for channel estimation/equalization; diffusion models and transformers also appear; VAE-based JSCC is reported to raise average PSNR and save bandwidth in cited works).
- **Synthesis of capabilities.** The reviewed works are argued to leverage three core GAI capabilities: capturing complex distributions, cross-dimensional transformation/processing, and data repair/enhancement.
- **Open issues.** Security and privacy (including GAI-based adversarial attacks and "fight-fire-with-fire" defenses), **model-driven GAI** (injecting domain priors when data is scarce), **resource-efficient learning** (distributed/federated GAI to offload training/inference for resource-constrained IoT/UAV devices), and **real-time adaptation** (meta-learning for fast adaptation to new channels/environments).

## Key findings

- The survey's organizing conclusion is that GAI is well matched to physical-layer problems because of its ability to model complex channel distributions, generate synthetic data under constraints, and quantify uncertainty — capabilities the authors argue extend beyond what discriminative AI offers. These are qualitative, review-level conclusions rather than measured results; specific quantitative figures (e.g., cited PSNR or bandwidth-saving numbers) belong to the surveyed works, not to this paper.

## Limitations / future work

The authors stress GAI is "still in its early stage of development" for the physical layer and name four open directions: defending against (and exploiting) GAI for security/privacy; **model-driven** GAI to reduce reliance on large training sets; **resource-efficient** GAI architectures (with distributed/federated learning and update compression) for constrained devices; and **real-time adaptation** via meta-learning, over-the-air evaluation, and implicit CSI feedback.

## Relation to the corpus

A **foundational generative-AI survey** that anchors the physical-layer side of the corpus's generative-AI thread, complementing the network-optimization tutorial [[du-2024-gdm-network-optimization-tutorial]], the GAI-for-ISAC physical-layer paper [[wang-gai-isac-physical-layer]], the edge-cloud AIGC-services survey [[xu-2024-mobile-aigc-survey]], and the GAI-for-wireless-optimization survey [[khoramnejad-2025-gai-wireless-optimization-survey]]. It introduces the corpus's [[variational-autoencoder]] concept and broadens coverage of [[generative-adversarial-network]], [[generative-diffusion-model]], and [[conditional-gan]] into physical-layer territory, while its PLS, IRS, and semantic-coding sections connect to [[physical-layer-security]], [[intelligent-reflecting-surface]], and [[semantic-communication]]. Unlike the MEC-offloading papers in the corpus, it sits at the physical layer rather than the computing layer, and it shares the Niyato/NTU generative-AI cluster authorship with several of those threads.

## Raw artifacts

- `raw/sources/Generative_AI_for_Physical_Layer_Communications_A_Survey/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
