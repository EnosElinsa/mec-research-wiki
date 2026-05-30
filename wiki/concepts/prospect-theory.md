---
type: concept
title: "Prospect Theory"
tags: [decision-theory, risk-aware, uncertainty, game-theory]
related:
  - "[[nash-equilibrium]]"
  - "[[qoe-modeling-mec]]"
  - "[[task-offloading]]"
  - "[[apostolopoulos-2021-prospect-theory-uav-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Prospect Theory

A behavioral decision model (Kahneman & Tversky) describing how people actually decide **under risk and uncertainty**, as an alternative to pure expected-utility theory. Its key departures: the utility (value) function is defined over **gains and losses** relative to a reference point rather than absolute wealth, is **concave for gains and convex for losses** (so people are risk-averse over gains, risk-seeking over losses), and is **steeper for losses** (loss aversion); probabilities are reweighted subjectively. The upshot is that an agent's perceived payoff under uncertainty is probabilistic and deviates from the risk-neutral expected value.

## Why an MEC paper uses it

In offloading, the classical assumption is that users are rational expected-utility maximizers. Prospect Theory instead models **risk-aware** users whose offloading choices reflect risk-seeking / loss-aversion — useful when some compute options have **uncertain** payoff (e.g. energy-constrained UAV servers that may fail to serve), making the offloading decision a gamble rather than a deterministic optimization.

## In this wiki

[[apostolopoulos-2021-prospect-theory-uav-offloading]] uses prospect-theoretic utility functions so that users treat **UAV-mounted MEC servers** as an uncertain "common pool of resources" (superior but risky) versus the safe/guaranteed local-computing and ground-MEC options. The resulting competition is a non-cooperative game whose Pure [[nash-equilibrium|Nash Equilibrium]] is proven unique. This is the corpus's distinct example of behavior-aware [[qoe-modeling-mec|user-satisfaction]] modeling in [[task-offloading]].
