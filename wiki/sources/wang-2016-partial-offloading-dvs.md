---
type: source
title: "Mobile-Edge Computing: Partial Computation Offloading Using Dynamic Voltage Scaling"
authors: ["Yanting Wang", "Min Sheng", "Xijun Wang", "Liang Wang", "Jiandong Li"]
year: 2016
url: "https://doi.org/10.1109/TCOMM.2016.2599530"
venue: "IEEE Transactions on Communications (IEEE TCOM)"
tags: [source, mobile-edge-computing, dynamic-voltage-scaling, binary-vs-partial-offloading, energy-latency-tradeoff, small-cell-mec, computation-to-communication-ratio, foundational]
related:
  - "[[mobile-edge-computing]]"
  - "[[dynamic-voltage-scaling]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[task-offloading]]"
  - "[[small-cell-mec]]"
  - "[[computation-to-communication-ratio]]"
  - "[[parallel-vs-serial-processing]]"
  - "[[you-2017-meco-resource-allocation]]"
  - "[[zhang-2013-energy-optimal-mcc-stochastic]]"
  - "[[mao-2016-lodco-eh-mec-offloading]]"
  - "[[miettinen-2010-mcc-energy-efficiency]]"
created: 2026-06-02
updated: 2026-06-02
---

# Mobile-Edge Computing: Partial Computation Offloading Using Dynamic Voltage Scaling

## Citation

Wang, Y., Sheng, M., Wang, X., Wang, L., & Li, J. (2016). *Mobile-Edge Computing: Partial Computation Offloading Using Dynamic Voltage Scaling*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2016.2599530. (Manuscript received 26 October 2015; revised 12 April and 1 July 2016; accepted 5 August 2016; date of publication 11 August 2016; date of current version 14 October 2016 → year 2016.)

## TL;DR

A foundational MEC paper that brings **dynamic voltage scaling (DVS)** into **partial computation offloading**, jointly optimizing three knobs at a smart mobile device (SMD): its **computational speed** $f_l$, its **transmit power** $P_t$, and the **offloading ratio** $\lambda$ (fraction of bits executed locally). Two design objectives are studied: **energy consumption minimization (ECM)** and **latency minimization (LM)**. For a single cloud (femto-cloud / FAP) server both are non-convex; the ECM problem is **recast as a convex problem via a variable-substitution technique** and solved optimally in closed form (the **EPCO** algorithm), while the non-convex, non-smooth LM problem is solved to a locally optimal point with a **univariate search**. The work then extends both objectives to a **multiple-cloud-servers** scenario, deriving the optimal computation distribution across servers and the optimal user association in closed form. A headline analytical result: **total offloading can never be optimal once DVS is available** at the SMD.

## Problem framing

Computation offloading broadens what resource-limited SMDs can run, but introduces communication overhead, so the core tension is the **computation-cost vs communication-cost tradeoff**. Prior offloading designs assume a *fixed* SMD computational speed, which is neither energy- nor latency-optimal. DVS lets the SMD adjust its clock/voltage to trade energy against compute time, but it also **complicates partial-offloading decisions**: the chosen speed couples to both the transmit power and the offloading ratio, so existing offloading designs cannot be applied directly. The paper sets out to be the first to design energy-optimal and latency-optimal **partial** offloading strategies when the SMD has DVS capability (a prior work considered DVS only for a local-vs-total-offload binary decision, ignoring computation partitioning, cloud processing time, and SMD receive energy).

## System model

- **Architecture.** A set of cloud-enhanced **femto access points (FAPs)** collaborate to form a **femto-cloud** (an instance of MEC), managed by a small-cell cloud manager (SCM) with offloading/operator/optimization modules. The nearest serving FAP executes the offloaded part; offloading proceeds in three sequential phases — uplink send, cloud execute, downlink return.
- **Application model.** Data-partition-oriented applications profiled by $(I, L_{\max})$: $I$ input bits and an application-dependent latency requirement. CPU cycles $C = \alpha I$; **full granularity** in data partition is assumed (so the optimum is an upper bound to be quantized in practice). $\lambda \in [0,1]$ is the fraction of bits executed locally.
- **Costs.** Local CPU power modeled as $P = k f^3$ (energy per cycle $\propto k f^2$). Uplink/downlink are frequency-flat block-fading Rayleigh channels (FDD) with Shannon rates; offloading energy combines static power, power-amplifier-scaled transmit power, and receive power. Because of parallelism, total latency is $L = \max\{t_l, t_c\}$ (local vs offloaded paths) and total SMD energy is $E = E_l + E_c$.
- **Objectives.** **P1 (ECM):** minimize $E(f_l, P_t, \lambda)$ subject to a latency bound $L \le L_{\max}$ and box constraints on $\lambda, P_t, f_l$. **P2 (LM):** minimize $L(f_l, P_t, \lambda)$ subject to an energy budget $E \le E_{\max}$ plus the same box constraints. Both are non-convex; LM is additionally non-smooth (because of the $\max$).

## Method

- **ECM (P1) → EPCO.** A feasibility analysis derives the range of $L_{\max}$ for which partial offloading is supportable. The non-convex ECM problem is **transformed into a convex problem via variable substitution**, giving the **energy-optimal partial computation offloading (EPCO)** algorithm with closed-form optimal SMD computational speed and transmit power. Structural results characterize when **local execution** is optimal (a derived necessary-and-sufficient condition) and prove that **total offloading cannot be optimal when DVS is used**.
- **LM (P2).** The non-convex, non-smooth latency problem is solved with a **univariate (one-dimensional) search** technique to a locally optimal solution.
- **Multiple-cloud-servers extension.** Both ECM and LM are extended to a scenario where the SMD may offload to a *set* of cloud servers; the paper obtains the **optimal computation distribution among servers** and the **optimal user association** in closed form, accounting for inter-FAP backhaul latency.

## Key findings

- **DVS makes total offloading suboptimal.** A central analytical conclusion: when the SMD can scale its computational speed, the energy-optimal solution always retains some local computation — full offloading is never optimal.
- The ECM problem admits a **globally optimal closed-form** solution (via the convex recast); the LM problem is solved to a local optimum.
- Extensive simulations are reported to **significantly reduce energy consumption and shorten latency** relative to existing offloading schemes. Specific numeric margins are figure-derived; treat exact values as indicative.

## Limitations / future work

For tractability the SMD computational speed is modeled as a **continuous** variable (in practice it is restricted to a discrete set, which would make the problem a mixed-integer NP-hard program), so the reported optimum serves as a **performance upper bound** that must be quantized for real deployments; quantization methods are sketched. The model assumes full-granularity data partitioning and a single serving FAP per task in the single-cloud case. Explicit future-work statements beyond these are `not in parse`.

## Relation to the corpus

An early **MEC fundamentals** anchor and one of the corpus's clearest treatments of the [[energy-latency-tradeoff]] under [[binary-vs-partial-offloading]] (here firmly *partial*, with a continuous ratio $\lambda$). Its femto-cloud / FAP substrate grounds [[small-cell-mec]], and the $\max\{t_l, t_c\}$ latency reflects the [[parallel-vs-serial-processing]] structure that distinguishes partial from full offloading. It is conceptually adjacent to the multiuser MECO resource-allocation policy of [[you-2017-meco-resource-allocation]] (both derive threshold/structural offloading policies under a latency constraint), to the **DVS-based energy-optimal MCC scheduling** of [[zhang-2013-energy-optimal-mcc-stochastic]], and to the green energy-harvesting Lyapunov offloading of [[mao-2016-lodco-eh-mec-offloading]] (which likewise couples offloading with DVFS CPU-frequency control). Its computation-vs-communication-cost framing traces back to the [[computation-to-communication-ratio]] established by [[miettinen-2010-mcc-energy-efficiency]]. The **dynamic voltage scaling** technique it foregrounds is captured in [[dynamic-voltage-scaling]].

## Raw artifacts

- `raw/sources/Mobile-Edge_Computing_Partial_Computation_Offloading_Using_Dynamic_Voltage_Scaling/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
