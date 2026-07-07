# Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks

Wen-Yu Dong, Song Zhao, Rui-Si Han, Qi Bi, Fellow, IEEE, Sheng Chen, Life Fellow, IEEE

Abstract—The emergence of high-frequency pulsating logistics unmanned aerial vehicle (UAV) swarms gives rise to “Digital Tides”, i.e., complex traffic dynamics that challenge sustainable resource provisioning in mobile computing networks. Conventional infrastructure provisioning strategies, which typically rely on static snapshot-based analysis and localized density estimation, fail to capture the macroscopic advection of computational workloads. As a result, reactive resource activation suffers from inherent hysteresis, yielding nominal efficiency gains at the cost of mission-critical service loss at the advancing wavefront. To address this issue, we develop a fluid-based spatiotemporal framework by explicitly solving the continuity equation to characterize the macroscopic velocity field of the workload flow. Building on this framework, we propose a flux-aware asymmetric activation strategy that leverages the derived information flux vector as a kinematic precursor of demand propagation. Unlike symmetric thresholding, the proposed control logic decouples activation and deactivation dynamics. Theoretical analysis confirms the intrinsic spatial phase-lead of the flux signal and shows that the proposed strategy generates a proactive guard ring to compensate for service setup latency, including delays caused by mobile edge computing container cold-starts. We further derive closed-form expressions for instantaneous service availability and periodaverage energy efficiency. In addition, we formulate a qualityof-service-penalized metric to evaluate effective energy efficiency under strict outage constraints. Numerical results show that the proposed flux-driven strategy enables zero-latency tracking of the mobile wavefront and achieves a Pareto-optimal trade-off between service reliability and energy consumption, outperforming reactive baselines in dynamic logistics corridors.

Index Terms—Digital Tides, UAV logistics, fluid-dynamic modeling, infrastructure provisioning, information flux.

## I. INTRODUCTION

hicles (UAVs) for food delivery, medical transport, etc. is reshaping the low-altitude economy, establishing aerial mobile computing as a cornerstone of future autonomous systems [1–4]. Unlike terrestrial users with stochastic mobility, logistics UAVs exhibit highly structured macroscopic flow patterns driven by on-demand delivery cycles. This creates a phenomenon we term the low-altitude digital tide, a pulsating traffic pattern where swarms periodically disperse from distribution centers and return to base. This tidal traffic pattern involves two critical kinematic phases: the expansion phase where the spatial footprint of the swarm grows rapidly, and the contraction phase where the swarm recedes. Supporting this complex tidal traffic poses a significant energy challenge. Ground infrastructures, such as mobile edge computing (MEC)-enabled base stations (BSs), typically employ alwayson service interfaces to guarantee availability. Given that infrastructure provisioning accounts for over 80% of network energy consumption [5], maintaining idle computing resources during the tide’s ebb periods fundamentally contradicts the sustainability goals of mobile computing systems.

Simply applying conventional energy-saving strategies to this scenario creates a critical reliability conflict. Existing methods, often rooted in static snapshot-based analysis [6– 8], predominantly rely on detecting local workload density. While effective for stationary hotspots, this static perspective is inherently ill-suited for the application scenario considered. The core failure mechanism lies in the mismatch between the resource provisioning speed and the workload advection speed. Specifically, as a UAV swarm propagates outward, it forms a rapidly moving demand wavefront. However, due to the inevitable service setup latency specified by the necessary transition time from sleep to active mode, including MEC container cold-starts, a node triggered solely by local density will activate too late, often after the leading UAVs have already entered its service area. This hysteresis results in a wavefront outage, creating a moving service void that compromises the reliability of mission-critical logistics operations.

While data-driven prediction methods attempt to mitigate this lag, they often incur prohibitive computational overheads for training and lack the generalizability to handle emergent swarm behaviors. To overcome this latency-induced failure, resource orchestration must shift from observing static snapshots to predicting dynamic workload flows. This paper introduces a fluid-dynamic provisioning framework for sustainable mobile computing infrastructure. Instead of restricting the analysis to independent static realizations common in traditional stochastic modeling, we model the logistics swarm as a continuous compressible fluid governed by conservation laws [9–11]. This allows us to derive an information-flux vector field that quantifies the momentum of computational demand. Moreover, unlike the scalar density, which peaks only upon arrival, the flux vector naturally points in the direction of flow and reaches its threshold ahead of the density peak. By exploiting this intrinsic kinematic phase lead, our strategy effectively generates a time buffer, waking up infrastructure resources just-in-time to reliably serve the incoming wavefront.

This article has been accepted for publication in IEEE Transactions on Mobile Computing. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/TMC.2026.3688690

## A. Related Works

Research on energy efficiency (EE) in non-terrestrial networks (NTNs) primarily focuses on two optimization domains: aerial agents and terrestrial infrastructure. The majority of existing literature prioritizes UAV endurance, extensively exploring joint trajectory design and power control to minimize propulsion and operational energy consumption [12, 13]. Conversely, studies focusing on terrestrial networks typically exploit UAVs as aerial edge nodes to offload workloads, thereby enabling ground BSs (GBSs) to enter sleep modes [14, 15]. However, the reciprocal challenge—optimizing the energy consumption of ground infrastructure dedicated to serving high-density aerial logistics—has received limited attention. Although early works such as [16] investigated GBS sleeping for UAV command and control, they relied on static access techniques like coordinated multi-point and non-orthogonal multiple access. These approaches treat aerial workloads as stationary spatial distributions, failing to capture the macroscopic advection inherent in logistics tides. Consequently, they lack the predictive capability necessary to compensate for service setup latency.

Adapting dynamic resource-scaling strategies from terrestrial mobile networks offers a potential solution. These strategies are generally categorized into robust optimization and learning-based prediction. Robust optimization frameworks, such as chance-constrained programming [17], address workload uncertainty via statistical moments. While robust against random fluctuations in stationary terrestrial clients, these methods typically adopt a discrete time-slotted perspective, which lacks the temporal resolution required to track a rapidly propagating demand wavefront. This leads to inherent hysteresisinduced outages. Similarly, data-driven paradigms, including long short-term memory (LSTM) networks [18–20] and deep reinforcement learning (DRL) [21], depend on continuous workload observability, a condition unavailable to sleeping nodes. Furthermore, these models often lack the physical generalizability required to handle emergent swarm behaviors on unseen logistics routes [21].

The ineffectiveness of adapting the aforementioned terrestrial strategies to the logistics UAV swarm context is fundamentally rooted in their mathematical modeling of system workload. Standard stochastic geometry analysis [22–25], widely adopted to derive EE limits in mobile networks, relies heavily on the snapshot assumption, treating network evolution as a sequence of independent static realizations. Although advances in spatio-temporal stochastic geometry have begun to address temporal interference correlations [26–28], these frameworks predominantly focus on stationary users or random waypoint mobility. They inherently lack the capability to capture the structured macroscopic advection characteristic of logistics tides. Consequently, such static modeling frameworks fail to provide the kinematic foresight needed to preemptively overcome service setup latency.

To address the limitations of discrete agent modeling, fluid dynamic models were proposed to capture macroscopic mobility patterns [9–11]. Similarly, mean field games were employed to mathematically formalize the interactions of massive

UAV agents as a continuum [29–31]. However, these works primarily focus on distributed trajectory optimization or power control, leaving the coupled dynamics between macroscopic workload flow and ground resource activation unexplored. Prior studies [9, 10] utilized the fluid principles for capacity estimation or trajectory synthesis. These contributions, however, remain largely descriptive rather than prescriptive. A critical gap persists in mapping continuous kinematic metrics, such as flow velocity and flux, to the discrete switching dynamics of resource activation. Mitigating service setup latency [32] in high-mobility corridors remains an open engineering challenge. This limitation leads to a deceptive reliability-efficiency trade-off, where reactive strategies achieve misleadingly high nominal EE by systematically shedding the energy-intensive demand wavefront. To bridge this gap, we propose a fluidbased spatiotemporal framework that leverages information flux as a kinematic precursor. Unlike reactive strategies limited by snapshot-based inputs, our approach proactively compensates for service setup latency by aligning network activation with the macroscopic momentum of the digital tide.

## B. Our Contributions

Our main contributions are summarized as follows.

• We establish a fluid-dynamic traffic model governed by conservation laws to characterize the pulsating dynamics of logistics UAV swarms. By explicitly solving the continuity equation, we derive the closed-form macroscopic velocity field. This continuous formulation overcomes the static limitations of classical stochastic modeling, establishing a fluid-based spatiotemporal framework that captures the cumulative spatiotemporal workload volume for evaluating non-stationary infrastructure sustainability.

• We propose a flux-aware asymmetric activation strategy that bridges the gap between macroscopic flow dynamics and discrete resource states. Identifying the information flux vector as a kinematic precursor for demand momentum, the proposed control logic exploits the intrinsic spatial phase-lead at the wavefront. This mechanism generates a proactive guard ring that effectively compensates for service setup latency, thereby enabling zero-latency tracking of the expanding demand wavefront.

• We develop a tractable analytical framework to quantify system performance, deriving closed-form expressions for the instantaneous service availability and period-average EE. To resolve the deceptive reliability-efficiency tradeoff suffered by existing strategies, we formulate a quality of service (QoS)-penalized effective EE metric. Guided by this metric, we demonstrate that the proposed strategy can be calibrated to identify the Pareto-optimal operating point, effectively decoupling the conflict between energy conservation and service reliability.

This paper is organized as follows. Section II introduces the fundamental concepts of digital tides and motivates the adoption of the fluid-dynamic paradigm. Section III establishes the system model, formulates the low-altitude digital tide using fluid dynamics and introduces the hardware constraints. Section IV details the flux-aware asymmetric activation strategy. Section V provides the theoretical performance analysis, deriving the resource activation geometry, service availability, and EE, alongside the proof of the flux phaselead property. Section VI presents numerical results, validating the analytical models and quantifying the performance gains regarding outage elimination and Pareto optimality. Section VII discusses the practical limitations and the generalizability of the proposed framework under non-ideal conditions. Finally, Section VIII concludes the paper.

TABLE I  
SUMMARY OF KEY MATHEMATICAL NOTATIONS
<table><tr><td>Symbol</td><td>Description</td></tr><tr><td> $\Phi _ { \mathrm { B S } } , \lambda _ { \mathrm { B S } }$ </td><td>PPP and density of GBSs</td></tr><tr><td> $H _ { \mathrm { U A V } }$ </td><td>Operational altitude of logistics UAVs</td></tr><tr><td> $P _ { \mathrm { a c t } } , P _ { \mathrm { s l p } }$ </td><td>Active and sleep power consumption of the LAS module</td></tr><tr><td> $\nu , \gamma$ </td><td>Path loss exponent and SINR threshold</td></tr><tr><td> $B , \eta _ { \mathrm { S E } }$ </td><td>Bandwidth and target spectral efficiency</td></tr><tr><td> $\lambda ( r , t )$ </td><td>Spatio-temporal workload density at distance r and time t</td></tr><tr><td> $N ( t )$ </td><td>Total workload demand</td></tr><tr><td> $\sigma ( t ) , \dot { \sigma } ( t )$ </td><td>Spatial spread parameter and its expansion rate</td></tr><tr><td> $N _ { 0 } , \sigma _ { 0 }$ </td><td>Baseline workload intensity and spatial spread</td></tr><tr><td> $\delta _ { N } , \delta _ { \sigma }$ </td><td>Load modulation index and spatial expansion index</td></tr><tr><td> $v _ { r } ( r , t )$ </td><td>Macroscopic radial expansion velocity</td></tr><tr><td> $\alpha ( \mathbf { x } , t )$ </td><td>Binary activation state of a GBS at location x</td></tr><tr><td> $\Phi ( \mathbf { x } , t )$ </td><td>Information flux vector quantifying demand momentum</td></tr><tr><td> $R _ { \mathrm { w f } } ( t )$ </td><td>Logistic wavefront position</td></tr><tr><td> $\lambda _ { \mathrm { a c t } } , \lambda _ { \mathrm { h o l d } }$ </td><td>Static activation and holding density thresholds</td></tr><tr><td> $\delta _ { \mathrm { t h } }$ </td><td>Flux sensitivity threshold</td></tr><tr><td> $\tau _ { \mathrm { b o o t } }$ </td><td>Service setup latency</td></tr><tr><td> $R _ { \mathrm { a c t i v e } } ( t )$ </td><td>Effective activation radius of the network</td></tr><tr><td> $\mathcal { G } _ { \mathtt { f l u x } }$ </td><td>Spatial flux gain</td></tr><tr><td> $\mathcal { T } _ { \mathrm { t o t a l } } , E _ { \mathrm { t o t a l } }$ </td><td>Total served workload volume and energy consumption</td></tr><tr><td> $\eta _ { \mathrm { E E } } , \eta _ { \mathrm { e f f } }$ </td><td>Raw energy efficiency and effective energy efficiency</td></tr></table>

Throughout this paper, $\mathbb { P } ( \cdot )$ and <sup>E</sup>[·] denote the probability and expectation operators, respectively. <sup>I</sup>(·) denotes the indicator function, which equals 1 if the condition inside is true, and 0 otherwise. $\mathcal { L } _ { I } ( s ) = \mathbb { E } [ e ^ { - s I } ]$ is the Laplace transform of the interference I. The probability density function (PDF) of random variable X is denoted by $f _ { x } ( x ) . ~ { _ 2 F _ { 1 } } ( a , b ; c ; z ) =$ $\begin{array} { r } { \sum _ { n = 0 } ^ { \infty } { \frac { ( a ) _ { n } ( b ) _ { n } } { ( c ) _ { n } n ! } } z ^ { n } } \end{array}$ is the standard mathematical notation for the Gaussian hypergeometric function, and $[ \cdot ] ^ { + } \triangleq \operatorname* { m a x } \{ 0 , \cdot \}$ For easy reference, Table I summarizes the key symbols used in this paper.

## II. BACKGROUND AND MOTIVATION

To establish the physical intuition behind the proposed methodology, this section introduces the fundamental concepts of digital tides and clarifies the motivation for adopting a fluiddynamic perspective.

## A. From Stochastic Mobility to Digital Tides

Traditional mobile networks are primarily designed to accommodate independent users with stochastic mobility patterns, such as random waypoint or Brownian motion. Under such microscopic randomness, the aggregate spatial distribution of users remains statistically stationary over short time scales.

However, the deployment of logistics UAV swarms introduces a distinct macroscopic dynamic. Governed by centralized scheduling and delivery deadlines, these swarms exhibit structured macroscopic flow patterns rather than isolated random walks. When a logistics hub dispatches a wave of delivery UAVs, it creates a pulsating traffic surge propagating outward, which we conceptualize as a digital tide. Serving this tide requires the ground infrastructure to activate and deactivate synchronously with the swarm propagation.

## B. Limitations of Reactive Density Detection

Evaluating dynamic infrastructure activation requires an accurate characterization of the spatial workload. Conventional resource provisioning strategies, often modeled via static stochastic geometry, predominantly rely on localized density detection. This approach triggers BSs by independently observing the instantaneous spatial accumulation of users.

While effective for stationary hotspots, the static density metric lacks predictive capability regarding macroscopic mobility. Specifically, a BS relying on local density detection initiates its activation sequence only after the swarm enters its coverage area. Given the service setup latency associated with hardware wake-up and MEC container cold-starts, this reactive detection creates a temporal lag. Consequently, the leading edge of the swarm, namely, the mission-critical wavefront, experiences significant service outages.

## C. The Fluid-Dynamic Paradigm and Information Flux

To overcome the hysteresis in reactive control, the infrastructure must anticipate the arrival of the demand. This requires a shift in mathematical abstraction from discrete static agents to a continuous dynamic flow. By modeling the dense UAV swarm as a compressible fluid governed by the continuity equation, we analytically define the macroscopic velocity field of the traffic.

Building upon this fluid-dynamic foundation, we introduce the concept of information flux. Defined as the product of the scalar spatial density and the macroscopic velocity vector, the flux encapsulates the momentum of the service demand. The physical motivation for utilizing this metric lies in its spatial phase-lead property. At the expanding wavefront, the macroscopic velocity increases the flux signal, allowing it to reach detection thresholds at greater distances compared to the static density. By exploiting this kinematic property, the network generates a proactive guard ring, reserving the required time buffer to execute MEC cold-starts before the physical workload arrives.

## III. SYSTEM MODEL AND PROBLEM FORMULATION

Fig. 1 illustrates an MEC-enabled urban logistics network driven by a pulsating logistics tide, which is conceptualized as a macroscopic spatiotemporal field of traffic density that undergoes periodic, radial expansion and contraction.

## A. Network Architecture

1) Logistics Hub and UAV Kinematics: The system serves a centralized logistics area $\mathcal { A } \subset \mathbb { R } ^ { 2 }$ , targeting scenarios such as food delivery or medical transport. A logistics hub is located at the origin of A, serving as the source and sink of the UAV swarm. UAVs operate at a constant altitude $H _ { \mathrm { U A V } }$ Unlike stochastic mobility models, such as random waypoint, the aggregate swarm kinematics exhibit a deterministic macroscopic structure: a radial velocity field driven by the periodic waves of delivery demand.

![](images/1934d8c7a4fa9f23da9a3318d28c430cacdc0871b89128db2aae90818a0f7657.jpg)  
Fig. 1. System model of the MEC-enabled UAV logistics network.

2) Ground Infrastructure and Hardware Constraints: The ground network comprises cellular BSs deployed according to a homogeneous Poisson point process (PPP) $\Phi _ { \mathrm { B S } }$ with density $\lambda _ { \mathrm { B S } }$ . To balance ubiquitous coverage reliability with high-capacity throughput requirements, we adopt a dual-layer heterogeneous architecture consisting of: 1) the terrestrial sector layer, where existing down-tilted sectors remain alwaysactive to provide basic command and control links via antenna sidelobes; and 2) the low-altitude sector (LAS) layer, where BSs are equipped with dedicated up-tilted modules utilizing orthogonal frequency resources for high-bandwidth computational task offloading.

In this framework, we adopt an MEC architecture where each GBS is equipped with an edge server to handle latencysensitive logistics tasks, such as visual navigation and path planning. Given that the radio unit and the edge computing module share a power supply and control interface, their activation is synchronized. Accordingly, the service setup latency $\tau _ { \mathrm { b o o t } }$ is modeled as the aggregate of the radio frequency circuit wake-up time and the MEC container cold-start delay, which includes the time needed to instantiate virtual machines and load service images.

This work focuses on the energy-efficient activation control of the power-consuming LAS layer. Consistent with analytical models for infrastructure sleep depth [32], we incorporate the activation latency $\tau _ { \mathrm { { b o o t } } }$ to account for the non-instantaneous transition from sleep to active mode. This imposes a timing constraint on the network control: to guarantee service availability at time t, the activation decision $\alpha ( \mathbf { x } , t )$ must be asserted at or before $t - \tau _ { \mathrm { b o o t } }$ . The specific design of the fluxaware control logic satisfying this constraint will be detailed in Section IV.

## B. Fluid-Dynamic Workload Modeling

To capture the macroscopic mobility of the UAV swarm, we model the traffic as a compressible fluid driven by logistics demand.

1) Density Field Formulation: We model the instantaneous mobile agent density $\lambda ( r , t )$ at distance r and time t as a timevarying, non-separable Gaussian field:

$$
\lambda ( r , t ) = \frac { N ( t ) } { 2 \pi \sigma ^ { 2 } ( t ) } \exp \left( - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } ( t ) } \right) .\tag{1}
$$

To explicitly capture the periodicity, we model the load $N ( t )$ and spread $\sigma ( t )$ as sinusoidal functions with period T<sub>period</sub>:

$$
N ( t ) = N _ { 0 } \left( 1 + \delta _ { N } \cos ( \omega t ) \right) ,\tag{2}
$$

$$
\sigma ( t ) = \sigma _ { 0 } \left( 1 + \delta _ { \sigma } \cos ( \omega t + \varphi ) \right) ,\tag{3}
$$

where $N _ { 0 }$ and $\sigma _ { 0 }$ are the baseline workload intensity and spatial spread, respectively, $\delta _ { N }$ and $\delta _ { \sigma }$ are the workload modulation index and spatial expansion index, while $\omega =$ $2 \pi / T _ { \mathrm { p e r i o d } }$ is the angular frequency, and $\varphi$ accounts for the phase synchronization offset between traffic generation and spatial expansion.

2) Macroscopic Velocity and Information Flux: Governed by the law of conservation of mass, the evolution of the density field $\boldsymbol { \lambda } ( \mathbf { x } , t )$ at position $\mathbf { x } \in \mathbb { R } ^ { 2 }$ and time t adheres to the continuity equation:

$$
\frac { \partial \lambda } { \partial t } + \nabla \cdot ( \lambda \mathbf { v } ) = 0 ,\tag{4}
$$

where $\mathbf { v } ( { \bf x } , t )$ is the macroscopic velocity field. By solving this equation (see Section S-I of the Supplementary File), we derive the radial expansion velocity of the logistics tide as $\begin{array} { r } { v _ { r } ( r , t ) \approx r \frac { \dot { \sigma } ( t ) } { \sigma ( t ) } } \end{array}$ , where $r = \| \mathbf { x } \|$ is the radial distance from the logistics hub.

Remark 1. The derivation in Section S-I reveals that the macroscopic flow is governed by two orthogonal forces: 1) source dynamics driven by load variation N<sup>˙</sup> , representing a “fictitious velocity” required to accommodate node creation or removal; and 2) transport dynamics driven by spatial reshaping σ˙ . In high-mobility logistics scenarios, the kinematic transport dominates the source variation, i.e., $| \dot { \sigma } / \sigma | \gg | \dot { N } / N |$ This dominance ensures that the flow physically manifests as a uniform expansion rather than a localized fluctuation, thereby validating the use of the linear velocity model $v _ { r } \propto r$ for proactive control.

Based on this kinematic description, we introduce the information flux to quantify the momentum of service demand.

Definition 1. The information flux, denoted by $\Phi ( \mathbf { x } , t )$ , is a vector field representing the rate of traffic demand flow passing through a unit spatial cross-section. Mathematically, it is defined as the product of the scalar spatio-temporal user density $\boldsymbol { \lambda } ( \mathbf { x } , t )$ and the macroscopic velocity vector $\mathbf { v } ( \mathbf { x } , t ) .$

$$
\Phi ( \mathbf { x } , t ) \triangleq \lambda ( \mathbf { x } , t ) \mathbf { v } ( \mathbf { x } , t ) \approx \lambda ( r , t ) \left( r \frac { \dot { \sigma } ( t ) } { \sigma ( t ) } \right) \mathbf { e } _ { r } ,\tag{5}
$$

where ${ \bf e } _ { r } = { \bf x } / \| { \bf x } \|$ is the unit radial vector pointing outwards from the $o r i g i n .$

This vector formulation offers a critical physical insight that cannot be obtained from scalar density alone. While $\boldsymbol { \lambda } ( \mathbf { x } , t )$ merely measures the static accumulation of load, $\Phi ( \mathbf { x } , t )$ quantifies the dynamic trend of the demand momentum. The magnitude ∥Φ∥ is amplified by the expansion velocity $v _ { r } ,$ which scales linearly with distance r. At the expanding wavefront where r is large, the flux intensity reaches its detection threshold before the workload density accumulates to the activation level. This kinematic property creates a spatial phase lead, serving as a predictive indicator for proactive activation.

3) Logistic Wavefront: We define the logistic wavefront, denoted as $R _ { \mathrm { w f } } ( t )$ , as the spatial boundary where the user density decays to the minimum service threshold λ :

$$
R _ { \mathrm { w f } } ( t ) \triangleq \left\{ r \in \mathbb { R } ^ { + } : \lambda ( r , t ) = \lambda _ { \mathrm { t h } } \right\} .\tag{6}
$$

Physically, $R _ { \mathrm { w f } } ( t )$ delineates the effective edge of the serving swarm. To quantify its propagation dynamics, we define the wavefront phase velocity as the time derivative of the wavefront position:

$$
v _ { \mathrm { w f } } ( t ) \triangleq \frac { \mathrm { d } R _ { \mathrm { w f } } ( t ) } { \mathrm { d } t } .\tag{7}
$$

During the expansion phase where $\dot { \sigma } \ > \ 0 .$ , this wavefront propagates outward with a positive velocity $v _ { \mathrm { w f } } ( t ) > 0 . \mathrm { ~ A ~ }$ critical implication is that any reactive strategy relying solely on the local density condition $\lambda \geq \lambda _ { \mathrm { t h } }$ will track this moving boundary with a temporal lag. This necessitates a proactive mechanism to compensate for the activation latency.

## C. Adiabatic Link Quality Model and SINR

To bridge the continuous macroscopic mobility and discrete microscopic transmission, we invoke the adiabatic assumption, also known as the time-scale separation principle. Analogous to the quasi-static block-fading model [33], this assumption holds because the task offloading time $T _ { \mathrm { p k t } }$ is orders of magnitude shorter than the characteristic evolution scale of the logistics tide $T _ { \mathrm { h y d r o } }$ . Physically, $T _ { \mathrm { h y d r o } }$ characterizes the time required for significant macroscopic reshaping, defined as the inverse of the maximum relative expansion rate: $T _ { \mathrm { h y d r o } } \sim ( \operatorname* { m a x } | \dot { \sigma } / \sigma | ) ^ { - 1 } \propto T _ { \mathrm { p e r i o d } }$ . Since the delivery cycle T<sub>period</sub> operates on hourly scale while $T _ { \mathrm { p k t } }$ is in milliseconds, $\hat { T _ { \mathrm { p k t } } } \ll T _ { \mathrm { h y d r o } }$ is strictly satisfied. Consequently, the spatial intensity field $\boldsymbol { \lambda } ( \mathbf { x } , t )$ and the aggregate interference are treated as time-invariant snapshots during each transmission interval.

Furthermore, the set of potential interferers is determined by the instantaneous binary activation states $\alpha ( \mathbf { X } _ { i } , t ) \in \{ 0 , 1 \}$ :

$$
\boldsymbol { \Phi } _ { \mathrm { a c t i v e } } ( t ) = \{ \mathbf { X } _ { i } \in \boldsymbol { \Phi } _ { \mathrm { B S } } \mid \alpha ( \mathbf { X } _ { i } , t ) = 1 \} ,\tag{8}
$$

where $\mathbf { X } _ { i } \in \mathbb { R } ^ { 2 }$ denotes the spatial location of the i-th GBS. In contrast to static homogeneous PPP networks, $\Phi _ { \mathrm { a c t i v e } } ( t )$ constitutes a time-varying, spatially inhomogeneous point process governed by the pulsating logistics tide.

For a typical UAV located at $\mathbf { x } _ { 0 } ,$ , the instantaneous signalto-interference-plus-noise ratio (SINR) is given by:

$$
\mathrm { S I N R } ( \mathbf { x } _ { 0 } , t ) = \frac { P _ { \mathrm { L A S } } h _ { 0 } L ( \left| \left| \mathbf { x } _ { 0 } - \mathbf { X } ^ { * } \right| \right| ) } { I _ { \mathrm { a g g } } ( \mathbf { x } _ { 0 } , t ) + P _ { \mathrm { N } } } ,\tag{9}
$$

where $\mathbf { X } ^ { * } \in \Phi _ { \mathrm { a c t i v e } } ( t )$ is the serving BS that provides the maximum received power, and $P _ { \mathrm { N } }$ is the noise power, while the aggregate interference $I _ { \mathrm { a g g } } ( \mathbf { x } _ { 0 } , t )$ is the summation of signals from all other active BSs within the active region (AR) $A _ { \mathrm { o n } } ( t )$

$$
I _ { \mathrm { a g g } } ( \mathbf { x } _ { 0 } , t ) = \sum _ { \mathbf { X } _ { i } \in \Phi _ { \mathrm { a c i v e } } ( t ) \backslash \{ \mathbf { X } ^ { * } \} } P _ { \mathrm { L A S } } h _ { i } L ( \| \mathbf { x } _ { 0 } - \mathbf { X } _ { i } \| ) .\tag{10}
$$

In (9) and (10), $h _ { 0 }$ and $h _ { i }$ are the respective small-scale fading channel power gains, which are exponentially distributed for Rayleigh fading, $L ( d ) { = } d ^ { - \nu }$ is the power-law path loss function with exponent $\nu > 2 .$ , and $P _ { \mathrm { L A S } }$ denotes the transmission power of the LAS module.

## D. Spatiotemporal Performance Metrics

To quantify the trade-off between sustainability and reliability under dynamic load, we define three key metrics over a logistics cycle $T _ { \mathrm { p e r i o d } } .$ . Let $\pmb { \alpha } = \{ \alpha ( \mathbf { x } , t ) \in \{ 0 , 1 \} \mid \mathbf { x } \in \mathcal { A } , t \in$ $[ 0 , T _ { \mathrm { p e r i o d } } ] \}$ be the binary activation policy of the LAS layer. 1) Total Served Workload Volume: The primary utility of the logistics network is the computational tasks offloaded by the UAVs. Unlike static networks where the instantaneous sum-rate suffices, the non-stationary logistics tide requires evaluating the cumulative service volume. We define the total served traffic, denoted as $\mathcal { T } _ { \mathrm { t o t a l } } ( \alpha )$ , as the spatio-temporal integration of the successful service capacity density:

$$
\mathcal { T } _ { \mathrm { t o t a l } } ( \alpha ) \triangleq \int _ { 0 } ^ { T _ { \mathrm { p e r i o d } } } \int _ { \mathcal { A } } \mathcal { R } ( \mathbf { x } , t ; \alpha ) \mathrm { d } \mathbf { x } \mathrm { d } t ,\tag{11}
$$

where $\mathcal { R } ( \mathbf { x } , t ; \mathbf { \alpha } _ { } \mathbf { \alpha } )$ represents the successful service capacity density, also known as the effective spatial throughput, formulated as $\mathcal { R } ( \mathbf { x } , t ; \alpha ) = B \eta _ { \mathrm { S E } } \lambda ( \mathbf { x } , t ) \mathsf { P } _ { \mathrm { c o v } } ( \mathbf { x } , t \mid \alpha )$ . Here, $\mathsf { P } _ { \mathrm { c o v } } ( \mathbf { x } , t \mid \mathbf { \alpha } ) = \mathbb { P } ( \mathrm { S I N R } ( \mathbf { x } , t ) > \mathbf { \gamma } \gamma )$ denotes the service availability which is mathematically quantified by the instantaneous coverage probability, B is the system bandwidth, and η<sub>SE</sub> represents the target spectral efficiency.

In the context of mission-critical logistics, this link-level coverage probability serves as the fundamental metric quantifying the system-level service availability.

2) Total Energy Consumption: The network energy consumption is directly determined by the spatiotemporal activation pattern of the GBSs. The total energy consumption over one period is defined as:

$$
E _ { \mathrm { t o t a l } } ( \alpha ) \triangleq \int _ { 0 } ^ { T _ { \mathrm { p e r i o d } } } \int _ { A } \lambda _ { \mathrm { B S } } P _ { \mathrm { G B S } } ( \alpha ( \mathbf { x } , t ) ) \mathrm { d } \mathbf { x } \mathrm { d } t ,\tag{12}
$$

where $P _ { \mathrm { G B S } } ( \cdot )$ models the power consumption of a single LAS module:

$$
\begin{array} { r } { P _ { \mathtt { G B S } } ( \alpha ) = P _ { \mathrm { a c t } } \cdot \alpha + P _ { \mathrm { s l p } } \cdot ( 1 - \alpha ) . } \end{array}\tag{13}
$$

Here, $P _ { \mathrm { a c t } }$ and $P _ { \mathrm { s l p } }$ denote the power consumption in the active and sleep modes, respectively.

3) Service Unavailability (Wavefront Outage): To quantify the reliability risk at the expanding edge, we define the instantaneous service unavailability, $\mathcal { O } ( t )$ , as the fraction of workload mass located in the “outage zone”—the spatial gap between the physical demand wavefront $R _ { \mathrm { w f } } ( t )$ and the effective service boundary $R _ { \mathrm { a c t i v e } } ( t )$ induced by the control policy α.

Mathematically, assuming that the policy generates a contiguous coverage area of radius $R _ { \mathrm { a c t i v e } } ( t ) , \mathcal { O } ( t )$ is calculated as the normalized user mass within the gap $[ R _ { \mathrm { a c t i v e } } ( t ) , R _ { \mathrm { w f } } ( t ) ] ;$

$$
\mathcal { O } ( t ; \alpha ) \triangleq \frac { \left[ \int _ { R _ { \mathrm { a c t i v e } } ( t ) } ^ { R _ { \mathrm { w f } } ( t ) } \lambda ( r , t ) \cdot 2 \pi r \mathrm { d } r \right] ^ { + } } { \int _ { 0 } ^ { R _ { \mathrm { w f } } ( t ) } \lambda ( r , t ) \cdot 2 \pi r \mathrm { d } r } .\tag{14}
$$

The unavailability is zero if the service boundary exceeds the wavefront, i.e., $R _ { \mathrm { a c t i v e } } ~ \geq ~ R _ { \mathrm { w f } }$ . This metric specifically

captures the percentage of the logistics swarm—most notably the strategic leading edge—that is physically present but disconnected due to infrastructure hysteresis.

## E. QoS-Constrained EE Maximization Problem

1) Objective Function and Constraints: The primary objective of sustainable mobile computing networks is to maximize the network EE, $\eta _ { \mathrm { E E } } ( \pmb { \alpha } )$ , which is the ratio of the total served workload volume to the total energy consumption over the logistics cycle:

$$
\eta _ { \mathrm { E E } } ( \pmb { \alpha } ) \triangleq \frac { \mathcal { T } _ { \mathrm { t o t a l } } ( \pmb { \alpha } ) } { E _ { \mathrm { t o t a l } } ( \pmb { \alpha } ) } .\tag{15}
$$

Mathematically, we formulate the network control problem as a QoS-constrained EE maximization problem:

$$
\mathcal { P } _ { 0 } : \quad \operatorname* { m a x } _ { \alpha } \quad \eta _ { \mathrm { E E } } ( \alpha ) ,\tag{16a}
$$

$$
\begin{array} { r } { \mathrm { s . t . } \quad \mathcal { O } ( t ; \boldsymbol { \alpha } ) \leq \epsilon _ { \mathrm { t h } } , \quad \forall t \in \mathbb { T } _ { \mathrm { e x p } } , } \end{array}\tag{16b}
$$

$$
\alpha ( \mathbf { x } , t ) \in \{ 0 , 1 \} , \quad \forall \mathbf { x } , t ,\tag{16c}
$$

where $\mathbb { T } _ { \mathrm { e x p } }$ denotes the time interval corresponding to the expansion phase of the logistics tide, and $\epsilon _ { \mathrm { t h } }$ is the maximum allowed service unavailability threshold, e.g., $\epsilon _ { \mathrm { t h } } = 0 . 0 1$

2) Generalized Effective Energy Efficiency: Problem $\mathcal { P } _ { 0 }$ is a non-convex fractional programming problem. Furthermore, the constraint (16b) imposes an infinite number of instantaneous QoS requirements over the continuous domain $\mathbb { T } _ { \mathrm { e x p } } ,$ rendering direct global optimization intractable.

To obtain a tractable formulation, we adopt a penaltyfunction method to transform the constrained optimization problem into an unconstrained maximization of a surrogate objective function, termed the generalized effective EE, denoted as $\eta _ { \mathrm { e f f } }$

Definition 2. We define the effective EE as the following QoSpenalized metric:

$$
\eta _ { \mathrm { e f f } } \triangleq \eta _ { \mathrm { E E } } \cdot \mathcal { U } _ { \beta } \left( \operatorname* { s u p } _ { t \in \mathcal { T } _ { \mathrm { e x p } } } \mathcal { O } ( t ) \right) .\tag{17}
$$

Here, $\mathcal { U } _ { \beta } ( \cdot )$ serves as a soft barrier function, or a multiplicative penalty function, derived from the reliability constraint. We adopt the polynomial form:

$$
\mathcal { U } _ { \beta } ( x ) = \left\{ \begin{array} { l l } { ( 1 - x ) ^ { \beta } , } & { i f 0 \le x < 1 , } \\ { 0 , } & { i f x \ge 1 , } \end{array} \right.\tag{18}
$$

where $\beta \geq 1$ is the penalty factor.

Remark 2. The formulation of $\eta _ { \mathrm { e f f } }$ reconciles the conflicting goals of ${ \bf \ddot { \rho } } _ { 0 } .$ . Physically, the term (1−x) represents the service availability. As the penalty factor β increases, the cost of violating the outage constraint (16b) becomes severe, forcing the optimal solution of the unconstrained proxy problem to asymptotically approach the feasible region of the original problem ${ \mathcal { P } } _ { 0 } .$ This conversion allows us to evaluate the system performance using a single scalar metric that reflects the holistic operational value under QoS constraints.

## IV. FLUX-AWARE ASYMMETRIC ACTIVATION STRATEGY

To effectively manage the high-frequency pulsating logistics tide, the network control logic must bridge the gap between macroscopic fluid dynamics and discrete hardware states. We propose a flux-aware asymmetric activation strategy. Unlike symmetric thresholding, this strategy decouples the activation and deactivation dynamics to accommodate the distinct kinematic requirements of the expansion and contraction phases.

## A. Principles of Asymmetric Activation

The core idea of the proposed strategy is to align the network response with the distinct risk profiles inherent in the pulsating workload. Rather than applying a uniform control logic, we design tailored state-transition mechanisms specifically adapted to the unique vulnerabilities of the expansion and contraction phases.

1) Expansion Phase $( \dot { \sigma } > 0 ) .$ : The primary risk is the wavefront outage caused by boot-up latency. To mitigate this, the strategy employs a proactive activation mechanism, leveraging the spatial phase-lead of the information flux to trigger GBSs before the workload density physically accumulates.

2) Contraction Phase $( { \dot { \sigma } } \ \leq \ 0 ) { : }$ The primary challenge is maintaining connectivity for agents located at the spatial periphery, i.e., the Gaussian tail, as the swarm recedes. To mitigate the risk of premature disconnection, the strategy employs a hysteresis retention mechanism. The flux trigger is deactivated because the inward-pointing macroscopic velocity vector no longer serves as a valid precursor for proactive activation. Instead, the control logic relies exclusively on a lowered density holding threshold, ensuring that the effective service boundary contracts at a slower rate than the physical decay of user density.

## B. Triggering Logic Formulation

Let $\alpha ( \mathbf { x } , t ) \in \{ 0 , 1 \}$ denote the binary activation state of a GBS at location x. We construct the state transition logic based on three distinct Boolean triggering conditions: the proactive flux trigger $\mathcal { C } _ { \mathrm { f l u x } }$ , the reactive load trigger $\mathcal { C } _ { \mathrm { l o a d } }$ , and the retention trigger $\mathcal { C } _ { \mathrm { h o l d } }$ , which are defined by:

$$
\left\{ \begin{array} { l l } { \mathcal { C } _ { \mathrm { f l u x } } : } & { \| \Phi ( \mathbf { x } , t ) \| \geq \delta _ { \mathrm { t h } } , } \\ { \mathcal { C } _ { \mathrm { l o a d } } : } & { \lambda ( \| \mathbf { x } \| , t ) \geq \lambda _ { \mathrm { a c t } } , } \\ { \mathcal { C } _ { \mathrm { h o l d } } : } & { \lambda ( \| \mathbf { x } \| , t ) \geq \lambda _ { \mathrm { h o l d } } , } \end{array} \right.\tag{19}
$$

where $\delta _ { \mathrm { t h } }$ is the flux sensitivity threshold, $\lambda _ { \mathrm { a c t } }$ is the activation density threshold, and we introduce a lower holding threshold $\lambda _ { \mathrm { h o l d } } < \lambda _ { \mathrm { a c t } }$ , such as $\lambda _ { \mathrm { h o l d } }  0$ , to implement the hysteresis mechanism. The activation protocol is defined as:

$$
\begin{array} { r } { \alpha ( \mathbf x , t ) = \left\{ \mathbb { I } \left( \mathcal { C } _ { \mathrm { l o a d } } \lor \mathcal { C } _ { \mathrm { f l u x } } \right) , \quad \mathrm { i f ~ } \dot { \sigma } ( t ) > 0 , \right. } \\ { \mathbb { I } \left( \mathcal { C } _ { \mathrm { h o l d } } \right) \cdot \alpha ( \mathbf x , t - 1 ) , \ \mathrm { i f ~ } \dot { \sigma } ( t ) \le 0 . } \end{array}\tag{20}
$$

To facilitate practical deployment in resource-constrained network controllers, we formalize the proposed logic in Algorithm 1.

## C. Complexity and Implementation Analysis

The proposed strategy exhibits linear computational complexity $O ( M )$ , where M is the number of GBSs. Unlike combinatorial optimization or reinforcement learning approaches that typically scale with $O ( M ^ { 2 } )$ or higher, our method relies on calculating analytical fluid metrics $( \lambda , \lVert \Phi \rVert )$ locally for each node. Beyond computational efficiency, the framework ensures minimal signaling overhead. Unlike centralized optimization schemes requiring real-time channel state information (CSI) from all UAVs, our framework operates on macroscopic statistical parameters, such as $\sigma ( t ) , N ( t )$ , that evolve slowly on the scale of minutes (the logistics cycle) rather than milliseconds. Consequently, the broadcast of these fluid parameters entails negligible bandwidth cost, and the localized flux calculation supports a fully distributed, event-driven activation logic that requires no backhaul coordination between neighboring GBSs. This low overhead is critical for real-time resource provisioning in large-scale mobile systems.

```tcl
Algorithm 1 Flux-Aware Asymmetric Cycle Control
Require: Time $t ;$ Fluid state $\left\{ \sigma , \dot { \sigma } , N \right\}$ ; Previous state $\pmb { \alpha } _ { t - 1 }$
Ensure: New activation state $\mathbf { \alpha } _ { \alpha \mathbf { \beta } } .$
1: Determine Phase:
2: if $\dot {               } \dot { \sigma } ( t ) > 0$ then Mode ← EXPANSION
3: else Mode ← CONTRACTION
4: Update GBS States:
5: for each GBS i at location $\mathbf { x } _ { i }$ do
6: Compute the local density $\lambda ( \mathbf { x } _ { i } , t )$ using (1).
7: if Mode is EXPANSION then
8: ▷ Compute Flux only when needed for proactive trigger
9: $\| \Phi ( \mathbf { x } _ { i } ) \|  \lambda ( \mathbf { x } _ { i } ) \cdot \| \mathbf { x } _ { i } \| \cdot \frac { \dot { \sigma } } { \sigma }$
10: Trigger: $\mathcal { C } _ { \mathrm { f l u x } } \dot {  } ( \| \dot { \Phi } ( \mathbf { x } _ { i } ) \| ) \geq \delta _ { \mathrm { t h } } )$
11: $\alpha ( \mathbf { x } _ { i } , t ) \gets \mathbb { I } ( \lambda ( \mathbf { x } _ { i } ) \geq \lambda _ { \mathrm { a c t } } ^ { } \lor { \mathcal { C } _ { \mathrm { f l u x } } } )$
12: else ▷ Hysteresis Retention Phase
13: $\alpha ( \mathbf { x } _ { i } , t ) \gets \mathbb { I } ( \lambda ( \mathbf { x } _ { i } ) \geq \lambda _ { \mathrm { h o l d } } ) \cdot \dot { \alpha ( \mathbf { x } _ { i } , t - 1 ) }$
14: return $\pmb { \alpha } _ { t }$
```

## D. Spatiotemporal Mechanism Analysis

The proposed logic results in a dynamic network topology that physically adapts to the logistics tide.

1) Traveling Wave Activation (Expansion): During the expansion phase, the condition $\| \Phi \| \ge \delta _ { \mathrm { t h } }$ creates a proactive guard ring ahead of the density wavefront. This does not imply simultaneous global activation. Since the flux magnitude $\| \Phi ( \boldsymbol { r } , t ) \|$ is spatially graded (peaking at the wavefront), the activation condition is satisfied sequentially from the center to the periphery. This results in a “traveling active zone” that propagates ahead of the UAV swarm, ensuring resources are provisioned selectively and just-in-time.

2) Hysteresis Retention (Contraction): As the swarm recedes, the flux intensity diminishes. The protocol automatically switches to the retention mode governed by $\mathcal { C } _ { \mathrm { h o l d } }$ . This ensures that the active region shrinks slower than the density decay, maintaining connectivity for tail users until the local load becomes negligible.

Remark 3. A potential concern with kinematic triggers is the vulnerability to false alarms caused by high-velocity but low-density transient outliers. However, under the proposed fluid-dynamic framework, the activation is governed by the information flux $( \Phi \ = \ \lambda \mathbf { v } ) ,$ , which acts as a robust spatiotemporal momentum filter. Mathematically, the exponential spatial decay of the density field strictly dominates the linear growth of the macroscopic velocity, ensuring that the flux magnitude naturally vanishes in sparse far-field regions. Physically, constrained by the maximum aerodynamic speed of UAVs, a sparse outlier with negligible density cannot generate sufficient momentum to cross the macroscopic threshold $\delta _ { \mathrm { t h } } .$ Consequently, such transient anomalies fail to trigger $\mathcal { C } _ { \mathrm { { f l u x } } } ,$ thereby preventing premature infrastructure activation and energy waste.

## V. PERFORMANCE ANALYSIS

Given the spatial inhomogeneity of the pulsating tide, for tractability, we employ a local homogeneity approximation to derive the CP and EE metrics.

## A. Spatio-Temporal Activation Geometry

The proposed asymmetric strategy yields a phase-dependent network topology. First, we formally derive the effective activation radius, denoted as $R _ { \mathrm { a c t i v e } } ( t )$

Proposition 1. The effective activation radius $R _ { \mathrm { a c t i v e } } ( t )$ that adapts to the expansion-contraction cycle of the logistics tide is expressed as

$$
R _ { \mathrm { a c t i v e } } ( t ) = \left\{ \begin{array} { l l } { \operatorname* { m a x } \left\{ R _ { \mathrm { a c t } } ( t ) , R _ { \mathrm { f l u x } } ( t ) \right\} , } & { i f \dot { \sigma } ( t ) > 0 , } \\ { R _ { \mathrm { h o l d } } ( t ) , } & { i f \dot { \sigma } ( t ) \le 0 , } \end{array} \right.\tag{21}
$$

where the component radii are given by:

$$
R _ { \mathrm { a c t } } ( t ) = \sigma ( t ) \sqrt { 2 \left[ \ln \left( \frac { N ( t ) } { 2 \pi \sigma ^ { 2 } ( t ) \lambda _ { \mathrm { a c t } } } \right) \right] ^ { + } } ,\tag{22a}
$$

$$
R _ { \mathrm { h o l d } } ( t ) = \sigma ( t ) \sqrt { 2 \left[ \ln \left( \frac { N ( t ) } { 2 \pi \sigma ^ { 2 } ( t ) \lambda _ { \mathrm { h o l d } } } \right) \right] ^ { + } } ,\tag{22b}
$$

$$
R _ { \mathrm { f l u x } } ( t ) = \operatorname* { s u p } \left\{ r \in \mathbb { R } ^ { + } : \frac { r } { \sigma ^ { 3 } ( t ) } e ^ { - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } ( t ) } } = \mathcal { K } _ { \mathrm { t h } } ( t ) \right\} ,\tag{22c}
$$

with $\begin{array} { r } { K _ { \mathrm { t h } } ( t ) ~ = ~ \frac { 2 \pi \delta _ { \mathrm { t h } } } { N ( t ) | \dot { \sigma } ( t ) | } } \end{array}$ representing the normalized flux threshold.

Proof. The detailed derivation is provided in Section S-II of the Supplementary File. □

This derived activation radius reveals distinct physical behaviors across the expansion-contraction cycle.

1) Expansion (Proactive Guard Ring): During the expansion phase, $\mathrm { i . e . , ~ } \dot { \sigma } > 0 .$ , the macroscopic velocity $v _ { r } \propto r$ amplifies the flux intensity at the periphery. This kinematic gain pushes the flux boundary $R _ { \mathrm { f l u x } } ( t )$ beyond the static density boundary $R _ { \mathrm { a c t } } ( t )$ , creating a proactive guard ring of width $\Delta R _ { \mathrm { l e a d } } = R _ { \mathrm { f l u x } } - R _ { \mathrm { a c t } }$ that spatially compensates for the boot-up latency.

2) Contraction (Hysteresis Retention): During the contraction phase, $\mathrm { i } . \mathrm { e } . , \dot { \sigma } \leq 0 \mathrm { ~ }$ , the flux trigger is disabled. The activation boundary is governed strictly by the holding threshold $\lambda _ { \mathrm { h o l d } }$ . Since $\lambda _ { \mathrm { h o l d } } ~ < ~ \lambda _ { \mathrm { a c t } }$ , the condition $R _ { \mathrm { h o l d } } ( t ) ~ > ~ R _ { \mathrm { a c t } } ( t )$ holds. This creates a retention zone of width $\Delta R _ { \mathrm { l a g } } = R _ { \mathrm { h o l d } } -$ $R _ { \mathrm { a c t } }$ , preventing the premature disconnection of users at the spatial periphery as the swarm recedes.

## B. Local Service Availability Analysis

The dynamic activation of LAS modules creates a spatially finite and inhomogeneous interference field. Unlike standard stochastic geometry approaches that assume an infinite field of interferers, we explicitly model the truncation of interference at the activation boundary $R _ { \mathrm { a c t i v e } } ( t )$ to derive an accurate CP.

Theorem 1. Consider the finite active region bounded by $R _ { \mathrm { a c t i v e } } ( t )$ . The instantaneous service availability CP for a typical UAV within the active zone is expressed as:

$$
\begin{array} { r } { \mathsf { P } _ { \mathrm { c o v } } ( r , t ) \approx \displaystyle \int _ { 0 } ^ { R _ { \mathrm { a c t i v e } } ( t ) } 2 \pi \lambda _ { \mathrm { B S } } y \exp \Big ( - \pi \lambda _ { \mathrm { B S } } y ^ { 2 } \Big ( 1 } \\ { + \mathcal { F } _ { \mathrm { f i n i t e } } ( y , R _ { \mathrm { a c t i v e } } ) \Big ) \Big ) \mathrm { d } y , } \end{array}\tag{23}
$$

where $\mathcal { F } _ { \mathrm { f i n i t e } } ( y , R _ { \mathrm { a c t i v e } } )$ is the finite interference factor explicitly capturing the boundary effect:

$$
\begin{array} { l } { { \displaystyle { \mathcal F } _ { \mathrm { f i n i t e } } ( y , R _ { \mathrm { a c t i v e } } ) = } _ { 2 } F _ { 1 } \left( 1 , \kappa ; 1 + \kappa ; - \gamma \right) } \\ { { \displaystyle ~ - \left( \frac { R _ { \mathrm { a c t i v e } } } { y } \right) ^ { 2 } } _ { 2 } F _ { 1 } \left( 1 , \kappa ; 1 + \kappa ; - \gamma \left( \frac { y } { R _ { \mathrm { a c t i v e } } } \right) ^ { \nu } \right) } \end{array}\tag{24}
$$

with $\kappa = 2 / \nu$ and γ being the SINR threshold.

Proof. The detailed derivation is provided in Section S-III of the Supplementary File. □

Remark 4. The second term in (24) represents the boundary correction. As $R _ { \mathrm { a c t i v e } }  \infty ,$ , this term vanishes, reducing to the classical infinite plane solution. However, near the network edge where $y ~ \to ~ R _ { a c t i v e } ,$ , this term significantly reduces the estimated interference.

## C. Network Energy Efficiency

By substituting the phase-dependent activation radius derived in Proposition 1 into the metric definitions, we obtain the closed-form expression for EE.

Theorem 2. The period-average EE of the network, defined as the ratio of total served traffic to total energy consumption over a cycle $T _ { \mathrm { p e r i o d } } ,$ is given by:

$$
\eta _ { \mathrm { E E } } = \frac { \mathcal { T } _ { \mathrm { t o t a l } } } { E _ { \mathrm { t o t a l } } } = \frac { B \eta _ { \mathrm { S E } } \int _ { 0 } ^ { T _ { \mathrm { p e r i o d } } } \mathcal { M } ( t ) \bar { \mathsf { P } } _ { \mathrm { c o v } } ( t ) \mathrm { d } t } { \int _ { 0 } ^ { T _ { \mathrm { p e r i o d } } } P ( t ) \mathrm { d } t } ,\tag{25}
$$

where $\bar { \mathsf { P } } _ { \mathrm { c o v } } ( t )$ denotes the spatially averaged CP over the dynamic active region $R _ { \mathrm { a c t i v e } } ( t )$ , approximated as:

$$
\bar { \mathsf { P } } _ { \mathrm { c o v } } ( t ) \approx \frac { 1 } { 1 + \mathcal { F } _ { \mathrm { f i n i t e } } ( R _ { \mathrm { a c t i v e } } ( t ) ) } ,\tag{26}
$$

with $\mathcal { F } _ { \mathrm { f i n i t e } }$ given in (24), while $\mathcal { M } ( t )$ and P (t) are the served workload mass and network power consumption defined below.

1) Served User Mass $\mathcal { M } ( t )$ : This term represents the aggregate workload demand covered by the active network, derived from the Gaussian integration:

$$
\mathcal { M } ( t ) = N ( t ) \left( 1 - \exp \left( - \frac { R _ { \mathrm { a c t i v e } } ^ { 2 } ( t ) } { 2 \sigma ^ { 2 } ( t ) } \right) \right) .\tag{27}
$$

2) Network Power Consumption $P ( t )$ : This term captures the instantaneous power cost of the infrastructure:

$$
P ( t ) = \pi R _ { \mathrm { a c t i v e } } ^ { 2 } ( t ) \lambda _ { \mathrm { B S } } \Delta P + P _ { \mathrm { b a s e } } ,\tag{28}
$$

where $\Delta P = P _ { \mathrm { a c t } } - P _ { \mathrm { s l p } }$ represents the activation power penalty, and $P _ { \mathrm { b a s e } } = | \mathcal { A } | \lambda _ { \mathrm { B S } } P _ { \mathrm { s l p } }$ denotes the baseline sleep power of the entire service area A.

Proof. The detailed derivation is provided in Section S-IV of the Supplementary File. □

This analytical form facilitates the numerical optimization of the flux threshold $\delta _ { \mathrm { t h } }$ . The objective is to balance the size of the proactive guard ring, which dictates coverage reliability, against the incremental energy cost, thereby locating the Pareto-optimal operating point.

## D. Theoretical Analysis of Flux Phase-Lead

The effectiveness of the proposed strategy depends on whether the information flux Φ provides an earlier detection signal than the scalar density λ at the expanding wavefront. We formally prove this property by analyzing the spatial monotonicity of the flux-to-load ratio.

Lemma 1. During the expansion phase where $\dot { \sigma } ( t ) > 0 ,$ , the ratio of the flux magnitude to the workload density, denoted as $\mathcal { R } _ { \Phi / \lambda } ( \boldsymbol { r } , t )$ , is a strictly monotonically increasing function of the radial distance r.

Proof. Recall the definition of information flux from Definition 1: $\| \Phi ( r , t ) \| = \lambda ( r , t ) \cdot | v _ { r } ( r , t ) |$ |. Substituting the derived macroscopic velocity $\begin{array} { r } { v _ { r } ( r , t ) \approx r \frac { \dot { \sigma } } { \sigma } } \end{array}$ , the ratio is given by:

$$
\mathcal { R } _ { \Phi / \lambda } ( \boldsymbol { r } , t ) \triangleq \frac { \Vert \Phi ( \boldsymbol { r } , t ) \Vert } { \lambda ( \boldsymbol { r } , t ) } = | v _ { r } ( \boldsymbol { r } , t ) | = r \frac { \dot { \sigma } ( t ) } { \sigma ( t ) } .\tag{29}
$$

For any fixed time instant t in the expansion phase where $\dot { \sigma } > 0$ , the term $\frac { \dot { \sigma } } { \sigma }$ is a positive constant with respect to space. Taking the partial derivative with respect to r:

$$
\frac { \partial } { \partial r } \mathcal { R } _ { \Phi / \lambda } ( r , t ) = \frac { \dot { \sigma } ( t ) } { \sigma ( t ) } > 0 .\tag{30}
$$

Thus, the relative strength of the flux signal compared to the density signal increases linearly with distance. This completes the proof. □

Remark 5. Lemma 1 provides the theoretical basis for the kinematic phase lead. At the swarm center where $r \  \ 0 ,$ density dominates. However, at the far-field wavefront where $r \gg \sigma ,$ , the high expansion velocity amplifies the flux signal. Consequently, for a decaying Gaussian tail, the flux threshold condition $\| \Phi \| \ge \delta _ { \mathrm { t h } }$ is satisfied at a strictly larger radius than the density condition $\lambda \ \geq \ \lambda _ { \mathrm { t h } }$ (assuming normalized thresholds). This ensures that the flux-triggered proactive guard ring is generated ahead of the traffic load.

1) Quantification of Spatial Flux Gain: Based on the monotonicity proven above, we quantify the spatial gain afforded by the flux-aware strategy.

Definition 3. During the expansion phase where $\dot { \sigma } > 0 ,$ , the flux gain $\mathcal { G } _ { \mathrm { f l u x } } ( t )$ is defined as the spatial difference between the proactive flux boundary and the reactive density boundary:

$$
\mathcal { G } _ { \mathrm { f l u x } } ( t ) \triangleq R _ { \mathrm { f l u x } } ( t ) - R _ { \mathrm { a c t } } ( t ) .\tag{31}
$$

Since the macroscopic velocity $\begin{array} { l } { \displaystyle \boldsymbol { v } _ { r } ( \boldsymbol { r } ) ~ \approx ~ \boldsymbol { r } \dot { \sigma } / \sigma } \end{array}$ increases linearly with distance, the flux intensity $\lVert \Phi \rVert = \lambda v _ { r }$ decays slower than the density λ at the wavefront. Consequently, for a properly calibrated $\delta _ { \mathrm { t h } }$ , the condition $\mathcal { G } _ { \mathrm { f l u x } } ( t ) > 0$ holds.

Remark 6. Physically, $\mathcal { G } _ { \mathrm { f l u x } }$ represents the width of the proactive guard ring. From a control theory perspective, this metric represents a space-time conversion: the strategy trades spatial redundancy in the form of an extra active ring of width $\mathcal { G } _ { \mathrm { f l u x } }$ for temporal margin. This spatial advance compensates for the inevitable time delay $\tau _ { \mathrm { b o o t } }$ inherent in hardware state transitions.

To ensure uninterrupted connectivity for the leading UAVs, the spatial gain must outpace the physical movement of the swarm during the wake-up process. This leads to the following fundamental condition for reliability.

Theorem 3. The wavefront outage is theoretically eliminated if and only if the flux gain satisfies:

$$
\mathcal { G } _ { \mathrm { f l u x } } ( t ) \geq \int _ { t } ^ { t + \tau _ { \mathrm { b o o t } } } v _ { \mathrm { w f } } ( \tau ) \mathrm { d } \tau \approx v _ { \mathrm { w f } } ( t ) \cdot \tau _ { \mathrm { b o o t } } ,\tag{32}
$$

where $v _ { \mathrm { w f } } ( t )$ is the wavefront phase velocity defined in (7). This inequality establishes the fundamental geometric constraint for the flux-aware activation boundary.

Remark 7. It is crucial to note that satisfying the kinematic zero-latency condition in Theorem 3 is a necessary but not sufficient condition for successful task offloading. The holistic system reliability is governed by a two-tier hierarchy. 1) Hardware Availability: The GBS must be active upon the UAV’s arrival, which is addressed by the flux-aware guard ring $\mathcal { G } _ { \mathrm { f l u x } } ,$ ; and 2) Link Reliability: The instantaneous SINR must exceed the target threshold γ. In our framework, this second tier is rigorously captured by the finite network coverage probability $\mathsf { P } _ { \mathrm { c o v } }$ derived in Theorem 1. Consequently, the overall served traffic $\tau _ { \mathrm { t o t a l } }$ defined in (11) explicitly integrates both the kinematic availability and the SINR-based coverage probability, ensuring that offloading failures due to signal degradation are inherently penalized.

The condition established in Theorem 3 imposes a fundamental geometric constraint on the activation boundary. To translate this theoretical kinematic requirement into practical system design, we derive the upper bound for the flux sensitivity threshold.

Proposition 2. To ensure zero-latency coverage given a service setup constraint $\tau _ { \mathrm { b o o t } } ,$ , the flux sensitivity threshold $\delta _ { \mathrm { t h } }$ must be calibrated to satisfy:

$$
\delta _ { \mathrm { t h } } \leq \operatorname* { i n f } _ { t \in \mathbb { T } _ { \mathrm { e x p } } } \left\| \Phi \left( R _ { \mathrm { a c t } } ( t ) + v _ { \mathrm { w f } } ( t ) \tau _ { \mathrm { b o o t } } , t \right) \right\| .\tag{33}
$$

This inequality serves as a design criterion: it quantifies the minimum sensitivity required to detect the precursor momentum at the specific look-ahead distance $d _ { \mathrm { l e a d } } = v _ { \mathrm { w f } } \tau _ { \mathrm { b o o t } }$

Proof. From Theorem 3, the zero-latency requirement is $R _ { \mathrm { f l u x } } \geq R _ { \mathrm { a c t } } + v _ { \mathrm { w f } } \tau _ { \mathrm { b o o t } }$ . Let the right-hand side be the required target radius $R _ { \mathrm { r e q } } \triangleq R _ { \mathrm { a c t } } + v _ { \mathrm { w f } } \tau _ { \mathrm { b o o t } }$ . Recall that $R _ { \mathrm { f l u x } }$ is the outer root of $\| \Phi ( r ) \| = \delta _ { \mathrm { t h } }$ . In the wavefront region where $r > \sigma$ , the flux magnitude $\| \Phi ( r ) \|$ is a monotonically decreasing function of $r .$ Therefore, to ensure the trigger radius $R _ { \mathrm { f l u x } }$ extends beyond $R _ { \mathrm { r e q } }$ , the triggering threshold $\delta _ { \mathrm { t h } }$ must be lower than the flux intensity at $R _ { \mathrm { r e q } }$

$$
\delta _ { \mathrm { t h } } = \| \Phi ( R _ { \mathrm { f l u x } } ) \| \leq \| \Phi ( R _ { \mathrm { r e q } } ) \| .\tag{34}
$$

Substituting the definition of Φ yields the bound in (33). This completes the proof. □

## VI. NUMERICAL RESULTS AND ANALYSIS

We validate the analytical framework using Monte Carlo simulations averaged over 50,000 iterations within a service area A of $2 0 \times 2 0 ~ \mathrm { k m ^ { 2 } }$ governed by the pulsating workload model. The default system parameters are listed in Table II. To ensure the realism of the evaluation, these parameters are selected based on a combination of standardization reports and practical hardware specifications. Specifically, the communication parameters, including the UAV operational altitude (150 m) and path loss exponent $( \nu = 2 . 5 )$ , are aligned with the 3GPP technical report for low-altitude aerial vehicles (TR 36.777) [34]. The hardware profiles, such as the active/sleep power consumption and the service setup latency $( \tau _ { \mathrm { b o o t } } = 5$ min), reflect the typical specifications of MEC-enabled micro BSs. This service setup latency accounts for the aggregate delay of the hardware transitioning from a deep sleep mode [32] and the software overhead of MEC container cold-starts [35]. Furthermore, the macroscopic traffic variables $( N _ { 0 }$ and σ<sub>0</sub>) are configured as design assumptions to represent a cityscale logistics hub serving a metropolitan area.

To assess the system-level gains, we compare the proposed flux-aware asymmetric strategy against the following four baseline strategies.

1) Static Always-On: All infrastructure modules remain active continuously. This provides an upper theoretical bound on service reliability but incurs the maximum possible energy cost.

2) Reactive Strategy: BSs activate strictly upon detecting local user density $\lambda \geq \lambda _ { \mathrm { { a c t } } }$ . This serves as the fundamental baseline for analyzing boot-up latency and resultant wavefront outages.

3) Robust Margin Strategy (RMS): Adapted from robust optimization methods based on statistical moments and chance constraints [17], this baseline adds a conservative spatial safety margin outside the density boundary to hedge against mobility fluctuations. In our implementation, this margin is instantiated as a fixed 8.5 km worstcase guard ring.

4) Traffic Snapshot Prediction (TSP) Baseline: Inspired by learning-based traffic prediction models (e.g., LSTM [18– 20] and DRL [21]), this serves as an oracle baseline. It assumes perfect foresight of the future static density boundary to fully cancel the temporal boot-up latency, activating BSs ahead of time based strictly on the predicted spatial density snapshots.

TABLE II  
DEFAULT SIMULATION PARAMETERS
<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td></tr><tr><td>GBS Density (LAS Layer)</td><td> $\lambda _ { \mathrm { B S } }$ </td><td>5 BSs/km²</td></tr><tr><td>UAV Flight Altitude</td><td> $H _ { \mathrm { U A V } }$ </td><td>150 m</td></tr><tr><td>Bandwidth per LAS</td><td>B</td><td>20 MHz</td></tr><tr><td>Path Loss Exponent</td><td>ν</td><td>2.5</td></tr><tr><td>Target SINR Threshold</td><td>γ</td><td>-5 dB</td></tr><tr><td>Target Spectral Efficiency Baseline Workload Intensity</td><td>ηSE</td><td>2 bps/Hz</td></tr><tr><td>Baseline Spatial Spread</td><td> $N _ { 0 }$ </td><td>25, 000 UAVs</td></tr><tr><td></td><td>σ0</td><td>4.5 km</td></tr><tr><td>Load Modulation Index</td><td> $\delta _ { N }$ </td><td>0.8</td></tr><tr><td>Spatial Expansion Index</td><td> $\delta _ { \sigma }$ </td><td>0.7</td></tr><tr><td>Active Power (LAS)</td><td> $P _ { \mathrm { a c t } }$ </td><td>400 W</td></tr><tr><td>Sleep Power (LAS)</td><td> $P _ { \mathrm { s l p } }$ </td><td>50 W</td></tr><tr><td>Service Setup Latency</td><td> $\tau _ { \mathrm { b o o t } }$ </td><td>300 s (5 min)</td></tr><tr><td>Flux Sensitivity Threshold</td><td> $\delta _ { \mathrm { t h } }$ </td><td>Variable</td></tr><tr><td>Static Activation Threshold</td><td> $\lambda _ { \mathrm { a c t } }$ </td><td> $5 0 \ \mathrm { a g e n t s } / \mathrm { k m ^ { 2 } }$ </td></tr><tr><td>Holding Threshold</td><td> $\lambda _ { \mathrm { h o l d } }$ </td><td> $\mathrm { 2 \ a g e n t s / k m ^ { 2 } }$ </td></tr></table>

![](images/d1605b56163232f01b1ed379164f60130952063361bc10aba2de34133d289a23.jpg)  
Fig. 2. Spatiotemporal evolution of the pulsating logistics tide.

The analysis proceeds in four steps: validating the analytical coverage model and visualizing flow dynamics (Section $\mathrm { V I - A } )$ , validating the spatial phase-lead of the information flux (Section VI-B), quantifying the reliability gain in eliminating outages (Section VI-C), and evaluating the overall network EE (Section VI-D).

## A. Model Visualization and Analytical Validation

1) Macroscopic Dynamics Visualization: To verify the kinematic basis of the proposed framework, Fig. 2 illustrates the spatio-temporal evolution of the workload density field $\lambda ( r , t )$ alongside the dynamic logistic wavefront $R _ { \mathrm { w f } } ( t )$ represented by a white contour. By superimposing the Lagrangian characteristic trajectories of hypothetical fluid particles (plotted as thin grey lines), we observe distinct phase-dependent behaviors: during the expansion phase where $t < 1$ h, the grey trajectories diverge rapidly, corroborating that the wavefront propagation is physically driven by the macroscopic advection velocity $v _ { r } \ > \ 0 ;$ conversely, during the contraction phase where $t > 1 \mathrm { ~ h ~ }$ , the grey trajectories converge, reflecting the inward momentum as the swarm returns to the hub. This confirms that the derived information flux metric provides an accurate kinematic representation of the swarm’s momentum.

![](images/ee1a4ba758302457090aebc7fba368b3faa292b294acdd3f38572ea9d9542687.jpg)  
Fig. 3. Validation of the analytical local coverage probability.

![](images/fa76fc6f4a9229242782a88a4d50d9fe6653f4d4d3ea898f3e429430f6322857.jpg)  
Fig. 4. Spatiotemporal evolution of the coverage probability over a full expansion-contraction cycle.

2) Validation of Analytical Expressions: We validate the finite network coverage model established in Theorem 1 against Monte Carlo simulations. Fig. 3 presents the spatial coverage profile at a representative snapshot of $R _ { \mathrm { a c t i v e } } = 1 0$ km, corresponding to the fully expanded service boundary, with path loss exponent $\nu = 3 . 0$ and SINR threshold $\gamma = - 3$ dB. Notably, the distinct boundary-induced coverage gain observed near the periphery (r ≈ 10 km) is precisely predicted by the proposed analysis. This validation confirms that the finite interference factor derived in (24) correctly quantifies the reduction in aggregate interference due to the sleep mode of GBSs outside the active region, thereby eliminating the estimation error at the wavefront.

Fig. 4 extends this validation to the temporal domain over a full expansion-contraction cycle. The heatmap reveals a traveling service plateau, visualized as the green region, which is strictly confined within the analytical activation boundary traced by the white curve. The precise alignment between the analytical boundary and the effective service zone confirms the robustness of the derived model under time-varying topologies. Even as the network size undergoes substantial fluctuations, the analytical framework accurately tracks the spatiotemporal evolution of the SINR field, demonstrating that the proposed fluid-based stochastic geometry offers a rigorous performance baseline for dynamic logistics corridors.

![](images/3ddbd940e93bb17d6e4797e1130145a4a5f18b147232f284a2510c8c69a74114.jpg)  
Fig. 5. Spatial mechanism of the flux-aware strategy at $t _ { 0 } = 0 . 6$ h, showing the proactive guard ring.

## B. Validation of Kinematic Mechanism: Flux Phase-Lead

We first validate the kinematic basis of the proposed framework, specifically the spatial and temporal phase-lead of the information flux Φ. The simulation focuses on the rapid expansion phase, as the resulting macroscopic advection velocity is the physical driver of the flux signal.

1) Spatial Mechanism: Proactive Guard Ring: Fig. 5 elucidates the spatial interplay between the normalized agent density $\lambda ( r , t _ { 0 } )$ and the flux magnitude $\| \Phi ( r , t _ { 0 } ) \|$ at a representative snapshot $t _ { 0 } { = } 0 . 6 \mathrm { h }$ . The results reveal a fundamental limitation of conventional detection methods. As shown by the blue solid curve, the agent density decays rapidly at the network periphery. This metric is strictly coupled to the physical presence of agents: the density threshold $\lambda _ { \mathrm { { a c t } } }$ is crossed only upon the swarm’s arrival. Consequently, any strategy relying solely on density fails to anticipate the load, making the service setup latency $\tau _ { \mathrm { { b o o t } } }$ an unavoidable penalty.

In contrast, the flux magnitude represented by the red dashed curve exhibits a distinct wavefront enveloping effect. Driven by the high macroscopic velocity $v _ { r } \propto r$ in the far field, the flux signal remains significant even in regions where the agent density is negligible, specifically at distances exceeding 10 km. This kinematic property effectively decouples the trigger signal from the physical load. As a result, the GBSs are activated by the flux condition $\lVert \Phi \rVert \geq \delta _ { \mathrm { t h } }$ well before the density condition is met. This predictive mechanism generates a substantial proactive guard ring of width $\Delta R \approx 8 . 2 5 \mathrm { k m }$ , buying the necessary time for the infrastructure to wake up before the agents actually arrive.

2) Temporal Validation: Zero-Latency Triggering: The translation of this spatial gain into an effective temporal lead is verified in Fig. 6, which traces the metric evolution at a representative far-field location located at a radial distance of 14.5 km. As the logistics tide propagates outward, the flux curve exhibits a sharp rise well in advance of the density curve. The calibrated trigger activates at time $t _ { \mathrm { f l u x } } .$ , which precedes the density arrival time $t _ { \mathrm { d e n } }$ by approximately 5 minutes. This interval closely approximates the mandatory service setup latency $\tau _ { \mathrm { b o o t } } .$ , confirming that the information flux functions as a robust precursor signal to ensure the GBS completes its activation sequence just as the physical load arrives.

![](images/6eb2ea89c22543fc584ae846ebf0b034f1ed2f0fbce4b186e07cc74d0d32e0b0.jpg)  
Fig. 6. Temporal validation of zero-latency triggering at the network edge (r = 14.5 km).

## C. Reliability Analysis: Elimination of Wavefront Outage

Having verified the kinematic phase-lead mechanism, we now quantify the system-level reliability gain during the critical expansion phase spanning the interval $t \in [ 0 . 2 , 0 . 8 ] \mathrm { I }$ h. The primary objective is to demonstrate how the proposed strategy mitigates service outages caused by a service setup latency of $\tau _ { \mathrm { { b o o t } } } = 5$ min. We evaluate reliability using the service unavailability metric $\mathcal { O } ( t )$ defined in (14).

The effective service boundary is physically constrained by the activation latency, formulated as $R _ { \mathrm { a c t i v e } } ( t ) = R _ { \mathrm { t r i g } } ( t { - } \tau _ { \mathrm { b o o t } } )$ For the reactive strategy, the trigger follows the static density wavefront where $R _ { \mathrm { t r i g } } ~ = ~ R _ { \mathrm { a c t } } .$ . Conversely, for the fluxaware strategy, we employ the robust calibration derived in Proposition 2 by setting $\delta _ { \mathrm { t h } } \approx 0 . 2 \cdot \delta _ { \mathrm { m a x } }$ to create a sufficient safety margin against the expansion velocity.

Fig. 7 visualizes the dynamic interaction between the traffic wavefront and the service boundary. The upper panel reveals a distinct tracking disparity where the reactive strategy, plotted as a blue dashed line, consistently lags behind the physical wavefront. This hysteresis creates a widening outage zone of approximately 1–2 km, confirming that static density detection is fundamentally too slow for high-mobility logistics corridors. In sharp contrast, the flux-aware strategy represented by the red dashed line maintains a service boundary that strictly envelopes the physical wavefront, effectively predicting the expansion trajectory.

The consequences are quantified in the lower panel. The reactive scheme suffers from a persistent service unavailability peaking at approximately 15%. This value represents the complete disconnection of the leading swarm, the most strategic assets executing long-range missions. The proposed strategy reduces this outage metric to near zero, validating the effectiveness of flux-based proactive control in eliminating wavefront outages.

![](images/f5e0d8264f8b1f22ef97b0cc443264651a319038538d376835da27ab029279ba.jpg)

(b) Reliability Analysis: Elimination of Wavefront Outage  
![](images/706117ed08bc5fcab95178c890d074feee44f21a6fb483877c8dbfeb60127289.jpg)  
Fig. 7. Reliability analysis during the expansion phase. (a) Service-boundary trajectory versus the physical wavefront. (b) Instantaneous service unavailability.

![](images/7b23f28714c45d189f943a766626d087184002c9140a8737cd4f2e86772f9587.jpg)  
Fig. 8. System-level performance comparison across benchmark strategies.

## D. System-Level Energy Efficiency and Pareto Optimization

Finally, we evaluate the comprehensive system performance to validate the economic viability of the proposed framework.

1) Comparison of Raw versus Effective Energy Efficiency: Fig. 8 presents the normalized performance comparison across the five evaluated strategies. An initial observation is the counter intuitive behavior of the raw EE (η<sub>EE</sub>). The reactive strategy and the TSP achieve the highest nominal η<sub>EE</sub>. However, this metric is deceptive in high-mobility logistics scenarios. As indicated by the served traffic ratio, the reactive strategy captures only 79.6% of the computational demand, while TSP, despite perfectly predicting the density boundary, only marginally improves this to 82.8%. This implies that both strategies fundamentally fail to serve the critical wavefront of the digital tide—specifically, the high-velocity leading UAVs entering new coverage areas before the local density reaches the activation threshold. Consequently, their high raw energy efficiencies are merely artifacts of severe service denial, which is operationally unacceptable for mission-critical logistics.

To resolve this efficiency-reliability trade-off, we analyze the effective EE $( \eta _ { \mathrm { e f f } } )$ , which explicitly penalizes service outages. Under this QoS-constrained metric, the performance of both the reactive and TSP strategies collapses. To guarantee service availability, the RMS enforces a static worst-case spatial guard ring, successfully elevating the served traffic to approximately 99.0%. However, this rigid geometric expansion incurs massive energy waste through severe over-activation, causing its $\eta _ { \mathrm { e f f } }$ to degrade to a level comparable with the static always-on upper bound. In contrast, the proposed flux-aware strategy leverages the fluid-dynamic velocity field to dynamically adjust the activation boundary. It seamlessly captures the wavefront momentum, achieving a 99.1% traffic service rate that is numerically comparable to the always-on benchmark, while promptly shrinking the boundary during swarm contraction to reduce trailing energy waste. By inherently balancing kinematic reliability and dynamic power consumption, the flux-aware framework achieves the maximum effective EE among all the evaluated approaches.

2) Optimal Threshold Calibration: To validate the existence of a unique optimal operating point, Fig. 9 analyzes the sensitivity of system performance to the flux threshold $\delta _ { \mathrm { t h } } .$ . The effective EE and service reliability curves depicted in Fig. 9 elucidate the fundamental trade-off between energy consumption and service reliability. Specifically, the optimization landscape reveals how flux sensitivity dictates the balance between energy waste and outage risks.

![](images/05da27782e72cb7161f8c9695fbb65bca81b04f23fb873c902c107e741f2329a.jpg)  
Fig. 9. Impact of the flux sensitivity threshold $\delta _ { \mathrm { t h } }$ on system performance and the resulting Pareto-optimal operating point.

2.a) Over-Sensitive Regime $( \delta _ { t h } < 1 0 ^ { - 1 } ) :$ Here, the low threshold results in high sensitivity. Both the effective EE and service reliability improve as $\delta _ { \mathrm { t h } }$ increases. As $\delta _ { \mathrm { t h } }$ approaches $1 0 ^ { - 1 }$ , the service reliability reaches approximately 100% but this comes at a severe energy cost with the effective EE suppressed below 0.7. This is because the system maintains an excessively wide proactive guard ring, activating GBSs far earlier than necessary.

2.b) Transition Regime $( 1 0 ^ { - 1 } \le \delta _ { t h } < 1 0 ^ { 2 } ) :$ This interval marks the efficiency-gaining phase. As $\delta _ { \mathrm { t h } }$ increases, the system progressively sheds spatial redundancy, and the effective EE climbs steadily from 0.7 to its peak, while reliability remains largely robust above 95%. This confirms that the flux trigger still provides sufficient lead time to compensate for $\tau _ { \mathrm { b o o t } }$ while eliminating the waste of an oversized guard ring.

2.c) Pareto-Optimal Point $( \delta _ { t h } \approx 1 0 ^ { 2 } )$ : The global maximum of the effective EE curve defines the optimal equilibrium. Crucially, this peak efficiency does not correspond to perfect reliability: at the optimal $\delta _ { \mathrm { t h } } .$ , service reliability drops from its peak of 100% to approximately 93%.

2.d) Under-Sensitive Regime $( \delta _ { t h } > 1 0 ^ { 2 } )$ : Beyond the optimal point, $\delta _ { \mathrm { t h } }$ becomes excessively high. Physically, the proactive guard ring contracts until its width is insufficient to compensate for the service setup latency $\tau _ { \mathrm { b o o t } } .$ . In the asymptotic limit, the flux trigger is effectively disabled, causing the strategy to degenerate into the reactive baseline. Consequently, the network detects the wavefront too late, causing service reliability to plummet below 75%. The heavy wavefront outage triggers the steep slope of the QoS penalty function $\mathcal { U } _ { \beta }$ , driving the effective EE to collapse toward the negligible performance floor of the reactive strategy.

This result demonstrates a strategic trade-off: to maximize the effective EE, the system must tolerate a marginal degradation in reliability, corresponding to an approximately 7% outage risk at the wavefront. This calibration tightens the proactive guard ring to the minimum size necessary to offset hardware latency, thereby locating the true Pareto-optimal frontier that is unattainable by strictly reactive mechanisms.

![](images/b8c6839bdb6a15a49169da4bf4dc3a0d69e6f76b9278a7806d66732c96e85abe.jpg)

![](images/6933831bb91f2e0ebaf440fcf2b7ff1dcad54fec0463d65178b8f6c5c78d8489.jpg)  
Fig. 10. Sensitivity of system performance to the service setup latency under the Pareto-optimal flux threshold: (a) impact on service reliability, and (b) impact on effective energy efficiency.

## E. System Sensitivity and Robustness Analysis

1) Sensitivity to Service Setup Latency: We evaluate the system robustness against service setup latency $\tau _ { \mathrm { b o o t } } \in [ 1 , 1 0 ]$ min, representing varying MEC instantiation and RF wakeup overheads. We fix the flux sensitivity threshold to the Pareto-optimal $\delta _ { \mathrm { t h } } = 1 0 ^ { 2 }$ . As shown in Fig. 10 (a), the reactive baseline’s service unavailability scales linearly with $\tau _ { \mathrm { b o o t } } .$ approaching 37% at a 10-minute latency. Conversely, the fluxaware strategy exhibits graceful degradation, restricting the outage to 6.2% at 5 minutes and below 15% at 10 minutes. This confirms that the proactive guard ring effectively absorbs the temporal lag. Consequently, as depicted in Fig. 10 (b), the reactive strategy’s effective EE plummets due to severe QoS penalties, whereas the proposed framework maintains superior energy efficiency across the latency spectrum, validating its stability for practical deployments.

2) Robustness Against RF Constraints: We further investigate the system sensitivity to underlying RF parameters under five scenarios using the control variable method, as illustrated in Fig. 11. First, fixing $\eta _ { \mathrm { S E } } = 2 . 0$ bps/Hz and increasing γ from −5 dB to 5 dB nonlinearly degrades the coverage probability, compressing the effective EE curves downward. Second, fixing $\gamma = - 5 \mathrm { d B }$ and increasing $\eta _ { \mathrm { S E } }$ from 2.0 to 4.0 bps/Hz linearly multiplies the spatial capacity, stretching the effective EE curves upward.

Despite these severe vertical fluctuations, the Pareto-optimal flux sensitivity threshold remains stationary at $\delta _ { \mathrm { t h } } ~ \approx ~ 1 0 ^ { 2 }$ across all scenarios. This invariant optimal point suggests that the required proactive guard ring is primarily governed by the macroscopic expansion velocity and hardware setup latency, while being largely insensitive to the tested microscopic RF link conditions. Consequently, network operators may be able to upgrade modulation and coding schemes without materially recalibrating the kinematic infrastructure triggering logic, although the absolute performance levels may still change.

![](images/dbef8ad19b79896152c353f1af9e970fc5b426e3e79ea2d33b826708d8fb9a62.jpg)  
Fig. 11. Normalized effective EE versus the flux sensitivity threshold under varying SINR thresholds and spectral efficiency requirements.

## VII. DISCUSSION AND PRACTICAL LIMITATIONS

While the proposed fluid-dynamic modeling and fluxaware activation framework establish a tractable methodology for macroscopic infrastructure provisioning, certain idealized mathematical abstractions warrant further discussion regarding their practical limitations under non-ideal conditions.

1) Impact of Spatial Deployment Deviations: The theoretical framework evaluates instantaneous coverage probability and energy efficiency under the assumption of a homogeneous PPP, denoted by $\Phi _ { \mathrm { B S } }$ . In complex urban environments, base station deployments are constrained by topography and zoning laws. Stochastic geometry literature establishes that the complete spatial randomness of a PPP typically yields a conservative lower bound on coverage probability compared to planned repulsive networks. Consequently, if the actual cellular deployment exhibits a more regular grid-like pattern, the variance of the nearest-serving distance decreases, mitigating severe local interference. In such scenarios, the effective service availability improves beyond our analytical predictions. Conversely, extreme clustering of infrastructure may introduce localized coverage holes. However, the core mechanism proposed in this paper, namely, the kinematic phase-lead of the macroscopic information flux over the scalar density, is expected to remain qualitatively robust. This predictive capability is governed by the continuity equation of the fluid dynamics and is decoupled from the microscopic spatial distribution of the ground infrastructure.

2) Fluid Approximation Boundaries and Abrupt Reconfiguration: Treating the UAV swarm as a continuous compressible fluid is effective under macroscopic high-density conditions with smooth workload flows. However, the validity of this continuous fluid model relies on the cohesive movement of the logistics fleet. Under non-ideal conditions, such as abrupt swarm reconfiguration or chaotic individual trajectories, the macroscopic continuity equation loses its predictive accuracy. In these regimes, the macroscopic flux vector fails to resolve microscopic discontinuities, causing the proactive system performance to degrade toward the reactive baseline. Addressing this limitation necessitates a hybrid methodology combining macroscopic fluid dynamics with discrete multi-agent tracking in future research.

3) Impact of Estimation Noise: The current analysis assumes the accurate acquisition of macroscopic state variables. In practical deployments, sensory measurements of the swarm density and velocity fields are subject to estimation noise. Such inaccuracies in the flux estimation can induce localized false alarms or delayed infrastructure activations. Mitigating this vulnerability requires the integration of temporal smoothing techniques or predictive filters, such as Kalman filtering, prior to the flux evaluation to ensure robust activation triggers.

4) Heterogeneous Service Startup Delays: The theoretical and simulation analyses evaluate system robustness under uniform service setup latencies. Real-world infrastructure often exhibits heterogeneous startup times due to varying hardware capabilities and backhaul states across different cells. Managing such spatial heterogeneity requires extending the current framework by transforming the global scalar flux sensitivity threshold, denoted by $\delta _ { \mathrm { t h } }$ , into a spatially varying field. This adaptation allows the system to dynamically adjust the proactive guard ring on a per-cell basis according to localized hardware constraints.

5) Applicability to Geometry-Constrained Corridors: The current analytical evaluation assumes a radially symmetric Gaussian tide. In practice, UAV logistics often follow geometry-constrained flight corridors due to urban topology or airway regulations. Nevertheless, the proposed flux-induced phase-lead mechanism is expected to remain valid under such asymmetric or one-dimensional constrained trajectories. This resilience is fundamentally rooted in the continuity equation. For a 1D delivery corridor, the spatial distribution reduces to a longitudinal profile $\lambda ( x , t )$ . Driven by the conservation of mass during the expansion phase, the macroscopic advection velocity $v _ { x }$ still scales proportionally with the propagation distance x. Consequently, the information flux magnitude $\| \Phi \| ~ = ~ \lambda ~ \cdot ~ v _ { x }$ inherently decays slower than the scalar density λ at the wavefront. Thus, the spatial monotonicity as proven in Lemma 1 mathematically holds, ensuring that the flux trigger continues to generate a proactive temporal margin to compensate for service setup latency in corridorbased deployments.

## VIII. CONCLUSION

This paper has investigated the critical conflict between EE and service reliability in urban UAV logistics networks. We have shown that conventional reactive sleeping strategies yield misleadingly high nominal efficiency, a metric inadvertently resulting from the systematic shedding of the energy-intensive traffic wavefront. To resolve this misalignment, we have transcended the static snapshot limitations of classical stochastic geometry by establishing a fluid-dynamic traffic model and proposing a flux-aware asymmetric activation strategy. By exploiting the intrinsic spatial phase-lead of the information flux, our control logic generates a proactive guard ring that effectively compensates for service setup latency. Numerical results have validated that this framework achieves a zerolatency response, reducing wavefront outages from approximately 20% to near zero compared to reactive baselines. Under our derived QoS-penalized metric, the proposed strategy achieves Pareto optimality, demonstrating that integrating macroscopic kinematic states into network control loops offers a resilient pathway for aerial mobile computing systems.

## REFERENCES

[1] M. M. Azari, et al., “Evolution of non-terrestrial networks from 5G to 6G: A survey,” IEEE Commun. Surveys Tuts., vol. 24, no. 4, pp. 2633–2672, 4th Quart., 2022.

[2] G. Geraci, et al., “What will the future of UAV cellular communications be? A flight from 5G to 6G,” IEEE Commun. Surveys Tuts., vol. 24, no. 3, pp. 1304–1335, 3rd Quart., 2022.

[3] W.-Y. Dong, S. Yang, and S. Chen, “Uplink performance analysis of heterogeneous non-terrestrial networks in harsh environments: A novel stochastic geometry model,” IEEE Trans. Commun., vol. 73, no. 8, pp. 6734–6747, Aug. 2025.

[4] W.-Y. Dong, S. Yang, P. Zhang, and S. Chen, “Stochastic geometry based modeling and analysis of uplink cooperative satellite-aerial-terrestrial networks for nomadic communications with weak satellite coverage,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3428–3444, Dec. 2024.

[5] G. Wu, C. Yang, S. Li, and G. Y. Li, “Recent advances in energy-efficient networks and their application in 5G systems,” IEEE Wireless Commun., vol. 22, no. 2, pp. 145–151, Apr. 2015.

[6] W.-Y. Dong, S. Yang, P. Zhang, and S. Chen, “Modeling and performance analysis of IoT-over-LEO satellite systems under realistic operational constraints: A stochastic geometry approach,” IEEE Internet Things J., vol. 12, no. 15, pp. 30576– 30593, Aug. 2025.

[7] W.-Y. Dong, et al., “Outage probability analysis of uplink heterogeneous non-terrestrial networks: A novel stochastic geometry model,” in Proc. GLOBECOM 2024 (Cape Town, South Africa), Dec. 8–12, 2024, pp. 2588–2593.

[8] W.-Y. Dong, et al., “Stochastic geometry based performance analysis of terrestrial-to-aerial networks for nomadic communications,” in Proc. GLOBECOM 2024 (Cape Town, South Africa), Dec. 8–12, 2024, pp. 2731–2736.

[9] C. Sergiou and V. Vassiliou, “Estimating maximum traffic volume in wireless sensor networks using fluid dynamics principles,” IEEE Commun. Lett., vol. 17, no. 2, pp. 257–260, Feb. 2013.

[10] R. J. Skehill and S. McGrath, “The application of fluid mobility modelling in wireless cellular networks,” Mobile Inform. Syst., vol. 3, no. 2, pp. 89–106, Jan. 2007.

[11] C.-F. Chiasserini, et al., “Fluid models for large-scale wireless sensor networks,” Performance Evaluation, vol. 10, no. 7/8, pp. 715–736, Aug. 2007.

[12] M. Zhou, H. Chen, L. Shu, and Y. Liu, “UAV-assisted sleep scheduling algorithm for energy-efficient data collection in agricultural Internet of Things,” IEEE Internet Things J., vol. 9, no. 13, pp. 11043–11056, Jul. 2022.

[13] L. Zhang, A. Celik, S. Dang, and B. Shihada, “Energyefficient trajectory optimization for UAV-assisted IoT networks,” IEEE Trans. Mobile Comput., vol. 21, no. 12, pp. 4323–4337, Dec. 2022.

[14] H. Li, et al., “UAV assisted BS sleep strategy for green communication,” IEEE Trans. Netw. Sci. Eng., vol. 12, no. 5, pp. 3770–3783, Sep./Oct. 2025.

[15] Z. Liu, et al., “Maximizing energy efficiency in UAV-assisted NOMA–MEC networks,” IEEE Internet Things J., vol. 10, no. 24, pp. 22208–22222, Dec. 2023,

[16] A. Chowdary, Y. Ramamoorthi, A. Kumar, and L. R. Cenkeramaddi, “Joint resource allocation and UAV scheduling with ground radio station sleeping,” IEEE Access, vol. 9, pp. 124505– 124518, Sep. 2021.

[17] W. Teng, et al., “Joint optimization of base station activation and user association in ultra dense networks under traffic uncertainty,” IEEE Trans. Commun., vol. 69, no. 9, pp. 6079– 6092, Sep. 2021.

[18] X. Wang, et al., “A base station sleeping strategy in heterogeneous cellular networks based on user traffic prediction,” IEEE Trans. Green Commun. Netw., vol. 8, no. 1, pp. 134–149, Mar. 2024.

[19] G. Jang, et al., “Base station switching and sleep mode optimization with LSTM-based user prediction,” IEEE Access, vol. 8, pp. 222711–222723, Dec. 2020.

[20] A. Azari, F. Salehi, P. Papapetrou, and C. Cavdar, “Energy and resource efficiency by user traffic prediction and classification in

cellular networks,” IEEE Trans. Green Commun. Netw., vol. 6, no. 2, pp. 1082–1095, Jun. 2022.

[21] Q. Wu, et al., “Deep reinforcement learning with spatiotemporal traffic forecasting for data-driven base station sleep control,” IEEE/ACM Trans. Netw., vol. 29, no. 2, pp. 935–948, Apr. 2021.

[22] F. Baccelli and B. Błaszczyszyn, Stochastic Geometry and Wireless Networks, Part I: Theory. Now Publishers Inc.: New York, NY, USA, 2009.

[23] J. Peng, H. Tang, P. Hong, and K. Xue, “Stochastic geometry analysis of energy efficiency in heterogeneous network with sleep control,” IEEE Wireless Commun. Lett., vol. 2, no. 6, pp. 615–618, Dec. 2013.

[24] A. Shabbir, et al., “Optimizing energy efficiency in heterogeneous networks: An integrated stochastic geometry approach with novel sleep mode strategies and QoS framework,” PLoS ONE, vol. 19, no. 2, Feb. 2024, Art. no. e0296392.

[25] G. Zhao, S. Chen, and L. Hanzo, “Energy-spectral-efficient heterogeneous cellular networks: Joint optimization of crosstier inter-BS cooperation and BS deployment,” IEEE Trans. Veh. Technol., vol. 73, no. 4, pp. 5659–5673, Apr. 2024.

[26] M. Z. Win, P. C. Pinto, and L. A. Shepp, “A mathematical theory of network interference and its applications,” Proc. IEEE, vol. 97, no. 2, pp. 205–230, Feb. 2009.

[27] M. Haenggi and R. Smarandache, “Diversity polynomials for the analysis of temporal correlations in wireless networks,” IEEE Trans. Wireless Commun., vol. 12, no. 11, pp. 5940–5951, Nov. 2013.

[28] X. Lu, et al., “Stochastic geometry analysis of spatial–temporal performance in wireless networks: A tutorial,” IEEE Commun. Surveys Tuts., vol. 23, no. 4, pp. 2753–2801, 4th Quart., 2021.

[29] H. Shiri, J. Park, and M. Bennis, “Communication-efficient massive UAV online path control: Federated learning meets mean-field game theory,” IEEE Trans. Commun., vol. 68, no. 11, pp. 6840–6857, Nov. 2020.

[30] D. Chen, et al., “Mean field deep reinforcement learning for fair and efficient UAV control,” IEEE Internet Things J., vol. 8, no. 2, pp. 813–828, Jan. 2021.

[31] Y. Wang, et al., “A survey on mean-field game for dynamic management and control in space-air-ground network,” IEEE Commun. Surveys Tuts., vol. 26, no. 4, pp. 2798–2835, 4th Quart., 2024.

[32] O. Onireti, A. Mohamed, H. Pervaiz, and M. Imran, “Analytical approach to base station sleep mode power consumption and sleep depth,” in Proc. PIMRC 2017 (Montreal, QC, Canada), Oct. 8-13, 2017, pp. 1–7.

[33] D. Tse and P. Viswanath, Fundamentals of Wireless Communication. Cambridge, U.K.: Cambridge Univ. Press, 2005.

[34] 3GPP, “Enhanced LTE support for aerial vehicles,” 3rd Generation Partnership Project (3GPP), Technical Report (TR) 36.777, Release 15, Jan. 2018.

[35] L. Pan, L. Wang, S. Chen, and F. Liu, “Retention-aware container caching for serverless edge computing,” in Proc. IEEE INFOCOM (London, United Kingdom), May 2-5, 2022, pp. 1069–1078.

![](images/1d6f7b81fb496dcf4b9170546d12a472b57524f84c0c757a94a811d3e18e5626.jpg)

Wen-Yu Dong received the B.S. degree in electronic and information engineering from Sichuan University, Chengdu, China, in 2019, and the Ph.D. degree in information and communication engineering from the School of Information and Communication Engineering, Beijing University of Posts and Telecommunications, Beijing, China, in 2025. He is currently a researcher with the China Telecom Research Institute, Beijing, China. His current research interests include space-air-ground integrated networks, information theory, stochastic geometry,

and wireless communications.  
![](images/045db86abec0af0745cde597224619e04d98ad6586520dd70797094afd97936c.jpg)  
vices, and network AI.

Song Zhao is a senior engineer with the Future Technology Center, China Telecom Research Institute, Beijing, China. He received his Ph.D. degree in Telecommunications and Information Systems from Beijing University of Posts and Telecommunications, Beijing, China. He serves as a delegate of China Telecom in the 3GPP SA2 and SA5 working groups, and as rapporteur for multiple 3GPP work items related to network automation and intelligence. His research interests include wireless channel modeling, radio resource management, proximity ser-

![](images/b64dc337807dad8fe6b14dd51f08e3ea300fa38d8bc86f5740142bdedeaee3bb.jpg)

Rui-Si Han received her B.S. degree in E-Commerce and Law from Beijing University of Posts and Telecommunications, Beijing, China, in 2021, and her M.Eng. degree in Information and Communication Engineering from the same university in 2024. She is currently a researcher at the China Telecom Cloud Network Operating System R&D Center, Beijing, China. Her research interests include mobile ad hoc networks and research project management.

![](images/d9bda9b83e37971fa275f01df640e9d7f8f42b24b8d3cd9b336c2dfafc5bafad.jpg)

Qi Bi (Fellow, IEEE) is Chief Scientist of China Telecom and CTO of its Research Institute, specializing in 5G and 6G. He received his M.S. from Shanghai Jiao Tong University and Ph.D. from Pennsylvania State University. He was awarded Bell Labs Fellow in 2002, the Bell Labs President’s Gold Awards in 2000 and 2002, the Asian American Engineer of the Year in 2005, the Beijing Outstanding Contribution Award for Innovation and Entrepreneurship for Overseas Scholars in 2019, and three Patent Silver Prizes from the China National

Intellectual Property Administration from 2022 to 2024.

![](images/3811583054a17e7151ea2df0150de9ff05945c5c92c1531f51050c26791b3bcb.jpg)

Sheng Chen (Life Fellow, IEEE) received his BEng degree from the East China Petroleum Institute, Dongying, China, in 1982, and his PhD degree from the City University, London, in 1986, both in control engineering. In 2005, he was awarded the higher doctoral degree, Doctor of Sciences (DSc), from the University of Southampton, Southampton, UK. From 1986 to 1999, He held research and academic appointments at the Universities of Sheffield, Edinburgh and Portsmouth, all in UK. Since 1999, he has been with the School of Electronics and Computer

Science, the University of Southampton, UK, where he holds the post of Professor in Intelligent Systems and Signal Processing. Dr Chen’s research interests include adaptive signal processing, wireless communications, neural network and machine learning. He has published over 700 research papers. Professor Chen has 22,000+ Web of Science citations with h-index 65 and 43,000+ Google Scholar citations with h-index 87. Dr. Chen is a Fellow of the United Kingdom Royal Academy of Engineering, a Fellow of Asia-Pacific Artificial Intelligence Association and a Fellow of IET. He is one of the original 200 ISI highly cited researchers in engineering (March 2004). Professor Chen is IEEE ComSoc Signal Processing and Computing for Communications (SPCC) 2025 Technical Recognition Award recipient.