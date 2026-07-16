---
type: source
title: "Cooperative UAV-Mounted RISs-Assisted Energy-Efficient Communications"
authors: ["Hongyang Pan", "Yanheng Liu", "Geng Sun", "Qingqing Wu", "Tierui Gong", "Pengfei Wang", "Dusit Niyato", "Chau Yuen"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3579597"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags:
  - source
  - intelligent-reflecting-surface
  - uav-mounted-ris
  - energy-efficient-mec
  - multi-objective-reinforcement-learning
  - constrained-multi-objective-evolutionary-algorithm
  - non-dominated-sorting-genetic-algorithm
  - drone-cell-3d-placement
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[drone-cell-3d-placement]]"
  - "[[energy-latency-tradeoff]]"
  - "[[geng-sun]]"
  - "[[yanheng-liu]]"
  - "[[qingqing-wu]]"
  - "[[dusit-niyato]]"
  - "[[cmop-evolutionary-uav-mec-lineage]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
created: 2026-06-03
updated: 2026-07-16
modeling_card: required
---

# Cooperative UAV-Mounted RISs-Assisted Energy-Efficient Communications

## Citation
Hongyang Pan, Yanheng Liu, Geng Sun, Qingqing Wu, Tierui Gong, Pengfei Wang, Dusit Niyato, Chau Yuen, "Cooperative UAV-Mounted RISs-Assisted Energy-Efficient Communications," *IEEE Transactions on Mobile Computing*, 2025. DOI: 10.1109/TMC.2025.3579597. (Received 22 May 2024; revised 21 Jan 2025; accepted 10 Jun 2025; date of publication 12 Jun 2025; date of current version 3 Sep 2025 → year 2025. Corresponding author: Geng Sun. Jilin University + Dalian Maritime University + Nanyang Technological University + Shanghai Jiao Tong University + Dalian University of Technology.)

## TL;DR
This paper studies a **cooperative UAV-mounted RIS (UAV-RIS)** cellular network where several RISs carried by UAVs jointly serve multiple ground users (GUs) when the direct BS→GU links are unavailable, exploiting **3D mobility and opportunistic deployment**. It formulates an **energy-efficient communication multi-objective optimization framework (EEComm-MOF)** that **simultaneously** (i) maximizes the minimum per-GU available rate (fairness), (ii) maximizes the total available rate (capacity), and (iii) minimizes total system energy (cost), jointly over the BS beamforming vector, the UAV-RIS 3D locations, and the **discrete** RIS phase shifts, under the BS transmit-power constraint. Because the problem is NP-hard, non-convex, and Pareto-conflicting, it proposes **INSGA-II-CDC** — an improved NSGA-II with continuous, discrete, and complex solution-processing mechanisms — to return a Pareto solution set in one run.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A ground BS with $N_{\mathrm{BS}}$ antennas serves $K$ ground users through $M$ cooperative UAV-RISs because direct BS-user links are unavailable. Each UAV-RIS has $N_{\mathrm{RIS}}$ passive elements and is deployed at a 3-D hovering location.

**Problem & objective**: Return a Pareto set for $\min\langle-f_1,-f_2,f_3\rangle$, where $f_1=\min_kR_k$ is the minimum available rate, $f_2=\sum_kR_k$ is total available rate, and $f_3=E_{\mathrm{pro}}+E_{\mathrm{hov}}$ is total deployment plus hovering energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| BS beamforming | $\mathbf w=[\mathbf w_1;\ldots;\mathbf w_K]$ | complex vectors | Active beam for each GU |
| UAV-RIS location | $\mathbf q_{\mathrm U m}$ | continuous 3-D | Hovering location of UAV-RIS $m$ |
| RIS phase shifts | $\theta_{m,n_m}$ | discrete, $\theta_{m,n_m}\in\mathcal C$ | Quantized phase of each reflecting element |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Horizontal deployment bounds: $L_{\min}\le x_{\mathrm U m}\le L_{\max}$ |
| C2 | Horizontal deployment bounds: $L_{\min}\le y_{\mathrm U m}\le L_{\max}$ |
| C3 | Altitude bounds: $Z_{\min}\le z_{\mathrm U m}\le Z_{\max}$ |
| C4 | Discrete phase set: $\theta_{m,n_m}\in\mathcal C$ with $\lvert\mathcal C\rvert=2^c$ |
| C5 | BS transmit power: $\mathbf w^H\mathbf w\le P_{\max}$ |

**Algorithm**: Run an improved NSGA-II with continuous operators for 3-D locations, discrete random and learning operators for quantized phases, and complex-solution normalization for BS beamforming; rank candidates by Pareto dominance and retain a diverse non-dominated set.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Pan et al. [x] study cooperative UAV-mounted RISs in a cellular network where direct BS-user links are blocked. Their EEComm-MOF jointly optimizes BS beamforming, 3-D UAV-RIS locations, and discrete RIS phases for minimum available rate, total available rate, and total deployment plus hovering energy. The proposed INSGA-II-CDC extends NSGA-II with continuous, discrete, and complex solution processing and uses Pareto dominance rather than scalar weighting. Simulations report higher minimum and total available rates and lower energy than evolutionary baselines for five- and ten-user deployments, together with convergence and Raspberry Pi implementability analyses.

## Problem framing
RIS reconfigures the wireless environment with cheap passive elements, but fixed RIS placement (on facades) limits energy efficiency and coverage; mounting RISs on UAVs adds flexible, opportunistic 3D deployment (faster and more controllable than balloons, while tethered balloons sacrifice deployment freedom). With many GUs, a single limited-size RIS can't serve everyone, and UAVs can't carry arbitrarily large surfaces, motivating **cooperative multiple UAV-RISs**. Prior work mostly considered a single UAV-RIS, or only 2D mobility, or folded multiple objectives into a single weighted scalar; the gap is jointly optimizing **multiple UAV-RISs serving multiple GUs** over 3D location + discrete phase shifts + BS beamforming under **true Pareto** multi-objective treatment.

## System model
- **Topology (Fig. 1):** one ground BS, several GUs with the direct BS→GU links entirely blocked, and M cooperative UAV-RISs in 3D space reflecting BS signals to all GUs simultaneously; mutual interference exists among the reflected links, so UAV-RIS placement matters.
- **Decision variables:** BS transmit beamforming vector; 3D location deployment of each UAV-RIS; **discrete** phase shifts of each UAV-RIS (chosen for hardware practicality over continuous shifts).
- **Energy model:** total system energy combines UAV flight energy consumption and communication energy consumption (the paper distinguishes both in its related-work comparison table).
- **Objectives (EEComm-MOF):** max-min available rate, max total available rate, min total energy — fair service vs system capacity vs system cost, with trade-offs among them; constrained by the BS transmit-power budget. The paper states it is the first to jointly tune 3D UAV-RIS locations, discrete phase shifts, and BS beamforming for multiple UAV-RISs serving multiple GUs under simultaneous multi-objective goals.

## Method
- **INSGA-II-CDC:** an **improved non-dominated sorting genetic algorithm-II** (see [[non-dominated-sorting-genetic-algorithm]]) extended with three mechanisms — a **continuous** solution-processing mechanism (better UAV-RIS locations, faster convergence), a **discrete** solution-processing mechanism (handles discrete RIS phase shifts), and a **complex** solution-processing mechanism (handles the complex-valued BS beamforming vector) — to jointly enhance search within limited iterations.
- **Pareto-dominance treatment:** rather than scalarizing the three objectives, the algorithm uses Pareto dominance so a full solution set is produced per run, letting decision-makers pick by need without re-running — placing it in the corpus's [[constrained-multi-objective-evolutionary-algorithm|CMOEA]] family.

## Key findings
Grounded in the abstract/contributions (benchmark-relative improvements quoted from the contributions list; treated as indicative since they are reported against the suboptimal benchmark per objective):
- For a 5-GU network, versus the best benchmark per objective, the proposed approach reports the minimum available rate enhanced by **74.62%**, total available rate improved by **64.45%**, and energy consumption saved by **10.55%**.
- For a 10-GU network, the reported figures are minimum available rate **+43.75%**, total available rate **+89.57%**, and energy **−13.60%**.
- The paper also reports verification of INSGA-II-CDC's convergence/optimality, stability, effectiveness of the three mechanisms, and CPU running time, plus an implementability analysis.

## Limitations / future work
- Results are simulation-based; the paper closes with an implementability analysis rather than a hardware deployment.
- The numerical improvements are reported relative to the best benchmark per objective, so they describe Pareto-front advantage rather than absolute optimality.
- Discrete phase shifts and a fixed number of cooperative UAV-RISs bound the design space; UAV propulsion/flight dynamics are captured through an energy term rather than full flight control.
- The direct BS→GU link is assumed entirely unavailable, an idealization that isolates the reflected-link design.

## Relation to the corpus
This is a UAV-RIS communications design whose distinctive angle is **cooperative multiple UAV-RISs** under a genuine three-objective Pareto formulation, captured in the new [[uav-mounted-ris]] concept and solved with an [[non-dominated-sorting-genetic-algorithm|NSGA-II]] variant that places it squarely in the [[constrained-multi-objective-evolutionary-algorithm|CMOEA]] solver family and the [[cmop-evolutionary-uav-mec-lineage]] lineage. It complements the corpus's other IRS/RIS-on-UAV work such as [[wu-2025-iopo-irs-uav-thz-mec]] (THz IRS-UAV-MEC), differing by optimizing **3D RIS placement + discrete phase shifts + BS beamforming** rather than offloading. Its author set ties it to the Jilin-University/NTU aerial cluster — [[geng-sun]], [[yanheng-liu]], [[qingqing-wu]], [[dusit-niyato]].

## Raw artifacts
- Parse: `raw/sources/Cooperative_UAV-Mounted_RISs-Assisted_Energy-Efficient_Communications/full.md`
- Origin PDF: `raw/sources/Cooperative_UAV-Mounted_RISs-Assisted_Energy-Efficient_Communications/8a131dd8-afe7-4f31-b1fa-e4560e6847ef_origin.pdf`
- Figures: `raw/sources/Cooperative_UAV-Mounted_RISs-Assisted_Energy-Efficient_Communications/images/`
