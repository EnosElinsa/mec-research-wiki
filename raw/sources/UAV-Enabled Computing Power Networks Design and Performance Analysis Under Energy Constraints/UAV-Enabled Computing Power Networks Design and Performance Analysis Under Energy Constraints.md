# UAV-Enabled Computing Power Networks: Design and Performance Analysis Under Energy Constraints

Yiqin Deng , Member, IEEE, Zhengru Fang , Graduate Student Member, IEEE,

Senkang Hu , Graduate Student Member, IEEE, Yanan Ma , Graduate Student Member, IEEE,

Xiaoyu Guo , Member, IEEE, Haixia Zhang , Senior Member, IEEE, and Yuguang Fang , Fellow, IEEE

Abstract—This paper presents an innovative framework that boosts computing power by utilizing ubiquitous computing power distribution and enabling higher computing node accessibility via adaptive UAV positioning, establishing a UAV-enabled Computing Power Network (UAV-CPN). In a UAV-CPN, a UAV functions as a dynamic relay, outsourcing computing tasks from the request zone to an expanded service zone with diverse computing nodes, including vehicle onboard units, edge servers, and dedicated powerful nodes. This approach has the potential to alleviate communication bottlenecks and overcome the “island effect” observed in multi-access edge computing. A significant challenge is to quantify computing power performance under complex dynamics of communication and computing. To address this challenge, we introduce task completion probability to capture the capability of UAV-CPNs for task computing. We further enhance UAV-CPN performance under a hybrid energy architecture by jointly optimizing UAV altitude and transmit power, where fuel cells and batteries collectively power both UAV propulsion and communication systems. Extensive evaluations show significant performance gains, highlighting the importance of balancing communication and computing capabilities, especially under dual-energy constraints. These findings underscore the potential of UAV-CPNs to significantly boost computing power.

Digital Object Identifier 10.1109/TMC.2026.3655118

Index Terms—Computing power networks, low-altitude economy, unmanned aerial vehicle (UAV), task completion probability, edge computing.

## I. INTRODUCTION

intensive applications, such as augmented reality and autonomous driving [2], [3], has intensified the demand for ubiquitous connected networks that seamlessly integrate communication and distributed computing capabilities [4]. While multi-access edge computing (MEC) architectures have expanded computing capability at the network edge [5], [6], existing computing resources remain geographically fragmented, leading to resource under-utilization and creating isolated computing power islands, known as “island effect” [7]. The computing power network (CPN) initiative aims to interconnect these islands via computation-aware networking, but faces challenges in accessibility, cost-efficiency, and resilience, especially during disasters or traffic peaks [7], [8]. Specifically, one major challenge is the communication bottleneck in providing ground users (GUs) with viable access to computing power on a wide range of mobile devices and in accessing isolated computing power islands (e.g., edge servers, computing clusters, and user-provided computing nodes). Another challenge is the cost associated with the ubiquitous deployment of computing nodes (CNs), and it is not cost-effective to deploy fixed edge servers to handle infrequently occurring local computing demands [7], [9]. In addition, during events such as disasters or rush hours [10], [11], where infrastructure may fail or computing resources become insufficient, these challenges are further exacerbated. Inaccessibility to computing resources can have devastating consequences [12].

Unmanned aerial vehicles (UAVs) offer a promising solution due to their rapid deployment, flexible 3D mobility, line-of-sight (LoS) connectivity, and on-demand provisioning of communication and computing services [4], [13], [14], [15]. UAV-assisted MEC has been widely studied [9], [16], [17], [18], [19], [20], [21], typically under the assumption of static CN accessibility, where the number and locations of available CNs are fixed and independent of a UAV’s position. This rigid assumption fundamentally limits scalability and fails to exploit the vast pool of spatially distributed computing resources (e.g., edge servers, connected autonomous vehicles, and user devices) that may become accessible under favorable UAV deployment and latency

Zhengru Fang, Senkang Hu, Yanan Ma, and Yuguang Fang are with the Hong Kong JC STEM Lab of Smart City and Department of Computer Science, City University of Hong Kong, Kowloon, Hong Kong SAR, China (e-mail: zhefang4-c@my.cityu.edu.hk; senkang.forest@my.cityu.edu.hk; yananma8-c@my.cityu.edu.hk; my.fang@cityu.edu.hk).

Haixia Zhang is with the Institute of Intelligent Communication Technologies, Shandong University, Jinan, Shandong 250061, China, and also with the Shandong Key Laboratory of Intelligent Communication and Sensing-Computing Integration, Shandong University, Jinan, Shandong 250061, China (e-mail: haixia.zhang@sdu.edu.cn).

conditions [22]. As a result, existing models cannot fully capture the opportunistic nature of resource integration in large-scale or infrastructure-scarce environments.

In contrast, we propose a novel paradigm: UAV-enabled Computing Power Networks (UAV-CPNs), where UAVs serve as dynamic aerial relays that adaptively connect spatially distributed and heterogeneous computing resources on demand into a unified service network architecture. Particularly, the set of accessible CNs is not predetermined; instead, it is dynamically shaped by a UAV’s 3D positioning and the end-to-end (E2E) latency requirements of tasks. This dynamic accessibility to computing resources enables more efficient utilization of ubiquitous but spatially distributed dynamic computing resources, especially in large-scale or infrastructure-scarce scenarios.

However, this flexibility introduces new modeling and optimization challenges. For instance, UAV altitude affects multiple performance dimensions. On the one hand, higher altitudes increase the existence probability of LoS links between GUs and the UAV, improving uplink reliability for GU-to-UAV task offloading and extending downlink reachability to remote CNs. On the other hand, increased altitude also leads to higher path loss and transmission delay due to longer propagation distances, degrading signal quality and increasing communication latency. Consequently, the optimal altitude that maximizes uplink rates may be suboptimal for UAV-to-CN forwarding and hence for overall task completion, as downlink performance depends on UAV-CN channel quality and CN accessibility, both of which are particularly sensitive to UAV positioning. These interdependent trade-offs create a complex optimization landscape, particularly in the vertical dimension, which remains underexplored in the current literature. In this paper, we therefore take the altitude as the primary geometric degree of freedom, while modeling the horizontal spatial variability of GUs and CNs statistically via homogeneous point processes. This leads to a horizontally homogeneous large-scale network model in which the absolute horizontal coordinates of the UAV are abstracted into spatial distributions, and the altitude emerges as the key deterministic parameter that shapes the GU–UAV and UAV–CN distance distributions, LoS/NLoS probabilities, and dual-energy consumption. Our focus on the vertical dimension provides a first-step towards the theoretical understanding of UAV-CPNs and is complementary to existing studies that fix the UAV altitude and optimize only the horizontal placement or trajectory in finite-user scenarios.

In addition to this complexity, practical UAV-CPNs must support extended operational durations under high service demands. Hybrid fuel cell and battery-powered systems, such as hydrogen fuel cell powered UAVs [23], are increasingly favored over conventional battery-only UAVs for their higher energy density and longer endurance [24]. In such hybrid architectures, the fuel cell and battery are typically integrated in serial, parallel, or decoupled configurations, each with distinct energy management strategies. The fuel cell, benefiting from its high energy density, serves as the primary power source for sustained propulsion and may also recharge the battery in certain designs. In contrast, the battery acts as a secondary energy buffer, delivering high-power bursts to support communication and control subsystems. This dual-power architecture enables UAV-CPNs to simultaneously support prolonged flight and intensive task computing. However, it also introduces dual-energy constraints: the task may fail if either the fuel cell energy or the battery capacity is depleted. In contrast with conventional battery-powered UAV networks [25], [26], [27], [28], where propulsion dominates energy consumption and communication energy is often negligible, hybrid systems require fine-grained coordination between the two energy sources. In this context, communication energy consumption becomes a critical factor and can no longer be ignored. As a result, performance bottlenecks may arise in communication, computing, or energy domain (propulsion or communication power), potentially leading to task failure. This necessitates a holistic optimization framework in which both UAV deployment and resource allocation are jointly designed to maximize system performance, considering not only computing task scheduling but also the efficient management of dual-energy supplies.

In summary, this is the first work to model and optimize UAV-CPNs under dynamic CN accessibility and dual-energy constraints. The main contributions are summarized as follows:

\- A novel UAV-CPN framework: We propose a spatially dynamic model where the set of accessible CNs is determined by a UAV’s positioning and task latency requirements. This model enables opportunistic integration of geographically distributed computing resources, breaking the “island effect” of conventional static-access computing architectures. Focusing on a foundational scenario involving a single UAV and its vertical positioning, we define task completion probability as the critical performance metric and develop an analytical procedure to obtain the performance metric.

\- Joint optimization under dual-energy budgets: For practical hybrid fuel cell and battery-powered UAV scenarios, we introduce novel propulsion and communication energy models for UAV-CPNs. Under these dual-energy models, we formulate a task completion probability maximization problem subject to both fuel (for propulsion) and battery (for communication) energy constraints. Moreover, we design a computationally efficient algorithm to jointly optimize UAV transmit power and altitude.

Performance evaluation and insights: Through extensive numerical analysis, we verify the accuracy of our analytical model and uncover trade-offs between communication parameters (e.g., UAV altitude and transmit power) and computing parameters (e.g., CN density and coverage), highlighting potential bottlenecks in resource allocation. Under energy constraints, we quantify the performance gains from joint power-altitude optimization compared to single-parameter optimization and static strategies. These findings provide concrete guidelines for network deployment.

The remainder of this paper is organized as follows. Section II reviews related works and Section III introduces the proposed architecture. Section IV develops an analytical framework for key performance metrics. Building on this foundation, Section V analyzes system performance under energy constraints and presents solutions for joint optimization. Section VI provides comprehensive numerical evaluations to validate theoretical findings and quantify performance gains through parameter optimization. Finally, Section VII concludes the paper.

## II. RELATED WORKS

In this section, we only review research works closely related to this paper in two aspects: UAV-assisted MEC frameworks and energy-constrained UAV optimization.

## A. UAV-Assisted Computing Framework

Numerous studies have focused on user association, computation offloading, and resource allocation in various UAVassisted MEC systems with UAVs serving as relay nodes [29], [30], [31], aerial edge servers [17], [18], [32], [33], and/or both [19], [34], [35]. These works have addressed design challenges, including energy consumption minimization, latency reduction, and task throughput enhancement. Recent research has also explored UAV-assisted CPNs, which is essentially a form of traditional UAV-assisted MEC systems. These CPNs are characterized by greater heterogeneity and dynamics in their computing resources, encompassing CPUs, GPUs, and TPUs, respectively [9], [21]. However, most of these studies assume that the set of available CNs remains fixed and predetermined, regardless of a UAV’s deployment location or the spatial distribution of computing resources. This static CN accessibility model significantly limits the system’s ability to leverage computing resources that are spatially distributed outside the immediate task request area. As a result, it leads to a mismatch between computing demand and supply, especially in scenarios where the local computing infrastructure is insufficient or unavailable [36]. This limitation is particularly critical in post-disaster situations, where UAVs must dynamically access computing resources outside the damaged geographic area to support mission-critical tasks.

In contrast to these works, our model does not assume a fixed set of CNs. Instead, the effective set of computing nodes accessible to UAVs is dynamically determined by their deployment position and the task’s E2E latency requirement. This approach enables UAVs to opportunistically access distributed computing resources across a large spatial area, thereby enhancing the flexibility and efficiency of UAV-assisted computing systems.

## B. Energy-Constrained UAV Optimization

Many research works also investigate methods to improve system performance, including perception, communication, and computing in UAV-assisted wireless networks under energy constraints through 3D trajectory design and resource allocation [13], [25], [26], [27], [28], [37], [38], [39]. In these studies, typical electric (battery-only) UAVs are adopted to support system operations, where the energy consumed in propelling UAVs significantly dominates that consumed in communication or/and computation, making propulsion the primary energy consumer. Indeed, many existing studies neglect transmission power altogether [40]. Although in [32], Lin et al. consider using a solar-powered UAV as an edge server to perform data collection and processing, where the amount of the harvested solar energy increases with flying altitude, but they only address the tradeoff between energy harvesting and communication performance. Similar to other studies, communication-related energy consumption has not been taken into consideration. With the advent of hybrid fuel cell and battery-powered UAVs, such as hydrogen fuel cell powered UAVs [23], a novel paradigm has emerged where both fuel cells and batteries are utilized to power propulsion, communication, and control modules. Depending on the energy management topology, whether the fuel cell and battery are configured in series or in parallel, the efficiency of energy utilization can vary [24]. Unlike traditional battery-powered UAVs, in this new paradigm, transmission energy consumption becomes crucial for system sustainability and must be considered alongside UAV deployment and resource allocation. Failure in either energy source, fuel or battery, can lead to task failure. Building on this, Zhang et al. [40] defined the energy efficiency in a hybrid fuel-powered UAV-relay transmission system as the ratio of transmitted data to total energy consumption, optimizing UAV trajectories and node transmission power to maximize the average energy efficiency during each time slot. However, no prior work has investigated computing performance within hybrid fuel cell and battery-powered UAV systems, where computing capability and communication conditions are closely intertwined with UAV deployment and resource allocation.

Compared to existing studies, this paper is the first to consider the use of UAVs to enable broader accessibility of potentially remote ubiquitous computing nodes both within and beyond the service request area (i.e., the request zone), thereby optimizing task computing efficiency. Considering the duration requirements of UAV operations, we adopt hybrid fuel cell and battery-powered UAVs, where both propulsion and communication energy consumption are jointly considered. This approach consequently introduces a unique challenge of balancing the communication-computing-energy tradeoff. Failure to address this balance could create systematic bottlenecks, leading to inefficiencies or failures in task computing.

## III. MODELING UAV-CPNS

In this section, we present the foundational framework for UAV-CPNs by modeling the core components: the network spatial model, air-ground channel model, and computing model. These models collectively provide the analytical basis for subsequent performance analysis.

To simplify the analysis for analytical tractability, we adopt a single-UAV with a single-CN system, which is to establish a theoretical performance floor for the system, providing a conservative performance benchmark that deliberately excludes performance gains from multi-CN parallel processing, a common optimization strategy in existing literature [36]. The proposed UAV-CPN framework itself is not restricted to this single-CN setting and, in principle, supports multi-CN parallel and cooperative processing; a more comprehensive treatment of joint CN selection and task partitioning will be left for future work.

## A. Network Spatial Model

To establish a tractable analytical framework for UAV-CPNs, we consider a single UAV-assisted computing scenario as shown in Fig. 1. A circular region of radius $R _ { u }$ , referred to as the request zone, contains GUs that generate computation tasks. The locations of GUs are modeled as an independent uniform point process within the request zone.

![](images/9b3e3370672785a673272d8fb3c883f945decba8dbbb8fc049813cdbc2cde662.jpg)  
Fig. 1. Illustration of a UAV-enabled computing power network, where GUs offload tasks generated within the service area to distributed computing power nodes for processing. The computing accessibility is enhanced by strategically adjusting key network parameters, e.g., the position of the aerial UAV relay.

Computing nodes (CNs), on the other hand, are distributed over an unbounded plane, referred to as the service zone, and are assumed to follow a homogeneous spatial Poisson Point Process (PPP) $\Phi _ { C }$ with density $\lambda _ { c } ~ ( \mathrm { n o d e s } / \mathrm { m } ^ { 2 } )$ . The spatial distributions of GUs and CNs are mutually independent, reflecting the independence between task generation and CN availability. Unlike conventional works that assume a fixed number and known locations of CNs, our proposed model reflects the spatial randomness and ubiquity of distributed computing resources. Importantly, the set of CNs accessible to the UAV is not fixed in advance, but is dynamically determined based on the UAV’s deployment position and the task’s E2E latency requirements.

We assume that a hybrid fuel cell and battery-powered rotarywing UAV is deployed at altitude <sup>h</sup> above the center of the request zone. It acts as an aerial relay to support two-way computation offloading between GUs and remote CNs. The effective service zone accessible by a UAV is determined by both the UAV’s communication range and the E2E latency requirements. Specifically, only those CNs that can satisfy the E2E latency constraints are considered valid candidates for task forwarding.

Let the UAV-to-CN distance be denoted as $d _ { u , c } ,$ and the GUto-UAV distance as $d _ { g , u } .$ . The total E2E latency for a task from a GU to a selected CN via the UAV is given by:

$$
T _ { \mathrm { t o t a l } } = T _ { \mathrm { o f f l o a d } } + T _ { \mathrm { f o r w a r d } } + T _ { \mathrm { c o m p u t e } } + T _ { \mathrm { r e t u r n } } ,\tag{1}
$$

where $T _ { \mathrm { o f f l o a d } }$ is the GU-to-UAV transmission time, $T _ { \mathrm { f o r w a r d } }$ is the UAV-to-CN transmission time, $T _ { \mathrm { c o m p u t e } }$ is the CN computing time, and $T _ { \mathrm { r e t u r n } }$ is the result return time from CN to GU. To ensure quality-of-service (QoS) compliance, we define a maximum allowable latency budget $T _ { \mathrm { m a x } }$ such that

$$
T _ { \mathrm { t o t a l } } \leq T _ { \mathrm { m a x } } .\tag{2}
$$

This constraint limits the maximum UAV-to-CN distance (i.e., the maximum service zone radius) $d _ { u , c } ^ { \operatorname* { m a x } }$ , and consequently defines the effective size of the service zone accessible by the UAV. Specifically, $d _ { u , c } ^ { \operatorname* { m a x } }$ is determined by the worst-case combination of $d _ { g , \cdot }$ and $d _ { u , c }$ under the constraint in (2).

Under the PPP assumption, the expected number of CNs within a subregion A of the service zone is [41]:

$$
\mathbb { E } [ N _ { \mathrm { C N } } ( \mathcal { A } ) ] = \lambda _ { c } \cdot \vert \mathcal { A } \vert ,\tag{3}
$$

where $| { \cal { A } } |$ denotes the area of A. Similarly, the expected number of GUs in a subregion of the request zone is determined by the GU density and the subregion area. At the framework level, all CNs located within the service zone and satisfying the latency constraint in (2) are treated as potential candidates for serving offloaded tasks, so that a GU is not restricted to receiving service from a pre-specified single node. In the subsequent analysis, we will specialize this general spatial model to a simplified single-CN benchmark scenario in order to develop a tractable performance analysis framework and gain fundamental insights into the system behavior.

## B. Air-Ground Channel Model

Following [42], we adopt a probabilistic air-ground channel model to characterize the mixture of line-of-sight (LoS) and non-line-of-sight (NLoS) channels for both the GU-to-UAV task offloading link and the UAV-to-CN task forwarding link. This model is widely used in the current literature on UAV communications to capture the aggregate impact of multipath propagation in diverse complex urban environments, where signal reflections, diffractions, and scattering significantly affect transmission quality, while still providing a tractable basis for performance analysis.

In the GU-to-UAV task offloading phase, the probability that the link is LoS is given by [42]:

$$
P _ { \mathrm { L o S , u p } } = \frac { 1 } { 1 + C \exp { \left( - B \left( \frac { 1 8 0 } { \pi } \arctan \left( \frac { h } { r _ { u } } \right) - C \right) \right) } } ,\tag{4}
$$

where <sup>B</sup> and <sup>C</sup> are environment-dependent parameters that reflect the urban or rural landscape’s impact on LoS existence probability. The GU-to-UAV channel model is then characterized as:

$$
\begin{array} { r } { P _ { r , \mathrm { u p } } = \left\{ \begin{array} { l l } { P _ { u } \cdot \left( r _ { u } ^ { 2 } + h ^ { 2 } \right) ^ { - \alpha _ { u } / 2 } } & { \mathrm { w i t h } \ : P _ { \mathrm { L o S , u p } } , } \\ { \eta P _ { u } \cdot \left( r _ { u } ^ { 2 } + h ^ { 2 } \right) ^ { - \alpha _ { u } / 2 } } & { \mathrm { w i t h } \ : 1 - P _ { \mathrm { L o S , u p } } , } \end{array} \right. } \end{array}\tag{5}
$$

where $P _ { u }$ is the GU transmit power, $r _ { u }$ is the horizontal GU– UAV distance, $\alpha _ { u }$ is the uplink path-loss exponent, and $\eta \in$ (0<sup>,</sup> 1) is the NLoS attenuation factor that accounts for additional signal degradation due to multipath effects such as scattering and reflection.

Analogously, for the UAV-to-CN task forwarding, the received power at a CN, denoted as $P _ { r , \mathrm { d o w n } } ,$ can be modeled based on the transmit power of the UAV $P _ { d } .$ , the horizontal UAV-CN distance $r _ { c } ,$ and the downlink path loss exponent $\alpha _ { c } .$ . Thus, the UAV-to-CN channel can be characterized similarly to the GU-to-UAV channel as in (5).

The proposed framework is also compatible with more general wireless fading models. While the current analysis focuses on the above probabilistic LoS/NLoS air–ground channel model for analytical clarity, it can be extended to incorporate small-scale fading effects such as Rayleigh, Rician, or Nakagami fading by introducing random channel gain terms in (5). For a given fading model, these gains follow known distributions, and the task completion probability expressions developed in Section IV retain the same functional structure, with the deterministic receivedpower terms replaced by their averages over their fading distribution. This leads to one-dimensional (or low-dimensional) integrals that can be efficiently evaluated numerically within our semi-analytical performance analytic framework, instead of closed-form solutions. Therefore, extending the channel model to include more general fading remains computationally feasible and does not change the order of complexity of the proposed derivation and optimization algorithm, while allowing the framework to capture both large-scale path loss and small-scale signal fading due to multipath propagation and thereby enhancing its applicability to diverse wireless environments.

## C. Computing Model

We consider heterogeneous CNs cooperatively operated by multiple service providers or CN node owners, where some factors such as hardware heterogeneity, queuing delays, and I/O interference among virtual machines collectively influence computational throughput [43]. To generically model the dynamic computing capabilities of CNs, reflecting their uncertainty as well, we characterize the computation time $t _ { c }$ through its cumulative distribution function (CDF):

$$
F _ { t _ { c } } ( t ; D ) = \mathbb { P } ( t _ { c } \leq t ) ,\tag{6}
$$

where <sup>t</sup> represents the available time budget for task completion, and <sup>D</sup> denotes the task-specific computational workload. This CDF quantifies the probability that a CN completes the task within the given time budget <sup>t</sup> with workload <sup>D</sup>.

## IV. TASK COMPLETION PROBABILITY ANALYSIS

To derive tractable analytical insights from the general UAV-CPN model introduced in Section III, in this section, we focus on a simplified baseline scenario where a UAV deployed at altitude <sup>h</sup> above the centroid of a circular request zone with radius $R _ { u }$ forwards a typical single GU’s computational tasks (with data size <sup>D</sup>) to a single randomly selected CN within the service zone.

This single-CN specialization is adopted solely for analytical tractability and to establish a theoretical performance floor for the system, providing a conservative performance benchmark that deliberately excludes performance gains from multi-CN parallel processing, a common optimization strategy in the existing literature [36]. The proposed UAV-CPN framework itself is not restricted to this single-CN setting and, in principle, supports multi-CN parallel and cooperative processing; a more comprehensive treatment of joint CN selection and task partitioning is left for future work.

To investigate the fundamental communication-computing tradeoff, we adopt idealized conditions without consideration of multi-user interference and resource contention, as commonly done in the current literature. We begin with modeling the E2E latency for task computing in our UAV-CPN framework. Building on this model, we formally define the task completion probability and derive a semi-analytical expression for a GU at an arbitrary location within the request zone. We then obtain the average value of this metric by spatially averaging over all GU positions to characterize system-wide performance, which is equal to the task completion rate or task throughput defined as in MEC systems [5], [22]. Although closed-form expressions in elementary functions are generally unavailable, the resulting one- and two-dimensional integrals can be efficiently evaluated numerically within our performance analytic framework. Through this semi-analytical analysis, we reveal the fundamental trade-offs among several critical parameters such as CN density $\lambda _ { c } , \mathrm { U A V }$ operational altitude $h ,$ and latency budget $T _ { \mathrm { m a x } }$ The numerical results based on this framework demonstrate how these parameters jointly determine the operational success of UAV-CPN task computing, yielding actionable design insights for latency-sensitive applications.

## A. End-to-End Latency

Given the bandwidth <sup>W</sup> and noise power $N _ { 0 } .$ , the transmission latency from a GU to the $\mathrm { U A V } \left( t _ { 1 } \right)$ can be calculated by:

$$
t _ { 1 } = \frac { D } { W \log _ { 2 } { ( 1 + P _ { r , \mathrm { u p } } / N _ { 0 } ) } } .\tag{7}
$$

Similarly, the transmission latency from the UAV to a CN (<sup>t</sup>2) can be calculated by:

$$
t _ { 2 } = \frac { D } { W \log _ { 2 } \left( 1 + P _ { r , \mathrm { d o w n } } / N _ { 0 } \right) } .\tag{8}
$$

The E2E latency represents the total time from task generation at the GU to the result reception. As assumed in most prior works, we ignore result feedback latency due to the small size of the result, yielding the total E2E latency as $T _ { \mathrm { E 2 E } } = t _ { 1 } + t _ { 2 } + t _ { c }$

## B. Performance Metric

The task completion probability serves as a critical performance metric, reflecting both the communication and computational capabilities of the system, which can be used to compute other performance metrics. For a specific GU, we define the task completion probability as the likelihood of locating a CN within the service zone to complete the computing task at this CN within the E2E latency constraint. Specifically, this means that the condition $t _ { 1 } + t _ { 2 } + t _ { c } \leq T _ { \operatorname* { m a x } }$ is satisfied. For system-wide analysis, this metric should be spatially averaged over all GU and CN positions governed by their respective distributions.

If $t _ { 1 } + t _ { 2 } \geq T _ { \mathrm { m a x } } ,$ the accumulated transmission latency across the $G U / / O { - } U A V$ task offloading and UAV-to-CN task forwarding phases exceeds the latency budget, resulting in a communication bottleneck, termed the comm-limited scenario. Instead, if $t _ { c } \ge T _ { \mathrm { m a x } } - t _ { 1 } - t _ { 2 }$ , the computational latency at the CN exceeds the residual time budget $T _ { \mathrm { r e s } }$ , resulting in a computational bottleneck termed the comp-limited scenario. Task completion probability necessitates the concurrent fulfillment of both communication and computing constraints. Violation of either constraint, whether comm-limited or comp-limited, severely degrades system performance. Leveraging stochastic geometry, we derive analytical expressions for the task completion probability, which is the computing power performance metric we will use to derive other performance metrics.

## C. Bottleneck Analysis

In this subsection, we derive the task completion probability. For a GU at horizontal distance $r _ { u }$ from the UAV, the latency constraint $T _ { \mathrm { m a x } }$ fundamentally limits service accessibility despite the theoretical availability of all CNs in UAV-CPNs. Specifically, the comm-limited condition imposes a critical spatial restriction by bounding the maximum radius $r _ { c } ^ { \operatorname* { m a x } } ( r _ { u } )$ for the effective service zone, which is determined by:

$$
t _ { 2 } = t _ { 2 } \left( r _ { c } ^ { \operatorname* { m a x } } ( r _ { u } ) \right) = T _ { \operatorname* { m a x } } - t _ { 1 } ( r _ { u } ) ,\tag{9}
$$

where $t _ { 1 } = t _ { 1 } ( r _ { u } )$ and $t _ { 2 } = t _ { 2 } ( r _ { c } )$ are the transmission times for GU-to-UAV task offloading and UAV-to-CN task forwarding, respectively.

Within this communication-constrained service zone $( r _ { c } \le$ $r _ { c } ^ { \operatorname* { m a x } } ( r _ { u } ) )$ , CNs must additionally satisfy the computing latency requirement. For residual time budget $T _ { \mathrm { r e s } } \triangleq T _ { \mathrm { m a x } } - t _ { 1 } - t _ { 2 }$ , the probability of a CN satisfying this latency constraint is quantified through its CDF as $F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D )$ , as characterized by Eq. (6).

Based on the previous analysis, we establish that task completion fails under either comm-limited or comp-limited conditions. Specifically, transmission failure occurs when CNs reside outside the communication-constrained service zone $( r _ { c } \le$ $r _ { c } ^ { \operatorname* { m a x } } ( r _ { u } ) )$ , leading to failure in task computing during the transmission phase. For successfully transmitted tasks, the task completion probability equals the likelihood of satisfying the computing latency requirement within the residual time budget $T _ { \mathrm { r e s } }$ . These dual constraints induce a probabilistic thinning [44] of the original homogeneous PPP $\Phi _ { c } ,$ producing a thinned PPP with spatially varying density. The resulting effective CN density is formally characterized in Proposition IV.1.

Proposition IV.1 (Effective CN Density): For a GU at a horizontal distance $r _ { u }$ from the UAV, the spatial density of CNs satisfying E2E latency constraint, simply called effective density or conditional spatial density, is given by:

$$
\begin{array} { r } { \lambda _ { c } ^ { \mathrm { e f f } } ( r _ { u } ) = \lambda _ { c } \mathbb { I } _ { \{ r _ { c } \leq r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) \} } \cdot F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D ) , } \end{array}\tag{10}
$$

where $\mathbb { I } _ { \{ r _ { c } \leq r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) \} }$ indicates successful communication; $F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; \tilde { D } )$ , as the CDF of computing latency, quantifies the probability of computing latency within $T _ { \mathrm { r e s } }$

Proof: A qualified CN must be located within the maximum coverage radius $r _ { c } ^ { \mathrm { m a x } } ( r _ { u } )$ for the service zone and have a computing latency $t _ { c } \leq T _ { \mathrm { r e s } } ,$ . The former condition is modeled by an indicator function, referred to as success in communication. The latter models the probability that a CN satisfies the computing latency constraint, referred to as success in computing. Since the spatial distribution and computing power dynamics are independent, the density of qualified CNs for task completion is the product of these two quantities. Thus, each CN at distance $r _ { c }$ is retained with probability:

$$
\begin{array} { r } { p _ { \mathrm { r e t a i n } } ( r _ { u } ) = \underbrace { \mathbb { I } _ { \{ r _ { c } \leq r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) \} } } _ { \mathrm { S u c c e s s i n c o m m u n i c a t i o n } } \cdot \underbrace { F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D ) } _ { \mathrm { S u c c e s s i n c o m p u t i n g } } . } \end{array}\tag{11}
$$

This qualification process represents an independent thinning of the original PPP $\Phi _ { c } .$ By the Poisson thinning property [44], the

resulting spatially thinned process retains the PPP property with effective density:

$$
\lambda _ { c } ^ { \mathrm { e f f } } ( r _ { u } ) = \lambda _ { c } \cdot p _ { \mathrm { r e t a i n } } ( r _ { c } ) .\tag{12}
$$

Since the thinning process preserves the PPP properties, the qualified CNs form a thinned PPP with effective density $\lambda _ { c } ^ { \mathrm { e f f } } ( r _ { u } )$ The expected number of qualified CNs is derived by integrating this effective density over the spatial domain of interest, as formalized in Proposition IV.2.

Proposition IV.2 (The Qualified Number of CNs): The expected number of qualified CNs for a GU located at a horizontal distance $r _ { u }$ from the UAV is given by:

$$
\Lambda ( r _ { u } ) = 2 \pi \lambda _ { c } \int _ { 0 } ^ { r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) } F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D ) r _ { c } d r _ { c } .\tag{13}
$$

Proof: The expected number of qualified CNs is derived from the intensity measure of the thinned PPP:

$$
\Lambda = \int \int _ { \mathbb { R } ^ { 2 } } \lambda _ { c } ^ { \mathrm { e f f } } ( \| \pmb { x } \| ) d \pmb { x } .\tag{14}
$$

Exploiting circular symmetry about the UAV, we convert to polar coordinates $( d \pmb { x } = r _ { c } d r _ { c } d \theta ) \colon$

$$
\begin{array} { c } { { \Lambda ( r _ { u } ) = \displaystyle \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) } \lambda _ { c } ^ { \mathrm { e f f } } ( r _ { c } ) r _ { c } d r _ { c } d \theta } } \\ { { = 2 \pi \lambda _ { c } \displaystyle \int _ { 0 } ^ { r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) } F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D ) r _ { c } d r _ { c } . } } \end{array}\tag{15}
$$

## D. Task Completion Probability

Based on the previous analysis, the task completion probability for a specific GU is summarized in Theorem IV.1.

Theorem IV.1: For a GU located at a horizontal distance $r _ { u }$ from the UAV, the probability that at least one CN satisfying the E2E latency constraint $t _ { 1 } + t _ { 2 } + t _ { c } \leq T _ { \operatorname* { m a x } }$ can be found is given by:

$$
\begin{array} { l l } { \displaystyle P _ { \mathrm { s u c c e s s } } ( \boldsymbol { r } _ { u } ) = 1 - \exp \biggl ( - 2 \pi \lambda _ { c } } \\ { \displaystyle \times \int _ { 0 } ^ { r _ { c } ^ { \mathrm { m a x } } ( r _ { u } ) } F _ { t _ { c } } \left( T _ { \mathrm { m a x } } - t _ { 1 } ( r _ { u } ) - t _ { 2 } ( r _ { c } ) ; D \right) r _ { c } \mathrm { d } r _ { c } \biggr ) , } \end{array}\tag{16}
$$

where $t _ { 1 } ( r _ { u } ) , t _ { 2 } ( r _ { c } ) , r _ { c } ^ { \operatorname * { m a x } } ( r _ { u } )$ , and $F _ { t _ { c } } ( T _ { \operatorname* { m a x } } - t _ { 1 } ( r _ { u } ) -$ $t _ { 2 } ( r _ { c } ) ; D )$ are obtained from $( 5 ) \AA { - } ( 9 )$ when the GU is located at a horizontal distance $r _ { u }$ from the UAV.

Proof: From Proposition IV.2, the number of qualified CNs, for a GU located at a horizontal distance $r _ { u }$ from the UAV, follows a Poisson distribution with mean $\Lambda ( r _ { u } )$ . The void probability (i.e., no qualified CNs exist) is $\exp ( - \Lambda ( r _ { u } ) )$ [41]. Thus, the success probability, which is the probability that there exists at least one CN that can complete the task, is given by: $P _ { \mathrm { s u c c e s s } } ( r _ { u } ) = 1 - \exp ( - \Lambda ( r _ { u } ) )$ . Substituting $\Lambda ( r _ { u } )$ from Eq. (13), we can complete the proof. ■

Remark: (GU Location Dependency and CN Density Impact): From Theorem IV.1, we observe that for a given UAV with altitude $h ,$ the success probability $P _ { \mathrm { s u c c e s s } } ( r _ { u } )$ decreases as the GU’s distance $r _ { u }$ from the UAV increases. This decrease occurs because GUs farther from the UAV experience longer offloading delays $( t _ { 1 } \propto \log ( r _ { u } ^ { 2 } + h ^ { 2 } ) )$ ), which reduces the residual time budget available for forwarding $( t _ { 2 } )$ and computing $\left( t _ { c } \right)$ . Moreover, for a given GU location, a higher CN density $\lambda _ { c }$ increases the spatial availability of CNs, thereby improving the task completion probability. Specifically, the task completion probability improves exponentially with the void probability obtained from PPP, given by $\exp ( - \Lambda ( r _ { u } ) )$ ).

To evaluate system-level performance, we must consider the spatial distribution of GUs. The overall task completion probability, accounting for these factors, is provided in the following result (Theorem IV.2).

Theorem IV.2: The spatially averaged task completion probability for GUs uniformly distributed within the request zone (with radius ${ \cal R } _ { u } )$ is given by:

$$
\overline { { P } } _ { \mathrm { s u c c e s s } } = \frac { 2 } { R _ { u } ^ { 2 } } \int _ { 0 } ^ { R _ { u } } P _ { \mathrm { s u c c e s s } } ( r _ { u } ) \cdot r _ { u } d r _ { u } ,\tag{17}
$$

where $P _ { \mathrm { s u c c e s s } } ( r _ { u } )$ is defined in Eq. (16).

Proof: Owing to the uniform spatial distribution of GUs, the radial distance $r _ { u }$ follows the probability density function (PDF):

$$
f _ { r _ { u } } ( r _ { u } ) = \frac { 2 r _ { u } } { R _ { u } ^ { 2 } } , 0 \leq r _ { u } \leq R _ { u } .\tag{18}
$$

By the law of total probability, the system-wide task completion probability equals the expectation of $P _ { \mathrm { s u c c e s s } } ( r _ { u } )$ over this distribution:

$$
\overline { { P } } _ { \mathrm { s u c c e s s } } = \mathbb { E } _ { r _ { u } } \left[ P _ { \mathrm { s u c c e s s } } ( r _ { u } ) \right] = \int _ { 0 } ^ { R _ { u } } P _ { \mathrm { s u c c e s s } } ( r _ { u } ) f _ { r _ { u } } ( r _ { u } ) d r _ { u } .\tag{19}
$$

Substituting $f _ { r _ { u } } ( r _ { u } )$ , we can complete the proof.

Remark (Analytical Intractability): The nested integrals in $\overline { { P } } _ { \mathrm { s u c c e s s } }$ cause the difficulty in obtaining closed-form solutions due to three fundamental challenges. First, the coverage radius $r _ { c } ^ { \operatorname* { m a x } } ( r _ { u } )$ of the communication-effective service zone exhibits implicit nonlinear dependence on $r _ { u }$ via the latency constraint (9), coupling with the integration domains of GU and CN locations. This interdependency prevents decoupling into separable integrals over $r _ { u }$ and $r _ { c } .$ Second, the residual time budget $T _ { \mathrm { r e s } } = T _ { \mathrm { m a x } } - t _ { 1 } ( r _ { u } ) - t _ { 2 } ( r _ { c } )$ within the integrand $F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D )$ inherits complexity from both components: $t _ { 1 } ( r _ { u } )$ contains a logarithmic term log $( r _ { u } ^ { 2 } + h ^ { 2 } )$ , while $t _ { 2 } ( r _ { c } )$ , though ostensibly a function of $r _ { c } .$ , indirectly depends on $r _ { u }$ through the latency-constrained integration upper limit $r _ { c } ^ { \operatorname* { m a x } } ( r _ { u } )$ . Third, the computing latency CDF $F _ { t _ { c } } ( T _ { \mathrm { r e s } } ; D )$ itself could be non-trivial. For instance, if $t _ { c }$ includes the queueing delays in stochastic computing systems, its CDF may lack explicit analytical closed forms. These intertwined nonlinearities in spatial, temporal, and statistical dimensions lead us to resort to numerical integration techniques or stochastic geometry-based approximations for practical evaluation. Despite this analytical intractability in terms of closed-form expressions, the integrals in $P _ { \mathrm { s u c c e s s } } ( r _ { u } )$ and ${ \overline { { P } } } _ { \mathrm { s u c c e s s } }$ remain low-dimensional and can be efficiently evaluated using standard numerical quadrature, which is the approach adopted in our performance evaluation. Moreover, when more general air–ground channels with small-scale fading are considered, the proposed framework can be extended by introducing random channel gains into the received-power expressions and taking expectations over their distributions. This introduces at most one additional integration dimension but preserves the overall semi-analytical structure and the order of computational complexity of the task completion probability evaluation.

## V. MAXIMIZING TASK COMPLETION UNDER ENERGY CONSTRAINTS

In this section, we investigate the performance optimization of the UAV-CPNs enabled by hybrid fuel cell and battery-powered UAVs. These hybrid energy architectures, whether implemented in serial, parallel, or decoupled configurations, exhibit distinct power delivery dynamics. However, they share a critical operational limitation: task computing failure can occur if either the battery energy is exhausted or the fuel supply is depleted. This highlights the necessity of joint energy-aware optimization to effectively balance communication and propulsion energy demands under heterogeneous energy sources.

To maximize the task completion probability under dual energy constraints, we develop a systematic optimization framework that explicitly accounts for the coupling between UAV transmit power $( P _ { d } )$ and operational altitude (<sup>h</sup>). First, we establish a comprehensive energy consumption model that captures both communication energy and propulsion energy, both of which are functions of $P _ { d }$ and <sup>h</sup>. Then, we formulate a joint optimization problem, aiming to maximize the average task completion probability, subject to realistic energy, hardware, and regulatory constraints. Finally, we propose an efficient alternating iterative optimization framework that enables real-time adaptation of transmit power and altitude, ensuring reliable and energy-efficient operation in dynamic UAV-CPN environments.

## A. Energy Consumption Modeling

In hybrid fuel cell and battery-powered UAV-CPNs, the energy consumption of the UAV arises from two parts: propulsion (including both mobility and hovering) and communication energy. Since this paper mainly focuses on the vertical movement, we establish an energy model that quantifies propulsion energy consumption as function of UAV altitude <sup>h</sup> and transmit power $P _ { d } .$ , expressed as [40]:

$$
\begin{array} { r } { E _ { \mathrm { p r o p } } ( P _ { d } , h ) = \left[ ( 1 + c ) \frac { W ^ { 3 / 2 } } { \sqrt { 2 \rho A } } + \frac { \delta \rho S _ { \mathrm { b l a d e } } v _ { \mathrm { t p } } ^ { 3 } } { 8 } \right] \cdot T ( P _ { d } , h ) } \\ { + G ( h - h _ { 0 } ) , \qquad ( 2 } \end{array}\tag{0}
$$

where $h _ { 0 }$ is the initial altitude of the UAV, $T ( P _ { d } , h ) =$ $t _ { 1 } ( P _ { d } , h ) + t _ { 2 } ( P _ { d } , h )$ (refer to (7) and (8)) represents hovering duration for $G U / / O { - } U A V$ task offloading and $U A V – t o – C N f o r \mathrm { - }$ warding, <sup>G</sup> is the UAV’s weight in Newtons (N), <sup>ρ</sup> denotes the air density in kilograms per cubic meter $\mathrm { ( k g / m ^ { 3 } ) }$ , <sup>A</sup> corresponds to the rotor disc area in square meters $( \mathrm { m } ^ { 2 } )$ , <sup>c</sup> serves as the induced power correction factor accounting for non-ideal aerodynamic effects, <sup>δ</sup> quantifies the profile drag coefficient of rotor blades, $S _ { \mathrm { b l a d e } }$ indicates the total blade area in square meters $( \mathrm { m } ^ { 2 } )$ , and $v _ { \mathrm { t i p } }$ specifies the blade tip speed in meters per second (m/s).

In UAV-CPNs, communication energy consumption refers to the energy consumed by transmitting tasks from the UAV to CNs, given by:

$$
E _ { \mathrm { c o m m } } ( P _ { d } , h ) = P _ { d } \cdot t _ { 2 } ( P _ { d } , h ) ,\tag{21}
$$

where $t _ { 2 } ( P _ { d } , h )$ denotes transmission time for $U A V – t o – C N f o r –$ warding according to (8).

## B. Energy-Aware Optimization Problem Formulation

To ensure broad applicability across diverse hybrid UAV-CPN architectures, we develop a generalized modeling framework in which communication energy consumption is constrained by the available battery capacity $( E _ { \mathrm { { b a t t e r y } } } )$ , while propulsion energy consumption is limited by the fuel budget $( E _ { \mathrm { f u e l } } )$ . Although certain simplifying assumptions are made for analytical tractability, this decoupled-yet-interdependent representation enables a systematic analysis of the complex interplay among energy usage, UAV transmit power $( P _ { d } )$ , and operational altitude (<sup>h</sup>).

As established in Section IV, UAV’s transmit power and altitude jointly determine CN coverage, which in turn influences critical parameters such as transmission distance, channel conditions, and CN capabilities. These factors collectively govern task computing latency, thereby dictating the UAV’s required hovering duration. Moreover, communication energy consumption is directly impacted by the transmit power itself, creating a dual dependency on both transmit power and altitude.

Operational altitude further affects mobility-related energy consumption through its influence on mobility distance. Beyond its role in UAV-to-CN communication and computing, altitude also impacts UAV-to-GN transmissions. Prolonged task computing latency increases hovering time, thereby elevating propulsion energy demands. Consequently, both mobility-related and hovering energy consumption contribute to the total propulsion energy burden.

Thus, we formulate a constrained optimization problem that simultaneously addresses: i) communication energy consumption bound by battery capacity $( E _ { \mathrm { b a t } } ) _ { \mathrm { \ell } }$ , ii) propulsion energy consumption limited by fuel budget $( E _ { \mathrm { f u e l } } )$ , iii) transmit power confined within hardware specifications $( [ P _ { \operatorname* { m i n } } , P _ { \operatorname* { m a x } } ] )$ , and iv) operational altitude restricted by airspace safety protocols $( [ h _ { \operatorname* { m i n } } , h _ { \operatorname* { m a x } } ] )$ . The joint optimization problem can be mathematically formulated as:

$$
( \mathbf { P 1 } ) \operatorname* { m a x } _ { P _ { d } , h } \quad \overline { { P } } _ { \mathrm { s u c c e s s } } ( P _ { d } , h )\tag{22a}
$$

$$
\begin{array} { r l } { \mathrm { s . t . } } & { { } E _ { \mathrm { c o m m } } ( P _ { d } , h ) \leq E _ { \mathrm { b a t t e r y } } , } \end{array}\tag{22b}
$$

$$
E _ { \mathrm { p r o p } } ( P _ { d } , h ) \leq E _ { \mathrm { f u e l } } ,\tag{22c}
$$

$$
P _ { d } \in [ P _ { \operatorname* { m i n } } , P _ { \operatorname* { m a x } } ] ,\tag{22d}
$$

$$
h \in [ h _ { \operatorname* { m i n } } , h _ { \operatorname* { m a x } } ] ,\tag{22e}
$$

where $\overline { { P } } _ { \mathrm { s u c c e s s } } ( P _ { d } , h )$ denotes the average task completion probability derived from analysis in Section IV, (22b) and (22c) represent the battery and fuel energy budgets, respectively, and (22d) and (22e) define the transmit power constraint and the operational altitude range, respectively.

Algorithm 1: Alternating Iterative Joint Optimization.   
Input: Energy budget $\overline { { ( E _ { \mathrm { b a t t e r y } } , E _ { \mathrm { f u e l } } ) } }$   
Output: Optimized parameters $( h ^ { \ast } , P _ { d } ^ { \ast } )$   
Initialization:   
Initial altitude $h ^ { ( 0 ) }$ , initial transmit power $P _ { d } ^ { ( 0 ) }$   
maximum iterations max\_iter, convergence   
threshold $\epsilon , \eta _ { \mathrm { p r e v } }  0$   
for $k = 1$ to max\_iter do   
Altitude optimization   
$h ^ { ( k ) } = \arg \operatorname* { m a x } _ { h } \overline { { P } } _ { \mathrm { s u c c e s s } } ( h , P ^ { ( k - 1 ) } ; E _ { \mathrm { b a t t e r y } } , E _ { \mathrm { f u e l } } )$   
Transmit power optimization:   
$P _ { d } ^ { ( k ) } = \arg \operatorname* { m a x } _ { P _ { d } } \overline { { P } } _ { \mathrm { s u c c e s s } } ( h ^ { ( k ) } , P ; E _ { \mathrm { b a t t e r y } } , E _ { \mathrm { f u e l } } )$   
Convergence Check:   
$\eta ^ { ( k ) } \gets \overline { { P } } _ { \mathrm { s u c c e s s } } ( h ^ { ( k ) } , P _ { d } ^ { ( k ) } )$   
if $| \eta ^ { ( k ) } - \eta _ { p r e \nu } | < \epsilon$ then   
return $( h ^ { ( k ) } , P _ { d } ^ { ( k ) } )$   
end   
$\eta _ { \mathrm { p r e v } }  \eta ^ { ( k ) }$   
end   
return $( h ^ { \mathrm { ( m a x \mathrm { } - i t e r ) } } , P _ { d } ^ { \mathrm { ( m a x \mathrm { } - i t e r ) } } )$

This formulation exhibits two characteristics that challenge conventional optimization methods. First, the altitudedependent LoS probability $P _ { \mathrm { L o S , u p } }$ introduces non-linear coupling between <sup>h</sup> and $P _ { d }$ . Second, the dual-energy constraints create discontinuous feasible regions in the parameter space. To address P1 while maintaining computational efficiency for real-time implementation, we develop an alternating iterative joint optimization strategy.

## C. Alternating Iterative Joint Optimization Framework

In this section, we propose a robust iterative method to solve P1, tailored to the practical constraints of hybrid-powered UAV-CPNs under dynamic CN accessibility.

The proposed joint optimization strategy operates through the following iterations. First, we initialize the UAV’s altitude $h ^ { ( 0 ) }$ , transmit power $P _ { d } ^ { ( 0 ) }$ , the maximum iteration count max \_i<sup>ter</sup>, and convergence threshold <sup></sup>. Subsequently, we employ a two-stage iterative optimization approach: While maintaining fixed transmit power, the altitude is optimized through golden-section search to maximize the task completion probability. This derivative-free approach effectively handles nonmonotonic relationships between altitude and system performance metrics (e.g., task completion probability and energy consumption). Following this altitude optimization, we employ a modified quasi-Newton method combining gradient descent with approximate Hessian information to optimize transmit power parameters. Adaptive learning rate decay will be adopted to prevent oscillations during gradient direction changes. These alternating updates continue until the relative improvement in the task completion probability over a sliding window of the last few iterations falls below <sup></sup>, or max \_i <sup>ter</sup> is reached, providing enhanced convergence stability. Upon convergence, the solution is validated against both communication and propulsion energy constraints. If either constraint is violated, the system automatically reverts to a predefined safe operating point (e.g., <sup>h</sup> = 50 m, $P _ { d } = 1 0 \mathrm { d B W } )$ , ensuring operational feasibility under model uncertainty or environmental variations. These alternating updates continue until the relative improvement in the task completion probability over a sliding window of the last <sup>W</sup> iterations (e.g., $W = 5 )$ falls below <sup></sup>, or max \_i<sup>ter</sup> is reached, providing enhanced convergence stability. Upon convergence, the solution is validated against both communication and propulsion energy constraints. If either constraint is again violated, the system automatically reverts to a predefined safe operating point (e.g., $h = 5 0$ m, $P _ { d } = 1 0 ~ \mathrm { W } )$ , ensuring operational feasibility under model uncertainty or environmental variations.

TABLE I  
PARAMETER SETTING FOR CPNS
<table><tr><td>Description</td><td>Parameter</td><td>Value</td></tr><tr><td>Transmit power of GUs</td><td> $P _ { u }$ </td><td>20 dBW</td></tr><tr><td>Path loss exponent</td><td> $\alpha _ { \mathscr { U } }$ </td><td> $^ 2$ </td></tr><tr><td>NLoS attenuation coefficient</td><td> $\eta$ </td><td>20dB</td></tr><tr><td>Bandwidth</td><td> $\dot { W }$ </td><td>8MHz</td></tr><tr><td>Noise power</td><td> $N _ { 0 }$ </td><td>-120 dBm</td></tr><tr><td>Data size</td><td> $D$ </td><td>1 MB</td></tr><tr><td>Maximum allowable latency</td><td> $T _ { \mathrm { m a x } }$ </td><td>55 ms</td></tr><tr><td>Node density (GUs, CNs)</td><td> $\lambda _ { u } , \lambda _ { c }$ </td><td>500, 5 nodes/km²</td></tr><tr><td>Zone radius (Request, service)</td><td> $R _ { \mathrm { u } } , R _ { \mathrm { d } }$ </td><td>200, 1000 m</td></tr><tr><td>Parameters for urban environment</td><td> $B , C$ </td><td>0.136, 11.95</td></tr></table>

The time complexity of this algorithm is determined by three main factors: i) the per-iteration computational cost of altitude and transmit power optimization, ii) the number of iterations required for convergence, and iii) the user population size <sup>N</sup>. At each iteration, altitude optimization via the golden-section method involves a fixed number of steps, where each step evaluates the objective function, resulting in a cost of $\mathcal { O } ( n _ { \mathrm { s t e p s \_ h } } \cdot N )$ . Similarly, optimizing transmit power through the modified quasi-Newton method requires a fixed number of steps, each step computing gradients and Hessians information of the objective function, leading to $\mathcal { O } ( n _ { \mathrm { s t e p s \_ p } } \cdot N )$ . Assuming a maximum of <sup>T</sup> iterations, the total time complexity becomes $\mathcal { O } ( T \cdot ( n _ { \mathrm { s t e p s \_ h } } + n _ { \mathrm { s t e p s \_ p } } ) \cdot N )$ . Since $n _ { \mathrm { s t e p s \_ h } }$ and $n _ { \mathrm { s t e p s \_ p } }$ are constants, this is simplified to $\mathcal { O } ( T \cdot N )$ . The dominant factor is the linear dependence on <sup>N</sup>, as evaluating the objective function requires iterating over all users to compute channel states and energy constraints. In practice, convergence often occurs far earlier than the theoretical maximum $T _ { \ast }$ , making the method scalable for large networks [40], [45].

## VI. NUMERICAL RESULTS

In this section, we evaluate the task completion probability using parameters listed in Tables I and II unless explicitly indicated. These parameters align with the scenarios where UAVs and GUs employ wireless transmission modules to support lowlatency services like real-time video analytics [2]. Our evaluation focuses on four critical aspects: i) the validation of theoretical models, ii) the trade-off among communication-computing resources through strategic positioning of UAV altitude, iii) the potential for performance enhancement with more reachable CNs, and iv) energy-constrained performance optimization and parameter sensitivity analysis.

TABLE II  
PARAMETER SETTING FOR THE UAV
<table><tr><td>Description</td><td>Parameter</td><td>Value</td></tr><tr><td>Incremental correction factor in (20)</td><td>C</td><td>0.1</td></tr><tr><td>UAV take-off mass</td><td>G</td><td> $2 6 ~ \mathrm { k g }$ </td></tr><tr><td>Air density</td><td> $\rho$ </td><td> $1 . 2 2 5 ~ \mathrm { k g / m ^ { 3 } }$ </td></tr><tr><td>Rotor disc area</td><td> $A$ </td><td> $1 ~ \mathrm { m ^ { 2 } }$ </td></tr><tr><td>Profile drag coefficient</td><td> $\delta$ </td><td> $0 . 0 1 2 $ </td></tr><tr><td>Total blade area</td><td> $S _ { \mathrm { b l a d e } }$ </td><td> $0 . 2 ~ \mathrm { m ^ { 2 } }$ </td></tr><tr><td>Speed of rotor blade tip</td><td> $v _ { \mathrm { t i p } }$ </td><td>250 m/s</td></tr><tr><td>Battery energy budget</td><td> $E _ { \mathrm { b a t t e r y } }$ </td><td> $2 0 - 1 2 0 { \mathrm { ~ J } }$ </td></tr><tr><td>Fuel cell energy budget</td><td> $E _ { \mathrm { f u e l } }$ </td><td> $\mathrm { 3 \times 1 0 ^ { 4 } - 6 \times 1 0 ^ { 4 } ~ J }$ </td></tr><tr><td>UAV initial altitude</td><td> $h _ { 0 }$ </td><td> $5 0 ~ \mathrm { m }$ </td></tr><tr><td>Transmit power of UAV</td><td> $P _ { d }$ </td><td>20 dBW</td></tr></table>

![](images/57e9ee31d70bbe3c827358457e18d9cb450c3f990c2ff142b7ff153f9f56fbdf.jpg)  
Fig. 2. Task completion probability vs. UAV altitude.

## A. Evaluation on Task Completion Probability

We first validate the analytical expressions derived in Theorem IV.2 through extensive Monte Carlo simulations (10,000 runs), each involving random sampling of 400 GUs for average task completion probability calculation. As shown in Fig. 2, our theoretical analysis (Theory curves) exhibits close alignment with Monte Carlo simulation results (Monte Carlo curves) across two representative computing capability scenarios: $t _ { c } = 0 . 2$ ms and $t _ { c } = 2 ~ \mathrm { m s }$ , respectively. System performance degrades at both extremely low and high UAV altitudes. Specifically, low altitudes result in NLoS-dominated link connections between the UAV and GUs or CNs, while high altitudes lead to excessive path loss, both of which restrict the communication coverage of the UAV and thus fundamentally limit the effective utilization of distributed computing power. Numerical results confirm the existence of an optimal UAV altitude (approximately 200 m when $t _ { c } = 2$ ms) that resolves communication bottlenecks through adaptive UAV positioning. Moreover, enhanced computing power (reducing $t _ { c }$ from 2 ms to 0.2 ms) mitigates computing bottlenecks (marked as comp\_limited), yielding altitude-dependent performance gains.

![](images/1b23ddf2dc6060a95a6a45468cd4910905666af6125236e8b5174b8babbd21e1.jpg)  
Fig. 3. Task completion probability vs. CN density & UAV altitude.

![](images/f895ed6053ffb587879d00b6538af86f1d7290431027c32022def0a99a8b9639.jpg)  
Fig. 4. Task completion probability vs. CN distribution & UAV altitude.

The UAV-CPN architecture consequently necessitates a dynamic configuration that involves both communication and computing simultaneously.

We further investigate the fundamental trade-off between communication coverage and computing power by analyzing the joint effects of CN density and UAV altitude on task completion probability. Fig. 3 presents a 3D surface plot that reveals a nonlinear interdependency between these two critical parameters and highlights their varying sensitivities. For example, when the CN density is low, the task completion probability is highly sensitive to the altitude of the UAV. Therefore, careful selection of the UAV altitude is crucial to achieve a high task completion probability under such conditions. In contrast, when the CN density is high, the altitude of the UAV can vary in a wide range while still maintaining a high task completion probability.

Next, we investigate the performance gain achieved through CN distribution radius expansion. Fig. 4 shows a 3D surface plot that reveals the coupled effects of CN spatial distribution and UAV altitude on task completion probability. For fixed UAV altitudes (e.g., at a UAV altitude of 300m), extending CN distribution beyond the request zone boundaries (specifically when the distribution radius exceeds 200m) produces substantial performance gains. Specifically, expanding the CN distribution radius from 200m (corresponding to our prior work [36]) to

1,000m achieves a 2<sup>.</sup>13× improvement in task completion probability (46.65% → 99.14%), confirming our framework’s capability to leverage ubiquitous computing power distribution. For fixed CN distributions, we confirm the existence of an altitude-dependent performance maximum, demonstrating the effectiveness of dynamic CN accessibility control, which is consistent with our prior work [36]. While the UAV-CPN architecture introduces multi-dimensional coordination complexity, this proves to be essential for overcoming individual communication or computing bottlenecks, ultimately achieving superior performance.

Finally, we evaluate the joint impact of UAV transmit power and altitude on task completion probability under different energy budgets. As shown in Fig. 5, our 3D surface analysis reveals a significant energy-performance tradeoff in UAV-CPNs. The constrained scenario (Fig. 5b) demonstrates severe performance degradation at high power (≥ 30 dBW) and high altitude (≥ 500 m) compared to the ideal case (Fig. 5(a)). For example, at a configuration of 30 dBW/310 m, the task completion probability drops from 1 under ideal conditions to nearly 0 under energy constraints due to excessive communication energy consumption. On average, the drop across different energy budgets is approximately 50%. This analysis confirms that energy constraints create critical performance bottlenecks, necessitating energy-aware UAV deployment strategies in UAV-CPNs. In the following section, we systematically evaluate optimization approaches to maintain service quality under strict energy budget constraints.

## B. Energy-Constrained Performance Analysis

We evaluate the performance gain achieved by jointly optimizing the UAV altitude and transmit power (hereafter referred to as the joint optimization strategy) under predefined battery $( E _ { \mathrm { { b a t t e r y } } } )$ and fuel $( E _ { \mathrm { f u e l } } )$ energy budgets, compared to three types of baseline configurations.

\- Transmit Power Only: Optimize the UAV’s transmit power while fixing the altitude at $h = 5 0 \mathrm { m }$ . This baseline isolates the impact of power allocation.

\- Altitude Only: Optimize the UAV’s altitude while fixing the transmit power at $P _ { d } = 5 \mathrm { d B W }$ . This baseline isolates the impact of altitude control.

\- Static Configurations: Three pairs of static parameters: – High altitude, low power: $h = 1 0 0$ m, $P _ { d } = 1 0 ~ \mathrm { d B W } .$ – Low altitude, high power: $h = 5 0 \mathrm { m } , P _ { d } = 1 0 \mathrm { d B W }$ – Conservative operation: $h = 5 0 \mathrm { m } , P _ { d } = 5 \mathrm { d B W }$

The analysis aims to: i) quantify the benefits of joint optimization, and ii) identify which parameter (altitude or transmit power) has a more pronounced impact on task completion probability under different combination of energy constraints $E _ { \mathrm { b a t t e r y } }$ and $E _ { \mathrm { f u e l } }$ . The performance gain is defined as the relative improvement in task completion probability:

Performance

$$
\mathrm { G a i n } \left( \% \right) = \frac { \mathcal { P } _ { \mathrm { j o i n t } } - \mathcal { P } _ { \mathrm { b a s e l i n e } } } { \mathcal { P } _ { \mathrm { b a s e l i n e } } } \times 1 0 0 .\tag{23}
$$

where $\mathcal { P } _ { \mathrm { j o i n t } }$ and $\mathcal { P } _ { \mathrm { b a s e l i n e } }$ denote the task completion probabilities of the joint optimization and baseline strategies, respectively.

![](images/be1f263a0953a0cdbdd61a0150aebe3227610f0b88136f57f2529c951c368412.jpg)  
(a) Ideal case without energy constraints

![](images/67ec335c5c6c436e733dd2f308367506bff0216a6735e01b236c463805efa70d.jpg)  
(b) Under energy budgets of $E _ { b a t t e r y } = 4 0 \rfloor$ and $E _ { f u e I } = 4 0 0 0 0 \rfloor$

Fig. 5. The joint impact of UAV transmit power and altitude on task completion probability under different energy supply conditions: (a) Ideal case without energy constraints, (b) Under energy budgets of $E _ { \mathrm { b a t t e r y } } = 4 0 \ : \mathrm { { J } }$ J and $E _ { \mathrm { f u e l } } = 4 0 , 0 0 0 \mathrm { J }$  
![](images/2d96e6b2f971f491da754c0b6efd2d6744387778b688eb1c8f48b93f2e2a785b.jpg)  
Fig. 6. Performance gain of the proposed joint optimization (altitude and transmit power) over key baseline strategies under varying energy budget combinations: (a) Transmit Power Only $( h = 5 0 \mathrm { m } )$ , (b) Altitude Only $( P _ { d } = 5 \mathrm { d B W } ) ,$ (c) Static Configuration $( h = 1 0 0 \mathrm { m } , P _ { d } = 1 0 \mathrm { d } \mathrm { B W } ) ,$ (d) Static Configuration $( h = 5 0 \mathrm { m }$ $P _ { d } = 1 0 ~ \mathrm { d B W ) }$ , (e) Static Configuration $( h = 5 0 \mathrm { m } , P _ { d } = 5 \mathrm { d } \mathrm { B W } )$ . The proposed method dynamically balances coverage, link quality, and energy constraints, achieving up to 29.6% higher task completion probability than the best-performing baseline. This highlights the critical importance of co-optimizing UAV altitude and transmit power in UAV-CPNs. Notably, while the static configuration with $h = 1 0 0$ m and $P _ { d } = \mathrm { 1 0 } \mathrm { \check { d } B W }$ occasionally achieves high performance, its practical feasibility is severely limited–40% of energy budget combinations are infeasible (indicated by white regions in Fig. 6c), resulting in complete task failure.

As shown in Fig. 6, the proposed Joint Optimization strategy demonstrates consistently superior performance, achieving strictly positive average gains ranging from 29.6% to 247.7%, against five baseline strategies, with peak improvements exceeding 390%. These results quantitatively validate its capability to maximize task completion probability under dual-energy constraints through parameter coordination. Subplots (a) and (b) of Fig. 6 reveal the critical advantage of joint optimization over single-parameter approaches, achieving 46.5% average and 130.2% maximum gains against power-only optimization, and more substantial 98.3% average and 160.4% maximum improvements over altitude-only optimization. These findings highlight the essential role of dynamic coordination between transmit power adjustment and altitude adaptation in maximizing the task completion probability. Moreover, the analysis reveals that transmit power optimization contributes more significantly to performance enhancement than altitude optimization, suggesting that CN spatial coverage improvements through power control may outweigh the benefits of that via altitude adjustments under dual-energy constraints. The most significant gains emerge in comparisons with the static $h = 5 0 \mathrm { m } , P _ { \mathrm { d } } = 5$ dBW configuration, reaching a peak improvement of 391.2%. This stems primarily from the dual limitations inherent to static strategies: fixed low transmit power $( P _ { \mathrm { d } } = 5 \mathrm { d B W ) }$ fundamentally restricts the communication coverage capability of CNs, while suboptimal altitude selection amplifies path loss inefficiencies. As shown in subplots (c)-(e) of Fig. 6, while the static configuration with $h = 1 0 0 \mathrm { m } , P _ { \mathrm { d } } =$ 10 dBW occasionally achieves the best performance among three static configurations, its practical viability is severely compromised by 40% invalid energy budget combinations (indicated by white spaces in subplots (c) of Fig. 6), where task completion probability collapses to zero. The reported gains derive from 480 valid energy budget combinations, with the static <sup>h</sup> = 100 m strategy exhibiting the worst robustness despite achieving the highest baseline task completion probabilities in valid regions. This phenomenon reinforces the necessity of dynamic parameter coordination to maintain reliable performance across the energy budget combination.

(a) Joint Optimization  
![](images/2391c5052a41f5ba400bc1ee0f9912ee79a6c38d9dddd8b98de912fa6fc154ce.jpg)  
(b) Transmit Power Only (h=50 m) (c) Altitude Only (Pd=5 dBW)

![](images/8541ee352db9692605c460b0d2b5d6b238cd03157f7a20b54e164fb8d7a9227c.jpg)  
(d) h=100 m, Pd=10 dBW

![](images/db4f1f0aa84fbba3447539e1e332f3aeb07bfa1be0bfe168b01b7d57ccc7f7e0.jpg)  
(e) h=50 m, Pd=10 dBW

![](images/531bc4d3262c0a28a4d58ba56441d69165269bac81aae423f834b0c3c8b13766.jpg)  
(f) h=50 m, Pd=5 dBW  
Fig. 7. Task completion probability under varying energy budget combinations: (a) Joint Optimization, (b) Transmit Power Only $( h = 5 0 ~ \mathrm { m } ) ,$ (c) Altitude Only $( \bar { P _ { d } } = 5 ~ \mathrm { d B W } )$ , (d) Static Configuration (h = 100 m, $P _ { d } = 1 0 ^ { - } \mathrm { d B W } )$ , (e) Static Configuration (h = 50 m, $P _ { d } = 1 0 ~ \mathrm { d B W ) } .$ , (f) Static Configuration $( h = 5 0$ m, $P _ { d } = 5 \mathrm { d B W } )$ . The proposed joint optimization achieves the highest task completion probability across all energy budget combinations while baseline strategies suffer from limited flexibility or frequent infeasibility, particularly under stringent energy conditions.

In Fig. 7, we display the concrete task completion probabilities for six UAV-CPN configurations under varying energy budgets $( E _ { \mathrm { { b a t t e r y } } } \in [ 2 0 , 1 2 0 ] \mathbf { J } , E _ { \mathrm { { f u e l } } } \in [ 3 0 , 6 0 ] \mathrm { { k J } } ,$ ). These results not only provide the foundation for the performance gain calculation in Fig. 6 but also offer intuitive insights into the system behavior. The Joint Optimization strategy achieves the best task completion probability across all energy combinations, obviously outperforming the other baseline strategies. Subplots (a) and (b) in Fig. 7 exhibit sensitivity to battery energy budgets $E _ { \mathrm { b a t t e r y } } ,$ reflecting the incorporation of transmit power optimization in both Joint Optimization and Transmit Power Only strategies. Similarly, subplots (a) and (c) in Fig. 7 reveal a significant dependence on fuel energy $E _ { \mathrm { f u e l } }$ , highlighting the critical role of propulsion energy in altitude optimization. At low altitudes (e.g., $h =$ 50 m), optimizing the transmit power (Fig. 7(b) vs. (e)) enhances task completion probability, demonstrating the dominance of power adaptation in energy-constrained regimes. Under low transmit power $( P _ { d } = 5 \mathrm { d B W } )$ , altitude optimization (Fig. 7(c) and (f)) increases the task completion probability, validating altitude tuning as a critical lever for communication coverage enhancement. A striking observation in static configurations is that when $E _ { \mathrm { f u e l } } \leq 4 2 , 0 0 0 \mathbf { J } .$ the strategy with $h = 1 0 0 \mathrm { m } .$ $P _ { d } = 1 0 \mathrm { d B W }$ fails completely, resulting in zero task completion probability. This corresponds to the white regions depicted in Fig. 6(c), indicating that with these configurations, the fuel energy $E _ { \mathrm { f u e l } }$ becomes the primary performance bottleneck.

The joint optimization of UAV altitude and transmit power under dual energy constraints, specifically from fuel cells and batteries, has not been previously addressed in the literature. Consequently, there are no established baseline mechanisms for direct comparison. To evaluate the effectiveness of the proposed alternating iterative joint optimization framework, we compare it against a Bayesian optimization (BO)-based baseline method, which is commonly used for black-box optimization of complex, multi-parameter problems. The results are presented in Figs. 8 and 9.

Subplots (b) and (c) in Fig. 8 illustrate the optimized altitude (<sup>h∗</sup>) and transmit power $( P _ { \mathrm { d } } ^ { * } )$ , respectively, obtained from the proposed method, while subplot (a) shows the corresponding task completion probability $( P _ { \mathrm { s u c c e s s } } ^ { * } )$ . From these three subplots, we observe that the optimal task completion probability, the optimized UAV altitude, and the optimized transmit power are all sensitive to the fuel energy budget $E _ { \mathrm { f u e l } }$ . Notably, transmit power exhibits greater sensitivity to both $E _ { \mathrm { f u e l } }$ and the battery energy budget $E _ { \mathrm { b a t t e r y } }$ than what altitude does. As a result, the spatial pattern of $P _ { \mathrm { s u c c e s s } } ^ { * }$ in Fig. 8(a) closely resembles that of $P _ { \mathrm { d } } ^ { * }$ in Fig. 8(c). This suggests that, while both parameters are important, transmit power tuning plays a more dominant role in shaping performance under the tested energy configurations, consistent with the insights from Fig. 6 and Fig. 7. The observed parameter sensitivities provide valuable theoretical guidance for energy management in hybrid fuel and battery-powered UAV-CPNs. For instance, when $E _ { \mathrm { f u e l } } > 5 0 , 0 0 0 { \mathrm { J } } .$ , converting excess fuel energy into electrical energy (e.g., via onboard generators) can alleviate battery energy limitations and thereby improve task completion probability, as demonstrated in Fig. 8(a). This confirms that $E _ { \mathrm { b a t t e r y } }$ can act as a performance bottleneck, aligning with findings in Fig. 5.

![](images/951b4ac98a4d371ae918a1b54796ca96e1e5208edd5fcb01c3643c976a5c9e7e.jpg)  
(a) Task Completion Probability

![](images/b72d0ed6793cbf6beee30d2e083ad7b373c8ab3ccbcbff271efbd6bee52b8a11.jpg)  
(b) Optimized Altitude

![](images/3f3355578f73be1b9b27c851299401b13c6b3433139f2b2e7236408b9f1fa52f.jpg)  
(c) Optimized Transmit Power

Fig. 8. Optimized performance and system parameters under varying battery-fuel cell energy budget combinations: (a) Maximum task completion probability $( P _ { \mathrm { s u c c e s s } } ^ { * } ) ,$ , (b) Optimized UAV altitude (h<sup>∗</sup>), and (c) Optimized transmit power $\overset { \cdot } { ( P _ { \mathrm { d } } ^ { * } ) }$ obtained via the proposed joint optimization framework.  
![](images/e9ab276d0f0478e137067cc957c02e9d5af4548f60c5427b125c28df8f9259b6.jpg)  
(a) Task Completion Probability

![](images/cd7841daaeb4c96a10cbba63542706c2d60271e761411d98dcb461a73c419a2f.jpg)  
(b) Optimized Altitude

![](images/3ef802749c5a78ccf78a8adc3401008b5ca34794251e133fb8f730b3170829d8.jpg)  
(c) Optimized Transmit Power  
Fig. 9. Performance of a Bayesian optimization-based baseline for solving problem P1 under varying battery–fuel cell energy budget combinations: (a) Achieved task completion probability $( \dot { P } _ { \mathrm { s u c c e s s } } ^ { * } ) ,$ (b) Optimized UAV altitude (h<sup>∗</sup>), and (c) Optimized transmit power $( P _ { \mathrm { d } } ^ { * } )$ . This joint optimization approach serves as a comparative benchmark for the proposed two-stage iterative method

To comprehensively evaluate the proposed optimization methodology, we implement a comparative BO framework [46] for solving the joint parameter optimization problem P1. While Bayesian methods demonstrate established competence in navigating multi-dimensional spaces through Gaussian process-based surrogate modeling, our controlled experimental analysis reveals critical performance limitations due to energy constraints. Under equivalent computational budgets (30 function evaluations per energy budget configuration to ensure equitable comparison conditions), the proposed optimization algorithm demonstrates consistent superiority with 13.8% average improvement in task completion probability across all energy budgets, achieving peak enhancements of 49.16% at critical operational points $( E _ { \mathrm { b a t t e r y } } = 4 6 . 3 2 ~ \mathrm { J } , ~ E _ { \mathrm { f u e l } } = 5 8 , 4 6 1 . 5 4 ~ \mathrm { J } )$ Spatial performance analysis confirms that our proposed method outperforms BO in 69.2% of operational scenarios. As visualized in Figs. 8(a) and 9(a), it becomes evident that our proposed algorithm achieves superior task completion probabilities. This performance gap primarily stems from: 1) The curse of dimensionality: alternating optimization decomposes the 2D problem into sequential 1D optimizations, whereas Bayesian optimization directly searches the full parameter space, resulting in significantly reduced sampling density under equivalent evaluation budgets; 2) Constraint-handling efficacy: our method incorporates explicit feasibility checks during each single-parameter optimization phase, while the Bayesian approach’s penalty-based constraint relaxation may induce convergence to infeasible regions. These comparative results validate that our proposed strategy has better suitability for real-world deployment in energy-constrained UAV-CPN systems.

## VII. CONCLUSION

In this paper, we have investigated the task completion probability (i.e., task completion rate or task throughput) in UAV-enabled computing power networks, where an aerial UAV relay facilitates the transmission of ground users’ computing tasks to distributed computing nodes (CNs) for real-time processing and computing. Our proposed framework enables tasks generated from a constrained request zone to be completed by CNs distributed across an unbounded geographical service zone, thereby enhancing access to more computing power. We have derived analytical expressions to characterize the task completion probability as the main performance metric for this study. Moreover, we have examined performance optimization by managing both communication and propulsion energy consumption in practical hybrid fuel cell and battery-powered UAV scenarios. Extensive numerical results have validated the analytical results and highlighted the importance of balanced resource coordination to achieve optimal system performance. By effectively managing both communication parameters (e.g., UAV altitude and transmit power) and computing power parameters (i.e., computing capabilities, CN density, and CN distribution radius), we can significantly enhance the task completion probability. This work lays the foundation for future research on the integration of advanced computing and communication technologies into future-generation wireless networks, leading to the emerging computing power networks that have been considered indispensable for future AI-enabled applications.

## REFERENCES

[1] Y. Deng, Z. Fang, S. Hu, Y. Ma, H. Zhang, and Y. Fang, “UAV-enabled computing power networks: Task completion probability analysis,” in Proc. IEEE GLOBECOM, Taipei, Taiwan, Dec. 8–12, 2025.

[2] Z. Fang, S. Hu, J. Wang, Y. Deng, X. Chen, and Y. Fang, “Prioritized information bottleneck theoretic framework with distributed online learning for edge video analytics,” IEEE Trans. Netw., vol. 33, no. 3, pp. 1203–1219, Jun. 2025.

[3] S. Hu, Z. Fang, Y. Deng, X. Chen, Y. Fang, and S. Kwong, “Toward full-scene domain generalization in multi-agent collaborative Bird’s Eye View segmentation for connected and autonomous driving,” IEEE Trans. Intell. Transp. Syst., vol. 26, no. 2, pp. 1783–1796, Feb. 2025.

[4] Y. Xiao et al., “Space-air-ground integrated wireless networks for 6G: Basics, key technologies, and future trends,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3327–3354, Dec. 2024.

[5] Y. Deng, X. Chen, G. Zhu, Y. Fang, Z. Chen, and X. Deng, “Actions at the edge: Jointly optimizing the resources in multi-access edge computing,” IEEE Wireless Commun., vol. 29, no. 2, pp. 192–198, Apr. 2022.

[6] Y. Ma, Z. Fang, L. Yuan, Y. Deng, X. Chen, and Y. Fang, “RAISE: Optimizing RIS placement to maximize task throughput in multi-server vehicular edge computing,” IEEE Trans. Wireless Commun., vol. 25, pp. 9185–9199, Dec. 2025.

[7] Y. Sun et al., “Computing power network: A survey,” China Commun., vol. 21, no. 9, pp. 109–145, Sep. 2024.

[8] X. Tang et al., “Computing power network: The architecture of convergence of computing and networking towards 6G requirement,” China Commun., vol. 18, no. 2, pp. 175–185, Feb. 2021.

[9] B. Ma et al., “UAV-assisted computing power network task allocation and 3D urban trajectory optimization,” IEEE Internet Things J., vol. 12, no. 12, pp. 19294–19307, Jun. 2025.

[10] X. Dai, Z. Xiao, H. Jiang, and J. C. S. Lui, “UAV-assisted task offloading in vehicular edge computing networks,” IEEE Trans. Mobile Comput., vol. 23, no. 4, pp. 2520–2534, Apr. 2024.

[11] H. Hao, C. Xu, W. Zhang, S. Yang, and G.-M. Muntean, “Joint task offloading, resource allocation, and trajectory design for multi-UAV cooperative edge computing with task priority,” IEEE Trans. Mobile Comput., vol. 23, no. 9, pp. 8649–8663, Sep. 2024.

[12] S. Basu, S. Roy, and S. DasBit, “A post-disaster demand forecasting system using principal component regression analysis and case-based reasoning over smartphone-based DTN,” IEEE Trans. Eng. Manag., vol. 66, no. 2, pp. 224–239, Dec. 2024. May 2019.

[13] C. Zhan, Y. Zeng, and R. Zhang, “Energy-efficient data collection in UAV enabled wireless sensor network,” IEEE Wireless Commun. Lett., vol. 7, no. 3, pp. 328–331, Jun. 2018.

[14] H. Li, P. Li, G. Cheng, J. Xu, J. Chen, and Y. Zeng, “Channel knowledge map (CKM)-assisted multi-UAV wireless network: CKM construction and UAV placement,” J. Commun. Inf. Netw., vol. 8, no. 3, pp. 256–270, Sep. 2023.

[15] H. Li, M. Xiao, K. Wang, D. I. Kim, and M. Debbah, “Large language model based multi-objective optimization for integrated sensing and communications in UAV networks,” IEEE Wireless Commun. Lett., vol. 14, no. 4, pp. 979–983, Apr. 2025.

[16] W.-Y. Dong, S. Yang, P. Zhang, and S. Chen, “Stochastic geometry based modeling and analysis of uplink cooperative satellite-aerial-terrestrial networks for nomadic communications with weak satellite coverage,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3428–3444, Dec. 2024.

[17] S. Liu, H. Yang, M. Zheng, and L. Xiao, “Multi-UAV-assisted MEC in IoV with combined multi-modal semantic communication under jamming attacks,” IEEE Trans. Mobile Comput., vol. 24, no. 8, pp. 7600–7614, Aug. 2025.

[18] T. Wu, M. Li, Y. Qu, H. Wang, Z. Wei, and J. Cao, “Joint UAV deployment and edge association for energy-efficient federated learning,” IEEE Trans. Cogn. Commun. Netw., vol. 11, no. 6, pp. 4126–4140, Dec. 2025.

[19] H. Xiao, X. Hu, W. Wang, Z. Su, K. Wong, and K. Yang, “STAR-RIS and UAV combination in MEC networks: Simultaneous task offloading and communications,” IEEE Trans. Commun., vol. 73, no. 8, pp. 6169–6184, Aug. 2025.

[20] A. Telikani et al., “Unmanned aerial vehicle-aided intelligent transportation systems: Vision, challenges, and opportunities,” IEEE Commun. Surv. Tuts., vol. 27, no. 6, pp. 3772–3819, Dec. 2025.

[21] M. Tao, X. Li, J. Feng, D. Lan, J. Du, and C. Wu, “Multi-agent cooperation for computing power scheduling in UAVs empowered aerial computing systems,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3521–3535, Dec. 2024.

[22] Y. Deng, H. Zhang, X. Chen, and Y. Fang, “UAV-assisted MEC with an expandable computing resource pool: Rethinking the UAV deployment,” IEEE Wirel. Commun., vol. 31, no. 5, pp. 110–116, Oct. 2024.

[23] X. Guo et al., “Integrated energy-efficient planning and management framework for autonomous long-endurance flight of hydrogen fuel cell/battery hybrid UAVs,” IEEE/ASME Trans. Mechatron., vol. 30, no. 6, pp. 6337–6347, Dec. 2025.

[24] S. Zhao, J. Ni, T. Lei, Y. Du, and S. Deng, “Dynamic-memory eventtriggered fixed-time distributed power management for UAV power system under intermittent communication failures,” IEEE Trans. Aerosp. Electron. Syst., vol. 61, no. 5, pp. 14533–14546, Oct. 2025.

[25] Y. Xu, T. Zhang, Y. Liu, D. Yang, L. Xiao, and M. Tao, “3D multi-UAV computing networks: Computation capacity and energy consumption tradeoff,” IEEE Trans. Veh. Technol., vol. 73, no. 7, pp. 10627–10641, Jul. 2024.

[26] H. Gong, B. Huang, and B. Jia, “Energy-efficient 3-D UAV ground node accessing using the minimum number of UAVs,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 12046–12060, Dec. 2024.

[27] X. Zhu, L. Zhai, N. Li, Y. Li, and F. Yang, “Multi-objective deployment optimization of UAVs for energy-efficient wireless coverage,” IEEE Trans. Commun., vol. 72, no. 6, pp. 3587–3601, Jun. 2024.

[28] M. D. Nguyen, W. Ajib, W. Zhu, and G. K. Kurt, “Integrated user association, computation offloading, resource allocation, and UAV trajectory control against jamming for UAV-based wireless networks,” IEEE Trans. Wireless Commun., vol. 24, no. 7, pp. 5588–5604, Jul. 2025.

[29] S. Qi, B. Lin, Y. Deng, X. Chen, and Y. Fang, “Minimizing maximum latency of task offloading for multi-UAV-assisted maritime search and rescue,” IEEE Trans. Veh. Technol., vol. 73, no. 9, pp. 13625–13638, Sep. 2024.

[30] F. Lu et al., “Resource and trajectory optimization for UAV-relayassisted secure maritime MEC,” IEEE Trans. Commun., vol. 72, no. 3, pp. 1641–1652, Mar. 2024.

[31] W. Pan, N. Lv, B. Hou, and Z. Ren, “Resource allocation and outage probability optimization method for multi-hop UAV relay network for servicing heterogeneous users,” IEEE Trans. Netw. Sci. Eng., vol. 11, no. 3, pp. 2769–2781, May/Jun. 2024.

[32] X. Lin, S. Bi, G. Su, and Y. Zhang, “A Lyapunov-based approach to joint optimization of resource allocation and 3-D trajectory for solarpowered UAV MEC systems,” IEEE Internet Things J., vol. 11, no. 11, pp. 20797–20815, Jun. 2024.

[33] Z. Lyu et al., “Empowering intelligent low-altitude economy with large AI model deployment,” 2025, arXiv:2505.22343.

[34] C. Wang, D. Zhai, R. Zhang, L. Cai, L. Liu, and M. Dong, “Joint association, trajectory, offloading, and resource optimization in air and ground cooperative MEC systems,” IEEE Trans. Veh. Technol., vol. 73, no. 9, pp. 13076–13089, Sep. 2024.

[35] A. Nabi and S. Moh, “Joint offloading decision, user association, and resource allocation in hierarchical aerial computing: Collaboration of UAVs and HAP,” IEEE Trans. Mobile Comput., vol. 24, no. 8, pp. 7267–7282, Aug. 2025.

[36] Y. Deng, H. Zhang, X. Chen, and Y. Fang, “UAV-assisted multi-access edge computing with altitude-dependent computing power,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 9404–9418, Aug. 2024.

[37] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

[38] J. Xu, Y. Zeng, and R. Zhang, “UAV-enabled wireless power transfer: Trajectory design and energy optimization,” IEEE Trans. Wireless Commun., vol. 17, no. 8, pp. 5092–5106, Aug. 2018.

[39] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.

[40] T. Zhang, G. Liu, H. Zhang, W. Kang, G. K. Karagiannidis, and A. Nallanathan, “Energy-efficient resource allocation and trajectory design for UAV relaying systems,” IEEE Trans. Commun., vol. 68, no. 10, pp. 6483–6498, Oct. 2020.

[41] J. Møller and F. P. Schoenberg, “Thinning spatial point processes into poisson processes,” Adv. Appl. Probab., vol. 42, no. 2, pp. 347–358, Jul. 2010.

[42] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.

[43] S.-W. Ko, K. Han, and K. Huang, “Wireless networks for mobile edge computing: Spatial modeling and latency analysis,” IEEE Trans. Wireless Commun., vol. 17, no. 8, pp. 5225–5240, Aug. 2018.

[44] S. P. Lalley, “Poisson processes,” Dept. Statist., Univ. Chicago, Chicago, IL, USA. [Online]. Available: https://galton.uchicago.edu/lalley/Courses/ 312/PoissonProcesses.pdf

[45] F. Pervez, A. Sultana, C. Yang, and L. Zhao, “Energy and latency efficient joint communication and computation optimization in a multi-UAVassisted MEC network,” IEEE Trans. Wireless Commun., vol. 23, no. 3, pp. 1728–1741, Mar. 2024.

[46] X. Wang, Y. Jin, S. Schmitt, and M. Olhofer, “Recent advances in Bayesian optimization,” ACM Comput. Surv., vol. 55, no. 13, pp. 1–36, Jul. 2023.

![](images/7ef5fb0a7cfef0b04c41c02d834beb6d1b0fec6eb0baad38aa7a9aa03f32af61.jpg)

Yiqin Deng (Member, IEEE) received the MS degree in software engineering and the PhD degree in computer science and technology from Central South University, Changsha, China, in 2017 and 2022, respectively. From 2019 to 2021, she was a visiting researcher with the University of Florida, Gainesville, FL, USA. From 2022 to 2024, she was a Postdoctoral Research Fellow with the School of Control Science and Engineering, Shandong University, Jinan, China. From 2024 to 2026, she was a postdoctoral research fellow with the Department of Computer Science,

City University of Hong Kong. She is currently a research assistant professor with the School of Data Science, Lingnan University, Hong Kong. Her research interests include edge computing/AI, wireless communication and networking, computing power networks, and the low-altitude economy.

![](images/ba1df2ea04623b32efcd31c32f5395713f80526606f49ad927298452e3816823.jpg)

Zhengru Fang (Graduate Student Member, IEEE) received the BS degree (with Hons.) in electronics and information engineering from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2019, and the MS degree (with Hons.) from Tsinghua University, Beijing, China, in 2022. He is currently working toward the PhD degree with the Department of Computer Science, City University of Hong Kong. His research work has been published in IEEE/CVF CVPR, IEEE/ACM Transactions on Networking, IEEE Journal on Selected Areas in

Communications, IEEE Transactions on Mobile Computing, IEEE ICRA, and ACM MM. His research interests include collaborative perception, V2X, age of information, and mobile edge computing. He was the recipient of Outstanding Thesis Award from Tsinghua University in 2022, Excellent Master Thesis Award from the Chinese Institute of Electronics in 2023, and the Hong Kong PhD Fellowship Scheme (HKPFS).

![](images/7f9b10aa647ece47d063c2bdc80930097a2a47d6597598efcc9d382ee34be389.jpg)

Senkang Hu (Graduate Student Member, IEEE)received the BEng degree from the School of Information and Electronics, Beijing Institute of Technology, in 2022. He is currently working toward the PhD degree with the Department of Computer Science, City University of Hong Kong and also from the Hong Kong JC STEM Lab of Smart City. He research interests include LLM-empowered multi-agent systems, LLM post-training, and autonomous driving. His works have been published in top-tier journals such as IEEE Transactions on

Mobile Computing (IEEE TMC), IEEE Transactions on Intelligent Transport Systems (IEEE TITS), IEEE/ACM Transactions on Networking (IEEE ToN), and top-tier conferences such as AAAI and ICRA. He is also a reviewer or Technical Program Committee member for ICML, ICLR, NeurIPS, ICRA, TMC, ToN, and TITS.

![](images/e82fec0806f2c1ba1bd26644e46bfbba4b3356eafbb156d8231018b2bc5fa29e.jpg)

Yanan Ma (Graduate Student Member, IEEE) received the BEng degree (with Hons.) in electronic information engineering (english intensive) and the MEng degree (with Hons.) in information and communication engineering from the Dalian University of Technology, Dalian, China, in 2020 and 2023, respectively. She is currently working toward the PhD degree with the Department of Computer Science, City University of Hong Kong. Her research interests include edge intelligence, wireless communication and networking, and machine learning. She was the recipient of the IEEE GLOBECOM Best Paper Award in 2025.

![](images/c2c24f2afbb7dbae3967b451bbb1d0831432ad6f736ca7a9fa084da62c34161f.jpg)

Xiaoyu Guo (Member, IEEE) received the bachelor’s degree from Beihang University, in 2018, the master’s degree (with Distinction) from the University of Cambridge, in 2019, and the PhD degree from the University of Manchester, in 2023. He is currently an assistant professor with the Department of Mechanical Engineering, City University of Hong Kong. He has authored or coauthored more than 40 papers in international journals including Nature Communications, IEEE Transactions on Automatic Control, Automatica, and IEEE/ASME Transactions

on Mechatronics. He was also granted more than 20 invention patents. His research interests include hydrogen-powered robotic systems, and bio-inspired control and perception. He is an assosciate editor for IEEE Transactions on Industrial Informatics, and Unmanned Systems.

![](images/67cbeeb937d3d11bb358125aa8dbd923e50288643df16d103878e5add000a0c2.jpg)

Haixia Zhang (Senior Member, IEEE) received the BE degree from the Department of Communication and Information Engineering, Guilin University of Electronic Technology, Guilin, China, in 2001, and the MEng and PhD degrees in communication and information systems from the School of Information Science and Engineering, Shandong University, Jinan, China, in 2004 and 2008, respectively. From 2006 to 2008, she was with the Institute for Circuit and Signal Processing, Munich University of Technology, Munich, Germany, as an academic assistant. From

2016 to 2017, she was a visiting professor with the University of Florida, Gainesville, FL, USA. She is currently a full professor with Shandong University, Jinan, China. Her research interests include wireless communication and networks, industrial Internet of Things, wireless resource management, and mobile edge computing. Dr. Zhang is actively participating in many professional services. She is/was the editor of the IEEE Transactions on Wireless Communications, IEEE Internet of Things Journal, IEEE Wireless Communication Letters, and China Communications and is/was as Symposium Chairs, TPC Members, Session Chairs, and Keynote Speakers of many conferences.

![](images/27f2280c97bf23b60d610fa2451985e0f4b07e78e9df02d24f97daa7eb22553a.jpg)

Yuguang Fang (Fellow, IEEE) received the MS degree from Qufu Normal University, China, the PhD degree from Case Western Reserve University, USA, and the second PhD degree from Boston University, USA, in 1987, 1994, and 1997, respectively. In 2000, he joined the Department of Electrical and Computer Engineering, University of Florida, as an assistant professor, and was promoted to associate professor, full professor, and distinguished Professor, in 2003, 2005, and 2019, respectively. Since 2022, he has been a Global STEM scholar and chair professor with the

Department of Computer Science, City University of Hong Kong. He is currently the founding director with the Hong Kong JC STEM Lab of Smart City funded by The Hong Kong Jockey Club Charities Trust. He was the recipient of many awards including U.S. NSF CAREER Award, U.S. ONR Young Investigator Award, 2018 IEEE Vehicular Technology Outstanding Service Award, and several IEEE Communications Society awards (AHSN Technical Achievement Award, CISTC Technical Recognition Award, and WTC Recognition Award). He was the editor-in-chief of IEEE Transactions on Vehicular Technology and IEEE Wireless Communications. He is also a fellow of ACM and AAAS.