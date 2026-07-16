---
type: source
title: "DFF-SLAM: Dynamic Feature Filtering-Based Simultaneous Localization and Mapping for UAV Positioning in IoT-Enabled Complex Environments"
authors: ["Jinglei Li", "Yiming Jia", "Meng Qin", "Qinghai Yang", "Tony Q. S. Quek", "Wen Gao", "Kyung Sup Kwak"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3600661"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: not_applicable
tags: [source, uav, visual-slam, localization, dynamic-objects, edge-intelligence, hardware-test]
related:
  - "[[dynamic-feature-filtering-vslam]]"
  - "[[edge-intelligence]]"
  - "[[autonomous-uav-swarms]]"
  - "[[rss-based-uav-localization]]"
  - "[[tony-q-s-quek]]"
created: 2026-07-12
updated: 2026-07-16
---

# DFF-SLAM: Dynamic Feature Filtering-Based Simultaneous Localization and Mapping for UAV Positioning in IoT-Enabled Complex Environments

## Citation

Li, J., Jia, Y., Qin, M., Yang, Q., Quek, T. Q. S., Gao, W., & Kwak, K. S. (2026). *DFF-SLAM: Dynamic Feature Filtering-Based Simultaneous Localization and Mapping for UAV Positioning in IoT-Enabled Complex Environments*. **IEEE Transactions on Mobile Computing**, 25(1), 550-565. DOI: 10.1109/TMC.2025.3600661.

## TL;DR

Extends ORB-SLAM2 for GPS-suppressed UAV flight by removing moving visual features in two passes: YOLOv3 filters prior-dynamic person/vehicle regions, then multiscale optical flow and epipolar geometry reject residual dynamic points. TUM RGB-D tests show large gains in high-dynamic scenes, and a Jetson Xavier NX flight-platform test sustains 16 FPS.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied visual SLAM positioning for UAV navigation in GPS-compromised IoT environments containing moving pedestrians and vehicles. They proposed DFF-SLAM, which first removes features inside YOLOv3 semantic detections, then tracks the remaining points through a multiscale optical-flow pyramid and rejects residual motion with epipolar geometry. On the high-dynamic TUM RGB-D `fr3_walking_xyz` sequence, DFF-SLAM reduced absolute-trajectory RMSE by 98.98% and relative-translation RMSE by 77.66% compared with the original SLAM system. An onboard Jetson Xavier NX experiment processed 16 frames per second, which the paper reports as meeting the real-time requirement for UAV positioning.

## Problem

Conventional V-SLAM assumes that most visual features belong to a static scene. Pedestrians and vehicles violate that assumption, so moving keypoints can corrupt pose estimation, loop closure, map construction, and UAV navigation. A useful onboard remedy must remove those points without exceeding the compute budget of a lightweight aerial platform.

## System and method

- A UAV-mounted depth camera supplies consecutive frames to an ORB-SLAM2 backend; no scalar optimization program is formulated.
- A YOLOv3 thread detects person and vehicle boxes and removes features in those prior-dynamic regions.
- Four-level Lucas-Kanade optical-flow pyramids match the remaining points across frames while handling scale and lighting changes.
- RANSAC estimates the fundamental matrix. Points whose epipolar distance exceeds the fixed `0.8` threshold are removed as dynamic; retained points drive motion estimation, loop closure, pose optimization, and mapping.
- The design selects ORB-SLAM2 and bounded pyramid depth to preserve real-time execution on embedded hardware.

## Key findings

- On TUM RGB-D `fr3_walking_xyz`, absolute-trajectory RMSE falls from `2.1054 m` to `0.0214 m` (`98.98%`), while standard deviation falls from `0.4087 m` to `0.0106 m` (`97.41%`).
- On low-dynamic `fr3_sitting_xyz`, absolute-trajectory RMSE falls from `0.0139 m` to `0.0117 m` (`15.83%`), showing a much smaller gain when few features move.
- On high-dynamic `fr3_walking_xyz`, relative-translation RMSE falls from `0.0685 m` to `0.0153 m` (`77.66%`).
- The AMOVLAB UAV test uses RealSense T265/D435i cameras, Pixhawk4, and Jetson Xavier NX. Compared with original ORB-SLAM2, DFF-SLAM raises GPU use from `14%` to `21%` and memory from `1.9 GB` to `2.8 GB`, while processing drops from 25 to 16 FPS; the authors treat 16 FPS as real time.

## Limitations / parse caveats

The physical-platform experiment demonstrates onboard filtering and runtime, but it provides no ground-truth ATE/RPE for the flight; quantitative accuracy comes from TUM RGB-D sequences. Semantic priors cover only people and vehicles, detector misses remain possible, and a scene dominated by one moving object can leave too few well-distributed static points for reliable geometry. Lighting and hardware compute remain explicit limitations. Several extracted table rows are internally inconsistent or shifted, so this page uses only cross-consistent rows and prose-supported values. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[dynamic-feature-filtering-vslam]] adds vision-based self-localization to the corpus's UAV positioning vocabulary. It differs from [[rss-based-uav-localization]], which estimates ground-object positions from radio measurements, and from adversarial localization under jamming. Its Jetson deployment is an [[edge-intelligence]] feasibility result, not a field-accuracy validation.

## Raw artifacts

- Parse: `raw/sources/DFF-SLAM_Dynamic_Feature_Filtering-Based_Simultaneous_Localization_and_Mapping_for_UAV_Positioning_in_IoT-Enabled_Complex_Environments/DFF-SLAM_Dynamic_Feature_Filtering-Based_Simultaneous_Localization_and_Mapping_for_UAV_Positioning_in_IoT-Enabled_Complex_Environments.md`
- Origin PDF: `raw/sources/DFF-SLAM_Dynamic_Feature_Filtering-Based_Simultaneous_Localization_and_Mapping_for_UAV_Positioning_in_IoT-Enabled_Complex_Environments/DFF-SLAM_Dynamic_Feature_Filtering-Based_Simultaneous_Localization_and_Mapping_for_UAV_Positioning_in_IoT-Enabled_Complex_Environments.pdf`
- Figures: `raw/sources/DFF-SLAM_Dynamic_Feature_Filtering-Based_Simultaneous_Localization_and_Mapping_for_UAV_Positioning_in_IoT-Enabled_Complex_Environments/images/`
