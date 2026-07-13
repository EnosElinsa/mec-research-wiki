---
type: concept
title: "Diffusion Model as Optimizer"
tags: [generative-ai, diffusion, optimization, decision-generation]
related:
  - "[[jin-2026-skyndn-incentivizer]]"
  - "[[generative-diffusion-model]]"
  - "[[contract-theory]]"
  - "[[ddpg]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[liu-2026-lyapunov-diffusion-uav-vehicular]]"
  - "[[wang-2026-diffusion-semantic-uav-edge]]"
  - "[[wen-2026-hybridrag-low-carbon-lae]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
created: 2026-05-29
updated: 2026-07-14
---

# Diffusion Model as Optimizer

[[jin-2026-skyndn-incentivizer]] uses a diffusion actor with twin critics to denoise a continuous consumer-producer allocation matrix. Infeasible allocations receive a constraint-count penalty, so the learned policy is an empirical optimizer and does not inherit the analytical auction's economic-property claims.

Using a [[generative-diffusion-model]] as a **solver/decision generator** for non-convex optimization problems that must be re-solved repeatedly (as costs, types, or environment parameters change). A conditional reverse-diffusion policy maps the problem's environment vector to a near-optimal decision in one inference pass; it is trained DRL-style — against value critics (often double-Q to curb overestimation), with a replay buffer and soft target updates — so it learns to *generate* good solutions rather than search for them each time.

In the wiki, [[ye-2025-aigc-diffusion-contract]] uses this pattern (GQCG/GLCG generators) to produce optimal [[contract-theory]] items, [[peng-2025-drudm-cfg]] applies a diffusion model with classifier-free guidance to MEC resource decisions, [[liu-2026-lyapunov-diffusion-uav-vehicular]] replaces the standard [[ddpg]] actor with a diffusion denoiser for delayed-CSI vehicular V2X control, and [[wang-2026-diffusion-semantic-uav-edge]] uses a denoising diffusion actor to generate UAV trajectory actions for semantic edge computing. It is an alternative to the corpus's DRL backbones when a controller must repeatedly generate near-feasible decisions for hard coupled optimization problems.

[[wen-2026-hybridrag-low-carbon-lae]] embeds a diffusion policy inside SAC for low-carbon LAE MEC control, making diffusion both a decision generator and part of a carbon-aware training pipeline.
