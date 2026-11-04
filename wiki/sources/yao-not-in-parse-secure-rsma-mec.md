---
type: source
title: "Latency Minimization for Secure RSMA-Assisted Mobile Edge Computing Networks"
authors: ["Jianping Yao", "Chao Tang", "Jie Xu", "Yi Fang", "Guojun Han", "Tony Q. S. Quek"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, rate-splitting-multiple-access, secure-offloading, internal-eavesdropper, mobile-edge-computing, block-coordinate-descent]
related:
  - "[[rate-splitting-multiple-access]]"
  - "[[physical-layer-security]]"
  - "[[task-offloading]]"
  - "[[computation-peer-offloading]]"
  - "[[jianping-yao]]"
  - "[[jie-xu]]"
  - "[[yi-fang]]"
  - "[[guojun-han]]"
  - "[[tony-q-s-quek]]"
created: 2026-11-02
updated: 2026-11-03
---

# Latency Minimization for Secure RSMA-Assisted Mobile Edge Computing Networks

## Citation

Yao, J., Tang, C., Xu, J., Fang, Y., Han, G., & Quek, T. Q. S. *Latency Minimization for Secure RSMA-Assisted Mobile Edge Computing Networks*. Venue, year, and DOI are not in the parse.

## TL;DR

An edge user offloads task segments to several helper users with rate-splitting multiple access, but each helper may eavesdrop on the others' segments. The paper minimizes total latency over offloading ratios, common-message rates, and the precoder under secrecy-rate and power constraints, solved by block coordinate descent with SCA.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna edge user (EU) splits its task among $K$ helper users (HUs). With RSMA, it sends a common message decoded by all HUs and private streams per HU through precoder $\mathbf W$. Each HU is a legitimate receiver of its own segment and a potential internal eavesdropper of the others.

**Problem & objective**: (P1): $\min_{\mathbf r,\mathbf W,\boldsymbol\beta}t(\mathbf r,\mathbf W,\boldsymbol\beta)$, the system latency.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading ratio | $\beta_k$ | $[0,1]$, $\sum_k\beta_k\le1$ | Share of the task sent to HU $k$ |
| Common-message rate | $r_k$ | nonnegative | Portion of the common stream assigned to HU $k$ |
| Precoder | $\mathbf W$ | complex matrix | Common and private stream beamformers |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (12b) | Common-rate decodability, $\sum_jr_j\le R_{c,k}(\mathbf W)$ for every HU. |
| (12c) | Power, $\mathrm{tr}(\mathbf W\mathbf W^{\mathrm H})\le P^{\mathrm{th}}$. |
| (12d) | Offloading ratios, $\sum_k\beta_k\le1$, $0\le\beta_k\le1$. |
| (12e) | Secrecy, $R_{s,k}(\mathbf W)\ge R^{\mathrm{th}}_{s,k}$ for each private stream. |

**Algorithm**: Block coordinate descent over offloading ratios, common rates, and precoder, with SCA convexifying the latency objective and the rate and secrecy constraints.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yao et al. [x] investigated a rate-splitting multiple access assisted secure mobile edge computing network, in which an edge user employs RSMA to securely offload its computation task to multiple helper users that may act as internal eavesdroppers. To keep each offloaded task segment confidential from the other helpers, each helper is treated both as a legitimate receiver of its own message and as a potential eavesdropper of the others. They minimized the total system latency by jointly optimizing the task offloading ratio, the common-message transmission rate, and the precoder matrix under secure offloading and power constraints. The non-convex problem is solved with an iterative algorithm that integrates block coordinate descent and successive convex approximation. In simulations, the design achieved lower latency than secure full offloading and a benchmark without the common stream, and it approached the latency lower bound given by a benchmark without eavesdropping as the transmit power budget grew.

## Problem framing

Offloading to nearby users rather than a server is attractive, but those users are untrusted with respect to one another. RSMA's common stream adds a degree of freedom for both rate and secrecy.

## System model

- Secrecy rate of each private stream is computed against the strongest other HU.
- Latency combines offloading and helper computation.

## Method

BCD with SCA.

## Key findings

- The proposed RSMA design lowers latency compared with benchmark schemes under the same secrecy requirements.

## Limitations / future work

Not stated beyond the presented design.

## Relation to the corpus

Applies [[rate-splitting-multiple-access]] and [[physical-layer-security]] to [[computation-peer-offloading]].

## Raw artifacts

- Parse: `raw/sources/Latency_Minimization_for_Secure_RSMA-Assisted_Mobile_Edge_Computing_Networks/Latency_Minimization_for_Secure_RSMA-Assisted_Mobile_Edge_Computing_Networks.md`
- Extracted figures are in the same folder; no companion PDF is present.
