---
type: source
modeling_card: required
title: "A UAV-Assisted Coordination Framework for Emergency Vehicle Priority and CAV Speed Optimization in Hybrid Human-Machine Driving on Expressways"
authors: ["Jinrui Zang", "Zhengyang Liu", "Guohua Song", "Xin Hu"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3651592"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, uav-assisted-its, emergency-vehicle-priority, cav, robust-optimization, pso, expressway]
related:
  - "[[speed-coordinated-robust-optimization-control]]"
  - "[[uav-enabled-its]]"
  - "[[uav-data-collection]]"
  - "[[particle-swarm-optimization]]"
created: 2026-07-10
updated: 2026-11-03
---

# A UAV-Assisted Coordination Framework for Emergency Vehicle Priority and CAV Speed Optimization in Hybrid Human-Machine Driving on Expressways

## Citation

Zang, J., Liu, Z., Song, G., & Hu, X. (2026). *A UAV-Assisted Coordination Framework for Emergency Vehicle Priority and CAV Speed Optimization in Hybrid Human-Machine Driving on Expressways*. **IEEE Transactions on Intelligent Transportation Systems**, 27(5), 6093-6109. DOI: 10.1109/TITS.2026.3651592.

## TL;DR

Uses UAV sensing and relaying to coordinate emergency-vehicle priority on expressways with mixed human-driven vehicles and CAVs. The core contribution is speed-coordinated robust optimization control (SROC): select an objective-lane CAV and schedule CAV speed adjustments so human lane changes clear space ahead of an emergency vehicle under uncertain merge timing.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: UAVs sense and relay mixed traffic state on a two-lane expressway containing an emergency vehicle (EV), human-driven vehicles, connected vehicles, and CAVs. An objective-lane CAV (O-CAV) and an evacuation-lane CAV (E-CAV) adjust speed so that non-priority vehicles in the EV's lane can merge, while human lane-change acceptance margins and durations are uncertain.

**Problem & objective**: The speed-coordinated robust optimization control (SROC) is an integer nonlinear min-max problem (7)/(23): minimize over the O-CAV choice and speed-adjustment times the worst case, over the uncertainty sets, of the EV travel loss $J_1=1-\frac{x_E(t_{end}^{impact})-x_E(t_{start})}{V_E(t_{end}^{impact}-t_{start})}$; objective (8), $J_2$, is the alternative non-priority-vehicle impact measure.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| O-CAV selection | $s_{O-CAV}$ | discrete, $\{CAV_1,\ldots,CAV_n\}$ | CAV in the objective lane chosen to open a gap |
| E-CAV adjustment times | $t_{1,a}^1,t_{1,b}^1$ | continuous | Start and end of E-CAV speed adjustment |
| O-CAV adjustment times | $t_{2,a}^1,t_{2,b}^1$ | continuous | Start and end of O-CAV speed adjustment |
| Adjustment order | $\sigma$ | binary | 1 if the O-CAV adjusts speed first, 0 if the E-CAV does |
| Uncertainty (inner max) | $M_{TC}^r(i),M_{TC}^p(i),\Delta t_c(i)$ | bounded intervals (11), (12), (17) | Accepted collision margins and lane-change durations of human drivers |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (1)-(4) | Piecewise speed profiles of the O-CAV and E-CAV with comfortable deceleration $a_c$ |
| (5) | Adjusted speeds stay nonnegative, the E-CAV stays below its leader's speed, and safe gaps to preceding vehicles are kept |
| (6) | In the gap-creation cases, the E-CAV's adjusted speed exceeds the O-CAV's |
| (11)-(13), (17) | Uncertainty sets for collision margins and lane-change time, and the margin condition that triggers a lane change |
| (14)-(16) | Fifth-degree polynomial lane-change trajectories with their boundary conditions |

**Algorithm**: Fuse UAV and connected-vehicle state → solve the inner worst-case search over margins and lane-change time with PSO → solve the outer search over O-CAV selection and adjustment times with PSO → execute the control and observe lane changes → re-optimize with rolling SROC when some vehicles have finished changing lanes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zang et al. [x] studied UAV-assisted emergency-vehicle priority and CAV speed optimization on expressways with mixed human and automated traffic. UAV sensing and relaying provide vehicle state to a controller that selects an objective-lane CAV and schedules speed adjustments to create human lane-change gaps. The robust integer nonlinear formulation minimizes worst-case emergency-vehicle travel loss or non-priority impact under uncertain merge timing and lane-change duration. A dual-layer particle swarm optimizer searches the uncertainty and control variables, while rolling SROC recomputes after observed lane changes. Simulations report shorter emergency-vehicle evacuation time and earlier obstructing-vehicle lane changes than one-time SROC and no-CAV-control baselines.

## Problem

Emergency vehicles can be delayed when human-driven vehicles respond slowly or need space to merge out of the evacuation lane. Pure traffic-signal priority or rule-based clearing does not directly control the gaps available to those vehicles on expressways. The paper uses UAV-collected vehicle states plus CAV speed control to create merge opportunities and shorten emergency-vehicle evacuation time.

## System model

- A two-lane expressway scenario contains an emergency vehicle, non-connected vehicles, connected human-driven vehicles, CAVs in the evacuation lane, and CAVs in the objective lane.
- UAVs collect non-connected vehicle position/speed, fuse it with V2V/V2I/OBD/camera information, relay it to a control center, warn obstructing vehicles, and issue V2U/CAV coordination instructions.
- Human uncertainty is modeled through merge-timing-control and lane-change-duration uncertainty sets.
- Lane-change trajectories use fifth-degree polynomials; following behavior uses IDM, CACC, and ACC models.

## Method

The paper formulates an integer nonlinear program over O-CAV selection, speed-adjustment timing, and the order of O-CAV versus E-CAV adjustment. Robust objectives minimize either emergency-vehicle travel-distance loss or non-priority-vehicle impact. A dual-layer PSO solves the min-max structure: the inner layer searches worst-case human timing and lane-change duration, and the outer layer chooses CAV selection and speed-control timing. A rolling SROC variant recomputes after observed lane changes.

## Key findings

- In the parsed base scenario, the emergency vehicle starts at -125 m with speed 16.6 m/s, the preceding vehicle is at 95 m with speed 8.3 m/s, and O-CAV candidates are at 91, 118, and 136 m.
- Compared with one-time SROC, rolling SROC reduces evacuation time by 17.3%; emergency-vehicle time to 850 m is 90 s for rolling SROC, 105 s for one-time SROC, and 120 s without CAV control.
- Lane-change start/end times advance for all four obstructing vehicles, with an average advancement of 14.2%.
- As CAV penetration improves, reducing evacuation-lane vehicles from 9 to 5 cuts rolling-SROC evacuation time from 105 s to 62 s.
- Selecting the O-CAV initially at 136 m yields 35 s evacuation time and 181 m emergency-vehicle travel distance, versus 63 s and 489 m for the 91 m candidate.
- Communication delay from 200 ms to 500 ms changes CAV speeds only slightly in the parsed sensitivity study, and rolling SROC shows no substantial emergency-vehicle distance change.

## Relation to the corpus

This is an ITS control source rather than an MEC offloading source. It extends [[uav-enabled-its]] toward road-priority coordination: UAVs act as sensing/relay infrastructure, while the actual control lever is CAV speed. It links to [[particle-swarm-optimization]] because PSO is the robust min-max solver, not just a tuning baseline.

## Limitations / extraction notes

The local Markdown parse is missing top-level DOI, venue, and year; the bibliographic fields above come from local PDF metadata. OCR artifacts affect Table I and one acceleration-comparison sentence, so the source page avoids the inconsistent acceleration claim.

## Raw artifacts

- Parse: `raw/sources/A_UAV-Assisted_Coordination_Framework_for_Emergency_Vehicle_Priority_and_CAV_Speed_Optimization_in_Hybrid_Human-Machine_Driving_on_Expressways/A_UAV-Assisted_Coordination_Framework_for_Emergency_Vehicle_Priority_and_CAV_Speed_Optimization_in_Hybrid_Human-Machine_Driving_on_Expressways.md`
- Origin PDF: `raw/sources/A_UAV-Assisted_Coordination_Framework_for_Emergency_Vehicle_Priority_and_CAV_Speed_Optimization_in_Hybrid_Human-Machine_Driving_on_Expressways/A_UAV-Assisted_Coordination_Framework_for_Emergency_Vehicle_Priority_and_CAV_Speed_Optimization_in_Hybrid_Human-Machine_Driving_on_Expressways.pdf`
- Figures: `raw/sources/A_UAV-Assisted_Coordination_Framework_for_Emergency_Vehicle_Priority_and_CAV_Speed_Optimization_in_Hybrid_Human-Machine_Driving_on_Expressways/images/`
