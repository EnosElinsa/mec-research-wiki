---
type: concept
title: "Conditional GAN (CGAN)"
tags: [generative-ai, deep-learning, channel-estimation]
related:
  - "[[faisal-2025-cgan-ris-isac-channel]]"
  - "[[generative-adversarial-network]]"
  - "[[csi-estimation-error]]"
  - "[[generative-ai-for-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Conditional GAN (CGAN)

A [[generative-adversarial-network]] in which both the generator and discriminator are conditioned on side information (e.g. observed pilots/measurements), so the generator learns a *conditional* mapping from observations to a target distribution rather than an unconditional sample.

In [[faisal-2025-cgan-ris-isac-channel]] a CGAN is used for **channel estimation** in RIS-assisted ISAC: the generator maps observed data to channel estimates while the discriminator's feedback refines accuracy, outperforming conventional deep-learning estimators across SNR and system-dimension settings. CGAN is one instance of the broader [[generative-ai-for-mec]] trend of using generative models as estimators/optimizers.
