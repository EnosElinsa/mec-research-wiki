# Channel Knowledge Map Enabled Low-Altitude ISAC Networks: Joint Air Corridor Planning and Base Station Deployment

Jiaxuan Li , Graduate Student Member, IEEE, Yilong Chen , Graduate Student Member, IEEE, Fan Liu , Senior Member, IEEE, and Jie Xu , Fellow, IEEE

Abstract—This letter addresses the joint air corridor planning and base station (BS) deployment problem for low-altitude integrated sensing and communication (ISAC) networks. In the considered system, unmanned aerial vehicles (UAVs) operate within a structured air corridor composed of connected cubic segments, and multiple BSs need to be selectively deployed at a set of candidate locations to ensure both sensing and communication coverage throughout the corridor. In particular, we leverage the channel knowledge map (CKM) to characterize wireless channels for candidate BS sites prior to deployment, thereby facilitating the offline planning. Under this setup, we minimize the system cost in terms of the weighted sum of the air corridor length and the number of deployed BSs, subject to the constraints on both sensing and communication performance across the corridor. To solve the formulated large-scale nonconvex integer programming problem, we develop a hierarchical coarse-to-fine grid decomposition algorithm. Simulation results demonstrate the benefit of the proposed joint design in reducing the overall deployment cost while ensuring the coverage of the low-altitude ISAC networks.

Index Terms—Low-altitude wireless network, integrated sensing and communication (ISAC), channel knowledge map (CKM), air corridor planning, base station (BS) deployment.

## I. INTRODUCTION

OW-ALTITUDE economy (LAE) leverages unmanned landing (eVTOL) aircraft for urban air mobility and cargo delivery. Air corridors and integrated sensing and communication (ISAC) have emerged as two promising techniques to ensure the safe and reliable operations of UAVs and eVTOLs. On the one hand, air corridors provide structured routing to deconflict traffic and simplify airspace management [1]. On

Received 12 October 2025; revised 2 December 2025; accepted 4 December 2025. Date of publication 10 December 2025; date of current version 26 December 2025. The work of Jiaxuan Li, Yilong Chen, and Jie Xu was supported in part by the National Natural Science Foundation of China under Grant 62471424, Grant 92267202, and Grant U25A20390; in part by the Basic Research Project of Hetao Shenzhen-HK S&T Cooperation Zone under Grant HZQB-KCZYZ-2021067; in part by the Guangdong Provincial Key Laboratory of Future Networks of Intelligence under Grant 2022B1212010001; and in part by the Shenzhen Fundamental Research Program under Grant JCYJ20250604141209012. The work of Fan Liu was supported in part by the National Science Foundation of China (NSFC) under Grant 62522107. The associate editor coordinating the review of this article and approving it for publication was O. L. Alcaraz López. (Corresponding authors: Jie Xu; Fan Liu.)

Jiaxuan Li, Yilong Chen, and Jie Xu are with the School of Science and Engineering, Shenzhen Future Network of Intelligence Institute, and the Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong (Shenzhen), Shenzhen 518172, Guangdong, China (e-mail: jiaxuanli4@link.cuhk.edu.cn; yilongchen@link.cuhk.edu.cn; xujie@cuhk.edu.cn).

Fan Liu is with the National Mobile Communications Research Laboratory, School of Information Science and Engineering, Southeast University, Nanjing 210096, China (e-mail: f.liu@ieee.org).

Digital Object Identifier 10.1109/LWC.2025.3642429 the other hand, ISAC networks enable simultaneous sensing and communication within air corridors, supporting realtime tracking, navigation, and reliable control of UAVs and eVTOLs [2]. As such, the integration of air corridors and ISAC is crucial for scalable and safe LAE.

In the literature, there have been various prior works investigating air corridors [3], [4] and ISAC networks [5], [6], [7] for LAE separately. First, the authors in [3], [4] studied the design of geometric configurations (e.g., cubic or cylindrical segments) of air corridors and the corresponding routing strategies, with the objective of maximizing the traffic throughput while ensuring collision-free operations. Next, various prior works (e.g., [5], [6], [7]) exploited onground ISAC networks to support low-altitude UAV operations via ground-based cellular infrastructure. For example, the authors in [7] utilized the cooperative transmit beamforming at multiple on-ground base stations (BSs) to support the communication and localization of cooperative UAVs and monitor the low-altitude airspace to prevent the invasion of unauthorized flight objects. Despite these advances, the joint optimization of air corridor planning and ISAC network deployment remains an open problem, which motivates this letter.

Specifically, we study joint design of air corridors and lowaltitude ISAC networks, for providing seamless sensing and communication coverage throughout air corridors. In this context, obtaining channel state information (CSI) with potential BS sites is particularly challenging due to the lack of prior measurements. Channel knowledge map (CKM) has emerged as a promising solution, which establishes a functional mapping from transceiver locations to the corresponding channel knowledge. In practice, CKM can be effectively constructed based on physical environment knowledge and limited channel measurements [8], [9], [10], providing CSI a priori to facilitate network deployment and operation [11], [12]. However, how to exploit CKM to facilitate the joint optimization of air corridor planning and BS deployment has not been studied in the literature yet.

This letter studies the CKM-enabled joint air corridor planning and BS deployment problem for low-altitude ISAC networks at the planning stage, providing a stable upper-layer infrastructure and corridor layout that can be further adapted in operation to dynamic urban environments. To be specific, we model the air corridor as a sequence of connected cubes with a fixed edge length located at a fixed altitude, and we need to selectively deploy multiple BSs at a set of candidate locations to provide communication and sensing coverage across the corridor. For each candidate BS site, we utilize the CKM to predict the CSI and evaluate the communication and sensing coverage performance, thereby enabling offline optimization. Under this setup, we aim to minimize the system cost in terms of the weighted sum of the air corridor length and the number of deployed BSs, subject to the sensing and communication coverage requirements throughout the corridor. We propose a hierarchical coarse-to-fine grid decomposition algorithm to solve the formulated large-scale nonconvex integer programming problem. In the coarse layer, we reformulate the problem as a linear integer program to obtain a feasible air corridor and BS deployment solution. In the fine layer, we use an alternating optimization (AO) procedure to refine the coarse layer solution for further reducing the system cost. Simulation results demonstrate that the proposed algorithm achieves shorter air corridor lengths and requires fewer BSs to fulfill the LAE tasks, thereby significantly reducing system costs compared with various baseline methods.

![](images/c5000435f2b5b521b80dd63cb1d574b1e36e84d5c394b13995f43043bfb263f8.jpg)

<details>
<summary>text_image</summary>

Departure point
H
Takeoff area
BS
UAV
BS
Destination
ISAC signal
BS
Landing area
</details>

Fig. 1. System model.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

We consider an ISAC network for LAE as illustrated in Fig. 1, in which potential UAVs pass through an urban area from a departure point to a destination point within a dedicated air corridor (to be designed) to fulfill various tasks such as urban air mobility and cargo delivery. To ensure reliable communication and real-time sensing for UAVs, multiple ground BSs are selectively deployed at a set of candidate locations on the ground to support these services throughout the corridor.

## A. Air Corridor Model

An air corridor is a three-dimensional (3D) volume of airspace reserved for UAV and eVTOL operations [3]. In this letter, we consider a corridor at a fixed-altitude $H . ^ { 1 }$ The vertical takeoff and landing zones are assumed to lie directly beneath the departure and destination points. Under these conditions, our objective is to design an air corridor that safely accommodates flights within the prescribed airspace.

As shown in Fig. 1, we adopt a discretized grid map with Cartesian coordinates, and the air corridor is modeled as a sequence of uniformly sized cubes connected face to face to form a continuous path [3]. The grid consists of an $N \times N$ 3D rectangular region at a constant altitude H, indexed by $\{ \mathcal { R } _ { i , j } ~ | ~ { \boldsymbol { i } } , { \boldsymbol { j } } ~ \in \mathcal { N } \} , ~ \mathcal { N } \triangleq \{ 1 , 2 , \ldots , N \}$ , with the origin at $( x ^ { O ^ { - } } , y ^ { O } , H )$ . The geographical coverage of each grid cell $\mathcal { R } _ { i , j }$ is defined as

$$
\begin{array}{l} \mathcal {R} _ {i, j} = \left[ x ^ {O} + (i - 1) \Delta_ {x}, x ^ {O} + i \Delta_ {x} \right] \\ \times \left[ y ^ {O} + (j - 1) \Delta_ {y}, y ^ {O} + j \Delta_ {y} \right] \times [ H, H + \Delta_ {z} ], (1) \\ \end{array}
$$

where $\Delta _ { x } , \Delta _ { y } .$ and $\Delta _ { z }$ denote the grid resolutions along the $x \mathrm { \cdot , \ y \mathrm { - } , }$ , and z-axes, respectively.

1The considered system can also be viewed as one representative air corridor among multiple corridors in a multi-layer air corridor architecture.

Furthermore, let A denote an $N \times N$ binary indicator matrix, with $A _ { i , j } ~ = ~ 1 ~ \mathrm { i f } ~ \mathcal { R } _ { i , j }$ is included in the air corridor, and $A _ { i , j } = \mathrm { { 0 } }$ otherwise. Without loss of generality, we designate $\mathcal { R } _ { 1 , 1 }$ and $\mathcal { R } _ { N , N }$ as the departure and destination points of the corridor, respectively. We thus have

$$
A _ {1, 1} = 1, \quad A _ {N, N} = 1. \tag {2}
$$

Note that in order for the air corridor to be feasible, a necessary condition is that the corridor should form a continuous path, meaning that all active cells with $A _ { i , j } = 1$ must be connected. This is equivalent to the condition that each active cell $( i , j )$ with $A _ { i , j } = 1$ should have at least two active adjacent grid along the x- or y-axis. Moreover, to avoid unnecessary branching, each active cell is restricted to have at most two active neighbors. To this end, for each grid $( i , j ) .$ , we define the set of four neighboring grid cells as $\bar { \mathcal { N } } _ { 4 } ( i , j ) \triangleq$ $\{ ( i ^ { \prime } , j ^ { \prime } ) \in \mathcal { N } \times \mathcal { N } : ~ | i ^ { \prime } - i | ^ { \smile } + | j ^ { \prime } - \overline { { j } } | = 1 \}$ . Accordingly, the connectivity constraints are expressed as

$$
2 A _ {i, j} \leq \sum_ {(i ^ {\prime}, j ^ {\prime}) \in \mathcal {N} _ {4} (i, j)} A _ {i ^ {\prime}, j ^ {\prime}} \leq 2. \tag {3}
$$

Additionally, to guarantee reachability, there must exist at least one active grid in each row and column between the departure point and the destination point. We have

$$
\begin{array}{l} \sum_ {i = 1} ^ {N} A _ {i, j} \geq 1, \quad \forall j \in \mathcal {N}, \\ \sum_ {j = 1} ^ {N} A _ {i, j} \geq 1, \quad \forall i \in \mathcal {N}. \tag {4} \\ \end{array}
$$

## B. Sensing and Communication Models

Suppose that there are K candidate BS sites with indices ${ \mathcal { K } } \ { \stackrel { \Delta } { = } } \ \left\{ 1 , \ldots , K \right\}$ . Let $\mathbf { q } _ { k } ~ = ~ ( q _ { k , x } , q _ { k , y } , q _ { k , z } )$ denote the location of site $k , k \in \mathcal { K }$ . We introduce a binary vector $\delta =$ $( \delta _ { 1 } , \dots , \delta _ { K } )$ to indicate the deployment status of candidate sites, where $\delta _ { k } = 1$ if a BS is deployed at candidate site k and $\delta _ { k } = 0$ otherwise.

To characterize the sensing and communication coverage throughout the air corridor, we need to acquire CSI from each candidate BS site to any point within the air corridor. However, acquiring such measurements at a dense set of locations is typically impractical, especially when the BS has not been properly deployed. To address this, we exploit the CKM to obtain channel power gains. In practice, we can first obtain the 3D environmental model of the considered region, and then utilize the ray tracing technique to construct the channel gain map $[ 1 3 ] . ^ { 2 }$ It is assumed that for each candidate BS site, we use the CKM to obtain the mapping from a 3D user location $\{ \mathbf { p } = ( q _ { x } , q _ { y } , q _ { z } ) \}$ to the corresponding channel power gain at that BS site. Let $h _ { k } ( \mathbf { p } )$ denote the channel power gain between BS site $k \in \mathcal { K }$ and location p, which in general is a discrete function without a closed-form expression. In particular, for the rectangular region $\mathcal { R } _ { i , j }$ associated with $A _ { i , j } , i , j \in \mathcal { N } _ { : }$ the set of sampled channel power gains from BS site $k , k \in \mathcal { K }$ within $\mathcal { R } _ { i , j }$ is

$$
\mathcal {G} _ {k, i, j} = \big \{h _ {k} (\mathbf {p}) \mid \mathbf {p} \in \mathcal {R} _ {i, j} \big \}. \tag {5}
$$

For communication, by leveraging the CKM, we evaluate the received signal-to-interference-plus-noise ratio (SINR) at

2The accuracy of ray tracing process highly depends on the accuracy of the 3D environment model. In order to focus our study on the network deployment design, we assume that the CKM is perfectly known a priori and leave the CKM construction and the analysis of inaccurate CKM for future work.

sample positions p as the communication performance metric. By considering that the receiver is deployed with a single antenna, the SINR of the arrival signal at location p from BS k is given by

$$
\gamma_ {k, i, j} (\mathbf {p}, \boldsymbol {\delta}) = \frac {P \delta_ {k} G h _ {k} (\mathbf {p})}{\sum_ {b \in \mathcal {K} \backslash k} \delta_ {b} P h _ {b} (\mathbf {p}) + \sigma^ {2}}, \tag {6}
$$

where $P$ is the transmit power of each BS, $G \ > \ 1$ is a coefficient capturing the transmit antenna gain and the potential transmit beamforming gain, and $\sigma ^ { 2 }$ is the noise power at the receiver. To ensure the coverage within each grid cell $( i , j )$ , we take the worst-case SINR over all sampling points within this cell as the communication performance metric. Specifically, for all points within $\mathcal { R } _ { i , j }$ , we define $h _ { k , i , j } ^ { \operatorname* { m i n } } \triangleq$ min $( \mathcal { G } _ { k , i , j } )$ and $h _ { k , i , j } ^ { \operatorname* { m a x } } \triangleq$ max $( \mathcal { G } _ { k , i , j } )$ as the minimum and maximum channel power gains from BS site $k ,$ respectively. Accordingly, the worst-case SINR is given by

$$
\underline {{\gamma}} _ {k, i, j} (\boldsymbol {\delta}) \triangleq \frac {P G \delta_ {k} h _ {k , i , j} ^ {\min}}{\sum_ {b \in \mathcal {K} \backslash k} \delta_ {b} P h _ {b , i , j} ^ {\max} + \sigma^ {2}}. \tag {7}
$$

In addition, we consider the line-of-sight (LoS) sensing to localize aircraft within the air corridor for navigation and surveillance. To this end, at least three LoS paths are needed, and the total received echo signal power from LoS paths should exceed a certain threshold [15]. We define an indicator $\mathcal { L } _ { k , i , j } .$ , where $\mathcal { L } _ { k , i , j } = 1$ if there exists a LoS link between BS site k and location $\mathbf { p } \in \mathcal { R } _ { i , j }$ , and $\mathcal { L } _ { k , i , j } = 0$ otherwise. Assuming a monostatic LoS sensing model, we consider the minimum echo signal power over $\mathcal { R } _ { i , j }$ from BS site k as the sensing performance metric, which is given by [14]

$$
p _ {k, i, j} \triangleq \min _ {\mathbf {p} \in \mathcal {R} _ {i, j}} \frac {\mathcal {L} _ {k , i , j} P G \lambda^ {2} \sigma_ {R C S}}{(4 \pi) ^ {3} d _ {k} ^ {4} (\mathbf {p})}, \tag {8}
$$

where $d _ { k } ( \mathbf { p } ) \triangleq \Vert \mathbf { q } _ { k } - \mathbf { p } \Vert _ { 2 }$ is the distance between BS site k and location $\mathbf { p } \in \mathcal { R } _ { i , j } , \lambda$ is the wavelength, and $\sigma _ { \mathrm { R C S } }$ denotes the radar cross section of potential UAV.

## C. Problem Formulation

In this letter, we aim to minimize the system cost in terms of the weighted sum of the air corridor length and the number of deployed BSs, subject to the path connectivity, SINR, LoS visibility, and sensing power constraints. The problem is formulated as

$$
\text {(P1)} \colon \quad \min _ {\mathbf {A}, \boldsymbol {\delta}} \quad \alpha_ {1} \mathbf {1} ^ {\top} \mathbf {A} \mathbf {1} + \alpha_ {2} \sum_ {k = 1} ^ {K} \delta_ {k},
$$

$$
\text { s.t. } \quad \sum_ {k = 1} ^ {K} \delta_ {k} p _ {k, i, j} \geq \epsilon_ {1} A _ {i, j}, \forall i, j \in \mathcal {N}, \tag {9a}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} \mathcal {L} _ {k, i, j} \geq 3 A _ {i, j}, \forall i, j \in \mathcal {N}, \tag {9b}
$$

$$
\max _ {k \in \mathcal {K}} \underline {{\gamma}} _ {k, i, j} (\boldsymbol {\delta}) \geq \epsilon_ {2} A _ {i, j}, \forall i, j \in \mathcal {N}, \tag {9c}
$$

$$
\delta_ {k} \in \{0, 1 \}, A _ {i, j} \in \{0, 1 \}, \forall k \in \mathcal {K}, i, j \in \mathcal {N}, (9 d)
$$

$$
(2) - (4),
$$

where $\alpha _ { 1 } ~ \geq ~ 0$ and $\alpha _ { 2 } \geq 0$ are weighting coefficients determined by the economics and policy constraints of the target low-altitude network with $\alpha _ { 1 } + \alpha _ { 2 } = 1$ , and $\mathbf { 1 } \in \mathbb { R } ^ { N }$ denotes the all-ones vector, with $\mathbf { 1 } ^ { \top }$ being its transpose. For any corridor cell $( i , j ) \ ( \mathrm { i . e . , } \ A _ { i , j } = 1 )$ , the constraints in (9a) and (9c) ensure received sensing power and communication SINR no less than the corresponding thresholds $\epsilon _ { 1 }$ and $\epsilon _ { 2 } ,$ respectively, while the constraint in (9b) guarantees the visibility from at least three LoS BSs.

Problem (P1) is an integer nonconvex program with hard integrality constraints that is inherently difficult to solve using relaxation-based methods. Note that the decision space consists of $N ^ { 2 } { + } K$ binary variables. Consequently, in practical settings with fine spatial resolution, (P1) becomes a large-scale problem, significantly increasing computational complexity.

## III. PROPOSED SOLUTION TO PROBLEM (P1)

In this section, we eliminate the nonconvex constraint in (9c), yielding a linear integer program. Despite this reformulation, the problem still remains computationally demanding due to its scale and integrality. To address this, we adopt a coarse-to-fine hierarchical framework that first obtains a jointly optimized coarse-resolution path and BS deployment, and then refines the solution at the fine layer to improve spatial coverage with reduced BS deployment overhead.

## A. Joint Optimization Over Coarse Grids

At the coarse layer, the original $N \times N$ map A is coarsened to an $M \times M$ grid B, with index set $\mathcal { M } \triangleq \{ 1 , \dots , M \}$ . Each coarse cell $B _ { a , b } , \ a , b \ \in \mathcal { M }$ represents a rectangular region $\tilde { \mathcal { R } } _ { a , b }$ with spatial resolutions $\tilde { \Delta } _ { x } , \tilde { \Delta } _ { y } .$ and $\Delta _ { z }$ . Let $\pmb { \delta } ^ { B }$ denote the associated BS deployment vector. For each $( a , \ b )$ , we evaluate the cell SINR γ˜k,a,b( $\underline { { \tilde { \gamma } } } _ { k , a , b } ( \delta ^ { B } )$ according to (7), by using the minimum and maximum channel power gains $\tilde { h } _ { k , a , b } ^ { \operatorname* { m i n } }$ and $\tilde { h } _ { k , a , b } ^ { \operatorname* { m a x } }$ $\tilde { \mathcal { G } } _ { k , a , b }$ $\tilde { \mathcal { R } } _ { a , b }$ outliers in each coarse cell, we discard the lowest 10% and $\tilde { \mathcal { G } } _ { k , a , b }$ $\tilde { h } _ { k , a , b } ^ { \operatorname* { m i n } }$ and $\tilde { h } _ { k , a , b } ^ { \operatorname* { m a x } }$ on the remainder. We also define $\tilde { \mathcal { L } } _ { k , a , b }$ and $\tilde { p } _ { k , a , b }$ in this layer, following the same form as in Section II-B.

We address the joint optimization problem (P1) at the re-partitioned coarse layer, with the newly defined indicator matrix B and deployment indicator vector $\pmb { \delta } ^ { B }$ . Firstly, to eliminate the max operator in (9c), we apply a Big-M reformulation [16]. Specifically, we introduce binary auxiliary variables $\{ z _ { k , a , b } ~ \in ~ \{ 0 , 1 \} | a , b ~ \in ~ \mathcal { M } , k ~ \in ~ \mathcal { K } \}$ to indicate whether BS site k satisfies the SINR threshold at cell $( a , b )$ . Then, for each coarse cell $( a , b ) , a , b \in { \mathcal { M } }$ the constraint $\begin{array} { r } { \operatorname* { m a x } _ { k \in { \mathcal K } } \tilde { \underline { { \gamma } } } _ { k , a , b } ( \delta ^ { B } ) \geq \epsilon _ { 2 } B _ { a , b } } \end{array}$ is equivalently enforced by

$$
\left(1 - z _ {k, a, b}\right) \zeta \geq \epsilon_ {2} B _ {a, b} \left(P \sum_ {k ^ {\prime} \in \mathcal {K} \backslash k} \delta_ {k ^ {\prime}} ^ {B} \tilde {h} _ {k ^ {\prime}, a, b} ^ {\max} + \sigma^ {2}\right)
$$

$$
- P G \delta_ {k} ^ {B} \tilde {h} _ {k, a, b} ^ {\min}, \tag {10a}
$$

$$
z _ {k, a, b} \leq \delta_ {k} ^ {B}, \tag {10b}
$$

$$
\sum_ {k = 1} ^ {K} z _ {k, a, b} \geq B _ {a, b}, \tag {10c}
$$

$$
z _ {k, a, b} \in \{0, 1 \}. \tag {10d}
$$

Here, $\zeta > 0$ is a sufficiently large constant (chosen larger than an upper bound on the right-hand side of (10a)) used to deactivate the SINR constraint in (10a) when $z _ { k , a , b } = 0$ , and to activate the constraint when $z _ { k , a , b } = 1$ . Eq. (10b) prevents the selection of an undeployed BS, and (10c) ensures that at least one deployed BS satisfies the threshold whenever $B _ { a , b } = 1$ .

The constraint (10a) remains nonconvex because it contains $B _ { a , b } \delta _ { k ^ { \prime } } ^ { B }$ . Since all these variables are binary, we introduce auxiliary binaries $w _ { k , a , b } = B _ { a , b } \delta _ { k } ^ { B }$ for all $k \in \mathcal { K }$ and $a , b \in { \mathcal { M } }$ . We enforce this identity $w _ { k , a , b } =$ $B _ { a , b } \delta _ { k } ^ { B }$ through the standard McCormick linearization [17]:

![](images/1834f23eb29f16d6ec4c76b97d5f85f7d8e73114555a5573862e1cc44cd21e31.jpg)

<details>
<summary>text_image</summary>

Departure point
Destination
Air corridor
Base station
</details>

Fig. 2. The considered area (from the OpenStreetMap database) and the spatial distribution of candidate BS sites.  
![](images/e197e4289747973c2cae2552996ea76fefa24cfcf727130ab758fd8ccf5331ba.jpg)

<details>
<summary>heatmap</summary>

| X-Direction grid index | Y-Direction grid index | Received sensing power (dBm) | SINR (dB) |
| :--- | :--- | :--- | :--- |
| 1 | 1 | 807 | -25 |
| 2 | 2 | 806 | -24 |
| 3 | 3 | 805 | -23 |
| 4 | 4 | 804 | -22 |
| 5 | 5 | 803 | -21 |
| 6 | 6 | 802 | -20 |
| 7 | 7 | 801 | -19 |
| 8 | 8 | 800 | -18 |
| 9 | 9 | 799 | -17 |
| 10 | 10 | 798 | -16 |
| 11 | 11 | 797 | -15 |
| 12 | 12 | 796 | -14 |
| 13 | 13 | 795 | -13 |
| 14 | 14 | 794 | -12 |
| 15 | 15 | 793 | -11 |
| 16 | 16 | 792 | -10 |
| 17 | 17 | 791 | -9 |
| 18 | 18 | 790 | -8 |
| 19 | 19 | 789 | -7 |
| 20 | 20 | 788 | -6 |
| 21 | 21 | 787 | -5 |
| 22 | 22 | 786 | -4 |
| 23 | 23 | 785 | -3 |
| 24 | 24 | 784 | -2 |
| 25 | 25 | 783 | -1 |
| 26 | 26 | 782 | 0 |
| 27 | 27 | 781 | 1 |
| 28 | 28 | 780 | 2 |
| 29 | 29 | 779 | 3 |
| 30 | 30 | 778 | 4 |
| 31 | 31 | 777 | 5 |
| 32 | 32 | 776 | 6 |
| 33 | 33 | 775 | 7 |
| 34 | 34 | 774 | 8 |
| 35 | 35 | 773 | 9 |
| 36 | 36 | 772 | 10 |
| 37 | 37 | 771 | 11 |
| 38 | 38 | 770 | 12 |
| 39 | 39 | 769 | 13 |
| 40 | 40 | 768 | 14 |
| 41 | 41 | 767 | 15 |
| 42 | 42 | 766 | 16 |
| 43 | 43 | 765 | 17 |
| 44 | 44 | 764 | 18 |
| 45 | 45 | 763 | 19 |
| 46 | 46 | 762 | 20 |
| 47 | 47 | 761 | 21 |
| 48 | 48 | 760 | 22 |
| 49 | 49 | 759 | 23 |
| 50 | 50 | 758 | 24 |
| 51 | 51 | 757 | 25 |
| 52 | 52 | 756 | 26 |
| 53 | 53 | 755 | 27 |
| 54 | 54 | 754 | 28 |
| 55 | 55 | 753 | 29 |
| 56 | 56 | 752 | 30 |
| 57 | 57 | 751 | 31 |
| 58 | 58 | 750 | 32 |
| 59 | 59 | 749 | 33 |
| 60+ (a) (Received sensing power) vs. Received sensing power (sinR) vs. Received sensing power (sinR) (a) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b) (b)
</details>

Fig. 3. (a) Coarse-layer air corridor overlaid on the sensing power map. (b) Fine-layer air corridor overlaid on the SINR map.

$$
w _ {k, a, b} \leq \delta_ {k} ^ {B}, \tag {11a}
$$

$$
w _ {k, a, b} \leq B _ {a, b}, \tag {11b}
$$

$$
w _ {k, a, b} \geq \delta_ {k} ^ {B} + B _ {a, b} - 1, \tag {11c}
$$

$$
w _ {k, a, b} \in \{0, 1 \}. \tag {11d}
$$

This linearization guarantees that $w _ { k , a , b } = 1$ if and only if $B _ { a , b } = 1$ $\bar { \delta } _ { k } ^ { B } = 1$ $w _ { k , a , b } = 0$ substituting $w _ { k ^ { \prime } , a , b }$ for $B _ { a , b } \delta _ { k ^ { \prime } } ^ { B }$ , (10a) is rewritten as

$$
\begin{array}{l} \left(1 - z _ {k, a, b}\right) \zeta \geq \epsilon_ {2} \left(P \sum_ {k ^ {\prime} \in \mathcal {K} \backslash k} \tilde {h} _ {k ^ {\prime}, a, b} ^ {\max} w _ {k ^ {\prime}, a, b} + \sigma^ {2} B _ {a, b}\right) \\ - P G \delta_ {k} ^ {B} \tilde {h} _ {k, a, b} ^ {\min}, \forall k \in \mathcal {K}, a, b \in \mathcal {M}. \tag {12} \\ \end{array}
$$

After that, at coarse layer, problem (P1) is reformulated as

$$
\begin{array}{l} \text {(P2)} \colon \quad \min _ {\mathbf {B}, \boldsymbol {\delta} ^ {B}} \quad \alpha_ {1} \mathbf {1} ^ {\top} \mathbf {B} \mathbf {1} + \alpha_ {2} \sum_ {k = 1} ^ {K} \delta_ {k} ^ {B}, \\ \left\{z _ {k, a, b}, \forall k \in \mathcal {K}, a, b \in \mathcal {M} \right\} \\ \{w _ {k, a, b}, \forall k \in \mathcal {K}, a, b \in \mathcal {M} \} \\ \end{array}
$$

$$
\text { s.t. } 2 B _ {a, b} \leq \sum_ {(a ^ {\prime}, b ^ {\prime}) \in \mathcal {N} _ {4} (a, b)} B _ {a ^ {\prime} b ^ {\prime}} \leq 2, \forall a, b \in \mathcal {M} \tag {13a}
$$

$$
\sum_ {a = 1} ^ {M} B _ {a, b} \geq 1, \forall b \in \mathcal {M}, \sum_ {b = 1} ^ {M} B _ {a, b} \geq 1, \forall a \in \mathcal {M} \tag {13b}
$$

$$
B _ {1, 1} = 1, \quad B _ {M, M} = 1, \tag {13c}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} ^ {B} \tilde {p} _ {k, a, b} \geq \epsilon_ {1} B _ {a, b}, \forall a, b \in \mathcal {M}, \tag {13d}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} ^ {B} \tilde {\mathcal {L}} _ {k, a, b} \geq 3 B _ {a, b}, \forall a, b \in \mathcal {M}, \tag {13e}
$$

$$
\delta_ {k} ^ {B} \in \{0, 1 \}, B _ {a, b} \in \{0, 1 \}, \forall k \in \mathcal {K}, a, b \in \mathcal {M} \tag {13f}
$$

$$
(1 0 \mathrm{b}) - (1 1 \mathrm{d}), (1 2).
$$

The coarse layer formulation (P2) reduces the joint optimization problem to a linear integer program with $\bar { K } M ^ { 2 }$ variables, compared to $K N ^ { 2 }$ in a direct fine layer formulation of (P1), where $N \gg M$ .

## B. Alternative Refinement of Air Corridor and BS Deployment

In the coarse layer, $B _ { a , b } = 1$ indicates that the air corridor passes through grid (a, b). Let $\begin{array} { r } { B = \{ ( a , b ) \ | \ B _ { a , b } = \ 1 \} } \end{array}$ denote the set of selected coarse-grid cells obtained by solving (P2). For each $( a , b ) \in B _ { \mathrm { : } }$ , we define $\mathbf { A } ^ { ( a , b ) }$ as the $( N / M ) \times$ $( N / M )$ (assuming N is divisible by M) submatrix of A for the region covered by $B _ { a , b }$ , where each entry $A _ { i , j } ^ { ( a , b ) } , i , j \in$ $\mathcal { N } ^ { ( a , b ) }$ , provides the unit-cube resolution for final planning.

We optimize the path within each $\mathbf { A } ^ { ( a , b ) } , \ ( a , b ) \in \ B$ and update the global BS deployment δ based on A, which is assembled from all $\mathbf { A } ^ { ( a , b ) }$ via an AO framework.

First, we initialize the fine layer deployment vector δ as the coarse layer solution $\pmb { \delta } ^ { B }$ . Next, for each $\mathbf { A } ^ { ( a , b ) } , ( a , b ) \in \mathcal { B }$ , we predefine its start and end points based on its adjacent coarsegrid neighbors. For example, if $B _ { a , b } = 1 , \ B _ { a - 1 , b } = 1$ , and $B _ { a , b + 1 } = 1$ , then cell (a, b) is connected to both its southern and eastern neighbors. We then set the midpoint of $\mathbf { A } ^ { ( a , b ) } \mathbf { \bar { s } }$ southern edge as the start point $A _ { s x , s y } ^ { ( a , b ) }$ , and the midpoint of its eastern edge as the destination point $4 _ { d x , d y } ^ { ( a , b ) }$ . Fixing δ and these end points, we solve the following subproblem (P3.1) independently for each $\mathbf { A } ^ { ( a , b ) } , ( a , b ) \in \mathcal { B }$ .

$$
\text {(P3.1)} \colon \min _ {\mathbf {A} ^ {(a, b)}} \quad \mathbf {1} ^ {\top} \mathbf {A} ^ {(a, b)} \mathbf {1},
$$

$$
\text { s.t. } 2 A _ {i, j} ^ {(a, b)} \leq \sum_ {\substack {(i ^ {\prime}, j ^ {\prime}) \in \mathcal {N} _ {4} (i, j) \cap \mathcal {N} ^ {(a, b)}}} A _ {i ^ {\prime}, j ^ {\prime}} ^ {(a, b)} \leq 2, \forall i, j \in \mathcal {N} ^ {(a, b)}, \tag{14}
$$

$$
\sum_ {i = s x} ^ {d x} A _ {i, j} ^ {(a, b)} \geq 1, \forall j \in \mathcal {N} ^ {(a, b)}, \sum_ {j = s y} ^ {d y} A _ {i, j} ^ {(a, b)} \geq 1, \forall i \in \mathcal {N} ^ {(a, b)}, \tag {15}
$$

$$
A _ {s x, s y} ^ {(a, b)} = 1, \quad A _ {d x, d y} ^ {(a, b)} = 1, \tag {16}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} p _ {k, i, j} ^ {(a, b)} \geq \epsilon_ {1} A _ {i, j} ^ {(a, b)}, \forall i, j \in \mathcal {N} ^ {(a, b)}, \tag {17}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} \mathcal {L} _ {k, i, j} ^ {(a, b)} \geq 3 A _ {i, j} ^ {(a, b)}, \quad \forall i, j \in \mathcal {N} ^ {(a, b)}, \tag {18}
$$

$$
\max _ {k \in \mathcal {K}} \underline {{\gamma}} _ {k, i, j} ^ {(a, b)} \geq \epsilon_ {2} A _ {i, j} ^ {(a, b)}, \forall i, j \in \mathcal {N} ^ {(a, b)}, \tag {19}
$$

$$
A _ {i, j} ^ {(a, b)} \in \{0, 1 \}, \forall i, j \in \mathcal {N} ^ {(a, b)}, \tag {20}
$$

where p k ,i ,j , $p _ { k , i , j } ^ { ( a , b ) } , \mathcal { L } _ { k , i , j } ^ { ( a , b ) }$ , and $\underline { { \gamma } } _ { k , i , j } ^ { ( a , b ) }$ follow the definitions in Section II-B and are evaluated within $\mathcal { \tilde { R } } _ { a , b }$ at the fine layer $A _ { 1 , 1 } ^ { ( 1 , 1 ) }$ and A(M ,M ) $A _ { N / M , N / M } ^ { ( M , M ) }$ N /M ,N /M have only one active adjacent neighbor.

Once all $\mathbf { A } ^ { ( a , b ) } , ( a , b ) \in \mathcal { B }$ have been updated, the global fine layer map A is reconstructed by assembling the submatrices. Subsequently, we solve problem (P3.2) to update δ based on the obtained A.

$$
\min _ {\delta} \sum_ {k = 1} ^ {K} \delta_ {k}, \tag {P3.2}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} p _ {k, i, j} \geq \epsilon_ {1} A _ {i, j}, \quad \forall i, j \in \mathcal {N}, \tag {21a}
$$

$$
\sum_ {k = 1} ^ {K} \delta_ {k} \mathcal {L} _ {k, i, j} \geq 3 A _ {i, j}, \quad \forall i, j \in \mathcal {N}, \tag {21b}
$$

$$
\max _ {k \in \mathcal {K}} \underline {{\gamma}} _ {k, i, j} \geq \epsilon_ {2} A _ {i, j}, \quad \forall i, j \in \mathcal {N}, \tag {21c}
$$

$$
\delta_ {k} \in \{0, 1 \}, \forall k \in \mathcal {K}. \tag {21d}
$$

Both (P3.1) and (P3.2) are linear integer programs. Since each AO step leads to monotonically non-increasing system cost (i.e., the air corridor length or the number of deployed BSs), and both objectives are bounded below, the algorithm is guaranteed to converge [18].

## IV. NUMERICAL RESULTS

This section presents numerical results to evaluate the performance of our proposed algorithms. We consider a 500 m×500 m area in Futian District, Shenzhen, China, with $K = 3 0$ candidate BSs, as shown in Fig. 2. We use the opensource library Sionna RT (v0.18.0) to generate CKMs [13]. The carrier frequency is set to be 1 GHz, the noise power at the UAV receiver is ${ \bf { \bar { \sigma } } } ^ { 2 } = - 1 1 0$ dBm, and the transmit power of each BS is $P = 3 0$ dBm. We set the transmit gain of each BS to $G = 1 2$ dB and the radar cross section to $\bar { \sigma } _ { \mathrm { { R C S } } } = 1 { \mathrm { m } } ^ { 2 }$ .

![](images/f6139fe45b9731e97147a1d2c1e0876cf5cd11a9e558455feecde165a7a5481d.jpg)  
(a)

![](images/005582705dd5269dd85d285882237cf07f1840350a1ef55b4d350d0690c5bfb9.jpg)  
Fig. 4. (a) The number of deployed BSs versus 1. (b) The length of air corridor paths versus $\epsilon _ { 2 } .$

The altitude of air corridor is set as H = 150 m, and the BS height is set as 25 m.

In the coarse layer, the map is divided into $1 0 \times 1 0$ grids, with each grid measuring 50 $\mathrm { ~ m ~ } \times \ 5 0$ m. For problem (P2), we set the weights as $\alpha _ { 1 } = 0 . 5$ and $\alpha _ { 2 } = 0 . 5$ , and choose the Big-M constant $\zeta = 1 0 ^ { - 8 }$ . In the fine layer, the map is divided into $1 0 0 \times 1 0 0$ grids, each with resolution $\Delta _ { x } = \Delta _ { y } = \Delta _ { z } =$ 5 m, which is consistent with the size of the air corridor cube.3 The received sensing power threshold is $\epsilon _ { 1 } = - 7 5$ dBm, and the SINR threshold is $\epsilon _ { 2 } = 3 ~ \mathrm { d B }$ .

We consider the following two benchmark schemes for comparison:

• A\*-based sequential planning: We first compute the shortest path via ${ \bf A } ^ { * } \left[ 2 0 \right]$ and then, conditioning on this path, solve problem (P3.2) to obtain the BS deployment subject to the communication and sensing constraints.  
• Random BS deployment: We randomly deploy BSs at the K candidate sites with the number of deployed BSs increasing from 1 to K, and solve problem (P3.1) with given δ until a feasible shortest path solution is obtained.

Fig. 3(a) illustrates the jointly optimized coarse-layer air corridor, BS deployment, and the received sensing power. It is observed that the cells traversed by the corridor satisfy both thresholds, and the length is minimized. On a $1 0 \times 1 0$ grid, our method yields a shortest path traversing 19 cells (50 m per cell) with 8 deployed BSs. Furthermore, Fig. 3(b) presents the fine-layer corridors and BS deployment after iterative optimizations, with each fine cell according to the SINR. On a 100 × 100 grid, our method yields a shortest path traversing 199 cells (5 m per cell) with 7 deployed BSs.

Fig. 4(a) shows the number of deployed BSs versus the minimum received sensing power threshold $\epsilon _ { 1 }$ (with $\epsilon _ { 2 } = 3$ dB), and Fig. 4(b) shows the length versus the minimum SINR threshold $\epsilon _ { 2 }$ (with $\epsilon _ { 1 } = - 7 5$ dBm) for our method and two benchmarks. The results for the two benchmarks are averaged over 100 random realizations. It is observed in Fig. 4(a) that the number of deployed BSs increases with $\epsilon _ { 1 }$ for all three schemes, whereas our approach consistently requires the fewest BSs. It is observed in Fig. 4(b) that the length of both our method and the random deployment baseline increases with $\epsilon _ { 2 } { \mathrm { . } }$ , whereas that of the $\mathbf { A } ^ { * }$ scheme remains unchanged. Nevertheless, our approach consistently identifies a feasible path and yields the shortest length among all three schemes. By contrast, the $\mathbf { A } ^ { * }$ scheme fails to find any feasible path once $\epsilon _ { 2 }$ exceeds 3.2 dB, and the random BS deployment baseline fails beyond 3.8 dB, since under stringent SINR thresholds and limited trial budget, these methods rarely identify a path satisfying all constraints.

3We target small-UAV corridors (max dimension <2 m [19]) and adopt a 5 m grid, sufficient for single-UAV operation.

## V. CONCLUSION

In this letter, we investigated the joint air corridor planning and BS deployment for low-altitude ISAC networks, with the objective of minimizing the network cost under both communication and sensing constraints. By leveraging CKMs, we enabled offline evaluation of each candidate BS’s performance without the need for real-time measurements. We proposed a coarse-to-fine framework with an AO algorithm to efficiently solve the formulated large-scale, nonconvex integer program. Simulation results show that the proposed method significantly reduces length and deployment cost compared to benchmark schemes, thereby demonstrating its effectiveness for costefficient planning of low-altitude ISAC networks.

## REFERENCES

[1] A. Bauranov and J. Rakas, “Designing airspace for urban air mobility: A review of concepts and approaches,” Prog. Aerosp. Sci., vol. 125, Aug. 2021, Art. no. 100726.  
[2] F. Liu et al., “Integrated sensing and communications: Toward dualfunctional wireless networks for 6G and beyond,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1728–1767, Jun. 2022.  
[3] S. I. Muna et al., “Air corridors: Concept, design, simulation, and rules of engagement,” Sensors, vol. 21, no. 22, p. 7536, 2021.  
[4] L. Yu et al., “Hybrid transformer based multi-agent reinforcement learning for multiple unpiloted aerial vehicle coordination in air corridors,” IEEE Trans. Mobile Comput., vol. 24, no. 6, pp. 5482–5495, Jun. 2025.  
[5] Y. Song et al., “An overview of cellular ISAC for low-altitude UAV: New opportunities and challenges,” IEEE Commun. Mag., vol. 63, no. 12, pp. 88–95, Dec. 2025.  
[6] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2912–2945, Oct. 2021.  
[7] G. Cheng et al., “Networked ISAC for low-altitude economy: Coordinated transmit beamforming and UAV trajectory design,” IEEE Trans. Commun., vol. 73, no. 8, pp. 5832–5847, Aug. 2025.  
[8] Y. Zeng et al., “A tutorial on environment-aware communications via channel knowledge map for 6G,” IEEE Commun. Surveys Tuts., vol. 26, no. 3, pp. 1478–1519, 3rd Quart., 2024.  
[9] B. Zhang and J. Chen, “Constructing radio maps for UAV communications via dynamic resolution virtual obstacle maps,” in Proc. IEEE 21st Int. Workshop Signal Process. Adv. Wireless Commun. (SPAWC), Atlanta, GA, USA, May 2020, pp. 1–5.  
[10] W. Liu and J. Chen, “UAV-aided radio map construction exploiting environment semantics,” IEEE Trans. Wireless Commun., vol. 22, no. 9, pp. 6341–6355, Sep. 2023.  
[11] Y. Zeng and X. Xu, “Toward environment-aware 6G communications via channel knowledge map,” IEEE Wireless Commun., vol. 28, no. 3, pp. 84–91, Jun. 2021.  
[12] H. Li et al., “Channel knowledge map (CKM)-assisted multi-UAV wireless network: CKM construction and UAV placement,” J. Commun. Inf. Netw., vol. 8, no. 3, pp. 256–270, Sep. 2023.  
[13] J. Hoydis et al., “Sionna RT: Differentiable ray tracing for radio propagation modeling,” in Proc. IEEE Globecom Workshops (GC Wkshps), 2023, pp. 317–321.  
[14] M. A. Richards et al., Principles of Modern Radar: Basic Principles. Ann Arbor, MI, USA: IET Digital Library, 2010.  
[15] S. Motie et al., “Self UAV localization using multiple base stations based on TDoA measurements,” IEEE Wireless Commun. Lett., vol. 13, no. 9, pp. 2432–2436, Jun. 2024.  
[16] M. S. Bazaraa et al., Linear Programming and Network Flows. New York, NY, USA: Wiley, 1990.  
[17] G. P. McCormick, “Computability of global solutions to factorable nonconvex programs: Part I—Convex underestimating problems,” Math. Program., vol. 10, no. 1, pp. 147–175, 1976.  
[18] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.  
[19] IEEE Standard for a Framework for Structuring Low-Altitude Airspace for Unmanned Aerial Vehicle (UAV) Operations, IEEE Standard 1939.1- 2021, 2021.  
[20] P. E. Hart et al., “A formal basis for the heuristic determination of minimum cost paths,” IEEE Trans. Syst. Sci. Cybern., vol. 4, no. 2, pp. 100–107, Jul. 1968.