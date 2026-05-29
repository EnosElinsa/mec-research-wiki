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
created: 2026-05-29
updated: 2026-05-29
---

# Diffusion Model as Optimizer

Using a [[generative-diffusion-model]] as a **solver/decision generator** for non-convex optimization problems that must be re-solved repeatedly (as costs, types, or environment parameters change). A conditional reverse-diffusion policy maps the problem's environment vector to a near-optimal decision in one inference pass; it is trained DRL-style — against value critics (often double-Q to curb overestimation), with a replay buffer and soft target updates — so it learns to *generate* good solutions rather than search for them each time.

In the wiki, [[ye-2025-aigc-diffusion-contract]] uses this pattern (GQCG/GLCG generators) to produce optimal [[contract-theory]] items, beating a DRL-based generator on test reward, and [[peng-2025-drudm-cfg]] applies a diffusion model with classifier-free guidance to MEC resource decisions. It is an alternative to the corpus's DRL backbones ([[ddpg]] etc.) for the "repeatedly re-solve a hard problem" setting.
