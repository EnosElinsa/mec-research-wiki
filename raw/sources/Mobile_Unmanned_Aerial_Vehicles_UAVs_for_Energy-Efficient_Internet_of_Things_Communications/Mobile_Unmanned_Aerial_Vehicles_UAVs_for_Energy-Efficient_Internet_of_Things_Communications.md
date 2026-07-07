# Mobile Unmanned Aerial Vehicles (UAVs) for Energy-Efficient Internet of Things Communications

Mohammad Mozaffari, Student Member, IEEE, Walid Saad, Senior Member, IEEE, Mehdi Bennis, Senior Member, IEEE, and Mérouane Debbah, Fellow, IEEE

Abstract— In this paper, the efficient deployment and mobility of multiple unmanned aerial vehicles (UAVs), used as aerial base stations to collect data from ground Internet of Things (IoT) devices, are investigated. In particular, to enable reliable uplink communications for the IoT devices with a minimum total transmit power, a novel framework is proposed for jointly optimizing the 3D placement and the mobility of the UAVs, device-UAV association, and uplink power control. First, given the locations of active IoT devices at each time instant, the optimal UAVs’ locations and associations are determined. Next, to dynamically serve the IoT devices in a time-varying network, the optimal mobility patterns of the UAVs are analyzed. To this end, based on the activation process of the IoT devices, the time instances at which the UAVs must update their locations are derived. Moreover, the optimal 3D trajectory of each UAV is obtained in a way that the total energy used for the mobility of the UAVs is minimized while serving the IoT devices. Simulation results show that, using the proposed approach, the total-transmit power of the IoT devices is reduced by 45% compared with a case, in which stationary aerial base stations are deployed. In addition, the proposed approach can yield a maximum of 28% enhanced system reliability compared with the stationary case. The results also reveal an inherent tradeoff between the number of update times, the mobility of the UAVs, and the transmit power of the IoT devices. In essence, a higher number of updates can lead to lower transmit powers for the IoT devices at the cost of an increased mobility for the UAVs.

Index Terms— UAV, Internet of Things, optimization, energy efficiency, uplink, reliability.

Manuscript received August 5, 2016; revised March 15, 2017 and August 17, 2017; accepted September 4, 2017. Date of publication September 15, 2017; date of current version November 9, 2017. This work was supported in part by the U.S. National Science Foundation under Grants AST-1506297, OAC-1541105, and IIS-1633363, in part by the U.S. Office of Naval Research (ONR) under Grant N00014-15-1-2709, and in part by the ERC Starting Grant MORE (Advanced Mathematical Tools for Complex Network Engineering), and in part by the Academy of Finland (CARMA). The associate editor coordinating the review of this paper and approving it for publication was S. Chong. (Corresponding author: Mohammad Mozaffari.)

M. Mozaffari and W. Saad are with the Wireless@VT, Electrical and Computer Engineering Department, Virginia Tech, VA 24061 USA (e-mail: mmozaff@vt.edu; walids@vt.edu).

M. Bennis is with the Centre for Wireless Communications, 90014 Oulu, Finland, and also with the Department of Computer Engineering, Kyung Hee University, Seoul 02447, South Korea (e-mail: bennis@ee.oulu.fi).

M. Debbah is with the Mathematical and Algorithmic Sciences Laboratory, Huawei France Research and Development, 92100 Paris, France, and also with the CentraleSupelec, Université Paris-Saclay, 91192 Gif-sur-Yvette, France, (e-mail: merouane.debbah@huawei.com).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TWC.2017.2751045

# I. INTRODUCTION

THE use of unmanned aerial vehicles (UAVs) as flyingwireless communication platforms has received signifi- wireless communication platforms has received significant attention recently [1]–[8]. On the one hand, UAVs can be used as wireless relays for improving connectivity and coverage of ground wireless devices. On the other hand, UAVs can act as mobile aerial base stations to provide reliable downlink and uplink communications for ground users and boost the capacity of wireless networks [1], [3], [6]–[10]. Compared to the terrestrial base stations, the advantage of using UAV-based aerial base stations is their ability to provide on-the-fly communications. Furthermore, the high altitude of UAVs enables them to effectively establish line-of-sight (LoS) communication links thus mitigating signal blockage and shadowing. Due to their adjustable altitude and mobility, UAVs can move towards potential ground users and establish reliable connections with a low transmit power. Hence, they can provide a cost-effective and energy-efficient solution to collect data from ground mobile users that are spread over a geographical area with limited terrestrial infrastructure.

Indeed, UAVs can play a key role in the Internet of Things (IoT) which is typically composed of small, batterylimited devices such as sensors, and health monitors [11]. These devices are typically unable to transmit over a long distance due to their energy constraints [11]. In such IoT scenarios, UAVs can dynamically move towards IoT devices, collect the IoT data, and transmit it to other devices which are out of the communication ranges of the transmitters [11]. In this case, the UAVs play the role of moving aggregators or base stations for IoT networks [5]. Nevertheless, to effectively use UAVs for the IoT, several technical challenges must be addressed such as optimal deployment, mobility and energy-efficient use of UAVs as outlined in [3] and [6].

In [2], the authors investigated the optimal trajectory of UAVs equipped with multiple antennas for maximizing sumrate in uplink communications. The work in [4] studied the optimization of the throughput of a relay-based UAV system by jointly controlling the UAV’s trajectory as well as the source/relay transmit power. However, these works considered a single UAV in their models. In [3], we investigated the optimal deployment and movement of a single UAV for supporting downlink wireless communications. The work in [12] proposed a low-complexity algorithm for the optimal deployment of multiple UAVs that provide coverage for ground users. The work in [10] provided a comprehensive downlink coverage analysis for a network in which a finite number of UAVs serve the ground users. In [13], the authors used UAVs to efficiently collect data and recharge the clusters’ head in a wireless sensor network which is partitioned into multiple clusters. However, this work is limited to a static sensor network, and does not investigate the optimal deployment of the UAVs. While the energy efficiency of uplink data transmission in a machine-tomachine (M2M) communication network was investigated in [14], the presence of UAVs was not considered. In fact, none of the prior studies in [1]–[14], addressed the problem of jointly optimizing the deployment and mobility of UAVs, device association, and uplink power control for enabling reliable and energy-efficient communications for IoT devices. To our best knowledge, this paper is one of the first comprehensive studies on the joint optimal 3D deployment of aerial base stations, device association, and uplink power control in an IoT ecosystem.

The main contribution of this paper is a novel framework for optimized deployment and mobility of multiple UAVs for the purpose of energy-efficient uplink data collection from ground IoT devices. In particular, we consider an IoT network in which the IoT devices can be active at different time instances. To minimize the total transmit power of these IoT devices, given device-specific signal-to-interferenceplus-noise-ratio (SINR) constraints, we propose an efficient approach to jointly find the UAVs’ locations, the association of devices to UAVs, and the optimal uplink transmit power of the devices. Our proposed framework is composed of two key steps. First, given the locations of the IoT devices, we propose a solution for optimizing the deployment and association of the UAVs. In this case, we solve the formulated problem by decomposing it into two subproblems which are solved iteratively. In the first subproblem, given the fixed UAVs’ locations, we find the jointly optimal device-UAV association and the devices’ transmit power. In the second subproblem, given the fixed device association, we determine the joint 3D UAVs’ locations. For this subproblem, we transform the non-convex continuous location optimization problem to a convex form and provide tractable solutions. Next, following our proposed algorithm, the results of solving the second subproblem are used as inputs to the first subproblem for the next iteration. Here, we show that our proposed approach leads to an efficient solution with a reasonable accuracy compared to the global optimal solution that requires significant overhead. Clearly, the UAVs’ locations and the device association that we obtain in this first step will depend on the locations of active IoT devices.

In the second step, we analyze the IoT network over a time period during which the set of active devices changes. In this case, we present a framework for optimizing the UAVs’ mobility by allowing them to dynamically update their locations depending on the time-varying devices’ activation process. First, we derive the closed-form expressions for the time instances (update times) at which the UAVs must move according to the activation process of the devices. Next, we derive the optimal 3D UAVs’ trajectory such that the total energy consumption of the UAVs while updating their locations is minimized. Our simulation results show that, using the proposed approach, the total transmit power of the IoT devices can be significantly reduced compared to a case in which stationary aerial base stations are deployed. The results also verify our analytical derivations for the update times and reveal an inherent tradeoff between the number of updates, the mobility of the UAVs, and transmit power of the IoT devices. In particular, it is shown that a higher number of updates leads to lower transmit powers for the IoT devices at the cost of higher UAVs’ energy consumptions.

![](images/2ce816396326ee9aa8f00974b23f41ab77bfadec3155c8b54b8b302367bda955.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["IoT device"] --> B["Device_i(x_i, y_i)"]
    B --> C["Control center"]
    D["Robot with car and laptop"] --> E["Device"]
    F["UAV_j(x_j^uav, y_j^uav, h_j)"] --> G["Device"]
    H["Robot with drone"] --> I["Device"]
    J["Robot with car"] --> K["Device"]
    L["Robot with drone"] --> M["Device"]
    N["Robot with drone"] --> O["Device"]
    P["Robot with drone"] --> Q["Device"]
    R["Robot with drone"] --> S["Device"]
    T["Robot with drone"] --> U["Device"]
    V["Robot with drone"] --> W["Device"]
    X["Robot with drone"] --> Y["Device"]
    Z["Robot with drone"] --> AA["Device"]
    AB["Robot with drone"] --> AC["Device"]
    AD["Robot with drone"] --> AE["Device"]
    AF["Robot with drone"] --> AG["Device"]
    AH["Robot with drone"] --> AI["Device"]
    AJ["Robot with drone"] --> AK["Device"]
    AL["Robot with drone"] --> AM["Device"]
    AN["Robot with drone"] --> AO["Device"]
    AP["Robot with drone"] --> AQ["Device"]
    AR["Robot with drone"] --> AS["Device"]
    AT["Robot with drone"] --> AU["Device"]
    AV["Robot with drone"] --> AW["Device"]
    AX["Robot with drone"] --> AY["Device"]
    AZ["Robot with drone"] --> BA["Device"]
    BB["Robot with drone"] --> BC["Device"]
    BD["Robot with drone"] --> BE["Device"]
    BF["Robot with drone"] --> BG["Device"]
    BH["Robot with drone"] --> BI["Device"]
    BJ["Robot with drone"] --> BK["Device"]
    BL["Robot with drone"] --> BM["Device"]
    BN["Robot with drone"] --> BO["Device"]
    BP["Robot with drone"] --> BQ["Device"]
    BR["Robot with drone"] --> BS["Device"]
    BT["Robot with drone"] --> BU["Device"]
    BV["Robot with drone"] --> BW["Device"]
    BX["Robot with drone"] --> BY["Device"]
    BZ["Robot with drone"] --> BY["Device"]
    ZB["Robot with drone"] --> ZB
    AA --> BB
    AB --> BC
    AC --> BF
    AD --> BG
    AE --> BH
    AF --> BI
    AG --> BJ
    AH --> BK
    AI --> BA
    AJ --> BB
    AK --> BC
    AL --> BF
    AM --> BG
    AN --> BH
    AO --> BI
    AP --> BJ
    AQ --> BK
    AR --> BA
    AS --> BB
    AT --> BC
    AU --> BF
    AV --> BG
    AW --> BX
    AX --> BY
    AZ --> BA
    BA --> BB
    BB --> BC
    BC --> BF
    BF --> BG
    BG --> BH
    BH --> BI
    BI --> BJ
    BJ --> BK
    BK --> BA
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style AC fill:#cfc,stroke:#333
    style AD fill:#fcc,stroke:#333
    style AE fill:#cff,stroke:#333
    style AF fill:#ffc,stroke:#333
    style AG fill:#fcc,stroke:#333
    style AH fill:#fcc,stroke:#333
    style AI fill:#fcc,stroke:#333
    style AJ fill:#fcc,stroke:#333
    style AK fill:#fcc,stroke:#333
    style AL fill:#fcc,stroke:#333
    style AM fill:#fcc,stroke:#333
    style AN fill:#fcc,stroke:#333
    style AO fill:#fcc,stroke:#333
    style AP fill:#fcc,stroke:#333
    style AQ fill:#fcc,stroke:#333
    style AR fill:#fcc,stroke:#333
    style AS fill:#fcc,stroke:#333
    style AT fill:#fcc,stroke:#333
    style AU fill:#fcc,stroke:#333
    style AV fill:#fcc,stroke:#333
    style AW fill:#fcc,stroke:#333
```
</details>

Fig. 1. System model.

The rest of this paper is organized as follows. In Section II, we present the system model and problem formulation. Section III presents the optimal deployment of UAVs and device association. In Section IV, we address the mobility and update time of the UAVs. In Section V we provide the simulation and analytical results, and Section VI draws some conclusions.

# II. SYSTEM MODEL AND PROBLEM FORMULATION

Consider an IoT system consisting of a set $\begin{array} { r l } { \mathcal { L } } & { { } = } \end{array}$ $\{ 1 , 2 , \ldots , L \}$ of L IoT devices. Examples of such devices include various types of sensors used for environmental monitoring, smart traffic control, and smart parking devices. In this system, a set $\mathcal { K } = \{ 1 , 2 , \ldots , K \}$ of K rotary wing UAVs must be deployed to collect data from the ground IoT devices. These UAVs can dynamically move, when needed, to effectively serve the IoT devices using uplink communication links. Here, the term served by a UAV implies that the uplink SINR is above the threshold and, thus, the UAV can successfully collect data from the ground IoT device. In our model, we assume that the devices transmit their data to the UAVs in the uplink using frequency division multiple access (FDMA) over R orthogonal channels. We consider $E _ { \mathrm { m a x } }$ to represent the maximum energy that each UAV can spend on its movement. The locations of device $i \in \mathcal { L }$ and $\mathrm { U A V } ~ j ~ \in ~ \mathcal { K }$ are, respectively, given by (xi , yi ) and ${ \pmb v } _ { j } ~ = ~ ( x _ { j } ^ { \mathrm { u a v } } , y _ { j } ^ { \mathrm { u a v } } , h _ { j } )$ as shown in Fig. 1. In our model, we consider a centralized network in which the locations of the devices and UAVs are known to a control center located at a central cloud server. The cloud server will determine the UAVs’ locations, the device-UAV association, and the transmit power of each IoT device.

We analyze the IoT network within a time interval [0, T ] during which the IoT devices can be active at different time instances and must be served by the UAVs at some pre-defined time slots. At the beginning of each slot, the positions of the UAVs as well as the device-UAV association are updated based on the locations of currently active devices that are assumed to be known to the cloud center.1 Hereinafter, the time instance at which the UAVs’ locations and associations are jointly updated, is referred to as the update time. The update times are denoted by $t _ { n } , 1 \le n \le N$ , with N being the number of updates. At each update time $t _ { n } .$ , based on the location of active devices, the optimal UAVs’ locations and the corresponding association must be determined for effectively serving the ground devices. Here, the IoT devices that become active during $[ t _ { n - 1 } , t _ { n } )$ are served by the UAVs during the time period $[ t _ { n } , t _ { n + 1 } )$ . Note that, during $[ t _ { n - 1 } , t _ { n } )$ , the UAVs’ locations and their device association do not change until the next update time, $t _ { n } .$ . Clearly, since at different update times, a different subset of devices might be active, the locations of the UAVs must dynamically change at each update time. Therefore, each UAV’s trajectory will consist of N stop locations at which the UAV serves the ground devices. Note that, in our model, the UAVs’ locations are not necessarily updated once the set of active devices changes. Instead, we consider some specific time instances (update times) at which the UAVs locations device associations, and devices’ transmit power are optimized. In particular, considering the fact that the set of active devices may continuously change, continuously updating the UAVs’ locations, the devices transmit powers, and the device-UAV associations may not be feasible as it can lead to low reliability, high UAVs’ energy consumption, and a need to solve complex real-time optimization processes. In our model, the update times are design parameters that depend on the activation of the devices, and the energy of UAVs. Given this model, our objective is to find the optimal joint UAVs’ locations and device association at each update time $t _ { n }$ so as to minimize the total transmit power of the active devices while meeting each device’s SINR requirement. Moreover, we need to develop a framework for determining the update times as well as the UAVs’ mobility to handle dynamic changes in the activation of the devices. To this end, first, we present the ground-to-air channel model and the activation models for the IoT devices.

# A. Ground-to-Air Path Loss Model

In our model, while optimizing the locations of the UAVs, the information available includes the ground devices’ locations, and the type of environment (e.g. rural, suburban, urban, highrise urban, etc.). Note that, in such practical scenarios, one may not have any additional information about the exact locations, heights, and number of the obstacles. Therefore, one must consider the randomness associated with the LoS and non-line-of-sight (NLoS) links while designing the UAV-based communication system. Therefore, for ground-toair communications, each device will typically have a LoS view towards a specific UAV with a given probability. This LoS probability depends on the environment, location of the

device and the UAV as well as the elevation angle [8]. One suitable expression for the LoS probability is given by [3], [6], [8]:

$$
P _ {\mathrm{LoS}} ^ {i j} = \frac {1}{1 + \psi \exp (- \beta [ \theta_ {i j} - \psi ])}, \tag {1}
$$

where $\psi$ and $\beta$ are constant values which depend on the carrier frequency and type of environment such as rural, urban, or dense urban, and $\theta _ { i j }$ is the elevation angle. Clearly, $\begin{array} { r l r } { \theta } & { { } = } & { \frac { 1 8 0 } { \pi } \ \times \ \sin ^ { - 1 } \left( \frac { \dot { h _ { j } } } { { d _ { i j } } } \right) } \end{array}$ , where $\begin{array} { r l } { d _ { i j } } & { { } = } \end{array}$ $\sqrt { ( x _ { i } - x _ { j } ^ { \mathrm { u a v } } ) ^ { 2 } + ( y _ { i } - y _ { j } ^ { \mathrm { u a v } } ) ^ { 2 } + h _ { j } ^ { 2 } }$ is the distance between device i and UAV j.

From (1), we can see that by increasing the elevation angle or increasing the UAV altitude, the LoS probability increases. The path loss model for LoS and NLoS links between device i and UAV j is given by [6] and [8]:

$$
L _ {i j} = \left\{ \begin{array}{l l} \eta_ {1} \left(\frac {4 \pi f _ {c} d _ {i j}}{c}\right) ^ {\alpha}, & \text {   LoS   link,   } \\ \eta_ {2} \left(\frac {4 \pi f _ {c} d _ {i j}}{c}\right) ^ {\alpha}, & \text {   NLoS   link,   } \end{array} \right. \tag {2}
$$

where $f _ { c }$ is the carrier frequency, α is the path loss exponent, $\eta _ { 1 }$ and η2 $( \eta _ { 2 } > \eta _ { 1 } > 1 )$ are the excessive path loss coefficients in LoS and NLoS cases, an light. Note that, the NLoS probability is Typically, given only the locations of the $P _ { \mathrm { N L o S } } ^ { i j } = 1 \stackrel { \sim } { - } P _ { \mathrm { L o S } } ^ { i j } .$ it is not possible to exactly determine which path loss type (LoS/NLoS) is experienced by the device-UAV link. In this case, the path loss average considering both LoS and NLoS links can be used for the device-UAV communications [6] and [8]. Now, using (1) and (2), the average path loss between device i and UAV j can be expressed as:

$$
\begin{array}{l} \bar {L} _ {i j} = P _ {\mathrm{LoS}} ^ {i j} \eta_ {1} \left(\frac {4 \pi f _ {c} d _ {i j}}{c}\right) ^ {\alpha} + P _ {\mathrm{NLoS}} ^ {i j} \eta_ {2} \left(\frac {4 \pi f _ {c} d _ {i j}}{c}\right) ^ {\alpha} \\ = \left[ P _ {\mathrm{LoS}} ^ {i j} \eta_ {1} + P _ {\mathrm{NLoS}} ^ {i j} \eta_ {2} \right] \left(K _ {o} d _ {i j}\right) ^ {\alpha}, \tag {3} \\ \end{array}
$$

where the U $\begin{array} { r } { K _ { o } = \frac { 4 \pi f _ { c } } { c } } \end{array}$ 4π fc . Clearly, the average channel gain between device is $\begin{array} { r } { \bar { g } _ { i j } \ = \ \frac { 1 } { \bar { L } _ { i j } } } \end{array}$ Note that, by using the average channel gain, there is no need to account for LoS and NLoS links separately, and, hence, the SINR expressions become more tractable. Therefore, we use the average channel gain to model the interference and desired links for all device-UAV communications while computing the SINR.

# B. IoT Device Activation Model

Indeed, the activation of IoT devices depends on the services that they are supporting. For instance, in some applications such as weather monitoring, smart grids, and home automation, the IoT devices need to report their data periodically. However, the IoT devices can have random activations in health monitoring, or smart traffic control applications. Therefore, the UAVs must be properly deployed to collect the IoT data while dynamically adapting to the activation patterns of IoT devices. Naturally, the optimal locations of the UAVs and their update times depend on the activation process of the

IoT devices. Here, we consider two activation models. In the first model, the IoT devices are randomly activated, as in smart traffic control applications. In this case, the concurrent transmissions of a massive number of devices within a short time duration can lead to a bursty traffic as pointed out in [15] and [16]. In fact, when massive IoT devices attempt to transmit within a short time period, the arrival patterns become more bursty [17]. Thus, the 3rd generation partnership project (3GPP) suggests a beta distribution to capture this traffic characteristic of IoT devices [18]. In this model, each IoT device will be active at time t ∈ [0, T ] following the beta distribution with parameters κ and ω [16]–[18]:

$$
f (t) = \frac {t ^ {\kappa - 1} (T - t) ^ {\omega - 1}}{T ^ {\kappa + \omega - 1} B (\kappa , \omega)}, \tag {4}
$$

where [0, T ] is the time interval within which the IoT devices can be active, and $\begin{array} { r } { B ( \kappa , \omega ) = \int _ { 0 } ^ { 1 } t ^ { \kappa - 1 } ( 1 - t ) ^ { \omega - 1 } \mathrm { d } t } \end{array}$ is the beta function with parameters κ and ω [19].

In addition, IoT devices such as smart meters typically report their data periodically rather than randomly. For such devices, the activation process is deterministic and assumed to be known in advance. In such case, we assume that device i becomes active each $\tau _ { i }$ seconds during [0, T ] time duration. Clearly, the number of activations for a device i during [0, T ] is $\left\lfloor \frac { T } { \tau _ { i } } \right\rfloor$ .

# C. Channel Assignment Strategy

Here, given only the devices’ locations, a practical channel assignment approach will be to assign different channels to devices which are located in proximity of each other. This approach significantly mitigates the possibility of having strong interference between two closely located devices. For the channel assignment problem, we have adopted a constrained K-mean clustering strategy [20], which is an efficient distance-based clustering approach in which a set of given points are grouped into K clusters based on their proximity. In this case, given the number of active devices, $L _ { n } ,$ and the number of orthogonal channels, $R \leq L _ { n }$ , we group the devices based on proximity, and assign different channels to devices that are in the same group.

Now, we present our optimization problem to find the UAVs’ locations, device association, and transmit power of IoT devices at each update time $t _ { n }$ during [0, T ]:

(OP):

$$
\min _ {\boldsymbol {v} _ {j}, \boldsymbol {c}, \boldsymbol {P}} \sum_ {i = 1} ^ {L _ {n}} P _ {i}, \quad \forall i \in \mathcal {L} _ {n}, \forall j \in \mathcal {K}, \tag {5}
$$

$$
\text { s.t. } \frac {P _ {i} \bar {g} _ {i c _ {i}} (\boldsymbol {v} _ {c _ {i}})}{\sum_ {k \in \mathcal {Z} _ {i}} P _ {k} \bar {g} _ {k c _ {i}} (\boldsymbol {v} _ {c _ {i}}) + \sigma^ {2}} \geq \gamma , \tag {6}
$$

$$
0 <   P _ {i} \leq P _ {\max}, \tag {7}
$$

where $L _ { n }$ is the total number of active devices at update time $t _ { n } ,$ , and $\mathcal { L } _ { n }$ is the set of devices’ index. P is the transmit power vector with each element $P _ { i }$ being the transmit power of device $i \in \mathcal { L } _ { n }$ . Also, $v _ { j }$ is the 3D location of UAV j , and c is the device association vector with each element $c _ { i }$ being

![](images/782a031c490c99040c7004cdfce163270af1a379d4ae9dde70145cb0c21b91a2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Solving (OP) to find v_j,c,P at each t_n"] --> B["L_n > R"]
    A --> C["L_n ≤ R"]
    B --> D["Interference scenario"]
    C --> E["Interference-free scenario"]
    D --> F["Solving (P1-a) to find c,P"]
    E --> G["Solving (P1-b) to find A_ij"]
    F --> H["Solving (P2-a) to find v_j,P"]
    G --> I["Solving (P2-b) to find v_j"]
    H --> J["Output v_j,c,P"]
    I --> K["Output v_j,A_ij"]
    style A fill:#f9f,stroke:#333
    style K fill:#bbf,stroke:#333
```
</details>

Fig. 2. Block diagram for the proposed solution.

the index of the UAV that is assigned to device i. $P _ { \mathrm { m a x } }$ is the maximum transmit power of each IoT device, and $\sigma ^ { 2 }$ is the noise power. Furthermore, $\bar { g } _ { i c _ { i } } ( \pmb { v } _ { c _ { i } } )$ is the average channel gain between device i and UAV $c _ { i }$ which is a function of the UAV’s location. Also, $\bar { g } _ { k c _ { i } } ( \pmb { v } _ { c _ { i } } )$ is the average channel gain between interfering device k and UAV $c _ { i }$ . In (6), $z _ { i }$ is the set of all other devices that use the same channel as device i and create interference. γ is the SINR target which must be achieved by all the devices, (6) represents the SINR requirement, and (7) shows the maximum transmit power constraint. Hereinafter, we call (OP) the original problem.

Note that, in (5), the transmit power of the IoT devices, the 3D locations of the UAVs, and the UAV-device associations are unknowns. Clearly, the locations of the UAVs impact the channel gain between the devices and UAVs and, hence, they affect the transmit power of each device, $P _ { i }$ . Furthermore, given (6), due to the mutual interference between the devices, the transmit power of each device depends also on the transmit power of the interfering devices as well as the device-UAV associations. In addition, the device-UAV associations depend on the UAVs’ locations which are also unknowns. Therefore, there is a mutual dependence between all the optimization variables in (OP). Moreover, considering (1) and constraint (6), we can see that, this optimization problem is highly nonlinear and non-convex. Indeed, solving (5) is significantly challenging due to the mutual dependence of the optimization variables, non-linearity, and non-convexity of the problem. Next, we propose a framework for solving this optimization problem.

In essence, our proposed framework for solving (OP) proceeds as follows. At each update time $t _ { n } .$ , given the fixed UAVs’ locations, we find the optimal device-UAV association and the transmit power of the devices. Next, given the fixed UAV association from the previous step, we determine the suboptimal locations of the UAVs and update the transmit power the devices accordingly. This procedure is done iteratively until the 3D UAVs’ locations, device association, and the transmit power of the devices are found. Clearly, at each step, the total transmit power of the devices decreases and, hence, the proposed algorithm converges. Fig. 2 shows a block diagram that summarizes the main steps for solving (OP). Next, we discuss, in detail, each block of the proposed solution in Fig. 2.

# III. UAV DEPLOYMENT AND DEVICE ASSOCIATION WITH POWER CONTROL

In this section, given the locations of active IoT devices, we minimize the total transmit power of the devices by solving (5). Clearly, the UAVs’ locations and the device association are mutually dependent. In particular, to find the device association, the locations of the UAVs must be known. Moreover, the UAVs’ locations cannot be optimized without knowing the device association.

Therefore, we decompose (OP) into two subproblems that will be solved iteratively. In the first subproblem, given the locations of the UAVs, we find the optimal device association and the transmit power of the devices such that the uplink SINR requirements of all active devices are satisfied with a minimum total transmit power. In the second subproblem, given the device association resulting from the first subproblem, we determine the sub-optimal locations of the UAVs for which the total transmit power of the devices is minimized. This is an iterative process in which the results of each subproblem are used in the other subproblem for the next iteration. These computations are performed by the control center until the 3D UAVs’ locations, device association, and transmit power of the devices are obtained.

Note that, given the limited number of available orthogonal channels, the interference between the devices will depend on the number of active devices at each update time. Clearly, there is no interference when the number of active devices at time $t _ { n }$ is less than the number of orthogonal channels, or equivalently $L _ { n } \ \leq \ R$ . Given that, in the interference-free scenario, one can provide a more tractable analysis for the deployment and association steps. Hence, we will investigate the interference and interference-free scenarios, separately.

# A. Device Association and Power Control

Here, given initial locations of the UAVs, we aim to find the optimal device association as well as the transmit power of each IoT device such that the total transmit power used for successful uplink communications is minimized.

1) Interference Scenario: In the presence of uplink interference when $L _ { n } \ > \ R$ , the power minimization problem at update time $t _ { n }$ will be given by:

(P1-a):

$$
\min _ {\boldsymbol {c}, \boldsymbol {P}} \sum_ {i = 1} ^ {L _ {n}} P _ {i}, \quad \forall i \in \mathcal {L} _ {n}, \forall j \in \mathcal {K}, \tag {8}
$$

$$
\text { s.t. } \frac {P _ {i} \bar {g} _ {i c _ {i}}}{\sum_ {k \in \mathbb {Z} _ {i}} P _ {k} \bar {g} _ {k c _ {i}} + \sigma^ {2}} \geq \gamma , \tag {9}
$$

$$
0 <   P _ {i} \leq P _ {\max}. \tag {10}
$$

To solve (P1-a), we need to jointly find the optimal device association and the transmit power of all active devices under the SINR constraints for the given UAVs’ locations. Clearly, given the fixed UAVs’ locations, optimization variables are the device association and the transmit power of the devices. Note that, satisfying the SINR requirement of each device significantly depends on the distance and altitude of its serving UAV. Therefore, the feasibility of the optimization problem in (8) depends on the locations of the UAVs. Next, we derive an upper bound and a lower bound for the altitude of serving UAV j as a function of its distance from device i .

Proposition 1: The lower and upper bounds for the altitude of a UAV j needed to serve a device i (meeting its SINR requirement), are given by:

$$
d _ {i j} \sin \left(\frac {1}{\beta} \ln \left(\frac {\psi Q}{1 - Q}\right) + \psi\right) \leq h _ {j} \leq \left(\frac {P _ {\max}}{\gamma K _ {o} ^ {\alpha} \sigma^ {2} \eta_ {1}}\right) ^ {1 / \alpha}, \tag {11}
$$

where $d _ { i j }$ is the distance between UAV j and device i, and $\begin{array} { r } { Q = \frac { { P _ { \mathrm { m a x } } } } { \gamma d _ { i i } ^ { \alpha } K _ { o } ^ { \alpha } \sigma ^ { 2 } ( \eta _ { 1 } - \eta _ { 2 } ) } - \frac { \eta _ { 2 } } { \eta _ { 1 } - \eta _ { 2 } } } \end{array}$ Pmax .

Proof: Let $I _ { i }$ be the cumulative interference from interfering devices on device i, then:

$$
\mathrm{SINR} _ {i} = \frac {P _ {i} \bar {g} _ {i j}}{I _ {i} + \sigma^ {2}} \geq \gamma ,
$$

$$
d _ {i j} ^ {\alpha} \leq \frac {P _ {i}}{\gamma K _ {o} ^ {\alpha} \left(I _ {i} + \sigma^ {2}\right) \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} P _ {\mathrm{NLoS}} ^ {i j}\right)}
$$

$$
\leq \frac {P _ {\max}}{\gamma K _ {o} ^ {\alpha} \sigma^ {2} \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} (1 - P _ {\mathrm{LoS}} ^ {i j})\right)},
$$

$$
P _ {\mathrm{LoS}} ^ {i j} \geq \frac {P _ {\max}}{\gamma d _ {i j} ^ {a} K _ {o} ^ {a} \sigma^ {2} (\eta_ {1} - \eta_ {2})} - \frac {\eta_ {2}}{\eta_ {1} - \eta_ {2}}. \tag {12}
$$

Now, considering $\begin{array} { r } { Q = \frac { P _ { \mathrm { m a x } } } { \gamma d _ { i j } ^ { \alpha } K _ { o } ^ { \alpha } \sigma ^ { 2 } ( \eta _ { 1 } - \eta _ { 2 } ) } - \frac { \eta _ { 2 } } { \eta _ { 1 } - \eta _ { 2 } } } \end{array}$ γ dαij K αo σ 2(η1−η2) − η2η1−η2 , and using Pmax equation (1) lead to:

$$
\theta_ {i j} \stackrel {(a)} {\geq} \frac {1}{\beta} \ln \left(\frac {\psi Q}{1 - Q}\right) + \psi ,
$$

$$
h _ {j} \geq d _ {i j} \sin \left(\frac {1}{\beta} \ln \left(\frac {\psi Q}{1 - Q}\right) + \psi\right), \tag {13}
$$

where (a) stems from (1). Also, we have:

$$
d _ {i j} ^ {\alpha} \leq \frac {P _ {\max}}{\gamma K _ {o} ^ {\alpha} \sigma^ {2} \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} (1 - P _ {\mathrm{LoS}} ^ {i j})\right)} \stackrel {(b)} {\leq} \frac {P _ {\max}}{\gamma K _ {o} ^ {\alpha} \sigma^ {2} \eta_ {1}}, \tag {14}
$$

where in (b) we consider $P _ { \mathrm { L o S } } = 1$ which is equivalent to $h _ { j } = d _ { i j }$ . Finally,

$$
h _ {j} \leq \left(\frac {P _ {\max}}{\gamma K _ {o} ^ {a} \sigma^ {2} \eta_ {1}}\right) ^ {1 / a}. \tag {15}
$$

Clearly, (13) and (15) prove the proposition.

Proposition 1 provides the necessary conditions for the UAV’s altitude needed in order to be able to serve a given IoT device. From (11), the minimum altitude must increase as the distance increases. In other words, the UAV’s altitude needs to be adjusted based on the distance such that the elevation angle between the device and the UAV exceeds $\begin{array} { r } { \frac { 1 } { \beta } \ln \left( \frac { \psi Q } { 1 - Q } \right) ~ + ~ \psi } \end{array}$ . Furthermore, as expected, the maximum altitude of the UAVs significantly depends on the maximum transmit power of the devices as given in (15).

Now, given the fixed UAVs’ locations, problem (P1-a) corresponds to the problem of joint user association and uplink power control in the terrestrial base station scenario. The algorithm presented in [21] and [22] leads to the global optimal solution to the joint user association and uplink power control under the SINR and maximum transmit power constraints.

As a result, the optimal transmit power of users and the base station association for which the total uplink transmit power is globally minimized, is determined. In problem (P1-a), the IoT devices correspond to the users, and fixed positioned UAVs correspond to the terrestrial base stations. For our case, this algorithm, as given in Algorithm 1, will proceed as follows. We start with an initial value for transmit power of all active devices in step 3. Then, in step 4 we compute $\rho _ { i j } ^ { ( t ) }$ ) at iteration t . In this case, ρ(t )i j $\rho _ { i j } ^ { ( t ) }$ represents the minimum required transmit power of device i to reach an SINR of 1 while connecting to UAV $j ,$ given the fixed transmit power of other devices. In step 5, we find the minimum transmit power of device i if it connects to the best UAV. Then, the index of the best UAV which is assigned to device i is given in step 6. In step 7 we update the transmit power of device i in order to achieve an SINR of $\gamma .$ . Steps 4 to 7 must be repeated for all devices to obtain the optimal transmit power and the device association vectors.

Algorithm 1 Iterative Algorithm for Joint Power Control and Device-UAV Association   
1: Inputs: Locations of UAVs and IoT devices
2: Outputs: Device association vector (c), and transmit power of all devices (P).
3: Set t = 0, and initialize $\boldsymbol{P}^{(0)} = \left(P_{1}^{(0)}, \ldots, P_{K}^{(0)}\right)$ .
4: Define $\rho_{ij}^{(t)} = \frac{\sigma^2 + \sum_{k \in \mathbb{Z}_i} P_k^{(t)} \bar{g}_{kj}}{\bar{g}_{ij}}$ .
5: Compute $S_i(\boldsymbol{P}^{(t)}) = \min_{j \in \mathcal{K}} \rho_{ij}^{(t)}$ .
6: Find $c_i(\boldsymbol{P}^{(t)}) = \arg \min_{j \in \mathcal{K}} \rho_{ij}^{(t)}$ .
7: Update $P_i^{(t+1)} = \min \left\{ \gamma S_i(\boldsymbol{P}^{(t)}), P_{\max} \right\}, \forall i \in \mathcal{L}_n.$ 8: Repeat steps 4 to 7 for all devices until $\boldsymbol{P}^{(t)}$ converges.
9: $\boldsymbol{P} = \boldsymbol{P}^{(t)}, \boldsymbol{c} = [c_i(\boldsymbol{P}^{(t)})], \forall i \in \mathcal{L}_n.$

As shown in [21], after several iterations this algorithm quickly converges to the global optimal solution if the SINR of each device is equal to γ . Hence, by solving (P1-a), we are able to find the optimal transmit power of the devices and the device association for any given fixed locations of the UAVs. Then, the device association and transmit power of the devices will be used as inputs for solving the second subproblem in which the UAVs’ locations need to be optimized (in Subsection III-B).

2) Interference-Free Scenario: At each update time $t _ { n } ,$ if the number of active devices is lower than the number of orthogonal channels or equivalently $L _ { n } \leq R .$ , there will be no interference between the devices. Unlike in the interference scenario, the transmit power of each device can be computed only based on the channel gain between the device and its serving UAV. Therefore, considering (3), and (6) without interference, the minimum transmit power of device i in order to connect to UAV j is $P _ { i } = \gamma \sigma ^ { 2 } \bar { L _ { i j } }$ . In this case, given the locations of the UAVs (fixed for all $\overset { \cdot } { \boldsymbol { v } _ { j } } ) , \ : \bar { \boldsymbol { L } } _ { i j }$ is known for all devices and problem (P1-a) can be simplified. Subsequently, the optimal association problem under minimum power in the interference-free scenario will be:

(P1-b):

$$
\min _ {A _ {i j}} \sum_ {j = 1} ^ {K} \sum_ {i = 1} ^ {L _ {n}} A _ {i j} \bar {L} _ {i j}, \tag {16}
$$

$$
\text { s.t. } \sum_ {j = 1} ^ {K} A _ {i j} = 1, \quad \forall i \in \mathcal {L} _ {n}, \tag {17}
$$

$$
A _ {i j} \bar {L} _ {i j} \leq \frac {P _ {\max}}{\gamma \sigma^ {2}}, \quad A _ {i j} \in \{0, 1 \}, \forall i \in \mathcal {L} _ {n}, j \in \mathcal {K}, \tag {18}
$$

where $\bar { L } _ { i j }$ is the average path loss between device i and UAV j, which is known, give the locations of the UAV and the device. $A _ { i j }$ is equal to 1 if device i is assigned to UAV $j ,$ otherwise $A _ { i j }$ will be equal to 0. Clearly, the optimization problem in (16) is an integer linear programming (ILP). In general, this problem can be solved by using standard ILP solution methods such as the cutting plane. However, these solutions might not be efficient as the size of the problem grows. In particular, due to the potentially high number of IoT devices, a more efficient technique for solving (16) is needed. Here, we transform problem (16) to a standard assignment problem [23] which can be solved in polynomial time. In the assignment problem, the objective is to find the optimal one-to-one assignment between two sets of nodes with a minimum cost. In our problem, the devices and the UAVs can be considered as two sets of nodes that need to be assigned to each other with an assignment cost of $L _ { i j }$ between nodes i and $j .$ However, compared to the classical assignment problem, (P1-b) has an additional constraint in (18) which results from the transmit maximum power constraint. This constraint indicates that device i cannot be assigned to UAV j if $\begin{array} { r } { \bar { L } _ { i j } > \frac { P _ { \mathrm { m a x } } } { \gamma \sigma ^ { 2 } } } \end{array}$ Pmax2 . Therefore, in the assignment problem we can consider $L _ { i j } = + \infty$ to avoid assigning device i to UAV j when $\begin{array} { r } { \bar { L } _ { i j } { \mathrm { ~ \scriptsize ~ > ~ } } \frac { P _ { \mathrm { m a x } } } { \gamma \sigma ^ { 2 } } } \end{array}$ γ σ that implies the constraint in (18) is violated. Subsequently, using the updated assignment costs, $L _ { i j }$ , problem (P1-b) will be transformed to the classical assignment problem which can be solved using the Hungarian method with a time complexity of $O ( ( L _ { n } K ) ^ { 3 } )$ [24]. We note that, in absence of interference, problems (P1-a) and (P1-b) have the same solution. Next, we present the second subproblem of the original optimization problem, given in (5), in order to optimize the UAVs’ locations.

# B. Optimal Locations of the UAVs

In this subsection, given the optimal device association, our goal is to find the sub-optimal locations of the UAVs for which the total transmit power of the devices is minimized. In other words, considering the mobile nature of the UAVs, we intelligently update the location of each UAV based on the location of its associated IoT devices.

1) Interference Scenario: In this scenario, given the UAV-device associations, the optimization problem to find the 3D locations of the UAVs and the transmit power of the devices will be:

(P2-a):

$$
\min _ {\boldsymbol {v} _ {j}, \boldsymbol {P}} \sum_ {i = 1} ^ {L _ {n}} P _ {i}, \quad \forall i \in \mathcal {L} _ {n}, \forall j \in \mathcal {K}, \tag {19}
$$

$$
\text { s.t. } \frac {P _ {i} \bar {g} _ {i j} (\boldsymbol {v} _ {j})}{\sum_ {k \in \mathcal {Z} _ {i}} P _ {k} \bar {g} _ {k j} (\boldsymbol {v} _ {j}) + \sigma^ {2}} \geq \gamma , \tag {20}
$$

$$
0 <   P _ {i} \leq P _ {\max}, \tag {21}
$$

where ${ \pmb v } _ { j } ~ = ~ ( x _ { j } ^ { \mathrm { u a v } } , y _ { j } ^ { \mathrm { u a v } } , h _ { j } )$ indicates the 3D location of UAV j. Clearly, the channel gains used in (20) depend on the locations of the UAVs. Note that, according to (1) and (3), $\bar { g } _ { i j } ( \pmb { v } _ { j } )$ is a non-convex function of $v _ { j }$ . Consequently, constraint (20) is also non-linear and non-convex. Furthermore, the transmit power of the devices and the UAVs’ locations are mutually dependent. On the one hand, the location of each UAV must be determined such that its associated devices can connect to it with a minimum transmit power. On the other hand, the UAV’s location will impact the amount of interference received from other interfering devices. Indeed, solving the optimization problem in (P2-a) is challenging as the problem is highly non-linear and non-convex. In particular, the complexity of this problem stems from the mutual dependence between the transmit power of the devices and the locations of the UAVs.

Our proposed approach to solve (P2-a) is based on optimizing the location of each UAV separately. Note that, using the results of (P1-a), for each UAV, the associated and nonassociated devices, and their transmit power, $P _ { i } ^ { * }$ , are known. Our proposed solution proceeds as follows. The cloud starts by considering a single UAV and then optimizing its location given the fixed transmit power for the non-associated devices. Then, the cloud updates the transmit power of the associated devices according to the new location of their serving UAV. Hence, at each step, the location of a UAV and the transmit power of its associated devices are updated. At each iteration, after finding $P _ { i } ^ { * }$ , we set $P _ { \mathrm { m a x } } = P _ { i } ^ { * }$ for the next iteration. This ensures that the transmit power of the devices does not increase during the iterative process. The entire process is repeated by the cloud for all UAVs one-by-one, until the transmit power of the devices cannot be further reduced by changing the UAVs’ locations. Note that, at each step, one must determine the optimal location of each UAV such that the total transmit power of its associated devices is minimized.

Now, let $C _ { j }$ be the set of devices’ index associated to UAV j . Given (3), (19), and (20), the optimal location of UAV j can be determined by solving the following problem:

$$
\min _ {\boldsymbol {v} _ {j}} \sum_ {i \in C _ {j}} F _ {i} (\boldsymbol {v} _ {j}), \tag {22}
$$

$$
\begin{array}{l} \text { s.t. } F _ {i} (\boldsymbol {v} _ {j}) = \gamma \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} P _ {\mathrm{NLoS}} ^ {i j}\right) \left(K _ {o} d _ {i j}\right) ^ {\alpha} \\ \times \left[ \sum_ {k \in Z _ {i}} \frac {P _ {k}}{\left(\eta_ {1} P _ {\mathrm{LoS}} ^ {k j} + \eta_ {2} P _ {\mathrm{NLoS}} ^ {k j}\right) \left(K _ {o} d _ {k j}\right) ^ {\alpha}} + \sigma^ {2} \right], (23) \\ F _ {i} (\boldsymbol {v} _ {j}) \leq P _ {i} ^ {*}, \quad \forall i \in \mathcal {C} _ {j}, (24) \\ \end{array}
$$

Note that, Pi jLoS, PkjLoS, dkj , and di j depend on the locations $P _ { \mathrm { L o S } } ^ { i j } , \ P _ { \mathrm { L o S } } ^ { k j } , \ d _ { k j }$ $d _ { i j }$ of UAVs $( \pmb { v } _ { j } )$ . Also, (24) guarantees that the transmit power of each device will be reduced by updating the location of serving UAV.

Clearly, (22), (23), and (24) are non-linear and non-convex. Considering the fact that the objective function and constraints are twice differentiable, we convert (22) to a quadratic form which can be solved using efficient techniques. In particular, we adopt the sequential quadratic programming (SQP) method as one of the most powerful algorithms for solving large scale and constrained differentiable non-linear optimization problems [25]. Clearly, considering the high non-linearity of (23) as well as the large number of constraints, the SQP is a suitable method for solving our optimization problem. In the SQP method, the objective function is approximated by a quadratic function, and the constraints are linearized. Subsequently, the optimization problem is solved by solving multiple quadratic subproblems. In our optimization problem, to find the optimal location of $\mathrm { U A V } ~ j , ~ \pmb { v } _ { j , k }$ , we start with an initial point $\pmb { v } _ { j , k }$ (starting with $k = 0 )$ . Then, we use the first order necessary optimality or Karush-Kuhn-Tucker (KKT) conditions to find the Lagrangian variables. In particular, we use:

$$
\nabla L (\boldsymbol {v} _ {j, k}, \boldsymbol {\lambda} _ {k}) = \sum_ {i \in C _ {j}} \nabla F _ {i} (\boldsymbol {v} _ {j, k}) + \nabla \boldsymbol {w} _ {i} (\boldsymbol {v} _ {j, k}) \boldsymbol {\lambda} _ {k} = 0, \tag {25}
$$

where $\begin{array} { c c l } { { { \cal L } ( \pmb { v } _ { j , k } , \pmb { \lambda } _ { k } ) } } & { { = } } & { { \displaystyle \sum _ { i \in { \cal C } _ { i } } F _ { i } ( \pmb { v } _ { j , k } ) \ + \ \lambda ^ { T } \pmb { w } ( \pmb { v } _ { j , k } ) } } \end{array}$ is the Lagrangian function, $\lambda _ { k }$ is the vector of Lagrangian variables, and ${ \pmb w } ( { \pmb v } _ { j , k } )$ is a vector of functions with each element being wi $( \pmb { v } _ { j , k } ) \overset {  } { = } ( F _ { i } ( \pmb { v } _ { j , k } ) - P _ { i } ^ { * } )$ . Then, given $\pmb { v } _ { j , k }$ , we determine the Lagrange variables by [25]:

$$
\boldsymbol {\lambda} _ {k} = - \left[ \boldsymbol {w} _ {i} (\boldsymbol {v} _ {j, k}) ^ {T} \nabla \boldsymbol {w} _ {i} (\boldsymbol {v} _ {j, k}) \right] ^ {- 1} \nabla \boldsymbol {w} _ {i} (\boldsymbol {v} _ {j, k}) ^ {T} \sum_ {i \in C _ {j}} \nabla F _ {i} (\boldsymbol {v} _ {j, k}). \tag {26}
$$

In the next step, we update $\pmb { v } _ { j , k + 1 } = \pmb { v } _ { j , k } + \pmb { d } _ { k }$ , where $\pmb { d } _ { k }$ is the solution to the following quadratic programming problem:

$$
\boldsymbol {d} _ {k} = \underset {\boldsymbol {d}} {\arg \min} \sum_ {i \in C _ {j}} \nabla F _ {i} (\boldsymbol {v} _ {j, k}) ^ {T} \boldsymbol {d} + \frac {1}{2} \boldsymbol {d} ^ {T} \nabla^ {2} [ L (\boldsymbol {v} _ {j, k}, \lambda_ {k}) ] \boldsymbol {d}, \tag {27}
$$

$$
\text { s.t. } F _ {i} (\boldsymbol {v} _ {j, k}) + \nabla F _ {i} (\boldsymbol {v} _ {j, k}) ^ {T} \boldsymbol {d} - P _ {i} ^ {*} \leq 0, \quad \forall i \in \mathcal {C} _ {j}, \tag {28}
$$

where, ∇ and $\nabla ^ { 2 }$ indicate the gradient and Hessian operations. Clearly, (27) is an inequality constrained quadratic programming. Moreover, it can be shown that the Hessian matrix, $\nabla ^ { 2 } [ \bar { L } ( \pmb { v } , \pmb { \lambda } _ { k } ) ]$ , is not positive semidefinite and, hence, (27) is non-convex in general. In this case, the two possible solution approaches are the active set, and the interior point methods. Typically, the active set method is preferred when the Hessian matrix is moderate/small and dense. The interior point, however, is a suitable approach when the Hessian matrix is large and sparse [26]. In our problem, due to the potential possible high number of active devices, the number of constraints can be high. Therefore, the Hessian matrix, $\nabla ^ { 2 } \left[ L ( \pmb { v } _ { j , k } , \pmb { \lambda } _ { k } ) \right]$ , is large and sparse, and, hence, the interior point method is used.

Finally, based on (25)-(28), and given the fixed device association, the sub-optimal location of each $\mathrm { U A V } \left( \pmb { v } _ { j } \right)$ will be determined. Next, we address the UAVs’ location optimization in an interference-free scenario.

![](images/2d43a5ff71737a13e454c7c98794bf47f0259073bb3bf43b8396c052c6af4788.jpg)

<details>
<summary>line</summary>

| UAV Altitude (m) | Error (%) |
| ---------------- | --------- |
| 50               | 3.44      |
| 100              | 3.46      |
| 150              | 3.47      |
| 200              | 3.48      |
| 250              | 3.485     |
| 300              | 3.49      |
| 350              | 3.492     |
| 400              | 3.495     |
| 450              | 3.497     |
| 500              | 3.498     |
</details>

Fig. 3. Error in the objective function approximation.

2) Interference-Free Scenario: In the absence of interference, we are able to provide tractable analysis on the UAVs’ locations optimization. Considering $\alpha = 2$ for LoS ground-toair propagation [8], the optimal location of each UAV will be given by:

(P2-b):

$$
\min _ {\boldsymbol {v} _ {j}} \sum_ {i \in C _ {j}} K _ {o} ^ {2} \sigma^ {2} \gamma \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} P _ {\mathrm{NLoS}} ^ {i j}\right) d _ {i j} ^ {2}, \tag {29}
$$

$$
\text { s.t. } \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} P _ {\mathrm{NLoS}} ^ {i j}\right) d _ {i j} ^ {2} \leq \frac {P _ {\max}}{K _ {o} ^ {2} \sigma^ {2} \gamma}, \quad \forall i \in \mathcal {C} _ {j}. \tag {30}
$$

This optimization problem is non-convex over $\begin{array} { r l } { \boldsymbol { v } _ { j } } & { { } = } \end{array}$ $( x _ { j } ^ { \mathrm { u a v } } , y _ { j } ^ { \mathrm { u a v } } , h _ { j } )$ . However, given any altitude $h _ { j } ,$ we can provide a tractable solution to this problem. First, given $h _ { j }$ , we consider the following function that is used in (29):

$$
q (d _ {i j}) = K _ {o} ^ {2} \sigma^ {2} \gamma \left(\eta_ {1} P _ {\mathrm{LoS}} ^ {i j} + \eta_ {2} P _ {\mathrm{NLoS}} ^ {i j}\right) d _ {i j} ^ {2}. \tag {31}
$$

Clearly, considering the fact that $0 \leq P _ { \mathrm { L o S } } ^ { i j } \leq 1$ , and $P _ { \mathrm { N L o S } } ^ { i j } =$ 1 − P i j $1 - P _ { \mathrm { L o S } } ^ { i j }$ LoS , we have:

$$
K _ {o} ^ {2} \sigma^ {2} \gamma \eta_ {1} d _ {i j} ^ {2} \leq q (d _ {i j}) \leq K _ {o} ^ {2} \sigma^ {2} \gamma \eta_ {2} d _ {i j} ^ {2}. \tag {32}
$$

From (32), we can see that $q ( d _ { i j } )$ is bounded between two quadratic functions that each is linearly proportional to $d _ { i j } ^ { 2 }$ . Now, using the least square estimation method, we find the coefficients $\alpha _ { 1 }$ and $\alpha _ { 2 }$ such that, given any $h _ { j }$ , $q ( d _ { i j } )$ is approximated by the following convex quadratic function:

$$
q (d _ {i j}) \approx \alpha_ {1} d _ {i j} ^ {2} + \alpha_ {2}, \tag {33}
$$

where $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are altitude dependent coefficients. Using the quadratic approximation, the solution of (29) becomes more tractable.

Fig. 3 shows the error in the objective function (29) due the quadratic approximation. As we can see from Fig. 3 which is obtained based on the parameters in Table I, the error is less than 4% for different UAVs’ altitudes.

(30), we consider early, D is an increasing $\begin{array} { r l } { D } & { { } = } \end{array}$ $\left( \eta _ { 1 } P _ { \mathrm { L o S } } ^ { i j ^ { \prime } } + \eta _ { 2 } P _ { \mathrm { N L o S } } ^ { i j } \right) d _ { i j } ^ { 2 }$ $d _ { i j }$ $\eta _ { 1 } \mathrm { ~ - ~ } \overset { \prime } { \eta _ { 2 } } \mathrm { ~ < ~ } 0$ probability is a decreasing function of distance. Therefore, using ${ d _ { i j } } ^ { 2 } = ( x _ { i } - x _ { i } ^ { \mathrm { u a v } } ) ^ { 2 } + ( y _ { i } - y _ { i } ^ { \mathrm { u a v } } ) ^ { 2 } + h _ { i } ^ { 2 }$ , and (33), for any given $h _ { j }$ we can write the optimization problem (29)

TABLE I SIMULATION PARAMETERS 

<table><tr><td>Parameter</td><td>Description</td><td>Value</td></tr><tr><td> $P_{\text{max}}$ </td><td>Maximum transmit power of each device</td><td>200 mW</td></tr><tr><td> $\alpha$ </td><td>Path loss exponent for LoS links</td><td>2</td></tr><tr><td> $\sigma^{2}$ </td><td>Noise power</td><td>-130 dBm</td></tr><tr><td> $\gamma$ </td><td>SINR threshold</td><td>5 dB</td></tr><tr><td> $L$ </td><td>Total number of IoT devices</td><td>500</td></tr><tr><td> $\eta_{1}$ </td><td>Additional path loss to free space for LoS</td><td>3 dB</td></tr><tr><td> $\eta_{2}$ </td><td>Additional path loss to free space for NLoS</td><td>23 dB</td></tr></table>

as:

$$
\min _ {x _ {j} ^ {\mathrm{uav}}, y _ {j} ^ {\mathrm{uav}}} \sum_ {i \in C _ {j}} (x _ {j} ^ {\mathrm{uav}} - x _ {i}) ^ {2} + (y _ {j} ^ {\mathrm{uav}} - y _ {i}) ^ {2} + h _ {j} ^ {2}, \tag {34}
$$

$$
\text { s.t. } \left(x _ {j} ^ {\mathrm{uav}} - x _ {i}\right) ^ {2} + \left(y _ {j} ^ {\mathrm{uav}} - y _ {i}\right) ^ {2} + h _ {j} ^ {2} - \epsilon^ {2} \leq 0, \quad \forall i \in \mathcal {C} _ {j}, \tag {35}
$$

where $\varepsilon = \{ d | K _ { o } ^ { 2 } \sigma ^ { 2 } \gamma \ ( \eta _ { 1 } P _ { \mathrm { L o S } } + \eta _ { 2 } P _ { \mathrm { N L o S } } ) d ^ { 2 } = P _ { \mathrm { m a x } } \}$ . Next, we derive the solution to problem (34) that seeks to find the sub-optimal UAVs’ locations.

Theorem 1: The solution to (34) is given by $\begin{array} { r l } { \pmb { S } ^ { * } } & { { } = } \end{array}$ $( x _ { { i } } ^ { \mathrm { u a v } * } , y _ { { i } } ^ { \mathrm { u a v } * } ) = - P ( \lambda ) ^ { - 1 } Q ( \lambda )$ , with the vector λ that maximizes the following concave function:

$$
\max _ {\lambda} \frac {1}{2} Q (\lambda) ^ {T} P (\lambda) ^ {- 1} Q (\lambda) + r (\lambda), \tag {36}
$$

$$
\text { s.t. } \lambda \geq 0, \tag {37}
$$

where $P ( \lambda ) = P _ { o } + \sum _ { i = 1 } ^ { | C _ { j } | } \lambda _ { i } P _ { i } , \mathrm { ~ } Q ( \lambda ) = 2 _ { o } + \sum _ { i = 1 } ^ { | C _ { j } | } \lambda _ { i } Q _ { i }$ and $r ( \lambda ) = r _ { o } + \sum _ { i = 1 } ^ { | C _ { j } | } \lambda _ { i } r _ { i }$ , with $P _ { o } , Q _ { o } , r _ { o } , P _ { i } , Q _ { i }$ , and $r _ { i }$ given in the proof.

Proof: As we can see from (34), the optimization problem is a quadratically constrained quadratic program (QCQP) whose general form is given by [27]:

$$
\min _ {s} \frac {1}{2} s ^ {T} P _ {o} s + Q _ {o} ^ {T} s + r _ {o}, \tag {38}
$$

$$
\text { s.t. } \frac {1}{2} \boldsymbol {s} ^ {T} \boldsymbol {P} _ {i} \boldsymbol {s} + \boldsymbol {Q} _ {i} ^ {T} \boldsymbol {s} + r _ {i}, i \in \mathcal {C} _ {j}. \tag {39}
$$

Given (34) and (35), we have:

$\begin{array} { r c l r c l } { { P _ { o } } } & { { = } } & { { \left[ \begin{array} { c c } { { 2 | C _ { j } | } } & { { 0 } } \\ { { 0 } } & { { 2 | C _ { j } | } } \end{array} \right] , P _ { i } } } & { { = } } & { { \left[ \begin{array} { c c } { { 2 } } & { { 0 } } \\ { { 0 } } & { { 2 } } \end{array} \right] , Q _ { o } } } & { { = } } & { { \begin{array} { c c } { { } } & { { } } \\ { { } } & { { } } \end{array} } } \end{array}$ $\left[ - 2 \sum _ { i = 1 } ^ { \vert C _ { j } \vert } x _ { i } - 2 \sum _ { i = 1 } ^ { \vert C _ { j } \vert } y _ { i } \right] ^ { T } , ~ \pmb { \mathrm { Q } } _ { i } = \left[ - 2 x _ { i } - 2 y _ { i } \right] ^ { T } . ~ \mathrm { A l s o } , ~ r _ { o } =$ T $\sum _ { i = 1 } ^ { \left| \overline { { C } } _ { j } \right| } x _ { i } ^ { 2 } + \sum _ { i = 1 } ^ { \left| C _ { j } \right| } y _ { i } ^ { 2 } ,$  x 2i + , and $r _ { i } ~ = ~ x _ { i } ^ { 2 } + y _ { i } ^ { 2 } + h _ { j } ^ { 2 } - \epsilon ^ { 2 }$ with i=1 i=1 $\dot { \varepsilon } ~ = ~ \{ d | \dot { K _ { o } ^ { 2 } \sigma ^ { 2 } } \gamma ~ ( \eta _ { 1 } P _ { \mathrm { L o S } } + \eta _ { 2 } P _ { \mathrm { N L o S } } ) d ^ { 2 } = P _ { \mathrm { m a x } } \}$ . Note that, $P _ { o }$ and $P _ { i }$ are positive semidefinite matrices and, hence, the QCQP problem in (38) is convex. Now, we write the Lagrange dual function as:

$$
\begin{array}{l} f (\boldsymbol {\lambda}) = \inf _ {s} \left[ \frac {1}{2} \mathbf {s} ^ {T} \boldsymbol {P} _ {o} \mathbf {s} + \boldsymbol {Q} _ {o} ^ {T} \mathbf {s} + r _ {o} \right. \\ \left. + \sum_ {i} \lambda_ {i} \left(\frac {1}{2} \boldsymbol {s} ^ {T} \boldsymbol {P} _ {i} \boldsymbol {s} + \boldsymbol {Q} _ {i} ^ {T} \boldsymbol {s} + r _ {i}\right) \right] \\ = \inf _ {s} \left[ \frac {1}{2} s ^ {T} P (\lambda) s + Q (\lambda) ^ {T} s + r (\lambda) \right]. \tag {40} \\ \end{array}
$$

Clearly, by taking the gradient of the function inside the infimum with respect to s, we find $s ^ { * } = - P ( \lambda ) ^ { - 1 } Q ( \lambda )$ . As a result, using $\begin{array} { r } { s ^ { * } , f ( \lambda ) = \frac { 1 } { 2 } Q ( \lambda ) ^ { T } P ( \lambda ) ^ { - 1 } Q ( \lambda ) + r ( \lambda ) } \end{array}$ . Finally, the dual of problem (38) or (34) will be:

$$
\max f (\lambda), \text {   s.t.   } \lambda \geq 0, \tag {41}
$$

which proves Theorem 1.

Using Theorem 1, for a fixed altitude, we find the optimal 2D coordinates of the UAV, $\begin{array} { r c l } { s ^ { * } } & { = } & { ( x _ { i } ^ { \mathrm { u a v } * } , y _ { i } ^ { \mathrm { u a v } * } ) } \end{array}$ (x uav ∗, yuav ∗). Then, the optimal UAV’s altitude is the argument that minimizes the following one-dimensional function as:

$$
h _ {j} ^ {*} = \underset {h _ {j}} {\arg \min} \left[ \alpha_ {1} \left(h _ {j} ^ {2} + \left\| s ^ {*} \right\| ^ {2}\right) + \alpha_ {2} \right], \tag {42}
$$

where $\alpha _ { 1 }$ and $\alpha _ { 2 }$ are the altitude dependent coefficients given in (33). Given (42), the sub-optimal altitude of the UAV is obtained via one dimensional search over a feasible range of altitudes. Consequently, we can determine the optimal 3D location of each UAV.

To solve the original optimization problem, (OP), the device association (presented in subsection III-A), and UAVs’ locations optimization (in III-B) are applied iteratively until there is no change in the location update step. Clearly, at each iteration, the total transmit power of the devices is reduced and the objective function is monotonically decreasing. Hence, the solution converges after several iterations. Note that, our proposed approach provides a suboptimal solution to the original problem. Nevertheless, our solution has a reasonable accuracy but significantly fast compared to the global optimal solution that can be achieved by the brute-force search, as will be further corroborated in the simulations.

Thus far, we considered the IoT network at one snapshot in the time duration [0, T ]. Next, we analyze the IoT network considering the entire time duration [0, T ] in which the set of active devices changes. In this case, to maintain the powerefficient and reliable uplink communications of the devices, the UAVs must update their locations at different update times $t _ { n }$ .

# IV. UPDATE TIMES AND MOBILITY OF UAVS

Here, we analyze the update times and the optimal trajectory of the UAVs to guarantee the reliable uplink transmissions of the IoT devices. Clearly, the trajectory of the UAVs and their update time depend on the activation process of the IoT devices. Furthermore, to move along the optimal trajectories, the UAVs must spend a minimum total energy on mobility so as to remain operational for a longer time. In the considered ground IoT network, the set of active IoT devices changes over time. Consequently, the UAVs must frequently update their locations accordingly. Note that, the UAVs do not continuously move as they must stop, serve the devices, and then update their locations. Moreover, the mobility of the UAVs is also limited due to their energy constraints. Hence, the UAVs update their locations only at some specific times. In this case, during time interval [0, T ], we need to find update times $t _ { n } , \ 1 \ \leq \ n \ \leq \ N$ with N updates, and a framework for optimizing the mobility of the UAVs at different update times. For tractability, we assume that the devices are synchronized at $t \ = \ 0 .$ . In this case, the synchronization process needs to be done only once during the entire activation period [0, T ]. It should be noted that, our optimization problems for jointly finding the optimal UAVs’ locations, the device association, and devices’ transmit power at each update time do not depend on this synchronization assumption.

# A. Update Time Analysis

First, we propose a framework to find the update times of the UAVs. As discussed in Section II, each UAV’s trajectory consists of multiple stop locations (determined in update times) at which each UAV serves its associated ground devices. Clearly, the update times depend on the activation of the IoT devices during the given time period [0, T ]. The number of update times, N, impacts the optimal location and trajectory of the UAVs as well as the power consumption of the IoT devices. A higher number of updates leads to a shorter time interval between the consecutive updates. Hence, a lower number of devices will be active during the shorter time interval. In such a case, the active devices experience lower interference from each other while transmitting their data to the UAVs. Therefore, the IoT devices can use lower transmit power to meet their SINR constraint. However, a higher number of updates requires more mobility and higher energy consumption for the UAVs. Next, we provide insightful analysis on the update time based on the probabilistic and periodic activation models of the IoT devices.

1) Periodic IoT Activation: In some applications such as weather monitoring, smart grids (e.g. smart meters), and home automation, the IoT devices can report their data periodically. Therefore, the devices are activated periodically. Let $\tau _ { i }$ be the activation period of device i during [0, T ]. Without loss of generality, assume $\tau _ { 1 } \ \leq \ \tau _ { 2 } \ \leq \ . . . \ \leq \ \tau _ { L }$ . Due to the periodic nature of devices’ activation, we can find the exact number of active devices at each update time $t _ { n }$ .

Proposition 2: The exact number of active IoT devices at update time $t _ { n }$ is given by:

$$
b _ {n} = \sum_ {i = 1} ^ {L} \mathbb {1} \left(\left\lfloor \frac {t _ {n} ^ {-}}{\tau_ {i}} \right\rfloor > \left\lfloor \frac {t _ {n - 1}}{\tau_ {i}} \right\rfloor\right), \quad n > 1, \tag {43}
$$

$$
b _ {1} = \underset {i} {\arg \max} \left\{t _ {1} > \tau_ {i} \right\}, \tag {44}
$$

where 1(.) is the indicator function which can only be equal to 1 or 0, and $t _ { n } ^ { - } = \operatorname* { l i m } _ { \varepsilon  0 ^ { + } } ( t _ { n } - \varepsilon )$ .

Proof: User i becomes active during $[ t _ { n - 1 } , t _ { n } )$ if there exists $q \in \mathbb { N }$ such that $t _ { n - 1 } \leq \ q \tau _ { i } < \ t _ { n }$ . Thus, the number of activations of device i before $t _ { n }$ must be greater than the one until $t _ { n - 1 }$ . Considering the fact that the number of activations before $t _ { n }$ is $\begin{array} { r } { \left\lfloor \frac { { t _ { n } } ^ { - } } { \tau _ { i } } \right\rfloor } \end{array}$ and until $\scriptstyle t _ { n - 1 } { \mathrm { ~ i s ~ } } \left\lfloor { \frac { t _ { n - 1 } } { \tau _ { i } } } \right\rfloor$ . we must have:

$$
\left\lfloor \frac {t _ {n} ^ {-}}{\tau_ {i}} \right\rfloor > \left\lfloor \frac {t _ {n - 1}}{\tau_ {i}} \right\rfloor . \tag {45}
$$

Hence, the total number of active devices which need to be served at $t _ { n }$ is equal to:

$$
b _ {n} = \sum_ {i = 1} ^ {L} \mathbb {1} \left(\left\lfloor \frac {t _ {n} {} ^ {-}}{\tau_ {i}} \right\rfloor > \left\lfloor \frac {t _ {n - 1}}{\tau_ {i}} \right\rfloor\right). \tag {46}
$$

Finally, considering $\begin{array} { r l r } { t _ { 0 } } & { { } = } & { 0 . } \end{array}$ we can write $\begin{array} { r l } { b _ { 1 } } & { { } = } \end{array}$ arg max {t1 > τi }.

Proposition 2 gives the exact number of devices that must be served by UAVs at each update time. In this case, the update times can be adjusted according to the number of devices that can be served by the UAVs. Indeed, knowing the exact number of active devices enables us to determine the update times in a deterministic and efficient way based on system requirements.

2) Probabilistic IoT Activation: Certain IoT devices can have probabilistic activations in applications such as health monitoring, and smart traffic control. In this case, each IoT device becomes active at time $t \in [ 0 , T ]$ following the beta distribution as given in (4). For this scenario, we will next derive the specific update times as a function of the average number of active devices.

Theorem 2: The update times during which, on the average, a total of $a _ { n }$ devices must be served by the UAVs, are given by:

$$
t _ {n} = T \times I ^ {- 1} \left(\frac {a _ {n}}{L} + I _ {\frac {t _ {n - 1}}{T}} (\kappa , \omega), \kappa , \omega\right), \quad n > 1, \tag {47}
$$

$$
t _ {1} = T \times I ^ {- 1} \left(\frac {a _ {1}}{L}, \kappa , \omega\right), \tag {48}
$$

where $I _ { x } ( . )$ is the regularized incomplete beta function and $I ^ { - 1 } ( . )$ is its inverse function. L is the total number of IoT devices, and [0, T ] is the time interval during which the devices can be active.

Proof: First, we find the probability that each device becomes active in order to send its data to a UAV at update time $t _ { n } .$ As discussed in the system model, a device needs to transmit at time $t _ { n }$ if it becomes active during time $[ t _ { n - 1 } , t _ { n } )$ . Thus, the probability that each device needs to be served at $t _ { n }$ is:

$$
\begin{array}{l} p _ {n} = \int_ {t _ {n - 1}} ^ {t _ {n}} \frac {t ^ {\kappa - 1} (T - t) ^ {\omega - 1}}{T ^ {\kappa + \omega - 1} B (\kappa , \omega)} \mathrm{d} t = \int_ {\frac {t _ {n - 1}}{T}} ^ {\frac {t _ {n}}{T}} \frac {t ^ {\kappa - 1} (1 - t) ^ {\omega - 1}}{B (\kappa , \omega)} \mathrm{d} t, \\ = \frac {B _ {\frac {t _ {n}}{T}} (\kappa , \omega) - B _ {\frac {t _ {n - 1}}{T}} (\kappa , \omega)}{B (\kappa , \omega)} = I _ {\frac {t _ {n}}{T}} (\kappa , \omega) - I _ {\frac {t _ {n - 1}}{T}} (\kappa , \omega), \tag {49} \\ \end{array}
$$

where $\begin{array} { r } { B _ { x } ( \kappa , \omega ) = \int _ { 0 } ^ { x } y ^ { \kappa - 1 } ( 1 - y ) ^ { \omega - 1 } \mathrm { d } y } \end{array}$ is the incomplete beta function with parameters κ and ω, and $I _ { x } ( . )$ is the regularized incomplete beta function.

Now, the average number of active devices at $t _ { n }$ is given by:

$$
\begin{array}{l} a _ {n} = \sum_ {k = 1} ^ {L} \binom {L} {k} p _ {n} ^ {k} (1 - p _ {n}) ^ {L - k} \\ = L p _ {n} \sum_ {k = 1} ^ {L} \frac {(L - 1) !}{(k - 1) ! (L - k) !} p _ {n} ^ {k - 1} (1 - p _ {n}) ^ {L - k}, \\ = \sum_ {k ^ {\prime} = 0} ^ {L ^ {\prime}} \frac {(L ^ {\prime}) !}{(k ^ {\prime}) ! (L ^ {\prime} - k ^ {\prime}) !} p _ {n} ^ {k ^ {\prime} - 1} (1 - p _ {n}) ^ {L ^ {\prime} - k ^ {\prime}} = L p _ {n}, \tag {50} \\ \end{array}
$$

where in (a), we used $L ^ { \prime } = L - 1$ and $k ^ { \prime } = k - 1$ . Note that, (50) corresponds to the mean of a binomial distribution. Then, we have:

$$
L \left[ I _ {\frac {t _ {n}}{T}} (\kappa , \omega) - I _ {\frac {t _ {n - 1}}{T}} (\kappa , \omega) \right] = a _ {n}, \tag {51}
$$

which leads to:

$$
t _ {n} = T \times I ^ {- 1} \left(\frac {a _ {n}}{L} + I _ {\frac {t _ {n - 1}}{T}} (\kappa , \omega), \kappa , \omega\right). \tag {52}
$$

Finally, considering $\begin{array} { r l r } { I _ { 0 } ( . ) } & { { } = } & { 0 , } \end{array}$ we find $\begin{array} { r l r } { t _ { 1 } } & { { } = } & { T \ \times } \end{array}$ $I ^ { - 1 } \left( \frac { \dot { a } _ { 1 } } { L } , \kappa , \omega \right)$ .

Clearly, the update times need to be determined based on the IoT devices’ activation patterns. In fact, $t _ { n }$ depends on the number of IoT devices, and their activation distribution. Furthermore, according to (47), each $t _ { n }$ depends also on the previous update time, $t _ { n - 1 }$ . This is due to the fact that, the number of active devices that need to be served at $t _ { n } ,$ depends on the update time difference $t _ { n } \mathrm { ~ - ~ } t _ { n - 1 }$ . Using Theorem 2, the update times of the UAVs can be adjusted according to the average number of active devices. Typically, at each update time, the number of devices which need to be served by the UAVs should not be high in order to avoid high interference. However, considering the number of available resources (orthogonal channels and UAVs), it is preferable to serve a maximum number of active devices at each update time. Hence, in this case, the number of active devices at each update time must not be relatively low. Therefore, considering system requirements and different parameters such as mutual interference between devices, acceptable delay for serving the devices, and number of available channels, an appropriate $t _ { n }$ must be adopted. For instance, using Theorem 2, the update times can be set such that the average number of active devices be lower than the number of channels, R, to avoid interference between the devices. Next, we investigate the UAVs’ mobility during the update times.

# B. UAVs’ Mobility

Thus far, we have determined the update times as well as the stop locations at each update time. Here, we investigate how the UAVs should move between the stop locations at different update times. In this case, considering the energy limitation of the UAVs, $E _ { \mathrm { m a x } }$ , we find the optimal trajectory of each UAV to guarantee reliable and energy-efficient uplink transmissions of activation IoT devices. The UAVs update their locations according to the activation of the IoT devices. Therefore, the UAVs move from their initial locations at $t _ { n - 1 }$ to a new optimal locations at $t _ { n } .$ This mobility should be done in such a way that the UAVs spend a minimum total energy on the mobility so as to remain operational for a longer time. In fact, given the optimal sets of UAVs’ locations at $t _ { n - 1 }$ and $t _ { n }$ obtained from Section III, we determine how to move the UAVs between the initial and the new sets of stop locations in order to minimize total mobility of the UAVs.

Now, let $I _ { n - 1 }$ and $I _ { n }$ be two sets comprising the $\mathrm { U A V s } ^ { \prime }$ locations at two consecutive update times $t _ { n - 1 }$ and $t _ { n } .$ . Our goal is to find the optimal mapping between these two sets in a way that the energy used for transportations (between two sets) is minimized. Not that, in our model, the total energy that each UAV can use for the mobility during [0, T ] is limited to $E _ { \mathrm { m a x } }$ . Clearly, in the multiple updates (mobilities) during [0, T ], the maximum energy consumption of each UAV at each update is equal to the remaining energy of the UAV. Let $\Gamma _ { n , k }$ be the remaining energy of the UAV at the location having index $k \in I _ { n - 1 }$ at time $t _ { n }$ . Then, we can write the following UAVs’ mobility optimization problem:

$$
\min _ {\mathbf {Z}} \sum_ {l \in I _ {n}} \sum_ {k \in I _ {n - 1}} E _ {k l} Z _ {k l}, \tag {53}
$$

$$
\text { s.t. } \sum_ {l \in I _ {n}} Z _ {k l} = 1, \sum_ {k \in I _ {n - 1}} Z _ {k l} = 1, \tag {54}
$$

$$
E _ {l k} \leq \Gamma_ {n, k}, Z _ {k l} \in \{0, 1 \}, \forall k \in I _ {n - 1}, \forall l \in I _ {n}, \tag {55}
$$

where $I _ { n - 1 }$ and $I _ { n } ,$ , are the initial and new sets of UAVs’ locations at times $t _ { n - 1 }$ and $t _ { n } . ~ { Z }$ is the $\vert I _ { n } \vert \times \vert I _ { n } \vert$ assignment matrix with each element $Z _ { k l }$ being 1 if UAV k is assigned to location l, and 0 otherwise. $E _ { k l }$ is the energy used for moving a UAV from its initial location with index $k \in I _ { n - 1 }$ to a new location with index $l \in \mathsf { \Gamma } _ { I _ { n } } .$ . Also, $\Gamma _ { n , k }$ is the remaining energy for the UAVs at time $t _ { n } .$ . (55) guarantees that UAVs remain operational until the end of the period T . The total energy consumption of the rotary wing UAV while moving between two stop locations can be computed as done in [28]:

$$
E = \frac {D}{v} (P _ {V} + P _ {H}), \tag {56}
$$

where D is the distance between two stop locations, $D / v$ is the flight duration, $P _ { V }$ is the power consumption for vertical movement, and $P _ { H }$ is the power consumption for horizontal movement. Clearly, if the altitude difference between two stop locations is h, the effective vertical and horizontal velocities will be Accord $\upsilon _ { \upsilon } = \upsilon$ sin [29 $\phi$ and and $\upsilon _ { h } = \upsilon$ $\phi _ { : }$ , with comp $\begin{array} { r } { \phi = \sin ^ { - 1 } \left( \frac { \Delta h } { D } \right) } \end{array}$ . $P _ { H }$ power and induced power needed for overcoming the parasitic drag and the lift-induced drag. The parasitic power, based on [30, equations (13.32), (13.27), and (11.3)], can be given by:

$$
P _ {P} = \frac {1}{2} \rho C _ {D _ {o}} A _ {e} v _ {h} ^ {3} + \frac {\pi}{4} N _ {b} c _ {b} \rho C _ {D _ {o}} \omega^ {3} R ^ {4} \left(1 + 3 \left(\frac {v _ {h}}{\omega R}\right) ^ {2}\right), \tag {57}
$$

where $v _ { h }$ is the effective horizontal velocity, $C _ { D _ { o } }$ is the drag coefficient, $\rho$ is the air density, $c _ { b }$ is the blade chord, $N _ { b }$ is the number of blades, and $A _ { e }$ is the reference area (frontal area of the UAV) [29], [30]. We note that the second term in (57) represents the blade power profile.

Using [30, eqs. (12.2), (13.13), and (13.19)], the induced power (assuming zero tilt angle) can be computed by:

$$
P _ {I} = \omega R W \times \lambda , \tag {58}
$$

where R is the rotor disk radius, W is the weight of the UAV, and ω is the angular velocity. Also, given [30, eqs. (12.1), (13.13), and (13.18)], we can find λ by solving the following equation:

$$
g (\lambda) = 2 \rho \pi \omega^ {2} R ^ {4} \lambda \sqrt {\frac {v _ {h} ^ {2}}{\omega^ {2} R ^ {2}} + \lambda^ {2}} - W = 0. \tag {59}
$$

The power consumption due to the vertical climbing and descending (assuming rapid descent known as windmill state) can be given by [30, eqs. (12.35), (12.47), and (12.50)]:

$$
P _ {V} = \left\{ \begin{array}{l l} \frac {W}{2} v _ {v} + \frac {W}{2} \sqrt {v _ {v} ^ {2} + \frac {2 W}{\rho \pi R ^ {2}}}, & \text { climbing }, \\ \frac {W}{2} v _ {v} - \frac {W}{2} \sqrt {v _ {v} ^ {2} - \frac {2 W}{\rho \pi R ^ {2}}}, & \text { descending }, \end{array} \right. \tag {60}
$$

where $\upsilon _ { \upsilon }$ is the effective vertical velocity. Finally, the total mobility energy consumption is computed using (56)-(60).

Clearly, the optimization problem in (53) is an integer linear programming (ILP). Following the similar approach we used for solving (16), we transform problem (53) to a standard assignment problem which can be solved using the Hungarian method in a polynomial time with a complexity of $O ( | I _ { n } | ^ { 3 } )$ . To this end, we need to remove constraint (55) by considering $E _ { l k } = + \infty$ when the constraint is not satisfied. To determine when (55) is not satisfied, we use $I _ { n - 1 }$ and $I _ { n }$ to compute $E _ { l k }$ , and compare it with the remaining energy of the UAVs, $\Gamma _ { n , k }$ . Then, in the objective function (53), we replace each $E _ { l k }$ corresponding to the unsatisfied constraint with $E _ { l k } ~ = ~ + \infty$ . Consequently, (53) is transformed into a standard assignment problem. The result of solving (53) will be the assignment matrix, Z, that optimally assigns the UAVs to the destinations. Therefore, the locations of the UAVs are updated according to the new destinations. Then, having the destinations of each UAV at different update times, we can find the optimal trajectory of the UAVs.

# V. SIMULATION RESULTS AND ANALYSIS

For our simulations, the IoT devices are located within a geographical area of size 1 km × 1 km. We consider a total number of 500 IoT devices which are uniformly distributed on the area. Furthermore, we consider UAV-based communications in an urban environment with $\psi = 1 1 . 9 5$ and $\beta = 0 . 1 4$ at 2 GHz carrier frequency [8]. Table I lists the simulation parameters. Here, we analyze the transmit power of the IoT devices, the energy consumption of UAVs on their mobility, and the update times. In our update time analysis, unless otherwise stated, we consider the probabilistic activation model for the IoT devices with the beta distribution parameters $\kappa = 3 .$ , and ω = 4 [18]. When applicable, we compare our results with pre-deployed stationary aerial base stations (i.e. UAVs) scenario while adopting the optimal device association and power control technique of Subsection III-A. In the stationary case, the locations of UAVs are assumed to be fixed over the target area and they are not updated according to the devices’ locations. All statistical results are averaged over a large number of independent runs.

Note that, in the given IoT network, serving all the active devices may not be possible due to the limitations on the number of UAVs and the maximum transmit power of the devices. Thus, in Fig. 4, we show the achieved system reliability which, here, is defined as the probability that all the active devices can be served by the UAVs. Clearly, the reliability depends on the locations and transmit powers of the devices as well as the number of UAVs.

![](images/d0dfc8894b1110dae143c03aa8ef2b336da5c53f437e1d619f21b383b09cf89a.jpg)

<details>
<summary>bar</summary>

| P_max (mW) | Stationary aerial base stations | Proposed approach |
| ---------- | ------------------------------- | ----------------- |
| 20         | 0.01                            | 0.18              |
| 40         | 0.30                            | 0.58              |
| 60         | 0.55                            | 0.73              |
| 80         | 0.61                            | 0.75              |
| 100        | 0.72                            | 0.81              |
| 120        | 0.80                            | 0.85              |
</details>

Fig. 4. Reliability comparison between the proposed approach and stationary aerial base stations using 5 UAVs.

![](images/6f72ac1829aaf500c4b1041902330fa3a65ce38fe9b21364e77ece18ccba6821.jpg)

<details>
<summary>scatter</summary>

| UAV   | x-coordinate (m) | y-coordinate (m) | Altitude (m) |
|-------|------------------|------------------|--------------|
| UAV 1 | 400              | 600              | 200          |
| UAV 2 | 400              | 400              | 250          |
| UAV 3 | 400              | 200              | 300          |
| UAV 4 | 400              | 200              | 250          |
| UAV 5 | 600              | 800              | 200          |
| Devices| 600              | 800              | 150          |
</details>

Fig. 5. UAVs’ locations and associations for one illustrative snapshot.

Fig. 4 shows the reliability as the maximum transmit power of the devices, $P _ { \mathrm { m a x } }$ , varies. In this case, 5 UAVs are deployed to serve 100 active IoT devices. Clearly, as $P _ { \mathrm { m a x } }$ increases, the reliability also increases. In fact, for higher $P _ { \mathrm { m a x } }$ values, the devices have a higher chance to successfully connect to UAVs. From Fig. 4, we can see that, our proposed approach leads to a significantly improved reliability compared to the case in which stationary aerial base stations are used. In particular, the difference between the reliability of the stationary case and our proposed approach is significant for lower $P _ { \mathrm { m a x } }$ . Indeed, a higher reliability is achieved by dynamically optimizing the UAVs’ locations based on the locations of the IoT devices. As shown in Fig. 4, by increasing $P _ { \mathrm { m a x } }$ from 40 mW to 100 mW, the reliability increases from 0.3 to 0.72 for the stationary case, while it increases from 0.58 to 0.82 in our proposed approach. Furthermore, the proposed approach yields a maximum of 28% improvement in the system reliability.

Fig. 5 shows a snapshot of the UAVs’ locations and their associated IoT devices (indicated by the same color) resulting from the proposed approach. In this figure, 5 UAVs are efficiently deployed to serve 100 active IoT devices which are uniformly distributed on the area. In this case, all the devices are able to send their data to the associated UAVs by using a minimum total transmit power. The 3D locations of the UAVs as well as the device association are determined based on the locations of the ground IoT devices and their transmit power. In Fig. 6, we show the total transmit power, needed by the IoT devices for reliable uplink communications, versus the number of UAVs in the interference scenario. Clearly, the total transmit power of the IoT devices can be reduced by deploying more UAVs. For instance, considering 100 active devices and 20 available channels, using our proposed approach, the total transmit power decreases from 2.4 W to 0.2 W by increasing the number UAVs from 5 to 10. Furthermore, using the proposed approach, the total transmit power of the devices decreases by 45% (on the average) compared to the stationary case. Clearly, for a lower number of UAVs, the proposed approach leads to a higher power reduction compare to the stationary case. In other words, intelligently optimizing the locations of UAVs provides more power reduction gains when the number of UAVs is low. In fact, for very dense networks with a high number of UAVs, updating the UAVs’ locations is obviously no longer necessary compared to a case with a low number of UAVs. For instance, as we can see from Fig. 6, the power reduction gain achieved by deploying 5 UAVs is around 7 times larger than the case with 10 UAVs.

![](images/08d09a5e20c97b086be48a90d411c844f735a44c38dd57113edb9e5a463f4acc.jpg)

<details>
<summary>line</summary>

| Number of UAVs | Proposed approach | Stationary aerial base stations |
| -------------- | ----------------- | -------------------------------- |
| 5              | 2.4               | 4.1                              |
| 6              | 1.7               | 2.8                              |
| 7              | 0.6               | 1.4                              |
| 8              | 0.3               | 1.0                              |
| 9              | 0.2               | 0.4                              |
| 10             | 0.2               | 0.4                              |
</details>

Fig. 6. Total transmit power of devices vs. number of UAVs in the presence of interference.

![](images/5fe3a84bbe12b93d21e5082fa0a26e1f001863a559d6d7c0dc1ff0a81500b9ef.jpg)

<details>
<summary>line</summary>

| Number of UAVs | Stationary aerial base stations | Proposed approach |
| -------------- | --------------------------------- | ------------------ |
| 5              | 0.41                              | 0.08               |
| 6              | 0.39                              | 0.07               |
| 7              | 0.29                              | 0.06               |
| 8              | 0.22                              | 0.05               |
| 9              | 0.16                              | 0.04               |
| 10             | 0.15                              | 0.03               |
</details>

Fig. 7. Total transmit power of devices vs. number of UAVs in the interference-free scenario.

Fig. 7 shows the total transmit power of the IoT devices as a function of the number of UAVs in an interference-free scenario. Compared to the interference scenario, the devices can obviously use a lower transmit power for sending their data to the UAVs. For instance, by efficiently deploying only 5 UAVs, the devices can establish reliable uplink communications with a total transmit power of 70 mW. Moreover, Fig. 7 shows that, our proposed approach leads to an average of 80% power reduction compared to the stationary case.

![](images/59810aa079e2b6422aa2b88144cfb8a63752624e27127ce68f91c7d29713e227.jpg)

<details>
<summary>line</summary>

| Number of orthogonal channels (R) | Stationary aerial base stations | Proposed approach |
| --------------------------------- | -------------------------------- | ----------------- |
| 25                                | 1.7                              | 1.25              |
| 30                                | 1.0                              | 0.75              |
| 35                                | 0.75                             | 0.5               |
| 40                                | 0.7                              | 0.45              |
| 45                                | 0.65                             | 0.4               |
| 50                                | 0.6                              | 0.35              |
</details>

Fig. 8. Total transmit power of devices vs. number of orthogonal channels.

![](images/4d979f91a5e84530fe07891353e2d1519ef19838fc2624d3b7a9ba554b43815f.jpg)

<details>
<summary>line</summary>

| Update time (normalized) | N=5 (Theory) | N=10 (Theory) | N=5 (Simulations) | N=10 (Simulations) |
| ------------------------ | ------------ | ------------- | ----------------- | ------------------ |
| 0.1                      | 50           | 10            | -                 | 10                 |
| 0.2                      | 70           | 40            | -                 | 40                 |
| 0.3                      | 100          | 80            | -                 | 80                 |
| 0.4                      | 180          | 100           | -                 | 100                |
| 0.5                      | 180          | 100           | -                 | 100                |
| 0.6                      | 180          | 90            | -                 | 90                 |
| 0.7                      | 160          | 60            | -                 | 60                 |
| 0.8                      | 80           | 30            | -                 | 30                 |
| 0.9                      | 40           | 10            | -                 | 10                 |
| 1.0                      | 10           | 5             | -                 | 5                  |
</details>

Fig. 9. Average number of active devices at update times for the probabilistic activation.

Fig. 8 shows the total transmit power of devices used for meeting the SINR requirement as the number of available channels varies. The result in Fig. 8 corresponds to a case with 100 active devices which are served by 5 UAVs. Clearly, the total transmit power decreases as the number of channels increases. This is due to the fact that, when more orthogonal channels are available, the interference between the devices will be lower. As a result, each device can reduce its transmit power while connecting to the serving UAV. From Fig. 8, we can see that, by increasing the number of channels from 25 to 50, the total transmit power of devices can be reduced by 68% in the proposed approach. In fact, the average number of interfering devices decreases from 4 to 2 when we increase the number of channels from 25 to 50. Consequently, less interference is generated by the devices while transmitting to the UAVs.

In Fig. 9, we show the average number of active devices that must be served by UAVs at different update times $t _ { n }$ which are normalized by T . Clearly, the number of active devices at each update time depends the activation process of the devices and the number of update times that indicates how frequently the UAVs serve the devices. In Fig. 9, due to the beta distribution model adopted for the activation of the IoT devices, the number of active devices decreases when $t _ { n }$ exceeds 0.5 for $N ~ = ~ 1 0$ . From Fig. 9, we can see that, for a higher number of update times or equivalently shorter time period between consecutive updates, the average number of devices that need to transmit their data decreases. For example, considering $t _ { n } ~ = ~ 0 . 6 ,$ the average number of active devices decreases from 180 to 80 when the number of updates increases from 5 to 10. We also note that, while a lower number of active devices leads to a lower interference between the devices, it requires more updates and mobility for the UAVs. Fig. 9 also verifies that the analytical results in Theorem 2 match the simulations.

![](images/e042aff840f37957e895184fca848624a420d2c7f69a7a6d37321dee299d35ea.jpg)

<details>
<summary>line</summary>

| Update time (normalized) | 10 updates | 30 updates |
| ------------------------ | ---------- | ---------- |
| 0.1                      | 70         | 65         |
| 0.2                      | 205        | 100        |
| 0.3                      | 250        | 130        |
| 0.4                      | 280        | 135        |
| 0.5                      | 290        | 125        |
| 0.6                      | 235        | 110        |
| 0.7                      | 235        | 115        |
| 0.8                      | 255        | 125        |
| 0.9                      | 285        | 100        |
| 1.0                      | 265        | 125        |
</details>

Fig. 10. Exact number of active devices at different update times for the periodic activation.

![](images/976c1eb1fbfbd890b23e0ff34df9ac9483f68dfe7f4b80875ce3dd9b8c7f89db.jpg)

<details>
<summary>line</summary>

| Update number | a = 100 | a = 75 | a = 50 |
| ------------- | ------- | ------ | ------ |
| 1             | 0.25    | 0.25   | 0.20   |
| 2             | 0.35    | 0.30   | 0.25   |
| 3             | 0.45    | 0.40   | 0.30   |
| 4             | 0.60    | 0.45   | 0.35   |
| 5             | 1.00    | 0.55   | 0.40   |
| 6             | -       | 0.65   | 0.45   |
| 7             | -       | 1.00   | 0.50   |
| 8             | -       | -      | 0.60   |
| 9             | -       | -      | 0.65   |
| 10            | -       | -      | 1.00   |
</details>

Fig. 11. Update times for different average number of active devices.

In Fig. 10, we show the exact number of active devices for the periodic activation case obtained from Proposition 2. In this case, each device becomes active with a certain activation period, $\tau _ { i } .$ As expected, for a higher number of updates, a lower number of active devices will need to be served by the UAVs. For instance, by increasing the number of updates from 10 to 30, on the average, the number of active devices decreases by 58%. Moreover, Fig. 10 shows that the maximum number of active devices for 10 updates is about two times larger than the case with 30 updates. Therefore, in order to avoid the interference between the devices, the number of orthogonal channels must be increased by a two-fold factor when the number of updates decreases from 30 to 10.

Fig. 11 presents a direct result of Theorem 2 that computes the update times based on the average number of active devices. Fig. 11 shows how to set update times in order to ensure that the number of devices (which needs to be served) at each update time does not exceed a specified number, a. As we can see from Fig. 11, to achieve a lower value of a, the updates must occur more frequently to reduce the time interval between the consecutive updates. For example, as can be seen from this figure, to meet $a = 1 0 0 , 7 5 .$ and 50, the 5th update must occur at $t _ { n } = 0 . 4 1 , 0 . 5 5$ , and 1. Moreover, Fig. 11 shows that, the number of updates increases as a decreases. For example, in this case, to reduce a from 100 to 50, the number of updates needs to be doubled.

![](images/716fa7585235ba89507d92d2a013e53cee82cd57718cd410d2f572f37fcb58ab.jpg)

<details>
<summary>line</summary>

| Number of updates | Area size= 0.7km × 0.7km | Area size= 1km × 1km |
| ----------------- | ------------------------ | -------------------- |
| 1                 | 30                       | 40                   |
| 2                 | 60                       | 90                   |
| 3                 | 80                       | 130                  |
| 4                 | 110                      | 180                  |
| 5                 | 130                      | 230                  |
| 6                 | 150                      | 280                  |
| 7                 | 170                      | 330                  |
| 8                 | 200                      | 380                  |
| 9                 | 220                      | 430                  |
| 10                | 240                      | 470                  |
</details>

Fig. 12. Total UAV energy consumption vs. number of updates.

Fig. 12 shows the impact of the number of updates on the amount of energy that the UAVs use to move. For our simulations, we have considered $\upsilon ~ = ~ 1 0 \mathrm { m } / \mathrm { s } , ~ \rho ~ = ~ 1 . 2 2 5 \mathrm { k g } / \mathrm { m } ^ { - 3 }$ , ω = 20 rad/s, R = 0.5 m, $c _ { b } ~ = ~ 1 0 \mathrm { c m }$ , $N _ { b } ~ = ~ 4 .$ , and $W ~ = ~ 5 0 \mathrm { N }$ [30]. Intuitively, a higher number of updates requires more mobility of the UAVs. Therefore, by increasing the number of updates, the total energy consumption of the UAVs will also increase. As we can see from Fig. 12, by increasing the number of updates from 3 to 6, the energy consumption of UAVs increases by a factor of 2.1 when the target area size is 1 km × 1 km. Note that, the mobility of the UAVs also depends on the size of geographical area in which the devices are distributed. Hence, on average, the UAVs need to move further for covering a larger area.

Interestingly, there is an inherent tradeoff between the number of updates, mobility of the UAVs, and transmit power of the IoT devices. In fact, considering Fig. 12, a higher number of updates leads to a higher energy consumption of the UAVs due to the higher mobility. In addition, as shown in Fig. 9, as the number of updates increases, a lower number of the IoT devices will be active at each update time and, hence, there will be lower interference between the devices. As a result, the transmit power of the devices that is needed for satisfying the SINR requirement, can be reduced. As we showed in Fig. 8, the devices’ transmit power decreases as the interference decreases (by increasing the number of orthogonal channels). Thus, while a higher number of updates leads to a lower devices’ transmit power, it requires more UAVs’ mobility.

Fig. 13 shows the overall convergence of the proposed power minimization algorithm that is used for solving the original problem (5) considering 5 UAVs. As we can see from the figure, the total transmit power of the IoT devices converges after 5 iterations. In Fig. 13, each iteration corresponds to a joint solution to the device association and UAVs’ locations optimization problems. Clearly, after several iterations, updating the device association and UAVs’ locations will no longer improve the solution.

![](images/4cfdc174928781167a1595a594b04fd036dc1b30667d128e77e0f967db0d37eb.jpg)

<details>
<summary>line</summary>

| Number of iterations | Total transmit power (W) |
| -------------------- | ------------------------ |
| 1                    | 4.0                      |
| 2                    | 1.5                      |
| 3                    | 0.3                      |
| 4                    | 0.1                      |
| 5                    | 0.1                      |
| 6                    | 0.1                      |
| 7                    | 0.1                      |
</details>

Fig. 13. Overall convergence of the algorithm.

![](images/95034d67b3febb3c7cf3e799394ec222ee570de49430ca8079ceb1ab3832e3a3.jpg)

<details>
<summary>line</summary>

| Number of active devices | Optimality gap (%) | Relative computational time |
| ------------------------ | ------------------ | --------------------------- |
| 10                       | 21                 | 200                         |
| 12                       | 9                  | 300                         |
| 14                       | 7                  | 500                         |
| 16                       | 6                  | 700                         |
| 18                       | 6                  | 900                         |
</details>

Fig. 14. Proposed approach vs. optimal solution.

In Fig. 14, we show an example to compare the accuracy and time complexity of our proposed approach with the optimal solution obtained by an exhaustive search. To perform an exhaustive search over the continuous space, we have discretized the space with a resolution of 0.1 m. In this case, two UAVs are deployed to serve the devices. As shown in this figure, the average gap between the proposed solution and the optimal solution is around 11%. Nonetheless, in this example, the proposed solution is around 500 times faster than the optimal solution.

# VI. CONCLUSION

In this paper, we have proposed a novel framework for efficiently deploying and moving UAVs to collect data in the uplink from ground IoT devices. In particular, we have determined the jointly optimal UAVs’ locations, device association, and uplink power control of the IoT devices such that the total transmit power of the devices under their SINR constraints is minimized. In addition, we have investigated the effective movement of the UAVs to collect the IoT data in a time-varying IoT network. For this case, based on the devices activation process, we have derived the update time instances at which the UAVs must update their locations. Furthermore, we have obtained the optimal trajectories that are used by the UAVs to dynamically serve the IoT devices with a minimum energy consumption. The results have shown that by intelligently moving and deploying the UAVs, the total transmit power of the devices significantly decreases compared to the case with pre-deployed stationary aerial base stations. Moreover, there is a fundamental tradeoff between the number of updates, the UAVs’ mobility, and the devices’ transmit power.

# REFERENCES

[1] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.   
[2] F. Jiang and A. L. Swindlehurst, “Optimization of UAV heading for the ground-to-air uplink,” IEEE J. Sel. Areas Commun., vol. 30, no. 5, pp. 993–1005, Jun. 2012.   
[3] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.   
[4] Y. Zeng, R. Zhang, and T. J. Lim, “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.   
[5] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Mobile Internet of Things: Can UAVs provide an energy-efficient mobile architecture?” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Washington, DC, USA, Dec. 2016, pp. 1–6.   
[6] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE Int. Conf. Commun. (ICC), Kuala Lumpur, Malaysia, May 2016, pp. 1–5.   
[7] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Optimal transport theory for cell association in UAV-enabled cellular networks,” IEEE Commun. Lett., vol. 21, no. 9, pp. 2053–2056, Sep. 2017.   
[8] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.   
[9] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647–1650, Aug. 2016.   
[10] V. V. Chetlur and H. S. Dhillon, “Downlink coverage analysis for a finite 3D wireless network of unmanned aerial vehicles,” IEEE Trans. Commun., to be published.   
[11] S.-Y. Lien, K.-C. Chen, and Y. Lin, “Toward ubiquitous massive accesses in 3GPP machine-to-machine communications,” IEEE Commun. Mag., vol. 49, no. 4, pp. 66–74, Apr. 2011.   
[12] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.   
[13] Y. Pang, Y. Zhang, Y. Gu, M. Pan, Z. Han, and P. Li, “Efficient data collection for wireless rechargeable sensor clusters in harsh terrains using UAVs,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Austin, TX, USA, Dec. 2014, pp. 234–239.   
[14] C.-Y. Tu, C.-Y. Ho, and C.-Y. Huang, “Energy-efficient algorithms and evaluations for massive access management in cellular based machine to machine communications,” in Proc. Veh. Technol. Conf. (VTC), San Francisco, CA, USA, Sep. 2011, pp. 1–5.   
[15] K.-C. Chen and S.-Y. Lien, “Machine-to-machine communications: Technologies and challenges,” Ad Hoc Netw., vol. 18, pp. 3–23, Jul. 2014.   
[16] M. Tavana, V. Shah-Mansouri, and V. W. S. Wong, “Congestion control for bursty M2M traffic in LTE networks,” in Proc. IEEE Int. Conf. Commun. (ICC), London, U.K., Jun. 2015, pp. 5815–5820.   
[17] X. Jian, X. Zeng, Y. Jia, L. Zhang, and Y. He, “Beta/M/1 model for machine type communication,” IEEE Commun. Lett., vol. 17, no. 3, pp. 584–587, Mar. 2013.   
[18] “Study on RAN improvements for machine type communication,” Tech. Rep. TR 37.868, 3GPP, Sep. 2011.   
[19] A. K. Gupta and S. Nadarajah, Handbook of Beta Distribution and Its Applications. Boca Raton, FL, USA: CRC Press, 2004.   
[20] S. Z. Selim and M. A. Ismail, “K-means-type algorithms: A generalized convergence theorem and characterization of local optimality,” IEEE Trans. Pattern Anal. Mach. Intell., vol. PAMI-6, no. 1, pp. 81–87, Jan. 1984.   
[21] R. D. Yates, “A framework for uplink power control in cellular radio systems,” IEEE J. Sel. Areas Commun., vol. 13, no. 7, pp. 1341–1347, Sep. 1995.   
[22] R. Sun, M. Hong, and Z.-Q. Luo, “Joint downlink base station association and power control for max-min fairness: Computation and complexity,” IEEE J. Sel. Areas Commun., vol. 33, no. 6, pp. 1040–1054, Jun. 2015.

[23] R. E. Burkard, M. Dell’Amico, and S. Martello, Assignment Problems. Philadelphia, PA, USA: SIAM, 2009.   
[24] H. W. Kuhn, “The Hungarian method for the assignment problem,” Naval Res. Logistics Quart., vol. 2, nos. 1–2, pp. 83–97, Mar. 1955.   
[25] P. T. Boggs and J. W. Tolle, “Sequential quadratic programming,” Acta Numer., vol. 4, pp. 1–51, Jan. 1995.   
[26] K. Scheinberg, “An efficient implementation of an active set method for SVMs,” J. Mach. Learn. Res., vol. 7, pp. 2237–2257, Oct. 2006.   
[27] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.   
[28] C. Di Franco and G. Buttazzo, “Energy-aware coverage path planning of UAVs,” in Proc. IEEE Int. Conf. Auto. Robot Syst. Competitions (ICARSC), Vila Real, Portugal, Apr. 2015, pp. 1–5.   
[29] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[30] A. Filippone, Flight Performance of Fixed and Rotary Wing Aircraft. Amsterdam, The Netherlands, Elsevier, 2006.

![](images/a9ce6a25e441d1f8c0631ac4cd8a9acd04386d2ed3e9bbbce0d122d282024cfe.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man with short dark hair and beard wearing a blue checkered shirt (no text or symbols visible)
</details>

Mohammad Mozaffari (S’15) received the B.Sc. degree in electrical engineering from the Sharif University of Technology, Iran, and the M.Sc. degree in geomatics engineering from the University of Calgary, Canada. He is currently pursuing the Ph.D. degree with the Bradley Department of Electrical and Computer Engineering, Virginia Tech. His research interests include wireless communications and statistical signal processing with a focus on unmanned aerial vehicle communications, 5G networks, satellite communications and localization.

![](images/df137b3ca97b8df7b9a1cd8c57edd92a95f4267ed2cb2968321711e823914efa.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in business attire (no text or symbols visible)
</details>

Walid Saad (S’07–M’10–SM’15) received the Ph.D. degree from the University of Oslo in 2010. He is currently an Associate Professor with the Department of Electrical and Computer Engineering, Virginia Tech, where he leads the Network Science, Wireless, and Security (NetSciWiS) Laboratory, Wireless@VT Research Group. His research interests include wireless networks, game theory, cyber security, unmanned aerial vehicles, and cyberphysical systems. He was a recipient of the NSF CAREER Award in 2013, the AFOSR Summer

Faculty Fellowship in 2014, and the Young Investigator Award from the Office of Naval Research in 2015. He has authored/co-authored six conference Best Paper Awards at the WiOpt in 2009, ICIMP in 2010, the IEEE WCNC in 2012, the IEEE PIMRC in 2015, the IEEE SmartGridComm in 2015, and EuCNC in 2017. He was a recipient of the 2015 Fred W. Ellersick Prize from the IEEE Communications Society. In 2015, he was named the Stephen O. Lane Junior Faculty Fellow at Virginia Tech and, in 2017, he was named the College of Engineering Faculty Fellow. He currently serves as an Editor of the IEEE TRANSACTIONS ON WIRELESS COMMU-NICATIONS, the IEEE TRANSACTIONS ON COMMUNICATIONS, the IEEE TRANSACTIONS ON MOBILE COMPUTING, and the IEEE TRANSACTIONS ON INFORMATION FORENSICS AND SECURITY.

![](images/20e0be5971979cef0e57ce8a1c982681a4c11404a754b2be38b27ba4a1961c37.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man with curly hair and beard (no text or symbols visible)
</details>

Mehdi Bennis (SM’15) received the M.Sc. degree in electrical engineering jointly from the EPFL, Switzerland, and the Eurecom Institute, France, in 2002, and the Ph.D. degree in 2009, with a focus on spectrum sharing for future mobile cellular systems. From 2002 to 2004, he was a Research Engineer with IMRA-EUROPE, where he was involved in investigating adaptive equalization algorithms for mobile digital TV. In 2004, he joined the Centre for Wireless Communications, University of Oulu, Finland, as a Research Scientist. In 2008, he was a Visiting Researcher with the Alcatel-Lucent Chair on flexible radio, SUP-ELEC. He is currently an Adjunct Professor with the University of Oulu and also the Academy of Finland Research Fellow. His main research interests are in radio resource management, heterogeneous networks, game theory, and machine learning in 5G networks and beyond. He has co-authored one book and published over 100 research papers in international conferences, journals, and book chapters. He was a recipient of the prestigious 2015 Fred W. Ellersick Prize from the IEEE Communications Society, the 2016 Best Tutorial Prize from the IEEE Communications Society, and the 2017 EURASIP Best paper Award for the Journal of Wireless Communications and Networks. He currently serves as an Editor of the IEEE TRANSACTIONS ON WIRELESS COMMUNICATION.

![](images/4c262360bf00ca54a3884734ba524aec46d250caa8e8bbd35aac6af4973f4393.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man in business attire (no text or symbols visible)
</details>

Mérouane Debbah (F’15) received the M.Sc. and Ph.D. degrees from the Ecole Normale Supérieure Paris-Saclay, France. He joined the Ecole Normale Supérieure Paris-Saclay in 1996. He was with Motorola Labs, Saclay, France, from 1999 to 2002, and the Vienna Research Center for Telecommunications, Vienna, Austria, until 2003. From 2003 to 2007, he was with the Mobile Communications Department, Institut Eurecom, Sophia Antipolis, France, as an Assistant Professor. Since 2007, he has been a Full Professor with CentraleSupelec, Gif-sur-Yvette, France. From 2007 to 2014, he was the Director of the Alcatel-Lucent Chair on flexible radio. Since 2014, he has been the Vice President of the Huawei France Research and Development Center and the Director of the Mathematical and Algorithmic Sciences Laboratory. He has managed 8 EU projects and more than 24 national and international projects. His research interests lie in fundamental mathematics, algorithms, statistics, and information and communication sciences research. He is a WWRF fellow and a member of the Academic Senate of Paris-Saclay. He was a recipient of the ERC Grant MORE, Advanced Mathematical Tools for Complex Network Engineering. He received 17 best paper awards, among which the 2007 IEEE GLOBECOM Best Paper Award, the Wi-Opt 2009 Best Paper Award, the 2010 Newcom++ Best Paper Award, the WUN CogCom Best Paper 2012 and 2013 Award, the 2014 WCNC Best Paper Award, the 2015 ICC Best Paper Award, the 2015 IEEE Communications Society Leonard G. Abraham Prize, the 2015 IEEE Communications Society Fred W. Ellersick Prize, the 2016 IEEE Communications Society Best Tutorial Paper Award, the 2016 European Wireless Best Paper Award, the 2017 Eurasip Best Paper Award, the Valuetools 2007, Valuetools 2008, CrownCom2009, Valuetools 2012, and SAM 2014 Best Student Paper Awards. He was a recipient of the Mario Boella Award in 2005, the IEEE Glavieux Prize Award in 2011, and the Qualcomm Innovation Prize Award in 2012. He was an Associate and a Senior Area Editor of the IEEE TRANSACTIONS ON SIGNAL PROCESSING from 2011 to 2013 and from 2013 to 2014, respectively. He is currently an Associate Editor-in-Chief of the journal Random Matrix: Theory and Applications.