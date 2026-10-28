# Latency Minimization Oriented Radio and Computation Resource Allocations for 6G V2X Networks With ISCC

Peng Liu , Graduate Student Member, IEEE, Xinyi Wang , Member, IEEE, Zesong Fei , Senior Member, IEEE, Yuan Wu , Senior Member, IEEE, Jie Xu , Fellow, IEEE, and Arumugam Nallanathan , Fellow, IEEE

Abstract—Incorporating mobile edge computing (MEC) and integrated sensing and communication (ISAC) has emerged as a promising technology to enable integrated sensing, communication, and computing (ISCC) in the sixth generation (6G) networks. ISCC is particularly attractive for vehicle-toeverything (V2X) applications, where vehicles perform ISAC to sense the environment and simultaneously offload the sensing data to roadside base stations (BSs) for remote processing. In this paper, we investigate a particular ISCC-enabled V2X system consisting of multiple multi-antenna BSs serving a set of singleantenna vehicles, in which the vehicles perform their respective ISAC operations (for simultaneous sensing and offloading to the associated BS) over orthogonal sub-bands. With the focus on fairly minimizing the sensing completion latency for vehicles while ensuring the detection probability constraints, we jointly optimize the allocations of radio resources (i.e., the sub-band allocation, transmit power control at vehicles, and receive beamforming at BSs) as well as computation resources at BS MEC servers. To solve the formulated complex mixed-integer nonlinear programming (MINLP) problem, we propose an alternating optimization algorithm. In this algorithm, we determine the sub-band allocation via the branch-and-bound method, optimize the transmit power control via successive convex approximation (SCA), and derive the receive beamforming and computation

Received 20 July 2025; accepted 22 September 2025. Date of publication 1 October 2025; date of current version 23 December 2025. This work was supported in part by the National Natural Science Foundation of China under Grant No. 62301032, 62471039, 62471424, 92267202, the Science and Technology Development Fund of Macau SAR under Grant FDCT 0158/2022/A, the Basic Research Project No. HZQB-KCZYZ-2021067 of Hetao Shenzhen-HK S&T Cooperation Zone, the Guangdong Provincial Key Laboratory of Future Networks of Intelligence under grant No. 2022B1212010001, and the Guangdong Major Project of Basic and Applied Basic Research (No. 2023B0303000001). The associate editor coordinating the review of this article and approving it for publication was S. Buzzi. (Corresponding author: Xinyi Wang.)

Peng Liu, Xinyi Wang, and Zesong Fei are with the School of Information and Electronics, Beijing Institute of Technology, Beijing 100081, China (e-mail: bit peng liu@163.com; bit wangxy@163.com; feizesong@bit. edu.cn).

Yuan Wu is with the State Key Laboratory of Internet of Things for Smart City and the Department of Computer and Information Science, University of Macau, Macau, SAR, China (e-mail: yuanwu@um.edu.mo).

Jie Xu is with the School of Science and Engineering (SSE), Shenzhen Future Network of Intelligence Institute (FNii-Shenzhen), and Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong at Shenzhen, Shenzhen, Guangdong 518172, China (e-mail: xujie@cuhk.edu.cn).

Arumugam Nallanathan is with the School of Electronic Engineering and Computer Science, Queen Mary University of London, E1 4NS London, U.K., and also with the Department of Electronic Engineering, Kyung Hee University, Yongin-si, Gyeonggi-do 17104, South Korea (e-mail: a.nallanathan@qmul.ac.uk).

Digital Object Identifier 10.1109/TCOMM.2025.3616242 resource allocation at BSs in closed form based on generalized Rayleigh entropy and fairness criteria, respectively. Simulation results demonstrate that the proposed joint resource allocation design significantly reduces the maximum task completion latency among all vehicles. Furthermore, we also demonstrate several interesting trade-offs between the system performance and resource utilizations.

Index Terms—Integrated sensing and communication (ISAC), mobile edge computing (MEC), vehicle-to-everything (V2X), resource allocation.

## I. INTRODUCTION

expected to support various emerging applications, and autonomous driving is among the most prominent ones. Towards this end, vehicles need to be equipped with sensing capabilities to monitor the environment and make swift decisions for autonomous operation. To fulfill the high sensing, communication, and computation needs at vehicles, vehicleto-everything (V2X) in 6G is particularly appealing, in which the vehicles and roadside base stations (BSs) can cooperate in sensing, communication, and computation [1]. Integrated sensing and communication (ISAC) and mobile edge computation (MEC) are becoming two important 6G technologies to support such operations in V2X networks.

ISAC has been recognized by the International Telecommunication Union Radio communication Sector (ITU-R) as a foundational technology for 6G [2], enabling future wireless terminals and cellular BSs to support both high-speed data transmission and high-precision environmental sensing. By jointly designing the sensing and communication functions on shared spectrum and hardware platforms, ISAC can significantly enhance both the spectral and energy efficiency with reduced hardware costs. On the other hand, the increasing volume of sensing data and the advancements of various signal processing and artificial intelligence (AI) algorithms pose new challenges in meeting strict low-latency requirements in V2X scenarios. For example, an autonomous vehicle must detect and respond to a sudden obstacle within tens of milliseconds to ensure driving safety [3], which imposes stringent demands on both computation and communication capabilities. To address this, MEC has emerged as a promising solution to process large amounts of data [4] and support advanced computationintensive sensing signal processing, such as spatial spectrum estimation [5] and deep learning-based algorithms [6]. While vehicles may only have limited on-board computing power and energy, MEC enables them to offload such computationintensive tasks to the network edge or cloud for remote processing, achieving high-accuracy and low-latency outcomes [7]. Consequently, integrating ISAC with MEC has been considered as a promising approach for integrating sensing, communication, and computing (ISCC) to support emerging V2X applications.

The emergence of ISCC raises new challenges in the joint radio and computation resource allocations, especially when the resources are distributed at different nodes and the sensing requests and computation requests are space- and timevarying. For example, an aggressive power control scheme for sensing might cause severe interference towards communication and a bandwidth allocation scheme that benefits offloading rates may cause significant interference among sensing nodes. Therefore, proper resource allocation is important for realizing the full potential of ISCC.

## A. Related Works

1) Resource Allocation in ISAC Systems: There have been extensive works studying resource allocation in ISAC systems from different perspectives on time, bandwidth, and power resources. The authors of [8] proposed a dynamic frame structure based on for time-division ISAC V2X systems, allowing all vehicles to coordinately allocate time ratios according to their different requests for sensing and communication, thus reducing communication delay. For bandwidth and power allocations, the authors of [9] proposed an algorithm based on cyclic minimization, which jointly optimizes the subcarrier selection and power allocation to effectively reduce the power consumption while meeting the requirements on sensing mutual information (MI) and communication rate. In [10], dynamic power allocation in ISAC V2X networks was studied, with a stochastic programming problem formulated to maximize sensing MI. Simulation results showed improved trade-offs between sensing MI and communication rate. Additionally, the authors of [11] investigated trajectory optimization and power allocation in an autonomous aerial vehicles (AAVs)-enabled ISAC system, formulating a novel sensing-constrained rate maximization problem to achieve a better trade-off between sensing beampattern gain and communication rate.

2) Resource Allocation in MEC Systems: Research on resource allocation in MEC systems have primarily focused on coordinating bandwidth, power, and computation resources among terminals and MEC servers, with the objective of optimizing the computation performance. The authors of [12] considered the bandwidth resource allocation problem and proposed an iterative algorithm to minimize device energy consumption. Regarding power allocation, the authors of [13] and [14] proposed two iterative algorithms to reduce the minimum task delay of devices by optimizing the transmission power. Furthermore, the authors of [15] jointly optimized the computing offloading strategy, the allocation of computational resources at MEC servers, and the transmit power of devices to minimize the weighted sum latency. In addition, in [16], resource allocation for AAV-enabled MEC has been investigated. An iterative algorithm has been proposed for jointly optimizing AAV positioning, terminal transmission power, and MEC server computation resources, with the aim of reducing the energy consumption of AAVs.

3) Resource Allocation in ISCC Systems: There have only been a handful of prior works investigating the resource allocation for ISCC. The authors of [17] proposed a cloud–edge–device collaborative three-tier ISCC framework, where the overall processing latency of sensing tasks is reduced by optimizing the beamforming vectors and transmit power at the terminals. In [18], the authors studied sub-channel allocation in ISCC systems and proposed an iterative matching algorithm to enhance the overall network utility. In [19], the authors explored a weighted optimization problem involving sensing MI and computation latency in ISCC systems, proposing a radio and computing resource allocation method based on the multi-agent actor-attention-critic model. Simulation results showed the trade-off between sensing MI and computation latency. The authors of [20] focused on ISCC-V2X networks, with the aim of improving the completion rate of cooperative sensing tasks via the joint optimization of bandwidth and edge computation resources. To examine the impacts of computation resources and power allocation on ISCC performance, the authors of [21] developed a multi-objective optimization approach to balance the energy consumption, offloading delay, and signal-to-interference-plus-noise ratio (SINR) for sensing. In [22], the authors studied a cooperative ISCC-V2X system and proposed a proximal policy optimization algorithm to optimize bandwidth, power, and computational resource allocation, with the aim of minimizing vehicle energy consumption. In [23], the authors addressed the power and computation resource allocation problem in ISCC-V2X and proposed a multi-agent deep deterministic policy gradientbased algorithm to reduce long-term average delay across vehicles. The authors of [24] investigated resource allocation in a non-orthogonal multiple access (NOMA)-aided ISCC system, considering both partial and binary offloading strategies. They jointly optimized the computational resources of MEC servers and the transmission power of terminals to enhance overall offloading rate. In [25], the authors investigated an MEC-aided ISAC system with short-packet transmissions, where ISAC beamforming matrices, short packet size, and computing resource allocation at the MEC server were jointly optimized to minimize the overall system energy consumption. offloading, in which the energy consumption of AAVs is minimized via jointly optimizing AAV trajectories and power allocation.

## B. Motivation and Contributions

Existing works on ISCC resource allocation primarily have focused on single-dimensional resource allocation design (e.g., bandwidth or power) [17], [18], or joint allocation of power and computation resources [19], [20], [21], [22], [23], [24], [25], with few studies exploring multi-dimensional resource allocation. Proper multi-dimensional resource allocation, including bandwidth, power, computation resource, and receive beamforming, can not only enhance the overall performance of the ISCC network, but also provide greater design flexibility for balancing multiple objectives (e.g., sensing accuracy, computing latency, and communication rate) and ensuring fairness in optimizing sensing and computing performance among terminals.

Despite the above advantages, multi-dimensional resource allocation presents significant challenges. On one hand, the consideration of more resources leads to greater conflicts and coupling among communication, sensing, and computation. For example, both sensing and computation require higher power to achieve better echo SINR and lower task computation latency, respectively, and both functions also need effective sub-band allocation to mitigate interference. Balancing these conflicting resource demands is a key challenge in resource allocation design. On the other hand, multi-dimensional resource allocation increases the complexity of performance optimization. The joint optimization must account for inherent heterogeneity, such as varying computing capabilities of MEC servers and terminals, differing computation task demands, and diverse sensing requirements. Together with the complex interdependencies among resources, this adds another challenge.

Motivated by this, we investigate an ISCC V2X system consisting of a number of multi-antenna BSs and single-antenna vehicles, in which the vehicles perform their respective ISAC operations (for simultaneous sensing and offloading to the associated BS) over orthogonal sub-bands. We study the joint radio (e.g., the sub-band allocation, transmit power at vehicles, and receive beamforming at BSs) and computation resource allocation to optimize the performance of sensing tasks, while ensuring vehicle detection performance for sensing. Unlike existing ISCC resource allocation studies that integrate learning-based methods [19], [22], [23], which require large amounts of data and long training periods, we propose a fully optimization-based resource allocation method, which avoids these challenges and ensures more predictable performance with lower computational complexity. The main contributions are summarized as follows.

• Under the above setup, we formulate a joint optimization problem to minimize the maximum completion latency of sensing tasks across all vehicles under the constraints of detection probability and power budget, through a design of joint radio and computation resource allocations. The sensing-performance-constrained latency minimization is a mixed-integer nonlinear programming (MINLP) problem that is generally difficult to handle.  
• We propose an alternating optimization algorithm to address the MINLP problem. Firstly, we propose a novel branch-and-bound (BnB) algorithm to decide the sub-band allocation. In particular, we first introduce a sensing-centric greedy algorithm to generate a global bound for the sub-band allocation problem, and then use it along with sensing constraints to assist the branch pruning, thus effectively reducing the complexity. For the power control optimization, we employ the successive convex approximation (SCA) technique to reformulate the non-convex sub-problems as solvable convex forms. Subsequently, we derive the closed-form solutions for both BSs’ receive beamforming and MEC computation

![](images/c63bdd8a10b027313544c736daec5b647b55de87f75fdd803e97d0087cabc9f2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["BS"] --> B["MEC server"]
  B --> C["Echo signal"]
  C --> D["Car traffic"]
  D --> E["Subband 1"]
  D --> F["Subband 2"]
  D --> G["Subband 3"]
  D --> H["Subband 4"]
  D --> I["Subband 5"]
  D --> J["Subband 6"]
  D --> K["Subband 7"]
  D --> L["Subband 8"]
  D --> M["Subband 9"]
  D --> N["Subband 10"]
  D --> O["Subband 11"]
  D --> P["Subband 12"]
  D --> Q["Subband 13"]
  D --> R["Subband 14"]
  D --> S["Subband 15"]
  D --> T["Subband 16"]
  D --> U["Subband 17"]
  D --> V["Subband 18"]
  D --> W["Subband 19"]
  D --> X["Subband 20"]
  D --> Y["Subband 21"]
  D --> Z["Subband 22"]
  D --> AA["Subband 23"]
  D --> AB["Subband 24"]
  D --> AC["Subband 25"]
  D --> AD["Subband 26"]
  D --> AE["Subband 27"]
  D --> AF["Subband 28"]
  D --> AG["Subband 29"]
  D --> AH["Subband 30"]
  D --> AI["Subband 31"]
  D --> AJ["Subband 32"]
  D --> AK["Subband 33"]
  D --> AL["Subband 34"]
  D --> AM["Subband 35"]
  D --> AN["Subband 36"]
  D --> AO["Subband 37"]
  D --> AP["Subband 38"]
  D --> AQ["Subband 39"]
  D --> AR["Subband 40"]
  D --> AS["Subband 41"]
  D --> AT["Subband 42"]
  D --> AU["Subband 43"]
  D --> AV["Subband 44"]
  D --> AW["Subband 45"]
  D --> AX["Subband 46"]
  D --> AY["Subband 47"]
  D --> AZ["Subband 48"]
  D --> BA["Subband 49"]
  D --> BB["Subband 50"]
```
</details>

Fig. 1. An illustration of ISCC V2X network.

resource allocation based on the generalized Rayleigh entropy and fairness criteria, respectively. A comprehensive complexity analysis is conducted to show the efficiency of the proposed algorithm.

• Simulation results are presented to validate the performance of the proposed algorithm. It is shown that the proposed joint resource allocation design significantly reduces the maximum sensing task completion latency for vehicles, as compared to benchmark schemes that only optimize the radio resource allocation or computation resource allocation. It is also shown that the proposed joint design achieves a better trade-off between target detection probability and task completion latency than other benchmark schemes with sensing-centric and computing-centric resource allocations. By evaluating the sensing task completion latency under different resource configurations, we also demonstrate the balance between the utilization of spectral and computation resources while maintaining consistent latency performance.

The remainder of this paper is organized as follows. Section II introduces the system model for the ISCC-enabled V2X network and formulates the associated optimization problem. In Section III, an efficient algorithm is developed to solve the joint resource allocation task. Section IV presents simulation results to validate the effectiveness of the proposed approach. Finally, Section V concludes the paper.

Notations: The uppercase bold letters denote matrices, while lowercase bold letters represent vectors. The expectation operator is denoted by E[·], and C denotes the set of complex numbers. For matrix operations, tr(·) indicates the trace, $[ \cdot ] ^ { H }$ the Hermitian (conjugate transpose), [·]∗ the complex conjugate, and $[ \cdot ] ^ { - 1 }$ the inverse. The norm of a vector is written as ||·||. A summary of key notations used in the paper is provided in Table I, where given constants are labeled as “Con”, derived constants or intermediate variables are labeled as “D-int” and optimization variables are labeled as “Opt”.

## II. SYSTEM MODEL

As shown in Fig. 1, we consider an ISCC V2X network consisting of M BSs, with each equipped with $N \ > \ 1$ antennas and indexed as $\mathcal { M } = \{ 1 , \dots , M \}$ , and K singleantenna vehicles1 indexed as $\mathcal { K } = \{ 1 , \ldots , K \}$ . Each BS is equipped with an MEC server to provide edge computing capabilities for vehicles. The vehicles transmit ISAC signals to simultaneously perform radar sensing and optionally offload the computation-intensive sensing tasks to the MEC servers. We assume that each BS m serves $K _ { m }$ vehicles and denote the set of vehicles servered by BS m as $\kappa _ { m }$ . Here, we assume that ${ \boldsymbol { \kappa } } _ { m } \mathbf { \tilde { s } }$ are pre-determined by considering load balancing among different $\mathrm { B S s } . ^ { 2 }$ Due to the limited spectrum resources, we assume that all BSs reuse the same spectrum resources to serve their respectively associated vehicles. Specifically, the overall available bandwidth is divided into L orthogonal sub-bands, indexed as $\mathcal { L } = \{ 1 , \ldots , L \}$ , where $L < K _ { m } , \forall m$ . To reduce the interference among different vehicles and vehicle-BS links,

TABLE I SUMMARY OF KEY NOTATIONS

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $N$ </td><td>Numbers of each BS&#x27;s antennas (Con)</td></tr><tr><td> $K$ </td><td>Numbers of vehicles (Con)</td></tr><tr><td> $M$ </td><td>Numbers of BSs (Con)</td></tr><tr><td> $K_{m}$ </td><td>Number of vehicles served by BS  $m$  (Con)</td></tr><tr><td> $L$ </td><td>Number of sub-bands (Con)</td></tr><tr><td> $\mathbf{u}_{k}$ </td><td>Receive beamforming vector for vehicle  $k$  (Opt)</td></tr><tr><td> $\mathbf{A}$ </td><td>Binary sub-band allocation martix (Opt)</td></tr><tr><td> $p_{k}$ </td><td>Vehicle  $k$ &#x27;s transmission power (dBm, Opt)</td></tr><tr><td> $B$ </td><td>The bandwidth of each sub-band (MHz, Con)</td></tr><tr><td> $\xi_{k}$ </td><td>The RCS of vehicles  $k$ &#x27;s sensing target (Con)</td></tr><tr><td> $P_{max}$ </td><td>Vehicle&#x27;s power budget (dBm, Con)</td></tr><tr><td> $R_{k,m}$ </td><td>Achievable data rate from vehicle  $k$  to BS  $m$  (bits/s, D-int)</td></tr><tr><td> $b_{k}$ </td><td>Volume of radar data generated by vehicle  $k$  (bits/s, D-int)</td></tr><tr><td> $e_{k}^{L}$ </td><td>CPU cycles required to process 1 bit for vehicle  $k$  (cycles/bit, Con)</td></tr><tr><td> $e_{k}^{M}$ </td><td>CPU cycles required to process 1 bit for MEC server (cycles/bit, Con)</td></tr><tr><td> $f_{L,k}$ </td><td>Vehicle  $k$ &#x27;s CPU frequency (cycles/s, Opt)</td></tr><tr><td> $f_{m,k}$ </td><td>CPU frequency allocated to vehicle  $k$  by MEC server  $m$  (cycles/s, Opt)</td></tr><tr><td> $\kappa$ </td><td>The coefficient determined by the hardware structure (Con)</td></tr><tr><td> $\eta$ </td><td>Ratio of the data volume offloaded to the overall data volume (Con)</td></tr><tr><td> $\gamma_{k}$ </td><td>Radar echo&#x27;s SINR (bits/s, D-int)</td></tr><tr><td> $S_{len}$ </td><td>Maximum storage capacity of each layer for BnB algorithm (Con)</td></tr></table>

BSs cooperatively allocate spectrum and power resources for its associated vehicles through a centralized control center with high computational capabilities.3 For clarity, we define a $L \times K$ binary sub-band allocation matrix as A with elements $\left\{ a _ { l k } \right\}$ , where l denotes the row index and k denotes the column index. If sub-band l is allocated to vehicle $k ,$ it follows that $a _ { l k } = 1$ ; otherwise, $a _ { l k } = 0$ .

## A. ISCC Signal Model

The channel vector from vehicle k to BS m over sub-band $\mathbf { h } _ { k , m } ^ { l } \in \mathbb { C } ^ { N \times 1 }$ . 01 The signal received at BS m over sub-band l can be expressed as

$$
\mathbf {r} _ {k, m} ^ {l} = a _ {l k} \mathbf {h} _ {k, m} ^ {l} s _ {k} + \sum_ {i = 1, i \neq k} ^ {K} a _ {l i} \mathbf {h} _ {i, m} ^ {l} s _ {i} + \mathbf {n} _ {m} ^ {l}, \tag {1}
$$

where $s _ { k }$ denotes the signal transmitted from vehicle $k$ and $\mathbb { E } [ s _ { k } s _ { k } ^ { * } ] = p _ { k }$ , with $p _ { k }$ being vehicle $k ' s$ transmission power. $\mathbf { n } _ { m } ^ { l } \sim \mathcal { C N } ( 0 , { \sigma _ { u } } ^ { 2 } \mathbf { I } _ { N } )$ denotes the additive white Gaussian noise (AWGN) at BS m over sub-band l. The second term of (1) represents the co-channel interference.

The achievable data rate (bit/s) from vehicle k to BS m is given by

$$
R _ {k, m} = \sum_ {l = 1} ^ {L} a _ {l k} B \log_ {2} \left(1 + \frac {p _ {k} \mathbf {u} _ {k} ^ {H} \mathbf {h} _ {k , m} ^ {l} (\mathbf {h} _ {k , m} ^ {l}) ^ {H} \mathbf {u} _ {k}}{\mathbf {u} _ {k} ^ {H} \mathbf {D} _ {k} ^ {l} \mathbf {u} _ {k}}\right), \tag {2}
$$

where B denotes the bandwidth of each sub-band, $, ~ { \bf u } _ { k } ~ \in$ $\mathbb { C } ^ { N \times 1 }$ denotes the receive beamforming vector for vehicle $k ' s$ transmit signal, and $\begin{array} { r } { \mathbf { D } _ { k } ^ { l } = \sum _ { i = 1 , i \neq k } ^ { K } \mathsf { \overline { { a _ { l i } p _ { i } } } } \mathbf { h } _ { i , m } ^ { l } ( \mathbf { h } _ { i , m } ^ { l } ) ^ { H } \mathrel { + } \qquad } \end{array}$ $\sigma _ { u } ^ { 2 } \mathbf { I } _ { N }$ .

In the sensing process, we assume that each vehicle performs target detection separately. To avoid collisions, the vehicles must detect the presence of targets within a minimum safe distance. The received signals at vehicle k over sub-band $l ,$ including the echo signal from the target of interest and interference from other vehicles allocated the same sub-band, can be expressed as

$$
r _ {s, k} ^ {l} [ w ] = a _ {l k} \alpha_ {k} s _ {k} [ w ] + \sum_ {i = 1, i \neq k} ^ {K} a _ {l i} g _ {i, k} ^ {l} s _ {i} [ w ] + n _ {r} ^ {l} [ w ], \tag {3}
$$

where αk = q $\begin{array} { r } { \alpha _ { k } = \sqrt { \frac { \rho _ { 0 } G _ { t } } { 4 \pi { d _ { t , k } } ^ { 2 } } \times \frac { \xi _ { k } A _ { r } } { 4 \pi { d _ { t , k } } ^ { 2 } } } } \end{array}$ 4πdt,k with $\xi _ { k }$ being the radar crosssection (RCS) of target to be sensed by vehicle $k , \rho _ { 0 }$ being the path loss at the reference distance $d _ { 0 } = 1 { \mathrm { m } } , G _ { t }$ and $A _ { r }$ being the transmit antenna gain and the effective aperture of the receive antenna, and $d _ { t , k }$ being the distance from vehicle k to its sensing target. $g _ { i , k } ^ { l }$ is the interfering channel from vehicle i to vehicle k over sub-band $l . \ w = 1 , \dots , N _ { s }$ denotes the time index, $N _ { s }$ denotes the number of symbols accumulated for sensing, and $n _ { r } ^ { l } \sim \mathcal { C N } ( 0 , \sigma _ { r } ^ { 2 } )$ is the AWGN at vehicles over sub-band $l . ^ { 5 }$ After receiving echoes, vehicle k executes target detection via hypothesis test, which can be formulated as

$$
r _ {s, k} ^ {l} [ w ] = \left\{ \begin{array}{l l} a _ {l k} \alpha_ {k} s _ {k} [ w ] + \sum_ {i = 1, i \neq k} ^ {K} a _ {l i} g _ {i, k} ^ {l} s _ {i} [ w ] + n _ {r} ^ {l} [ w ], \mathcal {H} _ {1}, \\ \sum_ {i = 1, i \neq k} ^ {K} a _ {l i} g _ {i, k} ^ {l} s _ {i} [ w ] + n _ {r} ^ {l} [ w ], & \mathcal {H} _ {0}. \end{array} \right. \tag {4}
$$

In (4), $\mathcal { H } _ { 1 }$ indicates that the target is present and $\mathcal { H } _ { 0 }$ indicates that the target is absent. By combining the signals from the $L$ sub-bands and using the Neyman-Pearson criterion along with the generalized likelihood ratio test (GLRT), the optimal detector is [28]

$$
T = \sum_ {l = 1} ^ {L} \sum_ {w = 1} ^ {N _ {s}} | r _ {s, k} ^ {l} [ w ] | ^ {2} \underset {\mathcal {H} _ {1}} {\overset {\mathcal {H} _ {0}} {\lesssim}} \psi , \tag {5}
$$

where $\psi$ is a threshold related to the constant false alarm probability and can be given by

$$
\psi = F _ {\mathcal {X} _ {2} ^ {2}} ^ {- 1} \left(1 - P _ {F A}\right). \tag {6}
$$

In (6), $P _ { F A }$ is the acceptable false alarm probability and $\mathcal { F } _ { \mathcal { X } _ { 2 } ^ { 2 } ( \cdot ) } ^ { - 1 }$ is the inverse operation of the Chi-square cumula-2tive distribution function (CDF). After matched filtering and whitening filtering, the asymptotic statistic of $T$ obeys the following distribution

$$
T \sim \left\{ \begin{array}{c c} \mathcal {X} _ {2} ^ {2} (\gamma_ {k}): \frac {1}{2} e ^ {- (T + \gamma_ {k}) / 2} \Gamma_ {0} (\sqrt {\gamma_ {k} T}), & \mathcal {H} _ {1}, \\ \mathcal {X} _ {2} ^ {2}: \frac {1}{2} e ^ {- T / 2}, & \mathcal {H} _ {0}, \end{array} \right. \tag {7}
$$

where $\mathcal { X } _ { 2 } ^ { 2 } ( \gamma _ { k } )$ represents the non-centrality chi-square distribution with degrees of freedom being two and $\Gamma _ { 0 } ( \cdot )$ denotes the Bessel function of the first kind. $\gamma _ { k }$ is the non-centrality parameter for $\begin{array} { r } { \mathcal { X } \int _ { 2 } ^ { 2 } \left( \gamma _ { k } \right) } \end{array}$ , and it is expressed as

$$
\gamma_ {k} = \sum_ {l = 1} ^ {L} \frac {a _ {l k} N _ {s} p _ {k} \alpha_ {k} ^ {2}}{\sum_ {i = 1 , i \neq k} ^ {K} a _ {l i} p _ {i} | | g _ {i , k} ^ {l} | | ^ {2} + \sigma_ {r} ^ {2}}. \tag {8}
$$

Consequently, the asymptotic detection probability $P _ { D }$ can be expressed as

$$
P _ {D} = P (T > \psi \mid \mathcal {H} _ {1}) = 1 - \mathcal {F} _ {\mathcal {X} _ {2} ^ {2} (\gamma_ {k})} \left(\mathcal {F} _ {\mathcal {X} _ {2} ^ {2} (\gamma_ {k})} ^ {- 1} (1 - P _ {F A})\right), \tag {9}
$$

where $\mathcal { F } _ { \mathcal { X } _ { \mathrm { ~ c ~ } } ^ { 2 } }$ represents the chi-square CDF. It has been established in [28] that $P _ { D }$ monotonically increases with respect to $\gamma _ { k }$ . We note that the expression for the non-centrality parameter $\gamma _ { k }$ is the same as radar echo’s SINR, indicating that higher SINR leads to better detection performance. Consequently, we constrain $\gamma _ { k }$ at the minimum detection distance $d _ { m i n }$ to be no

5The sensing model is simplified to focus on key aspects relevant to sensing SINR, making the analysis more manageable. However, the proposed method remains applicable to more realistic sensing channel models $( \mathrm { e . g . }$ , incorporating angle of arrival and clutter). In these cases, advanced techniques like transmit beamforming and cluster interference cancellation must be carefully designed to ensure optimal sensing performance. Introducing these techniques, however, will increase complexity and signal processing latency. Resource allocation for these more complex models will be explored in our future work.

smaller than a specific threshold, i.e.,

$$
\gamma_ {k \mid d _ {t, k} = d _ {\min}} \geq \Gamma_ {d}, \forall k \in \mathcal {K}, \tag {10}
$$

where $\Gamma _ { d }$ is the sensing SINR threshold.

Remark 1: Due to the mobility of vehicles, the instantaneous Channel State Information (CSI) typically varies rapidly. Similar to [29], [30], we assume that resource allocation is performed over a time block consisting of multiple slots, with a total duration on the order of several hundred microseconds. In this case, the large-scale fading, primarily determined by the vehicle’s position, is assumed to remain approximately constant within a time block. Meanwhile, small-scale fading is assumed to be constant within each slot but varies slowly across different slots, with the correlation between slots depending on factors such as vehicle speed and Doppler shifts. Furthermore, we assume perfect CSI for each slot to analyze the best resource coordination gains for the ISCC system within a given time block. The robust design of scenarios with imperfect per-block CSI is left for future work.

## B. Task Computation Model

In the radar sensing process, the vehicles execute real-time echo signal processing and analysis. Based on the practical radar engineering implementation and radar detection model [21], [31], the volume of echoes for vehicle k can be modeled as

$$
b _ {k} = \zeta f _ {s} q _ {k}, \tag {11}
$$

where $\zeta$ is a constant related to the configuration of radar systems, $f _ { s }$ denotes the sampling frequency of vehicle $k ,$ , and $q _ { k }$ denotes the quantization bits for each sample. Furthermore, we define the sensing computing task of vehicle $k$ as $D _ { k } =$ $( b _ { k } , e _ { k } ^ { L } )$ , where $e _ { k } ^ { L }$ is the task computation workload/intensity, which represents the per-bit computational load measured in central processing unit (CPU) cycles [4].

We consider that the radar data processing consists two stages. Initially, the vehicle performs local data preprocessing, which mainly involves the removal of unwanted signals [32] and data compression [12]. During the radar sensing process, received signals often contain redundant information unrelated to target detection, such as ground clutter, radio frequency interference, and noise. Through signal preprocessing, we can improve data quality and enhance radar detection performance. The preprocessed data is then offloaded to the BS for further analysis. Finally, the BS transmits the processed results back to the vehicle.

The latency and power consumption of local preprocessing at vehicle $k$ are respectively expressed as

$$
t _ {k} ^ {L} = \frac {b _ {k} e _ {k} ^ {L}}{f _ {L , k}}, k \in \{1, \dots , K \}, \tag {12}
$$

and

$$
p _ {k} ^ {L} = \kappa (f _ {L, k}) ^ {3}, k \in \{1, \dots , K \}, \tag {13}
$$

where $f _ { L , k }$ is vehicle $k ' s$ CPU frequency (cycles/s), $e _ { k } ^ { L }$ is the computation intensity (cycles/bit) of preprocessing, and $\kappa$ is the coefficient determined by the hardware structure.

![](images/2bdc77be9a5a69847672ff6e7e8596a80ea649e787928648877e00b90b0a4292.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Vehicle Signal transmission"] --> B["(t-1)-th slot"]
  B --> C["SO"]
  B --> D["LP"]
  B --> E["MSP"]
  C --> F["t-th slot"]
  D --> F
  E --> F
  G["Vehicle Computing"] --> H["Task Completing Latency"]
  H --> I["LP"]
  H --> J["TO"]
  H --> K["MSP"]
  I --> L["t^L_k"]
  J --> M["t^O_k"]
```
</details>

Fig. 2. Slot structure of the ISCC V2X network.

The latency of sensing task offloading and MEC server processing for vehicle k can be expressed as

$$
t _ {k} ^ {o} = \frac {\eta b _ {k}}{R _ {k , m}} + \frac {\eta b _ {k} e _ {k} ^ {M}}{f _ {m , k}}, \forall k \in \{1, \dots , K \}, \tag {14}
$$

where η denotes the ratio of the amount of offloaded data to $e _ { k } ^ { M }$ is the computational intensity (cycles/bit) of MEC server processing, and $f _ { m , k }$ is the CPU frequency allocated to vehicle k by BS m. In practice, the computing capabilities of MEC server and vehicles are limited. Therefore, the CPU frequency needs to meet the following constraints:

$$
\sum_ {k = 1} ^ {K _ {m}} f _ {m, k} \leq \hat {F} _ {m}, \forall m, \tag {15}
$$

$$
0 \leq f _ {L, k} \leq F _ {l}, \forall k, \tag {16}
$$

where $\hat { F } _ { m }$ denotes the computational capacity of MEC server and $F _ { l }$ denotes the maximum CPU frequency for vehicles. Consequently, vehicle $k ' s$ total task completion latency and power consumption can be expressed as

$$
T _ {k} = t _ {k} ^ {L} + t _ {k} ^ {o} = \frac {b _ {k} e _ {k} ^ {L}}{f _ {L , k}} + \frac {\eta b _ {k}}{R _ {k , m}} + \frac {\eta b _ {k} e _ {k} ^ {M}}{f _ {M , k}}, \tag {17}
$$

$$
P _ {k} = p _ {k} + p _ {k} ^ {L} = p _ {k} + \kappa (f _ {m, k}) ^ {3}. \tag {18}
$$

As the computational output is usually significantly smaller than the original sensing echoes, we do not consider the feedback delay from the BS to vehicles, as in [21], [24]. Moreover, similar to these works, we only consider the power consumption of vehicles, while the computation power at the MEC server is not included, since MEC servers are typically connected to stable power sources with sufficient supply. To illustrate the composition of latency and power more clearly, we present the slot structure diagram in Fig. 2. It is important to note that both computation and signal transmission significantly impact vehicles’ power consumption [24], and therefore, we impose a joint constraint on them.

## C. Problem Formulation

From the above discussions, we observe that appropriate sub-band allocation and power control can effectively reduce intra-band interference, thereby improving both offloading rates and detection performance. Furthermore, the offloading rate and the computation resource allocation directly influence the completion latency of sensing tasks. Therefore, in this paper, we focus on minimizing the completion latency of sensing tasks through joint radio and computation resource allocation. Specifically, we jointly optimize the sub-band allocation A, power control p, computation resources $\mathbf { f } _ { L } , \mathbf { f } _ { M }$ , and BSs’ receive beamforming u under the constraints of detection performance in (10), to minimize the maximum task completion latency for all vehicles max $T _ { k }$ . This thus ensures k the fairness among different vehicles. The joint optimization problem is formulated as

$$
\min _ {\mathbf {A}, \mathbf {p}, \mathbf {u}, \mathbf {f} _ {L}, \mathbf {f} _ {M}} \quad \max _ {k} T _ {k} \tag {19}
$$

$$
s. t. \quad \gamma_ {k} \geq \Gamma_ {d}, \forall k \in \mathcal {K}, \tag {19a}
$$

$$
a _ {l k} \in \{0, 1 \}, \forall l \in \mathcal {L}, k \in \mathcal {K}, \tag {19b}
$$

$$
\sum_ {l = 1} ^ {L} a _ {l k} \leq 1, \forall k \in \mathcal {K}, \tag {19c}
$$

$$
\sum_ {k = 1} ^ {K _ {m}} f _ {m, k} \leq \hat {F} _ {m}, \forall m, \tag {19d}
$$

$$
0 \leq f _ {L, k} \leq F _ {l}, \forall k \in \mathcal {K}, \tag {19e}
$$

$$
p _ {k} + \kappa (f _ {L, k}) ^ {3} \leq P _ {\max}, \forall k \in \mathcal {K}, \tag {19f}
$$

$$
\left| \left| \mathbf {u} _ {k} \right| \right| = 1, \forall k \in \mathcal {K}, \tag {19g}
$$

where $P _ { m a x }$ is the vehicle’s maximum power budget, and $\{ \mathbf { p } , \mathbf { u } , \mathbf { f } _ { L } , \mathbf { f } _ { M } \} \ \triangleq \ \{ p _ { k } , \mathbf { u } _ { k } , f _ { L , k } , f _ { m , k } \} _ { k = 1 } ^ { K }$ . Constraints (19b) and (19c) indicate that each vehicle is allocated with only one sub-band, while each sub-band can be assigned to multiple vehicles. From problem (19), we can see that the sub-band allocation matrix A, transmit power p, and $\mathbf { B S s } '$ receive beamforming u are coupled within the objective function and constraint (19a). Moreover, problem (19) is characterized as a MINLP problem due to the binary constraints in (19b), making it particularly challenging to solve.

Remark 2: In problem (19), there exist trade-offs between sensing and computing from multiple perspectives. Specifically, for the sensing process, it is preferable to allocate orthogonal channels to vehicles that cause strong mutual interference, thereby increasing the SINR of the received sensing echoes. In contrast, for the computing and communication process, orthogonal channels should be assigned to vehicles closer to the BS to reduce vehicle-to-BS interference, thus improving the offloading rates. Additionally, to improve detection probability, vehicles tend to maximize their transmission power to achieve sufficient echo SINR. However, as shown in constraint (19f), increasing transmission power reduces the available power for local computing, which in turn increases task completion latency.

## III. ALGORITHM DESIGN

Due to the presence of coupled variables and the binary integer constraint, achieving the globally optimal solution of problem (19) is challenging. Alternatively, we propose an alternating optimization algorithm to obtain a suboptimal but efficient solution. Specifically, we decompose the original problem with five variables into four subproblems, namely, (1) sub-band allocation A using a low-complexity BnB approach; (2) joint transmit power p and local CPU frequency $\mathbf { f } _ { L }$ optimization based on the SCA technique; (3) MEC servers’

![](images/3d965172631fe1779af25cf54384d3fda34f13a4c5417cd74075c84a595f7831.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["A = 0"] --> B["a11 = 1"]
  A --> C["a12 = 1"]
  A --> D["a13 = 1"]
  A --> E["..."]
  A --> F["a1L = 1"]
  G["The first layer"] --> H["a21 = 1"]
  G --> I["a22 = 1"]
  G --> J["a23 = 1"]
  G --> K["..."]
  G --> L["a2L = 1"]
  M["The second layer"] --> N["a31 = 1"]
  M --> O["a32 = 1"]
  M --> P["a33 = 1"]
  M --> Q["..."]
  M --> R["a3L = 1"]
```
</details>

Fig. 3. A search tree for the sub-band allocation matrix A.

CPU frequency ${ \bf f } _ { M }$ optimization based on the fairness criteria; and (4) BSs’ receive beamforming u optimization based on the generalized Rayleigh entropy.

## A. Sub-Band Allocation

In this subsection, we optimize sub-band allocation matrix A with given $\left\{ { \bf p } , { \bf u } , { \bf f } _ { L } , { \bf f } _ { M } \right\}$ . By defining $\begin{array} { r } { w _ { k } = \frac { 1 } { \eta b _ { k } } } \end{array}$ , problem (19) can be rewritten as

$$
\begin{array}{c} \max _ {\mathbf {A}} \quad \min _ {k} w _ {k} R _ {k, m} \\ s. t. (1 9 a), (1 9 b), (1 9 c). \end{array} \tag {20}
$$

1) Problem Analysis: Since there are a total of $K ^ { L }$ subband allocation strategies, it is almost impossible to solve subproblem (20) through brute force search, especially when the number of vehicles and available sub-bands are large. A common approach is to relax the binary variables to continuous variables and then further employ convex optimization tools for solving. However, due to the form of mutual interference in the objective function and constraint (19)a, problem (20) remains non-convex even after relaxation. To this end, we propose a BnB algorithm to directly solve the problem.

Firstly, as illustrated in Fig. 3, we model the search space for the sub-band allocation matrix A as an L-ary tree. Each leaf node within this L-ary tree represents a specific subband allocation scheme. We utilize a layer-by-layer method to allocate sub-bands to different vehicles. Initially, in the first layer, the l-th branch of the root node corresponds to exclusively assigning the l-th sub-band to vehicle 1, while the other vehicles remain unassigned. Then, in the k-th layer, sub-bands are allocated to the k-th vehicle, building upon the allocation completed for the first k − 1 vehicles.

This tree search problem can be optimally addressed using the classic BnB algorithm [33]. However, the traditional BnB method is highly complex. In the worst case, its complexity is comparable to that of a brute-force approach. Consequently, we introduce a sensing-centric greedy allocation algorithm (i.e., Algorithm 1) to generate a global upper bound that facilitates the pruning process. Building on this, we further propose a streamlined and low-complexity BnB algorithm (i.e., Algorithm 2).

2) Greedy Allocation Algorithm: The sensing-centric optimization problem with the aim of maximizing the minimum SINR of vehicles’ sensing echoes is formulated as

$$
\max _ {\mathbf {A}} \quad \min _ {k} \gamma_ {k}
$$

Algorithm 1 Greedy Allocation Algorithm for Solving (21)  
Input: Transmit power p, local CPU frequency $f_{L}$ , MEC server CPU frequency $f_{M}$ , sensing threshold $\Gamma_{d}$ , BSs' receive beamforming u.

1: Select the two vehicles corresponding to the highest interference metric.

2: repeat

3: Select the vehicle that has the highest interference metric with the already selected vehicles.

4: until L vehicles are selected.

5: Allocate L sub-bands to the L vehicles.

6: repeat

7: Select the next vehicle $\widetilde{k}$ to be allocated based on (22).

8: Select the sub-band $\widetilde{l}$ allocated to the vehicle based on (23).

9: Add vehicle k to the set $\widetilde{K}_{l}$ .

10: until All vehicles have been assigned sub-bands.

Output: Sub-band allocation matrix A.

Algorithm 2 Low-Complexity BnB Algorithm for Solving (20)  
Input: Transmit power p, local CPU frequency $f_{L}$ , MEC server CPU frequency $f_{M}$ , sensing threshold $\Gamma_{d}$ , BSs' receive beamforming u.

1: Calculate the global lower bound $B_{u}$ based on the solution from Algorithm 1.

2: Initialize i = 1.

3: repeat

4: Based on (24), calculate the minimum offloading rate $B_{d}$ for each node's sub-band allocation scheme at the i-th layer.

5: Remove nodes that do not satisfy constraints (19a) or $B_{d} < B_{u}$ and sort the minimum offloading rate $B_{d}$ of the remaining nodes at the i-th layer in descending order.

6: Retain $S_{len}$ nodes with the higher minimum offloading rate and branch them to the next layer.

7: Update $i = i + 1$ .

8: until $i = K + 1$ .

9: Select the sub-band allocation scheme corresponding to the node with the highest lower bound.

Output: the sub-band allocation matrix A.

$$
s. t. (1 9 \mathrm{b}), (1 9 \mathrm{c}). \tag {21}
$$

To assess the level of interference between different vehicles, we further define the interference metric between vehicle i and vehicle j as $I _ { i , j } = p _ { i } | | g _ { i , j } | | ^ { 2 }$ .

We begin by selecting two vehicles with the highest interference metric, as they form the pair with the strongest mutual interference, for which prioritizing orthogonal sub-band allocation yields the greatest interference mitigation gain. Next, we sequentially choose the next $L - 2$ vehicles that have the highest interference metrics with the already selected vehicles, assigning each vehicle to one of the remaining orthogonal sub-bands. To determine the sub-band allocation order for the remaining vehicles, we identify the next vehicle index to be assigned based on the following criteria:

$$
\widetilde {k} = \arg \max _ {k} \frac {1}{(L - 1)} \left(\sum_ {l = 1} ^ {L} \sum_ {j \in \widetilde {\mathcal {K}} _ {l}} I _ {k, j} - \min _ {l} \sum_ {j \in \widetilde {\mathcal {K}} _ {l}} I _ {k, j}\right), \tag {22}
$$

where ${ \widetilde { \kappa } } _ { l }$ denotes the set of vehicles that have been allocated with the l-th sub-band. $\begin{array} { r } { \sum _ { l = 1 } ^ { L } \sum _ { j \in \widetilde { \mathcal { K } } _ { l } } I _ { k , j } } \end{array}$ denotes the total e interference from vehicle k to other vehicles when vehicle k is assigned with different sub-bands. minl $\textstyle \sum _ { j \in { \widetilde { \mathcal { K } } } _ { l } } I _ { k , j }$ denotes e the minimum interference metric introduced when vehicle k is assigned different channels. Here, (22) implies that we tend to select the vehicle that would introduce the maximum average interference if it is not assigned to the sub-band with the minimum interference metric. The sub-band allocated to vehicle k is

$$
\widetilde {l} = \min _ {l} \sum_ {j \in \widetilde {\mathcal {K}} _ {l}} I _ {k, j}. \tag {23}
$$

In summary, we summarize the detailed process of the greedy allocation algorithm in Algorithm 1. Under this scheme, the minimum offloading rate among vehicles is set as the global lower bound $B _ { u }$ . Next, we introduce the lowcomplexity BnB algorithm for solving problem (20).

3) Low-Complexity BnB Algorithm: For the search tree depicted in Fig. 3, we adopt a breadth-first search approach to solve problem (20), performing branching and bounding operations at each layer based on the global lower bound derived from problem (21). Specifically, at the first layer, we calculate the minimum offloading rate for each node as

$$
B _ {d} = \min _ {l} \min _ {k \in \tilde {\mathcal {K}} _ {l}} w _ {k} B \log_ {2} \left(1 + \frac {p _ {k} \mathbf {u} _ {k} ^ {H} \mathbf {h} _ {k , m} ^ {l} (\mathbf {h} _ {k , m} ^ {l}) ^ {H} \mathbf {u} _ {k}}{\mathbf {u} _ {k} \widehat {\mathbf {D}} _ {k} ^ {l} \mathbf {u} _ {k} ^ {H}}\right), \tag {24}
$$

$\begin{array} { r l r } { \widehat { \bf D } _ { k } ^ { l } } & { = } & { \sum _ { i = 1 , i \neq k } ^ { K } \widehat { a } _ { l i } p _ { i } { \bf h } _ { i , m } ^ { l } ( { \bf h } _ { i , m } ^ { l } ) ^ { H } + \sigma _ { u } ^ { 2 } { \bf I } _ { N } } \end{array}$ $\{ \widehat { a } _ { l i } \} _ { \forall l , i }$ bi being the sub-band allocation of the current node. bWe compare $B _ { d }$ of each node with the global lower bound $B _ { u }$ obtained by the greedy allocation algorithm. If $B _ { d } ~ < ~ B _ { u }$ or constraints in (19a) are not satisfied, i.e., $\begin{array} { r l r } { \sum _ { l = 1 } ^ { L } \frac { \widehat { a } _ { l k } N _ { s } p _ { k } \alpha _ { k } ^ { 2 } } { \sum _ { i = 1 , i \neq k } ^ { K } \widehat { a } _ { l i } p _ { i } | | g _ { i , k } ^ { l } | | ^ { 2 } + \sigma _ { r } ^ { 2 } } < \Gamma _ { d } , \forall k \in \mathcal { K } , } \end{array}$ , a pruning boperation is performed. Subsequently, the remaining nodes are sorted in a descending order based on their minimum offloading rate, and the branching operation is repeated. To further reduce the complexity of the algorithm, we limit the maximum storage width of each layer to $S _ { l e n } .$ , meaning that only the largest $S _ { l e n }$ nodes are preserved for branching to the next layer. This process of recalculating boundaries and pruning is repeated until the final layer, where each vehicle is assigned a sub-band. The node with the highest minimum offloading rate is then selected as the final sub-band allocation scheme. The detailed BnB algorithm is summarized in Algorithm 2.6

6In practical network deployments, the implementation of Algorithm 1 and Algorithm 2 requires the exchange of information between the centralized control center, BSs, and vehicles. First, the BS collects the vehicle’s CSI based on pilot signals and uploads it to the control center. Then, the control center optimizes the sub-band allocation and sends the results back to both the BS and the corresponding vehicles. Finally, the vehicles perform sensing and data offloading on the assigned sub-band.

## B. Power Control and Local Computation Resource Allocation

We then optimize the transmit power p and vehicles’ local CPU frequency $\mathbf { f } _ { L }$ with given $\{ \mathbf { A } , \mathbf { u } , \mathbf { f } _ { M } \}$ . In this case, problem (19) is reformulated as

$$
\min _ {\mathbf {p}, \mathbf {f} _ {L}} \quad \max _ {k} \frac {b _ {k} e _ {k} ^ {L}}{f _ {L , k}} + \frac {\eta b _ {k}}{R _ {k , m}}
$$

$$
s. t. \quad (1 9 e), (1 9 f). \tag {25}
$$

By introducing slack variables $\mu _ { 1 }$ and $\mu _ { 2 } ,$ problem (25) can be equivalently rewritten as

$$
\min _ {\mathbf {p}, \mathbf {f} _ {L}} \quad \mu_ {1} + \mu_ {2} \tag {26}
$$

$$
s. t. \quad \frac {b _ {k} e _ {k} ^ {L}}{f _ {L , k}} \leq \mu_ {1}, \forall k \in \mathcal {K}, \tag {26a}
$$

$$
\frac {\eta b _ {k}}{R _ {k , m}} \leq \mu_ {2}, \forall k \in
$$

$$
(1 9 \mathrm{e}), (1 9 \mathrm{f}). \mathcal {K}, \tag {26b}
$$

It is observed that problem (26) remains challenging to solve due to the non-convex constraint (26b). To make it tractable, we introduce auxiliary variables $r _ { k } , c _ { 1 , k }$ , and $c _ { 2 , k } , \forall k \in \mathcal { K }$ . With these variables, we can reformulate constraint (26b) as

$$
\frac {\eta b _ {k}}{B r _ {k}} \leq \mu_ {2}, \forall k \in \mathcal {K}, \tag {27}
$$

$$
\frac {c _ {1 , k}}{c _ {2 , k}} \geq 2 ^ {r _ {k}} - 1, \forall k \in \mathcal {K}, \tag {28}
$$

$$
\sum_ {l = 1} ^ {L} a _ {l k} p _ {k} \mathbf {u} _ {k} ^ {H} \mathbf {h} _ {k, m} ^ {l} (\mathbf {h} _ {k, m} ^ {l}) ^ {H} \mathbf {u} _ {k} \geq c _ {1, k}, \forall k \in \mathcal {K}, \tag {29}
$$

$$
\sum_ {l = 1} ^ {L} \sum_ {i = 1, i \neq k} ^ {K} a _ {l i} p _ {i} \mathbf {u} _ {k} ^ {H} \mathbf {h} _ {i, m} ^ {l} (\mathbf {h} _ {i, m} ^ {l}) ^ {H} \mathbf {u} _ {k}
$$

$$
+ \mathbf {u} _ {k} ^ {H} \sigma_ {u} ^ {2} \mathbf {I} _ {N} \mathbf {u} _ {k} \leq c _ {2, k}, \forall k \in \mathcal {K}. \tag {30}
$$

Due to the fractional term on the left side of the inequality, constraint (28) remains non-convex. Next, we develop an iterative algorithm using the SCA technique to transform this constraint into a convex form. By introducing auxiliary variables $\begin{array} { r } { { v _ { 1 , k } } , \ { v _ { 2 , k } } . } \end{array}$ , and $v _ { 3 , k } ,$ constraint (28) is decomposed as

$$
c _ {1, k} \geq e ^ {v _ {1, k}}, v _ {1, k} - v _ {2, k} \geq v _ {3, k}, \forall k \in \mathcal {K}, \tag {31a}
$$

$$
c _ {2, k} \leq e ^ {v _ {2, k}}, 2 ^ {r _ {k}} - 1 \leq e ^ {v _ {3, k}}, \forall k \in \mathcal {K}. \tag {31b}
$$

We note that only constraint (31b) is non-convex. Next, we linearize it using the first-order Taylor expansion. Given points $\bar { v } _ { 2 , k }$ and $\bar { v } _ { 3 , k }$ , the non-convex constraint is convexified as

$$
c _ {2, k} \leq e ^ {\bar {v} _ {2, k}} \left(v _ {2, k} - \bar {v} _ {2, k} + 1\right),
$$

$$
2 ^ {r _ {k}} - 1 \leq e ^ {\bar {v} _ {3, k}} \left(v _ {3, k} - \bar {v} _ {3, k} + 1\right). \tag {32}
$$

Consequently, problem (26) is recast as

$$
\min _ {\mathbf {p}, \mathbf {f} _ {L}} \quad \mu_ {1} + \mu_ {2}
$$

$$
s. t. (1 9 \mathrm{e}), (1 9 \mathrm{f}), (2 6 \mathrm{a}), (2 7), (2 9), (3 0), (3 1 \mathrm{a}), (3 2), \tag {33}
$$

which is a convex problem that can be solved using the standard convex optimization tools such as CVX. By iteratively solving problem (33) and updating $\bar { v } _ { 2 , k }$ and $\bar { v } _ { 3 , k }$ , the original problem (25) can be solved.

## C. MEC Server Computation Resource Allocation

This subsection optimizes the MEC servers’ computation resource allocation ${ \bf f } _ { M }$ with given sub-band allocation matrix A, the transmit power p, vehicles’ CPU frequency $\mathbf { f } _ { L }$ , and BSs’ receive beamforming u. The subproblem is written as

$$
\min _ {\mathbf {f} _ {M}} \quad \max _ {k} \frac {\eta b _ {k} e _ {k} ^ {M}}{f _ {m , k}}
$$

$$
s. t. \quad (1 9 \mathrm{d}), \tag {34}
$$

which is a standard convex optimization problem and can be solved via the standard convex optimization tools. However, to reduce computational complexity, we provide the following proposition to obtain the optimal ${ \bf f } _ { M }$ in closed form.

Proposition 1: The optimal solution of $f _ { m , k } ^ { * }$ to problem (34) is

$$
f _ {m, k} ^ {*} = \frac {\eta b _ {k} e _ {k} ^ {M}}{\sum_ {i = 1} ^ {K _ {m}} \eta b _ {i} e _ {i} ^ {M}} \hat {F} _ {m}. \tag {35}
$$

Proof: When other optimization variables are fixed, the subproblem (34) can be decoupled for different MEC servers. The computation resource allocation subproblem for MEC server m is given by

$$
\max _ {\mathbf {f} _ {M}} \quad \min _ {k \in \mathcal {K} _ {m}} \frac {\eta b _ {k} e _ {k} ^ {M}}{f _ {m , k}} \tag {36}
$$

$$
s. t. \quad \sum_ {k = 1} ^ {K _ {m}} f _ {m, k} \leq \hat {F} _ {m}. \tag {36a}
$$

According to the fairness criterion, when problem (36) reaches its optimal solution, it follows that $\begin{array} { r } { \frac { \eta b 1 e _ { 1 } ^ { \dot { M } } } { f _ { 1 , k } } = \frac { \eta b 2 e _ { 2 } ^ { \dot { M } } } { f _ { m , 2 } } = } \end{array}$ have f ∗m,k $\begin{array} { r } { \cdots = \frac { \eta b K _ { m } e ^ { M } K _ { m } } { f _ { m , K _ { m } } } } \end{array}$ $\begin{array} { r } { f _ { m , k } ^ { * } = \frac { \eta b _ { k } e _ { k } ^ { M } } { \sum _ { i = 1 } ^ { K _ { m } } \eta b _ { i } e _ { i } ^ { M } } \hat { F } _ { m } . \mathbf { { \mathbf { \overline { { m } } } } } } \end{array}$ fm,Km ηbkeMk $\begin{array} { r } { \sum _ { k = 1 } ^ { K _ { m } } f _ { m , k } \le \hat { F } _ { m } , } \end{array}$ Km

## D. BSs’ Receive Beamforming Optimization

This subsection optimizes BSs’ receive beamforming u with given sub-band allocation matrix A, transmit power p, the CPU frequency of vehicles and MEC servers $\mathbf { f } _ { L } , \mathbf { f } _ { M }$ . The subproblem is given by

$$
\max _ {\mathbf {u}} \quad \min _ {k} \frac {R _ {k , m}}{\eta b _ {k}}
$$

$$
s. t. (1 9 \mathrm{g}). \tag {37}
$$

It is worth noting that the sub-problem for BSs’ receive beamforming can be decoupled for different vehicles. Consequently, the minimum uplink rate maximization problem can be solved individually for each vehicle. Therefore, problem (37) can be rewritten as follows:

$$
\mathcal {P} _ {k} ^ {\text { sub }} (\mathbf {u} _ {k}): \max _ {| | \mathbf {u} _ {k} | | = 1} \quad \frac {R _ {k , m}}{\eta b _ {k}}, \forall k \in \mathcal {K}. \tag {38}
$$

Since log(·) is a monotonically increasing function, problem (38) is equivalent to

$$
\mathcal {P} _ {k} ^ {\text { sub }} (\mathbf {u} _ {k}): \max _ {| | \mathbf {u} _ {k} | | = 1} \frac {p _ {k} \mathbf {u} _ {k} ^ {H} \mathbf {h} _ {k , m} ^ {\tilde {l}} \left(\mathbf {h} _ {k , m} ^ {\tilde {l}}\right) ^ {H} \mathbf {u} _ {k}}{\mathbf {u} _ {k} ^ {H} \mathbf {D} _ {k} ^ {\tilde {l}} \mathbf {u} _ {k}}, \forall k \in \mathcal {K}, \tag {39}
$$

which is a Rayleigh entropy problem and $\tilde { l }$ satisfies $a _ { \tilde { l } k } = 1$ . Therefore, we have the following proposition

Proposition 2: The optimal solution of $\mathbf { u } _ { k } ^ { * }$ to problem (39) is

$$
\mathbf {u} _ {k} ^ {*} = \frac {\operatorname{eigvec} \left\{\max \left\{\operatorname{eig} \left\{\left(\mathbf {D} _ {k} ^ {\tilde {l}}\right) ^ {- 1} \mathbf {h} _ {k , m} ^ {\tilde {l}} \left(\mathbf {h} _ {k , m} ^ {\tilde {l}}\right) ^ {H} \right\} \right\} \right\}}{\left| \left| \operatorname{eigvec} \left\{\max \left\{\operatorname{eig} \left\{\left(\mathbf {D} _ {k} ^ {\tilde {l}}\right) ^ {- 1} \mathbf {h} _ {k , m} ^ {\tilde {l}} \left(\mathbf {h} _ {k , m} ^ {\tilde {l}}\right) ^ {H}   \right\} \right\} \right\} \right| \right|}. \tag {40}
$$

where $\mathrm { e i g } \{ \cdot \}$ denote the eigenvalues and eigvec $\{ \lambda _ { e } \}$ denotes the eigenvector corresponding to the eigenvalue $\lambda _ { e } .$

$\mathbf { w } _ { k } = { ( \mathbf { D } _ { k } ^ { \tilde { l } } ) } ^ { 1 / 2 } \mathbf { u } _ { k } ,$ as

$$
\max _ {\mathbf {w} _ {k}} \frac {p _ {k} \mathbf {w} _ {k} ^ {H} (\mathbf {D} _ {k} ^ {\tilde {l}} {} ^ {- 1 / 2} \mathbf {h} _ {k , m} ^ {\tilde {l}} (\mathbf {h} _ {k , m} ^ {\tilde {l}}) ^ {H} \mathbf {D} _ {k} ^ {\tilde {l}} {} ^ {- 1 / 2}) \mathbf {w} _ {k}}{\mathbf {w} _ {k} \mathbf {w} _ {k} ^ {H}}, \forall k \in \mathcal {K}, \tag {41}
$$

which is a generalized eigenvector problem [34]. Leveraging the properties of Rayleigh entropy, the optimal solution $\mathbf { w } _ { k } ^ { * }$ can be obtained as the generalized eigenvector corresponding to the largest eigenvalue of the matrix $\mathbf { D } _ { k } ^ { \tilde { l } } \mathbf { \Lambda } ^ { - 1 / 2 } \mathbf { h } _ { k , m } ^ { \tilde { l } } ( \mathbf { h } _ { k , m } ^ { \tilde { l } } ) ^ { H } \mathbf { D } _ { k } ^ { \tilde { l } } \mathbf { \Lambda } ^ { - 1 / 2 }$ )H D˜l −1/2.

## Algorithm 3 Overall Algorithm for Solving Problem (19)

Input: Sensing SINR threshold $\overline { { \Gamma _ { d } } } ,$ the computation capacity of MEC server $\hat { F } _ { m } ,$ the maximum CPU frequency for vehicles $F _ { l } ,$ , maximum iteration number $N _ { i t } ^ { m a x } .$ .

1: Initialize transmit power p, local CPU frequency $\mathbf { f } _ { L } ,$ , MEC server CPU frequency $\mathbf { f } _ { M } .$ and BSs’ receive beamforming u.

2: Initialize A by using Algorithm 1.

3: $N _ { i t } = 1 .$

4: repeat

5: Update A by using Algorithm 2.

6: Update p and $\mathbf { f } _ { L }$ by solving problem (33).

7: Update ${ \bf f } _ { M }$ by equation (40).

8: Update u by equation (35).

9: Update ${ \ddot { N _ { i t } } } = { \bar { N } } _ { i t } + 1 .$ .

$N _ { i t } \ge N _ { i t } ^ { m a x }$ or the objective value of the problem (19) converges.

Output: Sub-band allocation matrix A, transmit power p, vehicles’ CPU frequency $\mathbf { f } _ { L } ,$ BSs’ receive beamforming u, and MEC servers’ computation resource allocation ${ \bf f } _ { M }$ .

## E. Overall Algorithm

Building upon the algorithms introduced in the preceding subsections, we now present a unified framework for solving problem (19) in Algorithm 3. Regarding its convergence, in step 5, note that the update occurs only if the objective value of the newly obtained subchannel allocation solution is smaller than the current objective value. Besides, p and $\mathbf { f } _ { L }$ are updated by solving problem (33) using the SCA technique, and ${ \bf f } _ { M }$ and u are updated based on the optimal closed-form solutions.

Consequently, the objective value of the problem is nonincreasing; hence, the algorithm is guaranteed to converge, as the objective value is lower bounded by 0.

The complexity of the overall algorithm primarily arises from Algorithms 1, 2, and optimizing p and $\mathbf { f } _ { L }$ . In Algorithm 1, the computational complexity mainly comes from the selection of vehicles and subchannels in lines 6-10, with a complexity of $\mathcal { O } ( K L )$ . In Algorithm 2 which involves a $K \cdot$ level tree, the number of search nodes per level is $\boldsymbol { L S } _ { l e n } ,$ leading to a complexity of $\mathcal { O } ( K L S _ { l e n } )$ . The computational complexity of optimizing p and $\mathbf { f } _ { L }$ mainly lies in solving problem (33), which can be addressed using the interiorpoint method with the worst-case computational complexity of $\mathcal { O } ( K ^ { 3 . 5 } )$ . Consequently, omitting lower order terms, the overall complexity of the algorithm 3 is $\mathcal { O } ( N _ { i t } ( K L S _ { l e n } + K ^ { 3 . 5 } ) )$ , where $N _ { i t }$ denotes the number of iterations.

## IV. NUMERICAL RESULTS

In this section, we demonstrate the effectiveness of the proposed joint optimization design in Algorithm 3. We first outline the simulation setup and comparison schemes, followed by a comprehensive analysis of the simulation results.

## A. Simulation Setup and Benchmarks

Unless otherwise specified, the following simulation settings are considered. For the ISCC network, we consider 4 BSs located within a square area specified by [−200m, 600m] × [−200m, 600m], with coordinates at [0m, 0m], [0m, 400m], [400m, 400m], and [400m, 400m]. Four lanes are arranged equidistantly in both the horizontal and vertical directions, with vehicles randomly distributed across these lanes. We assume that the channels between the BSs and vehicles follow Rayleigh fading, and the RCS of the sensing targets are uniformly distributed between 0.8 and 1. Additionally, the path loss at reference distance $d _ { 0 } = 1 \mathrm { m }$ is set as $\rho _ { 0 } = - 3 0$ dB. Other key parameters are listed in Table II. Furthermore, Monte Carlo simulations are conducted, and the results are averaged over 200 trials to ensure statistical reliability.

To evaluate the performance of the proposed joint optimization design, we consider the following five schemes under the same parameter configurations for comparison.

• Computing-centric resource allocation (CCRA) scheme: The CCRA minimizes the completion latency of sensing tasks by optimizing sub-band allocation, power, computation resources, and BSs’ receive beamforming, without considering sensing needs of the vehicles. The greedy algorithm-based approach proposed in [16] is adopted for sub-band allocation, with the optimization of other variables being the same as the joint optimization design.  
• Sensing-centric resource allocation (SCRA) scheme: In the SCRA scheme, resource allocation aims to maximize the sensing echoes’ SINR rather than task processing latency. BnB algorithm is applied for sensing-centric subband allocation.  
• Random sub-band allocation (RSBA) scheme: In the RSBA scheme, sub-bands are randomly allocated to different vehicles.

TABLE II SIMULATION PARAMETERS

<table><tr><td>Parameters</td><td>Value</td></tr><tr><td>Number of BS antennas N</td><td>4</td></tr><tr><td>Number of BSs M</td><td>4</td></tr><tr><td>Number of vehicles K</td><td>48</td></tr><tr><td>Number of sub-bands L</td><td>5</td></tr><tr><td>Bandwidth of each sub-band B</td><td>10 MHz</td></tr><tr><td>Local computation intensity  $e_k$ </td><td>50 cycles/bit</td></tr><tr><td>Edge computation intensity  $e_k^M$ </td><td>400 cycles/bit</td></tr><tr><td>Maximum CPU frequency for vecicles  $F_l$ </td><td>1 Gcycles/s</td></tr><tr><td>Computation capacity of MEC server  $F_m$ </td><td>30 Gcycles/s</td></tr><tr><td>Vehicles&#x27; maximum power  $P_{max}$ </td><td>30 dBm</td></tr><tr><td>The AWGN power at BS l  $σ_b^u$ </td><td>-100 dBm</td></tr><tr><td>Power coefficient related to the hardware structure κ</td><td> $10^{-26}$ </td></tr><tr><td>Maximum storage width of each layer for BnB algorithm  $S_{len}$ </td><td>16</td></tr><tr><td>Number of symbols accumulated for sensing  $N_s$ </td><td>500</td></tr><tr><td>Sensing SINR threshold of terminals  $Γ_d$ </td><td>20 dB</td></tr><tr><td>Minimum safety detection distance  $d_{min}$ </td><td>40 m</td></tr></table>

![](images/0c438e021a471b491f6da48d2597040aa8fc9a9e7a234996bbdd08b296650a4e.jpg)

<details>
<summary>line chart</summary>

| Iteration Number | F=1G cycles/s, F_m=30G cycles/s | F=0.7G cycles/s, F_m=30G cycles/s | F=0.4G cycles/s, F_m=30G cycles/s | F=1G cycles/s, F_m=15G cycles/s | F=1G cycles/s, F_m=7G cycles/s |
| ---------------- | ------------------------------ | -------------------------------- | -------------------------------- | ------------------------------ | ----------------------------- |
| 1                | 50                             | 50                               | 50                               | 50                             | 50                            |
| 2                | 12                             | 18                               | 20                               | 15                             | 20                            |
| 3                | 11                             | 17                               | 19                               | 14                             | 19                            |
| 4                | 10                             | 16                               | 18                               | 13                             | 18                            |
| 5                | 10                             | 15                               | 17                               | 13                             | 17                            |
| 6                | 10                             | 15                               | 17                               | 13                             | 17                            |
| 7                | 10                             | 15                               | 17                               | 13                             | 17                            |
| 8                | 10                             | 15                               | 17                               | 13                             | 17                            |
| 9                | 10                             | 15                               | 17                               | 13                             | 17                            |
</details>

Fig. 4. The convergence performance of Algorithm 3.

• Fixed power and computation resource (FPCR) scheme: In the RPCR scheme, the sub-band allocation and BSs’ receive beamforming are jointly optimized.  
• Maximum ratio combining (MRC) scheme: In this scheme, BSs adopt maximum ratio combining, i.e., ${ \bf u } _ { k } =$ $\begin{array} { r } { \frac { \mathbf { u } _ { k , m } } { | | \mathbf { h } _ { k , m } | | } , } \end{array}$ hk,m to receive signals from different vehicles, while other resource allocation optimization follows the same steps as the joint optimization design.

## B. Convergence Performance

We first present the convergence performance of our joint optimization design under different computation resource constraints in Fig. 4. It is seen that the proposed algorithm converges within only a few iterations. As vehicles’ available computation resources and MEC severs’ computational capacity increase, the maximum processing latency for sensing task decreases accordingly. Moreover, by comparing the red and black lines, we observe that appropriately increasing the computational capacity of MEC servers can achieve similar performance in task completion latency while requiring fewer local computation resources.

![](images/fd8537b28c055fb07f17ab86cc005b9be77fc711c79272c62f44053d22b25f77.jpg)

<details>
<summary>scatterplot</summary>

| X | Y (Red Circle) | Y (Green Square) | Y (Blue Circle) |
|---|---|---|---|
| -100 | 250 | 520 | -180 |
| 0 | 320 | 400 | 0 |
| 100 | 90 | 500 | 220 |
| 150 | -70 | 110 | 310 |
| 300 | 110 | 310 | -220 |
| 400 | 410 | 410 | -120 |
| 500 | 550 | 430 | 310 |
| 550 | 300 | 550 | 310 |
The chart displays a scatter plot with dashed lines connecting data points across multiple horizontal and vertical axes. The x-axis ranges from -200 to 600, and the y-axis ranges from -200 to 600. The legend indicates four distinct categories represented by different colored markers: red circles, green squares, orange triangles, and blue circles. No explicit title or axis labels are provided in the image.
</details>

![](images/b4a8b5e2bdff6ab303141d3ffb9f50c4cb86031e7e6281ba8e369c09d664669e.jpg)

<details>
<summary>scatterplot</summary>

| X | Y | Category |
| --- | --- | --- |
| -100 | 520 | Blue Diamond |
| -100 | 250 | Orange Triangle |
| -100 | -150 | Red Circle |
| 0 | 400 | Red Circle |
| 0 | 300 | Blue Diamond |
| 0 | 0 | Red Circle |
| 100 | 520 | Red Circle |
| 100 | 200 | Green Square |
| 100 | 100 | Orange Triangle |
| 100 | -100 | Red Circle |
| 300 | 300 | Green Square |
| 300 | -100 | Blue Diamond |
| 300 | -150 | Red Circle |
| 400 | 400 | Red Circle |
| 400 | -100 | Green Square |
| 400 | -150 | Red Circle |
| 500 | 550 | Blue Diamond |
| 500 | -150 | Green Square |
| 500 | -150 | Red Circle |
| 500 | 450 | Green Square |
| 500 | -150 | Green Square |
| 500 | 300 | Red Circle |
| 500 | 325 | Orange Triangle |
| 500 | 325 | Orange Triangle |
| 500 | -150 | Blue Diamond |
</details>

![](images/66e67c4494a666757b73a1e9bcc2b6aeecab1989b2f6163fc445eec332e7c591.jpg)

<details>
<summary>scatterplot</summary>

| X | Y | Series |
|---|---|---|
| -100 | 520 | Green Square |
| -100 | 240 | Blue Diamond |
| -100 | -180 | Red Circle |
| 0 | 400 | Red Circle |
| 0 | 320 | Orange Triangle |
| 0 | 0 | Red Circle |
| 100 | 520 | Blue Diamond |
| 100 | 220 | Green Square |
| 100 | 100 | Orange Triangle |
| 100 | -120 | Blue Diamond |
| 250 | 320 | Red Circle |
| 250 | 120 | Green Square |
| 250 | -160 | Red Circle |
| 300 | 320 | Red Circle |
| 300 | -240 | Blue Diamond |
| 400 | 400 | Red Circle |
| 400 | 420 | Red Circle |
| 400 | -160 | Orange Triangle |
| 500 | 540 | Green Square |
| 500 | 440 | Blue Diamond |
| 500 | -180 | Red Circle |
| 500 | 320 | Orange Triangle |
| 550 | 540 | Green Square |
| 550 | 320 | Orange Triangle |
| 550 | -180 | Red Circle |
</details>

Fig. 5. (a) Sub-band allocation in the CCRA scheme. (b) Sub-band allocation in the SCRA scheme. (c) Sub-band allocation in the joint optimization design.

## C. Sub-Band Allocation Results

To visually analyze the sub-band allocation characteristics of different schemes, we present the sub-band allocation results with K = 24 and L = 4 in Fig. 5. Circles of the same color represent vehicles assigned the same sub-band. In the CCRA scheme, we observe that sub-bands are preferentially allocated to vehicles located at similar distances from the BSs to ensure fairness in task offloading. This allocation is reasonable because assigning the same sub-band to vehicles with significantly different channel qualities may lead to the strong interference, consequently reducing the data offloading rate for one of the vehicles. Since the CCRA scheme does not consider sensing, the same sub-band may be allocated to nearby vehicles, resulting in substantial vehicle-to-vehicle interference and negatively impacting sensing performance. This conclusion may be further illustrated in subsequent analysis.

For the SCRA scheme, which prioritizes sensing performance, sub-bands allocated to neighboring vehicles are always orthogonal to minimize inter-vehicle interference. However, non-orthogonal sub-bands might be assigned to vehicles with significantly different channel qualities, reducing the fairness of task offloading. In contrast, our proposed sub-band allocation scheme not only ensures that sub-bands for neighboring vehicles remain orthogonal but also effectively avoids significant channel quality disparities among vehicles sharing the same sub-band.

## D. Sensing Task Completion Latency and Target Detection Performance

Next, we further examine the maximum task completion latency among vehicles and target detection performance of the proposed joint optimization design. Firstly, we show the maximum task completion latency under different schemes in Fig. 6. As can be seen, as the raw data compression ratio η increases, the amount of data that needs to be offloaded for processing also increases, leading to a linear increase in both the task offloading latency and the processing latency at the MEC server. Consequently, the maximum task completion latency increases linearly with η. Compared to RSBA, FPCR, and MRC schemes, the proposed joint optimization design achieves a lower maximum completion latency, demonstrating the advantages of jointly optimizing sub-bands, computation resources, power, and BSs’ receive beamforming. Since SCRA primarily focuses on sensing performance while overlooking the computational process, it exhibits a higher maximum task completion latency compared to the CCRA and joint optimization design. In comparison, although the joint optimization design also considers the sensing performance constraints, its maximum task completion latency is close to that of the CCRA scheme. This is because CCRA employs a greedybased algorithm [16] for sub-band allocation, which selects the optimal choice at each step, potentially resulting in a locally optimal solution for the final sub-band allocation. In contrast, the proposed joint optimization design, based on the low-complexity BnB method described in Algorithm 2, explores more potential solutions by continuously branching and pruning, thereby achieving a sub-band allocation scheme that approximates a globally optimal solution.

![](images/1ef9f848cf05f1c0942c0a18aac441e4b4c472c3cda9b743b4f42d8c38e4094f.jpg)

<details>
<summary>line chart</summary>

| The Raw Data Compression Ratio | Joint design | CCRA  | SCRA  | RSBA  | FPCR  | MRC   |
| ------------------------------ | ------------ | ----- | ----- | ----- | ----- | ----- |
| 0.3                            | 9.5          | 9.5   | 9.5   | 10.5  | 10.5  | 11.0  |
| 0.4                            | 10.5         | 10.5  | 11.5  | 12.5  | 13.0  | 14.5  |
| 0.5                            | 11.5         | 11.5  | 13.0  | 14.0  | 16.0  | 18.0  |
| 0.6                            | 12.5         | 12.5  | 15.0  | 16.0  | 19.0  | 21.0  |
| 0.7                            | 13.5         | 13.5  | 17.0  | 17.5  | 22.0  | 24.5  |
| 0.8                            | 14.5         | 14.5  | 23.5  | 19.0  | 25.0  | 28.0  |
</details>

Fig. 6. Maximum task completion latency versus different raw data compression ratio η.

![](images/ae532684f73cfe659cf76ac8413683234a640fb0a0b8f360d3b350ce25a4e2d4.jpg)

<details>
<summary>line chart</summary>

| Sensing Task Completion Latency (ms) | Joint design, K=48 | SCRA, K=48 | CCRA, K=48 | Joint design, K=32 | SCRA, K=32 | CCRA, K=32 |
| ------------------------------------ | ------------------ | ---------- | ---------- | ------------------ | ---------- | ---------- |
| 4                                    | 0.0                | 0.0        | 0.0        | 0.0                | 0.0        | 0.0        |
| 8                                    | 0.5                | 0.3        | 0.2        | 0.7                | 0.6        | 0.5        |
| 12                                   | 0.9                | 0.7        | 0.6        | 0.95               | 0.85       | 0.75       |
| 16                                   | 0.95               | 0.85       | 0.75       | 0.98               | 0.92       | 0.88       |
| 20                                   | 0.98               | 0.92       | 0.85       | 0.99               | 0.96       | 0.94       |
| 22                                   | 0.99               | 0.95       | 0.92       | 1.0                | 0.98       | 0.96       |
</details>

(a)

![](images/8388de98604d83a411a19cc1b58852dd1355b538e35f5552af479f7d7edd9e07.jpg)

<details>
<summary>line chart</summary>

| Vehicles Sensing SINR λk (dB) | Joint design, K=48 | SCRA, K=48 | CCRA, K=48 | Joint design, K=32 | SCRA, K=32 | CCRA, K=32 |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| 10 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | 0.02 |
| 15 | 0.06 | 0.04 | 0.03 | 0.04 | 0.03 | 0.03 |
| 20 | 0.12 | 0.07 | 0.06 | 0.12 | 0.07 | 0.06 |
| 25 | 0.25 | 0.15 | 0.12 | 0.25 | 0.15 | 0.12 |
| 30 | 0.45 | 0.35 | 0.32 | 0.45 | 0.35 | 0.32 |
| 35 | 0.65 | 0.55 | 0.52 | 0.65 | 0.55 | 0.52 |
| 40 | 0.85 | 0.75 | 0.72 | 0.85 | 0.75 | 0.72 |
| 45 | 0.98 | 0.95 | 0.93 | 0.98 | 0.95 | 0.93 |
</details>

(b)  
Fig. 7. (a) The empirical CDF of vehicles’ sensing task completion latency $T _ { k } .$ . (b) The empirical CDF of vehicles’ sensing SINR $\gamma _ { k }$ .

Additionally, in Fig. 6, we also observe that compared to RSBA, CCRA, and the joint optimization design, the latency in SCRA, FPCR, and MRC increase more rapidly with the raw data compression ratio $\eta .$ This is because SCRA and FPCR do not optimize local computation resource to mitigate the impact of increased offloading data volumes. Meanwhile, the MRC scheme, due to its ineffective elimination of co-channel interference between vehicles and BSs, results in a much lower offloading rate and is thus more affected by the increase in η.

In Fig. 7(a), we present the CDF of vehicles’ task completion latency. It is observed that the joint optimization design and CCRA scheme both achieve better fairness in sensing task completion latency compared to the SCRA scheme. This is because they adopt the minimization of the maximum completion latency among vehicles as the optimization objective, while the SCRA scheme focuses on maximizing the sensing echoes’ SINR. Additionally, an increase in the number of vehicles K leads to higher maximum task completion latency due to increased vehicle-to-BS interference, which subsequently reduces the offloading rate. Notably, compared to SCRA, the maximum task completion latency reductions of CCRA and joint optimization design grow with the increase of K. This is because SCRA prioritizes mitigating vehicleto-vehicle interference rather than vehicle-to-BS interference; as a result, the increase in vehicle-to-BS interference significantly diminishes the offloading rate and increases the task completion latency.

After verifying the effectiveness of the proposed algorithm in reducing maximum task completion latency, we evaluate the sensing performance across different schemes. In Fig. 7(b), we present the CDF of vehicles’ sensing SINR for CCRA, SCRA, and joint optimization design schemes. We can see that SCRA exhibits the best overall sensing performance, with over 99% of vehicles achieving a sensing SINR above 25dB when $K \ = \ 4 8$ . Moreover, compared to CCRA, the proposed joint optimization design demonstrates a higher sensing SINR, attributed to its dual consideration of sensing task completion latency and vehicle sensing performance in resource allocation design. Under $\Gamma _ { d } = 2 3 ~ \mathrm { d B }$ , all vehicles in the joint optimization design achieve a sensing SINR above 23 dB, validating the effectiveness of the sensing constraints. Additionally, we observed that as the number of vehicles K increases, the sensing SINR of all three schemes declines due to increased vehicle-to-vehicle interference.

![](images/1b05e8bb79a9d321c8d1b7576a23aaa5ddf735f450b00f0998c6bc0f504b0cf9.jpg)

<details>
<summary>line chart</summary>

| Detection distance (m) | Γ_d = 26dB | Γ_d = 23dB | Γ_d = 20dB |
| ---------------------- | ---------- | ---------- | ---------- |
| 10                     | 1.0        | 1.0        | 1.0        |
| 20                     | 1.0        | 1.0        | 1.0        |
| 30                     | 1.0        | 1.0        | 1.0        |
| 40                     | 1.0        | 1.0        | 1.0        |
| 50                     | 1.0        | 1.0        | 0.85       |
| 60                     | 1.0        | 0.98       | 0.7        |
| 70                     | 1.0        | 0.9        | 0.5        |
| 80                     | 1.0        | 0.8        | 0.3        |
| 90                     | 0.98       | 0.7        | 0.15       |
| 100                    | 0.85       | 0.25       | 0.05       |
</details>

Fig. 8. The average detection probability versus different target distance.

![](images/c7426c81aabfecd4fccc555d07919fa72e0dc9328c72bc7fa95adf596bdd9635.jpg)

<details>
<summary>line chart</summary>

| MEC servers' Computational capacity F_m (Gcycles/s) | Γ_d=26dB, L=5 | Γ_d=23dB, L=5 | Γ_d=20dB, L=5 | Γ_d=23dB, L=4 | Γ_d=23dB, L=6 |
| -------------------------------------------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 15                                                 | 14.0          | 13.5          | 13.0          | 14.0          | 13.0          |
| 20                                                 | 13.5          | 13.0          | 12.5          | 13.5          | 12.0          |
| 25                                                 | 13.0          | 12.5          | 12.0          | 13.0          | 11.5          |
| 30                                                 | 12.5          | 12.0          | 11.5          | 12.5          | 11.0          |
| 35                                                 | 12.0          | 11.5          | 11.0          | 12.0          | 10.5          |
| 40                                                 | 11.5          | 11.0          | 10.5          | 11.5          | 10.0          |
</details>

Fig. 9. Maximum task completion latency versus different MEC server’s computation capacity $\hat { F } _ { m }$ .

To more intuitively demonstrate the sensing performance of the joint optimization design, Fig. 8 presents the average detection probability under different sensing SINR thresholds with a minimum safety detection distance of $d _ { m i n } \ =$ 40m. It is observed that all three curves achieve a 100% detection probability at 40m and higher sensing SINR thresholds allow for detection at greater distances, demonstrating the joint optimization design’s effectiveness in target detection.

## E. Tradeoff Between System Performance and Different Resource Consumption

Although we demonstrated in Fig. 8 that increasing the sensing threshold $\Gamma _ { d }$ effectively improves the vehicles’ target detection performance, Fig. 9 shows that as $\Gamma _ { d }$ increases, the maximum task completion latency also increases. This is because improved sensing performance necessitates an increase in transmit power to enhance the SINR of target echoes, which leads to increased interference between vehicles and BS, as well as a reduction in local computing capacity, thereby increasing the maximum completion latency. Nevertheless, it is observed that increasing the number of sub-bands $L ,$ effectively reduces the maximum completion latency. Comparing the red and black curves, we find that when the sensing threshold $\Gamma _ { d }$ increases, it is possible to maintain the maximum task completion latency unchanged by increasing the number of orthogonal sub-bands, demonstrating the trade-off between sensing performance and sub-band resource utilization. Moreover, it is also observed that by increasing the computation resources of MEC servers, we achieve similar sensing and computing performance with fewer sub-bands, which demonstrates the balance between different resource utilizations.

![](images/a6771a2dae0d7bf9025c34eebd0ad47d65111e10427c1f904396a65287522414.jpg)

<details>
<summary>line chart</summary>

| Maximum Energy Consumption (mJ) | Perfect CSI | ε²=0.01 | ε²=0.05 | ε²=0.1 |
| ------------------------------- | ----------- | ------- | ------- | ------ |
| 5                               | 20.5        | 21.0    | 23.5    | 28.5   |
| 6                               | 15.5        | 16.0    | 18.5    | 22.0   |
| 7                               | 13.0        | 14.0    | 16.0    | 20.0   |
| 9                               | 11.5        | 12.5    | 14.5    | 19.0   |
| 13                              | 10.5        | 11.0    | 13.5    | 18.0   |
| 14                              | 10.0        | 10.5    | 13.0    | 17.5   |
</details>

Fig. 10. Maximum task completion latency versus maximum energy consumption.

![](images/c3b22e9fef0f2b5226c5b7c72169db1898bc1f7e04b396a245289171e9147782.jpg)

<details>
<summary>line chart</summary>

| Number of Vehicles K | Joint design | Joint design (2 iterations) | Joint design (2 iterations, 1 SCA) | SCRA |
|----------------------|--------------|-------------------------------|------------------------------------|------|
| 30                   | 10           | 10                            | 10                                 | 10   |
| 40                   | 12           | 12                            | 12                                 | 15   |
| 50                   | 15           | 15                            | 15                                 | 20   |
| 70                   | 18           | 20                            | 20                                 | 25   |
| 90                   | 20           | 22                            | 22                                 | 45   |
| 100                  | 20           | 25                            | 25                                 | 60   |
| 120                  | 20           | 30                            | 30                                 | 65   |
</details>

![](images/fe14a057ce5da0b8f64c352825d21cf1a5f0efbe24258556a6621a0c9ee33076.jpg)

<details>
<summary>line chart</summary>

| Number of Vehicles K | Joint design | Joint design (2 iterations) | Joint design (2 iterations, 1 SCA) | SCRA |
| --------------------- | ------------ | ---------------------------- | ---------------------------------- | ---- |
| 30                    | 50           | 50                           | 50                                 | 50   |
| 40                    | 75           | 75                           | 75                                 | 75   |
| 60                    | 150          | 150                          | 150                                | 150  |
| 90                    | 300          | 300                          | 300                                | 300  |
| 120                   | 500          | 500                          | 500                                | 500  |
</details>

(b)  
Fig. 11. (a) Maximum task completion latency versus the number of vehicles K. (b) Algorithm runtime versus the number of vehicles K.

Fig. 10 shows the maximum task completion latency versus the maximum energy consumption. As the energy consumption increases, the maximum task completion latency decreases. This is because higher energy enables greater transmission power, which improves the offloading rate; at the same time, the available computing frequency at the vehicle also increases, thereby reducing local processing latency. To evaluate the sensitivity of the proposed algorithm to CSI errors, we also present the minimum task completion latency under different CSI error levels in Fig. 10, where $\epsilon ^ { 2 }$ denotes the normalized CSI error. It is observed that when $\epsilon ^ { 2 } = 0 . 0 1$ , the algorithm’s performance degradation is negligible, since small CSI errors do not significantly change the resource allocation strategy. Nevertheless, when the CSI error increases $( \epsilon ^ { 2 } = 0 . 0 5 , 0 . 1 )$ , the resource allocation becomes less efficient due to inaccurate interference estimation, power control, and beamforming design.

To illustrate the complexity-performance trade-off, Fig. 11(a) and Fig. 11(b) show the variations in the maximum task completion latency and algorithm runtime, respectively, with respect to the number of vehicles K. Simulations have been conducted on an Intel Core i9-13900K processor, with the SeDuMi solver used to solve the convex problem. We observe that although the proposed joint design scheme achieves lower latency, it also incurs higher computational complexity, which increases with K. However, reducing the number of iterations and convex relaxations leads to a 92% reduction in runtime with only a 12% performance loss, thereby improving the complexity–performance trade-off and delivering better latency and runtime performance than the SCRA scheme. Furthermore, in practical deployments, optimization can be accelerated on field programmable gate arrays (FPGA) platforms, achieving microsecond-level execution latency [35] and ensuring the algorithm’s scalability and feasibility in large systems.

## V. CONCLUSION

In this paper, we investigated the joint optimization of radio and computation resource allocation in an ISCC-aided V2X network, where vehicles offload sensing echoes to MEC servers while detecting targets via unified ISAC signals. To ensure the fairness of network performance, we aimed to minimize the maximum sensing tasks completion latency among vehicles by optimizing the sub-bands, power, and computation resource allocation as well as BSs’ receive beamforming. An alternating optimization algorithm based on the low-complexity BnB and SCA techniques was proposed. Simulation results offer practical insights for the design of ISCC systems. Compared to purely optimizing radio or computation resource allocation, the joint resource allocation scheme significantly reduces sensing task completion latency while ensuring network fairness. Moreover, unlike conventional subband allocation schemes that focused solely on either sensing or computation functionality, the proposed algorithm considers both processes, resulting in a better trade-off between sensing and computing performance.

Although joint radio and computation resource allocation has proven effective for ISCC-enabled V2X systems, several challenges remain in practical systems. Specifically, in highmobility scenarios, dynamic propagation environment makes it difficult to obtain perfect CSI. Moreover, the Doppler effect, which induces frequency shifts in communication signals, further complicates CSI estimation and resource allocation. Therefore, our future work aims at addressing the imperfect CSI issues to enhance both efficiency and adaptability of resource allocation in highly dynamic environments. In addition, extending the current framework to incorporate the energy consumption of MEC servers will be considered to enable a more comprehensive system-level energy analysis.

## REFERENCES

[1] G. Zhu et al., “Pushing AI to wireless network edge: An overview on integrated sensing, communication, and computation towards 6G,” Sci. China Inf. Sci., vol. 66, no. 3, pp. 130–301, Feb. 2023.  
[2] A. Kaushik et al., “Toward integrated sensing and communications for 6G: Key enabling technologies, standardization, and challenges,” IEEE Commun. Standards Mag., vol. 8, no. 2, pp. 52–59, Jun. 2024.  
[3] Technical Specification Group Services and System Aspects; Service Requirements for V2X Services, document ETSI TS 122 185, 3GPP, Dec. 2017.  
[4] F. Wang, J. Xu, X. Wang, and S. Cui, “Joint offloading and computing optimization in wireless powered mobile-edge computing systems,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 1784–1797, Mar. 2018.  
[5] W. Wu, B. Tang, and R. Tao, “Performance bound optimization for MIMO radar direction finding with MUSIC,” IEEE Trans. Aerosp. Electron. Syst., vol. 59, no. 6, pp. 8845–8858, Dec. 2023.  
[6] M. Q. Nguyen, R. Feger, T. Wagner, and A. Stelzer, “High angular resolution method based on deep learning for FMCW MIMO radar,” IEEE Trans. Microw. Theory Techn., vol. 71, no. 12, pp. 5413–5427, Dec. 2023.  
[7] H. Zhang, L. Feng, X. Liu, K. Long, and G. K. Karagiannidis, “User scheduling and task offloading in multi-tier computing 6G vehicular network,” IEEE J. Sel. Areas Commun., vol. 41, no. 2, pp. 446–456, Feb. 2023.  
[8] Q. Zhang, H. Sun, X. Gao, X. Wang, and Z. Feng, “Time-division ISAC enabled connected automated vehicles cooperation algorithm design and performance evaluation,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2206–2218, Jul. 2022.  
[9] C. Shi, Y. Wang, F. Wang, S. Salous, and J. Zhou, “Joint optimization scheme for subcarrier selection and power allocation in multicarrier dualfunction radar-communication system,” IEEE Syst. J., vol. 15, no. 1, pp. 947–958, Mar. 2021.  
[10] H. Yang et al., “Dynamic power allocation for integrated sensing and communication-enabled vehicular networks,” IEEE Trans. Wireless Commun., vol. 23, no. 9, pp. 12313–12330, Sep. 2024.  
[11] Z. Lyu, G. Zhu, and J. Xu, “Joint maneuver and beamforming design for UAV-enabled integrated sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 4, pp. 2424–2440, Apr. 2023.  
[12] J.-B. Wang, J. Zhang, C. Ding, H. Zhang, M. Lin, and J. Wang, “Joint optimization of transmission bandwidth allocation and data compression for mobile-edge computing systems,” IEEE Commun. Lett., vol. 24, no. 10, pp. 2245–2249, Oct. 2020.  
[13] Z. Yang, C. Pan, J. Hou, and M. Shikh-Bahaei, “Efficient resource allocation for mobile-edge computing networks with NOMA: Completion time and energy minimization,” IEEE Trans. Commun., vol. 67, no. 11, pp. 7771–7784, Nov. 2019.  
[14] F. Fang, Y. Xu, Z. Ding, C. Shen, M. Peng, and G. K. Karagiannidis, “Optimal resource allocation for delay minimization in NOMA-MEC networks,” IEEE Trans. Commun., vol. 68, no. 12, pp. 7867–7881, Dec. 2020.  
[15] Z. Wu, H. Zhang, X. Liu, L. Li, and H. Li, “IRS empowered MEC system with computation offloading, reflecting design, and beamforming optimization,” IEEE Trans. Commun., vol. 72, no. 5, pp. 3051–3063, May 2024.  
[16] Z. Kuang, Y. Pan, F. Yang, and Y. Zhang, “Joint task offloading scheduling and resource allocation in air–ground cooperation UAVenabled mobile edge computing,” IEEE Trans. Veh. Technol., vol. 73, no. 4, pp. 5796–5807, Apr. 2024.  
[17] P. Liu, Z. Fei, X. Wang, J. Huang, J. Hu, and J. Andrew Zhang, “Joint offloading and beamforming design in integrating sensing, communication, and computing systems: A distributed approach,” IEEE Trans. Commun., vol. 73, no. 7, pp. 4697–4712, Jul. 2025, doi: 10.1109/ TCOMM.2024.3516488.  
[18] L. Zhao, D. Wu, L. Zhou, and Y. Qian, “Radio resource allocation for integrated sensing, communication, and computation networks,” IEEE Trans. Wireless Commun., vol. 21, no. 10, pp. 8675–8687, Oct. 2022.  
[19] S. Zhang, S. Yan, Z. Tang, D. Wang, and M. Peng, “Joint multiservice resource optimization for integrated sensing, communication, and computing networks,” IEEE Internet Things J., vol. 12, no. 16, pp. 32765–32779, Aug. 2025.  
[20] J. Zhao, R. Ren, D. Zou, Q. Zhang, and W. Xu, “IoV-oriented integrated sensing, computation, and communication: System design and resource allocation,” IEEE Trans. Veh. Technol., vol. 73, no. 11, pp. 16283–16294, Nov. 2024.  
[21] C. Ding, J.-B. Wang, H. Zhang, M. Lin, and G. Y. Li, “Joint MIMO precoding and computation resource allocation for dual-function radar and communication systems with mobile edge computing,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2085–2102, Jul. 2022.  
[22] M. Dong, Y. Fu, C. Li, M. Tian, F. Richard Yu, and N. Cheng, “Task offloading and resource allocation in vehicular cooperative perception with integrated sensing, communication, and computation,” IEEE Trans. Intell. Transp. Syst., vol. 26, no. 6, pp. 8481–8496, Jun. 2025.  
[23] B. Hu, W. Zhang, Y. Gao, J. Du, and X. Chu, “Multiagent deep deterministic policy gradient-based computation offloading and resource allocation for ISAC-aided 6G V2X networks,” IEEE Internet Things J., vol. 11, no. 20, pp. 33890–33902, Oct. 2024.  
[24] Z. Wang, X. Mu, Y. Liu, X. Xu, and P. Zhang, “NOMA-aided joint communication, sensing, and multi-tier computing systems,” IEEE J. Sel. Areas Commun., vol. 41, no. 3, pp. 574–588, Mar. 2023.  
[25] N. Huang et al., “Mobile edge computing aided integrated sensing and communication with short-packet transmissions,” IEEE Trans. Wireless Commun., vol. 23, no. 7, pp. 7759–7774, Jul. 2024.  
[26] Y. Sun, J. Xu, and S. Cui, “User association and resource allocation for MEC-enabled IoT networks,” IEEE Trans. Wireless Commun., vol. 21, no. 10, pp. 8051–8062, Oct. 2022.  
[27] Z. Yang, C. Pan, K. Wang, and M. Shikh-Bahaei, “Energy efficient resource allocation in UAV-enabled mobile edge computing networks,” IEEE Trans. Wireless Commun., vol. 18, no. 9, pp. 4576–4589, Sep. 2019.  
[28] S. M. Kay, Fundamentals of Statistical Signal Processing: Detection Theory. Upper Saddle River, NJ, USA: Prentice-Hall, 1998.  
[29] Y. Chen, Y. Wang, J. Zhang, and M. D. Renzo, “QoS-driven spectrum sharing for reconfigurable intelligent surfaces (RISs) aided vehicular networks,” IEEE Trans. Wireless Commun., vol. 20, no. 9, pp. 5969–5985, Sep. 2021.  
[30] W. U. Khan, F. Jameel, N. Kumar, R. Jantti, and M. Guizani, ¨ “Backscatter-enabled efficient V2X communication with nonorthogonal multiple access,” IEEE Trans. Veh. Technol., vol. 70, no. 2, pp. 1724–1735, Feb. 2021.  
[31] A. Farina, Introduction to Radar Signal and Data Processing: The Opportunity. Rome, Italy: SELEX Sistemi Integrati, 2006.  
[32] A. Farina and F. Studer, “Radar data processing. Volume 2-advanced topics and applications,” NASA STI/Recon Tech. Rep. A, vol. 86, no. 3, pp. 331–332, Feb. 1986.  
[33] Y.-F. Liu et al., “A survey of recent advances in optimization methods for wireless communications,” IEEE J. Sel. Areas Commun., vol. 42, no. 11, pp. 2992–3031, Nov. 2024.  
[34] X.-D. Zhang, Matrix Analysis and Applications. Cambridge, U.K.: Cambridge Univ. Press, 2017.  
[35] J. L. Jerez, P. J. Goulart, S. Richter, G. A. Constantinides, E. C. Kerrigan, and M. Morari, “Embedded online optimization for model predictive control at megahertz rates,” IEEE Trans. Autom. Control, vol. 59, no. 12, pp. 3238–3251, Dec. 2014.

![](images/432cf9a8c851378f16798913c69257ecf0a92e437e99cf7badc6014bca4a9466.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a white shirt (no text or symbols visible)
</details>

Peng Liu (Graduate Student Member, IEEE) received the bachelor’s degree in electronic engineering and the master’s degree in information and communication engineering from Beijing Institute of Technology, Beijing, China, in 2020 and 2023, respectively, where he is currently pursuing the Ph.D. degree with the Research Institute of Communication Technology. His research interests include integrated sensing and communications, mobile edge computing, and physical layer security.

![](images/210dc260873166f46d8f6ad9ce48a8374d5834dfb2210ca6eb20e387ca49da27.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a suit (no text or symbols visible)
</details>

Xinyi Wang (Member, IEEE) received the B.Eng. and Ph.D. degrees in information and communication engineering from Beijing Institute of Technology (BIT) in 2017 and 2022, respectively. From 2023 to 2024, he was a Post-Doctoral Researcher with BIT, where he is currently an Associate Professor. His research interests include integrated sensing and communications, multi-carrier modulation techniques, and low-altitude wireless networks. He is a Founding Member of the IEEE ComSoc Special Interest Group (SIG) on LAWN and served as a

TPC member for multiple IEEE flagship conferences. He was a recipient of the Best Paper Award in WOCC 2019 and a co-recipient of the Excellent Paper Award in ICSIDP 2024 and the Nomination Award for Outstanding Doctoral Dissertation by China Education Society of Electronics (CESE). He has been recognized as an Exemplary Reviewer for IEEE TRANSACTIONS ON COMMUNICATIONS and listed among the World’s Top 2% Scientists by Stanford University for citation impact in 2025.

![](images/7f855fafa4c94e71fc6fea9f55b12b84b679718bdacfcb97c6000e50b3d19eea.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses, suit, and tie (no text or symbols visible)
</details>

Zesong Fei (Senior Member, IEEE) received the Ph.D. degree from Beijing Institute of Technology (BIT), Beijing, China, in 2004. He is currently a Professor with the Research Institute of Communication Technology, BIT. His research interests include wireless communications and signal processing, including integrated sensing and communications, physical layer security, AAV communications, intelligent reflecting surface, channel coding, and multiple access. He is a fellow of China Institute of Communications. He has authored or co-authored

over 200 journal and conference papers and was a co-recipient of the Best Paper Award in WCSP 2012, Chinacom 2012, Chinacom 2013, and PIMRC 2015. He serves as an Associate Editor for IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY.

![](images/041b67bfbd1bde4d63f93b8a9eef4e04b14d9e2e11902495d199acc00783a4b3.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a striped shirt against a blue background (no text or symbols visible)
</details>

Yuan Wu (Senior Member, IEEE) is currently a Full Professor with the State Key Laboratory of Internet of Things for Smart City and the Department of Computer and Information Science, University of Macau, Macau, China. His research interests include resource management for wireless networks, mobile edge computing and edge intelligence, and integrated sensing and communications. He was a recipient of the Best Paper Award from the IEEE ICC’2016, IEEE TCGCC’2017, IWCMC’2021, and IEEE WCNC’2023. He is on the Editorial Board

of IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, IEEE TRANSAC-TIONS ON NETWORK SCIENCE AND ENGINEERING, and IEEE INTERNET OF THINGS JOURNAL. He is a Distinguished Lecturer of the IEEE Vehicular Technology Society (VTS).

![](images/2d1f056a806598c621773be6da2973b48cf4871b14c28865ac8415a3effa8ad7.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a suit (no text or symbols visible)
</details>

Jie Xu (Fellow, IEEE) received the B.E. and Ph.D. degrees from the University of Science and Technology of China. He is currently an Associate Professor (Tenured) with the School of Science and Engineering, Shenzhen Future Network of Intelligence Institute (FNii-Shenzhen), and Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong at Shenzhen. His research interests include wireless communications, wireless information and power transfer, AAV communications, edge computing and

intelligence, and integrated sensing and communication (ISAC). He was a recipient of the 2017 IEEE Signal Processing Society Young Author Best Paper Award, the IEEE/CIC ICCC 2019 Best Paper Award, the 2019 IEEE Communications Society Asia–Pacific Outstanding Young Researcher Award, and the 2019 Wireless Communications Technical Committee Outstanding Young Researcher Award. He is the Symposium Co-Chair of the IEEE GLOBECOM 2019 Wireless Communications Symposium and the IEEE ICC 2025 Communication Theory Symposium, the workshop co-chair of several IEEE ICC and GLOBECOM workshops, the Tutorial Co-Chair of the IEEE/CIC ICCC 2019/2022, the Chair of the IEEE Wireless Communications Technical Committee (WTC), and the Vice Co-Chair of the IEEE Emerging Technology Initiative (ETI) on ISAC. He served or is serving as the Associate Editor-in-Chief for IEEE TRANSACTIONS ON MOBILE COMPUTING, an Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE WIRELESS COMMUNICA-TIONS LETTERS, and Journal of Communications and Information Networks, an Associate Editor for IEEE ACCESS, and a Guest Editor for the IEEE WIRELESS COMMUNICATIONS, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, IEEE Internet of Things Magazine, Science China Information Sciences, and China Communications. He is a Distinguished Lecturer of the IEEE Communications Society.

![](images/408937dcd9f44c611368c81df410f8c498111d01b995ee0877ba6e22902aabf6.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a suit (no text or symbols visible)
</details>

Arumugam Nallanathan (Fellow, IEEE) has been a Professor of wireless communications and the Head of the Communication Systems Research (CSR) Group, School of Electronic Engineering and Computer Science, Queen Mary University of London, since September 2017. He was with the Department of Informatics, King’s College London, from December 2007 to August 2017, where he was a Professor of wireless communications from April 2013 to August 2017 and a Visiting Professor from September 2017 to August 2020. He was an Assis-

tant Professor with the Department of Electrical and Computer Engineering, National University of Singapore, from August 2000 to December 2007. He has published more than 700 technical papers in scientific journals and international conferences. His research interests include artificial intelligence for wireless systems, beyond 5G wireless networks, and the Internet of Things (IoT).

Dr. Nallanathan was a co-recipient of the best paper awards presented at the IEEE International Conference on Communications 2016 (ICC’2016), the IEEE Global Communications Conference 2017 (GLOBECOM’2017), the IEEE Vehicular Technology Conference 2018 (VTC’2018), and the IEEE Communications Society Leonard G. Abraham Prize in 2022. He is an IEEE Distinguished Lecturer. He was selected as a Web of Science Highly Cited Researcher in 2016 and (2022–2024). He received the IEEE Communications Society SPCE Outstanding Service Award 2012 and the IEEE Communications Society RCC Outstanding Service Award 2014. He served as the Chair for the Signal Processing and Communication Electronics Technical Committee of IEEE Communications Society and the technical program chair and a member of technical program committees for numerous IEEE conferences. He was a Senior Editor of IEEE WIRELESS COMMUNICATIONS LETTERS; and an Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, and IEEE SIGNAL PROCESSING LETTERS.