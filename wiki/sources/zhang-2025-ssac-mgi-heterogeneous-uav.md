---
type: source
modeling_card: required
title: "Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled Mobile Edge Computing"
authors: ["Xiuling Zhang", "Riheng Jia", "Quanjun Yin", "Zhonglong Zheng", "Minglu Li"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3632884"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, uav, mec, heterogeneous, safe-rl, trajectory, sac, collision-avoidance, multi-agent]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[masac]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[safe-reinforcement-learning]]"
  - "[[collision-avoidance-mgi]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[riheng-jia]]"
  - "[[minglu-li]]"
created: 2026-05-28
updated: 2026-07-16
---

# Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled MEC

## Citation

Zhang, X., Jia, R., Yin, Q., Zheng, Z., & Li, M. (2025). *Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3632884.

## TL;DR

Existing UAV-MEC schedulers assume **homogeneous** UAVs and uniform UE distributions — wrong for real deployments. This paper allows each UAV to carry a *subset* of service types with different resource budgets per type. The result: a UAV can only serve jobs whose service type it actually hosts, which forces UAVs to fly farther to find compatible jobs and inflates flight-energy.

Solution: **SSAC-MGI** — a multi-agent safe RL algorithm with two cooperating modules:

1. **SSAC (Shared Soft Actor-Critic)** — UAVs share a backbone for the *common* features (positions, time) but have heterogeneous heads for service-type-specific features. Lets the multi-agent system learn jointly without forcing identical capability assumptions.
2. **MGI (Markov Game of Intervention)** — a per-UAV two-agent safe-RL design. Each UAV is jointly controlled by a **Standard Agent** (a stochastic, reward-maximizing policy that minimizes job miss rate + UAV/UE energy) and a **Safety Agent** (a deterministic, risk-averse policy plus a binary *gating* policy `g(s)`). When the gate triggers (`g(s)=1`), the Safety Agent's action overrides the Standard Agent's; otherwise the Standard Agent acts. The Safety Agent pays a cost for each intervention, encouraging selective overrides. This gives safety guarantees during *and* after training, unlike reward-shaping baselines.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Heterogeneous fixed-altitude UAVs act as mobile edge servers with different onboard service types and CPU and memory capacities. Static or mobile UEs generate deadline-constrained workflows at unknown locations and upload each accepted job to one compatible UAV over an air-to-ground link.

**Problem & objective**: The multi-objective Dec-POMDP minimizes the job miss rate and normalized UE and UAV energy, $\min_{\mathcal Q}F(\mathcal Q)$, while separately minimizing cumulative safety-violation cost.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV flight action | $a_n^t=\{\varphi_n^t,v_n^t\}$ | continuous, $\varphi_n^t\in[\varphi_{\min},\varphi_{\max}]$, $v_n^t\in[0,V_{\max}]$ | Rotation angle and flight speed of UAV $n$ |
| Job association | $y_{n,k}^t$ | binary, $\{0,1\}$ | Whether job $k$ is uploaded to UAV $n$ |
| Execution instances | $x_{v_k^i,vm_n^r}^t$ | integer, $\mathbb Z_0^+$ | Number of parallel instances allocated to subtask $v_k^i$ on service type $r$ |
| UE transmit power | $p_m^t$ | continuous, $[0,p_{\max}]$ | Uplink power used by UE $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each job is associated with at most one UAV: $\sum_n y_{n,k}^t\leq1$. |
| C2 | Allocated CPU cores remain within $vcpu_n^r$ for every UAV and service type. |
| C3 | Allocated memory remains within $vmem_n^r$ for every UAV and service type. |
| C4 | Flight speed and UE power satisfy $v_n^t\leq V_{\max}$ and $0\leq p_m^t\leq p_{\max}$. |
| C5 | A safety violation is measured when $\lVert l_n^t-o_j^t\rVert_2<2r_d$ and is handled by the learned intervention policy. |

**Algorithm**: Run shared SAC modules for the standard, safety, and binary intervention policies, let the intervention gate select the executed flight action, allocate workflow instances with deadline-aware round robin, store policy-specific transitions, and update the three modules from replay buffers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied safe and energy-efficient trajectory planning in a heterogeneous multi-UAV enabled MEC network with unknown UE locations, stochastic job arrivals, diverse service requirements, and UAV-specific onboard resources. They formulated a Dec-POMDP that reduces job miss rate and average UAV and UE energy while accounting for service compatibility, association, computing-capacity, mobility, and collision-safety conditions. Their SSAC-MGI framework combines shared Soft Actor-Critic policies with a two-agent Markov Game of Intervention, in which a safety policy can override a standard flight action, and embeds a deadline-aware round-robin instance allocator. Real-trace-driven simulations using Alibaba workflows and UE locations show higher cumulative rewards and lower safety-violation costs than the evaluated adapted baselines, with lower UAV energy than the manual trajectory policy.

## Problem framing

Variables:

- UAV trajectories (continuous).
- Per-UAV per-slot job admission (which UE jobs to serve).
- Resource allocation per service type per UAV.

Objectives (multiplexed via reward):

- Minimize job miss rate (jobs that don't complete by deadline).
- Minimize average UAV energy consumption.
- Minimize average UE energy consumption.
- Maintain flight safety (no UAV-UAV collisions).

## Method specifics

- **Heterogeneous service representation.** Each UAV state includes a one-hot of its service-type set + per-type resource budget. SSAC's shared encoder ignores the type vector; per-head decoders condition on it.
- **Constraint shaping.** Safety is *not* folded into the reward — it is enforced by the per-UAV Safety Agent's triggered intervention (binary gating policy overriding the Standard Agent), giving safety guarantees during and after training that reward-shaping cannot.

## Findings

- On real-trace-driven simulations (UE locations from Twitter, workflow traces from the Alibaba cluster dataset), SSAC-MGI achieves the highest cumulative reward and the lowest safety-violation cost versus the adapted baselines: SSAC and STRPO (unconstrained reward-shaping MARL), SCPO (constrained MARL via CPO), the SSAC-MGI-FCFS resource-allocation variant, and a handcrafted MANUAL trajectory policy.
- Decoupling reward maximization (Standard Agent) from safety enforcement (Safety Agent) yields faster convergence and far lower in-flight collision risk than embedding safety into the reward.
- The MANUAL policy can reach a slightly lower job miss rate and UE energy via fully synchronized coverage trajectories, but at much higher UAV energy and safety-violation cost; SSAC-MGI's residual miss-rate gap shrinks as more UAVs are deployed.
- The heterogeneity-aware shared SSAC encoder lets all UAVs train jointly (no inter-UAV communication needed at execution) rather than per-UAV-isolated training.

## Limitations / future work

- UAVs fly at a **constant altitude** (UEs modeled at ground level, $z=0$), so trajectory planning is effectively 2-D over a $500\times500$ grid; full 3-D maneuvering is not modeled.
- Service-type set per UAV is modeled as pre-configured onboard capacity; live re-provisioning of onboard service types is not discussed in the parse.
- The parse's stated future work is **multi-modal perception and online fine-tuning**: image-based UE localization, obstacle detection, near-range UAV identification, and richer historical-trajectory observations to guide planning.

## Cross-link with related sources

- Same UAV-trajectory + multi-agent DRL family as [[liu-2026-jppo-en-convntm]] and [[peng-2025-drudm-cfg]]. The novel ingredient is **heterogeneity** + **safety as an explicit Markov-game constraint**.
- Composes with [[hierarchical-aerial-mec]] — heterogeneous UAVs at the lower tier can specialize, with HAPS as the catch-all.

## Comparison boundary

The Safety Agent's binary gate is a persistent intervention mechanism under the paper's sensing and intervention model, not an unconditional collision certificate for every neural policy or environment. The guarantee boundary is recorded in [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- `raw/sources/Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing/Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing.md`
