---
type: synthesis
title: "GAI as physical-layer generator vs decision-layer optimizer in ISAC"
tags: [synthesis, generative-ai, isac, diffusion, generative-adversarial-network, comparison]
related:
  - "[[wang-gai-isac-physical-layer]]"
  - "[[faisal-2025-cgan-ris-isac-channel]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[generative-ai-for-mec]]"
  - "[[generative-diffusion-model]]"
  - "[[generative-adversarial-network]]"
  - "[[conditional-gan]]"
  - "[[td3]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[isac-sensing-in-aerial-mec]]"
created: 2026-06-01
updated: 2026-06-01
---

# GAI as physical-layer generator vs decision-layer optimizer in ISAC

Four curated sources apply **generative AI (GAI)** — diffusion models and GANs — to [[integrated-sensing-and-communication|ISAC]] and ISAC-adjacent secure-communication problems. They split cleanly into **two architectural roles** for the generative model, and the split matters: it determines *what the model outputs*, *what it is trained against*, and *which part of the stack it replaces*. This page maps the two roles, what distinguishes them mechanically, and the fusion gap none of the four crosses. It is the GAI-role companion to [[isac-sensing-in-aerial-mec]] (which maps how sensing enters each design) and to the [[generative-ai-for-mec]] concept page.

## The two roles

| Role | Model output | Trained against | Replaces / augments | Sources |
|---|---|---|---|---|
| **Physical-layer generator** | A physical-layer quantity (channel estimate, signal spectrum) | Ground-truth signals / pilots (adversarial or denoising loss) | A signal-processing estimator | [[wang-gai-isac-physical-layer]], [[faisal-2025-cgan-ris-isac-channel]] |
| **Decision-layer optimizer** | A control decision (beamforming weights, UAV positions/excitation currents) | Value critics / reward (DRL loop) | A non-convex optimizer / search | [[zhang-2024-gdmtd3-aerial-secure-cb]], [[zhang-2025-gan-td3-isac-active-ris]] |

## Role 1 — GAI as physical-layer generator

Here the generative model **produces a physical-layer signal quantity directly**, learning the propagation/observation distribution rather than a policy.

- [[wang-gai-isac-physical-layer]] (IEEE Wireless Communications; **year not in parse**) is a magazine overview whose case study, a diffusion-based **signal spectrum generator (SSG)**, tackles near-field direction-of-arrival (DoA) estimation when antenna spacing exceeds half the wavelength — the regime that normally causes ambiguities. The parse reports a DoA **MSE of about 1.03°** (over 2000 generations) and, for the surveyed GAN-based CSI-compression example, a normalized MSE of **−7.05 dB** versus **−2.46 dB** for a deep-learning CS-CsiNet baseline at compression ratio 1/64. The generative model's output *is* the estimated spectrum/channel.
- [[faisal-2025-cgan-ris-isac-channel]] (IEEE TCOMM 2025) uses a [[conditional-gan|conditional GAN]] for **channel estimation** in a RIS-assisted ISAC system: a generator maps observed pilots to the true channel while a discriminator sharpens it adversarially (variants CE-CGAN and SE-CGAN). Reported gains over conventional DL estimators are qualitative in the parse (improved accuracy/stability across SNR and system dimensions); exact NMSE curves are in the paper.

The common thread: the GAI model lives **before the optimizer**, turning sparse/ambiguous observations into a usable channel or spectrum. It does not decide anything.

## Role 2 — GAI as decision-layer optimizer

Here the generative model is **embedded inside a DRL loop** and its output is a *decision*, trained against reward/critics rather than ground-truth signals. Both sources build on [[td3|TD3]], but GAI enters at a different point:

- [[zhang-2024-gdmtd3-aerial-secure-cb]] (IEEE TMC 2024) — **GDMTD3** integrates a [[generative-diffusion-model|generative diffusion model]] into TD3 to capture the high-dimensional probabilistic distribution needed for the policy's decisions ([[diffusion-model-as-optimizer]]). The decision it generates is the UAV swarm's **excitation-current weights and positions** for aerial collaborative-beamforming secure communication (the ASCEE-MOP: maximize secrecy rate, minimize swarm flight energy). GAI here sits on the **actor** side — it represents the action distribution.
- [[zhang-2025-gan-td3-isac-active-ris]] (IEEE IoT-J 2025) — **GAN-TD3** integrates a GAN into TD3 to design transmit/reflection/receive **beamforming** for a double-active-RIS ISAC network (maximize the sum of minimum sensing SINRs under QoS and power limits). Per the parse, the GAN's adversarial mechanism is leveraged to **boost the estimation accuracy of the Q-value** — i.e. GAI enters on the **critic** side, improving sample efficiency and generalization. The paper's stated trade-off: GAN-TD3 beats plain TD3 in performance and stability **at the cost of higher computational complexity** (and slower convergence).

So even within the optimizer role there is a sub-split: **diffusion-as-policy (actor)** in GDMTD3 versus **GAN-as-critic-regularizer** in GAN-TD3. Both keep the DRL scaffold and use GAI to make the *decision* better, not to estimate the channel.

## Why the distinction matters

- **Different training signal.** Generators are supervised by ground-truth signals/pilots (an estimation loss); optimizers are trained by reward and value critics (a control objective). They cannot be swapped without re-posing the problem.
- **Different failure mode.** A bad generator yields a wrong channel/spectrum (an estimation error that propagates downstream); a bad optimizer yields a feasible-but-suboptimal decision. The wang overview itself flags that hallucinated channel predictions are catastrophic for control loops — which is exactly the boundary between the two roles.
- **Different place in the pipeline.** Role 1 is upstream (perception); Role 2 is downstream (decision). In principle they compose.

## The fusion gap

**No source in the corpus uses GAI at both layers within one system.** Each of the four picks a single role: wang and faisal generate physical-layer quantities; the two TD3 variants generate decisions. A system that chained, say, a CGAN channel estimator ([[faisal-2025-cgan-ris-isac-channel]]) into a diffusion-policy beamformer ([[zhang-2024-gdmtd3-aerial-secure-cb]]) — letting the estimator's uncertainty inform the policy — is an open architectural opportunity the curated corpus does not yet instantiate. This complements the [[isac-sensing-in-aerial-mec]] gap that no source combines a learning-first generative method with the convex (AO + SDR + SCA) inner solver the secure-ISAC sources rely on: the ISAC GAI work is split not only generator-vs-optimizer but learning-first-vs-convex-first, with no design spanning the divide.

## Caveats

- The two surveyed numerical results in [[wang-gai-isac-physical-layer]] (SSG DoA ~1.03°; CSI-compression −7.05 dB) are a magazine case study / surveyed example, not a benchmarked comparison, and that source's **year is not in the parse**.
- [[faisal-2025-cgan-ris-isac-channel]], [[zhang-2024-gdmtd3-aerial-secure-cb]], and [[zhang-2025-gan-td3-isac-active-ris]] report their head-to-head gains qualitatively in their parses (specific curves are in the papers), so the role distinction here is architectural and grounded, while the magnitude of each method's advantage is indicative.
