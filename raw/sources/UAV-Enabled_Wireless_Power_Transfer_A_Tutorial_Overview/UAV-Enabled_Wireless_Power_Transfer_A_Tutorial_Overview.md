# UAV-Enabled Wireless Power Transfer: A Tutorial Overview

Lifeng Xie , Member, IEEE, Xiaowen Cao , Graduate Student Member, IEEE, Jie Xu , Member, IEEE, and Rui Zhang , Fellow, IEEE

(Invited Paper)

Abstract—Unmanned aerial vehicle (UAV)-enabled wireless power transfer (WPT) has recently emerged as a promising technique to provide sustainable energy supply for widely distributed low-power ground devices (GDs) in large-scale wireless networks. Compared with the energy transmitters (ETs) in conventional WPT systems which are deployed at fixed locations, UAV-mounted aerial ETs can fly flexibly in the three-dimensional (3D) space to charge nearby GDs more efficiently. This paper provides a tutorial overview on UAV-enabled WPT and its appealing applications, in particular focusing on how to exploit UAVs’ controllable mobility via their 3D trajectory design to maximize the amounts of energy transferred to all GDs in a wireless network with fairness. First, we consider the single-UAV-enabled WPT scenario with one UAV wirelessly charging multiple GDs at known locations. To solve the energy maximization problem in this case, we present a general trajectory design framework consisting of three innovative approaches to optimize the UAV trajectory, which are multi-location hovering, successive-hoverand-fly, and time-quantization-based optimization, respectively. Next, we consider the multi-UAV-enabled WPT scenario where multiple UAVs cooperatively charge many GDs in a large area. Building upon the single-UAV trajectory design, we propose two efficient schemes to jointly optimize multiple UAVs’ trajectories, based on the principles of UAV swarming and GD clustering, respectively. Furthermore, we consider two important extensions of UAV-enabled WPT, namely UAV-enabled wireless powered communication networks (WPCN) and UAV-enabled wireless powered mobile edge computing (MEC), by integrating the emerging WPCN and MEC techniques, respectively. For both cases, we investigate the UAV trajectory design jointly with communication/computation resource allocations to optimize the system performance, subject to the energy availability constraints

at GDs. Finally, open problems in UAV-enabled WPT and promising directions for its future research are discussed.

Index Terms—Unmanned aerial vehicle (UAV), wireless power transfer (WPT), trajectory design, resource allocation, wireless powered communication networks (WPCN), mobile edge computing (MEC).

## I. INTRODUCTION

## A. Wireless Power Transfer (WPT)

expected to enable numerous new applications in a variety of vertical domains such as smart city, smart factory, intelligent transportation systems, and so on. Towards this end, future wireless networks need to incorporate a massive number of low-power IoT devices with real-time sensing, communication, computation, and control functionalities. In this regard, how to maintain the sustainable operation of these low-power devices is becoming a more practically important as well as challenging problem to tackle. Different from conventional energy sources such as battery and/or environment energy harvesting [1], [2], the radio-frequency (RF) transmission enabled WPT has recently emerged as a viable new solution to provide sustainable energy supply for low-power IoT devices, where dedicated energy transmitters (ETs) are deployed for broadcasting RF signals to wirelessly charge them simultaneously [3]–[8]. Recently, there have been various start-up companies (such as Powercast, TransferFi, and Energous) that have developed commercialized RF-based WPT products for moderate-to-long-range wireless charging applications. Furthermore, WPT has been integrated in wireless communication and computation [9]–[11] networks for various new applications, such as simultaneous wireless information and power transfer (SWIPT) [12]–[16], wireless powered communication networks (WPCN) [17]–[19], and wireless powered mobile edge computing (MEC) [20]–[23].

How to enhance the energy transfer efficiency from ETs to distributed wireless devices is the essential challenge faced in RF-based WPT systems. First, due to the severe RF signal propagation loss over distance, the energy transfer efficiency degrades drastically when devices are located far away from the ETs. Second, when there are multiple devices distributed at different locations, the nearby devices from an ET will harvest significantly more energy than those far apart from all ETs, thus resulting in a critical near-far fairness issue. Under WPCN and wireless powered MEC applications, the near-far issue may become even more severe, in which the far-apart devices with less harvested energy need to consume more energy for information transmission to meet the same quality of service (QoS) as nearby devices. To tackle these challenges, there have been prior works that proposed various techniques to enhance the energy transfer efficiency via, e.g., transmit energy beamforming [5], [8], [24]–[27], energy waveform optimization [28], [29], adaptive power control [30], and deployment optimization [31] for the ETs. Despite these research progresses, the ultra-dense deployment of ETs at fixed locations is in general necessary to achieve ubiquitous coverage for WPT. This thus incurs unduly high deployment and maintenance costs that hinder its broad applications in practice.

## B. Unmanned Aerial Vehicle (UAV)-Enabled WPT

Recently, UAV-enabled wireless communications have attracted growing interests (see, e.g., [32]–[34]), in which UAVs are dispatched as aerial base stations (BSs), access points (APs), relays, etc., to support the mobile subscribers on the ground for point-to-point communications [35]–[38], multiuser communications [39]–[42], data collection [43]–[47], secrecy communications [48]–[50], device-to-device (D2D) communications [51]–[53], and so on. Motivated by the advancements of UAV-enabled wireless communications, UAV-enabled WPT has also emerged as a viable solution to resolve the aforementioned technical issues in WPT from a fundamentally new perspective. Different from conventional ETs at fixed locations, low-altitude UAVs can serve as a new type of aerial ETs that can fly flexibly to charge nearby low-power devices efficiently. Specifically, UAVs can not only enjoy the favorable line-of-sight (LoS) channels with ground devices (GDs) [54], [55] but also exploit their fullycontrollable mobility to adaptively adjust flight trajectories over time to reduce the transmission distances to GDs based on their real-time locations, thus enhancing the energy transfer efficiency to all GDs significantly and also ensuring their performance fairness effectively. As such, UAV-enabled WPT is particularly appealing for large-scale wireless networks with massive widely distributed GDs, for which the conventional approach of densely deploying fixed-location ETs is very costly if not infeasible. Some promising application scenarios of UAV-enabled WPT such as smart city, maritime communications, wireless sensor networks, and smart factory, are shown in Fig. 1. Furthermore, UAV-enabled WPT can be extended to UAV-enabled WPCN [56]–[61] and UAV-enabled wireless powered MEC [62]–[66], in which UAVs play multifarious roles such as aerial APs and aerial MEC servers (in addition to ETs) to provide sustainable data access and remote edge computing for GDs, respectively.

To fully reap the benefits of UAV-enabled WPT, how to properly design the UAV trajectories to maximize the energy transfer performance is a new and challenging problem to tackle innovatively. In the most basic case when there is one single UAV wirelessly charging one single GD, it is straightforward that the UAV should fly close to the GD as much as possible to minimize their transmission distance for maximizing the energy transfer efficiency. However, if there are multiple GDs distributed at different locations that are a-prior known, how to design the UAV’s trajectory to balance the transferred energy amounts to different GDs given a finite charging time becomes non-trivial. This is due to the fact that when the UAV flies close to one GD for charging more efficiently, it may have to leave far apart from some other GDs and charge less energy to them, thus leading to a fundamental tradeoff in balancing the transferred energy amounts among different GDs. Moreover, if there are more than one UAV cooperatively charging many GDs in a largescale network, the joint multi-UAV trajectory design becomes even more challenging.

![](images/988e224afd995b9c7eaec31b2942d2968a22550a511bafe9ac99ce57add2dbad.jpg)  
Fig. 1. Example applications of UAV-enabled WPT.

To tackle the above challenges, there have been a handful of prior works in the literature that investigated the trajectory design for enhancing the energy transfer performance for UAVenabled WPT when there is only one single UAV [67]–[72]. More specifically, the authors in [67] first considered the single-UAV-enabled WPT by assuming that the UAV flies at a fixed altitude, in which efficient two-dimensional (2D) UAV trajectory designs are proposed to maximize the sum energy harvested by all GDs or the minimum energy harvested among GDs, subject to the UAV’s flight time and speed constraints. Building upon the trajectory design framework in [67], the authors in [68] proposed the globally optimal one-dimensional (1D) UAV trajectory to maximize the minimum energy harvested among GDs, when all GDs are located on a line, while other works [69], [70] extended the UAV trajectory design to different setups [71], [72]. These trajectory designs have been further extended to the UAV-enabled WPCN in [58], [73]–[75] and wireless powered MEC in [62]–[66], where the joint design of UAV trajectory and communication/computation resource allocations was investigated.

![](images/9c57903d8fcf471d41af25ec0fda21796879d5bf65574aa2e4c390519e102e4d.jpg)  
Fig. 2. Organization of the paper.

## C. Paper Organization

In view of the above existing works, this paper aims to provide a comprehensive and up-to-date tutorial overview on UAV-enabled WPT, with the particular emphasis on how to exploit the UAV trajectory design for optimizing the system performance. The organization of this paper is summarized in Fig. 2.

• First, Section II considers the single-UAV-enabled WPT scenario with one single UAV wirelessly charging multiple GDs. In this case, we first use a toy example with one single GD to show the benefit of trajectory design, and then present a generic utility maximization problem to maximize the energy amounts transferred to multiple GDs in a fair manner subject to practical UAV flight constraints. To solve the formulated energy maximization problem in this case, we present a general trajectory design framework consisting of three innovative approaches to optimize the trajectory, which are multi-location hovering, successive-hover-and-fly, and time-quantization-based optimization, respectively.

• Next, Section III considers the multi-UAV-enabled WPT scenario with multiple UAVs cooperatively charging many GDs in a large area, for which a generic utility maximization problem to jointly optimize multiple UAVs trajectories and their energy transmissions is presented for the first time. While the optimal solution to this problem is still open, we propose two heuristic but efficient schemes based on the principles of UAV swarming and GD clustering, respectively, and design their corresponding multi-UAV trajectories by extending the single-UAV trajectory design solutions.

• Moreover, Sections IV and V consider two emerging applications of UAV-enabled WPT, namely UAV-enabled WPCN and UAV-enabled wireless powered MEC, respectively. Under properly designed operation protocols for these two applications, we formulate their utility maximization problems to jointly optimize the UAV trajectory and the communication/computation resource allocations, subject to UAV’s flight constraints and GD’s energy harvesting constraints. By extending the UAV trajectory design framework for WPT, efficient joint UAV trajectory and resource allocation designs are developed.

• Finally, Section VI provides discussions on the challenging open problems and important future research directions in UAV-enabled WPT, including the issues of non-linear energy harvesting models, channel state information (CSI) availability, over-the-air computation (AirComp), online trajectory design, and ground vehicles for WPT.

It is worth noting that there have been various overview papers on UAV-enabled wireless communications and the corresponding trajectory design/optimization approaches [32], [34], [76], [77]. However, the trajectory design for UAV-enabled WPT in this paper differs significantly from that for UAV-enabled wireless communications due to the following reasons. First, in UAV-enabled wireless communications, different GDs generally need to communicate with the UAV over orthogonal time-frequency blocks, and accordingly, the UAV should decide its trajectory over time based on the multiple-access scheme and the communicating GDs at each time instant. By contrast, in UAV-enabled WPT, different GDs can simultaneously harvest energy from the same RF signals sent by the UAV. Second, the utility/objective functions for communication versus WPT performance optimization are also different in general. To our best knowledge, a comprehensive tutorial overview on the UAV trajectory design for UAV-enabled WPT is still lacking in the current literature.

![](images/84e78a7952923a3e8ad978de09ffe40de6210fc98aa250597bc5ff63d2db3b0c.jpg)  
Fig. 3. A toy example with one single GD.

Notation: Scalars are denoted by lower-case letters, vectors by bold-face lower-case letters, and matrices by bold-face upper-case letters. For a vector m, m<sup>T</sup> denotes its transpose, and $\| \pmb { m } \|$ denotes its Euclidean norm. For a matrix M, $\mathbf { \bar { \boldsymbol { M } } } ^ { H }$ denotes its hermitian. <sup>E</sup>[ · ] denotes the statistical expectation. Tr(·) denotes the trace of a square matrix. diag(·) denotes a diagonal matrix with the argument denoting its main diagonal.

## II. SINGLE-UAV-ENABLED WPT

This section considers the single-UAV-enabled WPT system, in which one single UAV is dispatched as an aerial ET to wirelessly charge multiple GDs at known locations. In the following, we first provide a toy example with one single GD to show the benefit of UAV trajectory design in enhancing the energy transfer efficiency, then formulate the utility maximization problem to fairly maximize the harvested energy amounts at different GDs, and next present a general trajectory optimization framework, followed by numerical results.

## A. Toy Example With One GD

This subsection considers a toy example with one single GD, as shown in Fig. 3, to show the benefit of UAV-enabled WPT over the conventional WPT with a fixed ET. First, as the benchmark for comparison, we consider the conventional WPT in the 2D Cartesian coordinate system as shown in Fig. 3(a), where the ET and GD are deployed at fixed locations (0, H<sup>˜</sup> ) and $( D , \ 0 )$ , respectively, with distance $\tilde { d } = \sqrt { D ^ { 2 } + \tilde { H } ^ { 2 } }$ . In this case, the channel power gain from the ET to the GD is expressed as $\tilde { h } = \tilde { \beta _ { 0 } } / \tilde { d } ^ { \tilde { \alpha } }$ , where $\tilde { \beta _ { 0 } }$ denotes the channel power gain at reference distance $d _ { 0 } = 1$ meter (m) and α˜ denotes the path loss exponent with $\tilde { \alpha } \geq 2$ in general. Considering constant transmit power P at the ET and the linear energy harvesting model at the GD for converting the received RF signal into usable energy, the harvested power at the GD is

$$
E _ { \mathrm { f i x } } = \eta P \tilde { \beta } _ { 0 } / \tilde { d } ^ { \tilde { \alpha } } = \frac { \eta P \tilde { \beta } _ { 0 } } { \left( D ^ { 2 } + \tilde { H } ^ { 2 } \right) ^ { \tilde { \alpha } / 2 } } ,\tag{1}
$$

where $0 ~ < ~ \eta ~ \leq ~ 1$ denotes the linear RF-to-direct current (DC) energy conversion efficiency at the GD. It is observed from (1) that due to the signal path loss, the harvested power $E _ { \mathrm { f i x } }$ sharply decreases as the distance D becomes large, especially when the path loss exponent α˜ is high (e.g., when the signal propagation is blocked by obstacles).

Next, we consider the UAV-enabled WPT in a 2D Cartesian coordinate system as shown in Fig. 3(b). As the UAV is mobile, we focus on a finite charging period ${ \mathcal { T } } \triangleq ( 0 , T ]$ with duration T, and denote the UAV’s time-varying location as (x(t), H) at time $t \in \tau .$ Here, H denotes the fixed altitude of the UAV and $H \geq { \tilde { H } }$ generally holds due to the UAV’s relatively higher altitude than the conventional ET on the ground. Accordingly, the line-of-sight (LoS) link normally exists between the UAV and the GD, and thus we consider the free-space path loss model with path loss exponent $\alpha = 2 ,$ , as commonly adopted in the UAV literature [35], [78]. In order for fair comparison with the conventional WPT in Fig. 3(a), we assume that the UAV starts and finishes its charging mission at $x ( 0 ) = x ( T ) = 0 \mathrm { s }$ . In this case, the channel power gain between the UAV and the GD at any time instant $t \in \mathcal T$ is

$$
h ( x ( t ) ) = \beta _ { 0 } / ( d ( x ( t ) ) ) ^ { 2 } = \frac { \beta _ { 0 } } { ( x ( t ) - D ) ^ { 2 } + H ^ { 2 } } ,\tag{2}
$$

where $d ( x ( t ) ) = \sqrt { ( x ( t ) - D ) ^ { 2 } + H ^ { 2 } }$ denotes their distance. Accordingly, the harvested power by the GD at time instant $t \in \mathcal T$ is [67]

$$
\bar { E } ( x ( t ) ) = \frac { \eta P \beta _ { 0 } } { ( x ( t ) - D ) ^ { 2 } + H ^ { 2 } } .\tag{3}
$$

The total harvested energy by the GD over the entire period $\tau _ { \mathrm { i s } }$

$$
E ( \{ x ( t ) \} ) = \int _ { 0 } ^ { T } \frac { \eta P \beta _ { 0 } } { ( x ( t ) - D ) ^ { 2 } + H ^ { 2 } } \mathrm { d } t .\tag{4}
$$

By comparing $E ( \{ x ( t ) \} ) / T$ in (4) and $E _ { \mathrm { f i x } }$ in (1), it is observed that as compared to the conventional WPT, the UAVenabled WPT can enhance the average harvested power at the GD due to the following two main reasons. First, with the relatively higher altitude of the UAV, UAV-enabled WPT enjoys the LoS energy transmission link with lower path loss exponent. Second, the UAV can exploit its mobility via optimizing the trajectory {x(t)} to shorten the distance d(x(t)) with the GD (e.g., when the UAV hovers exactly above the GD with $x ( t ) = D$ , the distance between the UAV and the GD is minimized as H).

To fully exploit such benefits, how to optimize the UAV trajectory {x(t)} is crucial, which needs to take into account the UAV’s flight constraints in practice. Intuitively, to maximize the harvested energy $E ( \{ x ( t ) \} )$ at the GD in (4), the UAV should try its best to fly as close to the GD as possible. In July 05,2026 at 13:06:56 UTC from IEEE Xplore. Restrictions apply.

![](images/f6fd5974ac279b3139a794305bfef12e741ae3ee7be3b5d3f58faed51f8f52f0.jpg)  
Fig. 4. The average harvested power versus the GD’s horizontal location D under different time duration T.

particular, suppose that the UAV is constrained by the maximum flight speed $V _ { \mathrm { m a x } }$ . Then the UAV’s optimal trajectory design can be obtained as follows by considering two cases.

• When $T V _ { \mathrm { m a x } } \geq D$ , the UAV should first fly straightly towards the GD at the maximum flight speed $V _ { \mathrm { m a x } }$ with duration $D / V _ { \mathrm { m a x } } .$ , then hover above the GD with duration $T - 2 D / V _ { \mathrm { m a x } } ,$ , and finally fly straightly back to the initial location at speed $V _ { \mathrm { m a x } }$ with duration $D / V _ { \mathrm { m a x } } .$

• When $T V _ { \mathrm { m a x } } < D$ , the time duration is not sufficient for the UAV to hover above the GD. In this case, the UAV should first fly towards the GD at speed $V _ { \mathrm { m a x } }$ in the first half period, and then fly back in the second half.

Fig. 4 shows the average harvested power by the GD versus its horizontal location D, in which $\tilde { \alpha } = 3 , \eta = 6 0 \%$ $\tilde { H } = 2 \ \mathrm { m } , \ H = 5 \ \mathrm { m } , \ P = 4 0$ dBm, and $\beta _ { 0 } = - 3 0$ dB. It is observed that as the (initial) horizontal distance D between the ET/UAV and the GD increases, for conventional WPT the average harvested power degrades severely, while for UAVenabled WPT the average harvested power almost remains unchanged (especially when T becomes large). More specifically, when $T = 1 0 0$ in second (s), UAV-enabled WPT is observed to achieve 30 dB harvested power gain over the conventional WPT. This shows the enormous benefit of exploiting the UAV mobility to combat against the severe signal path loss for enhancing the energy transfer efficiency.

## B. Utility Maximization With Multiple GDs

Building upon the insights gained from the simplified case with one single GD in Section II-A, this subsection considers the general single-UAV-enabled WPT in the three-dimensional (3D) Cartesian coordinate system with $K > 1$ GDs, as shown in Fig. 5, in which the UAV is dispatched to serve K GDs over a finite charging period ${ \mathcal { T } } { \triangleq } ( 0 , { \bar { T } } ]$ . Let $( x _ { k } , y _ { k } , 0 )$ denote the location of each GD $k \in \mathcal { K } \triangleq \{ 1 , \dots , K \}$ , where $c _ { k } =$ $( x _ { k } , y _ { k } )$ denotes its horizontal coordinate. Let $( x ( t ) , y ( t ) , H )$ denote the UAV’s location at time instant $t \in \tau ,$ in which ${ \pmb u } ( t ) = ( x ( t ) , y ( t ) )$ ) denotes the time-varying horizontal location to be optimized. Accordingly, the distance between the UAV and GD $k \in \mathcal { K }$ is $\begin{array} { r } { d _ { k } ( { \pmb u } ( t ) ) = \sqrt { \| { \pmb u } ( t ) - { \pmb c } _ { k } \| ^ { 2 } + H ^ { 2 } } } \end{array}$ at time instant $t \in \tau .$ Hence, the channel power gain between the UAV and GD $k \in \mathcal { K }$ at time $t \in \mathcal T$ is

![](images/6f1bff1020eb9d9275ca100c6b716a08fce4269c91546992e1d90bba170f44c2.jpg)  
Fig. 5. Illustration of the UAV-enabled WPT system in the case with multiple GDs.

$$
h _ { k } ( { \pmb u } ( t ) ) = \frac { \beta _ { 0 } } { \left\| { \pmb u } ( t ) - { \pmb c } _ { k } \right\| ^ { 2 } + H ^ { 2 } } .\tag{5}
$$

Similarly as $\bar { E } ( x ( t ) )$ in (3), the harvested power by $\mathrm { G D } k \in \mathcal { K }$ at time $t \in \mathcal T$ is given by

$$
\hat { E } _ { k } ( { \pmb u } ( t ) ) = \frac { \eta P \beta _ { 0 } } { \left\| { \pmb u } ( t ) - { \pmb c } _ { k } \right\| ^ { 2 } + H ^ { 2 } } .\tag{6}
$$

As a result, the total harvested energy by GD k over the entire period T is given by

$$
E _ { k } ( \{ { \pmb u } ( t ) \} ) = \int _ { 0 } ^ { T } \frac { \eta P \beta _ { 0 } } { \| { \pmb u } ( t ) - { \pmb c } _ { k } \| ^ { 2 } + H ^ { 2 } } \mathrm { d } t .\tag{7}
$$

How to design the UAV trajectory {u(t)} to maximize the harvested energy amounts at multiple GDs is a non-trivial problem, as there generally exists a tradeoff in balancing the harvested energy amounts $\{ E _ { k } ( \{ \pmb { u } ( t ) \} ) \}$ at these distributed GDs. For instance, setting $\mathbf { \boldsymbol { u } } ( t ) ~ = ~ \boldsymbol { c } _ { k }$ can maximize the harvested energy at GD $k ,$ but may decrease the harvested energy at other GDs that are far apart. To deal with this issue, we introduce a utility function $U ( \{ { \pmb u } ( t ) \} )$ to maximize, which fairly balances the harvested energy amounts at all these GDs, defined as the minimum weighted harvested energy among the K GDs, i.e.,

$$
U ( \{ { \pmb u } ( t ) \} ) = \operatorname* { m i n } \biggl \{ \frac { E _ { 1 } ( \{ { \pmb u } ( t ) \} ) } { a _ { 1 } } , \frac { E _ { 2 } ( \{ { \pmb u } ( t ) \} ) } { a _ { 2 } } , \dots , \frac { E _ { K } ( \{ { \pmb u } ( t ) \} ) } { a _ { K } } \biggr \} .\tag{8}
$$

Here, $a _ { k } > 0$ denotes the constant energy weight of GD $k \in$ $\kappa ,$ , a larger value of which means that GD k has a higher priority in maximizing its harvested energy.

Based on the utility function $U ( \{ { \pmb u } ( t ) \} )$ , we formulate a generic trajectory optimization problem for the single-UAVenabled WPT system as follows by taking into account practical UAV flight constraints.

$$
\begin{array} { r l } { ( \operatorname { P 1 } ) \colon \displaystyle \operatorname* { m a x } _ { \{ \pmb { u } ( t ) \} } } & { { } U ( \{ \pmb { u } ( t ) \} ) } \\ { \mathrm { s . t . ~ } } & { { } f _ { i } ( \{ \pmb { u } ( t ) \} ) \geq 0 , \forall i \in \{ 1 , \ldots , I \} , } \end{array}\tag{9}
$$

where $f _ { i } ( \cdot ) \mathbf { \bar { s } }$ represent constraint functions on the UAV’s trajectory and I denotes the number of such constraints. Some widely adopted UAV trajectory constraints are introduced as follows.

• Flight speed constraints: Suppose that the flight speed of UAV is constrained by a maximum value $V _ { \mathrm { m a x } } .$ , and thus

we have

$$
\begin{array} { r } { \| \dot { \boldsymbol { u } } ( t ) \| \le V _ { \operatorname* { m a x } } , \forall t \in \mathcal { T } , } \end{array}\tag{10}
$$

where ${ \dot { \pmb u } } ( t )$ denotes the first-order derivation of u(t) with respect to t.<sup>1</sup>

• Acceleration constraints: The acceleration of UAVs is also subject to a maximum value $V _ { \operatorname* { m a x } } ^ { A C }$ in practice. This corresponds to second-order constraints on u(t), given by

$$
\lVert \ddot { \boldsymbol { u } } ( t ) \rVert \leq V _ { \operatorname* { m a x } } ^ { A C } , \forall t \in \mathcal { T } ,\tag{11}
$$

where $\ddot { \pmb u } ( t )$ denotes the second-order derivation of $\pmb { u } ( t )$ with respect to t.

• Initial/final location constraints: The UAV normally needs to start/finish its flight mission at certain locations $( \mathrm { e . g . }$ at UAV stations for charging). Suppose that the initial and final locations of UAV are ${ \pmb u } _ { I }$ and ${ \pmb u } _ { F } ,$ respectively. We thus have

$$
{ \pmb u } ( 0 ) = { \pmb u } _ { I } , { \pmb u } ( T ) = { \pmb u } _ { F } .\tag{12}
$$

• Obstacle avoidance constraints: During flight, the UAV should stay away from obstacles in the space. Let o and $d _ { \mathrm { m i n } }$ denote the location of a certain obstacle and the minimum distance requirement from the obstacle, respectively. We thus have

$$
\| { \pmb u } ( t ) - { \pmb 0 } \| \geq d _ { \operatorname* { m i n } } , \forall t \in \mathcal { T } .\tag{13}
$$

Notice that problem (P1) involves an infinite number of optimization variables over continuous time and the objective function is non-concave with respect to {u(t)} in general. Therefore, problem (P1) is a challenging problem to be optimally solved. To tackle this problem, prior works have proposed various efficient algorithms to solve (P1) under different setups and flight constraints (see, e.g., [68]–[70]). In particular, the authors in [67] present a framework to optimize the trajectory by considering the flight speed constraints in (10), which will be detailed next.

Remark 1: It is worth noticing that the trajectory optimization problem (P1) for the single-UAV-enabled WPT is different from that for the UAV-enabled multiuser wireless communications (see, e.g., [79]). For the UAV-enabled multiuser communications, different GDs will suffer from the inter-user interference in general, and thus the UAV should design its trajectory to not only maximize the received signal power at desired GDs but also minimize the interference power towards non-desired GDs, under properly designed multiple access schemes. By contrast, for the single-UAV-enabled WPT of our interest, different GDs can harvest the wireless energy transferred from the UAV at the same time. Therefore, the conventional trajectory designs for UAV-enabled multiuser communications (see, e.g., [40]) are not applicable for the UAV-enabled WPT of our interest.

Remark 2: It is also worth noting that, the weighted sum harvested energy can also be adopted as a utility function to balance the harvested energy tradeoff among multiple GDs. However, it has been shown in [67] that due to the linear relationship between the harvested energy and the channel power gain, the UAV only needs to hover at one single fixed location during the whole charging period to maximize the weighted sum harvested energy of all GDs with their given weights. This solution may cause a severe fairness issue if the weights for GDs are not properly set, as the nearby GDs with the UAV can harvest significantly more energy than far-apart GDs. This issue resembles that with the weighted sum rate maximization adopted in UAV-enabled multiuser communications [80].

## C. Trajectory Design Framework

This subsection introduces the trajectory design framework in [67] to solve problem (P1). For exploitation, we only consider the speed constraints in (10) in problem (P1), and the presented trajectory design framework is extendable to the case with other flight constraints. By introducing an auxiliary variable $E ,$ problem (P1) with the speed constraints in (10) is re-formulated as

$$
\begin{array} { r l } { ( \mathrm { P 1 . 1 } ) \colon \ \underset { \{ \boldsymbol u ( t ) \} , E } { \operatorname* { m a x } } } & { E } \\ { \mathrm { s . t . } } & { E _ { k } ( \{ \boldsymbol u ( t ) \} ) / a _ { k } \geq E , \forall k \in \mathcal { K } } \\ & { \| \dot { \boldsymbol u } ( t ) \| \leq V _ { \operatorname* { m a x } } , \forall t \in \mathcal { T } . } \end{array}\tag{14}
$$

(15)

In the trajectory design framework [67], problem (P1.1) is first relaxed by ignoring the UAV flight speed constraints in (15), for which the optimal multi-location hovering solution is obtained via the Lagrange duality method [81]. Next, building upon the multi-location hovering solution, a heuristic successive hover-and-fly (SHF) trajectory is presented by leveraging the traveling salesman problem (TSP), such that the UAV can sequentially visit these hovering locations with a shortest path. Finally, the time quantization is implemented to transform the continuous-time trajectory design problem (P1.1) into an equivalent discrete-time trajectory design problem that is solvable via successive convex approximation (SCA) [82], in which the SHF trajectory is adopted as the initial point for iteration. The detailed procedure for solving (P1.1) is given as follows.

1) Multi-Location-Hovering Design: First, we consider the relaxed problem by ignoring the UAV flight speed constraints in (15), which may correspond to the practical case when the time duration T is sufficiently long. The relaxed problem is expressed as

$$
\begin{array} { r } { ( \mathrm { P 1 . 2 } ) \colon \ \underset { \{ \boldsymbol { u } ( t ) \} , E } { \operatorname* { m a x } } ^ { E } ^ { E } } \\ { \mathrm { s . t . ~ } \ ( 1 4 ) . } \end{array}
$$

Although problem (P1.2) is still non-convex, it can be shown that it satisfies the so-called time-sharing condition in [83]. Consequently, the strong duality holds between problem (P1.2) and its Lagrange dual problem. Therefore, the optimal solution to (P1.2) can be obtained by using the Lagrange duality method. Let $\lambda _ { k } \ \ge \ 0 , k \in \mathcal K$ , denote the dual variable associated with the k-th constraint in (14).

The Lagrangian of (P1.2) is

$$
\begin{array} { r l r } {  { \mathcal { L } _ { 1 } ( \{ \boldsymbol { u } ( t ) \} , \{ \lambda _ { k } \} , E ) = ( 1 - \sum _ { k \in \mathcal { K } } \lambda _ { k } ) E } } \\ & { } & { + \sum _ { k \in \mathcal { K } } \lambda _ { k } E _ { k } ( \{ \boldsymbol { u } ( t ) \} ) / a _ { k } . } \end{array}\tag{16}
$$

The dual function becomes

$$
g _ { 1 } \big ( \{ \lambda _ { k } \} \big ) = \operatorname* { m a x } _ { \{ \pmb { u } ( t ) \} , E } \ \mathcal { L } _ { 1 } \big ( \{ \pmb { u } ( t ) \} , \{ \lambda _ { k } \} , E \big ) .\tag{17}
$$

As a result, the dual problem of (P1.2) is

$$
\begin{array} { r l } { { \displaystyle ( \mathrm { D 1 . 2 } ) \colon \operatorname* { m i n } _ { \{ \lambda _ { k } \geq 0 \} } } } & { { } { { g _ { 1 } } ( \{ \lambda _ { k } \} ) } } \\ { { \mathrm { s . t . } } } & { { } { \displaystyle \sum _ { k \in \mathcal { K } } \lambda _ { k } = 1 , } } \end{array}\tag{18}
$$

where the equality in (18) must hold in order to ensure $g _ { 1 } ( \left\{ \lambda _ { k } \right\} )$ to be bounded [67]. Due to the strong duality between (P1.2) and (D1.2), the optimal solution to problem (P1.2) can be obtained by equivalently solving the dual problem (D1.2) as follows.

• First, for any given feasible dual variables $\{ \lambda _ { k } \}$ , solving problem (17) to obtain the dual function $g _ { 1 } ( \left\{ \lambda _ { k } \right\} )$ is equivalent to solving the following problem.

$$
\operatorname* { m a x } _ { \{ \boldsymbol { u } ( t ) \} } \ \int _ { 0 } ^ { T } \sum _ { k \in \mathcal { K } } \frac { \lambda _ { k } } { a _ { k } } \frac { \eta P \beta _ { 0 } } { \| \boldsymbol { u } ( t ) - \boldsymbol { c } _ { k } \| ^ { 2 } + H ^ { 2 } } \mathrm { d } t .\tag{19}
$$

Notice that in problem (19), the optimization of UAV trajectory {u(t)} is independent over time t. Therefore, solving problem (19) is equivalent to finding the (hovering) location that maximizes the weighted sum harvested energy of all GDs:

$$
\operatorname* { m a x } _ { \pmb { u } } \ \sum _ { k \in \mathcal { K } } \frac { \lambda _ { k } } { a _ { k } } \frac { \eta P \beta _ { 0 } } { \left\| \pmb { u } - \pmb { c } _ { k } \right\| ^ { 2 } + H ^ { 2 } } .\tag{20}
$$

The optimal solution to problem (20) can be obtained by using a 2D exhaustive search over a region $\left[ \underline { { x } } , \underline { { y } } \right] \times \left[ \bar { x } , \bar { y } \right]$ where $x \triangleq$ min $\{ x _ { k } \} , y \triangleq$ min $\{ y _ { k } \} , { \bar { x } } \triangleq$ max{x }, and $\bar { y } \triangleq \operatorname* { m a x } \{ y _ { k } \}$ . Let $\boldsymbol { u } ^ { \left\{ \overline { { \lambda } } _ { k } \right\} }$ denote the optimal solution to problem (20), which may not be unique in general. As a result, the dual function $g _ { 1 } ( \left\{ \lambda _ { k } \right\} )$ is obtained.

• Next, we find the optimal dual variables to solve the dual problem (D1.2). In general, the dual function $g _ { 1 } ( \left\{ \lambda _ { k } \right\} )$ is always convex but generally nondifferentiable. With $g _ { 1 } ( \left\{ \lambda _ { k } \right\} )$ obtained, we solve the dual problem by subgradient-based methods such as the ellipsoid method [81]. Let $\{ \lambda _ { k } ^ { \mathrm { o p t } } \}$ denote the optimal dual solution, and ${ \pmb u } _ { \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} } , \omega \in \{ 1 , \dots , \Omega \}$ , denote the optimal hovering location solution to problem (20) under $\{ \bar { \lambda } _ { k } ^ { \mathrm { o p t } } \}$ , where $\Omega \geq 1$ is the number of the (non-unique) hovering location solutions.

• Finally, we construct the optimal primal solution to problem (P1.2) based on the obtained ${ \pmb u } _ { \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} }$ from the optimal dual solution. As the solution ${ \pmb u } _ { \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} }$ is generally non-unique (i.e., $\Omega > 1$ generally holds), proper time sharing among these hovering locations is essential, such that the UAV should hover above the Ω locations over time to maximize the minimum weighted harvested energy. Let $\tau _ { \omega } ~ \geq ~ 0$ denote the time-sharing factor or equivalently the hovering duration at the ω-th location, $\omega \in \{ 1 , \dots , \Omega \}$ , which can be obtained via solving the following linear programming (LP).

$$
\begin{array} { r l r } {  { \operatorname* { m a x } _ { \{ \tau _ { \omega } \geq 0 \} } E } } \\ & { \quad \mathrm { s . t . } \ } & { \sum _ { \omega = 1 } ^ { \Omega } \tau _ { \omega } E _ { k } ( \{ u _ { \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} } \} ) / a _ { k } \geq E , \forall k \in K } \\ & { \quad } & { \displaystyle \sum _ { \omega = 1 } ^ { \Omega } \tau _ { \omega } = T . \ } & { ( 2 1 } \end{array}
$$

Suppose that the optimal solution to the LP is $\{ \tau _ { \omega } ^ { * } \}$ . Then the optimal solution to problem (P1.2) is obtained, which corresponds to that the UAV successively hovers among the Ω locations $\{ \pmb { u } _ { \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} } \} .$ }, each with duration $\boldsymbol { \tau } _ { \omega } ^ { \ast } .$ This is thus called the multi-location-hovering solution. Note that the performance achieved by this solution is the upper bound of the optimal value of problem (P1.1) with the speed constraints in (15).

2) SHF Trajectory Design: Next, building upon the multilocation-hovering solution to the relaxed problem (P1.2), a heuristic SHF trajectory design is presented by taking into account the $\mathrm { U A V } \mathbf { \hat { s } }$ flight speed constraints in (15). With the SHF trajectory, the UAV sequentially visits and hovers above each of the obtained hovering locations ${ \pmb u } _ { \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} }$ and then flies among them straightly at the maximum flight speed $V _ { \mathrm { m a x } } .$ How to properly order the visited hovering locations and optimize the hovering duration at each location is crucial.

Towards this end, we first determine the UAV’s traveling path to visit all the optimal hovering locations with minimum flying distance. It is shown in [67] that the traveling path minimization problem can be transformed into a modified TSP without initial and final locations,<sup>2</sup> and thus can be solved efficiently by using some well-established methods such as integer programming [85]. Next, the hovering duration optimization can be formulated as an LP similar to problem (21) by further taking into account the harvested energy during the straight flight (see [67, eq. (25)]). By combining the flight path and the hovering durations, the SHF trajectory design for solving (P1) is completed.

3) Time Quantization Based Optimization: Besides the SHF trajectory, time quantization is another widely adopted approach to obtain the trajectory based on convex optimization techniques. In particular, the whole mission duration is discretized into a finite number of N time slots, each with equal duration $\delta ~ = ~ T / N$ , where the duration δ is sufficiently small such that the UAV location is assumed to be approximately unchanged during each slot, denoted as $\pmb { u } [ n ] = \pmb { u } ( n \delta )$ Accordingly, the minimum harvested energy maximization problem in (P1.1) with continuous-time trajectory can be reformulated as the following problem (P1.3) with discrete-time waypoints.

![](images/2d0ad876d36bfaab7e20a6d2d61ad6321c698784150fdd79cf3af7489581abb6.jpg)  
Fig. 6. Simulation system setup and trajectory design for single-UAV-enabled WPT with K <sup>=</sup> 10 GDs.

$$
\begin{array}{c} \begin{array} { r l } { ( \mathrm { P 1 . 3 } ) \colon \displaystyle \operatorname* { m a x } _ { \{ u [ n ] \} , E } } & { E } \\ { \mathrm { s . t . ~ } } & { \displaystyle \operatorname* { m a x } _ { \begin{array} { c } { 1 } \\ { \mathcal { T } a _ { k } } \end{array} } \sum _ { n = 1 } ^ { N } \frac { \eta \delta P \beta _ { 0 } } { \| u [ n ] - c _ { k } \| ^ { 2 } + H ^ { 2 } } \ge E , } \\ & { \quad \quad \quad \forall k \in \mathcal { K } } \\ & { \quad \quad \quad \| u [ n ] - u [ n + 1 ] \| \le \delta V _ { \operatorname* { m a x } } , } \\ & { \quad \quad \quad \forall n \in \{ 1 , \ldots , N - 1 \} , } \end{array}  \end{array}\tag{22}
$$

(23)

where (23) is the time-quantized UAV flight speed constraints. Although problem (P1.3) is still non-convex, we can obtain a high-quality solution by utilizing the SCA technique, which approximates the non-convex problem into a sequence of convex problems (see [67, eq. (35)]) that can be efficiently solved by convex optimization techniques such as CVX [86]. It is shown that by properly choosing the approximate functions, the convergence of the iterative SCA algorithm can be ensured [67]. Note that the performance of SCA-based algorithm critically depends on the initial point of iteration, and the proposed SHF trajectory design can serve as a high-quality initial point.

## D. Numerical Results

This subsection presents numerical results to evaluate the performance of the above three trajectory design approaches, as compared to the benchmarking static hovering scheme without exploiting the UAV’s mobility over time. In the static hovering scheme, the UAV hovers at one single location over the whole mission period to maximize the minimum weighted harvested energy, i.e., max<sub>u</sub> min $\cdot k { \in } \mathcal { K } \{ \hat { E } _ { k } ( \{ { \pmb u } \} ) / a _ { k } \}$ , for which the optimal static hovering solution can be obtained via a 2D exhaustive search.

In this simulation, we consider a single-UAV-enabled WPT system with K = 10 GDs that are randomly distributed within a 2D area of $2 0 \times 2 0 \mathrm { ~ m } ^ { 2 }$ , as shown in Fig. 6, where the parameters are set same as those for Fig. 4, and the maximum speed of the UAV is $V _ { \mathrm { m a x } } = 5$ m/s. In order to balance the harvested energy among all the GDs, we consider that $a _ { k } =$ $1 , \forall k \in \mathcal { K }$

![](images/fad169d18fa53d8588a92609590534b55d1a05aaffea0ad774005cc3c413d79e.jpg)

Fig. 7. The minimum average harvested power of GDs versus the UAV mission duration T.  
![](images/86113f1fa5989fa861c8c62f8961a7a19e242905755b0dcd6b3c819505c661a4.jpg)  
Fig. 8. Illustration of the multi-UAV-enabled WPT.

Fig. 6 shows the obtained trajectories based on the proposed approaches and the static hovering, where $T = 5 0 \mathrm { ~ s } .$ . It is observed that there are 4 optimal hovering locations in the multi-location-hovering design, which are close to GDs 8-10, GDs 5-7, GD 4, and GDs 1-3, respectively, in order to charge them efficiently. It is also observed that the time-quantizationbased trajectory deviates from the straight line of the SHF trajectory to maximize the energy transfer efficiency during the flight.

Fig. 7 shows the minimum average harvested power among all the GDs versus the UAV mission duration T. It is observed that the SHF and time-quantization-based trajectory designs significantly outperform the static hovering scheme and the performance gain becomes more significant when T increases. The time-quantization-based trajectory is observed to outperform the SHF trajectory. Furthermore, when T is sufficiently large, the SHF and time-quantization-based trajectory designs are observed to perform close to the performance upper bound achieved by the multi-location-hovering solution with the UAV’s flight speed constraints ignored.

## III. MULTI-UAV-ENABLED WPT

The preceding section studied the trajectory design for single-UAV-enabled WPT, which, however, may not work well when there are many GDs in a large area. Therefore, this section considers the general multi-UAV-enabled WPT system as shown in Fig. 8, in which multiple UAVs are dispatched to cooperatively charge the GDs. Different from the trajectory design for single-UAV-enabled WPT, multiple UAVs need to cooperatively design their trajectories jointly with their energy transmission to maximize the energy transfer performance.

![](images/99e9b79384a144c6d0a3a4f03b40a1b66b2d3fe2fcff7dfddef0ec9d07afa22d.jpg)  
Fig. 9. Optimized UAV trajectories of multi-UAV-enabled WPT under the UAV swarming design.

Suppose that there are a set, $\mathcal { M } = \{ 1 , \dots , M \}$ , of singleantenna UAVs cooperatively charging a set, $\mathcal { K } = \{ 1 , \ldots , K \}$ of GDs over the charging period ${ \mathcal { T } } = ( 0 , T ]$ . At time instant $t \in { \mathcal { T } } ,$ let ${ \pmb u } _ { m } ( t ) , m \in \mathcal { M }$ , denote the horizontal location of UAV m. Supposing that all UAVs stay at the same altitude H, the distance between UAV m and GD k is $d _ { k , m } ( { \pmb u } _ { m } ( t ) ) =$ $\sqrt { \| \boldsymbol { \mathbf { u } } _ { m } ( t ) - \boldsymbol { \mathbf { c } } _ { k } \| ^ { 2 } + H ^ { 2 } }$ . Under the LoS channel assumption, we express the channel coefficient between UAV m and GD k as follows, by considering the free-space path loss together with a random phase.

$$
\bar { h } _ { k , m } ( { \pmb u } _ { m } ( t ) ) \big ) = \sqrt { \frac { \beta _ { 0 } } { \| { \pmb u } _ { m } ( t ) - { \pmb c } _ { k } \| ^ { 2 } + H ^ { 2 } } } e ^ { j \theta _ { k , m } ( t ) } ,\tag{24}
$$

where $~ j ~ = ~ { \sqrt { - 1 } }$ , and $\theta _ { k , m } ( t )$ denotes the random phase that is assumed to be a uniformly distributed random variable in [0, 2π). Notice that similar channel models in (24) have been widely adopted in the UAV-enabled wireless communication literature (see, e.g., [42]), in order to capture the fact that the channel phase changes much more rapidly in practice than the free-space path loss.<sup>3</sup> By collecting the wireless channels from different UAVs, we denote $\bar { h } _ { k } ( t ) =$ $[ \bar { h } _ { k , 1 } ( t ) , \bar { h } _ { k , 2 } ( t ) , \dots , \bar { h } _ { k , M } ( t ) ] ^ { T }$ as the channel vector from the M UAVs to each GD $k \in \mathcal { K }$

Next, we consider the cooperative energy transmission at the M UAVs. Let $s _ { m } ( t )$ denote the transmit energy signal at each UAV $m \in { \mathcal { M } }$ , and $\pmb { \mathscr { s } } ( t ) = [ \mathscr { s } _ { 1 } ( t ) , \mathscr { \ldots } , \mathscr { s } _ { m } ( \bar { t } ) ] ^ { T }$ denote the collective transmit signals by the M UAVs. Accordingly, we denote $\pmb { S } ( t ) = \mathbb { E } [ \pmb { s } ( t ) \overline { { \pmb { s } ^ { H } ( t ) } } ]$ as the transmit energy covariance matrix. Notice that if $\mathbf { \boldsymbol { S } } ( t )$ is a diagonal matrix, then the M UAVs design their respective transmit energy signals independently, while if ${ \mathbf { } } S ( t )$ is of rank-one, then the M UAVs use cooperative beamforming to send one energy beam with common energy signals. In this case, the total harvested energy of GD $k \in \mathcal { K }$ over the entire period T is

$$
\tilde { E } _ { k } ( \{ \mathbf { \boldsymbol { u } } _ { m } ( t ) , \mathbf { \boldsymbol { S } } ( t ) \} ) = \int _ { 0 } ^ { T } \mathbb { E } \Big [ \eta \bar { \boldsymbol { h } } _ { k } ^ { H } ( t ) \mathbf { \boldsymbol { S } } ( t ) \bar { \boldsymbol { h } } _ { k } ( t ) \Big ] \mathrm { d } t ,\tag{25}
$$

where the expectation is taken with respect to the randomness in the channel phases.

It is observed in (25) that the harvested energy amounts at the K GDs are related to both the M $\mathrm { U A V s } '$ trajectories $\{ { \pmb u } _ { m } ( t ) \}$ and their transmit covariance matrices {S(t)}. Therefore, in order to maximize the harvested energy at the K GDs, we should jointly optimize both $\{ \pmb { u } _ { m } ( t ) \}$ and {S(t)}. Similarly as in (8) for single-UAV-enabled WPT, we define the utility function for multi-UAV-enabled WPT as

$$
\begin{array} { r l } & { U ( \{ { \pmb u } _ { m } ( t ) , { \pmb S } ( t ) \} ) } \\ & { \quad = \operatorname* { m i n } \biggr \{ \frac { E _ { 1 } ( \{ { \pmb u } _ { m } ( t ) , { \pmb S } ( t ) \} ) } { a _ { 1 } } , \frac { E _ { 2 } ( \{ { \pmb u } _ { m } ( t ) , { \pmb S } ( t ) \} ) } { a _ { 2 } } , } \\ & { \quad \quad \quad \cdots , \frac { E _ { K } ( \{ { \pmb u } _ { m } ( t ) , { \pmb S } ( t ) \} ) } { a _ { K } } \biggr \} . } \end{array}\tag{26}
$$

As a result, we have the generic utility maximization problem for multi-UAV-enabled WPT as

$$
\begin{array} { r l r } { ( \mathrm { P 2 } ) \colon \displaystyle \operatorname* { m a x } _ { \{ \pmb { u } _ { m } ( t ) , S ( t ) \} } } & { U ( \{ \pmb { u } _ { m } ( t ) , S ( t ) \} ) } & \\ { \mathrm { s . t . } \quad f _ { i , m } ( \{ \pmb { u } _ { m } ( t ) \} ) \geq 0 , \forall i \in \{ 1 , \ldots , I \} , } & \\ & { \quad \quad \quad m \in \mathcal { M } } & { ( 2 } \end{array}\tag{27}
$$

$$
\bar { f } _ { l } ( \{ \mathbf { \boldsymbol { u } } _ { m } ( t ) \} ) \ge 0 , \forall l \in \{ 1 , \dots , L \}\tag{28}
$$

$$
\begin{array} { r } { p _ { j } ( \pmb { S } ( t ) ) \geq 0 , \forall j \in \{ 1 , \dots , J \} , } \end{array}\tag{29}
$$

where $f _ { i , m } ( \cdot )  { \mathrm { \mathbf { s } } }$ denote the flight constraints for each individual UAV m similarly as in (9), and $\bar { f } _ { l } ( \cdot ) \cdot \mathrm { \mathbf { s } }$ denote the joint flight constraints for multiple UAVs with L representing the number of such constraints. For instance, the collision avoidance constraints to ensure safe flight for multiple UAVs can be given by

$$
\begin{array} { r } { \left\| { \boldsymbol u } _ { i } ( t ) - { \boldsymbol u } _ { j } ( t ) \right\| \geq d _ { \operatorname* { m i n } } , \forall i , j \in \mathcal { M } , i \neq j , t \in \mathcal { T } , } \end{array}\tag{30}
$$

where $d _ { \mathrm { m i n } }$ denotes the safety distance between any two different UAVs. Moreover, $p _ { j } ( \cdot ) \mathrm { ^ { \circ } s }$ represent the constraints on the transmit signals at UAVs with J representing the number of such constraints. For example, supposing that each UAV m is subject to a maximum transmit power $P _ { m }$ , we have the individual power constraints as ${ \mathrm { T r } } ( C _ { m } { \cal { S } } ( t ) ) \ \leq \ P _ { m } , \forall t \ \in$ $\tau , m \in \mathcal { M }$ , where $C _ { m }$ denotes a matrix with only the element in the m-th column and m-th row being 1 and all the other elements being 0. Assuming that the sum power of all the M UAVs are constrained by a maximum value $P _ { \mathrm { s u m } }$ , we have the sum-power constraints as $\mathrm { T r } ( S ( t ) ) \leq P _ { \mathrm { s u m } } , \forall t \in \mathcal { T } .$ In the following, we consider the individual power constraints for UAVs with $P _ { m } = P , \forall m \in \mathcal { M }$

It is worth noting that problem (P2) is much more challenging to be optimally solved than problem (P1) due to the involvement of multiple UAVs’ trajectories and their transmit covariance matrices, and such joint optimization may require information sharing among different UAVs. While finding the optimal solution to problem (P2) is still open and has not been investigated in the literature yet, in the next two subsections, we propose two heuristic designs based on the principles of UAV swarming and GD clustering, respectively, by extending the trajectory design framework for single-UAV-enabled WPT in Section II.

## A. UAV Swarming With TDMA Based Beamforming

First, we consider the UAV swarming based design, in which all UAVs are formed into a swarm to fly following the same speed and orientation. Suppose that UAV 1 acts as the swarm head with the time-varying location being ${ \mathbf { } } u _ { 1 } ( t ) = ( x _ { 1 } ( t ) , y _ { 1 } ( t ) )$ at time $t \in \tau .$ Furthermore, assuming that the UAVs’ formation is fixed over time, the location of $\mathrm { U A V } \ i \ \in \ \{ 2 , \dots , M \}$ is given as ${ \mathbf { } } { \mathbf { } } { \mathbf { } } ( t ) = { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } ( t ) + { \mathbf { } } { \mathbf { } } b _ { i } ,$ where $b _ { i }$ denotes its relative coordinate with respect to $\mathbf { \delta } \mathbf { u } _ { 1 }$ . For example, supposing that there are four UAVs that are formed into a square with edge length $d _ { \mathrm { m i n } } .$ , then the coordinates of UAVs 2, 3, and 4 at time t can be expressed as ${ \bf { u } } _ { 2 } ( t ) = { \bf { \epsilon } }$ $( x _ { 1 } ( t ) , y _ { 1 } ( t ) - d _ { \operatorname* { m i n } } ) , \ : u _ { 3 } ( t ) = ( x _ { 1 } ( t ) - d _ { \operatorname* { m i n } } , y _ { 1 } ( t ) - d _ { \operatorname* { m i n } } )$ and ${ \pmb u } _ { 4 } ( t ) = ( x _ { 1 } ( t ) - d _ { \operatorname* { m i n } } , y _ { 1 } ( t ) )$ , respectively. In this case, the design of multiple UAVs’ trajectories in problem (P2) is reduced into the design of trajectory $\{ { \pmb u } _ { 1 } ( t ) \}$ for the swarm head UAV 1 only.<sup>4</sup>

Next, we consider the design of transmit covariance matrices {S(t)}. While finding the optimal {S(t)} is non-trivial, we consider the TDMA-based beamforming design, in which all UAVs cooperatively send one energy beam towards one GD at each time. At time instant $t \in \tau ,$ let $\tau _ { E , k } ( t ) \ \in \ \{ 0 , 1 \}$ denote an energy beamforming indicator, where $\tau _ { E , k } ( t ) = 1$ denotes that the M UAVs design the energy beam towards GD k at time t, and $\tau _ { E , k } ( t ) ~ = ~ 0$ otherwise. Therefore, we have $\begin{array} { r } { \sum _ { k \in \mathcal { K } } \tau _ { E , k } ( t ) \ = \ 1 , \forall t \ \in \ \mathcal { T } . } \end{array}$ Accordingly, under $\tau _ { E , k } ( t ) = 1$ , each UAV m $\in \mathcal { M }$ sets the transmitted signal as $\sqrt { P } e ^ { j \phi _ { m , k } ( t ) } s ^ { E }$ , where $s ^ { E }$ denotes the common energy signal with unit power, and $\phi _ { m , k } ( t ) = - \theta _ { k , m } ( t )$ , such that the energy signals will be coherently combined at GD $k . ^ { 5 }$ In this case, the harvested power by GD k is given by

$$
\begin{array} { r l r } {  { \tilde { E } _ { k } ( \{ \mathbf { \boldsymbol { u } } _ { m } ( t ) \} ) = \eta \mathbb { E } [ | \sum _ { m = 1 } ^ { M } \sqrt { P } | \bar { h } _ { k , m } ( t ) | s ^ { E } | ^ { 2 } ] } } \\ & { } & { = \eta P ( \sum _ { m = 1 } ^ { M } \sqrt { \frac { \beta _ { 0 } } { \| \mathbf { \boldsymbol { u } } _ { m } ( t ) - \mathbf { \boldsymbol { c } } _ { k } \| ^ { 2 } + H ^ { 2 } } } ) ^ { 2 } , } \end{array}\tag{31}
$$

and that by any other GD ${ \bar { k } } \in { \mathcal { K } } \backslash \{ k \}$ with $\tau _ { E , \bar { k } } = 0$ (without coherent combining) is

$$
\begin{array} { r l r } {  { E _ { \vec { k } } ^ { \prime } ( \{ \boldsymbol { u } _ { m } ( t ) \} ) } } \\ & { } & { = \eta \mathbb { E } [ | ( \sum _ { m = 1 } ^ { M } \sqrt { P } \bar { h } _ { \vec { k } , m } ( t ) e ^ { j ( \theta _ { k , m } ( t ) - \theta _ { \vec { k } , m } ( t ) ) } ) s ^ { E } | ^ { 2 } ] } \\ & { } & { = \eta P \sum _ { m = 1 } ^ { M } \frac { \beta _ { 0 } } { \| \boldsymbol { u } _ { m } ( t ) - \boldsymbol { c } _ { \vec { k } } \| ^ { 2 } + H ^ { 2 } } . } \end{array}\tag{32}
$$

Therefore, the harvested power by GD k at time $t \in \tau$ is given by

$$
\begin{array} { r l } & { \tilde { E } _ { k } ^ { \mathrm { h a r } } \bigl ( \{ { \pmb u } _ { m } ( t ) \} , \tau _ { E , k } ( t ) \bigr ) } \\ & { \quad = \Bigl ( \tau _ { E , k } ( t ) \tilde { E } _ { k } ( \{ { \pmb u } _ { m } ( t ) \} ) + \bigl ( 1 - \tau _ { E , k } ( t ) \bigr ) E _ { k } ^ { \prime } ( \{ { \pmb u } _ { m } ( t ) \} ) \Bigr ) . } \end{array}\tag{33}
$$

The total harvested energy by GD k over the entire period $\tau$ is given by

$$
\tilde { E } _ { k } ^ { \mathrm { t o t } } \big ( \{ { \boldsymbol u } _ { m } ( t ) , \tau _ { E , k } ( t ) \} \big ) = \int _ { 0 } ^ { T } \tilde { E } _ { k } ^ { \mathrm { h a r } } \big ( { \boldsymbol u } _ { m } ( t ) , \tau _ { E , k } ( t ) \big ) \mathrm { d } t .\tag{34}
$$

Under the UAV swarming and TDMA-based beamforming designs and by considering the UAV flight speed constraints only (similarly as in Section II), the utility maximization problem (P2) is simplified as

$$
( \mathrm { P 2 . 1 } ) \colon \operatorname* { m a x } _ { \{ \boldsymbol { u } _ { 1 } ( t ) , \tau _ { E , k } ( t ) \} } \ \operatorname* { m i n } _ { k \in \mathcal K } \tilde { E } _ { k } ^ { \mathrm { t o t } } \big ( \{ \boldsymbol { u } _ { m } ( t ) , \tau _ { E , k } ( t ) \} \big ) / a _ { k }
$$

$$
\begin{array} { r } { \mathbf { s . t . } \qquad \| \dot { \pmb { u } } _ { 1 } ( t ) \| \le V _ { \operatorname* { m a x } } , \forall t \in \mathcal { T } } \end{array}\tag{35}
$$

$$
\tau _ { E , k } ( t ) \in \{ 0 , 1 \} , \forall k \in \mathcal { K } , t \in \mathcal { T } ( 3 6 )
$$

$$
\sum _ { k \in \mathcal { K } } \tau _ { E , k } ( t ) = 1 , \forall t \in \mathcal { T } ,\tag{37}
$$

which can be equivalently re-written as follows by introducing an auxiliary variable $\tilde { E }$

$$
\begin{array} { r l r } {  { \big ( \mathrm { P 2 . 2 } \big ) \colon \operatorname* { m a x } _ { \mathbf { \mu } \{ u _ { 1 } ( t ) , \tau _ { E , k } ( t ) \} , \tilde { E } } } } & { \tilde { E } } \\ & { \ \mathrm { s . t . ~ } \tilde { E } _ { k } ^ { \mathrm { t o t } } \big ( \big \{ { u _ { m } ( t ) , \tau _ { E , k } ( t ) } \big \} \big ) / a _ { k } \geq \tilde { E } , \forall k \in \mathcal { K } } & \\ & { \ \mathrm { ~ ( 3 5 ) , ~ ( 3 6 ) , ~ a n d ~ ( 3 7 ) } , } \end{array}\tag{38}
$$

in which only the trajectory design of the swarm head (UAV 1) needs to be optimized, jointly with the beamforming indicators $\{ \tau _ { E , k } ( t ) \}$ . It is observed that problem (P2.1)/(P2.2) has similar structures as (P1.1)/(P1.2), except the newly involved beamforming indicators $\{ \tau _ { E , k } ( t ) \}$ . Motivated by this, in the following we extend the trajectory design framework in Section II-C to solve problem (P2.1)/(P2.2).

1) Multi-Location-Hovering Design: Firstly, we consider the following relaxed problem by ignoring the UAV flight speed constraints in (35).

$$
\begin{array} { r } { ( \mathrm { P 2 . 3 } ) \colon \underset { \{ u _ { 1 } ( t ) , \tau _ { E , k } ( t ) \} , \tilde { E } } { \mathrm { m a x } } \quad \tilde { E } \quad \quad } \\ { \quad \quad \quad \quad \quad \mathrm { s . t . } \quad \ ( 3 6 ) , \ ( 3 7 ) , \ \mathrm { a n d } \ ( 3 8 ) . } \end{array}
$$

Similarly as for problem (P1.2), although problem (P2.3) is still non-convex, the strong duality holds between (P2.3) and its dual problem. Therefore, the optimal solution to (P2.3) can be obtained by using the Lagrange duality method. Let $\lambda _ { k } \geq$ $0 , k \in \mathcal { K }$ denote the dual variable associated with the k-th constraints in (38). The partial Lagrangian of (P2.3) is

$$
\begin{array} { r l r } {  { \mathcal L _ { 2 } \Big ( \{ \boldsymbol u _ { m } ( t ) , \boldsymbol \tau _ { E , k } ( t ) , \boldsymbol \lambda _ { k } \} , \tilde { E } \Big ) } } \\ & { } & { = ( 1 - \sum _ { k \in { \cal K } } \lambda _ { k } ) \tilde { E } + \int _ { 0 } ^ { T } \sum _ { k \in { \cal K } } \lambda _ { k } \tilde { E } _ { k } ^ { \mathrm { h a r } } \big ( \boldsymbol u _ { m } ( t ) , \boldsymbol \tau _ { E , k } ( t ) \big ) \mathrm { d } t . } \end{array}\tag{39}
$$

The dual function becomes

$$
\begin{array} { r } { g _ { 2 } ( \{ \lambda _ { k } \} ) = \underset { \left\{ u _ { m } ( t ) , \tau _ { E , k } ( t ) \right\} , \tilde { E } } { \mathrm { m a x } } ~ \mathcal { L } _ { 2 } \Big ( \big \{ u _ { m } ( t ) , \tau _ { E , k } ( t ) , \lambda _ { k } \big \} , \tilde { E } \Big ) } \\ { \mathrm { s . t . } ~ ( 3 6 ) , ~ ( 3 7 ) . } \end{array}
$$

As a result, the dual problem of (P2.3) is

$$
\begin{array} { r l } { { \displaystyle ( \mathrm { D 2 . 3 } ) \colon \operatorname* { m i n } _ { \{ \lambda _ { k } \geq 0 \} } } } & { { } q _ { 2 } ( \{ \lambda _ { k } \} ) } \\ { { \mathrm { s . t . ~ } } } & { { } \displaystyle \sum _ { k \in \mathcal { K } } \lambda _ { k } = 1 . } \end{array}\tag{41}
$$

The optimal solution to (P2.3) can be obtained by equivalently solving (D2.3). First, for any given feasible dual variables, the dual function $g _ { 2 } ( \left\{ \lambda _ { k } \right\} )$ in (40) can be obtained by solving the following problem.

$$
\begin{array} { r l } { \displaystyle \operatorname* { m a x } _ { \left\{ \pmb { u } _ { 1 } ( t ) , \tau _ { E , k } ( t ) \right\} } } & { \displaystyle \int _ { 0 } ^ { T } \sum _ { k \in \mathcal { K } } \lambda _ { k } \tilde { E } _ { k } ^ { \mathrm { h a r } } \big ( \pmb { u } _ { m } ( t ) , \tau _ { E , k } ( t ) \big ) \mathrm { d } t } \\ { \mathrm { s . t . ~ } } & { \mathrm { ( 3 6 ) , ~ ( 3 7 ) . } } \end{array}\tag{42}
$$

As problem (42) consists of infinite number of identical sub-problems for different time t, solving problem (42) is equivalent to

$$
\operatorname* { m a x } _ { u _ { 1 } , \left\{ \tau _ { E , k } \right\} } \ \sum _ { k \in \mathcal { K } } \lambda _ { k } \eta P \left( \tau _ { E , k } \left( \sum _ { m = 1 } ^ { M } \sqrt { \frac { \beta _ { 0 } } { \| u _ { m } - c _ { k } \| ^ { 2 } + H ^ { 2 } } } \right) ^ { \frac { \alpha } { 2 } } \right)
$$

$$
+ \sum _ { m = 1 } ^ { M } \frac { \bigl ( 1 - \tau _ { E , k } \bigr ) \beta _ { 0 } } { \left\| \boldsymbol { u } _ { m } ( t ) - \boldsymbol { c } _ { \bar { k } } \right\| ^ { 2 } + H ^ { 2 } } \biggr )\tag{43}
$$

$$
\mathbf { s . t . } ~ \tau _ { E , k } \in \{ 0 , 1 \} , \forall k \in \mathcal { K }\tag{44}
$$

$$
\sum _ { k \in \mathcal { K } } \tau _ { E , k } = 1 ,\tag{45}
$$

for each time $t \in \tau .$ Note that for the optimization of the beamforming indicators $\{ \tau _ { E , k } \}$ in (43), there are K feasible choices satisfying constraints (44) and (45), each with $\tau _ { E , k } =$ $1 , k \in { \mathcal { K } } .$ , and accordingly $\tau _ { E , \bar { k } } = 0 , \forall \bar { k } \in \mathcal { K } , \bar { k } \neq k$ . Under $\tau _ { E , k } = 1$ , problem (43) is equivalent to finding the optimal hovering location via solving the following problem:

$$
\begin{array} { r l } { } & { \displaystyle { \operatorname* { m a x } _ { u _ { 1 } } { \ \lambda _ { k } \eta { \cal P } } } \left( \displaystyle { \sum _ { m = 1 } ^ { M } \sqrt { \frac { \beta _ { 0 } } { \| u _ { m } - c _ { k } \| ^ { 2 } + H ^ { 2 } } } } \right) ^ { 2 } } \\ & { + \displaystyle { \sum _ { \bar { k } \in K \backslash \{ k \} } \lambda _ { \bar { k } } \eta { \cal P } } \displaystyle { \sum _ { m = 1 } ^ { M } \frac { \beta _ { 0 } } { \big \| u _ { m } - c _ { \bar { k } } \big \| ^ { 2 } + H ^ { 2 } } } , } \end{array}\tag{46}
$$

which can be solved by using a 2D exhaustive search. Hence, by comparing the obtained optimal values under the K choices for problem (46), the optimal solution to problem (43) can be obtained as ${ \pmb u } _ { 1 } ^ { \{ \lambda _ { k } \} }$ and $\tau _ { E , k } ^ { \left\{ \lambda _ { k } \right\} }$ , and accordingly the dual function $g _ { 2 } ( \left\{ \lambda _ { k } \right\} )$ is also obtained. Note that if any two of the K optimal values are equal, then the optimal solution to problem (43) can be non-unique, which leads to multiple hovering locations corresponding to energy beamforming design towards different GDs.

Next, we use subgradient-based methods to solve the dual problem (D2.3), where $\{ \lambda _ { k } ^ { \mathrm { o p t } } \}$ denote the accordingly obtained optimal dual solution. Under $\{ \lambda _ { k } ^ { \mathrm { o p t } } \}$ , let $\mathcal { K } ^ { \mathrm { o p t } }$ denote the set of GD k’s such that $\tau _ { E , k } ^ { \left\{ \lambda _ { k } ^ { \mathrm { o p t } } \right\} } = 1$ is one (non-unique) solution to (43) for any $k \in \mathcal { K } ^ { \mathrm { o p t } }$ , and ${ \pmb u } _ { 1 , k , \omega } ^ { \{ \lambda _ { k } ^ { \mathrm { o p t } } \} } , \omega \in \{ 1 , \dots , \Omega _ { k } \}$ denote the optimal hovering location solution to problem (46) under any $k \ \in \ \mathcal { K } ^ { \mathrm { o p t } }$ , with $\Omega _ { k }$ denoting the corresponding number of optimal hovering locations. In this case, there are a total number of $\textstyle \sum _ { k \in K ^ { \mathrm { o p t } } } \Omega _ { k }$ optimal hovering locations.

Finally, based on these optimal hovering locations, we need to time share among them via solving an LP similarly to problem (21). By implementing this, the optimal multilocation-hovering solution to primal problem (P2.3) is found, in which the UAVs need to hover among the $\textstyle \sum _ { k \in K ^ { \mathrm { o p t } } } \Omega _ { k }$ locations over time, over each of which the UAVs need to accordingly design the beamforming towards the corresponding GD.

2) SHF Trajectory Design: Next, by taking into account the UAV flight speed constraints, the SHF trajectory design can be constructed via using the TSP algorithm, in which the UAV swarm visits and hovers above each of the above obtained optimal hovering locations and flies among them straightly at the maximum flight speed $V _ { \mathrm { m a x } }$ . Under the flight path obtained by TSP, we still need to optimize the hovering duration at each location and the beamforming indicators over time. However, the optimization of beamforming indicators involves an infinite number of variables. To tackle this issue, we can quantize the entire UAV charging period into a finite number of equal-duration time slots, in each of which the UAV swarm is assumed to be stay at fixed locations. Furthermore, we can divide each time slot into K sub-slots with variable durations, and in each sub-slot k, all UAVs design their energy beamforming towards GD k. In this case, the optimization of hovering durations and beamforming indicators corresponds to optimizing the durations of sub-slots over time, which can be found via solving an LP.

3) Time Quantization Based Optimization: Finally, we can directly adopt time quantization to transform problem (P2.2) with continuous-time variables into an equivalent optimization problem with discrete-time variables. We discretize the whole charging period T into a set $\mathcal { N } \triangleq \{ 1 , \dots , N \}$ of time slots each with equal duration $\delta = T / N$ , and further divide each slot to K sub-slots, during each of which the UAVs perform cooperative energy beamforming towards GD k. At time slot $n \in \mathcal N ,$ let ${ \pmb u } _ { m } [ n ] = { \pmb u } ( n \delta ) , m \in \mathcal { M }$ , denote the UAV m’s location and $\tau _ { E , k } [ n ] , k \in \mathcal { K }$ denote the duration of sub-slot $k ,$ where we have $\begin{array} { r } { \sum _ { k \in \mathcal { K } } \tau _ { E , k } [ n ] = \delta } \end{array}$ . Accordingly, by introducing two sets of auxiliary variables of $\{ \alpha _ { k , m } [ n ] \}$ and $\{ A _ { k } [ n ] \}$ problem (P2.2) is reduced to

$$
\begin{array} { c } { { \mathrm { { } } } } \\ { { \vdots \qquad \mathrm { { m a x } } \qquad } } \\ { { \{ u _ { 1 } [ n ] , \tau _ { E , k } [ n ] { \geq } 0 \} , \tilde { E } , \qquad } } \\ { { \{ \alpha _ { k } [ n ] { \geq } 0 \} , \{ A [ n ] { \geq } 0 \} } } \end{array}\tag{P2.3):}
$$

$$
\mathfrak { s . t . } \frac { \eta P } { T a _ { k } } \sum _ { n = 1 } ^ { N } \left( \tau _ { E , k } [ n ] A _ { k } [ n ] + \left( \delta - \tau _ { E , k } [ n ] \right) \sum _ { m = 1 } ^ { M } \Phi _ { k , m } ( \boldsymbol { u } _ { m } [ n ] ) \right)
$$

$$
\ge \tilde { E } , \forall k \in \mathcal { K }\tag{47}
$$

$$
A _ { k } [ n ] \leq \Psi { \big ( } \alpha _ { k , m } [ n ] { \big ) } , \forall k \in K , n \in \mathcal { N }\tag{48}
$$

$$
\alpha _ { k , m } ^ { 2 } [ n ] \leq \Phi _ { k } ( \boldsymbol { \mathbf { u } } _ { m } [ n ] ) , \forall k \in \mathcal { K } , m \in \mathcal { M } , n \in \mathcal { N }\tag{49}
$$

$$
\sum _ { k \in \mathcal { K } } \tau _ { E , k } [ n ] = \delta , \forall n \in \mathcal { N }\tag{50}
$$

where $\begin{array} { r l r } { \Phi _ { k , m } ( { \pmb u } _ { m } [ n ] ) \qquad } & { { } = } & { \qquad \frac { \beta _ { 0 } } { \| { \pmb u } _ { m } [ n ] - { \pmb c } _ { k } \| ^ { 2 } + H ^ { 2 } } } \end{array}$ and $\begin{array} { c c l } { \Psi _ { k } ( \alpha _ { k , m } [ n ] ) } & { = } & { ( \sum _ { m = 1 } ^ { M } \alpha _ { k , m } [ n ] ) ^ { \dagger } } \end{array}$ . However, the constraints in $( 4 7 ) \AA - ( 4 9 )$ are still non-convex due to the coupling of the time allocation and UAV trajectory. Therefore, we apply an alternating-optimization-based method to solve this problem iteratively, in which we alternately optimize the time allocation and the UAV trajectory by assuming the other to be given.

Under given trajectory $\{ { \pmb u } _ { 1 } [ n ] \}$ (and equivalently $\{ \boldsymbol { { u } } _ { m } [ n ] \} )$ , the optimization of the time allocation $\{ \tau _ { E , k } [ n ] \}$ corresponds to an LP, which can be efficiently solved by CVX. Therefore, we only need to focus on optimizing the UAV trajectory.

Under any given time allocation $\{ \tau _ { E , k } [ n ] \}$ , the UAV trajectory optimization is still non-convex, due to the non-convex constraints (47)-(49). To deal with these non-convex constraints, we update the UAV swarm head’s trajectory $\{ { \pmb u } _ { 1 } [ n ] \}$ (equivalently $\{ { \pmb u } _ { m } [ n ] \} )$ and $\{ \alpha _ { k , m } [ n ] \}$ in an iterative manner by applying the SCA method. Let $\{ \boldsymbol { u } _ { 1 } ^ { ( i ) } [ n ] \}$ and $\{ \alpha _ { k , m } ^ { ( i ) } [ n ] \}$ denote the local points at the i-th iteration. By taking the Taylor expansion at any point, the lower bounds of $\Psi _ { k } \mathopen { } \mathclose \bgroup \left( \alpha _ { k , m } \aftergroup \egroup [ n \aftergroup \egroup \right) \mathclose { ) }$ and $\Phi _ { k , m } ( { \boldsymbol { \mathbf { u } } } _ { m } [ n ] )$ are given by

$$
\geq \Psi _ { k } \Big ( \alpha _ { k , m } ^ { ( i ) } [ n ] \Big ) + \Psi _ { k } ^ { \prime } \Big ( \alpha _ { k , m } ^ { ( i ) } [ n ] \Big ) \Big ( \alpha _ { k , m } [ n ] - \alpha _ { k , m } ^ { ( i ) } [ n ] \Big ) \Big )
$$

$$
\triangleq \Psi _ { k } ^ { \mathrm { l o w } } \big ( \alpha _ { k , m } [ n ] \big ) ,\tag{51}
$$

$$
\Phi _ { k , m } ( { \boldsymbol { \mathbf { u } } } _ { m } [ n ] )
$$

$$
\begin{array} { r l } & { \geq \Phi _ { k , m } \Big ( \pmb { u } _ { m } ^ { ( i ) } [ n ] \Big ) + \Phi _ { k , m } ^ { \prime } \Big ( \pmb { u } _ { m } ^ { ( i ) } [ n ] \Big ) \Big ( \pmb { u } _ { m } [ n ] - \pmb { u } _ { m } ^ { ( i ) } [ n ] \Big ) } \end{array}
$$

$$
\triangleq \Phi _ { k } ^ { \mathrm { l o w } } ( \boldsymbol { u } _ { m } [ n ] ) .\tag{52}
$$

By replacing $\Psi _ { k } \mathopen { } \mathclose \bgroup \left( \alpha _ { k , m } \aftergroup \egroup [ n \aftergroup \egroup \right) \mathclose { ) }$ and $\Phi _ { k , m } ( { \boldsymbol { \mathbf { u } } } _ { m } [ n ] )$ $\Psi _ { k } ^ { \mathrm { l o w } } ( \alpha _ { k , m } [ n ] )$ and $\Phi _ { k } ^ { \mathrm { l o w } } ( { \pmb u } _ { m } [ n ] )$ , we have

as

$$
\begin{array} { r l r }  \displaystyle \operatorname* { m a x } _ { \left\{ \substack { a _ { 1 } \nmid \cdot \} , \tilde { F } \geq 0 , } } } & { \\right\tilde { E } } & \\ { \displaystyle \lbrace \alpha _ { k , m } [ n ] \geq 0 , \{ 4 _ { k } [ n ] \geq 0 \} } & \\ { \displaystyle \otimes . \mathbf { t } . \frac { \eta { P } } { a _ { k } T } \sum _ { n = 1 } ^ { N } \Biggl ( \tau _ { E , k } [ n ] A _ { k } [ n ] + \left( \delta - \tau _ { E , k } [ n ] \right) \sum _ { m = 1 } ^ { M } \Phi _ { k } ^ { \mathrm { l o w } } ( \boldsymbol { u } _ { m } [ n ] ) \Biggr ) } & \\ { \displaystyle \geq \tilde { E } , \forall k \in K } & \\ { \displaystyle A _ { k } [ n ] \leq \Psi _ { k } ^ { \mathrm { l o w } } \left( \alpha _ { k , m } [ n ] \right) , \forall k \in K , n \in \mathcal { N } } & \\ { \displaystyle \alpha _ { k , m } ^ { 2 } [ n ] \leq \Phi _ { k } ^ { \mathrm { l o w } } ( \boldsymbol { u } _ { m } [ n ] ) , \forall m \in \mathcal { M } } & \\ { ( 3 5 ) , \displaystyle ( 5 0 ) . } & { ( 5 ! } \end{array}\tag{3}
$$

The above problem is convex and thus can be solved by the CVX tool. Accordingly, an optimized solution to problem (P2.3) is obtained.

## B. GD Clustering

Next, we consider another intuitive design based on GD clustering, which groups different GDs into a number of clusters, and allows different UAVs to design their trajectories in a distributed manner, each covering one cluster. In particular, we separate K GDs into M clusters each served by one UAV. Suppose that the set of GDs in cluster $m \in \mathcal { M }$ is denoted by $\kappa _ { m }$ and the number of GDs in each cluster m is denoted by $K _ { m } = | { \cal K } _ { m } |$ , where $\cup _ { m \in \mathcal { M } } \mathcal { K } _ { m } = \mathcal { K }$ and $\textstyle \sum _ { m \in { \mathcal { M } } } K _ { m } = K$ . Accordingly, the whole area is divided into M non-overlapping sub-areas, and each UAV is dispatched to serve the GDs within one corresponding sub-area. Furthermore, different from the UAV swarming design with cooperative transmit energy beamforming used, we consider that different UAVs send independent signals with the transmit covariance matrices being $\pmb { S } ( t ) = \mathrm { d i a g } ( P , \ldots , P )$ . For notational convenience, let $\mathbf { \sigma } _ { c _ { k , m } } = ( x _ { k , m } , y _ { k , m } ) , k \in \mathcal { K } _ { m } , m \in$ M denote the horizontal location of GD k in cluster m, and denote the distance between UAV m and GD k in cluster m as $d _ { k , m } ( { \pmb u } _ { m } ( t ) ) = \sqrt { \| { \pmb u } _ { m } ( t ) - { \pmb c } _ { k , m } \| ^ { 2 } + H ^ { 2 } }$ . In this case, the total harvested energy by GD $k \in \mathcal { K } _ { m }$ in cluster $m \in \mathcal { M }$ is given by

$$
E _ { k , m } ^ { \mathrm { c l u } } ( \{ { \pmb u } _ { m } ( t ) \} ) = \int _ { 0 } ^ { T } \sum _ { i \in \mathcal { M } } \frac { \eta P \beta _ { 0 } } { \left\| { \pmb u } _ { i } ( t ) - { \pmb c } _ { k , m } \right\| ^ { 2 } + H ^ { 2 } } \mathrm { d } t .\tag{54}
$$

Hence, the utility maximization problem (P2) is reduced as

$$
\begin{array} { r l } { ( \mathrm { P 2 . 4 } ) \colon \displaystyle \operatorname* { m a x } _ { \{ \pmb { u _ { m } } ( t ) \} } \displaystyle \operatorname* { m i n } _ { k \in { \cal K _ { m } } , m \in \mathcal { M } } \Bigl \{ { E _ { k , m } ^ { \mathrm { c l u } } ( \{ \pmb { u _ { m } ( t ) } \} ) } \Bigr \} } & { } \\ { \mathrm { s . t . ~ } \| \dot { \pmb { u _ { m } } } ( t ) \| \le V _ { \mathrm { m a x } } , \forall m \in \mathcal { M } , t \in \mathcal { T } } \\ { \displaystyle } & { ( 3 0 ) . } \end{array}\tag{55}
$$

Notice that as each UAV covers one sub-area, the collision avoidance constraints between different UAVs can be automatically satisfied. Furthermore, we suppose that the distance between UAV m and any non-associated GD $k , k \notin \mathcal { K } _ { m }$ , is generally long, and as a result, we can safely omit the harvested energy from nearby UAVs in (54) and approximate $E _ { k , m } ^ { \mathrm { c l u } } ( \{ \boldsymbol { \mathbf { \em u } } _ { m } ( t ) \} )$ as

$$
E _ { k , m } ^ { \mathrm { c l u } } ( \{ { \pmb u } _ { m } ( t ) \} ) \approx \int _ { 0 } ^ { T } \frac { \eta P \beta _ { 0 } } { \left\| { \pmb u } _ { m } ( t ) - { \pmb c } _ { k , m } \right\| ^ { 2 } + H ^ { 2 } } \mathrm { d } t .\tag{56}
$$

As a result, the multi-UAV trajectory design problem (P2.4) can be decomposed into M single-UAV trajectory design problems as follows, which can thus be solved by the trajectory design framework in Section II-C.

$$
\begin{array} { r l r } {  { \operatorname* { m a x } _ { \{ \pmb { u } _ { m } ( t ) \} } \operatorname* { m i n } _ { k \in { \mathcal { K } _ { m } } } \int _ { 0 } ^ { T } \frac { \eta P \beta _ { 0 } } { \| \pmb { u } _ { m } ( t ) - \pmb { c } _ { k , m } \| ^ { 2 } + H ^ { 2 } } \mathrm { d } t } } \\ & { } & { \mathrm { s . t . ~ } \ \| \dot { \pmb { u } } _ { m } ( t ) \| \le V _ { \operatorname* { m a x } } , \forall t \in { \mathcal { T } } , } \end{array}\tag{57}
$$

$m \in \mathcal { M }$ . It is worth noting that how to optimally group these GDs is still an open problem that is difficult to solve. Intuitively, we can assign nearby GDs into one cluster via clustering methods such as K-Means clustering. In this paper, we simply divide the whole area are into M sub-areas in a uniform manner, as will be illustrated next.

## C. Numerical Results

In this subsection, we present numerical results to evaluate the performance of the proposed UAV-swarming and GDclustering schemes as compared to the single-UAV-enabled WPT system with single antenna. In the simulation, we consider that $M = 4 ~ { \mathrm { U A V s } }$ are dispatched to serve $K = 2 0 \mathrm { G D s }$ that are randomly distributed within a 2D area of $2 0 \times 2 0 ~ \mathrm { m } ^ { 2 }$ as shown in Figs. 9 and 10. The system parameters are same as those for Fig. 4. In particular, for GD clustering, we simply separate the 2D area into four equal-size square sub-areas as shown in Fig. 10.

![](images/7d3b0dd23929a6ccd22e8796666a074805b9a4e0f66ade3c6a17db11e78e6c22.jpg)  
Fig. 10. Optimized UAV trajectories of multi-UAV-enabled WPT under the GD clustering design.

![](images/f6560c339a7b2278752ba8f3262d2188f61897a6c6aa29a7eb274fd39a384764.jpg)  
Fig. 11. The minimum average harvested power among all GDs versus mission duration T under different UAV cooperation schemes.

Figs. 9 and 10 show the optimized UAVs’ trajectories via time quantization under UAV swarming and GD-clustering designs, respectively. For UAV swarming, it is observed in Fig. 9 that the UAV swarm flies close to each GD sequentially to maximize the energy beamforming gain for that GD (under TDMA beamforming). For GD clustering, it is observed in Fig. 10 that the UAV in each sub-area flies following a similar trajectory as that in Fig. 6.

Fig. 11 shows the minimum average harvested power among all GDs versus the UAV charging duration T. It is observed that the multi-UAV-enabled WPT (via both UAV swarming and GD clustering) considerably outperforms the single-UAV counterpart. Specifically, when T is small $( { \mathrm { e . g . , ~ } } t \ < \ 1 0 \ \mathrm { ~ s ) ~ }$ the GD clustering design outperforms the UAV swarming, as the UAV swarm design generally needs longer durations to properly visit all GDs to charge them efficiently. By contrast, when T becomes large $( \mathrm { e } . \mathrm { g } . , \ T > 1 1 \ \mathrm { s } )$ , the UAV swarming surpasses the GD clustering design, due to the exploitation of cooperative transmit energy beamforming.

![](images/a242d7ffeb10726c82f1c4129a5ef8d4ae6eb4de68af47948acdee90e68c0d99.jpg)  
Fig. 12. Illustration of the UAV-enabled WPCN.

## D. Extensions

As an initial attempt, this section presented two efficient trajectory designs for multi-UAV-enabled WPT based on UAV swarming and GD clustering, respectively. There are still various potential extensions and open problems that are worth pursuing in future work, which are briefly discussed in the following.

• For UAV swarming, we considered simplified TDMA beamforming design and assumed fixed UAV formations over time. Generally speaking, using more advanced cooperative transmit energy beamforming and enabling more adaptive UAV formation are expected to achieve better energy transfer performance. For instance, when the GDs are randomly distributed over space, sending multiple energy beams at each time instant may further enhance the energy transmission efficiency.

• For GD clustering, we optimized the trajectory of each UAV independently by omitting the transferred energy from nearby UAVs. In practice, we can jointly optimize the multiple UAVs’ trajectories by directly solving problem (P2.4). Besides, how to properly cluster these GDs will be crucial for performance optimization, which is still an open problem.

• Furthermore, motivated by the performance comparison in Fig. 11, the ideas of UAV swarming and GD clustering can be combined to further enhance the efficiency of multi-UAV-enabled WPT. For instance, we can group GDs into several clusters each served by a sub-group of UAVs, where for each cluster UAV-swarming-based cooperative energy beamforming design can be adopted. In this case, we need to decide the number of clusters and the number of UAVs in each cluster, based on which we also need to cluster GDs and jointly design the UAVs’ trajectories and energy transmission strategies. These problems are all challenging to solve, for which the performance-complexity tradeoff should be considered properly.

## IV. UAV-ENABLED WPCN

Building upon the UAV-enabled WPT in the preceding two sections, this section considers the UAV-enabled WPCN, in which UAVs are dispatched as aerial hybrid APs to not only wirelessly charge GDs but also collect information from them. By exploiting the UAVs’ mobility via trajectory design, the

UAV-enabled WPCN is able to resolve the doubly near-far issue faced in the conventional WPCN with APs fixed on the ground. Nevertheless, due to the involvement of both downlink WPT and uplink wireless information transmission (WIT) as well as the newly introduced energy harvesting constraints at GDs, it is a critical task in UAV-enabled WPCN to optimize the UAV trajectory design jointly with the communication resource allocations. To gain essential insights on such joint optimization, in the following, we focus on the single-UAVenabled WPCN system over a finite mission period ${ \mathcal { T } } = ( 0 , T ]$ in which a single UAV flies in the sky to wirelessly charge a set of distributed GDs, and each GD uses the harvested energy to send information back to the UAV.

## A. Transmission Protocol

For the UAV-enabled WPCN, we need to properly design the transmission protocol to share the limited time-frequency resources for both multiuser WIT in the uplink and WPT in the downlink. In such transmission protocol, frequency division duplex (FDD) and time division duplex (TDD) are two duplexing schemes that are widely adopted, in which the downlink WPT and uplink WIT are implemented over orthogonal frequency and time resources, respectively.<sup>6</sup> Furthermore, to support multiuser WIT in the uplink, TDMA, FDMA, OFDMA, and even NOMA [88] can be implemented as the uplink multiple access schemes. Generally speaking, under different duplexing and uplink multiple access schemes, the UAV trajectory design and resource allocations can be different.

In particular, this section considers the transmission protocol with TDD and TDMA as in [74], in which the downlink WPT and uplink multiuser WIT are implemented over different time instants but in the same frequency bands. Notice that the consideration with TDD and TDMA is particularly appealing for UAV-enabled WPCN, as the UAV can properly adjust its locations over time for efficient WIT and WPT, respectively. Also notice that the presented designs in this section are extendible to other cases when different multiple access and/or duplexing schemes are employed.

Under TDD and TDMA, we define

$$
\tau _ { E } ( t ) \in \{ 0 , 1 \} , \tau _ { k } ( t ) \in \{ 0 , 1 \} , \forall k \in \mathcal { K } ,\tag{58}
$$

as indicators to denote the transmission mode of the UAVenabled WPCN at time instant $t \in \tau .$ Here, $\tau _ { E } ( t ) ~ = ~ 1$ means the downlink WPT mode, in which the UAV broadcasts wireless energy to the GDs at time t. Similarly, $\tau _ { k } ( t ) = 1$ corresponds to the uplink WIT mode with GD k, in which GD k sends information to the UAV at time t. As the downlink WPT and uplink WIT with different GDs cannot be implemented at the same time, we have

$$
\tau _ { E } ( t ) + \sum _ { k \in \mathcal { K } } \tau _ { k } ( t ) \leq 1 , \forall t \in \mathcal { T } .\tag{59}
$$

<sup>6</sup>In-band full duplex (see, e.g., [58], [87]) can also be implemented, in which the UAV’s uplink information reception may suffer from strong selfinterference from its downlink energy transmission. In this case, effective self-interference cancellation becomes essential.

First, we consider the downlink WPT mode with $\tau _ { E } ( t ) = 1$ and $\tau _ { k } ( t ) = 0 , \forall k \in \mathcal { K } .$ . The UAV adopts constant transmit power P. Similarly as in (6) for single-UAV-enabled WPT, the harvested power by each GD $k \in \mathcal { K }$ at time $t \in \tau$ is

$$
\bar { E } _ { k } ( { \pmb u } ( t ) , \tau _ { E } ( t ) ) = \tau _ { E } ( t ) \eta P h _ { k } ( { \pmb u } ( t ) ) .\tag{60}
$$

Accordingly, the total harvested energy by GD k over the entire period T is given by

$$
\bar { E } _ { k } ^ { \mathrm { t o t } } ( \{ { \boldsymbol u } ( t ) , \tau _ { E } ( t ) \} ) = \int _ { 0 } ^ { T } \tau _ { E } ( t ) \eta P h _ { k } ( { \boldsymbol u } ( t ) ) \mathrm d t .\tag{61}
$$

Next, we consider the WIT mode with GD k, where $\tau _ { k } ( t ) =$ 1, and $\tau _ { E } ( t ) = 0 , \tau _ { j } ( t ) = 0 , \forall j \in \mathcal { K } , j \neq k$ . Supposing that the transmit power at GD k is $Q _ { k } ( t )$ that can be adaptively adjusted over time, then the achievable data rate of $\mathrm { G D ~ } k \in \mathcal { K }$ at time $t \in \mathcal T$ is

$$
r _ { k } ( { \pmb u } ( t ) , Q _ { k } ( t ) , \tau _ { k } ( t ) ) = \tau _ { k } ( t ) \log _ { 2 } \biggr ( 1 + \frac { Q _ { k } ( t ) h _ { k } ( { \pmb u } ( t ) ) } { \sigma ^ { 2 } } \biggr ) ,\tag{62}
$$

where $\sigma ^ { 2 }$ is the noise power at the information receiver of the UAV. Accordingly, the average data-rate throughput of GD k over the entire period T is given by

$$
\begin{array} { l } { \displaystyle R _ { k } ( \{ { \pmb u } ( t ) , Q _ { k } ( t ) , \tau _ { k } ( t ) \} ) } \\ { \displaystyle = \frac { 1 } { T } \int _ { 0 } ^ { T } \tau _ { k } ( t ) \log _ { 2 } \biggl ( 1 + \frac { Q _ { k } ( t ) h _ { k } ( { \pmb u } ( t ) ) } { \sigma ^ { 2 } } \biggr ) \mathrm { d } t . } \end{array}\tag{63}
$$

## B. Generic Rate Maximization Problem Formulation

In UAV-enabled WPCN, our objective is to maximize the communication performance of uplink WIT while ensuring the sustainable operation of GDs. In this case, new energy harvesting constraints are imposed at GDs. Suppose that $\bar { E } _ { k } ^ { \mathrm { i n i t i a l } } \geq 0$ denotes the initial energy stored at GD k. Then we have the following energy harvesting constraints for GDs to avoid the energy outage [2]:

$$
\begin{array} { r l r } & { } & { \displaystyle { \int _ { 0 } ^ { t } \tau _ { k } ( \tilde { t } ) Q _ { k } ( \tilde { t } ) \mathrm { d } \tilde { t } } \leq \int _ { 0 } ^ { t } \tau _ { E } ( \tilde { t } ) \eta P h _ { k } ( { \boldsymbol { \mathbf { \mathit { u } } } ( \tilde { t } ) } ) \mathrm { d } \tilde { t } } \\ & { } & { \quad \quad +  E _ { k } ^ { \mathrm { i n i t i a l } } , \forall k \in \mathcal { K } , t \in \mathcal { T } , } \end{array}\tag{64}
$$

such that the accumulative energy consumed by each GD until any time $t \in \tau$ does not exceed the initial energy plus the energy accumulatively harvested from the UAV by that time. Notice that if $E _ { k } ^ { \mathrm { i n i t i a l } }$ is sufficiently large (or equivalently, each GD has a sufficiently large energy storage), the energy harvesting constraints in (64) can also be replaced by

$$
\int _ { 0 } ^ { T } \tau _ { k } ( t ) Q _ { k } ( t ) \mathrm { d } t \leq \int _ { 0 } ^ { T } \tau _ { E } ( t ) \eta P h _ { k } ( \boldsymbol { u } ( t ) ) \mathrm { d } t , \forall k \in \mathcal { K } ,\tag{65}
$$

such that we only need to ensure that the total energy consumption over the entire period T at each GD does not exceed the totally harvested energy at that GD, for its sustainable operation.

In order to balance the communication rates at different GDs in a fair manner, we define the utility function for UAV-enabled WPCN as the minimum weighted uplink date-rate throughput, i.e.,

$$
\begin{array} { r l } & { \bar { U } ( \{ \boldsymbol { \mathsf { \pmb { u } } ( t ) } , Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) \} ) } \\ & { \quad = \operatorname* { m i n } \biggl \{ \frac { R _ { 1 } \bigl ( \{ \boldsymbol { \mathsf { u } } ( t ) , Q _ { k } ( t ) , \tau _ { 1 } ( t ) \} \bigr ) } { \bar { a } _ { 1 } } , \frac { R _ { 2 } \bigl ( \{ \boldsymbol { \mathsf { u } } ( t ) , Q _ { k } ( t ) , \tau _ { 2 } ( t ) \} \bigr ) } { \bar { a } _ { 2 } } , } \\ & { \qquad \quad \ldots , \frac { R _ { K } \bigl ( \{ \boldsymbol { \mathsf { u } } ( t ) , Q _ { k } ( t ) , \tau _ { K } ( t ) \} \bigr ) } { \bar { a } _ { K } } \biggr \} , } \end{array}\tag{66}
$$

where $\bar { a } _ { k }$ denotes the rate weight for each GD k. Accordingly, we formulate the generic uplink average data-rate throughput maximization problem as problem (P3) in the following, in which both the UAV trajectory {u(t)} and the resource allocation $\{ Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) \}$ need to be jointly optimized.

$$
( \mathrm { P 3 } ) \colon \operatorname* { m a x } _ { \{ \substack { u ( t ) , Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) } \} } \bar { U } ( \{ \mathbf  \} u ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) , Q _ { k } ( t ) \} )
$$

$$
\mathbf { s . t . } ~ f _ { i } ( \{ \mathbf { \em u ( } t ) \} ) \geq 0 , \forall i \in \{ 1 , \dots , I \}\tag{67}
$$

$$
\int _ { 0 } ^ { T } \tau _ { k } ( t ) Q _ { k } ( t ) \mathrm { d } t \leq \int _ { 0 } ^ { T } \tau _ { E } ( t ) \eta P h _ { k } ( \boldsymbol { u } ( t ) ) \mathrm { d } t , \forall k \in \mathcal { K }
$$

(58), (59).

(68)

Note that compared with problem (P1) with trajectory design only, problem (P3) involves new variables $\{ Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) \}$ for resource allocation and new energy harvesting constraints in (68). Furthermore, the UAV trajectory {u(t)} and the resource allocation $\{ Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) \}$ are coupled at both the rate and energy functions in the objective as well as constraints. Therefore, problem (P3) is more challenging to be optimally solved than problem (P1).

## C. Joint UAV Trajectory and Resource Allocation Design Framework

In this subsection, we extend the trajectory design framework in Section II-C to obtain efficient solutions to problem (P3) [74]. For illustration, we only consider the UAV’s flight speed constraints in (10), i.e., we consider (P3) by replacing constraint (67) by (10) [74].

1) Multi-Location-Hovering Design: By considering the case with sufficiently long time duration, we relax problem (P3) as follows by omitting the UAV’s flight constraints.

$$
\begin{array} { r l r } {  { ( \mathrm { P 3 . 1 } ) \colon \mathrm { ~ } } } & { \operatorname* { m a x } } \\ & { } & { \{ u ( t ) , Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) \} , R } \\ & { } & { \mathrm { s . t . ~ } R _ { k } \big ( \{ u ( t ) , Q _ { k } ( t ) , \tau _ { k } ( t ) \} \big ) / \bar { a } _ { k } \geq R , \forall k \in \mathcal K } \\ & { } & { ( 5 8 ) , ~ ( 5 9 ) , ~ ( 6 8 ) , } \end{array}\tag{69}
$$

where R is an auxiliary variable. Similarly as for problem (P1.2), strong duality holds between the non-convex problem (P3.1) and its dual problem. Therefore, (P3.1) can be optimally solved by using the Lagrange duality method. Let $\lambda _ { k } \ \geq \ 0$ and $\mu _ { k } \geq 0 , k \in \mathcal { K } ,$ , denote the dual variables associated to the k-th constraints in (69) and (68), respectively. The partial Lagrangian is given as

$$
\begin{array} { r l } & { \mathcal { L } _ { 3 } ( \{ \boldsymbol u ( t ) , \boldsymbol Q _ { k } ( t ) , \tau _ { E } ( t ) , \tau _ { k } ( t ) , \lambda _ { k } , \mu _ { k } \} , R ) } \\ & { \quad = \displaystyle \left( 1 - \sum _ { k \in { \cal K } } \lambda _ { k } \right) R + \sum _ { k \in { \cal K } } \lambda _ { k } R _ { k } ( \{ \boldsymbol u ( t ) , Q _ { k } ( t ) , \tau _ { k } ( t ) \} ) / \bar { a } _ { k } } \\ & { \quad + \sum _ { k \in { \cal K } } \mu _ { k } \left( \bar { E } _ { k } ^ { \mathrm { t o t } } ( \{ \boldsymbol u ( t ) , \tau _ { E } ( t ) \} ) - \int _ { 0 } ^ { T } \tau _ { k } ( t ) Q _ { k } ( t ) \mathrm { d } t \right) . } \end{array}\tag{70}
$$

The dual function is

$$
\begin{array} { r l r } {  { g _ { 3 } \big ( \{ \lambda _ { k } , \mu _ { k } \} \big ) } } \\ & { = } & { \operatorname* { m a x } } \\ & { =  \{ \begin{array} { l } { \operatorname* { m a x } } \\ { \boldsymbol { u } ( t ) , \boldsymbol { q } _ { k } ( t ) , } \end{array} \} , R } \\ & { } & { \{ \begin{array} { l } { \boldsymbol { \mathfrak { x } } _ { k } ( t ) , \boldsymbol { \tau } _ { k } ( t ) } \\ { \boldsymbol { \tau } _ { k } ( t ) , \boldsymbol { \tau } _ { k } ( t ) } \end{array} \} , R } \\ & { } & { \mathrm { s . t . } \ ( 5 8 ) , \ ( 5 9 ) . } \end{array}
$$

Accordingly, the optimal solution to (P3.1) can be obtained by solving the following dual problem.

$$
\begin{array} { r l r } { ( \mathrm { D 3 . 1 } ) \colon } & { { \displaystyle \operatorname* { m i n } _ { \{ \lambda _ { k } \geq 0 \} , \atop { \{ \mu _ { k } \geq 0 \} } } } } & { g _ { 3 } \big ( \{ \lambda _ { k } , \mu _ { k } \} \big ) } & \\ & { {  } } & { \mathrm { ~ } } \\ & { { \hphantom { \{ \displaystyle \operatorname* { m i n } _ { \{ \lambda _ { k } \geq 0 \} } } } \mathrm { s . t . ~ } }  & { \displaystyle \sum _ { k \in \mathcal { K } } \lambda _ { k } = 1 . } \end{array}\tag{72}
$$

For given feasible $\{ \lambda _ { k } , \mu _ { k } \}$ , the dual function $g _ { 3 } ( \left\{ \lambda _ { k } , \mu _ { k } \right\} )$ can be obtained by solving problem (71). It can be shown that problem (71) can be decomposed into infinite number of sub-problems for different time t. By dropping the time index t, solving problem (71) is equivalent to solving the following sub-problems for any time t.

$$
\begin{array} { r l r } { \displaystyle \operatorname* { m a x } _ { \{ Q _ { k } , \tau _ { k } \} , u , \tau _ { E } } } & { \displaystyle \sum _ { k \in { \mathcal K } } \left( \tau _ { k } \left( \frac { \lambda _ { k } } { a _ { k } } \log _ { 2 } \left( 1 + \frac { Q _ { k } \beta _ { 0 } / \sigma ^ { 2 } } { \| u - c _ { k } \| ^ { 2 } + H ^ { 2 } } \right) \right. \right. } & \\ { \displaystyle \left. \left. - \sum _ { k \in { \mathcal K } } \mu _ { k } Q _ { k } \right) + \frac { \tau _ { E } \mu _ { k } \eta P \beta _ { 0 } / \sigma ^ { 2 } } { \| u - c _ { k } \| ^ { 2 } + H ^ { 2 } } \right) } & \\ { \displaystyle \mathrm { s . t . } ~ \tau _ { E } \in \{ 0 , 1 \} , \tau _ { k } \in \{ 0 , 1 \} , \forall k \in { \mathcal K } } & \\ { \displaystyle \sum _ { k \in { \mathcal K } } \tau _ { k } + \tau _ { E } = 1 . } & { ( 7 3 ) } \end{array}
$$

There are $K + 1$ feasible choices for $\tau _ { E }$ and $\{ \tau _ { k } \}$ , due to the constraints in (73). Thus, we exhaustively search over the K + 1 choices to find the optimal solution to (73). First, when GD k transmits information to the UAV with $\tau _ { k } = 1 , \tau _ { E } =$ $0 , \tau _ { j } = 0 , \forall j \in \mathcal { K } , j \neq k .$ , we have $\pmb { u } _ { k } ^ { * } = \pmb { c } _ { k } \ ( \mathrm { i . e . } .$ , the UAV hovers exactly above GD k), $Q _ { \bar { k } } ^ { * } = 0 , \breve { \forall k } \in \mathcal { K } , \bar { k } \neq k .$ , and $Q _ { k } ^ { * }$ can be obtained by checking the first-order derivative of the resultant objective function. Second, when the system operates in downlink WPT mode with $\tau _ { E } = 1 , \tau _ { k } = 0 , \forall k \in \mathcal { K }$ we have $Q _ { k } ^ { * } = 0 , \forall k \in { \mathcal { K } } .$ and the UAV’s optimal hovering locations can be obtained by using a 2D exhaustive search similarly to that for single-UAV-enabled WPT, which is generally non-unique. By comparing these K + 1 optimal values, problem (71) is solved.

Next, after optimally solving the dual problem (D3.1) via subgradient-based methods, we can accordingly obtain a set of optimal hovering locations and the corresponding communication resource allocation. By properly time-sharing these hovering locations, we can construct the optimal multilocation-hovering solution to (P3.1). It is shown in [74] that the UAV should hover above two different sets of locations, one set among different GDs for downlink WPT (with $Q _ { k } ^ { * } = 0 , \forall k \in \mathcal { K } )$ and the other set exactly above each GD k for uplink WIT (with $Q _ { k } > 0$ and $Q _ { \bar { k } } ^ { * } = 0 , \forall \bar { k } \in \mathcal { K } , \bar { k } \neq k )$ Note that the performance achieved by such multi-locationhovering solution serves as a performance upper bound for the optimal value of problem (P3) with the UAV’s flight speed constraints in (10).

2) SHF Trajectory Design: With UAV’s flight constraints considered, we can construct the SHF trajectory based on TSP, in which the UAV sequentially visits the two sets of hovering locations at the maximum flight speed $V _ { \mathrm { m a x } }$ with a shortest traveling path. Under this flight path, we still need to optimize the hovering duration at each location and resource allocations over time. Towards this end, we quantize the charging period into a finite number of equal-duration slots, and further divide each slot into $K + 1$ sub-slots with variable durations for each GD’s uplink WIT and the downlink WPT, respectively. In this case, the optimization of hovering durations and resource allocation can be formulated as a convex optimization problem, which can be solved via CVX [74].

3) Time Quantization Based Optimization: Furthermore, problem (P3) with continuous-time variables can be transformed into an equivalent problem with discrete-time variables via time quantization. Specifically, the whole mission period T is quantized into a set, $\mathcal { N } \triangleq \{ 1 , \dots , N \}$ , of time slots, each with equal duration $\delta = T / N$ . Particularly, suppose that the $K + 1$ transmission modes time share within each slots, such that we define $\tau _ { E } [ n ]$ and $\tau _ { k } [ n ] , k \in \mathcal { K }$ as the time-sharing duration of downlink WPT and that of uplink WIT of GD k at time slot $n \in \mathcal N ,$ respectively. We thus have

$$
\sum _ { k \in \mathcal { K } } \tau _ { k } [ n ] + \tau _ { E } [ n ] = \delta , \forall n \in \mathcal { N } .\tag{74}
$$

Let $Q _ { k } [ n ]$ denote GD $k \mathrm { { s } }$ transmit power and ${ \pmb u } [ n ]$ denote the UAV’s location at time slot $n \in { \mathcal { N } } .$ As a result, problem (P3) with continuous-time variables can be reformulated as the following problem.

$$
\begin{array}{c} \begin{array} { r l r } { \left. { ( \mathrm { P 3 . 2 } ) \colon \operatorname* { m a x } _ { \begin{array} { c } { u \in [ n ] , q [ n ] } \\ { \tau _ { E } [ n ] , \tau _ { k } [ n ] } \end{array} } \quad \operatorname* { m i n } \left\{ \frac { 1 } { T \tilde { a } _ { k } } \sum _ { n \in \mathcal { N } } \tau _ { k } [ n ] \right. } \\ & { } & { \times \quad \log _ { 2 } \left( 1 + \frac { Q _ { k } [ n ] / \sigma ^ { 2 } } { \left\| u [ n ] - c _ { k } \right\| ^ { 2 } + H ^ { 2 } } \right) } } } \\ & \right\{ } & { \mathrm { s . t . } \quad \sum _ { n \in \mathcal { N } } \tau _ { k } [ n ] Q _ { k } [ n ] \le \sum _ { n \in \mathcal { N } } \frac { \tau _ { E } [ n ] \eta P } { \left\| u [ n ] - c _ { k } \right\| ^ { 2 } + H ^ { 2 } } , \forall k \in \mathcal { K } } \\ & { } & { ( 2 3 ) , ~ ( 7 4 ) . } \end{array}  \end{array}
$$

Although (P3.2) is still challenging to be solved, we can optimize the UAV’s trajectory and resource allocations in an alternating manner together with SCA techniques towards a locally optimal solution [74], in which the SHF trajectory design can be utilized as the initial point for iteration.

## D. Numerical Results

In this subsection, we present numerical results to validate the efficiency of the above approaches as compared to the benchmarking static hovering scheme, in which the UAV hovers at one (optimized) location over the whole mission period.

We consider a UAV-enabled WPCN with K = 10 GDs, in which the simulation parameters are the same as those in UAV-enabled WPT in Section II-D. Fig. 13 shows the optimal hovering locations, the trajectory obtained by timequantization-based approach, and the static hovering location. It is observed that there are 3 optimal hovering locations for

![](images/e73e9e8ed79a54305e507129d2231faa4570fedc10141761d9f2b9bb1ab0b9c4.jpg)  
Fig. 13. Simulation system setup for UAV-enabled WPCN.

![](images/094ac16a21a3948de3cdef01b5cbaf3df57201a304fea7334c72fecfc49e451e.jpg)  
Fig. 14. The uplink minimum data-rate throughput versus the UAV mission duration T.

WPT, and 10 hovering locations each exactly above one GD for WIT.

Fig. 14 shows the uplink minimum data-rate throughput among all GDs versus the UAV mission duration T. It is observed that the time-quantization-based design significantly outperforms the static hovering scheme and the performance gain becomes more evident when T increases. Furthermore, when T is sufficiently large, the time-quantization-based design approaches the performance upper bound achieved by the multi-location hovering without UAV’s flight speed constraints.

## E. Extensions

So far, this section presented joint UAV trajectory design and communication resource allocation for the single-UAVenabled WPCN with one single UAV serving in the dual role of ET and AP. In the literature, there have also been works that extended the design framework to other setups [56]–[58], [89]–[97], as briefly discussed in the following.

1) Dual-UAV-Enabled WPCN With Separated ET and AP: Instead of using one single UAV as co-located ET and AP, we can alternatively dispatch two different UAVs as separated ET and AP for WPT and WIT, respectively [97]. The dual-UAV-enabled WPCN is expected to provide more degrees of freedom in optimizing the UAVs’ trajectories to enhance the system performance. For instance, under the TDD/TDMA protocol, the UAV-ET can follow the flight trajectory in Section II to fairly charge the distributed GDs, and the UAV-AP can follow a different trajectory to sequentially hover above different GDs to maximally collect the information, provided that the collision avoidance issue is properly addressed. Besides, the dual-UAV-enabled WPCN also provides opportunities to enabled in-band full duplex operation between WIT and WPT, as the two UAVs can stay further away from each other during the flight to reduce the interference from the WPT of UAV-ET to the information reception at UAV-AP.

2) UAV-Enabled Wireless Powered Backscatter Communications: Wireless powered backscatter communications have recently attracted a lot of attention as a new type of WPCN [98]. Instead of using active RF chains to send information, the backscatter devices can reflect the carrier signals from the ET with properly adjusted phase and/or amplitude to convey information. In UAV-enabled wireless powered backscatter communications, the UAV can be dispatched as both ET and RF readers to not only wirelessly charge these GDs but also collect the reflected signals for information decoding at the same time. Due to the interference caused by WPT, the UAV’s trajectory should be designed by considering the performance tradeoff between harvested energy and backscatter communication rate [99]–[106].

3) Multi-UAV-Enabled WPCN: Similarly as in multi-UAVenabled WPT, when the network size becomes large, it becomes necessary to use multiple UAVs to implement the WPCN, in which multiple UAVs need to cooperate in the joint trajectories design, as well as the energy transmission and information reception. For instance, if the UAV swarming (see Section III-A) is adopted, UAVs can cooperatively design their transmit energy covariance matrices for downlink WPT, and also use joint signal detection (via CoMP reception) for uplink WIT. On the other hand, with GD clustering, UAVs can each cover a dedicated non-overlapping sub-area for serving the GDs therein, while interference coordination needs to be considered to mitigate the co-channel interference among different clusters in WIT. Under these different designs, the UAVs’ trajectories need to be properly designed jointly with the corresponding resource allocation methods. In the literature, there is one prior work [73] that investigated the joint UAV trajectory design and communication resource allocation in a simplified case with two UAVs serving two GDs, where the two UAVs can cooperate in two different modes with CoMP and interference coordination, respectively. It is found in [73] that in the CoMP mode, the two UAVs prefer to stay between the two GDs to enhance the cooperative beamforming gain, while in the interference coordination mode, the two UAVs would keep far away from each other to alleviate the co-channel interference in uplink WIT. How to extend the UAV-enabled WPCN to scenarios with more UAVs and more GDs under different cooperation strategies is an open problem that has not been addressed yet.

![](images/0724d32dc1d6f2f547e9306b14969dffc2386ed3a3b547d10d6eb1943c6be351.jpg)  
Fig. 15. Illustration of the UAV-enabled wireless powered MEC.

## V. UAV-ENABLED WIRELESS POWERED MEC

Besides UAV-enabled WPCN, UAV-enabled wireless powered MEC is another recent application of UAV-enabled WPT, in which UAVs are dispatched as aerial MEC servers that can provide both wireless energy supply and cloud-like computing for low-power GDs. In the single-UAV-enabled wireless powered MEC as shown in Fig. 15, the UAV broadcasts wireless signals to charge GDs, and the GDs use the harvested energy to accomplish their respective computation tasks via local and/or remote execution. Generally speaking, the UAV-enabled wireless powered MEC is more complicated than the UAV-enabled WPT/WPCN, as it involves WPT, WIT (for computation task offloading/downloading), and computation in a unified design. In this case, how to design the UAV trajectory jointly with resource allocations for energy transmission, communication, and computation is a critical but challenging task. In the literature, although there have been several initial works [62]–[66] that investigated the UAV-enabled wireless powered MEC, the research on this topic is still in its infancy stage.

In this section, we consider the single-UAV-enabled wireless powered MEC over a particular mission period ${ \mathcal { T } } = \ ( 0 , T ]$ and present a generic utility maximization problem under new computation causality constraints and energy harvesting constraints. Next, we discuss their solutions. In order to gain insights to motivate future research, we focus on the case when the computation tasks are completely partitionable, such that the computation tasks can be partitioned into independent parts that can be executed locally (at the GD) or remotely (at the UAV) at the same time.

## A. Operation Protocol

The UAV-enabled wireless powered MEC generally consists of three wireless links, including the downlink WPT from the UAV to the GDs, the uplink task offloading from the GDs to the UAV, and the downlink result downloading from the UAV to the GDs. Besides, the GDs and the UAV should implement the local and remote execution, respectively, which are causally constrained by the task offloading and result downloading. In this case, how to design an efficient operation protocol for wireless powering, communication, and computation is a complicated task.

For illustration, we consider the TDD/TDMA protocol similarly as for the UAV-enabled WPCN, in which the wireless links for downlink WPT, uplink task offloading, and downlink result downloading are implemented over the same frequency band but orthogonal time instants. At time instant $t \in \tau ,$ let $\tau _ { E } ( t ) ~ \in ~ \{ 0 , 1 \} , ~ \tau _ { k } ^ { \mathrm { o } } ( t ) ~ \in ~ \{ 0 , 1 \}$ , and $\tau _ { k } ^ { \mathrm { d } } ( t ) \ \in \ \{ 0 , 1 \}$ denote the operation mode indicators. Here, $\tau _ { E } ( t ) = 1$ indicates the downlink WPT mode, $\tau _ { k } ^ { \mathrm { o } } ( t ) = 1$ means that GD k offloads the computation tasks to the UAV, and $\tau _ { k } ^ { \mathrm { d } } ( t ) = 1$ represents that GD k downloads the computation results from the UAV. Due to the TDD/TDMA consideration, we have $\begin{array} { r } { \tau _ { E } ( t ) + \sum _ { k \in \mathcal { K } } \tau _ { k } ^ { \mathrm { o } } ( t ) + \sum _ { k \in \mathcal { K } } \tau _ { k } ^ { \mathrm { d } } ( t ) \leq 1 , \forall t \in T } \end{array}$

First, we consider the downlink WPT. As the WPT is only implemented when $\tau _ { E } ( t ) = 1$ , the total harvested energy at GD k is given as $\bar { E } _ { k } ^ { \mathrm { t o t } } ( \{ { \bf \dot { u } } ( t ) , \tau _ { E } ( t ) \} )$ in (61), similarly as the UAV-enabled WPCN in Section IV.

Then, we consider the task offloading form GDs to the UAV. Supposing that $Q _ { k } ( t )$ denotes the transmit power at GD k, the number of task-input bits offloaded from GD k to the UAV at time t (in bits-per-second) is $\ell _ { k } ^ { \mathrm { o f f } } ( \tau _ { k } ^ { \mathrm { o } } ( t ) , Q _ { k } ( t ) , { \mathbf { \em u } } ( t ) ) \ =$ $\begin{array} { r } { \tau _ { k } ^ { \mathrm { o } } ( t ) \log _ { 2 } ( 1 + \frac { Q _ { k } ( t ) h _ { k } ( { \boldsymbol u } ( t ) ) } { \sigma ^ { 2 } } ) } \end{array}$

Next, after receiving the offloaded tasks from GDs, the UAV needs to execute the tasks using its computation resource and then sends the computation results back to GD k. In order to accomplish the offloaded tasks, the UAV must have enough computation capabilities to finish these tasks and send the computation results back to GD k, thus leading to the following two types of computation causality constraints. Let $f _ { 0 } ( t )$ denote the CPU frequency at the UAV at time $t \in \mathcal { T } , c _ { 0 }$ denote the number of CPU cycles for computing one bit at the UAV. Accordingly, the computation capacity (in bits-per-second) at the UAV at each time instant t is $f _ { 0 } ( t ) / c _ { 0 }$ . Furthermore, let $\varphi _ { k } ( t )$ denote the computation rate (in bits-per-second) for GD k at the UAV. We thus have

$$
\sum _ { k \in \mathcal { K } } \varphi _ { k } ( t ) \leq \frac { f _ { 0 } ( t ) } { c _ { 0 } } , \forall t \in \mathcal { T } .\tag{76}
$$

For the remote execution at the UAV, the accumulatively computed bits from for each GD $k \in \mathcal { K }$ by the UAV till any time instant t should not exceed that accumulatively offloaded from that GD by that time. We thus obtain the first type of computation causality constraints as

$$
\begin{array} { r l } {  { \int _ { 0 } ^ { t } \ell _ { k } ^ { \mathrm { o f f } } \big ( \tau _ { k } ^ { \mathrm { o } } \big ( \tilde { t } \big ) , Q _ { k } \big ( \tilde { t } \big ) , { \boldsymbol { u } } \big ( \tilde { t } \big ) \big ) \mathrm { d } \tilde { t } } } \\ & { \geq \displaystyle \int _ { 0 } ^ { t } \varphi _ { k } \big ( \tilde { t } \big ) \mathrm { d } \tilde { t } , \forall k \in \mathcal { K } , \forall t \in \mathcal { T } . } \end{array}\tag{77}
$$

Furthermore, we have the following constraint in order for the offloaded bits to be successfully computed before the deadline of T.

$$
\int _ { 0 } ^ { T } \ell _ { k } ^ { \mathrm { o f f } } \big ( \tau _ { k } ^ { \mathrm { o } } \big ( \tilde { t } \big ) , Q _ { k } \big ( \tilde { t } \big ) , \boldsymbol { u } \big ( \tilde { t } \big ) \big ) \mathrm { d } \tilde { t } = \int _ { 0 } ^ { T } \varphi _ { k } \big ( \tilde { t } \big ) \mathrm { d } \tilde { t } , \ \forall k \in \mathcal { K } .\tag{78}
$$

Besides, after completing the remote task execution, the UAV needs to download the computation results back to GDs. Under transmit power P at the UAV, the number of downloaded bits at time instant t is $\ell _ { k } ^ { \mathrm { d o w n } } ( \tau _ { k } ^ { \mathrm { d } } ( t ) , \boldsymbol { \mathbf { \ell } } \boldsymbol { u } ( t ) ) = \tau _ { k } ^ { \mathrm { d } } ( t ) \log ( 1 +$ $\frac { P h _ { k } ( \pmb { u } ( t ) ) } { \sigma _ { \mathfrak { r } } ^ { 2 } } )$ , where $\sigma _ { k } ^ { 2 }$ denotes the noise power at the receiver <sup>k</sup>of GD k. Notice that the accumulatively downloaded bits should not exceed that accumulatively computed at each time $t \in \tau$ and the downloading must be accomplished before the deadline of T. Therefore, by supposing that the size of computation results (task output bits) is a β portion of task input bits, we further have the second type of computation causality constraints as

$$
\begin{array} { r l } & { \int _ { 0 } ^ { t } \ell _ { k } ^ { \mathrm { d o w n } } \Big ( \tau _ { k } ^ { \mathrm { d } } \big ( \tilde { t } \big ) , Q _ { k } \big ( \tilde { t } \big ) , u \big ( \tilde { t } \big ) \Big ) \mathrm { d } \tilde { t } } \\ & { \quad \le \beta \int _ { 0 } ^ { t } \varphi _ { k } \big ( \tilde { t } \big ) \mathrm { d } \tilde { t } , \ \forall k \in \mathcal { K } , \ \forall t \in \mathcal { T } , } \\ & { \quad \int _ { 0 } ^ { T } \ell _ { k } ^ { \mathrm { d o w n } } \Big ( \tau _ { k } ^ { \mathrm { d } } \big ( \tilde { t } \big ) , Q _ { k } \big ( \tilde { t } \big ) , u \big ( \tilde { t } \big ) \Big ) \mathrm { d } \tilde { t } } \\ & { \quad = \beta \int _ { 0 } ^ { T } \varphi _ { k } \big ( \tilde { t } \big ) \mathrm { d } \tilde { t } , \ \forall k \in \mathcal { K } . } \end{array}\tag{79}
$$

(80)

Finally, we consider the local computing at GDs. Let $f _ { k } ( t )$ denote the CPU frequency (in cycles per second) at time $t \in { \mathcal { T } } ,$ and $c _ { k }$ the number of CPU cycles for computing one bit at GD $k .$ Accordingly, the computation rate at GD k (in bits per second) is $f _ { k } ( t ) / c _ { k }$ , and the corresponding power consumption is $\kappa _ { k } f _ { k } ^ { 3 } ( t )$ [107], where $\kappa _ { k }$ denotes the effective capacitance coefficient depending on the chip architecture. Hence, the total number of computation bits executed at GD k locally is $\begin{array} { r } { L _ { k } ^ { \mathrm { l o c } } ( \{ f _ { k } ( t ) \} ) = \int _ { 0 } ^ { T } \dot { f } _ { k } ( t ) / c _ { k } \mathrm { d } t } \end{array}$

## B. Joint Trajectory and Resource Allocation Design for Computation Utility Maximization

Under the TDD/TDMA protocol, we are interested in maximizing the computation rate or the total number of computed bits at each GD, given by $L _ { k } ^ { \mathrm { o f f } } ( \{ \tau _ { k } ^ { \mathrm { o } } ( t ) , Q _ { k } ( t ) , { \mathbf { u } } ( t ) \} ) \ +$ $L _ { k } ^ { \mathrm { l o c } } ( \{ f _ { k } ( t ) \} )$ where $L _ { k } ^ { \mathrm { o f f } } ( \{ \bar { \tau _ { k } ^ { \mathrm { o } } } ( t ) , { \cal Q } _ { k } ( t ) , { \bf \sf { u } } ( t ) \} ) \mathrm { ~ \qquad = ~ }$ $\begin{array} { r } { \int _ { 0 } ^ { \cdot { \hat { T } } } \ell _ { k } ^ { \mathrm { o f f } } ( \{ \tau _ { k } ^ { \mathrm { o } } ( t ) , Q _ { k } ( t ) , { \boldsymbol { \mathbf { \mathit { u } } } } ( t ) \} ) \mathrm { d } t } \end{array}$ . Accordingly, we define the utility function as

$$
\begin{array} { r l } & { \tilde { U } ( \{ \tau _ { k } ^ { \mathrm { o } } ( t ) , Q _ { k } ( t ) , \boldsymbol { u } ( t ) , f _ { k } ( t ) \} ) } \\ & { \quad = \displaystyle \operatorname* { m i n } _ { k \in \mathcal { K } } \bigg \{ \frac { L _ { k } ^ { \mathrm { o f f } } \big ( \{ \tau _ { k } ^ { \mathrm { o } } ( t ) , Q _ { k } ( t ) , \boldsymbol { u } ( t ) \} \big ) + L _ { k } ^ { \mathrm { l o c } } ( \{ f _ { k } ( t ) \} ) } { \tilde { a } _ { k } } \bigg \} , } \end{array}\tag{81}
$$

where $\tilde { a } _ { k }$ denotes the computing weight for each GD k.

Notice that similarly as in (64) for UAV-enabled WPCN, each GD k is subject to the energy harvesting constraints. By combining the communication energy consumption $Q _ { k } ( t )$ for offloading and computation energy consumption $\kappa _ { k } f _ { k } ^ { 3 } ( t )$ for local task execution, the energy harvesting constraints can be expressed as

$$
\begin{array} { r l } {  { \int _ { 0 } ^ { t } \kappa _ { k } f _ { k } ^ { 3 } \big ( \tilde { t } \big ) \mathrm { d } \tilde { t } + \int _ { 0 } ^ { t } \tau _ { k } \big ( \tilde { t } \big ) Q _ { k } \big ( \tilde { t } \big ) \mathrm { d } \tilde { t } } } \\ & { \le \int _ { 0 } ^ { t } \tau _ { E } \big ( \tilde { t } \big ) \eta P h _ { k } \big ( { \boldsymbol u } \big ( \tilde { t } \big ) \big ) \mathrm { d } \tilde { t } + E _ { k } ^ { \mathrm { i n i t i a l } } , \forall k \in \mathcal { K } , t \in \mathcal { T } , } \end{array}\tag{82}
$$

initial becomes sufficiently large.

$$
\begin{array} { r l r } {  { \int _ { 0 } ^ { T } \kappa _ { k } f _ { k } ^ { 3 } ( t ) \mathrm { d } t + \int _ { 0 } ^ { T } \tau _ { k } ( t ) Q _ { k } ( t ) \mathrm { d } t } } \\ & { } & { \leq \displaystyle \int _ { 0 } ^ { T } \tau _ { E } ( t ) \eta P h _ { k } ( \boldsymbol { u } ( t ) ) \mathrm { d } t , \forall k \in \mathcal { K } , t \in \mathcal { T } . } \end{array}\tag{83}
$$

In this case, we have the utility maximization problem as

$$
\begin{array} { r l } & { ( \mathrm { P 4 } ) \colon \underset { \left\{ \vphantom { \int _ { t _ { 0 } } ^ { t _ { 0 } } \geq 0 , f _ { k } ( t ) \geq 0 , \varphi _ { k } ( t ) \geq 0 } } } { \op\right\eratorname* { m a x } } \ \ \tilde { U } \big ( \big \{ \tau _ { k } ^ { \mathrm { o } } ( t ) , Q _ { k } ( t ) , { \boldsymbol u } ( t ) , { \boldsymbol f } _ { k } ( t ) \big \} \big ) } \\ & { \quad \mathrm { s . t . ~ } \ ( 9 ) , \ ( 7 6 ) , \ ( 7 7 ) , \ ( 7 8 ) , \ ( 7 9 ) , \ ( 8 0 ) , \ \mathrm { a n d ~ } ( 8 2 ) . } \end{array}
$$

Notice that problem (P4) for joint UAV trajectory and resource allocation design in the UAV-enabled wireless powered MEC is more difficult to solve than problem (P3) in the UAV-enabled WPCN, due to the computation causality constraints. How to solve problem (P4) is a challenging problem that has not been addressed yet.

In the literature, there have been some initial works [62], [64]–[66] that investigated simplified versions of problem (P4) by ignoring the computation causality constraints in (77)–(80). Indeed, in this case, problem (P4) has a similar structure as problem (P3), with the newly considered computation resource allocation variables. As a result, we can use similar approaches (i.e., multi-location-hovering, SHF trajectory, and time-quantization-based optimization) as those for problem (P3) in Section IV-C to solve the simplified version of (P4). For the general problem (P4) with constraints (77)–(80) considered, however, the above approaches may not work well due to the computation causality constraints. To tackle this issue, we may directly use time-quantization to transform problem (P4) with continuous-time variables as equivalent problems in discrete time, and then use the SCA techniques to solve it. It is expected that the UAV may fly back and forth to visit different GDs for offloading and downloading over time due to the computation causality constraints (see, e.g., [108]).

## C. Extensions

The single-UAV-enabled wireless powered MEC design can also be extended to the case with multiple UAVs and cloud integration, as discussed in the following to motivate future research.

• Multi-UAV Coordination: To provide sustainable computation services in a large area, multiple UAVs can be dispatched to cooperatively serve a large number of lowpower GDs. In this case, how to associate GDs with these UAVs and properly schedule their energy transmission, computation, and communication resources is a new problem to tackle.

• Edge-Cloud Integration: As the UAV-MEC-servers generally have limited computation capabilities, it is desirable to further integrate the centralized clouds to help the task execution, especially when the computation tasks are heavy. In practice, the centralized cloud can either be a large data center on the ground or deployed in high altitude platforms or even satellites [109]. In this case, it is necessary to partition the computation tasks into different parts to be executed locally at GDs and remotely at the UAV-MEC-server and/or cloud.

## VI. OTHER EXTENSIONS

In the preceding sections, we provided an overview on the UAV-enabled WPT and its applications in UAV-enabled

WPCN and UAV-enabled wireless powered MEC. Due to the space limitation, there are several important issues that are unaddressed. In the following, we briefly discuss these issues to motivate future research.

## A. Non-Linear Energy Harvesting Model

So far, we focused on the approximate linear energy harvesting model at GDs as widely adopted in the literature. In practice, however, the harvested DC power may not be a linear function with respect to the received RF power, especially when the received RF power level is sufficiently high or low. In general, the effect of non-linear energy harvesting models on the UAV-enabled WPT is still an uncharted area in the literature. For instance, due to the energy saturation at high RF power, the UAV may not need to fly exactly above the GDs for most efficient charging. Therefore, how to jointly optimize the transmit waveform and UAV trajectory is a crucial issue to be tackled for UAV-enabled WPT by considering the non-linear energy harvesting model [72].

## B. CSI Availability

CSI is important for UAVs to implement the (cooperative) transmit energy beamforming for WPT in multi-antenna and multi-UAV scenarios. There are generally three approaches for obtaining CSI in WPT, namely energy feedback, reverse-link channel estimation based on pilots, and channel estimation with limited feedback [8]. To obtain the CSI, the GDs normally need to consume additional time and energy to send training signals or implement channel estimation/feedback. Therefore, there generally exists a fundamental tradeoff in obtaining accurate CSI for efficient energy beamforming versus minimizing time/energy consumption [110], [111].

## C. AirComp

AirComp is an emerging approach to enable fast wireless data aggregation for achieving functional computation over the air by exploiting the superposition property of multiple access channels [112]–[114]. By exploiting AirComp, UAV and WPT, the UAV-enabled wireless powered AirComp can be an efficient way for aggregating the data from low-power GDs, which is expected to have abundant applications in future massive machine type communications, and for distributed learning [115], sensing [116], and consensus [117]. The key challenge lies in how to fully exploit the mobility of UAVs to achieve the required signal alignment for AirComp in a sustainable operation manner.

## D. Online Trajectory Design

So far, the UAV trajectory design is formulated as deterministic optimization problems, which can be generally solved in an offline manner via multi-location hovering, SHF trajectory design, time quantization and their variants. These designs, however, cannot work well when the channel propagation environments are spatial- and time-varying due to the obstacles between UAVs and moving GDs. To tackle this challenge, radio map [70], [118], [119] and reinforcement learning (RL) [120] are two useful tools to help autonomously update the UAV trajectories in an online manner.

## E. Ground Vehicles for WPT

Besides UAVs, ground vehicles can also be dispatched to serve as another type of mobile ETs on the ground to facilitate WPT, and the trajectory design framework can be generally extended to design the moving trajectory of ground vehicles for efficient WPT. Nevertheless, unlike UAVs that can freely fly in the 3D airspace, ground vehicles need to travel in the prescribed lane according to road conditions. Therefore, the trajectory optimization of ground vehicles is less flexible and may be even more challenging than that of UAVs.

## VII. CONCLUSION

In this paper, we provided a tutorial overview on UAVenabled WPT as well as its various applications and extensions, by focusing on how to exploit the UAV mobility to enhance the system performance. First, in the single-UAV-enabled WPT case, we presented a trajectory design framework to fairly maximize the harvested energy at multiple GDs, which consists of three main approaches, namely multi-location hovering, successive-hover-and-fly, and timequantization-based optimization. Next, we extended the trajectory design framework to the multi-UAV-enabled WPT case based on the schemes of UAV swarming and GD clustering, respectively. Then, we considered the UAV-enabled WPCN and wireless powered MEC, in which the trajectory design framework is investigated jointly with the resource allocations to improve communication/computation performance. Furthermore, open problems and promising research directions in UAV-enabled WPT were presented to inspire future exploration.

## REFERENCES

[1] C. K. Ho and R. Zhang, “Optimal energy allocation for wireless communications with energy harvesting constraints,” IEEE Trans. Signal Process., vol. 60, no. 9, pp. 4808–4818, Sep. 2012.

[2] H. Li, J. Xu, R. Zhang, and S. Cui, “A general utility optimization framework for energy-harvesting-based wireless communications,” IEEE Commun. Mag., vol. 53, no. 4, pp. 79–85, Apr. 2015.

[3] S. Bi, C. K. Ho, and R. Zhang, “Wireless powered communication: Opportunities and challenges,” IEEE Commun. Mag., vol. 53, no. 4, pp. 117–125, Apr. 2015.

[4] Z. Zhang, H. Pang, A. Georgiadis, and C. Cecati, “Wireless power transfer—An overview,” IEEE Trans. Ind. Electron., vol. 66, no. 2, pp. 1044–1058, Feb. 2019.

[5] J. Xu and R. Zhang, “A general design framework for MIMO wireless energy transfer with limited feedback,” IEEE Trans. Signal Process., vol. 64, no. 10, pp. 2475–2488, May 2016.

[6] K. Huang and V. K. N. Lau, “Enabling wireless power transfer in cellular networks: Architecture, modeling and deployment,” IEEE Trans. Wireless Commun., vol. 13, no. 2, pp. 902–912, Feb. 2014.

[7] X. Lu, D. Niyato, P. Wang, D. I. Kim, and Z. Han, “Wireless charger networking for mobile devices: Fundamentals, standards, and applications,” IEEE Wireless Commun., vol. 22, no. 2, pp. 126–135, Apr. 2015.

[8] J. Xu and R. Zhang, “Energy beamforming with one-bit feedback,” IEEE Trans. Signal Process., vol. 62, no. 20, pp. 5370–5381, Oct. 2014.

[9] Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, “A survey on mobile edge computing: The communication perspective,” IEEE Commun. Surveys Tuts., vol. 19, no. 4, pp. 2322–2358, 4th Quart., 2017.

[10] P. Mach and Z. Becvar, “Mobile edge computing: A survey on architecture and computation offloading,” IEEE Commun. Surveys Tuts., vol. 19, no. 3, pp. 1628–1656, 3rd Quart., 2017.

[11] X. Sun and N. Ansari, “EdgeIoT: Mobile edge computing for the Internet of Things,” IEEE Commun. Mag., vol. 54, no. 12, pp. 22–29, Dec. 2016.

[12] X. Zhou, R. Zhang, and C. K. Ho, “Wireless information and power transfer: Architecture design and rate-energy tradeoff,” IEEE Trans. Commun., vol. 61, no. 11, pp. 4754–4767, Nov. 2013.

[13] R. Zhang and C. K. Ho, “MIMO broadcasting for simultaneous wireless information and power transfer,” IEEE Trans. Wireless Commun., vol. 12, no. 5, pp. 1989–2001, May 2013.

[14] B. Clerckx, R. Zhang, R. Schober, D. W. K. Ng, D. I. Kim, and H. V. Poor, “Fundamentals of wireless information and power transfer: From RF energy harvester models to signal and system designs,” IEEE J. Sel. Areas Commun., vol. 37, no. 1, pp. 4–33, Jan. 2019.

[15] D. W. K. Ng, E. S. Lo, and R. Schober, “Wireless information and power transfer: Energy efficiency optimization in OFDMA systems,” IEEE Trans. Wireless Commun., vol. 12, no. 12, pp. 6352–6370, Dec. 2013.

[16] J. Xu, L. Liu, and R. Zhang, “Multiuser MISO beamforming for simultaneous wireless information and power transfer,” IEEE Trans. Signal Process., vol. 62, no. 18, pp. 4798–4810, Sep. 2014.

[17] H. Lee, K.-J. Lee, H. Kim, B. Clerckx, and I. Lee, “Resource allocation techniques for wireless powered communication networks with energy storage constraint,” IEEE Trans. Wireless Commun., vol. 15, no. 4, pp. 2619–2628, Apr. 2016.

[18] S. Bi, Y. Zeng, and R. Zhang, “Wireless powered communication networks: An overview,” IEEE Wireless Commun., vol. 23, no. 2, pp. 10–18, Apr. 2016.

[19] H. Ju and R. Zhang, “Throughput maximization in wireless powered communication networks,” IEEE Trans. Wireless Commun., vol. 13, no. 1, pp. 418–428, Jan. 2014.

[20] F. Wang, J. Xu, X. Wang, and S. Cui, “Joint offloading and computing optimization in wireless powered mobile-edge computing systems,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 1784–1797, Mar. 2018.

[21] F. Wang, J. Xu, and S. Cui, “Optimal energy allocation and task offloading policy for wireless powered mobile edge computing systems,” IEEE Trans. Wireless Commun., vol. 19, no. 4, pp. 2443–2459, Apr. 2020.

[22] S. Bi and Y. J. Zhang, “Computation rate maximization for wireless powered mobile-edge computing with binary computation offloading,” IEEE Trans. Wireless Commun., vol. 17, no. 6, pp. 4177–4190, Jun. 2018.

[23] X. Hu, K.-K. Wong, and K. Yang, “Wireless powered cooperationassisted mobile edge computing,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2375–2388, Apr. 2018.

[24] L. Liu, R. Zhang, and K.-C. Chua, “Secrecy wireless information and power transfer with MISO beamforming,” IEEE Trans. Signal Process., vol. 62, no. 7, pp. 1850–1863, Apr. 2014.

[25] Y. Zeng, B. Clerckx, and R. Zhang, “Communications and signals design for wireless power transmission,” IEEE Trans. Commun., vol. 65, no. 5, pp. 2264–2290, May 2017.

[26] D. W. K. Ng, E. S. Lo, and R. Schober, “Robust beamforming for secure communication in systems with wireless information and power transfer,” IEEE Trans. Wireless Commun., vol. 13, no. 8, pp. 4599–4615, Aug. 2014.

[27] G. Ma, J. Xu, Y.-F. Liu, and M. R. V. Moghadam, “Time-division energy beamforming for multiuser wireless power transfer with nonlinear energy harvesting,” IEEE Wireless Commun. Lett., vol. 10, no. 1, pp. 53–57, Jan. 2021.

[28] B. Clerckx and E. Bayguzina, “Waveform design for wireless power transfer,” IEEE Trans. Signal Process., vol. 64, no. 23, pp. 6313–6328, Dec. 2016.

[29] B. Clerckx, “Wireless information and power transfer: Nonlinearity, waveform design, and rate-energy tradeoff,” IEEE Trans. Signal Process., vol. 66, no. 4, pp. 847–862, Feb. 2018.

[30] E. Boshkovska, D. W. K. Ng, N. Zlatanov, A. Koelpin, and R. Schober, “Robust resource allocation for MIMO wireless powered communication networks based on a non-linear EH model,” IEEE Trans. Commun., vol. 65, no. 5, pp. 1984–1999, May 2017.

[31] S. Bi and R. Zhang, “Placement optimization of energy and information access points in wireless powered communication networks,” IEEE Trans. Wireless Commun., vol. 15, no. 3, pp. 2351–2364, Mar. 2016.

[32] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.

[33] Y. Zeng, J. Lyu, and R. Zhang, “Cellular-connected UAV: Potential, challenges, and promising technologies,” IEEE Wireless Commun., vol. 26, no. 1, pp. 120–127, Feb. 2019.

[34] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., early access, Oct. 19, 2020. [Online]. Available: https://arxiv.org/pdf/2010.09317.pdf

[35] Y. Zeng, R. Zhang, and T. J. Lim, “Throughput maximization for UAV-enabled mobile relaying systems,” IEEE Trans. Commun., vol. 64, no. 12, pp. 4983–4996, Dec. 2016.

[36] L. Zhu, J. Zhang, Z. Xiao, X. Cao, X.-G. Xia, and R. Schober, “Millimeter-wave full-duplex UAV relay: Joint positioning, beamforming, and power control,” IEEE J. Sel. Areas Commun., vol. 38, no. 9, pp. 2057–2073, Sep. 2020.

[37] P. K. Sharma and D. I. Kim, “Secure 3D mobile UAV relaying for hybrid satellite-terrestrial networks,” IEEE Trans. Wireless Commun., vol. 19, no. 4, pp. 2770–2784, Apr. 2020.

[38] S. Hosseinalipour, A. Rahmati, and H. Dai, “Interference avoidance position planning in dual-hop and multi-hop UAV relay networks,” IEEE Trans. Wireless Commun., vol. 19, no. 11, pp. 7033–7048, Nov. 2020.

[39] J. Lyu, Y. Zeng, and R. Zhang, “Cyclical multiple access in UAV-aided communications: A throughput-delay tradeoff,” IEEE Wireless Commu. Lett., vol. 5, no. 6, pp. 600–603, Dec. 2016.

[40] Q. Wu, J. Xu, and R. Zhang, “Capacity characterization of UAVenabled two-user broadcast channel,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1955–1971, Sep. 2018.

[41] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[42] L. Liu, S. Zhang, and R. Zhang, “CoMP in the sky: UAV placement and movement optimization for multi-user communications,” IEEE Trans. Commun., vol. 67, no. 8, pp. 5645–5658, Aug. 2019.

[43] J. Li et al., “Joint optimization on trajectory, altitude, velocity, and link scheduling for minimum mission time in UAV-aided data collection,” IEEE Internet Things J., vol. 7, no. 2, pp. 1464–1475, Feb. 2020.

[44] C. Zhan and Y. Zeng, “Aerial–ground cost tradeoff for multi-UAVenabled data collection in wireless sensor networks,” IEEE Trans. Commun., vol. 68, no. 3, pp. 1937–1950, Mar. 2020.

[45] C. You and R. Zhang, “3D trajectory optimization in rician fading for UAV-enabled data harvesting,” IEEE Trans. Wireless Commun., vol. 18, no. 6, pp. 3192–3207, Jun. 2019.

[46] Z. Wang, R. Liu, Q. Liu, J. S. Thompson, and M. Kadoch, “Energyefficient data collection and device positioning in UAV-assisted IoT,” IEEE Internet Thing J., vol. 7, no. 2, pp. 1122–1139, Feb. 2020.

[47] T. Feng, L. Xie, J. Yao, and J. Xu, “UAV-enabled data collection for wireless sensor networks with distributed beamforming,” Apr. 2020. [Online]. Available: https://arxiv.org/abs/2004.11332

[48] G. Zhang, Q. Wu, M. Cui, and R. Zhang, “Securing UAV communications via joint trajectory and power control,” IEEE Trans. Wireless Commun., vol. 18, no. 2, pp. 1376–1389, Feb. 2019.

[49] J. Yao and J. Xu, “Joint 3D maneuver and power adaptation for secure UAV communication with CoMP reception,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6992–7006, Oct. 2020.

[50] C. Zhong, J. Yao, and J. Xu, “Secure UAV communication with cooperative jamming and trajectory control,” IEEE Commun. Lett., vol. 23, no. 2, pp. 286–289, Feb. 2019.

[51] H. Wang, J. Wang, G. Ding, J. Chen, Y. Li, and Z. Han, “Spectrum sharing planning for full-duplex UAV relaying systems with underlaid D2D communications,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1986–1999, Sep. 2018.

[52] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.

[53] A. Asheralieva and D. Niyato, “Game theory and Lyapunov optimization for cloud-based content delivery networks with device-todevice and UAV-enabled caching,” IEEE Trans. Veh. Technol., vol. 68, no. 10, pp. 10094–10110, Oct. 2019.

[54] A. Al-Hourani and K. Gomez, “Modeling cellular-to-UAV path-loss for suburban environments,” IEEE Wireless Commun. Lett., vol. 7, no. 1, pp. 82–85, Feb. 2018.

[55] D. W. Matolak and R. Sun, “Unmanned aircraft systems: Air-ground channel characterization for future applications,” IEEE Veh. Technol. Mag., vol. 10, no. 2, pp. 79–85, Jun. 2015.

[56] S. Najmeddint, A. Bayat, S. Aïssa, and S. Tahar, “Energy-efficient resource allocation for UAV-enabled wireless powered communications,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), Marrakesh, Morocco, Apr. 2019, pp. 1–6.

[57] Y. Wang, W. Yang, X. Shang, and Y. Cai, “Energy-efficient secure transmission for UAV-enabled wireless powered communication,” in Proc. IEEE 10th Int. Conf. Wireless Commun. Signal Process. (WCSP), Hangzhou, China, Oct. 2018, pp. 1–5.

[58] H.-T. Ye, X. Kang, J. Joung, and Y.-C. Liang, “Optimization for full-duplex rotary-wing UAV-enabled wireless-powered IoT networks,” IEEE Trans. Wireless Commun., vol. 19, no. 7, pp. 5057–5072, Jul. 2020.

[59] S. Yin, Y. Zhao, L. Li, and F. R. Yu, “UAV-assisted cooperative communications with time-sharing information and power transfer,” IEEE Trans. Veh. Technol., vol. 69, no. 2, pp. 1554–1567, Feb. 2020.

[60] S. Yin, Y. Zhao, L. Li, and F. R. Yu, “UAV-assisted cooperative communications with power-splitting information and power transfer,” IEEE Trans. Green Commun. Netw., vol. 3, no. 4, pp. 1044–1057, Dec. 2019.

[61] S. Yin, L. Li, and F. R. Yu, “Resource allocation and basestation placement in downlink cellular networks assisted by multiple wireless powered UAVs,” IEEE Trans. Veh. Technol., vol. 69, no. 2, pp. 2171–2184, Feb. 2020.

[62] Y. Du, K. Yang, K. Wang, G. Zhang, Y. Zhao, and D. Chen, “Joint resources and workflow scheduling in UAV-enabled wirelessly-powered MEC for IoT systems,” IEEE Trans. Veh. Technol., vol. 68, no. 10, pp. 10187–10200, Oct. 2019.

[63] J. Wang, C. Jin, Q. Tang, N. Xiong, and G. Srivastava, “Intelligent ubiquitous network accessibility for wireless-powered MEC in UAVassisted B5G,” IEEE Trans. Netw. Sci. Eng., early access, Oct. 6, 2020, doi: 10.1109/TNSE.2020.3029048.

[64] Y. Liu, K. Xiong, Q. Ni, P. Fan, and K. B. Letaief, “UAV-assisted wireless powered cooperative mobile edge computing: Joint offloading, CPU control, and trajectory optimization,” IEEE Internet Things J., vol. 7, no. 4, pp. 2777–2790, Apr. 2020.

[65] F. Zhou, Y. Wu, R. Q. Hu, and Y. Qian, “Computation rate maximization in UAV-enabled wireless-powered mobile-edge computing systems,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1927–1941, Sep. 2018.

[66] X. Hu, K.-K. Wong, and Y. Zhang, “Wireless-powered edge computing with cooperative UAV: Task, time scheduling and trajectory design,” IEEE Trans. Wireless Commun., vol. 19, no. 12, pp. 8083–8098, Dec. 2020.

[67] J. Xu, Y. Zeng, and R. Zhang, “UAV-enabled wireless power transfer: Trajectory design and energy optimization,” IEEE Trans. Wireless Commun., vol. 17, no. 8, pp. 5092–5106, Aug. 2018.

[68] Y. Hu, X. Yuan, J. Xu, and A. Schmeink, “Optimal 1D trajectory design for UAV-enabled multiuser wireless power transfer,” IEEE Trans. Commun., vol. 67, no. 8, pp. 5674–5688, Aug. 2019.

[69] S. Ku, S. Jung, and C. Lee, “UAV trajectory design based on reinforcement learning for wireless power transfer,” in Proc. 34th Int. Techn. Conf. Circuits/Syst. Comput. Commun. (ITC-CSCC), JeJu, South Korea, Jun. 2019, pp. 1–3.

[70] X. Mo, Y. Huang, and J. Xu, “Radio-map-based robust positioning optimization for UAV-enabled wireless power transfer,” IEEE Wireless Commun. Lett., vol. 9, no. 2, pp. 179–183, Feb. 2020.

[71] T. Yang, Y. Hu, X. Yuan, and R. Mathar, “Genetic algorithm based UAV trajectory design in wireless power transfer systems,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), Marrakesh, Morocco, Apr. 2019, pp. 1–6.

[72] X. Yuan, T. Yang, Y. Hu, J. Xu, and A. Schmeink, “Trajectory design for UAV-enabled multiuser wireless power transfer with nonlinear energy harvesting,” IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 1105–1121, Feb. 2021.

[73] L. Xie, J. Xu, and Y. Zeng, “Common throughput maximization for UAV-enabled interference channel with wireless powered communications,” IEEE Trans. Commun., vol. 68, no. 5, pp. 3197–3212, May 2020.

[74] L. Xie, J. Xu, and R. Zhang, “Throughput maximization for UAVenabled wireless powered communication networks,” IEEE Internet Things J., vol. 6, no. 2, pp. 1690–1703, Apr. 2019.

[75] Z. Hadzi-Velkov, S. Pejoski, R. Schober, and N. Zlatanov, “Wireless powered ALOHA networks with UAV-mounted-base stations,” IEEE Wireless Commu. Lett., vol. 9, no. 1, pp. 56–60, Jan. 2020.

[76] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the sky: A tutorial on UAV communications for 5G and beyond,” Proc. IEEE, vol. 107, no. 12, pp. 2327–2375, Dec. 2019.

[77] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2334–2360, 3rd Quart., 2019.

[78] Y. Wu, L. Qiu, and J. Xu, “UAV-enabled wireless power transfer with directional antenna: A two-user case,” in Proc. 15th Int. Symp. Wireless Commun. Syst. (ISWCS), Lisbon, Portugal, Aug. 2018, pp. 1–6.

[79] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

[80] L. Liu, S. Zhang, and R. Zhang, “Multi-beam UAV communication in cellular uplink: Cooperative interference cancellation and sumrate maximization,” IEEE Trans. Wireless Commun., vol. 18, no. 10, pp. 4679–4691, Oct. 2019.

[81] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.

[82] M. Hong, Q. Li, and Y.-F. Liu, “Decomposition by successive convex approximation: A unifying approach for linear transceiver design in heterogeneous networks,” IEEE Trans. Wireless Commun., vol. 15, no. 2, pp. 1377–1392, Feb. 2016.

[83] W. Yu and R. Lui, “Dual methods for nonconvex spectrum optimization of multicarrier systems,” IEEE Trans. Commun., vol. 54, no. 7, pp. 1310–1322, Jul. 2006.

[84] J. K. Lenstra, A. H. G. R. Kan, E. L. Lawler, and D. B. Shmoys, The Traveling Salesman Problem: A Guided Tour of Combinatorial Optimization, 1st ed. Hoboken, NJ, USA: Wiley, 1985.

[85] C. E. Miller, A. W. Tucker, and R. A. Zemlin, “Integer programming formulation of traveling salesman problems,” J. ACM, vol. 7, no. 4, pp. 326–329, Oct. 1960. [Online]. Available: https://doi.org/10.1145/321043.321046

[86] M. Grant and S. Boyd, CVX: MATLAB Software for Disciplined Convex Programming, CVX Res., Austin, TX, USA, 2016.

[87] A. Sabharwal, P. Schniter, D. Guo, D. W. Bliss, S. Rangarajan, and R. Wichman, “In-band full-duplex wireless: Challenges and opportunities,” IEEE J. Sel. Areas Commun., vol. 32, no. 9, pp. 1637–1652, Sep. 2014.

[88] Y. Liu, Z. Qin, M. Elkashlan, Z. Ding, A. Nallanathan, and L. Hanzo, “Nonorthogonal multiple access for 5G and beyond,” Proc. IEEE, vol. 105, no. 12, pp. 2347–2381, Dec. 2017.

[89] H. Hu, K. Xiong, G. Qu, Q. Ni, P. Fan, and K. B. Letaief, “AoIminimal trajectory planning and data collection in UAV-assisted wireless powered IoT networks,” IEEE Internet Things J., vol. 8, no. 2, pp. 1211–1223, Jan. 2021.

[90] F. Wu, D. Yang, L. Xiao, and L. Cuthbert, “Energy consumption and completion time tradeoff in rotary-wing UAV enabled WPCN,” IEEE Access, vol. 7, pp. 79617–79635, 2019.

[91] Z. Wang, W. Xu, D. Yang, and J. Lin, “Joint trajectory optimization and user scheduling for rotary-wing UAV-enabled wireless powered communication networks,” IEEE Access, vol. 7, pp. 181369–181380, 2019.

[92] J. Tang, J. Song, J. Ou, J. Luo, X. Zhang, and K.-K. Wong, “Minimum throughput maximization for multi-UAV enabled WPCN: A deep reinforcement learning method,” IEEE Access, vol. 8, pp. 9124–9132, 2020.

[93] F. Wu, D. Yang, L. Xiao, and L. Cuthbert, “Minimum-throughput maximization for multi-UAV-enabled wireless-powered communication networks,” Sensors, vol. 19, no. 7, p. 1491, 2019.

[94] H. Wang, J. Wang, G. Ding, L. Wang, T. A. Tsiftsis, and P. K. Sharma, “Resource allocation for energy harvesting-powered D2D communication underlaying UAV-assisted networks,” IEEE Trans. Green Commun. Netw., vol. 2, no. 1, pp. 14–24, Mar. 2018.

[95] Z. Hadzi-Velkov, S. Pejoski, N. Zlatanov, and R. Schober, “UAVassisted wireless powered relay networks with cyclical NOMA-TDMA,” IEEE Wireless Commun. Lett., vol. 9, no. 12, pp. 2088–2092, Dec. 2020.

[96] Y. Li, D. Yang, Y. Xu, L. Xiao, and H. Chen, “Throughput maximization for UAV-enabled relaying in wireless powered communication networks,” Sensors, vol. 19, no. 13, p. 2989, 2019.

[97] J. Park, H. Lee, S. Eom, and I. Lee, “UAV-aided wireless powered communication networks: Trajectory optimization and resource allocation for minimum throughput maximization,” IEEE Access, vol. 7, pp. 134978–134991, 2019.

[98] G. Yang, C. K. Ho, and Y. L. Guan, “Multi-antenna wireless energy transfer for backscatter communication systems,” IEEE J. Sel. Areas Commun., vol. 33, no. 12, pp. 2974–2987, Dec. 2015.

[99] S. Yang, Y. Deng, X. Tang, Y. Ding, and J. Zhou, “Energy efficiency optimization for UAV-assisted backscatter communications,” IEEE Commun. Lett., vol. 23, no. 11, pp. 2041–2045, Nov. 2019.

[100] G. Yang, R. Dai, and Y.-C. Liang, “Energy-efficient UAV backscatter communication with joint trajectory design and resource optimization,” IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 926–941, Feb. 2021.

[101] G. Zhu, S.-W. Ko, and K. Huang, “Inference from randomized transmissions by many backscatter sensors,” IEEE Trans. Wireless Commun., vol. 17, no. 5, pp. 3111–3127, May 2018.

[102] A. Farajzadeh, O. Ercetin, and H. Yanikomeroglu, “Mobility-assisted over-the-air computation for backscatter sensor networks,” IEEE Wireless Commun. Lett., vol. 9, no. 5, pp. 675–678, May 2020.

[103] M. Hua, L. Yang, C. Li, Q. Wu, and A. L. Swindlehurst, “Throughput maximization for UAV-aided backscatter communication networks,” IEEE Trans. Commun., vol. 68, no. 2, pp. 1254–1270, Feb. 2020.

[104] A. Farajzadeh, O. Ercetin, and H. Yanikomeroglu, “UAV data collection over NOMA backscatter networks: UAV altitude and trajectory optimization,” in Proc. IEEE Int. Conf. Commun. (ICC), Shanghai, China, May 2019, pp. 1–7.

[105] S.-H. Yeh, Y.-S. Wang, T. D. P. Perera, Y.-W. P. Hong, and D. N. K. Jayakody, “UAV trajectory optimization for data-gathering from backscattering sensor networks,” in Proc. IEEE Int. Conf. Commun. (ICC), Dublin, Ireland, Jun. 2020, pp. 1–6.

[106] M. Hua, A. L. Swindlehurst, C. Li, and L. Yang, “UAV-aided backscatter networks: Joint UAV trajectory and protocol design,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Waikoloa, HI, USA, Dec. 2019, pp. 1–6.

[107] X. Cao, F. Wang, J. Xu, R. Zhang, and S. Cui, “Joint computation and communication cooperation for energy-efficient mobile edge computing,” IEEE Internet Things J., vol. 6, no. 3, pp. 4188–4200, Jun. 2019.

[108] X. Cao, J. Xu, and R. Zhang, “Mobile edge computing for cellularconnected UAV: Computation offloading and trajectory optimization,” in Proc. IEEE 19th Int. Workshop Signal Process. Adv. Wireless Commun. (SPAWC), Kalamata, Greece, Jun. 2018, pp. 1–5.

[109] W. Chen, B. Liu, H. Huang, S. Guo, and Z. Zheng, “When UAV swarm meets edge-cloud computing: The QoS perspective,” IEEE Netw., vol. 33, no. 2, pp. 36–43, Mar./Apr. 2019.

[110] Y. Zeng and R. Zhang, “Optimized training for net energy maximization in multi-antenna wireless energy transfer over frequencyselective channel,” IEEE Trans. Commun., vol. 63, no. 6, pp. 2360–2373, Jun. 2015.

[111] Y. Zeng and R. Zhang, “Optimized training design for wireless energy transfer,” IEEE Trans. Commun., vol. 63, no. 2, pp. 536–550, Feb. 2015.

[112] B. Nazer and M. Gastpar, “Computation over multiple-access channels,” IEEE Trans. Inf. Theory, vol. 53, no. 10, pp. 3498–3516, Oct. 2007.

[113] X. Cao, G. Zhu, J. Xu, and K. Huang, “Optimized power control for over-the-air computation in fading channels,” IEEE Trans. Wireless Commun., vol. 19, no. 11, pp. 7498–7513, Nov. 2020.

[114] X. Cao, G. Zhu, J. Xu, and K. Huang, “Cooperative interference management for over-the-air computation networks,” IEEE Trans. Wireless Commun., vol. 20, no. 4, pp. 2634–2651, Apr. 2021.

[115] G. Zhu, Y. Wang, and K. Huang, “Broadband analog aggregation for low-latency federated edge learning,” IEEE Trans. Wireless Commun., vol. 19, no. 1, pp. 491–506, Jan. 2020.

[116] O. Abari, H. Rahul, and D. Katabi, “Over-the-air function computation in sensor networks,” Dec. 2016. [Online]. Available: https://arxiv.org/pdf/1612.02307.pdf

[117] F. Molinari, S. Stanczak, and J. Raisch, “Exploiting the superposition property of wireless communication for average consensus problems in multi-agent systems,” in Proc. Eur. Control Conf. (ECC), Limassol, Cyprus, Jun. 2018, pp. 1766–1772.

[118] B. Zhang and J. Chen, “Constructing radio maps for UAV communications via dynamic resolution virtual obstacle maps,” in Proc. IEEE Int. Workshop Signal Process. Adv. Wireless Commun. (SPAWC), Atlanta, GA, USA, May 2020, pp. 1–5.

[119] O. Esrafilian, R. Gangula, and D. Gesbert, “Learning to communicate in UAV-aided wireless networks: Map-based approaches,” IEEE Internet Things J., vol. 6, no. 2, pp. 1791–1802, Apr. 2019.

[120] H. Bayerlein, M. Theile, M. Caccamo, and D. Gesbert, “UAV path planning for wireless data harvesting: A deep reinforcement learning approach,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Taipei, Taiwan, Dec. 2020, pp. 1–6.

![](images/ed608e4a6464e2f676788f8ce3c35eebebea52405be5444ade40086d5c21f790.jpg)  
Lifeng Xie (Member, IEEE) received the B.Eng. degree from Guangdong University of Technology, China, in 2016, where he is currently pursuing the Ph.D. degree with the School of Information Engineering. He is a visiting student with the Future Network of Intelligence Institute, The Chinese University of Hong Kong (Shenzhen), Shenzhen, China. His research interests include energy harvesting in wireless communications, wireless information and power transfer, and UAV communications.

![](images/4952d05f8428e958437397b5a406462b9e9256c3763bd84439a44308db4b9092.jpg)

Xiaowen Cao (Graduate Student Member, IEEE) received the B.Eng. degree from Guangdong University of Technology, China, in 2017, where she is currently pursuing the Ph.D. degree with the School of Information Engineering. She is a visiting student with the Future Network of Intelligence Institute, The Chinese University of Hong Kong (Shenzhen), Shenzhen, China. Her research interests include mobile edge computing and over-the-air computation.

![](images/e361f2f1f218b98a2bd60784bbb8e95241f3b95e6284dcbe6b4f456c9b97945d.jpg)

Jie Xu (Member, IEEE) received the B.E. and Ph.D. degrees from the University of Science and Technology of China in 2007 and 2012, respectively. From 2012 to 2014, he was a Research Fellow with the Department of Electrical and Computer Engineering, National University of Singapore. From 2015 to 2016, he was a Postdoctoral Research Fellow with the Engineering Systems and Design Pillar, Singapore University of Technology and Design. From 2016 to 2019, he was a Professor with the School of Information Engineering, Guangdong

University of Technology, China. He is currently an Associate Professor with the School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. His research interests include wireless communications, wireless information and power transfer, UAV communications, edge computing and intelligence, and integrated sensing and communication. He was a recipient of the 2017 IEEE Signal Processing Society Young Author Best Paper Award, the IEEE/CIC ICCC 2019 Best Paper Award, the 2019 IEEE Communications Society Asia–Pacific Outstanding Young Researcher Award, and the 2019 Wireless Communications Technical Committee Outstanding Young Researcher Award. He is the Symposium Co-Chair of the IEEE GLOBECOM 2019 Wireless Communications Symposium, the workshop co-chair of several IEEE ICC and GLOBECOM workshops, the Tutorial Co-Chair of the IEEE/CIC ICCC 2019, and the Vice Co-chair of the IEEE Emerging Technology Initiative on ISAC. He served or is serving as an Editor of the IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE WIRELESS COMMUNICATIONS LETTERS, and Journal of Communications and Information Networks, an Associate Editor of IEEE ACCESS, and a Guest Editor of IEEE WIRELESS COMMUNICATIONS, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, and Science China Information Sciences.

![](images/5413c73f2c4d131ece3dccc529677415283d38d400f8137d2668999c71a7ea64.jpg)

Rui Zhang (Fellow, IEEE) received the B.Eng. (First-Class Hons.) and M.Eng. degrees in electrical engineering from the National University of Singapore, Singapore, and the Ph.D. degree in electrical engineering from the Stanford University, Stanford, CA, USA.

From 2007 to 2010, he worked with the Institute for Infocomm Research, ASTAR, Singapore. Since 2010, he has been working with the National University of Singapore, where he is currently a Provosts Chair Professor with the Department of

Electrical and Computer Engineering. He has published over 200 journal papers and over 180 conference papers. He has been listed as a Highly Cited Researcher by Thomson Reuters/Clarivate Analytics since 2015. His current research interests include UAV/satellite communications, wireless power transfer, reconfigurable MIMO, and optimization methods.

Dr. Zhang was a recipient of the 6th IEEE Communications Society Asia–Pacific Region Best Young Researcher Award in 2011, the Young Researcher Award of National University of Singapore in 2015, and the Wireless Communications Technical Committee Recognition Award in 2020. He was the co-recipient of the IEEE Marconi Prize Paper Award in Wireless Communications in 2015 and 2020, the IEEE Communications Society Asia– Pacific Region Best Paper Award in 2016, the IEEE Signal Processing Society Best Paper Award in 2016, the IEEE Communications Society Heinrich Hertz Prize Paper Award in 2017 and 2020, the IEEE Signal Processing Society Donald G. Fink Overview Paper Award in 2017, and the IEEE Technical Committee on Green Communications and Computing Best Journal Paper Award in 2017. His coauthored paper received the IEEE Signal Processing Society Young Author Best Paper Award in 2017. He served for over 30 international conferences as the TPC co-chair or an organizing committee member, and as the Guest Editor for three special issues in the IEEE JOURNAL OF SELECTED TOPICS IN SIGNAL PROCESSING and the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS. He served as an Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS from 2012 to 2016, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS: Green Communications and Networking Series from 2015 to 2016, the IEEE TRANSACTIONS ON SIGNAL PROCESSING from 2013 to 2017, and IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING from 2016 to 2020. He is currently an Editor of IEEE TRANSACTIONS ON COMMUNICATIONS. He was an Elected Member of the IEEE Signal Processing Society SPCOM Technical Committee from 2012 to 2017 and SAM Technical Committee from 2013 to 2015, and served as the Vice Chair of the IEEE Communications Society Asia–Pacific Board Technical Affairs Committee from 2014 to 2015. He serves as a member of the Steering Committee of the IEEE WIRELESS COMMUNICATIONS LETTERS. He is a Distinguished Lecturer of IEEE Signal Processing Society and IEEE Communications Society.