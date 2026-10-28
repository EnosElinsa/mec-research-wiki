# Disconnectivity-Aware Energy-Efficient Cargo-UAV Trajectory Planning with Minimum Handoffs

Nesrine Cherif<sup>∗</sup>, Wael Jaafar<sup>†</sup>, Halim Yanikomeroglu<sup>†</sup>, and Abbas Yongacoglu<sup>∗</sup>.

<sup>∗</sup>School of Electrical Engineering and Computer Science, University of Ottawa, Ottawa, ON, Canada. <sup>†</sup>Department of Systems and Computer Engineering, Carleton University, Ottawa, ON, Canada.

Abstract—On-board battery consumption, cellular disconnectivity, and frequent handoff are key challenges for unmanned aerial vehicle (UAV) based delivery missions, a.k.a., cargo-UAV. Indeed, with the introduction of UAV technology into cargo shipping and logistics, designing energy-efficient paths becomes a serious issue for the next retail industry transformation. Typically, the latter has to guarantee uninterrupted or slightly interrupted cellular connectivity for the UAV’s command and control through a small number of handoffs. In this paper, we formulate the trajectory planning as a multi-objective problem aiming to minimize both the UAV’s energy consumption and the handoff rate, constrained by the UAV battery size and disconnectivity rate. Due to the problem’s complexity, we propose a dynamic programming based solution. Through simulations, we demonstrate the efficiency of our approach in providing optimized UAV trajectories. Also, the impact of several parameters, such as the cargo-UAV altitude, disconnectivity rate, and type of environment, are investigated. The obtained results allow to draw recommendations and guidelines for cargo-UAV operations.

## I. INTRODUCTION

Cargo unmanned aerial vehicle (cargo-UAV) is a popular mean of delivery, especially for remote and hard-to-reach areas [1]. Due to the technological advancements that made cargo-UAVs safer and cost-efficient, it is expected that the latter be deployed in dense urban centres [2]. Since cargo-UAVs operate at beyond visual line-of-sight (BVLoS), command and control (C&C) is crucial in ensuring the safety and security of the mission [3]. The latter relies on cellular networks, which have to be reliable enough for safe operation. Several works have investigated the practicality and feasibility of BVLoS cellularconnected UAVs [4]–[6].

Reusing the terrestrial networks for cargo-UAV cellular connectivity presents its own set of challenges as these networks were primarily designed to serve ground users only [2]. Although economically attractive, it may be difficult to provide reliable and seamless cellular connectivity to the cargo-UAVs, especially at high altitudes. Indeed, terrestrial base stations (BSs) are down-tilted, which means that cargo-UAVs can be served only through the sidelobes of BS antennas [7, Fig. 6]. Moreover, the cargo-UAV’s inherited mobility leads to frequent switching from one serving BS to another, i.e., handoff. As such, an additional amount of information is exchanged, which degrades further the transmission link. Even

though the energy consumption related to the communication overhead is relatively small compared to the cargo-UAV’s motion energy, handoff events should be kept to the minimum in order to guarantee the C&C stability. Due to the aforementioned factors, occasional cellular disconnectivity can be experienced by cargo-UAVs operating in BVLoS. Depending on the criticality of the mission and the level of autonomy, a cargo-UAV can tolerate an end-to-end disconnectivity rate, defined as the ratio of the time spent disconnected from all cellular BSs to the total mission time.

## A. Related Work

In order to keep low handoff and disconnectivity rates, cargo-UAV trajectory planning became significantly important in BVLoS missions. This problem has attracted many researchers for the last few years. For instance, the authors of [8] set up a testbed for cellular-connected UAV missions in the sky. Their qualitative study showed that handoff occurs more frequently for UAVs, compared to terrestrial users. Hence, proper UAV motion optimization is needed to reduce handoffs. A cellular disconnectivity-aware trajectory design was proposed in [9]. However, the authors relied rather on a simplistic cellular-to-air (C2A) propagation model that does not reflect the real 3D radiation patterns of BSs. In contrast, the authors of [10] studied the effects of both realistic 3D antenna radiation and limited backhaul on the UAV trajectory planning problem. Yet, this work lacked the insights on the handoff and disconnectivity rates during UAV missions. Recently, reinforcement-learning based trajectory planning solutions have been proposed for energy-efficiency maximization [11], mission time minimization [12], and route distance minimization [13]. However, none of these works has accounted for the UAV energy consumption, cellular disconnectivity, and handoffs, altogether. This has been investigated for the first time in [14], where a multi-armed-bandit based UAV velocity strategy is proposed for a predefined trajectory, and under a weighted handoff rate, cellular disconnectivity, and power consumption objective. However, the trajectory was not optimized with consideration of these factors.

## B. Contributions

Given the limitations of the aforementioned works, we study in this paper the disconnectivity and handoff aware trajectory planning problem for cargo-UAVs. Specifically, we aim to minimize the UAV’s energy consumption and handoff rate, with respect to the battery size and disconnectivity rate. Due to the problem’s complexity, we propose a dynamic programming (DP) based solution that provides reliable cargo-UAV trajectories. Through simulations, the efficiency of our method is demonstrated. Finally, by evaluating the impact of several parameters, e.g., cellular connectivity conditions and UAV altitude, we provide design guidelines for cargo-UAV operations.

The remaining of the paper is organized as follows. Section II presents the system model. Section III formulates the trajectory planning problem. Section IV presents the proposed DP-based solution, while the simulation results are discussed in Section V. Finally, Section VI closes the paper.

## II. SYSTEM MODEL

We assume a geographical area with its airspace, defined through a 3-dimensional (3D) axes system $( x , y , z )$ . As per the 3GPP report [15], a cargo-UAV is allowed to hover/fly at a maximum altitude of 300 m above the ground level. We assume that the cargo-UAV mission is to deliver an item from a retailer’s warehouse, located in $( x _ { s } , y _ { s } )$ in the $( x , y )$ plane to a consumer’s drop-off location $( x _ { d } , y _ { d } )$ . We envision that the cargo-UAV hovers vertically from the warehouse’s dockstation until it reaches the desired altitude $h \leq 3 0 0$ m at coordinates $\mathrm { S T A R T } = ( x _ { s } , y _ { s } , h )$ , then it travels horizontally with a fixed velocity v to reach the destination point, defined as END = $( x _ { d } , y _ { d } , h )$ . Finally, the cargo-UAV lands vertically to the dropoff location $( x _ { d } , y _ { d } )$

We assume that the cargo-UAV is exclusively served by the terrestrial cellular network. The latter is constituted of M BSs, where the location of the $i ^ { t h }$ BS is denoted by $( x _ { \mathrm { B S } } ^ { i } , y _ { \mathrm { B S } } ^ { i } , z _ { \mathrm { B S } } )$ The height of the BS depends on the type of environment, which is selected from 35 m, 25 m, and 10 m, for rural macro (RMa), urban macro (UMa), and urban micro (UMi), respectively.

## A. C2A Channel Model

The C2A channel model is outlined in the 3GPP reports [15], [16]. It considers several parameters, including the BS’s antenna gain, LoS probability, and path-loss.

1) BS Antenna Gain: As mentioned previously, UAVs in the sky are mainly connected to BSs through the radiating sidelobes. Hence, accurately modelling the BS 3D antenna radiation pattern is needed for accurate trajectory planning. In this work, we adopt the 3GPP antenna pattern model that mimics realistic antenna patterns [16]. That means, each BS is divided into three sectors, where a sector is equipped with cross-polarized antennas to form a uniform linear array (ULA). Each antenna element provides a gain up to $G _ { \mathrm { m a x } }$ (typically 8 dBi) in the direction of the mainlobe. The antenna element pattern is given by [16, Table 7.1.-1], which provides certain gains depending on the azimuth and elevation angles of the cargo-UAV with respect to the BS’s location. They are respectively given by

$$
G _ { \mathrm { a z } } ( \phi _ { i } ) = \operatorname* { m i n } \left\{ 1 2 \left( \frac { \phi _ { i } } { \phi _ { \mathrm { 3 d B } } } \right) , G _ { m } \right\} ,\tag{1}
$$

$$
G _ { \mathrm { e l } } ( \theta _ { i } ) = \mathrm { m i n } \left\{ 1 2 \left( \frac { \theta _ { i } } { \theta _ { \mathrm { 3 d B } } } \right) , \mathrm { S L A } \right\} ,\tag{2}
$$

where $\begin{array} { r } { \phi _ { i } = \tan ^ { - 1 } \left( \frac { h - z _ { \mathrm { B S } } } { d _ { 2 D , i } } \right) } \end{array}$ and $\begin{array} { r } { \theta _ { i } = \tan ^ { - 1 } \left( \frac { y - y _ { \mathrm { B S } } ^ { i } } { x - x _ { \mathrm { B S } } ^ { i } } \right) } \end{array}$ are the azimuth and elevation angles between the $i ^ { t h }$ BS and the cargo-UAV. Also, $d _ { 2 D , i }$ is the horizontal distance between the $i ^ { t h }$ BS and the cargo-UAV, while $\phi _ { \mathrm { 3 d B } }$ and $\theta _ { \mathrm { 3 d B } }$ are the 3 dB bandwidths fixed at $6 5 ^ { \circ }$ . Furthermore, $G _ { m }$ and SLA are the thresholds for antenna nulls, fixed to 30 dB. Finally, the antenna element gain in dB is expressed by

$$
G ( \theta _ { i } , \phi _ { i } ) = G _ { \mathrm { m a x } } - \operatorname* { m i n } \left\{ - \left( G _ { \mathrm { a z } } ( \phi _ { i } ) + G _ { \mathrm { e l } } ( \theta _ { i } ) \right) , G _ { m } \right\} .\tag{3}
$$

Assuming N antenna elements at BS i, equally distant by half of the wavelength, the array factor AF of the ULA with a down-tilt of $\theta _ { d }$ can be given by [17, eq. (2)]

$$
\operatorname { A F } ( \theta _ { i } ) = { \frac { \sin \left( { \frac { N \pi } { 2 } } \left( \sin \theta _ { i } - \sin \theta _ { d } \right) \right) } { { \sqrt { N } } \sin \left( { \frac { \pi } { 2 } } \left( \sin \theta _ { i } - \sin \theta _ { d } \right) \right) } } , \forall i = 1 , \dots , M .\tag{4}
$$

Finally, the array radiation pattern of the $i ^ { t h }$ BS is written by

$$
G _ { i } = G ( \theta _ { i } , \phi _ { i } ) + \mathrm { A F } ( \theta _ { i } ) , \forall i = 1 , \ldots , M .\tag{5}
$$

2) LoS Probability: The probability that the cargo-UAV is in LoS condition with the BS depends mainly on the terrestrial environment and the cargo-UAV altitude. For instance, when 22.5 m $< \textit { h } \leqslant 1 0 0$ m, the probability of LoS, denoted $P _ { \mathrm { L o S } } ( d _ { i } )$ in UMa is given by [15, Table B-1]

$$
\begin{array} { r } { P _ { \mathrm { L o S } } ( d _ { i } ) = \left\{ \begin{array} { l l } { 1 , \quad } & { d _ { 2 D , i } \leqslant d _ { 1 } } \\ { \frac { d _ { 1 } } { d _ { 2 D , i } } + \exp \left( \frac { - d _ { 2 D , i } } { p _ { 1 } } \right) \left( 1 - \frac { d _ { 1 } } { d _ { 2 D , i } } \right) , } & { d _ { 2 D , i } > d _ { 1 } , } \end{array} \right. } \end{array}\tag{6}
$$

where $d _ { i } = \sqrt { d _ { 2 D , i } ^ { 2 } + ( h - z _ { \mathrm { B S } } ) ^ { 2 } }$ is the 3D distance between the cargo-UAV and the $i ^ { t h } \mathrm { B S } , p _ { 1 } = 4 3 0 0 \log _ { 1 0 } ( h ) - 3 8 0 0$ , and $d _ { 1 } =$ max 460 $\log _ { 1 0 } ( h ) - 7 0 0 , 1 8 \}$ . When 100 m $< h \leq 3 0 0$ m, $P _ { \mathrm { L o S } } ( d _ { i } ) = 1$ . Finally, the NLoS probability is calculated as $P _ { \mathrm { N L o S } } ( d _ { i } ) = 1 - P _ { \mathrm { L o S } } ( d _ { i } )$

3) Pathloss Model: For the sake of simplicity, we follow the probabilistic pathloss model, as defined in [15, Tables B-1 and B-2]. The average pathloss of the channel between the cargo-UAV and the $i ^ { \star h }$ BS, denoted $L _ { i } ,$ is given by

$$
L _ { i } = P _ { \mathrm { L o S } } ( d _ { i } ) L _ { i } ^ { \mathrm { L o S } } + P _ { \mathrm { N L o S } } ( d _ { i } ) L _ { i } ^ { \mathrm { N L o S } } , \forall i = 1 , \dots , M ,\tag{7}
$$

where $L _ { i } ^ { \mathrm { L o S } }$ and $L _ { i } ^ { \mathrm { N L o S } }$ are the pathlosses related to fully LoS and NLoS communication links, respectively, defined in [15, Tables B-1 and B-2].

## B. Received Power Analysis

Based on the C2A channel model and assuming that the cargo-UAV is equipped with an omni-directional antenna with unit gain, the average received power from the $i ^ { t h }$ BS is given by

$$
P _ { r , i } = P _ { T } + G _ { i } - L _ { i } , \forall i = 1 , \ldots , M ,\tag{8}
$$

where $P _ { T }$ is the transmit power of any BS in dBm.

The received power from a BS at any 3D location determines the quality of the transmission link. As discussed in [15], the airspace is an interference-limited environment since a cargo-UAV may have cleared LoS conditions with several BSs using the same frequency resource at the same time<sup>1</sup>. Thus, we assume for simplicity that the cellular connectivity depends solely on the level of the signal-to-interference ratio (SIR), defined by

![](images/6fbc53363e907d7cf9b5e75a22329c396885a128a726e1024c85015e67b759cd.jpg)

![](images/70acabd4b763bdfec703d3b35da6eecca787724ceafd6703d75c5f0903865fce.jpg)  
Fig. 1. Cellular connectivity heatmap for different cargo-UAV altitudes. Colors denote the IDs of the serving BSs. ID 0 (dark blue) defines the coverage holes $( \theta _ { d } = - 1 0 ^ { \circ }$ , f = 2 GHz, v = 30 m/s, and $\beta _ { \mathrm { t h } } = 0 ~ \mathrm { d B } )$ .

$$
\mathsf { S l R } _ { i } = \frac { P _ { r , i } } { \displaystyle \sum _ { j = 1 , j \neq i } ^ { M } P _ { r , j } } , \forall i = 1 , \ldots , M .\tag{9}
$$

One location is presumed a coverage hole if SIR falls below a predefined threshold $\beta _ { \mathrm { t h } }$ .

Using (8), we depict in Fig. 1 the 3D cellular coverage of 10 BSs at different cargo-UAV altitudes. We assume here an area of $2 \times 2 ~ \mathrm { k m ^ { 2 } }$ , and the coverage at any 3D location is provided by the BS with the strongest SIR, i.e., SIR = $\operatorname* { m a x } _ { i = 1 , . . . , M } { \mathsf { S } } | { \mathsf { R } } _ { i }$ . We notice that the coverage area of the BS 10 at the north-east corner (clear yellow color) is located at the south-east corner of the map. This observation corroborates the fact that BSs serve cargo-UAVs using the sidelobes. Moreover, the coverage holes widen while the coverage areas shrink as the cargo-UAV flies higher. This is due to the large pathloss and low antenna gain at high elevation angles.

## C. Cargo-UAV Energy Model

The energy consumed by a cargo-UAV depends on its size, weight, and power (SWAP), in addition to its motion and communication regimes [18]. It is composed of the propulsion energy, needed for flying, and of the communication energy, for C&C operations. Typically, communication energy is very small compared to the propulsion energy, and thus, can be neglected. Using a rotary-wing cargo-UAV, the propulsion power can be given by [19]

$$
\begin{array} { r c l } { { { \cal P } _ { \mathrm { p r o p } } ( v ) } } & { { = } } & { { \displaystyle \frac { 1 } { 2 } \delta _ { 0 } \zeta r A v ^ { 3 } + \sigma _ { B } \left( 1 + \frac { 3 v ^ { 2 } } { U _ { \mathrm { t i p } } ^ { 2 } } \right) } } \\ { { } } & { { + } } & { { \displaystyle \sigma _ { I } \left( \sqrt { 1 + \frac { v ^ { 4 } } { 4 v _ { 0 } ^ { 4 } } } - \frac { v ^ { 2 } } { 2 v _ { 0 } ^ { 2 } } \right) ^ { \frac { 1 } { 2 } } , } } \end{array}\tag{10}
$$

where $\sigma _ { B }$ and $\sigma _ { I }$ are the blade profile power and induced power, respectively. v<sub>0</sub> is the mean rotor induced velocity and $U _ { \mathrm { t i p } }$ is the speed of the tip of the rotor blade. Also, ζ is the air density, $\delta _ { 0 }$ is the fuselage drag ratio, r is the rotor solidity, and A is the rotor disc area. Subsequently, the propulsion energy to fly for a distance d is

$$
E ( v , d ) = P _ { \mathrm { p r o p } } ( v ) ~ d / v , ~ v > 0 .\tag{11}
$$

We denote by $E _ { C }$ and $E _ { S }$ the initial cargo-UAV energy capacity and emergency reserve energy, respectively. $E _ { C }$ is available for the mission, while $E _ { S }$ is used in emergency pull-backs. Hence, the cargo-UAV available energy to travel between the START and END locations is

$$
E _ { A } ( v , h ) = E _ { C } - E _ { S } - 2 E ( v , h ) ,\tag{12}
$$

where $E ( v , h )$ is the required energy for tackoff/landing up to/down to the dockstation/drop-off location. Thus, the maximum horizontal travelling distance is given by

$$
d _ { \operatorname* { m a x } } = v E _ { A } ( v , h ) / P _ { \mathrm { p r o p } } ( v ) .\tag{13}
$$

## III. PROBLEM FORMULATION

The cargo-UAV mission is to deliver an item from a warehouse to a consumer drop-off location. Assuming that the cargo-UAV flies at a constant speed and altitude h, we aim to design its mission trajectory such that: 1) it consumes the lowest energy, 2) it minimizes the handoff rate, 3) it does not exhibit a cellular disconnectivity rate above a fixed threshold $\alpha _ { \mathrm { m a x } }$ during the mission. Based on the cellular connectivity heatmap shown in Fig. 1, a disconnectivity event happens when the cargo-UAV transits to/from an area with BS ID 0 (coverage hole), and the disconnectivity rate is calculated as the ratio of the time spent in areas with BS ID 0 to the total mission time. When the cargo-UAV transits from a coverage area to another (with BS IDs $\neq 0 )$ , a handoff event occurs. Then, the handoff rate is calculated as the total number of handoff events during the mission. Let $\mathcal { T } = \{ \mathbf { q } _ { 1 } , \dots , \mathbf { q } _ { | \mathcal { T } | } \}$ be the trajectory of the cargo-UAV, defined by the locations $\mathbf { q } _ { i } = ( x _ { i } , y _ { i } , h )$ . Also, let $\boldsymbol { S } = \left\{ \boldsymbol { s } _ { 1 } , \ldots , \boldsymbol { s } _ { | T | } \right\}$ be the set of BS IDs associated to the cargo-UAV locations in . Subsequently, the trajectory planning problem can be formulated as follows:

$$
\operatorname* { m i n } _ { \mathcal { T } } \quad w _ { 1 } \sum _ { i = 1 } ^ { | \mathcal { T } | - 1 } E ( v , d _ { i , i + 1 } ) + w _ { 2 } \sum _ { i = 1 } ^ { | \mathcal { T } | - 1 } \eta _ { i , i + 1 }\tag{P1}
$$

$$
\mathrm { s . t . } \sum _ { i = 1 } ^ { | T | - 1 } E ( v , d _ { i , i + 1 } ) \leq E _ { A } ( v , h ) ,\tag{P1.a}
$$

![](images/e5064d952c2c1671cd0e3b4c4fde584429edf180a6c8d5d2e48279762979567a.jpg)  
Fig. 2. Motion options for the cargo-UAV in one step.

$$
\frac { d _ { \mathrm { d i s c } } } { | T | - 1 } \leq \alpha _ { \mathrm { m a x } } ,\tag{P1.b}
$$

where $w _ { 1 }$ and $w _ { 2 }$ are weight factors balancing between energy consumption and handoff rate. $d _ { i , i + 1 } = \lVert { \bf q } _ { i } - { \bf q } _ { i + 1 } \rVert , d _ { \mathrm { d i s c } }$ is the sum of flying distances in coverage holes, and $\eta _ { i , i + 1 }$ is a binary variable reflecting the handoff event, i.e., $\eta _ { i , i + 1 } = 1$ if $s _ { i } \neq s _ { i + 1 }$ and $( s _ { i } , s _ { i + 1 } ) \neq ( 0 , 0 )$ , and $\eta _ { i , i + 1 } = 0$ otherwise. Problem (P1) is NP-hard. Indeed, the latter can be seen as the capacitated vehicle routing problem (CVRP) [20]. The CVRP is described as selecting the route for a vehicle, aiming to serve a group of customers. The vehicle has a limited capacity, which is used to depart from a depot point, serve a number of customers along its route, then return to the same or a different depot point. The objective of the CVRP is to minimize the total transport costs. Logically, the vehicle, customers, and transport costs, can be assimilated by the UAV, BSs, and (energy consumption + handoff rate), respectively. Since the CVRP is known to be NP-hard [20], then by restriction, (P1) is also NP-hard.

## IV. PROPOSED SOLUTION: DP ALGORITHM

In this section, we adopt, similarly to [9], the dynamic programming approach to derive a near-optimal trajectory solution for (P1).

First, we start by dividing the plane $( x , y )$ at altitude h to a grid of cells, numbered from 1 to J. We assume that the cargo-UAV can move in one step from the center of one cell to the center of an adjacent cell in one of the available directions, i.e., one of 8 movements can be realized as shown in Fig. 2. We define by $\mathcal { T } _ { j } , \boldsymbol { S } _ { j } , d _ { \mathrm { d i s c } } ^ { j }$ , and $E _ { j }$ the best trajectory to reach cell j (with respect to energy and disconnectivity constraints), the corresponding set of BS IDs, the sum of flying distances in coverage holes to reach cell $j$ when following trajectory $\tau _ { j }$ and the associated cargo-UAV consumed energy, respectively. Thus, for any cell $j ,$ the objective function can be computed

$$
\overset { \mathrm { a s } } { O _ { j } } ( t ) = \operatorname* { m i n } _ { j ^ { \prime } \in \mathcal { N } _ { j } } \left\{ O _ { j ^ { \prime } } ( t - 1 ) + w _ { 1 } E ( v , d _ { j ^ { \prime } , j } ) + w _ { 2 } \eta _ { j ^ { \prime } , j } \right\}\tag{15}
$$

such that $E _ { j ^ { \prime } } + E ( v , d _ { j ^ { \prime } , j } ) \leq E _ { A } ; \ \frac { d _ { \mathrm { d i s c } } ^ { j } } { \displaystyle \sum _ { i = 1 } ^ { j _ { j } / - 1 } d _ { i , i + 1 } } \leq \alpha _ { \operatorname* { m a x } } ,$

where t is the stage in the optimization process, ${ \mathcal { N } } _ { j }$ is the set of neighbouring cells to cell $j , \eta _ { j ^ { \prime } , j }$ is the binary variable indicating a handoff event, and

![](images/93befe6e6580b68710a67bf5b016dedc3ec740dc1eb6c920f0756816fded956c.jpg)  
Fig. 3. Cargo-UAV paths $( h = 2 0 0$ m, different $\alpha _ { \mathrm { m a x } } )$

$$
O _ { j } ( t ) = w _ { 1 } \sum _ { i = 1 } ^ { | T _ { j } | - 1 } E ( v , d _ { i , i + 1 } ) + w _ { 2 } \sum _ { i = 1 } ^ { | T _ { j } | - 1 } \eta _ { i , i + 1 } , \forall j .\tag{16}
$$

Eq. (15) states that if the cargo-UAV can reach the $j ^ { t h }$ cell from a neighboring cell while 1) minimizing the objective function, 2) not exceeding the available on-board energy, and 3) not exceeding the disconnectivity rate threshold, then, the new optimal trajectory is from that neighboring cell. When repeated with a sufficient number of iterations, this step provides the optimal trajectory.

In Algorithm 1, we present the pseudocode for the DP-based trajectory planning method. In lines 2 and 3, the minimum cost path matrices are initialized and computed. Then, the stage cost matrices are initialized in lines 4 and 5, where the initial cost of the START cell is set to zero. In line $^ { 6 , }$ we generate the matrix in which we will store the optimal cells indices guaranteeing the smallest costs. Lines 7 to 21 execute the DP algorithm iterations, where the battery, cellular disconnectivity, and handoff constraints are handled in line 13. Then, the solution is refined with a smaller cost at each iteration, as shown in line 14. Finally, the optimal path is extracted recursively in the procedure of lines 22 to 31.

## V. SIMULATION RESULTS

In this section, we evaluate the performance of the cargo-UAV DP-based path planning solution. Unless stated elsewhere, we assume here 10 BSs deployed in an UMa environment using the pathloss model of [15, Table B-1]. As shown in Fig. 3, the START and END locations for the cargo-UAV mission are selected in the two opposite corners of the map. We set the following parameters to $G _ { \mathrm { m a x } } = 8 \mathrm { d B i } , \theta _ { d } = - 1 0 ^ { \circ }$ $P _ { T } ~ = ~ 4 3$ dBm, $ { \boldsymbol { v } } \ = \ \ 3 0$ m/s, $E _ { C } - E _ { S } = 2 5 0 0$ kJ, and $w _ { 1 } = w _ { 2 } = 1$ . Finally, typical values of the cargo-UAV related parameters are taken from [19, Table I].

In Fig. 3, we illustrate the resulting cargo-UAV paths using Algorithm 1, given different values of the tolerated disconnectivity $\alpha _ { \mathrm { m a x } }$ . The dark blue color refers to the coverage holes, while the other colors correspond to the coverage areas of 10 BSs, located as shown in Fig. 1. As $\alpha _ { \mathrm { m a x } }$ decreases, we see that the followed path is longer. Indeed, the UAV needs to make detours in order to avoid partially $( \alpha _ { \mathrm { m a x } } > 0 \% )$ or completely $( \alpha _ { \mathrm { m a x } } = 0 \% )$ the coverage holes.

```latex
Algorithm 1 DP-based Trajectory Planning
Input: Matrix H of size $( M \times N )$ representing cellular connectivity
heatmap (e.g., Fig. 1), step size γ, v, α<sub>max</sub>, $E _ { A } .$ max<sub>iter</sub>, and
START and END locations.
Output: Optimal trajectory $\tau ^ { * }$
1: Compute $d _ { \mathrm { m a x } }$ using (13).
2: Initialize transition matrices T , $\nu \in$ {dist, disc, ho} of size
$( M N \times M N )$ with ∞.
3: Compute the cost (dist, disc, ho) from each cell in H to all other
cells and store it in $T _ { \nu } , \nu \in$ {dist, disc, ho}.
4: Initialize stage cost matrices $( S _ { \mathrm { d i s t } } , \ S _ { \mathrm { d i s c } } ,$ , and $S _ { \mathbf { h o } } )$ of size
[1, M] with ∞.
5: Set the initial cost of the START cell to $0 , \mathrm { i . e . , } S _ { \nu } ( \mathrm { S T A R T } ) = 0 ,$
ν ∈ {dist, disc, ho}.
6: Generate the predecessor matrix $P _ { \mathrm { d i s t } }$ of size $( M \times \operatorname* { m a x } _ { \mathrm { i t e r } } )$ for
recursion. % max is the maximal number of DP iterations
7: for $q = 2$ to max do
8: Store $S _ { \nu }$ in predecessor matrix $S _ { \nu } ^ { \mathrm { p r } }$ $\nu \in$ {dist, disc, ho}.
9: for i = 1 to M do
10: for $j = 1$ to N do
11: Compute the ν cost from cell j to cell i,
$\begin{array} { r } { \mathrm { i . e . , } \ \hat { \nu } _ { j } = T _ { \nu } ( j , i ) + S _ { \nu } ^ { \mathrm { p r } } ( j ) , \ \nu ^ { \mathrm { ' } } \in \{ \mathrm { d i s t , d i s c , h o } \} . } \end{array}$
12: if the previous distance cost is higher than the
computed one, i.e., dist<sub>j</sub> 6 S<sub>dist</sub>(j) then
13: if dist<sub>j</sub> 6 d<sub>max</sub> & disc<sub>j</sub> dist 6 α<sub>max</sub>,
& ho $_ j \leqslant S _ { \mathrm { h o } } ( j )$ then
14: Update S<sub>ν</sub> S<sub>ν</sub>(j) = ν<sub>j</sub>, ν ∈ {dist, disc, ho}.
15: Store the optimal path from cell j to cell i
in $P _ { \mathrm { d i s t } } ( j , { \dot { q } } ) = i .$
16: end if
17: end if
18: end for
19: end for
20: Break if the END cell is reached.
21: end for
22: Set the current cell to END cell.
23: Set st = size $P _ { \mathrm { d i s t } } , 2 ) ,$ index ind=2, and cell = END.
24: while 1 do
25: $\begin{array} { r l } { \mathcal { T } ^ { * } ( \mathrm { i n d - 1 } ) } & { { } = } \end{array}$ cell
26: cell= $P _ { \mathrm { d i s t } }$ (ind − 1, st − ind + 1)
27: if cell = START then
28: $\mathcal { T } ^ { * } ( \mathrm { i n d } ) = \mathrm { S T A R T }$
29: Break
30: end if
31: Set ind=ind+1.
32: end while
33: Return the optimal path stored in $\tau ^ { * }$ , representing the array of
cells that the cargo-UAV should visit to reach the END cell.
```

Fig. 4 shows the consumed energy rate, defined as the ratio of the consumed energy for the mission to the available energy $E _ { C } - E _ { S }$ , for the setup of Fig. 3. This performance metric is evaluated as a function of the flying altitude h and for different disconnectivity rates $\alpha _ { \mathrm { m a x } } . ~ \mathrm { A s } ~ \alpha _ { \mathrm { m a x } }$ becomes more stringent, the cargo-UAV consumes more energy in order to execute detours and avoid coverage holes, thus agreeing with the results of Fig. 3. Also, the energy consumption increases with the altitude. Indeed, in addition to the energy consumed between START and END locations, the cargo-UAV has to spend more effort in takeoff and landing to reach them.

In Fig. 5, we present the handoff rate as a function of h and for different $\alpha _ { \mathrm { m a x } }$ , given the setup of Fig. 3. We notice no clear trend or correlation can be identified between the handoff rate and the cargo-UAV altitude. However, the handoff rate increases as $\alpha _ { \mathrm { m a x } }$ decreases, given a fixed h. Indeed, as $\alpha _ { \mathrm { m a x } }$ nears zero, i.e., no disconnectivity is allowed, the cargo-UAV is required to follow paths that avoid coverage holes, i.e., it is more likely to trigger handoff events when travelling.

78%   
αmax = 0%   
ate 76% …… αmax = 5%   
…… αmax = 10%   
74% --x-- αmax = 20%   
- - - αmax = 30%   
72%   
70%   
68%   
66%   
62%   
40 60 80 100 120 140 160 180 200 220 240 260 280 300   
Cargo-UAV altitude h in meters

Fig. 4. Consumed energy rate vs. h (different α<sub>max</sub>).  
5%   
10%   
30%   
220 260 300   
Cargo-UAV altitude h in meters  
Fig. 5. Handoff rate vs. h (different $\alpha _ { \mathrm { m a x } } ) .$

Fig. 6 illustrates the average handoff rate (over different cargo-UAV altitudes) as a function of $\alpha _ { \mathrm { { m a x } } }$ , and for different SIR threshold values $\beta _ { \mathrm { t h } } . { \mathrm { A s } } \ \alpha _ { \mathrm { m a x } }$ increases, the handoff rate improves. Indeed, with $\alpha _ { \mathrm { m a x } }$ loosened, the cargo-UAV can cross a higher number of coverage holes, which does not account for handoff events. In contrast, a stringent $\alpha _ { \mathrm { m a x } }$ obligates the cargo-UAV to move only within the BSs’ coverage areas, thus increasing the handoff rate. Moreover, the handoff rate degrades as $\beta _ { \mathrm { t h } }$ decreases. In fact, a small $\beta _ { \mathrm { t h } }$ means that a small number of (or no) coverage holes are present within the network. Thus, the cargo-UAV experiences frequent handoffs when travelling. Finally, we notice that the average handoff rate is independent from $\alpha _ { \mathrm { m a x } }$ when $\beta _ { \mathrm { t h } } = - 5$ dB. Indeed, for this $\beta _ { \mathrm { t h } }$ value, no coverage holes are present, and hence no disconnectivity is encountered in the cargo-UAV path.

We investigate in Fig. 7 the average consumed energy rate as a function of $\alpha _ { \mathrm { m a x } } ,$ for different types of environments, namely UMa, UMi, and RMa, characterized by the BSs density $\lambda ,$ and where the results are averaged over 200 Monte-Carlo realisations of BSs locations. First, the energy performance improves with $\alpha _ { \mathrm { m a x } }$ in any environment type. This is expected since a more direct path is followed by the cargo-UAV for higher $\alpha _ { \mathrm { m a x } }$ . Second, RMa achieves the best consumed energy rate for any $\alpha _ { \mathrm { m a x } } .$ . Indeed, in RMa, a small number of BSs is used, which limits inter-cell interference and hence improves the coverage of the BSs. Consequently, short paths are followed by the cargo-UAV to reach its destination. However, as the environment becomes denser with BSs, the impact of inter-cell interference amplifies due to LoS links, causing a significant degradation to communication channels and coverage areas. Hence, the cargo-UAV has to make detours in order to reach its destination with respect to $\alpha _ { \mathrm { m a x } }$

![](images/93467f23a906ac6043af2a89c8e5cc32b3412f43f073ca70ee12eb717c87fbd8.jpg)

Fig. 6. Avg. handoff rate vs. $\alpha _ { \mathrm { m a x } }$ (different $\beta _ { \mathrm { t h } } )$  
![](images/7806c940bc7b12463df8dc7f1a2cc1ad6220ac917f8acbd7e454d7032b94a786.jpg)  
Fig. 7. Avg. consumed energy rate vs. $\alpha _ { \mathrm { m a x } }$ $( h ~ = ~ 1 0 0 ~ \mathrm { ~ m ~ }$ , different environments).

## VI. CONCLUSION

In this paper, we investigated the disconnectivity and handoff aware path planning problem for the cargo-UAV, aiming to minimize both its energy consumption and handoff rate. The formulated complex problem is solved using a dynamic programming approach, which achieves optimal flying trajectories. Through simulations, we establish the relationship between cellular disconnectivity and handoff rate for aerial communications. Indeed, a more stringent disconnectivity requirement increases both the handoff rate and the energy consumption due to longer trajectories. Also, the impact study of different parameters provides the following guidelines: 1) Given a high tolerable disconnectivity rate, it is preferable to fly at the lowest permissible altitude in the most direct path to reduce energy consumption, 2) to operate partially or fully independently from the disconnectivity rate, it is encouraged to use a high-sensitive receiver at the cargo-UAV (which corresponds to a low $\beta _ { \mathrm { t h } } ) .$ , however a high handoff rate is expected, and 3) for energy-efficient operation, it is recommended to operate in low-density areas, e.g., RMa, or to redesign the frequency strategy in high-density areas, e.g.,

UMi, in order to reduce inter-cell interference.

## REFERENCES

[1] [Online]. Available: https://www.amazon.com/Amazon-Prime-Air

[2] N. Cherif, W. Jaafar, H. Yanikomeroglu, and A. Yongacoglu, “3D aerial highway: The key enabler of the retail industry transformation,” 2020. [Online]. Available: https://arxiv.org/pdf/2009.09477.pdf

[3] A. Fotouhi, H. Qiang, M. Ding, M. Hassan, L. G. Giordano, A. Garcia-Rodriguez, and J. Yuan, “Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3417–3442, Firstquarter 2019.

[4] M. Ozger, M. Vondra, and C. Cavdar, “Towards beyond visual line of sight piloting of UAVs with ultra reliable low latency communication,” in Proc. IEEE Glob. Commun. Conf. (Globecom), Abu Dhabi, UAE, Dec. 2018, pp. 1–6.

[5] S. Li, Y. Gu, B. Subedi, C. He, Y. Wan, A. Miyaji, and T. Higashino, “Beyond visual line of sight UAV control for remote monitoring using directional antennas,” in Proc. IEEE Glob. Commun. Conf. (Globecom) Workshops, Waikoloa, HI, USA, Dec. 2019, pp. 1–6.

[6] R. M. de Amorim, J. Wigard, I. Z. Kovacs, T. B. Sorensen, and P. E. Mogensen, “Enabling cellular communication for aerial vehicles: Providing reliability for future applications,” IEEE Veh. Technol. Mag., vol. 15, no. 2, pp. 129–135, Jun. 2020.

[7] N. Cherif, M. Alzenad, H. Yanikomeroglu, and A. Yongacoglu, “Downlink coverage and rate analysis of an aerial user in vertical heterogeneous networks (VHetNets),” IEEE Trans. Wireless Commun., (Early Access).

[8] A. Fakhreddine, C. Bettstetter, S. Hayat, R. Muzaffar, and D. Emini, “Handover challenges for cellular-connected drones,” in Proc. ACM Workshop Micro Aerial Veh. Net., Sys., Applications, Seoul, South Korea, Jun. 2019, pp. 9–14.

[9] E. Bulut and I. Guevenc, “Trajectory optimization for cellular-connected UAVs with disconnectivity constraint,” in Proc. IEEE Int. Conf. Commun. (ICC) Workshops, Kansas City, MO, USA, May 2018, pp. 1–6.

[10] M. M. U. Chowdhury, S. J. Maeng, E. Bulut, and I. Guvenc¸, “3D¨ trajectory optimization in UAV-assisted cellular networks considering antenna radiation pattern and backhaul constraint,” IEEE Trans. Aerosp. Electron. Syst., Mar. 2020.

[11] U. Challita, W. Saad, and C. Bettstetter, “Deep reinforcement learning for interference-aware path planning of cellular-connected UAVs,” in Proc. IEEE Int. Conf. Commun. (ICC), Kansas City, MO, USA, May 2018, pp. 1–7.

[12] Y. Zeng and X. Xu, “Path design for cellular-connected UAV with reinforcement learning,” in Proc. IEEE Glob. Commun. Conf. (Globecom), Waikoloa, HI, USA, Dec. 2019, pp. 1–6.

[13] S. Zhang and R. Zhang, “Radio map based path planning for cellularconnected UAV,” in Proc. IEEE Glob. Commun. Conf. (Globecom), Waikoloa, HI, USA, Dec. 2019, pp. 1–6.

[14] M. M. Azari, A. H. Arani, and F. Rosas, “Mobile cellular-connected UAVs: Reinforcement learning for sky limits,” 2020. [Online]. Available: https://arxiv.org/pdf/2009.09815.pdf

[15] 3GPP, “Study on enhanced LTE support for aerial vehicles (release 15), TR 36.777,” Jun. 2018.

[16] ——, “Evolved universal terrestrial radio access (E-UTRA); further advancements for E-UTRA physical layer aspects (relase 9), TR 36.814,” Mar. 2010.

[17] X. Xu and Y. Zeng, “Cellular-connected UAV: Performance analysis with 3D antenna modelling,” in Proc. IEEE Int. Conf. Commun. (ICC) Workshops, Shanghai, China, May 2019, pp. 1–6.

[18] W. Jaafar and H. Yanikomeroglu, “Dynamics of laser-charged UAVs: A battery perspective,” ArXiv, 2020. [Online]. Available: https://arxiv.org/abs/2008.13316

[19] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Mar. 2019.

[20] J. K. Lenstra and A. H. G. R. Kan, “Complexity of vehicle routing and scheduling problems,” Networks, vol. 11, no. 2, pp. 221–227, 1981.