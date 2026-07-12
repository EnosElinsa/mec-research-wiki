---
type: concept
title: "Dynamic Feature Filtering for Visual SLAM"
tags: [uav, visual-slam, localization, dynamic-objects, computer-vision]
related:
  - "[[li-2026-dff-slam]]"
  - "[[edge-intelligence]]"
  - "[[autonomous-uav-swarms]]"
  - "[[rss-based-uav-localization]]"
  - "[[tony-q-s-quek]]"
created: 2026-07-12
updated: 2026-07-12
---

# Dynamic Feature Filtering for Visual SLAM

Dynamic feature filtering protects visual simultaneous localization and mapping from keypoints attached to moving people, vehicles, or objects. Those points violate the static-world geometry used to estimate camera motion, so leaving them in the pose solver can distort trajectory estimates and maps even when visual feature matching itself succeeds.

[[li-2026-dff-slam]] implements a two-pass filter on ORB-SLAM2. YOLOv3 first removes features inside person and vehicle boxes. Multiscale Lucas-Kanade optical flow then matches the remaining points, RANSAC estimates a fundamental matrix, and an epipolar-distance test removes residual motion that semantic detection missed. Static features alone feed pose estimation, loop closure, and mapping.

The semantic and geometric stages cover different failure modes. Semantic detection recognizes known movable classes but may miss objects or ignore unlisted classes; epipolar geometry can catch unrecognized motion but depends on a reliable fundamental-matrix estimate from enough well-distributed static correspondences. When a moving object dominates the image, both the feature count and fundamental-matrix estimate can fail.

For UAVs, embedded cost is part of the method rather than an afterthought. The DFF-SLAM platform test trades 25 FPS for 16 FPS on a Jetson Xavier NX while retaining the authors' real-time threshold. That is an [[edge-intelligence]] feasibility result; dataset trajectory accuracy and physical-flight runtime should not be conflated with field-validated localization accuracy.

This is visual self-localization, distinct from [[rss-based-uav-localization]], which uses a UAV's radio measurements to localize ground objects.
