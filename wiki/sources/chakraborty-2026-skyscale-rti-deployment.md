---
type: source
title: "Scalable Deployment of Aerial Networks via Radio Tomographic Attenuation Mapping"
authors: ["Ayon Chakraborty", "Subrata Das", "Pranav Ramesh"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3656779"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 9707-9720"
tags: [source, aerial-network, radio-environment-map, radio-tomography, uav-placement, measurement-planning]
related:
  - "[[radio-tomographic-attenuation-mapping]]"
  - "[[rank-saturation-rem-updates]]"
  - "[[segment-coverage-uav-trajectory]]"
  - "[[information-driven-uav-spectrum-mapping]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[uncertainty-triggered-radio-map-update]]"
created: 2026-07-14
updated: 2026-07-14
---

# Scalable Deployment of Aerial Networks via Radio Tomographic Attenuation Mapping

## Citation

Chakraborty, A., Das, S., & Ramesh, P. (2026). *Scalable Deployment of Aerial Networks via Radio Tomographic Attenuation Mapping*. **IEEE Transactions on Mobile Computing, 25**(7), 9707-9720. DOI: 10.1109/TMC.2026.3656779.

## TL;DR

SKYSCALE reconstructs a terrain-dependent 3-D attenuation field from UE-UAV measurements, then reuses that field to synthesize radio environment maps for arbitrary UE locations. Depth-based segmentation reduces the inverse problem to segment coefficients, a coverage-oriented trajectory gathers informative rays, and estimated-rank growth controls incremental updates. The benefit is strongest under UE mobility or churn; static deployments can favor direct interpolation.

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
