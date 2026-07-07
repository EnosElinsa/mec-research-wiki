# Better Together: Leveraging Multiple Digital Twins for Deployment Optimization of Airborne Base Stations

Mauro Belgiovine , Chris Dick , Senior Member, IEEE, and Kaushik Chowdhury , Fellow, IEEE

Abstract—Airborne Base Stations (ABSs) allow for flexible geographical allocation of network resources with dynamically changing load as well as rapid deployment of alternate connectivity solutions during natural disasters. Since the radio infrastructure is carried by unmanned aerial vehicles (UAVs) with limited flight time, it is important to establish the best location for the ABS without exhaustive field trials. This paper proposes a digital twin (DT)-guided approach to achieve this goal through the following key contributions: (i) Implementation of an interactive software bridge between two open-source DTs such that the same scene is evaluated with high fidelity across NVIDIA’s Sionna and Aerial Omniverse Digital Twin (AODT), highlighting the unique features of each of these platforms for this allocation problem, (ii) Design of a back-propagation-based algorithm in Sionna for rapidly converging on the physical location of the UAVs, orientation of the antennas and transmit power to ensure efficient coverage across the swarm of the UAVs, and (iii) numerical evaluation in AODT for large network scenarios (50 UEs, 10 ABS) that identifies the environmental conditions in which there is agreement or divergence of performance results between these twins. Finally, (iv) we propose a resilience mechanism to provide consistent coverage to missioncritical devices and demonstrate a use case for bi-directional flow of information between the two DTs.

Index Terms—Digital twin, ray tracing, optimization, unmanned aerial vehicle (UAV), airborne base stations, network planning.

## I. INTRODUCTION

tions, or Airborne Base Stations (ABSs), have gained significant attention as a complement to ground-based cellular networks [1]. As UAVs become more accessible, their ability to navigate 3-dimensional (3D) space provides flexibility in adapting to dynamic network demands [2], [3], enabling lineof-sight links to mission-critical units [4] and enhancing user tracking [5]. However, ABS-enabled connectivity introduces challenges such as collision avoidance, coordinated coverage, and optimal placement, considering limited flight times of 20 to 100 minutes [6]. These challenges are highly dependent on the

![](images/5856df80c7a341becc4dffbfb34f7fae1de37d8ed477e61d99ab37e73cf803b0.jpg)  
Fig. 1. Overview of proposed optimization and validation framework for Airborne Base Stations (ABSs) deployment using Multiple Digital Twins.

RF propagation environment, making prior channel knowledge essential for effective network planning.

• Motivation for Digital Twins: Optimal placement of Base Stations (BSs) is traditionally handled by telecom operators relying on domain knowledge and best practices. Various factors, including geography, network performance, and costs, influence these decisions. Digital Twins (DTs) and, specifically, Digital Twins for Networking (DTNs) [7], have emerged as strategic tools for network simulation, performance analysis, and “whatif” scenarios. DTNs aid in planning, performance tuning, and machine learning-driven traffic modeling. In wireless networks, they also enable accurate propagation modeling, antenna design, and multi-antenna configurations, playing a key role in developing 6G systems and beyond.

• Challenges in Using Digital Twins: Despite advancements in DTN tools, no single solution can comprehensively simulate complex wireless networks. Engineering such systems requires expertise in signal processing, propagation modeling, and software architectures. DTs offer varying capabilities, from network optimization to large-scale physical simulations. Integrating multiple DTs can enhance planning but introduces challenges such as 3D site model sharing, node placement consistency, and coherent interpretation of simulation results across different solvers.

• Contributions of the Paper: This work presents a Multiple-Digital Twin (Multi-DT) system for autonomous ABS deployment in city-scale environments. We integrate NVIDIA’s Sionna and Aerial Omniverse Digital Twin (AODT) to: (i) use Sionna’s differentiable simulation to optimize ABS trajectories and orientations, (ii) validate deployments with AODT-generated largescale simulation data, (iii) leverage AODT data to enhance ABS resilience for mission-critical coverage, and (iv) bridge interoperability gaps between DTs to enable cooperative functionalities. This framework demonstrates the advantages of Multi-DTs for complex wireless tasks and promotes their adoption in research. Proposed implementation overview is shown in Fig. 2.

![](images/e085c93b62e0d18262f9773b06381fe03e15bdf2652c3aab0f0ae5a576db7e80.jpg)  
Fig. 2. Multi-DT framework showing task separation: Sionna (left) performs gradient-based optimization, AODT (right) handles validation and mobility simulation, and the Shared Data Layer enables bidirectional communication through standardized data exchange (3D models, ABS configurations, User Equipment (UE) trajectories and simulation results). Arrows demonstrate the synergistic information flow between platforms at each computation step.

## II. RELATED WORK

ABS deployments have been explored for various applications [8], [9], including enhancing network capacity in dense areas [2], supporting vehicular networks [10], and aiding disaster-affected regions [11]. Autonomous ABS deployment is crucial in hazardous or inaccessible environments: Reinforcement Learning (RL)-based approaches have been proposed for ABS deployment in coverage-limited areas, optimizing position and orientation for backhaul connectivity [12], [13]. These models do not account for physical obstacles, limiting real-world applicability. Moreover, while RL approaches can be effective when ABSs have limited environmental data, they require extensive sensing and data generation for training. In contrast, our approach leverages complete environmental knowledge through Digital Twins, enabling direct gradient-based optimization without the computational overhead of exploration and learning phases required by RL methods. Some studies incorporate obstacles for UAV route planning in sensor data collection [14] and coverage optimization [15], but focus on single UAV operation or single target areas. While RL is useful when ABSs have access to limited environmental data, it demands extensive sensing and large-scale data generation for effective training. Furthermore, these works rely on stochastic channel models rather than precise RF propagation modeling. Recently, [16] proposed a placement approach based on radio propagation maps and discretized 3D locations, but it doesn’t consider navigation or interference caused by multiple UAVs deployment.

DTNs have gained interest as high-fidelity replicas of realworld networks scenarios [7], [17], [18], facilitating testing of UAV placements and communication technologies. Some studies explore DT-supported UAV resource allocation [19] and network reconstruction [20], but comprehensive, license-free DTNs integrating accurate wireless propagation, client mobility, and system-level RAN control remain underdeveloped. Table I summarizes the features of proposed approach compared to related works presented in this section.

## III. BRIDGING SIONNA AND AODT: A UNIFIED DIGITAL TWIN FRAMEWORK

The concept of using multiple DTs concurrently for a shared objective is still emerging [21]. This work focuses on DTNs with Ray Tracing [22] rather than statistical channel modeling, as they allow realistic multi-path propagation simulation in detailed 3D urban environments. We utilize two NVIDIA’s DTNs: Sionna<sup>1</sup> [23] and Aerial Omniverse Digital Twin (AODT)<sup>2</sup> [24]. Sionna and AODT represent a new class of AI-native, high-fidelity wireless simulation tools that go beyond the capabilities of traditional network simulators like NS-3 [25] and OMNeT++ [26], or EM tools like Remcom Wireless InSite [27] and ANSYS HFSS [28]. While traditional simulators focus on protocol-level abstraction or detailed electromagnetic modeling in static environments, Sionna and AODT integrate differentiable physical-layer models, photorealistic 3D environments, and efficient Ray Tracing simulation to support AI-driven design and optimization of 5G and 6G networks. This makes them uniquely suited for creating dynamic, end-to-end digital twins of urban wireless systems—enabling realistic channel modeling, beamforming, and users’ mobility-aware optimization within a fully interactive environment. For researchers and engineers developing next-generation wireless technologies with AI at the core, Sionna and AODT offer a future-ready platform that bridges the gap between high-level network design, and lowlevel physical realities in a scalable, GPU-accelerated workflow. This section summarizes their key features and highlights their design differences.

• Sionna Ray Tracing (RT): Sionna RT is part of NVIDIA’s Sionna [29] link-level simulation library. Its key feature is differentiability in RF simulation blocks, including statistical models and Ray Tracing, enabling direct optimization of network parameters and antenna orientation based on EM propagation effects. It leverages TensorFlow [30] for automatic differentiation and scalable gradient-based optimization.

TABLE I  
FEATURE COMPARISON OF EXISTING ABS-RELATED APPROACHES VERSUS OURS. PROPOSED MULTI-DT APPROACH PROVIDES UNIQUE CAPABILITIES INCLUDING CONTINUOUS-SPACE OPTIMIZATION, COMPREHENSIVE OBSTACLE HANDLING, AND DIFFERENTIABLE RF PROPAGATION MODELING THAT ENABLE SUPERIOR PERFORMANCE COMPARED TO LEARNING-BASED ALTERNATIVES THAT LACK COMPLETE ENVIRONMENTAL INFORMATION. NOTE THAT [20] OUTLINES A DT-BASED COORDINATION FRAMEWORK, BUT DOES NOT PROPOSE ANY EXPLICIT AUTONOMOUS UAV DEPLOYMENT SOLUTION.
<table><tr><td>Autonomous ABS Feature / Capability</td><td>RL-based ABS deployment (e.g. [12], [13])</td><td>Obstacle-aware UAV route / coverage (e.g. [14], [15])</td><td>Radio-map-based placement [16]</td><td>DT-supported UAV deployment (e.g. [19], [20])</td><td>Proposed approach</td></tr><tr><td>Learning/optimization based</td><td>√</td><td>√</td><td>√</td><td>V</td><td>√</td></tr><tr><td>Continuous-space UAV locations</td><td>x</td><td>√</td><td>x</td><td> $\pmb { \chi } ^ { \mathrm { [ 1 9 ] } } \check { \sqrt { 2 0 } }$ </td><td>√</td></tr><tr><td>Handles physical obstacles</td><td>x</td><td>√</td><td>√</td><td>x</td><td>√</td></tr><tr><td>Multi-UAV</td><td>x</td><td> $\pmb { x } ^ { [ 1 4 ] } \checkmark ^ { [ 1 5 ] }$ </td><td>√</td><td>√</td><td>√</td></tr><tr><td>Multi-target-area coordination</td><td>x</td><td> $\checkmark ^ { [ 1 4 ] } \times \AA ^ { [ 1 5 ] }$ </td><td>√</td><td>√</td><td>√</td></tr><tr><td>Ray Tracing RF propagation modeling</td><td>x</td><td>x</td><td>√</td><td>x</td><td>√</td></tr><tr><td>Navigation / dynamic repositioning</td><td> $\pmb { x } ^ { [ 1 2 ] } \checkmark ^ { [ 1 3 ] }$ </td><td>√</td><td>x</td><td> $\pmb { \chi } ^ { \mathrm { [ 1 9 ] } } \check { \sqrt { 2 0 } }$ </td><td>√</td></tr><tr><td>Interference management among multiple UAVs</td><td>x</td><td>x</td><td>x</td><td>√</td><td>√</td></tr><tr><td>High-fidelity digital-twin network (DTN)</td><td>x</td><td>x x</td><td>x x</td><td>√  $\pmb { \chi } ^ { \mathrm { [ 1 9 ] } } \check { \checkmark } ^ { [ 2 0 ] }$ </td><td>√</td></tr><tr><td>Integrates clients mobility</td><td>x</td><td>x</td><td>x</td><td></td><td>√</td></tr><tr><td>Allows system-level RAN simulation</td><td>x</td><td></td><td>√</td><td>x</td><td>√</td></tr><tr><td>Free to use / open-source framework</td><td>x</td><td>x</td><td></td><td>x</td><td>√</td></tr></table>

![](images/8e5097295cd0688ea0860f177c952859892a41d37dd56564f3a5664f68da3128.jpg)  
(a)

![](images/065351d85732989bd61cc451629d2f25eb86976f0e5b14319d930850756bb51e.jpg)  
(b)  
Fig. 3. The same Tokyo 3D map from high-detail PLATEAU dataset loaded in Sionna and AODT, used to demonstrate the proposed approaches for Multi-DT framework. (a) shows a path gain Coverage Map computed with Sionna and (b) presents a simulation frame from AODT multi-UE simulation in the same map location.

The Ray Tracing module utilizes the Mitsuba3 differentiable renderer [31], built on Dr.Jit [32], for efficient gradient computation. Fig. 3(a) illustrates a Coverage Map generated with Sionna.

• Aerial Omniverse Digital Twin (AODT): AODT, part of NVIDIA’s Omniverse DT ecosystem, supports EM propagation and system-level simulations. It enables realistic network deployment, leveraging NVIDIA Aerial CUDA Accelerated RAN [33] for full GPU acceleration of 5G L1/L2 layers. Its high-performance Ray Tracing engine, written in C++/CUDA, outperforms Sionna’s Python-based implementation while maintaining functionally identical EM propagation effects. Though non-differentiable, AODT supports rapid multi-User Equipment (UE) simulation data generation for offline analysis and ML/DL model training. This work focuses on AODT’s L1 EM simulation, leaving L2 integration for future studies. Fig. 3(b) shows an EM simulation in AODT.

• DTNs Choice Motivation: Our motivation for combining these specific DTNs is as follows: (i) Sionna outperforms commercial competitors [34], while AODT supports multi-UE mobility, diverse antenna configurations, and efficient Ray Tracing; (ii) As shown in Table II, they offer distinct functionalities, such as differentiable tensor blocks in Sionna and system-level simulation in AODT; (iii) Both are freely available. While Sionna provides a differentiable Ray Tracer for gradient-descent optimization in multi-path propagation models, AODT supports large-scale simulations with higher Ray Tracing sampling and mobility features. As telecom operators explore next-generation networks, these DTNs offer complementary capabilities for innovative solutions. Integrating their outputs enables tackling complex challenges.

## IV. CHALLENGES IN COMBINING DIGITAL TWINS

Integrating multiple DTNs presents several challenges due to their lack of built-in interoperability. While this work focuses on Sionna and AODT, these challenges apply broadly to other DTN combinations:

\- Sharing 3D Urban Models: Despite having similar Ray Tracing capabilities, Sionna and AODT use different scene

## TABLE II

SIMULATION FEATURES AND EM PROPAGATION EFFECTS CAPABILITIES OF AERIAL OMNIVERSE DIGITAL TWIN (AODT) AND SIONNA. †= SET BY USER (W/ GPU MEMORY CONSTRAINTS); §= SET BY USER (SHARED BY ALL RUS/UES IN THE SIMULATION); ∗ = FOR ANY INTERACTION OF THE RAY ALONG ITS PATH; ∗∗ = ONLY FOR LOS WEDGE INTERACTION WITH TRANSMITTER. NOTE: SIONNA QUANTITIES SPECIFICALLY RELATE TO ITS COVERAGE MAP FUNCTION.

<table><tr><td rowspan=1 colspan=1>Feature</td><td rowspan=1 colspan=1>AODT 1.1.1</td><td rowspan=1 colspan=1>Sionna 0.19</td></tr><tr><td rowspan=1 colspan=1>Simulation target</td><td rowspan=1 colspan=1>System-level</td><td rowspan=1 colspan=1>Link-level</td></tr><tr><td rowspan=1 colspan=1>3D geometry format</td><td rowspan=1 colspan=1>OpenUSD</td><td rowspan=1 colspan=1>Mitsuba</td></tr><tr><td rowspan=1 colspan=1>PHY (L1) simulation</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>MAC (L2) simulation</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>=</td></tr><tr><td rowspan=1 colspan=1>5G waveform compliant</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>Multi-device (BS/UE) simulation</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>UE mobility engine</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>–</td></tr><tr><td rowspan=1 colspan=1>Coverage Maps</td><td rowspan=1 colspan=1>I</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>Differentiable</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>Ray Tracing simulation engine</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>- Reflection</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>- Scattering / Diffusion</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>- Diffraction</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>- Surface material properties (ITU)</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>- Customizable antenna panels</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>Simulation Param. (max value)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Num. of rays emitted at every RU</td><td rowspan=1 colspan=1>1,000,000</td><td rowspan=1 colspan=1>†</td></tr><tr><td rowspan=1 colspan=1>Num. of reflection/diffusion events</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>†</td></tr><tr><td rowspan=1 colspan=1>Num. of diffraction events</td><td rowspan=1 colspan=1>1 × path*</td><td rowspan=1 colspan=1>1 × path**</td></tr><tr><td rowspan=1 colspan=1>Num. of UE</td><td rowspan=1 colspan=1>10,000</td><td rowspan=1 colspan=1>†</td></tr><tr><td rowspan=1 colspan=1>Num.of antenna elements per RU</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>§</td></tr><tr><td rowspan=1 colspan=1>Num. of antenna elements per UE</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>§</td></tr></table>

descriptors (Mitsuba3 vs. OpenUSD). Although both support OpenStreetMap imports, high-resolution custom models require manual conversion.

Wireless Device Deployment Exchange: AODT lacks procedural import/export functions for radio and user equipment placement, relying on manual GUI configuration. To bridge this gap, modifications were made to enable JSON-based deployment imports from Sionna and automate UE placement for specific areas in AODT.

\- Ray Tracing Variability: Differences in stochastic Ray Tracing implementations, unit systems, and antenna models make direct comparison difficult. Parameter adjustments are necessary to align simulation outputs.

\- Different Simulation Features: AODT supports only fixed ground stations, limiting ABS deployment studies. To overcome this, a custom BS mobility system was implemented, allowing pre-computed ABS trajectories during simulations.

Such challenges highlight the need for tailored solutions when integrating multiple DTNs for wireless network simulations and the main roadblocks addressed by our Multi-DT implementation.

## A. Shared Data Layer Components and Functions

In order to address these challenges, we have implemented a dedicated Shared Data Layer that allows exchange of 3D models and deployment configurations and to easily validate complex wireless deployments via proposed Multi-DT platform. The Shared Data Layer architecture provides several critical advantages, which are rooted in the following design principles:

1) Platform Independence: Each DT operates in its native environment while sharing standardized data representations;

2) Standardized Interoperability: JSON-based protocols can accommodate different numbers of ABSs, AOIs, and UE configurations;

3) Multi-DT Deployment Adaptation: Bidirectional communication enables dynamic scenario updates based on performance feedback from each DT;

4) Validation Integrity: Cross-platform consistency checks ensure optimization results translate effectively between environments;

5) Extensibility: Modular design allows integration of additional DT platforms and applications with minimal architectural changes.

The Shared Data Layer implements a multi-faceted approach to handle the fundamental incompatibilities between Sionna and AODT platforms. It consists of four main functional components:

1) 3D Scene Data Harmonization: Sionna uses Mitsuba3 scene descriptors while AODT employs OpenUSD format, creating incompatibility for high-resolution 3D urban models. This component includes:

\- Custom Blender Script: Automated conversion pipeline that reads OpenUSD scenes from AODT and exports Mitsuba3-compatible formats for Sionna;

\- Geometry Preservation: Ensures building coordinates, surface materials properties, and structural details remain consistent across both platforms;

\- Coordinate System Alignment: Maintains spatial consistency for Tokyo PLATEAU dataset across both environments by addressing possible unit measure differences (e.g., metric vs. imperial system) and coordinate system conventions (e.g. Global vs. Local, Right-handed vs. Left-handed Coordinate Systems).

2) Device Deployment Configuration Exchange: AODT lacks procedural import/export functions for radio equipment placement, relying on manual GUI configuration. Standardized data structures have been defined to exchange the following information via a JSON-based protocol:

\- AOIs Parameters: Center coordinates $( z _ { k } , w _ { k } )$ and radius $r _ { k }$ for each k-th AOI;

\- ABSs Parameters: Coordinates $( x _ { i } , y _ { i } )$ , orientations $( \phi _ { i } , \theta _ { i } )$ , and transmission powers $P _ { i } ^ { t x }$ for each i-th ABS;

\- ABSs Trajectories: A list of $( x _ { i } , y _ { i } )$ coordinates for each i-th ABS at a given simulation time-step;

\- UEs Trajectories: A list of coordinates $( x _ { u } , y _ { u } )$ for each u-th UE simulated in experiments with mobile terminals.

3) Simulation Parameter Synchronization: Different ray tracing implementations, unit systems, and antenna models make direct comparison difficult. Hence, several parameters need to be consistently tracked across Multi-DT platforms:

TABLE III  
COMPLETE PARAMETER REFERENCE FOR ABS DEPLOYMENT OPTIMIZATION FRAMEWORK. ∗ = MAP-DEPENDENT.
<table><tr><td>Parameter</td><td>Description</td><td>Equation / Section</td><td>Value</td></tr><tr><td colspan="4">Loss Function Components</td></tr><tr><td>Lp</td><td>Total loss function to minimize</td><td>(1)</td><td></td></tr><tr><td>α</td><td>Scaling factor for coverage term</td><td>(1)</td><td>0.01</td></tr><tr><td>β</td><td>Scaling factor for attraction penalty</td><td>(1)</td><td>1.0</td></tr><tr><td>γ</td><td>Scaling factor for repulsion penalty</td><td>(1)</td><td>0.8</td></tr><tr><td></td><td>Scaling factor for collision penalty</td><td>(1)</td><td>1.0</td></tr><tr><td>ηK</td><td>Coverage factor for spatial distribution</td><td>(2)</td><td></td></tr><tr><td>Pu</td><td>Repulsion penalty between ABSs</td><td>(3)</td><td></td></tr><tr><td>Pa</td><td>Attraction penalty toward AOIs</td><td>(4)</td><td></td></tr><tr><td> $P _ { b }$ </td><td>Collision avoidance penalty</td><td>(6)</td><td></td></tr><tr><td colspan="4">Spatial and Geometric Parameters</td></tr><tr><td>N</td><td>Total number of ABSs</td><td>(2,3)</td><td>10</td></tr><tr><td>M</td><td>Total number of Areas of Interest (AOIs)</td><td>(4)</td><td>5</td></tr><tr><td>pi</td><td>Position coordinates (xi, yi) of i-th ABS</td><td>(2,3)</td><td></td></tr><tr><td>Ck</td><td>Center coordinates (zk, wk) of k-th AOI</td><td>(4)</td><td>Table IV</td></tr><tr><td></td><td>Radius of k-th AOI</td><td>(4)</td><td>250-300m</td></tr><tr><td>τc</td><td>Set of evenly spaced 2D grid coordinates</td><td>(2)</td><td> $5 \times 5 ~ \mathrm { g r i d }$ </td></tr><tr><td> $g$ </td><td>Individual grid point coordinate</td><td>(2)</td><td></td></tr><tr><td> $m _ { e }$ </td><td>Margin distance from map edges</td><td>(2)</td><td>150m</td></tr><tr><td> $\underline { { d _ { m i n } } }$ </td><td>Minimum distance between ABSs</td><td>(3)</td><td>400m</td></tr><tr><td colspan="4">Building and Collision Parameters</td></tr><tr><td> $\overline { { B } }$ </td><td>Number of buildings in the map</td><td>(6)</td><td></td></tr><tr><td></td><td></td><td>V-A</td><td>70m</td></tr><tr><td>h</td><td>ABSs&#x27; elevation</td><td></td><td>15m</td></tr><tr><td> $c _ { b }$ </td><td>Minimum allowed distance from buildings</td><td>(6)</td><td></td></tr><tr><td> $d _ { i b }$ </td><td>Distance from ABS i to building b</td><td>(6,7)</td><td></td></tr><tr><td> $\left( p _ { x } , p _ { y } \right) _ { , }$ </td><td>ABS XY coordinates</td><td>(7)</td><td></td></tr><tr><td> $( \overbrace { m } _ { x } , \overbrace { m _ { y } } )$   $( M _ { x } , M _ { y } )$ </td><td>Min. XY coords. of building bounding box Max. XY coords. of building bounding box</td><td>(7) (7)</td><td></td></tr><tr><td> $\underline { { d _ { x } , d _ { y } } }$ </td><td>X,Y components of distance to building</td><td>(7)</td><td></td></tr><tr><td colspan="4">Steepness and Weight Parameters</td></tr><tr><td>Ka</td><td>Steepness factor for attraction exponential</td><td>(4)</td><td>0.02</td></tr><tr><td></td><td>Steepness factor for collision penalty</td><td>(6)</td><td>0.5</td></tr><tr><td> $\kappa _ { b }$  Ki</td><td>Steepness factor for sigmoid function</td><td>(5)</td><td>0.25</td></tr><tr><td> $\omega _ { k }$ </td><td>Weight factor for k-th AOI</td><td>(4,5)</td><td></td></tr><tr><td> $\sigma ( \boldsymbol { z } , t , \kappa )$ </td><td>Modified sigmoid: 1+e−κ(z−t) 1</td><td>(5)</td><td></td></tr><tr><td colspan="4"></td></tr><tr><td> $\overline { { C } }$ </td><td>Coverage Map and Ray Tracing  $\frac { \bullet } { \mathbb { R } ^ { N \times C _ { x } \times C _ { y } ^ { - } } }$ </td><td>(8)</td><td></td></tr><tr><td> $\begin{array} { r } { C _ { i , x , y } } \end{array} .$ </td><td>Coverage map tensor</td><td>(8)</td><td></td></tr><tr><td> $\hat { g } ( i , x , y )$ </td><td>Coverage map cell for ABS i at (x, y)</td><td>(8)</td><td></td></tr><tr><td> $N _ { R }$ </td><td>Estimated path gain for ABS i at cell (x, y) Number of valid rays hitting cell (x, y)</td><td>(8)</td><td></td></tr><tr><td> $N _ { C } ^ { \arg }$ </td><td>Total coverage map cells:  $\hat { C } _ { x } \cdot \boldsymbol { C } _ { y }$ </td><td>(8)</td><td></td></tr><tr><td> $| h ( s ( \bar { \psi _ { n } } ) ) | ^ { 2 }$ </td><td>Squared amplitude of path coefficients</td><td>(8)</td><td></td></tr><tr><td> $r ( \psi _ { n } )$ </td><td>Length of n-th path with direction ψn</td><td>(8)</td><td></td></tr><tr><td> $\alpha ( \psi _ { n } )$ </td><td>Angle between map normal and arrival direction</td><td>(8)</td><td></td></tr><tr><td> $\underline { { s ( \psi _ { n } ) } }$ </td><td>Intersection point of n-th path with map</td><td>(8)</td><td></td></tr><tr><td colspan="4"></td></tr><tr><td>ptx  $R S \mathring { S } _ { i , x , y }$ </td><td>Signal Strength and Interference Initial transmission power of i-th ABS (dBm)</td><td>(8,9)</td><td>43.0 dBm</td></tr><tr><td></td><td>Received Signal Strength at cell (x, y)</td><td></td><td></td></tr><tr><td> $R _ { i , x , y }$ </td><td>Signal-to-Interference Ratio at cell (x, y)</td><td>(9)</td><td></td></tr><tr><td>€</td><td>Noise floor (fixed)</td><td>(9)</td><td> $1 \times 1 0 ^ { - 2 0 }$ </td></tr><tr><td>Mi,x,y</td><td>Coverage mask for ABS i at cell (x, y)</td><td>(10)</td><td>0 or 1</td></tr><tr><td> $\hat { r } _ { i } ^ { \phantom { \dagger } }$ </td><td>Effective average SIR for i-th ABS (dB)</td><td>(11)</td><td></td></tr><tr><td colspan="4">Optimization Loss Functions</td></tr><tr><td>Lsmoothmin</td><td>Smooth minimum approximation loss</td><td>(12)</td><td></td></tr><tr><td> $\mathcal { L } _ { a v g S I R }$ </td><td>Average SIR maximization loss</td><td>(14)</td><td></td></tr><tr><td>Lo</td><td>Total orientation optimization loss</td><td>(15)</td><td></td></tr><tr><td> $\mathcal { L } _ { u }$ </td><td>Unweighted AOI ŚIR optimization loss</td><td>(18)</td><td></td></tr><tr><td> ${ \mathcal { L } } _ { w }$ </td><td>Weighted AOI SIR optimization loss</td><td>(19)</td><td></td></tr><tr><td> $N L S E ( r , \beta _ { L } )$ </td><td>Negative Log-Sum-Exp function</td><td>(13)</td><td></td></tr><tr><td> $\underline { { L S E ( r _ { m } ^ { * } , \beta _ { L } ) } }$ </td><td>Log-Sum-Exp for m-th AOI</td><td>(17)</td><td></td></tr><tr><td colspan="4">Algorithm and Optimization Parameters</td></tr><tr><td> $\overline { { \beta _ { L } } }$ </td><td>Temperature for NLSE/LSE functions</td><td>(12,13)</td><td>1.0</td></tr><tr><td>us</td><td>Scaling factor for average SIR term</td><td>(15)</td><td>0.25</td></tr><tr><td> $w _ { m }$ </td><td>Softmin weight for m-th AOI</td><td>(20)</td><td></td></tr><tr><td> $_ T$ </td><td>Temperature parameter for softmin</td><td>(20)</td><td>25</td></tr><tr><td></td><td>Mechanical azimuth of i-th ABS (degrees)</td><td>V-B</td><td></td></tr><tr><td>φi  $\dot { \theta } _ { i }$ </td><td>Mechanical tilt of i-th ABS (degrees)</td><td>V-B</td><td>[−2π,2π] [π/7,6π/7]</td></tr></table>

\- RF Parameter Alignment: Center frequency $( f _ { c } = 3 . 5$ GHz), sampling frequency and antenna patterns (TR 38.901 for ABS, half-wave dipole for UE);

\- Ray Tracing Harmonization: Consistent material properties, types of ray interactions (e.g., specular reflections, diffusion, diffraction) and number of interactions limit per Ray;

\- Power Scale Matching: Transmission power normalization (43.0 dBm baseline) and SIR computation standardization;

Fig. 2 depicts the flow of data exchanged between the chosen DTs via implemented Shared Data Layer. Table III provides a comprehensive list of all simulation parameters and notation used throughout this work.

## V. GRADIENT-BASED ABSS DEPLOYMENT OPTIMIZATION

This section presents a case study using the proposed Multi-DT framework to develop an autonomous ABS deployment algorithm for enhancing network capacity or restoring coverage in disaster-affected areas. The key requirements for this algorithm are as follows:

\- ABSs need to be deployed rapidly and autonomously;

\- These deployments are temporary and adaptive, with possibility of quick change of objectives and targets;

\- The deployment algorithm has to be general enough to adapt to different urban scenarios and be aware of obstacles in 3D space during navigation;

\- The deployment algorithm has to be aware of wireless propagation properties of the environment to avoid incurring in undesirable interference once hovering locations are identified.

By exploiting the rich information available within the DTs, we employ gradient-based optimization to first generate ABS navigation routes from random initial positions, targetingxbrk multiple coverage areas, and then optimize orientation and transmission power to minimize interference, using Sionna’s differentiable Ray Tracer. This approach enables a flexible method that can easily be adapted to different urban scenarios and coverage requirements, without the costly data generation and training required for learning-based methods. To validate our approach, we use Tokyo’s high-resolution 3D map from PLATEAU [35] dataset provided by AODT. The geometry is converted from OpenUSD to Mitsuba3 format for compatibility with Sionna, where the optimization is implemented via TensorFlow.

## A. Location Optimization

We assume ABSs hover at a fixed elevation of h m, which is considered a hyper-parameter, and we focus on optimizing ABSs’ locations only in the XY-plane. This elevation was selected to ensure ABSs operate above most urban obstacles in the targeted map while maintaining practical deployment constraints. The deployment optimization aims to find optimal locations $( x _ { i } , y _ { i } )$ for N ABSs to cover M Areas of Interest (AOIs), each defined by $( z _ { m } , w _ { m } )$ and radius $r _ { m }$ . Initially, <sup>( )</sup>ABSs are placed semi-randomly,<sup>3</sup> as they may be deployed from aerial vehicles, storage hubs, or accessible zones near disaster-affected areas. Optimal paths are computed to navigate from initial positions to target locations while avoiding obstacles and collisions. No limit is imposed on the number of ABSs per AOI, allowing flexibility in coverage. Once AOIs are served, remaining ABSs redistribute in their surroundings to enhance coverage or act as relays. Simultaneously computing optimal routes and locations requires tight coordination among ABSs. To achieve this, we model location optimization using a Particle Swarm Optimization-inspired gradient-descent approach [36]. By embedding ABS interactions with the environment into the loss function, the algorithm directly samples navigation waypoints, guiding ABSs through the optimization landscape.

Specifically, we define our loss function to be minimized as a composition of multiple loss terms summed together, with each individual loss addressing one of our optimization criteria. The devised ABS deployment optimization function is determined as follows:

$$
\mathcal { L } _ { p } = - \alpha K + \beta P _ { a } + \gamma P _ { u } + \eta P _ { b }\tag{1}
$$

where $K$ corresponds to a coverage factor, $P _ { u }$ is the repulsion penalty, $P _ { a }$ is the attraction penalty and $P _ { b }$ is a collision avoidance penalty. $\alpha , ~ \beta , ~ \gamma$ and η correspond to scaling factors for each of the loss terms and are considered as hyper-parameters.

K and $P _ { u }$ together encourage even distribution of particles across maps. Specifically, K is defined as follows:

$$
K = \sum _ { g \in { \pmb G } } \operatorname* { m i n } _ { 1 \le i \le N } \| { \pmb g } - { \pmb p } _ { i } \|\tag{2}
$$

and $P _ { u }$ is defined as:

$$
P _ { u } = \sum _ { j } ^ { N } \sum _ { i } ^ { N } \operatorname* { m a x } \left( 0 , d _ { \operatorname* { m i n } } - \left\| p _ { i } - p _ { j } \right\| \right)\tag{3}
$$

where G is a set of g evenly spaced 2D grid coordinates across the XY-plane of the 3D map and $p _ { i } = ( x _ { i } , y _ { i } )$ is the coordinates of the i-th ABS. The coordinates and size of the grid points is computed by taking in input the number of reference points along the X and Y-axis and evenly distributing them across the map, leaving a margin of $m _ { e }$ meters from the edges of the ground plane. These two terms together aims to maximize the sum of minimum distances from each grid points to all ABSs location while keeping the distance among each ABS at a minimum of $d _ { \mathrm { m i n } }$ , which is also considered a hyper-parameter.

The attraction penalty $P _ { a }$ aims to pull ABSs in the map towards AOIs and is defined as follows:

$$
\begin{array} { l } { \displaystyle P _ { a } = \sum _ { k = 1 } ^ { M } \sum _ { i = 1 } ^ { N } \left[ \omega _ { k } \cdot \| p _ { i } - \pmb { c } _ { k } \| - ( 1 - \omega _ { k } ) \right. } \\ { \displaystyle \left. \cdot \exp \left( - \kappa _ { a } \cdot \| p _ { i } - \pmb { c } _ { k } \| - r _ { k } \right) \right] } \end{array}\tag{4}
$$

where $c _ { k }$ and $r _ { k }$ corresponds to the center coordinates and radius values of the k-th $\mathrm { A O I } , \kappa _ { a }$ is a hyper-parameter steepness factor for the exponential function and

$$
\omega _ { k } = \exp \left[ - \sum _ { i = 1 } ^ { N } \sigma \left( \left\| p _ { i } - \pmb { c } _ { k } \right\| , \frac { 2 r _ { k } } { 3 } , - \kappa _ { i } \right) \right]\tag{5}
$$

is a weight factor that decreases as more ABSs end up within a given AOI. To avoid harsh discontinuity in the loss function, we use $\begin{array} { r } { \sigma ( z , t , \kappa ) = \frac { 1 } { 1 + e ^ { - \kappa ( z - t ) } } } \end{array}$ as a modified sigmoid function to smoothly approximate the condition $\begin{array} { r } { \| p _ { i } - c _ { k } \| < \frac { 2 r _ { k } } { 3 } } \end{array}$ and $\kappa _ { i }$ is a steepness factor. The idea is that, for each AOI, all ABSs are linearly attracted by it and as soon as one or more ABS are within $2 / 3$ of the AOI radius, the attraction switches to exponential to increase the pull of those ABSs toward the center of the AOI, while all the other particles pulls will be “switched off” for that particular AOI.

![](images/24308c8a81399c54f54211c57bb1db527fa72e53b54cf6a5aeaced3d682605fb.jpg)  
Fig. 4. Visualization of loss function terms $\gamma P _ { a }$ + $\eta P _ { b }$ projected over the 2D ground-plane of a 3D map of Tokyo for a sample AOI (delimited by the yellow circle) and considering ABSs’ elevation of $h \stackrel { = } { = } 7 0 \mathrm { m }$ . In this visualization, only one ABS is considered and loss values are clipped in the range [0,2000].

Finally, the collision avoidance penalty $P _ { b }$ is defined as follows:

$$
P _ { b } = \sum _ { i } ^ { N } \sum _ { b } ^ { B } \exp \left( \kappa _ { b } \cdot ( - d _ { i b } + c _ { b } ) \right)\tag{6}
$$

where $B$ is the number of buildings in the map, $\kappa _ { b }$ is a steepness factor, $c _ { b }$ is the minimum allowed distance in meters from a building, $d _ { i b }$ is the distance function from any given ABS i to any given building b’s closest edge, defined as

$$
\begin{array} { r l } & { d _ { i b } = \sqrt { d _ { x } ^ { 2 } + d _ { y } ^ { 2 } } , } \\ & { d _ { x } = \operatorname* { m a x } \left( \operatorname* { m a x } \left( m _ { x } - p _ { x } , p _ { x } - M _ { x } \right) , 0 \right) , } \\ & { d _ { y } = \operatorname* { m a x } \left( \operatorname* { m a x } \left( m _ { y } - p _ { y } , p _ { y } - M _ { y } \right) , 0 \right) } \end{array}\tag{7}
$$

given $( p _ { x } , p _ { y } )$ as the ABS’s XY coordinates, $( m _ { x } , m _ { y } )$ and $( M _ { x } , M _ { y } )$ as the minimum and maximum XY coordinate of a building’s binding box, respectively. As the ABS elevation is assumed constant, buildings that have heights below the hovering elevation (plus a tolerance of 15m to avoid blockages from rooftops) are excluded from the penalty term computation. In order to provide a better understanding of how the proposed loss function works, Fig. 4 offers a visual representation of the environment-dependent loss terms γ $P _ { a } + \eta P _ { b }$ . From this figure, it is possible to note how the loss values progressively become smaller for locations closer to the center of AOI, while higher values are present in proximity of buildings that have height higher than defined ABS’ hovering height.

The optimization procedure considers the $( x _ { i } , y _ { i } )$ coordinates for all the N ABSs as a set of parameters $\Theta _ { \mathrm { l } }$ , and aims to perform gradient-descent optimization by following the inverse direction provided by the gradients of the loss function w.r.t. the location parameters, i.e. $\frac { \overline { { \delta } } \mathcal { L } _ { p } } { \delta \Theta _ { 1 } }$

## B. Orientation and Power Optimization

Once the routes and final locations of ABS have been identified by the previous optimization step, their orientations also need to be adjusted. For this optimization step, we initially assume that the ABS antenna panels face directly the ground plane, with a mechanical tilt equal to $\theta _ { i } = 9 0 ^ { \circ }$ for each i-th ABS. As their location in the 3D space will also affect the wireless propagation features of the serviced area, their deployment needs to be optimized so that their transmissions will not interfere with each other, hence by minimizing their mutual interference by jointly adjusting their location and transmission power.

To do so, we utilize the differentiable Ray Tacer provided by Sionna to compute a differentiable Coverage Map $C \in$ $\dot { \mathbb { R } ^ { N \times C _ { x } \times C _ { y } } }$ , which consists of the average path gain experienced at each $( x , y )$ location of a discretized version of the ground plane made of $N _ { C } = C _ { x } \cdot C _ { y }$ surface cells of equal size. Each cell reports a value equal to the sum of contributions of reflected/diffused paths and diffracted paths, for each of the N ABS. For a given ABS i, the value of each cell $C _ { i , x , y } = \hat { g } ( i , x , y )$ is computed via Monte Carlo simulation as follows:

$$
\begin{array} { l } { \displaystyle \hat { g } ( i , x , y ) = } \\ { \displaystyle \frac { 4 \pi } { N _ { R } N _ { C } } \sum _ { n = 1 } ^ { N _ { R } } \left| h \left( s \left( \psi _ { n } \right) \right) \right| ^ { 2 } \frac { r \left( \psi _ { n } \right) ^ { 2 } } { \left| \cos \alpha \left( \psi _ { n } \right) \right| } \mathbf { 1 } \{ s \left( \psi _ { n } \right) \in C _ { i , x , y } \} } \end{array}\tag{8}
$$

where $N _ { R }$ is the number of valid rays hitting $C _ { i , x , y }$ cell, $| h ( s ( \psi _ { n } ) ) | ^ { 2 }$ is the squared amplitude of the path coefficients at position $s ( \psi _ { n } )$ (i.e., the point where the n-th path with <sup>( )</sup>direction of departure $\psi _ { n }$ intersects the Coverage Map), $r ( \psi _ { n } )$ is the lenght of the n-th path with direction of departure $\psi _ { n } ,$ $\alpha ( \psi _ { n } )$ is the angle between the coverage map normal and the direction of arrival of the path with direction of departure $\psi _ { n }$ and 1 $\{ s ( \psi _ { n } ) \in C _ { i , x , y } \}$ is the function that sets a value of 1 if the intersection point with the Coverage Map is within the current $( x , y )$ cell, or zero otherwise. If we consider a transmission power $P _ { i } ^ { \mathrm { t x } }$ expressed in Watts for each i-th ABS, we can obtain the Received Signal Strength (RSS) at each receiver location in the map as $\mathrm { R S S } _ { i , x , y } = P _ { i } ^ { \mathrm { t x } } \cdot \hat { g } ( i , x , y )$

We propose two separate optimization strategies based on gradient-descent in order to (i) improve the mutual interference of the ABSs over the whole map and (ii) improve the mutual interference over a set of specific AOIs.

1) ABSs’ Mutual Interference Optimization (Method $I ) .$ From proposed location optimization approach, we observe that the ABSs tend to group around the AOIs in a clustered formation, assuming AOIs are sufficiently close to each other. Intuitively, the ABSs will have lower Signal-to-Interference-Ratio (SIR) when located within the cluster and higher SIR when located on its borders. Although it might seem reasonable to optimize orientations by maximizing the average SIR for all devices in the map, it is important to note that this approach might not necessarily produce a better configuration, as the gradients might favor devices with excessively high SIR while neglecting the ones in the lowest SIR regions, creating areas in the map with a wider disparity of Quality-of-Service (QoS). Hence, we formulate a loss function based on a Max-Min approach that prioritizes improving the SIR of ABSs that experience the highest interference (i.e., those within the ABS cluster) while making sure not to excessively disrupt those in higher SIR regions (i.e., the ones on the cluster border). By targeting the worst-case SIR, the Max-Min approach ensures fairness by uplifting the leastperforming areas while avoiding over-optimization of ABSs with dominant SIR conditions. Specifically, for each i-th ABS we compute its SIR map in linear scale $\mathbf { R } _ { i } \mathbf { \bar { \Psi } } \in \mathbb { R } ^ { C _ { x } \times C _ { y } }$ from the RSS perceived at each cell location by combining the coverage map $\mathbf { \bar { \boldsymbol { C } } } \in \mathbb { R } ^ { N \times C _ { x } \times C _ { y } }$ path gains produced by Sionna and the transmission power of each ABS as follows:

$$
R _ { i , x , y } = \frac { P _ { i } ^ { \mathrm { t x } } C _ { i , x , y } } { \sum _ { j \neq i } P _ { j } ^ { \mathrm { t x } } C _ { j , x , y } + \epsilon }\tag{9}
$$

where $C _ { i } \in \mathbb { R } ^ { C _ { x } \times C _ { y } }$ is the i-th ABS’s coverage map and $\epsilon =$ $1 e - 2 0$ is a small value used as a proxy for thermal noise term <sup>1 20</sup>and for numerical stability. Then, we compute a coverage mask $M _ { i } \in \mathbb { R } ^ { C _ { x } \times C _ { y } }$

$$
M _ { i , x , y } = \left\{ { \begin{array} { l l } { 1 , } & { { \mathrm { i f } } \ C _ { i , x , y } > 0 } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } } \end{array} } \right.\tag{10}
$$

that we use to compute the average effective SIR $\hat { r } _ { i } \in \mathbb { R }$ expressed in dB as follows:

$$
\hat { r } _ { i } = \frac { \sum _ { y } \sum _ { x } R _ { i , x , y } ^ { d B } \cdot M _ { i , x , y } } { \sum _ { y } \sum _ { x } M _ { i , x , y } }\tag{11}
$$

where $\pmb { R } _ { i } ^ { d B } = 1 0 \cdot \log _ { 1 0 } ( \pmb { R } _ { i } )$ correspond to the SIR map $R _ { i }$ in logarithmic scale. It is important to note that the effective SIR, rather than the SIR over the whole map, has to be computed in order to avoid diluting the average SIR computation over the cells that have no coverage.

Once all the $\boldsymbol { r } = \{ \hat { r } _ { 1 } , . . . , \hat { r } _ { N } \}$ are obtained for all N ABSs, we formulate the first term of our loss function as follows:

$$
\mathcal { L } _ { \mathrm { s m o o t h m i n } } = - \mathrm { N L S E } \left( \boldsymbol { r } , \beta _ { \mathrm { L } } \right)\tag{12}
$$

where the Negative Log-Sum-Exp (NLSE) is used a smooth approximation of the minimum function. NLSE is defined as:

$$
N L S E ( \pmb { r } , \beta _ { \mathrm { L } } ) = - \frac { 1 } { \beta _ { \mathrm { L } } } \log \left( \sum _ { m = 1 } ^ { M } e ^ { - \beta _ { \mathrm { L } } r _ { m } } \right)\tag{13}
$$

and for small values of $\beta _ { \mathrm { { L } } } > 0$ it progressively includes more values of the input vector in the computation of approximate minimum, avoiding steep discontinuities in the loss output as it maximizes its minimums. Moreover, in order to avoid degrading too much the SIR of the other ABS, we add a second term to our loss function defined as follows:

$$
\mathcal { L } _ { \mathrm { a v g S I R } } = - \frac { \sum _ { m } ^ { M } r _ { m } } { M }\tag{14}
$$

that aim to maximize the overall average SIR for all ABSs and that is intended to be scaled using a factor $0 < \xi < 1$ to avoid over-optimization of ABS with high SIR as explained before.

Finally, we obtain the total loss function for orientation optimization by putting together the two loss terms defined above as follows:

$$
\mathcal { L } _ { o } = \mathcal { L } _ { \mathrm { s m o o t h m i n } } + \xi \mathcal { L } _ { \mathrm { a v g S I R } }\tag{15}
$$

The optimization procedure considers the set of $( \phi _ { i } , \theta _ { i } , P _ { i } ^ { \mathrm { t x } } )$ mechanical azimuth, mechanical tilt and transmission power for all the N ABSs as a set of parameters $\Theta _ { \mathrm { o p } } .$ , and aims to perform gradient-descent optimization by following the inverse direction provided by the gradients of the loss function w.r.t. the location parameters, i.e. $\overline { { \frac { \delta \mathcal { L } _ { o } } { \delta \Theta _ { \mathrm { o p } } } } }$

2) AOIs’ SIR Optimization (Method 2): The second approach we propose focuses on improving the mutual interference of ABSs specifically for a set of AOIs considered in the targeted urban scenario: while the previous approach considers the entirety of covered cells in the map, this approach focuses on maximizing the effective SIR of cells associated with the AOIs identified by the network operator by maximizing the SIR of each AOI’s serving ABS, in order to improve the signal strength of the UEs located in those areas.

To formulate the loss function for this strategy, we refer to the effective average SIR for each i-th ABS from (11). In this case, instead of considering the entire coverage map to compute $\boldsymbol { { \hat { r } } } _ { i }$ , we only consider the square area described by the center $( z _ { m } , w _ { m } )$ of the m-th AOI and defined within $\pm r _ { m }$ range of its radius on both X and Y-axis. To do so, we first obtain the cell’s x and y indexes of AOI’s center, $x _ { m } ^ { * }$ and $y _ { m } ^ { * }$ . Then, we compute the length in cells associated with AOI’s radius, $r _ { m } ^ { * } .$ assuming equal cell size along the X and Y-axis. Finally, we extract the coverage map’s area of m-th AOI, $\boldsymbol { A } _ { i } \in \mathbb { R } ^ { 2 r _ { m } ^ { * } \times 2 r _ { m } ^ { * } }$ for each i-th ABS:

$$
\pmb { A } _ { i } = \pmb { R } _ { i , x _ { m } ^ { * } } \pmb { \mathrm { { r } } } _ { m } ^ { * } , y _ { m } ^ { * } \pmb { \mathrm { { r } } } _ { m } ^ { * }\tag{16}
$$

Once $A _ { i }$ is obtained, we compute the effective SIR for all ABS $\pmb { r } _ { m } ^ { * } = \{ \tilde { r } _ { 1 } , . . . , \tilde { r } _ { N } \}$ using (11) and by substituting $\mathbf { { \mathit { R } } } _ { i }$ with $A _ { i }$ We then obtain its smooth maximum using Log-Sum-Exp (LSE) function, defined as:

$$
\begin{array} { r } { L S E ( \pmb { r } _ { m } ^ { * } , \beta _ { \mathrm { L } } ) = - N L S E ( \pmb { r } _ { m } ^ { * } , \beta _ { \mathrm { L } } ) } \end{array}\tag{17}
$$

The goal is to optimize the orientations and transmission powers of all ABSs in order to maximize the effective SIR for the ABS serving a given AOI (i.e., the one that has highest SIR for the cells corresponding to a given AOI), for all M AOIs. Combining these terms for all AOIs, we obtain the following unweighted loss term:

$$
\mathcal { L } _ { u } = - \sum _ { m = 1 } ^ { M } L S E ( \pmb { r } _ { m } ^ { * } , \beta _ { \mathrm { L } } )\tag{18}
$$

Similarly to the approach discussed in Section V-B1, we want to prioritize optimization of AOIs that suffer from the highest SIR compared to all others, while still aiming to improve collectively the SIR experienced in all AOIs. To do so, we use a weighted version of (18) that uses softmin with temperature function to assign priorities to each SIR maximization objective. Specifically, the weighted loss function will look as follows:

$$
\mathcal { L } _ { w } = - \sum _ { m = 1 } ^ { M } w _ { m } \cdot L S E ( \pmb { r } _ { m } ^ { * } , \beta _ { \mathrm { L } } )\tag{19}
$$

TABLE IV  
CONFIGURATION OF AREAS OF INTEREST (AOIS) FOR EXPERIMENTAL EVALUATION OF GRADIENT-BASED ABS DEPLOYMENT. COORDINATES $( z _ { m } , w _ { m } )$ AND RADIUS $r _ { m }$ OF THE m-TH AOI ARE EXPRESSED IN METERS.
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>AOI 0</td><td rowspan=1 colspan=1>AOI 1</td><td rowspan=1 colspan=1>AOI 2</td><td rowspan=1 colspan=1>AOI 3</td><td rowspan=1 colspan=1>AOI 4</td></tr><tr><td rowspan=1 colspan=1> $z _ { m }$ </td><td rowspan=1 colspan=1>450.0</td><td rowspan=1 colspan=1>-247.0</td><td rowspan=1 colspan=1>-423.0</td><td rowspan=1 colspan=1>353.0</td><td rowspan=1 colspan=1>-852.0</td></tr><tr><td rowspan=1 colspan=1> ${ \underline { { w _ { m } } } }$ </td><td rowspan=1 colspan=1>168.0</td><td rowspan=1 colspan=1>145.0</td><td rowspan=1 colspan=1>-416.0</td><td rowspan=1 colspan=1>-622.0</td><td rowspan=1 colspan=1>133.0</td></tr><tr><td rowspan=1 colspan=1> $r _ { m }$ </td><td rowspan=1 colspan=1>300.0</td><td rowspan=1 colspan=1>250.0</td><td rowspan=1 colspan=1>250.0</td><td rowspan=1 colspan=1>250.0</td><td rowspan=1 colspan=1>250.0</td></tr></table>

where the weights $w _ { m }$ sum up to 1.0 and are defined using the softmin function:

$$
w _ { m } = { \frac { \exp { \left( - { \frac { x _ { m } } { T } } \right) } } { \sum _ { j = 1 } ^ { M } \exp { \left( - { \frac { x _ { j } } { T } } \right) } } }\tag{20}
$$

where $\boldsymbol { x } _ { m } = L S E ( \boldsymbol { r } _ { m } ^ { * } , \beta _ { \mathrm { L } } )$ and $T$ is the temperature hyperparameter to control the sharpness of the weight distribution: a lower temperature makes the softmin more sensitive to differences, giving much higher weights to smaller values, while a higher temperature smooths the weights, distributing attention more evenly across all values. In order to promote fairness while still prioritizing the AOI with lowest perceived SIR, we choose a high temperature temperature approach.

In this case, we aim to optimize the same set of parameters $\Theta _ { \mathrm { o p } }$ introduced in the previous section, but this time optimizing w.r.t. ${ \mathcal { L } } _ { w }$ loss function, i.e. $\frac { \delta \mathcal { L } _ { w } } { \delta \Theta _ { \mathrm { o p } } }$

## C. Performance Evaluation

1) Hyperparameter Selection Methodology: Our hyperparameter values were determined through systematic exploration guided by the following principles:

Loss Function Scaling Factors: Values selected to balance competing optimization objectives while ensuring numerical stability. $\alpha = 0 . 0 1$ provides lower weight for coverage to prevent overshadowing obstacle avoidance, while $\beta = 1 . 0$ ensures standard weight for AOI attraction. $\gamma = 0 . 8$ allows necessary clustering near AOIs, and $\eta = 1 . 0$ maintains full weight for safety-critical collision avoidance.

\- Steepness Factors: $\kappa _ { a } = 0 . 0 2$ provides smooth attraction gradients avoiding optimization instability, $\kappa _ { b } = 0 . 5$ creates sharp building penalties while maintaining differentiability, and $\kappa _ { i } = 0 . 2 5$ ensures smooth sigmoid transitions.

\- Optimization Parameters: $\beta _ { L } = 1 . 0$ provides appropriate smoothness for minimum approximation, $\xi = 0 . 2 5$ prevents over-optimization of high-SIR ABSs, and $T = 2 5$ ensures fair attention distribution across AOIs.

These values were validated by achieving over 97% AOI satisfaction rates and effective obstacle avoidance across 1,800+ test runs.

2) Results for ABS Positioning: In order to evaluate the performance of proposed gradient-descent based route finding and positioning algorithm described in Section V-A, we define a fixed set of $M = 5$ non-overlapping AOIs in the area of Tokyo 3D map described above. Table IV reports the configuration chosen for this experiments. We define an AOI satisfaction rate,

![](images/9da8f7e9b0f11029fe33b9df16de70f3f7cfb012e2b39eb0cb660cc3f3850253.jpg)  
Fig. 5. AOI satisfaction metric for all combinations of M AOIs taken in groups of $m = \{ 1 , 2 , 3 , 4 , 5 \}$ . Each combination is averaged over 50 runs with semirandom initial ABS deployment, for a total of {250, 500, 500, 250, 50} runs each.

defined as:

$$
S _ { A O I } = \frac { \sum _ { m = 1 } ^ { M } \operatorname* { m i n } \left( 1 , \sum _ { n = 1 } ^ { N } \mathbf { 1 } \left\{ d _ { n } \leq \frac { 2 r _ { m } } { 3 } \right\} \right) } { M }\tag{21}
$$

which determines the ratio of correctly served AOIs by checking that distance $d _ { n } = | | p _ { n } - \pmb { c } _ { m } | |$ from the ABS coordinate $\pmb { p } _ { n } = ( x _ { n } , y _ { n } )$ <sup>=</sup>obtained at the end of the optimization to any given AOI center $\pmb { c } _ { m } = \left( z _ { m } , w _ { n } \right)$ coordinate is within $2 / 3$ of its radius $r _ { m } .$ , while allowing for one or more ABS to hover within the same AOI. Moreover, in order to test the performance of proposed algorithm under different conditions, we evaluate this approach for different number of AOIs considered at once in the map. We perform multiple experiments with $m = \{ 1 , 2 , 3 , 4 , 5 \}$ and for each of these configuration we test all the $\binom { M } { m }$ possible combinations of AOIs. Finally, for each AOI configuration, we perform 50 tests with initial semi-random deployment of ABSs. For each experiment, we consider a number of ABS $N = 1 0$ and use Adam optimizer with a learning rate $l _ { r } = 2 . 0 ,$ a limit of 2500 optimization iterations and early stopping criterion with a patience of 20 training epochs. We use hyper-parameter exploration to define our loss parameters: we choose loss term scaling factors $\alpha = 0 . 0 1 , \beta = 1 . 0 , \gamma = 0 . 8$ and $\eta = 1 . 0 ;$ for steepness factors, we select $\kappa _ { a } = 0 . 0 2 , \kappa _ { b } = 0 . 5 , \kappa _ { i } = 0 . 2 5$ ; finally, we define $c _ { b } = 1 5 \mathrm { m }$ and $d _ { \operatorname* { m i n } } = 4 0 0$ m as minimum distances of <sup>= 15 = 400</sup>ABSs from buildings and among ABSs themselves, respectively, and configure a set of $5 \times 5$ grid points equally distributed along the X and Y-axis of the map with a margin $m _ { e } = 1 5 0$ m from its edges, used for the coverage term K.

Fig. 5 shows the average satisfaction rate for all AOI combinations. The results indicate that our approach successfully configures ABS deployments, achieving an AOI satisfaction rate of over 97% across all runs and configurations. This demonstrates its effectiveness in navigating obstacles and landing in designated service areas.

To better illustrate the optimization performance, Fig. 6 presents a sample run considering all AOIs. The proposed method efficiently leverages the 3D city-scale map to optimize multiple ABS positions simultaneously while generating obstacle-avoiding routes (Fig. 6(b)) for real-world deployment.

TABLE V  
EFFECTIVE SIR (DB) EXPERIENCED BY EACH ABS BEFORE AND AFTER OPTIMIZATION. THE $\mathcal { L } _ { o }$ APPROACH ACHIEVES SUPERIOR WORST-CASE PERFORMANCE (MIN SIR) AND FAIRNESS (STD. DEV., JAIN’S FAIRNESS) COMPARED TO NAÏVE AVERAGE SIR MAXIMIZATION, DEMONSTRATING ITS EFFECTIVENESS IN IMPROVING POORLY-PERFORMING ABSS WHILE MAINTAINING OVERALL SYSTEM BALANCE.
<table><tr><td rowspan=1 colspan=1>SIR</td><td rowspan=1 colspan=1>Initial</td><td rowspan=1 colspan=1> $\mathbf { A f t e r } - \mathcal { L } _ { o }$ </td><td rowspan=1 colspan=1> $\mathbf { \overline { { A f t e r - \mathcal { L } _ { A v g S I R } } } }$ </td><td rowspan=1 colspan=1>Random</td></tr><tr><td rowspan=1 colspan=1>ABS 1</td><td rowspan=1 colspan=1>-9.595</td><td rowspan=1 colspan=1>-1.352</td><td rowspan=1 colspan=1>-12.963</td><td rowspan=1 colspan=1>-12.773</td></tr><tr><td rowspan=1 colspan=1>ABS 2</td><td rowspan=1 colspan=1>-0.189</td><td rowspan=1 colspan=1>1.421</td><td rowspan=1 colspan=1>7.941</td><td rowspan=1 colspan=1>-3.246</td></tr><tr><td rowspan=1 colspan=1>ABS3</td><td rowspan=1 colspan=1>-1.537</td><td rowspan=1 colspan=1>1.214</td><td rowspan=1 colspan=1>-3.302</td><td rowspan=1 colspan=1>-3.636</td></tr><tr><td rowspan=1 colspan=1>ABS4</td><td rowspan=1 colspan=1>-4.213</td><td rowspan=1 colspan=1>-0.542</td><td rowspan=1 colspan=1>-10.621</td><td rowspan=1 colspan=1>-10.530</td></tr><tr><td rowspan=1 colspan=1>ABS5</td><td rowspan=1 colspan=1>4.625</td><td rowspan=1 colspan=1>0.471</td><td rowspan=1 colspan=1>8.950</td><td rowspan=1 colspan=1>-2.795</td></tr><tr><td rowspan=1 colspan=1>ABS6</td><td rowspan=1 colspan=1>-1.165</td><td rowspan=1 colspan=1>-0.439</td><td rowspan=1 colspan=1>4.660</td><td rowspan=1 colspan=1>-7.507</td></tr><tr><td rowspan=1 colspan=1>ABS7</td><td rowspan=1 colspan=1>19.760</td><td rowspan=1 colspan=1>11.057</td><td rowspan=1 colspan=1>19.729</td><td rowspan=1 colspan=1>14.660</td></tr><tr><td rowspan=1 colspan=1>ABS 8</td><td rowspan=1 colspan=1>25.527</td><td rowspan=1 colspan=1>12.728</td><td rowspan=1 colspan=1>32.018</td><td rowspan=1 colspan=1>18.893</td></tr><tr><td rowspan=1 colspan=1>ABS 9</td><td rowspan=1 colspan=1>5.666</td><td rowspan=1 colspan=1>0.454</td><td rowspan=1 colspan=1>6.422</td><td rowspan=1 colspan=1>0.981</td></tr><tr><td rowspan=1 colspan=1>ABS 10</td><td rowspan=1 colspan=1>3.248</td><td rowspan=1 colspan=1>0.192</td><td rowspan=1 colspan=1>4.793</td><td rowspan=1 colspan=1>-0.519</td></tr><tr><td rowspan=1 colspan=1>Average</td><td rowspan=1 colspan=1>4.213</td><td rowspan=1 colspan=1>2.520</td><td rowspan=1 colspan=1>5.763</td><td rowspan=1 colspan=1>-0.647</td></tr><tr><td rowspan=1 colspan=1>Std. Dev.</td><td rowspan=1 colspan=1>10.209</td><td rowspan=1 colspan=1>4.765</td><td rowspan=1 colspan=1>12.662</td><td rowspan=1 colspan=1>9.648</td></tr><tr><td rowspan=1 colspan=1>Minimum</td><td rowspan=1 colspan=1>-9.595</td><td rowspan=1 colspan=1>-1.352</td><td rowspan=1 colspan=1>-12.963</td><td rowspan=1 colspan=1>-12.773</td></tr><tr><td rowspan=1 colspan=1>Jain&#x27;s Fairness</td><td rowspan=1 colspan=1>0.157</td><td rowspan=1 colspan=1>0.306</td><td rowspan=1 colspan=1>0.115</td><td rowspan=1 colspan=1>0.178</td></tr></table>

Finally, Fig. 6(c) shows that, while all AOIs are covered, the remaining ABSs distribute in a lattice-like formation, useful for serving as relay nodes or providing additional coverage.

3) Results for Orient. And Pow. Optimization (Method 1): Starting from the location configuration obtained in the experiment illustrated in Fig. 6(c), we now apply the orientation optimization strategy described in Section V-B1 to showcase the performance of proposed optimization approach for improving $_ \mathrm { A B S s } '$ mutual interference when considering the whole urban site map. For this experiment, we consider ABS mounting directional antennas specified in the 5 G NR standard TR 38.901 [37] and UE mounting half-wave dipole antennas, both with dual polarization (i.e., vertical and horizontal) and operating at a center frequency $f _ { c } = 3 . 5 \mathrm { G H z }$ . For every coverage map computation, we consider map cells size of m × m and downlink transmissions by setting the initial transmission power $P _ { i } ^ { \mathrm { t x } }$ in Watts for each ABS to 43.0 dBm. We consider Line-of-Sight (LOS), specular reflection, and diffuse scattering as possible rays interactions when generating the coverage maps during optimization and for coverage map plots. For each map, we consider 5M rays equally distributed across the ABSs and up to 3 ray interactions before reaching the destinations. For simplicity, we assign all objects and surfaces in the map with concrete material scattering properties, as defined by ITU-R P.2040 [38]. For these experiments, we use the RMSProp optimizer with learning rate $l _ { r } = 0 .$ and 150 training epochs, with early stopping criterion using $l _ { r }$ decay of 0.5 and patience of 5 training epochs. For the loss hyper-parameters, we choose $\beta _ { \mathrm { L } } = 1 . 0$ for the smooth minimum computation and $\xi = 0 . 2 5$ as a scaling factor for the global average SIR loss term.

To evaluate the benefits of the proposed approach, Table V compares the initial effective SIR per ABS with the results from (i) the Max-Min approach $( { \mathcal { L } } _ { o } ) _ { : }$ , (ii) a naïve average SIR maximization $( \mathcal { L } _ { \mathrm { a v g S I R } } )$ , and (iii) uniform random parameter selection. While approach (ii) achieves the highest average SIR (5.76 dB), it creates significant performance inequality

![](images/62961fde8f4b2338284bb56b1d982f86cf24b5fd8f791bd022c4cf72382c24f0.jpg)  
(a) Initial random deployment

![](images/ed09d28a42e37fc45fee9b0fa1d9e69b4c8991becfbcfa1e0a16d96cf537c6a0.jpg)  
(b) Generated routes

![](images/5bd0d39bec8d4095e167156eed7860fc19ccb77d83e45425facb3540f9664ac4.jpg)  
(c) Final deployment  
Fig. 6. Sample run from gradient-based ABS deployment optimization with M = 5 AOIs and $N = 1 0 { \mathrm { ~ A B S s } }$ . Each ABS trajectory is marked with a different color and each circle represents a given AOI.

## TABLE VI

DIFFERENCE OF AVERAGE SIR (DB) FOR EACH AOI AFTER ORIENTATION AND POWER OPTIMIZATION. ABSS SERVING A GIVEN AOI (I.E., THE ONE WITH HIGHEST SIR) ARE INDICATED IN BOLD. RESULTS ARE REPORTED FOR SAMPLE SCENARIO IN FIG. 6(c).

<table><tr><td rowspan=1 colspan=6>Average AOI Effective SIR (dB) difference</td></tr><tr><td rowspan=1 colspan=6>Weighted AOI SIR optimization  $\overline { { \mathcal { L } _ { w } } }$ (sample scenario)</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AOI 0</td><td rowspan=1 colspan=1>AOI 1</td><td rowspan=1 colspan=1>AOI 2</td><td rowspan=1 colspan=1>AOI3</td><td rowspan=1 colspan=1>AOI4</td></tr><tr><td rowspan=1 colspan=1>ABS1</td><td rowspan=1 colspan=1>+0.99</td><td rowspan=1 colspan=1>+11.51</td><td rowspan=1 colspan=1>-0.99</td><td rowspan=1 colspan=1>+0.05</td><td rowspan=1 colspan=1>+0.23</td></tr><tr><td rowspan=1 colspan=1>ABS 2</td><td rowspan=1 colspan=1>-0.02</td><td rowspan=1 colspan=1>-4.51</td><td rowspan=1 colspan=1>-2.27</td><td rowspan=1 colspan=1>-0.09</td><td rowspan=1 colspan=1>-0.25</td></tr><tr><td rowspan=1 colspan=1>ABS3</td><td rowspan=1 colspan=1>-0.79</td><td rowspan=1 colspan=1>-4.94</td><td rowspan=1 colspan=1>-6.22</td><td rowspan=1 colspan=1>-0.77</td><td rowspan=1 colspan=1>-0.26</td></tr><tr><td rowspan=1 colspan=1>ABS4</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>-10.37</td><td rowspan=1 colspan=1>-8.67</td><td rowspan=1 colspan=1>+2.48</td><td rowspan=1 colspan=1>-0.48</td></tr><tr><td rowspan=1 colspan=1>ABS5</td><td rowspan=1 colspan=1>+0.01</td><td rowspan=1 colspan=1>-1.40</td><td rowspan=1 colspan=1>-4.89</td><td rowspan=1 colspan=1>+0.07</td><td rowspan=1 colspan=1>+5.17</td></tr><tr><td rowspan=1 colspan=1>ABS6</td><td rowspan=1 colspan=1>+0.08</td><td rowspan=1 colspan=1>-5.45</td><td rowspan=1 colspan=1>-1.70</td><td rowspan=1 colspan=1>-0.004</td><td rowspan=1 colspan=1>-0.93</td></tr><tr><td rowspan=1 colspan=1>ABS7</td><td rowspan=1 colspan=1>-0.51</td><td rowspan=1 colspan=1>-2.33</td><td rowspan=1 colspan=1>-5.08</td><td rowspan=1 colspan=1>-0.25</td><td rowspan=1 colspan=1>+0.02</td></tr><tr><td rowspan=1 colspan=1>ABS8</td><td rowspan=1 colspan=1>-0.49</td><td rowspan=1 colspan=1>+0.28</td><td rowspan=1 colspan=1>-1.12</td><td rowspan=1 colspan=1>-0.62</td><td rowspan=1 colspan=1>+0.01</td></tr><tr><td rowspan=1 colspan=1>ABS9</td><td rowspan=1 colspan=1>+0.03</td><td rowspan=1 colspan=1>+0.11</td><td rowspan=1 colspan=1>+9.57</td><td rowspan=1 colspan=1>+1.94</td><td rowspan=1 colspan=1>-1.90</td></tr><tr><td rowspan=1 colspan=1>ABS 10</td><td rowspan=1 colspan=1>+0.01</td><td rowspan=1 colspan=1>-5.64</td><td rowspan=1 colspan=1>-2.90</td><td rowspan=1 colspan=1>+0.0003</td><td rowspan=1 colspan=1>-5.79</td></tr><tr><td rowspan=1 colspan=1>Serving ABS onl</td><td rowspan=1 colspan=5>y - Random Baseline(sample scenario, 50 runs mean)</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AOI 0</td><td rowspan=1 colspan=1>AOI 1</td><td rowspan=1 colspan=1>AOI 2</td><td rowspan=1 colspan=1>AOI3</td><td rowspan=1 colspan=1>AOI 4</td></tr><tr><td rowspan=1 colspan=1>ABS (serving)</td><td rowspan=1 colspan=1>-8.92</td><td rowspan=1 colspan=1>-6.14</td><td rowspan=1 colspan=1>-8.43</td><td rowspan=1 colspan=1>-10.17</td><td rowspan=1 colspan=1>-10.56</td></tr></table>

with a fairness $\mathrm { i n d e x } ^ { 4 }$ of only 0.115 and degrades worst-case performance (minimum SIR of −12.96 dB). This approach over-optimizes ABSs with already high SIR while severely penalizing those with lower values (e.g., ABS 1 and 4 at the cluster center). In contrast, the Max-Min approach (i) achieves superior fairness (fairness index of 0.306) and dramatically improves worst-case performance (minimum SIR of −1.35 dB vs −12.96 dB), demonstrating effective interference management by boosting lower-SIR ABSs (ABS 1, 2, 3, 4, and 6) by up to 8.24 dB while maintaining reasonable average performance. Random parameter selection, averaged over 50 samples, shows the poorest overall performance with negative average SIR (−0.65 dB) and very low fairness (0.178), validating the necessity of intelligent optimization. Table VIII details the final orientations and transmit power settings for the Max-Min approach.

<sup>4</sup>Jain’s Fairness Index: $F I = { \frac { ( \sum _ { i = 1 } ^ { n } x _ { i } ) ^ { 2 } } { n \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } } }$ , where $x _ { i }$ are linear power values converted from dB, and $0 \leq F \overline { { I } } \leq \overline { { 1 } }$ with higher values indicating more equitable distribution.

## TABLE VII

AVERAGE SIR DIFFERENCE FOR EACH AOI UNDER 50 DIFFERENT ABSS DEPLOYMENTS
<table><tr><td rowspan=1 colspan=6>Average AOI Effective SIR (dB) difference</td></tr><tr><td rowspan=1 colspan=6>Serving ABS only - Lw (50 scenarios/deployments mean)</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AOI 0</td><td rowspan=1 colspan=1>AOI1</td><td rowspan=1 colspan=1>AOI 2</td><td rowspan=1 colspan=1>AOI3</td><td rowspan=1 colspan=1>AOI4</td></tr><tr><td rowspan=1 colspan=1>ABS (serving)</td><td rowspan=1 colspan=1>-1.21</td><td rowspan=1 colspan=1>+12.98</td><td rowspan=1 colspan=1>+10.01</td><td rowspan=1 colspan=1>-1.70</td><td rowspan=1 colspan=1>+1.08</td></tr></table>

## TABLE VIII

CONFIGURATIONS OBTAINED WITH PROPOSED OPTIMIZATION FRAMEWORKS FOR SAMPLE SCENARIO (FIG. 6(c)). φ IS THE AZIMUTH ANGLE OF ROTATION IN DEGREES, θ IS THE MECHANICAL TILT IN DEGREE, P <sup>TX</sup> IS THE TRANSMISSION POWER IN DBM.
<table><tr><td rowspan=1 colspan=1>ABS</td><td rowspan=1 colspan=2>Coordinates</td><td rowspan=1 colspan=3>Orient. &amp; Power - Lo</td><td rowspan=1 colspan=3>Orient. &amp; Power - Lw</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X (m)</td><td rowspan=1 colspan=1>Y (m)</td><td rowspan=1 colspan=1>φ</td><td rowspan=1 colspan=1>θ</td><td rowspan=1 colspan=1>ptx</td><td rowspan=1 colspan=1>φ</td><td rowspan=1 colspan=1>θ</td><td rowspan=1 colspan=1>ptx</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-246.60</td><td rowspan=1 colspan=1>144.50</td><td rowspan=1 colspan=1>17.72</td><td rowspan=1 colspan=1>154.29</td><td rowspan=1 colspan=1>42.96</td><td rowspan=1 colspan=1>-30.07</td><td rowspan=1 colspan=1>88.96</td><td rowspan=1 colspan=1>43.00</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>223.43</td><td rowspan=1 colspan=1>334.20</td><td rowspan=1 colspan=1>-7.48</td><td rowspan=1 colspan=1>25.71</td><td rowspan=1 colspan=1>40.78</td><td rowspan=1 colspan=1>37.09</td><td rowspan=1 colspan=1>63.33</td><td rowspan=1 colspan=1>37.11</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>245.27</td><td rowspan=1 colspan=1>-174.25</td><td rowspan=1 colspan=1>-25.37</td><td rowspan=1 colspan=1>25.71</td><td rowspan=1 colspan=1>39.51</td><td rowspan=1 colspan=1>-4.80</td><td rowspan=1 colspan=1>77.19</td><td rowspan=1 colspan=1>35.23</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>-148.59</td><td rowspan=1 colspan=1>-243.15</td><td rowspan=1 colspan=1>2.54</td><td rowspan=1 colspan=1>120.73</td><td rowspan=1 colspan=1>41.88</td><td rowspan=1 colspan=1>-42.43</td><td rowspan=1 colspan=1>25.71</td><td rowspan=1 colspan=1>35.30</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>-735.17</td><td rowspan=1 colspan=1>56.92</td><td rowspan=1 colspan=1>81.42</td><td rowspan=1 colspan=1>104.03</td><td rowspan=1 colspan=1>38.91</td><td rowspan=1 colspan=1>-28.43</td><td rowspan=1 colspan=1>138.64</td><td rowspan=1 colspan=1>39.49</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>-68.51</td><td rowspan=1 colspan=1>503.55</td><td rowspan=1 colspan=1>11.42</td><td rowspan=1 colspan=1>25.71</td><td rowspan=1 colspan=1>39.75</td><td rowspan=1 colspan=1>38.94</td><td rowspan=1 colspan=1>74.68</td><td rowspan=1 colspan=1>35.08</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>225.58</td><td rowspan=1 colspan=1>-574.39</td><td rowspan=1 colspan=1>-60.03</td><td rowspan=1 colspan=1>25.71</td><td rowspan=1 colspan=1>32.10</td><td rowspan=1 colspan=1>-41.10</td><td rowspan=1 colspan=1>56.94</td><td rowspan=1 colspan=1>39.03</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>450.19</td><td rowspan=1 colspan=1>168.14</td><td rowspan=1 colspan=1>-0.84</td><td rowspan=1 colspan=1>39.74</td><td rowspan=1 colspan=1>26.89</td><td rowspan=1 colspan=1>-1.79</td><td rowspan=1 colspan=1>81.77</td><td rowspan=1 colspan=1>40.42</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>-535.52</td><td rowspan=1 colspan=1>-343.17</td><td rowspan=1 colspan=1>-68.07</td><td rowspan=1 colspan=1>134.79</td><td rowspan=1 colspan=1>34.60</td><td rowspan=1 colspan=1>114.99</td><td rowspan=1 colspan=1>133.16</td><td rowspan=1 colspan=1>42.26</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>-545.98</td><td rowspan=1 colspan=1>409.48</td><td rowspan=1 colspan=1>-99.82</td><td rowspan=1 colspan=1>154.29</td><td rowspan=1 colspan=1>37.14</td><td rowspan=1 colspan=1>-70.22</td><td rowspan=1 colspan=1>126.54</td><td rowspan=1 colspan=1>38.13</td></tr></table>

4) Results for Orient. And Pow. Optimization (Method 2): While the previous strategy optimizes mutual interference across the map, we now evaluate the approach from Section V-B2 to enhance SIR in specific AOIs. This method reuses the Sionna coverage map and optimization parameters, adjusting only the initial learning rate $( l _ { r } = 0 . 0 5 )$ ) and setting the smooth minimum weighting temperature to $T = 2 5$

<sup>= 25</sup>To evaluate the benefits of the proposed approach, we analyze the cell-to-ABS association patterns before and after optimization with ${ \mathcal { L } } _ { w }$ method. Fig. 7 presents association maps where each cell is colored according to the ABS that provides the highest SIR (i.e., serving ABS) at that location. The association maps reveal several key improvements after optimization: (i) coverage regions become more homogeneous within each AOI, ensuring UEs in critical areas experience consistent service from their designated serving ABS; (ii) boundaries between different ABS coverage zones become more clearly defined, reducing potential handover instabilities; and (iii) ABSs outside

![](images/1a3875dafc6fa0bce7726bca206cb834c0c592e3d95afdb7ba89d0b36b8d7b4e.jpg)  
Fig. 7. Cell-to-ABS association showing SIR-based coverage dominance before (left) and after (right) orientation and power optimization using the $L _ { w }$ approach for sample scenario in Fig. 6(c). Each cell on the ground surface is colored according to the ABS experiencing the highest SIR at that location, demonstrating improved coverage allocation within AOIs and more defined service boundaries. Quantitative SIR improvements are detailed in Table VI (up to +12.98 dB gains) and validated through AODT time-series average measurements in Figure 9 (37ndash;20 dB improvements). Highlighted regions show AOIs with the most significant optimization impact.

AOIs appropriately adjust their radiation patterns to minimize interference within AOIs.

Table VI quantifies the SIR improvements achieved by the weighted AOI optimization $( \mathcal { L } _ { w } )$ for the sample scenario, showing substantial gains for serving ABSs in most AOIs (e.g., +11.51 dB for ABS 1in AOI 1, +9.57 dB for ABS 9 in AOI 2, and +5.17 dB for ABS 5 in AOI 4) and degradation of less than 0.5 dB for AOI 0 and AOI 3. Notably, the random baseline consistently degrades performance on average across all AOIs, with serving ABSs experiencing SIR losses ranging from −6.14 dB to −10.56 dB. This stark contrast demonstrates improvements of 8.18–17.65 dB achieved by our optimization over random parameter selection, with particularly strong gains in AOIs 1 and 2 (+17.65 dB and +15.73 dB respectively). Table VII extends this analysis across 50 different ABS deployments, confirming the robustness of the proposed approach. The average results show consistent positive gains for most AOIs (+12.98 dB, +10.01 dB, and +1.08 dB for AOIs 1, 2, and 4 respectively), with only modest reductions in AOIs 0 and 3 (−1.21 dB and −1.70 dB). Note that in some configurations the SIR gains might be lower due to multiple ABSs positioned within the same AOI, although the average values confirm that proposed approach is effective in keeping intra-AOI interference at minimal levels. These results validate that accurate power and orientation control are essential for efficient SIR management in autonomous ABS deployment, as random parameter selection leads to systematic performance degradation. The final configurations for the sample scenario are detailed in Table VIII for reproducibility, highlighting how serving ABSs are assigned higher power levels and fine-tuned orientations to enhance effective SIR in their respective AOIs.

## D. Computational Performance Evaluation for Practical Deployment

We note that real-time operation analysis is beyond the scope of this paper, which focuses on demonstrating the feasibility and effectiveness of multi-digital twin optimization frameworks for ABS deployment. Our empirical measurements reveal distinct performance characteristics for the two optimization phases:

Location Optimization: Achieves 0.0371 s per iteration using only TensorFlow compiled operations and geometric calculations (without differentiable ray tracing). For the experimental scenario with 5 AOIs and 10 ABSs, complete optimization converges in approximately 92.75 s with a maximum of 2500 iterations, though early stopping significantly reduces this in practice. The computational efficiency stems from our gradient-based approach using only geometric loss functions.

Orientation and Power Optimization: Gradient optimization via differentiable ray tracing (SionnaRT) incurs substantially higher computational costs. Each training iteration requires approximately 15 s in our experimental settings, even with GPU acceleration. The computational complexity scales with map size, number of ABSs, polygon count, ray count, and ray interaction limits. Nevertheless, this performance profile is well-suited for practical ABS deployment scenarios where:

1) Mission planning phase: Combined optimization time (typically 2-5 minutes) is acceptable for pre-mission deployment planning;

2) Adaptive repositioning: The algorithm can provide updated configurations during flight operations, as typical ABS battery life is 20-100 minutes [6];

3) Hierarchical deployment: Fast location optimization provides initial positioning and initial coverage, with orientation refinement performed as needed during realworld operations using the Digital Twins;

4) Scalability: Optimization time scales with scenario complexity, enabling faster solutions for smaller deployments.

Future performance improvements could be achieved through careful hyperparameter tuning and leveraging improved SionnaRT implementations, built solely on Mitsuba3/Dr.Jit instead of the current<sup>5</sup> Mitsuba+TensorFlow architecture and that allows sampling techniques such as Russian Roulette (RR) for more efficient Ray Tracing differentiation [39]. While real-time optimization presents interesting challenges for future work, the current framework demonstrates the foundational capability of multi-DT systems for autonomous ABS deployment optimization.

![](images/e8f808820e3bf5ed9fdb6395289f59d0a291968649a39e45498ae8c746353762.jpg)  
Fig. 8. Live capture of ABS configuration imported from Sionna to AODT. UEs placed in AOI 1 and rays shown for all ABSs and a sample UE.

1) Profiling Analysis: Profiling analysis using NVIDIA Nsight Systems revealed that the computational pipeline exhibits a nearly balanced distribution between GPU kernel execution (51.6%) and memory operations (48.4%), indicating that the application operates in a memory-bound regime where data movement overhead significantly impacts overall performance. This memory-to-computation ratio suggests that while the GPU cores are effectively utilized for mathematical operations, substantial execution time is consumed by host-device data transfers and GPU memory management operations. The predominance of memory operations presents both a performance bottleneck and an optimization opportunity, as memory transfer patterns are often more amenable to algorithmic improvements than pure computational limitations. Such a profile typically indicates potential for performance gains through strategies that minimize data movement, such as maintaining GPU-resident data structures across multiple computational phases, implementing asynchronous memory transfers overlapped with kernel execution, and consolidating operations to reduce the frequency of host-device communication. The near-equal distribution between computation and memory operations underscores the importance of considering data locality and transfer efficiency as primary factors in the optimization strategy, rather than focusing solely on computational algorithm improvements.

2) Gradient-Based Vs. Learning-Based Approach Rationale: Our gradient-based optimization approach is specifically designed for systems with complete environmental information obtained via Digital Twin simulations. As mentioned in Section II, unlike RL approaches that require extensive exploration and training, our method leverages the differentiable nature of the targeted Multi-DT system for direct optimization of wireless system parameters. RL-based approaches would introduce unnecessary computational overhead including data collection phases, model architecture exploration and training, and deployment complexity. Since our proposed Multi-DT framework provides complete environmental knowledge with differentiable propagation models, direct gradient optimization offers superior efficiency with immediate applicability to new scenarios without retraining requirements.

The 0.0371 s per iteration performance for location optimization and deterministic convergence properties demonstrate the practical advantages of leveraging complete environmental information over trial-and-error learning approaches.

## VI. CROSS-VALIDATION OF ABS DEPLOYMENT IN AODT

In this section, we validate ABS deployments obtained via Sionna optmization by measuring UE-perceived signal strength over time using AODT-generated Channel Impulse Responses (CIRs) for point-to-point communications. Each simulation runs for 60 s at a granularity of 1 s time steps, leveraging AODT’s procedural UE generation. We focus on validating the $\mathcal { L } _ { w }$ optimization approach for the scenario in Section V-C4 (see Table VIII for full parameters) by mapping each AOI to a spawn zone in AODT. Due to AODT 1.1.1 constraints, we define square spawn zones centered on each AOI with edge lengths $2 r _ { m }$ and collect measurements for a single AOI at a time. Each simulation deploys $U = 5 0$ UEs moving within their AOI. We configure AODT with simulation parameters matching Sionna (where applicable), i.e. $f _ { c } = 3 . 5$ GHz, ITU concrete material for surfaces, <sup>= 3 5</sup>TR 38.901<sup>6</sup> antenna pattern for ABSs, halfwave dipole for UEs, and 500K rays per ABS. To optimize efficiency, we assume only vertical polarization for ABS and UE antennas. ABS parameters (location, orientation, power) are exported from Sionna in JSON format, then imported into our modified AODT code, which also deploys spawn zones per AOI. UEs are initialized with fixed mechanical azimuth and tilt $\phi = \theta = 0 . 0$ . We conduct multi-UE simulations for each AOI, separately collecting CIR for downlink transmissions and location data for all ABSs and UEs at each simulation step, stored in an AODT database. Fig. 8 shows a screenshot of the imported configuration during a live simulation.

We compute the signal strength perceived between the u-th UE and i-th ABS at time step t as the sum the channel gains for every valid path<sup>7</sup> multiplied by the ABS’s transmission power computed during Sionna optimization phase: $P _ { t , i , u } ^ { \mathrm { r x } } =$ $\begin{array} { r } { P _ { i } ^ { \mathrm { t x } } \sum _ { r = 1 } ^ { N _ { r } } | h _ { r } | ^ { 2 } } \end{array}$ , where $h _ { r } \in \mathbb { C }$ is the complex channel gain for the r-th channel tap (or ray path) and $N _ { r }$ is the total number of valid paths. In order to compute the SIR based on the power perceived from all other ABSs in the map, we compute the total signal power $\begin{array} { r } { P _ { t , u } ^ { \mathrm { t o t } } = \sum _ { j = 1 , j \neq i } ^ { N } P _ { t , j , u } ^ { \mathrm { r x } } } \end{array}$ and then compute the SIR for each u-th UE given an ABS i and simulation time t as $\begin{array} { r } { \mathrm { S I R } _ { t , u } = \frac { P _ { t , i , u } ^ { \mathrm { r x } } } { P _ { t , u } ^ { \mathrm { t o t } } } } \end{array}$

Fig. 9 presents SIR measurements for each AOI and mobile user in AODT. The SIR values, averaged over 50 UEs per AOI, are computed using the serving ABS’s reference signal power, both before and after orientation and power optimization obtained via Sionna. The optimized parameters improve SIR in AOIs 1, 2, and 4, with gains between 3 and 20 dB. Conversely, AOIs 0 and 3, which already had high SIR, experience slight reductions, due to adjustments favoring AOIs with poorer SIR.

AOI 4 (Serving ABS=5)  
![](images/ed2f3cb7d9051a8f691266dabfda7012c246090dd5f44050ead5b0b224ea3b76.jpg)

![](images/e17a14d0934b42c5b586e90a8dc246c2029db317c53e137e280dd8cb05a94923.jpg)

AOI 2 (Serving ABS=9)  
![](images/5488d2c964713f20b9b10f1bf50e29a9979c9c5b61a01ed0730c557739b84d83.jpg)

![](images/e4085d98cbaf17a52bdd3fceee806ef66aa0e619ea8ea49472f3184af1e14870.jpg)

![](images/b2466b1ab0cc4b8b24b16432b7b04b35e48ebc0bb1735c5e376f7e9f7ba83f44.jpg)  
Fig. 9. SIR measured with AODT, averaged over 50 UEs moving within a given AOI, using ABSs’ parameters obtained before and after orientation and power optimization via Sionna.

However, their SIR remains sufficient for reliable communication, demonstrating how the framework’s provides solutions generalizable across multiple DTs considering real-world scenarios. Finally, Fig. 10 compares UEs’ channel gains from both DTs using identical simulation parameters (where applicable) for the first simulation frame, showing consistency between the tools and further validating the feasibility of the proposed approach.

![](images/dd93eccd666f71ff562a7dd447e51b0f039c79479e92868f19f595907cd54281.jpg)

![](images/59766caeb5c314abcf16ea86c351a9a49b4bc965aae2fa24f697c62d6826a74a.jpg)

![](images/b072fe60aa3e6b722094dafad4da26d928e195e2a8c18d5f9bdee0c1d74ea76b.jpg)

![](images/09d1a45feb73649e75014c5e4bcbf42cbfc58a8a93369456b5d82825fb215952.jpg)

![](images/64ecd15e6c9dd29c384756c715f610069b6ac314b1025a402b5270f02bbe27cd.jpg)  
Fig. 10. Comparison between receiver power measured at each UE in AODT and Sionna at Simulation Frame 0, using TR 38.901 antenna pattern at Transmitter (ABS) and halfwave dipole at Receiver (UE).

## VII. ABS DEPLOYMENT ADAPTATION FOR MISSION-CRITICAL SCENARIOS

We have seen how Sionna can be used to perform deployment optimizations for wireless devices to produce configurations validated via AODT. In this section, we explore a use case that reverse the data flow between the two DTNs to address mission-critical UEs’ severe coverage loss due to shadowing. We propose a threshold-based algorithm to detect signal drops in AODT simulations and adapt trajectory optimization methods via Sionna to adjust ABS parameters, improving UE signal power. Once critical UE paths are identified, they can be used to predict future issues, enabling DTNs to provide pre-computed recovery solutions or serve as training data for learning-based models.

![](images/6f8218d108ea10e04e84517977446496764c2a978a70c0a0750bba4822d01f3e.jpg)  
Fig. 11. Trajectory (blue) of ABS computed via gradient-descent for signal recovery of critical UE, projected over Sionna’s coverage map of initial ABS position (marked with a red cross). In the cutout: Trajectory of critical UE simulated in AODT (moving right to left).

## A. Signal Drop Detection

Assuming a single critical UE u and its associated ABS i, we compute the receive power $P _ { t , i , u } ^ { \mathrm { r x } }$ expressed in Watts (see Section VI) for every t-th simulation step, obtaining a power measurements array $\mathbf p _ { i , u } = [ P _ { 1 , i , u } ^ { \mathrm { r x } } , . . . , P _ { N _ { t } , i , u } ^ { \mathrm { r x } } ]$ , where $N _ { t }$ is the number of simulated steps. Using this information, we want to identify one or more sudden drops in signal coverage for any UE u that span several consecutive simulation steps, indicating its passage in shadowed areas such as narrow streets between tall buildings or other blocking entities. To this extent, we propose a threshold-based detection algorithm that works as follows:

1) Detection: Scans $p _ { i , u }$ for received power drops below a threshold $T _ { m i n }$

2) Confirmation: A drop is confirmed only if $c _ { m i n }$ consecutive measurements remain below $T _ { m i n }$

3) Spurious Peak Tolerance: Allows up to $s _ { p }$ temporary peaks above $T _ { m i n }$ before ending detection.

4) Finalization: If peaks exceed $s _ { p } ,$ records start (ts) and end $\left( t _ { e } \right)$ frames of the drop, computing its duration $T _ { d } =$ $t _ { e } - t _ { s }$

5) Repeat: Continues scanning $p _ { i , u }$ to detect further drops.

By adjusting parameters $T _ { m i n } , c _ { m i n }$ and $s _ { p } ,$ , we can define different levels of tolerance for the power threshold and granularity of the detection algorithm, depending on the level of reliability required.

## B. ABS Recovery Trajectory and Configuration

Once the power drops have been identified, for each drop interval we want to find a new configuration of the serving ABS that allows to improve the coverage conditions of critical UEs and provide more reliable communication. Once $( t _ { s } , t _ { e } )$

![](images/52d5f1a021afc4aeaeb95e0ccbd290f718619c52509537af018c550b37049781.jpg)  
Fig. 12. Signal drop recovery mechanism overview for mission-critical UE. The bar plots show the receive power computed via AODT perceived by the UE experiencing a signal drop before (above) and after (below) the recovery mechanism is activated.

drop start and end frames are obtained, we extract from AODT the relative critical UE consecutive $T _ { d }$ route positions in the map, indicated as $D _ { \mathrm { c } } = \{ d _ { t _ { s } } , d _ { t _ { s } + 1 } , . . . , d _ { t _ { e } } \}$ where each $\mathbf { \delta } _ { d _ { t } } ^ { d _ { t } }$ corresponds to the 2D x, y coordinate of UE at time t. The proposed recovery approach aims to (i) find a trajectory via gradient-based optimization from the deployment location of the ABS toward the critical UE experiencing the power drop and (ii) compute the new ABS coordinates to be applied during simulation for the recovery operation.

For the first goal, we first extract the UE’s route coordinate corresponding to the middle point of the drop interval, indicated as $d _ { m }$ at time $t _ { m }$ , assuming $t _ { s } < t _ { m } < t _ { e }$ . We then use $d _ { m }$ as destination point for the trajectory computation, based on the technique explained in Section V-A and optimized via the following simplified criteria:

$$
\mathcal { L } _ { d } = \| p _ { i } - \pmb { c } _ { k } \| + P _ { b }\tag{22}
$$

which aims to minimize the distance between the current ABS location and $d _ { m }$ while avoiding collisions with buildings through the computation of $P _ { b }$ penalty term. Once the destination is reached, we can employ the Sionna differentiable Ray Tacer to further refine the final recovery configuration, by optimizing its orientation and transmission power through one of the methods proposed in Section V-B.

Once the optimization converges towards the destination point and the trajectory point for each optimization iteration are obtained, we then compute the adjusted simulation coordinates by dividing the recovery operation in three distinct phases:

\- Reaction phase: We extract $\lfloor T _ { d } / 2 \rfloor$ equally distanced points from the trajectory obtained via the optimizer, corresponding to the locations that the ABS will have to follow while reacting to the signal drop detection in the $( t _ { s } , t _ { m } )$ simulation interval;

\- Stationary phase: in this phase we consider the ABS hovering over the critical UE route during the signal drop in the $( t _ { m } , t _ { e } )$ simulation steps, in order to improve the signal coverage for the remainder of the drop interval;

\- Return phase: Once the drop interval is concluded, the ABS is instructed to fly back to its original deployment location, until the next coverage loss is detected. To do so, it follows the same $\lfloor T _ { d } / 2 \rfloor$ coordinates from Reaction phase in reverse order.

Fig. 12 offers a visual overview of the recovery phases discussed above.

## C. Experimental Evaluation

To evaluate the proposed coverage drop detection and recovery mechanism, we consider a single ABS and one critical UE. Fig. 11 illustrates the targeted sample scenario, having an UE’s passing through buildings that cause signal blockages and an ABS positioned ∼ 320m away and hovering behind a tall obstacle. Over 60 time steps, the UE moves along this path while collecting power measurements. For this experiment, we set $T _ { \mathrm { m i n } } = 1 0 ^ { - 1 4 } \mathrm { W } , c _ { \mathrm { m i n } } = 3$ , and $s _ { p } = 5$ , using Adam optimizer with $l _ { r } = 6 . 0$ , early stopping (0.5 decay, patience  3). A signal drop is detected between $t _ { s } = 2 2$ and $t _ { e } = 4 4$ , triggering the recovery trajectory optimizer. After assigning trajectory points for recovery, accounting for obstacles, we re-run the same UE simulation including provided ABS mobility $\mathrm { p a t t e r n } ^ { 8 }$ and collect new power measurements. Fig. 12 visualizes the coverage throughout the simulation, indicating signal drop and recovery phases. The plots confirm up $\mathrm { t o } \sim 6$ orders of magnitude power improvement post-optimization via the second DTN, proving the proposed approach effective in dynamically enhancing signal converage for that specific UE.

## VIII. CONCLUSION AND FUTURE WORK

This work demonstrates the potential of using multiple Digital Twins (DTs) to perform complex cyber-physical simulations in the context of wireless communications. It focuses on optimizing and validating the deployment of Airborne Base Stations in urban settings, evaluating multiple goals and varying system conditions. Proposed solutions aim to highlight the flexibility of gradient-based optimization combined with Ray Tracing and detailed 3D geometries that can be potentially transferred to real-world environments. This paves the way for new kinds of studies for large-scale wireless systems, enabling innovative applications and solutions that combine the powerful simulation capabilities of modern DTNs and generate data fueling novel research.

The gradient-based Multi-DT approach demonstrates clear advantages over alternative methods by leveraging complete environmental information and differentiable system components, avoiding the computational overhead and training requirements of learning-based approaches while achieving superior performance metrics. Future research directions focus on addressing computational efficiency and enhancing deployment intelligence. The orientation and power optimization overhead could be significantly reduced through improved SionnaRT implementations built solely on Mitsuba3/Dr.Jit [39], enabling advanced sampling techniques such as Russian roulette and reducing the current 15-second per iteration time to real-time levels. Integration with Channel Knowledge Map (CKM) techniques [40], [41] represents another promising avenue, where CKM-derived channel predictions could provide intelligent initialization for gradient-based optimization, reducing convergence time from minutes to seconds while enabling hybrid approaches that use CKM for coarse positioning and high-fidelity ray tracing for critical parameters. The convergence of enhanced ray tracing performance and intelligent prior knowledge integration through bi-directional CKM-Multi-DT information flow could create self-improving systems that continuously refine environmental knowledge while adapting to real-time changes.

## REFERENCES

[1] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the sky: A tutorial on UAV communications for 5G and beyond,” Proc. IEEE, vol. 107, no. 12, pp. 2327–2375, Dec. 2019.

[2] B. Galkin, J. Kibiłda, and L. A. DaSilva, “A stochastic model for UAV networks positioned above demand hotspots in urban environments,” IEEE Trans. Veh. Technol., vol. 68, no. 7, pp. 6985–6996, Jul. 2019.

[3] V. Sharma, M. Bennis, and R. Kumar, “UAV-assisted heterogeneous networks for capacity enhancement,” IEEE Commun. Lett., vol. 20, no. 6, pp. 1207–1210, Jun. 2016.

[4] S. Kukli´nski, K. Szczypiorski, and P. Chemouil, “UAV support for mission critical services,” Energies, vol. 15, no. 15, 2022, Art. no. 5681. [Online]. Available: https://www.mdpi.com/1996-1073/15/15/5681

[5] A. Koubaa and B. Qureshi, “Dronetrack: Cloud-based real-time object tracking using unmanned aerial vehicles over the internet,” IEEE Access, vol. 6, pp. 13810–13824, 2018.

[6] “Top 17 long range drones of 2024 (5-200 km range),” 2024. Accessed: Feb. 19, 2025. [Online]. Available: https://www.t-drones.com/blog/longrange-drones.htm

[7] X. Lin, L. Kundu, C. Dick, E. Obiodu, T. Mostak, and M. Flaxman, “6G digital twin networks: From theory to practice,” IEEE Commun. Mag., vol. 61, no. 11, pp. 72–78, Nov. 2023.

[8] M. Mozaffari, X. Lin, and S. Hayes, “Toward 6G with connected sky: UAVs and beyond,” IEEE Commun. Mag., vol. 59, no. 12, pp. 74–80, Dec. 2021.

[9] R. M. Rolly, P. Malarvezhi, and T. D. Lagkas, “Unmanned aerial vehicles: Applications, techniques, and challenges as aerial base stations,” Int. J. Distrib. Sensor Netw., vol. 18, no. 9, 2022, Art. no. 15501329221123933. [Online]. Available: https://doi.org/10.1177/15501329221123933

[10] M. M. Islam, M. T. R. Khan, M. M. Saad, M. A. Tariq, and D. Kim, “Dynamic positioning of UAVs to improve network coverage in VANETs,” Veh. Commun., vol. 36, no. C., Aug. 2022, Art. no. 100498. [Online]. Available: https://doi.org/10.1016/j.vehcom.2022.100498

[11] Z. Yao, W. Cheng, W. Zhang, and H. Zhang, “Resource allocation for 5G-UAV-based emergency wireless communications,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3395–3410, Nov. 2021.

[12] H. Zhang et al., “Autonomous navigation and configuration of integrated access backhauling for UAV base station using reinforcement learning,” in Proc. IEEE Future Netw. World Forum (FNWF), 2022, pp. 184–189.

[13] S. A. Al-Ahmed, M. Z. Shakir, and S. A. R. Zaidi, “Optimal 3D UAV base station placement by considering autonomous coverage hole detection, wireless backhaul and user demand,” J. Commun. Netw., vol. 22, no. 6, pp. 467–475, Dec. 2020.

[14] O. Bouhamed, H. Ghazzai, H. Besbes, and Y. Massoud, “A UAV-assisted data collection for wireless sensor networks: Autonomous navigation and scheduling,” IEEE Access, vol. 8, pp. 110446–110460, 2020.

[15] G. Shen et al., “Deep reinforcement learning for flocking motion of multi-UAV systems: Learn from a digital twin,” IEEE Internet Things J., vol. 9, no. 13, pp. 11141–11153, Jul. 2022.

[16] D. Romero, P. Q. Viet, and R. Shrestha, “Aerial base station placement via propagation radio maps,” IEEE Trans. Commun., vol. 72, no. 9, pp. 5349–5364, Sep. 2024.

[17] H. Ahmadi, A. Nag, Z. Khar, K. Sayrafian, and S. Rahardja, “Networked twins and twins of networks: An overview on the relationship between digital twins and 6G,” IEEE Commun. Standards Mag., vol. 5, no. 4, pp. 154–160, Dec. 2021.

[18] N. Apostolakis, L. E. Chatzieleftheriou, D. Bega, M. Gramaglia, and A. Banchs, “Digital twins for next-generation mobile networks: Applications and solutions,” IEEE Commun. Mag., vol. 61, no. 11, pp. 80–86, Nov. 2023.

[19] T. Li, S. Leng, X. Liao, and Y. Zhang, “Digital twin-based task-driven resource management in intelligent UAV swarms,” IEEE Trans. Intell. Transp. Syst., vol. 26, no. 4, pp. 5467–5480, Apr. 2025.

[20] L. Lei, G. Shen, L. Zhang, and Z. Li, “Toward intelligent cooperation of UAV swarms: When machine learning meets digital twin,” IEEE Netw., vol. 35, no. 1, pp. 386–392, Jan./Feb. 2021.

[21] C. Cimino, G. Ferretti, and A. Leva, “Harmonising and integrating the digital twins multiverse: A paradigm and a toolset proposal,” Comput. Ind., vol. 132, 2021, Art. no. 103501. [Online]. Available: https://www. sciencedirect.com/science/article/pii/S0166361521001081

[22] Z. Yun and M. F. Iskander, “Ray tracing for radio propagation modeling: Principles and applications,” IEEE Access, vol. 3, pp. 1089–1100, 2015.

[23] J. Hoydis et al., “Sionna rt: Differentiable ray tracing for radio propagation modeling,” in Proc. IEEE Globecom Workshops (GC Wkshps), 2023, pp. 317–321.

[24] NVIDIA, “Aerial omniverse digital twin,” https://developer.nvidia.com/ aerial-omniverse-digital-twin, 2024, Accessed: 2024-10-9.

[25] ns-3 Consortium, “NS-3 network simulator,” Accessed: Jan. 31, 2025. [Online]. Available: https://www.nsnam.org/

[26] A. Varga, “Omnet,” in Modeling and Tools for Network Simulation, K. M. W. Güne¸s and J. Gross, Eds. Berlin, Germany: Springer, 2010, pp. 35–59. [Online]. Available: https://doi.org/10.1007/978-3-642-12331-3\_3

[27] Remcom Inc., “Wireless InSite: 3D wireless prediction software,” Accessed: Jan. 31, 2025. [Online]. Available: https://www.remcom.com/ wireless-insite-em-propagation-software

[28] ANSYS Inc., “ANSYS HFSS: High frequency structure simulator,” Accessed: Jan. 31, 2025. [Online]. Available: https://www.ansys.com/ products/electronics/ansys-hfss

[29] J. Hoydis et al., “Sionna: An open-source library for next-generation physical layer research,” 2022, arXiv:2203.11854.

[30] M. Abadi et al., “ {TensorFlow }: A system for { Large-Scale} machine learning,” in Proc. 12th USENIX Symp. Operating Syst. Des. Implementation (OSDI 16), 2016, pp. 265–283.

[31] “Mitsuba 3 - a retargetable forward and inverse renderer,” Accessed: Oct. 9, 2024. [Online]. Available: https://www.mitsuba-renderer.org 2024.

[32] W. Jakob, S. Speierer, N. Roussel, and D. Vicini, “Dr. Jit: A just-in-time compiler for differentiable rendering,” ACM Trans. Graph., vol. 41, no. 4, pp. 1–9, Jul. 2022. [Online]. Available: https://doi.org/10.1145/3528223. 3530099

[33] “NVIDIA aerial CUDA-accelerated ran,” Accessed: Oct. 9, 2024. [Online]. Available: https://developer.nvidia.com/aerial-cuda-accelerated-ran

[34] M. Zhu, L. Cazzella, F. Linsalata, M. Magarini, M. Matteucci, and U. Spagnolini, “Toward real-time digital twins of EM environments: Computational benchmark for ray launching software,” IEEE Open J. Commun. Soc., vol. 5, pp. 6291–6302, 2024.

[35] “Project plateau| the initiative of digital twin in Japan,” Accessed: Oct. 13, 2024. [Online]. Available: https://www.mlit.go.jp/en/toshi/daisei/ plateau\_en\_2.html

[36] M. M. Noel, “A new gradient based particle swarm optimization algorithm for accurate computation of global minimum,” Appl. Soft Comput., vol. 12, no. 1, pp. 353–359, 2012. [Online]. Available: https://www.sciencedirect. com/science/article/pii/S1568494611003206

[37] “3GPP TR 38.901, “study on channel model for frequencies from 0.5 to 100 GHz,” release 16.1,” 2021. Accessed: Jan. 2, 2025. [Online]. Available: https://www.etsi.org/deliver/etsi\_tr/138900\_138999/138901/16.01. 00\_60/tr\_138901v160100p.pdf

[38] ITU-R, “effects of building materials and structures on radiowave propagation above about 100 MHz,” recommendation ITU-R P, 2040-3,” 2023. Accessed: Jan. 2, 2025. [Online]. Available: https://www.itu.int/ dms\_pubrec/itu-r/rec/p/R-REC-P.2040-3-202308-I!!PDF-E.pdf

[39] J. Hoydis et al., “Sionna RT: Differentiable ray tracing for radio propagation modeling,” in Proc. IEEE Globecom Workshops (GC Wkshps), Kuala Lumpur, Malaysia, 2023, pp. 317–321, doi: 10.1109/GCWkshps58843.2023.10465179.

[40] Y. Yang, X. Xu, Y. Zeng, H. Sun, and R. Q. Hu, “Channel knowledge map for cellular-connected uav via binary bayesian filtering,” IEEE Trans. Commun., early access, Mar. 25, 2025, doi: 10.1109/TCOMM.2025.3554681.

[41] K. Li, P. Li, Y. Zeng, and J. Xu, “Channel knowledge map for environmentaware communications: EM algorithm for map construction,” in Proc. 2022 IEEE Wireless Commun. Netw. Conf. (WCNC), 2022, pp. 1659–1664.

![](images/d28a5e4f5b2fe6456cf1c029a70171285f95173bcb9016ec8b58625d88691d32.jpg)  
Mauro Belgiovine received the PhD degree in computer engineering with Northeastern University Boston, MA in 2025 under the guidance of prof. Kaushik Chowdhury. He joined NVIDIA full-time in 2025 to continue his research on deep learning applications to wireless communication, digital twins, semantic communications, and generative AI.

![](images/20811c014a87e20f55f723bdaefa7dc7ae68102c748ce6538fcff757bfc652e5.jpg)

Chris Dick (Senior Member, IEEE) is currently a wireless architect with NVIDIA and the technical lead for the application of AI and machine learning to 5G and 6G wireless. In more than 24 years working in signal processing and communications, he has delivered silicon and software products for 3G, 4G, and 5G baseband DSP and Docsis 3.1 cable access. He has performed research and delivered products for digital frontend (DFE) technology for cellular systems.

![](images/bdee68f301760a0fdd245ddad34bb3ed439cd7c1d15eee7428275e4236001dcd.jpg)

Kaushik Chowdhury (Fellow, IEEE) is currently a chandra family endowed distinguished professor in electrical and computer engineering with The University of Texas at Austin. His research interests include systems aspects of machine learning for agile spectrum sensing/access, autonomous systems, programmable and open cellular networks, and large scale experimental deployment of emerging wireless technologies.