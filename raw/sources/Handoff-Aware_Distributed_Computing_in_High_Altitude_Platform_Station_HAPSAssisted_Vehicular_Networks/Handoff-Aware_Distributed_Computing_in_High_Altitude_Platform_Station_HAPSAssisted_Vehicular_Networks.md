# Handoff-Aware Distributed Computing in High Altitude Platform Station (HAPS)–Assisted Vehicular Networks

Qiqi Ren , Omid Abbasi , Senior Member, IEEE, Gunes Karabulut Kurt , Senior Member, IEEE, Halim Yanikomeroglu , Fellow, IEEE, and Jian Chen , Member, IEEE

Abstract— Distributed computing enables Internet of vehicle (IoV) services by collaboratively utilizing the computing resources from the network edge and the vehicles. However, the computing interruption issue caused by frequent edge network handoffs, and a severe shortage of computing resources are two problems in providing IoV services. High altitude platform station (HAPS) computing can be a promising addition to existing distributed computing frameworks because of its wide coverage and strong computational capabilities. In this regard, this paper proposes an adaptive scheme in a new distributed computing framework that involves HAPS computing to deal with the two problems of the IoV. Based on the diverse demands of vehicles, network dynamics, and the time-sensitivity of handoffs, the proposed scheme flexibly divides each task into three parts and assigns them to the vehicle, roadside units (RSUs), and a HAPS to perform synchronous computing. The scheme also constrains the computing of tasks at RSUs such that they are completed before handoffs to avoid the risk of computing interruptions. On this basis, we formulate a delay minimization problem that considers task-splitting ratio, transmit power, bandwidth allocation, and computing resource allocation. To solve the problem, variable replacement and successive convex approximation–based method are proposed. The simulation results show that this scheme not only avoids the negative effects caused by handoffs in a flexible manner, it also takes delay performance into account and maintains the delay stability.

Index Terms— Internet of Vehicles (IoV), high altitude platform station (HAPS), distributed computing, edge network handoff.

## I. INTRODUCTION

## A. Background

munication, the Internet of things, and artificial intelligence (AI), a concept of Internet of vehicles (IoV) has also gained great momentum, where autonomous driving is considered to be the ultimate goal [1], [2]. An intelligent and connected vehicle (ICV), which is the main component of the IoV, will integrate sensing, decision-making, and control functions. In the future, ICVs will realize the transformation of massive information from physical space to information space, and this transformation will depend on fine-grained data computation, including various machine learning-based models of training and inference [3], [4]. In the past few years, the field of machine learning has undergone a major shift from a big-data paradigm of centralized cloud processing to a small-data paradigm of distributed processing by devices at a network edge [5], [6]. The impetus for this shift is to synchronously utilize locally available resources and nearby resources of edge nodes to obtain real-time responses for AIbased task computing, thereby facilitating the development of distributed computing [7], [8]. Due to the advantages of distributed computing, such as proximity, efficiency, scalability, and easy collaboration, it is expected to play an important role in realizing autonomous driving.

Autonomous driving is expected to produce terabytes of data everyday [9]. In this context, the IoV of the future is likely to face a continuous shortage of computing resources, and this shortage will be more severe than for ordinary user networks. This prediction is driven by two reasons: First, unlike ordinary users, which only occupy resources when they are in use, ICVs are generally online for a long time, and therefore they occupy computing resources continuously. Secondly, IoV services require a higher level of security than ordinary user services. Providing good IoV services is directly related to road and personal safety, which means that a shortage of computing resources will present serious security problems [10]. To address this problem, a variety of solutions have been proposed, including vehicle collaborative computing, unmanned aerial vehicle (UAV) computing and satellite computing to complement edge computing and form new distributed computing frameworks [11], [12], [13], [14]. However, interruptions between vehicle-to-vehicle connections, short and unreliable UAV dwelling times, prohibitive satellite transmission delays, and complicated mobility management make it difficult to meet the demands of IoV in terms of security, stability, and reliability. This motivates us to explore other, more feasible solutions. More recently, high altitude platform station (HAPS) systems have been proposed as candidates for 6G networks [15], [16]. A HAPS is aerial platform, such as an airship or balloon, capable of longterm deployment as a wireless communication station in the stratosphere, where it has a bird’s-eye line-of-sight (LoS) view over a large ground area (with a radius of 50-500 km) [17]. Since HAPSs have large payloads (usually ≥ 100 kg), they can carry a variety of resources (antennas, capacity, computation, storage, and so on), which can play a powerful supplementary role for ground computing systems [18], [19]. Besides, current and future energy conversion techniques for solar energy and wind power as well as battery techniques can provide HAPS with a powerful energy supply potential [20], [21], [22]. Much work has been done to demonstrate the gains for introducing HAPS computing to IoT networks in terms of energy and delay performances [16], [23]. Inspired by this, we introduced HAPS computing into vehicular networks in our recent work [24] and proposed a computation offloading scheme to accelerate IoV services.

In addition to the prospect of severe shortages of computing resources, the IoV of the future also faces the issue of network handoffs. In practice, edge nodes usually have a small communication coverage (less than 300 m [25]). To ensure the connections of networks and the sustainability of services, ICVs will inevitably trigger the network connection handoff when they cross the coverage of different edge nodes. However, when a network handoff occurs, the ICV may experience a temporary interruption of the offloading process, or it may be unable to directly receive computation results due to being beyond the coverage of the computing target node. To address this, researchers have proposed a series of computing offloading solutions to cope with handoff issues [26], [27], [28], [29], [30], [31]. The authors in [26], [27] considered computational performance metrics to design handoff schemes. In [26], they studied how to maximize the connection time between vehicles and edge servers while minimizing the number of handoff times. In [27], while taking a shortage of edge server resources into consideration, they used remote cloud computing resources to assist in computing the tasks that could not be processed in time by the connected edge servers on the basis of jointly optimized network handoff and task migration decisions. However, the issue of IoV handoffs can be affected by a variety of factors, including received signal strength, vehicle speed, reliability, efficiency. Moreover, considering multi-dimensional factors in making handoff decisions complicates the problem-solving process [32], [33], [34]. In this regard, [28], [29], [30], [31] designed computing migration schemes to adapt to network handoffs, and eliminate their negative impact on computing performance. Accordingly, [28] proposed a scheme to migrate tasks among multiple servers when a handoff occurred. Reference [29] set a “hold on” mode for tasks, where vehicles would suspend task scheduling when tasks could not be processed before connecting to the next available server. Given that task results might not reach a vehicle due a handoff, H. Zhang et al. proposed to migrate the results among multiple servers [30]. Based on the assumption that path planning is predictable, [31] proposed a predictive uploading and downloading of computing tasks and results to improve the efficiency of result acquisition.

## B. Motivation and Contributions

From existing solutions, we know that the dominant approaches for adapting to edge network handoffs in distributed computing involves computing migration among edge nodes. However, these approaches are inflexible and their performance cannot be guaranteed. Specifically, most approaches have proposed to take compensatory measures for the computing tasks affected by handoffs, such as task and result migration, task re-offloading, and task postponement. While these designs aim to ensure that tasks can be performed or results successfully delivered, such approaches are passive and inflexible. Moreover, since only edge node resources are considered, tasks or their results usually need to be migrated among multiple edge nodes, which will cause a long response time or even unresponsiveness, thus resulting in a wildly fluctuating performance or even computing failure. Therefore, to cope with handoffs, the computing offloading scheme needs to avoid the negative impact of handoff on computing, and at the same time it needs to ensure the low-latency performance of computing tasks in both handoff and non-handoff cases to provide a smooth and stable service experience for ICVs.

Fortunately, a HAPS can help solve the above mentioned problems. With its bird’s-eye view of the ground and powerful computing resources, a HAPS can help absorb atypical demand surges and avoid computing interruptions caused by edge network handoffs. Therefore, the introduction of HAPS computing into IoV systems can both alleviate computing resource shortages and effectively deal with the handoff issue, which makes perfect sense for ICVs. In view of this critical observation, we follow the distributed computing framework proposed in our recent work [24]. On this basis, we propose a handoff-aware computing offloading scheme to deal with the computing interruption problem. In this scheme, the task will be dynamically split and distributedly assigned to the ICV, RSU, and HAPS nodes for synchronous processing, which means that an ICV’s task can be processed in parallel through the coordination of these three node types. Accordingly, when a network handover is about to happen, the RSU is only responsible for a very small amount of data processing to ensure that the task portion assigned to this node can be computed before the handoff occurs, while the HAPS bears most of the computational burden to smoothly complete the computing of the task. The contributions of this work are as follows:

![](images/b6a3fd483bd605c9c8baccdb712972cdce9de052a1fba5a259956ce62a452fae.jpg)  
Fig. 1. Handoff-aware distributed computing in in a HAPS-assisted vehicular network.

1) We develop a handoff-aware computing scheme by exploiting a distributed computing framework that integrates the computing resources of ICVs, RSUs, and HAPS nodes. Different from the existing solutions in edge network, this scheme utilizes the HAPS-assisted distributed framework to deal with the computing interruption issue caused by edge network handoffs in a flexible manner. To the best of our knowledge, this is the first work to investigate the benefits of HAPS computing for this topic.<sup>1</sup>

2) Due to the diverse needs of ICVs, network dynamics, and the time-sensitivity of handoffs, this scheme flexibly divides the tasks of each user into three parts and assigns them to ICVs, RSUs, and HAPS nodes to perform synchronous computing. In addition, this scheme constrains the computing of tasks at the RSUs so that they are completed before a handoff is about to occur, thereby avoiding the risk of a computing interruption.

3) With the objective of minimizing the delay in executing ICVs’ tasks, we formulate an optimization problem by finding task-splitting ratios, ICV transmit power, bandwidth allocation, and computing resource allocation. Then, using variable replacement and successive convex approximation (SCA) methods, we solve the optimization problem.

## II. HANDOFF-AWARE DISTRIBUTED COMPUTING MODEL A. System Model

The handoff-aware distributed computing model considered here for a HAPS-assisted vehicular network is shown in Fig. 1. A single HAPS at an altitude of 20 km provides coverage for a one-way road [35]. The road is divided into M nonoverlapping segments, each covered by an edge network access point, i.e., RSU. Each RSU is equipped with a computing server to process vehicular computing tasks, and both RSUs and their equipped computing resources can be considered as edge network resources in the system. These RSUs are labeled as $\mathcal { M } = \{ 1 , 2 , \dots , M \}$ in order. We assume that the coverage range of the RSUs is D (m). There are N ICVs, labeled as $\mathcal { N } = \{ 1 , 2 , \dots , N \}$ , running at a speed of v (m/s) along the road, and each ICV passes through the coverage range of the RSUs in order. This means that a handoff occurs when an ICV passes from one RSU coverage area to another. At the beginning of each decision time slot, the ICV n runs from its current position $l _ { n }$ (m), and generates one task to be computed, with the input data size $\varepsilon _ { n }$ (in bits) and computational density $\lambda _ { n }$ (in CPU Cycle/bit). Assuming the task is splittable, we consider a distributed parallel computing model, which is shown in Fig. 2. In this model, the task can be split into three portions and computed at three nodes simultaneously (i.e., at the ICV’s onboard device, at the associated RSU, and at the HAPS), which corresponds to three computing ways: local, RSU, and HAPS computing, respectively. Local computing can directly process the task portion it is assigned, while the task portions that are assigned to the RSU and HAPS need to be offloaded to the RSU and HAPS separately before the computing can be performed on their servers. In this work, we do not discuss the downloading of results because the amount of such data is small compared to the input data. Given that delay performance is critical for IoV services, and this performance influences vehicle and road safety as well as the driver’s experience, this work is dedicated to improving the delay performance of ICVs in performing computing tasks.

![](images/9016be4883dfbf3c88d0ab6e077d296ba077f8b428cc5ee2265c59c2df7d09f1.jpg)  
Fig. 2. Distributed parallel computing model.

Based on the model shown in Fig. 2, the data splitting model is described as follows: for ICV n, the data splitting ratio at its associated RSU node is indicated by $x _ { n } ^ { R } .$ , at the HAPS node is indicated by $x _ { n } ^ { H }$ , and at its onboard device is indicated by $1 - x _ { n } ^ { R } - \dot { x } _ { n } ^ { H }$ . The task splitting strategy is dynamically determined rather than using a fixed assignment. It depends on real-time channel conditions, the association between users and RSUs, variational task requirements (data volume and computational density), and available bandwidth and computing resource capacity [36]. In addition to these factors, the handoff issue of the edge network is also considered by adjusting the data splitting ratios in a flexible manner so that the task portion computed at the RSU is not interrupted by a handoff. Fig. 3 provides an illustration of a handoff. As we can see, at the beginning of a decision time slot, the ICV n moves from position A to network boundary B and is about to enter the coverage of the next RSU, which triggers a network handoff. According to the ICV’s initial speed v (m/s) and its position $l _ { n } ,$ the handoff timestamp can be given by $\begin{array} { r } { T _ { n } ^ { h a n d o f f } = \frac { D - \lvert l _ { n } ^ { ' \nu } \mod D \rvert } { v } } \end{array}$ , where $| l _ { n }$ mod D| is the remainder of dividing $l _ { n }$ by D, which indicates ICV n’s relative position from its associated RSU<sup>2</sup> $T _ { n } ^ { h a n d o f f }$ describes the time it takes for ICV n to run out of the RSU coverage boundary. During this journey, ICV n offloads a partial task with a splitting ratio $x _ { n } ^ { \bar { R } }$ to the RSU, and then the RSU server computes the assigned task portion. To ensure that the data processing will not be interrupted by the network handoff, the delay experienced must be guaranteed not to exceed the timestamp when the handoff occurs, i.e., $T _ { n } ^ { h a n d o f f }$ , which can be viewed as a hard time limit. If the processing delay of the task portion at RSU is greater than $T _ { n } ^ { h a n d o f f }$ , the corresponding portion will be dropped.

![](images/d1280a70d4f766f0b94a99b251e116e90067be9c6ffa8783ab4681807dbac3f2.jpg)  
Fig. 3. Illustration of handoff.

## B. Communication Model

In this system, we consider that both RSUs and ICVs are equipped with a single antenna, while the HAPS is equipped with multiple antennas. Based on this assumption, there are a very high number of spotbeams in HAPS network and that the target area is within a spotbeam [24]. At each time slot, the ICV n needs to offload the input data of the task portion with size $x _ { n } ^ { R } \varepsilon _ { n }$ to the associated RSU, while offloading the input data of the task portion with size $x _ { n } ^ { H } \varepsilon _ { n }$ to the HAPS at the same time. Therefore, the communication links are of two types: links between ICVs and RSUs; and links between ICVs and the HAPS. We consider a carrier frequency of 2 GHz for all links, and these links work on orthogonal channels. Given the available bandwidth $B _ { \mathrm { m a x } } .$ , the bandwidths for these orthogonal links are optimally allocated. For ICV n, the bandwidth ratios allocated to the links from the ICV to the RSU and from the ICV to the HAPS are indicated by $b _ { n } ^ { R }$ and $b _ { n } ^ { H }$ , respectively. The bandwidth allocation should satisfy the compacity constraint $\sum _ { n \in \mathcal { N } } b _ { n } ^ { R } + b _ { n } ^ { H } \leq 1$ . In addition, due to the limitations of the transmit power of ICVs, the power allocation is also investigated with the given $P _ { \mathrm { m a x } }$ . For ICV $n ,$ the power allocation ratios for the links from ICV n to the RSU and from ICV n to the HAPS are indicated by $p _ { n } ^ { R }$ and $p _ { n } ^ { H }$ , respectively. Here, we use $p _ { n } ^ { R } + p _ { n } ^ { H } \leq 1 , \forall n \in \dot { \mathcal { N } }$ to constrain the power allocation for the ICVs. We consider nonline-of-sight (NLoS) communication for the link from ICV n to the RSU, and the channel gain is modeled as

$$
G _ {n} ^ {R} = \frac {\beta_ {0} (f _ {c}) \big | h _ {n} ^ {R} \big | ^ {2}}{(d _ {n} ^ {R}) ^ {\alpha}},\tag{1}
$$

where $\beta _ { 0 } ( f _ { c } )$ is the path loss at the reference distance 1 m, $h _ { n } ^ { R }$ is the small-scale fading coefficient of the NLoS link following a Rayleigh distribution, $d _ { n } ^ { R }$ is the distance from ICV n to the RSU, and α is the path-loss exponent. The corresponding transmission rate is given by $\begin{array} { r } { R _ { n } ^ { \dot { R } } = b _ { n } ^ { R } B _ { \mathrm { m a x } } \mathrm { l o g } _ { 2 } \left( \dot { 1 } + \frac { p _ { n } ^ { R } \check { P } _ { \mathrm { m a x } } G _ { n } ^ { R } } { b _ { n } ^ { R } B _ { \mathrm { m a x } } N _ { 0 } } \right) } \end{array}$ , where $N _ { 0 }$ is the Gaussian noise power spectrum density.

Since the HAPS hovers in a high altitude and the highway is usually in a remote area, we consider the links from the ICVs to the HAPS to be LoS with their large-scale fading path loss following free-space path loss. The channel gain can be modeled by [37]:

$$
G _ {n} ^ {H} = G \left(\frac {c}{4 \pi d _ {n} ^ {H} f _ {c}}\right) ^ {2} \left| h _ {n} ^ {H} \right| ^ {2},\tag{2}
$$

where c is the speed of light, $d _ { n } ^ { H }$ is the distance from ICV n to the HAPS. $f _ { c }$ is the carrier frequency, which in this work we consider to be 2 GHz. Since environmental effects are negligible for the frequencies under 10 GHz, environmental attenuations are not considered in this work [38]. G is the directional antenna gain, and $h _ { n } ^ { H }$ is the small-scale fading coefficient corresponding to Rice fading that considers the LoS component. The corresponding transmission rate is given by $\begin{array} { r } { R _ { n } ^ { H } = b _ { n } ^ { H } B _ { \mathrm { m a x } } \mathrm { l o g } _ { 2 } \left( 1 ^ { ' } + \frac { p _ { n } ^ { H } P _ { \mathrm { m a x } } G _ { n } ^ { H } } { b _ { n } ^ { H } B _ { \mathrm { m a x } } N _ { 0 } } \right) } \end{array}$ . With the transmission rate, the delay for offloading the task portion of ICV n with size $x _ { n } ^ { R } \varepsilon _ { n }$ to the RSU can be modeled as $\frac { x _ { n } ^ { R } \varepsilon _ { n } } { R _ { n } ^ { R } }$ , and the delay for offloading the task portion of ICV n with size $x _ { n } ^ { H } \varepsilon _ { n }$ can be modeled as $\frac { x _ { n } ^ { H } \varepsilon _ { n } } { R _ { n } ^ { H } }$ . In addition, the propagation delays taken for the ICV’s signals to reach the RSU and HAPS are given by $\frac { d _ { n } ^ { R } } { c }$ and $\frac { d _ { n } ^ { H } } { c }$

## C. Computing Model

It is assumed that at each decision time slot, each ICV generates one task to compute that can be split into three portions and computed at three nodes in parallel. The available computing resources for ICVs doing local, RSU, and HAPS computing are indicated by ${ \boldsymbol { F } } ^ { L } , { \boldsymbol { F } } ^ { { \bar { R } } }$ , and $F ^ { H }$ (in CPU Cycle/s), respectively. After the splitting, the task portion assigned to the RSU with workloads $\bar { x _ { n } ^ { R } } \varepsilon _ { n } \lambda _ { n } ^ { \bar { ( } }$ will be computed at the RSU server, the task portion assigned to the HAPS with workloads $x _ { n } ^ { H } \varepsilon _ { n } \lambda _ { n }$ will be computed at the HAPS, and the task portion assigned to the ICV with workloads $( 1 - x _ { n } ^ { R } - x _ { n } ^ { \bar { H } } ) \varepsilon _ { n } \lambda _ { n }$ will be computed locally. The computing resources will be optimized at the RSU servers and HAPS server. For RSU computing, the computing resources will be allocated among the ICVs in the RSU’s covered segment. We let $\Phi _ { m }$ denote the ICV index set of RSU $m , m \in { \mathcal { M } } .$ . Let $f _ { n } ^ { R }$ indicate the computing resource ratio allocated for ICV n at its associated RSU server, so the computing resource allocation limitation at RSU m is given by $\sum _ { n \in \Phi _ { m } } ^ { \bullet } f _ { n } ^ { \breve { R } } \leq 1 , \forall m \in { \mathcal { M } }$ . Let $f _ { n } ^ { H }$ indicate the computing resource ratio allocated at the HAPS server for ICV n, and the computing resource allocation limitation at HAPS is constrained by $\sum _ { n \in \mathcal { N } } f _ { n } ^ { H } \ \leq \ 1$ . Furthermore, the computational delays can be expressed as $\frac { ( 1 - x _ { n } ^ { R } - x _ { n } ^ { H } ) \varepsilon _ { n } \lambda _ { n } } { F ^ { L } }$ for local computing, $\frac { x _ { n } ^ { \dot { R } } \varepsilon _ { n } \lambda _ { n } } { f _ { n } ^ { R } F ^ { R } }$ for RSU computing, and $\frac { x _ { n } ^ { H } \varepsilon _ { n } \lambda _ { n } } { f _ { n } ^ { H } F ^ { H } }$ for HAPS computing, respectively.

## D. Delay Model

Using the above communication and computing models, the delays for ICV n with local, RSU, and HAPS computing can be given as follows:

1) Local computing:

$$
T _ {n} ^ {L} = \frac {(1 - x _ {n} ^ {R} - x _ {n} ^ {H}) \varepsilon_ {n} \lambda_ {n}}{F ^ {L}}.\tag{3}
$$

2) RSU computing:

$$
T _ {n} ^ {R} = \frac {d _ {n} ^ {R}}{c} + \frac {x _ {n} ^ {R} \varepsilon_ {n}}{b _ {n} ^ {R} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {R} P _ {\max} G _ {n} ^ {R}}{b _ {n} ^ {R} B _ {\max} N _ {0}}\right)} + \frac {x _ {n} ^ {R} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {R} F ^ {R}}.\tag{4}
$$

3) HAPS computing:

$$
T _ {n} ^ {H} = \frac {d _ {n} ^ {H}}{c} + \frac {x _ {n} ^ {H} \varepsilon_ {n}}{b _ {n} ^ {H} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {H} P _ {\max} G _ {n} ^ {H}}{b _ {n} ^ {H} B _ {\max} N _ {0}}\right)} + \frac {x _ {n} ^ {H} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {H} F ^ {H}}.\tag{5}
$$

The delay for ICV n is ultimately determined by the maximum value of $\dot { T } _ { n } ^ { L } , T _ { n } ^ { R }$ and $T _ { n } ^ { H } .$ 3

## III. SUM-DELAY MINIMIZATION

In this section, we first formulate the optimization problem that minimizes the total delay of all ICVs in order to improve the average delay performance of the system. Then, we provide the problem transformation and solution for the formulated problem.

## A. Problem Formulation

We aim to optimize the sum-delay experienced by ICVs for executing tasks by finding the optimal values for the task-splitting ratios of RSU $\mathbf { \bar { X } } ^ { R } = [ x _ { 1 } ^ { R } , \dots , x _ { N } ^ { R } ]$ , the tasksplitting ratios of HAPS $\mathbf { X } ^ { H } = [ x _ { 1 } ^ { H } , \dots , x _ { N } ^ { H } ]$ , bandwidth allocations of the links from ICVs to RSU $\ddot { \bf B } ^ { R } = [ b _ { 1 } ^ { R } , \ldots , b _ { N } ^ { R } ] .$ bandwidth allocations of the links from ICVs to HAPS $\mathbf { B } ^ { H } = [ b _ { 1 } ^ { H } , \dots , b _ { N } ^ { H } ]$ , power allocations of the links from

TABLE I  
NOTATION DEFINITIONS

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\mathcal{M}, M$ </td><td>The RSU set and the number of RSUs</td></tr><tr><td> $\mathcal{N}, N$ </td><td>The ICV set and the number of ICVs</td></tr><tr><td> $\varepsilon$ </td><td>Volume of input data (Kbits)</td></tr><tr><td> $\lambda$ </td><td>Computation density (CPU cycle/bit)</td></tr><tr><td> $x_{n}^{R}, x_{n}^{H}$ </td><td>The data splitting ratio at RSU node, and HAPS node</td></tr><tr><td> $D$ </td><td>The coverage range of RSU (m)</td></tr><tr><td> $F^{L}, F^{R}, F^{H}$ </td><td>Computational capability of ICV, RSU and HAPS (CPU cycle/s)</td></tr><tr><td> $G^{R}, G^{H}, G$ </td><td>Link channel gain of RSU, link channel gain of HAPS, and directional antenna gain</td></tr><tr><td> $d^{R}, d^{H}$ </td><td>The link distance of RSU and HAPS (m)</td></tr><tr><td> $c, f_{c}, \alpha, \beta_{0}$ </td><td>Light speed (m/s), carrier frequency (Hz), NLoS link path loss factor, and NLoS link reference path loss</td></tr><tr><td> $h^{R}, h^{H}$ </td><td>LoS link small-scale fading coefficient and NLoS link small-scale fading coefficient</td></tr><tr><td> $N_{0}$ </td><td>Gaussian noise power spectrum density (dBm/Hz)</td></tr><tr><td> $B_{\text{max}}, R^{R}, R^{H}$ </td><td>Bandwidth limitation (MHz), transmission rate from ICV to RSU, and transmission rate from ICV to HAPS (bit/s)</td></tr><tr><td> $f, b$ </td><td>Computing resource allocation ratio and bandwidth allocation ratio</td></tr><tr><td> $P_{\text{max}}$ </td><td>Transmitter power limitation of ICV (dBm)</td></tr><tr><td> $T^{L}, T^{R}, T^{H}$ </td><td>Delay under local, RSU, and HAPS computing (s)</td></tr><tr><td> $T_{n}^{\text{handoff}}$ </td><td>The time to trigger handoff (s)</td></tr></table>

ICVs to RSU $\mathbf { P } ^ { R } = [ p _ { 1 } ^ { R } , \dots , p _ { N } ^ { R } ]$ , power allocations of the links from ICVs to HAPS $\mathbf { P } ^ { H } = [ p _ { 1 } ^ { H } , \dots , p _ { N } ^ { H } ]$ , computing resource allocations of RSU $\mathbf { F } ^ { R } = [ f _ { 1 } ^ { R } , \dots , f _ { N } ^ { R } ]$ , and computing resource allocations of HAPS $\mathbf { F } ^ { H } = [ f _ { 1 } ^ { H } , \dots , f _ { N } ^ { H } ]$ . The optimization problem can be formulated as follows:

$$
\min_{\substack{\boldsymbol{x}^{R},\boldsymbol{x}^{H},\boldsymbol{b}^{R},\boldsymbol{b}^{H},\\ \boldsymbol{p}^{R},\boldsymbol{p}^{H},\boldsymbol{f}^{R},\boldsymbol{f}^{H}}} \sum_{n}^{N}\max \left\{T_{n}^{L},T_{n}^{R},T_{n}^{H}\right\}\tag{6a}
$$

$$
\mathrm{s.t.} T _ {n} ^ {R} \leq T _ {n} ^ {\text { handoff }}, \forall n \in \mathcal {N},\tag{6b}
$$

$$
\sum_ {n \in \mathcal {N}} b _ {n} ^ {R} + b _ {n} ^ {H} \leq 1,\tag{6c}
$$

$$
p _ {n} ^ {R} + p _ {n} ^ {H} \leq 1, \forall n \in \mathcal {N},\tag{6d}
$$

$$
\sum_ {n \in \Phi_ {m}} f _ {n} ^ {R} \leq 1, \forall m \in \mathcal {M},\tag{6e}
$$

$$
\sum_ {n \in \mathcal {N}} f _ {n} ^ {H} \leq 1,\tag{6f}
$$

$$
x _ {n} ^ {R}, x _ {n} ^ {H}, b _ {n} ^ {R}, b _ {n} ^ {H}, p _ {n} ^ {R}, p _ {n} ^ {H}, f _ {n} ^ {R}, f _ {n} ^ {H} > 0.\tag{6g}
$$

Since we consider parallel task computing, the ICV’s delay is the maximum value of the delay to perform the task on the local, RSU, and HAPS, i.e., max $\left\{ T _ { n } ^ { L } , T _ { n } ^ { R } , T _ { n } ^ { H } \right\}$ . In Problem (6), the objective function (6a) is the total delay of ICVs. The constraint (6b) indicates that the task portion that is assigned to the RSU should be completed before the handoff occurs. (6c) denotes the bandwidth constraint for all links. (6d) denotes the transmit power constraint for each ICV. (6e) denotes the computing resource constraint for each RSU, and (6f) denotes the computing resource constraint for HAPS. Finally, (6g) indicates the non-negative requirements for all variables. It is clear that Problem (6) is nonconvex due to the non-smooth objective function, coupled variables, and complicated formulations. This is a difficult problem to solve directly, and there is no standard method to address this problem. In the following, we transform the problem into a tractable one.

## B. Problem Transformation and Solution

First of all, we introduce auxiliary variable $\mathrm { T } = [ T _ { 1 } , \dots , T _ { N } ]$ to represent the individual delays, so that the original non-smooth problem is transformed into a smooth one. Further, by expanding the representation of $T _ { n } ^ { L } , T _ { n } ^ { R }$ , and $T _ { n } ^ { H }$ , Problem (6) can be equivalently rewritten as

$$
\min_{\substack{\mathrm{T},\boldsymbol{x}^{R},\boldsymbol{x}^{H},\boldsymbol{b}^{R},\boldsymbol{b}^{H},\\ \boldsymbol{p}^{R},\boldsymbol{p}^{H},\boldsymbol{f}^{R},\boldsymbol{f}^{H}}} \sum_{n}^{N}T_{n}\tag{7a}
$$

$$
\text { s.t. } \quad \frac {(1 - x _ {n} ^ {R} - x _ {n} ^ {H}) \varepsilon_ {n} \lambda_ {n}}{F ^ {L}} \leq T _ {n}, \forall n \in \mathcal {N},
$$

$$
\frac {d _ {n} ^ {R}}{} + \frac {}{} x _ {n} ^ {R} \varepsilon_ {n}\tag{7b}
$$

$$
c ^ {\prime} b _ {n} ^ {R} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {R} P _ {\max} G _ {n} ^ {R}}{b _ {n} ^ {R} B _ {\max} N _ {0}}\right)
$$

$$
+ \frac {x _ {n} ^ {R} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {R} F ^ {R}} \leq T _ {n},
$$

$$
\forall n \in \mathcal {N},\tag{7c}
$$

$$
\frac {d _ {n} ^ {H}}{c} + \frac {x _ {n} ^ {H} \varepsilon_ {n}}{b _ {n} ^ {H} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {H} P _ {\max} G _ {n} ^ {H}}{b _ {n} ^ {H} B _ {\max} N _ {0}}\right)}
$$

$$
+ \frac {x _ {n} ^ {H} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {H} F ^ {H}} \leq T _ {n},\tag{7d}
$$

$$
\frac {d _ {n} ^ {R}}{c} + \frac {x _ {n} ^ {R} \varepsilon_ {n}}{b _ {n} ^ {R} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {R} P _ {\max} G _ {n} ^ {R}}{b _ {n} ^ {R} B _ {\max} N _ {0}}\right)} + \frac {x _ {n} ^ {R} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {R} F ^ {R}}
$$

$$
\leq T _ {n} ^ {\text { handoff }}, \forall n \in \mathcal {N},
$$

$$
(6 c), (6 d), (6 e), (6 f), (6 g).\tag{7e}
$$

(7f)

Next, in order to handle the coupling between the optimization variables in the constraints (7c), (7d), and (7e), we introduce auxiliary variables $\tau ^ { R } { = } [ \tau _ { 1 } ^ { R } , \dots , \tau _ { N } ^ { R } ]$ and $\tau ^ { H } { = } [ \tau _ { 1 } ^ { H } , \dots , \tau _ { N } ^ { H } ]$ to respectively represent the delays of ICVs offloading data to the RSU and HAPS, and relax the corresponding constraints. Then, Problem (7) can be equivalently rewritten as

$$
\min_{\substack{T,\boldsymbol{x}^{R},\boldsymbol{x}^{H},\boldsymbol{b}^{R},\boldsymbol{b}^{H},\\ \boldsymbol{p}^{R},\boldsymbol{p}^{H},\boldsymbol{\tau}^{R},\boldsymbol{\tau}^{H},\boldsymbol{f}^{R},\boldsymbol{f}^{H}}} \sum_{n}^{N}T_{n}\tag{8a}
$$

s.t.

$$
\frac {d _ {n} ^ {R}}{c} + \tau_ {n} ^ {R} + \frac {x _ {n} ^ {R} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {R} F ^ {R}} \leq T _ {n}, \forall n \in \mathcal {N},\tag{8b}
$$

$$
\frac {d _ {n} ^ {H}}{c} + \tau_ {n} ^ {H} + \frac {x _ {n} ^ {H} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {H} F ^ {H}} \leq T _ {n}, \forall n \in \mathcal {N},\tag{8c}
$$

$$
\frac {x _ {n} ^ {R} \varepsilon_ {n}}{b _ {n} ^ {R} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {R} P _ {\max} G _ {n} ^ {R}}{b _ {n} ^ {R} B _ {\max} N _ {0}}\right)} \leq \tau_ {n} ^ {R}, \forall n \in \mathcal {N},\tag{8d}
$$

$$
\frac {x _ {n} ^ {H} \varepsilon_ {n}}{b _ {n} ^ {H} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {H} P _ {\max} G _ {n} ^ {H}}{b _ {n} ^ {H} B _ {\max} N _ {0}}\right)} \leq \tau_ {n} ^ {H},
$$

$$
\forall n \in \mathcal {N},\tag{8e}
$$

$$
\frac {d _ {n} ^ {R}}{c} + \tau_ {n} ^ {R} + \frac {x _ {n} ^ {R} \varepsilon_ {n} \lambda_ {n}}{f _ {n} ^ {R} F ^ {R}} \leq T _ {n} ^ {\text {handoff}}, \forall n \in \mathcal {N},\tag{8f}
$$

$$
\begin{array}{l} (6 c) - (6 f), (7 b), \\ x _ {n} ^ {R}, x _ {n} ^ {H}, b _ {n} ^ {R}, b _ {n} ^ {H}, p _ {n} ^ {R}, p _ {n} ^ {H}, \tau_ {n} ^ {R}, \tau_ {n} ^ {H}, f _ {n} ^ {R}, f _ {n} ^ {H} > 0, \end{array}\tag{8g}
$$

where (8d) guarantees that the communication delays experienced by the ICVs offloading data to the RSU cannot exceed $\tau ^ { R }$ , and (8e) guarantees that the communication delays experienced by the ICVs offloading data to the HAPS cannot exceed $\tau ^ { H }$ . Then, to further address the variable coupling issue, we make the exponential transformations for variables $x ^ { R } , x ^ { H } , \tau ^ { R } , \tau ^ { H } , \dot { f } ^ { R }$ and $f ^ { H }$ . More specifically, the above variables for ICV n can be converted as follows: $x _ { n } ^ { R } \ \equiv \ \exp ( \overline { { { x _ { n } ^ { R } } } } ) , x _ { n } ^ { H } \ =$ exp $( \overline { { x _ { n } ^ { H } } } ) , \tau _ { n } ^ { R } ~ = ~ \mathrm { e x p } ( \overline { { \tau _ { n } ^ { R } } } ) , \tau _ { n } ^ { H }$ = $\mathrm { e x p } ( \overline { { \tau _ { n } ^ { H } } } ) , f _ { n } ^ { R } = \mathrm { e x p } ( \overline { { f _ { n } ^ { R } } } )$ and $f _ { n } ^ { H } = \exp ( \overline { { f _ { n } ^ { H } } } )$ . Then, we can obtain the following optimization problem:

$$
\min_{\substack{T,\overline{x^{R}},\overline{x^{H}},b^{R},b^{H},\\ p^{R},p^{H},\overline{\tau^{R}},\overline{\tau^{H}},f^{R},\overline{f^{H}}}} \sum_{n}^{N}T_{n}\tag{9a}
$$

$$
\text { s.t. } \frac {\varepsilon_ {n} \lambda_ {n}}{F ^ {L}} \left(1 - \exp \left(\overline {{x _ {n} ^ {R}}}\right) - \exp \left(\overline {{x _ {n} ^ {H}}}\right)\right) \leq T _ {n}, \forall n,\tag{9b}
$$

$$
\frac {d _ {n} ^ {R}}{c} + \exp \left(\overline {{\tau_ {n} ^ {R}}}\right) + \frac {\varepsilon_ {n} \lambda_ {n}}{F ^ {R}} \exp \left(\overline {{x _ {n} ^ {R}}} - \overline {{f _ {n} ^ {R}}}\right) \leq T _ {n},
$$

$$
\forall n \in \mathcal {N},\tag{9c}
$$

$$
\frac {d _ {n} ^ {H}}{c} + \exp \left(\overline {{\tau_ {n} ^ {H}}}\right) + \frac {\varepsilon_ {n} \lambda_ {n}}{F ^ {H}} \exp \left(\overline {{x _ {n} ^ {H}}} - \overline {{f _ {n} ^ {H}}}\right) \leq T _ {n},
$$

$$
\forall n \in \mathcal {N},\tag{9d}
$$

$$
\begin{array}{r l} & b _ {n} ^ {R} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {R} P _ {\max} G _ {n} ^ {R}}{b _ {n} ^ {R} B _ {\max} N _ {0}}\right) \\ & \geq \varepsilon_ {n} \exp \left(\overline {{x _ {n} ^ {R}}} - \overline {{\tau_ {n} ^ {R}}}\right), \\ & \forall n \in \mathcal {N}, \\ & b _ {n} ^ {H} B _ {\max} \log_ {2} \left(1 + \frac {p _ {n} ^ {H} P _ {\max} G _ {n} ^ {H}}{b _ {n} ^ {H} B _ {\max} N _ {0}}\right) \\ & \geq \varepsilon_ {n} \exp \left(\overline {{x _ {n} ^ {H}}} - \overline {{\tau_ {n} ^ {H}}}\right), \\ & \forall n \in \mathcal {N}, \\ & \frac {d _ {n} ^ {R}}{c} + \exp \left(\overline {{\tau_ {n} ^ {R}}}\right) + \frac {\varepsilon_ {n} \lambda_ {n}}{F ^ {R}} \exp \left(\overline {{x _ {n} ^ {R}}} - \overline {{f _ {n} ^ {R}}}\right) \\ & \leq T _ {n} ^ {h a n d o f f}, \end{array}\tag{9e}
$$

(9f)

$$
\forall n \in \mathcal {N},\tag{9g}
$$

$$
\sum_ {n \in \Phi_ {m}} \exp \left(\overline {{f _ {n} ^ {R}}}\right) \leq 1, \forall m \in \mathcal {M},\tag{9h}
$$

$$
\sum_ {n \in \mathcal {N}} \exp \left(\overline {{f _ {n} ^ {H}}}\right) \leq 1,\tag{9i}
$$

$$
\overline {{x _ {n} ^ {R}}}, \overline {{x _ {n} ^ {H}}}, b _ {n} ^ {R}, b _ {n} ^ {H}, p _ {n} ^ {R}, p _ {n} ^ {H}, \overline {{\tau_ {n} ^ {R}}}, \overline {{\tau_ {n} ^ {H}}}, \overline {{f _ {n} ^ {R}}}, \overline {{f _ {n} ^ {H}}} > 0,\tag{9j}
$$

$$
(6 c), (6 d).\tag{9k}
$$

Proposition 1: The resulting sets of constraints (9c)-(9i) are convex.

Proof: In the following, the proofs relevant to constraints (9c), (9d), (9g), (9h), as well as (9i) and (9e)-(9f) are developed separately.

1) The left hand of constraints $( 9 \mathrm { { c } ) , ( 9 \mathrm { { d } ) , ( 9 \mathrm { { g } ) , ( 9 \mathrm { { h } ) } } } }$ , and (9i) are in the form of a summation of positive terms of exponential functions, so these constraints are all convex.

2) Constraints (9e) and (9f) have similar expressions as follows:

$$
\theta y \mathrm{log} _ {2} (1 + \frac {\eta z}{\theta}) - q \exp (\delta - \omega) \geq 0,\tag{10}
$$

where $\alpha , \beta , \delta ,$ , and $\omega$ represent optimization variables, and $y , z ,$ , and $q$ represent constants. The first term $\begin{array} { r } { e ( \alpha , \beta ) = \alpha y \mathrm { l o g } _ { 2 } ( 1 ^ { - } + \frac { \beta z } { \alpha } ) } \end{array}$ is the perspective form of concave function $\log _ { 2 } ( 1 + \beta z ) \ [ 3 9 ]$ . Accordingly, we can say that $e ( \alpha , \beta )$ is jointly concave in variables α and $\beta .$ . Furthermore, it is easy to prove the second term $- q \exp ( \delta - \omega )$ is jointly concave in variables $\delta$ and ω. Therefore, both the resulting sets of constraints (9e) and (9f) are convex.

According to the proof, the exponential transformation of variables can effectively remove the coupling between variables. However, Problem (9) is still non-convex because of constraint (9b). To deal with this problem, we use the successive convex approximation (SCA) method. SCA is widely used for iteratively approximating an originally non-convex problem by using first-order Taylor expansion, which can transform the original problem into a series of convex versions [40], [41]. In this case, we first define $g _ { n } = 1 - \exp ( \overline { { x _ { n } ^ { R } } } ) - \exp ( \overline { { x _ { n } ^ { H } } } )$ for any $n \in \mathcal N$ . Then, we define $\pmb { \mathcal { A } } ^ { i } = \{ \mathcal { A } _ { n } ^ { i } \vert n \in \mathcal { N } \}$ , wherein $A _ { n } ^ { i } = \{ \hat { x _ { n } ^ { R } } [ i ] , \hat { x _ { n } ^ { H } } [ i ] \}$ is the local point set in the i-th iteration. Recalling that any concave function is globally upper bounded by its first-order Taylor expansion at any given point [42], [43], we can obtain the following inequality:

$$
\begin{array}{r l} & g _ {n} = 1 - \exp (\overline {{x _ {n} ^ {R}}}) - \exp (\overline {{x _ {n} ^ {H}}}) \\ & \quad \leq 1 - \exp \left(\hat {x _ {n} ^ {R}} [ i ]\right) - \exp \left(\hat {x _ {n} ^ {R}} [ i ]\right) \left(\overline {{x _ {n} ^ {R}}} - \hat {x _ {n} ^ {R}} [ i ]\right) \\ & \qquad - \exp \left(\hat {x _ {n} ^ {H}} [ i ]\right) - \exp \left(\hat {x _ {n} ^ {H}} [ i ]\right) \left(\overline {{x _ {n} ^ {H}}} - \hat {x _ {n} ^ {H}} [ i ]\right) = \hat {g _ {n}} [ i ]. \end{array}\tag{11}
$$

By applying the SCA method, the concave term of (9b) is replaced by a series of linear terms with given local points. As a consequence, Problem (9) is transformed into a series of iteratively convex problem, and the i-th convex problem is given by:

$$
\min_{\substack{\mathrm{T},\overline{x^{R}},\overline{x^{H}},\boldsymbol{b}^{R},\boldsymbol{b}^{H},\\ \boldsymbol{p}^{R},\boldsymbol{p}^{H},\overline{\tau^{R}},\overline{\tau^{H}},\overline{\boldsymbol{f}^{R}},\overline{\boldsymbol{f}^{H}}}}\sum_{n}^{N}T_{n}[i]\tag{12a}
$$

$$
\mathrm{s.t.} \frac {\varepsilon_ {n} \lambda_ {n}}{F ^ {L}} \hat {g _ {n}} [ i ] \leq T _ {n} [ i ],\tag{12b}
$$

$$
(6 c), (6 d), (9 c) - (9 j).\tag{12c}
$$

The SCA process is described in Algorithm 1 and its computational complexity is presented here. At each iteration, the computational complexity is determined by solving the convex problem, where the convex problem can be solved by using the interior point method. This method requires $\frac { \dot { \log } \left( \frac { N _ { I } } { u ^ { 0 } \rho } \right) } { \log ( \xi ) }$ number of iterations (Newton steps), where $N _ { I }$ is the number of constraints, u is the initial point used to estimate the accuracy of the interior-point method, $\gamma$ is the stopping criterion, and $\xi$ is the parameter for updating the accuracy of the interior point method [44]. The number of constraints in problem (12) is $2 + M + 4 N$ , where M and N represent the number of RSUs and ICVs in the system, respectively. Therefore, the computational complexity of Algorithm 1 is $\mathcal { O } \left( i _ { \operatorname* { m a x } } \frac { \log \left( \frac { N _ { I } } { u ^ { 0 } \rho } \right) } { \log ( \xi ) } \right)$ , where $i _ { \mathrm { m a x } }$ is the maximum number of iterations required for Algorithm 1 to converge.<sup>4</sup>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 The SCA-Based Method for Solving Problem (9)

1: Initialize precision $\zeta$, $i_{\text{max}}$, $\mathcal{A}^0$, and set $i = 0$.

2: repeat

3: According to the given local point set $\mathcal{A}^i$ and the expression (11), obtain $\hat{\pmb{g}}[i]$.

4: Solve the convex Problem (12) and find the optimal solution set $\Lambda = \{\mathbf{T}^*, \overline{\pmb{x}^R*}, \overline{\pmb{x}^H*}, \pmb{b}^{R*}, \pmb{b}^{H*}, \pmb{p}^{R*}, \pmb{p}^{H*}, \overline{\tau^R*}, \overline{\tau^H*}, \overline{\pmb{f}^R*}, \overline{\pmb{f}^H*}\}$.

5: Record the objective function value of the $i$-th iteration as $\sum_{n}^{N} T_n[i] = \phi^*$, and update $\mathcal{A}^{i+1}$ based on $\hat{\pmb{x}^R}[i+1] = \overline{\pmb{x}^R*}$ and $\hat{\pmb{x}^H}[i+1] = \overline{\pmb{x}^H*}$, then $i = i+1$.

6: until $\phi^*[i] - \phi^*[i+1] \leq \zeta$, or $i &gt; i_{\text{max}}$.
</div>

## IV. MAXIMUM-DELAY MINIMIZATION

In this section, we discuss a new optimization problem that focuses on the individual delay performance of ICVs by optimizing the delay fairness between them. Indeed, in delaysensitive applications, we have to consider individual delay performance by minimizing the maximum-delay value for all ICVs. Assuming the same parameters as the sum-delay minimization problem, the optimization problem can be expressed

as follows:

$$
\min_{\substack{\boldsymbol{x}^{R},\boldsymbol{x}^{H},\boldsymbol{b}^{R},\boldsymbol{b}^{H},\\ \boldsymbol{p}^{R},\boldsymbol{p}^{H},\boldsymbol{f}^{R},\boldsymbol{f}^{H}}} \max_{n\in \mathcal{N}} \quad \max \left\{T_{n}^{L},T_{n}^{R},T_{n}^{H}\right\}\tag{13a}
$$

$$
\mathrm{s.t.} T _ {n} ^ {R} \leq T _ {n} ^ {\text { handoff }}, \forall n \in \mathcal {N},\tag{13b}
$$

$$
\sum_ {n \in \mathcal {N}} b _ {n} ^ {R} + b _ {n} ^ {H} \leq 1,\tag{13c}
$$

$$
p _ {n} ^ {R} + p _ {n} ^ {H} \leq 1, \forall n \in \mathcal {N},\tag{13d}
$$

$$
\sum_ {n \in \Phi_ {m}} f _ {n} ^ {R} \leq 1, \forall m \in \mathcal {M},\tag{13e}
$$

$$
\sum_ {n \in \mathcal {N}} f _ {n} ^ {H} \leq 1,\tag{13f}
$$

$$
x _ {n} ^ {R}, x _ {n} ^ {H}, b _ {n} ^ {R}, b _ {n} ^ {H}, p _ {n} ^ {R}, p _ {n} ^ {H}, f _ {n} ^ {R}, f _ {n} ^ {H} > 0.\tag{13g}
$$

Problem (13) minimizes the maximum-delay value of all ICVs by finding the optimal solution of optimization variables. These variables include the task-splitting ratios of RSUs, i.e., $\mathbf { X } ^ { R } = [ x _ { 1 } ^ { R } , \dots , x _ { N } ^ { R } ]$ , the task-splitting ratios of HAPS, i.e., $\mathbf { X } ^ { H } = [ x _ { 1 } ^ { \mathsf { ^ { H } } } , \dots , x _ { N } ^ { \mathsf { ^ { H } } } ]$ , bandwidth allocations of the links from ICVs to RSUs, i.e., $\mathbf { B } ^ { R } = [ b _ { 1 } ^ { R } , \ldots , b _ { N } ^ { R } ]$ , bandwidth allocations of the links from ICVs to HAPS, i.e., $\mathbf { B } ^ { H } = [ b _ { 1 } ^ { H } , \ldots , b _ { N } ^ { H } ]$ power allocations of the links from ICVs to RSUs, i.e., $\mathbf { \dot { P } } ^ { R } = [ p _ { 1 } ^ { R } , \dots , p _ { N } ^ { R } ]$ , power allocations of the links from ICVs to HAPS, i.e., $\mathring { \mathbf { P } } ^ { H } = [ p _ { 1 } ^ { H } , \dotsc , p _ { N } ^ { H } ]$ , computing resource allocations of RSUs, i.e., $\mathbf { F } ^ { \tilde { R } } = [ f _ { 1 } ^ { R } , \ldots , f _ { N } ^ { R } ]$ , and computing resource allocations of HAPS, i.e., $\mathbf { F } ^ { \tilde { H } } = [ f _ { 1 } ^ { H } , \dots , \bar { f } _ { N } ^ { H } ]$ In addition, the constraint (13b) indicates that the delay for computing task on the RSU cannot exceed the network handoff time. Similar to the sum delay minimization problem, constraints (13c)-(13g) represent the basic constraints, including bandwidth capacity, power threshold, RSU and HAPS computational capabilities, and the non-negative conditions of variables, respectively. Problem (13) is clearly a non-convex problem. In order to solve it, similar to the solution of Problem (6), we adopt the following transformation and solution process: First, we introduce auxiliary variables $\mathrm { T } = [ T _ { 1 } , \dots , T _ { N } ]$ to transform the original objective function as: min $\operatorname* { m a x } _ { n \in \mathcal { N } } T _ { n } .$ Then, we further introduce variable $\mathbb { T }$ to replace $\operatorname* { m a x } _ { n \in \mathcal { N } } \ T _ { n } .$ Next, in order to deal with the coupling between optimization variables, the auxiliary variables $\bar { \tau } _ { n } ^ { R }$ and $\tau _ { n } ^ { H }$ are introduced for ICV $n \in \mathcal N$ to represent the delays for offloading data to the RSU and HAPS, respectively, and the corresponding delay constraints for these newly introduced variables are added. After that, we apply the exponential transformation for the variables $x _ { n } ^ { R } , x _ { n } ^ { H } , \hat { \tau _ { n } ^ { R } } , \hat { \tau _ { n } ^ { H } } , f _ { n } ^ { R }$ and $f _ { n } ^ { H }$ . In the transformed optimization problem, the constraint for the local delay will be $\begin{array} { r } { \frac { \varepsilon _ { n } \lambda _ { n } } { F ^ { L } } \left( 1 - \exp \left( \overline { { x _ { n } ^ { R } } } \right) - \exp \left( \overline { { x _ { n } ^ { H } } } \right) \right) \leq T _ { n } } \end{array}$ , where the left term is a concave function. Therefore, the resulting set from this constraint is non-convex. To address this issue, we use the SCA method proposed in Algorithm 1 to transform the original optimization problem into a series of convex sub-problems, and we obtain the final result through the corresponding iterations.

## V. SIMULATION RESULTS

For our simulation, we consider a one-way road covered by two RSUs and one HAPS. The HAPS is deployed in the stratosphere at an altitude of 20 km and located horizontally in the center of the road. All ICVs can communicate with the HAPS instantly and offload their data to the HAPS’s server for data processing. Two RSUs were deployed at positions of 80 m and 240 m, each covering a range of 160 m. The ICVs covered by the RSUs can communicate with the RSUs and offload data to their servers for data processing. When the ICV travels beyond the coverage area of the RSU it is connected to, a network handoff will occur. The ICV will then enter the coverage area of the next RSU, establish communication, and obtain services from it. In this simulation, ten ICVs were initially randomly deployed on the road. At the beginning of each decision time slot, each ICV randomly generated one task to be computed, depending on the individual input data. If not emphasized, the main parameters in this simulation were set as in TABLE II.

TABLE II  
SIMULTATION PARAMETERS

<table><tr><td>Definition</td><td>Value</td></tr><tr><td>Speed of ICV (m/s)</td><td>30</td></tr><tr><td>Bandwidth capacity (MHz)</td><td>20</td></tr><tr><td>Noise power density (dBm/Hz)</td><td>-174</td></tr><tr><td>NLoS Path-loss factor</td><td>3.7</td></tr><tr><td>Rician factor (dB)</td><td>10</td></tr><tr><td>Rayleigh distribution</td><td> $\mathcal{CN}(0,1)$ </td></tr><tr><td>Transmitter power of ICV (dBm)</td><td>23</td></tr><tr><td>Directional antenna gain of HAPS (dBi)</td><td>17 [46]</td></tr><tr><td>Computational density (CPU cycle/bit)</td><td>500, 1,000, 1,500, 2,000, or 2,500</td></tr><tr><td>Volume of input data (Kbits)</td><td>100, 300, 500, 700, or 900</td></tr><tr><td>Computational capability of ICV, RSU, HAPS (CPU cycle/s)</td><td>2 G, 32 G, 100 G</td></tr><tr><td>Maximum iteration</td><td>50</td></tr><tr><td>Convergence precision</td><td> $10^{-6}$ </td></tr></table>

![](images/ab71eb8392daa42634ab1a154406465505652df2f0badd1fa867ab6503ca31a8.jpg)  
Fig. 4. The convergence of the SCA method with the proposed scheme.

Fig. 4 shows the convergence performance of Algorithm 1 in solving the sum-delay minimization problem (labeled as ‘Sum’) and the maximum-delay minimization problem (labeled as ‘Max.’) in our proposed scheme, where the delay performance of the ‘Sum’ problem is measured by the average delay of all ICVs, and the ‘Max.’ problem is measured by the maximum-delay value of all ICVs. As we can see, the performance of both delays converge to stable points within ten iterations, thus confirming the convergence and efficiency of the SCA method.

![](images/f74252663bd90e55dd649900546ad98a2791d5a67afb3799a177a756dbe4c257.jpg)

(a) Average delay  
![](images/e27553a4edfaa3bf13da949bc59115faaa4fe594793018648f8e8608cebb38f9.jpg)

(b) Maximum delay  
![](images/ecc97038f74f8d543e5062cf20020e928f3b06f844d45cf6630f92dbb1f629b8.jpg)  
(c) Fairness

Fig. 5. Average delay, maximum delay, and fairness of the proposed scheme.  
![](images/90cf690b680c58e379715e645fa8c9368dd47b7c1e5769096bc37c32c97c477e.jpg)  
Fig. 6. Average delay vs. bandwidth.

Fig. 5 (a), (b), and (c) respectively show the ICVs’ average delay, maximum delay, and fairness index of the proposed scheme under the premise of solving the ‘Sum’ problem and the ‘Max.’ problem in five consecutive time slots. In this work, the fairness is measured by the widely used Jain’s equation, defined by $\textstyle { \mathcal { T } } = ( \sum _ { n = 1 } ^ { N } y _ { n } ) ^ { 2 } / ( N \times \sum _ { n = 1 } ^ { N } y _ { n } ^ { 2 } )$ . As we can see, the average delay of the ‘Sum’ problem is better than that of the ‘Max.’ problem, but its maximum delay value is worse. Under the ‘Max.’ problem, the ICVs can obtain higher fairness values. This is because the goal of the ‘Sum’ problem is to optimize the average delay performance of the ICVs, while the purpose of the ‘Max.’ problem is to optimize the maximum delay of the ICVs.

Fig. 6 – Fig. 9 show the effects of bandwidth capacity, ICV’s transmit power threshold, HAPS computational capability, and RSU computational capability settings on the average delay performance of different schemes when solving the ‘Sum’ and ‘Max.’ problems. To distinguish these schemes, we use the label ‘HRVIN’ to represent the proposed scheme within the distributed computing framework of the HAPS-RSU-vehicle integrated network, where the task of each ICV can be processed at its onboard device, RSU server and HAPS server in parallel. We use the label ‘woRSU’ to represent the twolayer computing scheme where there is no RSU computing, and we use the label ‘woHAPS’ to represent the two-layer computing scheme where there is no HAPS computing, which can also be regarded as a traditional distributed computing scheme.

![](images/49b3bed96421a9c7ddd2fbd3fcf447cc5d0348bdd92b09090570e0d4b136a644.jpg)  
Fig. 7. Average delay vs. transmit power of ICV.

![](images/06b053c01725a31f33c36494080d15822f4127ddbd16c48935fb4e082d80594d.jpg)  
Fig. 8. Average delay vs. computational capability of HAPS.

Fig. 6 shows the impact of different bandwidth capacity settings on delay performance. As we can see, the ‘HRVIN’ scheme with three layers of computing resources achieves better performance compared to the other two baseline schemes, which have only two layers of computing resources. This shows that the ‘HRVIN’ scheme is more conducive to accelerating the task computing. Besides, by comparing the ‘woRSU’ and ‘woHAPS’ schemes, we can see that only the HAPSassisted computing scheme ‘woRSU’ can also effectively improve the delay performance greater than the ‘woHAPS’ scheme, and this is because the HAPS can be equipped with more computing resources than the RSU. Moreover, the increase of bandwidth capacity can reduce the delay of computing tasks. The reason for this is that the increase of bandwidth enables ICVs to improve their ability to offload data to the RSUs and HAPS. Benefiting from this, more data can be offloaded to speed up the data processing, thereby improving the ICVs’ perceived delays.

![](images/d2cfe766aeff8346feee97b9cbdb6970593884a7f698cc61e5d6245030a7657a.jpg)  
Fig. 9. Average delay vs. computational capability of RSU.

Fig. 7 shows the impact of different transmit power threshold settings on delay performance. As we can see, increasing the power threshold can reduce the delay. Similar to the change of bandwidth capacity, the increase in power threshold improves the ICV’s ability to offload data. This allows ICVs to offload more data for processing, thus improving the delay performance.

Fig. 8 shows the impact of different computational capability settings of the HAPS server on the delay performance. We can observe that with the increase of the computational capability, the delay can be gradually reduced. This suggests that the increase in the computational capability of the HAPS server can help ICVs to offload more data to the HAPS to obtain more powerful computing resources, thus accelerating the data processing.

Fig. 9 shows the impact of different computational capability settings of the RSU server on the delay performance. On the whole, the increase in the server’s computational capability can speed up the execution of tasks.

As mentioned above, network handoffs between ICVs and RSUs will negatively affect computation offloading, and this problem will be more severe for high-speed mobile scenarios. To illustrate the impact of a network handoff and mobility on computing, Fig. 10 (a) and (b) show the total failed workloads of ICVs under different speed settings when removing network handoff constraint $T _ { n } ^ { R } ~ \stackrel { \textstyle = } { \le } ~ T _ { n } ^ { h a n d o \bar { f } f } , \forall n ~ \in ~ \mathcal { N } ,$ , for solving the sum-delay optimization problem, and the maximum-delay optimization problem, respectively. We count the averaged one-minute failed workloads, where the workload is defined as the product of the input data bits ε (bit) and the computational density λ (CPU Cycle/bit). As both figures show, the total failed workloads of ICVs increase as the speed increases on the whole. According to equation $\begin{array} { r } { T _ { n } ^ { h a n d o f f } = \frac { D - | l _ { n } \ m o d \ D | } { v } . } \end{array}$ the handoff time is inversely proportional to the speed of the ICV. This means that with the increase of speed, the time to trigger the network handoff will be earlier, so the frequency of handoffs occurring during the driving will also increase, and the cumulative failed workloads will increase. Fig. 10 shows that considering the network handoff factor when designing a computing strategy can effectively avoid failures caused by handoff interruptions. Obviously, this is of great significance for efficient and successful data processing, especially for high-speed mobile scenarios. In addition, by comparing the ‘woHAPS’ and ‘HRVIN’ schemes, we can see that the failed workloads of the ‘woHAPS’ scheme are higher than that of ‘HRVIN’ scheme. The reason is that when we do not consider the handoff factor, most of the ICVs in the ‘woHAPS’ scheme mainly rely on RSU computing, so the failed workloads caused by handoffs exceed the ‘HRVIN’ scheme that can depend on both RSU computing and HAPS computing. Although considering network handoffs in the ‘woHAPS’ scheme (i.e., adding the handoff constraint at RSUs) can avoid computational interruptions, it will force ICVs that encounter handoffs to rely only on their own local computing, thus resulting in poor delay performance. This fact will be verified in Fig. 11. In comparison, the ‘HRVIN’ scheme that does not consider the network handoff factor reduces the computational burden on the RSU server to a certain extent. Therefore, when encountering a handoff, the interrupted workloads are fewer. Further, if the handoff factor can be considered in the ‘HRVIN’ scheme when encountering a handoff, a large amount of data can be offloaded to the HAPS, which can yield a lower delay compared with the ‘woHAPS’ scheme that can only rely on local computing, and in summary, the negative impact of network handoffs on computing is avoided. Additionally, HAPS computing can help to improve the efficiency of task computing significantly while avoiding the adverse effects of network handoffs.

![](images/9a9b483a62b53a5ce5de1ba8e432380c2e0aa20d96d4cc1673aee9bfbac90073.jpg)  
(a) Sum-delay optimization

![](images/11cd9c4281414cb01a1466bf43f1b41dc8579f24a1f56aeaa303090bdebb36e6.jpg)  
(b) Maximum-delay optimization  
Fig. 10. The total failed workloads caused by a handoff vs. speed of ICV.

![](images/73f185c9c280daa6edfea7ad4b7e350c52afcf81e58579b6408e7ac4d50baeed.jpg)  
(a) Sum-delay optimization

![](images/5ca1c2ffeb70936c0db94a5a1a64976a4bb3fbe38118ae9211af1846dd008946.jpg)  
(b) Maximum-delay optimization  
Fig. 11. The effect of handoffs on delay performance.

Fig. 11 shows the average delays of two cases, one where no handoff occurs and one where the handoff does occur, indicated by ‘NoHandoff’ and ‘Handoff’, respectively. In both sub-figures, we compare the delay performance of the ‘woHAPS’ and ‘HRVIN’ schemes to illustrate the importance of HAPS computing to the handoff case. As we can see, in each sub-figure, the edge computing scheme ‘woHAPS has a delay increase of nearly 150 ms in the ‘Handoff’ case compared to the ‘NoHandoff’ case, while the delay increase of the ‘HRVIN’ scheme is only less than 10 ms. This is because, in order to avoid a computation interruption caused by a network handoff, the ICV in the ‘woHAPS’ scheme can only offload a small amount of data to the edge, leaving most of the data to be computed locally, thus resulting in a significant increase in delay. However, in the ‘HRVIN’ scheme, the ICV can send the data that the RSU cannot handle to the HAPS, so the delay increase is slight and acceptable. From the above comparison, we can see that the delay performance of traditional edge computing in the handoff case will suddenly deteriorate, which is obviously not conducive to the stability and safety of ICV driving. By contrast, a HAPS can resolve the negative impact of network handoff by completing task computing within an acceptable increase in delay. Therefore, introducing HAPS computing can help ICVs cope with the network handoffs.

Fig. 12 shows the averaged ratio of a task performed in three computing nodes: local, RSU, and HAPS with different bandwidth settings for the proposed scheme. Fig. 12 (a) and (b) show the comparison of data splitting in the two situations of ‘NoHandoff’ and ‘Handoff’ with the premise of solving the sum-delay optimization problem. Fig. 12 (c) and (d) reflect the above situations of solving the maximum-delay optimization problem. As we can observe in the ‘NoHandoff’ case in subfigures (a) and (b), when the bandwidth is 5 MHz, the data is mostly processed locally or on the HAPS server. This is because the small bandwidth limits the ability of ICVs to

![](images/e44d1cb4990fa9f163bffc613f5ade4ea4be19aaf52ed1f318840d8f81095708.jpg)

![](images/2dfd3328e9e68de6cac2dda898b19ac7fa821367167890d9cfdb30b606bc3a5b.jpg)  
(a) Sum-delay optimization

![](images/a8c67fee544211397007a42184979d4a62f19d6b08c79285072a4b101d877b22.jpg)

![](images/c8479caf26b83f3c077c262b3df3c313e9412fbe411cebabb2ebc1d388341331.jpg)  
(b) Maximum-delay optimization

Fig. 12. The data splitting ratio for the NoHandoff and Handoff cases vs. bandwidth.  
![](images/8aba81cb54638f3c479a2bdc512b6eca81bd33c3874bf74c0f12a69e940a4ce7.jpg)

![](images/2602993591555a3ec0fe721e78a860cf2ae8ad24dc940e6b52a33b49dc0c159e.jpg)  
(a) Sum-delay optimization

![](images/789f7ed1a0b00311db904afb6fcbd1f206b1faf746ae87ea8c1f76701d74c6a0.jpg)

![](images/c35dab0c71de28c723179e2ee173810713585df56f162babf7928526d2ffb868.jpg)  
(b) Maximum-delay optimization  
Fig. 13. The data splitting ratio for the NoHandoff and Handoff cases vs. computational capability of the HAPS server.

offload data. Consequently, the data tends to be directly processed by the ICV’s onboard device, or offloaded to the HAPS that has more computing resources. As the bandwidth capacity increases to 15 MHz, the throughput of offloading data to the RSUs and HAPS significantly improves, effectively reducing the corresponding communication delay, so the splitting ratio of local computing decreases, and the splitting ratios of RSU computing and HAPS computing increase. In addition, when we compare the ‘NoHandoff’ and ‘Handoff’ cases, we can observe that the splitting ratio of RSU computing significantly drops from 25%-35% to 3%. This is because the data offloaded to the RSUs needs to be successfully processed before the network handoff is triggered. Hence, in the ‘Handoff’ case, the data splitting ratio of the RSU is small. Meanwhile, the splitting ratio of the HAPS increases significantly from 38%- 46% to 62%-78%, indicating that most of the RSU’s workload has migrated to the HAPS to avoid computation interruptions. This tells us that HAPS computing plays an important role when the handoff occurs.

Similarly, Fig. 13 shows the averaged ratio of a task performed in three computing nodes: local, RSU, and HAPS under different computational capability settings of the HAPS for the proposed scheme. As we can observe in the ‘NoHandoff’ case in sub-figures (a) and (c), RSU computing plays a crucial role when the computational capability of the HAPS is set to 50 G CPU Cycle/s. This is because the computational capacity of the HAPS is smaller than the total capabilities of the two RSUs (each with 32 G CPU Cycle/s) in the system. When the computing capacity of the HAPS server increases to 100 G CPU Cycle/s, it is clear that HAPS computing plays a significant role. In addition, by comparing the ‘NoHandoff and ‘Handoff’ cases, we can ascertain that the HAPS takes on the majority of the workloads when the handoff occurs (i.e., about 70%-80%), while the RSU computing only handles a fraction of the workload. By looking at Fig. 12 and Fig. 13 together, we can draw two conclusions: First, in the ‘Handoff case, most of the data has migrated from the RSU to the HAPS, so the HAPS can play a crucial role in this case, which confirms that HAPS computing in this distributed framework can effectively deal with network handoffs. Second, according to the data splitting ratios, the proposed distributed computing scheme can indeed achieve more flexible and adaptive task scheduling.

## VI. CONCLUSION

In this work, we proposed a distributed parallel computing scheme with the assistance of HAPS to achieve a lower delay performance of vehicular computing tasks and at the same time provide a smooth and stable service experience for vehicles by avoiding the negative impact of handoff. As we saw, the scheme flexibly divides data into three parts and processes it in parallel on ICVs, RSUs, and a HAPS. By setting the task portion that is computed at the RSU to be completed before the network handoff, the scheme effectively eliminates the negative impact of the handoff on the computation. On this basis, this work formulated a total delay optimization problem and solved it using the SCA method. Then, we also discussed the formulation and solution of the maximum-delay optimization problem. Finally, extensive simulation results confirmed the effectiveness of our proposed scheme.

The energy consumption issue for HAPS network is critical because both hovering and computation require energy consumption. The role of HAPS in computing will be weakened when considering the energy issue of HAPS, which will make the delay perceived by ICVs longer. In the future work, we will discuss this comprehensive and interesting topic.

## REFERENCES

[1] J. Zhou, D. Tian, Y. Wang, Z. Sheng, X. Duan, and V. C. M. Leung, “Reliability-optimal cooperative communication and computing in connected vehicle systems,” IEEE Trans. Mobile Comput., vol. 19, no. 5, pp. 1216–1232, May 2020.

[2] K. N. Qureshi, S. Din, G. Jeon, and F. Piccialli, “Internet of Vehicles: Key technologies, network model, solutions and challenges with future aspects,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 3, pp. 1777–1786, Mar. 2021.

[3] M. Chen, Z. Yang, W. Saad, C. Yin, H. V. Poor, and S. Cui, “A joint learning and communications framework for federated learning over wireless networks,” IEEE Trans. Wireless Commun., vol. 20, no. 1, pp. 269–283, Oct. 2021.

[4] Z. Ning et al., “When deep reinforcement learning meets 5G-enabled vehicular networks: A distributed offloading framework for traffic big data,” IEEE Trans. Ind. Informat., vol. 16, no. 2, pp. 1352–1361, Feb. 2020.

[5] M. Chen et al., “Distributed learning in wireless networks: Recent progress and future challenges,” IEEE J. Sel. Areas Commun., vol. 39, no. 12, pp. 3579–3605, Dec. 2021.

[6] J. Kang et al., “Communication-efficient and cross-chain empowered federated learning for artificial intelligence of things,” IEEE Trans. Netw. Sci. Eng., vol. 9, no. 5, pp. 2966–2977, Sep. 2022.

[7] Y. Ye, R. Q. Hu, G. Lu, and L. Shi, “Enhance latency-constrained computation in MEC networks using uplink NOMA,” IEEE Trans. Commun., vol. 68, no. 4, pp. 2409–2425, Apr. 2020.

[8] M. Chen, N. Shlezinger, H. V. Poor, and S. Cui, “Communication efficient federated learning,” Proc. Nat. Acad. Sci. USA, vol. 118, Apr. 2021, Art. no. e2024789118.

[9] NTT DATA White Paper. When the Car Takes Over: A Glimpse Into the Future of Autonomous Driving. Accessed: Jun. 10, 2022. [Online]. Available: https://us.nttdata.com/en/-/media/assets/white-paper/mfgautonomous-cars-white-paper.pdf

[10] F. Lyu et al., “Characterizing urban vehicle-to-vehicle communications for reliable safety applications,” IEEE Trans. Intell. Transp. Syst., vol. 21, no. 6, pp. 2586–2602, Jun. 2020.

[11] G. Qiao, S. Leng, K. Zhang, and Y. He, “Collaborative task offloading in vehicular edge multi-access networks,” IEEE Commun. Mag., vol. 56, no. 8, pp. 48–54, Aug. 2018.

[12] W. Shi, H. Zhou, J. Li, W. Xu, N. Zhang, and X. Shen, “Drone assisted vehicular networks: Architecture, challenges and opportunities,” IEEE Netw., vol. 32, no. 3, pp. 130–137, May 2018.

[13] M. LiWang, S. Dai, Z. Gao, X. Du, M. Guizani, and H. Dai, “A computation offloading incentive mechanism with delay and cost constraints under 5G satellite-ground IoV architecture,” IEEE Wireless Commun. Mag., vol. 26, no. 4, pp. 124–132, Aug. 2019.

[14] H. Du, D. Niyato, Y.-A. Xie, Y. Cheng, J. Kang, and D. I. Kim, “Performance analysis and optimization for jammer-aided multiantenna UAV covert communication,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 2962–2979, Oct. 2022.

[15] Z. Jia, M. Sheng, J. Li, and Z. Han, “Toward data collection and transmission in 6G space–air–ground integrated networks: Cooperative HAP and LEO satellite schemes,” IEEE Internet Things J., vol. 9, no. 13, pp. 10516–10528, Jul. 2022.

[16] Z. Jia, Q. Wu, C. Dong, C. Yuen, and Z. Han, “Hierarchical aerial computing for Internet of Things via cooperation of HAPs and UAVs,” IEEE Internet Things J., vol. 10, no. 7, pp. 5676–5688, Apr. 2023.

[17] (2016). Radio Regulations Articles. [Online]. Available: http://www.itu. int/pub/R-REG-RR-2016

[18] Z. Jia, M. Sheng, J. Li, D. Zhou, and Z. Han, “Joint HAP access and LEO satellite backhaul in 6G: Matching game-based approaches,” IEEE J. Sel. Areas Commun., vol. 39, no. 4, pp. 1147–1159, Apr. 2021.

[19] W. Jaafar and H. Yanikomeroglu, “HAPS-ITS: Enabling future ITS services in trans-continental highways,” IEEE Commun. Mag., vol. 60, no. 10, pp. 80–86, Oct. 2022.

[20] The Promise and Challenges of Airborne Wind Energy. Accessed: May 18, 2021. [Online]. Available: https://physicsworld.com/a/ the-promise-and-challenges-of-airborne-wind-energy/

[21] HAPSMobile and APB Reach Basic Agreement to Develop Storage Batteries for HAPS Using all Polymer Battery. Accessed: May 18, 2021. [Online]. Available: https://www.hapsmobile. com/en/news/press/2020/20201224\_01/

[22] G. K. Kurt et al., “A vision and framework for the high altitude platform station (HAPS) networks of the future,” IEEE Commun. Surveys Tuts., vol. 23, no. 2, pp. 729–779, 2nd Quart., 2021.

[23] G. Karabulut Kurt and H. Yanikomeroglu, “Communication, computing, caching, and sensing for next-generation aerial delivery networks: Using a high-altitude platform station as an enabling technology,” IEEE Veh. Technol. Mag., vol. 16, no. 3, pp. 108–117, Sep. 2021.

[24] Q. Ren, O. Abbasi, G. K. Kurt, H. Yanikomeroglu, and J. Chen, “Caching and computation offloading in high altitude platform station (HAPS) assisted intelligent transportation systems,” IEEE Trans. Wireless Commun., vol. 21, no. 11, pp. 9010–9024, Nov. 2022.

[25] S. Yu, X. Gong, Q. Shi, X. Wang, and X. Chen, “EC-SAGINs: Edgecomputing-enhanced space-air-ground-integrated networks for Internet of Vehicles,” IEEE Internet Things J., vol. 9, no. 8, pp. 5742–5754, Apr. 2022.

[26] V. B. Souza, M. H. Pereira, L. H. S. Lelis, and X. Masip-Bruin, “Enhancing resource availability in vehicular fog computing through smart inter-domain handover,” in Proc. IEEE Global Commun. Conf., Dec. 2020, pp. 1–6.

[27] T. M. Ho and K.-K. Nguyen, “Joint server selection, cooperative offloading and handover in multi-access edge computing wireless network: A deep reinforcement learning approach,” IEEE Trans. Mobile Comput., vol. 21, no. 7, pp. 2421–2435, Jul. 2022.

[28] Q. Yuan, J. Li, H. Zhou, T. Lin, G. Luo, and X. Shen, “A joint service migration and mobility optimization approach for vehicular edge computing,” IEEE Trans. Veh. Technol., vol. 69, no. 8, pp. 9041–9052, Aug. 2020.

[29] W. Zhan et al., “Deep-reinforcement-learning-based offloading scheduling for vehicular edge computing,” IEEE Internet Things J., vol. 7, no. 6, pp. 5449–5465, Sep. 2020.

[30] H. Zhang, R. Wang, W. Sun, and H. Zhao, “Mobility management for blockchain-based ultra-dense edge computing: A deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 20, no. 11, pp. 7346–7359, Nov. 2021.

[31] T. Ojima and T. Fujii, “Resource management for mobile edge computing using user mobility prediction,” in Proc. Int. Conf. Inf. Netw. (ICOIN), Jan. 2018, pp. 718–720.

[32] C. W. Lee, L. M. Chen, M. C. Chen, and Y. S. Sun, “A framework of handoffs in wireless overlay networks based on mobile IPv6,” IEEE J. Sel. Areas Commun., vol. 23, no. 11, pp. 2118–2128, Nov. 2005.

[33] M. Liu, Z.-C. Li, and X.-B. Guo, “An efficient handoff decision algorithm for vertical handoff between WWAN and WLAN,” J. Comput. Sci. Technol., vol. 22, no. 1, pp. 114–120, Jan. 2007.

[34] K. Shafiee, A. Attar, and V. Leung, “Optimal distributed vertical handoff strategies in vehicular heterogeneous networks,” IEEE J. Sel. Areas Commun., vol. 29, no. 3, pp. 534–544, Mar. 2011.

[35] A. Ibrahim and A. S. Alfa, “Using Lagrangian relaxation for radio resource allocation in high altitude platforms,” IEEE Trans. Wireless Commun., vol. 14, no. 10, pp. 5823–5835, Oct. 2015.

[36] J. Kang et al., “Personalized saliency in task-oriented semantic communications: Image transmission and performance analysis,” IEEE J. Sel. Areas Commun., vol. 41, no. 1, pp. 186–201, Jan. 2023.

[37] A. Alsharoa and M.-S. Alouini, “Improvement of the global connectivity using integrated satellite-airborne-terrestrial networks with resource optimization,” IEEE Trans. Wireless Commun., vol. 19, no. 8, pp. 5088–5100, Aug. 2020.

[38] S. Karapantazis and F. Pavlidou, “Broadband communications via highaltitude platforms: A survey,” IEEE Commun. Surveys Tuts., vol. 7, no. 1, pp. 2–31, 1st Quart., 2005.

[39] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.

[40] J. Kaleva, A. Tölli, and M. Juntti, “Decentralized sum rate maximization with QoS constraints for interfering broadcast channel via successive convex approximation,” IEEE Trans. Signal Process., vol. 64, no. 11, pp. 2788–2802, Jun. 2016.

[41] A. Liu, V. K. N. Lau, and M.-J. Zhao, “Online successive convex approximation for two-stage stochastic nonconvex optimization,” IEEE Trans. Signal Process., vol. 66, no. 22, pp. 5941–5955, Nov. 2018.

[42] Q. Ren, J. Chen, O. Abbasi, G. K. Kurt, H. Yanikomeroglu, and F. R. Yu, “An application-driven nonorthogonal-multiple-access-enabled computation offloading scheme,” IEEE Internet Things J., vol. 8, no. 3, pp. 1453–1466, Feb. 2021.

[43] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[44] O. Abbasi, H. Yanikomeroglu, A. Ebrahimi, and N. M. Yamchi, “Trajectory design and power allocation for drone-assisted NR-V2X network with dynamic NOMA/OMA,” IEEE Trans. Wireless Commun., vol. 19, no. 11, pp. 7153–7168, Nov. 2020.

[45] F. B. Mismar and B. L. Evans, “Partially blind handovers for mmWave new radio aided by sub-6 GHz LTE signaling,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), May 2018, pp. 1–5.

![](images/ad8207c51ad9739a6e37f0f53aad5c8cf2501efd3d4959d0836359d14493d198.jpg)

Qiqi Ren received the B.Sc. degree from the North University of China in 2016 and the Ph.D. degree from the School of Telecommunications Engineering, Xidian University, Xi’an, China, in June 2022. From November 2019 to October 2021, she was a Visiting Researcher with the Department of Systems and Computer Engineering, Carleton University, Ottawa, ON, Canada. Her research interests include high altitude platform station (HAPS) networks and computation offloading.

![](images/0241c361dfc6c664142d4fdff821ae550ac8f1950f70c4e590f6e03469117793.jpg)

Omid Abbasi (Senior Member, IEEE) received the B.Sc. degree in electrical engineering from the University of Tabriz, Tabriz, Iran, in 2011, and the M.Sc. degree in electrical engineering from the Amirkabir University of Technology (Tehran Polytechnic), Tehran, Iran, in 2015, and the Ph.D. degree in electrical engineering from the Sahand University of Technology, Tabriz, in 2020. From February 2019 to September 2020, he was a Visiting Researcher with the Department of Systems and Computer Engineering, Carleton University, Ottawa,

Canada. Since October 2020, he has been a Post-Doctoral Fellow at Carleton University. His current research interests include high-altitude platform station (HAPS) for 6G. He has actively served as a reviewer for flagship IEEE journals and conferences.

![](images/e69ec716455faab801ed71453b051269be8fa7ad1b6b2833d664d21ec815b935.jpg)

Gunes Karabulut Kurt (Senior Member, IEEE) received the B.S. degree (Hons.) in electronics and electrical engineering from Bogaziçi University,˘ Istanbul, Turkey, in 2000, and the M.A.Sc. and Ph.D. degrees in electrical engineering from the University of Ottawa, ON, Canada, in 2002 and 2006, respectively. From 2000 to 2005, she was a Research Assistant with the CASP Group, University of Ottawa. From 2005 to 2006, she was with TenXc Wireless, Canada. From 2006 to 2008, she was with Edgewater Computer Systems Inc., Canada.

From 2008 to 2010, she was with Turkcell Research and Development Applied Research and Technology, Istanbul. From 2010 to 2021, she was with Istanbul Technical University. She is currently an Associate Professor of electrical engineering with Polytechnique Montre´al, Montreal, QC, Canada. She is also an Adjunct Research Professor at Carleton University. She has received the Turkish Academy of Sciences Outstanding Young Scientist (TÜBA-GEBIP) Award in 2019. She is serving as an Associate Technical Editor for the IEEE Communications Magazine, an Associate Editor for IEEE COMMUNICATION LETTERS and IEEE WIRELESS COMMUNICATIONS LETTERS, and an Area Editor for IEEE TRANSACTIONS ON MACHINE LEARNING IN COMMUNI-CATIONS AND NETWORKING. She is serving as a Secretary for the IEEE Satellite and Space Communications Technical Committee and the Chair for the IEEE Special Interest Group entitled “Satellite Mega-constellations: Communications and Networking.” She is a Distinguished Lecturer of the Vehicular Technology Society Class of 2022. She is a Marie Curie Fellow and a member of the IEEE WCNC Steering Board.

![](images/5ce0524c857586751296b56f66244579c027d8883837537a9e6bdf4b524f0ff5.jpg)

Halim Yanikomeroglu (Fellow, IEEE) received the B.Sc. degree in electrical and electronics engineering from Middle East Technical University, Ankara, Turkey, in 1990, and the M.A.Sc. degree in electrical engineering (now ECE) and the Ph.D. degree in electrical and computer engineering from the Universit of Toronto, Canada, in 1992 and 1998, respectively.

Since 1998, he has been with the Department of Systems and Computer Engineering, Carleton University, Ottawa, Canada, where he is currently a Full Professor. He has given more than 110 invited

seminars, keynotes, panel talks, and tutorials in the last five years. He has supervised or hosted over 150 postgraduate researchers at Carleton University. His extensive collaborative research with industry resulted in 39 granted patents. His research interests cover many aspects of wireless communications and networks, with a special emphasis on non-terrestrial networks (NTN) in the recent years.

Dr. Yanikomeroglu is a fellow of the Engineering Institute of Canada (EIC) and the Canadian Academy of Engineering (CAE). He is also a member of the IEEE ComSoc Governance Council, IEEE ComSoc GIMS, IEEE ComSoc Conference Council, and IEEE PIMRC Steering Committee. He received several awards for his research, teaching, and service, including the IEEE ComSoc Fred W. Ellersick Prize in 2021, the IEEE VTS Stuart Meyer Memorial Award in 2020, and the IEEE ComSoc Wireless Communications TC Recognition Award in 2018. He received the Best Paper Awards from the IEEE Competition on Non-Terrestrial Networks for B5G and 6G in 2022 (Grand Prize), IEEE ICC 2021, and IEEE WISEE 2021 and 2022. He served as the general chair and the technical program chair for several IEEE conferences. He is also serving as the Chair for the Steering Committee of IEEE’s Flagship Wireless Event and the Wireless Communications and Networking Conference (WCNC). He has also served in the editorial boards for various IEEE periodicals. He is a Distinguished Speaker of the IEEE Communications Society and the IEEE Vehicular Technology Society, and an Expert Panelist of the Council of Canadian Academies (CCA|CAC).

![](images/da28a9bc34056b05284911f90f94a5ee9675f2768f2b963500c8df7e95d41241.jpg)

Jian Chen (Member, IEEE) received the B.Sc. degree from Xi’an Jiaotong University, China, in 1989, the M.Sc. degree from the Xi’an Institute of Optics and Precision Mechanics, Chinese Academy of Sciences, China, in 1992, and the Ph.D. degree from Xidian University, China, in 2005. He was a Visiting Scholar with The University of Manchester, U.K., from 2007 to 2008, and a Senior Visiting Scholar with the University of Alberta, Canada, from 2017 to 2018. He is currently a Professor with the State Key Laboratory of Integrated Service

Networks, Xidian University. His research interests include physical layer security, wireless sensor networks, and non-orthogonal multiple access.