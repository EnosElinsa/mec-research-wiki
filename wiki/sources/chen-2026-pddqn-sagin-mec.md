---
type: source
title: "Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation"
authors: ["Haosheng Chen", "Haixia Cui", "Peng Cao", "Yejun He", "Jun Li", "Ivan Wang-Hei Ho", "Victor C. M. Leung"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3706356"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), 25, 2026"
modeling_card: required
tags: [source, sagin, leo-satellite-edge-computing, uav-mec, task-offloading, hybrid-action, parameterized-dqn, ddqn, ddpg]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[hybrid-action-decision-making]]"
  - "[[parameterized-dqn]]"
  - "[[ddqn]]"
  - "[[ddpg]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[device-association]]"
  - "[[victor-c-m-leung]]"
created: 2026-07-07
updated: 2026-07-16
---

# Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation

## Citation

Chen, H., Cui, H., Cao, P., He, Y., Li, J., Ho, I. W.-H., & Leung, V. C. M. (2026). *Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation*. **IEEE Transactions on Wireless Communications**, 25, 19115-19130. DOI: 10.1109/TWC.2026.3706356. (DOI/venue/year verified against the title-matched Crossref/IEEE DOI record; the parse header itself does not print the DOI.)

## TL;DR

Proposes a MEC-enabled SAGIN for remote areas where IoT devices can compute locally, offload to a UAV edge server, or offload to LEO satellite edge servers. The optimization minimizes weighted energy plus latency under satellite coverage-time and partial-offloading constraints. Because device association and satellite selection are discrete while transmit power, task ratios, and trajectory variables are continuous, the paper uses a parameterized DDQN (P-DDQN) that combines DDQN for discrete actions with DDPG for continuous parameters.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground IoT devices offload computation to one mobile UAV MEC server and multiple LEO satellite MEC servers, or execute locally. The UAV trajectory changes coverage while each satellite offers a time-limited service window determined by orbital geometry.

**Problem & objective**: The joint MINLP minimizes weighted delay and energy, $\min_{\mathbb A,\mathbb D,\mathbb U,\mathbb P}\sum_{n=1}^{N}\sum_{m=1}^{M}\alpha_m(n)\,\mathrm{Cost}^{\mathrm{sys}}_m(n)$, with $\mathrm{Cost}^{\mathrm{sys}}_m=\sigma T_m^{\mathrm{total}}+(1-\sigma)E_m^{\mathrm{total}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Association control | $\mathbb A=\{\alpha_m(n),\beta_m(n)\}$ | binary | IoT scheduling and satellite or UAV association |
| Task assignment | $\mathbb D=\{D_m^l,D_m^u,D_m^s\}$ | continuous, nonnegative | Local, UAV, and LEO task portions |
| UAV trajectory | $\mathbb U=\{u(n)\}$ | continuous 3-D path | UAV position and movement over slots |
| Transmit powers | $\mathbb P=\{P_{mu}^t,\hat P_{m,k}^t\}$ | continuous, bounded | IoT power to UAV and satellite $k$ |
| Hybrid action | $a(n)=\{j(n),a_j(n)\}$ | mixed | Discrete choice plus continuous parameters selected by P-DDQN |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each scheduled IoT device has one association: $\sum_m\alpha_m(n)=1$. |
| C2 | Each IoT device uses at most one LEO satellite: $\sum_k b_{m,k}(n)\le1$. |
| C3 | Satellite service delay fits its remaining coverage time: $T_{m,k}^{s}(n)\le T_{m,k}^{re}(n)$. |
| C4 | Task portions sum to the generated task: $D_m^l(n)+D_m^u(n)+D_m^s(n)=D_m(n)$. |
| C5 | IoT transmit powers are bounded: $0\le P_{mu}^t(n)\le P_{mu}^{\max}$ and $0\le P_{m,k}^t(n)\le P_{m,k}^{\max}$. |
| C6 | The required task volume is processed: $\sum_{n,m}\alpha_m(n)D_m(n)\ge D_{\mathrm{total}}$. |

**Algorithm**: Represent each discrete action with a DDPG-style continuous policy parameter, use a DDQN critic to select the discrete action, update actor and critic alternately with double-DQN targets and soft target updates, and train from replayed hybrid-action transitions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] formulated MEC in a space-air-ground integrated network with local, UAV, and LEO execution for each IoT task. Their weighted delay-energy MINLP jointly selects user and satellite associations, partial task portions, transmit powers, and a three-dimensional UAV trajectory under satellite coverage time, power, assignment, and task-completion constraints. P-DDQN combines a DDPG policy that generates continuous parameters with a DDQN critic that selects the discrete branch, avoiding direct discretization of the hybrid action space. The method converged near the reported reward after about 500 episodes and kept per-slot cost around 2.30 versus about 2.65 with fixed altitude, while more LEO satellites reduced cost further.

## Problem framing

Remote and underdeveloped regions lack terrestrial base-station support, while UAV-only MEC is constrained by coverage and energy. LEO satellites add wide-area coverage and stronger compute, but their moving coverage windows restrict feasible satellite offloading. The resulting resource-allocation problem couples UAV 3D trajectory, IoT-device association, transmit power, satellite association, and partial task assignment.

## System model

- **Layers.** Ground IoT devices, one UAV MEC server, and multiple LEO satellites with MEC servers.
- **Coverage.** UAV coverage depends on its 3D position; LEO service is constrained by remaining satellite coverage time derived from orbital geometry and minimum elevation angle.
- **Tasks.** Each IoT task can be partitioned for local execution, UAV execution, and LEO execution.
- **Objective.** Minimize a weighted sum of delay and energy while respecting UAV battery, communication, compute, and partial-offloading constraints.

## Method

The paper formulates a long-term sequential optimization problem with a hybrid action space. P-DDQN parameterizes each discrete action with continuous variables: DDQN selects discrete decisions such as user scheduling and satellite association, while a DDPG-style policy network generates continuous parameters such as task-offloading ratios and transmit powers. The double-DQN target is used to reduce Q-value overestimation relative to P-DQN.

## Key findings

- P-DDQN reaches the highest reward among P-DQN, PPO, DDPG, and DDQN baselines in the reported training comparison, converging around the reported reward level after roughly 500 episodes.
- System cost rises with task CPU-cycle demand and IoT-device count; P-DDQN remains below the baseline costs, with larger advantage when task complexity exceeds 1 Gcycle.
- System cost decreases as the number of LEO satellites increases because higher satellite density improves access probability, elevation, and coverage duration.
- Ablations show fixed transmit power and fixed UAV altitude increase system cost; the per-slot comparison reports P-DDQN around 2.30 system cost, fixed altitude around 2.65, and fixed power as the most unstable/higher-cost case.
- Optimized UAV altitude adapts to IoT-device distribution, flying higher for dispersed devices and lower for dense devices to reduce energy when long-range coverage is less necessary.

## Limitations / future work

The conclusion proposes extending the framework to more complex SAGIN scenarios with multi-UAV cooperative optimization, and exploring multi-agent hybrid-action algorithms based on soft actor-critic for broader evaluations.

## Relation to the corpus

This source strengthens the [[space-air-ground-integrated-network]] / [[leo-satellite-edge-computing]] offloading track with a native hybrid-action DRL formulation. It is close to [[chen-2024-ulse-game]] in using UAV-LEO cooperation and coverage-time constraints, but solves a joint offloading/resource/trajectory problem with P-DDQN rather than a game-theoretic distributed best-response. Methodologically it extends [[parameterized-dqn]] beyond vehicular MEC and connects [[ddqn]], [[ddpg]], [[hybrid-action-decision-making]], and [[leo-satellite-coverage-time]]. Co-author [[victor-c-m-leung]] links it to the wiki's recurring senior-collaborator roster.

## Raw artifacts

- `raw/sources/Mobile-Edge Computing in SAGINs A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation/Mobile-Edge Computing in SAGINs A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation.md`
- Original PDF and extracted figures (`images/`) in the same folder.
