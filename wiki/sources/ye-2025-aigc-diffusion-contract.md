---
type: source
title: "Optimizing AIGC Services by Prompt Engineering and Edge Computing: A Generative Diffusion Model-Based Contract Theory Approach"
tags:
  - source
  - mobile-edge-computing
  - aigc
  - generative-diffusion-model
  - contract-theory
  - prompt-engineering
  - incentive-mechanism
related:
  - "[[mobile-edge-computing]]"
  - "[[generative-ai-for-mec]]"
  - "[[qoe-modeling-mec]]"
  - "[[contract-theory]]"
  - "[[prompt-engineering]]"
  - "[[generative-diffusion-model]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[aigc-service-provider]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[bao-2025-ddpg-video-offloading]]"
created: 2026-05-29
updated: 2026-05-29
authors:
  - Dongdong Ye
  - Shuting Cai
  - Hongyang Du
  - Jiawen Kang
  - Yinqiu Liu
  - Rong Yu
  - Dusit Niyato
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3463420"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
---

# Optimizing AIGC Services by Prompt Engineering and Edge Computing: A Generative Diffusion Model-Based Contract Theory Approach

## TL;DR
To deliver text-to-image AIGC from an edge-deployed pretrained foundation model, an [[aigc-service-provider]] (ASP) must jointly tune four resource dimensions — level of [[prompt-engineering|prompt optimization]], number of diffusion denoising steps, CPU cycle frequency, and network transmission rate — while users are self-interested and their per-quality "gain" is private (information asymmetry). The paper formulates a **two-stage** [[contract-theory]] problem (a quality-based contract, then a latency-based contract per chosen quality item) and, because each non-convex contract must be re-solved repeatedly, uses a [[generative-diffusion-model]] as the solver ([[diffusion-model-as-optimizer]]) to generate optimal contract items directly. With Stable Diffusion XL + NIMA, the GDM scheme beats a DRL-based contract generator on test reward, and prompt optimization raises generation quality (+8% / +2% across types) and expected latency reduction (+22% for one type).

## Problem
Pretrained foundation models for [[generative-ai-for-mec|generative AI / AIGC]] are resource-hungry and highly sensitive to prompt quality, so resource-limited mobile users with weak prompts get low-quality images, frequent regenerations, and high latency. Hosting the model on an edge server as an ASP plus treating [[prompt-engineering|prompt optimization]] as a tunable resource can help, but three questions remain: how to **quantify** the relationship between prompt-optimization level, denoising steps, and generation quality; how to perform **multi-dimensional resource optimization** (prompt level, denoising steps, CPU frequency, transmission rate) in resource-sparse edge networks to improve [[qoe-modeling-mec|QoE]]; and how to **incentivize** the paid ASP–user relationship when users won't unconditionally obey the ASP and the ASP doesn't know each user's private gain type. The work targets text-to-image services but claims generality to other AIGC.

## System model
- **Actors:** one ASP (edge server running Stable Diffusion XL) and M users, partitioned by private "gain per quality" into I types and, within a quality group, by "gain per expected latency reduction" into J types. The ASP knows only the type **distribution** (e.g., via k-means), not each user's type.
- **QoE:** quality of image generation `A` and latency reduction `D`.
- **Quality:** `A = ρ1·ln(ρ2·l+1) − ρ3·l + ρ4·ln(ρ5·s+1) − ρ6·s` (Eq. 35), increasing in prompt-optimization level `l^A` and denoising steps `s^A`; image quality scored by the NIMA model.
- **Latency/energy:** total latency `= δl^A/x^T + ηs^A/y^T + d/r^T` (prompt-opt compute + denoising compute + transmission); `D = t^max −` (those terms). Compute energy via effective switched-capacitance `κ`.
- **Regeneration:** success probability `ζ_{l^A,s^A}` against threshold `Ā`; failed images are regenerated. `E[D] = ζ(1−ζ)^{g−1}[t^max − g(δl^A/x^T + ηs^A/y^T + d/r^T)]`; the paper uses `g = 1`.
- **Contracts:** quality item `Φ_i^A = (l_i^A, s_i^A, p_i^A)`; latency item `Φ_j^T = (x_j^T, y_j^T, r_j^T, p_j^T)`; feasibility via IR (non-negative utility) and IC (truthful self-selection).
- **Assumptions:** integer `l^A, s^A`; denoising lower bound `s^{A,min}=4` (outputs mostly invalid at ≤3 steps); `Ā = 5.0`; rational users; ASP knows type probabilities and user count.

## Method
- **Two-stage contract framework** combining [[contract-theory]] with a [[generative-diffusion-model]]. **Stage 1 (quality):** maximize ASP utility `U^A_sp = Σ_i M·q_i^A (p_i^A − σ_{1,i} l_i^A − σ_{2,i} s_i^A)` s.t. IR+IC over `(l_i^A, s_i^A, p_i^A)` — non-convex objective over integer sets (Problem 1). **Stage 2 (latency):** per group choosing the same quality item, maximize ASP utility from expected latency reduction over `(x^T, y^T, r^T, p^T)`.
- Variable user gains and ASP costs force repeatedly re-solving these non-convex problems, which is slow for classical methods — so a [[diffusion-model-as-optimizer|GDM is used as the solver]]. The conditional reverse-diffusion policy `π_ω(φ|e)` maps environment parameters `e` (types, probabilities, costs, M, I…) to a deterministic contract design (Eqs. 10–18).
- **Training is DRL-style:** a noise-prediction design network `ε_ω` (mean per Eq. 17, fixed covariance `β_k·I`) trained against two contract evaluation critics `H_v` via **double Q-learning** (min of two critics) to curb overestimation; replay buffer, soft target updates `τ`, discount `γ`, exploration noise `ε`. Two instances — GQCG (quality) and GLCG (latency).
- **Type:** principal-agent / contract optimization (non-convex, MINLP-like) solved by a generative decision generator rather than an MDP/game. Complexity `O(Z_e·Z_s·(K·ψ_a + ψ_c))` train, `O(ψ_a)` inference.

## Key findings
- GDM quality generator (GQCG) > DRL quality generator (DQCG) on test reward; GDM latency generator (GLCG) > DRL latency generator (DLCG) under identical parameters (Figs. 5, 8) — the diffusion process reduces randomness/noise.
- Generated contracts satisfy IR and IC: each type maximizes (non-negative) utility only by choosing its matched item (Figs. 6, 9), resolving information asymmetry.
- Prompt optimization improves diffusion-denoising quality by **8%** (type-θ1^A) and **2%** (type-θ2^A) and raises ASP and user utilities (Fig. 11).
- Prompt optimization raises expected latency reduction by **22%** for type-θ2^T(θ2^A) users, with higher ASP/user utilities (Fig. 12).
- Higher gain-per-quality users pay more, buying more denoising steps and higher prompt-optimization level (Fig. 7).
- Quality-fit coefficients: ρ1=9.7417, ρ2=0.0978, ρ3=0.7647, ρ4=0.5158, ρ5=3497.8463, ρ6=0.0307; `s^{A,min}=4`; `Ā=5.0`.
- (Cited from prior work [7], not the authors' own result) prompt optimization can raise user satisfaction with produced images by **380%**.

## Limitations
Simulation-only on a single workstation (Ubuntu 20.04, AMD Ryzen Threadripper PRO 3975WX, NVIDIA RTX A5000); no testbed. Small synthetic setting (M=20, I=2, J=2, M_i=10) with randomly sampled type/cost/channel parameters. Only single-generation `g=1` modeled (regeneration tail `g>1` is future work). Assumes the ASP knows type distributions and counts and that users are fully rational (the paper flags irrational behavior as future work). The quality function is curve-fit to one model/dataset (Stable Diffusion XL + NIMA) and `Ā` may vary. Some reported magnitudes are read from MinerU-parsed figures/tables (units sometimes unlabeled) and should be read as trends.

## Relation to the corpus
This is the corpus's clearest example of [[generative-ai-for-mec|generative-AI-for-MEC]] used as an **incentive-mechanism and optimization** problem rather than a UAV/aerial scheduling problem. Methodologically it is closest to [[peng-2025-drudm-cfg]], which likewise applies a diffusion model (with classifier-free guidance) to MEC resource decisions ([[diffusion-model-as-optimizer]]); the [[generative-diffusion-model]] here plays the solver role that DRL plays elsewhere. The paper explicitly benchmarks its GDM contract generator against a DRL contract generator, making DRL-based edge-decision work such as [[bao-2025-ddpg-video-offloading]] a natural contrast. Its [[contract-theory]] formulation (IR/IC under information asymmetry) and [[prompt-engineering]] resource dimension are new vocabulary for the corpus, complementing the existing [[mobile-edge-computing]] and [[qoe-modeling-mec]] building blocks.

## Raw artifacts
- `raw/sources/Optimizing_AIGC_Services_by_Prompt_Engineering_and_Edge_Computing_A_Generative_Diffusion_Model-Based_Contract_Theory_Approach/full.md`
