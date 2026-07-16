---
type: source
title: "Unleashing the Power of Edge-Cloud Generative AI in Mobile Networks: A Survey of AIGC Services"
authors: ["Minrui Xu", "Hongyang Du", "Dusit Niyato", "Jiawen Kang", "Zehui Xiong", "Shiwen Mao", "Zhu Han", "Abbas Jamalipour", "Dong In Kim", "Xuemin Shen", "Victor C. M. Leung", "H. Vincent Poor"]
year: 2024
url: "https://doi.org/10.1109/COMST.2024.3353265"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
modeling_card: not_applicable
tags: [source, survey, generative-ai, aigc, mobile-aigc-network, edge-cloud, generative-ai-for-mec]
related:
  - "[[mobile-aigc-network]]"
  - "[[generative-ai-for-mec]]"
  - "[[aigc-service-provider]]"
  - "[[generative-diffusion-model]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[task-offloading]]"
  - "[[service-caching-mec]]"
  - "[[mobility-aware-offloading]]"
  - "[[federated-learning]]"
  - "[[du-2024-d2sac-aigc-asp-selection]]"
  - "[[du-2024-gdm-network-optimization-tutorial]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[wang-gai-isac-physical-layer]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
  - "[[zehui-xiong]]"
created: 2026-05-31
updated: 2026-07-16
---

# Unleashing the Power of Edge-Cloud Generative AI in Mobile Networks: A Survey of AIGC Services

## Citation

Xu, M., Du, H., Niyato, D., Kang, J., Xiong, Z., Mao, S., Han, Z., Jamalipour, A., Kim, D. I., Shen, X., Leung, V. C. M., & Poor, H. V. (2024). *Unleashing the Power of Edge-Cloud Generative AI in Mobile Networks: A Survey of AIGC Services*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2024.3353265. (Date of publication 12 January 2024; date of current version 23 May 2024. Corresponding author: Hongyang Du. Author affiliations are listed in the article's Acknowledgment section per the parse.)

## TL;DR

A **survey** of how to deploy **Artificial-Intelligence-Generated-Content (AIGC)** services — e.g. ChatGPT, DALL-E — at mobile edge networks, which the authors call **mobile AIGC networks**. It covers (i) the background and fundamentals of generative models and the **AIGC service lifecycle** (data collection → pre-training → fine-tuning → inference → product management), (ii) the **collaborative cloud-edge-mobile infrastructure** and enabling technologies, (iii) AIGC-driven creative applications and use cases, and (iv) the implementation, security, and privacy challenges, closing with future research directions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xu et al. [x] surveyed the deployment of Artificial-Intelligence-Generated Content applications at mobile edge networks, which they term mobile AIGC networks. They introduced the background and fundamentals of generative models and organized the AIGC service lifecycle into data collection, pre-training, fine-tuning, inference, and product management. The survey examined the collaborative cloud-edge-mobile infrastructure and enabling technologies for real-time, personalized, and privacy-preserving AIGC services, and presented creative applications and representative use cases. It identified implementation challenges involving edge resource allocation, task and computation offloading, edge caching, mobility management, incentive mechanisms, security, and privacy. The paper also outlined future research directions from networking and computing, machine learning, and practical implementation perspectives.

## Problem framing

Cloud-hosted generative AI (pre-trained in data centers, accessed over the core network) suffers high latency, so interaction-intensive AIGC should move toward the edge. The survey's stated motivations for **mobile AIGC networks** are: **low latency** (download pre-trained models to edge/devices for fine-tuning + inference in the RAN), **localization & mobility** (localize service requests; use user location/mobility as fine-tuning input), **customization & personalization** (edge servers adapt to local users), and **privacy & security** (users submit requests to edge servers instead of the cloud). The proposed division of labor: **cloud layer** does pre-training/fine-tuning; **edge layer** and **mobile-device layer** do data collection, inference, and product management.

## System model (survey scope & structure)

- **Background & fundamentals (Sec. II).** Distinguishes PGC / UGC / AIGC; reviews generative-model families (the related-work table compares GANs, energy-based models, VAEs, autoregressive models, flow-based models, and **diffusion models**); ChatGPT used as a flagship case; AIGC lifecycle in mobile networks defined.
- **Technologies & collaborative infrastructure (Sec. III).** The cloud-edge-mobile collaborative architecture and the technologies (communication protocols, specialized hardware, FL, differential privacy) that support AIGC at the edge.
- **Applications & advantages (Sec. IV)** and **case studies (Sec. V):** e.g. **AIGC service provider (ASP) selection** ([[aigc-service-provider]]), generative-AI-empowered traffic/driving simulation, AI-generated incentive mechanisms, and blockchain-powered AIGC lifecycle management.
- **Implementation challenges (Sec. VI):** **edge resource allocation**, **task & computation offloading**, **edge caching** (request/model/service caching), **mobility management** (IoV, UAVs), and **incentive mechanisms**.
- **Future directions (Sec. VII):** networking & computing, ML, and practical-implementation perspectives, including AI **alignment**.

## Method

Survey / tutorial — no single experiment. It organizes the mobile-AIGC literature, tabulates representative works (scenarios, performance metrics / decision variables, benefits-challenges, and mathematical tools — e.g. control theory, ADMM, regularization-based online optimization, evolutionary game + auction, genetic algorithms, federated multi-agent RL), and presents a 2013→2023 development roadmap of AIGC and mobile edge computing.

## Key findings

As a survey, its "findings" are organizing claims rather than measured results:

- **Edge resource allocation** for AIGC must balance a trade-off among **model accuracy, latency, and resource consumption**; KPIs include model accuracy, bandwidth utilization, and edge resource consumption (Table IV). Personalization/customization makes evaluating model accuracy harder than in conventional optimization.
- **Task/computation offloading** of generative models from devices to edge servers reduces latency but adds transmission/result-download latency; key KPIs are **service latency** and **reliability** (Table V). Model partitioning (split a large model across device + edge) is a recurring architecture.
- **Edge caching** of models/requests/services (CDN-like) cuts model-access delay; **mobility management** and **incentive mechanisms** are needed to sustain participation across space and time.
- AIGC raises distinct **security/privacy** concerns (e.g. deepfakes, adversarial attacks on models) alongside benefits like content steganography.

## Limitations / future work

A survey, so it reflects the literature up to its 2023 coverage window rather than presenting validated new results; its roadmap and future directions (networking/computing, ML, alignment, blockchain-based management) are forward-looking. Some structural details (lifecycle/infrastructure figures, comparison tables) are MinerU-parsed and may be imperfectly transcribed.

## Relation to the corpus

The **anchor survey** for the wiki's generative-AI-for-MEC thread, complementing the methodological tutorial [[du-2024-gdm-network-optimization-tutorial]] and the GAI surveys/overviews [[khoramnejad-2025-gai-wireless-optimization-survey]] and [[wang-gai-isac-physical-layer]], plus the 6G foundation-models overview [[du-2024-distributed-foundation-models-6g]]. Its **ASP-selection** case study is realized concretely by [[du-2024-d2sac-aigc-asp-selection]] (D2SAC), and its AIGC-incentive/contract direction by [[ye-2025-aigc-diffusion-contract]]. It introduces the [[mobile-aigc-network]] concept and reinforces [[generative-ai-for-mec]], [[aigc-service-provider]], and [[generative-diffusion-model]]. Shares the Du / Niyato / Kang / Xiong / Mao / Han author cluster that recurs across the corpus's generative-AI sources.

## Raw artifacts

- `raw/sources/Unleashing_the_Power_of_Edge-Cloud_Generative_AI_in_Mobile_Networks_A_Survey_of_AIGC_Services/full.md`
- Original PDF (`2daf7688-fbfa-4594-bf8e-78567f6b4e65_origin.pdf`) and extracted figures (`images/`) in the same folder.
