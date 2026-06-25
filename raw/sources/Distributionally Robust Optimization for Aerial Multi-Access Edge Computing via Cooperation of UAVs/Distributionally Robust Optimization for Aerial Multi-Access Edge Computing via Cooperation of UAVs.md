# Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs and HAPs

Ziye Jia , Member, IEEE, Can Cui , Chao Dong , Member, IEEE, Qihui Wu , Fellow, IEEE, Zhuang Ling , Member, IEEE, Dusit Niyato , Fellow, IEEE, and Zhu Han , Fellow, IEEE

Abstract—With an extensive increment of computation demands, the aerial multi-access edge computing (MEC), mainly based on uncrewed aerial vehicles (UAVs) and high altitude platforms (HAPs), plays significant roles in future network scenarios. In detail, UAVs can be flexibly deployed, while HAPs are characterized with large capacity and stability. Hence, in this paper, we provide a hierarchical model composed of an HAP and multi-UAVs, to provide aerial MEC services. Moreover, considering the errors of channel state information from unpredictable environmental conditions, we formulate the problem to minimize the total energy cost with the chance constraint, which is a mixed-integer nonlinear problem with uncertain parameters and intractable to solve. To tackle this issue, we optimize the UAV deployment via the weighted K-means algorithm. Then, the chance constraint is reformulated via the distributionally robust optimization (DRO). Furthermore, based on the conditional value-at-risk mechanism, we transform the DRO problem into a mixed-integer second order cone programming, which is further decomposed into two subproblems via the primal decomposition. Moreover, to alleviate the complexity

Received 13 November 2024; revised 13 May 2025; accepted 14 May 2025. Date of publication 19 May 2025; date of current version 3 September 2025. This work was supported in part by Jiangsu Province Frontier Leading Technology Basic Research Project under Grant BK 20222013, in part by National Natural Science Foundation of China under Grant 62301251, in part by the Natural Science Foundation of Jiangsu Province of China under Grant BK20220883, in part by the open research fund of National Mobile Communications Research Laboratory, Southeast University under Grant 2024D04, in part by the Aeronautical Science Foundation of China under Grant 2023Z071052007, in part by the Young Elite Scientists Sponsorship Program by CAST under Grant 2023QNRC001, and in part by NSF under Grant ECCS-2302469, Grant CMMI-2222810, Toyota. Amazon and Japan Science and Technology Agency (JST) Adopting Sustainable Partnerships for Innovative Research Ecosystem (ASPIRE) JPMJAP2326. Recommended for acceptance by A. Garcia-Saavedra. (Corresponding authors: Can Cui; Chao Dong.)

Ziye Jia is with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China, and also with National Mobile Communications Research Laboratory, Southeast University, Nanjing 211111, China (e-mail: jiaziye@nuaa.edu.cn).

Can Cui, Chao Dong, and Qihui Wu are with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China (e-mail: cuican020619@nuaa.edu.cn; dch@nuaa.edu.cn; wuqihui@nuaa.edu.cn).

Zhuang Ling is with the College of Communication Engineering, Jilin University, Changchun 130012, China (e-mail: lingzhuang@jlu.edu.cn).

Dusit Niyato is with the School of Computer Science and Engineering, Nanyang Technological University,, Singapore 639798 (e-mail: dniyato@ ntu.edu.sg).

Zhu Han is with the University of Houston, Houston, TX 77004 USA, and also with the Department of Computer Science and Engineering, Kyung Hee University, Seoul 446-701, South Korea (e-mail: hanzhu22@gmail.com).

This article has supplementary downloadable material available at https://doi.org/10.1109/TMC.2025.3571023, provided by the authors.

Digital Object Identifier 10.1109/TMC.2025.3571023

of the binary subproblem, we design a binary whale optimization algorithm. Finally, we conduct extensive simulations to verify the effectiveness and robustness of the proposed schemes by comparing with baseline mechanisms.

Index Terms—Aerial multi-access edge computing, resource allocation, distributionally robust optimization (DRO), conditional value-at-risk (CVaR), primal decomposition, binary whale optimization (BWOA).

# I. INTRODUCTION

N RECENT years, with the extensive growth of computational intensive tasks, the multi-access edge computing (MEC) technique is raised to provide services for various ground users (GUs) in the sixth generation (6G) communication networks [1], [2], [3], [4]. However, as for the GUs in remote areas such as deserts and oceans, it lacks ground infrastructures to provide communication coverage and MEC services [5], [6]. As forecasted that the global uncrewedaerial vehicles (UAVs) market is expected to reach the worth of \$55.8 billion by 2030, UAVs show the colossal potential in the applications of future industries [7]. The non-terrestrial networks can provide ubiquitous coverage for the remote GUs, in which UAVs can be flexibly and quickly deployed on demand with low cost [8], [9], [10], [11], [12], [13]. However, UAVs are limited by the load capacity of computing module, battery, etc. Alternatively, the high altitude platform (HAP), suspending above 20 km at a quasi-static position, and equipped with stronger computing resources and sufficient energy, can compensate for the resource-limited UAVs [14], [15]. Besides, compared with HAPs, UAVs are relatively flexible and can be rapidly deployed to meet the sudden surge in data requests. Therefore, in the context of 6G networks, the cooperation of UAVs and HAPs can provide flexible and stable aerial MEC for GUs in diverse applications to reduce latency and improve the quality of service (QoS).

Unfortunately, in the aerial MEC network, the tasks generated from GUs may be heterogeneous with different QoS demands such as the tolerated delay. Besides, the resources of aerial MEC networks, such as communication, computing, and energy are limited, in which the energy supply is the basic for all operations [16]. Hence, how to guarantee the QoS of GUs and take full advantage of aerial resources is a key issue for ubiquitous communication and computation services in the 6G networks [17], [18]. Furthermore, considering the unpredictable environmental fluctuations, the communication link from the GU to UAV (G2U) is highly dynamic, and the channel state information (CSI) is imperfect, which may cause errors and mismatches between the realistic situation and ideal circumstance [19]. Such errors bring more challenges for the resource allocation scheme in the aerial MEC. Besides, how to cooperate UAVs and HAPs for efficient data offloading and resource optimization is also challenging.

To deal with the above challenges, in this paper, we propose an aerial MEC framework composed of UAVs and an HAP to cooperatively serve the GUs in remote areas, with the consideration of imperfect transmission CSI. In detail, an uncertainty set is constructed to capture the potential random parameters and a chance constraint for task latency with CSI estimation errors is formulated. Then, considering multi-resource constraints for UAVs and the HAP, we formulate the problem to minimize the total energy consumption, with regard to UAV positions, GU-UAV connection decisions, offloading strategies and resource allocation. Since the problem is in the form of mixed integer non-linear programming (MINLP) and NP-hard to solve [20], we first cluster the GUs and deploy UAVs at appropriate positions via proposing the weighted K-means deployment (WKD) based algorithm with a low time complexity. Taking into account the different characteristics of tasks, the weighted distance metric is applied so that the importance of different tasks is incorporated. Then, we reformulate the chance constraint without distribution information into a mixed integer second order cone programming (MISOCP) form by employing the distributionally robust optimization (DRO) and conditional value-at-risk (CVaR) mechanism. To reduce the complexity, via the primal decomposition, we further decompose the MISOCP problem into two subproblems with respect to the offloading decisions and computing resource allocation, respectively. The problem concerning resource allocation is solved by a standard convex toolkit. Moreover, to tackle the integer programming problem related to the offloading decision, we design a metaheuristic algorithm termed as binary whale optimization algorithm (BWOA).

The main contributions of this work are summarized as follows.

We propose a hierarchical aerial MEC model composed of an HAP and multi-UAVs to provide services for remote GUs, in which UAVs can be deployed flexibly and the HAP provides stable and strong computing services. Besides, the CSI estimation error is modeled by an uncertainty set based on the historical statistical information and the time latency requirement is formulated as a chance constraint.   
- To handle the problem of multi-UAV deployment, a WKD based algorithm is designed. Then, by the DRO and CVaR based mechanism, the chance constraint is reformulated into an MISOCP form.   
To tackle the reformulated mixed integer programming (MIP) problem with the MISOCP constraint, by leveraging the primal decomposition, it is decomposed into two subproblems. The subproblem on the resource allocation is convex and solved via CVX. To further reduce the

complexity of the binary offloading subproblem, we design the BWOA.

Extensive simulations are conducted to evaluate the proposed algorithms under various circumstances. The robustness of the designed algorithms with CSI estimation errors is verified. Moreover, by comparing with other baseline algorithms, the effectiveness and low-complexity of the proposed algorithms are verified.

The rest of this paper is arranged as follows. Related works are presented in Section II. Section III proposes the system model and problem formulation. Algorithms are designed in Section IV. Simulations and numerical results are provided in Section V. Finally, we draw conclusions in Section VI.

# II. RELATED WORKS

As for the UAV-based MEC, there exist abundant recent researches. For instance, [21] proposed a collaborative MEC frame and exploited a deep reinforcement learning method to jointly optimize resource allocation, UAV trajectory, and task scheduling. [22] discussed a multi-UAV-enabled MEC system and solved the decoupled two subproblems via alternating optimization and successive convex approximation mechanisms. Considering the competitive relationship among UAVs, [23] formulated a joint optimization problem for the multi-dimensional resource constrained UAV-MEC network and put forward a triple learner based approach. While these studies made significant progresses in the resource and trajectory optimization, improved frameworks are still worth considering. In [24], the authors designed a three-stage alternating algorithm to address issues concerning energy consumption in the UAV-related MEC system. In [25], a deep reinforcement learning approach was devised to minimize the computation cost in the multi-UAV based MEC system. [26] investigated a multi-objective optimization problem in the MEC network to minimize the delay and energy consumption as well as maximize the number of collected tasks of UAVs. In [27], a hierarchical UAV-assisted MEC framework was studied to minimize the sum of latency and energy consumption, in which a method by jointly combining deep reinforcement learning and convex optimization was designed. [28] presented a two-layer optimization framework to reduce the energy consumption for the UAV-based MEC. The authors in [29] designed a two-layer optimization approach and tackled the 0-1 integer programming problem by a greedy algorithm, in which by jointly optimizing task scheduling and UAV locations, the energy consumption in the MEC system was minimized. [30] designed a robust multi-agent approximation strategy to address the uncertainties of CSI and task complexity, which was solved by the multi-agent deep reinforcement learning. However, limited by their battery capacities, the applications of UAVs are restricted in terms of the large-scale service provision for delay sensitivity and computation intensive tasks.

Although the above researches have made great progresses in the resource and trajectory optimization, UAVs are limited by their battery capacities and have shortcomings in providing better services for delay sensitive and computationally intensive tasks. Different from UAVs with constrained capabilities, HAPs can provide strong payloads and stable coverage, which contributes to completing intensive MEC services. In recent years, some works begin to explore the applications of HAPs based MEC services. For example, [31] jointly deployed multi-UAVs and an HAP to provide connectivity and computing service for GUs. [32] focused on data offloading in the UAV-HAP MEC system and developed a matching-based algorithm to maximize the total processed data. In [33], a multi-dimensional resource allocation problem in the UAV-HAP system was designed to minimize the average age of information in response to the uncertain errors of CSI, and a learning-based algorithm was presented to tackle this non-convex problem. Due to the limited resources of the aerial MEC platforms, more studies focused on the issue to improve the energy consumption and resource utilization. In [34], a resource allocation problem minimizing the energy cost was studied for the UAV-HAP assisted MEC, and solved by the distributed online algorithm based on the game theory. The authors in [35] focused on the energy-efficient trajectory optimization problem in the UAV-HAP based MEC system and designed a modified multi-objective reinforcement learning algorithm. [36] employed the K-means and multi-agent reinforcement learning algorithms for resource utilization in the UAV-HAP assisted MEC system. The authors in [37] investigated a computation offloading problem in the UAV-HAP aerial MEC system, and a markov game was conducted to enhance the energy harvesting performance for UAVs. [38] built a multiobjective Markov decision process model towards the age of information and energy tradeoff problem in which UAVs and HAPs cooperatively provided MEC services for ground devices.

As analyzed above, the cooperation of UAVs and HAPs leverages the advantages of the aerial platforms for better energy efficiency, lower latency, and higher capability. Nevertheless, in these studies, the CSI errors are mostly ignored or following a specific distribution, which is impractical due to the various interferences caused by actual environment. The inability to estimate accurate CSI in the practical scenarios brings more challenges for efficient resource allocations. Therefore, it is essential to exploit robust algorithms to deal with the unpredictable fluctuation from the environment. Based on above considerations, in this paper, we focus on the cooperation of UAVs and the HAP to provide robust aerial MEC services for GUs, with the consideration of the imperfect CSI by the uncertainty set.

# III. SYSTEM MODEL AND PROBLEM FORMULATION

In this section, a two-layer aerial MEC model is proposed in Section III-A. Then, the communication model and offloading model are proposed in Sections III-B and III-C, respectively. The problem formulation is detailed in Section III-D.

# A. Aerial MEC Model

As shown in Fig. 1, a hierarchical aerial MEC system is proposed. M GUs indicated by the set $\mathcal { M } = \{ 1 , 2 , \dots , M \}$ , $m \in \mathcal { M }$ = 1 2, are randomly distributed within the remote areas. N UAVs equipped with edge servers, the set of which is denoted by $\mathcal { N } = \{ 1 , 2 , \ldots , N \} , n \in \mathcal { N } .$ , are deployed to provide MEC ser-= 1 2vices. An HAP, denoted by h, hovers at a fixed position and acts as the supplement for the resource-limited UAVs. The Cartesian coordinate is utilized to represent the locations. $\mathbf { w } _ { m }$ denotes the location of GU m, where $\mathbf { w } _ { m } = ( x _ { m } , y _ { m } )$ . All UAVs are = (assumed to hover at the same altitude $z _ { n } ,$ )and the horizontal deployment position of UAV n is denoted by $\boldsymbol { v } _ { n } = ( x _ { n } , y _ { n } )$ . = ( )After deployment, the UAVs hover in the air and are regarded as quasi-stationary. The distance between GU m and UAV n is calculated as:

![](images/0283ed8a3a4b84dd21556d71dc482406e647b3ee17e68069b503d36783fe3731.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Ground users"] --> B["Δg"]
    B --> C["HAP"]
    B --> D["UAV"]
    C --> E["Data transmission link"]
    D --> F["MEC service"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cff,stroke:#333
    style D fill:#ffc,stroke:#333
    style E fill:#cfc,stroke:#333
    style F fill:#fcc,stroke:#333
```
</details>

Fig. 1. Aerial MEC model composed of UAVs and an HAP.

$$
d _ {m, n} = \sqrt {\left(x _ {m} - x _ {n}\right) ^ {2} + \left(y _ {m} - y _ {n}\right) ^ {2} + z _ {n} ^ {2}}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}. \tag {1}
$$

Since UAVs are equipped with limited computing resources, an HAP with strong capabilities is deployed in the upper layer to assist with computing, whose location is denoted by $\varpi _ { h } =$ $\left( x _ { h } , y _ { h } , z _ { h } \right)$ =. Therefore, the distance between UAV n and HAP (h is

$$
d _ {n, h} = \sqrt {(x _ {n} - x _ {h}) ^ {2} + (y _ {n} - y _ {h}) ^ {2} + (z _ {n} - z _ {h}) ^ {2}}, \forall n \in \mathcal {N}. \tag {2}
$$

The task generated from GU m is denoted as $\left( L _ { m } , c _ { m } , T _ { m } ^ { \mathrm { m a x } } \right)$ , where $L _ { m }$ represents the size of task data, $c _ { m }$ ( )indicates the required CPU cycles to process 1 b data and $T _ { m } ^ { \mathrm { m a x } }$ is the maximum tolerable delay of task m. To guarantee the delay limitation, the task needs to be completed within $T _ { m } ^ { \mathrm { m a x } }$ . We consider that the task cannot be divided and the task offloading pattern is the binary mode. Let binary variable $\delta _ { m } ^ { n }$ indicate the connection relationship between GU m and UAV n, i.e.,

$$
\delta_ {m} ^ {n} = \left\{ \begin{array}{l l} 1, & \text { GU   } m \text {   is   connected   with   UAV   } n, \\ 0, & \text { otherwise. } \end{array} \right. \tag {3}
$$

Considering the accessing constraint, each GU can only connect to one UAV, we have

$$
\sum_ {n = 1} ^ {N} \delta_ {m} ^ {n} = 1, \forall m \in \mathcal {M}. \tag {4}
$$

If a UAV is not able to provide sufficient computing resources for the task, or the delay limitation is unable to be satisfied, then the task is forwarded to the HAP for processing. In this case, the UAV performs as a relay. In detail, binary variable $\lambda _ { m } ^ { n }$ is introduced to indicate whether the task collected by UAV n is forwarded to the HAP, i.e.,

$$
\lambda_ {m} ^ {n} = \left\{ \begin{array}{l l} 1, & \text { task   } m \text {   is   forwarded   to   the   HAP   by   UAV   } n, \\ 0, & \text { otherwise. } \end{array} \right. \tag {5}
$$

The HAP is assumed to process at most H tasks simultaneously, and so we have

$$
\sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} \leq H. \tag {6}
$$

# B. Communication Model

1) G2U Channel Model: The G2U channel is a large-scale fading model [39] and can be regarded as a line-of-sight channel. The uplink transmission channel gain under ideal condition of GU m is given as:

$$
\bar {g} _ {m} ^ {u} = \sum_ {n = 1} ^ {N} \frac {\delta_ {m} ^ {n} g _ {0} ^ {u}}{d _ {m , n} ^ {2}}, \forall m \in \mathcal {M}, \tag {7}
$$

where $g _ { 0 } ^ { u }$ is the power gain at the reference distance $d _ { 0 } = 1$ m.

= 1Since the G2U channel is time-varying and vulnerable with the impacts from obstacles, complicated terrains and electromagnetic interferences, the CSI cannot be obtained precisely. In other words, there exist CSI estimation errors between the ideal and realistic environments, due to the inevitable disturbances and interferences from the environment. Accordingly, we denote the actual G2U channel gain as $g _ { m } ^ { u }$ :

$$
g _ {m} ^ {u} = \bar {g} _ {m} ^ {u} + \Delta_ {m}, \forall m \in \mathcal {M}, \tag {8}
$$

where $\Delta _ { m }$ is the unmeasurable CSI estimation error. Clearly, it is difficult to obtain accurate results or probability distributions of the CSI errors in real situations. Therefore, we consider that the moment estimation information can be obtained from the historical statistical data. In particular, the uncertainty set $\mathcal { P }$ is constructed to describe all the possible distributions of the random errors, i.e.,

$$
\mathcal {P} = \left\{\mathbb {P} \in \mathcal {P} \middle | \begin{array}{l} \mathbb {E} _ {\mathbb {P}} (\Delta_ {m}) = \mu_ {m}, \\ \mathbb {D} _ {\mathbb {P}} (\Delta_ {m}) = \sigma_ {m} ^ {2}, \end{array} \right\}, \tag {9}
$$

where $\mu _ { m }$ is the mean of random parameters $\Delta _ { m }$ under distribution P, and $\sigma _ { m } ^ { 2 }$ Δis the corresponding variance. The uncertainty set $\mathcal { P }$ comprises all possible probability distributions of the random CSI estimation error $\Delta _ { m } .$ , i.e., $\mathbb { P } \in \mathcal { P }$ . Besides, to simplify Δthe communication model, we adopt the orthogonal frequency division multiple access (OFDMA) technology. In this way, GUs are enabled to transmit their data simultaneously, and the mutual interference is correspondingly ignored. According to the Shannon formula, the uplink rate of G2U channel is

$$
r _ {m} ^ {u} = B _ {u} \log_ {2} \left(1 + \frac {p _ {u} g _ {m} ^ {u}}{n _ {0} B _ {u}}\right), \forall m \in \mathcal {M}, \tag {10}
$$

where $B _ { u }$ denotes the bandwidth allocated to each task, $p _ { u }$ is the transmitting power of GUs, and $n _ { 0 }$ represents the power spectrum density of additive white noise. Then, the uplink transmission delay of GU m is

$$
t _ {m} ^ {u} = \frac {L _ {m}}{r _ {m} ^ {u}}, \forall m \in \mathcal {M}. \tag {11}
$$

2) U2H Channel Model: Different from the vulnerable G2U link, there are few obstacles or environment reflection disturbances in the UAV-to-HAP (U2H) link. Therefore, characterized with a wider view, we consider that the U2H link is estimated precisely [33]. Moreover, the OFDMA is adopted in the U2H channel to avoid interferences. Consequently, considering the free space loss and rain attenuation, the maximum achievable rate from UAV n to HAP h is [40], [41], [42]

$$
r _ {n} ^ {h} = B _ {h} \log_ {2} \left(1 + \frac {p _ {h} g _ {n} ^ {h} L _ {s} L _ {l}}{k _ {B} T _ {0} B _ {h}}\right), \forall n \in \mathcal {N}, \tag {12}
$$

where $p _ { h }$ and $g _ { n } ^ { h }$ denote the transmission power and antenna power gain between UAV n and HAP $h ,$ respectively. $d _ { n , h }$ is the distance between UAV n and HAP h. Moreover, $L _ { s } =$ $\big ( \frac { v _ { c } } { 4 \pi d _ { n . h } f _ { c } } \big ) ^ { 2 }$ 4πdn,hfc is the free space path loss. $L _ { l }$ =is the total line loss. kB ( )is the Boltzmann’s constant. $T _ { 0 }$ is the system noise temperature. $B _ { h }$ denotes the bandwidth. $f _ { c }$ represents the center frequency. $v _ { c }$ is the speed of light. Therefore, the transmission latency and energy consumption for task m from UAV n to HAP h are calculated as:

$$
t _ {m, n} ^ {h} = \frac {\lambda_ {m} ^ {n} L _ {m}}{r _ {n} ^ {h}}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {13}
$$

and

$$
E _ {m, n} ^ {h} = p _ {h} t _ {m, n} ^ {h}, \forall m \in \mathcal {M}, \forall n \in \mathcal {N}, \tag {14}
$$

respectively. Since the backhaul data is much smaller than uplink data, the backhaul delay is ignored [43].

# C. Computation Model

1) UAV-Based Computation Model: Let $f _ { m }$ represent the CPU frequency allocated to task m. Recall that $L _ { m }$ denotes the data size and $c _ { m }$ is the required number of CPU cycles to compute 1 b data. As a result, the computation latency for processing task m is

$$
t _ {m} ^ {c u} = \frac {c _ {m} L _ {m}}{f _ {m}}, \forall m \in \mathcal {M}. \tag {15}
$$

Based on [44], the energy consumption for handling task m is

$$
E _ {m} ^ {c u} = \sum_ {n = 1} ^ {N} (\delta_ {m} ^ {n} - \lambda_ {m} ^ {n}) \varepsilon_ {n} c _ {m} L _ {m} f _ {m} ^ {2}, \forall m \in \mathcal {M}, \tag {16}
$$

where $\varepsilon _ { n }$ is the effective switched capacitance related to the architecture of MEC servers on UAVs. Note that the CPU frequency of the MEC server is constrained:

$$
\sum_ {m = 1} ^ {M} (\delta_ {m} ^ {n} - \lambda_ {m} ^ {n}) f _ {m} \leq F _ {\max} ^ {n}, \forall n \in \mathcal {N}, \tag {17}
$$

where $F _ { \mathrm { m a x } } ^ { n }$ is denoted as the maximum CPU cycle frequency of the UAV n.

2) HAP-Based Computing Model: Recall that binary variable $\lambda _ { m } ^ { n }$ represents whether task from GU m is computed at the HAP. Then, in the HAP based computation model, the computing delay and energy consumption for handling task m are

$$
t _ {m} ^ {c h} = \frac {c _ {m} L _ {m}}{f _ {m}}, \forall m \in \mathcal {M}, \tag {18}
$$

and

$$
E _ {m} ^ {c h} = \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} \varepsilon_ {h} f _ {m} ^ {2} c _ {m} L _ {m}, \forall m \in \mathcal {M}, \tag {19}
$$

respectively, in which $\varepsilon _ { h }$ is the energy consumption coefficient related to the specific chip structure of an MEC server [45]. Let $F _ { \mathrm { m a x } } ^ { h }$ denote the maximum computational rate of HAP, the CPU frequency constraint for MEC server of the HAP is

$$
\sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} f _ {m} \leq F _ {\max} ^ {h}. \tag {20}
$$

Based on the above discussion, the total delay for computing task m is related to the transmission and computation, i.e.,

$$
\begin{array}{l} t _ {m} ^ {\text { total }} = t _ {m} ^ {u} + \sum_ {n = 1} ^ {N} (\delta_ {m} ^ {n} - \lambda_ {m} ^ {n}) t _ {m} ^ {c u} + \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} t _ {m, n} ^ {h} \\ + \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} t _ {m} ^ {c h}, m \in \mathcal {M}. \tag {21} \\ \end{array}
$$

Moreover, since UAVs are hovering in the air after deployment, the energy consumption for hovering is constant. Therefore, the remaining energy consumption for UAV n is for transmission and computation [27], i.e.,

$$
E _ {n} ^ {\text { total }} = \sum_ {m = 1} ^ {M} E _ {m, n} ^ {h} + \sum_ {m = 1} ^ {M} E _ {m} ^ {c u}, \forall n \in \mathcal {N}. \tag {22}
$$

Besides, since the HAP hovers at the quasi-position, the remaining energy consumption of the HAP is for computation:

$$
E _ {h} ^ {\text { total }} = \sum_ {m = 1} ^ {M} E _ {m} ^ {\text { ch }}. \tag {23}
$$

# D. Problem Formulation

To deal with the potential uncertainties without distribution information, we formulate P0 with the chance constraints to minimize the total energy cost of the aerial MEC platforms, with restrictions of UAV deployment, task offloading, and resource limitation, i.e.,

$$
\mathbf {P 0}: \min _ {\mathbf {v}, \boldsymbol {\delta}, \boldsymbol {\lambda}, \mathbf {f}} \sum_ {n = 1} ^ {N} E _ {n} ^ {\text { total }} + E _ {h} ^ {\text { total }}
$$

$$
\text { s.t. } \quad \operatorname * {P r} \left\{t _ {m} ^ {\text { total }} \leq T _ {m} ^ {\max} \right\} \geq \alpha_ {m}, \forall m \in \mathcal {M}, \tag {24a}
$$

$$
\lambda_ {m} ^ {n} \leq \delta_ {m} ^ {n}, \forall m \in \mathcal {M}, n \in \mathcal {N}, \tag {24b}
$$

$$
E _ {n} ^ {\text { total }} \leq E _ {n} ^ {\max}, \forall n \in \mathcal {N}, \tag {24c}
$$

$$
E _ {h} ^ {\text { total }} \leq E _ {h} ^ {\max}, \tag {24d}
$$

![](images/42cd7958ff29d16313548b9c05f2c86030c13d2013cc49b2e8cd09da06b7fcd4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    P0["P0"] -->|Algorithm 1| UAV[" UAV deployment v, GU-UAV connection δ "]
    UAV --> P1["P1 with the chance constraint"]
    P1 -->|DRO and CVaR based reformulation| P2["P2"]
    P2 -->|Primal decomposition| P3["P3"]
    P2 -->|Penalty| P5["P5"]
    P3 --> Resource_Allocation[" Resource allocation f "]
    P4["P4"] -->|Penalty| P5
    P5 -->|Offloading decision λ| UAV
    Resource Allocation --> P3
    Resource Allocation --> P4
    Resource Allocation --> P5
```
</details>

Fig. 2. Overview of the designed algorithms.

$$
v _ {n} \in \left\{(x _ {n}, y _ {n}) \middle | X ^ {\min} \leq x _ {n} \leq X ^ {\max} \right. \tag {24e}
$$

$$
\left. Y ^ {\min} \leq y _ {n} \leq Y ^ {\max} \right\}, \forall n \in \mathcal {N}, \tag {24f}
$$

$$
\delta_ {m} ^ {n} \in \{0, 1 \}, \forall m \in \mathcal {M}, n \in \mathcal {N}, \tag {24g}
$$

$$
\lambda_ {m} ^ {n} \in \{0, 1 \}, \forall m \in \mathcal {M}, n \in \mathcal {N},
$$

$$
f _ {m} \geq 0, \forall m \in \mathcal {M}, \tag {24h}
$$

$$
(4), (6), (1 7), (2 0),
$$

where in $\mathbf { v } = \{ v _ { n } | \forall n \}$ is the UAV deployment positions, δ $\{ \delta _ { m } ^ { n } | \forall m , \forall n \}$ =represents GU-UAV connection relationships, $\pmb { \lambda } = \{ \lambda _ { m } ^ { n } | \forall m$ , ∀n} denotes the task offloading indicators and $\mathbf { f } = \{ f _ { m } | \forall m \}$ is the resource allocation schemes. With respect to the uncertain CSI estimation errors, (24a) is the chance constraint under the uncertainty set ${ \mathcal { P } } _ { : }$ , which indicates that the total latency for processing task m should not be larger than $T _ { m } ^ { \mathrm { m a x } }$ with a probability of $\alpha _ { m } .$ . Constraint (24b) is the data $\lambda _ { m } ^ { n }$ and $\delta _ { m } ^ { n }$ . Constraints (24c) and (24d) indicate the total energy consumption of UAV and HAP should not be larger than the maximum capacities $E _ { n } ^ { \mathrm { m a x } }$ and $E _ { h } ^ { \mathrm { m a x } }$ , respectively. (24e) is the constraint for the deployment range of UAVs, wherein Xmin, Xmax and Y min, Y max are the horizontal and vertical [ ] [ ]bounds of the area, respectively.

It is observed that P0 is related with the random parameter $\Delta _ { m }$ under uncertainty set $\mathcal { P }$ without distribution information. ΔBesides, P0 is an MINLP concerning binary variables δ and λ, and continuous variables f and v, and the time complexity is exponential with the problem scale growing. Therefore, solving P0 with efficiency is intractable.

# IV. ALGORITHM DESIGN

To tackle P0 efficiently, we divide the process into two phases of UAV deployment and computation offloading. For clarity, the overview of the designed algorithms is illustrated in Fig. 2. As for the UAV deployment, we design a WKD based algorithm in Section IV-A to obtain UAV positions v and GU-UAV connections δ with a low time complexity. Then, based on the determined pre-deployment of UAVs to handle the CSI estimation error, the CVaR-based mechanism is proposed in Section IV-B. Thus, problem P1 with the chance constraint (24a) is conservatively approximated and reformulated into P2 via the DRO and CVaR based mechanism. In Section IV-C, the reformulated problem P2 is dealt with by the primal decomposition. P3 is in the form of SOCP and can be solved via CVX. Furthermore, to effectively obtain the integer offloading strategies of the subproblem P4, it is reformulated into P5, and the BWOA is designed in Section IV-D.

# A. UAV Deployment Optimization

Generally, to reduce the G2U transmission delay, UAVs should be deployed closer to GUs. Moreover, considering the various tasks with different inherent characteristics including data size $L _ { m }$ , computation complexity $c _ { m } .$ , and the maximum tolerable delay $T _ { m } ^ { \mathrm { m a x } }$ , if the UAV is deployed closer to GUs with larger load, the latency is further reduced to better satisfy the QoS. Hence, we design the WKD mechanism to obtain the deployment position v of UAVs and the GU-UAV connections $\delta ,$ which highlights the importance of time-sensitive tasks and provides a more practical and efficient solution for the pre-deployment of UAVs. Since the potential uncertainties have a relatively small impact, they are ignored during the pre-deployment operations. The detailed WKD algorithm is provided in Algorithm 1.

First, we select N points in the area as initial positions for UAVs. Then, the distance between UAVs and GUs is obtained according to (1) and all GUs are accordingly assigned to their nearest clusters (line 4). Then, the center point of each cluster is recalculated and the UAV positions are updated as (line 6):

$$
v _ {n} = \frac {\sum_ {m \in \mathcal {U} _ {n}} \iota_ {m} \mathbf {w} _ {m}}{\sum_ {m \in \mathcal {U} _ {n}} \iota_ {m}}, \forall n \in \mathcal {N}, \tag {25}
$$

here the tained via $\iota _ { m }$ ask fr. Spec $m$ isnd $\begin{array} { r } { \iota _ { m } = \varsigma _ { 1 } L _ { m } + \varsigma _ { 2 } c _ { m } + \frac { 1 - \varsigma _ { 1 } - \varsigma _ { 2 } } { T _ { * * } ^ { \mathrm { m a x } } } } \end{array}$ $\varsigma _ { 1 }$ $\varsigma _ { 2 }$ = + + are weighted variables for a tradeoff among $L _ { m } , c _ { m }$ and $T _ { m } ^ { \mathrm { m a x } } . \mathcal { U } _ { n }$ denotes the set of GUs belonging to cluster n. Then, this process is repeated until the result converges and Imax is denoted as the number of iterations. After v is obtained, GUs are accordingly connected with their corresponding UAVs (line 11). During each iteration, the distances between GUs and UAVs are calculated and the positions of UAVs are updated towards convergence [46]. Moreover, since the time complexity of Algorithm 1 is related to the scale of GU M and UAV N, the corresponding time complexity is $\mathcal { O } ( M N I _ { 1 } ^ { \mathrm { m a x } } )$ . During the ( )clustering process, each user is assigned to a cluster and the UAVs are deployed at the weighted cluster centers. Leveraging the proposed WKD algorithm, which is operated based on the distribution of GUs, we obtain the pre-deployment for N UAVs to cover all the clusters as the initial positions for the subsequent operations.

# B. CVaR-Based Mechanism for Chance Constraint

From Algorithm 1, we obtain the UAV deployment strategy v and the GU-UAV connection δ. Thus, the original problem P0 turns into P1, which is only related with task offloading decision λ and resource allocation f:

Algorithm 1: Weighted K-Means Based Multi-UAV Deployment.   
Input: Locations of GUs $w_{m}$ .
1: Initialization: Set initial v, $\delta_{m}^{n}=0$ , $\forall m\in M$ , $\forall n\in N$ .
2: repeat
3: for $n\in N$ do
4: Calculate the distance $d_{m,n}$ between GU m and UAV n based on (1).
5: Assign GU m to its nearest UAV $n^{*}$ .
6: Update $v_{n}$ based on (25).
7: end for
8: until the result converges.
9: for $n\in N$ do
10: for $m\in U_{n}$ do
11: Connect GU m with UAV n, i.e., $\delta_{m}^{n}=1$ .
12: end for
13: end for
Output: UAV deployment location v and the GU-UAV connection $\delta$ .

$$
\mathbf {P 1}: \min _ {\boldsymbol {\lambda}, \mathbf {f}} \sum_ {n = 1} ^ {N} E _ {n} ^ {t o t a l} + E _ {h} ^ {t o t a l}
$$

$$
\text { s.t. } \quad (2 4 \mathrm{a}) - (2 4 \mathrm{d}), (6), (1 7), (2 0), (2 4 \mathrm{g}), (2 4 \mathrm{h}). \tag {26}
$$

Note that (24a) is the chance constraint, and to deal with it without distribution information and obtain a conservative solution for problem P1, we employ DRO to transform (24a) into a distributionally robust chance constraint (DRCC) with uncertainty set P . In detail, let $^ { i n f } _ { \mathbb { P } \in \mathcal { P } }$ denote the lower bound of possibility for all potential distributions, aiming to seek the solution under the worst case. Then, the chance constraint is reformulated as

$$
\inf _ {\mathbb {P} \in \mathcal {P}} \operatorname * {P r} _ {\mathbb {P}} \left\{t _ {m} ^ {\text { total }} \leq T _ {m} ^ {\max} \right\} \geq \alpha_ {m}, \forall m \in \mathcal {M}, \tag {27}
$$

which is still complicated due to the random parameter $\Delta _ { m }$ under the uncertainty set P.

Accordingly, we leverage CVaR mechanism to obtain a conservative estimation for the resource allocation and offloading strategy, which can efficiently improve the reliability while reducing the energy consumption. Generally, CVaR is an indicator to evaluate the risk quantification. It is defined as the conditional expectation value of loss that exceeds a certain probability level under a given probability distribution [47], [48]. The inherent relationship between the loss function φ ξ for random parameter ξ and CVaR under safety factor α is

$$
\mathbb {P} \left\{\phi (\xi) \leq \mathbb {P} - C V a R _ {\alpha} (\phi (\xi)) \right\} \geq \alpha . \tag {28}
$$

Then, the CVaR constraint in (28) can constitute a conservative approximation for the DRCC, i.e.,

$$
\begin{array}{l} \sup _ {\mathbb {P} \in \mathcal {P}} \mathbb {P} - C V a R _ {\alpha} (\phi (\xi)) \leq 0, \forall \mathbb {P} \in \mathcal {P} \\ \Leftrightarrow \inf _ {\mathbb {P} \in \mathcal {P}} \mathbb {P} \left\{\phi (\xi) \leq 0 \right\} \geq \alpha , \tag {29} \\ \end{array}
$$

where sup is the upper bound under distribution P [49], [50]. P∈P

Moreover, referring [51], we obtain Lemma 1.

Lemma 1: For $\Theta \in \mathbb { R }$ and $\theta ^ { 0 } \in \mathbb { R }$ , if the loss function is $\phi ( \xi ) = \Theta \xi + \theta ^ { 0 }$ , the worst-case CVaR $\mathbf { \Pi } _ { \mathbb { P } \in \mathcal { P } } ^ { s u p } \ : ^ { \mathbb { P } - }$ $C V a R _ { \alpha } ( \phi ( \xi ) )$ can be derived as a second order cone program-(ming, i.e.,

$$
\inf _ {\beta , e, q, z, s} \beta + \frac {1}{1 - \alpha} (e + s),
$$

$$
e - \theta^ {0} + \beta + q - \Theta \mu - z > 0,
$$

$$
e \geq 0, z > 0,
$$

$$
\left\| \begin{array}{c} q \\ \Theta \sigma \\ z - s \end{array} \right\| \leq z + s, \tag {30}
$$

in which $\beta , e , q , z ,$ , and s are auxiliary variables. $\mu$ and σ are the mean and standard deviation of random parameter ξ, respectively.

Proof: The detailed proof is in Appendix A, available online. -

Hence, the DRCC in (27) can be approximated by a conservative and convex programming problem [52]. Specifically, the complete expression for $t _ { m } ^ { t o t a l }$ is

$$
\begin{array}{l} t _ {m} ^ {\text { total }} = \frac {L _ {m}}{B _ {u} \log_ {2} \left(1 + \frac {p _ {u} (\tilde {g} _ {m} ^ {u} + \Delta_ {m})}{n _ {0} B _ {u}}\right)} \\ + \sum_ {n = 1} ^ {N} \frac {\lambda_ {m} ^ {n} L _ {m}}{B _ {h} \log_ {2} \left(1 + \frac {p _ {h} g _ {n} ^ {h} L _ {s} L _ {l}}{k _ {B} T _ {0} B _ {h}}\right)} + \frac {c _ {m} L _ {m}}{f _ {m}}. \tag {31} \\ \end{array}
$$

Since the estimation error $\Delta _ { m }$ is much smaller than the theoret-Δical value of channel gain [53], we adopt the first-order Taylor expansion to approximate the latency $t _ { m } ^ { t o t a l }$ t m ， , i.e.,

$$
t _ {m} ^ {\text { total }} \approx \frac {L _ {m}}{B _ {u} \log_ {2} \left(1 + \frac {p _ {u} \bar {g} _ {m} ^ {u}}{n _ {0} B _ {u}}\right)} + \frac {c _ {m} L _ {m}}{f _ {m}}
$$

$$
+ \sum_ {n = 1} ^ {N} \frac {\lambda_ {m} ^ {n} L _ {m}}{B _ {h} \log_ {2} \left(1 + \frac {p _ {h} g _ {n} ^ {h} L _ {s} L _ {l}}{k _ {B} T _ {0} B _ {h}}\right)}
$$

$$
- \frac {L _ {m} \ln 2}{B _ {u}} \frac {p _ {u} \Delta_ {m}}{\left(n _ {0} B _ {u} + p _ {u} \bar {g} _ {m} ^ {u}\right) \ln^ {2} \left(1 + \frac {p _ {u} \bar {g} _ {m} ^ {u}}{n _ {0} B _ {u}}\right)}. \tag {32}
$$

Consequently, the DRCC in (27) is reformulated into

$$
\inf _ {\mathbb {P} \in \mathcal {P}} \operatorname * {P r} _ {\mathbb {P}} \left\{\Theta_ {m} \Delta_ {m} + \theta_ {m} ^ {0} \leq 0 \right\} \geq \alpha_ {m}, \forall m \in \mathcal {M}, \tag {33}
$$

where

$$
\Theta_ {m} = - \frac {L _ {m} f _ {m} \ln 2}{B _ {u}} \frac {p _ {u}}{\left(n _ {0} B _ {u} + p _ {u} \bar {g} _ {m} ^ {u}\right) \ln^ {2} \left(1 + \frac {p _ {u} \bar {g} _ {m} ^ {u}}{n _ {0} B _ {u}}\right)}, \tag {34}
$$

and

$$
\theta_ {m} ^ {0} = \frac {L _ {m} f _ {m}}{B _ {u} \log_ {2} \left(1 + \frac {p _ {u} \bar {g} _ {m} ^ {u}}{n _ {0} B _ {u}}\right)} + c _ {m} L _ {m}
$$

$$
+ \sum_ {n = 1} ^ {N} \frac {\lambda_ {m} ^ {n} L _ {m} f _ {m}}{B _ {h} \log_ {2} \left(1 + \frac {p _ {h} g _ {n} ^ {h} L _ {s} L _ {l}}{k _ {B} T _ {0} B _ {h}}\right)} - T _ {m} ^ {\max} f _ {m}. \tag {35}
$$

Therefore, according to Lemma 1, the DRCC in (27) with random parameter $\Delta _ { m }$ is reformulated into an MISOCP, i.e.,

$$
\inf _ {\beta_ {m}, e _ {m}, q _ {m}, z _ {m}, s _ {m}} \beta_ {m} + \frac {1}{1 - \alpha_ {m}} \left(e _ {m} + s _ {m}\right) \leq 0,
$$

$$
e _ {m} - \theta_ {m} ^ {0} + \beta_ {m} + q _ {m} - \Theta_ {m} \mu_ {m} - z _ {m} > 0,
$$

$$
e _ {m} \geq 0, z _ {m} > 0,
$$

$$
\left\| \begin{array}{c} q _ {m} \\ \Theta_ {m} \sigma_ {m} \\ z _ {m} - s _ {m} \end{array} \right\| \leq z _ {m} + s _ {m}, \tag {36}
$$

where $\beta _ { m } , e _ { m } , q _ { m } , z _ { m }$ , and $s _ { m }$ are all auxiliary variables. Recall that $\mu _ { m }$ is the mean value of CSI estimation error $\Delta _ { m }$ , and $\sigma _ { m }$ Δis the corresponding standard deviation. Thus, via CVaR, P1 is reformulated as

$$
\mathbf {P 2}: \min _ {\lambda , \mathbf {f}, \beta , \mathbf {e}, \mathbf {q}, \mathbf {z}, \mathbf {s}} \sum_ {n = 1} ^ {N} E _ {n} ^ {t o t a l} + E _ {h} ^ {t o t a l}
$$

$$
\text { s.t. } \quad (2 4 \mathrm{b}) - (2 4 \mathrm{d}), (6), (1 7), (2 0), (2 4 \mathrm{g}), (2 4 \mathrm{h}), (3 6), \tag {37}
$$

with the MISOCP constraint in (36) under the worst-case scenario, and a conservative solution can be obtained to enhance the robustness against the fluctuations. β, e, q, z and s are the corresponding vectors of $\beta _ { m } , e _ { m } , q _ { m } , z _ { m }$ and $s _ { m } .$ , respectively. However, it is still an MIP problem and complicated to deal with both the binary variables and continuous variables.

# C. Primal Decomposition for P2

It is noting that the constraints of problem P2 can be divided into constraints (24c), (24d), (24h), (17), (20), (36) with respect to variable f , β, e, q, z and s, as well as constraints (24b), (24d), (24g), (6), (17), (20), (36) related with the binary offloading strategies λ [54]. Specifically, when λ is fixed, the subproblem P3 related to f , β, e, q, z and s is accordingly obtained:

$$
\mathbf {P 3}: \min _ {\mathbf {f}, \boldsymbol {\beta}, \mathbf {e}, \mathbf {q}, \mathbf {z}, \mathbf {s}} \sum_ {n = 1} ^ {N} E _ {n} ^ {\text { total }} + E _ {h} ^ {\text { total }}
$$

$$
\text { s.t. } \quad (2 4 c), (2 4 d), (2 4 h), (1 7), (2 0), (3 6). \tag {38}
$$

In the form of SOCP, P3 can be solved by a standard convex optimization toolkit such as CVX.

With the value of $\mathbf { f } , \beta , \mathbf { e } , \mathbf { q } ,$ z and s, the offloading decision subproblem P4 is only related with variable λ:

$$
\mathbf {P 4}: \min _ {\lambda} \sum_ {n = 1} ^ {N} E _ {n} ^ {t o t a l} + E _ {h} ^ {t o t a l}
$$

$$
\text { s.t. } \quad (2 4 \mathrm{b}) - (2 4 \mathrm{d}), (2 4 \mathrm{g}), (6), (1 7), (2 0), (3 6). \tag {39}
$$

As a result, P2 can be handled by iteratively solving P3 and P4. However, P4 is still intractable to directly solve due to the binary variables.

TABLE I PARAMETER SETTING 

<table><tr><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td></tr><tr><td> $p_u$ </td><td>0.5W</td><td> $p_h$ </td><td>2W</td></tr><tr><td> $g_0^u$ </td><td>-50dB</td><td> $n_0$ </td><td>-174dBm/Hz</td></tr><tr><td> $B_u$ </td><td>5MHz</td><td> $B_h$ </td><td>5MHz</td></tr><tr><td> $T_0$ </td><td>1000K</td><td> $k_B$ </td><td> $1.38\times 10^{-23}J/K$ </td></tr><tr><td> $f_c$ </td><td>2.4GHz</td><td> $v_c$ </td><td> $3\times 10^8m/s$ </td></tr><tr><td> $L_l$ </td><td>-23dB</td><td> $g_m^h$ </td><td>42dB</td></tr><tr><td> $c_m$ </td><td>300cycles/bit</td><td> $T_m^{max}$ </td><td>20s</td></tr><tr><td>H</td><td>10</td><td> $α_m$ </td><td>95%</td></tr><tr><td> $F_{max}^n$ </td><td> $8\times 10^9Hz$ </td><td> $F_{max}^h$ </td><td> $4\times 10^{11}Hz$ </td></tr><tr><td> $ε_n$ </td><td> $10^{-27}$ </td><td> $ε_h$ </td><td> $10^{-28}$ </td></tr><tr><td> $E_{n}^{max}$ </td><td>200J</td><td> $E_{h}^{max}$ </td><td>20kJ</td></tr><tr><td> $μ_m$ </td><td>0</td><td> $σ_m$ </td><td> $0.1\bar{g}_m^u$ </td></tr><tr><td> $ζ_1$ </td><td>0.4</td><td> $ζ_2$ </td><td>0.2</td></tr></table>

# D. BWOA for P4

As for P4, the exhaustive search can obtain the optimal solutions. However, as the scale of problem increases, it faces exponential complexity. Hence, we design a meta-heuristic BWOA for efficient solutions, in which each searching agent represents a potential solution for the binary problem. However, since the original BWOA is designed for unconstrained optimization problems, the solution provided by the agent may be not feasible. To address this issue, we adopt the penalty mechanism and reformulate the objective function of P4 into $T ( \lambda )$ , which includes ( )both the objective function as well as the penalty value [55]. Specifically, the agents violating constraints are assigned with a higher fitness value under the influence of penalty factors. As such, the constrained problem is effectively transformed without constraints. Based on above discussions, the fitness function related to λ is defined as:

$$
\begin{array}{l} \Gamma (\boldsymbol {\lambda}) = \sum_ {n = 1} ^ {N} E _ {n} ^ {t o t a l} + E _ {h} ^ {t o t a l} \\ + \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \vartheta H _ {m n, 1} (h _ {m n, 1} (\boldsymbol {\lambda})) h _ {m n, 1} ^ {2} (\boldsymbol {\lambda}) \\ + \sum_ {n = 1} ^ {N} \vartheta H _ {n, 2} (h _ {n, 2} (\boldsymbol {\lambda})) h _ {n, 2} ^ {2} (\boldsymbol {\lambda}) + \vartheta H _ {3} (h _ {3} (\boldsymbol {\lambda})) h _ {3} ^ {2} (\boldsymbol {\lambda}) \\ + \sum_ {n = 1} ^ {N} \vartheta H _ {n, 4} (h _ {n, 4} (\boldsymbol {\lambda})) h _ {n, 4} ^ {2} (\boldsymbol {\lambda}) + \vartheta H _ {5} (h _ {5} (\boldsymbol {\lambda})) h _ {5} ^ {2} (\boldsymbol {\lambda}) \\ + \vartheta H _ {6} (h _ {6} (\boldsymbol {\lambda})) h _ {6} ^ {2} (\boldsymbol {\lambda}) + \sum_ {m = 1} ^ {M} \vartheta H _ {m, 7} (h _ {m, 7} (\boldsymbol {\lambda})) h _ {m, 7} ^ {2} (\boldsymbol {\lambda}), \tag {40} \\ \end{array}
$$

where the penalty factor ϑ is set as $1 0 ^ { 5 } . H ( \cdot )$ is an index function. $H ( h ( \lambda ) ) = 0 \mathrm { i f } h ( \lambda ) \leq 0$ 10 (, and otherwise $H ( h ( \lambda ) ) = 1$ . Hence, ( ( )) = 0 ( ) 0 ( ( )) = 1by introducing the penalty factor and index function, the solution which violates the constraints leads to an increasing fitness. The penalty factors act as a role to prevent agents from searching infeasible solutions during their explorations and determine whether the current solution satisfies the corresponding constraints. $h ( \lambda )$ is defined based on the constraints of P4, i.e.,

$$
\left\{ \begin{array}{l} h _ {m n, 1} (\boldsymbol {\lambda}) = \lambda_ {m} ^ {n} - \delta_ {m} ^ {n}, \\ h _ {n, 2} (\boldsymbol {\lambda}) = \sum_ {m = 1} ^ {M} \lambda_ {m} ^ {n} E _ {m} ^ {h} + \sum_ {m = 1} ^ {M} \left(\delta_ {m} ^ {n} - \lambda_ {m} ^ {n}\right) E _ {m} ^ {c u} - E _ {n} ^ {\max}, \\ h _ {3} (\boldsymbol {\lambda}) = \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \lambda_ {m} ^ {n} E _ {m} ^ {c h} - E _ {h} ^ {\max}, \\ h _ {n, 4} (\boldsymbol {\lambda}) = \sum_ {m = 1} ^ {M} \left(\delta_ {m} ^ {n} - \lambda_ {m} ^ {n}\right) f _ {m} - F _ {\max} ^ {n}, \\ h _ {5} (\boldsymbol {\lambda}) = \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} f _ {m} - F _ {\max} ^ {h}, \\ h _ {6} (\boldsymbol {\lambda}) = \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N} \lambda_ {m} ^ {n} - H, \\ h _ {m, 7} (\boldsymbol {\lambda}) = - e _ {m} + \theta_ {m} ^ {0} - \beta_ {m} - q _ {m} + \Theta_ {m} \mu_ {m} + z _ {m}. \end{array} \right. \tag {41}
$$

Consequently, the objective function of BWOA to tackle P4 is further transformed as

$$
\mathbf {P 5}: \min _ {\boldsymbol {\lambda}} \Gamma (\boldsymbol {\lambda})
$$

$\begin{array} { r l } { \mathrm { s . t . } } & { { } ( 2 4 \mathrm { g } ) . } \end{array}$ (42)

Based on the objective function of P5, BWOA is further enhanced to search for quasi-optimal solutions, which is a swarm-based technology in light of hunting behaviors of whales [56], [57]. The positions of agents are updated iteratively based on the social behaviors of whales including exploration and exploitation [58]. The quality of each solution is evaluated by calculating the fitness function $T ( \lambda )$ in (40). The position of each agent $X ( i _ { 2 } )$ ( )during iteration i2 represents a potential ( )solution for λ. Specifically, the procedures of BWOA include encircling prey, spiral updating, and searching for prey, detailed as follows.

1) Encircling Prey: For the agent encircling prey, it might update its current position linearly toward the current optimal solution $\vec { X } ^ { * } ( i _ { 2 } )$ . The position of the agent in the next integration is

$$
\vec {X} (i _ {2} + 1) = \left\{ \begin{array}{l l} \mathbb {C} (\vec {X} (i _ {2})), & \text { if } P _ {B W O A} <   \tau_ {e p}, \\ \vec {X} (i _ {2}), & \text { if } P _ {B W O A} \geq \tau_ {e p}, \end{array} \right. \tag {43}
$$

where $\tau _ { e p }$ is the step size, which is a possibility to determine whether there is a switch (from 0 to 1 or from 1 to 0) between the current bit value and the value in the next iteration. Specifically,

$$
\tau_ {e p} = \frac {1}{1 + \exp (- 1 0 (\vec {A} \cdot \vec {D} - 0 . 5))}, \tag {44}
$$

where

$$
\vec {A} = 2 \vec {a} \cdot \vec {r _ {1}} - \vec {a}, \tag {45}
$$

and

$$
\vec {C} = 2 \cdot \vec {r _ {2}}, \tag {46}
$$

are coefficient factors. The operation · indicates element-wise multiplication [55]. a linearly decreases from 2 to 0 during the

![](images/f8baf99f298665597e0c88eb7ed3e880bd4b44136c5d0cc000ead8c38ebcdc5a.jpg)

<details>
<summary>scatter</summary>

| x (m) | y (m) |
|-------|-------|
| 50    | 920   |
| 100   | 470   |
| 150   | 470   |
| 200   | 770   |
| 250   | 350   |
| 300   | 280   |
| 350   | 200   |
| 400   | 650   |
| 450   | 330   |
| 500   | 480   |
| 550   | 180   |
| 600   | 430   |
| 650   | 740   |
| 700   | 690   |
| 750   | 610   |
| 800   | 580   |
| 850   | 290   |
| 900   | 40    |
| 950   | 730   |
| 1000  | 150   |
</details>

(a) Distribution of GUs.

![](images/10051614365cad8b244746ba08c60f581095bef8cadc7f3b8673b249f5dbe328.jpg)

<details>
<summary>scatter</summary>

| x    | y    | Group                     |
| ---- | ---- | ------------------------- |
| 100  | 920  | Blue                      |
| 200  | 820  | Blue (star marker)       |
| 250  | 770  | Purple                    |
| 300  | 780  | Purple                    |
| 400  | 160  | Blue (star marker)       |
| 450  | 330  | Blue (star marker)       |
| 500  | 500  | Yellow (star marker)     |
| 600  | 480  | Yellow (star marker)     |
| 700  | 720  | Orange (star marker)     |
| 800  | 190  | Green (star marker)      |
| 850  | 290  | Green (star marker)      |
| 950  | 160  | Green (star marker)      |
| 150  | 460  | Purple                    |
| 200  | 440  | Purple                    |
| 250  | 420  | Purple                    |
| 300  | 280  | Purple                    |
| 350  | 190  | Purple                    |
| 400  | 160  | Purple                    |
| 450  | 330  | Blue (star marker)       |
| 500  | 480  | Blue (star marker)       |
| 600  | 440  | Yellow (star marker)     |
| 700  | 720  | Orange (star marker)     |
| 800  | 190  | Green (star marker)      |
| 950  | 720  | Orange (star marker)     |
| 150  | 540  | Blue (star marker)       |
| 200  | 460  | Blue (star marker)       |
| 250  | 420  | Blue (star marker)       |
| 300  | 280  | Blue (star marker)       |
| 350  | 190  | Blue (star marker)       |
| 400  | 160  | Blue (star marker)       |
| 450  | 330  | Blue (star marker)       |
| 500  | 480  | Blue (star marker)       |
| 600  | 440  | Yellow (star marker)     |
| 700  | 720  | Orange (star marker)     |
| 800  | 190  | Green (star marker)       |
| 950  | 160  | Green (star marker)       |
| -    | -    | Blue (star marker)       |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                   |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple            |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                  |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                        |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple              |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                          |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                      |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| -    | -    | Purple                    |
| ... (approximate from chart: ~15 to ~12, ~18 to ~16, ~22 to ~14, ~28 to ~18, ~32 to ~16, ~38 to ~18, ~42 to ~18, ~48 to ~18, ~52 to ~18, ~58 to ~18, ~62 to ~18, ~68 to ~18, ~72 to ~18, ~78 to ~18, ~82 to ~18, ~88 to ~18, ~92 to ~18, ~98 to ~18, ~1.2 vs. Other clusters).
</details>

(b)UAV deployment results.   
Fig. 3. Cluster results via the WKD algorithm (30 GUs and 6 UAVs in the 1 km × 1 km area).

iteration:

$$
a = 2 - i _ {2} \times \frac {2}{I _ {2} ^ {\max}}, \tag {47}
$$

where $i _ { 2 }$ is the index of current iteration, $I _ { 2 } ^ { \mathrm { m a x } }$ is the maximum number of iterations. $\vec { r _ { 1 } }$ and $\vec { r _ { 2 } }$ are random vectors within [0,1]. $\complement ( \cdot )$ represents the complement operation. $P _ { B W O A } \in [ 0 , 1 ]$ is a ( ) [0 1]basis for action selection in the mechanism of encircling prey, and the distance vector $\vec { D }$ is calculated by

$$
\vec {D} = \left| \vec {C} \cdot \vec {X} ^ {*} \left(i _ {2}\right) - \vec {X} \left(i _ {2}\right) \right|. \tag {48}
$$

2) Spiral Updating: The agent tends to approach the current optimal individual in either encircling prey or spiral manner. In detail, the spiral updating mechanism for position updating in BWOA is

$$
\vec {X} (i _ {2} + 1) = \left\{ \begin{array}{l l} \mathbb {C} (\vec {X} (i _ {2})), & \text { if } P _ {B W O A} <   \tau_ {s u}, \\ \vec {X} (i _ {2}), & \text { if } P _ {B W O A} \geq \tau_ {s u}. \end{array} \right. \tag {49}
$$

Moreover, the step size $\tau _ { s u }$ is calculated as

$$
\tau_ {s u} = \frac {1}{1 + \exp \left(- 1 0 \left(\vec {A} \cdot \vec {D ^ {\prime}} - 0 . 5\right)\right)}, \tag {50}
$$

Algorithm 2: BWOA for the Offloading Decision.   
1: Initialization: Set the iteration index $i_{2}=1$ , maximum number of iteration $I_{2}^{\max}$ and the agent population $X_{k}$ , $k=1,2,\ldots,K$ .
2: Calculate the fitness value of the search agents and obtain the best search agent $\vec{X}^{*}(i_{2})$ .
3: repeat
4: for $k \in \{1, 2, \ldots, K\}$ do
5: Update A, C, and a according to (45), (46) and (47), respectively.
6: Generate the parameter $P_{rand} \in [0, 1]$ randomly.
7: if $P_{rand} \geq 0.5$ then
8: Update $\vec{D}$ by (51) and $\tau_{su}$ by (50).
9: Update the position $\vec{X}(i_{2})$ by (49).
10: else
11: if $|A| \geq 1$ then
12: Select a random agent $\vec{X}_{rand}$ and update $\vec{D}$ based on (54).
13: Update $\tau_{sp}$ via (53) and $\vec{X}(i_{2})$ via (52).
14: else
15: Update $\vec{D}$ via (48) and $\tau_{ep}$ via (44).
16: Update the positions of agents $\vec{X}(i_{2})$ via (43).
17: end if
18: end if
19: end for
20: Calculate the fitness value of each agent via (40) and obtain the best position $\vec{X}^{*}(i_{2})$ of the agents.
21: Update the iteration index $i_{2} = i_{2} + 1$ .
22: until $i_{2} > I_{2}^{\max}$ Output: The best fitness value $\Gamma$ and offloading decision $\lambda$ .

where $\vec { A }$ is updated based on (45), and $\vec { D ^ { \prime } }$ is updated as

$$
\vec {D} ^ {\prime} = | \vec {X} ^ {*} (i _ {2}) - \vec {X} (i _ {2}) |. \tag {51}
$$

3) Search for Prey: To achieve more exploration and avoid falling into local optima, some agents conduct random searches instead of updating toward the current optimal. This mechanism is called search for prey in BWOA. Since the exploration may bring agents to deviate from the current optima, it enhances the global search capacities of the agents. The updating rule for the positions of agents is

$$
\vec {X} (i _ {2} + 1) = \left\{ \begin{array}{l l} \mathbb {C} (\vec {X} (i _ {2})), & \text { if } P _ {B W O A} <   \tau_ {s p}, \\ \vec {X} (i _ {2}), & \text { if } P _ {B W O A} \geq \tau_ {s p}, \end{array} \right. \tag {52}
$$

where

$$
\tau_ {s p} = \frac {1}{1 + \exp \left(- 1 0 \left(\vec {A} \cdot \vec {D} ^ {\prime \prime} - 0 . 5\right)\right)}. \tag {53}
$$

Furthermore, $\vec { A }$ is obtained by (45), and $\vec { D ^ { \prime \prime } }$ is calculated as

$$
\vec {D} ^ {\prime \prime} = | \vec {C} \cdot \vec {X} _ {\text { rand }} (i _ {2}) - \vec {X} (i _ {2}) |, \tag {54}
$$

where $\vec { X } _ { r a n d }$ denotes the position of a random selected agent.

![](images/74b7713647ffc2faa3ed2675e8f172b5aedf4684b60b197d4e187807bba4bb6f.jpg)

<details>
<summary>bar</summary>

| Network scale | Optimal solution | BWOA | Greedy algorithm | SAA |
| ------------- | ---------------- | ---- | ---------------- | --- |
| M=9,N=2       | 40               | 40   | 40               | 40  |
| M=10,N=2      | 45               | 45   | 45               | 45  |
| M=11,N=2      | 60               | 60   | 60               | 60  |
| M=12,N=2      | 75               | 75   | 85               | 75  |
| M=15,N=3      | 100              | 105  | 135              | 105 |
| M=20,N=4      | 180              | 175  | 220              | 175 |
| M=25,N=5      | 260              | 260  | 290              | 255 |
| M=30,N=6      | 340              | 335  | 375              | 350 |
</details>

(a)

![](images/751f5736078acb731c2f81918c4a9730028d5a351cdaa9900d5c4707caa431f7.jpg)

<details>
<summary>bar</summary>

| Number of GUs | N = 2 | N = 3 | N = 4 | N = 5 |
| ------------- | ----- | ----- | ----- | ----- |
| M=10          | 45    | 45    | 45    | 45    |
| M=20          | 180   | 180   | 180   | 180   |
| M=30          | 270   | 330   | 330   | 330   |
| M=40          | 270   | 370   | 470   | 490   |
| M=50          | 270   | 370   | 470   | 540   |
</details>

(a)

![](images/01fdff0ad5b873ff874248991224a64b9496d34ee822c3162d0ce15017b946db.jpg)

<details>
<summary>line</summary>

| Network scale | Optimal solution | BWOA | Greedy algorithm | SAA |
| ------------- | ---------------- | ---- | ---------------- | --- |
| M=9 N=2       | 0                | 0    | 0                | 0   |
| M=10 N=2      | 100              | 0    | 0                | 0   |
| M=11 N=2      | 450              | 0    | 0                | 0   |
| M=12 N=2      | 1850             | 0    | 0                | 0   |
| M=15 N=3      | 0                | 0    | 0                | 0   |
| M=20 N=4      | 0                | 0    | 0                | 0   |
| M=25 N=5      | 0                | 0    | 0                | 0   |
| M=30 N=6      | 0                | 0    | 0                | 0   |
</details>

(b)

![](images/fcd5d8a5a3e084368c3dcd8359a52ae3dfe752f32f17b2126592bff9f9b7ecf6.jpg)

<details>
<summary>bar</summary>

| Number of GUs | N = 2 | N = 3 | N = 4 | N = 5 |
| ------------- | ----- | ----- | ----- | ----- |
| M=10          | 10    | 10    | 10    | 10    |
| M=20          | 20    | 20    | 20    | 20    |
| M=30          | 26    | 30    | 30    | 30    |
| M=40          | 26    | 33    | 38    | 40    |
| M=50          | 26    | 33    | 39    | 43    |
</details>

(b)   
Fig. 4. Performance of different algorithms under different network scales.   
Fig. 5. Energy cost and number of served GUs v.s. the number of GUs with different UAV scale.

4) Algorithm Design: The BWOA is provided in Algorithm 2 for solving P5. To begin with, K agents are set randomly. Then, the positions of agents are initialized, and the value of fitness function Γ λ for λ can be calculated according to (40). ( )Furthermore, at each iteration, the corresponding parameters a, A and C are updated (line 5). Each agent adopts different strategies based on the probability and updates its position in the next iteration. Specifically, each agent has a possibility of 0.5 to update the parameters and its positions towards optimal in the spiral manner according to (49) (lines 8-9). Otherwise, if the parameter $| { \cal A } | \geq 1$ , the agent is expected to randomly select 1another agent and search for prey to its direction (lines 12-13). Then, the position in the next iteration is obtained by (52). When $| A | < 1$ , the agent encircling prey and linearly approach the 1individual with best fitness value via (43) (lines 15-16). After all agents updating their positions, their fitness function values are calculated and the position of the current best agent is updated (line 20). The above process is repeated until the result converges [54]. Finally, the offloading decisions concerning λ can be derived. The implementation of Algorithm 2 is mainly related with the number and dimension of agents, i.e., K and MN, respectively. Moreover, the $M N + M + 2 N + 3$ constraints of

![](images/cd43f16c300b0650bb2ab09adee534c591557029fc3167016961c380c5322e44.jpg)

<details>
<summary>bar_line</summary>

| Network scale | Served GUs via WKD | Served GUs via R&R | Energy cost via WKD | Energy cost via R&R |
| :--- | :--- | :--- | :--- | :--- |
| M=20,N=4 | 20 | 20 | 180 | 185 |
| M=25,N=4 | 25 | 25 | 230 | 235 |
| M=30,N=4 | 30 | 30 | 270 | 275 |
| M=35,N=4 | 35 | 35 | 320 | 325 |
| M=40,N=4 | 39 | 36 | 390 | 395 |
</details>

Fig. 6. Performance of the algorithm with deployment optimization.

problem P4 impact the computational complexity to calculate the index functions. Hence, the complexity of Algorithm 2 is $\mathcal { O } ( K M N ( M N + M + 2 N + 3 ) I _ { 2 } ^ { \mathrm { m a x } } )$ .

![](images/a9cdefff63c38aa86a98974a8154d3398f8a6f5243b730353edf96c309fa0134.jpg)

<details>
<summary>bar</summary>

| Data size of tasks/Mbit | CVaR-based DRCC | Ideal circumstance |
| :--- | :--- | :--- |
| 50 | 218 | 218 |
| 55 | 284 | 284 |
| 60 | 367 | 365 |
| 65 | 463 | 461 |
| 70 | 579 | 574 |
</details>

(a)

![](images/fc87d12fc1290f657e033c6bd84549bfa077a3b719a6b4c9bc4dd124c69fc6a8.jpg)

<details>
<summary>line</summary>

| Data size of tasks/bit ×10^7 | T_max = 18s | T_max = 20s | T_max = 22s | T_max = 24s |
| ---------------------------- | ----------- | ----------- | ----------- | ----------- |
| 5                            | 260         | 210         | 180         | 150         |
| 5.5                          | 350         | 280         | 240         | 200         |
| 6                            | 450         | 370         | 300         | 260         |
| 6.5                          | 570         | 460         | 380         | 320         |
| 7                            | 730         | 580         | 480         | 400         |
</details>

(a)

![](images/a7c9d7030c40506b29a02c0852db074b6fbad8ac2e49cc35f6040ef66f7acb54.jpg)

<details>
<summary>bar</summary>

| Data size of tasks/Mbit | CVaR-based DRCC (Required CPU frequency/Hz ×10^10) | Ideal circumstance (Required CPU frequency/Hz ×10^10) |
| :--- | :--- | :--- |
| 50 | 2.4 | 2.4 |
| 55 | 2.65 | 2.65 |
| 60 | 2.9 | 2.9 |
| 65 | 3.18 | 3.18 |
| 70 | 3.45 | 3.45 |
</details>

(b)

![](images/b87ec572874fe260627164c4c03805e852a2b42b90efb6422e3185ba7e198c4b.jpg)

<details>
<summary>line</summary>

| Data size of tasks/bit (×10⁷) | T_max = 18s | T_max = 20s | T_max = 22s | T_max = 24s |
| ----------------------------- | ----------- | ----------- | ----------- | ----------- |
| 5                             | 2.6         | 2.4         | 2.2         | 2.0         |
| 5.5                           | 2.9         | 2.6         | 2.4         | 2.2         |
| 6                             | 3.2         | 2.9         | 2.6         | 2.4         |
| 6.5                           | 3.5         | 3.2         | 2.9         | 2.6         |
| 7                             | 3.8         | 3.4         | 3.1         | 2.8         |
</details>

(b)   
Fig. 7. Performance of the model with CSI estimation errors and ideal conditions.   
Fig. 8. Impact of tolerable delay on the network performance.

# V. SIMULATION RESULTS

In this section, simulations are conducted to evaluate the proposed algorithms. The GUs are distributed randomly in a 1 km × 1km area. The altitude of UAVs is 100m and the coordinate of the HAP is $\varpi _ { h } = [ 5 0 0 , 5 0 0 , 2 \times 1 0 ^ { 4 } ]$ m. The major = [500 500 2 10 ]parameters are in Table I [32], [33]. The data size of tasks is within , Mbits.

[50 70]The distribution of GUs and UAVs is depicted in Fig. 3(a), including 30 GUs and 6 UAVs. Algorithm 1 is applied to obtain the deployment positions of UAVs, and the clustering results of 30 GUs as well as the positions of 6 UAVs are shown in Fig. 3(b). It is observed that UAVs are deployed at the centers of GU clusters.

To evaluate the effectiveness and efficiency of the proposed BWOA, it is compared with the optimal solution (obtained by exhaustive search), greedy offloading algorithm, as well as the simulated annealing algorithm (SAA), as shown in Fig. 4. Specifically, from Fig. 4(a), it is observed that the optimization results of BWOA are close to optimal and outperform the greedy algorithm and SAA. Meanwhile, Fig. 4(b) provides the corresponding time complexity. Although the optimal solution is obtained by the exhaustive search, the time cost is not acceptable in the large-scale situations. Besides, the time cost of BWOA is lower than the greedy algorithm and SAA with the network scale increasing. Hence, the BWOA shows near optimal performance with lower time complexity.

Fig. 5 depicts the performance of energy cost and the number of served GUs with different number of UAVs. As the number of served GUs increases, more energy is consumed as expected. Moreover, with the same number of served GUs, the energy consumption is almost unchanged by simply increasing the number of UAVs. Besides, note that there exist unserved GUs if the resources are inadequate or the QoS demand of tasks cannot be comprehensively satisfied, indicating that the number of GUs in the network exceeds the network’s capacity and the constraints are violated with penalty factors. This is on accounting for the insufficient UAVs which leads to the limited aerial resources and less served GUs. In such a case, the number of served GUs can be improved by deploying more UAVs to alleviate load pressure.

The superiority of proposed WKD based algorithm is verified in Fig. 6. The total energy cost obtained via our proposed algorithms is compared with the results that UAVs are randomly deployed and GUs are randomly connected to the UAVs (R&R). Note that less energy is consumed compared with the baseline result with the same served GUs. Moreover, compared with the R&R method, the proposed WKD method can increase the number of GUs that the system can accommodate and make a better use of available resources. Besides, the overloading or under utilization of UAVs can be avoided.

![](images/506216052be1123c67bb15647c1be9273cb8b7b62b403a38bd8f02dbddd516eb.jpg)

<details>
<summary>line</summary>

| Data size of tasks/bit ×10^7 | Total energy consumption/J (p_u = 0.1W) | Total energy consumption/J (p_u = 0.3W) | Total energy consumption/J (p_u = 0.5W) |
| ---------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| 5                            | 220                                      | 220                                      | 220                                      |
| 5.5                          | 290                                      | 285                                      | 280                                      |
| 6                            | 370                                      | 365                                      | 360                                      |
| 6.5                          | 470                                      | 465                                      | 460                                      |
| 7                            | 590                                      | 585                                      | 580                                      |
</details>

![](images/fd07466f37741fadffa0b695e2112ae86ac4b308bd5fda4e248b8744647f4e04.jpg)

<details>
<summary>line</summary>

| Data size of tasks/bit (×10⁷) | Required CPU frequency/Hz (×10¹⁰) for p_u = 0.1W | Required CPU frequency/Hz (×10¹⁰) for p_u = 0.3W | Required CPU frequency/Hz (×10¹⁰) for p_u = 0.5W |
| ----------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| 5                             | 2.4                                             | 2.4                                             | 2.4                                             |
| 5.5                           | 2.65                                            | 2.65                                            | 2.65                                            |
| 6                            | 2.9                                             | 2.9                                             | 2.9                                             |
| 6.5                           | 3.2                                             | 3.2                                             | 3.2                                             |
| 7                            | 3.45                                            | 3.45                                            | 3.45                                            |
</details>

(b)

Fig. 9. Impact of transmission power of GUs.   
![](images/eb523b0cfd9aa9fb32d768f77ffb395d2f90bde88b11909f9ce836e95e9ec15d.jpg)

<details>
<summary>line</summary>

| Data size of tasks/bit (×10⁷) | p_h = 1W | p_h = 2W | p_h = 4W |
| ----------------------------- | -------- | -------- | -------- |
| 5                             | 200      | 200      | 220      |
| 5.5                           | 260      | 270      | 290      |
| 6                             | 330      | 340      | 370      |
| 6.5                           | 420      | 440      | 460      |
| 7                             | 530      | 550      | 570      |
</details>

(a)

![](images/4d3f304f2fe36388bca11e522aa94ca214b6f272ad4afeef0a1e2900214cc321.jpg)

<details>
<summary>line</summary>

| Data size of tasks/bits (×10⁷) | Required CPU frequency/Hz (×10¹⁰) for p_h = 1W | Required CPU frequency/Hz (×10¹⁰) for p_h = 2W | Required CPU frequency/Hz (×10¹⁰) for p_h = 4W |
| ------------------------------ | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| 5                              | 2.4                                             | 2.4                                             | 2.4                                             |
| 5.5                            | 2.6                                             | 2.6                                             | 2.6                                             |
| 6                              | 2.8                                             | 2.8                                             | 2.8                                             |
| 6.5                            | 3.0                                             | 3.0                                             | 3.0                                             |
| 7                              | 3.4                                             | 3.4                                             | 3.4                                             |
</details>

(b)   
Fig. 10. Impact of transmission power of UAVs.

Fig. 7 verifies the robustness of the proposed mechanism (CVaR-based DRCC). As provided in Fig. 7(a), we compare the results optimized via DRCC and CVaR based method with the ”ideal circumstance” to evaluate the impact of imperfect CSI, in which the accurate CSI is obtained. When there exist CSI estimation errors, more energy is consumed compared with the ideal circumstance. This is accounted by the fact that the MEC servers allocate more computing resources for the tasks to cope with the impact of environmental disturbances, as shown in Fig. 7(b).

The impacts of the tolerable delay of tasks are shown in Fig. 8. As the maximum tolerable delay increases, the energy consumption decreases, due to the less consumption of computing tasks in Fig. 8(a), since it provides more time for MEC processing and the required CPU frequency is decreased, as shown in Fig. 8(b). Hence, the computation energy is decreased. In addition, Fig. 9 shows the influence of GU transmission power. It is observed that with the increment of transmission power of GUs, both the total energy consumption and the required CPU frequency are decreased. It is explained that the transmission delay is decreased due to the increment of transmission rate, so the time is sufficient for computation.

The effect of transmission power of UAVs on the performance is discussed in Fig. 10. As expected in Fig. 10(a), UAVs consume more energy with the increment of transmission power. Moreover, in Fig. 10(b), more transmission power of UAVs leads to less CPU frequency consumption. It is explained that the transmission rate for G2U link is growing with the increment of transmission power, and thus, there is more remaining time for MEC processing, resulting in less CPU frequency required.

# VI. CONCLUSION

In this paper, we proposed a hierarchical aerial MEC model consisting of multiple UAVs and an HAP. Considering the limitation of battery capacities, we jointly optimized the UAV deployment strategies, resources allocation and offloading decisions to minimize the total energy consumption. Taking into account the imperfect CSI affected by the unpredictable environmental factors, we established an uncertainty set for CSI estimation errors and formulated the problem with the chance constraint. As for the solution, we designed the WKD based algorithm for the deployment of UAVs. Moreover, the chance constraint was transformed into a DRCC, and accordingly approximated into an MISOCP form under the worst case by employing the CVaR mechanism. Additionally, the MIP problem was further decomposed into two subproblems. To tackle the binary subproblem, BWOA was designed. Finally, we conducted extensive simulations to evaluate the robustness and efficiency. The results showed superiority of the proposed algorithm in the near optimal solution and low time complexity compared with other baseline algorithms. In the future works, the dynamic deployment for UAVs will be further investigated.

# REFERENCES

[1] H. Guo, X. Zhou, J. Wang, J. Liu, and A. Benslimane, “Intelligent task offloading and resource allocation in digital twin based aerial computing networks,” IEEE J. Sel. Areas Commun., vol. 41, no. 10, pp. 3095–3110, Oct. 2023.   
[2] J. Tian, D. Wang, H. Zhang, and D. Wu, “Service satisfaction-oriented task offloading and UAV scheduling in UAV-enabled MEC networks,” IEEE Trans. Wireless Commun., vol. 22, no. 12, pp. 8949–8964, Dec. 2023.   
[3] R. Xu, Z. Chang, X. Zhang, and T. Hämäläinen, “Blockchain-based resource trading in multi-UAV edge computing system,” IEEE Internet Things J., vol. 11, no. 12, pp. 21559–21573, Jun. 2024.   
[4] Y. Zhao et al., “Joint content caching, service placement, and task offloading in UAV-enabled mobile edge computing networks,” IEEE J. Sel. Areas Commun., vol. 43, no. 1, pp. 51–63, Jan. 2025.   
[5] Z. Jia, M. Sheng, J. Li, D. Niyato, and Z. Han, “LEO-satellite-assisted UAV: Joint trajectory and data collection for internet of remote things in 6G aerial access networks,” IEEE Internet Things J., vol. 8, no. 12, pp. 9814–9826, Jun. 2021.   
[6] X. Zhang, Z. Chang, T. Hämäläinen, and G. Min, “AoI-energy tradeoff for data collection in UAV-assisted wireless networks,” IEEE Trans. Commu., vol. 72, no. 3, pp. 1849–1861, Mar. 2024.   
[7] Y. Bai, H. Zhao, X. Zhang, Z. Chang, R. Jäntti, and K. Yang, “Toward autonomous multi-UAV wireless network: A survey of reinforcement learning-based approaches,” IEEE Commun. Surv. Tuts., vol. 25, no. 4, pp. 3038–3067, Fourth Quarter 2023.   
[8] C. Zhan, H. Hu, Z. Wang, R. Fan, and D. Niyato, “Unmanned aircraft system aided adaptive video streaming: A joint optimization approach,” IEEE Trans. Multimedia, vol. 22, no. 3, pp. 795–807, Mar. 2020.   
[9] Y. Chen, M. Liu, B. Ai, Y. Wang, and S. Sun, “Adaptive bitrate video caching in UAV-assisted MEC networks based on distributionally robust optimization,” IEEE Trans. Mobile Comput., vol. 23, no. 5, pp. 5245–5259, May 2024.   
[10] H. Guo, Y. Wang, J. Liu, and C. Liu, “Multi-UAV cooperative task offloading and resource allocation in 5G advanced and beyond,” IEEE Trans. Wireless Commun., vol. 23, no. 1, pp. 347–359, Jan. 2024.   
[11] J. You, Z. Jia, C. Dong, L. He, Y. Cao, and Q. Wu, “Computation offloading for uncertain marine tasks by cooperation of UAVs and vessels,” in Proc. IEEE Int. Conf. Commun., Rome, Italy, 2023, pp. 666–671.   
[12] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and A. Nallanathan, “Deep reinforcement learning based dynamic trajectory control for UAV-assisted mobile edge computing,” IEEE Trans. Mobile Comput., vol. 21, no. 10, pp. 3536–3550, Oct. 2022.   
[13] W. Chen, C. Liu, W. Wang, M. Peng, and W. Zhang, “Adaptive hybrid beamforming for UAV mmWave communications against asymmetric jitter,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 9432–9445, Aug. 2024.   
[14] G. Karabulut Kurt and H. Yanikomeroglu, “Communication, computing, caching, and sensing for next-generation aerial delivery networks: Using a high-altitude platform station as an enabling technology,” IEEE Veh. Technol. Mag., vol. 16, no. 3, pp. 108–117, Sep. 2021.

[15] G. Karabulut Kurt et al., “A vision and framework for the high altitude platform station (HAPs) networks of the future,” IEEE Commun. Surv. Tut., vol. 23, no. 2, pp. 729–779, Second Quarter 2021.   
[16] Q. Li, L. Shi, Z. Zhang, and G. Zheng, “Resource allocation in UAVenabled wireless-powered MEC networks with hybrid passive and active communications,” IEEE Internet Things J., vol. 10, no. 3, pp. 2574–2588, Feb. 2023.   
[17] F. Zhou, R. Q. Hu, Z. Li, and Y. Wang, “Mobile edge computing in unmanned aerial vehicle networks,” IEEE Wirel. Commun., vol. 27, no. 1, pp. 140–146, Feb. 2020.   
[18] C. Dong et al., “UAVs as an intelligent service: Boosting edge intelligence for air-ground integrated networks,” IEEE Netw., vol. 35, no. 4, pp. 167– 175, Jul./Aug. 2021.   
[19] M. Sheng, C. Zhao, J. Liu, W. Teng, Y. Dai, and J. Li, “Energy-efficient trajectory planning and resource allocation in UAV communication networks under imperfect channel prediction,” Sci. China Inf. Sci., vol. 65, no. 12, pp. 222301:1–222301:15, Nov. 2022.   
[20] Z. Yu, Y. Gong, S. Gong, and Y. Guo, “Joint task offloading and resource allocation in UAV-enabled mobile edge computing,” IEEE Internet Things J., vol. 7, no. 4, pp. 3147–3159, Apr. 2020.   
[21] N. Zhao, Z. Ye, Y. Pei, Y.-C. Liang, and D. Niyato, “Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing,” IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 6949–6960, Sep. 2022.   
[22] C. Zhan, H. Hu, Z. Liu, Z. Wang, and S. Mao, “Multi-UAV-enabled mobileedge computing for time-constrained IoT applications,” IEEE Internet Things J., vol. 8, no. 20, pp. 15553–15567, Oct. 2021.   
[23] J. Li, C. Yi, J. Chen, K. Zhu, and J. Cai, “Joint trajectory planning, application placement, and energy renewal for UAV-assisted MEC: A triple-learner-based approach,” IEEE Internet Things J., vol. 10, no. 15, pp. 13622–13636, Aug. 2023.   
[24] B. Liu, Y. Wan, F. Zhou, Q. Wu, and R. Q. Hu, “Resource allocation and trajectory design for MISO UAV-assisted MEC networks,” IEEE Trans. Veh. Technol., vol. 71, no. 5, pp. 4933–4948, May 2022.   
[25] Z. Ning, Y. Yang, X. Wang, Q. Song, L. Guo, and A. Jamalipour, “Multiagent deep reinforcement learning based UAV trajectory optimization for differentiated services,” IEEE Trans. Mobile Comput., vol. 23, no. 5, pp. 5818–5834, May 2024.   
[26] F. Song et al., “Evolutionary multi-objective reinforcement learning based trajectory control and task offloading in UAV-assisted mobile edge computing,” IEEE Trans. Mobile Comput., vol. 22, no. 12, pp. 7387–7405, Dec. 2023.   
[27] B. Liu, C. Liu, and M. Peng, “Computation offloading and resource allocation in unmanned aerial vehicle networks,” IEEE Trans. Veh. Technol., vol. 72, no. 4, pp. 4981–4995, Apr. 2023.   
[28] Y. Luo, W. Ding, and B. Zhang, “Optimization of task scheduling and dynamic service strategy for multi-UAV-enabled mobile-edge computing system,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 3, pp. 970–984, Sep. 2021.   
[29] Y. Wang, Z.-Y. Ru, K. Wang, and P.-Q. Huang, “Joint deployment and task scheduling optimization for large-scale mobile users in multi-UAVenabled mobile edge computing,” IEEE Trans. Cybern., vol. 50, no. 9, pp. 3984–3997, Sep. 2020.   
[30] B. Li, R. Yang, L. Liu, J. Wang, N. Zhang, and M. Dong, “Robust computation offloading and trajectory optimization for multi-UAV-assisted MEC: A multi-agent DRL approach,” IEEE Internet Things J., vol. 11, no. 3, pp. 4775–4786, Feb. 2024.   
[31] F. Granelli, C. Costa, J. Zhang, R. Bassoli, and F. H. Fitzek, “Design of an on-demand agile 5G multi-access edge computing platform using aerial vehicles,” IEEE Commun. Standards Mag., vol. 4, no. 4, pp. 34–41, Dec. 2020.   
[32] Z. Jia, Q. Wu, C. Dong, C. Yuen, and Z. Han, “Hierarchical aerial computing for Internet of Things via cooperation of HAPs and UAVs,” IEEE Internet Things J., vol. 10, no. 7, pp. 5676–5688, Apr. 2023.   
[33] M. Ansarifard, N. Mokari, M. Javan, H. Saeedi, and E. A. Jorswieck, “AI-based radio and computing resource allocation and path planning in NOMA NTNs: AoI minimization under CSI uncertainty,” 2023, arXiv:2305.00780.   
[34] Y. Chen, K. Li, Y. Wu, J. Huang, and L. Zhao, “Energy efficient task offloading and resource allocation in air-ground integrated MEC systems: A distributed online approach,” IEEE Trans. Mobile Comput., vol. 23, no. 8, pp. 8129–8142, Aug. 2024.   
[35] F. Song, M. Deng, H. Xing, Y. Liu, F. Ye, and Z. Xiao, “Energy-efficient trajectory optimization with wireless charging in UAV-assisted MEC based on multi-objective reinforcement learning,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 10867–10884, Dec. 2024.

[36] H. Cao, G. Yu, and Z. Chen, “Cooperative task offloading and dispatching optimization for large-scale users via UAVs and HAP,” in Proc. IEEE Wireless Commun. Netw. Conf., Glasgow, U.K., 2023, pp. 1–6.   
[37] Z. Cheng, M. Liwang, N. Chen, L. Huang, X. Du, and M. Guizani, “Deep reinforcement learning-based joint task and energy offloading in UAVaided 6G intelligent edge networks,” Comput. Commun., vol. 192, pp. 234– 244, 2022.   
[38] F. Song et al., “AoI and energy tradeoff for aerial-ground collaborative MEC: A multi-objective learning approach,” IEEE Trans. Mobile Comput., vol. 23, no. 12, pp. 11278–11294, Dec. 2024.   
[39] G. Zheng, C. Xu, M. Wen, and X. Zhao, “Service caching based aerial cooperative computing and resource allocation in multi-UAV enabled MEC systems,” IEEE Trans. Veh. Technol., vol. 71, no. 10, pp. 10934–10947, Oct. 2022.   
[40] S. Li et al., “Joint computation offloading and multidimensional resource allocation in air-ground integrated vehicular edge computing network,” IEEE Internet Things J., vol. 11, no. 20, pp. 32687–32700, Oct. 2024.   
[41] S. Li et al., “Two-hop packet scheduling, resource allocation, and UAV trajectory design for internet of remote things in air-ground integrated network,” IEEE Internet Things J., vol. 11, no. 15, pp. 26160–26172, Aug. 2024.   
[42] H. Kang, X. Chang, J. Miši´c, V. B. Miši´c, J. Fan, and Y. Liu, “Cooperative UAV resource allocation and task offloading in hierarchical aerial computing systems: A MAPPO-based approach,” IEEE Internet Things J., vol. 10, no. 12, pp. 10497–10509, Jun. 2023.   
[43] Y. Liu, S. Xie, and Y. Zhang, “Cooperative offloading and resource management for UAV-enabled mobile edge computing in power IoT system,” IEEE Trans. Veh. Technol., vol. 69, no. 10, pp. 12229–12239, Oct. 2020.   
[44] Y. Liu, K. Xiong, Q. Ni, P. Fan, and K. B. Letaief, “UAV-assisted wireless powered cooperative mobile edge computing: Joint offloading, CPU control, and trajectory optimization,” IEEE Internet Things J., vol. 7, no. 4, pp. 2777–2790, Apr. 2020.   
[45] N. Lin, H. Tang, L. Zhao, S. Wan, A. Hawbani, and M. Guizani, “A PDDQNLP algorithm for energy efficient computation offloading in UAV-assisted MEC,” IEEE Trans. Wireless Commun., vol. 22, no. 12, pp. 8876–8890, Dec. 2023.   
[46] S. Z. Selim and M. A. Ismail, “K-means-type algorithms: A generalized convergence theorem and characterization of local optimality,” IEEE Trans. Pattern Anal. Mach. Intell., vol. PAMI-6, no. 1, pp. 81–87, Jan. 1984.   
[47] S. Sarykalin, G. Serraino, and S. Uryasev, “Tutorials in operations research: State-of-the-art decision-making tools in the information-intensive age,” in Value-At-Risk Vs. Conditional Value-At-Risk in Risk Management and Optimization, Chapter 13. Oct. 2014, pp. 270–294. [Online]. Available: https://pubsonline.informs.org/doi/abs/10.1287/educ.1080.0052   
[48] R. T. Rockafellar and S. Uryasev, “Optimization of conditional value-atrisk,” J. Risk, vol. 2, no. 3, pp. 21–41, Sep. 2000.   
[49] C. Cui, Z. Jia, C. Dong, Z. Ling, J. You, and Q. Wu, “Distributionally robust chance-constrained optimization for hierarchical UAV-based MEC,” in Proc. IEEE Conf. Comput. Commun. Workshops, Hoboken, NJ, 2023, pp. 1–6.   
[50] Z. Ling, F. Hu, Y. Zhang, L. Fan, F. Gao, and Z. Han, “Distributionally robust chance-constrained backscatter communication-assisted computation offloading in WBANs,” IEEE Trans. Commu., vol. 69, no. 5, pp. 3395– 3408, May 2021.   
[51] K.-W. Ding, D. M.-H. Wang, and N. Huang, “Distributionally robust chance constrained problem under interval distribution information,” Optim. Lett., vol. 12, pp. 1862–4472, Aug. 2018.   
[52] S. Zymler, B. Kuhn, and D. Rustem, “Distributionally robust joint chance constraints with second-order moment information,” Math. Program., vol. 137, no. 1/2, pp. 167–198, Feb. 2011.   
[53] Z. Wu, B. Li, Z. Fei, Z. Zheng, B. Li, and Z. Han, “Energy-efficient robust computation offloading for Fog-IoT systems,” IEEE Trans. Veh. Technol., vol. 69, no. 4, pp. 4417–4425, Apr. 2020.   
[54] D. Palomar and M. Chiang, “A tutorial on decomposition methods for network utility maximization,” IEEE J. Sel. Areas Commun., vol. 24, no. 8, pp. 1439–1451, Aug. 2006.   
[55] Q.-V. Pham, S. Mirjalili, N. Kumar, M. Alazab, and W.-J. Hwang, “Whale optimization algorithm with applications to resource allocation in wireless networks,” IEEE Trans. Veh. Technol., vol. 69, no. 4, pp. 4285–4297, Apr. 2020.   
[56] H. F. Eid, “Binary whale optimization: An effective swarm algorithm for feature selection,” Int. J. Metaheuristics, vol. 7, no. 1, pp. 67–79, May 2018.   
[57] V. Kumar and D. Kumar, “Binary whale optimization algorithm and its application to unit commitment problem,” Neural Comput. Appl., vol. 32, pp. 2095–2123, Apr. 2020.   
[58] S. Mirjalili and A. Lewis, “The whale optimization algorithm,” Adv. Eng. Softw., vol. 95, pp. 51–67, May 2016.

![](images/56f15017a0dad6eba61e296e41c4987387f1b0d60644339612d7d2f2c55affc9.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling woman with short hair and glasses, wearing a bright yellow top (no text or symbols visible)
</details>

Ziye Jia (Member, IEEE) received the BE, MS, and PhD degrees in communication and information systems from Xidian University, Xi’an, China, in 2012, 2015, and 2021, respectively. From 2018 to 2020, she was a visiting PhD Student with the Department of Electrical and Computer Engineering, University of Houston. She is currently an associate professor with the Key Laboratory of Dynamic Cognitive System of Electromagnetic Spectrum Space, Ministry of Industry and Information Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, China.

Her current research interests include space-air-ground networks, aerial access networks, UAV networking, resource optimization, machine learning, etc.

![](images/3aca788700d87b74024c6548311a739ac652fef5b8d8b8f612c5831ed1752d52.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a woman with shoulder-length hair wearing a black collared shirt (no text or symbols visible)
</details>

Can Cui is a postgraduate student with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing, China. Her current research interests include convex optimization and its applications in computation offloading and resource allocation, edge computing, and low-altitude intelligent networks.

![](images/42d190732d0cd8f18a8dc9f3c0cb18df6e72965cff2846344c9ab231d458655d.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing a black hoodie (no text or symbols visible)
</details>

Chao Dong (Member, IEEE) received the PhD degree in communication engineering from PLA University of Science and Technology, China, in 2007. He is now a full professor with College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, China. His current research interests include D2D communications, UAVs swarm networking and anti-jamming network protocol.

![](images/d923feb519c312e1f45c1cbba845160b52fb552e933839ad1f8fdefbff4fed52.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in formal attire with glasses against a blue background (no text or symbols visible)
</details>

Qihui Wu (Fellow, IEEE) received the BS degree in communications engineering and the MS and PhD degrees in communications and information systems from the Institute of Communications Engineering, Nanjing, China, in 1994, 1997, and 2000, respectively. From 2003 to 2005, he was a post-doctoral research associate with Southeast University, Nanjing. From 2005 to 2007, he was an associate professor with the College of Communications Engineering, PLA University of Science and Technology, Nanjing, where he was a full professor, from 2008 to 2016.

From March 2011 to September 2011, he was an advanced visiting scholar with the Stevens Institute of Technology, Hoboken, NJ, USA. Since May 2016, he has been a full professor with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing. His current research interests include wireless communications and statistical signal processing, with an emphasis on system design of software defined radio, cognitive radio, and smart radio.

![](images/87530b7f04dc1f017192aecf7f69c16d66a867416c36c07da538473a60caca0b.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in a suit and tie (no text or symbols visible)
</details>

Zhuang Ling (Member, IEEE) received the BS and PhD degrees in the College of Communication Engineering, Jilin University, Jilin, China, in 2016 and 2021, respectively. Currently, he serves as an associate professor in the College of Communication Engineering, Jilin University, Changchun, Jilin, China. He was formerly a postdoctoral fellow in the same college. In 2019, he served as a visiting PhD student in the Department of Electrical and Computer Engineering with the University of Houston. His research interests include Wireless Body Area Network, High-Speed Railway, Backscatter Communications, Energy Harvesting, Age of Information, and Distributionally Robust Optimization.

![](images/738a0dbbeb8c8fa05c32b3974a3541e566ca8fa2796b37ea81f7ff3a39d64baa.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a dark jacket (no visible text or symbols)
</details>

Dusit Niyato (Fellow, IEEE) received the BEng degree from the King Mongkuts Institute of Technology Ladkrabang (KMITL), Thailand and the PhD degree in electrical and computer engineering from the University of Manitoba, Canada. He is a professor in the College of Computing and Data Science, with Nanyang Technological University, Singapore. His research interests are in the areas of mobile generative AI, edge intelligence, quantum computing and networking, and incentive mechanism design.

![](images/676822ea867f5a4cddb8e625ba2b51c1b3fd540861a9f756a107c70d96d3fa2e.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in formal suit and bow tie, standing indoors with decorative elements (no visible text or symbols)
</details>

Zhu Han (Fellow, IEEE) received the BS degree in electronic engineering from Tsinghua University, in 1997, and the MS and PhD degrees in electrical and computer engineering from the University of Maryland, College Park, in 1999 and 2003, respectively. From 2000 to 2002, he was an R&D Engineer of JDSU, Germantown, Maryland. From 2003 to 2006, he was a research associate with the University of Maryland. From 2006 to 2008, he was an assistant professor with Boise State University, Idaho. Currently, he is a John and Rebecca Moores professor in the Electrical and Computer Engineering Department as well as in the Computer Science Department, University of Houston, Texas. Dr. Han’s main research targets on the novel game-theory related concepts critical to enabling efficient and distributive use of wireless networks with limited resources. His other research interests include wireless resource allocation and management, wireless communications and networking, quantum computing, data science, smart grid, carbon neutralization, security and privacy. Dr. Han received an NSF Career Award, in 2010, the Fred W. Ellersick Prize of the IEEE Communication Society, in 2011, the EURASIP Best Paper Award for the Journal on Advances in Signal Processing, in 2015, IEEE Leonard G. Abraham Prize in the field of Communications Systems (best paper award in IEEE JSAC), in 2016, IEEE Vehicular Technology Society 2022 Best Land Transportation Paper Award, and several best paper awards in IEEE conferences. Dr. Han was an IEEE Communications Society Distinguished Lecturer from 2015 to 2018 and ACM Distinguished Speaker from 2022 to 2025, AAAS fellow since 2019, and ACM Fellow since 2024. Dr. Han is a 1% highly cited Researcher since 2017 according to Web of Science. Dr. Han is also the winner of the 2021 IEEE Kiyo Tomiyasu Award (an IEEE Field Award), for outstanding early to mid-career contributions to technologies holding the promise of innovative applications, with the following citation: “for contributions to game theory and distributed management of autonomous communication networks.”