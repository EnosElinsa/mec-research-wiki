---
type: source
title: "3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting"
authors: ["Changsheng You", "Rui Zhang"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2911939"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-data-collection, wireless-sensor-network, trajectory-optimization, rician-fading, outage-probability, block-coordinate-descent, successive-convex-approximation]
related:
  - "[[uav-data-collection]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[zhan-2011-uav-relay-heading-optimization]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# 3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting

## Citation

You, C., & Zhang, R. (2019). *3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2019.2911939.

## TL;DR

Optimizes a UAV's 3-D trajectory and sensor scheduling for wireless-sensor-network data harvesting under angle-dependent Rician fading. Instead of assuming deterministic LoS channels, the paper models a Rician factor tied to the UAV-sensor elevation angle, approximates the outage-aware effective fading power with a logistic regression model, then solves the resulting max-min data-rate problem with block coordinate descent and SCA.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV harvests data from ground sensor nodes over angle-dependent Rician fading. It follows a three-dimensional route from a prescribed start to a prescribed finish and schedules at most one sensor per time slot.

**Problem & objective**: Problem P1 maximizes the worst sensor's average outage-aware rate, $\max_{\mathbf q,z,\mathbf a}\eta$, subject to $\frac1M\sum_ma_n[m]R_n[m]\geq\eta$ for every sensor $n$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Horizontal trajectory | $\mathbf q[m]$ | continuous position | UAV planar position in slot $m$ |
| Altitude | $z[m]$ | continuous, $z[m]\geq H$ | UAV height in slot $m$ |
| Sensor scheduling | $a_n[m]$ | binary | Indicates whether sensor $n$ transmits in slot $m$ |
| Common rate | $\eta$ | continuous, nonnegative | Minimum average rate guaranteed across sensors |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 11a | Every sensor's average outage-aware rate is at least $\eta$ |
| 11b | Horizontal displacement is at most $S_{xy}$ per slot |
| 11c | Vertical displacement is at most $S_z$ per slot |
| 11d-11e | The three-dimensional trajectory has prescribed initial and final points |
| 11f | UAV altitude satisfies $z[m]\geq H$ |
| 11g-11h | At most one sensor is scheduled per slot and all scheduling variables are binary |

**Algorithm**: The inverse-Marcum-Q effective fading power is approximated by an elevation-dependent logistic function fitted to numerical channel data. Block coordinate descent then alternates an optimal scheduling linear program with horizontal and vertical trajectory subproblems, each solved by successive convex approximation until the max-min objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

You and Zhang [x] optimized three-dimensional UAV trajectory and sensor scheduling for outage-constrained data harvesting under angle-dependent Rician fading. Their max-min formulation chooses horizontal position, altitude, and a binary sensor schedule under mobility, endpoint, altitude, and single-access constraints. A logistic regression model approximates the effective fading power obtained from the inverse Marcum-Q relation and exposes its dependence on elevation angle. Block coordinate descent alternates sensor scheduling with successive-convex-approximation updates for horizontal and vertical trajectories. At a 26-second mission duration, the reported Rician-aware design achieved about twice the max-min rate of the line-of-sight benchmark. Under outage probability 0.01, it improved the achieved max-min rate by about 1.5 times, while the optimized altitude balanced fading improvement against added path loss.

## Problem

UAV data-collection papers often optimize 2-D routes at a fixed altitude and assume simplified LoS links. That can be inaccurate in urban/suburban settings where small-scale fading remains relevant. This paper asks how a data-collection UAV should jointly choose horizontal motion, altitude, and sensor scheduling when the achievable rate must satisfy a per-sensor outage probability constraint.

## System model

- A UAV collects sensing data from multiple ground sensor nodes.
- Each sensor transmits only when scheduled/woken by the UAV.
- The objective maximizes the minimum average data-collection rate across sensors.
- The UAV-SN channel uses Rician fading whose factor grows with the elevation angle; the reliability constraint is expressed through a maximum tolerable outage probability.

## Method

- The effective fading power needed for outage-aware rate calculation has no convenient closed form, so the paper fits a logistic S-shaped function to numerical data.
- The approximate optimization is decomposed into communication scheduling, horizontal trajectory, and vertical trajectory blocks.
- The horizontal and vertical trajectory subproblems are handled by successive convex approximation inside a block-coordinate-descent loop.

## Key findings

- Under moderate mission duration, the Rician-fading-based design can attain about two times the max-min rate of the LoS-based benchmark at T = 26 s.
- With stringent outage probability, the proposed Rician-fading-based design improves achieved max-min rate over the LoS-based benchmark by about 1.5 times when epsilon = 0.01.
- The optimized altitude balances two effects: higher elevation angle increases effective fading power, while larger distance increases path loss.
- The conclusion names multi-UAV extension with joint 3-D trajectories, scheduling, resource allocation, and 3-D collision avoidance as a natural next step.

## Relation to the corpus

This is a foundational UAV-data-harvesting/channel-model source rather than an MEC offloading paper. It extends [[uav-data-collection]] and [[air-to-ground-channel-model]] with [[angle-dependent-rician-fading]], a channel model that sits between deterministic LoS simplifications and geometry/statistical LoS-probability models. Its BCD/SCA solution connects to [[alternating-optimization-sdr-sca]] and complements the fixed-/rotary-wing trajectory-energy foundations in [[zeng-2017-energy-efficient-uav-trajectory]] and [[xu-2018-uav-wpt-trajectory]].

## Raw artifacts

- `raw/sources/3D_Trajectory_Optimization_in_Rician_Fading_for_UAV-Enabled_Data_Harvesting/3D_Trajectory_Optimization_in_Rician_Fading_for_UAV-Enabled_Data_Harvesting.md`
- Original PDF and extracted figures (`images/`) in the same folder.
