# UAV-Enabled Passive 6D Movable Antennas: Joint Deployment and Beamforming Optimization

Changhao Liu , Graduate Student Member, IEEE, Weidong Mei , Member, IEEE, Peilan Wang , Member, IEEE, Yinuo Meng, Student Member, IEEE, Zhi Chen , Senior Member, IEEE, and Boyu Ning , Member, IEEE

Abstract—Intelligent reflecting surface (IRS) is composed of numerous passive reflecting elements and can be mounted on uncrewed aerial vehicles (UAVs) to achieve six-dimensional (6D) movement by adjusting the UAV’s three-dimensional (3D) location and 3D orientation simultaneously. Hence, in this paper, we investigate a new UAV-enabled passive 6D movable antenna (6DMA) architecture by mounting an IRS on a UAV and address the associated joint deployment and beamforming optimization problem. In particular, we consider a passive 6DMA-aided multicast system with a multi-antenna base station (BS) and multiple remote users, aiming to jointly optimize the IRS’s location and 3D orientation, as well as its passive beamforming to maximize the minimum received signal-to-noise ratio (SNR) among all users under the practical angle-dependent signal reflection model. However, this optimization problem is challenging to be optimally solved due to the intricate relationship between the users’ SNRs and the IRS’s location and orientation. To tackle this challenge, we first focus on a simplified case with a single user, showing that one-dimensional (1D) orientation suffices to achieve the optimal performance. Next, we show that for any given IRS’s location, the optimal 1D orientation can be derived in closed form, based on which several useful insights are drawn. To solve the max-min SNR problem in the general multi-user case, we propose an alternating optimization (AO) algorithm by alternately optimizing the IRS’s beamforming and location/orientation via successive convex approximation (SCA) and hybrid coarse- and fine-grained search, respectively. To avoid undesirable local sub-optimal solutions, a Gibbs sampling (GS) method is proposed to generate new IRS locations and orientations for exploration in each AO iteration. Numerical results validate our theoretical analyses and demonstrate the superiority of our proposed AO algorithm with GS to conventional AO and other baseline deployment strategies with location or orientation optimization only.

Digital Object Identifier 10.1109/TWC.2025.3643647

Index Terms—Uncrewed aerial vehicle (UAV), intelligent reflecting surface (IRS), 6D movable antennas, IRS deployment, 3D orientation, alternating optimization (AO), Gibbs sampling.

## I. INTRODUCTION

NTELLIGENT reflecting surface (IRS), also known as reconfigurable intelligent surface (RIS), has recently emerged as a promising technology to enhance the performance of wireless communication systems in an energyefficient and cost-effective manner. Specifically, an IRS is a planar meta-surface consisting of a large number of subwavelength-size passive reflecting elements, each of which is capable of reflecting the impinging signals with an adjustable phase shift. By jointly optimizing the phase shifts of its reflecting elements (i.e., passive beamforming), the IRS can alter the direction of its reflected signals, thereby realizing various purposes such as coverage extension, interference suppression, wireless power transfer, target sensing, etc [2], [3], [4], [5], [6], [7], [8].

However, the deployment of the IRS plays a significant role in realizing the above benefits, as an IRS can only reflect signals from/to its pointing half-space and may cause severe signal power loss due to its passive reflection. Hence, some prior works have delved into the IRS deployment optimization under different system setups [9], [10], [11], [12], [13], [14]. For example, a two-timescale optimization framework was proposed in [9], where the IRS’s deployment and passive beamforming were optimized based on the long- and shortterm channel knowledge, respectively. In [10], the authors optimized the deployment and beamforming of two IRSs distributed on the same wall to extend the BS’s signal coverage within a target region. In [11], the authors jointly optimized the beamforming and deployment of an IRS to maximize the non-outage secrecy rate in a secure wireless communication system. The authors in [12] compared the capacity regions achievable by two IRS deployment strategies with the IRS/IRSs deployed near the base station (BS) and each of distributed users, respectively, and showed the superiority of the former over the latter under the same total number of reflecting elements. In [13] and [14], the authors optimized IRS’s deployment to achieve the trade-off between the indoor coverage performance and total deployment cost using graphbased approaches. However, all of the above works [9], [10], [11], [12], [13], [14] assumed terrestrial IRSs, which still face limitations due to their generally fixed positions and 180<sup>◦</sup> halfspace reflection, potentially failing to cover all BSs/users.

TABLE I  
COMPARISON OF EXISTING RELATED WORKS
<table><tr><td rowspan=1 colspan=1>Referencenumber</td><td rowspan=1 colspan=1>Orientationoptimization</td><td rowspan=1 colspan=1>Positionoptimization</td><td rowspan=1 colspan=1>Reflectionmodel</td><td rowspan=1 colspan=1>Systemsetup</td></tr><tr><td rowspan=1 colspan=1>[18]</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3D</td><td rowspan=1 colspan=1>Isotropic</td><td rowspan=1 colspan=1>Single-user</td></tr><tr><td rowspan=1 colspan=1>[19]</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2D</td><td rowspan=1 colspan=1>Isotropic</td><td rowspan=1 colspan=1>Coverage</td></tr><tr><td rowspan=1 colspan=1>[23]</td><td rowspan=1 colspan=1>1D</td><td rowspan=1 colspan=1>1D</td><td rowspan=1 colspan=1>Angle-dependent</td><td rowspan=1 colspan=1>Single-user</td></tr><tr><td rowspan=1 colspan=1>[24]</td><td rowspan=1 colspan=1>1D</td><td rowspan=1 colspan=1>2D</td><td rowspan=1 colspan=1>Angle-dependent</td><td rowspan=1 colspan=1>Single-user</td></tr><tr><td rowspan=1 colspan=1>[1]</td><td rowspan=1 colspan=1>3D</td><td rowspan=1 colspan=1>1D</td><td rowspan=1 colspan=1>Angle-dependent</td><td rowspan=1 colspan=1>Single-user</td></tr><tr><td rowspan=1 colspan=1>This paper</td><td rowspan=1 colspan=1>3D</td><td rowspan=1 colspan=1>2D</td><td rowspan=1 colspan=1>Angle-dependent</td><td rowspan=1 colspan=1>Multi-user</td></tr></table>

To overcome the above issues, some previous studies have proposed mounting the IRS on an aerial platform (e.g., an uncrewed aerial vehicle (UAV)), referred to as aerial IRS (AIRS).<sup>1</sup> Compared to its terrestrial counterpart, an AIRS is more likely to achieve 360<sup>◦</sup> panoramic full-angle reflection, due to its much higher altitude than the terrestrial BSs and users [16]. In addition, its location and even orientation can be flexibly adjusted by leveraging the maneuverability of UAVs.<sup>2</sup> Motivated by the above benefits of the AIRS, the authors in [18] and [19] aimed to jointly optimize the location and reflection of an AIRS serving multiple users. However, both works assumed isotropic signal reflection by each AIRS reflecting element, while the AIRS’s passive beamforming gain is practically dependent on its incident and reflected angles, as have been validated in [20], [21], and [22] via on-site measurements. In view of this fact, the orientation of the AIRS plays a critical role in affecting the overall communication performance and should be carefully optimized as well. In [23] and [24], the authors have investigated the joint location and orientation optimization for a terrestrial IRS and an AIRS, respectively. Nevertheless, they only considered one-dimensional (1D) orientation adjustment, despite the additional degrees of freedom (DoFs) offered by three-dimensional (3D) orientation/posture control. Moreover, both [23] and [24] considered a single-user setup, while the effects of AIRS orientation on the multi-user communication system remain unknown. In our prior work [1], we studied the joint position and orientation optimization of an AIRS in the single-user scenario. In this paper, we extend the study to the multiuser case, which is more challenging due to the need to accommodate the channel conditions for multiple users. A summary of the existing works is provided in Table I.

To fully exploit all six-dimensional (6D) DoFs available for UAV-mounted IRSs or AIRSs, i.e., 3D location and 3D orientation, we propose a new architecture of UAV-enabled passive 6D movable antenna (6DMA) in this paper, as shown in Fig. 1. Note that compared to the terrestrial 6DMA proposed in [25] and [26], our proposed UAV-enabled 6DMA offers a broader range of tuning for antenna positioning and orientation thanks to the mobility of the UAV. Focusing on a multicast communication system, we aim to jointly optimize the AIRS’s location and 3D orientation, as well as its passive beamforming to maximize the minimum received signal-to-noise ratio (SNR) among all users under the practical angle-dependent signal reflection model. To the best of our knowledge, this is the first work investigating the performance optimization of a UAV-enabled passive 6DMA in the literature. Our main contributions are summarized as follows.

To gain useful insights into the passive 6DMA, we first solve the SNR maximization problem in a simplified single-user setup. Our analysis demonstrates that in this case, 1D orientation is sufficient to achieve the maximum received SNR at the user. Next, we show that for any given AIRS location, the optimal 1D orientation can be derived in closed form, based on which several useful insights are drawn. Furthermore, in some special cases regarding the AIRS’s altitude and the BS-user distance, we also derive the AIRS’s optimal location in closed form.

However, the max-min SNR optimization problem in the general multi-user case is much more challenging to be optimally solved due to the intricate coupling of the AIRS’s 6D movement and beamforming. To tackle this challenge, we propose an alternating optimization (AO) algorithm by alternately optimizing the AIRS’s passive beamforming and location/orientation via successive convex approximation (SCA) and multi-dimensional search, respectively. Particularly, to reduce the searching complexity in location/orientation optimization with given AIRS passive beamforming, we first conduct a coarse-grained search to quickly obtain a locally suboptimal solution, followed by a fine-grained search near this solution. Furthermore, to avoid undesirable trapping at sub-optimal solutions in the conventional AO, a Gibbs sampling (GS) method is proposed to generate a sequence of samples of the AIRS’s candidate locations and orientations via a probability-based Markov chain for solution exploration.

• Numerical results validate our theoretical analyses and demonstrate the superiority of our proposed enhanced AO algorithm with GS to conventional AO without GS and other baseline deployment strategies with either location or orientation optimization only and that without accounting for the AIRS’s angle-dependent signal reflection. It is also shown that the proposed algorithm shows varying characteristics in balancing the passive beamforming gain, end-to-end path loss, and effective aperture gain among the users, depending on their dense or sparse geographic distributions.

It is worth noting that the relative locations of all reflecting elements of the AIRS keep unchanged in our proposed passive 6DMA, while they may also be altered to bring even more

![](images/d09e800fbdcbe59a6ab955e38389f56479d691ae4e190705c20d95da531180d6.jpg)  
Fig. 1. UAV-enabled passive 6DMA-assisted multicast system.

DoFs for performance enhancement [27], [28], [29], [30], [31], [32], [33], [34], [35], at the cost of increased sensitivity to aerial flutter.

The rest of this paper is organized as follows. Section II introduces the system model for the UAV-enabled passive 6DMA-aided multicast system and formulates the design problem. In Section III, we consider a simplified single-user case and show the optimality of 1D orientation, deriving its optimal solution in closed form. In Section IV, we propose an enhanced AO algorithm with GS to solve the max-min SNR problem in the general multi-user setup. Section V presents numerical results to evaluate the performance of our proposed algorithm. Section VI concludes the paper.

Notations: For a complex number s, symbols $\angle s , | s |$ , and $s ^ { * }$ denote its phase, amplitude, and conjugate, respectively. For a vector x, symbols $\mathbf { x } ^ { \hat { T } } , \mathbf { x } ^ { H } , \| \mathbf { x } \| , ( \mathbf { x } ) _ { n } ^ { \mathbf { \bar { \alpha } } }$ , and diag(x) denote its transpose, conjugate transpose, Euclidean norm, the n-th entry, and a diagonal matrix with its entries on the main diagonal, respectively. For a matrix $\mathbf { X } , \mathbf { X } [ m , n ]$ denotes the element on the m-th row and n-th column of X. Symbol $\mathbb { C } ^ { M \times N }$ denotes the set of $M \times N$ complex-valued matrices. For two sets A and $B , \ A \cup B$ denotes the union of $\mathcal { A }$ and B, and $\mathcal A \backslash B$ denotes the set of elements that belong to A but are not in B. The symbols $\varnothing , \otimes , \odot ,$ and $j$ denote the empty set, Kronecker product, Hadamard product, and the imaginary unit with $j ^ { 2 } =$ $^ { - 1 , }$ respectively.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

## A. System Model

As shown in Fig. 1, we consider the downlink transmission from a BS to $N _ { u }$ remote users aided by an AIRS. The direct links between the BS and users are assumed to be non-existent due to the severe path loss caused by large distances. Thanks to UAV’s flexible deployment and posture control as well as AIRS’s beamforming design, the phase shifts and location/orientation of the AIRS can be adaptively tuned to enhance the communication performance based on users’ locations. The BS is assumed to be equipped with a uniform linear array (ULA) with M antennas, while each user is equipped with a single antenna, and the users are distributed in a remote area A. In this paper, we focus on a coherent time slot to investigate the performance of our proposed algorithms taking into account user mobility. The AIRS deployment and passive beamforming are updated across different time slots.<sup>3</sup> In addition, to characterize the theoretical performance limit of the proposed scheme, we assume a relatively calm environment, such that aerial flutter can be effectively mitigated using various available techniques, such as a 3-axis gimbal equipped with active or passive damping mechanisms [17].

For convenience, we establish a global Cartesian coordinate system (CCS) in the considered system, assuming that the BS is located at the origin, i.e., $, \textbf { b } = ~ [ 0 , 0 , 0 ] ^ { T }$ . Let the coordinate of the l-th user be $\mathbf { w } _ { l } = [ w _ { l x } , \dot { w _ { l y } } , 0 ] ^ { T } , l \in \mathcal { N } _ { u } \triangleq$ $\{ 1 , 2 , \cdots , N _ { u } \}$ . The ULA at the BS is assumed to be parallel to the z-axis in the global CCS. In the presence of the UAVenabled orientation of the AIRS, to ease the computation of the angle information from the AIRS to the BS/users, we also define a local CCS at the AIRS which lies in its $x ^ { \prime } { - } y ^ { \prime }$ plane, as shown in Fig. 1. Without loss of generality, we select the bottom-left element of the AIRS as its reference element and denote its coordinate by $\mathbf { q } = [ q _ { x } , q _ { y } , H ] ^ { T }$ , where $q _ { x }$ and $q _ { y }$ denote its projection onto the x- and y-axis, respectively, with H denoting its altitude. The AIRS is assumed to be equipped with a uniform planar array (UPA) with $N \ = \ N _ { x } \times N _ { y }$ reflecting elements, where $N _ { x }$ and $N _ { y }$ denote the numbers of reflecting elements along the $x ^ { \prime } -$ and $y ^ { \prime }$ -axes of the local CCS, respectively. The distances between any two adjacent antennas and elements at the BS and the AIRS are denoted as $d _ { t x }$ and $d _ { r s } .$ , respectively.

The 3D orientation of the AIRS can be represented by $\psi =$ $[ \psi _ { z } , \psi _ { y } , \psi _ { x } ] ^ { T }$ , where $\psi _ { z } , \psi _ { y } ,$ , and $\psi _ { x }$ are Euler angles denoting the AIRS’s degree of orientation around $z ^ { \prime } \mathrm { , ~ } y ^ { \prime } \mathrm { - }$ , and $\boldsymbol { x } ^ { \prime } \mathrm { - } \mathrm { a x i s } .$ respectively. Then, the relationship between the global CCS and the local CCS is characterized by the following orientation matrix [36],

$$
\mathbf { Q } ( \psi ) = \mathbf { Q } _ { z } ( \psi _ { z } ) \mathbf { Q } _ { y } ( \psi _ { y } ) \mathbf { Q } _ { x } ( \psi _ { x } ) ,\tag{1}
$$

where $\mathbf { Q } _ { z } ( \psi _ { z } )$ indicates the orientation of $\psi _ { z }$ radians around the z-axis and is given by

$$
\begin{array} { r } { { \bf Q } _ { z } ( \psi _ { z } ) = \left[ \begin{array} { c c c } { \cos \psi _ { z } - \sin \psi _ { z } 0 } \\ { \sin \psi _ { z } \cos \psi _ { z } 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] , } \end{array}\tag{2}
$$

$\mathbf { Q } _ { y } ( \psi _ { y } )$ indicates the orientation of $\psi _ { y }$ radians around the $y -$ axis and is given by

$$
\mathbf { Q } _ { y } ( \psi _ { y } ) = \left[ \begin{array} { l l l } { \cos { \psi _ { y } } } & { 0 \sin { \psi _ { y } } } \\ { 0 } & { 1 } & { 0 } \\ { - \sin { \psi _ { y } } } & { 0 \cos { \psi _ { y } } } \end{array} \right] ,\tag{3}
$$

and $\mathbf { Q } _ { x } ( \psi _ { x } )$ indicates the orientation of $\psi _ { x }$ radians around the x-axis and is given by

$$
{ \bf Q } _ { x } ( \psi _ { x } ) = \left[ \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 \cos \psi _ { x } - \sin \psi _ { x } } } \\ { { 0 \sin \psi _ { x } } } & { { \cos \psi _ { x } } } \end{array} \right] .\tag{4}
$$

Based on (1), for any given 3D location p in the global CCS, its corresponding coordinates in the local CCS are given by [36]

$$
\mathbf { p } ^ { \mathrm { l o c a l } } = \mathbf { Q } ^ { T } ( \psi ) ( \mathbf { p } - \mathbf { q } ) .\tag{5}
$$

Obviously, we have $\mathbf { q } ^ { \mathrm { l o c a l } } \ = \ [ 0 , 0 , 0 ] ^ { T }$ , i.e., the reference element of the AIRS is at the origin of the local CCS. Moreover, the coordinate of the BS in the local CCS are given by

$$
{ \bf b } ^ { \mathrm { l o c a l } } = { \bf Q } ^ { T } ( \psi ) ( { \bf b } - { \bf q } ) = [ b _ { x } ^ { \mathrm { l o c a l } } , b _ { y } ^ { \mathrm { l o c a l } } , b _ { z } ^ { \mathrm { l o c a l } } ] ^ { T } ,\tag{6}
$$

and those of the users in the local CCS are

$$
\mathbf { w } _ { l } ^ { \mathrm { l o c a l } } = \mathbf { Q } ^ { T } ( \psi ) ( \mathbf { w } _ { l } - \mathbf { q } ) = [ w _ { l x } ^ { \mathrm { l o c a l } } , w _ { l y } ^ { \mathrm { l o c a l } } , w _ { l z } ^ { \mathrm { l o c a l } } ] ^ { T } , l \in \mathcal { N } _ { u } .\tag{7}
$$

Given the above local coordinates, we can define the angle of departure (AoD) from the BS to the AIRS, the elevation/azimuth angle of arrival (AoA) at the AIRS from the BS, and the elevation/azimuth AoD from the AIRS to user l as φ<sub>BA</sub>, $\vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } , \phi _ { A U , l } ^ { ( e ) }$ , and $\phi _ { A U , l } ^ { ( a ) }$ , respectively, which can be obtained based on geometry as

$$
\phi _ { B A } = \operatorname { a r c c o s } { \frac { H } { \lVert \mathbf { q } \rVert } } ,\tag{8}
$$

$$
\vartheta _ { A B } ^ { ( e ) } = \operatorname { a r c c o s } \frac { - b _ { z } ^ { \mathrm { l o c a l } } } { \left\| \mathbf { q } \right\| } , \qquad \vartheta _ { A B } ^ { ( a ) } = \arctan \frac { b _ { y } ^ { \mathrm { l o c a l } } } { b _ { x } ^ { \mathrm { l o c a l } } } ,\tag{9}
$$

$$
\phi _ { A U , l } ^ { ( e ) } = \operatorname { a r c c o s } \frac { w _ { l z } ^ { \mathrm { l o c a l } } } { \left\| \mathbf { w } _ { l } - \mathbf { q } \right\| } , \phi _ { A U , l } ^ { ( a ) } = \arctan \frac { w _ { l y } ^ { \mathrm { l o c a l } } } { w _ { l x } ^ { \mathrm { l o c a l } } } , l \in \mathcal { N } _ { u } .\tag{10}
$$

Unlike the isotropic signal reflection assumed in [19], we consider a more practical angle-dependent signal reflection model by taking into account the effective AIRS reflection aperture. To this end, we define $\phi _ { 1 } \ ( \phi _ { 2 , l } )$ as the incident angle (reflection angles) of the BS’s signal at the AIRS with respect to (w.r.t.) user $l , \ l \in \mathcal { N } _ { u }$ . Based on the above local coordinates, it is seen that

$$
\phi _ { 1 } = \operatorname { a r c c o s } \frac { - b _ { z } ^ { \mathrm { l o c a l } } } { \lVert \mathbf { q } \rVert } = \vartheta _ { A B } ^ { ( e ) } ,\tag{11}
$$

$$
\phi _ { 2 , l } = \operatorname { a r c c o s } \frac { - w _ { l z } ^ { \mathrm { l o c a l } } } { \lVert \mathbf { q } - \mathbf { w } _ { l } \rVert } = \pi - \phi _ { A U , l } ^ { ( e ) } .\tag{12}
$$

Notably, it must hold that $\phi _ { 1 } \in [ 0 , \frac { \pi } { 2 } ]$ and $\phi _ { 2 , l } \in [ 0 , \frac { \pi } { 2 } ]$ , ∀l ∈ $\mathcal { N } _ { u }$ to ensure that all users and the BS are located in the reflection space of the AIRS. By substituting (1)-(7) into (11) and (12), we have

$$
\cos { \phi _ { 1 } } = \frac { q _ { x } L _ { 1 } + q _ { y } L _ { 2 } + H L _ { 3 } } { \sqrt { q _ { x } ^ { 2 } + q _ { y } ^ { 2 } + H ^ { 2 } } } ,\tag{13}
$$

$$
\cos { \phi _ { 2 , l } } = \frac { ( q _ { x } - w _ { l x } ) L _ { 1 } + ( q _ { y } - w _ { l y } ) L _ { 2 } + H L _ { 3 } } { \sqrt { ( q _ { x } - w _ { l x } ) ^ { 2 } + ( q _ { y } - w _ { l y } ) ^ { 2 } + H ^ { 2 } } } ,\tag{14}
$$

where

$$
L _ { 1 } = \cos \psi _ { z } \sin \psi _ { y } \cos \psi _ { x } + \sin \psi _ { z } \sin \psi _ { x } ,\tag{15}
$$

$$
L _ { 2 } = \sin \psi _ { z } \sin \psi _ { y } \cos \psi _ { x } - \cos \psi _ { z } \sin \psi _ { x } ,\tag{16}
$$

$$
L _ { 3 } = \cos \psi _ { y } \cos \psi _ { x } .\tag{17}
$$

As such, the effective aperture gain due to the AIRS’s orientation w.r.t. user l can be expressed as [20]

$$
F _ { \mathrm { A G } , l } ( \mathbf { q } , \psi ) = \cos { \phi _ { 1 } } \cos { \phi _ { 2 , l } } , l \in \mathcal { N } _ { u } .\tag{18}
$$

It is noted that in the conventional isotropic reflection model, we have $F _ { \mathrm { A G } , l } = 1$ regardless of $\phi _ { 1 }$ and $\phi _ { 2 , l }$ . However, when $\phi _ { 1 }$ and/or $\phi _ { 2 , l }$ are close to $\frac { \pi } { 2 }$ , the effective aperture gain in (18) approaches zero.

In this paper, we assume that the UAV/AIRS’s altitude, H, is fixed at the minimum altitude satisfying free-space LoS propagation from the UAV to the BS/users (e.g., $H \geq 1 0 0$ meter (m) in the urban macro scenario [37]) to reduce the end-to-end path loss. In Section V, we will also evaluate the effects of the AIRS’s altitude on the overall performance via simulation. As such, the path gain from the BS to the AIRS can be expressed as $\begin{array} { r } { \beta _ { 1 } = \frac { \beta _ { 0 } ^ { * } } { \| \mathbf { q } \| ^ { 2 } } } \end{array}$ , and that from the AIRS to the user l is expressed as $\begin{array} { r } { \beta _ { 2 , l } = \frac { \beta _ { 0 } } { \| \mathbf { q } - \mathbf { w } _ { l } \| ^ { 2 } } , ~ l \in \mathcal { N } _ { u } } \end{array}$ , where $\beta _ { 0 }$ denotes the path gain at the reference distance of 1 m. Moreover, due to the practically high altitude of the UAV, we assume far-field propagation between the AIRS and the BS/users.

Hence, the channel from the BS to the AIRS is given by

$$
\mathbf { H } _ { B A } = \sqrt { \beta _ { 1 } } e ^ { - j \frac { 2 \pi \| \mathbf { q } \| } { \lambda } } \mathbf { a } _ { I } ( \vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } ) \mathbf { a } _ { B } ^ { H } ( \phi _ { B A } ) ,\tag{19}
$$

where ${ \bf a } _ { I } ( \vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } )$ and $\mathbf { a } _ { B } \left( \phi _ { B A } \right)$ represent the receive and transmit array response vectors at the AIRS and the BS, respectively, which can be expressed as

$$
\begin{array} { r l } & { \mathbf { a } _ { I } \big ( \vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } \big ) } \\ & { \ = \mathbf { a } _ { I x } \otimes \mathbf { a } _ { I y } } \\ & { \ = \left[ 1 , \cdots , e ^ { - j \frac { 2 \pi ( N _ { x } - 1 ) } { \lambda } d _ { r s } \sin ( \vartheta _ { A B } ^ { ( e ) } ) \cos ( \vartheta _ { A B } ^ { ( a ) } ) } \right] ^ { T } } \\ & { \ \otimes \left[ 1 , \cdots , e ^ { - j \frac { 2 \pi ( N _ { y } - 1 ) } { \lambda } d _ { r s } \sin ( \vartheta _ { A B } ^ { ( e ) } ) \sin ( \vartheta _ { A B } ^ { ( a ) } ) } \right] ^ { T } , } \end{array}\tag{20}
$$

and

$$
\mathbf { a } _ { B } ( \phi _ { B A } ) = \left[ 1 , e ^ { - j \frac { 2 \pi } { \lambda } d _ { t x } \cos \phi _ { B A } } , \cdot \cdot \cdot , e ^ { - j \frac { 2 \pi ( M - 1 ) } { \lambda } d _ { t x } \cos \phi _ { B A } } \right] ^ { T } .\tag{21}
$$

Similarly, the channel from the AIRS to user l can be given as

$$
\mathbf { h } _ { A U , l } ^ { H } = \sqrt { \beta _ { 2 , l } } e ^ { - j \frac { 2 \pi \| \mathbf { q } - \mathbf { w } _ { l } \| } { \lambda } } \mathbf { a } _ { 2 } ^ { H } \big ( \phi _ { A U , l } ^ { ( e ) } , \phi _ { A U , l } ^ { ( a ) } \big ) , l \in \mathcal { N } _ { u } ,\tag{22}
$$

where $\mathbf { a } _ { 2 } ( \phi _ { A U , l } ^ { ( e ) } , \phi _ { A U , l } ^ { ( a ) } )$ is the transmit array response vector at the AIRS and can be expressed as

$$
\begin{array} { r l } & { \mathbf { a } _ { 2 } ( \phi _ { A U , l } ^ { ( e ) } , \phi _ { A U , l } ^ { ( a ) } ) } \\ & { \mathbf { \Psi } = \mathbf { a } _ { 2 x , l } \otimes \mathbf { a } _ { 2 y , l } } \\ & { \mathbf { \Psi } = \left[ 1 , \cdots , e ^ { - j \frac { 2 \pi ( N _ { x } - 1 ) } { \lambda } d _ { r s } \sin ( \phi _ { A U , l } ^ { ( e ) } ) \cos ( \phi _ { A U , l } ^ { ( a ) } ) } \right] ^ { T } } \end{array}
$$

$$
\begin{array} { r } { \otimes \left[ 1 , \cdots , e ^ { - j \frac { 2 \pi ( N _ { y } - 1 ) } { \lambda } d _ { r s } \sin ( \phi _ { A U , l } ^ { ( e ) } ) \sin ( \phi _ { A U , l } ^ { ( a ) } ) } \right] ^ { T } . } \end{array}\tag{23}
$$

The received signal at user l can be expressed as

$$
y _ { l } = \mathbf { h } _ { A U , l } ^ { H } \Theta \mathbf { H } _ { B A } \mathbf { v } \sqrt { P F _ { \mathrm { A G } , l } ( \mathbf { q } , \psi ) } s + n _ { w } , l \in \mathcal { N } _ { u } ,\tag{24}
$$

where $\Theta = \mathrm { d i a g } ( e ^ { j \theta _ { 1 } } , \cdot \cdot \cdot , e ^ { j \theta _ { N } } )$ denotes the reflection matrix of the AIRS with $\theta _ { n }$ denoting the phase shift of the n-th reflecting element,<sup>4</sup> $\mathbf { v } \in \mathbb { C } ^ { M \times \bar { 1 } }$ is the transmit beamforming vector of the BS with unit-norm, $P$ and s denote the BS’s transmit power and symbol, respectively, and $n _ { w } \sim \mathcal { C N } ( 0 , \sigma ^ { 2 } )$

is the additive white Gaussian noise (AWGN) with $\sigma ^ { 2 }$ denoting the noise power. Thus, the received SNR of user l is

$$
\begin{array} { r l } & { \gamma _ { l } ( { \bf q } , \psi , \Theta , { \bf v } ) } \\ & { = \frac { P F _ { \mathrm { A G } , l } ( { \bf q } , \psi ) | { \bf h } _ { A U , l } ^ { H } \Theta { \bf H } _ { B A } { \bf v } | ^ { 2 } } { \sigma ^ { 2 } } } \\ & { = \frac { \bar { P } \beta _ { 0 } ^ { 2 } F _ { \mathrm { A G } , l } ( { \bf q } , \psi ) G _ { \mathrm { B F } , l } ( { \bf q } , \psi , \theta ) \left| { \bf a } _ { B } ^ { H } \left( \phi _ { B A } \right) { \bf v } \right| ^ { 2 } } { \| { \bf q } \| ^ { 2 } \| { \bf q } - { \bf w } _ { l } \| ^ { 2 } } , ~ l \in \mathcal { N } _ { u } , } \end{array}\tag{25}
$$

where $\begin{array} { r } { \bar { P } = \frac { P } { \sigma ^ { 2 } } } \end{array}$ , and

$$
\begin{array} { r l } & { G _ { \mathrm { B F } , l } ( \mathbf { q } , \psi , \pmb { \theta } ) } \\ & { \ = \left| \mathbf { a } _ { 2 } ^ { H } ( \phi _ { A U , l } ^ { ( e ) } , \phi _ { A U , l } ^ { ( a ) } ) \Theta \mathbf { a } _ { I } ( \vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } ) \right| ^ { 2 } = \left| \mathbf { f } _ { l } ^ { H } \pmb { \theta } \right| ^ { 2 } } \end{array}\tag{26}
$$

represents the passive beamforming gain at user l, where $\pmb \theta =$ $[ e ^ { \dot { j } \theta _ { 1 } } , \cdot \cdot \cdot , e ^ { j \theta _ { N } } ] ^ { T }$ and

$$
\begin{array} { r l } & { \mathbf { f } _ { l } = \mathbf { a } _ { 2 } \big ( \phi _ { A U , l } ^ { ( e ) } , \phi _ { A U , l } ^ { ( a ) } \big ) \odot \mathbf { a } _ { I } ^ { * } \big ( \vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } \big ) } \\ & { \quad = \big ( \mathbf { a } _ { 2 x , l } \otimes \mathbf { a } _ { 2 y , l } \big ) \odot \big ( \mathbf { a } _ { I x } ^ { * } \otimes \mathbf { a } _ { I y } ^ { * } \big ) } \\ & { \quad = \big ( \mathbf { a } _ { 2 x , l } \odot \mathbf { a } _ { I x } ^ { * } \big ) \otimes \big ( \mathbf { a } _ { 2 y , l } \odot \mathbf { a } _ { I y } ^ { * } \big ) } \\ & { \quad = \mathbf { f } _ { l x } \otimes \mathbf { f } _ { l y } . } \end{array}\tag{27}
$$

Note that as all users share a common BS-AIRS channel, to maximize the received SNR at any user l in (25), the optimal transmit beamforming vector is given by

$$
\mathbf { v } ^ { \mathrm { o p t } } = \frac { \mathbf { a } _ { B } ( \phi _ { B A } ) } { \| \mathbf { a } _ { B } ( \phi _ { B A } ) \| } = \frac { \mathbf { a } _ { B } ( \phi _ { B A } ) } { \sqrt { M } } .\tag{28}
$$

Substituting (28) into (25) yields

$$
\gamma _ { l } ( \mathbf { q } , \psi , \pmb { \theta } ) = \frac { \bar { P } \beta _ { 0 } ^ { 2 } M F _ { \mathrm { A G } , l } ( \mathbf { q } , \psi ) G _ { \mathrm { B F } , l } ( \mathbf { q } , \psi , \pmb { \theta } ) } { \| \mathbf { q } \| ^ { 2 } \| \mathbf { q } - \mathbf { w } _ { l } \| ^ { 2 } } .\tag{29}
$$

## B. Problem Formulation

The goal of this paper is to maximize the minimum received SNR among all users by jointly optimizing the AIRS’s location q, 3D orientation angles ψ, and phase shifts θ. Hence, the optimization problem can be formulated as

$$
\left( \mathrm { P 1 } \right) \operatorname* { m a x } _ { \mathbf { q } , \psi , \theta } \operatorname* { m i n } _ { l \in \mathcal { N } _ { u } } \gamma _ { l } ( \mathbf { q } , \psi , \pmb { \theta } )
$$

$$
{ \mathrm { s . t . ~ } } { \bf q } \in { \mathcal { Q } } ,\tag{30}
$$

$$
q _ { x } L _ { 1 } + q _ { y } L _ { 2 } + H L _ { 3 } \geq 0 ,\tag{31}
$$

$$
( q _ { x } - w _ { l x } ) L _ { 1 } + ( q _ { y } - w _ { l y } ) L _ { 2 } + H L _ { 3 } \geq 0 ,\tag{32}
$$

$$
| ( \theta ) _ { n } | = 1 ,\tag{33}
$$

where Q denotes the prescribed region for the AIRS’s movement. The constraints (31) and (32) are imposed to ensure that the BS and all users are located in the half-reflection plane of the AIRS, i.e., (13) and (14) must be positive. However, problem (P1) is a non-convex optimization problem with the design variables q, ψ and θ intricately coupled with each other. To gain useful insights into the proposed passive 6DMA, we first consider a simplified single-user scenario in Section III and then address the general multi-user scenario in Section IV.

Remark 1: It is worth noting that additional constraints can be incorporated into (P1) to limit the maximum rotational angle of the AIRS, e.g., 120<sup>◦</sup> for DJI Phantom 4 Pro V2.0 UAV [17]. However, the constraints in (31) and (32) have inherently prevented the AIRS’s rotational angle from becoming excessively large, as this may cause one or more terrestrial nodes to fall outside its reflection half-space. Based on our simulation results presented in Section V, the optimized rotational angles in the considered scenarios remain within practical limits.

Remark 2: In (P1), we assume that all required channel state information (CSI) is available at the UAV for optimization. Notably, the LoS-dominated UAV-ground channels are mainly determined by the locations of the BS, the UAV, and the users. While the locations of the BS and the UAV can be known a priori, the user locations need to be estimated in general via different localization and tracking techniques. With the rapid advancement of high-definition optical cameras, an efficient approach is to equip the UAV with such sensors to localize users and thereby infer the overall channel information.

Remark 3: In this paper, we focus on the deployment optimization of the UAV, which means that the UAV itself is stationary or quasi-static, rendering the Doppler effect at the AIRS side negligible. As for the Doppler effects caused by user mobility, it can be compensated for similarly as in terrestrial communications. For example, we can let the UAV transmit reference signal for the user to estimate the Doppler shift and then compensate for it in the signal reception. It is also worth noting that thanks to the high altitude of the UAV, the Doppler shift at the user side generally changes slowly, thus leading to sufficient time for its estimation.

Remark 4: In the high-mobility scenario, the deployment of the AIRS should be dynamically re-optimized based on the users’ time-varying locations to achieve optimal performance, which may lead to an outdated CSI issue. Nonetheless, as will be shown in Section V-E via simulation, this issue may only result in a marginal performance loss, as the high altitude of the UAV ensures that moderate variations in user positions induce negligible changes in UAV-user distances and angles.

## III. SINGLE-USER CASE

In this section, we focus on solving (P1) under the singleuser case with $N _ { u } = 1$ . Without loss of generality, we label the single user as user 0 and assume that it is located along the x-axis. As such, let $\mathbf { w } _ { 0 } = [ D , 0 , 0 ] ^ { T }$ denote its coordinate, where D denotes its distance with the BS. Furthermore, to reduce the end-to-end path loss and simplify the optimization, we further set $q _ { y } = 0$ for the AIRS in this section.<sup>5</sup>

## A. Optimal AIRS Reflection for Given Location and Orientation

In the case of a single user, the AIRS reflection should be designed to maximize the end-to-end channel power gain, i.e., $G _ { \mathrm { B F } , 0 } ( \mathbf { q } , \psi , \pmb { \theta } )$ . Thus, the optimal phase shift of the AIRS’s n-th reflecting element is given by

$$
\theta _ { n } = \angle \left( \mathbf { a } _ { 2 } ( \phi _ { A U , 0 } ^ { ( e ) } , \phi _ { A U , 0 } ^ { ( a ) } ) \right) _ { n } - \angle \left( \mathbf { a } _ { I } ( \vartheta _ { A B } ^ { ( e ) } , \vartheta _ { A B } ^ { ( a ) } ) \right) _ { n } ,\tag{34}
$$

<sup>5</sup>Notably, $q _ { y }$ can also be optimized by performing a similar algorithm as in Section IV. However, assuming a fixed $q _ { y }$ helps reveal more essential insights into the effects of the AIRS orientation, as will be shown later in this section.

![](images/ed5ac7fa63f81c82e9c1dac650d4d48f2eaecb81fc63ff0d564feb414827354e.jpg)  
Fig. 2. The end-to-end path loss versus AIRS’s location with $D = 5 0 0$ m.

![](images/e0c07888d7b35dd6d2b11be0b6b883ce97f43e37a8c26bb1fa06693d4c8d5a9e.jpg)  
Fig. 3. Effective aperture gain versus AIRS’s location with $\psi _ { z } = \psi _ { x } = 0$ and H = 300 m.

such that the signals reflected by all reflecting elements of the AIRS are in-phase at the user’s receiver. By noting $N _ { u } = 1$ and $q _ { y } = 0$ , (18) reduces to

$$
F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi ) = \frac { q _ { x } L _ { 1 } + H L _ { 3 } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } \frac { ( q _ { x } - D ) L _ { 1 } + H L _ { 3 } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } .\tag{35}
$$

By substituting (34) and (35) into (29), we have

$$
\gamma _ { 0 } ( q _ { x } , \psi ) = \frac { \bar { P } \beta _ { 0 } ^ { 2 } F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi ) M N ^ { 2 } } { [ q _ { x } ^ { 2 } + H ^ { 2 } ] [ ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } ] } .\tag{36}
$$

It is observed from (36) that the maximum received SNR depends on the end-to-end path loss as well as the effective aperture gain $F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi )$ , both of which are affected by the AIRS’s location, $q _ { x } .$ . To better illustrate the effect of $q _ { x }$ on them, we plot in Figs. 2 and 3 the end-to-end path loss and effective aperture gain versus $q _ { x }$ , respectively, with $\beta _ { 0 } = - 4 0 ~ \mathrm { d B }$

It is observed from Fig. 2 that there exists an optimal $q _ { x }$ such that the end-to-end path loss is minimized, and such an optimal location depends on the UAV’s altitude, H. As H is low/high, the optimal $q _ { x }$ will approach the end points/midpoint of the BS-user line, as also previously revealed in [19]. On the other hand, it is observed from Fig. 3 that there also exists an optimal $q _ { x }$ maximizing the effective aperture gain, which is affected by the orientation angles, e.g., $\psi _ { y } .$ . In particular, when $\psi _ { y } = - 2 0 ^ { \circ }$ , the optimal $q _ { x }$ may be even at the left hand side (LHS) of the BS, instead of the end points or midpoint of the BS-user segment. It is seen that the optimal $q _ { x }$ for minimizing the end-to-end path loss and maximizing the effective aperture gain may be different. In addition, the AIRS’s orientation angle will also affect the optimal $q _ { x }$ for maximizing the effective aperture gain. Thus, the AIRS’s location and orientation should be jointly optimized to balance the end-to-end path loss and effective aperture gain.

Given the user’s received SNR in (36), problem (P1) can be simplified as

$$
\begin{array} { r l } { ( \mathrm { P 2 } ) \underset { q _ { x } , \psi } { \operatorname* { m a x } } } & { \gamma _ { 0 } ( q _ { x } , \psi ) } \\ { \mathrm { s . t . } } & { q _ { x } L _ { 1 } + H L _ { 3 } \geq 0 , } \\ & { \qquad ( q _ { x } - D ) L _ { 1 } + H L _ { 3 } \geq 0 , } \\ & { q _ { x } \in \mathcal { Q } . } \end{array}
$$

However, problem (P2) is still difficult to be optimally solved due to the coupling between the location $q _ { x }$ and orientation ψ in the objective function. Although an optimal solution can be obtained by performing an exhaustive search over $q _ { x }$ and ψ, this incurs practically exorbitant complexity. Next, we will propose an efficient algorithm to solve (P2) optimally.

## B. Proposed Solution to (P2)

In this subsection, we first show that for any given AIRS’s location, its 1D orientation around the $y ^ { \prime } { \mathrm { - } } \mathrm { a x i s }$ suffices to achieve the optimal performance of 3D orientation, and then solve the resulting simplified optimization problem accordingly.

1) Optimality of AIRS’s 1D Orientation: To show the optimality of 1D orientation, we present the following proposition to first show the optimality of two-dimensional (2D) orientation.

Proposition 1: For any given AIRS’s 3D orientation $\psi _ { 3 \mathrm { D } } = $ $[ \psi _ { z } , \psi _ { y } , \psi _ { x } ] ^ { T }$ and location $q _ { x } ,$ , there always exists a 2D orientation solution $\psi _ { \mathrm { 2 D } } ^ { \star } = [ 0 , \psi _ { y } ^ { \star } , \psi _ { x } ^ { \star } ] ^ { T }$ , such that

$$
\gamma _ { 0 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) = \gamma _ { 0 } ( q _ { x } , \psi _ { \mathrm { 3 D } } ) .\tag{37}
$$

The detailed proof is provided in Appendix. Following the result in Proposition 1, we further show the optimality of 1D orientation in Proposition 2 below.

Proposition 2: For any given 2D orientation solution $ { \psi _ { \mathrm { 2 D } } } =$ $[ 0 , \psi _ { y } , \psi _ { x } ] ^ { T }$ and $q _ { x }$ , there always exists a 1D orientation solution $\begin{array} { r } { \dot { \psi } _ { 1 \mathrm { { D } } } ^ { \star } = [ 0 , \psi _ { y } ^ { \star } , 0 ] ^ { T } } \end{array}$ that satisfies

$$
\gamma _ { 0 } ( q _ { x } , \psi _ { \mathrm { 1 D } } ^ { \star } ) \geq \gamma _ { 0 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ) .\tag{38}
$$

Proof: Similar to the proof of Proposition 1, it is equivalent to prove $F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { \mathrm { 1 D } } ^ { \star } ) \geq F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { \mathrm { 2 D } } )$ , for which it suffices to prove cos $\phi _ { 1 } \big ( q _ { x } , \psi _ { \mathrm { 1 D } } ^ { \star } \big ) \ \geq$ cos $\phi _ { 1 } ( q _ { x } , \psi _ { 2 \mathrm { D } } )$ and cos $\phi _ { 2 , 0 } ( q _ { x } , \psi _ { 1 \mathrm { D } } ^ { \star } ) \geq$ cos $\phi _ { \mathrm { 2 , 0 } } ( q _ { x } , \psi _ { \mathrm { 2 D } } )$ . Note that

$$
\begin{array} { c } { \cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 1 D } } ^ { \star } ) = \frac { q _ { x } \sin \psi _ { y } ^ { \star } + H \cos \psi _ { y } ^ { \star } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } } \\ { \overset { \mathrm { ( a ) } } { \geq } \frac { \left( q _ { x } \sin \psi _ { y } ^ { \star } + H \cos \psi _ { y } ^ { \star } \right) \cos \psi _ { x } ^ { \star } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } } \\ { = \cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ) , } \end{array}\tag{39}
$$

$$
\begin{array} { c c c } { \cos \phi _ { 2 , 0 } ( q _ { x } , \psi _ { \mathrm { l D } } ^ { \star } ) = } & { \displaystyle \frac { ( q _ { x } - D ) \sin \psi _ { y } ^ { \star } + H \cos \psi _ { y } ^ { \star } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } } \\ { \displaystyle } & { \displaystyle \geq \frac { \left( ( q _ { x } - D ) \sin \psi _ { y } ^ { \star } + H \cos \psi _ { y } ^ { \star } \right) \cos \psi _ { x } ^ { \star } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } } \\ { = } & { \cos \phi _ { 2 , 0 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ) , } \end{array}\tag{40}
$$

where inequalities (a) and (b) hold in that $q _ { x } \sin \psi _ { y } ^ { \star } +$ H cos $\psi _ { y } ^ { \star } \geq 0$ and $( q _ { x } \mathrm { ~ - ~ } D )$ sin $\psi _ { y } ^ { \star } + H$ cos $\psi _ { y } ^ { \star } \geq 0$ due to the constraints in (P2) for effective signal reflection. Thus, the proof of Proposition 2 is completed. 

Proposition 2 suggests that only the 1D orientation around the $y ^ { \prime } { \mathrm { - a x i s } } ,$ i.e., $\psi _ { y }$ , is sufficient to achieve the maximum received SNR at the user. In this case, the effective aperture gain in (35) can be simplified as

$$
\begin{array} { c } { F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { y } ) = \displaystyle \frac { q _ { x } \sin \psi _ { y } + H \cos \psi _ { y } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } . } \\ { \displaystyle \frac { ( q _ { x } - D ) \sin \psi _ { y } + H \cos \psi _ { y } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } , } \end{array}\tag{41}
$$

and the user’s received SNR in (36) becomes

$$
\gamma _ { b } ( q _ { x } , \psi _ { y } ) = \frac { \bar { P } \beta _ { 0 } ^ { 2 } M N ^ { 2 } \sin { ( \psi _ { y } + \psi _ { 1 } ( q _ { x } ) ) } \sin { ( \psi _ { y } + \psi _ { 2 } ( q _ { x } ) ) } } { [ q _ { x } ^ { 2 } + H ^ { 2 } ] [ ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } ] } ,\tag{42}
$$

where

$$
\psi _ { 1 } ( q _ { x } ) = \operatorname { a r c c o s } \frac { q _ { x } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } ,\tag{43}
$$

$$
\psi _ { 2 } ( q _ { x } ) = \operatorname { a r c c o s } \frac { q _ { x } - D } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } .\tag{44}
$$

The formulated problem (P2) can be simplified as

$$
\begin{array} { r l } { ( \mathrm { P 3 } ) \underset { q _ { x } , \psi _ { y } } { \operatorname* { m a x } } } & { \gamma _ { b } ( q _ { x } , \psi _ { y } ) } \\ { \mathrm { s . t . } ~ q _ { x } \sin \psi _ { y } + H \cos \psi _ { y } \geq 0 , } \\ & { \left( q _ { x } - D \right) \sin \psi _ { y } + H \cos \psi _ { y } \geq 0 , } \\ & { ~ q _ { x } \in \mathcal { Q } . } \end{array}
$$

Based on (41) and (42), it is noted that without the AIRS orientation optimization, i.e., $\psi _ { y } = 0$ , we have $\gamma _ { b } ( q _ { x } , 0 ) =$ ¯ 2 2 2   
$\frac { \cdot ~ \mapsto ~ \mapsto ~ \dots ~ \dots ~ } { [ q _ { x } ^ { 2 } + H ^ { 2 } ] ^ { 3 / 2 } [ ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } ] ^ { 3 / 2 } }$ . In this case, the optimal $q _ { x }$ should be such that the end-to-end path loss is minimized, which is identical to the isotropic signal reflection as studied in [19], i.e.,

$$
\begin{array} { r } { q _ { x } ^ { \mathrm { i s o } } = \left\{ \begin{array} { l l } { \displaystyle \frac { D } { 2 } , } & { \mathrm { ~ i f ~ } 0 \leq \frac { D } { H } \leq 2 } \\ { \displaystyle \frac { D } { 2 } \pm \sqrt { \frac { D ^ { 2 } } { 4 } - H ^ { 2 } } , } & { \mathrm { ~ o t h e r w i s e . } } \end{array} \right. } \end{array}\tag{45}
$$

2) AIRS’s Optimal 1D Orientation for Any Given Location: For the simplified problem (P3), we have the following proposition that characterizes the optimal 1D orientation in terms of the AIRS’s location, $q _ { x }$

Proposition 3: For any given $q _ { x }$ in (P3), the optimal 1D orientation for (P3) is given by $\begin{array} { r } { \psi _ { y } ^ { \star } ( q _ { x } ) = \frac { \bar { \pi } - \psi _ { 1 } ( q _ { x } ) ^ { \star } - \psi _ { 2 } ( q _ { x } ) } { 2 } } \end{array}$

Proof: By exploiting the product-to-sum identities, (42) becomes

$$
\begin{array} { c } { { \gamma _ { b } ( q _ { x } , \psi _ { y } ) = \alpha _ { 0 } ( q _ { x } ) \Big [ \cos \left( \psi _ { 1 } ( q _ { x } ) - \psi _ { 2 } ( q _ { x } ) \right) } } \\ { { - \cos \left( 2 \psi _ { y } + \psi _ { 1 } ( q _ { x } ) + \psi _ { 2 } ( q _ { x } ) \right) \Big ] , } } \end{array}\tag{46}
$$

where $\begin{array} { r l r } { \alpha _ { 0 } ( q _ { x } ) } & { { } = } & { \frac { \bar { P } \beta _ { 0 } ^ { 2 } M N ^ { 2 } } { 2 \left[ q _ { x } ^ { 2 } + H ^ { 2 } \right] \left[ ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } \right] } } \end{array}$ . To maximize (46) for any $\mathrm { g i v e n } \quad q _ { x } ,$ , the optimal $\psi _ { y }$ should satisfy cos $\left( 2 { \psi } _ { y } ^ { \star } + { \psi } _ { 1 } ( q _ { x } ) + { \psi } _ { 2 } ( q _ { x } ) \right) = - 1$ , which results in

$$
\psi _ { y } ^ { \star } ( q _ { x } ) = \frac { \pi - \psi _ { 1 } ( q _ { x } ) - \psi _ { 2 } ( q _ { x } ) } { 2 } .\tag{47}
$$

This completes the proof.

The analytical optimal solution for 1D orientation in (47) reveals several interesting insights. Specifically, if the AIRS is located above the midpoint of the BS and the user, i.e., $q _ { x } =$ $\begin{array} { l } { { \frac { D } { 2 } } } \end{array}$ , we have $\psi _ { 1 } ( q _ { x } ) + \psi _ { 2 } ( q _ { x } ) = \pi$ by recalling (43) and (44), which results in $\psi _ { y } ^ { \star } ( q _ { x } ) = 0$ . This implies that no orientation is needed in this case. Interestingly, if the AIRS is sufficiently far from the BS/user, i.e., $q _ { x } \to \infty \ ( \mathrm { o r } \ - \infty )$ , we have $\psi _ { 1 } ( q _ { x } ) =$ $\psi _ { 2 } ( q _ { x } ) = 0 ~ ( \mathrm { o r } ~ \pi ) ~$ , which results in $\begin{array} { r } { \psi _ { y } ^ { \star } ( q _ { x } ) = \frac { \pi } { 2 } ~ ( \mathrm { o r } ~ - \frac { \pi } { 2 } ) } \end{array}$ It is also worth noting that $\begin{array} { r } { \psi _ { y } ^ { \star } \left( \frac { D } { 2 } + \delta _ { q } \right) = \psi _ { y } ^ { \star } \left( \frac { \tilde { D } } { 2 } - \delta _ { q } \right) } \end{array}$ for any $\delta _ { q } > 0$ , which implies that the optimal AIRS’s orientation angle is symmetric to $\begin{array} { r } { q _ { x } = \frac { D } { 2 } } \end{array}$

3) AIRS’s Optimal Location: By substituting the optimal $\psi _ { y }$ in (47) into (P3), we obtain the following single scalarvariable optimization problem w.r.t. $q _ { x } ,$ , i.e.,

$$
( \mathrm { P 4 } ) \operatorname* { m a x } _ { q _ { x } } \gamma _ { c } ( q _ { x } ) , \mathrm { s . t . } q _ { x } \in \mathcal { Q } ,
$$

where

$$
\gamma _ { c } ( q _ { x } ) = \frac { \bar { P } \beta _ { 0 } ^ { 2 } M N ^ { 2 } \left[ 1 + \cos \left( \psi _ { 1 } ( q _ { x } ) - \psi _ { 2 } ( q _ { x } ) \right) \right] } { 2 \left[ q _ { x } ^ { 2 } + H ^ { 2 } \right] \left[ ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } \right] } .\tag{48}
$$

It is noted from (48) that the ${ \bf A I R S } ^ { \prime } { \bf s }$ orientation mainly affects the user’s received SNR through the term $1 ~ +$ cos $( \psi _ { 1 } ( q _ { x } ) - \psi _ { 2 } ( q _ { x } ) )$ . To gain more insights, we investigate the following special cases.

First, in the case of a terrestrial IRS with $H  0 ,$ we have $\psi _ { 1 } ( q _ { x } ) = \psi _ { 2 } ( q _ { x } ) = 0$ based on (43) and (44), and thus $1 +$ cos $( \psi _ { 1 } ( q _ { x } ) - \psi _ { 2 } ( q _ { x } ) )$ can obtain its maximum value of 2. As a result, the optimal $q _ { x }$ should be such that the end-to-end path loss, i.e., the denominator of (48), is minimized, which is given by $q _ { x } ^ { \star } = 0$ or D. In this case, the optimal orientation angle for the terrestrial IRS is always $\begin{array} { r } { \psi _ { y } ^ { \star } ( q _ { x } ) = \pm \frac { \pi } { 2 } } \end{array}$ based on (47), which is consistent with the result presented in [23].

On the other hand, if the AIRS’s altitude is sufficiently high, i.e., $H \to \infty$ , we have $\begin{array} { r } { \psi _ { 1 } ( q _ { x } ) = \psi _ { 2 } ( q _ { x } ) = \frac { \pi } { 2 } } \end{array}$ , and the optimal $q _ { x }$ is given by $\begin{array} { r } { q _ { x } ^ { \star } = \frac { D } { 2 } } \end{array}$ , similar to the isotropic reflection in (45). However, in this case, the AIRS’s optimal orientation angle is given by $\psi _ { y } ^ { \star } ( q _ { x } ^ { \star } ) = 0$ . This implies that optimizing the AIRS’s orientation can barely bring performance gain, which is expected as the AIRS may be treated as a point in this case due to its extremely far distance with the ground.

Finally, if the BS and the user are sufficiently close, i.e., $\begin{array} { r l } { D } & { { }  \quad 0 , } \end{array}$ we have $\begin{array} { r c l } { \psi _ { 1 } ( q _ { x } ) } & { = } & { \psi _ { 2 } ( q _ { x } ) } \end{array}$ and 1 + cos $( \psi _ { 1 } ( q _ { x } ) - \psi _ { 2 } ( q _ { x } ) ) = 2 .$ As a result, the AIRS’s optimal location should minimize the end-to-end path loss, which is given by $q _ { x } ^ { \star } = 0$ . Note that this also results in $\psi _ { 1 } ( q _ { x } ) =$ $\begin{array} { r } { \psi _ { 2 } ( q _ { x } ) = \frac { \pi } { 2 } } \end{array}$ , and $\psi _ { y } ^ { \star } ( q _ { x } ^ { \star } ) = 0$ , implying that $D  0$ shows similar trend to $H  \infty$

However, in other general cases with an arbitrary H or D, (48) is a highly non-convex function w.r.t. $q _ { x } ,$ making it difficult to obtain its optimal solution in closed form.

![](images/172b135cfff142ae0b0d23be6e46f4b556b77dfce1f573a300d65308579df5f7.jpg)  
Fig. 4. Schematic diagram of the hybrid grained search.

Hence, we apply an exhaustive search over Q to obtain the optimal $q _ { x }$

In summary, the single-user case provides fundamental insights into the effects of AIRS rotation on wireless communication performance. These insights serve as a theoretical foundation to tackle the general multi-user scenario, where additional trade-offs among multiple users need to be reconciled, as will be studied in the next section.

## IV. GENERAL MULTI-USER CASE

In this section, we aim to solve (P1) in the general multi-user case with $N _ { u } ~ > ~ 1$ . To this end, we propose an AO algorithm to decouple it into three sub-problems w.r.t. the AIRS’s location q, orientation $\psi ,$ , and phase shifts θ, respectively, as presented in Section IV-A. To avoid the local convergence issue of the AO algorithm, an enhanced AO algorithm is also proposed by applying the GS in Section IV-B.

## A. AO Algorithm Without GS

Consider the jth iteration of the AO algorithm and denote the initial values of the ${ \bf A R S } ^ { \prime } { \bf s }$ location, orientation, and phase shifts as $\mathbf { q } ^ { ( j - 1 ) } , \psi ^ { ( j - 1 ) }$ and $\pmb { \theta } ^ { ( j - 1 ) }$ , respectively.

1) Location Optimization With Given AIRS Orientation and Phase Shifts: In this case, (P1) is simplified as

$$
\begin{array} { r l } & { ( \mathrm { P l . 1 } ) \underset { \mathbf { q } } { \operatorname* { m a x } } \underset { l \in \mathcal { N } _ { u } } { \operatorname* { m i n } } \ \gamma _ { l } \left( \mathbf { q } , \psi ^ { ( j - 1 ) } , \pmb \theta ^ { ( j - 1 ) } \right) } \\ & { \mathrm { s . t . } \ \mathbf { q } \in \mathcal { Q } . } \end{array}\tag{49}
$$

Problem (P1.1) is still a non-convex optimization problem w.r.t. the AIRS’s location q. One straightforward approach is by discretizing the space Q and searching for the optimal location of the AIRS among the sampling points. However, this results in practically high computational complexity, especially in the case of a high sampling resolution to improve the searching accuracy. To properly balance the complexity and performance, we propose a 2D hybrid coarse- and fine-grained search strategy to optimize q, as depicted in Fig. 4(a).

Specifically, Q is first uniformly divided into $\bar { N } _ { x } \times \bar { N } _ { y }$ rectangular sub-regions along the x- and y-axes, respectively, where $\hat { N } _ { x }$ and $\bar { N } _ { y }$ denote the numbers of the sampling points along x- and y-axes, respectively. As such, there exist $N _ { \mathrm { t o t } } = \bar { N } _ { x } \times \bar { N } _ { y }$ sub-regions in total. Denote by ${ \bf q } _ { n } \in \mathfrak { Q }$ the center of the n-th sub-region, with $1 \leq n \leq N _ { \mathrm { t o t } }$ . Then, the minimum received SNR among all users if the AIRS is deployed above ${ \bf q } _ { n }$ can be expressed as

$$
\gamma _ { \mathrm { m i n } } \left( \mathbf { q } _ { n } , \psi ^ { ( j - 1 ) } , \pmb \theta ^ { ( j - 1 ) } \right) = \operatorname* { m i n } _ { l \in \mathcal { N } _ { u } } \ \gamma _ { l } \left( \mathbf { q } _ { n } , \psi ^ { ( j - 1 ) } , \pmb \theta ^ { ( j - 1 ) } \right) .\tag{50}
$$

Among the $N _ { \mathrm { t o t } }$ sub-regions, we denote $\mathbf { q } _ { n ^ { * } }$ as the best center that achieves the highest minimum received SNR among all centers, with

$$
n ^ { * } = \arg \operatorname* { m a x } _ { 1 \leq n \leq N _ { \mathrm { t o t } } } \gamma _ { \mathrm { m i n } } \left( \mathbf { q } _ { n } , \psi ^ { ( j - 1 ) } , \theta ^ { ( j - 1 ) } \right) .\tag{51}
$$

Note that the sampling resolution in the above searching can be set relatively low to quickly determine the sub-region in (51). Next, a finer-grained search within the $n ^ { * }$ -th sub-region is conducted by discretizing it into a multitude of sampling points, as shown in Fig. 4(a). Let $N _ { x , n ^ { * } }$ ∗ and $N _ { y , n ^ { * } }$ ∗ denote the number of sampling points along x- and y-axes within the $n ^ { * }$ -th sub-region. As such, there are $N _ { \mathrm { t o t } , n ^ { * } } = N _ { x , n ^ { * } } \times N _ { y , n ^ { * } }$ sampling points in the $n ^ { * } { \mathrm { - } } { \mathrm { t h } }$ sub-region, and we denote by $\mathbf { q } _ { n ^ { * } } ^ { ( m ) } \in \mathcal { Q }$ the coordinate of the m-th sampling point in it. Then, the optimized AIRS location in the j-th AO iteration can be obtained as

$$
\begin{array} { l } { \displaystyle { \mathbf { q } ^ { ( j ) } } } \\ { = \displaystyle { \mathbf { q } _ { n ^ { * } } ^ { ( m ^ { \star } ) } } , m ^ { \star } = \arg \operatorname* { m a x } _ { 1 \leq m \leq N _ { \mathrm { t o t } , n ^ { * } } } \gamma _ { \mathrm { m i n } } \left( \mathbf { q } _ { n ^ { * } } ^ { ( m ) } , \psi ^ { ( j - 1 ) } , \pmb { \theta } ^ { ( j - 1 ) } \right) . } \end{array}\tag{52}
$$

2) Orientation Optimization With Given AIRS Location and Phase Shifts: Next, the sub-problem of AIRS orientation optimization can be formulated as

$$
\begin{array} { r l r } & { \left( \mathrm { P 1 . 2 } \right) \underset { \psi } { \operatorname* { m a x } } \underset { l \in \mathcal { N } _ { u } } { \operatorname* { m i n } } \ \gamma _ { l } \left( \mathbf { q } ^ { ( j ) } , \psi , \pmb { \theta } ^ { ( j - 1 ) } \right) } & \\ & { \mathrm { s . t . } \ q _ { x } ^ { ( j ) } L _ { 1 } + q _ { y } ^ { ( j ) } L _ { 2 } + H L _ { 3 } \geq 0 , } & { \left( 5 3 \right) } \\ & { } & { \left( q _ { x } ^ { ( j ) } - w _ { l x } \right) L _ { 1 } + \left( q _ { y } ^ { ( j ) } - w _ { l y } \right) L _ { 2 } + H L _ { 3 } \geq 0 , } \end{array}\tag{54}
$$

where $[ q _ { x } ^ { ( j ) } , q _ { y } ^ { ( j ) } , H ] ^ { T } \ = \ \mathbf { q } ^ { ( j ) }$ . Unlike the single-user case, problem (P1.2) is difficult to be optimally solved, since the optimal AIRS needs to cater to the SNRs at multiple users at the same time. To tackle the issue, we apply a similar hybrid coarse- and fine-grained searching method as in AIRS position optimization.

Specifically, we uniformly partitioned the angular interval $[ - \pi / 2 , \pi / 2 ]$ around $z ^ { \prime } { \bar { \cdot } } , \ y ^ { \prime } { \bar { \cdot } } , \ \bar { x ^ { \prime } }$ -axes into $\tilde { N } _ { z } , \ \tilde { N } _ { y } .$ , and $\tilde { N } _ { x }$ segments, respectively, which give rise to $\tilde { N } _ { \mathrm { t o t } } = \tilde { N } _ { z } { \times } \tilde { N } _ { y } { \times } \tilde { N } _ { x }$ cuboid in total, as shown in Fig. 4(b). Denote by $\psi _ { m } = $ $[ \tilde { \psi } _ { z } , \tilde { \psi } _ { y } , \tilde { \psi } _ { x } ] ^ { T }$ the center of the m-th cuboid, with $1 \leq m \leq$ $N _ { \mathrm { t o t } }$ , where

$$
\begin{array} { r l } & { \tilde { \psi } _ { z } = \frac { \pi ( 2 n _ { z } + 1 - \tilde { N } _ { z } ) } { 2 \tilde { N } _ { z } } , n _ { z } = \left\lfloor m / ( \tilde { N } _ { y } \tilde { N } _ { x } ) \right\rfloor , } \\ & { \tilde { \psi } _ { y } = \frac { \pi ( 2 n _ { y } + 1 - \tilde { N } _ { y } ) } { 2 \tilde { N } _ { y } } , n _ { y } = \left\lfloor \left( m - n _ { z } ( \tilde { N } _ { y } \tilde { N } _ { x } ) \right) / \tilde { N } _ { x } \right\rfloor , } \\ & { \tilde { \psi } _ { x } = \frac { \pi ( 2 n _ { x } - 1 - \tilde { N } _ { x } ) } { 2 \tilde { N } _ { x } } , n _ { x } = m - n _ { z } \left( \tilde { N } _ { y } \tilde { N } _ { x } \right) - n _ { y } \tilde { N } _ { x } , } \end{array}
$$

where $\lfloor \cdot \rfloor$ denotes the largest integer that is no larger than its argument. Among them, we denote $\psi _ { m ^ { * } }$ as the best cuboid center that achieves the highest minimum received SNR among all centers, with

$$
m ^ { * } = \arg \operatorname* { m a x } _ { 1 \leq m \leq \tilde { N } _ { \mathrm { t o t } } } \gamma _ { \mathrm { m i n } } \left( \mathbf { q } ^ { ( j ) } , \psi _ { m } , \pmb { \theta } ^ { ( j - 1 ) } \right) .\tag{55}
$$

Next, a finer-grained search within the $m ^ { * } { \bf - } { \mathrm { t h } }$ cuboid is conducted by further discretizing it into a multitude of sampling points, as shown in Fig. 4(b). Let $\tilde { N } _ { z , m ^ { * } } , \tilde { N } _ { y , m ^ { * } }$ , and $\tilde { N } _ { x , m ^ { * } }$ denote the number of sampling angles of $\psi _ { z } , \ \psi _ { y } ,$ , and $\psi _ { x }$ within the m<sup>∗</sup>-th cuboid, respectively. As such, there are $\tilde { N } _ { \mathrm { t o t } , m ^ { * } } = \tilde { N } _ { z , m ^ { * } } \times \tilde { N } _ { y , m ^ { * } } \times \tilde { N } _ { x , m ^ { * } }$ sampling points in the $m ^ { * } .$ th cuboid, and we denote by $\psi _ { m ^ { * } } ^ { ( n ) }$ the coordinate of the n-th sampling point in it. Then, the optimized AIRS orientation in the j-th AO iteration can be obtained as

$$
\psi ^ { ( j ) } = \psi _ { m ^ { * } } ^ { ( n ^ { * } ) } , \mathrm { ~ } n ^ { \star } = \arg \operatorname* { m a x } _ { 1 \leq n \leq \tilde { N } _ { \mathrm { t o t } , m ^ { * } } } \gamma _ { \operatorname* { m i n } } \left( \mathbf { q } ^ { ( j ) } , \psi _ { m ^ { * } } ^ { ( n ) } , \pmb { \theta } ^ { ( j - 1 ) } \right) .\tag{56}
$$

3) Phase Shift Optimization With Given AIRS Location and Orientation: Finally, the sub-problem of AIRS phase-shift optimization is given by

$$
\begin{array} { r l } & { ( \mathrm { P 1 . 3 } ) \underset { \pmb { \theta } } { \operatorname* { m a x } } \underset { l \in \mathcal { N } _ { u } } { \operatorname* { m i n } } \gamma _ { l } \left( \mathbf { q } ^ { ( j ) } , \psi ^ { ( j ) } , \pmb { \theta } \right) } \\ & { \mathrm { s . t . } | ( \pmb { \theta } ) _ { n } | = 1 , n = 1 , 2 , \cdots , N . } \end{array}\tag{57}
$$

Problem (P1.3) is similar to conventional IRS-aided multicast as studied in e.g., [39] and [40]. However, as the AIRS is generally equipped with a larger number of reflecting elements than its terrestrial counterparts, the existing methods, $\mathrm { e . g . }$ semi-definite relaxation (SDR), may result in excessively high computational complexity. To address this difficulty, we further decouple problem (P1.3) into two sub-problems corresponding to the horizontal and vertical passive beamforming of the AIRS along the $x ^ { \prime } -$ and $y ^ { \prime } .$ -axes, respectively, and solve them alternately. Let $\theta _ { x }$ and $\theta _ { y }$ denote the horizontal and vertical AIRS passive beamforming, respectively, with $\theta = \theta _ { x }$ ⊗ $\theta _ { y } .$ By noting $\mathbf { f } _ { l x }$ and $\mathbf { f } _ { l y }$ in (27), the received SNR in (29) can be re-expressed in terms of $\theta _ { x }$ and $\theta _ { y }$ as

$$
\gamma _ { l } \left( { \bf q } ^ { ( j ) } , \psi ^ { ( j ) } , \pmb { \theta } \right) = \frac { \bar { P } \beta _ { 0 } ^ { 2 } M F _ { \mathrm { A G } , l } ( { \bf q } ^ { ( j ) } , \psi ^ { ( j ) } ) | { \bf f } _ { l x } ^ { H } \pmb { \theta } _ { x } | ^ { 2 } | { \bf f } _ { l y } ^ { H } \pmb { \theta } _ { y } | ^ { 2 } } { \| { \bf q } ^ { ( j ) } \| ^ { 2 } \| { \bf q } ^ { ( j ) } - { \bf w } _ { l } \| ^ { 2 } } .\tag{58}
$$

For any given vertical passive beamforming $\theta _ { y }$ and by discarding irrelevant constant terms, it can be shown that the horizontal passive beamforming design can be formulated as

$$
\begin{array} { r l } & { \frac { \ d } { \ d t } ( \mathsf { P } 1 . 3 x ) \underset { \theta _ { x } } { \operatorname* { m a x } } \underset { l \in \mathcal { N } _ { u } } { \operatorname* { m i n } } \alpha _ { l } \vert \mathbf { f } _ { l x } ^ { H } \pmb { \theta } _ { x } \vert ^ { 2 } } \\ & { \qquad \mathrm { s . t . } \left. ( \pmb { \theta } _ { x } ) _ { n } \right. = 1 , n = 1 , 2 , \cdots , N _ { x } , } \end{array}\tag{59}
$$

where

$$
\alpha _ { l } = \sqrt { \frac { \frac { F _ { \mathrm { A G } , l } ( \mathbf { q } ^ { ( j ) } , \boldsymbol { \psi } ^ { ( j ) } ) } { \| \mathbf { q } ^ { ( j ) } - \mathbf { w } _ { l } \| ^ { 2 } } } { \sum _ { l = 1 } ^ { N _ { u } } \frac { F _ { \mathrm { A G } , l } ( \mathbf { q } ^ { ( j ) } , \boldsymbol { \psi } ^ { ( j ) } ) } { \| \mathbf { q } ^ { ( j ) } - \mathbf { w } _ { l } \| ^ { 2 } } } } , l \in \mathcal { N } _ { u } ,\tag{60}
$$

is a normalized constant expression depending on $\mathbf { q } ^ { ( j ) }$ and $\boldsymbol { \psi } ^ { ( j ) }$ . By introducing an epigraph auxiliary variable $\delta ,$ (P1.3x) can be recast as

$$
\operatorname* { m a x } _ { \theta _ { x } } ~ \delta\tag{61}
$$

$$
\begin{array} { r } { \mathrm { s . t . } \alpha _ { l } \big | { \mathbf f } _ { l x } ^ { H } { \pmb \theta } _ { x } \big | ^ { 2 } \geq \delta , l \in \mathcal N _ { u } , } \end{array}\tag{62}
$$

$$
\left| ( \pmb \theta _ { x } ) _ { n } \right| = 1 , n = 1 , 2 , \cdots , N _ { x } .\tag{63}
$$

However, (62) and (63) are both non-convex constraints. To recast (63) into a convex form, we first lift the beamforming vector $\theta _ { x }$ to a positive semi-defined (PSD) matrix ${ \textbf { \textsf { W } } } \in$ $\mathbb { C } ^ { N _ { x } \times N _ { x } }$ , with $\begin{array} { r } { \dot { \bf W } = \pmb { \theta } _ { x } \pmb { \theta } _ { x } ^ { H } } \end{array}$ being a rank-one matrix. Due to the matrix lifting, we recast (62) into a convex form using auto-correlation function as [40]

$$
\left. \mathbf { f } _ { l x } ^ { H } \pmb { \theta } _ { x } \right. ^ { 2 } = \operatorname { R e } \left( \mathbf { f } _ { l x } ^ { H } \mathbf { r } _ { x } \right) ,\tag{64}
$$

where the auto-correlation vector is defined as

$$
\begin{array} { l } { { \displaystyle ( { \bf r } _ { x } ) _ { 1 } = \sum _ { k = 1 } ^ { N _ { x } } ( { \pmb \theta } _ { x } ) _ { k } ( { \pmb \theta } _ { x } ^ { * } ) _ { k } = N _ { x } } , \qquad ( } \\ { { \displaystyle ( { \bf r } _ { x } ) _ { n } = 2 \sum _ { k = 1 } ^ { N _ { x } - n + 1 } { \bf W } [ k + n - 1 , k ] } , n = 2 , 3 , \cdots , N _ { x } . } \end{array}\tag{65}
$$

(66)

Taking (64)-(66) into account, (62) and (63) can be equivalently recast as

$$
\alpha _ { l } \mathbf { R e } \left( \mathbf { f } _ { l x } ^ { H } \mathbf { r } _ { x } \right) \geq \delta , ~ l \in \mathcal { N } _ { u } ,\tag{67}
$$

$$
| \mathbf { W } [ n , n ] | = 1 , n = 1 , 2 , \cdots , N _ { x } ,\tag{68}
$$

$$
\operatorname { r a n k } ( \mathbf { W } ) = 1 .\tag{69}
$$

However, (69) is still non-convex. To handle this issue, a penalty strategy is used to incorporate (69) into the objective function (61). To be specific, for a PSD matrix W with $\mathrm { T r } ( \mathbf { W } ) > 0$ , (69) is equivalent to

$$
\| \mathbf { W } \| _ { * } - \| \mathbf { W } \| _ { 2 } = 0 ,\tag{70}
$$

where $\left\| \mathbf { W } \right\| ,$ <sub>∗</sub> represents the nuclear norm, and $\lVert \mathbf { W } \rVert _ { 2 }$ is the spectral norm. Taking (70) as the penalty term for rank-one matrix, (61) can be expressed as

$$
\operatorname* { m a x } _ { \mathbf { W } } ~ \delta - \rho ( \| \mathbf { W } \| _ { * } - \| \mathbf { W } \| _ { 2 } ) ,\tag{71}
$$

where $\rho > 0$ is a pre-defined penalty parameter. Although (71) is still non-convex, the successive convex approximation (SCA) technique can be utilized to successively approach (71) with the first-order Taylor expansion at different local points. Specifically, in the kth SCA iteration, problem (P1.3x) can be expressed as

$$
\begin{array} { r l } & { \displaystyle \operatorname* { m a x } _ { \mathbf { W } } ~ \delta - \rho \bigg ( \| \mathbf { W } \| _ { * } - \bigg ( \| \mathbf { W } ^ { k } \| _ { 2 } } \\ & { ~ + \operatorname { R e } \big ( \mathrm { T r } \big ( ( \partial _ { \mathbf { W } ^ { k } } \| \mathbf { W } \| _ { 2 } ) ( \mathbf { W } - \mathbf { W } ^ { k } ) ) \big ) \bigg ) \bigg ) } \\ & { \mathrm { s . t . ~ } ( 6 5 ) , ~ ( 6 6 ) , ~ ( 6 7 ) , ~ ( 6 8 ) , } \end{array}\tag{72}
$$

where $\mathbf { W } ^ { k }$ represents the local value of W in the kth SCA iteration, and the sub-gradient can be efficiently computed as $\partial _ { \mathbf { W } ^ { k } } \| \mathbf { W } \| _ { 2 } = \mathbf { s } \mathbf { s } ^ { H }$ , with s denoting the singular vector corresponding to the largest singular value of $\mathbf { W } ^ { \overline { { k } } }$ . The SCA proceeds until the objective values output by two adjacent iterations is smaller than a pre-defined threshold, or the number of iterations reaches a pre-defined value. Note that $\mathbf { W } ^ { k }$ is initialized as an all-zero matrix in this paper.

Upon the convergence of the SCA algorithm, the optimized horizontal AIRS passive beamforming can be obtained by performing the singular value decomposition (SVD) on the converged value of W as $\theta _ { x } ^ { ( j ) }$ . Similarly to the above SCA procedures, we can obtain the SCA-optimized AIRS vertical passive beamforming as $\theta _ { y } ^ { ( j ) }$ <sup>)</sup>, for which the details are omitted for brevity. Finally, the optimized AIRS passive beamforming in the j-th AO iteration can be obtained as

![](images/794cdf751ff72337c14c5568fb5e195bbe0ee85476f6de2c961f346ed8de8813.jpg)  
Fig. 5. Schematic diagram of the proposed enhanced AO algorithm with GS.

$$
\pmb { \theta } ^ { ( j ) } = \pmb { \theta } _ { x } ^ { ( j ) } \otimes \pmb { \theta } _ { y } ^ { ( j ) } .\tag{73}
$$

The AO algorithm then proceeds to the $( j + 1 )$ -th iteration. Since this gives rise to non-decreasing objective value of (P1), the convergence can always be achieved [41].

## B. Enhanced AO With GS

Although the AO algorithm proposed in the last subsection is generally effective to solve (P1), its ultimate performance may be locally optimal and even get trapped at an undesirable sub-optimal solution, especially for a max-min optimization problem [40]. To tackle the challenge, we propose an enhanced AO algorithm with GS phases in optimizing the AIRS’s location and orientation [42], [43], as depicted in Fig. 5. Its basic idea is to explore nearby solutions around the solution obtained by solving (52) and (56) or jump to farther solutions with significantly different location and/or orientation via random selection. Note that the operations involved in the GS are conducted via a probability-based Markov chain. This offers two major benefits: exploring nearby solutions enhances the stability of the max-min received SNR, while the random selection mitigates the risk of being stuck by low-quality local optima.

Mathematically, consider the end of the j-th AO iteration with $\pmb \theta = \pmb \theta ^ { ( j ) }$ . Let $\mathbf { u } = \{ \mathbf { q } , \psi \}$ denote the set of candidate location and orientation solutions with $\mathbf { u } \in { S }$ , where S denotes the set of all candidate location and orientation solutions in the GS. To generate S, we equally partition the feasible space of the associated optimization variables $( \mathrm { i . e . , ~ } q _ { x } , q _ { y } , \psi _ { z } , \psi _ { y } ,$ , and $\psi _ { x } )$ into several sub-regions. The users’ minimum received SNR at u can be expressed as

$$
\gamma _ { \mathrm { m i n } } ( \mathbf { u } ) = \operatorname* { m i n } _ { l \in \mathcal { N } _ { u } } \ \gamma _ { l } \left( \mathbf { u } , \pmb { \theta } ^ { ( j ) } \right) .\tag{74}
$$

Let $\Delta _ { q }$ and $\Delta _ { \psi }$ denote the spacing between any two adjacent location variables $( \mathrm { i . e . , ~ } q _ { x }$ and $q _ { y } )$ and that between two adjacent orientation variables $( \mathrm { i } . \mathrm { e } . , \psi _ { z } , \psi _ { y }$ , and $\psi _ { x } )$ after the space partitioning, respectively.

Each GS phase commences at the end of each AO iteration after solving the sub-problem (P1.3) for AIRS passive beamforming, consisting of T iterations. Consider its t-th iteration and let $\mathbf u ( t - 1 )$ denote the optimized solution of u in the $( t - 1 )$ -th iteration, with ${ \bf u } ( t - \mathrm { 1 } ) = \{ { \bf q } ^ { t - 1 } , \psi ^ { t - 1 } \} =$ $\left\{ [ q _ { x } ^ { t - 1 } , q _ { y } ^ { \dot { t } - 1 } , \dot { H } ] ^ { T } , [ \psi _ { z } ^ { t - 1 } , \psi _ { y } ^ { t - 1 } , \psi _ { x } ^ { t - 1 } ] ^ { T } \right\}$ . In each GS iteration, we select a fixed number of candidate solutions for exploration, denoted as I, which is much smaller than the total number of candidate solutions in S. In particular, we calculate the minimum SNRs achievable by the I selected candidate locations based on (74). Let ${ \bf { u } } _ { i } ( t )$ denote the i-th candidate solution in the t-th GS iteration, $i = 1 , 2 , \cdots , I .$ The I candidate solutions, $\mathrm { i } . \mathrm { e } . , \mathrm { u } _ { i } ( t ) ^ { \flat } \mathrm { s }$ , are generated as the union of two sets, denoted as B and D, respectively. The first set, B, consists of 10 nearby solutions of $\mathbf { u } ( t - 1 )$ , including 4 nearby solutions in terms of locations along x- and y-axes, i.e.,

$$
\begin{array} { r } { \mathbf { u } _ { 1 } ( t ) = \left\{ [ q _ { x } ^ { t - 1 } + \Delta _ { q } , q _ { y } ^ { t - 1 } , H ] ^ { T } , \psi ^ { t - 1 } \right\} , } \\ { \mathbf { u } _ { 2 } ( t ) = \left\{ [ q _ { x } ^ { t - 1 } - \Delta _ { q } , q _ { y } ^ { t - 1 } , H ] ^ { T } , \psi ^ { t - 1 } \right\} , } \\ { \mathbf { u } _ { 3 } ( t ) = \left\{ [ q _ { x } ^ { t - 1 } , q _ { y } ^ { t - 1 } + \Delta _ { q } , H ] ^ { T } , \psi ^ { t - 1 } \right\} , } \\ { \mathbf { u } _ { 4 } ( t ) = \left\{ [ q _ { x } ^ { t - 1 } , q _ { y } ^ { t - 1 } - \Delta _ { q } , H ] ^ { T } , \psi ^ { t - 1 } \right\} , } \end{array}
$$

and 6 nearby solutions in terms of orientations around $x ^ { \prime } \mathrm { - } , y ^ { \prime } \mathrm { - }$ , and $z ^ { \prime } { \mathrm { - a x e s } }$ , i.e.,

$$
\begin{array} { r } { { \bf u } _ { 5 } ( t ) = \{ { \bf q } ^ { t - 1 } , [ \psi _ { z } ^ { t - 1 } + \Delta _ { \psi } , \psi _ { y } ^ { t - 1 } , \psi _ { x } ^ { t - 1 } ] ^ { T } \} , } \\ { { \bf u } _ { 6 } ( t ) = \{ { \bf q } ^ { t - 1 } , [ \psi _ { z } ^ { t - 1 } - \Delta _ { \psi } , \psi _ { y } ^ { t - 1 } , \psi _ { x } ^ { t - 1 } ] ^ { T } \} , } \\ { { \bf u } _ { 7 } ( t ) = \{ { \bf q } ^ { t - 1 } , [ \psi _ { z } ^ { t - 1 } , \psi _ { y } ^ { t - 1 } + \Delta _ { \psi } , \psi _ { x } ^ { t - 1 } ] ^ { T } \} , } \\ { { \bf u } _ { 8 } ( t ) = \{ { \bf q } ^ { t - 1 } , [ \psi _ { z } ^ { t - 1 } , \psi _ { y } ^ { t - 1 } - \Delta _ { \psi } , \psi _ { x } ^ { t - 1 } ] ^ { T } \} , } \\ { { \bf u } _ { 9 } ( t ) = \{ { \bf q } ^ { t - 1 } , [ \psi _ { z } ^ { t - 1 } , \psi _ { y } ^ { t - 1 } , \psi _ { x } ^ { t - 1 } + \Delta _ { \psi } ] ^ { T } \} , } \\ { { \bf u } _ { 1 0 } ( t ) = \{ { \bf q } ^ { t - 1 } , [ \psi _ { z } ^ { t - 1 } , \psi _ { y } ^ { t - 1 } , \psi _ { x } ^ { t - 1 } - \Delta _ { \psi } ] ^ { T } \} . } \end{array}
$$

The second set, D, contains $( I \mathrm { ~ - ~ } 1 0 )$ solutions randomly selected from the non-selected candidate solutions in the set $s \setminus B$ . Note that any solution that is out of the feasible region will be truncated, ${ \bf e . g . , \ u _ { 5 } } ( t )$ will be truncated as $\{ \bar { \mathbf { q } } ^ { t - 1 } , [ \psi _ { \mathrm { m a x } } , \psi _ { y } ^ { t - 1 } , \psi _ { x } ^ { t - 1 } ] ^ { T } \}$ if $\psi _ { z } ^ { t - 1 } + \Delta _ { \psi } > \psi _ { \mathrm { { m a x } } }$ , with $\psi _ { \mathrm { m a x } }$ denoting the maximum achievable orientation angle of the gimbal. In addition, we denote $\mathcal { E } ( t - 1 )$ as the set of all feasible solutions the GS has visited, i.e., $\mathcal { E } ( t - 1 ) ~ =$ $\{ \mathbf { u } ( 0 ) , \ \mathbf { u } ( 1 ) , \ \mathbf { u } ( 2 ) , \ \cdot \ \cdot \ , \ \mathbf { u } ( t \ - \ 1 ) \}$ , where u(0) is set as the optimized solution in the j-th AO iteration, i.e., ${ \bf u } ( 0 ) = { }$ $\left\{ { \bf q } ^ { ( j - 1 ) } , \psi ^ { ( j - 1 ) } \right\}$

The refined GS is achieved by designing a Markov chain for updating the AIRS’s location and 3D orientation iteratively, and the transition probability from the solution in the (t−1)-th iteration to the t-th iteration is given by [43]

$$
\begin{array} { r l } & { \mathbf { P } _ { i } ^ { t } = \operatorname* { P r } \big \{ \mathbf { u } ( t ) = \mathbf { u } _ { i } ( t ) | \mathbf { u } ( t - 1 ) = \{ \mathbf { q } ^ { t - 1 } , \psi ^ { t - 1 } \} \big \} } \\ & { \quad = \frac { e ^ { \mu \gamma _ { \mathrm { m i n } } ( \mathbf { u } _ { i } ( t ) ) } } { \sum _ { \mathbf { u } _ { i } ( t ) \in \mathcal { B } \cup \mathcal { D } } e ^ { \mu \gamma _ { \mathrm { m i n } } ( \mathbf { u } _ { i } ( t ) ) } } , i = 1 , 2 , \cdots , I , } \end{array}\tag{75}
$$

where $\mu \quad \geq \quad 0$ is a pre-defined scaling parameter. To avoid undesirable bouncing between two solutions with the highest minimum SNR, we manually set $\gamma _ { \mathrm { m i n } } \left( \mathbf { u } _ { i } ( t ) \right) \ =$ $\gamma _ { \mathrm { m i n } } \left( \mathbf { u } _ { i } ( t ) \right) - 3$ dB in the case of ${ \bf u } _ { i } ( t ) \in \mathcal { E } ( t - 1 )$ . To determine ${ \bf \delta u } ( t )$ based on (75), we randomly generate a float (denoted as $p _ { t } )$ between 0 and 1, and update

$$
\mathbf { u } ( t ) = \mathbf { u } _ { i ^ { \star } } ( t ) ,\tag{76}
$$

where $i ^ { \star }$ is the index satisfying $\begin{array} { r } { \sum _ { i = 1 } ^ { i ^ { \star } - 1 } \mathbf { P } _ { i } ^ { t } < p _ { t } \leq \sum _ { i = 1 } ^ { i ^ { \star } } \mathbf { P } _ { i } ^ { t } . } \end{array}$

Algorithm 1 Proposed Enhanced AO With GS for Solving   
(P1)   
Input: $N _ { x } , N _ { y } , J , T , N _ { u } ,$ w<sub>l</sub>   
$j  1$   
while $j < J ;$   
// AO without GS   
Update $\mathbf { q } ^ { ( j ) }$ based on (52);   
Update $\bar { \psi } ^ { ( j ) }$ based on (56);   
Update $\overset { \cdot } { \pmb { \theta } } ^ { ( j ) }$ based on (73)   
// refined GS   
$t \gets 1 , \mathbf { u } ( 0 ) = \{ \mathbf { q } ^ { ( j ) } , \psi ^ { ( j ) } \} , \mathcal { E } ( 0 ) \gets \{ \mathbf { u } ( 0 ) \}$   
while $t < T :$   
Generate B and D and update ${ \bf \delta u } ( t )$ based on (76)   
Update $\mathscr { E } ( t ) = \mathscr { E } ( t - 1 ) \cup \mathbf { u } ( t )$   
$t \gets t + 1$   
end while   
Update $\{ \mathbf { q } ^ { ( j ) } , \psi ^ { ( j ) } \}$ as $\{ \mathbf { q } ^ { t ^ { \star } } , \psi ^ { t ^ { \star } } \}$ based on (77)   
$j  j + 1$   
end while   
Output: $\mathbf { q } ^ { ( J ) } , \psi ^ { ( J ) } , \theta ^ { ( J ) }$

The GS proceeds until the iteration number t reaches a predefined maximum number of iterations, denoted by T . Finally, among all solutions in $\mathcal { E } ( T )$ , we choose the solution that yields the maximum minimum SINR as the output of GS, which is given by

$$
{ \bf u } ( t ^ { \star } ) = \left\{ { \bf q } ^ { t ^ { \star } } , \psi ^ { t ^ { \star } } \right\} = \arg \operatorname* { m a x } _ { { \bf u } \in \mathcal { E } ( T ) } \gamma _ { \mathrm { m i n } } \left( { \bf u } \right) .\tag{77}
$$

The $\left\{ \mathbf { q } ^ { ( j ) } , \psi ^ { ( j ) } \right\}$ is then updated as $\left\{ \mathbf { q } ^ { t ^ { \star } } , \psi ^ { t ^ { \star } } \right\}$ for the next AO iteration. Note that as $\mathcal { E } ( T )$ includes the optimized solution in the j-th AO iteration, i.e., ${ \bf u } ( 0 ) = \left\{ { \bf q } ^ { ( j - 1 ) } , \psi ^ { ( j - 1 ) } \right\}$ the GS phase must yield an objective value of (P1) no worse than $\left\{ { \bf q } ^ { \left( j - 1 \right) } , \dot { \psi } ^ { \left( j - 1 \right) } \right\}$ . Hence, the convergence of the proposed enhanced AO algorithm is ensured. We summarize the main steps of our proposed enhanced AO with GS in Algorithm 1.

Next, we analyze the complexity of Algorithm 1. The complexity order of solving sub-problem (P1.1) via the hybrid search can be expressed as $\mathcal { O } ( N _ { u } N _ { \mathrm { t o t } } ) + \mathcal { O } ( N _ { u } N _ { \mathrm { t o t } , n ^ { * } } )$ , and that of solving sub-problem (P1.2) is given by $\mathcal { O } ( N _ { u } \tilde { N } _ { \mathrm { t o t } } ) +$ $\mathcal { O } ( N _ { u } \tilde { N } _ { \mathrm { t o t } , m ^ { * } } )$ . To solve each sub-problem (P1.3x), it can be shown that the complexity order is given by $\mathcal { O } ( N _ { u } ^ { 1 . 5 } N _ { x } ^ { 6 . 5 } )$ [44]. As such, the complexity of solving (P1.3) is given by $\mathcal { O } ( N _ { u } ^ { 1 . 5 } N _ { x } ^ { 6 . 5 } ) { + } \mathcal { O } ( N _ { u } ^ { 1 . 5 } \bar { N } _ { u } ^ { 6 . 5 } )$ . Finally, the complexity order of the GS phase per AO iteration is given by $\mathcal { O } ( N _ { u } T I )$ . It follows that the overall complexity of Algorithm 1 is polynomial w.r.t. the number of users $N _ { u }$ . In particular, the complexity of the additional GS phase is linear in $N _ { u }$ and independent of the AIRS size, making it practically affordable in largescale wireless networks. Furthermore, additional strategies such as user scheduling and/or AIRS element grouping can be employed in practice to further reduce the overall complexity.

## V. NUMERICAL RESULTS

In this section, numerical results are provided to evaluate the performance of our proposed UAV-enabled passive 6DMA and validate the theoretical analyses.

## A. Simulation Parameters

The noise power and the BS’s transmit power are set as $\sigma ^ { 2 } = - 1 1 0$ dBm and $P = 2 0$ dBm, respectively, while the reference path gain is $\beta _ { 0 } = - 4 0$ dB. The distance between adjacent transmit antennas at the BS is $\begin{array} { r } { d _ { t x } \ = \ \frac { \lambda } { 2 } } \end{array}$ , and the distance between adjacent reflecting elements of the AIRS is $\begin{array} { r } { d _ { r s } = \frac { \lambda } { 2 } } \end{array}$ . The number of the BS’s antennas is set to $M =$ 64. The number of AIRS reflecting elements per dimension is assumed to be identical as $N _ { x } = N _ { y } = 1 6 , { \mathrm { i . e . , ~ } } N = 2 5 6 .$ Unless otherwise stated, the AIRS’s altitude is fixed as $H =$ 100 m. The maximum numbers of AO and GS iterations are $J = 3$ and $T = 4 0 0$ , respectively. The penalty parameter in the beamforming optimization is set as $\rho = 1 0 \ \AA$ . In the GS, the scaling parameter, number of selected candidate solutions, location interval, and orientation interval are set as $\mu = 2 0 $ $I = 3 0 , \Delta _ { q } = 5$ m, and $\Delta _ { \psi } ~ = ~ \pi / 1 8 0$ , respectively. The numbers of sampling points in the coarse- and fine-grained search are ${ \bar { N } } _ { x } = { \bar { N } } _ { y } = N _ { x , n ^ { * } } = N _ { y , n ^ { * } } = 1 0 0 , { \tilde { N } } _ { z } = { \tilde { N } } _ { y } = $ $\tilde { N } _ { x } = 6 0$ , and $\tilde { N } _ { z , m ^ { * } } = \tilde { N } _ { y , m ^ { * } } = \tilde { N } _ { x , m ^ { * } } = 3 ,$ , respectively. In the single-user case, the BS-user distance is fixed as $D \ = \ 5 0 0 \ \mathrm { m } .$ , the UAV’s movement region is set as ${ \mathcal { Q } } =$ $\{ q _ { x } | \ : - \ : 0 . 2 D \ : \le \ : q _ { x } \ : \le \ : 1 . 2 D \}$ . In the multi-user case, we consider two setups of the users’ geographic distributions with the number of users fixed as $N _ { u } ~ = ~ 3$ . In the first setup, the locations of the users are sparse and given by $\begin{array} { r l } { \mathbf { w } _ { 1 } } & { { } = } \end{array}$ $[ 3 3 0 , 2 4 0 , 0 ] ^ { T } , \textbf { w } _ { 2 } = [ 6 5 0 , 1 3 0 , 0 ] ^ { T } , \textbf { w } _ { 3 } = [ 4 4 0 , 1 5 , 0 ] ^ { T }$ In the second setup, the locations of the users are denser and given by $\begin{array} { r } { \begin{array} { l } { \mathbf { w } _ { 1 } } & { = \ [ 6 5 5 , 1 3 0 , 0 ] ^ { T } , \ \mathbf { w } _ { 2 } \ = \ [ 6 5 0 , 1 3 5 , 0 ] ^ { T } . } \end{array} } \end{array}$ $\mathbf { w } _ { 3 } = [ 6 5 0 , 1 3 0 , 0 ] ^ { T }$ . The UAV’s movement region is set as $\mathcal { Q } = \{ ( q _ { x } , q _ { y } ) | - 1 4 0 \leq q _ { x } \leq 7 9 0 , - 5 8 \leq q _ { y } \leq 2 9 8 \}$

The AIRS’s location, orientation, and phase shifts are initialized individually in the AO algorithm based on the following procedures. First, the AIRS’s location is initialized as

$$
\mathbf { q } ^ { ( 1 ) } = \arg \operatorname* { m a x } _ { \mathbf { q } \in \mathcal { Q } } \operatorname* { m i n } _ { l \in \mathcal { N } _ { u } } \frac { 1 } { \| \mathbf { q } \| ^ { 2 } \| \mathbf { q } - \mathbf { w } _ { l } \| ^ { 2 } } ,\tag{78}
$$

which maximizes the minimum path gain from the BS to all users. Second, the AIRS’s orientation is initialized as

$$
\boldsymbol { \psi } ^ { ( 1 ) } = \arg \operatorname* { m a x } _ { \boldsymbol { \psi } } \operatorname* { m i n } _ { l \in \mathcal { N } _ { u } } F _ { \mathrm { A G } , l } \left( \mathbf { q } ^ { ( 1 ) } , \boldsymbol { \psi } \right) ,\tag{79}
$$

which maximizes the minimum aperture gain from the BS to all users. Finally, the AIRS’s passive beamforming is initialized as $\pmb { \theta } ^ { ( 1 ) }$ by solving (P1.3x) and (P1.3y) with $\alpha _ { l } = 1$ which maximizes the minimum passive beamforming gain achievable by all users.

![](images/775cf5668c29d1835cd3ad50e68f64a89f792afc8386a5a81a9116c5d3b1446b.jpg)

Fig. 6. AIRS’s orientation versus its location.  
![](images/e02486a3917e6274cc728f16a1bff631e901e7d2bd95d4ef7ad07e252cc2725d.jpg)  
Fig. 7. User’s received SNR versus BS-user distance.

## B. Single-User Case

In the single-user case, we consider the following two benchmark schemes, i.e.

• AIRS’s orientation optimization only with $q _ { x }$ fixed as (45), which is optimal for isotropic signal reflection.

$\mathbf { A R S } ^ { \prime } \mathbf { s }$ location optimization only with $\psi _ { y } = 0 .$

First, by varying the AIRS’s altitude H, Fig. 6 depicts the AIRS’s optimal orientations and locations under D = 500 m by the proposed joint location and orientation optimization and the two benchmark schemes. It is observed that the AIRS’s optimal locations by the two benchmark schemes are identical, which validates our analysis presented at the end of Section III-B1). Moreover, it is observed that the AIRS’s optimal orientation is symmetric to $\begin{array} { r } { q _ { x } \ = \ \frac { D } { 2 } } \end{array}$ , at which the AIRS is parallel to the ground, i.e., no orientation is needed. This observation is consistent with our theoretical analyses provided in Section III-B2). Furthermore, as the AIRS’s altitude H decreases, its optimal orientation angle becomes closer to $\frac { \pi } { 2 }$ $\mathrm { o r } \ - { \frac { \pi } { 2 } }$ while its optimal location becomes closer to 0 or D. On the other hand, as H increases, the AIRS’s optimal location and orientation angle approach $\begin{array} { r } { q _ { x } = \frac { D } { 2 } } \end{array}$ and $\psi _ { y } = 0$ respectively. As a result, the AIRS’s location and orientation by the joint optimization are mostly different from those by the two benchmark schemes for a moderate H. All of the above observations match the theoretical analyses conducted in Section III-B3) for $H \to 0 { \mathrm { ~ o r ~ } } \to \infty$

Next, Fig. 7 shows the user’s received SNR under $H =$ 100 m versus the BS-user distance $D .$ In addition to the two benchmarks, we also show the user’s received SNR in the case of isotropic signal reflection by the AIRS, i.e., $F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { y } ) = 1$ , which serves as an upper bound on the performance of the considered three schemes. It is observed from Fig. 7 that as D increases, the SNR performance of all schemes becomes worse, due to the more severe end-to-end path loss. Nonetheless, the proposed joint optimization yields better performance than the other two benchmark schemes. Particularly, the AIRS’s orientation optimization is observed to significantly outperform its location optimization, which implies that the orientation plays a more significant role than the location in affecting the user’s SNR performance. The possible reason is that the effective reflection aperture gain $F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { y } )$ can rapidly change with the AIRS’s orientation angle, which is more dramatic than the change of the endto-end path loss with the AIRS’s location. Furthermore, all of the considered schemes are observed to yield comparable SNR performance to the upper bound when D is small, as analyzed in Section III-B3).

![](images/0a2708937f8db3bd78ea515d1bb7c7e63038364b80effe3864a44b18d0a34f01.jpg)  
Fig. 8. User’s received SNR versus AIRS’s altitude.

Finally, Fig. 8 shows the user’s received SNR under $D =$ 500 m versus the AIRS’s altitude H. It is first observed from Fig. 8 that the SNR performance of all schemes degrades with H due to the more severe path loss. It is also observed that the joint optimization yields better performance than the other two benchmark schemes for a small H. However, as H increases, the performance gap with them gradually vanishes, and all schemes yield comparable performance to the performance upper bound. This implies that orientation optimization brings lower performance gain for a large H, as analyzed in Section III-B3).

## C. Multi-User Case

In the multi-user case, the proposed enhanced AO algorithm with GS is labeled as “AO w/ GS”, and we consider the following four benchmark schemes:

• AO without GS (AO w/o GS): The conventional AO algorithm described in Section IV-A.

• Individual optimization: The AIRS’s position, orientation, and phase shifts are individually optimized to maximize the minimum end-to-end path gain, aperture gain, and beamforming gain, respectively, i.e., $\mathbf { q } ^ { ( 1 ) } , \psi ^ { ( 1 ) }$ and $\pmb { \theta } ^ { ( 1 ) }$ given at the end of Section V-A.

• w/o AIRS orientation: Only the AIRS’s location and phase shifts are optimized, while its orientation is fixed as $\psi = [ 0 , 0 , 0 ] ^ { T }$

Fig. 9 shows the users’ max-min received SNR by different schemes versus the AIRS’s altitude with sparsely distributed users. It is observed that the SNR performance of all schemes (except the conventional AO without GS) decreases with the AIRS’s altitude due to the increased path loss, which is similar to the observation made for the single-user case in Fig. 8. However, the conventional AO without GS is observed to experience significant performance fluctuation as the AIRS’s altitude increases. For example, as H increases from 200 m to 250 m, its achieved SNR increases from −5 dB to −1.3 dB. This implies that it may be trapped by lowquality local optimums and thus result in an unstable SNR performance. It is also observed that our proposed algorithm outperforms all benchmark schemes considered, thus validating its effectiveness. However, as the AIRS’s altitude H increases, the gap between the proposed scheme and the scheme without AIRS orientation is observed to gradually vanish, implying that the effects of AIRS orientation plays a less significant role. This observation is consistent with the observation made for the single-user case in Fig. 8 as well.

![](images/646d7b6d7e4d244914ce5308d0684a6043b0e0f9e784818a4cf3ac40f9dc1f9a.jpg)  
Fig. 9. Users’ max-min SNR versus AIRS’s altitude for sparse user distribution.

![](images/2e032d223f709eec33b3b9e5d081170a2e1a3bdf29fd3c0261e6db8ab3daf139.jpg)  
Fig. 10. Optimized AIRS position and orientation with different altitudes.

Fig. 10 shows the optimized AIRS location and orientation for different altitudes. It is observed that the optimized AIRS’s position varies with its altitude. In particular, it is approximately arranged along the line between the BS and user 2 when its altitude is sufficiently high (e.g., H ≥ 100 m), due to the most severe end-to-end path loss between the BS and user 2 among all users, while its orientation is altered to ensure the effective aperture gain achievable by all users. It is also observed that less orientation is needed for the AIRS with a sufficiently high altitude, due to the less significant role of AIRS orientation in this case, as similarly observed in Figs. 6, 8, and 9.

To gain more insights, Figs. 11(a)-11(d) show the distribution of the optimized end-to-end path gain, effective aperture gain, passive beamforming gain and max-min user SNR (all in dB) over the AIRS’s moving region Q by the proposed enhanced AO algorithm, with H = 100 m. Note that any effective aperture gain less than −40 dB is plotted as −40 dB in Fig. 11(b) due to its excessively small value. It is observed from Fig. 11(a)-11(c) that the proposed algorithm can properly balance all of the path gain, effective aperture gain, and beamforming gain achievable by the three users, thus ensuring the max-min SNR in Fig. 11(d). Compared to the path gain and the effective aperture gain, the fluctuation of the passive beamforming gain is observed to be more significant within Q. Nonetheless, it is worth noting that the maximum passive beamforming gain achievable by each user is given by $1 0 { \times } \log _ { 1 0 } ( N ^ { 2 } ) = 4 8 . 2 \ \mathrm { d B }$ with $N = 1 6 ^ { 2 }$ , while the three users are observed to reap a passive beamforming gain of around 40 dB. This implies that the proposed algorithm helps generate multiple high-gain passive beams aligned to each of them.

Fig. 12 shows the users’ max-min received SNR by different schemes versus the AIRS’s altitude with densely distributed users. It is observed that at H = 100 m, the proposed AO algorithm w/ GS achieves an identical SNR performance to “Joint Optimization” at $D \ : = \ : 6 6 3$ m in Fig. 7, and 663 m is approximately the distance from the BS to user 3. This observation implies that in the case of densely distributed users, the AIRS’s location and orientation may suffice to be designed based on a certain user thanks to the small inter-user distances compared to H. This fact can also be seen from the smaller performance gap between the proposed algorithm and the benchmark with individual optimization compared to that in Fig. 9.

## D. Comparison With Full-Duplex Relay

In this subsection, we compare the performance of the proposed UAV-enabled passive 6DMA with that of a fullduplex amplify-and-forward (FD-AF) UAV relay, taking the single-user scenario as an example. For the FD-AF relay scheme, let $P _ { B } ^ { ( A F ) }$ and $P _ { R }$ denote the maximum transmit power of the BS and the UAV, respectively. For fairness of comparison, in our proposed scheme, we set the BS’s transmit power as $P = P _ { B } ^ { ( A \dot { F } ) } \dot { + } P _ { R }$ . The number of the UAV relay’s antennas is denoted as $N _ { A }$ . It can be shown that for any given UAV’s position $q _ { x } ,$ , the user’s maximum received SNR in the FD-AF relay scheme is given by [45]

$$
\gamma ^ { ( A F ) } ( q _ { x } ) = \frac { M N _ { A } ^ { 2 } P _ { R } P _ { B } ^ { ( A F ) } \beta _ { 1 } ( q _ { x } ) \beta _ { 2 , 0 } ( q _ { x } ) } { ( N _ { A } \rho _ { A } P _ { R } ^ { 2 } + N _ { A } \sigma ^ { 2 } P _ { R } ) \beta _ { 2 , 0 } ( q _ { x } ) + \sigma ^ { 2 } } ,\tag{80}
$$

where $\begin{array} { r } { \beta _ { 1 } ( q _ { x } ) = \frac { \beta _ { 0 } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } , \beta _ { 2 , 0 } ( q _ { x } ) = \frac { \beta _ { 0 } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } . } \end{array}$ , and $\rho _ { A }$ characterizes the effects of self-interference cancellation. The optimal UAV position $q _ { x }$ that maximizes (80) can be obtained via an exhaustive search. Compared to the received SNR in (48) by our proposed scheme, it is noted that the FD-AF relay scheme suffers from self-interference, i.e., $N _ { A } \rho _ { A } P _ { R } ^ { 2 } \beta _ { 2 , 0 } ( q _ { x } )$ In particular, assuming that ${ \underline { { P } } } _ { R } = \alpha _ { A } P _ { B } ^ { ( A F ) }$ with $\alpha _ { A }$ being a constant and letting $P _ { B } ^ { ( A F ) }  \infty$ , it can be shown that $\begin{array} { r } { \gamma ^ { ( A F ) } ( q _ { x } )  \frac { M N _ { A } \beta _ { 1 } \overline { { ( } } q _ { x } ) } { \rho _ { A } \alpha _ { A } } } \end{array}$ , i.e., it reaches a limit due to selfinterference. Regarding the deployment, it can be shown that the UAV FD-AF relay should be deployed closely to the BS in the case that $P _ { R } = \alpha _ { A } P _ { B } ^ { ( A F ) }  \infty ,$ i.e., $q _ { x } \to 0 ,$ , so that $\beta _ { 1 } ( q _ { x } )$ is maximized. In contrast, the optimal AIRS position is independent of the BS’s transmit power $P$ in our proposed scheme.

![](images/22b95f0ead4dea937e4dc6e6647012950f1e614212cce7a752c84a6eff64cda5.jpg)  
(a) End-to-end path gain

![](images/afd36fb1e46007a33f6757c6fb45c8c80e55d40ff8a9145b7f7181793c1ea6a5.jpg)  
(c) Passive beamforming gain

![](images/7e1b32d83f26c89f649f89ca610727f101b394351a1f784e3565ada00451dfd5.jpg)  
(b) Effective aperture gain

![](images/33e89c173e92dcee1b566dfecd1e76cd3fd7199b6cac5ceca16535a23d4930ba.jpg)  
(d) Max-min user SNR

Fig. 11. Distribution of the optimized path gain, effective aperture gain, passive beamforming gain, and max-min user SNR over the AIRS’s moving region with H = 100 m.  
![](images/abd80708046cd7b486148004ec5fbe251f990eecb50ec78a029342ddf23b1785.jpg)  
Fig. 12. Users’ max-min SNR versus AIRS’s altitude for dense user distribution.

![](images/0f98cf6808fe9b777f7b4f8b33bb087e5ec44cd88a5ab09e48dedca0b1758e56.jpg)  
Fig. 13. Performance comparison with FD-AF UAV relay.

In Fig. 13, we plot the user’s maximum reveived SNRs by our proposed scheme and the FD-AF relay scheme versus the BS’s transmit power $P ,$ with the BS-user distance $D = 2 0 0 \mathrm { m }$ . In the FD-AF relay scheme, we assume $P _ { B } ^ { ( A F ) } = P _ { R } = P / 2$ It is observed that the performance of the FD-AF relay scheme first increases with $P$ but eventually converges due to the self-interference, validating the above analysis. In contrast, the performance of our proposed scheme monotonically increases with $P$ due to the absence of self-interference. Moreover, it is observed that the proposed scheme yields a more significant performance gain over the FD-AF relay scheme as $P$ is lowto-moderate. This is because in the FD-AF relay scheme, the user’s received SNR is proportional to the product of $P _ { B } ^ { A F }$ and $P _ { R } ;$ whereas in the proposed scheme, it is proportional to their sum. When $P$ is relatively small, the product of $P _ { B } ^ { A F }$ and $P _ { R }$ decreases more rapidly with $P$ than their sum. In contrast, when $P$ is large, the product increases faster than the sum. As a result, the FD-AF relay yields a higher SNR than the proposed scheme under $N _ { A } = 2 5 6$ , at the cost of increased hardware complexity due to the use of an active antenna array on the UAV. Moreover, the proposed scheme is observed to outperform the FD-AF relay scheme over the whole range of $P$ considered for $N _ { A } = 6 4$

![](images/8f1b4a5569df7ae240aec81df6159836e75d843a9cdadf20adf8d961843c5dd4.jpg)  
Fig. 14. Users’ max-min SNR versus their positional shifts.

## E. User Mobility Consideration

Finally, considering that adjusting the AIRS’s position and orientation incurs certain delays, we evaluate the robustness of our optimized AIRS passive beamforming and deployment solutions in the presence of user mobility. Specifically, we consider the multi-user scenario with sparsely distributed users, as illustrated in Fig. 11. We simulate user mobility by shifting all user positions along the x-axis by the same amount. We consider the following three benchmarks. In the “timely optimization” benchmark, both the AIRS passive beamforming and deployment are synchronized with user movement and updated accordingly. In the “outdated deployment optimization” benchmark, only the AIRS’s passive beamforming is synchronized and updated, while its deployment remains unchanged. In the “outdated optimization” benchmark, neither the AIRS passive beamforming nor the deployment is synchronized with user movement, and both remain fixed as those prior to the shift. Fig. 14 shows the users’ max-min SNRs versus their positional shifts under the above three benchmarks, with the UAV’s altitude fixed at H = 100 m. As expected, outdated deployment optimization leads to certain performance degradation compared to timely optimization, and this degradation increases with the positional shift. However, even with a shift of ±20 m, the SNR loss is limited to approximately 0.1 dB and 1 dB for the “outdated deployment optimization” and “outdated optimization” benchmarks. It follows that the performance loss due to outdated optimization is tolerable and our proposed algorithm manifests robustness. This robustness is primarily due to the significantly higher altitude of the AIRS relative to terrestrial users, such that moderate variations in user positions have a marginal impact on the relative distances and angles between the AIRS and the users.

## VI. CONCLUSION

In this paper, we investigated a joint location, orientation, and beamforming optimization problem for a passive 6DMAaided multicast system under the practical angle-dependent reflection model. In the special single-user case, we unveiled that it suffices to exploit the AIRS’s 1D orientation to achieve the optimal performance. Furthermore, we derived the optimal AIRS orientation and location in closed form in some special cases and show their non-trivial relationship with the AIRS’s altitude and the BS-user distance. In the general multi-user case, we proposed an enhanced AO algorithm with GS, where the AIRS’s location and orientation were updated iteratively via a probability-based Markov chain to avoid low-quality local optimum. Numerical results validated our theoretical analyses and demonstrate the superiority of our proposed AO algorithm with GS to other baseline schemes. It was also shown that the AIRS’s orientation may have a profound effect on the user SNRs, especially if the AIRS’s altitude is not high. Furthermore, the user distribution can affect the efficacy of the joint optimization versus the individual optimization of the AIRS’s location and orientation. This paper can be extended to various directions as future work, e.g., the performance optimization of the passive 6DMA for physical-layer security, multi-user broadcasting, non-orthogonal multiple access, etc. It is also interesting to study more general passive 6DMA with tunable relative positions of the AIRS’s reflecting elements and evaluate its performance gain. Last but not least, it is worthwhile to investigate the effects of aerial flutter on the overall performance of the proposed scheme, as well as to develop robust deployment and beamforming designs to mitigate its effects.

## APPENDIX PROOF OF PROPOSITION 1

By noting that only F is affected by ψ in (36), to prove (37), it is equivalent to prove

$$
F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) = F _ { \mathrm { A G , 0 } } ( q _ { x } , \psi _ { \mathrm { 3 D } } ) .\tag{81}
$$

By substituting (35) into (81), it becomes

$$
\begin{array} { r l } & { \cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) \cos \phi _ { 2 , 0 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) } \\ & { = \cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 3 D } } ) \cos \phi _ { 2 , 0 } ( q _ { x } , \psi _ { \mathrm { 3 D } } ) . } \end{array}\tag{82}
$$

To achieve (82), we next aim to find a feasible $\psi _ { \mathrm { 2 D } } ^ { \star }$ satisfying

$$
\cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) = \cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 3 D } } )\tag{83}
$$

and

$$
\cos \phi _ { 2 , 0 } ( { q _ { x } } , \psi _ { \mathrm { 2 D } } ^ { \star } ) = \cos \phi _ { 2 , 0 } ( { q _ { x } } , \psi _ { \mathrm { 3 D } } )\tag{84}
$$

at the same time. To this end, based on (13) and (14), we can respectively express the LHSs of (83) and (84) as

$$
\cos \phi _ { 1 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) = \frac { q _ { x } \sin \psi _ { y } ^ { \star } \cos \psi _ { x } ^ { \star } + H \cos \psi _ { y } ^ { \star } \cos \psi _ { x } ^ { \star } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } ,\tag{85}
$$

$$
\cos \phi _ { 2 , 0 } ( q _ { x } , \psi _ { \mathrm { 2 D } } ^ { \star } ) = \frac { ( q _ { x } - D ) \sin \psi _ { y } ^ { \star } \cos \psi _ { x } ^ { \star } + H \cos \psi _ { y } ^ { \star } \cos \psi _ { x } ^ { \star } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } ,\tag{86}
$$

with | sin $\psi _ { y } ^ { \star }$ cos $| \psi _ { x } ^ { \star } | \leq 1$ and | cos $\psi _ { y } ^ { \star }$ cos $| \psi _ { x } ^ { \star } | \leq 1$ . Similarly, the right hand sides (RHSs) of (83) and (84) can be expressed as

$$
\cos \phi _ { 1 } ( q _ { x } , \psi _ { 3 \mathrm { D } } ) = \frac { q _ { x } L _ { 1 } + H L _ { 3 } } { \sqrt { q _ { x } ^ { 2 } + H ^ { 2 } } } ,\tag{87}
$$

$$
\cos \phi _ { 2 , 0 } ( q _ { x } , \psi _ { 3 \mathrm { D } } ) = \frac { ( q _ { x } - D ) L _ { 1 } + H L _ { 3 } } { \sqrt { ( q _ { x } - D ) ^ { 2 } + H ^ { 2 } } } ,\tag{88}
$$

with $L _ { 1 }$ and $L _ { 3 }$ also satisfying $| L _ { 1 } | \leq 1$ and $| L _ { 3 } | \le 1$ . By comparing (85)-(86) with (87)-(88), if there exists a set of $\psi _ { x } ^ { \star }$ and $\psi _ { y } ^ { \star }$ that satisfy both of the following two equations, i.e.,

$$
\sin \psi _ { y } ^ { \star } \cos \psi _ { x } ^ { \star } = L _ { 1 } ,\tag{89}
$$

$$
\cos { \psi _ { y } ^ { \star } } \cos { \psi _ { x } ^ { \star } } = L _ { 3 } ,\tag{90}
$$

then (83) and (84) can be met at the same time.

After some manipulations, it can be shown that both (86) and (86) hold if and only if

$$
\cos ^ { 2 } \psi _ { x } ^ { \star } = L _ { 1 } ^ { 2 } + L _ { 3 } ^ { 2 } .\tag{91}
$$

Then, if $L _ { 1 } ^ { 2 } + L _ { 3 } ^ { 2 } \leq 1$ , we can always find a $\psi _ { x } ^ { \star }$ that satisfies (91). Next, we prove

$$
L _ { 1 } ^ { 2 } + L _ { 3 } ^ { 2 } \leq 1 .\tag{92}
$$

To this end, we substitute (15)-(17) into (86) and recast it as

2 sin ψ<sub>z</sub> cos ψ<sub>z</sub> sin ψ<sub>y</sub> sin ψ<sub>x</sub> cos $\psi _ { x } + \cos ^ { 2 } \psi _ { y } \cos ^ { 2 } \psi _ { x }$

$$
+ \sin ^ { 2 } \psi _ { z } \sin ^ { 2 } \psi _ { x } + \cos ^ { 2 } \psi _ { z } \sin ^ { 2 } \psi _ { y } \cos ^ { 2 } \psi _ { x } \leq 1 .\tag{93}
$$

Note that the RHS of (86), i.e., 1, can be rewritten as

$$
1 = \cos ^ { 2 } \psi _ { z } ( \cos ^ { 2 } \psi _ { y } + \sin ^ { 2 } \psi _ { y } ) + ( \sin ^ { 2 } \psi _ { z } + \cos ^ { 2 } \psi _ { z } ) \sin ^ { 2 } \psi _ { x } .\tag{94}
$$

By substituting (86) into (86), (86) becomes

$\cos ^ { 2 } \psi _ { z } \sin ^ { 2 } \psi _ { y } \cos ^ { 2 } \psi _ { x } + 2$ sin ψ<sub>z</sub> cos ψ<sub>z</sub> sin $\psi _ { y }$ sin $\psi _ { x }$ cos ψ<sub>x</sub> $\leq \sin ^ { 2 } \psi _ { y } \cos ^ { 2 } \psi _ { x } + \cos ^ { 2 } \psi _ { z } \sin ^ { 2 } \psi _ { x }$ (95)

By applying the fact that $\cos ^ { 2 } \psi _ { z } = 1 - \sin ^ { 2 } \psi _ { z }$ to the first term in (86), (86) becomes

$$
\begin{array} { r l } & { 2 \sin \psi _ { z } \cos \psi _ { z } \sin \psi _ { y } \sin \psi _ { x } \cos \psi _ { x } } \\ & { \leq \sin ^ { 2 } \psi _ { z } \sin ^ { 2 } \psi _ { y } \cos ^ { 2 } \psi _ { x } + \cos ^ { 2 } \psi _ { z } \sin ^ { 2 } \psi _ { x } . } \end{array}\tag{96}
$$

Next, we move the LHS of (86) to its RHS and obtain

$$
0 \leq ( \sin \psi _ { z } \sin \psi _ { y } \cos \psi _ { x } - \cos \psi _ { z } \sin \psi _ { x } ) ^ { 2 } ,\tag{97}
$$

which is always true. Hence, the inequality in (86) always holds, and we can calculate $\psi _ { x } ^ { \star }$ from (91) as

$$
\psi _ { x } ^ { \star } = \pm \operatorname { a r c c o s } \sqrt { L _ { 1 } ^ { 2 } + L _ { 3 } ^ { 2 } } .\tag{98}
$$

By substituting (98) into (86) and (86), we can calculate $\psi _ { y } ^ { \star }$ as

$$
\psi _ { y } ^ { \star } = \arcsin \frac { L _ { 1 } } { \sqrt { L _ { 1 } ^ { 2 } + L _ { 3 } ^ { 2 } } } .\tag{99}
$$

The proof of Proposition 1 is thus complete.

## REFERENCES

[1] C. Liu, W. Mei, and Z. Chen, “Joint 3D orientation and location optimization for UAV-mounted intelligent reflecting surface,” in Proc. IEEE Global Commun. Conf., Cape Town, South Africa, Dec. 2024, pp. 2725–2730.

[2] E. Basar, M. Di Renzo, J. De Rosny, M. Debbah, M.-S. Alouini, and R. Zhang, “Wireless communications through reconfigurable intelligent surfaces,” IEEE Access, vol. 7, pp. 116753–116773, 2019.

[3] Q. Wu, S. Zhang, B. Zheng, C. You, and R. Zhang, “Intelligent reflecting surface-aided wireless communications: A tutorial,” IEEE Trans. Commun., vol. 69, no. 5, pp. 3313–3351, May 2021.

[4] M. Di Renzo et al., “Smart radio environments empowered by reconfigurable intelligent surfaces: How it works, state of research, and the road ahead,” IEEE J. Sel. Areas Commun., vol. 38, no. 11, pp. 2450–2525, Nov. 2020.

[5] W. Mei, B. Zheng, C. You, and R. Zhang, “Intelligent reflecting surfaceaided wireless networks: From single-reflection to multireflection design and optimization,” Proc. IEEE, vol. 110, no. 9, pp. 1380–1400, Sep. 2022.

[6] B. Zheng, C. You, W. Mei, and R. Zhang, “A survey on channel estimation and practical passive beamforming design for intelligent reflecting surface aided wireless communications,” IEEE Commun. Surveys Tuts., vol. 24, no. 2, pp. 1035–1071, 2nd Quart., 2022.

[7] Q. Wu, X. Guan, and R. Zhang, “Intelligent reflecting surface-aided wireless energy and information transmission: An overview,” Proc. IEEE, vol. 110, no. 1, pp. 150–170, Jan. 2022.

[8] S. Gong et al., “Toward smart wireless communications via intelligent reflecting surfaces: A contemporary survey,” IEEE Commun. Surveys Tuts., vol. 22, no. 4, pp. 2283–2314, 2020.

[9] X. Mu, Y. Liu, L. Guo, J. Lin, and R. Schober, “Joint deployment and multiple access design for intelligent reflecting surface assisted networks,” IEEE Trans. Wireless Commun., vol. 20, no. 10, pp. 6648–6664, Oct. 2021.

[10] J. Feng et al., “Joint passive beamforming and deployment design for dual distributed-IRS aided communication,” IEEE Trans. Veh. Technol., vol. 72, no. 10, pp. 13758–13763, Oct. 2023.

[11] J. Bai, H.-M. Wang, and P. Liu, “Robust IRS-aided secrecy transmission with location optimization,” IEEE Trans. Commun., vol. 70, no. 9, pp. 6149–6163, Sep. 2022.

[12] S. Zhang and R. Zhang, “Intelligent reflecting surface aided multi-user communication: Capacity region and deployment strategy,” IEEE Trans. Commun., vol. 69, no. 9, pp. 5790–5806, Sep. 2021.

[13] W. Mei and R. Zhang, “Joint base station and IRS deployment for enhancing network coverage: A graph-based modeling and optimization approach,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 8200–8213, Nov. 2023.

[14] M. Fu, W. Mei, and R. Zhang, “Multi-passive/active-IRS enhanced wireless coverage: Deployment optimization and cost-performance tradeoff,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 9657–9671, Aug. 2024.

[15] DJI.(2025). Flycart 30. [Online]. Available: https://www.dji.com/uk/ flycart-30/specs

[16] C. You, Z. Kang, Y. Zeng, and R. Zhang, “Enabling smart reflection in integrated air-ground wireless network: IRS meets UAV,” IEEE Wireless Commun., vol. 28, no. 6, pp. 138–144, Dec. 2021.

[17] DJI.(2021). Support for Phantom 4 Pro V2.0. [Online]. Available: https:// www.dji.com/uk/support/product/phantom-4-pro-v2

[18] T. Shafique, H. Tabassum, and E. Hossain, “Optimization of wireless relaying with flexible UAV-borne reflecting surfaces,” IEEE Trans. Commun., vol. 69, no. 1, pp. 309–325, Jan. 2021.

[19] H. Lu, Y. Zeng, S. Jin, and R. Zhang, “Aerial intelligent reflecting surface: Joint placement and passive beamforming design with 3D beam flattening,” IEEE Trans. Wireless Commun., vol. 20, no. 7, pp. 4128–4143, Jul. 2021.

[20] W. Tang et al., “Path loss modeling and measurements for reconfigurable intelligent surfaces in the millimeter-wave frequency band,” IEEE Trans. Commun., vol. 70, no. 9, pp. 6259–6276, Sep. 2022.

[21] E. Dong et al., “Intelligent reflecting surface partitioning-based channel modeling and performance analysis,” IEEE Commun. Lett., vol. 29, no. 2, pp. 343–347, Feb. 2025.

[22] L. Ling, Z. Lian, Z. Ma, L. Zhang, and Y. Su, “Channel modeling and performance analysis for RIS-assisted mmWave communications,” IEEE Internet Things J., vol. 12, no. 3, pp. 3188–3201, Feb. 2025.

[23] S. Zeng, H. Zhang, B. Di, Z. Han, and L. Song, “Reconfigurable intelligent surface (RIS) assisted wireless coverage extension: RIS orientation and location optimization,” IEEE Commun. Lett., vol. 25, no. 1, pp. 269–273, Jan. 2021.

[24] Y. Cheng, W. Peng, C. Huang, G. C. Alexandropoulos, C. Yuen, and M. Debbah, “RIS-aided wireless communications: Extra degrees of freedom via rotation and location optimization,” IEEE Trans. Wireless Commun., vol. 21, no. 8, pp. 6656–6671, Aug. 2022.

[25] X. Shao and R. Zhang, “6DMA enhanced wireless network with flexible antenna position and rotation: Opportunities and challenges,” IEEE Commun. Mag., vol. 63, no. 4, pp. 121–128, Apr. 2025.

[26] X. Shao, R. Zhang, and R. Schober, “Exploiting six-dimensional movable antenna for wireless sensing,” IEEE Wireless Commun. Lett., vol. 14, no. 2, pp. 265–269, Feb. 2025.

[27] L. Zhu, W. Ma, and R. Zhang, “Movable antennas for wireless communication: Opportunities and challenges,” IEEE Commun. Mag., vol. 62, no. 6, pp. 114–120, Jun. 2024.

[28] B. Ning et al., “Movable antenna-enhanced wireless communications: General architectures and implementation methods,” IEEE Wireless Commun., vol. 32, no. 5, pp. 108–116, Oct. 2025.

[29] W. Mei, X. Wei, B. Ning, Z. Chen, and R. Zhang, “Movable-antenna position optimization: A graph-based approach,” IEEE Wireless Commun. Lett., vol. 13, no. 7, pp. 1853–1857, Jul. 2024.

[30] X. Wei, W. Mei, D. Wang, B. Ning, and Z. Chen, “Joint beamforming and antenna position optimization for movable antenna-assisted spectrum sharing,” IEEE Wireless Commun. Lett., vol. 13, no. 9, pp. 2502–2506, Sep. 2024.

[31] B. Zheng, Q. Wu, T. Ma, and R. Zhang, “Rotatable antenna enabled wireless communication: Modeling and optimization,” 2025, arXiv:2501.02595.

[32] L. Zhu et al., “A tutorial on movable antennas for wireless networks,” IEEE Commun. Surveys Tuts., early access, Feb. 27, 2025, doi: 10.1109/ COMST.2025.3546373.

[33] H. Ma, W. Mei, X. Wei, B. Ning, and Z. Chen, “Robust movableantenna position optimization with imperfect CSI for MISO systems,” IEEE Commun. Lett., vol. 29, no. 7, pp. 1594–1598, Jul. 2025.

[34] X. Shen, X. Wei, W. Mei, Z. Chen, J. Fang, and B. Ning, “Movable-antenna-enhanced physical-layer service integration: Performance analysis and optimization,” IEEE Wireless Commun. Lett., vol. 14, no. 9, pp. 2952–2956, Sep. 2025.

[35] X. Wei et al., “Movable antennas meet intelligent reflecting surface: Friends or foes?,” IEEE Trans. Commun., vol. 73, no. 11, pp. 12756–12770, Nov. 2025.

[36] P. Wang, W. Mei, J. Fang, and R. Zhang, “Target-mounted intelligent reflecting surface for joint location and orientation estimation,” IEEE J. Sel. Areas Commun., vol. 41, no. 12, pp. 3768–3782, Dec. 2023.

[37] Study on Channel Model for Frequencies From 0.5 to 100 GHz, document TR-38.90, 3GPP, 2017. [Online]. Available: https://www.3gpp.org/ DynaReport/38901.htm

[38] Q. Wu and R. Zhang, “Beamforming optimization for wireless network aided by intelligent reflecting surface with discrete phase shifts,” IEEE Trans. Commun., vol. 68, no. 3, pp. 1838–1851, Mar. 2020.

[39] G. Yan, L. Zhu, and R. Zhang, “Passive reflection optimization for IRSaided multicast beamforming with discrete phase shifts,” IEEE Wireless Commun. Lett., vol. 12, no. 8, pp. 1424–1428, Aug. 2023.

[40] W. Mei and R. Zhang, “Performance analysis and user association optimization for wireless network aided by multiple intelligent reflecting surfaces,” IEEE Trans. Commun., vol. 69, no. 9, pp. 6296–6312, Sep. 2021.

[41] A. Beck and L. Tetruashvili, “On the convergence of block coordinate descent type methods,” SIAM J. Optim., vol. 23, no. 4, pp. 2037–2060, Jan. 2013.

[42] X. Li, X. Tang, C.-C. Wang, and X. Lin, “Gibbs-sampling-based optimization for the deployment of small cells in 3G heterogeneous networks,” in Proc. 11th Int. Symp. Workshops Model. Optim. Mobile, Ad Hoc Wireless Netw. (WiOpt), May 2013, pp. 444–451.

[43] Z. Kang, C. You, and R. Zhang, “3D placement for multi-UAV relaying: An iterative Gibbs-sampling and block coordinate descent optimization approach,” IEEE Trans. Commun., vol. 69, no. 3, pp. 2047–2062, Mar. 2021.

[44] K.-Y. Wang, A. M.-C. So, T.-H. Chang, W.-K. Ma, and C.-Y. Chi, “Outage constrained robust transmit optimization for multiuser MISO downlinks: Tractable approximations by conic optimization,” IEEE Trans. Signal Process., vol. 62, no. 21, pp. 5690–5705, Nov. 2014.

[45] Q. Ding, J. Yang, Y. Luo, and C. Luo, “Intelligent reflecting surfaces vs. full-duplex relays: A comparison in the air,” IEEE Commun. Lett., vol. 28, no. 2, pp. 397–401, Feb. 2024.

![](images/6ead77fa2655589900e336979446c5f5ce8946a7e68492a83b84025d534e2f7c.jpg)  
Changhao Liu (Graduate Student Member, IEEE) received the B.Eng. degree in communication engineering from the University of Electronic Science and Technology of China (UESTC), Chengdu, China, in 2024. He is currently pursuing the Ph.D. degree with the National Key Laboratory of Wireless Communications, UESTC. His current research interests include aerial communication, intelligent reflecting surface, and movable antenna.

![](images/220df5dbb1ab8150d349840b5778b70f91fae9a23171cd32424115d659d8520c.jpg)

Weidong Mei (Member, IEEE) received the B.Eng. degree in communication engineering and the M.Eng. degree in communication and information systems from the University of Electronic Science and Technology of China, Chengdu, China, in 2014 and 2017, respectively, and the Ph.D. degree from NUS Graduate School, National University of Singapore, in 2021, under the Integrative Sciences and Engineering Program (ISEP) Scholarship.

He was a Research Fellow with the Department of Electrical and Computer Engineering, National

University of Singapore, from July 2021 to January 2023. He is currently a Professor with the University of Electronic Science and Technology of China. His research interests include reconfigurable antennas, intelligent reflecting surface, wireless drone communications, and convex optimization techniques.

Dr. Mei has been listed in World’s Top 2% Scientists by Stanford University since 2021. He was a recipient of the Best Paper Award from the IEEE International Conference on Communications in 2021, the Best Student Paper Award from the International Conference on Future Communications and Networks in 2025, and the Outstanding Master’s Thesis Award from the Chinese Institute of Electronics in 2017. He mentored his students to win the IEEE ComSoc SPCC Technical Committee Student Challenge and Video Contest Award in 2024. He was honoured as the Exemplary Editor of IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY in 2024; and the Exemplary Reviewer of IEEE TRANSACTIONS ON COMMUNICATIONS in 2019 and 2020, the IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY in 2021 and 2024, the IEEE WIRELESS COMMUNICATIONS LETTERS in 2019, 2021, 2022, and 2023, and IEEE COMMUNICATIONS LETTERS in 2021 and 2022. He serves as an Associate Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE WIRELESS COMMUNICATIONS LETTERS, and IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY, and as the Co-Chair of the Workshop on Intelligent Movable and Reconfigurable Antennas for Future Wireless Communication and Sensing in IEEE Globecom from 2024 to 2025 and IEEE ICC from 2025 to 2026.

![](images/469a26bae6efde661da4a5d5c5c8c4bbe312ee926450fbeb8fbaf29442879918.jpg)

Peilan Wang (Member, IEEE) received the B.Eng. and Ph.D. degrees from the University of Electronic Science and Technology of China (UESTC), Chengdu, China, in 2018 and 2023, respectively. From 2022 to 2023, she was a Visiting Research Scholar with the Department of Electrical and Computer Engineering, National University of Singapore (NUS). She is currently working as a Postdoctoral Research Associate with the National Key Laboratory of Science and Technology on Communications, UESTC. Her current research interests include compressed sensing, millimeter-wave/THz communications, intelligent reflecting surfaces, signal processing, and integrated sensing and communications. She received the IEEE Jack Neubauer Memorial Award in 2025 and the IEEE Signal Processing Letters Best Paper Award in 2024.

![](images/b91dd25b5ea23fdaed8337e4dfe2a30bd6d9bf414fa119d3a5083f7e86cb2b79.jpg)

Yinuo Meng (Student Member, IEEE) is currently pursuing the B.Eng. degree in electronic information engineering from Glasgow College, University of Electronic Science and Technology of China (UESTC), Chengdu, China. His research interests include uncrewed aerial vehicle (UAV) communications, intelligent reflecting surfaces (IRS), and AI-enabled wireless communications.

![](images/29133528382c79e605517b29e2932f1b66ece41a86417b64e676c5e6dfb39239.jpg)

Zhi Chen (Senior Member, IEEE) received the B.Eng., M.Eng., and Ph.D. degrees in electrical engineering from the University of Electronic Science and Technology of China (UESTC) in 1997, 2000, and 2006, respectively. In April 2006, he joined the National Key Laboratory of Science and Technology on Communications, UESTC, where he has been a Professor since 2013. He was a Visiting Scholar with the University of California, Riverside, Riverside, from 2010 to 2011. He is also the Deputy Director of the Key Laboratory of Terahertz Technology,

Ministry of Education. His current research interests include terahertz communication, 5G mobile communications, and tactile Internet. He serves as an Editor for IEEE TRANSACTIONS ON COMMUNICATIONS.

![](images/cca1caf05ac5e9eac50f7b6d86f29b353afcbaae944d7094b59d7ae6b780c85e.jpg)

Boyu Ning (Member, IEEE) received the B.S. degree in communication engineering from the Ying-Cai Honors College, University of Electronic Science and Technology of China (UESTC), Chengdu, China, in 2018, and the Ph.D. degree from the National Key Laboratory of Wireless Communications, UESTC, in 2023. From 2022 to 2023, he was a Visiting Student with the Department of Electrical and Computer Engineering, National University of Singapore. His research interests include terahertz communication, movable antennas, intelli-

gent reflecting surface, massive MIMO, physical-layer security, and convex optimization.