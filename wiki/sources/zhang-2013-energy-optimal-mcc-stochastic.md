---
type: source
title: "Energy-Optimal Mobile Cloud Computing under Stochastic Wireless Channel"
authors: ["Weiwen Zhang", "Yonggang Wen", "Kyle Guan", "Dan Kilper", "Haiyun Luo", "Dapeng Oliver Wu"]
year: 2013
url: "https://doi.org/10.1109/TWC.2013.072513.121842"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, mobile-cloud-computing, computation-offloading, energy-latency-tradeoff, dynamic-voltage-frequency-scaling, stochastic-channel, convex-optimization]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[virtual-machine-multiplexing]]"
  - "[[mao-2016-lodco-eh-mec-offloading]]"
  - "[[mao-2017-mec-survey-communication]]"
created: 2026-06-01
updated: 2026-07-16
modeling_card: required
---

# Energy-Optimal Mobile Cloud Computing under Stochastic Wireless Channel

## Citation

Zhang, W., Wen, Y., Guan, K., Kilper, D., Luo, H., & Wu, D. O. (2013). *Energy-Optimal Mobile Cloud Computing under Stochastic Wireless Channel*. **IEEE Transactions on Wireless Communications**, 12(9), 4569–4581. DOI: 10.1109/TWC.2013.072513.121842. (Received 20 Nov 2012; revised 19 Feb 2013; accepted 24 Jun 2013.)

## TL;DR

An early **mobile cloud computing (MCC)** offloading paper that builds a theoretical framework for **minimizing mobile-device energy** by choosing **mobile execution** (run the app locally) vs **cloud execution** (offload to a cloud clone running on a VM), under a **stochastic wireless channel** modeled by a **Gilbert-Elliott** Markov process, subject to an application completion **deadline**. For local execution it optimally schedules **CPU clock frequency** (via Dynamic Voltage Scaling, DVS); for cloud execution it optimally schedules the **data transmission rate** against the random channel. Both are cast as **convex optimization** problems with **closed-form** optimal scheduling policies, and for small-output-data apps a simple **threshold policy** on the data consumption rate decides where to execute.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A mobile application is executed either locally on a battery-limited device or remotely on its cloud clone. The single mobile-to-cloud link does not model multiuser multiple access; its wireless state follows a two-state Gilbert-Elliott Markov channel, while local CPU workload is probabilistic and controlled through dynamic voltage scaling.

**Problem & objective**: Choose the execution mode with minimum device energy, $\min\{\mathcal E_m^*,\mathcal E_c^*\}$; local execution solves $\min_{\{f(w)\}}\kappa\sum_{w=1}^{W_\rho}F_W^c(w)f^2(w)$, and cloud execution solves $\min_{\{s_t\}}\mathbb E[\sum_{t=1}^{T}\mathcal E_t(s_t,g_t)]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Execution choice | Eq. (5), comparing $\mathcal E_m^*$ and $\mathcal E_c^*$ | binary, mobile or cloud | Selects the lower-energy local-computation or cloud-offloading mode |
| CPU clock schedule | $f(w)$ | continuous, $f(w)>0$ | Frequency used after completing CPU cycle $w$ |
| Transmitted bits | $s_t$ | continuous relaxation, $s_t\geq0$ | Input bits sent to the cloud in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 10 | The allocated workload meets the completion probability, $F_W(W_\rho)\geq\rho$ |
| 14 | Local execution meets the deadline, $\sum_{w=1}^{W_\rho}1/f(w)\leq T$ |
| 19a | Cloud execution transmits all input bits, $\sum_{t=1}^{T}s_t=L$ |
| 19b | Every slot allocation is nonnegative, $s_t\geq0$ |
| 5 | Select mobile execution when $\mathcal E_m^*\leq\mathcal E_c^*$ and cloud execution otherwise |

**Algorithm**: Derive the closed-form optimal DVS frequency schedule and its minimum expected local energy; solve the Gilbert-Elliott transmission schedule by dynamic programming in closed form; compare the two minimum energies; for small-output applications, implement the resulting threshold rule on the effective data consumption rate $R_e=L/T$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied energy-optimal mobile cloud computing under a stochastic wireless channel. They minimized mobile-device energy by choosing between mobile execution and cloud execution subject to an application completion deadline. For mobile execution, they optimized the CPU clock-frequency schedule under a probabilistic workload model, while for cloud execution they optimized the transmitted bits over a Gilbert-Elliott channel. Closed-form scheduling policies were derived for both cases, followed by a threshold execution policy based on the effective data consumption rate for applications with small output data. Numerical results include a case in which cloud execution consumed thirteen times less energy than mobile execution for the evaluated application profile.

## Problem framing

The tension between resource-hungry applications and resource-poor, battery-limited mobile devices is a central driver of mobile-platform evolution; limited battery life is consistently the top user complaint. Cloud offloading (Cloudlet, CloneCloud, Weblet) can extend device capability, but prior work on *when to offload* typically assumed a **fixed transmission data rate**, ignoring channel randomness. This paper instead treats the wireless channel as **stochastic** (Gilbert-Elliott good/bad states) and pairs it with a realistic local-computing energy model, deriving optimal energy-conserving policies under a deadline.

## System model

- **Platform.** Each mobile device has a system-level **clone running on a cloud VM** (nearby cloud infrastructure) that can migrate with the user and synchronizes state; an app runs either on the device (**mobile execution**) or on the clone (**cloud execution**) — application offloading.
- **Mobile execution.** Energy minimized by scheduling **CPU clock frequency** via **DVS**; super-linear energy-vs-frequency relationship.
- **Cloud execution.** Transmission energy minimized by scheduling the **data transmission rate** over a **stochastic (Gilbert-Elliott) channel**.
- **Constraint / objective.** Each formulated as a constrained convex problem: minimize device energy subject to completing the application within a **time deadline** $T$ for input data size $L$.

## Method

- Formulate both scheduling problems as **convex optimization** and derive **closed-form** optimal schedulers and minimum device-energy expressions.
- Provide **asymptotic analysis** of the optimal policies and identify the **operational region** where mobile vs cloud execution is more energy-efficient.
- Derive a **threshold policy** (Theorem 6.1) for apps with **small output data** (e.g., CloudAV antivirus, face recognition): compare the **effective data consumption rate** $R_e = L/T$ against a threshold $R_{th} = \lceil M/C(n)\rceil^{1/(n-3)}$ that depends on the energy-consumption model (monomial order $n$) and the channel model. The reported energy-coefficient ratio example is $\kappa/\lambda = 6.67\times 10^{-12}$ (verbatim).

## Key findings

- A **significant amount of device energy** can be saved by optimally offloading to the cloud **in some cases** — but not always; the optimal choice depends on the application profile $(L,T)$, the transmission energy model, and the energy-coefficient ratio (the paper's stated, deliberately conditional, conclusion).
- The **threshold policy** gives a simple, deployable rule for small-output-data applications: evaluate $L/T$ against $R_{th}$ to pick mobile vs cloud execution.
- Treating the channel as **stochastic** (vs the prior fixed-rate assumption) and coupling it with a realistic compute-energy model is the methodological advance over the authors' prior work.

## Limitations / future work

Single-device, single-application focus with small-output-data emphasis (the threshold result targets apps like CloudAV). The summary section flags further directions; the framework is theoretical with numerical validation.

## Relation to the corpus

An **early mobile-cloud-computing offloading** anchor that predates and feeds the MEC-era offloading literature. Its "where to execute under an energy/deadline trade-off" question and DVS/DVFS + transmission-rate control are the conceptual ancestors of the [[energy-latency-tradeoff]] and [[binary-vs-partial-offloading]] machinery formalized for MEC in [[mao-2016-lodco-eh-mec-offloading]] (which adds energy harvesting and a Lyapunov online algorithm) and catalogued in [[mao-2017-mec-survey-communication]]. Its cloud-clone-on-VM model relates to [[virtual-machine-multiplexing]].

## Raw artifacts

- `raw/sources/Energy-Optimal_Mobile_Cloud_Computing_under_Stochastic_Wireless_Channel/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
