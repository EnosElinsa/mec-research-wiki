---
type: concept
title: "Contract Theory (Principal-Agent Incentive Mechanism)"
tags: [game-theory, incentive-mechanism, information-asymmetry, mechanism-design]
related:
  - "[[stackelberg-game]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[generative-ai-for-mec]]"
  - "[[ye-2025-aigc-diffusion-contract]]"
created: 2026-05-29
updated: 2026-05-29
---

# Contract Theory (Principal-Agent Incentive Mechanism)

A mechanism-design framework for incentivizing self-interested agents under **information asymmetry**. A principal (e.g. an edge service provider) designs a menu of **contract items** — each bundling a resource/quality level with a price/reward — and agents (users) self-select the item matched to their private "type." Feasibility rests on two constraints:

- **Individual Rationality (IR):** every agent gets non-negative utility from its chosen item (so it participates).
- **Incentive Compatibility (IC):** every agent maximizes its utility by truthfully picking the item designed for its own type (so it doesn't mimic another type).

Unlike a [[stackelberg-game]] (observable leader-follower moves) or [[matching-theory-for-resource-allocation|matching]], contract theory specifically handles hidden types. In the wiki, [[ye-2025-aigc-diffusion-contract]] designs a two-stage contract (quality then latency) for edge AIGC services and — because the non-convex contracts must be re-solved repeatedly — generates the optimal items with a [[diffusion-model-as-optimizer|diffusion model]] rather than a classical solver.
