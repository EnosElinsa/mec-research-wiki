---
type: source
title: "Scalable Deployment of Aerial Networks via Radio Tomographic Attenuation Mapping"
authors: ["Ayon Chakraborty", "Subrata Das", "Pranav Ramesh"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3656779"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 9707-9720"
modeling_card: required
tags: [source, aerial-network, radio-environment-map, radio-tomography, uav-placement, measurement-planning]
related:
  - "[[radio-tomographic-attenuation-mapping]]"
  - "[[rank-saturation-rem-updates]]"
  - "[[segment-coverage-uav-trajectory]]"
  - "[[information-driven-uav-spectrum-mapping]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[uncertainty-triggered-radio-map-update]]"
created: 2026-07-14
updated: 2026-07-16
---

# Scalable Deployment of Aerial Networks via Radio Tomographic Attenuation Mapping

## Citation

Chakraborty, A., Das, S., & Ramesh, P. (2026). *Scalable Deployment of Aerial Networks via Radio Tomographic Attenuation Mapping*. **IEEE Transactions on Mobile Computing, 25**(7), 9707-9720. DOI: 10.1109/TMC.2026.3656779.

## TL;DR

SKYSCALE reconstructs a terrain-dependent 3-D attenuation field from UE-UAV measurements, then reuses that field to synthesize radio environment maps for arbitrary UE locations. Depth-based segmentation reduces the inverse problem to segment coefficients, a coverage-oriented trajectory gathers informative rays, and estimated-rank growth controls incremental updates. The benefit is strongest under UE mobility or churn; static deployments can favor direct interpolation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV base station samples uplink RSS from ground UEs at known locations while flying through a discretized three-dimensional aerial region. Stereo-depth segmentation groups terrain voxels into $P$ attenuation segments, RTI reconstructs a UE-independent attenuation field, and forward projection creates one REM per UE so the UAV can select the point with maximum aggregate channel utility.

**Problem & objective**: Equation (10) is an NP-hard maximum-coverage trajectory problem, $\Theta_{opt}=\arg\max_{\Theta}\left|\bigcup_{n\in\Theta}S_n\right|$ subject to $\mathtt{path\_length}(\Theta)\leq c$, which maximizes intercepted terrain segments within the measurement-flight budget.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Measurement trajectory | $\Theta=[\ell^0,\ell^1,\ldots]$ | ordered path over $\mathcal U$ | Sequence of navigable UAV voxels used for RSS collection |
| Next measurement waypoint | $\ell^i$ | discrete, $i\in\mathcal U$ | Greedy next voxel selected by distance per unseen segment |
| Segment attenuation field | $\mathbf x\in\mathbb R^P$ | continuous | One attenuation coefficient for every segmented terrain region |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 9 | Each waypoint exposes a grounded segment set, $S_n=\bigcup_{k=1}^{K}\mathcal Z_{k,n}$ with $S_n\subseteq\{1,\ldots,P\}$ |
| 10 | The ordered path stays within its distance budget, $\mathtt{path\_length}(\Theta)\leq c$ |
| Algorithm 1 | Candidate waypoints are navigable and satisfy $\mathrm{dist}(\ell^{cur},\ell^i)\geq d_{\min}$ |
| 4-5 | Attenuation reconstruction uses the regularized inverse model $\arg\min_{\mathbf x}\|\mathbf A\mathbf x-\mathbf m\|_2^2+\beta\|L\mathbf x\|_2^2$ with $\beta>0$ |

**Algorithm**: SKYSCALE segments the stereo depth map, constructs a reduced ray-segment projection matrix, and plans measurements with distance-weighted greedy set cover plus Bresenham 3-D paths until budget $c$ is exhausted. It solves the Laplacian-regularized RTI inverse problem, forward-projects REMs for current UE locations, selects the maximum-utility operating voxel, and triggers later reconstructions when estimated projection-matrix rank grows meaningfully.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chakraborty et al. [x] studied scalable placement of a UAV base station for mobile or changing ground users by estimating a terrain-dependent three-dimensional attenuation field rather than rebuilding one radio environment map per user. They formulated measurement-trajectory planning as an NP-hard maximum-coverage problem that maximizes the number of intercepted terrain segments under a path-length budget. SKYSCALE segments stereo depth maps to reduce RTI dimensionality, uses a distance-weighted greedy set-cover trajectory, reconstructs attenuation with Laplacian-regularized least squares, and forward-projects user-specific maps to choose the operating point with maximum aggregate utility. In four-user experiments at 100% churn, it reduces average measurement flight time by a factor of 3 to 4 while keeping average REM error within 3 dB, whereas interpolation is about 8% to 10% faster with no churn. In the 16-user study, it reports an 8 to 10 times average-flight-time reduction at high churn and learns the attenuation image after about 600 seconds at 50% churn.

## Problem and system model

A UAV base station must choose a 3-D operating position that gives spatially distributed ground UEs strong aggregate channel quality. Conventional methods build a separate RSS or SNR map for each UE, so movement or churn makes those maps stale and forces another measurement flight.

SKYSCALE separates UE-specific radio environment maps from terrain attenuation that is assumed to persist across UE relocation. The UAV receives uplink transmissions along a discretized 3-D trajectory, with UE locations assumed known. Each measurement ray accumulates attenuation through intersected voxels, producing the inverse problem $A x = m$. A generalized Tikhonov objective with a graph-Laplacian regularizer estimates the attenuation field.

The full voxel problem is too large for the demonstrated onboard Raspberry Pi: a 100 m x 100 m x 50 m region at 1 m resolution has 500,000 voxels. Stereo depth and WATERSHED segmentation therefore group voxels into 3-D regions that share an attenuation coefficient. The reduced projection matrix stores ray length through each segment, replacing $N$ voxel unknowns with $P \ll N$ segment unknowns.

## Method

[[radio-tomographic-attenuation-mapping]] builds one reusable attenuation image and forward-projects it to estimate a REM for any UE location. Candidate aerial points aggregate the UE maps, with median RSS given as an example utility, and the point with maximum utility becomes the operating position.

[[segment-coverage-uav-trajectory]] formulates measurement planning as an NP-hard maximum-coverage problem. A distance-weighted greedy set-cover heuristic selects UAV voxels that reveal unseen terrain segments under a path-length budget and minimum movement distance. The minimum distance is predicted from segmented-depth statistics and voxel resolution; the prose reports 5-8 m prediction error while retaining 90%-95% of optimal performance.

Measurements accumulate across flights and UE locations. [[rank-saturation-rem-updates]] uses meaningful estimated projection-matrix rank growth, rather than the offline 3 dB REM-error criterion, to decide when additional information warrants reconstruction. QR most closely follows true rank, Lanczos is the proposed accuracy-efficiency compromise, and convex-hull area is a low-cost relative proxy.

The testbed uses a custom quadcopter with Pixhawk 2.4.8, Raspberry Pi 4, stereo camera, 2.4 GHz WiFi, seven Raspberry Pi UEs, and more than 10,000 measurements in a 75 m x 75 m arena. The evaluation also uses a seven-smartphone SKYRAN LTE trace and two 3.59 GHz SIONNA ray-traced terrains.

## Key findings

- Against SKYRAN interpolation in four-UE experiments, SKYSCALE reduces average measurement flight time by a factor of 3-4 at 100% churn while maintaining average REM error within 3 dB. With no churn, SKYRAN is about 8%-10% faster because RTI adds unnecessary reconstruction overhead.
- In 16-UE experiments, the prose reports an 8-10x average-flight-time reduction at high churn. At 50% churn, the attenuation image is learned after about 600 s of cumulative flight and then supports reliable REM prediction without further measurements.
- Fig. 13's caption reports about 300 s of measurements for 3 dB average REM accuracy at 50% churn on TERR1/TERR2. This is figure-caption-derived, not a separately quantified prose result. The 500 m trajectory budget in Fig. 16 is also figure-caption-derived.
- A U-Net trained from complete REMs at seven UE locations, about 10,000 measurements, and about 20 minutes of flight has a prose-reported 8-10 dB median error for arbitrary UE locations. The prose reports 30-180x higher energy consumption for the compared U-Net/FASTSAM segmentation methods than for WATERSHED.
- Across all 35 splits of seven testbed UEs into four map-building and three served UEs, placement has median losses of 3-4 dB RSS and 1-3 Mbps TCP throughput relative to the optimal position; these are losses, not absolute achieved performance.
- After an initial 500 s flight for 16 UEs and 100 s of UE movement without UAV measurement motion, the method maintains approximately 3-4 dB REM error by using the new UE paths. The introduction's 50-100x compute reduction remains an author-reported headline because the parse has no single end-to-end table supporting the full range.

## Limitations

The method depends on UE mobility or churn creating geometrically diverse rays. Static or sparse UEs can leave projection-matrix rank stagnant, and direct interpolation may then be cheaper. UE positions are assumed known, but localization error and its effect on RTI are not evaluated. Shared attenuation within each segment introduces undersegmentation and oversegmentation tradeoffs, while poor initial coverage can leave persistent reconstruction error.

Terrain attenuation is treated as stable; changing foliage or structures, moving blockers, interference, weather, and transmit-power calibration are not evaluated. The real testbed covers one 75 m x 75 m WiFi site, while the LTE study is trace-driven and the larger 5G studies are simulated. The rank value near 60 is setup-specific, and convex-hull area is only a proxy that can mis-trigger in irregular terrain.

The paper preserves two source-level inconsistencies. Its segmentation prose compares WATERSHED, U-Net, and FASTSAM, while Fig. 5's caption also names classical SLIC without explaining it elsewhere. The introduction calls the work the first use of RTI for ground-to-air optimization, the conclusion says "among the first," and reference [36] is the authors' 2024 SkyScale conference paper; the journal article is therefore best read as an expanded system and evaluation, not an unqualified first publication of the core idea.

## Relation to the corpus

This source complements [[information-driven-uav-spectrum-mapping]] and [[radio-map-aided-uav-path-planning]], but reconstructs persistent terrain attenuation rather than only a UE-specific radio map. Its update signal is related to [[uncertainty-triggered-radio-map-update]], with projection-rank saturation replacing uncertainty as the operational trigger.

## Raw artifacts

- Parse: `raw/sources/Scalable_Deployment_of_Aerial_Networks_via_Radio_Tomographic_Attenuation_Mapping/Scalable_Deployment_of_Aerial_Networks_via_Radio_Tomographic_Attenuation_Mapping.md`
- Origin PDF: `raw/sources/Scalable_Deployment_of_Aerial_Networks_via_Radio_Tomographic_Attenuation_Mapping/Scalable_Deployment_of_Aerial_Networks_via_Radio_Tomographic_Attenuation_Mapping.pdf`
- Figures: `raw/sources/Scalable_Deployment_of_Aerial_Networks_via_Radio_Tomographic_Attenuation_Mapping/images/`
