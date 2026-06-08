---
type: source
title: "Diffusion-Based Reinforcement Learning for Edge-Enabled AI-Generated Content Services"
authors: ["Hongyang Du", "Zonghang Li", "Dusit Niyato", "Jiawen Kang", "Zehui Xiong", "Huawei Huang", "Shiwen Mao"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3356178"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, generative-ai, aigc, diffusion-model-as-optimizer, soft-actor-critic, edge-computing, drl]
related:
  - "[[generative-ai-for-mec]]"
  - "[[generative-diffusion-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[aigc-service-provider]]"
  - "[[soft-actor-critic]]"
  - "[[mobile-edge-computing]]"
  - "[[qoe-modeling-mec]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-31
updated: 2026-06-08
---

# Diffusion-Based Reinforcement Learning for Edge-Enabled AI-Generated Content Services

## Citation

Du, H., Li, Z., Niyato, D., Kang, J., Xiong, Z., Huang, H., & Mao, S. (2024). *Diffusion-Based Reinforcement Learning for Edge-Enabled AI-Generated Content Services*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3356178. (Date of publication 19 January 2024; date of current version 6 August 2024. Hongyang Du and Zonghang Li contributed equally; corresponding author Zonghang Li.)

## TL;DR

An **AIGC-as-a-Service (AaaS)** architecture deploys [[generative-ai-for-mec|generative-AI]] (AIGC) models on wireless edge servers so Metaverse users can request content from any device. The core problem is **AIGC Service Provider (ASP) selection**: assign each arriving user task to the best edge-hosted AIGC model under environmental uncertainty, framed as a resource-constrained task-assignment MDP. The paper proposes the **AI-Generated Optimal Decision (AGOD)** algorithm — a [[generative-diffusion-model|diffusion model]] adapted to *generate* the optimal discrete selection decision ([[diffusion-model-as-optimizer]]) — and integrates it into [[soft-actor-critic|SAC]] to form **Deep Diffusion Soft Actor-Critic (D2SAC)**. D2SAC outperforms seven leading DRL baselines on the ASP-selection task.

## Problem framing

Two goals: **G1** make AIGC accessible from any device, anywhere, anytime; **G2** provide human-centric AIGC services maximizing user utility. AaaS (deploy models on edge servers) addresses G1, but G2 is hard because different AIGC models suit different tasks, users have varying preferences, and servers have varying capacity. So an ASP-selection algorithm must match tasks to the best model/server. Difficulty: user utilities and model capabilities are hard to model mathematically, and pure DRL can converge to suboptimal policies under exploration-exploitation trade-offs — motivating a diffusion-model decision generator.

## System model

- **AaaS.** ASPs run AIGC models (e.g. Stable Diffusion) on edge servers; users upload a request (e.g. a text prompt + required denoising steps) and receive generated content ([[mobile-edge-computing]], [[aigc-service-provider]]).
- **ASP selection = resource-constrained task assignment.** Sequential tasks $\mathcal{I}=\{j_1,\dots,j_J\}$, ASPs $\{i_1,\dots,i_I\}$, each ASP's utility $u_i(\cdot)$; assign tasks to ASPs to maximize total utility, subject to each ASP's resource (max concurrent tasks) limit.
- **Resource $T_j$** = number of diffusion **denoising steps**, positively correlated with energy cost (empirically validated on a Dell Precision 5820 / Xeon W-2235: energy rises with denoising steps).
- **MDP.** State = arriving-task feature vector $s^T$ + per-ASP resource-status vector $s^A$ (normalized); action = ASP choice; reward = AIGC quality reward $r^R$ (via an image-quality score) minus a crash penalty $r^P$ when a chosen ASP's resources are exceeded ([[qoe-modeling-mec]]).

## Method

- **AGOD.** A conditional reverse-diffusion policy generates the optimal decision from the environment state — diffusion models used to generate *decisions* rather than media ([[diffusion-model-as-optimizer]]). Unlike prior diffusion-RL (e.g. Diffusion Q-Learning) restricted to **continuous** offline action spaces, AGOD targets the **discrete** ASP-selection action space online.
- **D2SAC.** AGOD is embedded as the actor inside [[soft-actor-critic|Soft Actor-Critic]] (entropy-regularized, off-policy, double-Q critics, replay buffer, target networks) to give efficient and effective ASP selection.
- **Type.** MDP solved by a diffusion-policy DRL agent. Code released by the authors.

## Key findings

- **D2SAC outperforms seven representative DRL algorithms** — DQN, DRQN, Prioritized-DQN, Rainbow, REINFORCE, PPO, and SAC — on the studied ASP-selection task (abstract and contributions; specific reward curves in the figures).
- Energy cost rises consistently with the number of diffusion **denoising steps** (Fig. 2, the authors' own measurement), grounding the resource model.
- AGOD is presented as **extensible** to other wireless-network optimization problems, not only ASP selection.

## Limitations / future work

Simulation/experiment-based (no wireless field trial). The reward uses an image-quality proxy; performance evaluation of AIGC is human-subjective and hard to model exactly (the paper flags this as challenge C2). Some reported magnitudes are read from MinerU-parsed figures and should be read as trends.

## Relation to the corpus

A flagship **diffusion-model-as-optimizer** entry, closely related to [[ye-2025-aigc-diffusion-contract]] (same diffusion-as-solver pattern by an overlapping author group — Hongyang Du, Jiawen Kang, Dusit Niyato) and to [[peng-2025-drudm-cfg]] (diffusion with classifier-free guidance for MEC decisions). Where ye-2025 generates [[contract-theory]] items, this paper generates **discrete ASP-selection** decisions and benchmarks the diffusion policy against a wide DRL baseline set, sharpening the [[generative-diffusion-model]] vs conventional-DRL comparison. It grounds [[soft-actor-critic]] (SAC as the host RL algorithm) and broadens the [[generative-ai-for-mec]] thread toward Metaverse/AIGC edge services. Shares co-authors Dusit Niyato / Jiawen Kang with the Geng-Sun and CMOP clusters.

## Raw artifacts

- `raw/sources/Diffusion-Based_Reinforcement_Learning_for_Edge-Enabled_AI-Generated_Content_Services/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
