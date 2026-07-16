---
type: source
title: "Optimal LAP Altitude for Maximum Coverage"
authors: ["Akram Al-Hourani", "Sithamparanathan Kandeepan", "Simon Lardner"]
year: 2014
url: "https://doi.org/10.1109/LWC.2014.2342736"
venue: "IEEE Wireless Communications Letters (IEEE WCL)"
modeling_card: required
tags: [source, low-altitude-platform, air-to-ground-channel-model, line-of-sight-probability, coverage-optimization, post-disaster-mec]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[post-disaster-mec]]"
  - "[[high-altitude-platform-station]]"
created: 2026-05-31
updated: 2026-07-16
---

# Optimal LAP Altitude for Maximum Coverage

## Citation

Al-Hourani, A., Kandeepan, S., & Lardner, S. (2014). *Optimal LAP Altitude for Maximum Coverage*. **IEEE Wireless Communications Letters**. DOI: 10.1109/LWC.2014.2342736. (Manuscript received 28 Apr 2014; date of publication 24 Jul 2014; date of current version 17 Dec 2014 → year 2014.)

## TL;DR

A foundational analytical letter that derives the **optimal altitude of a low-altitude aerial platform (LAP)** to maximize ground radio coverage. It models air-to-ground (ATG) propagation as a probabilistic mix of LoS and NLoS groups, gives a **closed-form sigmoid (S-curve) approximation of the LoS probability** as a function of elevation angle and ITU urban statistical parameters (α, β, γ), and shows the optimal altitude depends on the maximum allowed pathloss and the environment, with a derived **optimal elevation angle** that is independent of the pathloss threshold.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One quasi-stationary low-altitude platform acts as an airborne base station for ground receivers in an urban environment. The multiple-access scheme is not specified; the air-to-ground channel uses a mean pathloss model that combines free-space loss with probabilistic LoS and NLoS excessive loss, where LoS probability is a sigmoid function of elevation angle and urban parameters.

**Problem & objective**: A one-dimensional analytical coverage optimization chooses the LAP altitude to solve $\max_h R(h)$, where the coverage boundary satisfies $\Lambda(h,R)=\mathrm{PL}_{\max}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| LAP altitude | $h$ | continuous, $h>0$ | Platform altitude that determines elevation angle, mean pathloss, and coverage radius |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 7 | A covered receiver satisfies $\Lambda(h,r)\leq\mathrm{PL}_{\max}$, with $R=r\mid_{\Lambda=\mathrm{PL}_{\max}}$ on the coverage boundary |
| Practical bound | If the unconstrained optimum is infeasible, impose the platform limit $h\leq h_{\max}$ |

**Algorithm**: Substitute the sigmoid LoS probability and LoS/NLoS pathloss terms into the boundary equation to obtain the implicit radius-altitude relation in Eq. (10), solve $\partial R/\partial h=0$ numerically for $h_{\mathrm{OPT}}$, and solve Eq. (13) for the environment-specific optimum elevation angle.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Al-Hourani et al. [x] studied altitude optimization for low-altitude aerial platforms deployed as airborne base stations in rapid relief networks. They modeled the air-to-ground mean pathloss as a probabilistic combination of LoS and NLoS propagation and approximated the geometrical LoS probability with a modified sigmoid function parameterized by the urban environment. They defined the coverage zone through a maximum allowable pathloss and obtained the LAP altitude that maximizes the ground coverage radius by solving the critical-point condition numerically, then derived an optimum elevation-angle equation whose solution is independent of the pathloss threshold. The analysis shows that the optimum altitude depends on the maximum allowed pathloss and the urban statistical parameters, while the optimum elevation angle is unique for a given environment parameter set.

## Problem framing

After disasters that disrupt fixed cellular infrastructure, airborne base stations (LAPs — quadcopters, balloons, helicopters in the troposphere) offer rapid recovery coverage for public-safety users. Deployable LAPs are scarce in the chaotic aftermath, so each one must be placed at the altitude that maximizes its ground coverage disk. The question: given an urban environment and a link budget, what altitude maximizes the coverage radius?

## System model

- **Propagation.** ATG mean pathloss = free-space pathloss + mean excessive pathloss η_ξ, with two dominant propagation groups ξ ∈ {LoS, NLoS}; spatial expectation Λ = Σ_ξ PL_ξ · P(ξ, θ).
- **LoS probability.** Built from the ITU P.1410 geometric method over three urban statistical parameters: α (built-up land ratio), β (buildings per km²), γ (Rayleigh building-height scale). Approximated by a modified sigmoid P(LoS, θ) = 1/(1 + a·exp(−b[θ − a])), with a, b fit to (αβ, γ) via a two-variable polynomial surface (coefficients tabulated). This sigmoid LoS model is the core of the [[air-to-ground-channel-model]].
- **Coverage.** A service threshold PL_max defines a coverage disk of radius R; the optimization maximizes R over altitude h.

## Method

- Substitute the S-curve LoS model and FSPL into the expected-pathloss equation to get an implicit relation between LAP altitude h and coverage radius R at Λ = PL_max.
- Solve ∂R/∂h = 0 numerically for the optimum altitude h_OPT for each of four environments (suburban, urban, dense-urban, high-rise).
- Reframe in terms of elevation angle and solve ∂R/∂θ = 0 to obtain the **optimum elevation angle θ_OPT**, shown to be independent of PL_max and unique for a given (a, b, A).

## Key findings

- The optimal altitude is a function of the maximum allowed pathloss and the urban statistical parameters; a closed-form LoS-probability expression is provided (the paper's stated contributions).
- A constant optimal elevation angle links h_OPT and R regardless of the pathloss threshold (explains the straight line connecting the tips of the R–h curves).
- For large PL_max the optimum altitude can exceed practical limits, so a physical altitude constraint can be imposed (discussion section). Illustrative figures use PL_max = 10 dB-style settings, f = 2000 MHz, and four environment (η_LoS, η_NLoS) pairs (e.g. suburban (0.1, 21), high-rise (2.3, 34) dB) — read from the parse text; figure curves are indicative.

## Limitations / future work

This is a propagation/coverage-optimization letter, **not** an MEC paper; it carries no offloading, computing, or energy model. Future work (stated): analyze the random behavior of the ATG channel, including large-scale variations and small-scale fading.

## Relation to the corpus

A **foundational channel-model anchor**: this letter is the widely-cited origin of the sigmoid LoS-probability vs elevation-angle model that recurs across the corpus's aerial sources (the statistical sub-family noted in [[blockage-aware-channel-model]], used by [[hsu-2025-drl-hues-hap-noma]], [[bao-2025-ddpg-video-offloading]], and many others). It grounds the new [[air-to-ground-channel-model]] concept page and contrasts LAPs with the [[high-altitude-platform-station|HAPs]] of the hierarchical-aerial track; the rapid-recovery framing connects to [[post-disaster-mec]].

## Raw artifacts

- `raw/sources/Optimal_LAP_Altitude_for_Maximum_Coverage/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
