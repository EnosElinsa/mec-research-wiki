---
type: source
title: "Heuristic-Supervised-DRL: A Unified Optimization Framework with Convergence Analysis"
authors: ["Wei Zhao", "Kai Wang", "Xiangyu Liu", "Zhi Liu", "Nei Kato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3681665"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, heuristic-supervised-drl, two-timescale-optimization, particle-swarm-optimization, multi-agent-reinforcement-learning, uav-mec]
related:
  - "[[heuristic-supervised-drl]]"
  - "[[two-timescale-optimization]]"
  - "[[particle-swarm-optimization]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[ppo]]"
  - "[[ctde-multi-agent-drl-protocol]]"
modeling_card: not_applicable
created: 2026-07-07
updated: 2026-07-16
---

# Heuristic-Supervised-DRL: A Unified Optimization Framework with Convergence Analysis

## Citation

Zhao, W., Wang, K., Liu, X., Liu, Z., & Kato, N. (2026). *Heuristic-Supervised-DRL: A Unified Optimization Framework with Convergence Analysis*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3681665.

## TL;DR

Proposes HSD, a closed-loop hybrid framework where a heuristic upper-tier planner chooses slow strategic variables, a DRL/MARL lower tier executes fast control, and an online supervised predictor estimates the downstream value of candidate plans. The key contribution is not just a PSO-MARL case study: the paper models the predictor/policy updates as a two-timescale stochastic approximation and gives conditional convergence and robustness statements for the coupled loop.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] proposed Heuristic-Supervised-DRL, a unified framework for coupling heuristic planning with DRL through an online supervised predictor. The upper tier searches slow strategic variables using the predictor as a fitness oracle, while the lower tier executes fast control and returns observed values for predictor and policy updates. They analyzed the coupled updates through two-timescale stochastic approximation and established conditional convergence to an asymptotically stable equilibrium, with bounded planner error yielding convergence to a neighborhood. A PSO-MARL UAV-MEC case study was used to evaluate the framework for trajectory planning and communication-computation resource allocation. The reported case-study results show higher task-completion ratio and long-term reward, lower normalized delay, and improved performance over the version without the predictive bridge and the evaluated baselines.

## Problem framing

Hybrid heuristic-plus-DRL systems often use heuristics for high-dimensional planning and DRL for reactive control, but many are open-loop or empirically justified only. In online hierarchical systems, the value of an upper-tier candidate depends on a lower-tier policy that is changing during learning. HSD targets that nonstationarity by continuously retraining a supervised bridge from execution feedback.

## System model

The abstract HSD interface has an upper-tier planning variable $x$, a lower-tier action $a$, a state $s$, a heuristic planner, a supervised predictor $f_\theta(s,x)$, and a DRL policy $\pi_\psi(a|s,x)$. The paper's case study instantiates this in a multi-UAV MEC network: PSO plans UAV trajectories, while MARL handles communication and computation resource allocation under task, delay, and utilization objectives.

## Method

HSD executes a repeated plan-execute-learn cycle. The heuristic planner searches upper-tier candidates using the supervised predictor as a cheap fitness oracle; the DRL/MARL agent executes lower-tier control under the selected plan; observed rewards update both the predictor and the policy. The theoretical analysis treats the supervised predictor as the fast-timescale recursion and the policy update as the slow-timescale recursion. Under listed assumptions and conditions, the joint process converges almost surely to an asymptotically stable equilibrium; with bounded planner error, it converges to a neighborhood whose radius scales with the error.

## Key findings

- In the UAV-MEC case study, PSO-MARL reaches about 0.40 task-completion ratio, about 0.42 normalized delay, and long-term reward around 125-135 near convergence, outperforming PPO-JO, Greedy, DTLCM-MADDPG, and PSO-MARL without the predictive bridge.
- Removing the supervised bridge lowers completion from about 0.40 to 0.36, increases delay from about 0.42 to 0.45, and reduces reward from about 125-135 to about 110-120.
- The supervised-model MSE drops from about 4.6e3 to below 1e2 within about 1000 SGD iterations and reaches about 8 after 20,000 updates, matching the intended fast-timescale tracking behavior.
- PSO budget sensitivity shows the default 10-iteration setting gives reward about 133.7 with about 139.5 ms planning time; 5 iterations lowers reward to about 119.9 but reduces time to about 126.1 ms, while 15-20 iterations add overhead with limited reward gain.
- The reported per-slot decision latency for PSO-MARL is 406.285 ms in the default runtime comparison, about 4.06% of the 10 s flight-phase slot.

## Limitations / future work

The convergence result is conditional: it depends on the listed stochastic-approximation assumptions, stability of the employed MARL update, and idealized or bounded heuristic planner error. The case study uses a synchronized slot-based abstraction; a fully asynchronous/event-driven formulation is left for future work. Comprehensive multi-domain validation is also left for future work.

## Relation to the corpus

This paper gives a theory-facing counterpart to the corpus's many empirical hybrid solvers. It connects [[particle-swarm-optimization]] to [[two-timescale-optimization]] through the new [[heuristic-supervised-drl]] concept, while the UAV-MEC case sits beside [[ctde-multi-agent-drl-protocol]] and decomposition-oriented source pages that split slow trajectory planning from fast offloading/resource allocation.

## Raw artifacts

- `raw/sources/Heuristic-Supervised-DRL_A_Unified_Optimization_Framework_With_Convergence_Analysis/Heuristic-Supervised-DRL_A_Unified_Optimization_Framework_With_Convergence_Analysis.md`
- Original PDF and extracted figures (`images/`) in the same folder.
