---
type: source
modeling_card: required
title: "Joint Deployment and Resource Allocation Design for JRC-Enabled Multi-UAV Cooperative Systems"
authors: ["Lingyun Zhou", "Chunyong Yang", "Yongqiang Cui", "Rongqing Zhang", "Zhongxiang Wei", "Qingjiang Shi"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3635277"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav, jrc, isac, deployment, resource-allocation, user-association, power-allocation]
related:
  - "[[spectral-clustering-monotone-gibbs-deployment]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cramer-rao-bound]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[device-association]]"
  - "[[rongqing-zhang]]"
  - "[[zhongxiang-wei]]"
  - "[[qingjiang-shi]]"
created: 2026-07-13
updated: 2026-07-16
---

# Joint Deployment and Resource Allocation Design for JRC-Enabled Multi-UAV Cooperative Systems

## Citation

Zhou, L., Yang, C., Cui, Y., Zhang, R., Wei, Z., & Shi, Q. (2026). *Joint Deployment and Resource Allocation Design for JRC-Enabled Multi-UAV Cooperative Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3635277.

## TL;DR

Jointly assigns communication users and FDMA subchannels, allocates communication and sensing power, and places a cooperative UAV fleet. The scalar objective trades the minimum user rate against the maximum sensing-target squared position error bound (SPEB), while alternating optimization combines smooth extrema, convex power updates, and spectral-clustering-initialized Gibbs deployment search.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A central station coordinates $K$ fixed-altitude dual-function UAVs that serve multiple communication users and jointly localize multiple sensing targets. Communication uses FDMA subchannels, sensing and communication occupy separate bands, and quasi-static air-to-ground links follow a free-space LoS model.

**Problem & objective**: Problem (31) is an NP-hard non-smooth MINLP that balances worst-user rate and worst-target SPEB, $\max_{\mathbf A,\mathbf P,\mathbf Q}\omega_1\Psi^{c}-\omega_2\Psi^{s}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User-channel association | $a_{imk}$ | binary | Whether UAV $k$ serves CU $i$ on subchannel $m$ |
| Communication power | $p_{mk}^{c}$ | continuous, nonnegative | UAV $k$ power on communication subchannel $m$ |
| Sensing power | $p_{jk}^{s}$ | continuous, nonnegative | UAV $k$ power assigned to sensing target $j$ |
| UAV deployment | $\mathbf Q=[\mathbf q_1,\ldots,\mathbf q_K]$ | continuous/discrete grid | Fixed-altitude horizontal UAV locations |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every communication user receives exactly one assignment, $\sum_{m,k}a_{imk}=1$ |
| C2 | Each UAV subchannel serves at most one user, $\sum_i a_{imk}\leq1$ |
| C3 | Association entries are binary and all powers are nonnegative |
| C4 | Per-UAV communication plus sensing power satisfies $\sum_jp_{jk}^{s}+\sum_mp_{mk}^{c}\leq p_k^{\max}$ |
| C5 | Inter-UAV distance lies between $d_{\min}$ and $d_{\max}$ |

**Algorithm**: Smooth the minimum-rate and maximum-SPEB terms with log-sum-exp → initialize deployment by spectral clustering → update binary association through implicit enumeration → update power through convex approximation and descent search → refine deployment by monotone reduced-space Gibbs sampling → alternate blocks to convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhou et al. [x] studied joint deployment and resource allocation in a JRC-enabled cooperative multi-UAV system serving communication users and sensing targets. They formulated an NP-hard MINLP that maximizes a weighted difference between the minimum communication-user rate and the maximum sensing-target squared position error bound. The decisions include binary user and FDMA-subchannel association, communication and sensing power allocation, and fixed-altitude UAV deployment under assignment, power, and inter-UAV-distance constraints. Their alternating method smooths the extrema, updates association and power in separate subproblems, and combines spectral-clustering initialization with monotone Gibbs deployment search. Simulations averaged over 100 trials report gains over the evaluated random-association, equal-power, spectral-clustering-only, and uniform-deployment designs.

## System model

- A central station coordinates fixed-altitude dual-function UAVs serving communication users and sensing targets in separate communication and sensing bands.
- Communication performance is the worst user rate. Sensing performance is the worst target SPEB, obtained from the trace of the corresponding Cramer-Rao bound.
- Decisions include binary UAV/user/subchannel association, communication and sensing powers, and horizontal UAV positions, subject to unique assignment, total-power, and minimum/maximum inter-UAV-distance constraints.

## Method

Log-sum-exp smooth approximations replace the non-differentiable minimum and maximum; the paper bounds the smoothing error by a term proportional to the smoothing parameter and `log K`. The alternating solver handles association through an implicit enumeration/MOSEK step, power through first-order convex approximations and line search, and deployment through spectral-clustering initialization followed by a monotone Gibbs search over local and random candidates.

The paper establishes conditional monotonic improvement for its block updates, not global optimality. Association complexity is exponential in the number of communication users (`O((MK)^N_c)` in the paper's notation), and the Gibbs deployment block remains a suboptimal search.

## Key findings

- The reported alternating procedure converges in roughly **8-10 iterations** across the illustrated settings.
- Increasing the communication-to-sensing weight ratio from **0.2 to 5** makes the worst-target SPEB almost three times larger, while the worst-user rate rises by less than 10% in the reported sweep.
- The numerical study averages **100 independent trials** and compares against random user association/channel assignment, equal power allocation, spectral-clustering-only deployment, and uniform deployment baselines.
- Other gains are figure-level trends rather than safely extractable exact values: joint design improves the modeled worst-user/worst-target tradeoff relative to each partial-design baseline.

## Limitations / interpretation

Evidence is simulation-only. The model assumes centralized coordination, known user/target geometry, quasi-static LoS channels, fixed altitude, sufficient separated sensing bandwidth, Gaussian ranging noise, and reliable GPS/IMU support. It does not optimize flight trajectories, propulsion energy, or field-control overhead. The association block is described as an integer linear program although the surrounding smoothed formulation is nonlinear and the derivation is incomplete. The convergence discussion also alternates between a non-increasing transformed objective and prose saying the objective “rapidly increases”; the result should be read as empirical stabilization, not a universal convergence claim.

## Relation to the corpus

This is a scalarized counterpart to [[dual-objective-multi-uav-isac]]: it protects the worst communication user and worst sensing target through extrema inside one weighted objective, rather than returning a Pareto archive. Its deployment routine adds a reusable bridge between geometric clustering and monotone stochastic local search.

## Raw artifacts

- `raw/sources/Joint_Deployment_and_Resource_Allocation_Design_for_JRC-Enabled_Multi-UAV_Cooperative_Systems/Joint_Deployment_and_Resource_Allocation_Design_for_JRC-Enabled_Multi-UAV_Cooperative_Systems.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
