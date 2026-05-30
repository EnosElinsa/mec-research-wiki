# Joint Trajectory and Communication Design for Multi-UAV Enabled Wireless Networks

Qingqing Wu, Member, IEEE, Yong Zeng , Member, IEEE, and Rui Zhang , Fellow, IEEE

Abstract— Due to the high maneuverability, flexible deployment, and low cost, unmanned aerial vehicles (UAVs) have attracted significant interest recently in assisting wireless communication. This paper considers a multi-UAV enabled wireless communication system, where multiple UAV-mounted aerial base stations are employed to serve a group of users on the ground. To achieve fair performance among users, we maximize the minimum throughput over all ground users in the downlink communication by optimizing the multiuser communication scheduling and association jointly with the UAV’s trajectory and power control. The formulated problem is a mixed integer nonconvex optimization problem that is challenging to solve. As such, we propose an efficient iterative algorithm for solving it by applying the block coordinate descent and successive convex optimization techniques. Specifically, the user scheduling and association, UAV trajectory, and transmit power are alternately optimized in each iteration. In particular, for the nonconvex UAV trajectory and transmit power optimization problems, two approximate convex optimization problems are solved, respectively. We further show that the proposed algorithm is guaranteed to converge. To speed up the algorithm convergence and achieve good throughput, a low-complexity and systematic initialization scheme is also proposed for the UAV trajectory design based on the simple circular trajectory and the circle packing scheme. Extensive simulation results are provided to demonstrate the significant throughput gains of the proposed design as compared to other benchmark schemes.

Index Terms— UAV communications, throughput maximization, optimization, trajectory design, mobility control.

# I. INTRODUCTION

U NMANNED aerial vehicles (UAVs), also commonlyknown as drones, have attracted significant attention known as drones，have attracted significant attention in the past decade for various applications, such as surveillance and monitoring, aerial imaging, cargo delivery, etc [2]. As reported in [3], the global market for commercial UAV applications, estimated at about 2 billion dollars in 2016, will skyrocket to as much as 127 billion dollars by 2020. Equipped with advanced transceivers and batteries, UAVs are gaining increasing popularity in information technology (IT)

Manuscript received May 7, 2017; revised August 13, 2017, October 30, 2017, and December 26, 2017; accepted December 27, 2017. Date of publication January 5, 2018; date of current version March 8, 2018. This work was supported by the National University of Singapore under Research Grant R-263-000-B62-112. This paper was presented in part at the IEEE GLOBECOM 2017 [1]. The associate editor coordinating the review of this paper and approving it for publication was L. Song. (Corresponding author: Yong Zeng.)

The authors are with the Department of Electrical and Computer Engineering, National University of Singapore, Singapore 609774 (e-mail: elewuqq@nus.edu.sg; elezeng@nus.edu.sg; elezhang@nus.edu.sg).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TWC.2017.2789293

applications due to their high maneuverability and flexibility for on-demand deployment. In particular, UAVs typically have high possibilities of line-of-sight (LoS) air-to-ground communication links, which are appealing to the wireless service providers [4]. To capitalize on this growing opportunity, several leading IT companies have launched pilot projects, such as Project Aquila by Facebook [5] and Project Loon by Google [6], for providing ubiquitous internet access worldwide by leveraging the UAV/drone technology. The 3rd Generation Partnership Project (3GPP) is also looking up into the sky and studying aerial vehicles supported by Long Term Evolution (LTE) where the initial focus is on UAV [7]. In fact, with the approval of Federal Aviation Administration (FAA), Qualcomm and AT&T have optimized LTE networks for UAV communications [8], which aims to pave the way to a wide-scale deployment of UAVs in the upcoming fifth generation (5G) wireless networks, especially for missioncritical use cases. Meanwhile, extensive research efforts from the academia have also been devoted to employing UAVs as different types of wireless communication platforms [9], such as aerial mobile base stations (BSs) [10]–[14], mobile relays [15], [16], and flying computing cloudlets [17], [18]. In particular, employing UAVs as aerial BSs is envisioned as a promising solution to enhance the performance of the existing cellular systems. Depending on whether the UAV’s high mobility is exploited or not, two different lines of research can be identified in the literature, namely static-UAV or mobile-UAV enabled wireless networks.

The research on the static-UAV enabled wireless networks mainly focuses on the UAV deployment/placement optimization [10]–[14], with the UAVs serving as aerial quasi-static BSs to support ground users in a given area from a certain altitude. As such, the altitude and the horizontal location of the UAV can be either separately or jointly optimized for different quality-of-sevice (QoS) requirements. In particular, the authors in [12] provide an analytical approach to optimize the altitude of a UAV for providing maximum coverage for ground users. In contrast, by fixing the altitude, the horizontal positions of UAVs are optimized in [13] to minimize the number of required UAV BSs to cover a given set of ground users. In three-dimensional (3D) space, a drone-enabled small cell placement optimization problem is investigated in [14] to maximize the number of users that can be covered.

Besides the UAV placement optimization, exploiting the UAV’s high mobility in the mobile-UAV enabled wireless networks is anticipated to unlock the full potential of UAV-ground communications. With the fully controllable UAV mobility, the communication distance between the UAV and ground users can be significantly shortened by proper UAV trajectory design and user scheduling. This is analogous and yet in sharp contrast to the existing small-cell technology [19]–[22], where the cell radius is reduced by increasing the number of small-cell BSs deployed, but at the cost of increased infrastructure expenditure. Motivated by this, the UAV trajectory design is rigorously studied in [16] and [23] for a mobile relaying system and point-to-point energy-efficient system, respectively, where sequential convex optimization techniques are applied to solve the non-convex trajectory optimization problems therein. Though providing a general framework for trajectory optimization in two-dimensional (2D) space, the studies in [16] and [23] only focus on the setup with single UAV and single ground user. For UAV-enabled multiuser system, a novel cyclical multiple access scheme is proposed in [24], where the UAV communicates with ground users when it flies sufficiently close to each of them in a periodic (cyclical) time-division manner. An interesting throughput-access delay tradeoff is revealed and it has been shown that significant throughput gains can be achieved over the case of a static UAV for delay-tolerant applications. However, only one single UAV with the constant flying speed is considered in [24], and the ground users are assumed to be uniformly located in a one-dimensional (1D) line, which simplifies the analysis but limits the applicability in practice.

In this paper, we study a general multi-UAV enabled wireless communication system, where multiple UAVs are employed to serve a group of users on the ground in a given 2D area. Although a single UAV has demonstrated its advantages in performance enhancement for wireless networks [1], [16], [23], [25]–[29], it has limited capability in general and may not guarantee availability during the entire mission due to its practical size, weight and power (SWAP) constraints [9]. This thus motivates the deployment of multiple or a swarm of UAVs which cooperatively serve the ground users to achieve more efficient communications. For example, a group of UAVs may be deployed to keep track of the participants in a largearea event and to form a multi-hop communication network connecting to the ground audience. More importantly, in a multi-UAV enabled network, users could be served in parallel with higher throughput and lower access delay, which could effectively alleviate the fundamental throughput-access delay tradeoff in single-UAV communications [24].

Without loss of generality, we consider that all UAVs share the same frequency band for their communications with the ground users. By focusing on the downlink transmission from the UAVs to ground users, our goal is to maximize the minimum average rate among all users by jointly optimizing the user communication scheduling and association, and the UAV trajectory and transmit power control in a given finite period. Such a joint optimization problem is practically appealing, but has not been investigated in the literature to the authors’ best knowledge. On one hand, by properly designing the trajectories of different UAVs, not only short-distance LoS links can be proactively and dynamically established for those desired UAV-user pairs, but also the interfering channel distances between the undesired UAV-user pairs can be enlarged to alleviate the co-channel interference. On the other hand, in the occasional scenarios when the UAVs have to get close with each other for serving nearby users, their transmission power can be adjusted to reduce interference. While maximum transmission power is used for maximizing spectrum efficiency when the UAVs are far apart to serve users that are well separated. Therefore, the system performance can benefit from different design dimensions of the proposed joint optimization. However, such a joint trajectory and adaptive communication design problem is non-trivial to solve. This is because the user scheduling and association, UAV trajectory optimization, and transmit power control are closely coupled with each other in our considered problem, which makes it challenging to solve in general.

To tackle the above challenges, we first relax the binary variables for user scheduling and association into continuous variables and solve the resulting problem with an efficient iterative algorithm by leveraging the block coordinate descent method [30]. Specifically, the entire optimization variables are partitioned into three blocks for the user scheduling and association, UAV trajectory, and transmit power control, respectively. Then, these three blocks of variables are alternately optimized in each iteration, i.e., one block is optimized at each time while keeping the other two blocks fixed. However, even with fixed user scheduling and association, the UAV trajectory optimization problem with fixed power control and the UAV power control problem with fixed trajectory are still difficult to solve due to their non-convexity. We thus apply the successive convex optimization technique to solve them approximately. We also show that our proposed algorithm is guaranteed to converge. To speed up the algorithm convergence and achieve a superior performance, we propose an efficient and systematic trajectory initialization scheme based on the simple circular trajectory and the circle packing scheme. Numerical results show that significant throughput gains are achieved by our proposed joint design, as compared to conventional static UAV or other benchmark schemes with heuristic UAV trajectories. It is also shown that the throughput of the proposed mobile UAV system increases with the UAV trajectory design period, revealing the general throughput-access delay tradeoff [1], [24] in multi-UAV enabled communications. In addition, compared to the single-UAV case, this tradeoff is shown to be significantly improved by the use of multiple UAVs.

The rest of this paper is organized as follows. Section II introduces the system model and the problem formulation for a multi-UAV enabled wireless network. In Section III, we propose an efficient iterative algorithm by applying the block coordinate descent and the successive convex optimization techniques. Section VI presents the numerical results to demonstrate the performance of the proposed design. Finally, we conclude the paper in Section VI.

Notations: In this paper, scalars are denoted by italic letters, vectors and matrices are respectively denoted by bold-face lower-case and upper-case letters. $\mathbf { \mathbb { R } } ^ { M \times 1 }$ denotes the space of M-dimensional real-valued vector. For a vector a, -arepresents its Euclidean norm and $\mathbf { a } ^ { T }$ denotes its transpose. For a time-dependent function x(t), x˙(t) denotes the derivative with respect to time t . For a set K, |K| denotes its cardinality.

# II. SYSTEM MODEL AND PROBLEM FORMULATION

# A. System Model

As shown in Fig. 1, we consider a wireless communication system where $M \geq 1 ~ \mathrm { U A V s }$ are employed to serve a group of $K > 1$ ground users. The user and UAV sets are denoted as and , respectively, where $| { \mathcal { K } } | = K$ and $| { \mathcal { M } } | = M$ . This practically corresponds to an information broadcast system enabled by UAVs. Assume that all the UAVs share the same frequency band for communication over consecutive periods each of duration $T \ > \ 0$ in second (s). During any period, each of the UAVs serves its associated ground users via a periodic/cyclical time-division multiple access (TDMA). Note that the choice of T has a significant impact on the system performance. On one hand, thanks to the UAV mobility, a larger period T provides more time for each UAV to move closer to its served users to achieve better communication channels, as well as to fly sufficiently away from the users served by other UAVs for more effective interference mitigation, thus achieving a higher throughput. On the other hand, a larger T in general implies a larger access delay for users since each user may need to wait for a longer time to be scheduled to communicate with a UAV between two periods. Therefore, the period T needs to be properly chosen in practice to strike a balance between the user throughput and access delay, i.e., there exists a fundamental throughput-access delay tradeoff [24] in UAV-enabled communications.

Without loss of generality, we consider a 3D Cartesian coordinate system where the horizontal coordinate of each ground user k is fixed at $\begin{array} { r } { \mathbf { w } _ { k } = [ x _ { k } , y _ { k } ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 } , k \in \mathcal { K } . } \end{array}$ All UAVs are assumed to fly at a fixed altitude H above ground and the time-varying horizontal coordinate of UAV $m \in { \mathcal { M } }$ at time instant t is denoted by $\mathbf { q } _ { m } ( t ) = [ x _ { m } ( t ) , y _ { m } ( t ) ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 }$ , with $0 \leq t \leq T$ . The UAV trajectories need to satisfy the following constraint

$$
\mathbf {q} _ {m} (0) = \mathbf {q} _ {m} (T), \quad \forall m, \tag {1}
$$

which implies that each UAV needs to return to its initial location by the end of each period T such that users can be served periodically in the next period. In practice, the trajectories of UAVs are also subject to the maximum speed constraints1 and collision avoidance constraints, i.e,

$$
\left| \left| \dot {\mathbf {q}} _ {m} (t) \right| \right| \leq V _ {\max}, \quad 0 \leq t \leq T, \quad \forall m, \tag {2}
$$

$$
\left| \left| \mathbf {q} _ {m} (t) - \mathbf {q} _ {j} (t) \right| \right| \geq d _ {\min}, \quad 0 \leq t \leq T, \quad \forall j \neq m, \tag {3}
$$

where $V _ { \mathrm { m a x } }$ in (2) denotes the maximum UAV speed in meter/second (m/s) and $d _ { \mathrm { m i n } }$ denotes the minimum inter-UAV distance in m to ensure collision avoidance. For ease of exposition, the period T is discretized into N equaltime slots, indexed by $n ~ = ~ 1 , \ldots , N$ . The elemental slot length $\begin{array} { r } { \delta _ { t } \ = \ \frac { T } { N } } \end{array}$ is chosen to be sufficiently small such that a $\mathrm { U A V } _ { \mathrm { \Delta } }$ location is considered as approximately unchanged

1Here, we do not consider the minimum speed constraints, which is practically valid for the rotary-wing UAVs with the capability of keeping stationary at fixed positions, i.e., a minimum zero-speed is feasible. However, for the fixed-wing UAVs that must move forward to remain aloft, additional minimum speed constraints, $\mathrm { i . e . , } | | \dot { \mathbf { q } } _ { m } ( t ) | | \geq V _ { \operatorname* { m i n } } > 0 , 0 \leq t \leq T , \forall m$ , need to be imposed [23], which can be handled by the proposed algorithm with only a minor modification.

![](images/96c5416d3b75857ad351f578068e409996e045d94b22bb06cdf35dcf56a5845a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["直升机"] -->|Signal| B["Device 1"]
    A -->|Signal| C["Device 2"]
    A -->|Signal| D["Device 3"]
    A -->|Signal| E["Device 4"]
    A -->|Signal| F["Device 5"]
    G["直升机"] -->|Interference| B
    G -->|Interference| C
    G -->|Interference| D
    G -->|Interference| E
    G -->|Interference| F
    style A fill:#f9f,stroke:#333
    style G fill:#bbf,stroke:#333
```
</details>

Fig. 1. A multi-UAV enabled wireless network.

within each time slot even at the maximum speed $V _ { \mathrm { m a x } }$ . As a result, the trajectory of UAV m can be approximated by the N two-dimensional sequences ${ \bf q } _ { m } [ n ] = [ x _ { m } [ n ] , y _ { m } [ n ] ] ^ { T } ,$ , $n = 1 , \cdots , N$ . Furthermore, the trajectory constraints (1)–(3) can be equivalently written as

$$
\mathbf {q} _ {m} [ 1 ] = \mathbf {q} _ {m} [ N ], \tag {4}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n + 1 ] - \mathbf {q} _ {m} [ n ] \right| \right| ^ {2} \leq S _ {\max} ^ {2}, \quad n = 1, \dots , N - 1, \tag {5}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ] \right| \right| ^ {2} \geq d _ {\min} ^ {2}, \quad \forall n, m, j \neq m, \tag {6}
$$

where $S _ { \operatorname* { m a x } } \triangleq V _ { \operatorname* { m a x } } \delta _ { t }$ is the maximum horizontal distance that the UAV can travel in each time slot. In fact, any required accuracy of the adopted discrete-time approximation can be always satisfied by choosing a minimum $N ,$ as follows. To guarantee a certain accuracy, the ratio of $S _ { \mathrm { m a x } }$ and H can be restricted below a threshold, i.e., $\begin{array} { r } { \frac { S _ { \mathrm { m a x } } } { H } \leq \varepsilon _ { \mathrm { m a x } } } \end{array}$ , where $\varepsilon _ { \mathrm { m a x } }$ is the given threshold. Then, the minimum number of time slots required for achieving the accuracy with a given $\varepsilon _ { \mathrm { m a x } }$ can be obtained as

$$
N \geq \frac {V _ {\max} T}{H \varepsilon_ {\max}}. \tag {7}
$$

However, further increasing N also increases our design complexity. Therefore, the number of time slots N can be properly chosen in practice to balance between the accuracy and complexity.

The distance from UAV m to user k in time slot n can be expressed as

$$
d _ {k, m} [ n ] = \sqrt {H ^ {2} + | | \mathbf {q} _ {m} [ n ] - \mathbf {w} _ {k} | | ^ {2}}. \tag {8}
$$

For simplicity, we assume that the communication links from the UAV to the ground users are dominated by the LoS links where the channel quality depends only on the UAV-user distance. Furthermore, the Doppler effect caused by the UAV mobility is assumed to be well compensated at the receivers. Thus, the channel power gain from UAV m to user k during slot n follows the free-space path loss model, which can be expressed as

$$
h _ {k, m} [ n ] = \rho_ {0} d _ {k, m} ^ {- 2} [ n ] = \frac {\rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {m} [ n ] - \mathbf {w} _ {k} | | ^ {2}}, \tag {9}
$$

where ρ0 denotes the channel power at the reference distance $d _ { 0 } = 1 \mathrm { ~ m ~ }$ . Define a binary variable $a _ { k , m } [ n ]$ , which indicates that user k is served by UAV m in time slot n if $\alpha _ { k , m } [ n ] = 1 ;$ otherwise, $a _ { k , m } [ n ] = 0 .$ As such, $a _ { k , m } [ n ]$ specifies not only the user communication scheduling across the different time slots, but also the UAV-user association for each time slot. We assume that in each time slot, each UAV only serves at most one user and each user is only served by at most one UAV, which yields the following constraints

$$
\sum_ {k = 1} ^ {K} \alpha_ {k, m} [ n ] \leq 1, \quad \forall m, n, \tag {10}
$$

$$
\sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \leq 1, \quad \forall k, n, \tag {11}
$$

$$
\alpha_ {k, m} [ n ] \in \{0, 1 \}, \quad \forall k, m, n. \tag {12}
$$

The downlink transmit power of UAV m, $m \in { \mathcal { M } }$ in time slot n is denoted by $p _ { m } [ n ]$ , which is subject to the constraint $0 ~ \leq ~ p _ { m } [ n ] ~ \leq ~ P _ { \operatorname* { m a x } } ,$ , with $P _ { \mathrm { m a x } }$ denoting the peak UAV transmission power. Thus, if user k is served by UAV m in time slot n, i.e., $a _ { k , m } [ n ] = 1$ , the corresponding received signal-tointerference-plus-noise ratio (SINR) at user k can be expressed as

$$
\gamma_ {k, m} [ n ] = \frac {p _ {m} [ n ] h _ {k , m} [ n ]}{\sum_ {j = 1 , j \neq m} ^ {M} p _ {j} [ n ] h _ {k , j} [ n ] + \sigma^ {2}}, \tag {13}
$$

where $\sigma ^ { 2 }$ is the power of the additive white $\begin{array} { r l } { ~ } & { { } \sum _ { j = 1 , j \ne m } ^ { M } p _ { j } [ n ] h _ { k , j } [ n ] } \end{array}$ GN) at the receiver. The termin the denominator of (13) represents other UAVs in time slot n. Thus, the achievable rate of user k in time slot n, denoted by $R _ { k } [ n ]$ in bits/second/Hertz (bps/Hz), can be expressed as

$$
R _ {k} [ n ] = \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \log_ {2} (1 + \gamma_ {k, m} [ n ]). \tag {14}
$$

Thus, the achievable average rate of user k over N time slots is given by Rk = 1N Nn=1 Ri [n]. $\begin{array} { r } { R _ { k } = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \mathbf { \bar { \Sigma } } R _ { i } [ n ] } \end{array}$

# B. Problem Formulation

Let $\mathrm { ~ \bf ~ A ~ } = \{ \alpha _ { k , m } [ n ] , \forall k , m , n \} , \mathrm { ~ \bf ~ Q ~ } = \{ { \bf q } _ { m } [ n ] , \forall m , n \}$ , and $\mathbf { P } = \{ p _ { m } [ n ] , \forall m , n \}$ . By assuming that the locations of the ground users are known, our goal is to maximize the minimum average rate among all users by jointly optimizing the user scheduling and association $( \mathrm { i . e . , \mathbf { A } } )$ , UAV trajectory (i.e., Q), and transmit power (i.e., P) over all time slots. Define $\eta ( \mathbf { A } , \mathbf { Q } , \mathbf { P } ) = \operatorname* { m i n } _ { k \in \mathcal { K } } R _ { k }$ as a function of A, Q, and P. The k∈ Koptimization problem is formulated as

$$
\max _ {\eta , \mathbf {A}, \mathbf {Q}, \mathbf {P}} \eta \tag {15a}
$$

$$
\text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \log_ {2} (1 + \gamma_ {k, m} [ n ]) \geq \eta , \quad \forall k, \tag {15b}
$$

$$
\sum_ {k = 1} ^ {K} \alpha_ {k, m} [ n ] \leq 1, \quad \forall m, n, \tag {15c}
$$

$$
\sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \leq 1, \quad \forall k, n, \tag {15d}
$$

$$
\alpha_ {k, m} [ n ] \in \{0, 1 \}, \quad \forall k, m, n, \tag {15e}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n + 1 ] - \mathbf {q} _ {m} [ n ] \right| \right| ^ {2} \leq S _ {\max} ^ {2}, \quad n = 1, \dots , N - 1, \tag {15f}
$$

$$
\mathbf {q} _ {m} [ 1 ] = \mathbf {q} _ {m} [ N ], \quad \forall m, \tag {15g}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ] \right| \right| ^ {2} \geq d _ {\min} ^ {2}, \quad \forall n, m, j \neq m, \tag {15h}
$$

$$
0 \leq p _ {m} [ n ] \leq P _ {\max}, \quad \forall m, n. \tag {15i}
$$

Problem (15) is challenging to solve due to the following two main reasons. First, the optimization variables A for user scheduling and association are binary and thus (15c)-(15e) involve integer constraints. Second, even with fixed user scheduling and association, (15b) and (15h) are still nonconvex constraints with respect to UAV trajectory variables Q and/or transmit power variables P. Therefore, problem (15) is a mixed-integer non-convex problem, which is difficult to be optimally solved in general.

# III. PROPOSED ALGORITHM

To make problem (15) more tractable, we first relax the binary variables in (15e) into continuous variables, which yields the following problem

$$
\max _ {\eta , \mathbf {A}, \mathbf {Q}, \mathbf {P}} \eta \tag {16a}
$$

$$
\text { s.t. } 0 \leq \alpha_ {k, m} [ n ] \leq 1, \quad \forall k, m, n, \tag {16b}
$$

$$
(1 5 \mathrm{b}), (1 5 \mathrm{c}), (1 5 \mathrm{d}), (1 5 \mathrm{f}), (1 5 \mathrm{g}), (1 5 \mathrm{h}), (1 5 \mathrm{i}). (1 6 \mathrm{c})
$$

Such a relaxation in general implies that the objective value of problem (16) serves as an upper bound for that of problem (15). Although relaxed, problem (16) is still a non-convex optimization problem due to the non-convex constraint (15b). In general, there is no standard method for solving such nonconvex optimization problems efficiently. In the following, we propose an efficient iterative algorithm for the relaxed problem (16) by applying the block coordinate descent [30] and successive convex optimization techniques. Specifically, for given UAV trajectory Q and transmit power P, we optimize the user scheduling and association A by solving a linear programming (LP). For any given user scheduling and association A and transmit power P (UAV trajectory Q), the UAV trajectory Q (transmit power P) is optimized based on the successive convex optimization technique [16], [23]. Then, we present the overall algorithm and analytically show its convergence. Furthermore, we propose a low-complexity initialization scheme for the UAV trajectory design. Finally, we show how to reconstruct a binary solution to the original problem (15) based on the obtained solution to problem (16).

# A. User Scheduling and Association Optimization

For any given UAV trajectory and transmit power {Q, P}, the user scheduling and association of problem (16) can be optimized by solving the following problem

$$
\max _ {\eta , \mathbf {A}} \eta \tag {17a}
$$

$$
\text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \log_ {2} (1 + \gamma_ {k, m} [ n ]) \geq \eta , \quad \forall k, \tag {17b}
$$

$$
\sum_ {k = 1} ^ {K} \alpha_ {k, m} [ n ] \leq 1, \quad \forall m, n, \tag {17c}
$$

$$
\sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \leq 1, \quad \forall k, n, \tag {17d}
$$

$$
0 \leq \alpha_ {k, m} [ n ] \leq 1, \quad \forall k, m, n. \tag {17e}
$$

Since problem (17) is a standard LP, it can be solved efficiently by existing optimization tools such as CVX [31]. Furthermore, it is easy to see that the constraints (17c) and (17d) are met with equalities when the optimal solution A is attained for given {Q, P}.

# B. UAV Trajectory Optimization

For any given user scheduling and association as well as UAV transmit power {A, P}, the UAV trajectory of problem (16) can be optimized by solving the following problem

$$
\max _ {\eta , \mathbf {Q}} \eta \tag {18a}
$$

$$
\text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \log_ {2} (1 + \gamma_ {k, m} [ n ]) \geq \eta , \quad \forall k, \tag {18b}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n + 1 ] - \mathbf {q} _ {m} [ n ] \right| \right| ^ {2} \leq S _ {\max} ^ {2}, \quad n = 1, \dots , N - 1, \tag {18c}
$$

$$
\mathbf {q} _ {m} [ 1 ] = \mathbf {q} _ {m} [ N ], \quad \forall m, \tag {18d}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ] \right| \right| ^ {2} \geq d _ {\min} ^ {2}, \quad \forall n, m, j \neq m. \tag {18e}
$$

Note that problem (18) is neither a concave or quasi-concave maximization problem due to the non-convex constraints in (18b) and (18e). In general, there is no efficient method to obtain the optimal solution. In the following, we adopt the successive convex optimization technique for the trajectory optimization. To this end, $R _ { k , m } [ n ]$ , in constraints (18b) can be written as

$$
\begin{array}{l} R _ {k, m} [ n ] \\ = \log_ {2} \left(1 + \frac {\frac {p _ {m} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {m} [ n ] - \mathbf {w} _ {k} | | ^ {2}}}{\sum_ {j = 1 , j \neq m} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}}\right) \\ = \hat {R} _ {k, m} [ n ] - \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}\right), \tag {19} \\ \end{array}
$$

where

$$
\hat {R} _ {k, m} [ n ] = \log_ {2} \left(\sum_ {j = 1} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}\right). \tag {20}
$$

With (19) and (20), constraints (18b) are transformed into

$$
\frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \bigg (\hat {R} _ {k, m} [ n ]
$$

$$
- \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}\right) \geq \eta , \quad \forall k. \tag {21}
$$

Note that constraints in (21) are still non-convex. By introducing slack variables $\mathbf { S } = \{ S _ { k , j } [ n ] = | | \mathbf { q } _ { j } [ n ] - \mathbf { w } _ { k } | | ^ { 2 } , \forall ~ j \neq$ $m , j \in \mathcal { M } , k , n \}$ , problem (18) can be reformulated as

$$
\max _ {\eta , \mathbf {Q}, \mathbf {S}} \eta \tag {22a}
$$

$$
\text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \left(\hat {R} _ {k, m} [ n ] \right.
$$

$$
\left. - \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + S _ {k , j} [ n ]} + \sigma^ {2}\right)\right) \geq \eta , \quad \forall k, \tag {22b}
$$

$$
S _ {k, j} [ n ] \leq | | \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} | | ^ {2}, \quad \forall k, j \neq m, n, \tag {22c}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n + 1 ] - \mathbf {q} _ {m} [ n ] \right| \right| ^ {2} \leq S _ {\max} ^ {2}, \quad n = 1, \dots , N - 1, \tag {22d}
$$

$$
\mathbf {q} _ {m} [ 1 ] = \mathbf {q} _ {m} [ N ], \quad \forall m, \tag {22e}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ] \right| \right| ^ {2} \geq d _ {\min} ^ {2}, \quad \forall n, m, j \neq m. \tag {22f}
$$

It can be verified that without loss of optimality to problem (22), all constraints in (22c) can be met with equality, since otherwise we can always increase $S _ { k , j } [ n ]$ without decreasing the objective value. Note that in (22b), $\hat { R } _ { k , m } [ n ]$ is neither convex nor concave with respect to ${ \bf q } _ { j } [ n ]$ . While in (22c), even though $| | \mathbf { q } _ { j } [ n ] - \mathbf { w } _ { k } | | ^ { 2 }$ is convex with respect to ${ \bf q } _ { j } [ n ]$ , the resulting set is not a convex set since the superlevel set of a convex quadratic function is not convex in general. Thus, problem (22) is still a non-convex optimization problem due to the non-convex feasible set.

To tackle the non-convexity of (22b), (22c), and (22f), the successive convex optimization technique can be applied where in each iteration, the original function is approximated by a more tractable function at a given local point. Specifically, define ${ \bf Q } ^ { r } = \{ { \bf q } _ { m } ^ { r } [ n ] , \forall m , n \}$ as the given trajectory of UAVs in the r -th iteration.2 The key observation is that in (20), although $\hat { R } _ { k , m } [ n ]$ is not concave with respect to ${ \bf q } _ { j } [ n ]$ , it is convex with respect to $| | \mathbf { q } _ { j } [ n ] - \mathbf { w } _ { k } | | ^ { 2 }$ . Recall that any convex function is globally lower-bounded by its first-order Taylor expansion at any point [32]. Therefore, with given local point $\mathbf { Q } ^ { r }$ in the r -th iteration, we obtain the following lower bound for $\hat { R } _ { k , m } [ n ]$ as in [16] and [23], i.e.,

$$
\begin{array}{l} \hat {R} _ {k, m} [ n ] = \log_ {2} \left(\sum_ {j = 1} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}\right) \\ \geq \sum_ {j = 1} ^ {M} - A _ {k, j} ^ {r} [ n ] \left(\left| \left| \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} \right| \right| ^ {2} - \left| \left| \mathbf {q} _ {j} ^ {r} [ n ] - \mathbf {w} _ {k} \right| \right| ^ {2}\right) \\ + B _ {k, j} ^ {r} [ n ] \triangleq \hat {R} _ {k, m} ^ {\mathrm{lb}} [ n ], \tag {23} \\ \end{array}
$$

where $A _ { k , j } ^ { r } [ n ]$ and $B _ { k , j } ^ { r } [ n ]$ are constants that are given by

$$
A _ {k, j} ^ {r} [ n ] = \frac {\frac {p _ {j} [ n ] \rho_ {0}}{(H ^ {2} + | | \mathbf {q} _ {j} ^ {r} [ n ] - \mathbf {w} _ {k} | | ^ {2}) ^ {2}} \log_ {2} (e)}{\sum_ {l = 1} ^ {M} \frac {p _ {l} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {l} ^ {r} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}}, \quad \forall k, j, n, \tag {24}
$$

2In Section III-D, we show that $\mathbf { Q } ^ { r }$ is in fact the solution obtained from the (r − 1)th iteration.

$$
B _ {k, j} ^ {r} [ n ] = \log_ {2} \left(\sum_ {l = 1} ^ {M} \frac {p _ {l} [ n ] \rho_ {0}}{H ^ {2} + | | \mathbf {q} _ {l} ^ {r} [ n ] - \mathbf {w} _ {k} | | ^ {2}} + \sigma^ {2}\right), \quad \forall k, j, n. \tag {25}
$$

In constraints (22c), since $| | \mathbf { q } _ { j } [ n ] - \mathbf { w } _ { k } | | ^ { 2 }$ is a convex function with respect to ${ \bf q } _ { j } [ n ]$ , we have the following inequality by applying the first-order Taylor expansion at the given point ${ \bf q } _ { j } ^ { r } [ n ]$ ,

$$
\begin{array}{l} \left| \left| \mathbf {q} _ {j} [ n ] - \mathbf {w} _ {k} \right| \right| ^ {2} \geq \left| \mathbf {q} _ {j} ^ {r} [ n ] - \mathbf {w} _ {k} \right| | ^ {2} + 2 \left(\mathbf {q} _ {j} ^ {r} [ n ] - \mathbf {w} _ {k}\right) ^ {T} \\ \times (\mathbf {q} _ {j} [ n ] - \mathbf {q} _ {j} ^ {r} [ n ]), \quad \forall k, j \neq m, n. \tag {26} \\ \end{array}
$$

Similarly, by applying the first-order Taylor expansion at the given point ${ \bf q } _ { m } ^ { r } [ n ]$ and ${ \bf q } _ { j } ^ { r } [ n ]$ to $| | \mathbf { q } _ { m } [ n ] - \mathbf { q } _ { j } [ n ] | | ^ { 2 }$ , we obtain

$$
\begin{array}{l} \left. \right.\left|\left| \mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ] \right|\right| ^ {2} \geq - \left|\left| \mathbf {q} _ {m} ^ {r} [ n ] - \mathbf {q} _ {j} ^ {r} [ n ] \right|\right| ^ {2} + 2 \left(\mathbf {q} _ {m} ^ {r} [ n ] - \mathbf {q} _ {j} ^ {r} [ n ]\right) ^ {T} \\ \times (\mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ]), \quad \forall j \neq m, n. \tag {27} \\ \end{array}
$$

With any given local point $\mathbf { Q } ^ { r }$ as well as the lower bounds in (23) and (26), problem (22) is approximated as the following problem

$$
\max _ {\eta_ {\mathrm{trj}} ^ {r}, \mathbf {Q}, \mathbf {S}} \eta_ {\mathrm{trj}} ^ {r} \tag {28a}
$$

$$
\text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \left(\hat {R} _ {k, m} ^ {\mathrm{lb}} [ n ] \right.
$$

$$
- \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} \frac {p _ {j} [ n ] \rho_ {0}}{H ^ {2} + S _ {k , j} [ n ]} + \sigma^ {2}\right) \geq \eta_ {\mathrm{trj}} ^ {r}, \quad \forall k, \tag {28b}
$$

$$
\begin{array}{l} S _ {k, j} [ n ] \leq | | \mathbf {q} _ {j} ^ {r} [ n ] - \mathbf {w} _ {k} | | ^ {2} + 2 (\mathbf {q} _ {j} ^ {r} [ n ] - \mathbf {w} _ {k}) ^ {T} \\ \times (\mathbf {q} _ {j} [ n ] - \mathbf {q} _ {j} ^ {r} [ n ]), \quad \forall k, j \neq m, n, \tag {28c} \\ \end{array}
$$

$$
\left| \left| \mathbf {q} _ {m} [ n + 1 ] - \mathbf {q} _ {m} [ n ] \right| \right| ^ {2} \leq S _ {\max} ^ {2}, \quad n = 1, \dots , N - 1, \tag {28d}
$$

$$
\mathbf {q} _ {m} [ 1 ] = \mathbf {q} _ {m} [ N ], \quad \forall m, \tag {28e}
$$

$$
d _ {\min} ^ {2} \leq - | | \mathbf {q} _ {m} ^ {r} [ n ] - \mathbf {q} _ {j} ^ {r} [ n ] | | ^ {2}
$$

$$
+ 2 \left(\mathbf {q} _ {m} ^ {r} [ n ] - \mathbf {q} _ {j} ^ {r} [ n ]\right) ^ {T} \left(\mathbf {q} _ {m} [ n ] - \mathbf {q} _ {j} [ n ]\right), \quad \forall n, m, j \neq m. \tag {28f}
$$

Since the left-hand-side (LHS) of the constraint (28b) is jointly concave with respect to ${ \bf q } _ { j } ^ { r } [ n ]$ and $S _ { k , j } [ n ]$ , it is convex now. Furthermore, (28d) is a convex quadratic constraint and (28c), (28e), and (28f) are all linear constraints. Therefore, problem (28) is a convex optimization problem that can be efficiently solved by standard convex optimization solvers such as CVX [32]. It is worth noting that the lower bounds adopted in (28b) and (28c) suggest that any feasible solution of problem (28) is also feasible for problem (22), but the reverse does not hold in general. As a result, the optimal objective value obtained from the approximate problem (28) in general serves as a lower bound of that of problem (22).

# C. UAV Transmit Power Control

For any given user scheduling and association as well as UAV trajectory {A, Q}, the UAV transmit power of problem (16) can be optimized by solving the following problem

$$
\max _ {\eta , \mathbf {P}} \eta \tag {29a}
$$

$$
\text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \log_ {2} (1 + \gamma_ {k, m} [ n ]) \geq \eta , \quad \forall k, \tag {29b}
$$

$$
0 \leq p _ {m} [ n ] \leq P _ {\max}, \quad \forall m, n. \tag {29c}
$$

Problem (29) is a non-convex optimization problem due to the non-convex constraint (29b) and in fact NP-hard for general N. Note that the LHS of (29b), i.e., $R _ { k , m } [ n ]$ , can be written as a difference of two concave functions with respect to the power control variables, i.e.,

$$
\begin{array}{l} R _ {k, m} [ n ] = \log_ {2} \left(1 + \frac {p _ {m} [ n ] h _ {k , m} [ n ]}{\sum_ {j = 1 , j \neq m} ^ {M} p _ {j} [ n ] h _ {k , j} [ n ] + \sigma^ {2}}\right) \\ = \log_ {2} \left(\sum_ {j = 1} ^ {M} p _ {j} [ n ] h _ {k, j} [ n ] + \sigma^ {2}\right) - \check {R} _ {k, m} [ n ], \tag {30} \\ \end{array}
$$

where

$$
\check {R} _ {k, m} [ n ] = \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} p _ {j} [ n ] h _ {k, j} [ n ] + \sigma^ {2}\right). \tag {31}
$$

To handle the non-convex contraint of (29b), we apply the successive convex optimization technique to approximate $\check { R } _ { k , m } [ n ]$ with a convex function in each iteration. Specifically, define ${ { \bf { P } } ^ { r } } = \{ { \bf { p } } _ { m } ^ { r } [ n ] , \forall m , n \}$ as the given transmit power of UAV m in the r-th iteration. Recall that any concave function is globally upper-bounded by its first-order Taylor expansion at any point [32]. Thus, we have the following convex upper bound at the given local point $p _ { j } ^ { r }$ [n]

$$
\begin{array}{l} \check {R} _ {k, m} [ n ] = \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} p _ {j} [ n ] h _ {k, j} [ n ] + \sigma^ {2}\right) \\ \leq \sum_ {j = 1, j \neq m} ^ {M} D _ {k, j} [ n ] \left(p _ {j} [ n ] - p _ {j} ^ {r} [ n ]\right) \\ + \log_ {2} \left(\sum_ {j = 1, j \neq m} ^ {M} p _ {j} ^ {r} [ n ] h _ {k, j} [ n ] + \sigma^ {2}\right) \\ \triangleq \check {R} _ {k, m} ^ {\mathrm{ub}} [ n ], \tag {32} \\ \end{array}
$$

where

$$
D _ {k, j} [ n ] = \frac {h _ {k , j} [ n ] \log_ {2} (e)}{\sum_ {l = 1 , l \neq m} ^ {M} p _ {j} ^ {r} [ n ] h _ {k , l} [ n ] + \sigma^ {2}}, \quad \forall k, j, n. \tag {33}
$$

With any given local point $\mathbf { P } ^ { r }$ and the upper bound $\check { R } _ { k , m } ^ { \mathrm { u b } } [ n ]$ in (32), problem (29) is approximated as the following problem

$$
\max _ {\eta_ {\text { pow }} ^ {r}, \mathbf {P}} \eta_ {\text { pow }} ^ {r} \tag {34a}
$$

$$
\begin{array}{l} \text { s.t. } \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \left(\log_ {2} \left(\sum_ {j = 1} ^ {M} p _ {j} [ n ] h _ {k, j} [ n ] + \sigma^ {2}\right) \right. \\ \left. - \check {R} _ {k, m} ^ {\mathrm{ub}} [ n ]\right) \geq \eta_ {\text { pow }} ^ {r}, \quad \forall k, \tag {34b} \\ \end{array}
$$

Algorithm 1 Block Coordinate Descent Algorithm for Problem (16)

1: Initialize $\mathbf { Q } ^ { 0 }$ and $\mathbf { P } ^ { 0 } .$ . Let $r = 0 .$ .   
2: repeat   
3: Solve problem (17) for given $\{ \mathbf { Q } ^ { r } , \mathbf { P } ^ { r } \}$ , and denote the optimal solution as $\{ { \bf A } ^ { r + 1 } \}$ .   
4: Solve problem (28) for given $\{ \mathbf { A } ^ { r + 1 } , \mathbf { Q } ^ { r } , \mathbf { P } ^ { r } \}$ , and denote the optimal solution as $\{ \mathbf { Q } ^ { r + 1 } \}$ .   
5: Solve problem (34) for given $\{ \mathbf { A } ^ { r + 1 } , \mathbf { Q } ^ { r + 1 } , \mathbf { P } ^ { r } \}$ , and denote the optimal solution as $\{ { \bf P } ^ { r + 1 } \}$ .   
6: Update $r = r + 1 .$   
7: until The fractional increase of the objective value is below a threshold $\epsilon > 0 .$

$$
0 \leq p _ {m} [ n ] \leq P _ {\max}, \quad \forall m, n. \tag {34c}
$$

Problem (34) is a convex optimization problem, which can be efficiently solved by standard convex optimization solvers such as CVX [32]. It is also worth noting that the upper bound adopted in (34b) suggests that the feasible set of problem (34) is always a subset of that of problem (29). Therefore, the optimal objective value obtained from problem (34) in general serves as a lower bound of that of problem (29).

# D. Overall Algorithm and Convergence

Based on the results presented in the previous three subsections, we propose an overall iterative algorithm for problem (16) by applying the block coordinate descent method [33], also known as the alternating optimization method. Specifically, the entire optimization variables in original problem (16) are partitioned into three blocks, i.e., {A, Q, P}. Then, the user scheduling and association A, UAV trajectory Q, and transmit power P are alternately optimized, by solving problem (17), (28), and (34) correspondingly, while keeping the other two blocks of variables fixed. Furthermore, the obtained solution in each iteration is used as the input of the next iteration. The details of this algorithm are summarized in Algorithm 1. It is worth pointing out that in the classical block coordinate descent method, the sub-problem for updating each block of variables is required to be solved exactly with optimality in each iteration in order to guarantee the convergence [33]. However, in our case, for the trajectory optimization problem (18) and transmit power optimization problem (29), we only solve their approximate problems (28) and (34) optimally. Thus, the convergence analysis for the classical coordinate descent method cannot be directly applied and the convergence of Algorithm 1 needs to be proved, as shown next.

Defiwhere $\eta _ { \mathrm { t r j } } ^ { \mathrm { l b } , r } ( { \bf A } , { \bf Q } , { \bf P } ) = \eta _ { \mathrm { t r i } } ^ { r }$ and tively $\eta _ { \mathrm { p o w } } ^ { \mathrm { l b } , r } ( { \bf A } , { \bf Q } , { \bf P } ) = \eta _ { \mathrm { p o w } } ^ { r }$ $\eta _ { \mathrm { t r i } } ^ { r }$ $\eta _ { \mathrm { p o w } } ^ { r }$ problem (28) and (34) based on A, Q, and P. First, in step 3 of Algorithm 1, since the optimal solution of (17) is obtained for given $\mathbf { Q } ^ { r }$ and $\mathbf { P } ^ { r }$ , we have

$$
\eta (\mathbf {A} ^ {r}, \mathbf {Q} ^ {r}, \mathbf {P} ^ {r}) \leq \eta (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r}, \mathbf {P} ^ {r}), \tag {35}
$$

where $\eta ( \mathbf { A } , \mathbf { Q } , \mathbf { P } )$ is defined prior to problem (15). Second, for given $\mathbf { A } ^ { r + 1 }$ , Qr , and $\mathbf { P } ^ { r }$ in step 4 of Algorithm 1, it follows that

$$
\begin{array}{l} \eta (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r}, \mathbf {P} ^ {r}) \stackrel {(a)} {=} \eta_ {\mathrm{trj}} ^ {\mathrm{lb}, r} (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r}, \mathbf {P} ^ {r}) \\ \stackrel {(b)} {\leq} \eta_ {\mathrm{trj}} ^ {\mathrm{lb}, r} (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r}) \\ \stackrel {(c)} {\leq} \eta (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r}), \tag {36} \\ \end{array}
$$

where (a) holds since the first-order Taylor expansions in (23) and (26) are tight at the given local points, respectively, which means that problem (28) at $\mathbf { Q } ^ { r }$ has the same objective value as that of problem (18); (b) holds since in step 4 of Algorithm 1 with the given $\mathbf { A } ^ { r + 1 }$ and $\mathbf { P } ^ { r } .$ , problem (28) is solved optimally with solution $\mathbf { Q } ^ { r + 1 } ;$ (c) holds since the objective value of problem (28) is the lower bound of that of its original problem (18) at $\mathbf { Q } ^ { r + 1 }$ . The inequality in (36) suggests that although only an approximate optimization problem (28) is solved for obtaining the UAV trajectory, the objective value of problem (18) is still non-decreasing after each iteration. Third, for given $\mathbf { A } ^ { r + 1 }$ , $\mathbf { Q } ^ { r + 1 }$ , and $\mathbf { P } ^ { r }$ in step 5 of Algorithm 1, it follows that

$$
\begin{array}{l} \eta (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r}) = \eta_ {\text { pow }} ^ {\text { lb }, r} (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r}) \\ \leq \eta_ {\text { pow }} ^ {\text { lb }, r} (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r + 1}) \\ \leq \eta (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r + 1}), \tag {37} \\ \end{array}
$$

which can be similarly shown as in (36). Based on (35)–(37), we obtain

$$
\eta (\mathbf {A} ^ {r}, \mathbf {Q} ^ {r}, \mathbf {P} ^ {r}) \leq \eta (\mathbf {A} ^ {r + 1}, \mathbf {Q} ^ {r + 1}, \mathbf {P} ^ {r + 1}), \tag {38}
$$

which indicates that the objective value of problem (16) is non-decreasing after each iteration of Algorithm 1. Since the objective value of problem (16) is upper bounded by a finite value, the proposed Algorithm 1 is guaranteed to converge. Simulation results in Section IV show that the proposed block coordinate descent method converges quickly for our considered setup. Furthermore, since only convex optimization problems need to be solved in each iteration of Algorithm 1, which are of polynomial complexity, Algorithm 1 can be practically implemented with fast convergence for wireless networks of a moderate number of users.

Note that in Algorithm 1, the UAV trajectory has to be initialized. It is known that for such iterative algorithms, the converged solution and the ultimate system performance in general depend on the initialization schemes. Thus, we further propose an efficient trajectory initialization scheme, which is elaborated in the next subsection.

# E. Trajectory Initialization Scheme

In this subsection, we propose a low-complexity and systematic initialization scheme for the trajectory design in Algorithm 1 based on the simple circular trajectory and the circle packing scheme. Specifically, the initial trajectory of each UAV is set to be a circular trajectory with the UAV speed taking a constant value V , with $0 ~ < ~ V ~ \leq ~ V _ { \mathrm { m a x } } .$ Furthermore, the radius of the initial trajectory circles are assumed to be the same for all UAVs. The center and radius of the circular trajectories are denoted by ${ \bf c } _ { \mathrm { t r j } } ^ { m } = [ x _ { \mathrm { t r j } } ^ { m } , y _ { \mathrm { t r j } } ^ { m } ] ^ { T }$ and $r _ { \mathrm { t r j } }$ , respectively. Thus, for any given period T , we have $2 \pi r _ { \mathrm { t r j } } = V T$ . Intuitively, circles that correspond to the initial trajectories of different UAVs should be sufficiently separated to minimize the co-channel interference, and at the same time, all circles together should cover the entire area as much as possible so as to better balance the users’ rates. Therefore, the initial circular trajectories are obtained based on circle packing. To this end, we first determine the geometric center of users as $\begin{array} { r } { \mathbf { c } _ { \mathrm { g } } = \frac { \sum _ { k = 1 } ^ { K } \mathbf { w } _ { k } } { K } } \end{array}$ Kk=1 wkK . The radius of the minimum circle with $\mathbf { c } _ { \mathrm { g } }$ as the circle center which can cover all users is denoted by $r _ { \mathrm { u } } ,$ , which is equal to the maximum distance between $\mathbf { c } _ { \mathrm { g } }$ and all the users, i.e., $r _ { \mathrm { u } } = \operatorname* { m a x } _ { k \in \mathcal { K } } | | \mathbf { w } _ { k } - \mathbf { c } _ { \mathrm { g } } | |$ |. Given the number of UAVs M and $r _ { \mathrm { u } } .$ K, we exploit the circle packing (CP) scheme [34], also known as point packing, to obtain the center of each of the M circles ${ \bf c } _ { \mathrm { t r j } } ^ { m }$ as well as the corresponding radius $r ^ { \mathrm { c p } }$ . To balance the number of users inside and outside the circular trajectory, $\frac { r ^ { \mathrm { c p } } } { 2 }$ is a reasonable choice for the trajectory circle radius. However, due to the maximum UAV speed constraint, the resulting radius $\frac { r ^ { \mathrm { c p } } } { 2 }$ may not be always achievable given the finite time T if $\pi \tilde { r ^ { \mathrm { c p } } } > V _ { \mathrm { m a x } } T$ . In this case, the maximum allowed radius is computed as

![](images/6c09373b3445a901807f63f2fcdab331c4b93dff9dbd86b985a526fbc66ab5f0.jpg)

<details>
<summary>text_image</summary>

r_u
r_{tr}
c_{trj}^m
r_{cp}
</details>

Fig. 2. An example of UAV trajectories initialization based on circle packing for M = 2 (left) and M = 3 (right). The black dots and the dashed blue circles are the results obtained from the circle packing scheme. The solid red circles are the initial circular trajectories of UAVs.

$$
r _ {\max} = \frac {V _ {\max} T}{2 \pi}. \tag {39}
$$

As such, the radius of the initial circular trajectory is set as $r _ { \mathrm { t r j } } =$ min $( r _ { \operatorname* { m a x } } , \frac { r _ { \mathrm { c p } } } { 2 } )$ . Let $\begin{array} { l } { { \theta _ { n } } } \end{array} \triangleq 2 \pi \frac { ( n - 1 ) } { N - 1 }$ (n−1)N−1 ∀ n, and Q0 = , ${ \bf Q } ^ { 0 } =$ $\{ \mathbf { q } _ { m } ^ { 0 } [ n ] , \forall m , n \}$ . Based on ${ \bf c } _ { \mathrm { t r i } } ^ { m }$ and $r _ { \mathrm { t r j } }$ , the initial trajectory of UAV m in time slot n is then obtained as

$$
\mathbf {q} _ {m} ^ {0} [ n ] = \left[ x _ {\mathrm{trj}} ^ {m} + r _ {\mathrm{trj}} \cos \theta_ {n}, y _ {\mathrm{trj}} ^ {m} + r _ {\mathrm{trj}} \sin \theta_ {n} \right] ^ {T}, \quad n = 1, \dots , N. \tag {40}
$$

Note that for $M \ \geq \ 2 .$ , if the inter-UAV distance is larger than or equal to $d _ { \mathrm { m i n } }$ , then the trajectory obtained in (40) is feasible for original problem (15). Otherwise, a feasible initial trajectory can be always obtained by scaling $r _ { \mathrm { u } }$ such that $r _ { \mathrm { c p } }$ is larger than or equal to $d _ { \mathrm { m i n } }$ .

# F. Reconstruct the Binary User Scheduling and Association Solution

Note that Algorithm 1 is to solve the relaxed problem (16) where the binary user scheduling and association variables in the original problem (15) are relaxed to continuous variables between 0 and 1. Thus, in the solution obtained by Algorithm 1, if the user scheduling and association variables $\alpha _ { k , m } [ n ]$ are all binary, then the relaxation is tight and the obtained solution is also a feasible solution of problem (15). Otherwise, the binary user scheduling and association solution needs to be reconstructed based on the solution obtained for (16). To this end, we further divide each time slot into τ sub-slots so that the new total number of sub-slots is $N ^ { \prime } = \tau N .$ , $\tau \geq 1$ . Then, the number of sub-slots assigned to user k by UAV m in time slot n is $N _ { k , m } [ n ] = \lfloor \tau \alpha _ { k , m } [ n ] \rceil$ , where 	x denotes the nearest integer of x . It is not difficult to see that as τ increases, $N _ { k , m } [ n ]$ approaches an integer which allows a binary solution. For example, consider a single-UAV enabled two-user system with $\alpha _ { 1 } [ \ell ] = 0 . 6 9$ and $\alpha _ { 2 } [ \ell ] = 0 . 3 1$ in time slot , where the UAV index is dropped for convenience. If $\tau = 1 .$ , we have $N _ { 1 } [ \ell ] = \lfloor 0 . 6 9 \rfloor = 1$ and $N _ { 2 } [ \ell ] = \lfloor 0 . 3 1 \rceil = 0 \mathrm { . }$ , respectively. If each time slot is further divided into 10 subslots, i.e., $\tau \ = \ 1 0$ , then $N _ { 1 } [ \ell ] = \lfloor 6 . 9 \rceil = 7$ and $N _ { 2 } [ \ell ] =$ $\lfloor 3 . 1 \rceil = 3 .$ , respectively. Although such a rounding still causes a performance gap, the gap decreases as the duration of the sub-slot decreases. Alternatively, if each time slot is divided into 100 sub-slots, i.e., $\tau ~ = ~ 1 0 0$ , user 1 and user 2 will be assigned 69 and 31 sub-slots, respectively, i.e., $N _ { 1 } [ \ell ] =$ $\lfloor 6 9 \rceil ~ = ~ 6 9$ and $N _ { 2 } [ \ell ] ~ = ~ \lfloor 3 1 \rceil ~ = ~ 3 1$ , which permits a binary solution with zero relaxation gap. Furthermore, since constraints (17c) and (17d) are met with equalities in the optimal solution to problem (17), a binary solution for the case of multiple UAVs can be easily reconstructed by applying the above procedure.

It is worth pointing out that such a reconstructed binary solution is always feasible for problem (15) with the same larger $N ^ { \prime }$ slots, while we do not need to resolve problem (15) with $N ^ { \prime } \ > \ N$ directly to avoid high computational complexity. Thus, the complexity of our proposed approach is lower compared to that of directly solving problem (15) with $N ^ { \prime }$ slots. On the other hand, the case of $\tau = 1$ which directly rounds off the continuous variables to binary ones, is a special case of the proposed scheme but at the expense of certain performance loss in general. Therefore, our proposed scheme not only ensures to obtain a feasible solution to problem (15) with any given N slots, but also can achieve higher accuracy and better performance by using $N ^ { \prime } \ > \ N$ slots yet without increasing the complexity. In other words, if the number of time slots N  is set very large initially, then directly solving problem (15) with $N ^ { \prime }$ will incur very high complexity. In this case, we can first formulate and solve the problem with a smaller $N = N ^ { \prime } / \tau$ by choosing a suitable $\tau > 1$ (note that τ cannot be set too large as this may render the discrete-time approximation of the UAV trajectory inaccurate), and then use our results to construct a feasible solution to problem (15) with the larger number of times slots $N ^ { \prime }$ , to achieve lower complexity.

# IV. NUMERICAL RESULTS

In this section, we provide numerical examples to demonstrate the effectiveness of the proposed algorithm. We consider a system with $K = 6$ ground users that are randomly and uniformly distributed within a 2D area of $2 \times 2 ~ \mathrm { k m } ^ { 2 }$ . The following results are obtained based on one random realization of the user locations as shown in Fig. 3. All the UAVs are assumed to fly at a fixed altitude $H ~ = ~ 1 0 0$ m. The receiver noise power is assumed to be $\sigma ^ { 2 } = - 1 1 0$ dBm. The channel power gain at the reference distance $d _ { 0 } = 1$ m is set as $\rho _ { 0 } = - 6 0$ dB. The maximum transmit power and the maximum speed of UAVs are assumed as $P _ { \operatorname* { m a x } } = 0 . 1 ~ \mathrm { W }$ and $V _ { \mathrm { m a x } } = 5 0 ~ \mathrm { m / s } ,$ respectively. The threshold 	 in Algorithm 1 is set as $1 0 ^ { - 4 }$ . The transmit power of the UAVs is initialized by the maximum transmit power, i.e., $p _ { m } [ n ] = P _ { \mathrm { m a x } }$ , ∀ m. Other parameters are set as $d _ { \operatorname* { m i n } } = 1 0 0$ m and $\tau = 1 0 0$ .

![](images/e2c43e2a334f0a3a3b449bef3b9bd70eb75e0c1317be59a855aedfd50c7e642c.jpg)

<details>
<summary>line</summary>

| Time (s) | x (m) | y (m) |
|----------|-------|-------|
| 30       | -1000 | 500   |
| 30       | -800  | 400   |
| 30       | -600  | 300   |
| 30       | -400  | 200   |
| 30       | -200  | 100   |
| 30       | 0     | 0     |
| 30       | 200   | -100  |
| 30       | 400   | -200  |
| 30       | 600   | -300  |
| 30       | 800   | -400  |
| 60       | -1000 | 550   |
| 60       | -800  | 500   |
| 60       | -600  | 450   |
| 60       | -400  | 400   |
| 60       | -200  | 350   |
| 60       | 0     | 300   |
| 60       | 200   | 250   |
| 60       | 400   | 200   |
| 60       | 600   | 150   |
| 60       | 800   | 100   |
| 175      | -800  | -650  |
| 175      | -600  | -650  |
| 175      | -400  | -650  |
| 175      | -200  | -650  |
| 175      | 0     | -650  |
| 175      | 200   | -650  |
| 175      | 400   | -650  |
| 175      | 600   | -650  |
| 175      | 800   | -650  |
| 210      | -800  | -650  |
| 210      | -600  | -650  |
| 210      | -400  | -650  |
| 210      | -200  | -650  |
| 210      | 0     | -650  |
| 210      | 200   | -650  |
| 210      | 400   | -650  |
| 210      | 600   | -650  |
| 210      | 800   | -650  |
|          | -1200 |         |
|          | -1444 |         |
|          | -849   |         |
|          | -449   |         |
|          | -249   |         |
|          | 249    |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |                 |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
|          |           |         |
| T=35     | -849   |         |
| T=35     | -649   |         |
| T=35     | -449   |         |
| T=35     | -249   |         |
| T=35     | 249    |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            |         |
| T=35     |            =775*|
| T=35     |            =849*|
| T=35     |            =849*|
| T=35     |            =849*|
| T=35     |            =849*|
| T=35     |            =849*|
| T=35     |            =849*|
| T=35     |            =849*|
| T=35     |            =849*|
</details>

Fig. 3. Optimized UAV trajectories for different periods T for a single-UAV system. Each trajectory is sampled every 5 s and the sampled points are marked with ‘’ by using the same colors as their corresponding trajectories. The user locations are marked by Blue circles ‘’.

# A. Singe UAV Case

We first consider the special case with one single UAV, i.e., $M \ = \ 1$ , where there is no co-channel interference in the system. It is not difficult to see that in this case, the UAV should always transmit with its maximum power, $\mathrm { i . e . , ~ } p [ n ] = P _ { \mathrm { m a x } } , \forall n$ . Then, problem (15) is simplified to a joint user scheduling and UAV trajectory optimization problem that can be solved by a slight modification of Algorithm 1. In Fig. 3, we illustrate the optimized trajectories obtained by the proposed Algorithm 1 under different periods T . It is observed that as T increases, the UAV exploits its mobility to adaptively enlarge and adjust its trajectory to move closer to the ground users. When T is sufficiently large, e.g., $T = 2 1 0 \ { \mathrm { s } } .$ , the UAV is able to sequentially visit all the users and stay stationary above each of them for a certain amount of time (i.e., with a zero speed), while the UAV trajectory becomes a closed loop with segments connecting all the points right on top of the user locations. Except the time spent on traveling between the user locations, the UAV sequentially hovers above the users so as to enjoy the best communication channels. For example, for the case of $T = 2 1 0 ~ \mathrm { s }$ , it can be observed that the sampled points on the trajectory around each user have higher densities than those far way from the users. This means that when the UAV flies close to each user, it will reduce the speed accordingly such that more information can be transmitted over a better air-to-ground channel. This phenomenon can be more directly observed from Fig. 4 for the case of $T = 2 1 0 \mathrm { ~ s ~ }$ , where the UAV speed reduces to zero when it flies right above each user, such as $t = 3 5 \mathrm { ~ s ~ }$ . While for $T = 3 0$ and 60 s, the UAV always flies at the maximum speed $V _ { \mathrm { m a x } }$ in order to get as close to

![](images/b5a9c3d0d051ea45f448da9cb8ffc33498b6fb58343a7d5c384ed76bd2231fd2.jpg)

<details>
<summary>line</summary>

| Time t (s) | UAV speed (m/s) |
| ---------- | --------------- |
| 0          | 0               |
| 35         | 50              |
| 70         | 0               |
| 105        | 50              |
| 140        | 0               |
| 175        | 50              |
| 210        | 0               |
</details>

Fig. 4. The UAV speed versus time for $T = 2 1 0 \mathrm { ~ s ~ }$

each user as possible for shorter LoS links within each limited period T .

In Fig. 5, we compare the average max-min rate achieved by the following schemes: 1) Proposed trajectory, which is obtained by Algorithm 1; 2) Circular trajectory, which is obtained by the proposed initialization scheme with $M = 1 ;$ and 3) Static UAV, where the UAV is placed at the geometric center of the user positions and remains static during the whole period T . For all the three schemes, the user scheduling is optimized by Algorithm 1 with given trajectory. It is observed from Fig. 5 that the max-min rate of the static UAV is independent of T since without mobility, the channel links between the UAV and users are time-invariant. In contrast, for the proposed trajectory and the circular trajectory schemes, the max-min rate increases with T and eventually becomes saturated when T is sufficiently large. This is expected since with the UAV mobility, a larger T provides the UAV more time to fly closer to the users to be served, which thus improves the max-min rate. In addition, when T and/or $V _ { \mathrm { m a x } }$ is sufficiently large such that the UAV’s travelling time between users is negligible, each ground user is sequentially served with equal time duration when the UAV is directly on top of it. In this case, the max-min rate for each user can be obtained as

$$
R ^ {\mathrm{ub}} = \frac {1}{K} \log_ {2} \left(1 + \frac {P \rho_ {0}}{H ^ {2} \sigma^ {2}}\right) = 1. 6 6 1 2 \mathrm{bps/Hz}. \tag {41}
$$

It is worth pointing out that since the travelling time in practice is always not negligible for any finite UAV speed, the maximum objective value of problem (15) is strictly upperbounded by the rate in (41). As the obtained trajectory by our proposed algorithm is able to move the UAV to be above of each user, the asymptotic optimality of the proposed algorithm can be demonstrated with increasing T , which can be seen in Fig. 5. In Fig. 6, we plot the access delay for two of the users versus the period T based on the optimized user scheduling variables. One can observe that as T increases, the user access delay also increases, which implies that each user needs to wait for a longer time to be scheduled for communication with the UAV. Based on Figs. 5 and 6, the fundamental delaythroughput tradeoff is demonstrated.

By comparing the performance of the proposed trajectory with that of the circular trajectory in Fig. 5, the advantage of fully exploiting the trajectory design is also demonstrated. Since the circular trajectory restricts the UAV to fly along a circle, the users that are not around the circle suffer from worse channels. As a result, more time needs to be assigned to those users, which poses the bottleneck for the achievable max-min throughput. While for the proposed trajectory with a sufficiently large period T , the UAV is able to fly closer to or even stays stationary above all users to serve them with better channels. Therefore, the max-min throughput is improved, but at the cost of longer access delay on average for the users.

![](images/24cf1a0199b7cbc36dfc74687dc87fab5390334669b676b3cfa7b81b5333eb62.jpg)

<details>
<summary>line</summary>

| Period T (s) | Upper bound | Proposed trajectory | Circular trajectory | Static UAV |
| ------------ | ----------- | ------------------- | ------------------- | ---------- |
| 0            | 1.7         | 0.7                 | 0.7                 | 0.65       |
| 100          | 1.7         | 1.1                 | 0.9                 | 0.65       |
| 200          | 1.7         | 1.35                | 0.9                 | 0.65       |
| 300          | 1.7         | 1.45                | 0.9                 | 0.65       |
| 400          | 1.7         | 1.5                 | 0.9                 | 0.65       |
| 500          | 1.7         | 1.52                | 0.9                 | 0.65       |
| 600          | 1.7         | 1.55                | 0.9                 | 0.65       |
| 700          | 1.7         | 1.57                | 0.9                 | 0.65       |
| 800          | 1.7         | 1.58                | 0.9                 | 0.65       |
</details>

Fig. 5. Max-min rate versus period T for a single-UAV system with different trajectory designs.

![](images/09fef003c34c3547727b80d8b28805175365c92ff2ff3cce7a23a7541f991288.jpg)

<details>
<summary>line</summary>

| Iteration number | Max-min rate (bps/Hz) |
| ---------------- | --------------------- |
| 0                | 1.0                   |
| 5                | 1.3                   |
| 10               | 1.5                   |
| 15               | 1.65                  |
| 20               | 1.75                  |
| 25               | 1.8                   |
| 30               | 1.82                  |
| 35               | 1.83                  |
| 40               | 1.84                  |
| 45               | 1.85                  |
| 50               | 1.85                  |
| 55               | 1.85                  |
| 60               | 1.85                  |
| 65               | 1.85                  |
| 70               | 1.85                  |
</details>

Fig. 7. Convergence behaviour of the proposed Algorithm 1.

![](images/ad21df1a1c02e588e4fa82d50e0dcd24c37bf3987e407484d22aa9e199560ffe.jpg)

<details>
<summary>line</summary>

| Period T (s) | User 1 | User 2 |
| ------------ | ------ | ------ |
| 30           | 25     | 25     |
| 60           | 50     | 45     |
| 90           | 75     | 70     |
| 120          | 100    | 95     |
| 150          | 125    | 120    |
| 180          | 150    | 145    |
| 210          | 175    | 170    |
| 240          | 200    | 195    |
| 270          | 225    | 220    |
| 300          | 250    | 245    |
</details>

Fig. 6. User access delay versus period T for a single-UAV system. The locations of users 1 and 2 are [−419, 400] T and [600, 1130] T in m, respectively, which are shown in Fig. 3.

![](images/f88dfcee648b2b40336ed1267fbb193fb7e6b5412a65e752547705472ae28ec5.jpg)

<details>
<summary>line</summary>

| Period T (s) | Scheme I | Scheme II | Scheme III |
| ------------ | -------- | --------- | ---------- |
| 0            | 0.8      | 0.8       | 0.8        |
| 30           | 1.1      | 1.0       | 1.0        |
| 60           | 1.6      | 1.4       | 1.0        |
| 90           | 1.9      | 1.7       | 1.0        |
| 120          | 2.0      | 1.8       | 1.0        |
| 150          | 2.0      | 1.85      | 1.0        |
</details>

Fig. 8. Max-min rate versus period T for a two-UAV system with different optimization schemes.

# B. Multi-UAVs Case

Next, we study the max-min throughput of the multi-UAV network. Before the performance comparison, we show the convergence behaviour of the proposed Algorithm 1 in Fig. 7 for the case of two UAVs under T = 90 s. It can be observed from the figure that the max-min rate achieved by the proposed algorithm increases quickly with the number of iterations and the algorithm converges in about 40 iterations.

In order to show the performance gain brought by the optimization of the different design variables in Algorithm 1, in Fig. 8, we compare the following three schemes for a two-UAV network, namely, 1) Scheme I: All variables are jointly optimized as in Algorithm 1; 2) Scheme II: Jointly optimized user scheduling and association as well as UAV trajectory but with full transmit power (i.e., no transmit power control); and 3) Scheme III: Optimized user scheduling and association but with simple circular trajectory and full transmit power of UAVs. Several important observations can be made from Fig. 8. First, as expected, the max-min rates of all the three schemes increase as the period T becomes large. Second, the performance gap between Scheme II and Scheme III demonstrates the throughput gain brought by the proposed trajectory design even without transmit power control applied, and the performance gap between the two schemes increases with increasing T . This is because with larger T , the optimization of UAVs’ trajectories becomes more crucial for both achieving better direct links and avoiding severe co-channel interference links, especially when there is no transmit power control applied, whereas restricting the UAVs flying along circles limits the potential of UAV mobility. Second, by comparing Scheme I and Scheme II, the additional gain of power control is also demonstrated. When the power control can be optimized, it also provides more flexibility for designing UAVs’ trajectories, which helps achieve better user rates. Last but not the least, by comparing Scheme I and its counterpart for the case of a single UAV in Fig. 5, it is observed that the user access delay is significantly reduced by employing two UAVs to serve users jointly. For example, to achieve the same average max-min rate about 1.60 bps/Hz, a single-UAV system requires more than $T = 8 0 0 \mathrm { ~ s ~ }$ as shown in Fig. 5, whereas this value dramatically reduces to about $T = 7 0$ s for a two-UAV system, both applying the proposed Algorithm 1. Such a performance gain is mainly attributed to two facts. On one hand, the spectrum efficiency is improved by allowing concurrent transmissions of the two UAVs with the same power budget. In fact, this can be directly observed by comparing the upper bound of the max-min rate for a single-UAV system which is 1.6612 bps/Hz given in (41) with the achievable max-min rate of the two-UAV system which is more than 2.00 bps/Hz as shown in Fig. 8. On the other hand, the traveling time of each UAV over its served ground users is reduced and the average air-to-ground channels are also improved when the number of UAVs increases, which saves more time for them to stay above each user to maintain the best LoS channels. In summary, the above observations demonstrate the effectiveness of employing multiple UAVs for improving the user throughput and/or reducing the access delay, which thus improves the fundamental throughput-access delay tradeoff.

![](images/8898ce210277968851cff05a970a0e9a1e06cadaf6727cd6d6ce04afc75045ee.jpg)

<details>
<summary>line</summary>

| t     | x (m)   | y (m)   |
|-------|---------|---------|
| 80 s  | -1100   | 550     |
| 80 s  | -700    | 400     |
| 80 s  | -1100   | -600    |
| 20 s  | 300     | 250     |
| 20 s  | 700     | 1100    |
| 20 s  | 1100    | -400    |
| 40 s  | -1100   | 550     |
| 40 s  | -700    | -600    |
| 40 s  | -1100   | 400     |
| 60 s  | -1100   | 550     |
| 60 s  | -700    | -600    |
| 60 s  | -1100   | 400     |
| 80 s  | -700    | -600    |
| 80 s  | -1100   | 450     |
| 80 s  | -1100   | -650    |
| 80 s  | -700    | -650    |
| 80 s  | -1100   | -650    |
| 80 s  | -700    | -650    |
| 80 s  | -1100   | -650    |
| 80 s  | -700    | -650    |
| 80 s  | -1100   | -650    |
|
| 80 s  | -700    | -650    |
| 80 s  | -1100   | -650    |
| 80 s  | -700    | -650    |
| 80 s  | -1100   | -650    |
| 80 s  | -700    | -650    |
| 2 s   | -1100   | 550     |
| 2 s   | -700    | -65      |
| 2 s   | -1100   | 45      |
| 2 s   | -700    | -45      |
| 2 s   | -1100   | -45      |
| 2 s   | -700    | -45      |
| 2 s   | -1100   | -45      |
| 2 s   | -700    | -45      |
| 2 s   | -1100   | -45      |
| 2 s   | -700    | -45      |
| 2 s   | -1355   | 55      |
| 2 s   | -755    | -65      |
| 2 s   | -1355   | 45      |
| 2 s   | -755    | -45      |
| 2 s   | -1355   | -45      |
| 2 s   | -755    | -45      |
| 2 s   | -1355   | -45      |
| 2 s   | -755    | -45      |
| 2 s   | -1355   | -45      |
| 2 s   | -755    | -45      |
| 2 s   | -1157.5 | 55      |
| 2 s   | -777.5  | -65      |
| 2 s   | -1177.5 | 45      |
| 2 s   | -777.5  | -45      |
| 2 s   | -1177.5 | -45      |
| 2 s   | -777.5  | -45      |
| 2 s   | -1177.5|
</details>

(a) Optimized UAV trajectories without power control.

![](images/998a8c85a51392a6e2c02aad0741a250bca06eddc75f57343dac4c3615ebeb5e.jpg)  
(b) Optimized UAV trajectories with power control.   
Fig. 9. Trajectory comparison for a two-UAV system when $T = 9 0 \ { \mathrm { s . } }$ The initial locations of trajectories are marked with blue square ‘-’. Black arrows represent the directions of the trajectories. Each trajectory is sampled every 5 s and the sampling points are marked with ‘’s by using the same colors as their corresponding trajectories.

In Fig. 9, we compare the optimized UAV trajectories obtained by Schemes I and II with the period $T ~ = ~ 9 0 ~ \mathrm { ~ s ~ }$ . It can be observed from Fig. 9 (a) that for Scheme II without power control, i.e., when the maximum transmit power is used by both UAVs, the trajectories of the two UAVs tend to keep away from each other as far as possible to avoid cochannel interference. However, at some pair of UAV locations, this is realized at the cost of sacrificing favourable direct communication links, especially when they have to serve two users that are close to each other. As a result, the advantage of trajectory design is compromised so as to trade off between the direct channel and the co-channel interference. In contrast, in Fig 9 (b) for Scheme I when the transmit power is also optimized, the two UAVs can reduce the interference by properly adjusting the transmit power when they get close to each other to serve nearby users. As such, strong direct links and weak co-channel interference can be achieved at the same time, which helps unlock the potential benefit brought by the trajectory design and thereby achieves a larger maxmin rate $( R _ { k } = 1 . 8 4 3 4$ bps/Hz, ∀ k, with Scheme I versus $R _ { k } = 1 . 5 9 4 7 \mathrm { ~ b p s } / \mathrm { H z } , \forall k .$ , with Scheme II). The corresponding UAV transmit power versus time is plotted in Fig. 10. First, it can be observed that at any time instant, there is always one UAV that transmits with the maximum power. Second, when two UAVs are far away from each other, both of them tend to transmit with the maximum power so as to improve the spectrum efficiency, e.g., from $t = 1 0 \mathrm { ~ s ~ t o ~ } t = 2 0$ s where two UAVs flight towards the opposite directions. In contrast, when the two UAVs are getting very close to each other, one UAV will reduce the transmit power to zero to avoid severe interference, e.g., from $t = 4 0 \mathrm { ~ s ~ t o ~ } t = 4 5 \mathrm { ~ s ~ }$ where the two UAVs are serving the two nearby users in the center. Therefore, without power control, the communication interference can only be mitigated by adjusting the UAV trajectory, while a joint power control and trajectory design provides more flexibility to mitigate the co-channel interference and thus achieves a higher max-min rate.

![](images/1277b6679d71f924819d700d4fcbc48d764914988d4c80309cea66e361cc1814.jpg)

<details>
<summary>line</summary>

| Time t (s) | p₁    | p₂    |
| ---------- | ----- | ----- |
| 0          | 0.1   | 0.04  |
| 10         | 0.1   | 0.01  |
| 20         | 0.1   | 0.1   |
| 30         | 0.1   | 0.1   |
| 40         | 0.1   | 0.1   |
| 50         | 0.0   | 0.1   |
| 60         | 0.03  | 0.1   |
| 70         | 0.04  | 0.1   |
| 80         | 0.1   | 0.1   |
| 90         | 0.1   | 0.04  |
</details>

Fig. 10. UAV transmit power versus time for a two-UAV system.

![](images/5da1f5d0361f7b8fc2d6cee85d9b5ab9d50def0aded5c4bb7222bdb3a0084c3d.jpg)

<details>
<summary>line</summary>

| Period T (s) | Proposed trajectory | Circular trajectory | Static UAV | Orthogonal transmission |
| ------------ | ------------------- | ------------------- | ---------- | ----------------------- |
| 0            | 0.8                 | 0.8                 | 0.8        | 0.8                     |
| 30           | 1.1                 | 1.0                 | 0.8        | 0.9                     |
| 60           | 1.6                 | 1.0                 | 0.8        | 1.1                     |
| 90           | 1.9                 | 1.0                 | 0.8        | 1.3                     |
| 120          | 2.0                 | 1.0                 | 0.8        | 1.4                     |
| 150          | 2.0                 | 1.0                 | 0.8        | 1.4                     |
</details>

Fig. 11. Max-min rate versus period T for a two-UAV system with different trajectory designs and the orthogonal transmission.

In Fig. 11, we compare the average max-min rate achieved by the three trajectory designs in a two-UAV system similar to those in Fig. 5 for the single-UAV case, i.e., 1) Proposed trajectory; 2) Circular trajectory, which is obtained by the proposed initialization scheme with $M = 2 ;$ and 3) Static UAV, where each UAV m is placed at ${ \bf c } _ { \mathrm { t r j } } ^ { m }$ as in the initialization scheme and remains static for the entire T . For all the three schemes, both the user scheduling and association as well as power control are optimized by Algorithm 1 with given corresponding trajectory. In addition, an orthogonal UAV transmission scheme is also adopted for comparison. Specifically, the multiple UAVs take turns to transmit information to their served ground users over orthogonal time slots, thus the system is interference-free. This is achieved by imposing the following constraints,3

$$
\sum_ {k = 1} ^ {K} \alpha_ {k, m} [ M (\ell - 1) + m ] \leq 1, \quad \forall m, \ell = 1, \dots , \frac {N}{M}, \tag {42}
$$

$$
\sum_ {k = 1} ^ {K} \alpha_ {k, j} [ M (\ell - 1) + m ] = 0, \quad \forall j \neq m, \ell = 1, \dots , \frac {N}{M}, \tag {43}
$$

which guarantee that in each time slot, only one UAV is allowed to transmit. Accordingly, the achievable rate of user k can be expressed as

$$
\begin{array}{l} R _ {k} ^ {I I} = \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} \alpha_ {k, m} [ n ] \\ \times \log_ {2} \left(1 + \frac {p _ {m} [ n ] \rho_ {0}}{(H ^ {2} + | | \mathbf {q} _ {m} [ n ] - \mathbf {w} _ {k} | | ^ {2}) \sigma^ {2}}\right). \tag {44} \\ \end{array}
$$

Since the above case is a special case of problem (15), the corresponding problem can be solved similarly by Algorithm 1. As can be seen, the max-min rate of the static-UAV case is still regardless of the period T due to the time-invariant air-toground channels. In contrast, by exploiting the UAV mobility, the max-min rates achieved by the other two trajectory designs are non-decreasing with T , which further demonstrates the fundamental throughput-access delay tradeoff. Compared to Fig. 5 with a single UAV, it can also be observed that such a tradeoff has been significantly improved (i.e., higher maxmin rate is achieved with the same given T ) by employing more than one UAVs. In addition, compared to the orthogonal transmission scheme, the spectrum sharing gain by the two UAVs is also demonstrated.

# V. CONCLUSIONS

In this paper, we have investigated a new type of multi-UAV enabled wireless networks. Specifically, the user scheduling and association, UAV trajectories, and transmit power are jointly optimized with the objective of maximizing the minimum average rate among all users. By means of the block coordinate descent and the successive convex optimization techniques, an efficient iterative algorithm has been proposed, which is guaranteed to converge. Numerical results demonstrate that the UAV mobility provides the benefit of achieving better air-to-ground channels as well as additional flexibility for interference mitigation, and thereby improves the system throughput, compared to the conventional case with static BSs. Furthermore, the proposed trajectory design significantly outperforms the simple circular trajectory. The interesting throughput-access delay tradeoff is also shown for multi-UAV enabled communications.

3For convenience, we select the value of N such that $\textstyle { \frac { N } { M } }$ N is an integer for a given M.

Although we focus on the downlink communication scenario from the UAVs to ground users, the problem for the uplink communication scenario from ground users to the UAVs can be pursued by following a similar approach via optimizing the UAV trajectory alternately with the joint optimization of user scheduling and power control. However, how to integrate the solution of the joint optimization of user scheduling and power control into the framework of the block coordinate descent method to guarantee the convergence is challenging and needs further investigation. In addition, there are still many other interesting research directions that could be pursued in future work by extending the results of this paper, including e.g. 1) Co-existence design of a network with both aerial and ground BSs; 2) 3D UAV trajectory design with both altitude and horizontal position optimization; and 3) Energyefficient UAV trajectory design for the general multi-UAV and/or multiuser scenario by taking into account the UAV movement energy consumption [23].

# REFERENCES

[1] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for UAV-enabled multiple access,” in Proc. IEEE GLOBECOM, to be published. [Online]. Available: https://arxiv.org/abs/1704.01765   
[2] K. P. Valavanis and G. J. Vachtsevanos, Handbook of Unmanned Aerial Vehicles. Springer, 2014.   
[3] Global UAV Market. Accessed: Mar. 20, 2017. [Online]. Available: https://www.aiaa.org/Detail.aspx?id=33690   
[4] X. Lin et al. (Jul. 2017). “The sky is not the limit: LTE for unmanned aerial vehicles.” [Online]. Available: https://arxiv.org/abs/1707.07534   
[5] Facebook Takes Flight. Accessed: Apr. 10, 2017. [Online]. Available: http://www.theverge.com/a/mark-zuckerberg-future-of-facebook/aquiladrone-internet   
[6] Project Loon. Accessed: Apr. 10, 2017. [Online]. Available: https://www.google.com/loon   
[7] 3GPP: Study on Enhanced Support for Aerial Vehicles. Accessed: Apr. 10, 2017. [Online]. Available: https://lnkd.in/gR5fpdf   
[8] Paving the Path to 5G: Optimizing Commercial LTE Networks for Drone Communication. Accessed: Apr. 10, 2017. [Online]. Available: https://www.qualcomm.com/news/onq/2016/09/06/paving-path-5goptimizing-commercial-lte-networks-drone-communication   
[9] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.   
[10] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.   
[11] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647–1650, Aug. 2016.   
[12] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.   
[13] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.   
[14] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE ICC, May 2016, pp. 1–5.   
[15] P. Zhan, K. Yu, and A. L. Swindlehurst, “Wireless relay communications with unmanned aerial vehicles: Performance and optimization,” IEEE Trans. Aerosp. Electron. Syst., vol. 47, no. 3, pp. 2068–2085, Jul. 2011.   
[16] Y. Zeng, R. Zhang, and T. J. Lim, “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.   
[17] S. W. Loke. (Jul. 2015). “The Internet of flying-things: Opportunities and challenges with airborne fog computing and mobile cloud in the clouds.” [Online]. Available: https://arxiv.org/abs/1507.04492

[18] S. Jeong, O. Simeone, and J. Kang. (Sep. 2016). “Mobile edge computing via a UAV-mounted cloudlet: Optimization of bit allocation and path planning.” [Online]. Available: https://arxiv.org/abs/1609.05362   
[19] Q. Wu, G. Y. Li, W. Chen, and D. W. K. Ng, “Energy-efficient small cell with spectrum-power trading,” IEEE J. Sel. Areas Commun., vol. 34, no. 12, pp. 3394–3408, Dec. 2016.   
[20] Q. Wu, G. Y. Li, W. Chen, D. W. K. Ng, and R. Schober, “An overview of sustainable green 5G networks,” IEEE Wireless Commun., vol. 24, no. 4, pp. 72–80, Aug. 2017.   
[21] S. Zhang, Q. Wu, S. Xu, and G. Li, “Fundamental green tradeoffs: Progresses, challenges, and impacts on 5G networks,” IEEE Commun. Surveys Tuts., vol. 19, no. 1, pp. 33–56, 1st Quart., 2017.   
[22] F. Wang, W. Chen, H. Tang, and Q. Wu, “Joint optimization of user association, subchannel allocation, and power allocation in multicell multi-association OFDMA heterogeneous networks,” IEEE Trans. Commun., vol. 65, no. 6, pp. 2672–2684, Jun. 2017.   
[23] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[24] J. Lyu, Y. Zeng, and R. Zhang, “Cyclical multiple access in UAV-aided communications: A throughput-delay tradeoff,” IEEE Wireless Commun. Lett., vol. 5, no. 6, pp. 600–603, Dec. 2016.   
[25] G. Zhang, Q. Wu, M. Cui, and R. Zhang, “Securing UAV communications via trajectory optimization,” in Proc. IEEE GLOBECOM, to be published.   
[26] G. Zhang, Q. Wu, M. Cui, and R. Zhang, “Securing UAV communications via joint trajectory and power control,” IEEE Trans. Wireless Commun., submitted for publication.   
[27] Q. Wu and R. Zhang, “Delay-constrained throughput maximization in UAV-enabled OFDM systems,” in Proc. IEEE APCC, to be published.   
[28] Q. Wu and R. Zhang, “Common throughput maximization in UAVenabled OFDMA systems with delay consideration,” IEEE Trans. Commun., submitted for publication.   
[29] D. Yang, Q. Wu, Y. Zeng, and R. Zhang, “Energy tradeoff in ground-to-UAV communication via trajectory design,” IEEE Trans. Veh. Technol., submitted for publication. [Online]. Available: https://arxiv.org/abs/1709.02975   
[30] M. Hong, M. Razaviyayn, Z.-Q. Luo, and J.-S. Pang, “A unified algorithmic framework for block-structured optimization involving big data: With applications in machine learning and signal processing,” IEEE Signal Process. Mag., vol. 33, no. 1, pp. 57–77, Jan. 2016.   
[31] M. Grant and S. Boyd. (2016). CVX: MATLAB Software for Disciplined Convex Programming. [Online]. Available: http://cvxr.com/cvx   
[32] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.   
[33] D. P. Bertsekas, Nonlinear Programming. Belmont, MA, USA: Athena Scientific, 1999.   
[34] Packings of Equal Circles in Fixed-Sized Containers With Maximum Packing Density. Accessed: Apr. 5, 2017. [Online]. Available: http://www.packomania.com

![](images/22500c753c45cfb42649ba36c7844e9dd3e684d66f226f78aae5a3600e2b2eb3.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young man wearing glasses and an orange shirt, standing on a sports field with green turf (no text or symbols visible)
</details>

Qingqing Wu (S’13–M’16) received the B.Eng. degree in electronic engineering from the South China University of Technology in 2012 and the Ph.D. degree in electronic engineering from Shanghai Jiao Tong University (SJTU), China, in 2016 (in advance). From 2015 to 2016, he was a Visiting Research Scholar with the School of Electrical and Computer Engineering, Georgia Institute of Technology, Atlanta, GA, USA. His research interests include convex and nonconvex optimization, energyefficient wireless communications, wireless power

transfer, and unmanned aerial vehicle communications. He received the IEEE WCSP Best Paper Award in 2015 and the Exemplary Reviewer Award of the IEEE COMMUNICATIONS LETTERS in 2016. He was also the recipient of outstanding Ph.D. thesis funding in SJTU in 2016. He served as a TPC member for the IEEE VTC 2017 and Globecom 2016.

![](images/13cb2d908c9eab1b45aed5943120d0dbfde3f6b1f07574cf85fb8a15f84ba28b.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in a black shirt (no text or symbols visible)
</details>

Yong Zeng (S’12–M’14) received the B.E. degree (Hons.) and the Ph.D. degree from Nanyang Technological University, Singapore, in 2009 and 2014, respectively. Since 2013, he has been with the National University of Singapore, first as a Research Fellow and then as a Senior Research Fellow. He has authored 34 IEEE journal papers (16 as first author) and 22 IEEE conference papers, including one invited paper in IEEE TRANSACTIONS ON COMMUNICATIONS, four ESI highly cited papers, and two ESI hot papers. His research interests include UAV communications, wireless power transfer, massive multi-in multi-out (MIMO) and mm-wave communications for 5G, and multiuser MIMO communications. He received the 2017 IEEE Communications Society Heinrich Hertz Award, the 2015 IEEE WIRELESS COMMUNICATIONS LETTERS Exemplary Reviewer Award, and the Best Paper Award for the 10th IEEE International Conference on Information, Communications and Signal Processing. He is currently serving as an Associate Editor for the IEEE ACCESS, a Leading Guest Editor for the IEEE WIRELESS COM-MUNICATIONS Issue on Integrating UAVs into 5G and Beyond and China Communications on Network-Connected UAV Communications. He is the Workshop Co-Chair for two workshops in ICC 2018 and the 23rd Asia–Pacific Conference on Communications.

![](images/3283fa625357f152a74a7664fcefba8fe25de396dbc0de29621832d1b5cc5699.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man wearing glasses and a suit (no text or symbols visible)
</details>

Rui Zhang (S’00–M’07–SM’15–F’17) received the B.Eng. degree (Hons.) and the M.Eng. degree in electrical engineering from the National University of Singapore, Singapore, and the Ph.D. degree in electrical engineering from the Stanford University, Stanford, CA, USA.

From 2007 to 2010, he was a Research Scientist with the Institute for Infocomm Research, A\*STAR, Singapore. Since 2010, he has been with the Department of Electrical and Computer

Engineering, National University of Singapore, where he is currently a Dean’s Chair Associate Professor with the Faculty of Engineering. He has authored over 300 papers. He has been listed as a Highly Cited Researcher (also known as the World’s Most Influential Scientific Minds) by Thomas Reuters since 2015. His research interests include wireless information and power transfer, drone communications, wireless information surveillance, energy-efficient and energy-harvesting-enabled wireless communications, multiuser multi-in multi-out, cognitive radio, and optimization methods.

He was a recipient of the 6th IEEE Communications Society Asia–Pacific Region Best Young Researcher Award in 2011 and the Young Researcher Award of National University of Singapore in 2015. He was a co-recipient of the IEEE Marconi Prize Paper Award in Wireless Communications in 2015, the IEEE Communications Society Asia–Pacific Region Best Paper Award in 2016, the IEEE Signal Processing Society Best Paper Award in 2016, the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2017, the IEEE Signal Processing Society Donald G. Fink Overview Paper Award in 2017, and the IEEE Technical Committee on Green Communications and Computing Best Journal Paper Award in 2017. He authored the paper that received the IEEE Signal Processing Society Young Author Best Paper Award in 2017. He served as a TPC co-chair or an organizing committee member for over 30 international conferences and as a guest editor for 10 special issues in the IEEE and other internationally refereed journals. He was an elected member of the IEEE Signal Processing Society SPCOM from 2012 to 2017 and SAM from 2013 to 2015 Technical Committees, and served as the Vice Chair for the IEEE Communications Society Asia–Pacific Board Technical Affairs Committee from 2014 to 2015. He served as an Editor for the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS from 2012 to 2016 and the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS: Green Communications and Networking Series from 2015 to 2016. He is currently an Editor of the IEEE TRANSACTIONS ON COMMUNICATIONS, the IEEE TRANSACTIONS ON SIGNAL PROCESSING, and the IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING.