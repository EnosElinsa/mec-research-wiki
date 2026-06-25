# Mobile Edge Deployment and Resource Management for Maritime Wireless Networks

Chaoyue Zhang, Member, IEEE, Bin Lin , Senior Member, IEEE, Ziru Chen , Member, IEEE, Lin X. Cai , Senior Member, IEEE, and Jianli Duan

Abstract—Mobile Edge Computing (MEC) has been envisioned as one of the key technologies for supplying computation and storage resources in Internet of Vessels (IoV) networks. Due to its flexible deployment, low cost and agile maneuverability, Unmanned Surface Vehicle (USV) has emerged as a promising solution, to provide communication and computation services for maritime users. In this paper, we study mobile edge deployment and resource management for MEC-assisted maritime wireless networks where USVs with diverse computation resources are deployed to provide edge computing services that complement the cloud-based services. To this end, we formulate an optimization problem to minimize the expected response time by jointly optimizing the deployment of mobile USVs and computation offloading decisions. To solve the mixed-integer nonlinear program problem, we propose a Dual-Layer Reinforcement Learning (DLRL) framework to attain a near-optimal solution. Specifically, a Deep Deterministic Policy Gradient (DDPG) algorithm is designed to obtain the best USV deployment in the outer layer learning, and a Q-learning algorithm is designed to determine the best computation offloading decisions in the inner layer learning. Numerical results demonstrate that the proposed solution outperforms some literature algorithms by effectively handling both continuous and discrete variables.

Index Terms—Internet of Vessels (IoV), maritime wireless networks, unmanned surface vehicle (USV), mobile edge deployment and resource management, deep reinforcement learning.

# I. INTRODUCTION

NTERNET of Vessels (IoV) becomes an indispensable part I of maritime wireless communication networks, which enables many smart maritime applications, such as environment monitoring [1], intelligent navigation and voice/video streams, etc. The rapid growth in requirements for maritime applications leads to an increased demand for high bandwidth, low latency, and enhanced computation capabilities. Both academia and the

Received 23 April 2024; revised 24 September 2024; accepted 17 December 2024. Date of publication 27 December 2024; date of current version 20 May 2025. The work of Bin Lin was supported in part by the National Natural Science Foundation of China under Grant 62371085 and Grant 51939001 and in part by the Fundamental Research Funds for the Central Universities under Grant 3132023514. The review of this article was coordinated by Dr. Phone Lin. (Corresponding author: Bin Lin.)

Chaoyue Zhang and Bin Lin are with Information Science and Technology College, Dalian Maritime University, Dalian 116026, China (e-mail: zcy\_11335577@163.com; binlin@dlmu.edu.cn).

Ziru Chen and Lin X. Cai are with the Department of Electrical and Computer Engineering, Illinois Institute of Technology, Chicago, IL 60616 USA (e-mail: zchen71@hawk.iit.edu; lincai@iit.edu).

Jianli Duan is with the School of Science, Qingdao University of Technology, Qingdao 266520, China (e-mail: duanjianli@qut.edu.cn).

Digital Object Identifier 10.1109/TVT.2024.3521393

maritime industry conduct research on the deployment of maritime wireless networks to meet the increasing demand from IoV users. Maritime wireless communication networks are typically classified into shore-based communication networks and offshore-based communication networks. Shore-based communication networks can utilize 3G/4G/5G communication technologies to provide broadband data transmissions, typically covering a radius of up to thirty kilometers from the shore. For offshore-based communication networks, communication services can be provisioned through High Frequency (HF) and Very High Frequency (VHF) channels, and maritime satellites. Typical offshore communication systems, such as PACTOR system, Automatic Identification System (AIS) and VHF Data Exchange System (VDES), operate in the HF/VHF band [2]. These systems usually offer low data rate services over a large communication coverage, e.g., several hundreds of kilometers. In contrast, maritime satellites can offer high data rate services worldwide from anywhere [3]. However, the high cost of vesselborne equipment and communication expenses pose significant challenges for small vessels. In general, existing maritime wireless networks may not meet the application requirements for communication and computation resources in IoV.

Mobile Edge Computing (MEC) provides proximate access to users with computation resources through the deployment of edge servers [4], [5]. Compared with cloud computing, MEC consumes less transmission time and energy due to a shorter transmission distance [6], [7], [8]. In terrestrial networks, MEC has received extensive attention [9], [10], [11], [12]. However, research on MEC-assisted maritime wireless networks is lagging behind that in the terrestrial networks. Applying MEC in maritime wireless networks presents new research challenges compared to those in terrestrial networks. First, despite the vast expanse of the ocean surface, finding a stable area for deploying an edge server is a challenging task. Second, maintenance and management of edge servers in maritime environments, such as applying security patches, troubleshooting, and hardware repairs, may incur high operating costs. Third, it is challenging to ensure low-latency transmission from maritime users to the edge due to the hostile communication environment of the ocean. Owing to these complex factors, transmission efficiency is often low in maritime environments.

In this context, Unmanned Surface Vehicles (USVs) can serve as portable edge servers in close proximity to maritime users, leveraging the advantages of high mobility and ever-reducing cost [13], [14], [15]. Given the limited computation resource of an individual USV, how to deploy multiple USVs and design offloading strategies to improve the computation resource

0018-9545 © 2024 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

utilization, to reduce the computation overload, and to reduce the response time of processing tasks is a critical issue in MEC-assisted maritime wireless networks. It is worth noting that the USV deployment and computation offloading decisions are mutually coupled. Different deployments of USVs may lead to different offloading decisions to achieve the minimum response time, and vice versa. Therefore, USV deployment and computation offloading decisions need to be jointly optimized to minimize the response time. To the best of our knowledge, there have been no prior studies on jointly optimizing multi-USV deployment and computation offloading based on the demands of maritime users in an MEC-assisted maritime wireless network.

In this paper, we formulate a joint optimization problem for USV deployment and computation offloading decisions in MEC-assisted maritime wireless networks. Our objective is to minimize the expected response time, which is comprised of the uplink transmission time, the computation time at the edge server or cloud, and the downlink transmission time. The formulated problem is a Mixed-Integer Non-Linear Program (MINLP) problem with both continuous and discrete variables, i.e., the deployment locations of USVs in a continuous space and the binary offloading decisions in a discrete space. It is worth noting that the deployment locations and the computation offloading decisions are tightly coupled, i.e., the best offloading decisions are dependent on the locations of USVs, and vice versa. In addition, the hybrid variables in both continuous and discrete space pose significant challenges in the optimization framework, as MINLP is well known to be NP-hard. To the best of our knowledge, existing solutions typically involve discretizing continuous actions [16], [17], or employing continuous functions to approximate discrete actions [18], [19], or integrating different tools to handle different types of variables, e.g., to utilize learning techniques for continuous variables and matching theory for discrete variables [20], [21]. These solutions may result in reduced accuracy and/or increased computational complexity. To this end, we first reformulate the optimization problem as a Markov Decision Process (MDP), and propose a novel Dual-Layer Reinforcement Learning (DLRL) framework that integrates Deep Deterministic Policy Gradient (DDPG) and Q-learning to handle the complex hybrid action spaces. Specifically, a DDPG algorithm is designed to optimize the locations of USVs, and a Q-learning algorithm is designed to determine the best computation offloading decisions. Finally, extensive simulation results verify that the proposed DLRL algorithm can effectively reduce the expected response time, in comparison with the benchmark algorithms in the literature. The main contributions of this work can be summarized as follows.

We propose a framework for mobile edge deployment and resource management in MEC-assisted maritime wireless networks, where computation tasks of each vessel can be offloaded to an edge server or cloud center. A joint USV deployment and computation offloading problem is formulated to minimize the expected response time, subject to the constraint of edge computation resources.   
- To solve the formulated optimization problem, we reformulate it as an MDP problem, and propose a DLRL framework that integrates DDPG and Q-learning to handle the discrete and continuous actions to facilitate collaborative training.   
- In the DLRL algorithm, the outer layer DDPG is designed to optimize the locations of USVs in continuous space,

based on the locations and computation tasks of vessels from historical experiences; and the inner layer Q-learning is designed to determine the best computation offloading decisions in discrete space based on the locations of USVs. Further analysis is conducted on the complexity of the proposed learning algorithm.

The remainder of this paper is organized as follows. The related works are presented in Section II. An MEC-assisted maritime wireless network model and problem formulation are introduced in Section III. A DLRL algorithm is proposed to solve the optimal USV deployment and computation offloading problem in Section IV. Numerical results are presented to evaluate the performance of the proposed DLRL algorithm in Section V, followed by concluding remarks in Section VI.

# II. RELATED WORKS

Computation offloading in MEC networks has been extensively studied in the literature [12], [22], [23]. Generally, the computation tasks can be processed at mobile users, or be offloaded to the edge server or the the cloud server. In [12], a DDQN algorithm is applied to jointly optimize the computation offloading decisions, and spectrum and computation resource allocation in an MEC network with a single edge server, aiming to minimize the energy consumption of the system. Computation offloading in an MEC network with multiple edge servers is studied in [22], [23]. In [22], convex optimization methods are used to optimize the computation offloading, the computation resource allocation, and transmission power control in an MEC network, with the objective of minimizing the overall energy consumption. In [23], an end-to-end deep reinforcement learning algorithm is proposed to optimize the offloading decisions and computational frequency allocation in an MEC network with multiple users and multiple edge servers, aiming to maximize the number of tasks completed on time while minimizing the energy consumption.

The deployment of edge servers can be categorized into two types, i.e., 1) fixed deployment, where edge servers are strategically placed within the network infrastructure, with the location unchanged after deployment to ensure stable and reliable edge services; and 2) on-demand deployment, where edge servers are deployed based on network dynamics, and the configuration of the edge servers is adjustable in response to the changing network conditions and demands.

Some studies investigate deploying edge servers among a set of fixed candidate locations. In [24], leveraging the advantages of the bipartite graph and heuristic algorithm, a two-step optimization method is proposed to address the edge server deployment and task scheduling, aiming to maximize the profits of the service provider. In [25], a deployment algorithm based on k-means clustering and particle swarm optimization is proposed to solve the cloudlet deployment problem, with the objective of minimizing the average service delay. In these works, a single objective optimization is formulated. There are some works that formulate the edge server deployment problem as a multi-objective optimization problem [9], [26], [27]. In [26], the objective is to balance the workload and minimize the access delay. Genetic algorithm and local search algorithm are designed to find the best solution. The work in [27] studies how to strike a trade-off among the coverage rate, the waiting time, and the workload balance. The Niched Pareto Genetic Algorithm II (NPGA-II) is adopted to find the feasible solutions for edge server deployment. In these aforementioned works, heuristic algorithms are proposed to find the deployment solutions, and the deployment is not adaptive to the dynamic demands of the network.

Recent advancement on Unmanned Aerial Vehicles (UAVs) offers a viable and flexible solution for MEC where UAVs equipped with edge servers can provide on-demand services to users in the proximity and the locations of UAVs can dynamically adapt to the user demands. The trajectories of UAVs are usually modeled as continuous variables, and efficient methods and algorithms based on machine learning and convex optimization are proposed to dynamically optimize decision-making processes. The deployment of a single UAV equipped with an edge server is studied in [28], [29]. In [28], an alternative algorithm based on convex optimization and Lyapunov-based approach is proposed to optimize the resource allocation and UAV trajectory in a UAV-assisted MEC system, with the objective of minimizing the average energy consumption. In [29], an alternative algorithm based on block coordinate descent and successive convex approximation techniques is proposed to solve the computation offloading decisions, bits allocation and UAV trajectory optimization problem in a UAV-enhanced MEC network, with the objective of minimizing the total energy consumption. A few research works study multi-UAV deployment and computation offloading in the multi-UAV-enabled MEC network [18], [30], [31], [32]. Generally, joint optimization of multiple UAV trajectories and offloading decisions in a wireless network is a complex optimization problem which is usually modeled as an MINLP problem [33]. Deep reinforcement learning offers an efficient solution to tackle the challenging problem. In [18], a Q-learning algorithm and transport theory are proposed to optimize the multi-UAV deployment and user association, with the objective of minimizing the transmit power consumption. The work in [30] develops a multi-agent DDPG algorithm to jointly optimize the vehicle association, resource allocation and multi-UAV trajectory in an MEC- and UAV-assisted vehicular network. The algorithms used in [18], [30] utilize the approximation method to handle the complex optimization problem, resulting in performance loss. The work in [31] applies a manyto-one matching to optimize the subchannel allocation, and leverages a DDPG algorithm to train the multi-UAV trajectory in a multi-UAV collaborative caching network, aiming to minimize the total content retrieving delay. In [32], an algorithm based on the transport theory and particle swarm intelligence is proposed to find the optimal user association and multi-UAV deployment, with the objective of minimizing the average task delay. The algorithms used in [31], [32] utilize iteration optimization to separately solve the continuous and discrete variables to attain a local optimal solution with high computational complexity. In addition, the existing works mainly consider a small scale MEC network with no more than four UAVs. The complexity of these algorithms usually increases exponentially with the number of UAVs, and thus they are not suitable for a medium or a large scale deployment of MEC with a large number of mobile edge servers.

Similar to UAVs, USVs equipped with edge servers can provide mobile edge services to users in a maritime wireless network. Joint resource management and USV deployment are studied in [34], [35], and successive convex approximation, semidefinite programming relaxation, interior-point and block coordinate descent methods are proposed to solve the joint optimization problem. Numerical results show that a USV deployed in the maritime wireless network can greatly improve the network throughput. Multi-USV deployment is studied in [36], where bisection search is used to find the optimal placement of USVs along with the data uploading duration and signal powers to achieve the minimum energy consumption. In this work, the number of USVs is no more than six.

The aforementioned literature works focus on either computation task offloading or edge server deployment in an MEC network. Basically, offloading decisions should be adaptive to the dynamic demands of users, which is not generally coupled with network deployment in traditional MEC with fixed deployment of edge servers. Thanks to the mobility of USVs, it is possible and favorable to deploy mobile edge servers according to the dynamic network demands. Therefore, a joint optimization of the edge server deployment and computation offloading beckons for further research. In addition, while most existing works only consider a limited number of USVs/UAVs, a scalable solution is required for a maritime wireless network because a large number of USVs are required to cover a wide area in marine. To the best of our knowledge, our work is the first to jointly optimize multi-USV deployment and computation offloading based on the demands of maritime users in an MEC-assisted maritime wireless network.

# III. SYSTEM MODEL AND PROBLEM FORMULATION

# A. Network Model

In this paper, we consider an MEC-assisted maritime wireless network consisting of a cloud center, a coastal Base Station (BS), a group of USVs denoted as $\mathcal { U } = \{ 1 , . . . , U \}$ and a group of vessels denoted as $\mathcal { M } = \{ 1 , . . . , M \}$ , as illustrated in Fig. 1. Each vessel is associated with a USV via a wireless link, and USVs can communicate with a coastal BS, which is connected to the cloud center via a wired link. The BS serves as the network controller that collects the network information for mobile edge deployment and resource management. Each USV can be equipped with computation and storage units to provision edge computing services for vessels in the proximity. Due to the limited computation resources in each individual USV, multiple USVs can be deployed in one area to form a cluster of USVs so that the vessel associated with the USVs in the cluster can share the aggregated computing resources. Without loss of generality, USVs are grouped into N clusters, and each USV cluster may contain one1 or multiple USVs. Denote the set of USVs in USV cluster $n \in \mathcal { N } = \{ 1 , . . . , N \}$ as $\mathcal { Z } _ { n } = \{ 1 , . . . , Z _ { n } \} , \forall z _ { n } \in \mathcal { Z } _ { n } ,$ where $\begin{array} { r } { \sum _ { n = 1 } ^ { N } Z _ { n } = U ( U \geq N ) } \end{array}$ USVs. In a 2D Cartesian coordinate system, the location of i is denoted as $\mathbf { L } _ { i } = [ x _ { i } , y _ { i } ]$ , where i can be a vessel $i \in \mathcal { M }$ , or a USV cluster $i \in \mathcal N$ . Assume that the task arrival rate of vessel m follows Poisson distribution with mean $\lambda _ { m } .$ . Let $I _ { m }$ denote the number of computation tasks of vessel m in a time slot. The main notations are listed in Table I.

1This is the special case that each USV will be individually deployed without clustering.

![](images/9835672489e375c674bbb8eaeb0f64c03926dd40c5cc832c7a46f6bd583d5259.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Cloud center"] -->|Wired link| B["Coastal BS"]
    A -->|Wireless link| B
    B --> C["USV cluster"]
    C --> D["Vessel"]
    C --> E["Edge server"]
    D --> F["Vessel"]
    E --> G["Edge server"]
    F --> H["Vessel"]
    G --> I["USV cluster"]
    I --> J["Vessel"]
    I --> K["Edge server"]
    J --> L["Vessel"]
    K --> M["Edge server"]
    L --> N["Vessel"]
    M --> O["Vessel"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#fcc,stroke:#333
    style F fill:#cff,stroke:#333
    style G fill:#cff,stroke:#333
    style H fill:#ffc,stroke:#333
    style I fill:#ffc,stroke:#333
    style J fill:#ffc,stroke:#333
    style K fill:#ffc,stroke:#333
    style L fill:#ffc,stroke:#333
    style M fill:#ffc,stroke:#333
```
</details>

Fig. 1. An MEC-assisted maritime wireless network with multiple USVs.

TABLE I MAIN NOTATIONS AND DESCRIPTIONS 

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $\mathcal{U}$ </td><td>A set of USVs</td></tr><tr><td> $\mathcal{M}$ </td><td>A set of vessels</td></tr><tr><td> $\mathcal{N}$ </td><td>A set of USV clusters</td></tr><tr><td> $\mathcal{Z}_{n}$ </td><td>A set of USVs in USV cluster  $n$ </td></tr><tr><td> $\alpha_{m,n}$ </td><td>Offloading decision variable. 1 means vessel  $m$  offloads task to USV cluster  $n \in \mathcal{N}$  or the cloud center  $n = \{0\}$ ; and 0 vice versa.</td></tr><tr><td> $\lambda_{m}$ </td><td>The task arrival rate of vessel  $m$ </td></tr><tr><td> $I_{m}$ </td><td>The number of computation tasks of vessel  $m$ </td></tr><tr><td> $c_{m}$ </td><td>The required CPU cycles for processing the computation task of vessel  $m$ </td></tr><tr><td> $b_{m}^{\text{in}}$ </td><td>The average input data volume of the computation task of vessel  $m$ </td></tr><tr><td> $b_{m}^{\text{out}}$ </td><td>The average data volume of the computation task computation result of vessel  $m$ </td></tr><tr><td> $\mathbf{L}_{i}$ </td><td>The location of  $i$ , where  $i \in \mathcal{M} \cup \mathcal{N}$ </td></tr><tr><td> $P_{i}$ </td><td>The transmit power of  $i$ , where  $i \in \mathcal{M} \cup \mathcal{N}$ </td></tr><tr><td> $H_{i}$ </td><td>The antenna height of  $i$ , where  $i \in \mathcal{M} \cup \mathcal{N}$ </td></tr><tr><td> $B$ </td><td>Channel bandwidth</td></tr><tr><td> $h_{i,j}$ </td><td>The channel gain between  $i$  and  $j$ , where  $i,j \in \mathcal{M} \cup \mathcal{N}$ </td></tr><tr><td> $R_{i,j}$ </td><td>The transmission rate from  $i$  to  $j$ , where  $i,j \in \mathcal{M} \cup \mathcal{N}$ </td></tr><tr><td> $C_{n}$ </td><td>The computation resource of  $n$ , where  $n \in \mathcal{N} \cup \{0\}$ </td></tr></table>

Considering the impacts of sea surface reflection and antenna height, a two-ray signal transmission model is adopted for maritime channels [3]. The transmission model assumes that the maritime channel mainly consists of a direct path and a reflection path, the channel gain between vessel m and the USV cluster n can be expressed as

$$
h _ {m, n} = \left(\frac {l}{4 \pi d _ {m , n}}\right) ^ {2} \left[ 2 \sin \left(\frac {2 \pi H _ {m} H _ {n}}{l d _ {m , n}}\right) \right] ^ {2},
$$

$$
\forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {1}
$$

where l is the carrier wavelength, $H _ { m }$ is the antenna height of vessel $m , \ H _ { n }$ is antenna height of n-th USV cluster header, $d _ { m , n } = \sqrt { ( x _ { m } - x _ { n } ) ^ { 2 } + ( y _ { m } - y _ { n } ) ^ { 2 } }$ is the communication link distance. The uplink transmission rate $R _ { m , n }$ from vessel m to USV cluster, and the downlink transmission rate $R _ { n , m }$ from USV cluster n to vessel m are

$$
R _ {m, n} = B \log_ {2} \left(1 + \frac {P _ {m} h _ {m , n}}{\sigma^ {2}}\right), \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {2}
$$

$$
R _ {n, m} = B \log_ {2} \left(1 + \frac {P _ {n} h _ {m , n}}{\sigma^ {2}}\right), \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {3}
$$

respectively, where $\sigma ^ { 2 }$ denotes the white Gaussian noise power, B denotes the channel bandwidth, $P _ { m }$ denotes the transmit power of vessel m, $P _ { n }$ denotes the transmit power of n-th USV cluster header.

Vessels can offload their tasks to USV clusters or the cloud center. We introduce a binary variable $\alpha _ { m , n } \in \{ 0 , 1 \}$ , ∀m ∈ $\mathcal { M } , \forall n \in \mathcal { N } \cup \{ 0 \}$ to represent computation offloading decision of vessel m. Specifically, $\alpha _ { m , n } = 1$ indicates that vessel m offloads the task to a USV cluster $n \in \mathcal N$ or the cloud center $n = \{ 0 \}$ , and $\alpha _ { m , n } = 0$ otherwise. Each vessel can offload its computation tasks to either one USV cluster for edge computing or the cloud center for cloud computing, satisfying

$$
\sum_ {n \in \mathcal {N} \cup \{0 \}} \alpha_ {m, n} = 1, \forall m \in \mathcal {M}. \tag {4}
$$

Case 1. Edge Computing: In the case that the computation tasks are offloaded to the edge server, the response time of the vessel is the sum of the uplink transmission time from vessel m USV clustertime from a $n ,$ oted as luster $T _ { m , n } ^ { \mathrm { u l } } ,$ e downlink denoted as ission. Thus, $n ,$ $T _ { m , n } ^ { \mathrm { c o m p } }$ $m ,$ $T _ { n , m } ^ { \mathrm { d l } }$ we have

$$
T _ {m, n} = T _ {m, n} ^ {\mathrm{ul}} + T _ {m, n} ^ {\mathrm{comp}} + T _ {n, m} ^ {\mathrm{dl}}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}. \tag {5}
$$

The uplink transmission time $T _ { m , n } ^ { \mathrm { u l } }$ is given by

$$
T _ {m, n} ^ {\mathrm{ul}} = \alpha_ {m, n} \frac {I _ {m} b _ {m} ^ {\mathrm{in}}}{R _ {m , n}}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {6}
$$

where $b _ { m } ^ { \mathrm { i n } }$ denotes the average input data volume of the computation task of vessel m.

The computation resource of USV cluster n is $C _ { n } =$ $\textstyle \sum _ { u \in { \mathcal { Z } } _ { n } } C _ { u } .$ , where $C _ { u }$ is the computation resource equipped in

USV u. The computation time at USV cluster n to process the offloaded tasks of vessel m is

$$
T _ {m, n} ^ {\text { comp }} = \alpha_ {m, n} \frac {I _ {m} c _ {m}}{C _ {n}}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {7}
$$

where $c _ { m }$ denotes the required CPU cycles for computing the computation task of vessel m.

The downlink transmission time of computation results to be sent from USV cluster n to vessel m is given by

$$
T _ {n, m} ^ {\mathrm{dl}} = \alpha_ {m, n} \frac {I _ {m} b _ {m} ^ {\mathrm{out}}}{R _ {n , m}}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {8}
$$

where $b _ { m } ^ { \mathrm { o u t } }$ denotes average data volume of the task computation result of vessel m.

Note that the total edge computation resource to serve vessels cannot exceed the maximum computation resource of the USV cluster n,

$$
\sum_ {m \in \mathcal {M}} \alpha_ {m, n} \lambda_ {m} c _ {m} \leq C _ {n}, \forall n \in \mathcal {N}. \tag {9}
$$

Case 2. Cloud Computing: In the case that the computation tasks are offloaded to the cloud, the response time is the sum of the uplink transmission time from vessel m to the cloud center, denoted as $T _ { m , 0 } ^ { \mathrm { u l } } .$ , the computation time at the cloud center, denoted as $T _ { m , 0 } ^ { \mathrm { c o m p } }$ , and the downlink transmission time from the m,0 cloud center to vessel $m ,$ denoted as $T _ { 0 , m } ^ { \mathrm { d l } }$ . Thus, we have

$$
T _ {m, 0} = T _ {m, 0} ^ {\mathrm{ul}} + T _ {m, 0} ^ {\mathrm{comp}} + T _ {0, m} ^ {\mathrm{dl}}, \forall m \in \mathcal {M}. \tag {10}
$$

The uplink transmission time $T _ { m , 0 } ^ { \mathrm { u l } }$ is given by

$$
T _ {m, 0} ^ {\mathrm{ul}} = \alpha_ {m, 0} \left(\frac {I _ {m} b _ {m} ^ {\mathrm{in}}}{R _ {m , n}} + \frac {I _ {m} b _ {m} ^ {\mathrm{in}}}{R _ {n , 0}} + \tau_ {0}\right), \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {11}
$$

where the first term in the braces represents the task transmission time from vessel m to the nearest USV cluster n, the second term is the transmission time from the USV cluster n to the coastal BS, and the third term $\tau _ { 0 }$ denotes the transmission time from the coastal BS to the cloud center.

Generally, the computation resource of the cloud center is much greater than that in the edge server, and we have $C _ { 0 } > >$ $C _ { n }$ . The computation time at the cloud center to process the offloaded tasks of vessel m is

$$
T _ {m, 0} ^ {\text { comp }} = \alpha_ {m, 0} \frac {I _ {m} c _ {m}}{C _ {0}}, \forall m \in \mathcal {M}. \tag {12}
$$

The computation results are then transmitted from the cloud center to vessel m through the coastal BS, and the transmission time is thus given by

$$
T _ {0, m} ^ {\mathrm{dl}} = \alpha_ {m, 0} \left(\tau_ {0} + \frac {I _ {m} b _ {m} ^ {\text {out}}}{R _ {0 , \mathrm{n}}} + \frac {I _ {m} b _ {m} ^ {\text {out}}}{R _ {\mathrm{n} , \mathrm{m}}}\right), \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {13}
$$

where the first term in the braces, $\tau _ { 0 } ,$ denotes the transmission time of computation results from the cloud center to the coastal BS, the second term represents the transmission time from the coastal BS to the USV cluster n, and the third term represents the transmission time from the USV cluster n to vessel m.

# B. Problem Formulation

The objective is to minimize the expected response time by jointly optimizing the deployment of USV clusters $\mathbf { L } ^ { \mathrm { u s v } } =$ $\{ \mathbf { L } _ { n } , \forall n \in \mathcal { N } \}$ and the computation offloading decisions for vessels $\pmb { \alpha } = \{ \alpha _ { m , n } , \forall m \in \mathcal { M } , \forall n \in \mathcal { N } \cup \{ 0 \} \}$ , while satisfying the edge computing resource constraint. Mathematically, we formulate the Expected Response Time Minimization (ERTM) problem as follows,

(ERTM) :

$$
\min _ {\mathbf {L} ^ {\mathrm{usv}}, \boldsymbol {\alpha}} T = \frac {1}{M} \sum_ {m \in \mathcal {M}} (T _ {m, n} + T _ {m, 0}) \tag {14}
$$

$$
\text { s.t. } \alpha_ {m, n} \in \{0, 1 \}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N} \cup \{0 \}, \tag {14a}
$$

$$
\sum_ {n \in \mathcal {N} \cup \{0 \}} \alpha_ {m, n} = 1, \forall m \in \mathcal {M}, \tag {14b}
$$

$$
\sum_ {m \in \mathcal {M}} \alpha_ {m, n} \lambda_ {m} c _ {m} \leq C _ {n}, \forall n \in \mathcal {N}, \tag {14c}
$$

$$
0 \leq x _ {n} \leq x _ {\max}, 0 \leq y _ {n} \leq y _ {\max}, \forall n \in \mathcal {N}. \tag {14d}
$$

Constraints (14a) and (14b) represent that each vessel can offload its tasks to either one USV cluster or the cloud center. Constraint (14c) means that the total computation resource cannot exceed the maximum computation resource of the USV cluster. Constraint (14d) is the deployment area constraint.

# IV. DUAL-LAYER REINFORCEMENT LEARNING ALGORITHM DESIGN

In this section, we first reformulate the ERTM problem as an MDP, and then propose a dual-layer reinforcement learning framework to handle the hybrid action spaces and to attain the optimal solution.

# A. MDP Formulation

In this subsection, we reformulate the ERTM problem as an MDP. For the DLRL algorithm, the coastal BS is modeled as an agent, and the MEC-assisted maritime wireless network is the environment. The state space, the action space, and the reward function of the MDP are defined as follows.

1) Action Space: The action space in the t-th round is $\mathbf { a } _ { t } = \{ \mathbf { v } _ { t } , \pmb { \vartheta } _ { t } , \mathbf { D } _ { t } \}$ , where $\mathbf { v } _ { t } = \{ v _ { m , t } | m \in \mathcal { M } \}$ denotes the computation offloading decisions of vessels, $\vartheta _ { t } = \{ \vartheta _ { n , t } | \vartheta _ { n , t } \in$ $[ 0 , 2 \bar { \pi } ) , \forall n \in \mathcal { N } \}$ denotes the search angle for USV clusters, and $\mathbf { D } _ { t } = \{ D _ { n , t } | D _ { n , t } \in [ 0 , D _ { \operatorname* { m a x } } ] , \forall \bar { n } \in \mathcal N \}$ denotes the search distance of USV clusters within a maximal search distance $D _ { \mathrm { m a x } }$ .   
2) State Space: The state space in the t-th round is $\mathbf { s } _ { t } =$ $\{ \mathbf { L } _ { t } ^ { \mathrm { u s v } } , \mathbf { h } _ { t } \}$ , where ${ \bf L } _ { t } ^ { \mathrm { u s v } } = \{ { \bf L } _ { n , t } \} n \in \mathcal { N } \}$ denotes the locations of USV clusters, and $\mathbf { h } _ { t } = \{ h _ { m , n , t } | m \in \mathcal { M } , n \in \mathcal { N } \}$ denotes the channel gain between vessels and USV clusters.   
3) Reward Function: According to the problem formulation in Section III, the objective of the ERTM problem is to minimize the expected response time by optimizing the deployment of each USV cluster and computation offloading decisions. Therefore, the reward function of the DLRL algorithm should be inversely proportional to the expected response time, which is defined as

$$
r _ {t} = \frac {1}{T (\mathbf {s} _ {t} , \mathbf {a} _ {t})}, \tag {15}
$$

where $T ( \mathbf { s } _ { t } , \mathbf { a } _ { t } )$ is the expected response time of all vessels at the state $\mathbf { s } _ { t }$ and taking the action $\mathbf { a } _ { t }$ .

![](images/fa36f853c271661c38290ac25c07603a2e6a9ec36235cc75fdf7e5f1859023ef.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Replay Buffer"] -->|sampling (s_t^out, a_t^out, r_t, s_{t+1}^out)| B["Mini-Batch (s_j^out, a_j^out, r_j, s_{j+1}^out)"]
    B --> C["Outer-layer: DDPG-based USV cluster deployment algorithm"]
    C --> D["Online Actor Network θ^μ"]
    C --> E["Target Actor Network θ^μ"]
    D --> F["Soft update"]
    E --> G["Soft update"]
    F --> H["Output: Computation offloading α"]
    G --> I["Input: USV clusters deployment L^usv"]
    H --> J["Inner-layer: Q-learning-based computation offloading algorithm"]
    I --> J
    J --> K["Inner environment"]
    K --> L["r(s_e^inn, a_e^inn)"]
    L --> M["Update Q-table"]
    M --> N["Q-table"]
    N --> O["Input state s^inn"]
    P["Environment"] --> Q["Cloud center"]
    Q --> R["Wired link"]
    R --> S["Coastal BS"]
    S --> T["USV cluster 1"]
    S --> U["USV cluster 2"]
    S --> V["USV cluster N"]
    T --> W["Vessel"]
    U --> X["Vessel"]
    V --> Y["Vessel"]
    W --> Z["Wireless link"]
    X --> AA["Wireless link"]
    Y --> AB["Wireless link"]
    Z --> AC["USV cluster 1"]
    Z --> AD["USV cluster 2"]
    Z --> AE["USV cluster N"]
```
</details>

Fig. 2. Framework of the DLRL algorithm.

# B. Dual-Layer Reinforcement Learning

We propose a dual-layer learning framework to solve the formulated problem. As shown in Fig. 2, the outer layer DDPG is employed for the USV deployment in continuous space and the inner layer Q-learning is employed for the computation offloading decisions in discrete space. Specifically, the inner layer learning is executed at the beginning of each epoch, which can obtain the best computation offloading results and interact with the environment. The results of the inner layer learning is used to further train the outer layer Deep Neural Networks (DNNs). In the outer layer, we utilize a DDPG to train the USV deployment design, where two main DNNs, i.e., the actor network and the critic network, are trained with the same structure but different parameters. In the ${ \mathrm { D L R L } } ,$ a mini-batch is used to sample the historical experience stored in the replay buffer for updating network parameters. Finally, the USV deployment actions and computation offloading selection actions are coordinated to achieve convergence. The detailed designs of the outer layer and inner layer learning algorithms are presented as follows.

1) Outer Layer Framework of DLRL Algorithm: A deep reinforcement learning algorithm based on DDPG is proposed to optimize the deployment locations of USVs in the continuous action space. Based on the MDP, DDPG can guide the agent to efficiently approach the near-optimal solution with continuous variables by exploring and interacting with the environment. The agent observes the current environment state, selects an action, receives an immediate reward based on the current state and action, and then observes the next state. Specifically, for the outer layer, the action space in the t-th round is $\mathbf { a } _ { t } ^ { \mathrm { { o u t } } } = \{ \vartheta _ { t } , \mathbf { D } _ { t } \}$ , and the state space in the t-th round is $\mathbf s _ { t } ^ { \mathrm { o u t } } = \{ \mathbf L _ { t } ^ { \mathrm { u s v } } , \dot { \mathbf h } _ { t } \}$ .

The DDPG algorithm consists of two main networks, i.e., the actor network and the critic network. Both the actor and critic networks feature two subnets, i.e., the online network and the target network with the same structure. The critic network is trained to approximate the Q-values based on the state and action. The actor network is trained to generate a deterministic policy and returns the corresponding action based on the current state. Besides, experience replay buffer and target networks are employed to enhance the stability and convergence of the learning process in the online networks.

The goal of DDPG is to find optimal policies that maximize the cumulative reward value. A policy $\mu$ can be considered as a function that maps states to actions. Thus, we can obtain the action-value function as follows,

$$
Q (\mathbf {s} _ {t} ^ {\mathrm{out}}, \mathbf {a} _ {t} ^ {\mathrm{out}} | \theta^ {Q}) = \mathbb {E} [ r _ {t} + \zeta^ {\mathrm{out}} Q (\mathbf {s} _ {t + 1} ^ {\mathrm{out}}, \mathbf {a} _ {t + 1} ^ {\mathrm{out}} | \theta^ {Q}) ], \tag {16}
$$

where $\theta ^ { Q }$ is the weight of the online critic network, $\zeta ^ { \mathrm { o u t } } \in [ 0 , 1 ]$ is the discount factor that represents the uncertainly of future revenue, E[·] is the expectation.

The training process can be described as follows. Initially, the actor network adds the noise $\beta$ and generates the action $\mathbf { a } _ { t } ^ { \mathrm { { o u t } } } = \mu ( \mathbf { s } _ { t } ^ { \mathrm { { o u t } } } | \theta ^ { \mu } ) + \beta ,$ , where $\theta ^ { \mu }$ is the weight of the online actor network. Upon interaction with the environment using action $\mathbf { a } _ { t } ,$ the agent receives a reward $r _ { t }$ and transitions to the next state ${ \bf s } _ { t + 1 } ^ { \mathrm { o u t } }$ . This experience $( \mathbf { s } _ { t } ^ { \mathrm { { o u t } } } , \mathbf { a } _ { t } ^ { \mathrm { { o u t } } } , r _ { t } , \mathbf { s } _ { t + 1 } ^ { \mathrm { { o u t } } } )$ is stored in the experience replay buffer O. After that, a set of historical experiences from the replay buffer are randomly sampled into a mini-batch buffer, such as $( \mathbf { s } _ { j } ^ { \mathrm { o u t } } , \mathbf { a } _ { j } ^ { \mathrm { o u t } } , r _ { j } , \mathbf { s } _ { j + 1 } ^ { \mathrm { o u t } } )$ , to update the network weights.

The critic network updates its online network by minimizing loss of the critic network, which is approximated by

$$
L (\theta^ {Q}) = \mathbb {E} [ (Q (\mathbf {s} _ {j} ^ {\text { out }}, \mathbf {a} _ {j} ^ {\text { out }} | \theta^ {Q}) - Y _ {j}) ^ {2} ], \tag {17}
$$

where $Y _ { j } = r _ { j } + \zeta Q ( \mathbf { s } _ { j + 1 } ^ { \mathrm { { o u t } } } , \hat { \mu } ( \mathbf { s } _ { j + 1 } ^ { \mathrm { { o u t } } } | \theta ^ { \hat { \mu } } ) | \theta ^ { \hat { Q } } )$ is the Q-value produced by the target critic network, $\theta ^ { \hat { \mu } }$ and $\theta ^ { \hat { Q } }$ are weights of the target actor network and the target critic network, respectively. The symbol ${ \hat { \mu } } ( \cdot | \theta ^ { { \hat { \mu } } } )$ means the action policy obtained by the target actor network. Correspondingly, the weight $\theta ^ { Q }$ of the online critic network is updated as

$$
\bigtriangledown_ {\theta^ {Q}} L (\theta^ {Q}) = \mathbb {E} [ (Q (\mathbf {s} _ {j} ^ {\text { out }}, \mathbf {a} _ {j} ^ {\text { out }} | \theta^ {Q}) - Y _ {j})
$$

$$
\times \bigtriangledown_ {\theta^ {Q}} Q (\mathbf {s} _ {j} ^ {\text { out }}, \mathbf {a} _ {j} ^ {\text { out }} | \theta^ {Q}) ], \tag {18}
$$

$$
\theta^ {Q} = \theta^ {Q} + \gamma_ {Q} \bigtriangledown_ {\theta^ {Q}} L (\theta^ {Q}), \tag {19}
$$

where $\bigtriangledown \theta Q ^ { \prime }$ · denotes the gradient vector with the weight $\theta ^ { Q }$ , γQ is the learning rate of the online critic network.

With the Adam optimizer, the gradient of the weight $\theta ^ { \mu }$ is derived as $\bigtriangledown \theta ^ { \mu } \mu \big ( \mathbf { s } _ { j } ^ { \mathrm { o u t } } | \theta ^ { \mu } \big )$ . Based on the sampling mini-batch, the policy gradient of the online actor network with the weight $\theta ^ { \mu }$ is updated as

$$
\bigtriangledown_ {\theta^ {\mu}} J \left(\theta^ {\mu}\right) = \mathbb {E} \left[ \bigtriangledown_ {a} Q \left(\mathbf {s} _ {j} ^ {\text { out }}, a \mid \theta^ {Q}\right) \mid_ {a = \mu \left(\mathbf {s} _ {j} ^ {\text { out }} \mid \theta^ {\mu}\right)} \bigtriangledown_ {\theta^ {\mu}} \mu \left(\mathbf {s} _ {j} ^ {\text { out }} \mid \theta^ {\mu}\right) \right]. \tag {20}
$$

Correspondingly, the weight $\theta ^ { \mu }$ of the online actor-network is expressed as

$$
\theta^ {\mu} = \theta^ {\mu} + \gamma_ {\mu} \bigtriangledown_ {\theta^ {\mu}} J (\theta^ {\mu}), \tag {21}
$$

where $\gamma _ { \mu }$ is the learning rate of the online actor network.

With the soft update strategy, the weights of the target actor network and the target critic network are updated as

$$
\theta^ {\hat {\mu}} \leftarrow \delta \theta^ {\mu} + (1 - \delta) \theta^ {\hat {\mu}}, \tag {22}
$$

$$
\theta^ {\hat {Q}} \leftarrow \delta \theta^ {Q} + (1 - \delta) \theta^ {\hat {Q}}, \tag {23}
$$

respectively. Here, $\delta \in [ 0 , 1 ]$ is the soft update coefficient.

2) Inner Layer Framework of DLRL Algorithm: Q-learning is an effective model-free reinforcement learning algorithm based on value iteration, which can find the optimal action in a finite MDP [37]. In the inner layer, the action space is ${ \bf a } _ { e } ^ { \mathrm { i n n } } = \{ { \bf v } _ { e } \}$ , and the state space is e value of each state-act $\bar { \mathbf { s } } _ { e } ^ { \mathrm { i n n } } = \{ \mathbf { h } _ { e } \}$ . The agentupdates the Q-value in a Q-table after each interaction.

The -greedy policy is employed to strike a balance between exploitation and exploration. Specifically, the agent selects the optimal action based on the current Q-table with a probability of for exploitation. With a probability of $1 - \epsilon ,$ the agent selects a random action for exploration, which enables the agent to try out new actions and potentially discover better ones that may not have been selected through exploitation. Thus, the action with -greedy policy in the e-th epoch is given by

$$
\mathbf {a} _ {e} ^ {\text { inn }} = \left\{ \begin{array}{l} \operatorname{argmax} _ {\mathbf {a} _ {e} ^ {\text { inn }} \in \mathbf {a} ^ {\text { inn }}} Q \left(\mathbf {s} _ {e} ^ {\text { inn }}, \mathbf {a} _ {e} ^ {\text { inn }}\right), \quad \text { with   probability } \epsilon , \\ \text { a   random   action }, \quad \text { with   probability } 1 - \epsilon . \end{array} \right. \tag {24}
$$

Q-value is a state-action value, which describes the benefit of an agent performing a particular action in a state. Therefore, the ultimate goal of Q-learning is to appropriately update the Q-table such that the agent obtains the maximum reward. The Q-value in the Q-table can be calculated by

$$
\begin{array}{l} Q (\mathbf {s} _ {e} ^ {\mathrm{inn}}, \mathbf {a} _ {e} ^ {\mathrm{inn}}) \leftarrow Q (\mathbf {s} _ {e} ^ {\mathrm{inn}}, \mathbf {a} _ {e} ^ {\mathrm{inn}}) + \gamma^ {\mathrm{inn}} [ r (\mathbf {s} _ {e} ^ {\mathrm{inn}}, \mathbf {a} _ {e} ^ {\mathrm{inn}}) \\ + \zeta^ {\text { inn }} \max _ {\mathbf {a} _ {e + 1} ^ {\text { inn }}} Q (\mathbf {s} _ {e + 1} ^ {\text { inn }}, \mathbf {a} _ {e + 1} ^ {\text { inn }}) - Q (\mathbf {s} _ {e} ^ {\text { inn }}, \mathbf {a} _ {e} ^ {\text { inn }}) ], \tag {25} \\ \end{array}
$$

where $Q ( \mathbf { s } _ { e } ^ { \mathrm { i n n } } , \mathbf { a } _ { e } ^ { \mathrm { i n n } } )$ is the state-action value, $\zeta ^ { \mathrm { i n n } } \in \{ 0 , 1 \}$ is the discount factor representing the weight of future rewards, and $\gamma ^ { \mathrm { i n n } }$ is the learning rate.

The proposed DLRL algorithm, including the inner layer Qlearnig and outer layer DDPG is presented in Algorithm 1.

Algorithm 1: DLRL Algorithm.   
Input: Episode length $E^{out}$ and $E^{inn}$ , training round T, experience replay buffer O, mini-batch size o, learning rate for actor network $\gamma_{\mu}$ , learning rate for critic network $\gamma_{Q}$ , discount factor $\zeta^{out}$ , learning rate of Q-learning $\gamma^{inn}$ , soft update coefficient $\delta$ ;

Output: Locations of USV clusters $L^{usv}$ , computation offloading decisions $\alpha$ ;

1: Initialize online actor network and online critic network with the weights $\theta^{\mu}$ and $\theta^{Q}$ ;

2: Initialize target actor network and target critic network with the weights $\theta^{\hat{\mu}}$ and $\theta^{\hat{Q}}$ ;

3: Initialize the locations of USV clusters $L_{0}^{usv}$ ;

4: Empty experience replay buffer;

5: for episode = 1 to $E^{out}$ do

6: Inner layer Q-learning ———

7: Initialize $Q(\mathbf{s}^{\mathrm{inn}}, \mathbf{a}^{\mathrm{inn}}) = 0$ ;

8: for e = 1 to $E^{inn}$ do

9: Select an action $a_{e}^{inn}$ according to the $\epsilon$ -greedy policy at state $s_{e}^{inn}$ ;

10: if rand( $\cdot$ ) < $\epsilon$ then

11: Choose the action $a_{e}^{inn}$ that maximizes the Q-value $Q(\mathbf{s}_{e}^{\mathrm{inn}}, \mathbf{a}_{e}^{\mathrm{inn}})$ ;

12: else

13: Randomly select an action $a_{e}^{inn}$ ;

14: end if

15: Execute action $a_{e}^{inn}$ , and calculate the reward value $r(\mathbf{s}_{e}^{\mathrm{inn}}, \mathbf{a}_{e}^{\mathrm{inn}})$ ;

16: Update $Q(\mathbf{s}_{e}^{\mathrm{inn}}, \mathbf{a}_{e}^{\mathrm{inn}})$ by (25);

17: end for

18: Obtain the computation offloading decisions $\alpha$ based on the result of the previous episode;

19: Outer layer DDPG ———

20: Obtain the initial state $s_{1}^{out}$ ;

21: for training round t = 1 to T do

22: Update the state $s_{t}^{out}$ ;

23: Select the action $a_{t}^{out} = \mu(\mathbf{s}_{t}^{\mathrm{out}}|\theta^{\mu}) + \beta$ by the online actor network;

24: Obtain the next state $s_{t+1}^{out}$ and the reward $r_{t}$ based on the state $s_{t}^{out}$ and action $a_{t}^{out}$ ;

25: Store the experience ( $s_{t}^{out}, a_{t}^{out}, r_{t}, s_{t+1}^{out}$ ) in O;

26: Random sample a mini-batch of o experiences ( $s_{j}^{out}, a_{j}^{out}, r_{j}, s_{j+1}^{out}$ ) from O;

27: Update the critic network with (18) and (19);

28: Update the actor network with (20) and (21);

29: Update the weights $\theta^{\hat{\mu}}$ and $\theta^{\hat{Q}}$ by (22) and (23);

30: end for

31: end for

32: Return $L^{usv}, \alpha$ .

# C. Computational Complexity Analysis

In this subsection, we discuss the computational complexity of the proposed DLRL algorithm. For the inner layer, the computational complexity of the Q-learning depends upon the state space size and action space size. Thus, the computational complexity is $\mathcal { O } ( E ^ { \mathrm { i n n } } | \mathbf { s } ^ { \mathrm { i n n } } | | \mathbf { a } ^ { \mathrm { i n n } } | )$ , where $E ^ { \mathrm { i n n } }$ is the total number of episodes in the training process, $\big \vert \mathbf { s } ^ { \mathrm { i n n } } \big \vert$ is the state space size, and $\left| \mathbf { a } ^ { \mathrm { i n n } } \right|$

TABLE II SIMULATION PARAMETERS 

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Deployment area</td><td>10nmile× 10nmile</td></tr><tr><td>The number of vessels, M</td><td>20~45</td></tr><tr><td>The number of USVs, U</td><td>10~36</td></tr><tr><td>The number of tasks per vessel, Im</td><td>5~10</td></tr><tr><td>The computation resource of USV u, Cu</td><td>3GHz</td></tr><tr><td>The computation resource of the cloud center, C0</td><td>100GHz</td></tr><tr><td>Channel bandwidth, B</td><td>1MHz</td></tr><tr><td>Noise power spectral density, σ2</td><td>-114dBm</td></tr><tr><td>The carrier wavelength, l</td><td>0.05m</td></tr><tr><td>The antenna height of USV u, Hu</td><td>5m</td></tr><tr><td>The antenna height of vessel m, Hm</td><td>9.8m</td></tr><tr><td>The transmit power of USV u, Pu</td><td>44.7dBm</td></tr><tr><td>The transmit power of vessel m, Pm</td><td>47dBm</td></tr></table>

is the action space size. For the outer layer, the computational complexity of the DDPG usually depends on the actor and critic networks. The actor network has $L _ { a }$ layers with $F _ { i }$ neurons in the i-th layer $( i \leq L _ { a } )$ . The complexity of the i-th layer is $\mathcal { O } ( F _ { i - 1 } F _ { i } + F _ { i } F _ { i + 1 } )$ . The complexity of the actor network is $\begin{array} { r } { \mathcal { O } ( \sum _ { i = 2 } ^ { L _ { a } - 1 } ( F _ { i - 1 } F _ { i } + F _ { i } F _ { i + 1 } ) ) } \end{array}$ [38]. The critic network has $L _ { c }$ layers with $G _ { j }$ in the j-th layer $( j \leq L _ { c } )$ . The complexity of the j-th layer is $\mathcal { O } ( G _ { j - 1 } G _ { j } + G _ { j } G _ { j + 1 } )$ . The complexity of the critic network is $\begin{array} { r l } {  { \mathcal { O } ( \sum _ { j = 2 } ^ { L _ { c } - 1 } ( G _ { j - 1 } G _ { j } + G _ { j } G _ { j + 1 } ) ) } \qquad } & { { } } \end{array}$ . $\begin{array} { r } { \mathcal { O } ( E ^ { \mathrm { o u t } } T ( \sum _ { i = 2 } ^ { L _ { a } - 1 } ( F _ { i - 1 } F _ { i } + F _ { i } F _ { i + 1 } ) + \sum _ { j = 2 } ^ { L _ { c } - 1 } ( G _ { j - 1 } G _ { j } + } \end{array}$ $G _ { j } G _ { j + 1 } ) ) ) ,$ is O(EoutT ( -La−1i=2 $\begin{array} { r } { \tilde { \mathcal { O } } ( E ^ { \mathrm { o u t } } T ( \sum _ { i = 2 } ^ { L _ { a } - 1 } ( F _ { i - 1 } F _ { i } + F _ { i } F _ { i + 1 } ) + \sum _ { j = 2 } ^ { L _ { c } - 1 } ( G _ { j - 1 } G _ { j } + } \end{array}$ $G _ { j } G _ { j + 1 } ) ) + E ^ { \mathrm { o u t } } E ^ { \mathrm { i n n } } | \mathbf { s } ^ { \mathrm { i n n } } | | \mathbf { a } ^ { \mathrm { i n n } } | )$ .

# V. PERFORMANCE EVALUATION

We develop a simulator in Python to evaluate the performance of the proposed DLRL framework for an MEC-assisted maritime wireless network with multiple USVs as described in Section III. The DLRL algorithm is implemented in TensorFlow. we set $\gamma _ { \mu } = 0 . 0 0 0 1$ and $\gamma _ { Q } = 0 . 0 0 0 1$ as the learning rate for the actor network and the critic network, respectively, and $\gamma ^ { \mathrm { i n n } } = 0 . 0 1$ as the learning rate for the inner layer. Both the actor network and the critic network have three hidden layers with (256,128,64) neurons. The main simulation parameters used in the experiments are listed in Table II, as in [39], [40], [41].

We also implement four benchmark algorithms for performance comparison as follows.

1) Particle Swarm Optimization (PSO) and Greedy (PSO-G) algorithm [42]. We select PSO algorithm as the first benchmark algorithm for performance comparison as it provides a generic solution to handle complex optimization problems with mixed variables. Specifically, a PSO algorithm based on swarm intelligence search is adopted to optimize the locations of USV clusters; and a greedy algorithm is used to optimize the computation offloading decisions. The USV cluster deployment and computation offloading decisions are updated iteratively until a convergence is reached.

![](images/cabd94f5049ba9e0529872676c459f9e71510731f88ed791363826a3bf597fa1.jpg)

<details>
<summary>line</summary>

| The number of USV clusters | DLRL  | PSO-DDQN | DDPG  | PSO-G | DQN   |
| -------------------------- | ----- | -------- | ----- | ----- | ----- |
| 1                          | 5.5   | 6.2      | 6.2   | 6.3   | 7.0   |
| 2                          | 5.1   | 5.9      | 5.8   | 6.0   | 6.7   |
| 3                          | 4.7   | 5.6      | 5.4   | 5.8   | 6.5   |
| 4                          | 4.6   | 5.4      | 5.2   | 5.6   | 6.3   |
| 5                          | 4.5   | 5.3      | 5.1   | 5.5   | 6.1   |
| 6                          | 4.5   | 5.2      | 5.0   | 5.4   | 5.9   |
| 7                          | 4.5   | 5.1      | 4.9   | 5.3   | 5.7   |
| 8                          | 4.5   | 5.0      | 4.8   | 5.2   | 5.6   |
| 9                          | 4.5   | 5.0      | 4.7   | 5.2   | 5.5   |
| 10                         | 4.5   | 5.0      | 4.6   | 5.2   | 5.5   |
| 11                         | 4.5   | 5.0      | 4.6   | 5.2   | 5.5   |
| 12                         | 4.5   | 5.0      | 4.6   | 5.2   | 5.5   |
</details>

Fig. 3. Performance comparison of the expected response time $( M = 4 0$ vessels and $U = 2 4 \mathrm { { U S V s } ) }$ .

2) PSO and Double Deep Q-Network (PSO-DDQN) algorithm [43]. We selected the PSO-DDQN algorithm as the second benchmark due to its effectiveness in addressing MINLP problems. Specifically, the PSO algorithm is employed to optimize the locations of USV clusters, while the DDQN algorithm is utilized to refine the computation offloading decisions. This combined approach optimizes the computation offloading strategies based on the USVs’ locations, iteratively updating until convergence is achieved.

3) Deep Q Network (DQN) algorithm [44]. A deep reinforcement learning algorithm based on Deep Q-Network (DQN) is selected as the third benchmark algorithm due to its high performance in tackling problems with discrete action space. In order to handle mixed action spaces, the actions of USV deployment are discretized, while the action of offloading is set as that in Section IV-A.

4) DDPG algorithm. A deep reinforcement learning algorithm based on DDPG is selected as the fourth benchmark algorithm due to its high performance in tackling problems with continuous action space [45]. To handle the mixed action spaces, the discrete offloading action is approximated in continuous action space, while the continuous actions of USV deployment are set as that in Section IV-A.

Fig. 3 compares the performance of the proposed algorithm with that of the four benchmark algorithms versus different numbers of USV clusters. The number of vessels and USVs are set to $M = 4 0$ and $U = 2 4$ . The computation resource of each USV is 3 GHz. Each vessel carries out a variable number of computation tasks from 5 to 10. It is shown that the proposed learning algorithm outperforms the PSO-G, PSO-DDQN, DQN, and DDPG in terms of the achieved response time. The DDPG uses continuous actions to approximate the discrete offloading decisions, while the DQN algorithm discretizes the actions of USV deployment, resulting in reduced accuracy, compared with the proposed dual-layer learning solution. The PSO-G and PSO-DDQN algorithms involve iterative optimization for both discrete and continuous variables. Generally, PSO-G prioritizes exploration to find the optimal solutions while DDPG and DQN algorithms prioritize exploitation by leveraging learned policies to maximize the rewards. PSO-DDQN algorithm as a form of deep reinforcement learning by incorporating PSO and DDQN for exploration and exploitation. The proposed DLRL algorithm that integrates DDPG and Q-learning to handle the continuous and discrete actions achieves the best performance. It can also be seen that the expected response time decreases when the number of USV clusters increases from 1 to 5, and the decrease rate becomes much slower for $N > 5$ . As the number of USV clusters increases, the distance between the vessel and the USV cluster decreases, which effectively decreases the transmission time. The results suggest that it may not be necessary to deploy each individual USV to the optimal location, and an appropriate number of USV clusters can be determined to facilitate the efficient deployment without notably reducing the network performance.

Fig. 4 studies the performance of the proposed algorithm under different numbers of tasks. The edge computing ratio, defined as the number of computation tasks offloaded to the USVs for edge computing over the total number of tasks, is shown in Fig. 4(a). For $U = 2 4$ and $N = 5 ,$ , when the number of vessels exceeds $M > 2 5$ , some tasks cannot be offloaded to the edge server but have to be forwarded to the remote cloud for data processing, due to the limited computation resources of deployed USVs. Thus, the edge computing ratio decreases with the number of vessels, and the corresponding expected response time increases as shown in Fig. 4(b). We further increase the number of USVs to $U = 3 6$ , and more computation tasks can be offloaded to the USVs with more computation resources, and the edge computing ratio is higher than that with $U = 2 4$ , and a smaller expected response time is achieved correspondingly, as shown in Fig. 4(c).

Fig. 5 studies the impact of the computation resources on the performance of the proposed algorithm. The more computation resources, the more tasks can be offloaded to the edge server to achieve a lower response time. As shown in Fig. 5, when the computation resource is larger than $1 0 0 , \mathrm { i . e . }$ , in the case of $U > 2 0$ and $C _ { u } = 5 \mathrm { G H z }$ , or $U > 2 8$ and $C _ { u } = 4 \mathrm { G H z } .$ , all computation tasks of vessels can be offloaded to the edge servers to attain the minimum expected response time.

The convergence performance of the proposed DLRL algorithm under different numbers of USV clusters and vessels is shown in Fig. 6. In Fig. 6(a), the number of vessels and USVs are set to $M = 1 5$ and $U = 1 0 ,$ , respectively. It is found that the achieved expected response time for $N = 1 0$ is reduced compared with the cases of $N = 1 , 3 , 5$ clusters. It is also observed that the convergence time increases with N due to a larger searching space of the optimal locations. For example, when the number of USV clusters is $N = 1 0$ , the convergence performance increases by about 1100, 800, 600 episodes compared with the cases of $N = 1 , 3 , 5$ , respectively. Similar results can be observed in Fig. 6(b) where the number of vessels and USVs increases to $M = 4 0$ and $U = 2 4$ , respectively. Compared with the case of $N = 5$ , the expected response time for $N = 1 0$ is reduced by 1.8% at the cost of increased convergence time. In a large scale IoV networks with a high number of vessels and USVs, clustering provides an efficient and scalable solution to strike a balance between the response time and the convergence time.

Fig. 7 compares the convergence performance of the proposed four learning algorithms, i.e., DLRL, PSO-DDQN, DDPG, and $\mathrm { D Q N } . ^ { 2 }$ The proposed DLRL algorithm typically converges in about 400 episodes, while the DDPG algorithm requires approximately 800 episodes to converge. In addition, the final accumulated reward of the DLRL algorithm is slightly higher

![](images/8daeaf92ccaf478a99bd180b48c1b6572e3249c29ae53334631d9da1b10c2991.jpg)

<details>
<summary>line</summary>

| The number of vessels | U=24 | U=36 |
| --------------------- | ---- | ---- |
| 20                    | 100  | 100  |
| 25                    | 100  | 100  |
| 30                    | 93   | 100  |
| 35                    | 83   | 100  |
| 40                    | 70   | 100  |
| 45                    | 67   | 98   |
</details>

![](images/317bc58c9667dd9d75177d0778c9fcc9529b2f61c261928dfd001a2bd8d7827b.jpg)

<details>
<summary>line</summary>

| The number of vessels | DLRL  | PSO-DDQN | DDPG  | DQN   | PSO-G |
| --------------------- | ----- | -------- | ----- | ----- | ----- |
| 20                    | 3.25  | 4.05     | 3.75  | 4.60  | 4.25  |
| 25                    | 3.35  | 4.15     | 3.80  | 4.65  | 4.35  |
| 30                    | 3.60  | 4.60     | 4.25  | 5.10  | 4.80  |
| 35                    | 4.00  | 5.00     | 4.65  | 5.55  | 5.20  |
| 40                    | 4.50  | 5.40     | 5.10  | 6.10  | 5.50  |
| 45                    | 4.90  | 5.90     | 5.50  | 6.30  | 6.00  |
</details>

(b)

![](images/c17ab9688d57ec152a45412c10225e5247ddbe7adba734a6ea4e1967e8b0ecdc.jpg)

<details>
<summary>line</summary>

| The number of vessels | DLRL  | PSO-DDQN | DDPG  | DQN   | PSO-G |
| --------------------- | ----- | -------- | ----- | ----- | ----- |
| 20                    | 3.2   | 3.9      | 3.5   | 4.3   | 4.1   |
| 25                    | 3.25  | 3.95     | 3.55  | 4.35  | 4.15  |
| 30                    | 3.3   | 4.0      | 3.6   | 4.4   | 4.2   |
| 35                    | 3.35  | 4.05     | 3.65  | 4.45  | 4.25  |
| 40                    | 3.4   | 4.1      | 3.7   | 4.5   | 4.3   |
| 45                    | 3.6   | 4.3      | 3.9   | 4.7   | 4.5   |
</details>

（c）  
Fig. 4. Performance study of the edge computing ratio and expected response time $( N = 5 \mathrm { U S V }$ clusters). (a) Edge computing ratio. (b) Expected response time $( U = 2 4 { \mathrm { U S V s } } )$ . (c) Expected response time $( U = \dot { 3 } 6 \mathrm { U S V s } )$ .

2The converge performance of PSO-G is not presented as PSO-G is not typically based on rewards as the reinforcement learning algorithms.

![](images/c93f8863e0dac6b262abf76ec2cff564e66ba81fe9f9a6496be70c93ee7e6a3f.jpg)

<details>
<summary>line</summary>

| The number of USVs | Cu=3GHz | Cu=4GHz | Cu=5GHz |
| ------------------ | ------- | ------- | ------- |
| 16                 | 50      | 68      | 83      |
| 20                 | 65      | 80      | 100     |
| 24                 | 70      | 98      | 100     |
| 28                 | 83      | 100     | 100     |
| 32                 | 95      | 100     | 100     |
</details>

(a)

![](images/4f8f2729c837fe0907a98d7e6cfd8cf37dd660dda299ea44bcfd714db55a3381.jpg)

<details>
<summary>bar</summary>

| Number of USV clusters | Expected response time (s) |
| ---------------------- | -------------------------- |
| 1                      | 5.5                        |
| 3                      | 4.7                        |
| 5                      | 4.5                        |
| 10                     | 4.4                        |
</details>

![](images/a6c212a70fdfe375b2044197afea6f6c87948acf569f05a35084fcbca827858d.jpg)

<details>
<summary>line</summary>

| Number of episodes | N=10 | N=5 | N=3 | N=1 |
| ------------------ | ---- | --- | --- | --- |
| 0                  | 30   | 30  | 30  | 30  |
| 500                | 60   | 45  | 40  | 35  |
| 1000               | 60   | 45  | 40  | 35  |
| 1500               | 60   | 45  | 40  | 35  |
</details>

(a)

![](images/aa0d2050596385d79d0cde9e2507a265c0bbf1876ef0e4fffbe395359cad399a.jpg)

<details>
<summary>line</summary>

| The number of USVs | Cu=3GHz | Cu=4GHz | Cu=5GHz |
| ------------------ | ------- | ------- | ------- |
| 16                 | 5.3     | 4.7     | 4.2     |
| 20                 | 4.8     | 4.4     | 3.85    |
| 24                 | 4.5     | 4.0     | 3.8     |
| 28                 | 4.25    | 3.85    | 3.8     |
| 32                 | 4.0     | 3.8     | 3.8     |
</details>

(b)

![](images/94b020b4a672d2b52057d9a964b477332bb364d07135b5cbc04458ff78ddd0c2.jpg)

<details>
<summary>bar</summary>

| Number of USV clusters | Expected response time (s) |
| ---------------------- | -------------------------- |
| 1                      | 5.1                        |
| 3                      | 4.5                        |
| 5                      | 4.2                        |
| 10                     | 4.1                        |
</details>

![](images/111d8b00637bc7e100243ef47648a045eba202e2261cadafe36c6d76f273b845.jpg)

<details>
<summary>line</summary>

| Number of episodes | N=10 | N=5 | N=3 | N=1 |
| ------------------ | ---- | --- | --- | --- |
| 0                  | 20   | 20  | 20  | 20  |
| 500                | 45   | 45  | 40  | 34  |
| 1000               | 48   | 46  | 42  | 34  |
| 1500               | 49   | 47  | 43  | 34  |
</details>

(b)   
Fig. 5. The impact of the computation resources $( M = 4 0$ vessels and $N = 5$ USV clusters). (a) Edge computing ratio. (b) Expected response time.   
Fig. 6. Convergence performance versus different numbers of USV clusters and vessels. (a) $\tilde { M } = 1 \dot { 5 }$ vessels, $U = 1 0 \mathrm { U S V s }$ . (b) $M = 2 4$ vessels, $U = 4 0$ USVs.

than that of the DDPG algorithm because the DDPG approximates the discrete offloading action in continuous action space, resulting in reduced accuracy. Although the DQN algorithm achieves a good convergence performance, the accumulated reward learned from the DQN is lower than that of the DLRL, as DQN discretizes the continuous action space which results in performance degradation. For the PSO-DDQN algorithm, the convergence performance is inferior to that of the DLRL, as the incorporation of PSO increases the complexity of exploration, which ultimately degrades overall performance. The proposed DLRL algorithm achieves the highest rewards with good convergence performance compared to PSO-DDQN, DDPG and DQN primarily due to its effective handling of hybrid actions.

# VI. CONCLUSION

In this paper, we have studied the mobile edge deployment and resource management for MEC-assisted maritime wireless networks, where USVs with computation resources are deployed to provide edge computation services for vessels. A dual-layer reinforcement learning framework has been proposed to optimize the deployment of USVs and computation offloading decisions. Simulation results have demonstrated that the USV cluster deployment provides an efficient and scalable solution for large scale maritime wireless networks with a high number of USVs and vessels. Compared with four benchmark algorithms in the literature, the proposed DLRL algorithm has achieved a significant improvement in reducing the expected response time. In the future, we will further study the computation offloading in a heterogeneous MEC-assisted maritime wireless network with different types of tasks with different QoS requirements.

![](images/3ca0edc17c1befdef918bd337b46922e7cff74d90bda1842314a48f6edab25e8.jpg)

<details>
<summary>line</summary>

| Number of episodes | DDPG | DQN | PSO-DDQN | DLRL |
| ------------------ | ---- | --- | -------- | ---- |
| 0                  | 30   | 25  | 25       | 25   |
| 500                | 38   | 35  | 24       | 40   |
| 1000               | 37   | 36  | 35       | 41   |
| 1500               | 38   | 37  | 36       | 42   |
</details>

Fig. 7. Convergence performance of DLRL, PSO-DDQN, DDPG and DQN algorithms.

# REFERENCES

[1] L. Lyu, Z. Chu, B. Lin, Y. Dai, and N. Cheng, “Fast trajectory planning for UAV-enabled maritime IoT systems: A fermat-point based approach,” IEEE Wireless Commun. Lett., vol. 11, no. 2, pp. 328–332, Feb. 2022.   
[2] B. Lin, J. Duan, M. Han, and L. X. Cai, Next Generation Marine Wireless Communication Networks. Cham, Switzerland: Springer, 2022.   
[3] T. Wei, W. Feng, Y. Chen, C.-X. Wang, N. Ge, and J. Lu, “Hybrid satelliteterrestrial communication networks for the maritime Internet of Things: Key technologies, opportunities, and challenges,” IEEE Internet Things J., vol. 8, no. 11, pp. 8910–8934, Nov. 2022.   
[4] H. Song, B. Gu, K. Son, and W. Choi, “Joint optimization of edge computing server deployment and user offloading associations in wireless edge network via a genetic algorithm,” IEEE Trans. Netw. Sci. Eng., vol. 9, no. 4, pp. 2535–2548, Apr. 2023.   
[5] X. Zhang, Z. Li, C. Lai, and J. Zhang, “Joint edge server placement and service placement in mobile-edge computing,” IEEE Internet Things J., vol. 9, no. 13, pp. 11261–11274, Jul. 2022.   
[6] W. Fan, L. Yao, J. Han, F. Wu, and Y. Liu, “Game-based multitype task offloading among mobile-edge-computing-enabled base stations,” IEEE Internet Things J., vol. 8, no. 24, pp. 17691–17704, Dec. 2022.   
[7] K. Cao, L. Li, Y. Cui, T. Wei, and S. Hu, “Exploring placement of heterogeneous edge servers for response time minimization in mobile edgecloud computing,” IEEE Trans. Ind. Inform., vol. 17, no. 1, pp. 494–503, Jan. 2022.   
[8] Z. Tang, K. Yu, G. Yang, L. X. Cai, and H. Zhou, “New bridge to cloud: An ultra-dense leo assisted green computation offloading approach,” IEEE Trans. Green Commun. Netw., vol. 7, no. 2, pp. 552–564, Feb. 2024.   
[9] B. Cao et al., “Large-scale many-objective deployment optimization of edge servers,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 6, pp. 3841–3849, Jun. 2021.   
[10] Y. Wu, L. P. Qian, K. Ni, C. Zhang, and X. Shen, “Delay-minimization nonorthogonal multiple access enabled multi-user mobile edge computation offloading,” IEEE J. Sel. Topics Signal Process., vol. 13, no. 3, pp. 392–407, Mar. 2019.   
[11] Y. Luo, W. Ding, and B. Zhang, “Optimization of task scheduling and dynamic service strategy for multi-UAV-enabled mobile-edge computing system,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 3, pp. 970–984, Mar. 2021.   
[12] H. Zhou, K. Jiang, X. Liu, X. Li, and V. C. M. Leung, “Deep reinforcement learning for energy-efficient computation offloading in mobile-edge computing,” IEEE Internet Things J., vol. 9, no. 2, pp. 1517–1530, Jan. 2022.   
[13] J.-B. Wang, C. Zeng, C. Ding, H. Zhang, M. Lin, and J. Wang, “Unmanned surface vessel assisted maritime wireless communication toward 6 G: Opportunities and challenges,” IEEE Wireless Commun., vol. 29, no. 6, pp. 72–79, Jun. 2022.   
[14] C. Tang, H.-T. Zhang, and J. Wang, “Flexible formation tracking control of multiple unmanned surface vessels for navigating through narrow channels with unknown curvatures,” IEEE Trans. Ind. Electron., vol. 70, no. 3, pp. 2927–2938, Mar. 2023.   
[15] Z. Peng, D. Wang, Z. Chen, X. Hu, and W. Lan, “Adaptive dynamic surface control for formations of autonomous surface vehicles with uncertain dynamics,” IEEE Trans. Control Syst. Technol., vol. 21, no. 2, pp. 513–520, Feb. 2013.   
[16] T. Zhang, J. Lei, Y. Liu, C. Feng, and A. Nallanathan, “Trajectory optimization for UAV emergency communication with limited user equipment energy: A safe-DQN approach,” IEEE Trans. Green Commun. Netw., vol. 5, no. 3, pp. 1236–1247, Mar. 2022.

[17] Y.-J. Chen and D.-Y. Huang, “Joint trajectory design and BS association for cellular-connected UAV: An imitation-augmented deep reinforcement learning approach,” IEEE Internet Things J., vol. 9, no. 4, pp. 2843–2858, Apr. 2023.   
[18] L. Wang, H. Zhang, S. Guo, and D. Yuan, “Deployment and association of multiple UAVs in UAV-assisted cellular networks with the knowledge of statistical user position,” IEEE Trans. Wireless Commun., vol. 21, no. 8, pp. 6553–6567, Aug. 2022.   
[19] S. Zhang, W. Liu, and N. Ansari, “Completion time minimization for data collection in a UAV-enabled IoT network: A deep reinforcement learning approach,” IEEE Trans. Veh. Technol., vol. 72, no. 11, pp. 14734–14742, Nov. 2023.   
[20] Z. Zhao, J. Shi, Z. Li, J. Si, P. Xiao, and R. Tafazolli, “Matching-aidedlearning resource allocation for dynamic offloading in mmWave MEC system,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 7580–7591, Nov. 2023.   
[21] S. F. Abedin, A. Mahmood, N. H. Tran, Z. Han, and M. Gidlund, “Elastic O-RAN slicing for industrial monitoring and control: A distributed matching game and deep reinforcement learning approach,” IEEE Trans. Veh. Technol., vol. 71, no. 10, pp. 10808–10822, Oct. 2022.   
[22] Y. Dai, D. Xu, S. Maharjan, and Y. Zhang, “Joint computation offloading and user association in multi-task mobile edge computing,” IEEE Trans. Veh. Technol., vol. 67, no. 12, pp. 12313–12325, Dec. 2018.   
[23] L. Ale, N. Zhang, X. Fang, X. Chen, S. Wu, and L. Li, “Delay-aware and energy-efficient computation offloading in mobile-edge computing using deep reinforcement learning,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 3, pp. 881–892, Mar. 2021.   
[24] Y. Gao, J. Tao, H. Wang, Z. Wang, W. Sun, and C. Song, “Joint server deployment and task scheduling for the maximal profit in mobile-edge computing,” IEEE Internet Things J., vol. 10, no. 24, pp. 22501–22513, Dec. 2023.   
[25] T. K. Rodrigues, K. Suto, and N. Kato, “Edge cloud server deployment with transmission power control through machine learning for 6 G Internet of Things,” IEEE Trans. Emerg. Topics Comput., vol. 9, no. 4, pp. 2099–2108, Apr. 2021.   
[26] S. K. Kasi et al., “Heuristic edge server placement in industrial Internet of Things and cellular networks,” IEEE Internet Things J., vol. 8, no. 13, pp. 10308–10317, Jul. 2020.   
[27] J. Zhang, J. Lu, X. Yan, X. Xu, L. Qi, and W. Dou, “Quantified edge server placement with quantum encoding in internet of vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 7, pp. 9370–9379, Jul. 2022.   
[28] J. Zhang et al., “Stochastic computation offloading and trajectory scheduling for UAV-assisted mobile edge computing,” IEEE Internet Things J., vol. 6, no. 2, pp. 3688–3699, Feb. 2019.   
[29] H. Guo and J. Liu, “UAV-enhanced intelligent offloading for Internet of Things at the edge,” IEEE Trans. Ind. Inform., vol. 16, no. 4, pp. 2737–2746, Apr. 2020.   
[30] H. Peng and X. Shen, “Multi-agent reinforcement learning based resource management in MEC- and UAV-assisted vehicular networks,” IEEE J. Sel. Areas Commun., vol. 39, no. 1, pp. 131–141, Jan. 2021.   
[31] P. Qin, Y. Fu, J. Zhang, S. Geng, J. Liu, and X. Zhao, “DRL-based resource allocation and trajectory planning for NOMA-enabled multi-UAV collaborative caching 6 G network,” IEEE Trans. Veh. Technol., vol. 73, no. 6, pp. 8750–8764, Jun. 2024.   
[32] Z. Han, T. Zhou, T. Xu, and H. Hu, “Joint user association and deployment optimization for delay-minimized UAV-aided MEC networks,” IEEE Wireless Commun. Lett., vol. 12, no. 10, pp. 1791–1795, Oct. 2023.   
[33] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and L. Hanzo, “Multi-agent deep reinforcement learning-based trajectory planning for multi-UAV assisted mobile edge computing,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 1, pp. 73–84, Mar. 2021.   
[34] C. Zeng, J.-B. Wang, C. Ding, H. Zhang, M. Lin, and J. Cheng, “Joint optimization of trajectory and communication resource allocation for unmanned surface vehicle enabled maritime wireless networks,” IEEE Trans. Commun., vol. 69, no. 12, pp. 8100–8115, Dec. 2021.   
[35] C. Zeng, J.-B. Wang, C. Ding, M. Lin, and J. Wang, “MIMO unmanned surface vessels enabled maritime wireless network coexisting with satellite network: Beamforming and trajectory design,” IEEE Trans. Commun., vol. 71, no. 1, pp. 83–100, Jan. 2023.   
[36] M. Li, L. P. Qian, X. Dong, B. Lin, Y. Wu, and X. Yang, “Secure computation offloading for marine IoT: An energy-efficient design via cooperative jamming,” IEEE Trans. Veh. Technol., vol. 72, no. 5, pp. 6518–6531, May 2023.   
[37] X. Wang, T. Jin, L. Hu, and Z. Qian, “Energy-efficient power allocation and q-learning-based relay selection for relay-aided D2D communication,” IEEE Trans. Veh. Technol., vol. 69, no. 6, pp. 6452–6462, Jun. 2020.

[38] X. Yuan, S. Hu, W. Ni, R. P. Liu, and X. Wang, “Joint user, channel, modulation-coding selection, and RIS configuration for jamming resistance in multiuser OFDMA systems,” IEEE Trans. Commun., vol. 71, no. 3, pp. 1631–1645, Mar. 2023.   
[39] L. P. Qian, H. Zhang, Q. Wang, Y. Wu, and B. Lin, “Joint multi-domain resource allocation and trajectory optimization in UAV-assisted maritime IoT networks,” IEEE Internet Things J., vol. 10, no. 1, pp. 539–552, Jan. 2022.   
[40] N. Su, J.-B. Wang, C. Zeng, H. Zhang, M. Lin, and G. Y. Li, “Unmannedsurface-vehicle-aided maritime data collection using deep reinforcement learning,” IEEE Internet Things J., vol. 9, no. 20, pp. 19773–19786, Oct. 2022.   
[41] N. Cheng et al., “Space/aerial-assisted computing offloading for IoT applications: A learning-based approach,” IEEE J. Sel. Areas Commun., vol. 37, no. 5, pp. 1117–1129, Mar. 2019.   
[42] Z. Chen, H. Zheng, J. Zhang, X. Zheng, and C. Rong, “Joint computation offloading and deployment optimization in multi-UAV-enabled MEC systems,” Peer-to-Peer Netw. Appl., vol. 1, no. 15, pp. 194–205, 2022.   
[43] H. Sun, J. Wang, D. Yong, M. Qin, and N. Zhang, “Deep reinforcement learning-based computation offloading for mobile edge computing in 6 G,” IEEE Trans. Consum. Electron., vol. 70, no. 4, pp. 7482–7493, Nov. 2024.   
[44] V. Mnih et al., “Playing atari with deep reinforcement learning,” 2013, arXiv:1312.5602.   
[45] T. Zhang, K. Zhu, and J. Wang, “Energy-efficient mode selection and resource allocation for D2D-enabled heterogeneous networks: A deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 1175–1187, Feb. 2021.

![](images/6ac06d661861eecf00ee3f44df855f58caefffd73ae0774128a655df71b99c24.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman in a white collared shirt against a solid blue background (no text or symbols visible)
</details>

Chaoyue Zhang ( Member, IEEE) received the B.S. degree from Wuhan University of Science and Technology, Wuhan, China, in 2017, and the M.S. degree from Dalian Maritime University, Dalian, China, in 2020, where she is currently working toward the Ph.D. degree with the Information Science and Technology College. Her research interests include maritime communication networks, mobile edge computing, and resource management.

![](images/93cd637d488d3aa8880e763683ad2e9fc400b3019aca348d77cb6d488bc313e9.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman in a black collared shirt (no text or symbols visible)
</details>

Bin Lin (Senior Member, IEEE) received the B.S. and M.S. degrees from Dalian Maritime University, Dalian, China, in 1999 and 2003, respectively and the Ph.D. degree from the Broadband Communications Research Group, Department of Electrical and Computer Engineering, University of Waterloo, Waterloo, ON, Canada, in 2009. She is currently a Full Professor and the Dean of Communication Engineering with the College of Information Science and Technology, Dalian Maritime University. She has been a Visiting Scholar with George Washington University,

Washington, DC, USA, from 2015 to 2016. Her research interests include wireless communications, network dimensioning and optimization, resource allocation, artificial intelligence, maritime communication networks, edge/cloud computing, wireless sensor networks, and Internet of Things. She is an Associate Editor of IEEE TRANSACTION ON VEHICULAR TECHNOLOGY and IET Communications.

![](images/7060a49fdaefa033890e8f1b5a600623da6c369cab14234b8f5bbf865332d70a.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Ziru Chen (Graduate Student Member, IEEE) received the B.E. degree in automation from Hunan University, Changsha, China, in 2014, and the M.S. degree in electric engineering from Illinois Institute of Technology, Chicago, IL, USA, in 2017, where he is currently working toward the Ph.D. degree with the Department of Electrical and Computer Engineering. His research interests include RF energy harvesting, stochastic geometry, nonorthogonal multiple access, and AI-assisted wireless networking.

![](images/5416363dfc37a1446eabf95b460d9e6ee77d7d8134e70d97f410347f2c31dbf2.jpg)

<details>
<summary>natural_image</summary>

Portrait of a woman with short dark hair wearing a collared sweater (no text or symbols visible)
</details>

Lin X. Cai (Senior Member, IEEE) received the M.A.Sc. and Ph.D. degrees in electrical and computer engineering from the University of Waterloo, Waterloo, ON, Canada, in 2005 and 2010, respectively. She is currently an Associate Professor with the Department of Electrical and Computer Engineering, Illinois Institute of Technology, Chicago, IL, USA. Her research interests include green communication and networking, intelligent radio resource management, and wireless Internet of Things. She was the recipient of the Best Paper Award from the IEEE

Globecom 2011, an NSF Career Award in 2016, IIT Sigma Xi Research Award in the Junior Faculty Division in 2019, and the N2Women Stars award in Computer Networking and Communiations in 2021. She is a Executive Editorial Committee Member of IEEE TRANSACTION ON WIRELESS COMMUNICATIONS, and an Associate Editor of IEEE TRANSACTION ON VEHICULAR TECHNOLOGIES, and a co-chair for IEEE conferences.

![](images/087f3c74b1f48082a0f8df06c8fa446dbd6c91b3d92c624e52f241a816ad8f3c.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a woman with shoulder-length dark hair against a blue background (no text or symbols visible)
</details>

Jianli Duan received the M.S. and Ph.D. degrees from Dalian Maritime University, Dalian, China, in 2003 and 2020, respectively. She is currently an Associate Professor in School of Science, Qingdao University of Technology, Qingdao, China. Her research interests include maritime telecommunications and networking, wireless sensor networks, and network planning and optimization.