---
type: source
title: "Aerial RIS-Enhanced Communications: Joint UAV Trajectory, Altitude Control, and Phase Shift Design"
authors: ["Bin Li", "Dongdong Yang", "Lei Liu", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3621306"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, aerial-ris, uav-mounted-ris, uav-trajectory-control, soft-actor-critic, prioritized-experience-replay, beamforming, sum-rate-maximization]
related:
  - "[[liu-2026-passive-6dma]]"
  - "[[passive-six-dimensional-movable-antenna]]"
  - "[[tilt-aware-aerial-ris-control]]"
  - "[[uav-mounted-ris]]"
  - "[[uav-trajectory-control]]"
  - "[[soft-actor-critic]]"
  - "[[prioritized-experience-replay]]"
  - "[[collaborative-beamforming]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[huang-2025-fedx-ris-uav-trajectory]]"
  - "[[dusit-niyato]]"
created: 2026-07-10
updated: 2026-07-16
modeling_card: required
---

# Aerial RIS-Enhanced Communications: Joint UAV Trajectory, Altitude Control, and Phase Shift Design

## Citation

Li, B., Yang, D., Liu, L., & Niyato, D. (2026). *Aerial RIS-Enhanced Communications: Joint UAV Trajectory, Altitude Control, and Phase Shift Design*. **IEEE Transactions on Wireless Communications**, 25, 5830-5845. DOI: 10.1109/TWC.2025.3621306.

## TL;DR

Optimizes aerial RIS communication when the UAV-mounted RIS does not behave like a position-only reflector. The controller accounts for UAV motion, Euler-angle tilt, orientation-dependent RIS gain, and phase shifts; BS beamforming is handled separately by ZF plus water-filling, while SAC with prioritized experience replay learns the continuous RIS/UAV control policy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV-mounted aerial RIS serves single-antenna ground users from a multi-antenna BS when direct BS-user links can be blocked; RIS gain depends on position, incidence angles, and UAV attitude.

**Problem & objective**: Jointly control aerial-RIS motion and attitude, RIS sub-surface phases, and BS beamforming to maximize horizon sum rate, $\max\sum_l\sum_kR_k[l]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV position and motion | $\mathbf q[l],\mathbf v[l],\mathbf a[l]$ | continuous, bounded | Horizontal trajectory, speed, and acceleration of the ARIS carrier |
| Euler-angle variation | $\widetilde{\boldsymbol\Phi}[l]$ | continuous bounded increments | Roll, pitch, and yaw changes used for attitude control |
| RIS phase shifts | $\boldsymbol\Theta[l]$ | continuous phases, quantized if required | Shared phase of each RIS sub-surface |
| BS beamforming | $\mathbf W[l]$ | complex matrix under power budget | Zero-forcing and water-filling beamformer computed for the current ARIS state |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | BS transmit power and per-user beamforming satisfy the power budget. |
| C2 | RIS phases and Euler angles, including per-slot angle variations, remain physically bounded. |
| C3 | UAV position stays in the permitted region and speed and acceleration obey their maxima. |
| C4 | Flight energy remains nonnegative and the safety penalties for leaving the region or violating motion limits are avoided. |
| C5 | In multi-ARIS extensions, inter-ARIS distance stays above the minimum separation. |

**Algorithm**: Cast sequential control as an MDP, compute BS beamforming with zero forcing plus water-filling or bisection, and train a maximum-entropy SAC policy with prioritized experience replay and automatic temperature tuning.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied aerial-RIS communication with attitude-aware UAV motion, sub-surface phase shifts, and separate BS beamforming. They maximized horizon sum rate under transmit-power, phase, Euler-angle, flight-region, speed, acceleration, energy, and safety constraints, while the source model captures orientation-dependent RIS gain. Their SAC-PER controller learns the continuous motion and phase policy and uses zero-forcing with water-filling for the BS beamformer. Simulations report convergence near 150 thousand steps and up to 14.4% higher sum rate than PPO, with additional gains from larger RISs, BS arrays, energy budgets, and multi-ARIS deployment.

## Problem

Existing aerial-RIS studies often optimize UAV trajectory and RIS phase shifts while treating RIS gain as if it were independent of UAV attitude. For a quadrotor carrying a RIS, acceleration and deceleration change the UAV's Euler angles, which changes incidence/reflection geometry and can misalign the reflected beam. The paper targets the resulting sum-rate loss under realistic aerial RIS motion and energy constraints.

## System model

- A multi-antenna BS serves $K$ single-antenna ground users through a UAV-mounted RIS; direct BS-user links may be unreliable or blocked.
- The RIS has $N$ elements, grouped into sub-surfaces that share phase shifts.
- Time is slotted over a finite flight horizon.
- The UAV/ARIS state includes position, velocity, acceleration, Euler angles, energy, and achieved sum rate.
- BS-ARIS and ARIS-user channels use Rician fading.
- ARIS gain depends on incidence and reflection angles through an exponential-Lambertian radiation pattern.

## Method

The objective maximizes total sum rate over the flight horizon by jointly controlling UAV attitude/motion, RIS phase shifts, and BS beamforming under transmit-power, phase, Euler-angle, safety, flight-energy, region, speed, and acceleration constraints. The paper casts the sequential control part as an MDP. The action space includes Euler-angle variations and sub-surface RIS phase shifts; BS beamforming is computed outside the DRL policy using zero forcing and water-filling/bisection. The learning algorithm is SAC with automatic entropy-temperature tuning and prioritized experience replay.

## Key findings

- SAC-PER converges around 150K training steps in the parsed experiment, while PPO and vanilla SAC converge around 200K and DDPG performs poorly.
- The RIS-elements experiment reports up to 14.4% higher sum rate for SAC-PER than PPO.
- Among learning rates 0.0001, 0.001, and 0.01, the parsed experiment identifies 0.0001 as the best setting.
- The default simulation uses ARIS initial position $(20,20,100)$ m, BS position $(100,100,10)$ m, a 150 m by 150 m area, $K=8$ users, $M=8$ BS antennas, $N=40$ RIS elements, $T=30$, $L=60$, maximum speed 15 m/s, and maximum acceleration 5 m/s^2.
- More RIS elements, more BS antennas, and higher BS transmit power improve sum rate.
- Larger energy budgets, tested at 8500, 9000, and 9500 J, allow more aggressive early motion and higher sum rate.
- A multi-ARIS extension with $I=2$ converges around 400K steps and improves performance under a minimum inter-ARIS distance constraint.

## Limitations / extraction notes

The validation is simulation-only. The robustness discussion models trajectory uncertainty from inaccurate positioning or wind gusts with Gaussian perturbations. The local parse's title and framing emphasize altitude control, but the main system model also fixes altitude $H$; the source page therefore treats the grounded control variables conservatively as UAV attitude/motion, RIS phase shifts, and BS beamforming. Future work in the parse points to dynamic user mobility, imperfect CSI, and distributed multi-agent learning.

## Relation to the corpus

This source sharpens [[uav-mounted-ris]] from placement/phase-shift optimization into [[tilt-aware-aerial-ris-control]], where UAV attitude affects the RIS radiation gain. It complements [[pan-2025-uav-ris-energy-efficient-comm]], which optimizes multiple UAV-mounted RIS locations and phase shifts for energy-efficient communication, and [[huang-2025-fedx-ris-uav-trajectory]], which accelerates RIS-assisted trajectory learning. Its SAC-PER solver also extends the [[soft-actor-critic]] and [[prioritized-experience-replay]] branches beyond MEC offloading into aerial RIS control.

## Raw artifacts

- Parse: `raw/sources/Aerial_RIS-Enhanced_Communications_Joint_UAV_Trajectory_Altitude_Control_and_Phase_Shift_Design/Aerial_RIS-Enhanced_Communications_Joint_UAV_Trajectory_Altitude_Control_and_Phase_Shift_Design.md`
- Origin PDF: `raw/sources/Aerial_RIS-Enhanced_Communications_Joint_UAV_Trajectory_Altitude_Control_and_Phase_Shift_Design/Aerial_RIS-Enhanced_Communications_Joint_UAV_Trajectory_Altitude_Control_and_Phase_Shift_Design.pdf`
- Figures: `raw/sources/Aerial_RIS-Enhanced_Communications_Joint_UAV_Trajectory_Altitude_Control_and_Phase_Shift_Design/images/`
