---
type: source
title: "Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network"
authors: ["Peng Qin", "Min Fu", "Yang Fu", "Jingjing Wang"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3582151"
venue: "IEEE Transactions on Wireless Communications"
tags: [source, uav, mec, blockchain, masac, lyapunov, multi-agent, trajectory, noma, pbft, dpos]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[lyapunov-optimization]]"
  - "[[masac]]"
  - "[[noma]]"
  - "[[air-ground-integrated-network]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-05-28
updated: 2026-06-02
---

# Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network

## Citation

Qin, P., Fu, M., Fu, Y., & Wang, J. (2025). *Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3582151.

Authors with North China Electric Power University and Beihang University.

## TL;DR

Joint design of (a) UAV trajectories, (b) terminal sensing-data admission, (c) terminal transmission power, and (d) UAV edge resource allocation across compute *and* blockchain workloads — under long-term queue-delay and block-creation-delay constraints. The hard part is that constraints are long-term but decisions are per-time-slot.

Solution stack: **[[lyapunov-optimization|Lyapunov optimization]]** to decouple the long-term constraints into per-slot drift+penalty problems, then split the per-slot problem into three subproblems solved by **CVX** (sensing admission), **[[masac|MASAC (multi-agent SAC)]]** (transmission power + UAV trajectory), and **DOA (Dingo Optimization Algorithm)** (compute / block-resource split). Reports +13.16% data sensing rate and –29.47% queue delay vs benchmarks.

## Problem framing

Setup: $J$ IoT devices + $K$ UAVs over $T$ time slots. Each UAV is *both* a compute node *and* a blockchain node (DPoS for processor selection, PBFT for consensus on offload-task records). Devices admit a portion $e_j(t)$ of randomly arriving sensed data $s_j(t)$, offload it to the nearest UAV via [[noma|NOMA]] uplink, and the UAV processes it while concurrently running blockchain block-generation / consensus.

Objective: maximize long-term average admitted sensing rate

$$
\max\;\lim_{T\to\infty} \frac{1}{T} \sum_{t,j} e_j(t)
$$

subject to long-term queue stability of $Q_j(t)$ (terminal queue) and $H_{j,k}(t)$ (UAV queue), plus a long-term cap on block-creation delay $\delta_k^g(t)$ to keep security overhead from drowning the compute.

Decision variables: $\{e_j(t), p_{j,k}(t), \theta_k(t), v_k(t), f^c_{j,k}(t), f^b_k(t), f^{b,v}_k(t)\}$.

## System model highlights

- **Trajectory:** fixed altitude $H$, per-slot heading $\theta_k(t)$ and speed $v_k(t)$. 2-D, but extends naturally to 3-D.
- **Channel:** [[noma|NOMA]] within a UAV cluster, orthogonal across UAVs. Probabilistic LoS / NLoS path loss with elevation-dependent LoS probability $p_{j,k}^{LoS}$.
- **Queues:** FIFO at both terminal and UAV. Little's Law gives queue delay $\delta_j^Q(t) = Q_j(t) / \tilde e_j(t)$.
- **Blockchain:** DPoS picks block processor; PBFT consensus has block-generation, propagation, and verification phases — each costing UAV CPU cycles that compete with the offloaded compute.

## Method (Section V)

### Layer 1 — Lyapunov decoupling

Define virtual queues for each long-term constraint, write the drift-plus-penalty Lyapunov function $\Delta(\Theta) - V \cdot \mathbb{E}[\sum_j e_j(t)]$, and minimize the upper bound of this expression at each time slot. This converts the original stochastic long-term problem into a per-slot deterministic one.

### Layer 2 — Three subproblems per slot

1. **Sensing admission $e_j(t)$** — convex in isolation, solved with CVX.
2. **Transmission power $p_{j,k}(t)$ + UAV trajectory $(\theta_k, v_k)$** — non-convex, multi-agent. Solved with **AGIN-MASAC**: each terminal and each UAV is an SAC agent in a multi-agent learning loop. Centralized critic, decentralized actors.
3. **UAV resource allocation** — split CPU between offload-compute, block-generation, and block-verification. Solved with **DOA (Dingo Optimization Algorithm)** — a swarm-intelligence heuristic that is cheap enough to run per-slot.

## Findings

- **vs MADDPG, NT-MASAC (no trajectory opt), NP-MASAC (no power opt), PSO-resource:** the joint scheme improves long-term average data sensing rate by **>13.16%** and reduces queue delay by **>29.47%** over the strongest baseline.
- **Trajectory optimization matters more than power optimization** — NT-MASAC suffers a larger gap than NP-MASAC, suggesting that movement is the dominant lever in dense, mobile UAV-MEC.
- **MASAC vs MADDPG** — SAC's entropy-regularized objective gives more stable convergence in the multi-agent setting than MADDPG's deterministic policies, an empirical echo of pure-RL results.

## Limitations / future work

- Fixed altitude — extension to 3-D trajectory acknowledged but not evaluated.
- DOA is a metaheuristic with no convergence guarantee; competitive but the authors don't analyze its bound.
- Block processor selection is taken as given (DPoS); attack on the DPoS election layer is out of scope. Compare with [[mao-2025-bcsa-frl]] which explicitly hardens consensus voting via [[ccvm-correction-voting]].

## Cross-link with related sources

- Shares the **blockchain-on-edge** thread with [[mao-2025-bcsa-frl]] — both layer consensus on top of MEC, but Mao et al. attack the trust problem at the FL aggregation layer (CCVM/CSRA), while Qin et al. attack the resource-contention problem at the per-slot allocation layer (Lyapunov + DOA).
- Shares the **multi-UAV trajectory + DRL** thread with [[liu-2026-jppo-en-convntm]] — both pick continuous-action DRL for UAV control, but Qin et al. additionally need to balance an on-chain workload that Liu et al. don't have.

## Raw artifacts

- `raw/sources/Cooperative_UAV_Trajectory_Design_and_Resource_Allocation_in_Blockchain-Enabled_Secure_Aerial_Edge_Computing_Network/full.md`
- Original PDF and extracted figures.
