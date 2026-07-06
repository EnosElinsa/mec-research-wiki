---
type: concept
title: "Diffusion Model as Optimizer"
tags: [generative-ai, diffusion, optimization, decision-generation]
related:
  - "[[generative-diffusion-model]]"
  - "[[contract-theory]]"
  - "[[ddpg]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[liu-2026-lyapunov-diffusion-uav-vehicular]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
created: 2026-05-29
updated: 2026-07-06
---

# Diffusion Model as Optimizer

Using a [[generative-diffusion-model]] as a **solver/decision generator** for non-convex optimization problems that must be re-solved repeatedly (as costs, types, or environment parameters change). A conditional reverse-diffusion policy maps the problem's environment vector to a near-optimal decision in one inference pass; it is trained DRL-style — against value critics (often double-Q to curb overestimation), with a replay buffer and soft target updates — so it learns to *generate* good solutions rather than search for them each time.

In the wiki, [[ye-2025-aigc-diffusion-contract]] uses this pattern (GQCG/GLCG generators) to produce optimal [[contract-theory]] items, [[peng-2025-drudm-cfg]] applies a diffusion model with classifier-free guidance to MEC resource decisions, and [[liu-2026-lyapunov-diffusion-uav-vehicular]] replaces the standard [[ddpg]] actor with a diffusion denoiser for delayed-CSI vehicular V2X control. It is an alternative to the corpus's DRL backbones when a controller must repeatedly generate near-feasible decisions for hard coupled optimization problems.
