# 3D Trajectory Optimization in Rician Fading for UAV-Enabled Data Harvesting

Changsheng You , Student Member, IEEE, and Rui Zhang , Fellow, IEEE

Abstract— Dispatching unmanned aerial vehicles (UAVs) to harvest sensing-data from distributed sensors is expected to significantly improve the data collection efficiency in conventional wireless sensor networks (WSNs). In this paper, we consider a UAV-enabled WSN, where a flying UAV is employed to collect data from multiple sensor nodes (SNs). Our objective is to maximize the minimum average data collection rate from all SNs subject to a prescribed reliability constraint for each SN by jointly optimizing the UAV communication scheduling and three-dimensional (3D) trajectory. Different from the existing works that assume the simplified line-of-sight (LoS) UAV-ground channels, we consider the more practically accurate angledependent Rician fading channels between the UAV and SNs with the Rician factors determined by the corresponding UAV-SN elevation angles. However, the formulated optimization problem is intractable due to the lack of a closed-form expression for a key parameter termed effective fading power that characterizes the achievable rate given the reliability requirement in terms of outage probability. To tackle this difficulty, we first approximate the parameter by a logistic (“S” shape) function with respect to the 3D UAV trajectory by using the data regression method. Then, the original problem is reformulated to an approximate form, which, however, is still challenging to solve due to its nonconvexity. As such, we further propose an efficient algorithm to derive its suboptimal solution by using the block coordinate descent technique, which iteratively optimizes the communication scheduling, the UAV’s horizontal trajectory, and its vertical trajectory. The latter two subproblems are shown to be non-convex, while locally optimal solutions are obtained for them by using the successive convex approximation technique. Finally, extensive numerical results are provided to evaluate the performance of the proposed algorithm and draw new insights on the 3D UAV trajectory under the Rician fading as compared to conventional LoS channel models.

Index Terms— UAV communication, wireless sensor network, 3D trajectory optimization, logistic function, data regression.

## I. INTRODUCTION

expected to be widely deployed in the future for enabling a proliferation of applications ranging from aerial delivery to surveillance and monitoring, disaster rescue, and remote sensing [1]–[3]. Among others, dispatching UAVs to harvest sensing-data from distributed sensor nodes (SNs) is anticipated to be a promising technology for realizing the future Internet of Things (IoT). Different from conventional wireless sensor networks (WSNs) that rely on static data collecting nodes and multihop data relaying among the SNs, the UAV-enabled WSN leverages a mobile data collector mounted on the UAV that communicates with the SNs directly by exploiting the line-ofsight (LoS) dominant UAV-ground channels. This helps not only significantly improve the WSN coverage and throughput, but also effectively reduce energy consumption of the SNs by scheduling their transmissions based on the UAV’s trajectory. Such advantages have attracted growing research attention in recent years on UAV-enabled WSNs, including the designs of UAV trajectory, SN wakeup schedule, trajectory-aware signal modulation and coding, etc [4]–[12]. In particular, for the trajectory design in UAV-enabled WSNs, most of the existing works (e.g., [6]–[12]) assumed that the UAV flies at a fixed (minimum) altitude and thus only the two-dimensional (2D) UAV trajectory was considered. In contrast, our current work further exploits the vertical trajectory of the UAV and presents a new design framework of three-dimensional (3D) UAV trajectory to further improve the rate performance in UAVenabled WSNs.

Besides UAV-enabled WSNs, UAV trajectory design has been widely investigated in other wireless networks, such as UAV-assisted terrestrial communication [13]–[16], relay systems [17], cellular networks [18], radio access networks [19], and wireless power transfer networks [20]. The UAV trajectory design critically relies on the UAV-ground channel modelling. Among others, there are three commonly adopted channel models in the literature, including the LoS channel, probabilistic LoS channel, and Rician fading channel. Particularly, as the UAV at a sufficiently high altitude has a high likelihood to establish an LoS link with the ground node [21], the deterministic LoS channel following the free-space pathloss model has been widely used in most of the existing works on the UAV trajectory design (see e.g., [6]–[12]) due to its convenience for optimization. However, such a simplified model may be practically inaccurate in urban/suburban areas, as it neglects the stochastic shadowing and small-scale fading. Considering shadowing, the signal propagation can be blocked by obstacles (e.g., buildings) in urban areas and thereby the UAV-ground channels can be largely categorized into either LoS or non-LoS (NLoS) link at different locations with different characteristics. To avoid the excessive measurement cost for attaining the complete information of LoS/NLoS channels at all locations in a large geographical area, a statistical probability based model for the occurrence of LoS/NLoS channels was proposed in [22] as a logistic function, whose parameters are determined by the specific environment and the elevation angle of the UAV. Based on this empirical model, substantial research has been conducted for designing the 3D UAV placement to optimize the communication performance in terms of coverage, throughput, delay, and reliability (see e.g., [23]–[28] and the references therein). This channel model, although being suitable for communication performance analysis, cannot be directly applied to design UAV trajectory. The reason is that along the UAV trajectory, the LoS probability in a local region generally is not identical to that averaged over the whole area of interest, and it is also spatially correlated depending on the surrounding environment. The work [29] made the first attempt to tackle this difficulty by learning the local channel parameters and constructing a local 3D radio map, based on which the UAV trajectory was designed by a novel map compression method. Another widely adopted model is the Rician fading model that comprises a deterministic LoS component and a random multipath component due to reflection, scattering, and diffraction by the ground obstacles [30]. This model is suitable for urban/suburban areas with the UAV at a sufficiently high altitude with less shadowing but non-negligible small-scale fading. The Rician factor, as reported in [31], is affected by the communication band (L/C band), surrounding environment, and the UAV-ground elevation angle. As the elevation angle enlarges, the experimental results in [32] show that the Rician factor tends to exponentially increase since a larger elevation angle is likely to incur less ground reflection, scattering, and obstruction. Such an (elevation) angle-dependent Rician fading model is more practically accurate than the conventional simplified LoS model, but the UAV trajectory design under this model has not yet been investigated in the existing literature. This thus motivates our current work as the first attempt to design the 3D UAV trajectory in the angle-dependent Rician fading channel.

Specifically, in this paper, we consider a UAV-enabled WSN where a UAV flies over multiple SNs to collect data from them. The SNs are normally in the silent mode for energy saving and transmit data only when being waken up by the UAV (e.g., by broadcasting a beacon signal) and scheduled for transmission. Our objective is to maximize the minimum average data collection rate from all SNs, while ensuring that the sent data is reliably received by the UAV with an outage probability less than a prescribed value. Compared with the existing works on UAV trajectory design relying on the simplified LoS channel model, adopting the angle-dependent Rician fading channel model introduces new design issues. First, as the UAV-SN channel is not fully predictable along the UAV trajectory due to the random small-scale fading, we should consider an outage-aware adaptive-rate transmission scheme. However, the relationship between the resultant achievable rate and the UAV trajectory is non-trivial due to the distancedependent pathloss and angle-dependent Rician factor. Second, unlike the conventional 2D trajectory designs with a fixed UAV altitude, the elevation angle-dependent Rician fading calls for a joint optimization of both the horizontal and vertical UAV trajectories, leading to the said 3D UAV trajectory design. Tackling these key issues yields the main contributions of this paper as summarized below.

• First, we formulate an optimization problem to maximize the minimum data collection rate from all SNs with an outage probability guarantee for each SN by jointly designing the UAV communication scheduling and 3D trajectory. This problem, however, is intractable due to the lack of a closed-form expression for a key parameter termed effective fading power, which characterizes the achievable rate in the fading channel under the given outage probability constraint. To address this difficulty, by leveraging the data regression method, we approximate the effective fading power by a logistic function with respect to (w.r.t.) the 3D UAV trajectory, and then reformulate the original problem into a tractable form.

• Next, we propose an efficient algorithm for solving the reformulated non-convex problem. Specifically, we first apply continuous relaxation to the integer UAV scheduling constraint and then solve the relaxed problem by using the block coordinate descent (BCD) technique that iteratively optimizes the UAV communication scheduling, horizontal trajectory, and vertical trajectory. Since the subproblems for optimizing the UAV horizontal and vertical trajectories are still non-convex, the successive convex approximation (SCA) technique is applied to derive the locally optimal solutions to them.

• Last, numerical results are provided to evaluate the performance of the proposed algorithm and compare the optimized UAV trajectories under the considered Rician fading and conventional LoS channel models. We show that for the case with one single SN, the proposed UAV trajectory can exploit the vertical trajectory (altitude variation) to enhance the data collection rate, especially given a high maximum vertical speed and a stringent outage probability requirement. Moreover, the designed UAV trajectory is close to that assuming the LoS channel when the Rician fading approaches to either the Rayleigh fading or LoS channel. Furthermore, for the case with multiple SNs, by leveraging the angle-aware joint horizontal and vertical trajectory design, the proposed 3D UAV trajectory can significantly enhance the performance over the conventional trajectory assuming the simplified LoS channel.

The remainder of this paper is organized as follows. Section II presents the system model and problem formulation. In Section III, the effective-fading-power function is approximated by a logistic form, based on which the optimization problem is reformulated. Subsequently, we propose an efficient algorithm for solving the reformulated problem in Section IV. Numerical results are provided in Section V, followed by the conclusions in Section VI.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

Consider a UAV-enabled WSN as shown in Fig. 1 with a UAV flying over N ground SNs and collecting data from them within a given time duration of $T .$ The SNs are indexed by the set $\mathcal { N } = \{ 1 , \cdots , N \}$ and their individual location is represented by the 3D Cartesian coordinate $( \mathbf { w } _ { n } ^ { T } , 0 )$ ∀ $n \in \mathcal N .$ with $\mathbf { w } _ { n } = [ x _ { n } , y _ { n } ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 }$ denoting the horizontal coordinate. The UAV’s initial and final locations are predetermined, represented by $( \mathbf { q } _ { 0 } ^ { T } , z _ { 0 } )$ and $\bigl ( \mathbf { q } _ { F } ^ { T } , z _ { F } \bigr )$ respectively, where $\mathbf { q } _ { 0 } ^ { T } \in \mathbb { R } ^ { 1 \times 2 }$ and $\mathbf { q } _ { F } ^ { T } \in \mathbb { R } ^ { 1 \times 2 }$ denote the <sup>0</sup>horizontal coordinates, and $z _ { \mathrm { 0 } }$ and $z _ { F }$ are the corresponding altitudes. Assuming that the UAV has prior information of all SNs’ locations, we jointly design the UAV communication scheduling and 3D trajectory for maximizing the minimum average data collection rate from all SNs, under the constraints on the UAV communication scheduling and 3D trajectory, while ensuring data being reliably received by the UAV under a given tolerable outage probability.

![](images/9d579d61ec62c8708f11a58eb7787e1b3670bddd864f22507d8f9e45126e503c.jpg)  
Fig. 1. UAV-enabled data collection.

## A. UAV Trajectory Model

For ease of exposition, the time horizon T is discretized into M equal time slots, indexed by $\mathcal { M } \ = \ \{ 1 , \cdots , M \}$ The elemental slot length $\delta \ : = \ : T / M$ is appropriately cho-<sup>=</sup>sen such that the UAV’s location can be assumed to be approximately unchanged within each time slot. Then the UAV trajectory can be approximated by an $( M + 1 )$ -length 3D sequence $\mathbf { \bar { \{ ( q [ m ] ^ { T } , } }  \bar { z [ m ] ) } \}$ }, with $\mathbf { q } [ m ] = [ x [ m ] , y [ m ] ] ^ { T }$ <sup>( [ ] [ ]) [ ] = [ [ ] [ ]]</sup>and z m respectively denoting the horizontal and vertical coordinates. Assume that the UAV can independently control the horizontal and vertical flying speeds with the maximum speeds denoted by $V _ { \mathrm { x y } }$ and $V _ { \mathrm { { z } } }$ in meter/second (m/s), respectively [33]. Then the maximum horizontal and vertical flying distances within each time slot are $S _ { \mathrm { x y } } ~ = ~ V _ { \mathrm { x y } } \delta$ and $S _ { \mathrm { z } } ~ =$ $V _ { \mathrm { z } } \delta ,$ respectively, leading to the following UAV flying speed constraints:

$$
| | \mathbf { q } [ m + 1 ] - \mathbf { q } [ m ] | | \leq S _ { \mathrm { x y } } \quad { \mathrm { a n d ~ } } | z [ m + 1 ] - z [ m ] | \leq S _ { \mathrm { z } } ,
$$

$\forall m \ \in \ { \mathcal { M } }$ . In addition, the predetermined initial and final locations for the UAV enforce:

$$
\begin{array} { r } { ( \mathbf q [ 1 ] ^ { T } , z [ 1 ] ) = ( \mathbf q _ { 0 } ^ { T } , z _ { 0 } ) \quad \mathrm { a n d } ( \mathbf q [ M + 1 ] ^ { T } , z [ M + 1 ] ) = ( \mathbf q _ { F } ^ { T } , z _ { F } ) . } \end{array}
$$

Last, to avoid obstacles and maintain the LoS paths between the UAV and SNs, the UAV is required to fly

above the SNs with a minimum altitude H, leading to: $z [ m ] \geq H$ , ∀m.

## B. UAV-Ground Channel Model

We consider the block fading channels for the UAV-SN links, where the channel remains unchanged within each fading block and independently changes over different blocks. As the duration of each fading block is typically much smaller than that of each time slot, we assume each time slot consisting of $L > 1$ fading blocks. As reported in practical experiments, the UAV at a sufficiently high altitude is likely to establish LoS links with the ground SNs and also experiences smallscale fading due to rich scattering [34]. Therefore, the channel between each SN, say SN n, and the UAV in the -th fading block of time slot m can be modeled as

$$
h _ { n } [ m , \ell ] = \sqrt { \beta _ { n } [ m ] } g _ { n } [ m , \ell ] ,\tag{1}
$$

where $\beta _ { n } [ m ]$ is the large-scale average channel power gain accounting for signal attenuation including both the pathloss and shadowing and $g _ { n } [ m , \ell ]$ is the small-scale fading coefficient. Specifically, let $d _ { n } [ m ]$ denote the the distance between <sup>[ ]</sup>the UAV and SN n in time slot $m ,$ given by

$$
d _ { n } [ m ] = \sqrt { | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } } .\tag{2}
$$

Then, the average channel power gain, $\beta _ { n } [ m ]$ , can be modeled as

$$
\beta _ { n } [ m ] = \beta _ { 0 } d _ { n } ^ { - \alpha } [ m ] ,\tag{3}
$$

where $\beta _ { 0 }$ is the average channel power gain at a reference distance of $d _ { 0 } = 1$ m, α is the pathloss exponent that usually has a value between 2 and $6 . { } ^ { 1 }$ Next, due to the existence of the LoS path, the small-scale fading can be modeled by the Rician fading below with $\mathbb { E } [ | g [ m , \ell ] | ^ { 2 } ] = 1$

$$
g _ { n } [ m , \ell ] = \sqrt { \frac { \tilde { K } _ { n } [ m , \ell ] } { \tilde { K } _ { n } [ m , \ell ] + 1 } } g + \sqrt { \frac { 1 } { \tilde { K } _ { n } [ m , \ell ] + 1 } } \tilde { g } ,\tag{4}
$$

where g denotes the deterministic LoS channel component with $| g | \ = \ 1 , \ \tilde { g }$ represents the random scattered component which is a zero-mean unit-variance circularly symmetric complex Gaussian (CSCG) random variable, and $\tilde { K } _ { n } [ m , \ell ]$ denotes the Rician factor of the channel between SN n and the UAV in the -th fading block of time slot m. Note that due to the mobility of the UAV, the Rician factors for SN n in different time slots are in general non-identical, which is closely related to the elevation angle between the SN and the UAV (see Fig. 1) as reported in prior experiments [32]. Particularly, as the elevation angle increases, the UAV-SN link tends to experience less scattering and thus includes a larger portion of LoS component, leading to an increasing Rician factor. Since the elevation angle within each time slot has negligible change, the Rician factors in different fading blocks over the same time slot are assumed identical, i.e., $\tilde { K } _ { n } [ m , \ell ] =$ <sup>[ ] =</sup>, ∀. In other words, the channels in the same time slot

<sup>1</sup>In general, for UAV communications, the pathloss exponent and variance of random shadowing are also functions of the elevation angle between the UAV and SN, but are assumed constant in the current work for tractable analysis.

are identically distributed. Based on the experimental results in [32], the angle-dependent Rician factor can be modeled by the following exponential function:

$$
K _ { n } [ m ] = A _ { 1 } \exp ( A _ { 2 } \theta _ { n } [ m ] ) ,\tag{5}
$$

where $\theta _ { n } [ m ]$ is the elevation angle given by

$$
\theta _ { n } [ m ] = \arcsin ( z [ m ] / d _ { n } [ m ] ) ,\tag{6}
$$

$A _ { 1 }$ and $A _ { 2 }$ are constant coefficients determined by the specific environment. Then we have $K _ { \mathrm { m i n } } \leq K _ { n } [ m ] \leq K _ { \mathrm { m a x } } ,$ where $K _ { \operatorname* { m i n } } = A _ { 1 }$ and $K _ { \operatorname* { m a x } } = A _ { 1 } e ^ { A _ { 2 } \pi / 2 }$ . It is worth noting that, for each SN, the distributions of the small-scale fading in different time slots are correlated and determined by the 3D UAV trajectory, which can be observed from (4)–(6), making the optimization problem formulated in the sequel highly challenging to solve.

## C. Data Collection Model

Assume that each SN transmits data with a constant transmit power $P _ { n }$ only when being waken up by the UAV and scheduled for transmission, and otherwise keeps in the silent mode for energy saving. Let $a _ { n } [ m ]$ denote the binary UAV communication scheduling for SN n in time slot $m ,$ where the SN wakes up if $a _ { n } [ m ] = 1$ and sleeps otherwise. Assume that only one SN is scheduled for transmission in each time slot, leading to the following scheduling constraints:

$$
\begin{array}{c} \sum _ { n = 1 } ^ { N } a _ { n } [ m ] \leq 1 , \forall m \in { \mathcal { M } } , \mathrm { a n d }  \\ { a _ { n } [ m ] \in \{ 0 , 1 \} , \forall n \in { \mathcal { N } } , m \in { \mathcal { M } } . } \end{array}
$$

At the beginning, the UAV determines its trajectory $\{ \mathbf { q } [ m ] , z [ m ] \}$ and communication scheduling $\{ a _ { n } [ m ] \}$ using the knowledge of SNs’ locations, which is assumed to be known at the UAV. Then along the flying trajectory, the UAV wakes up the corresponding SN in each time slot and informs it the transmission rate via the downlink reliable control channel. Consider data transmission for each SN, say SN n. In each time slot m, if the SN is waken up, the maximum achievable rate at the UAV from the SN during the -th fading block of time slot m, denoted by $C _ { n } [ m , \ell ]$ in bits/second/Hertz (bps/Hz), is given as

$$
C _ { n } [ m , \ell ] = \log _ { 2 } { \left( 1 + \frac { | h _ { n } [ m , \ell ] | ^ { 2 } P _ { n } } { \sigma ^ { 2 } \Gamma } \right) } ,\tag{7}
$$

where $\sigma ^ { 2 }$ is the receiver noise power and $\Gamma > 1$ denotes the signal-to-noise ratio (SNR) gap between the practical modulation-and-coding scheme and the theoretical Gaussian signaling. However, for UAV trajectory design, the above rate is not exactly known due to the lack of the knowledge for instantaneous channels (i.e., $\{ h _ { n } [ m , \ell ] \} ,$ ) prior to the UAV’s <sup>[ ]</sup>flight. Since the SN-UAV channel is independent and identically distributed (i.i.d.) in the fading blocks of the same time slot and non-identically distributed in different time slots, we consider the adaptive-rate transmission scheme at the SNs. To be specific, each SN transmits data at a fixed rate $R _ { n } [ m ]$ in the fading blocks of the same time slot and different rates over different time slots. Therefore, the outage probability that the UAV cannot successfully receive the transmitted data from SN n in the -th fading block of time slot m can be expressed by

$$
\begin{array} { r l } & { p _ { n } [ m , \ell ] = \mathbb { P } ( C _ { n } [ m , \ell ] < R _ { n } [ m ] ) } \\ & { \quad \quad = \mathbb { P } \bigg ( | g _ { n } [ m , \ell ] | ^ { 2 } < \frac { \sigma ^ { 2 } \Gamma ( 2 ^ { R _ { n } [ m ] } - 1 ) } { \beta _ { n } [ m ] P _ { n } } \bigg ) } \\ & { \quad \quad = F _ { n , m } \bigg ( \frac { \sigma ^ { 2 } \Gamma ( 2 ^ { R _ { n } [ m ] } - 1 ) } { \beta _ { n } [ m ] P _ { n } } \bigg ) , } \end{array}\tag{8}
$$

where $F _ { n , m } ( u )$ denotes the cumulative distribution function (cdf) of the random variable $| g _ { n } [ m , \ell ] | ^ { 2 }$ which is a nondecreasing function w.r.t. $R _ { n } [ m ]$ . For Rician fading, the cdf of $| g _ { n } [ m , \ell ] | ^ { 2 }$ can be explicitly expressed as

$$
F _ { n , m } ( u ) = 1 - Q _ { 1 } \biggl ( \sqrt { 2 K _ { n } [ m ] } , ~ \sqrt { 2 ( K _ { n } [ m ] + 1 ) u } \biggr ) ,\tag{9}
$$

where $Q _ { 1 } ( x , y )$ is the standard Marcum-Q function. Note <sup>1( )</sup>that in the same time slot, the outage probability of SN $n ,$ $p _ { n } [ m , \ell ] ,$ , is identical over different fading blocks and thus is re-denoted by $p _ { n } ^ { \mathrm { o u t } } [ m ]$ . To maximize the data collection rate and ensure the transmitted data from all SNs in different fading blocks being reliably received by the UAV, $R _ { n } [ m ]$ is chosen such that $p _ { n } ^ { \mathrm { o u t } } [ m ] = \epsilon , \forall n , m .$ , where  is the maximum tolerable outage probability which is typically in the range of $0 ~ < ~ \epsilon ~ \le ~ 0 . 1$ in practice. Combining (8) and (3) with $p _ { n } [ m , \ell ] = \epsilon$ <sup>0 1</sup>yields the outage-aware achievable rate $R _ { n } [ m ]$ given by:

$$
R _ { n } [ m ] = \log _ { 2 } { \bigg ( 1 + \frac { f _ { n } [ m ] \gamma _ { n } } { ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } ) ^ { \alpha / 2 } } \bigg ) } ,\tag{10}
$$

where $\begin{array} { r } { \gamma _ { n } \ \stackrel { \triangle } { = } \ \frac { P _ { n } \beta _ { 0 } } { \sigma ^ { 2 } \Gamma } } \end{array}$ and $f _ { n } [ m ]$ denotes the unique solution to $F _ { n , m } ( u ) \stackrel { } { = } \stackrel {  } { \epsilon } .$ When $F _ { n , m } ( 1 ) < \epsilon .$ , we set $f _ { n } [ m ] = 1$ It is worth noting that given a fixed maximum tolerable outage probability, $f _ { n } [ m ]$ is determined by the cdf $F _ { n , m } ( u )$ which in turn implicitly depends on the 3D UAV trajectory $\{ \mathbf { q } [ m ] , z [ m ] \}$ via the Rician factor $K _ { n } [ m ]$ and the elevation <sup>[ ]</sup>angle $\theta _ { n } [ m ]$ , as shown in (2)–(6) and (8)–(9). As a result, $f _ { n } [ m ]$ can be equivalently denoted as a function of the UAV trajectory: $f _ { n } [ m ] = \varphi _ { n } ( \mathbf { q } [ m ] , z [ m ] )$ where the function $\varphi _ { n } ( x , y )$ , however, has no explicit form and will be approximated in the sequel. Intuitively, $f _ { n } [ m ]$ can be understood as the effective fading power that guarantees reliable transmission of SN n given the outage probability requirement leading to the achievable rate given in (10), and thus is termed as effective fading power. As such, $\varphi _ { n } ( \mathbf { q } [ m ] , z [ m ] )$ is called the effectivefading-power function.

## D. Problem Formulation

Our objective is to maximize the minimum average data collection rate from all SNs under the constraints on the UAV communication scheduling and 3D trajectory, while ensuring data being reliably collected given the maximum tolerable outage probability. Based on the preceding models, this problem can be formulated as

follows.

<sub>(</sub><sup>P1</sup><sub>)</sub>

$$
\begin{array} { r l r } {  { \int \operatorname* { m a x } } } \\ & { } & { \{ \mathbf { q } [ m ] , z [ m ] , \} , \eta } \\ & { } & { \mathrm { s . t . } \ \frac { 1 } { M } \displaystyle \sum _ { m = 1 } ^ { M } a _ { n } [ m ] \log _ { 2 } } \\ & { } & { \times ( 1 + \frac { \varphi _ { n } ( \mathbf { q } [ m ] , z [ m ] ) \gamma _ { n } } { ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } ) ^ { \alpha / 2 } } ) } \\ & { } & { \geq \eta , \forall n \in \mathcal { N } , \qquad ( 1 1 \mathrm { a } } \end{array}
$$

$$
| | \mathbf { q } [ m + 1 ] - \mathbf { q } [ m ] | | \leq S _ { \mathrm { x y } } , \forall m \in \mathcal { M } ,\tag{11b}
$$

$$
| z [ m + 1 ] - z [ m ] | \leq S _ { \mathrm { z } } , \forall m \in \mathcal { M } ,\tag{11c}
$$

$$
\begin{array} { r } { ( \mathbf q [ 1 ] ^ { T } , z [ 1 ] ) = ( \mathbf q _ { 0 } ^ { T } , z _ { 0 } ) , } \end{array}\tag{11d}
$$

$$
( \mathbf { q } [ M + 1 ] ^ { T } , z [ M + 1 ] ) = ( \mathbf { q } _ { F } ^ { T } , z _ { F } ) ,\tag{11e}
$$

$$
z [ m ] \geq H , \forall m \in \mathcal { M } ,\tag{11f}
$$

$$
\sum _ { n = 1 } a _ { n } [ m ] \leq 1 , ~ \forall m \in { \mathcal { M } } ,\tag{11g}
$$

$$
a _ { n } [ m ] \in \{ 0 , 1 \} , \forall n \in \mathcal { N } , m \in \mathcal { M } .\tag{11h}
$$

Note that the derivation for the optimal solution to Problem P1 is intractable due to the lack of a closedform expression for the effective-fading-power function, $\varphi _ { n } ( \mathbf { q } [ m ] , z [ m ] )$ which can be observed from (9) since $f _ { n } [ m ] = \varphi _ { n } ( { \bf q } [ m ] , z [ m ] )$ is the inverse of the standard <sup>[ ] = ( [ ] [ ])</sup>Marcum-Q function whose exact value can only be computed by iterative algorithms (e.g., [35]). As a result, the rate constraint (11a) relates to the 3D UAV trajectory variables, $\{ \mathbf { q } [ m ] , z [ m ] \}$ , in an implicit manner. Moreover, the UAV scheduling variables, $\{ a _ { n } [ m ] \}$ , are binary and hence incur the integer constraint (11h). To address these issues, we propose an efficient algorithm to derive a suboptimal solution to Problem P1. The key idea is to firstly reformulate the optimization problem by approximating the effective-fading-power function in a tractable form, and then design efficient UAV scheduling and 3D trajectory by solving the reformulated problem, which are elaborated in the following sections.

## III. APPROXIMATION FOR EFFECTIVE FADING POWER AND PROBLEM REFORMULATION

In this section, we approximate the effective-fading-power function by using the logistic regression method, based on which the optimization problem is reformulated.

## A. Approximation for Effective Fading Power

The intractability for the effective-fading-power function is due to the lack of an explicit form for the inverse Marcum-Q function. This issue can be addressed by approximating the inverse Marcum-Q function as derived in [36]. Combining it with (9) yields the result given in the following lemma. In this subsection, the superscripts of notations are omitted for ease of exposition without incurring confusion.

Lemma 1: Considering practical outage probability requirement $( \mathrm { e . g . , 0 < \epsilon \leq 0 . 1 ) }$ , the effective fading power $f$ can be approximated in the following closed form by using the approximation for the inverse Marcum-Q function in [36]:

$$
f \approx \bar { f } \triangleq \frac { w ^ { 2 } } { 2 ( K + 1 ) } ,\tag{12}
$$

where w is given by

$$
w = \left\{ \begin{array} { l l } { \sqrt { - 2 \ln ( 1 - \epsilon ) } e ^ { \frac { K } { 2 } } , } & { K \le \frac { K _ { \mathrm { t h } } ^ { 2 } } { 2 } , } \\ { \sqrt { 2 K } + \frac { 1 } { 2 Q ^ { - 1 } ( \epsilon ) } } \\ { ~ \times \ln \left( \displaystyle \frac { \sqrt { 2 K } } { \sqrt { 2 K } - Q ^ { - 1 } ( \epsilon ) } \right) - Q ^ { - 1 } ( \epsilon ) , } & { K > \frac { K _ { \mathrm { t h } } ^ { 2 } } { 2 } , } \end{array} \right.
$$

$K _ { \mathrm { t h } }$ is the intersection of the sub-functions at $\sqrt { 2 K } > Q ^ { - 1 } ( \epsilon )$ <sup>th</sup>and $Q ^ { - 1 } ( x )$ is the inverse Q-function.

The approximation in Lemma 1 can be shown to be largely accurate by numerical results (omitted for brevity). Nevertheless, although Lemma 1 approximates the effective fading power $f$ in an explicit form, it still relates with the 3D UAV trajectory $\{ \mathbf { q } , z \}$ in a complicated manner via the Rician factor and elevation angle, which can be observed from (12), (13), and (2)–(6). This makes it hard to characterize the effects of 3D UAV trajectory on the effective fading power and hence on the outage-aware achievable rate, and in turn renders the optimization problem still challenging to solve.

To overcome this difficulty, in this work, we apply the data regression method to directly approximate the effective-fadingpower function w.r.t. the 3D UAV trajectory, which comprises the following two key procedures.

1. Model selection: We first generate the numeral data for f according to (2)–(6), (8) and (9), and plot the curves of f versus (vs.) v under different maximum Rician factors and maximum tolerable outage probabilities as shown in Fig. 2 (dash lines), where v is called angle indicator defined as $\begin{array} { r } { v \triangleq \sin ( \theta ) = \frac { z } { \sqrt { | | \mathbf { q } - \mathbf { w } | | ^ { 2 } + z ^ { 2 } } } } \end{array}$ . Several important observations are listed as follows.

(i) $f _ { \operatorname* { m i n } } \leq f \leq 1$ , where $0 \leq f _ { \operatorname* { m i n } } \leq 1$

(ii) f is monotonically non-decreasing with v.

(iii) For large $K _ { \mathrm { m a x } } .$ , as v increases, the derivative of f would increase to a maximum value and then decrease.

The above observations indicate that the effective-fadingpower function should have an $\mathbf { \partial } ^ { \ast } \mathbf { S } ^ { \ast }$ shape w.r.t. v and within the range of $[ f _ { \operatorname* { m i n } } , 1 ]$ . This suggests to approximate the effective-fading-power function by the following logistic model:

$$
\begin{array} { r l } & { f \approx \tilde { f } = \tilde { \varphi } ( \mathbf { q } , z ) } \\ & { \begin{array} { l } { \triangleq C _ { 1 } + \frac { C _ { 2 } } { 1 + e ^ { - ( B _ { 1 } + B _ { 2 } \ v ) } } } \\ { = C _ { 1 } + \frac { C _ { 2 } } { 1 + \exp { \left( - \left( B _ { 1 } + B _ { 2 } \frac { z } { \sqrt { | | \mathbf { q } - \mathbf { w } | ^ { 2 } + z ^ { 2 } } } \right) \right) } } , } \end{array} } \end{array}\tag{13}
$$

where the coefficients $B _ { 1 } < 0$ reflects the positive logistic mid-point, $B _ { 2 } > 0$ is the logistic growth rate, $C _ { 1 } > 0$ and $C _ { 2 } > 0$ satisfy $C _ { 1 } + C _ { 2 } = 1$

![](images/00a2024d40f08675f83ecde35026cdd166aa6cca6c933d617b2b7df9e5e8b9c1.jpg)  
(a) Maximum tolerable outage probability = 0.01.  
Fig. 2. Comparisons between numerical data and the logistic model with $K _ { \mathrm { m i n } } = 0 ~ \mathrm { d B } .$

2. Model evaluation: Next, to evaluate the logistic model, we choose the model parameters based on the criterion of minimum mean square error and fit the model to the numerical data as shown in Fig. 2 (solid lines). It can be observed that the proposed logistic model in (13) matches the numerical data in most cases.

Compared with (12), the newly approximated effectivefading-power function in (13) is much more tractable and thus can facilitate characterizing its relationship with the 3D UAV trajectory $( \tilde { f }$ is also called effective fading power in the sequel for brevity without causing confusion). In particular, if the horizontal distance is much larger than the UAV altitude, we have v ≈ and the smallest effective fading power is $\begin{array} { r l } { \tilde { f } _ { \mathrm { m i n } } = C _ { 1 } + \frac { C _ { 2 } } { 1 + e ^ { - B _ { 1 } } } } \end{array}$ . On the other hand, if the UAV is right <sup>1</sup>above the SN, $\mathrm { i . e . , } \left| \left| \mathbf { q } \mathbf { - } \mathbf { w } \right| \right| = 0$ , we have v and $\tilde { f }$ achieves its maximum value $\begin{array} { r } { \tilde { f } _ { \mathrm { m a x } } = C _ { 1 } + \frac { C _ { 2 } } { 1 + e ^ { - ( B _ { 1 } + B _ { 2 } ) } } } \end{array}$ . In other cases, <sup>1+</sup>the effective fading power increases with the angle indicator v following the ${ \bf \bar { S } } ^ { \prime }$ shape. This shape indicates that in the small elevation-angle regime, slightly enlarging the elevation angle can significantly enhance the effective fading power, but the improvement diminishes after the angle indictor exceeds a certain threshold.

The specific logistic model is essentially determined by the maximum tolerable outage probability and Rician factor coefficients. Their effects on the effective fading power can be observed from Fig. 2, which are summarized as follows.

1. Effects of maximum tolerable outage probability: First, given the elevation angle and Rician factor coefficients $\{ K _ { \operatorname* { m i n } } , K _ { \operatorname* { m a x } } \}$ , a larger maximum tolerable outage probability results in a higher effective fading power. This implies that the SN can transmit data at a higher rate when the outage probability requirement relaxes. Second, comparing Figs. 2(a) and 2(b), we can observe that for the case with a more tolerable outage requirement, it has a larger minimum effective fading power at $v = 0$ and thus the improvement on the effective fading power by increasing the elevation angle is more limited.

2. Effects of maximum Rician factor: We can observe from both Figs. 2(a) and 2(b) that for the case with a larger maximum Rician factor $K _ { \mathrm { m a x } }$ , the effective fading power grows faster in the small elevation-angle regime and saturates to its maximum value earlier. This infers that if $K _ { \mathrm { m a x } } ~  ~ \infty$ , the Rician fading can be approximated as the LoS channel and we have $\stackrel { \triangledown } { \hat { f } } \approx 1$ for almost all elevation angles. On the other hand, if $K _ { \mathrm { m a x } } =$ $K _ { \operatorname* { m i n } }  0$ , the Rician fading reduces to Rayleigh fading <sup>m</sup>and $\begin{array} { r } { \tilde { f } = C _ { 1 } + \frac { C _ { 2 } } { 1 + e ^ { - B _ { 1 } } } } \end{array}$ for all elevation angles. Therefore, <sup>1+</sup>in these two extreme cases, enlarging the elevation angle cannot bring significant improvement on the effective fading power.

(b) Maximum tolerable outage probability = 0.1.  
![](images/527a1dcde9b0a0be49f268a3e449d212980a8ff90c246b942ffe678dc358bd68.jpg)

## B. Problem Reformulation

Based on the logistic modelling for the effective-fadingpower function, the achievable rate given the prescribed outage probability requirement, $R _ { n } [ m ]$ in (10), can be approximated by

$$
\begin{array} { l } { { R _ { n } [ m ] \approx \tilde { R } _ { n } [ m ] } } \\ { { \ \stackrel { \triangle } { = } \log _ { 2 } \bigg ( 1 + \bigg ( C _ { 1 } + \frac { C _ { 2 } } { 1 + e ^ { - ( B _ { 1 } + B _ { 2 } v _ { n } [ m ] ) } } \bigg ) } } \\ { { \times \left( \frac { \gamma _ { n } } { ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } ) ^ { \alpha / 2 } } \right) \bigg ) , } } \end{array}\tag{14}
$$

and thus Problem P1 is readily reformulated as:

<sub>(</sub><sup>P2</sup><sub>)</sub>

$$
\begin{array} { l } { \displaystyle \int \operatorname* { m a x } _ { { \boldsymbol a } \left[ m \right] , { \boldsymbol v } \left[ m \right] } \cdot \boldsymbol { \eta } } \\ { \displaystyle \left. \begin{array} { c } { \mathbf { q } \left[ m \right] , { \boldsymbol v } \left[ m \right] } \\ { { \boldsymbol a } _ { n } [ m ] , { \boldsymbol v } _ { n } [ m ] } \end{array} \right. , \boldsymbol { \eta } } \\ { \displaystyle \mathrm { s . t . } \ \frac { 1 } { M } \sum _ { m = 1 } ^ { M } a _ { n } [ m ] \tilde { R } _ { n } [ m ] \ge { \boldsymbol \eta } , ~ \forall n , } \\ { \displaystyle v _ { n } [ m ] = \frac { z [ m ] } { \sqrt { | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } } } , ~ \forall n , m , } \\ { \displaystyle ( 1 1 \mathrm { c } ) - ( 1 1 \mathrm { h } ) , } \end{array}\tag{15a}
$$

(15b)

where $\tilde { R } _ { n } [ m ]$ is expressed in (14). Problem P2 is still dif-<sup>[ ]</sup>ficult to solve due to its non-convexity that arises from the coupling among $v _ { n } [ m ] , \ \mathbf { q } _ { n }$ , and $z [ m ]$ in the rate constraint (15a), the non-affine equality constraint (15b), and the integer UAV scheduling constraint (11h). To tackle these difficulties, an efficient algorithm is proposed in the next section for attaining a suboptimal solution to Problem P2.

## IV. PROPOSED ALGORITHM FOR PROBLEM P2

To solve Problem P2, we first relax the integer constraint for the UAV scheduling in (11h), leading to the following optimization problem:

$$
\begin{array} { r l } { \big ( \mathbf { P 3 } \big ) } & { \underset { \left\{ \begin{array} { c } { \mathbf { q } [ m ] , z [ m ] } \\ { a _ { n } [ m ] , v _ { n } [ m ] } \end{array} \right\} , \eta } { \mathrm { m a x } } \eta } \\ & { \qquad \mathrm { s . t . ~ } 0 \leq a _ { n } [ m ] \leq 1 , \forall n , m , } \\ & { \qquad ( 1 1 \mathrm { c } ) - ( 1 1 \mathrm { g } ) , ( 1 5 \mathrm { a } ) , ( 1 5 \mathrm { b } ) . } \end{array}\tag{16a}
$$

Observe that this relaxed problem is still non-convex. Among others, one of the major challenges for solving it is the nonaffine equality constraint (15b). To address it, one important property of Problem P3 is presented as below, which will facilitate the subsequent optimizations.

Lemma 2: The solution to Problem P3 can be obtained by solving Problem P4 formulated below that relaxes the equality constraint (15b) as the inequality constraint:

P4

$$
\begin{array} { r l } & { \underset { \left\{ a _ { n } \left[ m \right] , z _ { n } \left[ m \right] \right\} , \eta } { \mathrm { m a x } } \eta } \\ & { \mathrm { s . t . } ~ v _ { n } [ m ] \leq \frac { z [ m ] } { \sqrt { \left| | { \mathbf { q } } [ m ] - { \mathbf { w } } _ { n } \right| | ^ { 2 } + z [ m ] ^ { 2 } } } , ~ \forall n , m , } \\ & { ( 1 1 \mathrm { c } ) - ( 1 1 \mathrm { g } ) , ( 1 5 \mathrm { a } ) , ( 1 6 \mathrm { a } ) . } \end{array}\tag{17a}
$$

Proof: See Appendix A.

-

The equivalent Problem P4 remains non-convex due to the existence of coupling variables in the constraints. To address this challenge, we propose to derive a suboptimal solution to Problem P4 by applying the BCD and SCA techniques. Specifically, given the 3D UAV trajectory $\{ \mathbf { q } [ m ] , z [ m ] \}$ , the UAV scheduling is optimized by solving a linear programming (LP). For any feasible UAV scheduling and vertical trajectory, we optimize the UAV horizontal trajectory by using the SCA technique. The approach is also applied to optimize the UAV vertical trajectory given any feasible UAV scheduling and horizontal trajectory. These subproblems are solved in the following subsections. Last, we summarize the overall algorithm and its convergence property.

## A. UAV Communication Scheduling Optimization

Given any feasible 3D UAV trajectory $\{ \mathbf { q } [ m ] , z [ m ] \}$ , Problem P4 reduces to:

$$
\begin{array} { r l } { ( \mathbf { P 5 } ) } & { \underset { \{ a _ { n } [ m ] \} , \eta } { \operatorname* { m a x } } ~ \eta } \\ & { \quad \mathrm { s . t . } ~ ( 1 1 \mathbf { g } ) , ( 1 5 \mathrm { a } ) , ( 1 6 \mathrm { a } ) . } \end{array}
$$

Problem P5 is a standard LP which can be efficiently solved by existing solvers, e.g., CVX. Moreover, it can be proved by contradiction that in the optimal solution to Problem P5, the constraints on the UAV scheduling in (11g) for all time slots are active, i.e., $\begin{array} { r } { \sum _ { n = 1 } ^ { N } { a _ { n } ^ { * } [ m ] } = 1 , \breve { \forall } m } \end{array}$

## B. UAV Horizontal Trajectory Optimization

Given any feasible UAV scheduling $\{ a _ { n } [ m ] \}$ and its vertical trajectory $\{ z [ m ] \}$ , Problem P4 can be rewritten as the following optimization problem for the UAV horizontal trajectory:

$$
\begin{array} { r l } { { \bf ( P 6 ) } } & { \underset { \{ { \bf q } [ m ] , v _ { n } [ m ] \} , \eta } { \mathrm { m a x } } \quad \eta } \\ & { \quad \quad \mathrm { s . t . } ~ { \bf q } [ 1 ] = { \bf q } _ { 0 } , \quad { \bf q } [ M + 1 ] = { \bf q } _ { F } , } \\ & { \quad \quad \quad ( 1 1 { \bf c } ) , ( 1 5 { \bf a } ) , ( 1 7 { \bf a } ) . } \end{array}\tag{19a}
$$

First, observe that in the rate constraint (15a), $\tilde { R } _ { n } [ m ]$ given in (14) is neither concave nor convex w.r.t. the optimization variables $v _ { n } [ m ]$ and q m . To tackle this difficulty, we first introduce an important lemma as below.

Lemma 3: Given $\gamma , C _ { 1 } , C _ { 2 } \geq 0 .$ , the function $\psi ( x , y ) \ { \overset { \triangle } { = } } \quad$ $\begin{array} { r } { \log _ { 2 } \left( 1 + \left( C _ { 1 } + \frac { C _ { 2 } } { x } \right) \frac { \gamma } { y ^ { \alpha / 2 } } \right) } \end{array}$ is convex w.r.t. $x > 0$ and $y > 0$ Proof: See Appendix B. -

Using Lemma 3, we can easily prove that $\tilde { R } _ { n } [ m ]$ in (14) is a convex function w.r.t. $( 1 { \dot { ~ + ~ } } { \dot { e } } ^ { - ( B _ { 1 } + B _ { 2 } ~ v _ { n } [ m ] ) } )$ and $( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } )$ . Although the constraint (15a) is <sup>( [ ] + [ ] )</sup>still non-convex, we can leverage the SCA technique to derive its convex approximation. To be specific, using the fact that the first-order Taylor approximation of a convex function is a global under-estimator, $\tilde { R } _ { n } [ m ]$ can be lower-bounded as follows.

Lemma 4: For any local UAV horizontal trajectory, $\{ \hat { \bf q } _ { n } [ m ] \}$ , we have

$$
\begin{array} { r l } & { \tilde { R } _ { n } [ m ] \geq \tilde { R } _ { n } ^ { \mathrm { l b } } [ m ] \stackrel { \triangle } { = } \hat { R } _ { n } [ m ] - \hat { \Phi } _ { n } [ m ] ( e ^ { - s _ { n } [ m ] } - e ^ { - \hat { s } _ { n } [ m ] } ) } \\ & { \qquad - \hat { \Psi } _ { n } [ m ] ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } - | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } ) , \forall n , m , } \end{array}
$$

where the equality holds at the point ${ \bf q } [ m ] = \hat { \bf q } [ m ]$ . The coefficients $\bar { \hat { \boldsymbol { R } } } _ { n } [ m ] , \ \hat { \Psi } _ { n } [ m ] , \ \hat { \Phi } _ { n } [ m ]$ , and $\hat { s } _ { n } [ m ]$ are given in Appendix C, and $s _ { n } [ m ]$ <sup>[ ] Φ [ ]</sup>is defined by

$$
s _ { n } [ m ] \stackrel { \triangle } { = } B _ { 1 } + B _ { 2 } v _ { n } [ m ] .\tag{20}
$$

Proof: See Appendix C.

-

Modifying Problem P6 by replacing $\tilde { R } _ { n } [ m ]$ given in (14) with its lower bound in Lemma $\bar { 4 } , \tilde { R } _ { n } ^ { \mathrm { l b } } [ m ]$ , and combing (17a) with (20) yields the following approximate problem:

$$
\begin{array} { r l r } {  { \operatorname* { m a x } } } \\ & { \{ \mathbf { q } [ m ] , s _ { n } [ m ] \} , \eta } \\ & { \{ \mathbf { s } . \mathbf { t } . }  & { \frac { 1 } { M } \sum _ { m = 1 } ^ { M } a _ { n } [ m ] \tilde { R } _ { n } ^ { \mathrm { l b } } [ m ] \geq \eta , \forall n , ( 2 \mathrm { l a } ) } \\ & { } & \\ & { s _ { n } [ m ] \leq B _ { 1 } + B _ { 2 } \frac { z [ m ] } { \sqrt { | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } } } , } \\ & { \quad } & { \forall n , m \qquad \ ( 2 \mathrm { l b } ) } \\ & { \ } & { ( 1 1 \mathrm { c } ) , ( 1 9 \mathrm { a } ) . } \end{array}\tag{<sub>(</sub><sup>P7</sup><sub>)</sub>}
$$

The remaining difficulty for solving Problem P7 is the constraint (21b), for which $\begin{array} { r } { v _ { n } [ m ] = \frac { z \lfloor m \rfloor } { \sqrt { \lvert | \mathbf { q } [ m ] - \mathbf { w } _ { n } \rvert | ^ { 2 } + z [ m ] ^ { 2 } } } } \end{array}$ is not <sup>[ ] + [ ]</sup>concave w.r.t. q m . To address it, one key observation is that $v _ { n } [ m ]$ is convex w.r.t. $( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + \dot { z } [ m ] ^ { 2 } )$ . This useful property allows us to lower-bound $v _ { n } [ m ]$ by using the SCA technique, which is given as follows.

Lemma 5: For any local UAV horizontal trajectory, $\{ \hat { \bf q } _ { n } [ m ] \}$ , we have

$$
\begin{array} { r l } & { v _ { n } [ m ] \geq v _ { n } ^ { \mathrm { l b } } [ m ] \stackrel { \triangle } { = } \hat { v } _ { n } [ m ] } \\ & { \qquad - \hat { \Lambda } _ { n } [ m ] ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } - | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } ) , ~ \forall n , m , } \end{array}\tag{22}
$$

where the equality holds at the point $\mathbf { q } [ m ] = { \hat { \mathbf { q } } } [ m ]$ , and the coefficients $\hat { v } _ { n } [ m ]$ and $\hat { \Lambda } _ { n } [ m ]$ are defined in Appendix D.

<sup>ˆ [ ] Λ [</sup>Proof: See Appendix D.

-

Consequently, Problem P7 can be transformed to the following approximate problem by substituting (22) into (21b):

$$
\begin{array} { r l } { ( \mathbf { P 8 } ) } & { \underset { \{ \mathbf { q } [ m ] , s _ { n } [ m ] \} , \eta } { \operatorname* { m a x } } ~ \eta } \\ & { \quad \quad \mathrm { s . t . } ~ s _ { n } [ m ] \leq B _ { 1 } + B _ { 2 } v _ { n } ^ { \mathrm { l b } } [ m ] , \forall n , m , } \\ & { \quad \quad \quad ( 1 1 \mathrm { c } ) , ( 1 9 \mathrm { a } ) , ( 2 1 \mathrm { a } ) . } \end{array}
$$

Problem P8 is now a convex optimization problem, which can be efficiently solved by using existing solvers, e.g., CVX. It is worthwhile to note that, by approximating the concave constraints with their convex lower bounds, the feasible set of Problem P8 is always a subset of Problem P6. Therefore, solving Problem P8 gives the lower bound of the objective value in Problem P6.

## C. UAV Vertical Trajectory Optimization

Given any feasible UAV scheduling $\{ a _ { n } [ m ] \}$ and its hor-<sup>[ ]</sup>izontal trajectory {q m }, Problem P4 can be rewritten as the following optimization problem for the UAV vertical trajectory:

$$
\begin{array} { r l } { ( { \bf P 9 } ) } & { \underset { \{ z [ m ] , v _ { n } [ m ] \} , \eta } { \mathrm { m a x } } ~ \eta } \\ & { \quad \quad \mathrm { s . t . } ~ z [ 1 ] = z _ { 0 } , ~ z [ M + 1 ] = z _ { F } , } \\ & { \quad \quad \quad ( 1 1 \mathrm { c } ) , ( 1 1 \mathrm { f } ) , ( 1 5 \mathrm { a } ) , ( 1 7 \mathrm { a } ) . } \end{array}\tag{24a}
$$

Observe that Problem P9 has a similar form with Problem P6. Therefore, following a similar procedure as for solving Problem P6 (i.e., applying the SCA technique for the constraint (15a)), Problem P9 can be transformed to the following approximate problem.

$$
\begin{array} { r l r } {  { ( z | \mathbf { m } ) ^ { \mathrm { { n a x } } } \mathbf { m } ) } } \\ & { } & { \mathrm { s . t . } \ \xrightarrow [ M ] { M } \ a _ { \mathrm { n } } [ m ] } \\ & { } & { \quad \times ( \ \tilde { F } _ { \mathrm { { n } } } [ m ] - \ \tilde { \Phi } _ { \mathrm { n } } [ m ] ( e ^ { - s _ { \mathrm { n } } [ m ] } - e ^ { - s _ { \mathrm { n } } [ m ] } )  } \\ & { } & {  - \ \tilde { \Psi } _ { \mathrm { n } } [ m ] ( z | \mathbf { m } ) ^ { 2 } - \bar { z } [ m ] ^ { 2 } ) \ \geq \eta , \ \forall n ,  } \\ & { } & {  ( 2 5 \mathbf { a } )  } \\ & { } & {  s _ { \mathrm { { n } } } [ m ] \leq B _ { 1 } + B _ { 2 } \frac { z [ m ] } { \sqrt { ( | \mathbf { q } | [ m ] - \mathbf { w } _ { \mathrm { n } } | [ 2 + z [ m ] ^ { 2 } ) } }  } \\ & { } & {  \forall n , m ,  } \\ & { } & {  ( 1 \mathrm { c } ) , ( 1 \mathrm { f r } ) , ( 2 4 \mathbf { a } ) ,  } \end{array}\tag{P10}
$$

where $\check { R } _ { n } [ m ] , \ \check { \Phi } _ { n } [ m ] , \ \check { s } _ { n } [ m ]$ and $\check { z } _ { n } [ m ]$ are the coefficients determined by the local vertical trajectory $\{ \hat { z } [ m ] \}$ and can be derived using the similar method as in Appendix C and thus

Algorithm 1 Proposed Algorithm for Problem P2   
1: Initialize $\{ \mathbf { q } [ n ] , z [ n ] \}$ . Let $i = 0$   
2: repeat   
3: Solve Problem P5 for given $\{ \mathbf { q } ^ { i } [ m ] , z ^ { i } [ m ] \}$ , and denote   
the optimal solution as $\{ \alpha _ { n } ^ { i + 1 } [ m ] \} .$   
4: Solve Problem P8 for given $\{ a _ { n } ^ { i + 1 } [ m ] , z ^ { i } [ m ] \}$ , and denote   
the optimal solution as $\{ \mathbf { q } ^ { i + 1 } [ m ] \bar  \}$   
5: Solve Problem P10 for given $\{ \stackrel { - } { a } _ { n } ^ { i + 1 } [ m ] , { \bf q } ^ { i + 1 } [ m ] \}$ , and   
denote the optimal solution as $\{ z ^ { i + 1 } [ m ] \}$   
6: Updata $i = i + 1$   
7: until Converge to a prescribed accuracy.

omitted for brevity. As proved in Appendix E, Problem P10 is a convex optimization problem and thus can be solved by using existing methods, e.g., the interior-point method.<sup>2</sup>

## D. Overall Algorithm, Complexity, and Convergence

Using the results obtained in the previous three subsections, the overall algorithm for computing the suboptimal solution to Problem P2 is summarized in Algorithm 1 with the computation complexity analyzed as follows. In each iteration, the UAV communication scheduling, horizontal trajectory, and vertical trajectory are sequentially optimized using the convex solver based on the interior-point method, and thus their individual complexity can be represented by $\mathcal { O } ( ( N M ) ^ { 3 . 5 } \log ( 1 / \epsilon ) )$ ， $\mathcal { O } ( ( M \bar { + } N M ) ^ { 3 . 5 } \log ( 1 / \bar { \epsilon } ) )$ , and $\mathcal { O } ( ( M + N M ) ^ { 3 . 5 } \log ( 1 / \epsilon ) )$ respectively, given the solution accuracy of $\epsilon > 0 \ [ 3 7 ]$ <sup>(1 ))</sup>. Then <sup>0</sup>accounting for the BCD iterations with the complexity in the order of $\log ( 1 / \epsilon )$ , the total computation complexity of Algorithm 1 is thus $\mathcal { O } ( ( M + N M ) ^ { 3 . 5 } \log ^ { 2 } ( 1 / \epsilon ) )$

Next, we address the convergence of Algorithm 1. Let $\eta ( \{ a _ { n } ^ { i } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} )$ denote the objective value of <sup>( [ ] [ ] [ ] )</sup>Problem P2 in the i-th iteration. Since Problem P5 is optimally solved, we have

$$
\begin{array} { r l } & { \eta ( \{ a _ { n } ^ { i } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \qquad \leq \eta _ { \alpha } ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \end{array}\tag{26}
$$

where $\eta _ { \alpha } ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} )$ denotes the computed objective value of Problem P5. For the optimization of UAV horizontal trajectory, we have

$$
\begin{array} { r l } & { \eta ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \qquad \stackrel { ( a ) } { = } \eta _ { \mathbf { q } } ^ { \mathrm { l b } } ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \qquad \stackrel { ( b ) } { \leq } \eta _ { \mathbf { q } } ^ { \mathrm { l b } } ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \qquad \stackrel { ( c ) } { \leq } \eta ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \end{array}\tag{27}
$$

where $\eta _ { \mathbf { q } } ^ { \mathrm { l b } }$ denotes the objective value of Problem P8, a is <sup>( )</sup>due to the tightness of the first-order Taylor expansions at locally points in Problem P8, b holds since P8 is optimally solved, and c holds because the optimal objective value of Problem P8 is the lower bound of that of Problem P6 (see Section IV-B). Therefore, solving Problem P8 guarantees that the objective value of Problem P6 is non-decreasing. Using the similar derivation procedure as in (27), we have

![](images/39d52e616fc2b64c3737b08e5371f72e16851b20814ec510685f58e086c51bfd.jpg)  
(a) Effects of horizontal distance.

![](images/b2988e7a59db09c2cd3fb1903ca8699696c1b901e133882f7fb1090e3d95cdb7.jpg)  
(b) Effects of altitude.  
Fig. 3. Achievable rates under (a) different horizontal distances and the same altitude (100 m); (b) different altitudes and the same horizontal distance (200 m) with the model parameters given by $B _ { 1 } = - 4 . 3 2 2 1 , B _ { 2 } = 6 . 0 7 5 0 , C _ { 1 } = 0 , \mathrm { a n d } C _ { 2 } = 1$

$$
\begin{array} { r l } & { \eta ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \qquad = \eta _ { z } ^ { \mathrm { l b } } ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \qquad \leq \eta _ { z } ^ { \mathrm { l b } } ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i + 1 } [ m ] \} ) } \\ & { \qquad = \eta ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i + 1 } [ m ] \} ) . } \end{array}\tag{28}
$$

Consequently, combing (26)-(28), we can obtain that

$$
\begin{array} { r l } & { \eta ( \{ a _ { n } ^ { i } [ m ] \} , \{ \mathbf { q } ^ { i } [ m ] \} , \{ z ^ { i } [ m ] \} ) } \\ & { \quad \quad \quad \leq \eta ( \{ a _ { n } ^ { i + 1 } [ m ] \} , \{ \mathbf { q } ^ { i + 1 } [ m ] \} , \{ z ^ { i + 1 } [ m ] \} ) , } \end{array}\tag{29}
$$

which guarantees that the objective value of Problem P2 is non-decreasing over the iterations and thus Algorithm 1 can converge to a locally optimal solution of Problem P2.

Last, it is useful to mention that 1) the initial UAV trajectory can be constructed as the straight flight from the initial location to the final location; and 2) the continuous UAV scheduling obtained from solving Problem P5 can be reconstructed to the binary scheduling using the method in [14] without compromising the optimality.

## V. NUMERICAL RESULTS

In this section, numerical results are provided to characterize the properties of designed 3D UAV trajectory and evaluate the performance of our proposed algorithm. We consider a UAVenabled WSN with SNs randomly and uniformly distributed in a square area of $1 0 0 0 \times 1 0 0 0 ~ \mathrm { m ^ { 2 } } .$ . For ease of illustration, the following results are based on one specific realization of SNs’ locations for both the cases with single and multiple SNs. Unless otherwise stated, the numerical settings are as follows. The UAV is assumed to fly from the initial location 0, 500, 100 m towards the final location 1000, 500, 100 m within $T = 2 6 \ { \mathrm { s } } ,$ with the maximum horizontal and vertical speeds set as $V _ { \mathrm { x y } } = 5 0$ m/s and $V _ { \mathrm { z } } = 2 0$ m/s, respectively. The maximum tolerable outage probability $\epsilon = 0 . 0 1$ and all the SNs transmit data at the same power of $P _ { n } = 0 . 1 \ \mathrm { W } .$ The channel power gain at the reference distance $d _ { 0 } = 1$ m is $\beta _ { 0 } =$ −60 dB, the pathloss exponent is $\alpha = 2 .$ , the receiver noise power $\sigma ^ { 2 } = - 1 0 9 ~ \mathrm { d B m }$ , and the SNR gap $\Gamma = 8 . 2$ dB. Other parameters are set as $H = 1 0 0 \ \mathrm { m } , \delta = 0 . 2 \ \mathrm { s } , \ K _ { \operatorname* { m i n } } = 0 \ \mathrm { d B }$ and $K _ { \operatorname* { m a x } } = 3 0 ~ \mathrm { d B }$

For comparison, we consider three benchmark schemes, namely, 1) LoS-based (LB) scheme, which designs the UAV scheduling and trajectory assuming the simplified LoS channel as in [14]; 2) Rician-fading with the lowest altitude (RFLA) scheme that only optimizes the UAV scheduling and horizontal trajectory proposed in this work without the optimization for the vertical trajectory which is simply set as the lowest altitude, i.e., 100 m; and 3) Rician-fading fixed suboptimal altitude (RFFSA) scheme, which resembles the RFLA scheme but differs in that it selects the best fixed UAV altitude among several candidate altitudes {100, 125, 150, · · · , 300} m. In addition, our proposed algorithm is named as Ricianfading based (RFB) scheme. Note that the (average) max-min rates computed from the corresponding algorithms, named as estimated max-min rates, are incomparable since in practice they may not be achievable. For fair comparison, we consider another performance metric, called achieved max-min rate, which is computed using the precise outage-aware achievable rate in (10) and corresponding computed UAV trajectory and scheduling.

## A. Comparisons of Achievable-Rate Functions

The differences of the optimized UAV trajectories for the LB and RFB schemes essentially arise from their different achievable rates. Compared with the simplified LoS channel model, the achievable rate for the considered Rician fading model given in (14) has an extra term, namely the effective fading power, which is determined by the 3D UAV trajectory. The effects of horizontal distance and altitude on the achievable-rate functions are discussed as follows.

Fig. 3(a) plots the curves of achievable rate vs. the horizontal distance in different channel models given a fixed UAV altitude. It can be observed that as the horizontal distance increases, the achievable rate for the Rician fading model decreases much faster than that of the simplified LoS channel model. This is because for the considered model, reducing the horizontal distance can not only shorten the UAV-SN distance leading to a smaller pathloss as in the case of LoS channel model, but also enlarge the elevation angle yielding a larger effective fading power. This difference implies that if given the vertical trajectory, the UAV should fly closer to the scheduled SNs to further reap the angle gain by increasing the elevation angle. Another observation is that the achievable rate under the LoS channel model is always larger than that under the Rician-fading channel model. The reason is that the previous model ensures zero outage probability and the latter, due to the existence of random small-scale fading, needs to reduce the transmission rate for satisfying the outage probability requirement.

![](images/f6e2540241198da671bc7e7a90a85b937752e3aa1c40d4d4a6493679169cd72a.jpg)  
(a) 3D UAV trajectory.  
Fig. 4. Effectiveness of proposed algorithm.

Fig. 3(b) shows the effects of the UAV altitude on the achievable rates in different channel models. We can observe that, as the altitude increase, the achievable rate under the Rician fading model is firstly increasing and then decreasing, which is significantly different from that under the LoS channel model with a monotonically decreasing rate. The is because except the special case with the UAV right above the SN, raising the UAV to a higher altitude can enlarge the elevation angle leading to a larger effective fading power, but at the same time, result in more pathloss. Consequently, the UAV altitude should be optimized to balance the pathlossand-fading (or distance-and-angle) tradeoff in our considered 3D UAV trajectory design.

## B. Single SN

Next, we consider a special case with only one SN located at , ,  and demonstrate the effectiveness of proposed algorithm. Then for easy of illustration, we focus on the comparison of LB and RFB schemes and evaluate the effects of several parameters on the UAV trajectory design and rate performance, including the time duration, UAV maximum vertical speed, maximum tolerable outage probability, and maximum Rician factor.

1) Effectiveness of Proposed Algorithm: In Fig. 4, we evaluate the effectiveness of proposed algorithm by comparing its rate performance with other benchmark schemes under different y coordinates of final location. First, we can observe that the proposed RFB scheme significantly outperforms the LB scheme in terms of the achieved max-min rate, since it adopts a practical angle-dependent Rician fading model and jointly optimizes the 3D UAV trajectory. Next, as for the RFLA scheme, although it adopts the practical channel model, the UAV vertical trajectory is not jointly optimized with the UAV scheduling and horizontal trajectory, and thereby the scheme cannot fully attain the angle gain as the RFB scheme. Specifically, the RFLA scheme only has marginal rate performance improvement compared with the LB scheme due to the similar horizontal trajectory. Third, the RFFSA achieves larger max-min rates than the RFLA scheme as it further optimizes the fixed UAV altitude, but it still suffers considerable performance loss as compared to the RFB scheme since it cannot adaptively tune the altitude along the trajectory. These observations show the importance of adopting a practical model and joint 3D trajectory optimization. Last, it is observed that the rate performance monotonically decreases with the increase of y coordinate of final location, since the UAV has to spend a longer time duration on flying towards the SN and then the destination, and thus has shorter time to collect data.

2) Effects of Time Duration: Fig. 5(a) shows the optimized UAV trajectories of LB and RFB schemes under different time durations T . Several interesting observations are listed as follows. First, as shown in Fig. 5(a), the proposed UAV horizontal trajectory is almost the same as that assuming the simplified LoS channel. This is because with one single SN, both schemes share the same principle in the horizontal trajectory design, i.e., the UAV flies towards the SN at the maximum horizontal speed, hovers above the SN as long as possible, and then leaves to arrive at the destination in time. This leads to the elevation angle variations along the trajectory shown in Fig. 5(b), i.e., increasing-(constant)-decreasing. Second, compared with the LB scheme, our proposed RFB scheme can exploit an extra degrees-of-freedom (DoF) on the UAV vertical trajectory so as to adaptively adjust its altitude to balance the said distance-and-angle tradeoff. This renders the RFB scheme to achieve a better elevation angle along the trajectory, especially for the case with a short time duration (e.g., 26 s). However, the enlargement of elevation angle diminishes when the time duration is sufficiently long (e.g., 40 s).

The effects of the time duration on the max-min rate are shown in Fig. 5(c), while the instantaneous achieved rates are shown in Fig. 5(d). One can observe that the estimated max-min rate of the proposed RFB scheme is close to the achieved one, while the gap is considerably large for the LB scheme. This observation validates the effectiveness of our proposed regression method. Moreover, it indicates that it is unsuitable to control the transmission rates using the estimated rates obtained from the algorithm assuming the LoS channel, as it would cause unacceptable outage probability due to the ignorance of the small-scale fading. Next, the achieved max-min rate of the LB scheme is only moderately less as compared to that of the RFB scheme in the regime of both short $( \mathrm { e . g . , } T = 2 0 . 2 \ \mathrm { s } )$ and long $( { \mathrm { e . g . , ~ } } T = 4 0 ~ ;$ s) <sup>= =</sup>time durations. The underpinning reason is that in the former case, the UAV in both schemes has limited mobility DoF and thus has to almost fly straightly to the final location, leading to the similar UAV trajectories. Moreover, although the dominant instantaneous-rate regime is when the UAV flies closer to the SN, the proposed scheme only has marginal gain in this regime due to the similar design principle as that of the LB scheme, i.e., reducing the UAV altitude when hovering above the SN. This trend can also be observed in the case with a long time duration, for which the performance gain from the optimized vertical trajectory is diminishing since it can only marginally improve the rates in the non-dominant rate regime. Last, it is worth mentioning that the proposed RFB scheme can achieve substantial performance gain in the regime of moderate time duration, for example, it attains two folds of max-min rate when the time duration T 26 s.

![](images/783dc24f148da26a1a86a9adc684289553b1c649e990cfbf60bfaad62a44ebc6.jpg)  
(a) 3D UAV trajectory

![](images/25d05195a2045ee613300e546314b3663b4643030d5792c7e5acaa19feb32a39.jpg)  
(b) UAV elevation angle.

![](images/826a57eddb98412c00daca784bef8fa9c20cb852b078301d965ef08edb1cb60d.jpg)  
(c) Max-min rate vs. time duration.

![](images/af22946181c0530d6c9f08c0dca0a953c8811f07339bedcd9e8a3a467750c761.jpg)  
(d) Instantaneous achieved rate

Fig. 5. Comparison of the UAV trajectories and rate performance in different schemes under different time durations.  
![](images/3707161fb9bf72585ac9e707aa8dc692f2d6b71f68fbb2cd1e65d620c0491245.jpg)  
(a) 3D UAV trajectory

![](images/65688bcc1a826a363cb452668f20f3e92dd5814c3999efe55df714b516176ed1.jpg)  
(b) Max-min rate vs. UAV maximum vertical speed.  
Fig. 6. Comparison of the UAV trajectories and rate performance in different schemes under different maximum vertical speeds.

3) Effects of UAV Maximum Vertical Speed: In Fig. 6(a), we plot the UAV trajectories of the LB and RFB schemes under different maximum vertical speeds. Observe that with a higher maximum vertical speed, the UAV has more DoF to fly upwards and downwards for balancing the distance-and-angle tradeoff. The resultant performance gain can be observed in Fig. 6(b). Again, the performance gap between the estimated and achieved max-min rates is negligible for the RFB scheme but significantly large for the LB scheme. Moreover, the proposed RFB scheme has larger achieved max-min rates than the LB scheme, and the gap increases with the vertical speed and tends to saturate in the regime of high maximum vertical speed. This is expected since in that case, the UAV can fully achieve the angle gain and the vertical speed is not the performance bottleneck any more. Other observations are similar to those in Fig. 5(c).

![](images/0ae5c48a3076866e49d5f3fb4774dc6d3f5c913a6c4415a7875f4ac82d97d730.jpg)  
(a) 3D UAV trajectory.

![](images/05b97a763cb69c74eff074dc3bf32f24d1a9c1cd34fd225d313439ed813ebcf6.jpg)  
(b) Max-min rate vs. maximum tolerable outage probability

Fig. 7. Comparison of the UAV trajectories and rate performance in different schemes under different maximum tolerable outage probabilities.  
![](images/ba8c5b04f64eb48c51d73a697fd0660b38fd7aa56f69387cadd9b3424eba242d.jpg)  
(a) 3D UAV trajectory.

![](images/41326251abaf58981e286714086d608d9f4ecaf6aa10c6436acaa8e2868989a3.jpg)  
(b) Max-min rate vs. maximum Rician factor  
Fig. 8. Comparison of the UAV trajectories and performance of max-min rate in different schemes under different maximum Rician factors.

4) Effects of Maximum Tolerable Outage Probability: Fig. 7(a) compares the UAV trajectories by the LB and RFB schemes under different outage probability requirements. It is observed that the trajectory of the LB scheme remains unchanged regardless of the value of outage probability requirement. However, for the RFB scheme, the UAV tends to fly lower given a larger maximum tolerable outage probability. The reason can be inferred from Fig. 2 that the angle gain is limited in this scenario since the effective fading power is already large even at a small elevation angle and the low UAV altitude incurs smaller pathloss.

The performance of max-min rate vs. the outage probability requirement is shown in Fig. 7(b). Observe that for the case with a more stringent outage probability requirement (e.g., for ultra-reliable communications), our proposed RFB scheme can effectively enhance the achieved max-min rate as compared to that of the LB scheme (about 1.5 times when $\epsilon = 0 . 0 1 )$ . However, the performance gain reduces with the growth of maximum tolerable outage probability.

5) Effects of Maximum Rician Factor: The effects of the maximum Rician factor on the UAV trajectories are shown in Fig. 8(a). One interesting observation is that for the RFB scheme, with a larger maximum Rican factor, it is not always beneficial to increase the UAV altitude. In particular, when $K _ { \mathrm { m a x } } = 0 ~ \mathrm { d B }$ , our proposed UAV trajectory reduces to that assuming the LoS channel. The reason is that the elevation angle has negligible effects on the effective fading power in this case (see Fig. 2) and thus flying at the minimum altitude is optimal. With a larger maximum Rician factor, we can observe the ascent of the UAV in the overall trajectory, since a higher elevation angle can bring the considerable angle gain.

![](images/038ba3ec689f77155e7b600d798b41187d867e2e7098a139aec0bd61025baade.jpg)  
(a) 3D UAV trajectory.

![](images/b0fa77d8ebda004a75308163bbfe36da021cc13e2893af349fa4ab0f29e8b313.jpg)

![](images/2a9af5a846b66b8b836895aa55d22e70ddc9441306a9c0b049c8f7e1eab0a2ce.jpg)  
(c) Scheduled transmission rate

(b) Horizontal trajectory.  
![](images/2250afa10fa56727b3d8030ceff6250e655c5412bfb994dc9d5d156de7ce5abf.jpg)  
(d) Max-min rate.  
Fig. 9. Comparison of the UAV trajectories and rate performance in different schemes for the case with 4 SNs.

However, when the maximum Rician factor is sufficiently large (e.g., 100 dB), the proposed UAV trajectory would reduce its altitude and is expected to be equivalent to that assuming the LoS channel when $K _ { \mathrm { m a x } }  \infty$ . This is because in this case, the effective fading power would dramatically increase to its maximum value at a small elevation angle and stay unchanged even further increasing the angle. Therefore, the optimal trajectory should also fly at the lowest altitude to attain the favorable angle gain while achieving the minimum pathloss.

The curves of max-min rate vs. the maximum Rician factor are shown in Fig. 8(b). Observe that although the proposed UAV trajectory has different trends in the regimes of small and large maximum Rician factor (see Fig. 8(a)), the performance of max-min rate is monotonically increasing with the growth of the maximum Rician factor and converges to that of the estimated one assuming the LoS channel when the maximum Rician factor is sufficiently large. Moreover, the performance gain of our proposed scheme firstly increases and then decreases as the maximum Rician factor increases. This is expected since the UAV trajectories in both extreme cases, i.e., with a small and infinite $K _ { \mathrm { m a x } }$ , reduce to those of the LB scheme.

## C. Multiple SNs

Last, we consider the case with multiple SNs to evaluate the variations of designed trajectory due to more SNs and the corresponding performance. The effects of some parameters (e.g., time duration) are similar to those of the single-SN case and thus omitted for brevity.

In Figs. 9(a) and 9(b), we compare the optimized UAV trajectories by different schemes with 4 SNs and $T = 2 6 \mathrm { ~ s ~ }$ Observe that for the horizontal trajectory, due to the limited time duration, the UAVs in all the schemes cannot sequentially visit all the SNs and stay stationary on top of each of them, following the classic traveling-salesman-problem (TSP) solution which is known to be optimal for a sufficiently large T [14]. Therefore, they can only sequentially travel nearby each SN (resembling the TSP solution). Unlike the case with one single SN, there exist significant differences on the horizontal trajectories of the schemes assuming different channel models. In particular, compared with the LB scheme, the UAV of proposed RFB scheme gets closer to SNs 2 and 3 when traveling nearby them at the cost of being more away from SNs 1 and 4. The underpinning reason can be inferred from Fig. 9(c), where the scheduled transmission rate $a _ { n } [ m ] R _ { k } [ m ]$ is shown. Specifically, for the LB scheme, the individual average achievable rates of SNs 2 and 3 are much smaller than those of SNs 1 and 4 due to the designed trajectory assuming the inaccurate LoS channel, which limits the network maxmin rate. In contrast, the proposed RFB scheme maintains the achievable rates for SNs 1 and 4 by ascending the UAV altitude, and at the same time, letting the UAV travel closer to SNs 2 and 3 horizontally so as to improve their rates and hence the network max-min rate as shown in Fig. 9(d). The RFLA scheme, although having the similar horizontal trajectory as the RFB scheme, only has marginal performance gain over the LB scheme due to the lack of vertical trajectory optimization. Another interesting observation is that the RFFSA scheme has comparable performance as the RFB scheme in this case, although at the cost of huge complexity for searching the best altitude. The reason is that besides the similar horizontal trajectory, the vertical flight of the UAV in the RFFSA scheme is also analogous to that of the RFB scheme, i.e., ascending to a desirable altitude at the largest speed, hovering at that altitude, and then descending. Moreover, for the RFFSA scheme, the multiuser gain from scheduling optimization more-or-less compensates the performance loss from the trajectory optimization. The above results show that by leveraging the angle-aware horizontal and vertical trajectory joint design, the proposed algorithm can effectively enhance the network rate performance by balancing the achievable rates for different SNs.

## VI. CONCLUSIONS

This paper considers a UAV-enabled WSN where a UAV is despatched to collect data from multiple SNs. Our objective is to maximize the minimum average data collection rate of all SNs under the practical UAV trajectory, communication scheduling, and reliability constraints. For the UAV-SN channels, we consider the practical angle-dependent Rician fading model with the Rician factor determined by the UAV-SN elevation angle. The formulated optimization problem, however, is intractable due to the lack of a closed-form expression for the effective fading power that characterizes the achievable rate. We tackle this difficulty by approximating its function w.r.t. the 3D UAV trajectory by a logistic model using the data regression method and thereby reformulate the problem to a tractable approximate form. To solve the non-convex reformulated problem, we propose an efficient algorithm to obtain its suboptimal solution by using the BCD and SCA techniques, and evaluate its performance numerically as compared to the benchmark designs assuming the simplified LoS channel or 2D trajectory with a fixed altitude. This work makes the first attempt to design the 3D UAV trajectory under angle-dependent Rician fading channels. The proposed approach is general and can be applied to design UAV trajectories in other wireless networks and/or under other statistical channel models. For example, in multi-UAV enabled networks, the UAV cooperation can be designed by jointly optimizing their 3D trajectories as well as communication scheduling and resource allocation under 3D collision avoidance constraints.

## A. Proof of Lemma 2

## APPENDIX

This lemma is proved by contradiction. First, consider Problem P4. We can easily derive that in the optimal solution to Problem P4, the constraints (15a) for all SNs should be active, i.e., $\begin{array} { r } { \frac { 1 } { M } \sum _ { m = 1 } ^ { M } a _ { n } ^ { * } [ m ] \tilde { R } _ { n } ^ { * } [ m ] = \eta ^ { * } , \forall n } \end{array}$ . Otherwise, we can always adjust $\{ a _ { n } [ m ] \}$ to satisfy the equality without <sup>[ ]</sup>decreasing the objective value. Next, for the constraint (17a), we assume that in the optimal solution to Problem P4, there exists a $v _ { n } ^ { * } [ m ]$ such that $\begin{array} { r } { v _ { n } ^ { * } [ m ] \ < \ \frac { z ^ { * } \lfloor m \rfloor } { \sqrt { \lvert | \mathbf { q } ^ { * } [ m ] - \mathbf { w } _ { n } \rvert | ^ { 2 } + z ^ { * } [ m ] ^ { 2 } } } . } \end{array}$ Then we can always find another $\dot { v } _ { n } [ \dot { m } ]$ <sup>[ ]</sup>such that $\dot { v } _ { n } [ m ] =$ $\frac { z ^ { * } \left. m \right. } { \sqrt { | | \mathbf { q } ^ { * } \left[ m \right] - \mathbf { w } _ { n } | | ^ { 2 } + z ^ { * } \left[ m \right] ^ { 2 } } }$ . With the newly chosen $\dot { v } _ { n } [ m ]$ , at least <sup>[ ] + [ ]</sup>one of the constraints in (15a) for a SN is inactive and thus the objective value of Problem P4 can be further improved, thus contradicting to the assumption. In summary, in the optimal solution to Problem P4, both the constraints (15a) and (17a) are active. Last, using the similar contradiction method, we can prove that in the optimal solution to Problem P3, the constraints (15a) are active for all SNs. Combining these conclusions leads to the desired result.

## B. Proof of Lemma 3

Let ξ x, y <sup>-</sup> $\begin{array} { r } { \left( 1 + ( C _ { 3 } + \frac { C _ { 4 } } { x } ) \frac { 1 } { y ^ { \alpha / 2 } } \right) } \end{array}$ where $\begin{array} { r l } { C _ { 3 } } & { { } = } \end{array}$ $C _ { 1 } \gamma > 0$ and $C _ { 4 } = C _ { 2 } \dot { \gamma } > 0 .$ , then $\psi ( x , y ) \overset { \prime } { = } \xi ( x , y ) \log _ { 2 } ( e )$ <sup>1 0 4 = 2 0</sup>We first prove the convexity of $\xi ( x , y )$ <sup>2</sup>by the definition <sup>( )</sup>of convex functions. It can be obtained that the first-order derivatives of $\xi ( x , y )$ w.r.t. x and y are

$$
\begin{array} { l } { \displaystyle \xi _ { x } ( x , y ) = \frac { - C _ { 4 } } { x ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) } , } \\ { \displaystyle \xi _ { y } ( x , y ) = \frac { - ( \alpha / 2 ) ( C _ { 3 } x + C _ { 4 } ) } { y ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) } . } \end{array}\tag{30}
$$

Then, the Hessian of $\xi ( x , y )$ is

$$
\nabla ^ { 2 } \xi ( x , y ) = \left[ { \begin{array} { l l } { { \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial x ^ { 2 } } } } & { { \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial x \partial y } } } \\ { { \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial y \partial x } } } & { { \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial y ^ { 2 } } } } \end{array} } \right] ,\tag{31}
$$

where

$$
\begin{array} { r l } & { \displaystyle \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial x ^ { 2 } } = \frac { C _ { 4 } ( 2 x y ^ { \alpha / 2 } + 2 C _ { 3 } x + C _ { 4 } ) } { x ^ { 2 } ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } \mathrm { , } } \\ & { \displaystyle \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial x \partial y } = \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial y \partial x } = \frac { ( \alpha / 2 ) C _ { 4 } y ^ { \alpha / 2 - 1 } } { ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } \mathrm { , } } \\ & { \displaystyle \frac { \partial ^ { 2 } \xi ( x , y ) } { \partial y ^ { 2 } } = \frac { ( \alpha / 2 ) ( C _ { 3 } x + C _ { 4 } ) [ ( 1 + \alpha / 2 ) x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ] } { y ^ { 2 } ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } \mathrm { . } } \end{array}
$$

For any $\mathbf { t } = [ t _ { 1 } , t _ { 2 } ] ^ { T }$ , given $\alpha \geq 2$ , we can prove that $\mathbf { t } ^ { T } \nabla ^ { 2 }$ $\xi ( x , y ) \mathbf { t } \ge 0$ <sup>[ 1</sup>for $x > 0$ and $y > 0$ shown at the top of next page. Therefore, $\xi ( x , y )$ is a convex function, leading to the convexity of $\psi ( x , y )$

## C. Proof of Lemma 4

Using Lemma 3, it can be proved that $\begin{array} { r l } { \tilde { \psi } ( x , y ) } & { { } = } \end{array}$ $\begin{array} { r } { \log _ { 2 } \left( 1 + \left( C _ { 1 } + \frac { C _ { 2 } } { X + x } \right) \frac { \gamma } { ( Y + y ) ^ { \alpha / 2 } } \right) } \end{array}$ is a convex function w.r.t. $x \ \geq \ - X$ and $y ~ \ge ~ - Y$ <sup>+ )</sup>. Then using the SCA technique,

$$
\begin{array} { r l } & { \mathbf { t } ^ { T } \nabla ^ { 2 } \xi ( x , y ) \mathbf { t } } \\ & { \qquad \geq t _ { 1 } ^ { 2 } \left( \frac { C _ { 4 } ( 2 x y ^ { \alpha / 2 } + 2 C _ { 3 } x + C _ { 4 } ) } { x ^ { 2 } ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } \right) + t _ { 2 } ^ { 2 } \left( \frac { ( C _ { 3 } x + C _ { 4 } ) ( 2 x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) } { y ^ { 2 } ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } \right) + \frac { 2 t _ { 1 } t _ { 2 } C _ { 4 } y ^ { \alpha / 2 - 1 } } { ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } } \\ & { \qquad = \frac { C _ { 4 } x y ^ { \alpha / 2 } \left( t _ { 2 } x + t _ { 1 } y \right) ^ { 2 } + C _ { 4 } t _ { 1 } ^ { 2 } y ^ { 2 } ( x y ^ { \alpha / 2 } + 2 C _ { 3 } x + C _ { 4 } ) + t _ { 2 } ^ { 2 } x ^ { 2 } \left[ ( 2 C _ { 3 } x + C _ { 4 } ) x y ^ { \alpha / 2 } + ( C _ { 3 } x + C _ { 4 } ) ^ { 2 } \right] } { x ^ { 2 } y ^ { 2 } ( x y ^ { \alpha / 2 } + C _ { 3 } x + C _ { 4 } ) ^ { 2 } } \geq 0 , } \end{array}
$$

for any given $x _ { 0 }$ and $y _ { 0 } ,$ , we have $\tilde { \psi } ( x , y ) \ge \tilde { \psi } ( x _ { 0 } , y _ { 0 } ) +$ $\psi _ { x } ( x _ { 0 } , y _ { 0 } ) ( x - x _ { 0 } ) + \psi _ { y } ( x _ { 0 } , y _ { 0 } ) ( y - y _ { 0 } ) , \forall x , y .$ , where

$$
\begin{array} { r l } & { \tilde { \psi } _ { x } ( x _ { 0 } , y _ { 0 } ) } \\ & { \ = \frac { - ( \log _ { 2 } e ) \gamma C _ { 2 } } { \left( X + x _ { 0 } \right) \left[ \left( X + x _ { 0 } \right) \left( Y + y _ { 0 } \right) ^ { \alpha / 2 } + \gamma \left( C _ { 1 } ( X + x _ { 0 } ) + C _ { 2 } \right) \right] } } \\ & { \tilde { \psi } _ { y } ( x _ { 0 } , y _ { 0 } ) } \\ & { \ = \frac { - ( \log _ { 2 } e ) ( \alpha / 2 ) \gamma \left( C _ { 1 } ( X + x _ { 0 } ) + C _ { 2 } \right) } { \left( Y + y _ { 0 } \right) \left[ \left( X + x _ { 0 } \right) \left( Y + y _ { 0 } \right) ^ { \alpha / 2 } + \gamma \left( C _ { 1 } ( X + x _ { 0 } ) + C _ { 2 } \right) \right] } . } \end{array}
$$

By letting $x _ { 0 } = 0$ and $y _ { 0 } = 0$ , we can obtain

$$
\begin{array} { r l r } {  { \log _ { 2 } ( 1 + ( C _ { 1 } + \frac { C _ { 2 } } { X + x } ) \frac { \gamma } { ( Y + y ) ^ { \alpha / 2 } } ) } } \\ & { } & { \geq \log _ { 2 } ( 1 + ( C _ { 1 } + \frac { C _ { 2 } } { X } ) \frac { \gamma } { Y ^ { \alpha / 2 } } ) } \\ & { } & { - \frac { ( \log _ { 2 } e ) \gamma C _ { 2 } } { X ( X Y ^ { \alpha / 2 } + \gamma ( C _ { 1 } X + C _ { 2 } ) ) } x } \\ & { } & { - \frac { ( \log _ { 2 } e ) ( \alpha / 2 ) \gamma ( C _ { 1 } X + C _ { 2 } ) } { Y ( X Y ^ { \alpha / 2 } + \gamma ( C _ { 1 } X + C _ { 2 } ) ) } y . } \end{array}
$$

By letting $\begin{array} { r l r l r } { \gamma } & { { } = } & { \gamma _ { n } , \hat { v } _ { n } [ m ] } & { { } = } & { \frac { z [ m ] } { \sqrt { | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } } } , } \end{array}$ $\begin{array} { r l r } { X } & { { } = } & { 1 + e ^ { - \left( B _ { 1 } + B _ { 2 } \hat { v } _ { n } [ m ] \right) } , x = e ^ { \mathrm { ~ } \vec { v } _ { 1 } \cdot \vec { s } _ { 1 } } \vec { \mathbf { \Gamma } } _ { \vec { \mathbf { \Gamma } } } ^ { i } - \vec { \mathbf { \Gamma } } _ { \vec { \mathbf { \Gamma } } } ^ { i } \cdot \vec { \mathbf { \Gamma } } _ { \vec { \mathbf { \Gamma } } } ^ { i } - \vec { \mathbf { \Gamma } } _ { \vec { \mathbf { \Gamma } } } ^ { i } \cdot \vec { \mathbf { \Gamma } } _ { \vec { \mathbf { \Gamma } } } ^ { i } } \end{array}$ $e ^ { - ( B _ { 1 } + B _ { 2 } \hat { v } _ { n } [ m ] ) } , \ Y \ = \ | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 }$ , and $y =$ $| | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } - | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 }$ <sup>+ [ ] =</sup>, we thus derive Lemma 4 where $\begin{array} { r l r } { \hat { R } _ { n } [ m ] } & { = } & { \log _ { 2 } \left( 1 + \left( C _ { 1 } + \frac { C _ { 2 } } { X } \right) \frac { \gamma } { Y ^ { \alpha / 2 } } \right) , \hat { \Phi } _ { n } [ m ] = } \end{array}$ $\frac { ( \log _ { 2 } e ) \gamma C _ { 2 } } { X { \bigl ( } X Y ^ { \alpha / 2 } + \gamma ( C _ { 1 } X + C _ { 2 } ) { \bigr ) } }$ , and $\begin{array} { r } { \hat { \Psi } _ { n } [ m ] = \frac { \hat { ( \log _ { 2 } ^ { \prime } e ) } ( \alpha / 2 ) \gamma ( C _ { 1 } X + C _ { 2 } ) } { Y ( X Y ^ { \alpha / 2 } + \gamma ( C _ { 1 } X + C _ { 2 } ) ) } } \end{array}$

## D. Proof of Lemma 5

Define a function $\begin{array} { r } { \tilde { v } ( x ) = \frac { D } { \sqrt { X + x } } } \end{array}$ . It can be easily shown <sup>+</sup>that v x is a convex function w.r.t. $x \ \geq \ - X$ . Similar to Appendix C, by using the SCA technique, for any given $x _ { 0 } ,$ we have

$$
\tilde { v } ( x ) \geq \frac { D } { \sqrt { X + x _ { 0 } } } - \frac { D } { 2 ( X + x _ { 0 } ) ^ { \frac { 3 } { 2 } } } ( x - x _ { 0 } ) .\tag{32}
$$

By letting $x _ { 0 } ~ = ~ 0 _ { \mathrm { { \scriptsize ~ . ~ } } }$ , we can obtain $\begin{array} { r } { \frac { D } { \sqrt { X + x } } \ge \frac { D } { \sqrt { X } } - \frac { D x } { { _ 2 X } ^ { \frac { 3 } { 2 } } } . } \end{array}$ Last, by letting $D = z [ n ] , X = | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { \hat { 2 } }$ and $x = | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } - | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 }$ <sup>[ ] + [ ]</sup>, we can derive Lemma 5 where

$$
\begin{array} { l } { \hat { v } _ { n } [ m ] = \displaystyle \frac { z [ m ] } { \sqrt { | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } } } , \ ~ } \\ { \hat { \Lambda } _ { n } [ m ] = \displaystyle \frac { z [ m ] } { 2 ( | | \hat { \mathbf { q } } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } ) ^ { \frac { 3 } { 2 } } } . \ } \end{array}\tag{33}
$$

## E. Proof of Convexity of Problem 11

It is observed that except the constraint (25a), the objective function and other constraints in Problem P10 are convex. Then the remaining effort is to prove the convexity of the constraint (25a). To this end, we first derive the first-order derivative of $\begin{array} { r } { v _ { n } [ m ] \ = \ \frac { z [ m ] } { \sqrt { | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } } } } \end{array}$ w.r.t. z m as follows.

$$
\frac { \partial v _ { n } [ m ] } { \partial z [ m ] } = \frac { | | \mathbf q [ m ] - \mathbf w _ { n } | | ^ { 2 } } { ( | | \mathbf q [ m ] - \mathbf w _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } ) ^ { \frac { 3 } { 2 } } } .\tag{34}
$$

Then the second-order derivative of $v _ { n } [ m ]$ w.r.t. $z [ m ]$ is

$$
\frac { \partial ^ { 2 } ~ v _ { n } [ m ] } { \partial z [ m ] ^ { 2 } } = \frac { - 3 z [ m ] ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } ) } { ( | | \mathbf { q } [ m ] - \mathbf { w } _ { n } | | ^ { 2 } + z [ m ] ^ { 2 } ) ^ { \frac { 5 } { 2 } } } \leq 0 ,\tag{35}
$$

for $z [ m ] \geq H > 0$ . Therefore, $v _ { n } [ m ]$ is concave w.r.t. z m <sup>[ ] 0 [ ] [ ]</sup>and thus (25a) is the convex constrain, leading to the desired result.

## REFERENCES

[1] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.

[2] H. Baek and J. Lim, “Design of future UAV-relay tactical data link for reliable UAV control and situational awareness,” IEEE Commun. Mag., vol. 56, no. 10, pp. 144–150, Oct. 2018.

[3] C. H. Liu, T. He, K.-W. Lee, K. K. Leung, and A. Swami, “Dynamic control of data ferries under partial observations,” in Proc. IEEE Wireless Commun. Netw. Conf., Apr. 2010, pp. 1–6.

[4] A. E. A. A. Abdulla, Z. M. Fadlullah, H. Nishiyama, N. Kato, F. Ono, and R. Miura, “An optimal data collection technique for improved utility in UAS-aided networks,” in Proc. IEEE Int. Conf. Comput. Commun. (INFOCOM), Apr./May 2014, pp. 736–744.

[5] C. H. Liu, Z. Chen, J. Tang, J. Xu, and C. Piao, “Energy-efficient UAV control for effective and fair communication coverage: A deep reinforcement learning approach,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 2059–2070, Sep. 2018.

[6] J. Liu, X. Wang, B. Bai, and H. Dai, “Age-optimal trajectory planning for UAV-assisted data collection,” in Proc. IEEE Int. Conf. Comput. Commun. Workshops (INFOCOM), Apr. 2018, pp. 553–558.

[7] C. Zhan, Y. Zeng, and R. Zhang, “Energy-efficient data collection in UAV enabled wireless sensor network,” IEEE Wireless Commun. Lett., vol. 7, no. 3, pp. 328–331, Jun. 2018.

[8] C. Zhan, Y. Zeng, and R. Zhang, “Trajectory design for distributed estimation in UAV-enabled wireless sensor network,” IEEE Trans. Veh. Techn., vol. 67, no. 10, pp. 10155–10159, Oct. 2018.

[9] J. Gong, T.-H. Chang, C. Shen, and X. Chen, “Flight time minimization of UAV for data collection over wireless sensor networks,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1942–1954, Sep. 2018.

[10] D. Ebrahimi, S. Sharafeddine, P.-H. Ho, and C. Assi, “UAV-aided projection-based compressive data gathering in wireless sensor networks,” IEEE Internet Things J., to be published.

[11] Y. Zeng, X. Xu, and R. Zhang, “Trajectory design for completion time minimization in UAV-enabled multicasting,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2233–2246, Apr. 2018.

[12] D. Yang, Q. Wu, Y. Zeng, and R. Zhang, “Energy trade-off in ground-to-UAV communication via trajectory design,” IEEE Trans. Veh. Technol, vol. 67, no. 7, pp. 6721–6726, Jul. 2018.

[13] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

[14] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[15] Q. Wu, J. Xu, and R. Zhang, “Capacity characterization of UAV-enabled two-user broadcast channel,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1955–1971, Sep. 2018.

[16] Q. Wu and R. Zhang, “Common throughput maximization in UAV-enabled OFDMA systems with delay consideration,” IEEE Trans. Wireless Commun., vol. 66, no. 12, pp. 6614–6627, Dec. 2018.

[17] Y. Zeng et al., “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.

[18] S. Zhang, Y. Zeng, and R. Zhang, “Cellular-enabled UAV communication: A connectivity-constrained trajectory optimization perspective,” IEEE Trans. Commun., vol. 67, no. 3, pp. 2580–2604, Mar. 2019.

[19] J. Zhang, Y. Zeng, and R. Zhang, “UAV-enabled radio access network: Multi-mode communication and trajectory design,” IEEE Trans. Signal Process., vol. 66, no. 20, pp. 5269–5284, Oct. 2018.

[20] J. Xu, Y. Zeng, and R. Zhang, “UAV-enabled wireless power transfer: Trajectory design and energy optimization,” IEEE Trans. Wireless Commun., vol. 17, no. 8, pp. 5092–5106, Aug. 2018.

[21] Study Enhanced LTE Support for Aerial Vehicles, document 3GPP TR 36.777 V1.0.0, Dec. 2017.

[22] J. Holis and P. Pechac, “Elevation dependent shadowing model for mobile communications via high altitude platforms in built-up areas,” IEEE Trans. Antennas Propag., vol. 56, no. 4, pp. 1078–1084, Apr. 2008.

[23] J. Lyu, Y. Zeng, R. Zhang, and T. J. Lim, “Placement optimization of UAV-mounted mobile base stations,” IEEE Commun. Lett., vol. 21, no. 3, pp. 604–607, Mar. 2017.

[24] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.

[25] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Efficient deployment of multiple unmanned aerial vehicles for optimal wireless coverage,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1647–1650, Aug. 2016.

[26] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Mobile unmanned aerial vehicles (UAVs) for energy-efficient Internet of Things communications,” IEEE Trans. Wireless Commun., vol. 16, no. 11, pp. 7574–7589, Nov. 2017.

[27] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE Int. Conf. Commun. (ICC), May 2016, pp. 1–5.

[28] M. Alzenad, A. El-Keyi, and H. Yanikomeroglu, “3-D placement of an unmanned aerial vehicle base station for maximum coverage of users with different QoS requirements,” IEEE Wireless Commun. Lett., vol. 7, no. 1, pp. 38–41, Feb. 2018.

[29] O. Esrafilian, R. Gangula, and D. Gesbert, “Learning to communicate in UAV-aided wireless networks: Map-based approaches,” IEEE Internet Things J., to be published.

[30] A. A. Khuwaja, Y. Chen, N. Zhao, M.-S. Alouini, and P. Dobbins, “A survey of channel modeling for UAV communications,” IEEE Commun. Surveys Tuts., vol. 20, no. 4, pp. 2804–2821, 4th Quart., 2018.

[31] D. W. Matolak and R. Sun, “Air–ground channel characterization for unmanned aircraft systems—Part III: The suburban and near-urban environments,” IEEE Trans. Veh. Technol., vol. 66, no. 8, pp. 6607–6618, Aug. 2017.

[32] Iskandar and S. Shimamoto, “Channel characterization and performance evaluation of mobile communication employing stratospheric platforms,” IEICE Trans. Commun., vol. E89-B, no. 3, pp. 937–944, Mar. 2006.

[33] Y. Sun, D. Xu, D. W. K. Ng, L. Dai, and R. Schober. (2018). “Optimal 3D-trajectory design and resource allocation for solar-powered UAV communication systems.” [Online]. Available: https://arxiv. org/abs/1808.00101

[34] W. Khawaja, I. Guvenc, D. Matolak, U.-C. Fiebig, and N. Schneckenberger. (2018). “A survey of air-to-ground propagation channel modeling for unmanned aerial vehicles.” [Online]. Available: https://arxiv.org/abs/1801.01656

[35] A. Gil, J. Segura, and N. M. Temme, “The asymptotic and numerical inversion of the Marcum Q-function,” Stud. Appl. Math., vol. 133, no. 2, pp. 257–278, 2014.

[36] M. M. Azari, F. Rosas, K.-C. Chen, and S. Pollin, “Ultra reliable UAV communication using altitude and cooperation diversity,” IEEE Trans. Commun., vol. 66, no. 1, pp. 330–344, Jan. 2018.

[37] A. Ben-Tal and A. Nemirovski, Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications, vol. 2. Philadelphia, PA, USA: SIAM, 2001.

![](images/634f658fa01ae311515e92cac53fcf662de0c4421ec48cb7f835091a2b3487e1.jpg)

Changsheng You (S’15) received the B.Eng. degree in electronic engineering and information science from the University of Science and Technology of China in 2014 and the Ph.D. degree in electrical and electronic engineering from The University of Hong Kong in 2018. He is currently a Research Fellow with the Department of Electrical and Computer Engineering, National University of Singapore. His research interests include UAV communications, mobile-edge computing, fog computing, wireless power transfer, energy harvesting systems, and convex optimization.

![](images/a64595189c0684faa984a4b3f7539b7888b4752148a156625e7223a099e6dab9.jpg)

Rui Zhang (S’00–M’07–SM’15–F’17) received the B.Eng. (Hons.) and M.Eng. degrees from the National University of Singapore, Singapore, and the Ph.D. degree from Stanford University, Stanford, CA, USA, all in electrical engineering.

From 2007 to 2010, he was a Research Scientist with the Institute for Infocomm Research, ASTAR, Singapore. Since 2010, he has been with the Department of Electrical and Computer Engineering, National University of Singapore, where he is currently the Dean’s Chair Associate Professor with the Faculty of Engineering. He has authored over 300 papers. He has been listed as a Highly Cited Researcher (also known as the World’s Most Influential Scientific Minds), by Thomson Reuters (Clarivate Analytics) since 2015. His research interests include UAV/satellite communication, wireless information and power transfer, multiuser MIMO, smart and reconfigurable environment, and optimization methods.

Dr. Zhang was a recipient of the 6th IEEE Communications Society Asia–Pacific Region Best Young Researcher Award in 2011 and the Young Researcher Award of the National University of Singapore in 2015. He was a co-recipient of the IEEE Marconi Prize Paper Award in Wireless Communications in 2015, the IEEE Communications Society Asia–Pacific Region Best Paper Award in 2016, the IEEE Signal Processing Society Best Paper Award in 2016, the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2017, the IEEE Signal Processing Society Donald G. Fink Overview Paper Award in 2017, and the IEEE Technical Committee on Green Communications and Computing (TCGCC) Best Journal Paper Award in 2017. His coauthored paper received the IEEE Signal Processing Society Young Author Best Paper Award in 2017. He served for over 30 international conferences as the TPC co-chair or an organizing committee member, and as the Guest Editor for three special issues in the IEEE JOURNAL OF SELECTED TOPICS IN SIGNAL PROCESSING and the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS. He was an elected member of the IEEE Signal Processing Society SPCOM Technical Committee from 2012 to 2017 and the SAM Technical Committee from 2013 to 2015, and served as the Vice Chair for the IEEE Communications Society Asia–Pacific Board Technical Affairs Committee from 2014 to 2015. He served as an Editor for the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS from 2012 to 2016, the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS: GREEN COMMUNICATIONS AND NETWORKING SERIES from 2015 to 2016, and the IEEE TRANSACTIONS ON SIGNAL PROCESSING from 2013 to 2017. He is currently an Editor of the IEEE TRANSACTIONS ON COMMUNICA-TIONS and the IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING. He serves as a member of the Steering Committee for the IEEE WIRELESS COMMUNICATIONS LETTERS.