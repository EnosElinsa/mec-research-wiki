# Computation Rate Maximization in UAV-Enabled Wireless-Powered Mobile-Edge Computing Systems

Fuhui Zhou , Member, IEEE, Yongpeng Wu , Senior Member, IEEE, Rose Qingyang Hu , Senior Member, IEEE, and Yi Qian , Senior Member, IEEE

Abstract— Mobile-edge computing (MEC) and wireless power transfer are two promising techniques to enhance the computation capability and to prolong the operational time of low-power wireless devices that are ubiquitous in Internet of Things. However, the computation performance and the harvested energy are significantly impacted by the severe propagation loss. In order to address this issue, an unmanned aerial vehicle (UAV)-enabled MEC wireless-powered system is studied in this paper. The computation rate maximization problems in a UAV-enabled MEC wireless powered system are investigated under both partial and binary computation offloading modes, subject to the energy-harvesting causal constraint and the UAV’s speed constraint. These problems are non-convex and challenging to solve. A two-stage algorithm and a three-stage alternative algorithm are, respectively, proposed for solving the formulated problems. The closed-form expressions for the optimal central processing unit frequencies, user offloading time, and user transmit power are derived. The optimal selection scheme on whether users choose to locally compute or offload computation tasks is proposed for the binary computation offloading mode.

Manuscript received January 4, 2018; revised May 1, 2018; accepted June 15, 2018. Date of publication August 13, 2018; date of current version November 21, 2018. The work of F. Zhou was supported in part by the Natural Science Foundation of China under Grant 61701214, in part by the Excellent Youth Foundation of Jiangxi Province under Grant 2018ACB21012, in part by the Young Natural Science Foundation of Jiangxi Province under Grant 20171BAB212002, in part by the Open Foundation of the State Key Laboratory of Integrated Services Networks under Grant ISN19-08, and in part by the Postdoctoral Science Foundation of Jiangxi Province under Grant 2017M610400, Grant 2017KY04, and Grant 2017RC17. The work of Y. Wu was supported in part by the Natural Science Foundation of China under Grant 61701301 and in part by the Young Elite Scientist Sponsorship Program by CAST. The work of R. Q. Hu was supported in part by the National Science Foundation under Grants EECS-1308006, NeTS-1423348, and EARS-1547312 and in part by the Natural Science Foundation of China under Grant 61728104. The work of Y. Qian was supported by the National Science Foundation under Grants EECS-1307580, NeTS-1423408, and EARS-1547330. (Corresponding author: Yongpeng Wu.)

F. Zhou is with the School of Information Engineering, Nanchang University, Nanchang 330031, China, also with the Department of Electrical and Computer Engineering, Utah State University, Logan, UT 84322 USA, and also with the State Key Laboratory of Integrated Services Networks, Xidian University, Xi’an 710071, China (e-mail: zhoufuhui@ieee.org).

Y. Wu is with the Department of Electronic Engineering, Shanghai Jiao Tong University, Minhang 200240, China (e-mail: yongpeng.wu@sjtu.edu.cn).

R. Q. Hu is with the Department of Electrical and Computer Engineering, Utah State University, Logan, UT 84322 USA (e-mail: rose.hu@usu.edu).

Y. Qian is with the Department of Electrical and Computer Engineering, University of Nebraska–Lincoln, Omaha, NE 68182 USA (e-mail: yqian2@unl.edu).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/JSAC.2018.2864426

Simulation results show that our proposed resource allocation schemes outperform other benchmark schemes. The results also demonstrate that the proposed schemes converge fast and have low computational complexity.

Index Terms— Mobile-edge computing, wireless power transfer, unmanned aerial vehicle-enabled, resource allocation, binary computation offloading, partial computation offloading.

# I. INTRODUCTION

THE Internet of Things (IoT) has been widely developedwith the unprecedented proliferation of mobile devices, with the unprecedented proliferation of mobile devices, such as smart phones, cloud-based mobile sensors, tablet computers and wearable devices, which facilitates the realization of smart environment (e.g. smart city, smart home, smart transportation, etc.) [1]. IoT enables mobile users to experience intelligent applications (e.g., automatic navigation, face recognition, unmanned driving, etc.) and to enjoy diverse services with high quality of service (QoS) such as mobile online gaming, augmented reality, etc. These services normally require a massive number of size-constrained and low-power mobile devices to perform computation-intensive and latency-sensitive tasks [2]. However, it is challenging for mobile devices to perform these services due to their low computing capability and finite battery lifetime.

Mobile edge computing (MEC) and wireless power transfer (WPT) have been deemed two promising technologies to tackle the above mentioned challenges [2]–[4]. Recently, MEC has received an ever-increasing level of attention from industry and academia since it can significantly improve the computation capability of mobile devices in a cost-effective and energy-saving manner [2]. It enables mobile devices to offload partial or all of their computation-intensive tasks to MEC servers that locate at the edge of the wireless network, such as cellular base stations (BSs) and access points (APs). Different from the conventional cloud computing, MEC servers are deployed in a close proximity to end users. Thus, MEC has the potential to provide low-latency services, to save energy for mobile users, and to achieve high security [2]. Up to now, there are a number of leading companies (e.g., IBM, Intel, and Huawei) that have identified MEC as a promising technique for the future wireless communication networks. In general, MEC has two operation modes, namely, partial and binary computation offloading. In the first mode, the computation task can be partitioned into two parts, and one part is locally executed while the other part is offloaded to the MEC servers for computing [5]–[9]. For the second mode, computation tasks cannot be partitioned. Thus they can be either executed locally or completely offloaded [10].

On the other hand, WPT can provide low-power mobile devices with sustainable and cost-effective energy supply by using radio-frequency (RF) signals [3]. It facilitates a perpetual operation and enables users to have high QoE, especially in the case that mobile devices do not have sufficient battery energy for offloading task or taking the services when the battery energy is exhausted. Compared to the conventional energy harvesting techniques, such as solar or wind charging, WPT is more attractive since it can provide a controllable and stable power supply [4]. It is envisioned that the computation performance can be significantly improved by integrating WPT into MEC networks [11]–[16]. However, the harvested power level can be significantly degraded by the severe propagation loss. Recently, an unmanned aerial vehicle (UAV)-enabled WPT architecture has been proposed to improve the energy transfer efficiency [17]–[20]. It utilizes an unmanned aerial vehicle (UAV) as an energy transmitter for powering the ground mobile users. It was shown that the harvested power level can be greatly improved due to the fact that there is a high possibility that short-distance line-of-sight (LoS) energy transmit links exist [17]–[20]. Moreover, the computation performance can also be improved by using the UAV-assisted MEC architecture [21]–[25]. Furthermore, UAV-assisted architectures can provide flexible deployment and low operational costs, and are particularly helpful in the situations that the conventional communication systems are destroyed by natural disasters [26]–[32].

Motivated by the above mentioned reasons, a UAV-enabled and wireless powered MEC network is studied in this paper. In order to maximize the achievable computation rate, the communication and computation resources and the trajectory of the UAV are jointly optimized under both partial and binary computation offloading modes. To the authors’ best knowledge, this is the first work that considers the UAV-enabled wireless powered MEC network and studies the computation rate maximization problems in this type of network.

# A. Related Work and Motivation

In wireless powered MEC systems, it is of great importance to design resource allocation schemes so as to efficiently exploit energy, communication, and computation resources and improve the computation performance. Resource allocation problems have been extensively investigated in the conventional MEC networks [5]–[10] and also in MEC networks relying on energy harvesting [11]–[16]. Recently, efforts have also been dedicated to designing resource allocation and trajectory schemes in UAV-enabled wireless powered communications network [17]–[20] and UAV-assisted MEC networks [21]–[25]. These contributions are summarized as follows.

In MEC networks, the communication and computation resources and the selection of the offloading mode were jointly optimized to achieve the objective of the system design, e.g., the users’ consumption energy minimization [5], [6], the revenue maximization [7], the maximum cost minimization [8], etc. Specifically, in [5], the total energy of all users in a multi-cell MEC network was minimized by jointly optimizing the user transmit precoding matrices and the central processing unit (CPU) frequencies of the MEC server allocated to each user. It was shown that the performance achieved by jointly optimizing the communication and computation resources is superior to that obtained by optimizing these resources separately. You et al. [6] extended the energy minimization problem into the multi-user MEC systems with time-division multiple access (TDMA) and orthogonal frequency-division multiple access (OFDMA), respectively. It was proved that the optimal offloading policy has a threshold-based structure, which is related to the channel state information (CSI) [6]. Particularly, mobile users offload their computation tasks when the channel condition is strong; otherwise, they can locally execute the computation tasks. In [7], the revenue of the wireless cellular networks with MEC was maximized by jointly designing the computation offloading decision, resource allocation, and content caching strategy. The works in [5]–[7] focused on optimizing a single objective, which over-emphasizes the importance of one metric and may not achieve a good tradeoff among multiple metrics. Recently, Du et al. [8] and Liu et al. [9] studied the fairness and multi-objective optimization problem in MEC networks. It was shown that there exist multiple tradeoffs in MEC systems, such as the tradeoff between the total computation rate and the fairness among users. Different from the works in [5]–[9], MEC systems with the binary computation offloading mode were considered and the optimal resource allocation strategy was designed to minimize the consumption energy in [10].

Energy harvesting was not considered in the MEC systems [5]–[10]. Recently, Xu et al. [11], Mao et al. [12], You et al. [13], Wang et al. [14], Mao et al. [15] , and Bi and Zhang [16] have studied the resource allocation problem in various MEC systems relying on energy harvesting. In [11] and [12], The reinforcement learning and Lyapunov optimization theory were used to design resource allocation schemes in MEC systems relying on the conventional energy harvesting techniques. Different from [11] and [12], the resource allocation problems were studied in wireless powered MEC systems [13]–[16]. Specifically, You et al. [13] proposed an energy-efficient computing framework in which the energy consumed for local computing and task offloading is from the harvested energy. The consumed energy was minimized by jointly optimizing the CPU frequency and the mode selection. In [14], the energy minimization problem was extended into a multi-input single-out wireless powered MEC system, and the offloading time, the offloading bits, the CPU frequency and the energy beamforming were jointly optimized. Unlike [14], energy efficiency was defined and maximized in a full-duplex wireless powered MEC system by jointly optimizing the transmission power, offloaded bits, computation energy consumption, time slots for computation offloading and energy transfer [15]. In contrast to the work in [13]–[15], the computation bits were maximized in a wireless powered MEC system under the binary computation offloading mode [16]. Two sub-optimal algorithms based on the alternating direction method were proposed to solve the combinatorial programming problem. The proposed algorithms actually did not provide the optimal selection scheme for the user operation mode.

Although WPT has been exploited to improve the computation performance of MEC systems [13]–[16], the energy harvested by using WPT can be significantly degraded by the severe propagation loss. The energy conversion efficiency is low when the distance between the energy transmitter and the harvesting users is large. In order to tackle this challenge, the authors in [17]–[20] proposed a UAV-enabled wireless powered architecture where a UAV transmits energy to the harvesting users. Due to the high possibility of having lineof-sight (LoS) air-to-ground energy harvesting links, the harvesting energy can be significantly improved by using this architecture. Moreover, it was shown that the harvesting energy can be further improved by optimizing the trajectory of the UAV [18]–[20]. Thus, it is envisioned that the application of the UAV-enabled architecture into wireless powered MEC systems is promising and valuable to be studied [26]. However, to the authors’ best knowledge, few investigations have focused on this area.

Recently, the UAV-enabled MEC systems have been studied and their resource allocation schemes have been proposed [21]–[25]. In [21], the UAV-enabled MEC architecture was first proposed and the computation performance was improved by using UAV. Zhao et al. [22] proposed a new caching UAV framework to help small cells to offload traffic. It was shown that the throughput can be greatly improved while the overload of wireless backhaul can be significantly reduced. In order to further improve the computation performance, Jeong et al. [23], [24] designed a resource allocation scheme that jointly optimizes the CPU frequency and the trajectory of the UAV. In [25], a theoretical game method was applied to design a resource allocation scheme for the UAV-enabled MEC system and the existence of Nash Equilibrium was demonstrated.

Although resource allocation problems have been well studied in MEC systems [5]–[10], MEC systems relying on energy harvesting [11]–[16] and UAV-enabled MEC systems [21]–[25], few investigations have been conducted for designing resource allocation schemes in the UAV-enabled wireless powered MEC systems. Moreover, resource allocation schemes proposed in the above-mentioned works are inappropriate to UAV-enabled MEC wireless powered systems since the computation performance not only depends on the optimization of energy, communication and computation resources, but also relies on the design of the UAV trajectory. Furthermore, the application of UAV into wireless powered MEC systems has the potential to enhance the user computation capability since it can improve the energy conversion efficiency and task offloading efficiency [33], [34]. Thus, in order to improve the computation performance and provide mobile users with high QoE, it is of great importance and worthiness to study resource allocation problems in UAV-enabled wireless powered MEC systems. However, these problems are indeed challenging to tackle. The reasons are from two aspects. On one hand, there exists dependence among different variables (e.g., the CPU frequency, the task offloading time and the variables related to the trajectory of the UAV), which makes the problems non-convex. On the other hand, when the binary computation offloading mode is applied, the resource allocation problems in UAV-enabled wireless powered MEC systems have binary variables related to the selection of either local computation or offloading tasks. It makes the problem a mixed integer non-convex optimization problem.

# B. Contributions and Organization

In contrast to [5]–[16], this paper studies the resource allocation problem in UAV-enabled wireless powered MEC systems, where a UAV transmits energy signals to charge multiple mobile users and provides computation services for them. Although the computation performance is limited by the flight time of the UAV, it is worth studying UAV-enabled wireless powered MEC systems since these systems are promising in environments such as mountains and desert areas, where no terrestrial wireless infrastructures exist, and in environments where the terrestrial wireless infrastructures are destroyed due to the natural disasters [33], [34]. Thus, in this paper, the weighted sum computation bits of all users are maximized under both partial and binary computation offloading modes. The main contributions of this work are summarized as follows:

1) It is the first time that the resource allocation framework is formulated in UAV-enabled MEC wireless powered systems under both partial and binary computation offloading modes. The weighted sum computation bits are maximized by jointly optimizing the CPU frequencies, the offloading times and the transmit powers of users as well as the UAV trajectory. Under the partial computation offloading mode, a two-stage alternative algorithm is proposed to solve the non-convex and challenging computation bits maximization problem. The closed-form expressions for the optimal CPU frequencies, the offloading times and the transmit powers of users are derived for any given trajectories.

2) Under the binary computation offloading mode, the weighted sum computation bits maximization problem is a mixed integer non-convex optimization problem, for which a three-stage alternative algorithm is proposed. The optimal selection scheme on whether users choose to locally compute or offload tasks is derived in a closed-form expression for a given trajectory. The structure for the optimal selection scheme shows that whether users choose to locally compute or offload their tasks to the UAV for computing depends on the tradeoff between the achievable computation rate and the operation cost. Moreover, the trajectory of the UAV is optimized by using the successive convex approximation (SCA) method under both partial and binary computation offloading modes.

3) The simulation results show that the computation performance obtained by using the proposed resource allocation scheme is better than these achieved by using the disjoint optimization schemes. Moreover, it only takes several iterations for the proposed alternative algorithms to converge. Furthermore, simulation results verify that the priority and fairness of users can be improved by using the weight vector. Additionally, it is shown that the total computation bits increase with the number of users.

![](images/3d8dd3e37f8b7f0fbbe30629917d0a97c57e616b7f40900f15e3a40e5f16565b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Drone"] -->|Wireless powered link| B["User1"]
    A -->|Computation offloading link| C["User2"]
    A -->|Wireless powered link| D["UseM"]
    B --> E["y"]
    C --> F["y"]
    D --> G["y"]
    E --> H["z"]
    F --> I["z"]
    G --> J["z"]
    H --> K["Energy harvesting"]
    I --> L["Local computing"]
    J --> M["Usem"]
```
</details>

Fig. 1. The system model.

The remainder of this paper is organized as follows. Section II gives the system model. The resource allocation problem is formulated under the partial computation offloading mode in Section III. Section IV formulates the resource allocation problem under the binary computation offloading mode. Simulation results are presented in Section V. Finally, our paper is concluded in Section VI.

# II. SYSTEM MODEL

A UAV-enabled wireless powered MEC system is considered in Fig. 1, where an RF energy transmitter and an MEC server are implemented in UAV. The UAV transmits energy to M users and provides MEC services for these users. Each user has an energy harvesting circuit and can store energy for its operation. The UAV has an on-board communication circuit and an on-board computing processor. So does each user. The computing processor of each user is an on-chip microprocessor that has low computing capability and can locally execute simple tasks. The UAV has a powerful processor that can perform computation-intensive tasks [21]–[25]. Similar to [13]–[16], each user can simultaneously perform energy harvesting, local computing and computation offloading while the UAV can simultaneously transmit energy and perform computation. In this paper, all devices are equipped with a single antenna.

Without loss of generality, a three-dimensional (3D) Euclidean coordinate is adopted. Each user’s location is fixed on the ground. The location of the mth ground user is denoted by $\mathbf { q } _ { m } .$ , where $\mathbf { q } _ { m } = [ x _ { m } , y _ { m } ] , m \in \mathcal { M }$ and $\mathcal { M } = \{ 1 , 2 , \cdots , M \}$ . Boldface lower case letters represent vectors and boldface upper case letters represent matrices. $x _ { m }$ and $y _ { m }$ are the horizontal plane coordinates of the mth ground user. It is assumed that user positions are known to the UAV for designing the trajectory [18]–[20]. A finite time horizon with duration T is considered. During T , the UAV flies at the same altitude level denoted by H $( H > 0 )$ . In practice, the fixed altitude is the minimum altitude that is appropriate to the work terrain and can avoid building without the requirement of frequent aircraft descending and ascending. A block fading channel model is applied, i.e., during each T , the channel remains static.

For the ease of exposition, the finite time T is discretized into N equal time slots, denoted by $n = 1 , 2 , \cdots , N$ . At the nth slot, it is assumed that the horizontal plane coordinate of the UAV is ${ \bf q } _ { u } \left[ n \right] = [ x _ { u } [ n ] , y _ { u } [ n ] ]$ . Similar to [27]–[32], it is assumed that the wireless channel between the UAV and each user is dominated by LOS. Thus, the channel power gain between the UAV and the mth user, denoted by $h _ { m } \left[ n \right]$ , can be given as

$$
h _ {m} [ n ] = \beta_ {0} d _ {m, n} ^ {- 2} = \frac {\beta_ {0}}{H ^ {2} + \left\| \mathbf {q} _ {u} [ n ] - \mathbf {q} _ {m} \right\| ^ {2}}, m \in \mathcal {M}, n \in \mathcal {N}, \tag {1}
$$

where $\beta _ { 0 }$ is the channel power gain at a reference distance $d _ { 0 } ~ = ~ 1$ m; $d _ { m , n }$ is the horizontal plane distance between the UAV and the mth user at the nth slot, $n \in \mathcal { N } , \mathcal { N } =$ $\{ 1 , 2 , \cdots , N \} ; \| \cdot \|$ denotes its Euclidean norm. The details for the UAV-enabled wireless powered MEC system are presented under partial and binary computation offloading modes in the following, respectively.

# A. Partial Computation Offloading Mode

Under the partial computation offloading mode, the computation task of each user can be partitioned into two parts, one for local computing and one for offloading to the UAV. The energy consumed for local computing and task offloading comes from the harvested energy. In this paper, in order to shed meaningful insights into the design of a UAV-enabled wireless powered MEC system, similar to [4] and [13]–[16], the linear energy harvesting model is applied. Thus, the harvested energy $E _ { m } \left[ n \right]$ at the mth user during n time slots is given as

$$
E _ {m} [ n ] = \sum_ {i = 1} ^ {n} \frac {T \eta_ {0} h _ {m} [ i ] P _ {0}}{N}, \quad m \in \mathcal {M}, n \in \mathcal {N}, \tag {2}
$$

where $\eta _ { 0 }$ denotes the energy conservation efficiency, $0 < \eta _ { 0 } \leq 1$ and $P _ { 0 }$ is the transmit power of the UAV. In this paper, the UAV employs a constant power transmission [18]–[20]. The details for the operation of each user under the partial computation offloading mode are presented as follows.

1) Local Computation: Similar to [14]–[16], the energy harvesting circuit, the communication circuit, and the computation unit are all separate. Thus, each user can simultaneously perform energy harvesting, local computing, and computation offloading. Let C denote the number of CPU cycles required for computing one bit of raw data at each user. In order to efficiently use the harvested energy, each user adopts a dynamic voltage and frequency scaling technique and then can adaptively control the energy consumed for performing local computation by adjusting the CPU frequency during each time slot [14]–[16]. The CPU frequency of the mth user during the nth slot is denoted by $f _ { m } \left[ n \right]$ with a unit of cycles per second. Thus, the total computation bits executed at the mth user during n slots and the total consumed energy at the mth user during n slots are respectively given as $\sum { \frac { n } { \sum { \frac { T f _ { m } [ k ] } { N C } } } }$ and ${ \frac { T } { N } } \sum _ { k = 1 } ^ { n } \gamma _ { c } f _ { m } ^ { 3 }$ [k] [14]–[16], where $\gamma _ { c }$ is the k=1 k=1 effective capacitance coefficient of the processor’s chip at the mth user, $n \in \mathcal { N } , m \in \mathcal { M }$ . Note that $\gamma _ { c }$ is dependent of the chip architecture of the mth user.

![](images/3d53988fbe5e428e1f455d58c0b52027b40929291c3424d1cf017c6853365c9b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["The first slot"] --> B["The second slot"]
    B --> C["..."]
    C --> D["The nth slot"]
    D --> E["..."]
    E --> F["The Nth slot"]
    G["User1 → UAV Offloading"] --> H["..."]
    I["UserM → UAV Offloading"] --> J["..."]
    K["UAV → User1 Download"] --> L["..."]
    M["UAV → UserM Download"] --> N["..."]
    O["t1 [1"] --> P["..."]
    Q["tM [1"] --> R["..."]
    S["≈ 0"] --> T["..."]
    U["≈ 0"] --> V["..."]
```
</details>

Fig. 2. The TDMA protocol for multiuser computation offloading.

2) Computation Offloading: In order to avoid interference among users during the offloading process, a TDMA protocol shown in Fig. 2 is applied. Specifically, each time slot consists of three stages, namely, the offloading stage, the computation stage, and the downloading stage. In the offloading stage, M users offload their respective computation task one by one during each slot. Let $t _ { m } \left[ n \right] \times T / N \ ( 0 \leq t _ { m } \left[ n \right] \leq 1 )$ denote the duration in which the mth user offloads its computation task to the UAV at the nth slot, $n \in \mathcal { N } , m \in \mathcal { M }$ . Similar to [16], the computation task of the mth user to be offload is composed of raw data and communication overhead, such as the encryption and packer header. Let $\nu _ { m } R _ { m } \left[ n \right]$ denote the total number of bits that the mth user offloads to the UAV during the nth slot, where $R _ { m } \left[ n \right]$ is the number of raw data to be computed at the UAV and $\nu _ { m }$ indicates the communication overhead included in the offloading task. Thus, one has

$$
\begin{array}{l} R _ {m} [ n ] \leq \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] P _ {m} [ n ]}{\sigma_ {0} ^ {2}}\right), \\ n \in \mathcal {N}, \quad m \in \mathcal {M}, \tag {3} \\ \end{array}
$$

where B is the communication bandwidth; $P _ { m } \left[ n \right]$ is the transmit power of the mth user at the nth slot and $\sigma _ { 0 } ^ { 2 }$ denotes the noise power at the mth user.

After all users offload their computation tasks at the nth slot, the UAV performs computing task and sends the computing results back to all the users. Similar to [14]–[16], the computation time and the downloading time of the UAV are neglected since the UAV has a much stronger computation capability than the users and the number of the bits related to the computation result is very small. Since the total offloading time of all users does not exceed the duration of one time slot, one has

$$
\sum_ {m = 1} ^ {M} t _ {m} [ n ] \leq 1, \quad n \in \mathcal {N}. \tag {4}
$$

Since the energy consumed for local computing and task offloading comes from the harvested energy, the following energy harvesting causal constraint should be satisfied.

$$
\begin{array}{l} \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ \gamma_ {c} f _ {m} ^ {3} [ k ] + t _ {m} [ k ] P _ {m} [ k ] \right] \leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0}, \\ n \in \mathcal {N}, \quad m \in \mathcal {M}. \tag {5} \\ \end{array}
$$

Under the partial computation offloading mode, the total computation bits $R _ { m }$ of the mth user is given as

$$
\begin{array}{l} R _ {m} = \sum_ {n = 1} ^ {N} \frac {T f _ {m} [ n ]}{N C} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \mathrm{log} _ {2} \left(1 + \frac {h _ {m} [ n ] P _ {m} [ n ]}{\sigma_ {0} ^ {2}}\right), \\ m \in \mathcal {M}. \tag {6} \\ \end{array}
$$

# B. Binary Computation Offloading Mode

Under the binary computation offloading mode, the computation task cannot be partitioned. All the users need to choose to either locally compute the task completely or offload the entire task. This case can be widely experienced in practice. For example, in order to improve the estimation accuracy, the raw data samples that are correlated need to be jointly computed altogether [10], [16]. Let $\mathcal { M } _ { 0 }$ and $\mathcal { M } _ { 1 }$ denote the set of users that choose to perform local computation and the set of users that choose to perform task offloading, respectively. Thus, $\mathcal { M } = \mathcal { M } _ { 0 } \cup \mathcal { M } _ { 1 }$ and $\mathcal { M } _ { 0 } \cap \mathcal { M } _ { 1 } = \Theta$ , where Θ denotes the null set.

1) Users Choosing to Perform Local Computing: In this case, a user in $\mathcal { M } _ { 0 }$ exploits all the harvested energy to perform local computing. Thus, the total computation rate of the ith user denoted by $R _ { i } ^ { L }$ can be given as

$$
R _ {i} ^ {L} = \sum_ {n = 1} ^ {N} \frac {T f _ {i} [ n ]}{N C}, \quad i \in \mathcal {M} _ {0}. \tag {7}
$$

And the energy harvesting causal constraint for a user in $\mathcal { M } _ { 0 }$ can be given as

$$
\frac {T}{N} \sum_ {k = 1} ^ {n} \gamma_ {c} f _ {i} ^ {3} [ k ] \leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {i} [ k ] P _ {0}, \quad n \in \mathcal {N}, i \in \mathcal {M} _ {i}. \tag {8}
$$

2) Users Choosing to Perform Task Offloading: Each user in $\mathcal { M } _ { 1 }$ exploits all the harvested energy to perform task offloading. The TDMA protocol is applied to avoid interference among these users during the offloading process. Since the total offloading time of all users in $\mathcal { M } _ { 1 }$ at the nth slot cannot exceed the duration of a time slot, one has

$$
\sum_ {j \in \mathcal {M} _ {1}} t _ {j} [ n ] \leq 1, \quad n \in \mathcal {N}. \tag {9}
$$

Let $R _ { i } ^ { O }$ denote the total computation rate of the jth user in the set $\breve { \mathscr { M } } _ { 1 }$ . Then, one has

$$
R _ {j} ^ {O} = \sum_ {n = 1} ^ {N} \frac {B T t _ {j} [ n ]}{\nu_ {j} N} \log_ {2} \left(1 + \frac {h _ {j} [ n ] P _ {j} [ n ]}{\sigma_ {0} ^ {2}}\right), j \in \mathcal {M} _ {1}. \tag {10}
$$

The energy harvesting causal constraint for a user in $\mathcal { M } _ { 1 }$ can be given as

$$
\frac {T}{N} \sum_ {k = 1} ^ {n} t _ {j} [ k ] P _ {j} [ k ] \leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {j} [ k ] P _ {0}, \quad n \in \mathcal {N}, j \in \mathcal {M} _ {1}. \tag {11}
$$

Sections III and IV will respectively formulate the computation rate maximization problem for the partial and binary computation offloading modes.

# III. RESOURCE ALLOCATION UNDER THE PARTIAL COMPUTATION OFFLOADING MODE

In this section, the resource allocation problem is studied under the partial computation offloading mode. The weighted sum computation bits are maximized by jointly optimizing the CPU frequencies, the offloading times and the transmit powers of users as well as the trajectory of the UAV. In order to tackle this non-convex problem, a two-stage alternative algorithm is proposed.

# A. Resource Allocation Problem Formulation

Under the partial computation offloading mode, the weighted sum computation bits maximization problem in the UAV-enabled wireless powered MEC system is formulated as ${ \bf P } _ { 1 }$ ,

$$
\begin{array}{l} \mathbf {P} _ {1}: \max _ {f _ {m} [ n ], P _ {m} [ n ], \mathbf {q} _ {u} [ n ], t _ {m} [ n ]} \sum_ {m = 1} ^ {M} w _ {m} \\ \times \left[ \sum_ {n = 1} ^ {N} \frac {T f _ {m} [ n ]}{N C} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \right. \\ \left. \times \left(1 + \frac {h _ {m} [ n ] P _ {m} [ n ]}{\sigma_ {0} ^ {2}}\right) \right] \tag {12a} \\ \end{array}
$$

$$
\text { s.t. } C 1: f _ {m} [ n ] \geq 0, P _ {m} [ n ] \geq 0,
$$

$$
m \in \mathcal {M}, n \in \mathcal {N},
$$

$$
C 2: \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ \gamma_ {c} f _ {m} ^ {3} [ k ] + t _ {m} [ k ] P _ {m} [ k ] \right]
$$

$$
\leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0} \tag {12b}
$$

$$
m \in \mathcal {M}, \quad n \in \mathcal {N}, \tag {12c}
$$

$$
C 3: \sum_ {m = 1} ^ {M} t _ {m} [ n ] \leq 1, \quad n \in \mathcal {N}, \tag {12d}
$$

$$
C 4: \left\| \mathbf {q} _ {u} [ n + 1 ] - \mathbf {q} _ {u} [ n ] \right\| ^ {2}
$$

$$
\leq V _ {\max} \frac {T}{N}, \quad n \in \mathcal {N}, \tag {12e}
$$

$$
C 5: \mathbf {q} _ {u} [ 1 ] = \mathbf {q} _ {0}, \mathbf {q} _ {u} [ N + 1 ] = \mathbf {q} _ {F}, (1 2 f)
$$

where $V _ { \mathrm { m a x } }$ denotes the maximum speed of the UAV in the unit of meter per second; ${ \bf q } _ { 0 }$ and $\mathbf { q } _ { F }$ are the initial and final horizontal locations of the UAV, respectively. In (12), $w _ { m }$ denotes the weight of the mth user, which takes the priority and the fairness among users into consideration. C1 is the CPU frequency constraint and the computation offloading power constraint imposed on each user; C2 represents the energy harvesting causal constraint; C3 is the time constraint that the total time of all users offloading the computation bits cannot exceed the duration of each time slot; C4 and C5 are the speed constraint and the initial and final horizontal location constraint of the UAV, respectively. ${ \bf P } _ { 1 }$ is non-convex since there exist non-linear couplings among the variables, $f _ { m } [ n ] .$ , $P _ { m } [ n ] , \mathbf { q } _ { u } [ n ] , t _ { m } [ n ]$ and the objective function is non-concave with respect to the trajectory of the UAV. In order to solve it, a two-stage alternative optimization algorithm is proposed. The details for the algorithm are presented as follows.

# B. Two-Stage Alternative Optimization Algorithm

Let $z _ { m } \left[ n \right] = t _ { m } \left[ n \right] P _ { m } \left[ n \right] , n \in \mathcal { N } .$ . For a given trajectory, ${ \bf P } _ { 1 }$ can be transformed into $\mathbf { P } _ { 2 }$ .

$$
\begin{array}{l} \mathbf {P} _ {2}: \max _ {f _ {m} [ n ], z _ {m} [ n ], t _ {m} [ n ]} \sum_ {m = 1} ^ {M} w _ {m} \\ \times \left[ \sum_ {n = 1} ^ {N} \frac {T f _ {m} [ n ]}{N C} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \right. \\ \left. \times \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{t _ {m} [ n ] \sigma_ {0} ^ {2}}\right) \right] \tag {13a} \\ \begin{array}{c} \text {s.t.} C 1, C 3, \end{array} \\ \end{array}
$$

$$
C 5: \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ \gamma_ {c} f _ {m} ^ {3} [ k ] + z _ {m} [ k ] \right]
$$

$$
\leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0}, \tag {13b}
$$

$$
m \in \mathcal {M}, \quad n \in \mathcal {N}. \tag {13c}
$$

It is easy to prove that $\mathbf { P } _ { 2 }$ is convex and can be solved by using the Lagrange duality method [35], based on which the optimal solutions for the CPU frequency and the transmit power can be derived. Let $f _ { m } ^ { o p t } \left[ n \right]$ ] and $P _ { m } ^ { o p t }$ [n] denote the optimal CPU frequency and transmit power of the mth user at the nth time slot, respectively, where m $\in \mathcal { M }$ and $n \in \mathcal N$ . By solving $\mathbf { P } _ { 2 } .$ , Theorem 1 can be stated as follows.

Theorem 1: For a given trajectory ${ \bf q } _ { u } \left[ n \right] .$ , the optimal CPU frequency and transmit power of users can be respectively expressed as

$$
f _ {m} ^ {\text { opt }} [ n ] = \sqrt {\frac {w _ {m}}{3 C \gamma_ {c} \sum_ {k = n} ^ {N} \lambda_ {m , k}}}, \tag {14a}
$$

$$
P _ {m} ^ {\text { opt }} [ n ] = \left\{ \begin{array}{l l} 0, & \text { if } t _ {m} [ n ] = 0, \\ \left[ \frac {w _ {m} B}{\nu_ {m} \ln 2 \sum_ {k = n} ^ {N} \lambda_ {m , k}} - \frac {\sigma_ {0} ^ {2}}{h _ {m} [ n ]} \right] ^ {+}, & \text { otherwise }, \end{array} \right. \tag {14b}
$$

where $\lambda _ { m , n } ~ \geq ~ 0$ is the dual variable associated with the constraint $C 2 ; [ a ] ^ { + } = \operatorname* { m a x } { ( a , 0 ) }$ and max (a, 0) denotes the bigger value of a and 0.

Proof: See Appendix A.

Remark 1: It can be seen from Theorem 1 that users choose to offload their computation tasks only when the channel state information between users and the UAV is stronger than a threshold, namely, $h _ { m } \left[ n \right] \ge \left( \sigma _ { 0 } ^ { 2 } \nu _ { m } \ln 2 \sum _ { k = n } ^ { N } \lambda _ { m , k } \right) / \left( w _ { m } B \right)$ . This indicates that the user chooses to perform local com- k=n putation when the horizontal distance between the user and the UAV is larger than $\frac { \beta _ { 0 } w _ { m } B } { \sigma _ { 0 } ^ { 2 } \nu _ { m } \ln 2 \sum _ { k = n } ^ { N } \lambda _ { m , k } } - H ^ { 2 }$ . Moreover, λm,k

it can be seen that the larger the weight is, the higher the chance for the user to chooses to offload its computation task. Furthermore, users prefers to offload their computation task when the local computation frequency is very large, namely, $\begin{array} { r } { f _ { m } ^ { o p t } \left[ n \right] \ge \sqrt { \frac { \sigma _ { 0 } ^ { 2 } \nu _ { m } \ln { 2 } } { 3 C \gamma _ { c } B h _ { m } \left[ n \right] } } } \end{array}$ .

Theorem 2: If there exists a time slot that $f _ { m } ^ { o p t } \left[ n \right] = 0$ , the equation $f _ { m } ^ { o p t } \left[ k \right] = 0$ must hold, $0 \leq k \leq n .$ .

Proof: Since $\lambda _ { m , n }$ is the dual variable and $\lambda _ { m , n } \geq 0$ , from Theorem 1 $f _ { m } ^ { o p t } \left[ n \right]$ increases with n. Thus, if there exists a time slot n so that $f _ { m } ^ { o p t } \left[ n \right] = 0$ , one must have $f _ { m } ^ { o p t } \left[ k \right] = 0 .$ , for $0 \leq k \leq n$ . Theorem 2 is proved.

Remark 2: Theorem 2 indicates that the user CPU frequency increases with the time slot index. This means that the number of computation bits obtained by local computing increases with the time slot index. Moreover, the user CPU frequency increases with the weight assigned to that user since more resources are allocated to the user with a higher weight.

Theorem 3: For a given trajectory ${ \bf q } _ { u } \left[ n \right]$ , the optimal user offloading time can be obtained by solving the following equation.

$$
\log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{\sigma_ {0} ^ {2} t _ {m} [ n ]}\right) - \frac {h _ {m} [ n ] z _ {m} [ n ]}{\ln 2 \{\sigma_ {0} ^ {2} t _ {m} [ n ] + h _ {m} [ n ] z _ {m} [ n ] \}}
$$

$$
- \frac {\nu_ {m} N \alpha_ {n}}{B T} = 0. \tag {15}
$$

Remark 3: Theorem 3 can be readily proved based on the proof for Theorem 1. Thus this proof is omitted for the sake of saving space. Moreover, (15) can be solved by using the bisection method [35].

The values of the dual variables are needed in order to obtain the optimal CPU frequency, the optimal transmit power and the optimal offloading time for all users. The subgradient method in Lemma 1 can be used to tackle this problem [36].

Lemma 1: The subgradient method for obtaining the dual variables is given as

$$
\lambda_ {m, n} (l + 1) = \left[ \lambda_ {m, n} (l) - \theta (l) \Delta \lambda_ {m, n} (l) \right] ^ {+}, m \in \mathcal {M}, n \in \mathcal {N} \tag {16a}
$$

$$
\alpha_ {n} (l + 1) = \left[ \alpha_ {n} (l) - \vartheta (l) \Delta \alpha_ {n} (l) \right] ^ {+}, \quad n \in \mathcal {N}, \tag {16b}
$$

where l denotes the iteration index; $\theta \left( l \right)$ and $\vartheta \left( l \right)$ represent the iterative steps at the lth iteration. In (16), $\Delta \lambda _ { m , n } \left( l \right)$ and $\Delta \alpha _ { n } \left( l \right)$ are the corresponding subgradients, given as

$$
\begin{array}{l} \Delta \lambda_ {m, n} (l) = \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0} \\ - \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ \gamma_ {c} \left(f _ {m} ^ {l, o p t} [ k ]\right) ^ {3} + z _ {m} ^ {l, o p t} [ k ] \right], \tag {17a} \\ \end{array}
$$

$$
\Delta \alpha_ {n} (l) = 1 - \sum_ {m = 1} ^ {M} t _ {m} ^ {l, o p t} [ n ], \quad n \in \mathcal {N}, \tag {17b}
$$

where $f _ { m } ^ { l , o p t } [ n ] , z _ { m } { } ^ { l , o p t } [ n ]$ , and $t _ { m } ^ { l , o p t } \left[ n \right]$ denote the optimal solutions at the lth iterations. According to [35], the subgradient guarantees to converge to the optimal value with a very small error range.

C. Trajectory Optimization

For any given CPU frequency, transmit power, and offloading time of users, the trajectory optimization problem can be formulated as $\mathbf { P } _ { 3 } .$ .

$$
\mathbf {P} _ {3}: \max _ {\mathbf {q} _ {u} [ n ]} \sum_ {m = 1} ^ {M} w _ {m} \times \left[ \sum_ {n = 1} ^ {N} \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \right.
$$

$$
\times \left. \left(1 + \frac {\beta_ {0} P _ {m} [ n ]}{\sigma_ {0} ^ {2} (H ^ {2} + \| \mathbf {q} _ {u} [ n ] - \mathbf {q} _ {m} \| ^ {2})}\right) \right]
$$

$$
\text { s.t. } C 2: \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ \gamma_ {c} f _ {m} ^ {3} [ k ] + t _ {m} [ k ] P _ {m} [ k ] \right] \tag {18a}
$$

$$
\leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} \frac {\beta_ {0} P _ {0}}{H ^ {2} + \| \mathbf {q} _ {u} [ k ] - \mathbf {q} _ {m} \| ^ {2}}, m \in \mathcal {M},
$$

$$
n \in \mathcal {N} \tag {18b}
$$

$$
C 4 \quad \text { and } C 5. \tag {18c}
$$

Since C2 is non-convex and the objective function is non-concave with respect to ${ \bf q } _ { u } [ n ] , { \bf P } _ { 3 }$ is non-convex and we use the SCA technique to solve the optimization problem. The obtained solutions can be guaranteed to satisfy the Karush-Kuhn-Tucker (KKT) conditions of $\mathbf { P } _ { 3 } \ [ 2 7 ]$ . By using the SCA technique, Theorem 4 is given as follows.

Theorem 4: For any local trajectory $\mathbf { q } _ { u , \jmath } \left[ n \right] , n \in \mathcal { N }$ at the jth iteration, one has

$$
\sum_ {i = 1} ^ {n} \frac {P _ {0} \beta_ {0}}{H ^ {2} + \left\| \mathbf {q} _ {u} [ i ] - \mathbf {q} _ {m} \right\| ^ {2}}
$$

$$
\geq P _ {0} \beta_ {0} \overline {{{h _ {m}}}} [ n ], \tag {19a}
$$

$$
\overline {{h _ {m}}} [ n ] = \sum_ {i = 1} ^ {n} \left\{\frac {H ^ {2} + 2 \| \mathbf {q} _ {u , j} [ i ] - \mathbf {q} _ {m} \| ^ {2} - \| \mathbf {q} _ {u} [ i ] - \mathbf {q} _ {m} \| ^ {2}}{\left(H ^ {2} + \| \mathbf {q} _ {u , j} [ i ] - \mathbf {q} _ {m} \| ^ {2}\right) ^ {2}} \right\} \tag {19b}
$$

where the equality holds when $\mathbf q _ { u } \left[ n \right] = \mathbf q _ { u , \ j } \left[ n \right]$ .

Proof: Let $\begin{array} { l } { f \left( z \right) = } \end{array} \frac { a } { b + z } $ , where a and b are positive constants, and $z \geq 0$ . Since $\dot { \boldsymbol f } \left( \boldsymbol z \right)$ is convex with respect to z, the following inequality can be obtained:

$$
\frac {a}{b + z} \geq \frac {a}{b + z _ {0}} - \frac {a}{(b + z _ {0}) ^ {2}} (z - z _ {0}), \tag {20}
$$

where $z _ { \mathrm { 0 } }$ is a given local point. By using (20), Theorem 4 is proved.

In order to tackle the objective function of $\mathbf { P } _ { 3 }$ , Lemma 2 is given as follows.

[27]

Lemma 2: Using the SCA method, the following inequality can be obtained,

$$
\log_ {2} \left(1 + \frac {\beta_ {0} P _ {m} [ n ]}{\sigma_ {0} ^ {2} \left(H ^ {2} + \| \mathbf {q} _ {u} [ n ] - \mathbf {q} _ {m} \| ^ {2}\right)}\right)
$$

$$
\geq y _ {m, \jmath} \left(\left\{\mathbf {q} _ {u} [ n ] \right\}\right), \tag {21a}
$$

TABLE ITWO-STAGE ALTERNATIVE OPTIMIZATION ALGORITHM

<table><tr><td>Algorithm 1: The two-stage alternative optimization algorithm</td></tr><tr><td>1: Setting: $P_0, T, N, V_{\text{max}}, \mathbf{q}_0, \mathbf{q}_F$ , and the tolerance errors  $\xi, \xi_1$ ;2: Initialization:The iterative number  $i = 1$ ,  $\lambda_{m,n}^i$ ,  $\alpha_n^i$  and  $\mathbf{q}_u^i$  [n];3: Repeat 1:calculate  $f_m^{opt,i}$  [n] and  $P_m^{opt,i}$  [n] using Theorem 1for given  $\mathbf{q}_u^i$  [n];use the bisection method to solve (20) and obtain  $t_m^{i,opt}$  [n];update  $\lambda_{m,n}^i$  and  $\alpha_n^i$  using the subgradient algorithm;initialize the iterative number  $j = 1$ ;Repeat 2:solve  $\mathbf{P}_4$  by using CVX for the given  $f_m^{opt,i}$  [n],  $P_m^{opt,i}$  [n]and  $t_m^{i,opt}$  [n];update  $j = j + 1$ , and  $\mathbf{q}_u^j$  [n];if  $\sum_{n=1}^{N} \left\| \mathbf{q}_u^j$  [n] -  $\mathbf{q}_u^{j-1}$  [n] $\leq \xi$  $\mathbf{q}_u^i$  [n] =  $\mathbf{q}_u^j$  [n];break;endend Repeat 2update the iterative number  $i = i + 1$ ;if  $|R^i - R^{i-1}| \leq \xi_1$ break;endend Repeat 14: Obtain solutions: $f_m^{opt}$  [n],  $P_m^{opt}$  [n] and  $t_m^{opt}$  [n] and  $\mathbf{q}_u^{opt}$  [n].</td></tr></table>

$$
\begin{array}{l} y _ {m, \jmath} \left(\left\{\mathbf {q} _ {u} [ n ] \right\}\right) \\ = \log_ {2} \left(1 + \frac {\beta_ {0} P _ {m} [ n ]}{\sigma_ {0} ^ {2} \left(H ^ {2} + \| \mathbf {q} _ {u , j} [ n ] - \mathbf {q} _ {m} \| ^ {2}\right)}\right) \\ \beta_ {0} P _ {m} [ n ] \log_ {2} e \\ \left(\sigma_ {0} ^ {2} H ^ {2} + \beta_ {0} P _ {m} [ n ] + \sigma_ {0} ^ {2} \| \mathbf {q} _ {u, \jmath} [ n ] \| ^ {2}\right) \left(H ^ {2} + \| \mathbf {q} _ {u, \jmath} [ n ] \| ^ {2}\right) \\ \times \left(\| \mathbf {q} _ {u} [ n ] \| ^ {2} - \| \mathbf {q} _ {u, \jmath} [ n ] \| ^ {2}\right), \tag {21b} \\ \end{array}
$$

$$
\begin{array}{l} \beta_ {0} P _ {m} [ n ] \log_ {2} e \\ \left(\sigma_ {0} ^ {2} H ^ {2} + \beta_ {0} P _ {m} [ n ] + \sigma_ {0} ^ {2} \| \mathbf {q} _ {u, \jmath} [ n ] \| ^ {2}\right) \left(H ^ {2} + \| \mathbf {q} _ {u, \jmath} [ n ] \| ^ {2}\right) \\ \times \left(\| \mathbf {q} _ {u} [ n ] \| ^ {2} - \| \mathbf {q} _ {u, \jmath} [ n ] \| ^ {2}\right), \tag {21b} \\ \end{array}
$$

where the equality holds when $\mathbf { q } _ { u } \left[ n \right] = \mathbf { q } _ { u , \ j } \left[ n \right] .$ .

Using Theorem 4 and Lemma 2, P3 can be solved by iteratively solving the approximate problem $\mathbf { P } _ { 4 } .$ , given as

$$
\mathbf {P} _ {4}: \max _ {\mathbf {q} _ {u} [ n ]} \sum_ {m = 1} ^ {M} w _ {m} \left[ \sum_ {n = 1} ^ {N} \frac {B T t _ {m} [ n ] y _ {m , j} (\{\mathbf {q} _ {u} [ n ] \})}{\nu_ {m} N} \right] \tag {22a}
$$

s.t. C4 and C5, (22b)

$$
\sum_ {k = 1} ^ {n} \left[ \gamma_ {c} f _ {m} ^ {3} [ k ] + t _ {m} [ k ] P _ {m} [ k ] \right] \leq \eta_ {0} P _ {0} \beta_ {0} \overline {{h _ {m}}} [ n ],
$$

$$
m \in \mathcal {M}, n \in \mathcal {N}. \tag {22c}
$$

It can be seen that $\mathbf { P } _ { 4 }$ is convex and can be readily solved by using CVX [4]. By solving $\mathbf { P } _ { 2 }$ and $\mathbf { P } _ { 4 }$ , a two-stage alternative optimization algorithm denoted by Algorithm 1 is further developed to solve ${ \bf P } _ { 1 }$ . The details for Algorithm 1 can be found in Table I. In Table I, $R ^ { i }$ denotes the value of the objective function of $\mathbf { P } _ { 1 }$ at the ith iteration.

# IV. RESOURCE ALLOCATION IN BINARY COMPUTATION OFFLOADING MODE

In this section, the weighted sum computation bits maximization problem is studied in the UAV-enabled wireless powered MEC system under the binary computation offloading mode. The CPU frequencies of the users that choose to perform local computation, the offloading times, the transmit powers of users that choose to perform task offloading, the trajectory of the UAV, and the mode selection are jointly optimized to maximize the weighted sum computation bits of all users. The formulated problem is a mixed integer non-convex optimization problem, for which a three-stage alternative optimization problem is proposed.

# A. Resource Allocation Problem Formulation

Under the binary computation offloading mode, the weighted sum computation bit maximization problem subject to the energy harvesting causal constraints, the UAV speed and position constraints is formulated as $\mathbf { P } _ { 5 }$ ,

$$
\begin{array}{l} \mathbf {P} _ {5}: \max _ {f _ {i} [ n ], P _ {j} [ n ], q [ n ], t _ {j} [ n ], \mathcal {M} _ {0}, \mathcal {M} _ {1}} \sum_ {i \in \mathcal {M} _ {0}} \sum_ {n = 1} ^ {N} w _ {i} \frac {f _ {i} [ n ] T}{C N} \\ + \sum_ {j \in \mathcal {M} _ {1}} \frac {w _ {j} B T}{\nu_ {j} N} \sum_ {n = 1} ^ {N} t _ {j} [ n ] \log_ {2} \\ \times \left(1 + \frac {h _ {j} [ n ] P _ {j} [ n ]}{\sigma_ {0} ^ {2}}\right) \tag {23a} \\ \end{array}
$$

$$
\text { s.t. } \frac {T}{N} \sum_ {k = 1} ^ {n} \gamma_ {c} f _ {i} ^ {3} [ k ] \leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {i} [ k ] P _ {0},
$$

$$
n \in \mathcal {N}, i \in \mathcal {M} _ {0}, \tag {23b}
$$

$$
\frac {T}{N} \sum_ {k = 1} ^ {n} t _ {j} [ k ] P _ {j} [ k ] \leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {j} [ k ] P _ {0},
$$

$$
n \in \mathcal {N}, j \in \mathcal {M} _ {1}, \tag {23c}
$$

$$
\sum_ {j \in \mathcal {M} _ {1}} t _ {j} [ n ] \leq 1, \quad n \in \mathcal {N}, \tag {23d}
$$

$$
\mathcal {M} = \mathcal {M} _ {0} \cup \mathcal {M} _ {1}, \quad \mathcal {M} _ {0} \cap \mathcal {M} _ {1} = \Theta , \tag {23e}
$$

$$
f _ {i} [ n ] \geq 0, P _ {j} [ n ] \geq 0, i \in \mathcal {M} _ {0}, j \in \mathcal {M} _ {1}, \tag {23f}
$$

$$
C 4 \quad \text { and } C 5. \tag {23g}
$$

(23b) and (23c) are the energy harvesting causal constraints imposed on these users who choose to perform local computation and on these users who choose to perform task offloading, respectively; (23d) is the offloading time constraint during each slot and (23e) is the user operation selection constraint. In $\mathbf { P } _ { 5 }$ there exist close couplings among different optimization variables. Furthermore, the binary user operation mode selection makes $\mathbf { P } _ { 5 }$ a mixed integer programming problem. The exhaustive search method leads to a prohibitively high computational complexity, especially when there exist a large number of users. Motivated by how we solve $\mathbf { P } _ { 1 } , \mathbf { P } _ { 5 }$ has a similar structure as ${ \bf P } _ { 1 }$ when the operation modes of users are determined. Thus, the optimal CPU frequency, transmit power, and offloading time of users can be obtained by using the same method as the one used for $\mathrm { P _ { 1 } }$ and the trajectory optimization for the UAV can also be achieved by using the SCA method. As such, a three-stage alternative optimization algorithm is proposed based on the two-stage Algorithm 1. The details for the algorithm are presented as follows.

# B. Three-Stage Alternative Optimization Algorithm

In order to efficiently solve $\mathbf { P } _ { 5 }$ , a binary variable denoted by $\rho _ { m }$ is introduced, where $\rho _ { m } ~ \in ~ \{ 0 , 1 \}$ and $m \in \mathcal { M }$ . $\rho _ { m } = 0$ indicates that the mth user performs local computation mode while $\rho _ { m } = 1$ means that the mth user performs task offloading. Moreover, the user operation selection indicator variable $\rho _ { m }$ is relaxed as a sharing factor $\rho _ { m } \in [ 0 , 1 ]$ . Thus, $\mathbf { P } _ { 5 }$ can be rewritten as

$$
\begin{array}{l} \mathbf {P} _ {6}: \max _ {f _ {m} [ n ], P _ {n} [ n ], \mathbf {q} [ n ], t _ {m} [ n ], \rho_ {m}} \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} w _ {m} \left\{(1 - \rho_ {m}) \frac {f _ {m} [ n ] T}{C N} \right. \\ \left. + \frac {B T t _ {m} [ n ] \rho_ {m}}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] P _ {m} [ n ]}{\sigma_ {0} ^ {2}}\right) \right\} \tag {24a} \\ \end{array}
$$

$$
\text { s.t. } (1 - \rho_ {m}) \frac {T}{N} \sum_ {k = 1} ^ {n} \gamma_ {c} f _ {m} ^ {3} [ k ] + \rho_ {m} \frac {T}{N}
$$

$$
\times \sum_ {k = 1} ^ {n} t _ {m} [ k ] P _ {m} [ k ]
$$

$$
\leq \frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0}, \quad m \in \mathcal {M}, \tag {24b}
$$

$$
\sum_ {m = 1} ^ {M} \rho_ {m} t _ {m} [ n ] \leq 1, \quad n \in \mathcal {N}, \tag {24c}
$$

$$
f _ {m} [ n ] \geq 0, P _ {m} [ n ] \geq 0, n \in \mathcal {N}, m \in \mathcal {M}, \tag {24d}
$$

C4 and C5. (24e)

Even by relaxing the binary variable $\rho _ { m } , { \bf P } _ { 6 }$ is still difficult to solve as there exist couplings among different variables. For any given $\rho _ { m }$ and the trajectory of the UAV, $\mathbf { P } _ { 6 }$ has a similar structure as $\mathbf { P } _ { 1 }$ . Thus, using the same techniques applied to ${ \bf P } _ { 1 }$ , the optimal CPU frequency, transmit power and offloading time of users for a given $\rho _ { m }$ and the UAV trajectory can be obtained. It is easy to verify that the optimal CPU frequency, transmit power and offloading time of users for a given trajectory have the same forms given by Theorem 1 and Theorem 3.

Theorem 5: For any given $f _ { m } [ n ] , P _ { m } [ n ] , t _ { m } [ n ]$ and ${ \bf q } _ { u } \left[ n \right]$ , the user operation selection scheme can be obtained by

$$
\rho_ {m} ^ {\text { opt }} = \left\{ \begin{array}{l l} 0 & \text { if } G _ {1} \geq G _ {2}, \\ 1 & \text { otherwise }; \end{array} \right. \tag {25a}
$$

$$
G _ {1} = \sum_ {n = 1} ^ {N} \left\{\frac {w _ {m} f _ {m} [ n ]}{C} - v _ {m, n} \sum_ {k = 1} ^ {n} \gamma_ {c} f _ {m} ^ {3} [ k ] \right\}, \tag {25b}
$$

$$
\begin{array}{l} G _ {2} = \sum_ {n = 1} ^ {N} \left\{\frac {B t _ {m} [ n ]}{\nu_ {m}} \log_ {2} \left(1 + \frac {h _ {m} [ n ] P _ {m} [ n ]}{\sigma_ {0} ^ {2}}\right) \right. \\ \left. - v _ {m, n} \sum_ {k = 1} ^ {n} t _ {m} [ k ] P _ {m} [ k ] - \frac {N}{T} \varepsilon_ {n} t _ {m} [ n ] \right\}, \tag {25c} \\ \end{array}
$$

where $v _ { m , n } \geq 0$ and $\varepsilon _ { n } \geq 0$ are the dual variables associated with the constraints given by (24b) and (24c), respectively.

Proof: See Appendix B.

Remark 4: Theorem 5 indicates that the user operation selection scheme depends on the tradeoff between the achievable computation rate and the operation cost. If the tradeoff of the user achieved by local computing is better than that obtained by task offloading, the user chooses to perform local computing; otherwise, the user chooses to offload its computation tasks to the UAV for computing.

Finally, the trajectory optimization for any given $\rho _ { m } , f _ { m } \left[ n \right]$ , $P _ { m } \left[ n \right]$ and $t _ { m }$ [n] can be obtained by solving $\mathbf { P } _ { 7 } ,$ , given as

$$
\mathbf {P} _ {7}: \max _ {\mathbf {q} _ {u} [ n ]} \sum_ {m = 1} ^ {M} w _ {m} \rho_ {m} \left[ \sum_ {n = 1} ^ {N} \frac {B T t _ {m} [ n ] y _ {m , j} (\{\mathbf {q} _ {u} [ n ] \})}{\nu_ {m} N} \right] \tag {26a}
$$

${ \mathrm { s . t . ~ } } C 4 \ { \mathrm { ~ \ a n d ~ } } C 5 ,$ (26b)

$$
\begin{array}{l} \left(1 - \rho_ {m}\right) \sum_ {k = 1} ^ {n} \gamma_ {c} f _ {m} ^ {3} [ k ] + \rho_ {m} \sum_ {k = 1} ^ {n} t _ {m} [ k ] P _ {m} [ k ] \\ \leq \eta_ {0} P _ {0} \beta_ {0} \overline {{h _ {m}}} [ n ], \quad m \in \mathcal {M}, n \in \mathcal {N}, \tag {26c} \\ \end{array}
$$

where $\overline { { h _ { m } } } \left[ n \right]$ and $y _ { j } \left( \{ \mathbf { q } _ { u } \left[ n \right] \} \right)$ are given by (19b) and (21b), respectively. $\mathbf { P } _ { 7 }$ is convex and can be efficiently solved by using CVX [4]. Based on Theorem 1, Theorem 5 and the solutions of $\mathbf { P } _ { 7 }$ , a three-stage alternative optimization algorithm denoted by Algorithm 2 is proposed to solve $\mathbf { P } _ { 5 }$ . The details for Algorithm 2 are presented in Table 2. In Table 2, $R ^ { l }$ and $R ^ { i }$ denote the value of the objective function of $\mathbf { P } _ { 5 }$ at the lth and i iteration, respectively.

# C. Complexity Analysis

The complexity of Algorithm 1 comes from four aspects. The first aspect is from the computation of the CPU frequency and the offloading power. The second aspect is from the bisection method for obtaining the offloading time. The third aspect is from the subgradient method for computing the dual variables. The fourth aspect comes from the application of CVX for solving $\mathrm { P } _ { 4 }$ . Let $L _ { 1 }$ and $L _ { 2 }$ denote the number of iterations required for the outer loop and the inner loop of Algorithm 1, respectively. Let $\ell _ { 1 }$ and $\ell _ { 2 }$ denote the tolerance error for the bisection method and the subgradient method, respectively. Thus, according to the works in [35], [38], and [39], the total complexity of Algorithm 1 is $\mathcal { O } \left[ L _ { 1 } \left( 2 M N + M \log _ { 2 } { ( \ell _ { 1 } / T ) } + 1 / \ell _ { 2 } ^ { 2 } + \dot { L } _ { 2 } N ^ { 3 } \right) \right]$ and $\mathcal { O } \left( \cdot \right)$ is the big-O notation [35].

The complexity of Algorithm 2 comes from five aspects. Four aspects are the same as these of Algorithm 1. The fifth aspect is from the computation of the operation selection indicator variable $\rho _ { m }$ . Let $L _ { 1 } , L _ { 2 }$ and $L _ { 3 }$ denote the number of iterations required for the first, second and third loop of Algorithm 2, respectively. Similar to the complexity analysis for Algorithm 1, the total complexity of Algorithm 2 is $\mathcal { O } \left[ L _ { 1 } \breve { L } _ { 2 } \left( 2 M N + M + M \log _ { 2 } \breve { ( \ell _ { 1 } / T ) } + 1 / \ell _ { 2 } ^ { 2 } \breve { + } L _ { 3 } N ^ { 3 } \right) \right]$ .

TABLE II THREE-STAGE ALTERNATIVE OPTIMIZATION ALGORITHM 

<table><tr><td>Algorithm 2: The three-stage alternative optimization algorithm</td></tr><tr><td>1: Setting: $P_0, T, N, V_{\text{max}}, \mathbf{q}_0, \mathbf{q}_F$ , and the tolerance errors  $\xi, \xi_1$  and  $\xi_2$ ;2: Initialization:The iterative number  $i = 1$ ,  $v_{m,n}^i$  and  $\varepsilon_n^i$ , and  $\mathbf{q}_u^i [n]$ ;3: Repeat 1:initialize the iterative number  $l = 1$  and  $\rho_m^l$ ;Repeat 2:calculate  $f_m^{opt,i}[n]$  and  $P_m^{opt,i}[n]$  using Theorem 1for given  $\mathbf{q}_u^i [n]$  and  $\rho_m^{opt,l}$ ;use the bisection method to solve (20) and obtain  $t_m^{i,opt}[n]$ ;update  $v_{m,n}^i$  and  $\varepsilon_n^i$  using the subgradient algorithm;calculate  $\rho_m^{opt,l}$  using Theorem 5 and update  $l = l + 1$ ;if  $|R^l - R^{l-1}| \leq \xi$ break;endinitialize the iterative number  $j = 1$ ;Repeat 3:solve P7 by using CVX for the given  $f_m^{opt,i}[n], P_m^{opt,i}[n]$ ,  $t_m^{i,opt}[n]$  and  $\rho_m^{opt,l}$ ;update  $j = j + 1$ , and  $\mathbf{q}_u^j [n]$ ;if  $\sum_{n=1}^{N} \left\| \mathbf{q}_u^j [n] - \mathbf{q}_u^{j-1}[n] \right\| \leq \xi$  $\mathbf{q}_u^i [n] = \mathbf{q}_u^j [n]$ ;break;endend Repeat 3update the iterative number  $i = i + 1$ ;if  $|R^i - R^{i-1}| \leq \xi_1$ break;endend Repeat 2end Repeat 14: Obtain solutions: $f_m^{opt}[n], P_m^{opt}[n]$  and  $t_m^{opt}[n], \rho_m^{opt}$  and  $\mathbf{q}_u^{opt}[n]$ .</td></tr></table>

# V. SIMULATION RESULTS

In this section, simulation results are presented to compare the performance of our proposed designs with that of other benchmark schemes. The convergence performance of the proposed algorithms is also evaluated. The simulation settings are based on the works in [7], [14], [16], and [23]. The positions of users are set as: $\mathbf { q } _ { 1 } ~ = ~ [ 0 , 0 ] , ~ \mathbf { q } _ { 2 } ~ = ~ [ 0 , 1 0 ]$ , ${ \bf q } _ { 3 } = [ 1 0 , 1 0 ] , { \bf q } _ { 4 } = [ 1 0 , 0 ]$ . The detailed settings are given in Table III. The weight vector of each user $[ w _ { 1 } \ w _ { 2 } \ w _ { 3 } \ w _ { 4 } ]$ is set as [0.1 0.4 0.3 0.2].

Fig. 3 shows the UAV trajectory under different schemes with $T \ = \ 2$ seconds. The UAV transmit power is set as $P _ { 0 } = 0 . 1 \mathrm { { \small ~ W } } .$ In the constant speed scenario, the UAV flies straight with a constant speed from the initial position to the final position. In the semi-circle scenario, the UAV flies along the trajectory that is a semi-circle with its diameter being $\| \mathbf { q } _ { F } - \mathbf { q } _ { 0 } \|$ . The trajectory of the offloading mode is obtained by using Algorithm 1 for the partial computation offloading mode and the trajectory of the binary mode is obtained by using Algorithm 2 for the binary computation offloading mode. It can be seen from the trajectories of our proposed schemes the UAV is always close to user 2 and user 3, irrespective of the operation modes. The reason is that the weights of user 2 and user 3 are larger than these of user 1 and user 4. Thus, the UAV needs to fly close to user 2 and user 3 so as to provide more energy to them. This indicates that the priority and the fairness among users can be obtained by using the weight vector.

TABLE III SIMULATION PARAMETERS 

<table><tr><td>Parameters</td><td>Notation</td><td>Typical Values</td></tr><tr><td>Numbers of Users</td><td>M</td><td>4</td></tr><tr><td>The height of the UAV</td><td>H</td><td>10 m</td></tr><tr><td>The time length of the UAV flying</td><td>T</td><td>2 sec</td></tr><tr><td>Numbers of CPU cycles</td><td>C</td><td> $10^{3}$ cycles/bit</td></tr><tr><td>Energy conversation efficiency</td><td> $\eta_0$ </td><td>0.8</td></tr><tr><td>Communication bandwidth</td><td>B</td><td>40 MHz</td></tr><tr><td>The receiver noise power</td><td> $\sigma_0^2$ </td><td> $10^{-9}$ W</td></tr><tr><td>The number of time slots</td><td>N</td><td>50</td></tr><tr><td>The effective switched capacitance</td><td> $\gamma_c$ </td><td> $10^{-28}$ </td></tr><tr><td>The channel power gain</td><td> $\beta_0$ </td><td>-50 dB</td></tr><tr><td>The tolerance error</td><td> $\xi, \xi_1$ </td><td> $10^{-4}$ </td></tr><tr><td>The initial position of the UAV</td><td> $\mathbf{q}_0$ </td><td>[0, 0]</td></tr><tr><td>The final position of the UAV</td><td> $\mathbf{q}_F$ </td><td>[10, 0]</td></tr><tr><td>The maximum speed of the UAV</td><td> $V_{\text{max}}$ </td><td>20 m/s</td></tr></table>

![](images/b95f678a634acdc3e93bfcd0047206bf94287c9affd168463301f0844c94c6f7.jpg)

<details>
<summary>line</summary>

| User   | x (m) | y (m) |
|--------|-------|-------|
| User 1 | 0     | 0     |
| User 1 | 2     | 4     |
| User 1 | 4     | 5     |
| User 1 | 6     | 5     |
| User 1 | 8     | 4     |
| User 1 | 10    | 0     |
| User 2 | 0     | 0     |
| User 2 | 2     | 8     |
| User 2 | 4     | 7     |
| User 2 | 6     | 9     |
| User 2 | 8     | 9     |
| User 2 | 10    | 10    |
| User 3 | 0     | 0     |
| User 3 | 2     | 8     |
| User 3 | 4     | 7     |
| User 3 | 6     | 9     |
| User 3 | 8     | 9     |
| User 3 | 10    | 10    |
| User 4 | 0     | 0     |
| User 4 | 2     | 4     |
| User 4 | 4     | 3     |
| User 4 | 6     | 5     |
| User 4 | 8     | 3     |
| User 4 | 10    | 0     |
| A semi-circle | 0   | 0     |
| A semi-circle | 2   | 4     |
| A semi-circle | 4   | 5     |
| A semi-circle | 6   | 5     |
| A semi-circle | 8   | 3     |
| A semi-circle | 10   | 0     |
| The binary mode | 0   | 0     |
| The binary mode | 2   | 4     |
| The binary mode | 4   | 5     |
| The binary mode | 6   | 5     |
| The binary mode | 8   | 4     |
| The binary mode | 10   | 0     |
| A constant speed | 0   | 0     |
| A constant speed | 2   | 4     |
| A constant speed | 4   | 3     |
| A constant speed | 6   | 5     |
| A constant speed | 8   | 3     |
| A constant speed | 10   | 0     |
The offloading mode
The offloading mode
A semi-circle
The offloading mode
The offloading mode
A constant speed
</details>

Fig. 3. The trajectory of the UAV under different schemes with T = 2 seconds.

Fig. 4 shows the weighted sum computation bits of all users versus the transmit power of the UAV under different schemes. The optimal local computing is the mode that all users only perform local computing while the optimal offloading mode is that all users only perform task offloading. And the trajectory of the UAV is jointly optimized under these two benchmark schemes. The results under the binary mode and the partial offloading mode are obtained by using Algorithm 2 and Algorithm 1, respectively. In Fig. 4 the weighted sum computation bits achieved under the partial offloading mode is the largest among these obtained by other schemes. The reason is that all the users can dynamically select the operation mode based on the quality of the channel state information under the partial computation offloading mode. Moreover, the optimal offloading mode outperforms the optimal local computing. This result is consistent with the results obtained in [13]. Furthermore, the weighted sum computation bits of all users increase with the UAV transmit power. It can be explained by the fact that the harvesting energy increases with the transmit power of the UAV. Thus, users have more energy to perform local commutating or task offloading.

![](images/19d9b44eb036f7cece36ccdf09631c149768285a72895a2ae62d9f147aa48d66.jpg)

<details>
<summary>line</summary>

| The transmit power of the UAV (W) | Optimal local computing | Optimal offloading | The binary mode | The partial offloading mode |
| --------------------------------- | ------------------------ | ------------------ | --------------- | --------------------------- |
| 0.1                               | 1.0                      | 1.2                | 1.5             | 1.6                         |
| 0.2                               | 1.3                      | 1.5                | 1.7             | 1.8                         |
| 0.3                               | 1.6                      | 1.8                | 1.9             | 2.0                         |
| 0.4                               | 1.9                      | 2.1                | 2.2             | 2.3                         |
| 0.5                               | 2.2                      | 2.4                | 2.5             | 2.6                         |
| 0.6                               | 2.5                      | 2.7                | 2.8             | 2.9                         |
| 0.7                               | 2.8                      | 3.0                | 3.1             | 3.2                         |
| 0.8                               | 3.1                      | 3.3                | 3.4             | 3.5                         |
| 0.9                               | 3.4                      | 3.6                | 3.7             | 3.8                         |
| 1.0                               | 3.7                      | 3.9                | 4.0             | 4.1                         |
</details>

Fig. 4. The weighted sum computation bits of all users versus the transmit power of the UAV under different schemes.

Fig. 5 shows the weighted sum computation bits of all the users versus the transmit power of the UAV under different trajectories with the partial computation offloading mode and the binary computation offloading mode. As shown in Fig. 5, the weighted sum computation bits of all the users achieved by using our proposed schemes are larger than that obtained by using the trajectory with a constant speed and than that obtained by using the semi-circle trajectory, irrespective of the operation modes. This indicates that the optimization of the trajectory of the UAV can improve the weighted sum computation bits. It also verifies that our proposed resource allocation scheme outperforms the disjoint optimization schemes.

Fig. 6 shows the total computation bits of each user under different operation modes. The transmit power of the UAV is set as $P _ { 0 } = 0 . 1 ~ \mathrm { W }$ . The total computation bits of user 2 and user 3 are higher than those of user 1 and user 4. The reason is that the weights of user 2 and user 3 are larger than those of user 1 and user 4. Thus, the resource allocation scheme should consider the priority of user 2 and user 3. This further verifies that the application of the weight vector can improve the priority and also the fairness of users.

Fig. 7 is given to verify the efficiency of our proposed Algorithm 1 and Algorithm 2. The transmit power of the UAV is given as 0.1 W or 0.2 W. The results show that Algorithm 1 and Algorithm 2 only need several iterations to converge. This indicates that the proposed Algorithm 1 and Algorithm 2 are computationally effective and have a fast convergence rate. It can also be seen that the weighted sum computation bits of all the users achieved under the partial computation offloading mode are larger than those obtained under the binary computation offloading mode. The reason is that users can simultaneously perform local computing and task offloading when the channel state information is strong under the partial computation offloading mode. However, users can only perform either local computing or task offloading in the binary offloading mode even when the channel state information is strong. The computation performance is improved by the flexible selection of the operation mode based on the channel state information.

![](images/d72cb0216ed6076953e6d31d231a90fb46818c1dc641049271ae96b0b9e7829e.jpg)

<details>
<summary>line</summary>

| The transmit power of the UAV (W) | The partial offloading mode | The partial offloading mode with the semi-circle trajectory | The partial offloading mode with a constant speed |
| --------------------------------- | ---------------------------- | ------------------------------------------------------------- | -------------------------------------------------- |
| 0.1                               | 1.5e7                        | 1.3e7                                                         | 1.2e7                                              |
| 0.2                               | 1.8e7                        | 1.6e7                                                         | 1.4e7                                              |
| 0.3                               | 2.0e7                        | 1.8e7                                                         | 1.6e7                                              |
| 0.4                               | 2.3e7                        | 2.0e7                                                         | 1.9e7                                              |
| 0.5                               | 2.6e7                        | 2.3e7                                                         | 2.2e7                                              |
| 0.6                               | 2.9e7                        | 2.6e7                                                         | 2.5e7                                              |
| 0.7                               | 3.2e7                        | 2.9e7                                                         | 2.8e7                                              |
| 0.8                               | 3.5e7                        | 3.2e7                                                         | 3.1e7                                              |
| 0.9                               | 3.9e7                        | 3.6e7                                                         | 3.5e7                                              |
| 1.0                               | 4.2e7                        | 3.9e7                                                         | 3.8e7                                              |
</details>

![](images/65b0b9fe963d851cf83a7b99d1eabdb8f17944a6c003a086727dd31f88c7a154.jpg)

<details>
<summary>line</summary>

| The transmit power of the UAV (W) | The binary mode with joint optimization | The binary mode with the semi-circle trajectory | The binary mode with a constant speed |
| --------------------------------- | ---------------------------------------- | -------------------------------------------------- | -------------------------------------- |
| 0.1                               | 1.5e7                                    | 1.3e7                                              | 1.2e7                                  |
| 0.2                               | 1.7e7                                    | 1.5e7                                              | 1.4e7                                  |
| 0.3                               | 1.9e7                                    | 1.7e7                                              | 1.6e7                                  |
| 0.4                               | 2.2e7                                    | 1.95e7                                             | 1.8e7                                  |
| 0.5                               | 2.5e7                                    | 2.25e7                                             | 2.1e7                                  |
| 0.6                               | 2.8e7                                    | 2.55e7                                             | 2.4e7                                  |
| 0.7                               | 3.1e7                                    | 2.85e7                                             | 2.7e7                                  |
| 0.8                               | 3.4e7                                    | 3.15e7                                             | 3.0e7                                  |
| 0.9                               | 3.8e7                                    | 3.55e7                                             | 3.4e7                                  |
| 1.0                               | 4.1e7                                    | 3.85e7                                             | 3.7e7                                  |
</details>

Fig. 5. (a) The weighted sum computation bits of all users versus the transmit power of the UAV under different trajectories with the partial computation offloading mode; (b) The weighted sum computation bits of all users versus the transmit power of the UAV under different trajectories with the binary computation offloading mode.

Fig. 8 shows the weighted sum computation bits of all users versus the number of users under different operation modes. The transmit power of the UAV is set as $P _ { 0 } = 0 . 2 \ : \mathrm { W }$ or $P _ { 0 } =$ 0.4 W. In Fig. 8 the weighted sum computation bits of all users increase with the number of users. The reason is that more users can exploit the harvesting energy to perform local computing and computation offloading. It is also observed that the growth rate decreases with the increase of the number of users. The reason is that the offloading time allocated for each user decreases with the increase of the number of users since the total offloading time is limited by T .

TABLE IV COMPARISON OF THE REQUIRED RUN TIME OF ALGORITHM 1 WITH THAT OF ALGORITHM 2 (S) 

<table><tr><td>Algorithms $\frac{(N,M)}{ }$ </td><td>(50,2)</td><td>(50,4)</td><td>(50,8)</td><td>(60,2)</td><td>(60,4)</td><td>(60,8)</td><td>(70,2)</td><td>(70,4)</td><td>(70,8)</td></tr><tr><td>Algorithm 1</td><td>43.72</td><td>104.54</td><td>186.38</td><td>154.74</td><td>198.65</td><td>235.85</td><td>224.74</td><td>291.53</td><td>352.72</td></tr><tr><td>Algorithm 2</td><td>89.35</td><td>167.17</td><td>265.46</td><td>223.19</td><td>275.42</td><td>321.87</td><td>308.56</td><td>388.92</td><td>468.39</td></tr></table>

![](images/70309ee5e7da99e006f7d2cc17fcc736455d7c06df1e2bd43ccf655600c1c569.jpg)

<details>
<summary>bar</summary>

| Users | The binary mode (Bits) | The partial offloading mode (Bits) |
| :--- | :--- | :--- |
| User 1 | 1500000 | 1550000 |
| User 2 | 6100000 | 6300000 |
| User 3 | 4550000 | 4750000 |
| User 4 | 3050000 | 3150000 |
</details>

Fig. 6. The total computation bits of each user under different operation modes with $P _ { 0 } = 0 . 1$ W.

![](images/2aa92a4207e0d6c36980656775ff8ce3e3171bcdae0ca5d2c22815e5cf1b16d0.jpg)

<details>
<summary>line</summary>

| The number of iterations | P₀=0.2 W, Algorithm 1 | P₀=0.2 W, Algorithm 2 | P₀=0.1 W, Algorithm 1 | P₀=0.1 W, Algorithm 2 |
| ------------------------ | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| 2                        | 2.55                   | 2.65                   | 2.45                   | 2.40                   |
| 4                        | 2.10                   | 2.45                   | 2.05                   | 2.00                   |
| 6                        | 1.90                   | 2.20                   | 1.85                   | 1.80                   |
| 8                        | 1.80                   | 1.95                   | 1.70                   | 1.65                   |
| 10                       | 1.78                   | 1.80                   | 1.60                   | 1.55                   |
| 12                       | 1.78                   | 1.75                   | 1.60                   | 1.55                   |
| 14                       | 1.78                   | 1.75                   | 1.60                   | 1.55                   |
| 16                       | 1.78                   | 1.75                   | 1.60                   | 1.55                   |
| 18                       | 1.78                   | 1.75                   | 1.60                   | 1.55                   |
| 20                       | 1.78                   | 1.75                   | 1.60                   | 1.55                   |
</details>

Fig. 7. The weighted sum computation bits of all users versus the number of iterations required by using Algorithms 1 and 2 under different transmit powers of the UAV and different operation modes.

Table IV is given to evaluate the run times of Algorithm 1 and Algorithm 2 shown in the top of the next page. The run times are obtained by using a computer with 64-bit Intel(R) Core(TM) i7-4790 CPU, 8 GB RAM. From Table IV we can see that the required run time of Algorithm 1 is smaller than that of Algorithm 2. This indicates that the complexity of Algorithm 1 is lower than that of Algorithm 2. It can be verified by the complexity analysis presented in Subsection C of Section IV. Moreover, the effect of the number of time slots on the run time is larger than that of the number of users. The reason is that the complexity of these two algorithms mainly depends on the number of time slots. This can also be verified by the complexity analysis.

![](images/9460574ab95c8dcbf8a9e03d03ac04c2c14548bdd36c9f70400b8fbea42ebb61.jpg)

<details>
<summary>line</summary>

| The number of users | The partial offloading mode, P₀=0.4 W | The binary mode, P₀=0.4 W | The partial offloading mode, P₀=0.2 W | The binary mode, P₀=0.2 W |
| ------------------- | -------------------------------------- | ------------------------- | -------------------------------------- | ------------------------- |
| 2                   | 1.6e7                                  | 1.5e7                     | 1.3e7                                  | 1.2e7                     |
| 4                   | 2.3e7                                  | 2.2e7                     | 1.8e7                                  | 1.7e7                     |
| 6                   | 3.0e7                                  | 2.9e7                     | 2.4e7                                  | 2.3e7                     |
| 8                   | 3.3e7                                  | 3.1e7                     | 2.7e7                                  | 2.5e7                     |
| 10                  | 3.5e7                                  | 3.3e7                     | 2.9e7                                  | 2.8e7                     |
| 12                  | 3.6e7                                  | 3.5e7                     | 3.1e7                                  | 3.0e7                     |
</details>

Fig. 8. The weighted sum computation bits of all users versus the number of users under different transmit powers of the UAV and different operation modes.

# VI. CONCLUSIONS

The resource allocation problems were studied for UAV-enabled wireless powered MEC systems under both the partial and binary computation offloading modes. The weighted sum computation rates of users were maximized by jointly optimizing the CPU frequencies, the user offloading times, the user transmit powers, and the UAV trajectory. Two alternative algorithms were proposed to solve these challenging problems. The closed-form expressions for the optimal CPU frequencies, user offloading times, and user transmit power were derived. Moreover, the optimal selection scheme whether users choose to locally compute or offload tasks was proposed for the binary computation offloading mode. It was shown that the performance achieved by using our proposed resource allocation scheme is superior to these obtained by using the disjoint optimization schemes. Simulation results also verified the efficiency of our proposed alternative algorithms and our theoretical analysis.

$$
\begin{array}{l} \mathcal {L} (\Xi) = \sum_ {m = 1} ^ {M} w _ {m} \left[ \sum_ {n = 1} ^ {N} \frac {f _ {m} [ n ]}{C} \frac {T}{N} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{\sigma_ {0} ^ {2} t _ {m} [ n ]}\right) \right] \\ + \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \lambda_ {m, n} \left\{\frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0} - \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ \gamma_ {c} f _ {m} ^ {3} [ k ] + z _ {m} [ k ] \right] \right\} + \sum_ {n = 1} ^ {N} \alpha_ {n} \left\{1 - \sum_ {m = 1} ^ {M} t _ {m} [ n ] \right\}, \tag {27} \\ \end{array}
$$

$$
\mathcal {L} (\Xi) = \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} w _ {m} \left\{\frac {T}{N} \frac {f _ {m} [ n ]}{C} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{\sigma_ {0} ^ {2} t _ {m} [ n ]}\right) \right\} + \mu_ {m, n} g _ {m} [ k ] + \frac {\alpha_ {n}}{M} - \alpha_ {n} t _ {m} [ n ]. \tag {28}
$$

$$
\max _ {\lambda_ {m, n}, \alpha_ {n}, f _ {m} [ n ] \geq 0} \mathcal {L} _ {m} \left(\lambda_ {m, n}, \alpha_ {n}, f _ {m} [ n ], z _ {m} [ n ], t _ {m} [ n ]\right) \tag {31a}
$$

$$
\mathcal {L} _ {m} \left(\lambda_ {m, n}, \alpha_ {n}, f _ {m} [ n ], z _ {m} [ n ], t _ {m} [ n ]\right) \tag {31b}
$$

$$
= \sum_ {n = 1} ^ {N} \left\{w _ {m} \left\{\frac {T}{N} \frac {f _ {m} [ n ]}{C} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{\sigma_ {0} ^ {2} t _ {m} [ n ]}\right) \right\} + \mu_ {m, n} g _ {m} [ n ] + \frac {\alpha_ {n}}{M} - \alpha_ {n} t _ {m} [ n ] \right\}. \tag {31c}
$$

$$
\begin{array}{l} \mathcal {L} _ {1} \left(\Xi_ {1}\right) = \sum_ {m = 1} ^ {M} w _ {m} \left[ \left(1 - \rho_ {m}\right) \sum_ {n = 1} ^ {N} \frac {f _ {m} [ n ]}{C} \frac {T}{N} + \frac {B T \rho_ {m} t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{t _ {m} [ n ] \sigma_ {0} ^ {2}}\right) \right] \\ + \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} v _ {m, n} \left\{\frac {\eta_ {0} T}{N} \sum_ {k = 1} ^ {n} h _ {m} [ k ] P _ {0} - \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ (1 - \rho_ {m}) \gamma_ {c} f _ {m} ^ {3} [ k ] + \rho_ {m} z _ {m} [ k ] \right] \right\} \\ + \sum_ {n = 1} ^ {N} \varepsilon_ {n} \left\{1 - \sum_ {m = 1} ^ {M} \rho_ {m} t _ {m} [ n ] \right\}, \tag {33} \\ \end{array}
$$

The exploitation of UAV to improve the energy conversation efficiency and the computation performance was studied in this paper. However, the computation performance is also limited by the flight time of the UAV. It is interesting to exploit multiple antennas techniques to tackle this challenge. This will be investigated in our future work.

# APPENDIX A PROOF OF THEOREM 1

Let $\lambda _ { m , n }$ and $\alpha _ { n }$ denote the dual variables associated with the constraint C2 and C3, respectively, where $\lambda _ { m , n } \geq 0$ and $\alpha _ { n } \geq 0$ . Then, the Lagrangian of $\mathbf { P } _ { 2 }$ can be given by (27) at the top of this page, where Ξ denotes a collection of all the primal and dual variables related to $\mathbf { P } _ { 2 }$ . Let $\mu _ { m , n } ~ =$ $\sum _ { k = n } ^ { N } \lambda _ { m , k }$ and $g _ { m } \left[ k \right] = \eta _ { 0 } h _ { m } \left[ k \right] P _ { 0 } - \gamma _ { c } f _ { m } ^ { 3 } \left[ k \right] - z _ { m } \left[ k \right]$ . Then, k=n the Lagrangian function $L \left( \Xi \right)$ can be rewritten by (28) at the top of this page. And the Lagrangian dual function of $\mathbf { P } _ { 2 }$ can be presented as

$$
g \left(\lambda_ {m, n}, \alpha_ {n}\right) = \max _ {0 \leq f _ {m} [ n ]} \mathcal {L} (\Xi). \tag {29}
$$

Based on (29), the optimal solutions of $\mathbf { P } _ { 2 }$ can be obtained by solving its dual problem, given as

$$
\min _ {\lambda_ {m, n}, \alpha_ {n}} g \left(\lambda_ {m, n}, \alpha_ {n}\right). \tag {30}
$$

It can be seen from (30) that the dual problem can be decoupled into M independent optimization problems, given by (31), at the top of the this page. Thus, let the derivation of (31b), at the top of the this page, with respect to $f _ { m } \left[ n \right]$ and $z _ { m } \left[ n \right]$ be zero, one has

$$
\frac {T w _ {m}}{N C} - \frac {3 T \gamma_ {c} f _ {m} ^ {2} [ k ]}{N} \sum_ {k = n} ^ {N} \lambda_ {m, k} = 0, \tag {32a}
$$

$$
\frac {w _ {m} B T t _ {m} [ n ]}{\nu_ {m} N \ln 2} \frac {h _ {m} [ n ]}{\sigma_ {0} ^ {2} t _ {m} [ n ] + h _ {m} [ n ] z _ {m} [ n ]} - \frac {T}{N} \sum_ {k = n} ^ {N} \lambda_ {m, k} = 0. \tag {32b}
$$

Note that $z _ { m } \left[ k \right] = t _ { m } \left[ k \right] P _ { m } \left[ k \right]$ and $P _ { m } \left[ k \right] \geq 0$ . Moreover, the case that $t _ { m } \left[ n \right] = 0$ can be identified as $P _ { m } \left[ n \right] = 0$ . Thus, based on (32), Theorem 1 is proved. The proof for Theorem 1 is complete.

# APPENDIX B PROOF OF THEOREM 5

Let $v _ { m , n }$ and $\varepsilon _ { n }$ denote the dual variables with respect to the constraints given by (24b) and (24c), respectively, where $v _ { m , n } \geq 0$ and $\varepsilon _ { n } \geq 0$ . Then, for any given $f _ { m } [ n ] , P _ { m } \left[ n \right]$ , $t _ { m } \left[ n \right]$ and ${ \bf q } _ { u } \left[ n \right]$ , the Lagrangian of $\mathbf { P } _ { 6 }$ can be expressed by (33) at the top of this page, where $\Xi _ { 1 }$ denotes a collection of all the primal and dual variables related to $\mathrm { P } _ { 6 } . \Xi _ { 2 }$ denotes a collection of $v _ { m , n } , \alpha _ { n } , f _ { m } [ n ] , z _ { m } [ n ] , t _ { m } [ n ]$ and $\rho _ { m }$ . Using

$$
\max _ {\upsilon_ {m, n}, \varepsilon_ {n}, f _ {m} [ n ] \geq 0} \mathcal {L} _ {m} ^ {1} \left(\Xi_ {2}\right)
$$

$$
\mathcal {L} _ {m} ^ {1} \left(\Xi_ {2}\right) = \sum_ {n = 1} ^ {N} w _ {m} \left\{\frac {T \left(1 - \rho_ {m}\right) f _ {m} [ n ]}{N C} + \frac {B T \rho_ {m} t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{t _ {m} [ n ] \sigma_ {0} ^ {2}}\right) \right\} \tag {34a}
$$

$$
+ \sum_ {n = 1} ^ {N} \varpi_ {m, n} \ell_ {m} [ n ] + \frac {\varepsilon_ {n}}{M} - \varepsilon_ {n} t _ {m} [ n ], \tag {34b}
$$

$$
\frac {\partial \mathcal {L} _ {m} ^ {1} (\Xi_ {2})}{\partial \rho_ {m} ^ {o p t}} \left\{ \begin{array}{l l} <   0, & \rho_ {m} ^ {o p t} = 0, \\ = 0, & 0 <   \rho_ {m} ^ {o p t} <   1,   m \in \mathcal {M} \\ > 0, & \rho_ {m} ^ {o p t} = 1; \end{array} \right.
$$

$$
\frac {\partial \mathcal {L} _ {m} ^ {1} (\Xi_ {2})}{\partial \rho_ {m} ^ {o p t}} = \left\{\sum_ {n = 1} ^ {N} - \frac {w _ {m} f _ {m} [ n ]}{C} \frac {T}{N} + \frac {B T t _ {m} [ n ]}{\nu_ {m} N} \log_ {2} \left(1 + \frac {h _ {m} [ n ] z _ {m} [ n ]}{t _ {m} [ n ] \sigma_ {0} ^ {2}}\right) \right\} \tag {35a}
$$

$$
+ \sum_ {n = 1} ^ {N} v _ {m, n} \left\{- \frac {T}{N} \sum_ {k = 1} ^ {n} \left[ - \gamma_ {c} f _ {m} ^ {3} [ k ] + z _ {m} [ k ] \right] \right\} - \sum_ {n = 1} ^ {N} \varepsilon_ {n} t _ {m} [ n ]. \tag {35b}
$$

the same techniques that are used for the proof of Theorem 1, for any given $f _ { m } [ n ] , z _ { m } [ n ] , t _ { m } [ n ]$ and ${ \bf q } _ { u } \left[ n \right] , { \bf P } _ { 6 }$ can be solved by solving M independent optimization problems, given by (34) at the top of the next page, where $\ell _ { m } \left[ n \right] =$ $\eta _ { 0 } h _ { m } \left[ n \right] P _ { 0 } - ( 1 - \rho _ { m } ) \gamma _ { c } f _ { m } ^ { 3 } \left[ n \right] - \rho _ { m } z _ { m } \left[ n \right]$ and $\begin{array} { l l } { \varpi _ { m , n } } & { = } \end{array}$ $\sum _ { k = n } ^ { N } v _ { m , k }$ . Thus, according to [37], the optimal $\rho _ { m }$ denoted k=by $\rho _ { m } ^ { o p t }$ can be obtained by (35) at the top of the this page. Based on (35), since $z _ { m } \left[ n \right] = t _ { m } \left[ n \right] P _ { m } \left[ n \right]$ , Theorem 5 is proved.

# REFERENCES

[1] F. Zhou, Y. Wu, R. Q. Hu, Y. Wang, and K. K. Wong, “Energyefficient NOMA enabled heterogeneous cloud radio access networks,” IEEE Netw., vol. 32, no. 2, pp. 152–160, Mar./Apr. 2018.   
[2] Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, “A survey on mobile edge computing: The communication perspective,” IEEE Commun. Surveys Tuts., vol. 19, no. 4, pp. 2322–2358, 4th Quart., 2017.   
[3] X. Lu, P. Wang, D. Niyato, D. I. Kim, and Z. Han, “Wireless networks with RF energy harvesting: A contemporary survey,” IEEE Commun. Surveys Tuts., vol. 17, no. 2, pp. 757–789, 2nd Quart., 2015.   
[4] F. Zhou, Z. Li, J. Cheng, Q. Li, and J. Si, “Robust AN-aided beamforming and power splitting design for secure MISO cognitive radio with SWIPT,” IEEE Trans. Wireless Commun., vol. 16, no. 4, pp. 2450–2464, Apr. 2017.   
[5] S. Sardellitti, G. Scutari, and S. Barbarossa, “Joint optimization of radio and computational resources for multicell mobile-edge computing,” IEEE Trans. Signal Inf. Process. Over Netw., vol. 1, no. 2, pp. 89–103, Jun. 2015.   
[6] C. You, K. Huang, H. Chae, and B.-H. Kim, “Energy-efficient resource allocation for mobile-edge computation offloading,” IEEE Trans. Wireless Commun., vol. 16, no. 3, pp. 1397–1411, Mar. 2017.   
[7] C. Wang, C. Liang, F. R. Yu, Q. Chen, and L. Tang, “Computation offloading and resource allocation in wireless cellular networks with mobile edge computing,” IEEE Trans. Wireless Commun., vol. 16, no. 8, pp. 4924–4938, Aug. 2017.   
[8] J. Du, L. Zhao, J. Feng, and X. Chu, “Computation offloading and resource allocation in mixed fog/cloud computing systems with min-max fairness guarantee,” IEEE Trans. Commun., vol. 66, no. 4, pp. 1594–1608, Apr. 2018.   
[9] L. Liu, Z. Chang, X. Guo, S. Mao, and T. Ristaniemi, “Multi-objective optimization for computation offloading in fog computing,” IEEE Internet Things J., vol. 5, no. 1, pp. 283–294, Jan. 2018.

[10] W. Zhang, Y. Wen, K. Guan, D. Kilper, H. Luo, and D. O. Wu, “Energy-optimal mobile cloud computing under stochastic wireless channel,” IEEE Trans. Wireless Commun., vol. 12, no. 9, pp. 4569–4581, Sep. 2013.   
[11] J. Xu, L. Chen, and S. Ren, “Online learning for offloading and autoscaling in energy harvesting mobile edge computing,” IEEE Trans. Cogn. Netw., vol. 3, no. 3, pp. 361–373, Sep. 2017.   
[12] Y. Mao, J. Zhang, Z. Chen, and K. B. Letaief, “Dynamic computation offloading for mobile-edge computing with energy harvesting devices,” IEEE J. Sel. Areas Commun., vol. 34, no. 12, pp. 3590–3605, Dec. 2016.   
[13] C. You, K. Huang, and H. Chae, “Energy efficient mobile cloud computing powered by wireless energy transfer,” IEEE J. Sel. Areas Commun., vol. 34, no. 5, pp. 1757–1771, May 2016.   
[14] F. Wang, J. Xu, X. Wang, and S. Cui, “Joint offloading and computing optimization in wireless powered mobile-edge computing systems,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 1784–1797, Mar. 2018.   
[15] S. Mao, S. Leng, K. Yang, X. Huang, and Q. Zhao, “Fair energy-efficient scheduling in wireless powered full-duplex mobile-edge computing systems,” in Proc. IEEE Global Commun. Conf., Singapore, Dec. 2017, pp. 1–6.   
[16] S. Bi and Y. Zhang, “Computation rate maximization for wireless powered mobile-edge computing with binary computation offloading,” IEEE Trans. Wireless Commun., vol. 17, no. 6, pp. 4177–4190, Jun. 2018.   
[17] H. Wang, J. Wang, G. Ding, L. Wang, T. A. Tsiftsis, and P. K. Sharma, “Resource allocation for energy harvesting-powered D2D communication underlaying UAV-assisted networks,” IEEE Trans. Green Commun. Netw., vol. 2, no. 1, pp. 14–24, Jan. 2018.   
[18] S. Yin, J. Tan, and L. Li, “UAV-assisted cooperative communications with wireless information and power transfer,” IEEE Trans. Wireless Commun., to be published. [Online]. Available: https://arxiv.org/abs/1710.00174v1   
[19] J. Xu, Y. Zeng, and R. Zhang, “UAV-enabled wireless power transfer: Trajectory design and energy region characterization,” in Proc. IEEE Global Commun. Conf., Singapore, Dec. 2017, pp. 1–7.   
[20] J. Xu, Y. Zeng, and R. Zhang, “UAV-enabled wireless power transfer: Trajectory design and energy optimization,” IEEE Trans. Wireless Commun., vol. 17, no. 8, pp. 5092–5106, Aug. 2018.   
[21] N. H. Motlagh, M. Bagaa, and T. Taleb, “UAV-based IoT platform: A crowd surveillance use case,” IEEE Commun. Mag., vol. 55, no. 2, pp. 128–134, Feb. 2017.   
[22] N. Zhao et al., “Caching UAV assisted secure transmission in hyperdense networks based on interference alignment,” IEEE Trans. Commun., vol. 66, no. 5, pp. 2281–2294, May 2018.   
[23] S. Jeong, O. Simeone, and J. Kang, “Mobile edge computing via a UAVmounted cloudlet: Optimization of bit allocation and path planning,” IEEE Trans. Veh. Technol., vol. 67, no. 3, pp. 2049–2063, Mar. 2018.

[24] S. Jeong, O. Simeone, and J. Kang, “Mobile edge computing with a UAV-mounted cloudlet: Optimal bit allocation for communication and computation,” IET Commun., vol. 11, no. 7, pp. 969–974, Nov. 2017.   
[25] M. A. Messous, H. Sedjelmaci, N. Houari, and S. M. Senouci, “Computation offloading game for an UAV network in mobile edge computing,” in Proc. IEEE Int. Conf. Commun., Paris, France, May 2017, pp. 1–6.   
[26] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.   
[27] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[28] P. Yang, X. Cao, C. Yin, Z. Xiao, X. Xi, and D. Wu, “Proactive dronecell deployment: Overload relief for a cellular network under flash crowd traffic,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 10, pp. 2877–2892, Oct. 2017.   
[29] E. Kalantari, H. Yanikomeroglu, and A. Yongacoglu, “On the number and 3D placement of drone base stations in wireless cellular networks,” in Proc. IEEE VTC Fall, Montreal, QC, Canada, Sep. 2016, pp. 1–6.   
[30] E. Kalantari, M. Z. Shakir, H. Yanikomeroglu, and A. Yongacoglu, “Backhaul-aware robust 3D drone placement in 5G+ wireless networks,” in Proc. ICC Workshops, Paris, France, May 2017, pp. 109–114.   
[31] L. Zeng, X. Cheng, C. X. Wang, and X. Yin, “A 3D geometry-based stochastic channel model for UAV-MIMO channels,” in Proc. IEEE WCNC, San Francisco, CA, USA, Mar. 2017, pp. 1–5.   
[32] C. X. Wang, A. Ghazal, B. Ai, P. Fan, and Y. Liu, “Channel measurements and models for high-speed train communication systems: A survey,” IEEE Commun. Surveys Tuts., vol. 18, no. 2, pp. 974–987, 2nd Quart., 2016.   
[33] N. Cheng et al., “Aire-ground integrated mobile edge networks: Architecture, challenges and opportunities,” IEEE Commun. Mag., to be published.   
[34] M. Mozaffari, W. Saad, M. Bennis, Y. H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., to be published. [Online]. Available: https://arxiv.org/abs/1803.00680   
[35] S. P. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.   
[36] F. Zhou, N. C. Beaulieu, Z. Li, J. Si, and P. Qi, “Energy-efficient optimal power allocation for fading cognitive radio channels: Ergodic capacity, outage capacity and minimum-rate capacity,” IEEE Trans. Wireless Commun., vol. 15, no. 4, pp. 2741–2755, Apr. 2016.   
[37] F. Zhou, N. C. Beaulieu, J. Cheng, Z. Chu, and Y. Wang, “Robust max– min fairness resource allocation in sensing-based wideband cognitive radio with SWIPT: Imperfect channel sensing,” IEEE Syst. J., to be published.   
[38] S. Bubeck, “Convex optimization: Algorithms and complexity,” Found. Trends Mach. Learn., vol. 8, nos. 3–4, pp. 231–357, 2015.   
[39] C. Gutierrez, F. Gutierrez, and M. C. Rivara, “Complexity of the bisection method,” Theor. Comput. Sci., vol. 382, no. 2, pp. 131–138, 2007.

![](images/2ca491bb05e26ad122588ad7034a1df42b2025f67dab11f68e3a1fb8ac602850.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Fuhui Zhou received the Ph.D. degree from Xidian University, Xian, China, in 2016. He was an international Visiting Ph.D. Student of The University of British Columbia from 2015 to 2016. He is currently an Associate Professor with the School of Information Engineering, Nanchang University. He is also a Research Fellow with Utah State University. His research interests focus on cognitive radio, green communications, edge computing, machine learning, NOMA, physical-layer security, and resource allocation. He has authored over 40 papers, including the IEEE JOURNAL OF SELECTED AREAS IN COMMUNICATIONS, the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, the IEEE WIRELESS COMMUNICATIONS, IEEE Network, and the IEEE GLOBECOM. He has served as a Technical Program Committee Member for many international conferences, such as IEEE GLOBECOM and IEEE ICC. He serves as an Associate Editor for the IEEE ACCESS.

![](images/d1156398e81c5819cd3a8d2179d2b2805835eda825ce7744e9dbb67ed5d4ab63.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a dark polo shirt against a blue background (no text or symbols visible)
</details>

Yongpeng Wu (S’08–M’13–SM’17) received the B.S. degree in telecommunication engineering from Wuhan University, Wuhan, China, in 2007, and the Ph.D. degree in communication and signal processing from the National Mobile Communications Research Laboratory, Southeast University, Nanjing, China, in 2013. He is currently a Tenure-Track Associate Professor with the Department of Electronic Engineering, Shanghai Jiao Tong University, China. Previously, he was a Senior Research Fellow with the Insti-

tute for Communications Engineering, Technical University of Munich, Germany, and the Humboldt Research Fellow and the Senior Research Fellow with the Institute for Digital Communications, University of Erlangen– Nürnberg, Germany. During his Ph.D., he conducted cooperative research with the Department of Electrical Engineering, Missouri University of Science and Technology, Rolla, MO, USA. His research interests include massive MIMO/MIMO systems, physical-layer security, signal processing for wireless communications, and multivariate statistical theory.

Dr. Wu was a recipient of the IEEE Student Travel Grants for the IEEE International Conference on Communications (ICC) 2010, the Alexander von Humboldt Fellowship in 2014, the Travel Grants for the IEEE Communication Theory Workshop 2016, and the Excellent Doctoral Thesis Awards of China Communications Society 2016. He was an Exemplary Reviewer of the IEEE TRANSACTIONS ON COMMUNICATIONS in 2015 and 2016. He is the Lead Guest Editor for the upcoming special issue—Physical Layer Security for 5G Wireless Networks—of the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS. He is currently an Editor of the IEEE ACCESS and the IEEE COMMUNICATIONS LETTERS. He has been a TPC member of various conferences, including Globecom, ICC, VTC, and PIMRC.

![](images/d4021631952a36515bab5d031314c12496f53bf43624cb03586b03c0b5e6c15e.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman with shoulder-length dark hair, wearing a patterned blouse (no visible text or symbols)
</details>

Rose Qingyang Hu received the B.S. degree from the University of Science and Technology of China, the M.S. degree from New York University, and the Ph.D. degree from The University of Kansas. She is currently a Professor with the Electrical and Computer Engineering Department, Utah State University. She has more than 10 years of R&D experience with Nortel, Blackberry, and Intel as a Technical Manager, a Senior Wireless System Architect, and a Senior Research Scientist, actively participating in industrial 3G/4G technology development, stan-

dardization, system-level simulation, and performance evaluation. She has authored over 180 papers in top IEEE journals and conferences. She holds numerous patents in her research areas. Her current research interests include next-generation wireless communications, wireless system design and optimization, green radios, Internet of Things, cloud computing/fog computing, multimedia QoS/QoE, wireless system modeling, and performance analysis. She was a recipient of the best paper awards from IEEE Globecom 2012, IEEE ICC 2015, IEEE VTC Spring 2016, and IEEE ICC 2016. She is an IEEE Communications Society Distinguished Lecturer from 2015–2018.

![](images/921389dfc5e8b11767c5f3015428eee0384e00fd2f837dc2528d6eae09a387b1.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a white shirt with tie (no text or symbols visible)
</details>

Yi Qian (M’95–SM’07) received the Ph.D. degree in electrical engineering from Clemson University. He was involved in the telecommunications industry, academia, and the government. Some of his previous professional positions include serving as a Senior Member of Scientific Staff and a Technical Advisor at Nortel Networks, a senior systems engineer and a technical advisor at several start-up companies, an Assistant Professor with the University of Puerto Rico at Mayaguez, and a Senior Researcher with the National Institute of Standards and Technology. He is currently a Professor with the Department of Electrical and Computer Engineering, University of Nebraska–Lincoln. His research interests include information assurance and network security, network design, network modeling, simulation and performance analysis for next-generation wireless networks, wireless ad hoc and sensor networks, vehicular networks, smart-grid communication networks, broadband satellite networks, optical networks, high-speed networks, and the Internet. He is a member of the ACM. He was the Chair of the IEEE Communications Society Technical Committee for Communications and Information Security from 2014 to 2015. He is the Technical Program Chair for the IEEE International Conference on Communications 2018. He is serving on the editorial boards for several international journals and magazines, including serving as the Associate Editor-in-Chief for the IEEE Wireless Communications Magazine. He is a Distinguished Lecturer for the IEEE Vehicular Technology Society and the IEEE Communications Society.