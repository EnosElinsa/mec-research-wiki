# Low-Altitude UAV Tracking via Sensing-Assisted Predictive Beamforming

Yifan Jiang , Qingqing Wu , Senior Member, IEEE, Hongxun Hui , Senior Member, IEEE, Wen Chen , Senior Member, IEEE, and Derrick Wing Kwan Ng , Fellow, IEEE

Abstract—Sensing-assisted predictive beamforming shows significant promise for enhancing various future unmanned aerial vehicle (UAV) applications in integrated sensing and communication (ISAC) systems. However, the impact of such beamforming technique on the communication reliability was largely unexplored and challenging to characterize. To fill this research gap and tackle this issue, this paper proposes a cellular-connected UAV tracking scheme leveraging extended Kalman filtering (EKF), where the predicted UAV trajectory, sensing duration ratio, and target constant received signal-to-noise ratio (SNR) are jointly optimized to maximize the outage capacity at each time slot. To address the implicit nature of the objective function, analytical outage probability (OP) approximations are proposed based on second-order Taylor expansions, providing an efficient and full characterization of outage capacity. Subsequently, an efficient algorithm is proposed based on a combination of bisection search and successive convex approximation (SCA) to address the non-convex optimization problem with guaranteed convergence. To further reduce computational complexity, a second efficient algorithm is developed based on alternating optimization (AO). Simulation results validate the accuracy of the derived OP approximations, the effectiveness of the proposed algorithms, and the significant outage capacity enhancement over various benchmarks. Furthermore, we show that the optimized predicted UAV trajectory tends to be parallel to the base station’s uniform linear array antennas with a nonzero minimum distance, indicating a trade-off between decreasing path loss and enjoying wide beam coverage for outage capacity maximization.

Index Terms—Integrated sensing and communication (ISAC), unmanned aerial vehicle (UAV), tracking, low-altitude, outage, sensing-assisted predictive beamforming.

## I. INTRODUCTION

HE production of unmanned aerial vehicles (UAVs), T also known as drones, is anticipated to experience sustained rapid growth over the next decade, reaching a global market value of over 70 billion dollars by 2030 [1]. To date, the emerging low-altitude economy (LAE) has attracted significant worldwide attention, which unprecedently utilizes vertical space below an altitude of 1000 meters for numerious applications such as logistics, industrial monitoring, emergency rescue, and air taxis [2], [3], [4]. However, it can be envisioned that signal interference and network congestion will intensify considerably due to the explosive increase in UAV equipment. Under these challenging circumstances, it is crucial to guarantee the communication and tracking performance of UAV users and targets, since these metrics serve the foundations for the aforementioned applications. In addition, despite the independent progress made in UAV communication and tracking, such as short packet communication and global navigation satellite system [5], incompatibility among standalone systems designed for different functions causes inefficient use of hardware and spectrum resources, which degrades overall system performance.

In recent years, integrated sensing and communication (ISAC) has been proposed and widely investigated as an enabling technology for the upcoming sixth-generation (6G) network [6], [7], [8], [9]. By effectively utilizing the inherent reciprocity between sensing and communication, ISAC is expected to offer more precise and reliable wireless coverage for UAVs, thereby mitigating signal interference among multiple UAVs and enabling the access of a massive number of UAVs. Meanwhile, hardware and spectrum resources can be efficiently integrated, significantly reducing system overhead and improving overall spectral efficiency. Therefore, ISAC technologies present a vital solution to address the aforementioned issues, while simultaneously providing high-quality communication and tracking services for UAVs.

Among various existing signal processing and architecture designs for ISAC, sensing-assisted predictive beamforming is appealing due to its effectiveness in enhancing both target tracking accuracy and communication links for users concurrently [8], [10], [11]. Specifically, sensing-assisted predictive beamforming refers to the design of beamforming vectors based on both predicted and measured user information, typically user directions or positions. By utilizing the predicted user information, the system overhead associated with conventional beam training and feedback can be considerably reduced and the beam alignment accuracy can be improved from the perspective of Bayesian filtering [11]. Existing studies have demonstrated that sensing-assisted predictive beamforming can significantly enhance the performance of vehicular networks [8], [10], [11], [12], [13], [14], [15], [16]. For instance, a predictive beamforming framework was proposed in [10] for vehicular communications, leveraging the popular extended Kalman filtering (EKF) technique and substantially enhancing the achievable rate over conventional feedbackbased communication schemes. In [12], the average achievable sum-rate was maximized by optimizing the predictive beamformer for multi-user vehicular communications, exhibiting an upper-bound-approaching communication performance. Other works have extended sensing-assisted predictive beamforming designs to a wide range of cases with complex driving behaviour or trajectories [13], [14], end-to-end transmission [15], extended targets [16], etc.

Given the potential of sensing-assisted predictive beamforming, more recent works have explored its applications for system performance enhancement in low-altitude UAV networks [17], [18], [19]. In [17], a predictive beam management approach utilizing visual information was proposed based on the EKF for multi-UAV communication and tracking, showing a 20.34% data rate gain under a 64-antenna setup. In [18] and [19], UAV eavesdropper tracking schemes were proposed based on sensing-assisted predictive beamforming to improve the secrecy rates of legitimate users and the adversary UAV tracking accuracy. The above works are limited to scenarios with unknown or uncontrollable UAV trajectories. Nevertheless, unlike vehicular networks with constrained vehicle trajectories, there are many cases in low-altitude UAV networks where UAV trajectories can be optimized and controlled in real time within a large volume of three-dimensional (3D) space, such as cellular-connected drone surveillance, displays, and tourism [2], [3], [5]. In these cases, the achievable rate and Cramer-Rao bound (CRB) for UAV movement estimation are´ not only affected by predictive beamforming designs but also highly dependent on UAV trajectories [20], [21], [22]. Therefore, the joint optimization of UAV trajectory and predictive beamforming is promising for improving the communication and tracking performance of the aforementioned low-altitude UAV applications. However, such joint optimization is challenging due to the complicated coupling between the UAV trajectory and BS beamformer. Moreover, the UAV trajectory can only be partially optimized because of the inherently random aerial environmental variations and control errors in practice [5], [23], [24], thus requiring dedicated optimization approaches to address UAV trajectory uncertainties.

Furthermore, the majority of existing works on sensingassisted predictive beamforming have focused on spectral efficiency improvement, which is insufficient for characterizing communication reliability. However, modern low-altitude UAV applications have stringent requirements for communication reliability, such as an extremely low probability of signal outage [2], [5]. So far, relatively few investigations have examinated the improvements in beam alignment probability brought about by sensing-assisted predictive beamforming [11], [13], [16]. In [11], the impact of beamwidth on the beam alignment probability was studied for predictive beamformingenabled vehicle tracking. Following [11], dynamic beamwidth designs for vehicle tracking were proposed to improve the tracking or communication performance incorporating the beam alignment probability [13], [16]. Nevertheless, the beam alignment probability cannot characterize the reliable data rate or link capacity, which are crucial performance metrics for practical system designs. Instead, the outage probability (OP) and outage capacity are more appropriate and fundamental communication performance metrics to be studied [25]. Far from solely considering an uninvestigated performance metric, important insights can be drawn by studying the OP and outage capacity into the roles of sensing accuracy on communication reliability and the mechanisms of maximizing the reliable communication performance via predictive beamforming and UAV trajectory optimization. Meanwhile, it is intractable to derive the OP and outage capacity directly from the studied beam alignment probability owing to the different definitions, making it challenging to characterize the OP and outage capacity in the sensing-assisted predictive beamforming scheme.

Motivated by the aforementioned issues, we investigate the outage capacity characterization and maximization via UAV trajectory optimization in this paper. Specifically, a cellularconnected UAV is served and also concurrently tracked via EKF by a monostatic ISAC BS. Through remote control from the BS, the predicted UAV trajectory can be proactively controlled, although it is interfered by control noise modeled as a Gaussian random process. Within each short time slot, the UAV motion state is assumed to be deterministic yet unknown in advance. Meanwhile, the communication performance directly depends on a sensing duration ratio between the prediction and measurement durations at each time slot under the sensing-assisted predictive beamforming scheme. As a result, the system communication reliability at each time slot can be evaluated by OPs and outage capacities at the prediction and measurement stages, respectively. The main contributions of this paper are summarized as follows:

• A joint UAV tracking and outage capacity maximization scheme is proposed for reliable communication, where an optimization problem for outage capacity maximization is formulated and addressed at each time slot to optimize the predicted UAV trajectory, sensing duration ratio, and target constant received signal-to-noise ratios (SNRs), subject to constraints on UAV velocity and a maximum tolerable OP.

To address the implicit and non-convex objective function and constraints in the formulated problem, closed-form approximations of OPs for both the prediction and measurement stage are proposed based on second-order Taylor expansions, enabling the full characterization of outage capacity and a more tractable optimization problem formulation. To the best of our knowledge, this paper represents the first effort to characterize the outage capacity under the sensing-assisted predictive beamforming scheme in ISAC systems.

An efficient algorithm is proposed to handle the formulated optimization problem with guaranteed convergence, in which the formulated problem is decomposed into two feasibility problems addressed by the bisection search and SCA, respectively. Moreover, the updating rules between the two feasibility problems are heuristically designed based on the proved monotonicity of apporximated OPs with respect to (w.r.t.) the target constant received SNRs. To further reduce computational complexity and avoid unnecessary trials involving infeasible solutions, a second efficient algorithm is proposed capitalizing alternating optimization (AO), which maximizes the outage capacity within a few iterations.

TABLE I  
LIST OF KEY NOTATIONS
<table><tr><td rowspan=1 colspan=1>Symbols</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1> ${ \bf x } _ { n } , \breve { { \bf x } } _ { n } , \hat { { \bf x } } _ { n }$ </td><td rowspan=1 colspan=1>The actual, predicted and estimated UAV motion statevector at the nth time slot</td></tr><tr><td rowspan=1 colspan=1> $\mathbf { M } _ { \mathrm { p } , n } , \mathbf { M } _ { n }$ </td><td rowspan=1 colspan=1>The prediction and estimation MSE matrix</td></tr><tr><td rowspan=1 colspan=1> $\xi _ { \mathrm { p } , n } , \xi _ { \mathrm { e } , n }$ </td><td rowspan=1 colspan=1>The random variable for the complemetary outage eventat the prediction and estimation stage</td></tr><tr><td rowspan=1 colspan=1> $\tilde { \xi } _ { \mathfrak { p } , n } , \tilde { \xi } _ { \mathfrak { e } , n }$ </td><td rowspan=1 colspan=1>The approximated random variable for the complemetaryoutage event</td></tr><tr><td rowspan=1 colspan=1> $\gamma _ { n } , \gamma _ { n }$ </td><td rowspan=1 colspan=1>The target constant received SNR at the prediction andestimation stage</td></tr><tr><td rowspan=1 colspan=1> $\underline { { \boldsymbol { \gamma } } } _ { n }$ </td><td rowspan=1 colspan=1>The target constant received SNR vector</td></tr><tr><td rowspan=1 colspan=1> $\zeta _ { \mathfrak { p } , n } , \zeta _ { \mathfrak { e } , n }$ </td><td rowspan=1 colspan=1>The OP at the prediction and estimation stage</td></tr><tr><td rowspan=1 colspan=1> $\tilde { \zeta } _ { \mathfrak { p } , n } , \tilde { \zeta } _ { \mathfrak { e } , n }$ </td><td rowspan=1 colspan=1>The approximated OP at the prediction and estimationstage</td></tr><tr><td rowspan=1 colspan=1> $\overline { { C _ { \mathfrak { p } , n } , C _ { \mathfrak { e } , n } } }$ </td><td rowspan=1 colspan=1>The outage capacity at the prediction and estimation stage</td></tr><tr><td rowspan=1 colspan=1> $\overline { { C _ { n } } }$ </td><td rowspan=1 colspan=1>The overall outage capacity</td></tr><tr><td rowspan=1 colspan=1> $w _ { n }$ </td><td rowspan=1 colspan=1>The sensing duration ratio</td></tr><tr><td rowspan=1 colspan=1> ${ \bf q } _ { n } , \breve { { \bf q } } _ { n } , \hat { { \bf q } } _ { n }$ </td><td rowspan=1 colspan=1>The ground-truth, predicted and estimated UAV trajectory</td></tr><tr><td rowspan=1 colspan=1> $\kappa ( \cdot ) , \varkappa ( \cdot )$ </td><td rowspan=1 colspan=1>The function denoting the beam alignment accuracy andthe maximum OP</td></tr></table>

• Simulation results validate the effectiveness of our proposed OP approximations, algorithms, and outage capacity maximization scheme. In addition, in the prediction mean square error (MSE)-dominant case, our proposed scheme achieves a significant outage capacity improvement compared to benchmarks. Moreover, our results reveal that the optimized predicted UAV trajectory ends up with being parallel to the BS uniform linear array (ULA) antennas with a nonzero minimum distance, which also demonstrates a trade-off between reducing path loss and enlarging beam coverage area.

Notation: ${ \bf 0 } _ { m }$ and ${ \bf 1 } _ { m }$ denote a $m \times 1$ column vector with all elements equal to 0 and 1, respectively. O(·) represents the big-O notation for computational complexity. $\mathbb { E } _ { x } [ \cdot ]$ is statistical expectation w.r.t. the distribution of $x . \ { \mathcal { N } } ( \mathbf { x } , \mathbf { Q } )$ denotes a real-valued Gaussian distribution with a mean vector x and covariance matrix Q and ∼ means “distributed $\mathrm { a s } ^ { \prime \prime } . \preceq$ is the element-wise component inequality. ⊗ is the Kronecker product. diag(b<sub>1</sub>, . . . , b<sub>L</sub>) denotes a diagonal matrix with $b _ { 1 } , \dotsc , b _ { L }$ being its diagonal elements. For an arbitrary matrix $\mathbf { A } , \mathbf { A } ^ { T } , \mathbf { A } ^ { - 1 }$ , det(A), and $[ \mathbf { A } ] _ { i j }$ denote its transpose, inverse, determinant, and $( i , j )$ -th element, respectively. $\nabla f ( \cdot )$ represents the gradient of the function $f ( \cdot )$ . Other key notations are summarized in Table I.

## II. SYSTEM MODEL

We consider a terrestrial BS that employs downlink ISAC signals to simultaneously track and communicate with a single-antenna cellular-connected UAV.<sup>1</sup> As an initial study, it is assumed that the UAV flies at a fixed altitude of H m, and the BS is equipped with ULAs comprising $N _ { \mathrm { t } }$ transmit antennas and $N _ { \mathrm { r } }$ receive antennas.<sup>2</sup> Furthermore, the uncertainty of the UAV motion state (i.e., the UAV position and velocity) is considered owing to practical issues such as control errors [23], [24]. Moreover, with a sufficiently short time interval ∆T s, the UAV motion state can be assumed to be invariant [26]. Therefore, without loss of generality, a three-dimensional (3D) Cartesian coordinate system is considered, where the BS is located at the origin and the UAV motion state vector at the n-th time slot can be denoted by $\mathbf { x } _ { n } = [ x _ { n } , v _ { n } ^ { \mathrm { x } } , y _ { n } , v _ { n } ^ { \mathrm { y } } ] ^ { T }$ with $x _ { n } , v _ { n } ^ { \mathrm { x } } , y _ { n } ,$ and $v _ { n } ^ { \mathrm { y } }$ denoting the x-axis coordinate, the velocity along x-axis, the y-axis coordinate, and the velocity along y-axis, respectively. Despite the inherent uncertainty in UAV motion state, it is still possible to partially plan the UAV trajectory by designing the predicted state vector at the $( n { + } 1 ) \cdot$ th time slot, which can be realized by remote control from the BS [5], [17], [24]. The other parts of our considered system are specified in the following subsections.

![](images/612dabf44ddc8b350929464c992c924dee196eefce88e762b48ae1df2a0d4c94.jpg)  
Fig. 1. System model illustration.

## A. UAV Mobility Model

The entire UAV flight dynamic can be described exploiting a discrete-time state evolution model expressed as [27]

$$
\begin{array} { r } { { \bf x } _ { n } = { \bf G } { \bf x } _ { n - 1 } + { \bf u } _ { n } + { \bf z } _ { \mathrm { p } , n } , \forall n \in \{ 1 , 2 , \ldots , N \} , } \end{array}\tag{1}
$$

where $\mathbf { G } \in \mathbb { R } ^ { 4 \times 4 }$ denotes the transition matrix, $\mathbf { u } _ { n } \in \mathbb { R } ^ { 4 \times 1 }$ denotes the motion control input from the BS, N denotes the total number of time slots, and ${ \bf z } _ { \mathrm { p } , n } \sim \mathcal { N } ( { \bf 0 } , { \bf Q } _ { \mathrm { p } } )$ denotes the process noise owing to control errors [27], respectively. The expressions of G and $\mathbf { Q } _ { \mathrm { p } } \in \mathbb { R } ^ { 4 \times 4 }$ can be given by

$$
\mathbf { G } = \mathbf { I } _ { 2 } \otimes { \left[ \begin{array} { l l } { 1 } & { \Delta T } \\ { 0 } & { 1 } \end{array} \right] } , \mathbf { Q } _ { \mathrm { p } } = \mathbf { I } _ { 2 } \otimes { \left[ \begin{array} { l l } { { \frac { 1 } { 3 } } \Delta T ^ { 3 } } & { { \frac { 1 } { 2 } } \Delta T ^ { 2 } } \\ { { \frac { 1 } { 2 } } \Delta T ^ { 2 } } & { \Delta T } \end{array} \right] } { \tilde { q } } ,\tag{2}
$$

, respectively, where $\tilde { q }$ denotes the process noise intensity.<sup>3</sup>

Note that $\{ \mathbf { x } _ { n } \} , \forall n$ , is indeed a random process and cannot be directly acquired by either the UAV or the BS. Fortunately, ${ \bf x } _ { n }$ can be predicted at the (n−1)-th time slot and subsequently estimated at the n-th time slot, which are denoted by $\breve { \mathbf { x } } _ { n } =$ $[ \breve { x } _ { n } , \breve { v } _ { n } ^ { \mathrm { x } } , \breve { y } _ { n } , \breve { v } _ { n } ^ { \mathrm { y } } ] ^ { T }$ and $\begin{array} { r l r } { \hat { \bf x } _ { n } } & { = } & { [ \hat { x } _ { n } , \hat { v } _ { n } ^ { \mathrm { x } } , \hat { y } _ { n } , \hat { v } _ { n } ^ { \mathrm { y } } ] ^ { T } } \end{array}$ , respectively. More specifically, by designing the motion control input as $\mathbf { u } _ { n } = \breve { \mathbf { x } } _ { n } - \mathbf { G } \hat { \mathbf { x } } _ { n - 1 }$ , the relationship between ${ \bf x } _ { n }$ and $\breve { \mathbf { x } } _ { n }$ can be compactly expressed as

$$
{ \bf x } _ { n } = \breve { { \bf x } } _ { n } + { \bf G } ( { \bf x } _ { n - 1 } - \hat { { \bf x } } _ { n - 1 } ) + { \bf z } _ { \mathrm { p } , n } .\tag{3}
$$

Therefore, the UAV trajectory optimization can be performed by appropriately optimizing $\breve { \mathbf { x } } _ { n }$ . The detailed procedures for obtaining $\hat { \mathbf { x } } _ { n }$ are dependent on $\breve { \mathbf { x } } _ { n }$ and are specified in the following subsection. Furthermore, a crucial assumption about the prediction and estimation errors is specified as follows:

Assumption 1 (Small prediction/estimation error): In this paper, we assume that the prediction and estimation errors, although inherently exist and follow different probability distributions, are sufficiently small. Thus, the ground-truth value of the state vector can be approximated by the predicted and estimated values, i.e., ${ \bf x } _ { n } \approx \breve { \bf x } _ { n } \approx \hat { \bf x } _ { n }$ [10], [28], [29].

Remark 1: Although assumption 1 may appear idealistic, small prediction and estimation errors are practically achievable in scenarios such as millimeter-wave ISAC systems. Specifically, highly accurate localization/tracking can be achieved thanks to favorable channel conditions and large antenna array gain [11], [14], [15], [16]. Moreover, this study primarily focuses on characterizing the impact of UAV trajectories on communication reliability under the sensing-assisted predictive beamforming scheme. Therefore, assumption 1 is well-justified and does not diminish the necessity and value of the proposed investigation.

## B. Sensing-Assisted Beamforming

In our considered ISAC system, a two-stage predictive beamforming scheme is implemented by the BS to achieve real-time UAV tracking and communication [10]. At each stage, the BS adaptively designs its beamforming vector according to the predicted or estimated UAV motion state, which is detailed as follows:

1) Prediction Stage: At the beginning $w _ { n }$ ratio of the nth time slot, the BS generates the predicted state vector $\breve { \mathbf { x } } _ { n }$ and transmits ISAC signals with the beamforming vector expressed as $\breve { \mathbf { f } } _ { n } = \mathbf { a } ( \breve { \theta } _ { n } ) = \mathbf { a } ( \arctan ( \breve { y } _ { n } / \breve { x } _ { n } ) )$ , where $w _ { n }$ and $\bar { \theta } _ { n }$ denote the sensing duration ratio and the predicted azimuth angle, respectively. Based on assumption 1, predictive beamforming can achieve sufficient accuracy such that the UAV is reliably illuminated by the main lobe of the beam, enabling the BS to successfully receive echo signals from the UAV. Meanwhile, the BS measures the azimuth angle $\theta _ { n }$ and distance $d _ { n }$ of the UAV from echo signals via the matched-fitering technique [22]. The measurement model is explicitly given by

$$
\mathbf { w } _ { n } = \mathbf { h } ( \mathbf { x } _ { n } ) + \mathbf { z } _ { \mathrm { m } , n } = \left[ { \frac { \arctan ( y _ { n } / x _ { n } ) } { \sqrt { x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } } } } \right] + \left[ z _ { 2 , n } \right] ,\tag{4}
$$

where ${ \bf w } _ { n } = [ \hat { \theta } _ { n } , \hat { d } _ { n } ] ^ { T }$ represents the measured results, $\hat { \theta } _ { n }$ denotes the measured azimuth angle, $\hat { d } _ { n }$ denotes the measured distance, ${ \bf z } _ { \mathrm { m } , n }$ represents the measurement noise vector with $z _ { i , n } \sim \mathcal { N } ( 0 , \sigma _ { i , n } ^ { 2 } ) , i = 1 , 2$ , and $\sigma _ { i , n } ^ { 2 } , i = 1 , 2$ denote the corresponding measurement noise variance, respectively. Given the sparse blockages and scatterings in the vertical dimension, the communication channel between the BS and UAV can be assumed to be line-of-sight (LoS)-dominant with free-space path loss [26], [30], [31].<sup>4</sup> Consequently, the expressions of $\sigma _ { i , n } ^ { 2 } , i = 1 , 2$ are given by

$$
\sigma _ { 1 , n } ^ { 2 } = { \frac { a _ { 1 } ^ { 2 } ( x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } ) ^ { 2 } ( x _ { n } ^ { 2 } + y _ { n } ^ { 2 } ) } { \rho _ { \mathrm { r } } w _ { n } y _ { n } ^ { 2 } } } ,\tag{5}
$$

$$
\sigma _ { 2 , n } ^ { 2 } = \frac { a _ { 2 } ^ { 2 } ( x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } ) ^ { 2 } } { \rho _ { \mathrm { r } } w _ { n } } ,\tag{6}
$$

and the measurement noise covariance matrix for ${ \bf z } _ { \mathrm { m } , n }$ can be derived as $\mathbf { Q } _ { \mathrm { m } , n } = \mathrm { d i a g } ( \sigma _ { 1 , n } ^ { 2 } , \sigma _ { 2 , n } ^ { 2 } )$ . In (5) and $( 6 ) , a _ { i } , i = 1 , 2$ represent the corresponding measurement capability coefficients calculated according to the system configurations and signal processing designs [10], [28], and $\rho _ { \mathrm { r } } \in \mathbb { R }$ denotes the sensing power gain coefficient given by [29]

$$
\rho _ { \mathrm { r } } = { \frac { P _ { \mathrm { A } } N _ { \mathrm { s y m } } N _ { \mathrm { t } } N _ { \mathrm { r } } } { \sigma ^ { 2 } } } \left( { \frac { \sigma _ { \mathrm { R C S } } \lambda ^ { 2 } } { ( 4 \pi ) ^ { 3 } } } \right) ,\tag{7}
$$

where $P _ { \mathrm { { A } } }$ denotes the BS transmit power, $N _ { \mathrm { s y m } }$ is matchedfitering gain accumulated during the whole time slot, $\sigma ^ { 2 }$ denotes the additive white Gaussian noise power at the receiver, $\sigma _ { \mathrm { R C S } }$ signifies the target radar cross-section, and λ denotes the carrier wavelength [22].

2) Estimation Stage: During the remaining period of the nth time slot, the BS generates the estimated state vector $\hat { \mathbf { x } } _ { n }$ following the standard EKF procedures and then transmit ISAC signals with an updated transmit beamforming vector expressed as $\hat { \mathbf { f } } _ { n } ~ = ~ \mathbf { a } ( \hat { \theta } _ { n } ) ~ = ~ \mathbf { a } ( \arctan ( \hat { y } _ { n } / \hat { x } _ { n } ) )$ for a statistically more precise beam alignment.<sup>5</sup> The standard EKF procedures are given by the following steps [33].

a) Obtaining the predicted state vector $\breve { \mathbf { x } } _ { n }$

b) Linearization: $\begin{array} { r } { { \bf H } _ { n } = \frac { \partial { \bf h } } { \partial { \bf x } _ { n } } | _ { { \bf x } _ { n } = \breve { { \bf x } } _ { n } } , \forall n . } \end{array}$

c) Calculating the prediction MSE matrix:

$$
\begin{array} { r } { \mathbf { M } _ { \mathrm { p } , n } = \mathbf { G } \mathbf { M } _ { n - 1 } \mathbf { G } ^ { H } + \mathbf { Q } _ { \mathrm { p } } . } \end{array}\tag{8}
$$

d) Calculating the Kalman gain matrix:

$$
{ \bf K } _ { n } = { \bf M } _ { \mathrm { p } , n } { \bf H } _ { n } ^ { H } ( { \bf Q } _ { \mathrm { m } , n } + { \bf H } _ { n } { \bf M } _ { \mathrm { p } , n } { \bf H } _ { n } ^ { H } ) ^ { - 1 } .\tag{9}
$$

e) Obtaining the estimated state vector:

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { n } = \check { \mathbf { x } } _ { n } + \mathbf { K } _ { n } \big ( \mathbf { w } _ { n } - \mathbf { h } \big ( \check { \mathbf { x } } _ { n } \big ) \big ) . } \end{array}\tag{10}
$$

f) Calculating the estimation MSE matrix:

$$
\mathbf { M } _ { n } = \left( \mathbf { I } - \mathbf { K } _ { n } \mathbf { H } _ { n } \right) \mathbf { M } _ { \mathbf { p } , n } = \left( \mathbf { H } _ { n } ^ { H } \mathbf { Q } _ { \mathbf { m } , n } ^ { - 1 } \mathbf { H } _ { n } + \mathbf { M } _ { \mathbf { p } , n } ^ { - 1 } \right) ^ { - 1 } .\tag{11}
$$

The detailed derivation of (11) can be referred to [10]. In (9) and (11), the expression of $\mathbf { H } _ { n }$ is given by

$$
\mathbf { H } _ { n } = \left[ \frac { - \frac { \check { y } _ { n } } { \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } } 0 \frac { \check { x } _ { n } } { \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } } 0 } { \frac { \mathscr { x } _ { n } } { \sqrt { \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } + H ^ { 2 } } } 0 \frac { \check { y } _ { n } } { \sqrt { \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } + H ^ { 2 } } } 0 } \right] .\tag{12}
$$

## C. Outage Capacity Characterization

The outage capacity refers to the maximum rate maintained over the fading block such that the OP is less than a predetermined outage threshold $\varepsilon _ { \mathrm { o u t } }$ [25], which can be characterized as follows in our considered system. Given the considered predictive beamforming scheme and LoS-dominant channel model, the instantaneous received SNRs of the UAV at the prediction and estimation stage of the nth time slot can be represented by

![](images/d4e92e07281773816eb0149fb139dd84622159267d8fe7a6ae579a8804de96e9.jpg)  
Fig. 2. A geometric illustration of COR and approximated COR (aCOR).

$$
\gamma _ { \mathsf { p } , n } = \frac { \tilde { P } | \mathbf { a } ( \theta _ { n } ) ^ { H } \mathbf { a } ( \check { \theta } _ { n } ) | } { x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } } , \gamma _ { \mathsf { e } , n } = \frac { \tilde { P } | \mathbf { a } ( \theta _ { n } ) ^ { H } \mathbf { a } ( \hat { \theta } _ { n } ) | } { x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } } ,\tag{13}
$$

respectively, where the coefficient $\tilde { P }$ is defined as $\tilde { P } \stackrel { \triangle } { = }$ $P _ { \mathrm { A } } \bar { \beta } _ { 0 } / \sigma ^ { 2 }$ , and $\beta _ { 0 } = ( \lambda / 4 \pi ) ^ { 2 }$ represents the channel power gain at the reference distance of 1 m. $\mathbf { a } ( \cdot )$ denotes the transmitting steering vector expressed as

$$
\mathbf { a } ( \theta _ { n } ) = [ 1 , \exp ( \mathfrak { j } \pi \cos \theta _ { n } ) , \dots , \exp ( \mathfrak { j } ( N _ { \mathrm { t } } - 1 ) \pi \cos \theta _ { n } ) ] ^ { T } .\tag{14}
$$

Since the random factors in $\gamma _ { \mathrm { p } , n }$ and $\gamma _ { \mathrm { e } , n }$ (i.e., ${ \theta } _ { n } , ~ \breve { \theta } _ { n } , ~ \hat { \theta } _ { n } ,$ $x _ { n } ,$ and $y _ { n } )$ are assumed constant within $\Delta T \ s ,$ the BS-UAV channel fading can be modeled as slow flat fading with a coherence time of $\Delta T \ \mathrm { ~ s ~ } \ [ 2 5 ] .$ . Consequently, the complementary outage events (i.e., the events of the UAV not being in outage) at the prediction and estimation stage of the nth time slot are expressed as $\xi _ { \mathrm { p } , n } \triangleq \gamma _ { \mathrm { p } , n } - \check { \gamma } _ { n } \geq 0$ and $\xi _ { \mathrm { e } , n } \triangleq \gamma _ { \mathrm { e } , n } - \hat { \gamma } _ { n } \geq 0$ , respectively, where $\breve { \gamma } _ { n }$ and $\hat { \gamma } _ { n }$ denote the target constant received SNRs ensuring the OP less than $\varepsilon _ { \mathrm { o u t } }$ at the corresponding stage. Then, the OPs at the two stages of the nth time slot can be uniformly expressed as

$$
\zeta _ { \iota , n } = \mathbb { P } \left( \xi _ { \iota , n } < 0 \right) = 1 - \int _ { \mathscr { Q } _ { \iota , n } } f _ { \iota } ( \xi _ { \iota , n } ) \mathrm { d } \xi _ { \iota , n } , \iota \in \{ \mathrm { p } , \mathrm { e } \} ,\tag{15}
$$

where the set $\mathcal { Q } _ { \iota , n } = \{ \xi _ { \iota , n } | \xi _ { \iota , n } \geq 0 \}$ is named as the complementary outage region $( \mathbf { C O R } ) , f _ { \iota } ( \cdot )$ denotes the probability density function (PDF) of $\xi _ { \iota , n } ,$ , and the subscript $\iota = { \mathfrak { p } }$ and $\iota = { \mathfrak { e } }$ denote the prediction and estimation stage, respectively. As illustrated in Fig. 2, the COR is equivalent to the set constituted by all $( x _ { n } , y _ { n } )$ satisfying $\xi _ { \iota , n } \ \geq \ 0$ due to (13). Since $\zeta _ { \iota , n }$ monotonically decreases with the decreasing of $\gamma _ { \iota , n } ,$ $\zeta _ { \mathrm { p } , n } ( \breve { \gamma } _ { n } ) = \zeta _ { \mathrm { e } , n } ( \hat { \gamma } _ { n } ) = \varepsilon _ { \mathrm { o u t } }$ hold. Accordingly, the outage capacities normalized by the bandwidth at the prediction and estimation stage of the nth time slot are expressed as

$$
C _ { \mathfrak { p } , n } = \log _ { 2 } ( 1 + \zeta _ { \mathfrak { p } , n } ^ { - 1 } ( \varepsilon _ { \mathrm { o u t } } ) ) = \log _ { 2 } ( 1 + \breve { \gamma } _ { n } ) ,\tag{16}
$$

$$
C _ { \mathrm { e } , n } = \log _ { 2 } ( 1 + \zeta _ { \mathrm { e } , n } ^ { - 1 } ( \varepsilon _ { \mathrm { o u t } } ) ) = \log _ { 2 } ( 1 + \hat { \gamma } _ { n } )\tag{17}
$$

respectively, where $\zeta _ { \iota , n } ^ { - 1 } ( \cdot )$ denotes the inverse cumulative distribution function [25]. The overall outage capacity at the nth time slot is represented by $C _ { n } = w _ { n } C _ { \mathfrak { p } , n } + ( 1 - w _ { n } ) C _ { \mathfrak { e } , n } .$

## D. Problem Formulation

In this paper, we propose a joint UAV tracking and outage capacity maximization scheme. To be specific, the predicted UAV trajectory $\breve { \mathbf { q } } _ { n } = [ \breve { x } _ { n } , \breve { y } _ { n } ] ^ { T }$ , sensing duration ratio $w _ { n }$ and target constant received SNR vector $\boldsymbol { \gamma _ { n } } ^ { - } = [ \breve { \gamma } _ { n } , \hat { \gamma } _ { n } ] ^ { T }$ are jointly optimized to maximize the overall outage capacity at each time slot. The corresponding optimization problem is formulated as

$$
( \mathrm { P 1 } ) : \operatorname* { m a x } _ { \{ \check { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { n } \} } C _ { n }
$$

$$
\begin{array} { r } { \mathrm { s . t . } \left\| \check { \mathbf { q } } _ { n } - \hat { \mathbf { q } } _ { n - 1 } \right\| \leq v _ { \mathrm { A , m a x } } \Delta T , } \end{array}\tag{18}
$$

$$
\breve { y } _ { n } \geq y _ { \mathrm { m i n } } ,\tag{18a}
$$

$$
w _ { \mathrm { m i n } } \le w _ { n } \le w _ { \mathrm { m a x } } ,\tag{18b}
$$

$$
\varkappa ( \breve { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { n } ) \leq 0 ,\tag{18c}
$$

(18d)

$$
\mathbf { 0 } \prec \gamma _ { n } \prec \gamma _ { \operatorname* { m a x } } \mathbf { 1 } _ { 2 } ,\tag{18e}
$$

where $\hat { \mathbf { q } } _ { n - 1 } ~ = ~ [ \hat { x } _ { n - 1 } , \hat { y } _ { n - 1 } ] ^ { T }$ denotes the estimated UAV trajectory at the $( n \mathrm { ~ - ~ } 1 ) { \cdot } { \mathrm { t h } }$ time slot, $v _ { \mathrm { A , m a x } }$ denotes the UAV maximum velocity, $\begin{array} { r } { \varkappa ( \check { \mathbf q } _ { n } , w _ { n } , \gamma _ { n } ) = \operatorname* { m a x } \left( \zeta _ { \mathsf { p } , n } , \zeta _ { \mathsf { e } , n } \right) - } \end{array}$ $\varepsilon _ { \mathrm { o u t } }$ represents the maximum OP at the nth time slot and $\gamma _ { \mathrm { m a x } } \ \stackrel { - } { = } \ \tilde { P } N _ { \mathrm { t } } / ( y _ { \mathrm { m i n } } ^ { 2 } + H ^ { 2 } )$ denotes the maximum target constant received SNR due to the maximum beamforming gain and the minimum path loss, respectively. In (P1), (18a) represents the maximum UAV velocity constraint, while (18b) represents a minimum y-axis coordinate constraint of a flyable zone.<sup>6</sup> (18c), (18d) and (18e) denote the sensing duration ratio range, maximum tolerable OP, and SNR range constraints, respectively. It is non-trivial to solve (P1) because the objective function and the constraint (18d) are implicit functions of $\breve { \mathbf { q } } _ { n } ,$ $w _ { n }$ , and $\gamma _ { n } .$

## III. PROPOSED OP APPROXIMATIONS

To address the implicit objective function and constraint (18d) in (P1), OP approximations with analytical expressions are proposed in this section for the prediction and estimation stages by approximating the CORs via Taylor expansions, which makes it tractable to solve (P1).

## A. Prediction Stage

Let us denote the ground-truth UAV trajectory by ${ \bf q } _ { n } =$ $[ x _ { n } , y _ { n } ] ^ { T }$ . Then, based on assumption 1, it can be reasonably inferred that the UAV is consistently illuminated by the main lobe of the downlink transmitted beam thanks to the small prediction/estimation error. As a result, the beamforming gain from the BS can be expressed as

$$
| \mathbf { a } ( \theta _ { n } ) ^ { H } \mathbf { a } ( \breve { \theta } _ { n } ) | = \frac { \sin \left( \frac { N _ { \mathrm { t } } \pi } { 2 } \kappa ( \mathbf { q } _ { n } ; \breve { \mathbf { q } } _ { n } ) \right) } { \sin \left( \frac { \pi } { 2 } \kappa ( \mathbf { q } _ { n } ; \breve { \mathbf { q } } _ { n } ) \right) } ,\tag{19}
$$

where the expression of $\kappa ( \mathbf { q } _ { n } ; \breve { \mathbf { q } } _ { n } )$ is given by

$$
\begin{array} { l } { \kappa ( \mathbf { q } _ { n } ; \breve { \mathbf { q } } _ { n } ) \triangleq \cos \left( \breve { \theta } _ { n } \right) - \cos \left( \theta _ { n } \right) } \\ { = \displaystyle \frac { \breve { x } _ { n } } { \sqrt { \breve { x } _ { n } ^ { 2 } + \breve { y } _ { n } ^ { 2 } } } - \frac { x _ { n } } { \sqrt { x _ { n } ^ { 2 } + y _ { n } ^ { 2 } } } . } \end{array}\tag{20}
$$

As such, the complementary outage event at the prediction stage, i.e., $\xi _ { \mathfrak { p } , n } \geq 0 ;$ , can be reformulated as

$$
\frac { \sin \left( \frac { N _ { \mathrm { t } } \pi } { 2 } \kappa ( \mathbf { q } _ { n } ; \check { \mathbf { q } } _ { n } ) \right) } { \sin \left( \frac { \pi } { 2 } \kappa ( \mathbf { q } _ { n } ; \check { \mathbf { q } } _ { n } ) \right) } \geq \frac { \check { \gamma } _ { n } ( x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } ) } { \tilde { P } } .\tag{21}
$$

<sup>6</sup>In practice, the UAV position with $\breve { y } _ { n } = 0$ leads to the infinite azimuth angle measurement noise variance. Thus, we consider a case where the UAV trajectory is constrained in an area with a nonzero minimum y-axis coordinate denoted by $y _ { \mathrm { m i n } } > 0$

However, the left-hand side (LHS) of (21) is intractable for calculating the integral in (15) and also overly complicated for the Taylor expansion w.r.t. $\breve { \mathbf { q } } _ { n }$ . To tackle this issue, we propose a two-step approximation detailed as follows.

In the first step, the LHS of (21) is approximated by its second-order Taylor expansion w.r.t. the function $\kappa ( \cdot )$ at the point $\breve { \kappa } _ { n } = 0$ , yielding:

$$
\begin{array} { r l } & { \frac { \sin \big ( \frac { N _ { \mathrm { t } } \pi } { 2 } \kappa ( \mathbf { q } _ { n } ; \check { \mathbf { q } } _ { n } ) \big ) } { \sin \big ( \frac { \pi } { 2 } \kappa \big ( \mathbf { q } _ { n } ; \check { \mathbf { q } } _ { n } ) \big ) } \approx N _ { \mathrm { t } } - M \kappa ( \mathbf { q } _ { n } ; \check { \mathbf { q } } _ { n } ) ^ { 2 } , } \end{array}\tag{22}
$$

with $\begin{array} { r } { M = \frac { N _ { \mathrm { t } } \pi ^ { 2 } ( N _ { \mathrm { t } } ^ { 2 } - 1 ) } { \gamma _ { A } } } \end{array}$ . Then, the COR can be approximated by $Q _ { \mathrm { p } , n } \approx \mathcal { Q } _ { \mathrm { p a } , n } ^ { \mathrm { ~ - ~ } } = \{ \xi _ { \mathrm { p a } , n } | \xi _ { \mathrm { p a } , n } \geq 0 \}$ with

$$
\xi _ { \mathtt { p a } , n } = \kappa ( \mathbf { q } _ { n } ; \breve { \mathbf { q } } _ { n } ) ^ { 2 } + \frac { \breve { \gamma } _ { n } ( x _ { n } ^ { 2 } + y _ { n } ^ { 2 } + H ^ { 2 } ) } { \tilde { P } M } - \frac { N _ { \mathrm { t } } } { M } \geq 0 .\tag{23}
$$

In (23), the function $\kappa ( \mathbf { q } _ { n } ; \breve { \mathbf { q } } _ { n } )$ remains challenging to handle due to its fractional structure. Thus, the second step is to approximate $\xi _ { \mathrm { p a } , n }$ by the second-order Taylor expansion w.r.t. the ground-truth UAV trajectory $\mathbf { q } _ { n }$ at the point ${ \bf q } _ { n } = \breve { \bf q } _ { n }$ and reformulate (23) as

$$
\boldsymbol { \xi } _ { \mathrm { p a } , n } \approx \tilde { \xi } _ { \mathrm { p } , n } = \frac { 1 } { 2 } \boldsymbol { \dot { \mathbf { q } } } _ { n } ^ { T } \boldsymbol { \tilde { \xi } } _ { \mathrm { p } , n } ^ { ( 2 ) } \boldsymbol { \dot { \mathbf { q } } } _ { n } + ( \boldsymbol { \tilde { \xi } } _ { \mathrm { p } , n } ^ { ( 1 ) } ) ^ { T } \boldsymbol { \dot { \mathbf { q } } } _ { n } + \boldsymbol { \tilde { \xi } } _ { \mathrm { p } , n } ^ { ( 0 ) } \geq 0 ,\tag{24}
$$

where the vector ${ \check { \mathbf { q } } } _ { n } = \mathbf { q } _ { n } - { \check { \mathbf { q } } } _ { n } = [ { \acute { x } } _ { n } , { \acute { y } } _ { n } ] ^ { T }$ represents the deviation of predicted UAV trajectory from the groundtruth UAV trajectory, $\tilde { \pmb { \xi } } _ { \mathfrak { p } , n } ^ { ( 2 ) }$ and $\tilde { \pmb { \xi } } _ { \mathfrak { p } , n } ^ { ( 1 ) }$ denote the Hessian matrix and gradient of the LHS of (23) w.r.t. the ground-truth UAV trajectory ${ \bf q } _ { n }$ , respectively. The specific expressions of $\tilde { \pmb { \xi } } _ { \mathbf { p } , n } ^ { ( 2 ) } .$ $\tilde { \pmb { \xi } } _ { \mathfrak { p } , n } ^ { ( 1 ) }$ and $\tilde { \xi } _ { \mathtt { p } , n } ^ { ( 0 ) }$ are given by

$$
\tilde { \pmb { \xi } } _ { \mathrm { p } , n } ^ { ( 2 ) } = \left[ 2 \tilde { \xi } _ { n } ^ { ( 2 0 ) } \ \tilde { \xi } _ { n } ^ { ( 1 1 ) } \right] , \tilde { \pmb { \xi } } _ { \mathrm { p } , n } ^ { ( 1 ) } = \left[ \tilde { \xi } _ { n } ^ { ( 1 0 ) } \right] ,\tag{25}
$$

with

$$
\tilde { \xi } _ { n } ^ { ( 2 0 ) } = \frac { \check { y } _ { n } ^ { 4 } } { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } } + \frac { \check { \gamma } _ { n } } { M \tilde { P } } , \tilde { \xi } _ { n } ^ { ( 1 1 ) } = \frac { - 2 \check { x } _ { n } \check { y } _ { n } ^ { 3 } } { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } } ,\tag{26}
$$

$$
\tilde { \xi } _ { n } ^ { ( 0 2 ) } = \frac { \breve { x } _ { n } ^ { 2 } \breve { y } _ { n } ^ { 2 } } { ( \breve { x } _ { n } ^ { 2 } + \breve { y } _ { n } ^ { 2 } ) ^ { 3 } } + \frac { \breve { \gamma } _ { n } } { M \tilde { P } } , \ : \tilde { \xi } _ { n } ^ { ( 1 0 ) } = \frac { 2 \breve { \gamma } _ { n } \breve { x } _ { n } } { M \tilde { P } } ,\tag{27}
$$

$$
\tilde { \xi } _ { n } ^ { ( 0 1 ) } = \frac { 2 \check { \gamma } _ { n } \check { y } _ { n } } { M \tilde { P } } , \tilde { \xi } _ { \mathrm { p } , n } ^ { ( 0 ) } = \frac { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } + H ^ { 2 } ) \check { \gamma } _ { n } } { \tilde { P } M } - \frac { { N _ { \mathrm { t } } } } { M } .\tag{28}
$$

Through (22) and (24), the COR at the prediction stage can be approximated by $Q _ { \mathrm { p } , n } \approx \mathcal { Q } _ { \mathrm { p a } , n } \approx \tilde { \mathcal { Q } } _ { \mathrm { p } , n } = \{ \tilde { \xi } _ { \mathrm { p } , n } | \tilde { \xi } _ { \mathrm { p } , n } \geq 0 \}$ where the set $\tilde { \mathcal { Q } } _ { \mathfrak { p } , n }$ denotes the aCOR. Note that it can be easily obtained that de $\lvert \tilde { \xi } _ { \mathfrak { p } , n } ^ { ( 2 ) } \rangle > 0$ holds due to $\breve { \gamma } _ { n } ~ > ~ 0$ Consequently, the aCOR boundary denoted by $\tilde { \xi } _ { \mathfrak { p } , n } = 0$ represents an ellipse on the $( \acute { x } _ { n } , \acute { y } _ { n } )$ plane, as illustrated in Fig. 2. Given the aCOR expression, our proposed approximated OP at the prediction stage of the nth time slot is provided in the following proposition.

Proposition 1: Given assumption 1, the OP at the prediction stage of the nth time slot can be approximated by

$$
\begin{array} { r } { \zeta _ { \mathsf { p } , n } \approx \zeta _ { \mathsf { p } , n } | _ { \mathcal { Q } _ { \mathsf { p } , n } = \tilde { \mathcal { Q } } _ { \mathsf { p } , n } } = \tilde { \zeta } _ { \mathsf { p } , n } = 1 - \mathbb { E } _ { \hat { x } _ { n } } \left[ \check { \chi } ( \dot { x } _ { n } ) \right] , } \end{array}\tag{29}
$$

with

$$
\check { \chi } ( \acute { x } _ { n } ) \triangleq \left\{ \begin{array} { r l } & { \frac { \mathrm { e r f } ( \check { \chi } _ { \mathrm { U } } ( \acute { x } _ { n } ) ) - \mathrm { e r f } ( \check { \chi } _ { \mathrm { L } } ( \acute { x } _ { n } ) ) } { 2 } \acute { x } _ { n } \in [ \acute { x } _ { \mathrm { L } } , \acute { x } _ { \mathrm { U } } ] , } \\ & { \mathrm { ( O t h e r w i s e , } } \end{array} \right.\tag{30}
$$

where ${ \acute { x } } _ { n }$ follows a zero mean Gaussian distribution with a variance of $\breve { \Lambda } _ { \mathrm { x } , n } ^ { 2 } ~ = ~ [ { \bf M } _ { \mathrm { p } , n } ] _ { 1 1 }$ . The specific expressions of $\breve { \chi } _ { \mathrm { U } } ( \cdot ) , \ \breve { \chi } _ { \mathrm { L } } ( \cdot ) , \ \acute { x } _ { \mathrm { U } }$ , and x´<sub>L</sub> are given by (31)-(33), shown at the bottom of the next page, respectively.

Proof: Please refer to Appendix A.

## B. Estimation Stage

Let us denote the estimated UAV trajectory at the nth time slot by $\hat { \mathbf { q } } _ { n } = [ \hat { x } _ { n } , \hat { y } _ { n } ] ^ { T }$ and define $\dot { \mathbf { q } } _ { n }$ as ${ \dot { \mathbf { q } } } _ { n } \triangleq \mathbf { q } _ { n } - { \hat { \mathbf { q } } } _ { n } =$ $[ \dot { x } _ { n } , \dot { y } _ { n } ] ^ { T }$ . Note that $\hat { \mathbf { q } } _ { n }$ is unknown at the $( n - 1 ) \operatorname { t h }$ time slot and only available after receiving the echo signals at the nth time slot. To address this issue, the approximation $\hat { \mathbf { q } } _ { n } \approx \breve { \mathbf { q } } _ { n }$ is reasonably applied thanks to assumption 1 so that the OP at the estimation stage of the nth time slot can be approximately calculated at the (n − 1)th time slot. Then, similar as the derivation process from (19) to (24), the aCOR at the estimation stage of the nth time slot can be expressed as $\tilde { \mathcal { Q } } _ { \mathrm { e } , n } = \{ \tilde { \xi } _ { \mathrm { e } , n } | \tilde { \xi } _ { \mathrm { e } , n } \overset { \sim } { \geq } 0 \}$ with

$$
\tilde { \xi } _ { \mathrm { e } , n } = \frac { 1 } { 2 } \hat { \mathbf { q } } _ { n } ^ { T } \tilde { \xi } _ { \mathrm { e } , n } ^ { ( 2 ) } \hat { \mathbf { q } } _ { n } + ( \tilde { \pmb { \xi } } _ { \mathrm { e } , n } ^ { ( 1 ) } ) ^ { T } \hat { \mathbf { q } } _ { n } + \tilde { \xi } _ { \mathrm { e } , n } ^ { ( 0 ) } ,\tag{34}
$$

where $\tilde { \pmb { \xi } } _ { \mathrm { e } , n } ^ { ( 2 ) } , \tilde { \pmb { \xi } } _ { \mathrm { e } , n } ^ { ( 1 ) }$ , and $\tilde { \xi } _ { \mathrm { e } , n } ^ { ( 0 ) }$ are given by $\tilde { \pmb { \xi } } _ { \mathrm { e } , n } ^ { ( 2 ) } = \tilde { \pmb { \xi } } _ { \mathrm { p } , n } ^ { ( 2 ) } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } }$ $\tilde { \pmb { \xi } } _ { \mathrm { e } , n } ^ { ( 1 ) } = \tilde { \pmb { \xi } } _ { \mathrm { p } , n } ^ { ( 1 ) } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } }$ , and $\tilde { \xi } _ { \mathfrak { e } , n } ^ { ( 0 ) } = \tilde { \xi } _ { \mathfrak { p } , n } ^ { ( 0 ) } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } }$ , respectively.

Meanwhile, similar as the derivation process in the proof of Proposition $1 , \ \grave { \mathbf { q } } _ { n } \sim \mathcal { N } ( \mathbf { 0 } , \hat { \mathbf { A } } _ { n } )$ approximately holds with

$$
\begin{array} { r } { \hat { \bf \cal N } _ { n } = [ \hat { \Lambda } _ { \mathrm { x } , n } ^ { 2 } \ \hat { \Lambda } _ { \mathrm { x y } , n } ^ { 2 } ] \approx [ [ { \bf M } _ { n } ] _ { 1 1 } \ [ { \bf M } _ { n } ] _ { 1 3 } ] , } \\ { \hat { \Lambda } _ { \mathrm { x y } , n } ^ { 2 } \ \hat { \Lambda } _ { \mathrm { y } , n } ^ { 2 } ] \approx [ [ { \bf M } _ { n } ] _ { 3 1 } \ [ { \bf M } _ { n } ] _ { 3 3 } ] , } \end{array}\tag{35}
$$

and the OP at the estimation stage of the nth time slot can be approximated by

$$
\begin{array} { r } { \zeta _ { \mathrm { e } , n } \approx \zeta _ { \mathrm { p } , n } | _ { \mathcal { Q } _ { \mathrm { e } , n } = \tilde { \mathcal { Q } } _ { \mathrm { e } , n } } = \tilde { \zeta } _ { \mathrm { e } , n } = 1 - \mathbb { E } _ { \hat { x } _ { n } } \left[ \hat { \chi } ( \hat { x } _ { n } ) \right] , } \end{array}
$$

with

(36)

$$
\hat { \chi } ( \hat { x } _ { n } ) \triangleq \left\{ \begin{array} { r l } & { \frac { \mathrm { e r f } ( \hat { \chi } _ { \mathrm { U } } ( \hat { x } _ { n } ) ) - \mathrm { e r f } ( \hat { \chi } _ { \mathrm { L } } ( \hat { x } _ { n } ) ) } { 2 } , \hat { x } _ { n } \in [ \hat { x } _ { \mathrm { L } } , \hat { x } _ { \mathrm { U } } ] , } \\ & { 0 , \hat { x } _ { n } \in ( - \infty , \hat { x } _ { \mathrm { L } } ) \cup ( \hat { x } _ { \mathrm { U } } , \infty ) . } \end{array} \right.\tag{37}
$$

The expressions of functions $\hat { \chi } _ { \mathrm { U } } ( \grave { x } _ { n } )$ and $\hat { \chi } _ { \mathrm { L } } ( \dot { x } _ { n } )$ are given by

$$
\hat { \chi } _ { \mathrm { U } } ( \hat { x } _ { n } ) = \frac { \hat { \Lambda } _ { \mathrm { x } , n } ^ { 2 } \hat { y } _ { \mathrm { U } } ( \hat { x } _ { n } ) - \hat { \Lambda } _ { \mathrm { x y } , n } ^ { 2 } \hat { x } _ { n } } { \sqrt { 2 | \operatorname* { d e t } \left( \hat { \Lambda } _ { n } \right) | } \hat { \Lambda } _ { \mathrm { x } , n } } ,\tag{38}
$$

$$
\hat { \chi } _ { \mathrm { L } } ( \dot { x } _ { n } ) = \frac { \hat { \Lambda } _ { \mathrm { x } , n } ^ { 2 } \dot { y } _ { \mathrm { L } } ( \dot { x } _ { n } ) - \hat { \Lambda } _ { \mathrm { x y } , n } ^ { 2 } \dot { x } _ { n } } { \sqrt { 2 | \operatorname* { d e t } \left( \hat { \Lambda } _ { n } \right) | } \hat { \Lambda } _ { \mathrm { x } , n } } ,\tag{39}
$$

with $\begin{array} { r } { \dot { x } _ { \mathrm { L } } = \dot { x } _ { \mathrm { L } } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } } , \ \dot { x } _ { \mathrm { U } } = \check { x } _ { \mathrm { U } } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } } , \ \dot { y } _ { \mathrm { L } } = \check { y } _ { \mathrm { L } } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } } } \end{array}$ and $\dot { y } _ { \mathrm { U } } = \dot { y } _ { \mathrm { U } } | _ { \check { \gamma } _ { n } = \hat { \gamma } _ { n } }$ , respectively.

Remark 2: Estentially, our proposed OP approximations are derived from aCORs and thus the approximation accuracies mainly depend on the two-step Taylor expansion approximation accuracies. Although the aCOR seems quite different from the COR as shown in Fig. 2, our proposed approximations still achieve satisfactory accuracies when the PDFs of $\breve { \mathbf { q } } _ { n }$ and $\hat { \mathbf { q } } _ { n }$ are highly concentrated in a neighborhood of ${ \bf q } _ { n }$ contained by both the COR and the aCOR, in which $\left\| { \breve { \mathbf { q } } } _ { n } - \mathbf { q } _ { n } \right\|$ and $\| \hat { \mathbf { q } } _ { n } - \mathbf { q } _ { n } \|$ are sufficiently small. Fortunately, the existence of such neighborhood is theoretically guaranteed by assumption 1 and the property of Taylor expansions, which validates our proposed approximations. Simulations further verify the approximation accuracies in Section V. Furthermore, (1) and (36) show that the sensing accuracy characterized by MSE matrices decides the integral over aCOR, which further influences the communication reliability.

## IV. PROPOSED ALGORITHMS

Given the approximated OPs presented in (29) and (36), (P1) can be reformulated into an approximated optimization problem as:

$$
\begin{array} { r l } & { ( \mathrm { P 2 } ) : \underset { \{ \check { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { n } \} } { \mathrm { m a x } } C _ { n } } \\ & { \quad \quad \quad \mathrm { s . t . ~ } \left( 1 8 \mathrm { a } \right) \ – ( 1 8 \mathrm { c } ) , \ ( 1 8 \mathrm { e } ) , } \\ & { \quad \quad \quad \quad \tilde { \varkappa } ( \check { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { n } ) \leq 0 , } \end{array}\tag{40}
$$

(40a)

with $\tilde { \varkappa } ( \check { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { n } ) \ = \ \operatorname* { m a x } \big ( \tilde { \zeta } _ { \mathsf { p } , n } , \tilde { \zeta } _ { \mathsf { e } , n } \big ) \ - \ \varepsilon _ { \mathsf { o u t } } .$ . Compared with (P1), the original implicit constraint (18d) in (P1) has been replaced by the approximated outage constraint (40a). However, (P2) remains challenging to be optimally solved due to non-convex constraint (40a) and the coupling among the optimization variables. To address this issue, an algorithm based on bisection search is proposed to obtain an efficient solution to (P2) with guaranteed convergence. To further reduce computational complexity, a second efficient algorithm is proposed based on AO.

## A. Search-Based Algorithm

To decouple $\breve { \mathbf { q } } _ { n }$ from $w _ { n }$ and $\gamma _ { n } \colon$ , our proposed search-based algorithm solves (P2) by iteratively solving two subproblems formulated as

$$
\begin{array} { r } { ( \mathrm { P 2 . 1 } ) : \mathrm { F i n d } w _ { n } , \gamma _ { n } \qquad } \\ { \mathrm { s . t . } ( 1 8 \mathrm { c } ) , ( 1 8 \mathrm { e } ) \ , \ } \\ { C _ { n } = C _ { i } , \qquad } \end{array}\tag{41}
$$

(41a)

and

$$
( { \mathrm { P 2 . 2 } } ) : \operatorname* { m i n } _ { { \check { \mathbf { q } } } _ { n } } \quad { \tilde { \varkappa } } ( { \check { \mathbf { q } } } _ { n } , w _ { i } , \gamma _ { i } ) \ \mathrm { ~ s . t . ~ } \ ( 1 8 \mathrm { a } ) , \ ( 1 8 \mathrm { b } ) ,
$$

respectively, where $C _ { i }$ and $( w _ { i } , \gamma _ { i } )$ denote a given objective value and the solution to (P2.1) in the i-th iteration, respectively. Our proposed search-based algorithm solves (P2.1) to generate a candidate solution $( w _ { i } , \gamma _ { i } )$ and subsequently evaluate its feasibility to (P2) by solving (P2.2) in the i-th iteration, as summarized in Algorithm 1.

To address the non-convex constraint (41a), (P2.1) can be further divided into two subproblems with $C _ { \mathfrak { p } , n } \geq C _ { \mathfrak { e } , n }$ and $C _ { \mathfrak { p } , n } < C _ { \mathfrak { e } , n } .$ respectively. In both cases, $C _ { n }$ is the monotonical function of $\gamma _ { n }$ and $w _ { n }$ . Then, the updating rule of the given objective value is designed based on the monotonicity of $\tilde { \varkappa } ( \breve { \mathbf q } _ { n } , w _ { n } , \gamma _ { n } )$ w.r.t. $\gamma _ { n }$ given in the following proposition.<sup>7</sup>

Proposition 2: Given any feasible $\breve { \mathbf { q } } _ { i } , w _ { i } , \tilde { \varkappa } ( \breve { \mathbf { q } } _ { i } , w _ { i } , \gamma _ { n } )$ is a monotonically nondecreasing function of $\gamma _ { n }$

## Proof: Please refer to Appendix B.

Proposition 2 indicates that it is easier to identify feasible solutions to (P2) with smaller target constant received SNRs. Let us denote the feasible set for (P2) given γ by

$$
S _ { i } ( \gamma ) = \{ ( w _ { n } , \check { \mathbf { q } } _ { n } ) | \tilde { \varkappa } ( \check { \mathbf { q } } _ { n } , w _ { n } , \gamma ) < 0 \} ,\tag{42}
$$

respectively. Then, for different $\gamma$ and $\gamma ^ { \prime } , \mathcal { S } _ { i } ( \gamma ) \subseteq \mathcal { S } _ { i } ( \gamma ^ { \prime } )$ holds if $\gamma _ { i } \preceq \gamma _ { i } ^ { \prime }$ is satisfied due to

$$
\tilde { \varkappa } ( \check { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { i } ^ { \prime } ) \leq \tilde { \varkappa } ( \check { \mathbf { q } } _ { n } , w _ { n } , \gamma _ { i } ) \leq 0 , \forall \gamma _ { i } \in S _ { i } ( \gamma ) .\tag{43}
$$

Thanks to the continuity of $\tilde { \varkappa } ( \breve { \mathbf q } _ { n } , w _ { n } , \gamma _ { n } )$ w.r.t $\breve { \mathbf { q } } _ { n }$ in most parts of COR, the feasible set $S _ { i } ( \gamma ^ { \prime } )$ probably contains elements not belonging to $S _ { i } ( \gamma )$ , which further indicates a higher chance of finding a feasible solution to (P2) in $S _ { i } ( \gamma ^ { \prime } )$ than in $S _ { i } ( \gamma )$ . Inspired by this observation, a two-layer bisection search is applied to solve (P2.1) ensuring the convergence.

To address the non-convex objective function in (P2.2), the subalgorithm for (P2.2) applies the SCA technique to efficiently obtain a locally optimal solution [31]. In the m-th iteration, (P2.2) is solved with the objective function replaced by a surrogate function based on the second-order Taylor expansion, given by

$$
\begin{array} { r l } & { \widetilde { \varkappa } _ { \mathbf { a } } ( \breve { \mathbf { q } } _ { m } ; \breve { \mathbf { q } } _ { m - 1 } ^ { \mathrm { E } } , w _ { j } , \gamma _ { k } ) = \varkappa ( \breve { \mathbf { q } } _ { m - 1 } ^ { \mathrm { E } } ; w _ { j } , \gamma _ { k } ) } \\ & { \quad + \nabla \widetilde { \varkappa } ( \breve { \mathbf { q } } _ { m - 1 } ^ { \mathrm { E } } ; w _ { j } , \gamma _ { k } ) ^ { T } ( \breve { \mathbf { q } } _ { m } - \breve { \mathbf { q } } _ { m - 1 } ^ { \mathrm { E } } ) } \\ & { \quad + Q \| \breve { \mathbf { q } } _ { m } - \breve { \mathbf { q } } _ { m - 1 } ^ { \mathrm { E } } \| ^ { 2 } , } \end{array}\tag{44}
$$

where $\breve { \mathbf q } _ { m - 1 } ^ { \mathrm { E } }$ denotes the Taylor expansion point in the $( m { - } 1 ) .$ th iteration and $Q$ is a given positive real number ensuring the convexity of (44). Problem (P2.2) with the objective function replaced by (44) is a convex optimization problem and can be optimally solved by standard numerical convex programming solvers such as CVX tools [34]. The overall algorithm iteratively solving (P2.1) and (P2.2) is summarized in Algorithm 2.

## B. AO-Based Algorithm

The computational overhead of our proposed search-based algorithm mainly exists in the iteration number k owing to the complicated function $\tilde { \varkappa } ( \cdot )$ and trials of infeasible $( w _ { j } , \gamma _ { k } )$ . To significantly reduce these redundant computations, a second

$$
\check { \chi } _ { \mathrm { U } } ( \hat { x } _ { n } ) = \frac { \check { \Lambda } _ { x , n } ^ { 2 } \dot { y } _ { \mathrm { U } } ( \hat { x } _ { n } ) - \check { \Lambda } _ { x _ { \mathrm { Y } } , n } ^ { 2 } \hat { x } _ { n } } { \sqrt { 2 | \operatorname* { d e t } { ( \check { \Lambda } _ { n } ) } | \check { \Lambda } _ { x , n } } } , \check { \chi } _ { \mathrm { L } } ( \hat { x } _ { n } ) = \frac { \check { \Lambda } _ { x , n } ^ { 2 } \dot { y } _ { \mathrm { L } } ( \hat { x } _ { n } ) - \check { \Lambda } _ { x _ { \mathrm { Y } } , n } ^ { 2 } \hat { x } _ { n } } { \sqrt { 2 | \operatorname* { d e t } { ( \check { \Lambda } _ { n } ) } | } \check { \Lambda } _ { x , n } } , \hat { x } _ { \mathrm { U } } = - \check { x } _ { n } + \sqrt { - \frac { Y _ { 1 } } { Y _ { 2 } } } , \hat { x } _ { \mathrm { L } } = - \check { x } _ { n } - \sqrt { - \frac { Y _ { 1 } } { Y _ { 2 } } } ,\tag{31}
$$

$$
\dot { y } _ { \mathrm { U } } ( \dot { x } _ { n } ) = - \check { y } _ { n } + Y _ { 0 } ( \dot { x } _ { n } + \check { x } _ { n } ) + \sqrt { Y _ { 1 } + Y _ { 2 } ( \dot { x } _ { n } + \check { x } _ { n } ) ^ { 2 } } , \dot { y } _ { \mathrm { L } } ( \dot { x } _ { n } ) = - \check { y } _ { n } + Y _ { 0 } ( \dot { x } _ { n } + \check { x } _ { n } ) - \sqrt { Y _ { 1 } + Y _ { 2 } ( \dot { x } _ { n } + \check { x } _ { n } ) ^ { 2 } } ,\tag{32}
$$

$$
Y _ { 0 } = \frac { \check { x } _ { n } y _ { n } ^ { 3 } \tilde { P } M } { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } \tilde { y } _ { n } + \check { x } _ { n } ^ { 2 } y _ { n } ^ { 2 } \tilde { P } M } , Y _ { 1 } = \frac { ( \tilde { P } N _ { \mathrm { t } } - H ^ { 2 } \check { y } _ { n } ) ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } } { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } \tilde { y } _ { n } + \check { x } _ { n } ^ { 2 } \check { y } _ { n } ^ { 2 } \tilde { P } M } , Y _ { 2 } = - \frac { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 4 } ( ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 2 } \check { y } _ { n } ^ { 2 } + \tilde { P } M \check { y } _ { n } ^ { 2 } \check { y } _ { n } ) } { ( ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } \check { y } _ { n } + \check { x } _ { n } ^ { 2 } \check { y } _ { n } ^ { 2 } \tilde { P } M ) ^ { 2 } } ,\tag{33}
$$

Algorithm 1 Proposed Search-Based Algorithm for (P2)   
1: Initialize the case indicator $\overline { { l _ { \mathrm { C } } \ ( l _ { \mathrm { C } } = 0 } }$ for the case with   
$C _ { \mathfrak { p } , n } \geq C _ { \mathfrak { e } , n }$ or $l _ { \mathrm { C } } = 1$ otherwise), the error tolerance $\delta _ { \mathrm { C } } ,$   
$C _ { \mathrm { m a x } } = \log _ { 2 } ( 1 + \gamma _ { \mathrm { m a x } } ) .$ , and $i = 1 .$   
2: Set the searching range $[ C _ { i } ^ { \mathrm { L } } , C _ { i } ^ { \mathrm { U } } ] = [ 0 , C _ { \mathrm { m a x } } ] .$   
3: for $l _ { \mathrm { C } } = 0$ to 1 do   
4: while $| C _ { i } ^ { \mathrm { U } } - C _ { i } ^ { \mathrm { L } } | \leq \delta _ { \mathrm { C } }$ is satisfied. do   
5: Obtain $C _ { i } \stackrel { \cdot \mathrm { ~ \tiny ~ { ~ C ~ } ~ } } { = } ( C _ { i } ^ { \mathrm { { L } } } + C _ { i } ^ { \mathrm { { U } } } ) / 2$ and solve (P2.1) and   
(P2.2) iteratively by Algorithm 2 given $C _ { i }$ and $l _ { \mathbf { C } } .$   
6: Obtain the outputted feasibility indicator $l _ { \mathrm { f } } .$   
7: if $l _ { \mathrm { f } } = 0$ then   
8: Update $[ C _ { i + 1 } ^ { \mathrm { L } } , C _ { i + 1 } ^ { \mathrm { U } } ] = [ C _ { i } ^ { \mathrm { L } } , C _ { i } ] .$   
9: else   
10: Update $[ C _ { i + 1 } ^ { \mathrm { L } } , C _ { i + 1 } ^ { \mathrm { U } } ] = [ C _ { i } , C _ { i } ^ { \mathrm { U } } ] .$   
11: end if   
12: Update $i = i + 1 .$   
13: end while   
14: end for   
15: Compare $C _ { i }$ between the case with $l _ { \mathrm { C } } = 0$ and $l _ { \mathrm { C } } = 1$ and   
output the larger value as the maximized outage capacity.

algorithm for (P2) is proposed based on the AO method, where the obtained $w _ { n }$ and $\gamma _ { n }$ are always feasible to (P2) in each iteration. To be specific, given a feasible predicted UAV trajectory $\breve { \mathbf { q } } _ { n } = \breve { \mathbf { q } } _ { i }$ in the i-th iteration of our AO-based algorithm, (P2) is simplified as a subproblem formulated as

(45)

$$
\begin{array} { r l } & { \mathrm { ( P 3 . 1 ) : ~ } \displaystyle \operatorname* { m a x } _ { \{ w _ { n } , \gamma _ { n } \} } C _ { n } } \\ & { \quad \mathrm { s . t . ~ } \displaystyle \mathrm { ( 1 8 c ) , ~ } ( 1 8 \mathrm { e } ) ~ , } \\ & { \quad \quad \quad \quad \tilde { \varkappa } ( \check { \mathbf { q } } _ { i } , w _ { n } , \gamma _ { n } ) \leq 0 . } \end{array}\tag{45a}
$$

To handle the non-convex objective function and constraint (45a) in (P3.1), $w _ { n }$ can be heuristically searched by a onedimensional search, such as the golden section search [35]. As such, the subproblem of (P3.1) given the searched $w _ { n }$ is a convex optimization problem thanks to Proposition $^ { 2 , }$ and thus can be optimally solved by the bisection search [36]. Then, as summarized in Algorithm 3, given the obtained solution to (P3.1) denoted by $( w _ { i } ^ { * } , \gamma _ { i } ^ { * } )$ in the i-th iteration, our proposed algorithm solves (P2.2) and updates $\breve { \mathbf { q } } _ { i + 1 }$ by the obtained solution to (P2.2).

## C. Convergence and Computational Complexity Analysis

The computational complexities of our proposed searchbased and AO-based algorithm can be analyzed as follows. Specifically, the number of iterations needed for the convergence of the bisection search for $w _ { n }$ and $C _ { \mathfrak { p } , n }$ can be given by $I _ { \mathrm { w } } ~ = ~ \mathrm { l o g } _ { 2 } ( \lfloor ( w _ { \mathrm { m a x } } - w _ { \mathrm { m i n } } ) / \epsilon _ { \mathrm { w } } \rfloor )$ and $I _ { \mathrm { C } } ~ =$ log<sub>2</sub> $( \lfloor \log _ { 2 } { ( 1 + \gamma _ { \operatorname* { m a x } } ) } / \epsilon _ { \mathrm { C } } \rfloor )$ , respectively, where $\epsilon _ { \mathrm { w } }$ and $\epsilon _ { \mathrm { { C } } }$ denotes the tolerance of the bisection search for $w _ { n }$ and $C _ { \mathfrak { p } , n }$ , respectively [36]. Thus, the computational complexity of our proposed search-based algorithm can be given by $\mathcal { O } ( 2 I _ { \mathrm { w } } I _ { \mathrm { C } } ^ { \bar { 2 } } J _ { \mathrm { A } } )$ , where $J _ { \mathrm { A } }$ represents the number of iterations needed for the convergence of the SCA to solve (P2.2). In comparison, the computational complexity of our proposed AO-based algorithm can be given by $\mathcal { O } ( \bar { I } _ { \mathrm { w } } ^ { \prime } I _ { \mathrm { C } } + \bar { J } _ { \mathrm { A } } )$ , where $I _ { \mathrm { w } } ^ { \prime }$ denotes the number of iterations needed for the convergence of the one-dimensional search for $w _ { n }$ . Assuming

```latex
Algorithm 2 Overall Algorithm for (P2.1) and (P2.2)
1: Initialize $\overline { { C _ { i } , \ l _ { \mathrm { C } } , \ j \ = \ 1 } } ,$ , the error tolerance $\delta _ { \mathrm { w } } , \delta _ { \mathrm { p } } ,$ the
searching range $[ w _ { j } ^ { \mathrm { L } } , w _ { j } ^ { \mathrm { U } } ] = [ w _ { \mathrm { m i n } } , w _ { \mathrm { m a x } } ] .$ , and feasibility
indicator $l _ { \mathrm { f } } = 0 .$
2: while $| w _ { j } ^ { \mathrm { U } } - w _ { j } ^ { \mathrm { L } } | > \delta _ { \mathrm { w } }$ and $l _ { \mathrm { f } } = 0$ do
3: Obtain $w _ { j } = ( w _ { j } ^ { \mathrm { L } } + w _ { j } ^ { \mathrm { U } } ) / 2$ and set $k = 1$
4: Set the searching range $[ C _ { \mathrm { p } , k } ^ { \mathrm { L } } , C _ { \mathrm { p } , k } ^ { \mathrm { U } } ] ~ = ~ [ C _ { i } , C _ { \mathrm { m a x } } ]$
for the case with $l _ { \mathrm { { C } } } ~ = ~ 0 ,$ or $[ C _ { \mathrm { p } , k } ^ { \mathrm { L } } , C _ { \mathrm { p } , k } ^ { \mathrm { U } } ] = [ 0 , C _ { i } ]$
otherwise.
5: while $| C _ { \mathfrak { p } , k } ^ { \mathrm { U } } - C _ { \mathfrak { p } , k } ^ { \mathrm { L } } | > \delta _ { \mathfrak { p } }$ and $l _ { \mathrm { f } } = 0$ do
6: Obtain $C _ { \mathsf { p } , k } \doteq ( C _ { \mathsf { p } , k } ^ { \mathrm { L } } + C _ { \mathsf { p } , k } ^ { \mathrm { U } } ) / 2$ and $C _ { \mathrm { e } , k }$ from (41a).
7: Obtain $\dot { \gamma _ { k } } = [ \check { \gamma } _ { k } , \hat { \gamma } _ { k } ] ^ { T } = [ 2 ^ { C _ { \mathsf { p } , k } } - 1 , 2 ^ { C _ { \mathsf { e } , k } } - 1 ] ^ { T }$
8: Solve (P2.2) by SCA with $( w _ { j } , \gamma _ { k } )$ to obtain $\breve { \mathbf { q } } _ { k }$
9: if $\tilde { \varkappa } ( \breve { \mathbf q } _ { k } , w _ { j } , \gamma _ { k } ) < 0$ then
10: Set $l _ { \mathrm { f } } = 1$ and $( \breve { \mathbf { q } } _ { i } ^ { * } , w _ { i } ^ { * } , \gamma _ { i } ^ { * } ) = ( \breve { \mathbf { q } } _ { k } , w _ { j } , \gamma _ { k } ) .$
11: else
12: Update $\begin{array} { r l r } { [ C _ { \mathrm { p } , k + 1 } ^ { \mathrm { L } } , C _ { \mathrm { p } , k + 1 } ^ { \mathrm { U } } ] } & { { } = } & { [ C _ { \mathrm { p } , k } ^ { \mathrm { L } } , C _ { \mathrm { p } , k } ] } \end{array}$ for
the case with <sup>˜</sup>ζ<sub>p,n</sub> $\begin{array} { r l r } { ( \breve { \bf q } _ { k } , w _ { j } , \breve { \gamma } _ { k } ) } & { { } \geq } & { 0 , } \end{array}$ or
$[ C _ { \mathrm { p } , k + 1 } ^ { \mathrm { L } } , C _ { \mathrm { p } , k + 1 } ^ { \mathrm { U } } ] = [ C _ { \mathrm { p } , k } , C _ { \mathrm { p } , k } ^ { \mathrm { U } } ]$ otherwise.
13: end if
14: Update $k = k + 1 .$
15: end while
16: if $l _ { \mathrm { f } } = 0$ then
17: Update $[ w _ { j + 1 , \ast } ^ { \mathrm { L } } w _ { j + 1 , - } ^ { \mathrm { U } } ] = [ w _ { j } , w _ { j + 1 } ^ { \mathrm { U } } ]$ for the case with
$l _ { \mathrm { C } } = 0 , \mathrm { o r } \ ' [ w _ { j + 1 } ^ { \mathrm { L } } , w _ { j + 1 } ^ { \mathrm { U } } ] = [ w _ { j } ^ { \mathrm { L } } , w _ { j } ]$ otherwise.
18: end if
19: Update $j = j + 1 .$
20: end while
21: Output $l _ { \mathrm { f } }$ and additionally $( \breve { \mathbf { q } } _ { i } ^ { * } , w _ { i } ^ { * } , \gamma _ { i } ^ { * } )$ if $l _ { \mathrm { f } } = 1$ holds.
```

Algorithm 3 Proposed AO-Based Algorithm for (P2)   
1: Initialize the maximum iteration number $I _ { \mathrm { m a x } }$ and a   
solution $\breve { \mathbf { q } } _ { 0 } ^ { * }$ feasible to (P2). Set the iteration number   
$i = 1 .$   
2: while $i \leq I _ { \mathrm { m a x } }$ do   
3: Solve (P3.1) given $\breve { \mathbf { q } } _ { i - 1 } ^ { * }$ by searching $w _ { n }$ via the golden   
section in the outer layer and searching $\gamma _ { i }$ via the   
bisection search in the inner layer. Obtain the solution   
$( w _ { i } ^ { * } , \gamma _ { i } ^ { * } )$   
$4 { : }$ Solve (P2.2) given $( w _ { i } ^ { * } , \gamma _ { i } ^ { * } )$ by SCA and obtain the   
solution $\breve { \mathbf { q } } _ { i } ^ { * } .$   
5: Update $i = i + 1 .$   
6: end while

$I _ { \mathrm { w } } ~ \approx ~ I _ { \mathrm { w } } ^ { \prime } .$ , the computational complexity of our proposed AO-based algorithm is generally lower than that of our search-based algorithm. Nevertheless, the convergence of the search-based algorithm is guaranteed thanks to the guaranteed convergence of the bisection search while the convergence of the AO-based algorithm is not guaranteed owing to the heuristic search for $\breve { \mathbf { q } } _ { n }$ . To ensure practical applicability, a maximum number of iterations can be predetermined to force the termination of AO-based algorithm.

## V. SIMULATION RESULTS

In this section, numerical results are provided to verify the effectiveness of proposed OP approximations and algorithms.

![](images/b9bbd605b0b4fdac73e9fa8581fceab7c88dfb3559f5897ff86e538b5390cac7.jpg)

![](images/1365cb412b89e0b13a38b11c4cfd0bc22e6a919a12c2c5bd8c831f5844d65872.jpg)  
(a) OPs at the prediction stage.  
(b) OPs at the estimation stage.

![](images/f1f1c3267a2febf5342516f3896c3a96062916e45a3759ce4bbb594326b17fee.jpg)  
(c) CORs at the prediction stage.

Fig. 3. Accuracies of proposed approximated OPs and CORs under different $\breve { \mathbf { q } } _ { n }$  
![](images/d03b475999bc80a576686d03fedaa05b99acc840d6a027ec265afab751405f60.jpg)  
(a) OP versus $\breve { \mathbf { q } } _ { n }$ with $N _ { \mathrm { t } } = 3 2 .$

![](images/9db613d47a2aaa94eaa94aaea8e0f30e921e018cb9cb8cddefbdc3e6e9cbfa96.jpg)  
(c) CORs with $N _ { \mathrm { t } } = 3 2 .$  
Fig. 4. OPs and CORs with different $\breve { \mathbf { q } } _ { n }$ and $N _ { \mathrm { t } } .$

(b) OP versus $\breve { \mathbf { q } } _ { n }$ with $N _ { \mathrm { t } } = 6 4 .$  
![](images/15092aa0444d5ceeed303c3f6357476cf77d2d022f2bc87237d6896deb610ab1.jpg)

Unless specified otherwise, the following system parameters are used: $P _ { \mathrm { A } } = 0 . 1 \mathbf { W } , \ \sigma _ { \mathrm { R C S } } = 0 . 2 \mathbf { m } ^ { 2 } , \ \lambda = 0 . 0 1 \mathbf { m } , \ \sigma ^ { 2 } \ =$ −80dBm, $H = 5 0 \mathrm { m } , \Delta T = 0 . 0 2 \mathrm { s } , v _ { \mathrm { A , m a x } } = 3 0 \mathrm { m } / \mathrm { s } , \tilde { q } = 1 0 ^ { - 3 }$ $N _ { \mathrm { s y m } } = 1 0 ^ { 4 }$ , N = 10<sup>3</sup>, $w _ { \mathrm { m i n } } = 0 . 1$ , and $w _ { \mathrm { m a x } } = 1 ~ [ 1 6 ]$ [29], [37].

## A. Proposed OP Approximations

Fig. 3(a) and Fig. 3(b) illustrate the accuracies of our proposed approximated OPs at the prediction and estimation stage and compare their differences under three representative predicted UAV positions. Specifically, the Monte Carlo results in Fig. 3(a) and Fig. 3(b) are obtained by simulating the OP results with random noises (including the initial noise, process noise and measurement noise) in one time slot. The number of

![](images/e8007cd4ba5da961a85e215fd1e70a7ddd87ff296557e7d930625ffe828e3f88.jpg)  
(d) CORs with $N _ { \mathrm { t } } = 6 4$

Monte Carlo simulation runs is set to $1 0 ^ { 4 }$ , and other specific system parameters are given by $a _ { 1 } = a _ { 2 } = 0 . 1 , N _ { \mathrm { t } } = N _ { \mathrm { r } } = 1 6$ $N = 1 , w _ { n } = 0 . 5$ and $\mathbf { M } _ { 0 } = 1 0 ^ { - 2 } \mathbf { I } \ [ 1 6 ]$ , respectively. It can be observed that our proposed OP approximations closely match the Monte Carlo results in the cases with $\breve { \mathbf { q } } _ { n } = [ 0 , 7 ] ^ { \breve { T } }$ and $\breve { \mathbf { q } } _ { n } = [ 0 , 1 5 ] ^ { T }$ , thus validating the proposed approximation accuracy and effectiveness.<sup>8</sup> However, our proposed OP approximations are less accurate in the case with $\breve { \mathbf q } _ { n } = [ 0 , 3 ] ^ { T }$ especially at the prediction stage, which indicates that the proposed approximation accuracy is conditional on the UAV position. To explain such property, Fig. 3(c) demonstrates the relationships among the dominant part of $\check { \mathbf { q } } _ { n }$ PDF, COR and aCOR in the cases with $\breve { \bf q } _ { n } ~ = ~ [ 0 , 3 ] ^ { T }$ and $\breve { \bf q } _ { n } ~ = ~ [ 0 , 7 ] ^ { T }$ respectively, given the target constant received SNR $\breve { \gamma } _ { n } = 3 5$ Note that the COR with $\breve { \bf q } _ { n } = [ 0 , 3 ] ^ { T }$ is the same as that with $\breve { \mathbf { q } } _ { n } = [ 0 , 7 ] ^ { T }$ , since (21) is irrelevant to ${ \breve { x } } _ { n }$ and $\breve { y } _ { n }$ given $\breve { x } _ { n } = 0$ . In the scenario with $\breve { \mathbf q } _ { n } = [ 0 , 7 ] ^ { T }$ , despite the seemingly considerable difference between the COR and aCOR, our proposed approximation is still accurate because both the COR and aCOR contain the dominant part of $\check { \mathbf { q } } _ { n }$ PDF, which verifies a condition for our proposed approximation being accurate: the prediction/estimation error must be sufficiently small such that the difference between COR and aCOR can have negligible impacts on the integral of the highly concentrated $\check { \mathbf { q } } _ { n } \ P D F$ In contrast, in the case with $\breve { \mathbf q } _ { n } = [ 0 , 3 ] ^ { T }$ , both the COR and aCOR intersect with the dominant part of $\check { \mathbf { q } } _ { n }$ PDF, and thereby the difference between the COR and aCOR causes nonnegligible approximation accuracy loss. Furthermore, although it is intractable to analytically characterize the relationship between the proposed approximation accuracy and the UAV position, (18b) is considered in this paper as a conservative but efficient constraint on UAV trajectories to avoid the low OP approximation accuracy, such as the case with $\breve { \mathbf q } _ { n } = [ 0 , 3 ] ^ { T }$

![](images/236e71845ba871287819bc262d44697ade5f457febdca63a019cad952120963e.jpg)  
(a) Convergence behaviour of proposed algorithms.  
Fig. 5. Performance of proposed algorithms.

To obtain important insights into the relationship between the UAV trajectory and OPs, Fig. 4(a) and Fig. 4(b) illustrate the OP at the prediction stage within a given range of $\breve { \mathbf { q } } _ { n }$ with $N _ { \mathrm { t } } = 3 2$ and $N _ { \mathrm { t } } = 6 4$ , respectively.<sup>9</sup> A typically high target constant received SNR is set as $\breve { \gamma } _ { n } = 0 . 9 7 5 \gamma _ { \mathrm { m a x } }$ for both cases, and other system parameters are specified as: $\mathbf { M } _ { 0 } = 1 0 ^ { - 4 } \mathbf { I }$ , N = 1, $y _ { \mathrm { m i n } } = 3$ m and $a _ { 1 } = a _ { 2 } = 0 . 1$ As shown in Fig. 4(a) and Fig. 4(b), the optimal predicted UAV trajectories resulting in the minimum OP exist at the line of $\breve { y } _ { n } = y _ { \mathrm { { m i n } } }$ , i.e., the minimum distance from the BS, with a certain x-axis coordinate given by ±5.8 m in both cases. Around the optimal predicted UAV trajectories, there exist certain regions where the OP is relatively low. Compared to the case with $N _ { \mathrm { t } } = 3 2$ , the low-OP region with $N _ { \mathrm { t } } = 6 4$ becomes smaller and more concentrated at the optimal predicted UAV trajectories. Also, the positions near the direction $\breve { \theta } _ { n } = 0 ^ { \circ }$ are not contained in the low-OP region with $N _ { \mathrm { t } } = 6 4$ . To explain such results, Fig. 4(c) and Fig. 4(d) show the accurate CORs with different predicted UAV trajectories $\breve { \mathbf { q } } _ { n }$ corresponding to the cases in Fig. 4(a) and Fig. 4(b), respectively. In both cases, the COR width increases when the predicted UAV trajectory $\breve { \mathbf { q } } _ { n }$ varies from the direction $\breve { \theta } _ { n } = 9 0 ^ { \circ } { \mathrm { ~ t o ~ } } \breve { \theta } _ { n } = 0 ^ { \circ }$ , which is the main reason why the optimal predicted UAV trajectory $\breve { \mathbf { q } } _ { n } ^ { * }$ is located at the line of $\breve { y } _ { n } = y _ { \mathrm { { m i n } } }$ . However, the UAV should be sufficiently close to the BS due to the potentially severe path loss, and the requirement of letting its dominant part of $\check { \mathbf { q } } _ { n }$ or ${ \dot { \mathbf { q } } } _ { n }$ PDF be contained in the COR. Therefore, the predicted UAV trajectory $\breve { \mathbf { q } } _ { n }$ achieves a trade-off between minimizing the path loss and being covered by the mainlobe beam for minimizing the OP. Moreover, as illustrated in Fig. 4(a) and Fig. 4(b), the smaller low-OP region with $N _ { \mathrm { t } } ~ = ~ 6 4$ is due to the narrower beam pattern generated by the larger transmit antenna number.

![](images/0a94d03887d7109de8774540b319f63bc439272b6f326988935c19e1d078f848.jpg)  
(b) Outage capacity versus sensing duration ratio.

## B. Proposed Algorithms

Fig. 5(a) shows the convergence behaviour of our proposed search-based algorithm and AO-based algorithm in cases with $\varepsilon _ { \mathrm { o u t } } = 1 0 ^ { - 2 }$ and $\varepsilon _ { \mathrm { o u t } } = 1 0 ^ { - 3 }$ . The initial state of the UAV is given by $\mathbf { x } _ { 0 } = [ 0 , 0 , 4 , 0 ] ^ { T }$ and the initial estimated state variables are represented by $\hat { \textbf { x } } _ { 0 } ~ = ~ \textbf { x } _ { 0 } + \textbf { z } _ { 0 }$ with $\begin{array} { r l } { \mathbf { z } _ { 0 } } & { { } = } \end{array}$ $[ 0 . 0 8 3 , - 0 . 0 0 1 , \bar { 0 . } 0 3 7 , 0 . 0 4 2 ] ^ { T }$ The other system parameters are given by: $a _ { 1 } = a _ { 2 } = 0 . 7 , N _ { \mathrm { t } } = N _ { \mathrm { r } } = 6 4 , N = 1$ , and $\mathbf { M } _ { 0 } \mathbf { \bar { \Pi } } = 1 0 ^ { - 3 } \mathbf { I }$ . As shown in Fig. 5(a), the convergence of our proposed search-based algorithm is verified and our proposed AO-based algorithm also exhibits satisfactory convergence performance in both cases. Particularly, despite the slight fluctuation of the maximized outage capacity owing to the heuristic update of $\breve { \mathbf { q } } _ { n } ,$ , the output of our proposed AO-based algorithm approaches the maximum outage capacity much faster than the search-based algorithm, which demonstrates its effectiveness and considerably reduced computational complexity. Besides, compared to the case with $\varepsilon _ { \mathrm { o u t } } ~ = ~ 1 0 ^ { - 2 }$ the maximum outage capacity significantly decreases and its fluctuation under the AO-based algorithm is more obvious in the case with $\varepsilon _ { \mathrm { o u t } } ~ = ~ 1 0 ^ { - 3 }$ , indicating the difficulty of maintaining a large outage capacity with a stringent OP tolerance threshold $\varepsilon _ { \mathrm { o u t } }$

Fig. 5(b) demonstrates the varying trends of the outage capacity w.r.t. the sensing duration ratio $w _ { n }$ with different UAV positions. The initial UAV states in the two cases are given by $\mathbf { x } _ { 0 } = [ 4 , 0 , 0 , 0 ] ^ { T }$ and $\mathbf { x } _ { 0 } = [ 0 , 0 , 4 , 0 ] ^ { T }$ , respectively, to emphasize the different varying trends of outage capacity w.r.t. $w _ { n }$ . The other system parameters are as those in Fig. 5(a) except the OP threshold given by $\varepsilon _ { \mathrm { o u t } } ~ = ~ 1 0 ^ { - 2 }$ It can be observed that the impact of $w _ { n }$ on the outage capacity with ${ \bf q } _ { 0 } ~ = ~ [ 0 , 4 ] ^ { T }$ is much larger than that with $\mathbf { q } _ { 0 } ~ = ~ [ 4 , 0 ] ^ { T }$ . This is because, when the UAV is at $[ 0 , 4 ] ^ { T }$ the state measurement provides a highly accurate estimation of the UAV trajectory and thus $C _ { \mathbf { e } , n }$ can be quite larger than $C _ { \mathfrak { p } , n }$ . Under such circumstances, the sensing duration ratio $w _ { n }$ achieves a fundamental trade-off between sensing and sensing-assisted communication: when $w _ { n }$ is too small, the matched-filtering gain is insufficient to obtain highly accurate sensing results and thus cannot significantly enhance the communication efficiency or reliability; however, when $w _ { n }$ is exceedingly large, the duration of enjoying the highly accurate beam alignment from sensing becomes limited, which also leads to sub-optimal communication performance. In contrast to the case with ${ \bf q } _ { 0 } = { \bf \{ 0 , 4 \} } ^ { T }$ , the sensing gain is negligible when the UAV is at $[ 4 , 0 ] ^ { T }$ due to the almost infinite measurement noise variance of the azimuth angle, resulting in the minor effect of sensing duration ratio $w _ { n }$ on the outage capacity. Therefore, when the UAV trajectory is infavorable to sensing, incorporating the measured results contributes little to the outage capacity enhancement and thus the overhead for real-time state measurement can be saved. Moreover, Fig. 5(b) verifies that a near-optimal solution can be obtained by the subalgorithm for solving (P3.1) of the AO-based algorithm.

## C. UAV Trajectories and System Performance

In this subsection, the results of our proposed UAV trajectory optimization scheme are compared with those of benchmarks in the prediction MSE-dominant (PMD) and prediction MSE-nondominant (PMnD) case, respectively. In the PMD case, the prediction MSE is so much smaller than the measurement MSE that ${ \bf K } _ { n }$ ≈ 0 holds [38], which leads to the estimation MSE donimated by the prediction MSE, i.e., $\mathbf { M } _ { n } \approx \mathbf { M } _ { \mathrm { p } , n } ,$ due to (11). Comparatively, the PMnD scenario refers to the case where the prediction MSE is not sufficiently smaller than the measurement MSE to satisfy ${ \mathbf { K } } _ { n } \approx \mathbf { 0 } .$ , indicating that the measurement MSE is small and the measured results are useful for decreasing the estimation MSE. In both cases, our proposed UAV trajectory design is compared with the following benchmarks:

• Straight flight and hover (SFH): The UAV directly flies towards a specific position denoted by q<sub>F</sub> with its maximum velocity $v _ { \mathrm { A , m a x } }$ and then hovers at $\mathbf { q } _ { \mathrm { F } }$ [31].

• Posterior Cramer-Rao bound (PCRB) minimization (m-´ PCRB): At each time slot, the UAV trajectory is optimized to minimize the sum of predicted PCRBs for state variables of the next time slot, which can be expressed as [7]

$$
\operatorname* { m i n } _ { \check { \mathbf { q } } _ { n } } ~ \mathrm { T r } ( \mathbf { M } _ { n } | _ { \mathbf { x } _ { n } = \check { \mathbf { x } } _ { n } } ) ~ \mathrm { s . t . } ~ ( 1 8 \mathrm { a } ) ~ .
$$

$\tilde { \sigma } _ { 1 , n } ^ { 2 }$ minimization $( \mathbf { m } { - } \tilde { \sigma } _ { 1 , n } ^ { 2 } ) { : }$ At each time slot, the UAV trajectory is optimized to minimize the approximated measurement noise variance for azimuth angle $\theta _ { n }$ of the next time slot denoted by $\tilde { \sigma } _ { 1 , n } ^ { 2 } = \sigma _ { 1 , n } ^ { 2 } | _ { \mathbf { x } _ { n } = \Breve { \mathbf { x } } _ { n } }$ , which can be expressed as

$$
\operatorname * { m i n } _ { \check { \mathbf { q } } _ { n } } ~ \tilde { \sigma } _ { 1 , n } ^ { 2 } ~ \mathrm { s . t . } ~ ( 1 8 \mathrm { a } ) , ~ ( 1 8 \mathrm { b } ) ~ .
$$

The sensing duration ratio $w _ { n }$ is given by $w _ { \mathrm { m a x } } = 1$ to ensure the sensing performance as much as possible for all benchmarks.

1) UAV Trajectories: Fig. 6(a) and Fig. 6(b) illustrate the UAV trajectories obtained by the benchmarks and our proposed UAV trajectory optimization scheme in both the PMD and PMnD cases. To compare the dynamical UAV trajectories under different schemes during the whole $N \Delta T = 2 0 ~ \mathrm { s }$ , the initial UAV motion state under all schemes are uniformly set as $\mathbf { x } _ { 0 } = [ 2 0 , 0 , 2 0 , 0 ] ^ { T }$ . The measurement capability coefficients are set as $a _ { 1 } ~ = ~ a _ { 2 } ~ = ~ 1$ and $a _ { 1 } ~ = ~ a _ { 2 } ~ = ~ 0 . 1$ for the PMD and PMnD case, respectively. To fairly compare our proposed scheme and benchmarks, the constraint (18b) with $y _ { \mathrm { m i n } } = 1$ is also applied in the $\mathbf { m } { - } \tilde { \sigma } _ { 1 , n } ^ { 2 }$ scheme and the specific position under the SFH scheme is given by ${ \bf q } _ { \mathrm { F } } = { \bf \Psi } [ 1 , 1 ] ^ { T }$ Other system parameters are given by $\tilde { q } \ = \ 1 0 ^ { - 5 }$ . First, it can be observed from both Fig. 6(a) and Fig. 6(b) that the UAV trajectory obtained by our proposed AO-based algorithm (dentoed by “Prop.”) well match the results obtained by the exhaustive search (denoted by “Ex.”), which validates the effectiveness of our proposed AO-based algorithm. Second, in both the PMD and PMnD cases, the UAV trajectory under the m-PCRB scheme is approximately circular to maintain an optimal distance minimizing the PCRB, while the UAV under the $\mathbf { m } { - } \tilde { \sigma } _ { 1 , n } ^ { 2 }$ scheme approaches the BS in the direction of $\theta _ { n } \ = \ 9 0 ^ { \circ }$ and then hovers around $[ 0 , 1 ] ^ { T }$ , which is the optimal position for minimizing ${ \tilde { \sigma } } _ { 1 , n } ^ { 2 } .$ . Different from the UAV trajectories under benchmarks, the UAV under our proposed scheme tends to approach the BS with a relatively smaller azimuth angle and then stay at the straight line with $\breve { y } _ { n } = y _ { \mathrm { { m i n } } }$ parallel to the BS ULA antennas in both the PMD and PMnD cases. The reason for such trajectory is that being at the line with $\breve { y } _ { n } ~ = ~ y _ { \mathrm { { m i n } } }$ leads to wide COR/beam cov erage, which is consistent with our previous observation from Fig. 4(a) and Fig. 4(b) and also demonstrates the importance of beam coverage to signal reception reliability. Consequently, the predicted UAV trajectory parallel to the BS ULA antennas with $\breve { y } _ { n } = y _ { \mathrm { { m i n } } }$ is advantageous for outage capacity maximization. In addition, the UAV trajectory with $\varepsilon _ { \mathrm { o u t } } = 1 0 ^ { - 4 }$ is generally farther away from the BS than that with $\varepsilon _ { \mathrm { o u t } } = 1 0 ^ { - 2 }$ in both the PMD and PMnD cases, indicating that a larger UAV-BS distance is more beneficial for enhancing the communication reliability.

2) Outage Capacities: Fig. 7(a) and Fig. 7(b) compare the outage capacities achieved by the benchmarks and our proposed scheme in both cases. Particularly, the outage capacities of benchmarks are calculated by our proposed algorithm for (P3.1) given their optimized predicted UAV trajectories and the OP threshold $\varepsilon _ { \mathrm { o u t } } \stackrel { - } { = } 1 0 ^ { - 2 }$ . As illustrated in Fig. 7(a), the communication performances under the SFH and $\mathbf { m } { - } \tilde { \sigma } _ { 1 , n } ^ { 2 }$ scheme exhibit large random variations similar as fast fadings in the PMD case. The reason is that the UAV is improperly near the BS and can be easily away from the COR/beam coverage due to the position uncertainty. The outage capacity under the m-PCRB scheme are relatively stable but limited by the high path loss. Comparatively, the outage capacity under our proposed scheme is much more stable than benchmarks and also higher than benchmarks for over 0.2 bps/Hz, which validates the effectiveness and superiorities of our proposed outage capacity maximization scheme over benchmarks in the PMD case. Nevertheless, Fig. 7(b) shows that such superiorities disappear in the PMnD case because the small measurement MSE leads to a low OP even if the UAV is close to the BS. Besides, the outage capacity under our proposed scheme in the case with $\varepsilon _ { \mathrm { o u t } } = 1 0 ^ { - 4 }$ is lower than that with $\varepsilon _ { \mathrm { o u t } } = 1 0 ^ { - 2 }$ , which shows the trade-off between the communication reliability and efficiency.

![](images/347f914ba2073507d64ee302f1dd7239999651269f4ab6b96075a39562dfe6dc.jpg)  
(a) UAV trajectories in the PMD case.

![](images/0577ea895cb86d7c5e421ac7f24f232400fb7a2bb748b7e0c952fd4e702b6da7.jpg)  
(b) UAV trajectories in the PMnD case.

Fig. 6. UAV trajectory comparisons between the PMD and PMnD case.  
![](images/176e51f204a922fbc3fc87e1fec2594d49ad836672529dc56e8aa9c802d175e3.jpg)  
(a) Outage capacities in the PMD case.

![](images/d79c4f4cf582b670dd3f86f580c815c2f6659c0ceaf63c3a1d20457cdf8d3c0e.jpg)  
(b) Outage capacities in the PMnD case.

![](images/a6f948c2d9b3e988d3457b8de4b063629da9f986d3ef340de06b4755dcc183b0.jpg)  
(c) Sum of root PCRBs in the PMnD case.  
Fig. 7. System performance comparsions among different schemes between the PMD and PMnD case.

3) Sensing Accuracies: Fig. 7(c) compares the sensing accuracies under our proposed scheme among different $\varepsilon _ { \mathrm { o u t } }$ in the PMnD case. The sensing accuracy is characterized by the sum of root PCRBs for $x _ { n }$ and $y _ { n }$ given by $\sqrt { [ \mathbf { M } _ { n } ] _ { 1 1 } } \dot { + }$ $\sqrt { [ \mathbf { M } _ { n } ] _ { 3 3 } }$ [7]. It can be seen that the sensing accuracy gradually maintains stable with the increasing of time resulted from the little variance of UAV trajectory. Besides, the sensing accuracy is generally higher with a larger $\varepsilon _ { \mathrm { o u t } }$ . This is because the UAV tends to obtain a smaller azimuth angle w.r.t. the BS for a wider beam coverage, by which means the more stringent OP tolerance constraint can be satisfied. However, such UAV trajectory can degrade the measurement MSE for the azimuth angle, which further results in the larger estimation MSE. Therefore, the UAV trajectory also achieves a trade-off between the sensing accuracy and the tolerated minimum OP in our system.

## VI. CONCLUSION

This paper studied the outage capacity maximization for UAV tracking enabled by sensing-assisted predictive beamforming, where the UAV trajectory, sensing duration ratio, and target constant received SNRs were jointly optimzied. To facilitate the formulation of a tractable optimization problem, closed-form OP approximations were proposed based on second-order Taylor expansions, which also characterized the outage capacity. Then, two efficient algorithms were proposed to address the non-convex approximated optimization problem: a search-based algorithm with ensured convergence and an AO-based algorithm with lower complexity. Simulation results verified the effectiveness of our proposed approximations, algorithms, and the superiority of the proposed joint UAV tracking and outage capacity maximization scheme over benchmarks in the PMD case. Furthermore, our results demonstrated that the optimal predicted UAV trajectory tended to be parallel to the BS ULA antennas with a nonzero minimum distance, achieving a trade-off between decreasing path loss and increasing beam coverage area for outage capacity maximization. The extension of our proposed approximations to multi-static ISAC systems are worthwhile future works.

## APPENDIX A PROOF OF PROPOSITION 1

According to the EKF framework [33], the state vector at each time slot can be approximately Gaussian distributed, represented by $\mathbf { x } _ { n - 1 } \sim { \mathcal { N } } ( { \hat { \mathbf { x } } } _ { n - 1 } , \mathbf { M } _ { n - 1 } ) , \forall n \in \{ 1 , 2 , \ldots , N \}$ Thus, $\mathbf { x } _ { n } \sim \mathcal { N } ( \breve { \mathbf { x } } _ { n } , \mathbf { M } _ { \mathsf { p } , n } )$ is derived from (3) and (8). Furthermore, as a marginal distribution of the state vector $\mathbf { x } _ { n } .$ the ground-truth UAV trajectory ${ \bf q } _ { n }$ is also Gaussian distributed given by $\mathbf { q } _ { n } \sim \mathcal { N } ( \breve { \mathbf { q } } _ { n } , \breve { \mathbf { N } } _ { n } )$ with

$$
\breve { \mathbf { A } } _ { n } = \left[ \breve { \Lambda } _ { \mathrm { x } , n } ^ { 2 } \breve { \Lambda } _ { \mathrm { x y } , n } ^ { 2 } \right] = \left[ \left[ \mathbf { M } _ { \mathrm { p } , n } \right] _ { 1 1 } \left[ \mathbf { M } _ { \mathrm { p } , n } \right] _ { 1 3 } \right] .\tag{46}
$$

Therefore, $\check { \mathbf { q } } _ { n } \sim { \mathcal { N } } ( \mathbf { 0 } , \check { \mathbf { N } } _ { n } )$ holds. Note that $\tilde { \xi } _ { \mathfrak { p } , n }$ is a univariate function of $\check { \mathbf { q } } _ { n }$ . Then, the approximated $\mathrm { O P }$ at the prediction stage of the nth time slot (29) can be derived from (15) with $\begin{array} { r } { \mathcal { Q } _ { \mathfrak { p } , n } \approx \tilde { \mathcal { Q } } _ { \mathfrak { p } , n } , \mathrm { i . e . } } \end{array}$

$$
\zeta _ { \mathsf { p } , n } \approx \tilde { \zeta } _ { \mathsf { p } , n } = 1 - \int _ { \hat { x } _ { \mathrm { L } } } ^ { \hat { x } _ { \mathrm { U } } } \left( \int _ { \hat { y } _ { \mathrm { L } } ( \hat { x } _ { n } ) } ^ { \hat { y } _ { \mathrm { U } } ( \hat { x } _ { n } ) } f ( \acute { \mathbf { q } } _ { n } ) \mathrm { d } \acute { y } _ { n } \right) \mathrm { d } \acute { x } _ { n } ,\tag{47}
$$

where $f ( \cdot )$ denotes the Gaussian PDF of $\acute { \mathbf { q } } _ { n } , \acute { x } _ { \mathrm { \scriptscriptstyle L } }$ and $\acute { x } _ { \mathrm { U } }$ can be obtained from the equation $\mathrm { d } \acute { x } _ { n } / \mathrm { d } \acute { y } _ { n } = 0$ . This completes the proof.

## APPENDIX B

## PROOF OF PROPOSITION 2

For notational simplicity, we adopt $\chi$ to represent either the function $\breve { \chi }$ or χˆ. Accordingly, $\gamma , \bar { x } , \chi _ { \mathrm { U } } , \chi _ { \mathrm { L } } , \Lambda _ { \mathrm { x } , n } , \Lambda _ { n }$ represents $\breve { \gamma } _ { n } , \acute { x } _ { n } , \breve { \chi } _ { \mathrm { U } } , \breve { \chi } _ { \mathrm { L } } , \breve { \Lambda } _ { \mathrm { x } , n } , \breve { \Lambda } _ { n }$ in the case where $\chi$ denotes $\breve { \chi } ,$ , and $\hat { \gamma } _ { n } , \dot { x } _ { n } \hat { \chi } _ { \mathrm { U } } , \hat { \chi } _ { \mathrm { L } } , \hat { \Lambda } _ { \mathrm { x } , n } , \hat { \Lambda } _ { n }$ in the case where $\chi$ denotes $\hat { \chi } ,$ respectively. Then, an upperbound of the partial derivative of $\chi$ w.r.t. γ can be derived as

$$
\frac { \partial \chi } { \partial \gamma } \leq A \left( \frac { \partial Y _ { 1 } } { \partial \gamma } + ( \bar { x } + \check { x } _ { n } ) ^ { 2 } \frac { \partial Y _ { 2 } } { \partial \gamma } \right) = A \rho ( \gamma ) ,\tag{48}
$$

with $\begin{array} { r } { A = \frac { \Lambda _ { \mathrm { x } , n } \operatorname* { m a x } \left\{ \frac { e ^ { - \chi _ { \mathrm { U } } ( \gamma ) ^ { 2 } } } { \sqrt { \pi } } , \frac { e ^ { - \chi _ { \mathrm { L } } ( \gamma ) ^ { 2 } } } { \sqrt { \pi } } \right\} } { \sqrt { 2 | \operatorname* { d e t } ( \Lambda _ { n } ) | ( Y _ { 1 } + Y _ { 2 } ( \hat { x } + \hat { x } _ { n } ) ^ { 2 } ) } } } \end{array}$ . The derivative of $\rho ( \gamma )$ w.r.t. γ can be derived as $\begin{array} { r } { \frac { \mathrm { d } \rho } { \mathrm { d } \gamma } = \frac { ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 6 } \tilde { P } ( \rho _ { 1 } \gamma + \rho _ { 0 } ) } { ( ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } \gamma + \check { x } _ { n } ^ { 2 } \check { y } _ { n } ^ { 2 } \tilde { P } M ) ^ { 4 } } } \end{array}$ , where the specific expressions of $\rho _ { 0 }$ and $\rho _ { 1 }$ are given by

$$
\rho _ { 0 } = 2 \check { x } _ { n } ^ { 2 } \check { y } _ { n } ^ { 2 } \tilde { P } M ( \check { y } _ { n } ^ { 2 } ( ( \dot { x } _ { n } + \check { x } _ { n } ) ^ { 2 } ( \check { x } _ { n } ^ { 2 } + 2 \check { y } _ { n } ^ { 2 } )
$$

$$
+ \breve { x } _ { n } ^ { 2 } H ^ { 2 } ) M + ( \breve { x } _ { n } ^ { 2 } + \breve { y } _ { n } ^ { 2 } ) ^ { 3 } N _ { \mathrm { t } } ) \geq 0 ,\tag{49}
$$

$$
\begin{array} { c } { { \rho _ { 1 } = 2 { \check { y } } _ { n } ^ { 2 } ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 3 } ( ( \dot { x } _ { n } + \check { x } _ { n } ) ^ { 2 } ( \check { x } _ { n } ^ { 2 } - \check { y } _ { n } ^ { 2 } ) + \check { x } _ { n } ^ { 2 } H ^ { 2 } ) M } } \\ { { + \ 2 ( \check { x } _ { n } ^ { 2 } + \check { y } _ { n } ^ { 2 } ) ^ { 6 } N _ { \mathrm { t } } . } } \end{array}\tag{50}
$$

Next, two cases with $\rho _ { 1 } ~ \geq ~ 0$ and $\rho _ { 1 } ~ < ~ 0$ are discussed, respectively. For the case with $\rho _ { 1 } ~ \geq ~ 0 , ~ { \frac { \mathrm { d } \rho } { \mathrm { d } \gamma } } ~ \geq ~ 0$ holds due to $\gamma \ \geq \ 0$ . As for the case with $\rho _ { 1 } ~ < ~ 0 , ~ \frac { \mathrm { d } \rho } { \mathrm { d } \gamma }$ is a monotonically nonincreasing function. Since both $\frac { \mathrm { d } \rho } { \mathrm { d } \gamma } | _ { \gamma = 0 } \geq 0$ and $\operatorname* { l i m } _ { \gamma \to \infty } { \frac { \mathrm { d } \rho } { \mathrm { d } \gamma } } \geq 0$ can be obtained, $\begin{array} { r } { \frac { \mathrm { d } \rho } { \mathrm { d } \gamma } \geq 0 } \end{array}$ also holds in this case. Thus, $\rho ( \gamma )$ is a monotonically nondecreasing function of $\gamma .$ . Finally, both $\rho ( 0 ) \leq 0$ and $\operatorname* { l i m } _ { \gamma \to \infty } \rho ( \gamma ) = 0$ can be obtained. As a result, $\begin{array} { r } { \frac { \partial { \boldsymbol { \chi } } } { \partial \gamma } \leq A \rho ( \gamma ) \leq 0 } \end{array}$ holds, completing the proof.

## REFERENCES

[1] W. Khawaja et al., “A survey on detection, classification, and tracking of UAVs using radar and communications systems,” IEEE Commun. Surveys Tuts., vol. 28, pp. 3272–3310, 2025.

[2] Y. Wang et al., “Toward realization of low-altitude economy networks: Core architecture, integrated technologies, and future directions,” 2025, arXiv:2504.21583.

[3] Y. Jiang et al., “Integrated sensing and communication for low altitude economy: Opportunities and challenges,” IEEE Commun. Mag., vol. 63, no. 12, pp. 72–78, Dec. 2025.

[4] C. Zhao, Y. Feng, H. Luo, F. Gao, F. Liu, and S. Jin, “Networked ISACbased UAV tracking and handover toward low-altitude economy,” IEEE Trans. Wireless Commun., vol. 24, no. 9, pp. 7670–7685, Sep. 2025.

[5] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2912–2945, Oct. 2021.

[6] F. Liu et al., “Integrated sensing and communications: Toward dualfunctional wireless networks for 6G and beyond,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1728–1767, Jun. 2022.

[7] F. Dong, F. Liu, Y. Cui, W. Wang, K. Han, and Z. Wang, “Sensing as a service in 6G perceptive networks: A unified framework for ISAC resource allocation,” IEEE Trans. Wireless Commun., vol. 22, no. 5, pp. 3522–3536, May 2023.

[8] Z. Du et al., “Toward ISAC-empowered vehicular networks: Framework, advances, and opportunities,” IEEE Wireless Commun., vol. 32, no. 2, pp. 222–229, Apr. 2025.

[9] G. Chen, Q. Wu, S. Lu, M. Hua, and W. Chen, “Multi-IRS aided ISAC system: Multi-path exploitation versus reduction,” 2025, arXiv:2506.21968.

[10] F. Liu, W. Yuan, C. Masouros, and J. Yuan, “Radar-assisted predictive beamforming for vehicular links: Communication served by sensing,” IEEE Trans. Wireless Commun., vol. 19, no. 11, pp. 7704–7719, Nov. 2020.

[11] W. Yuan, F. Liu, C. Masouros, J. Yuan, D. W. K. Ng, and N. Gonzalez-´ Prelcic, “Bayesian predictive beamforming for vehicular networks: A low-overhead joint radar-communication approach,” IEEE Trans. Wireless Commun., vol. 20, no. 3, pp. 1442–1456, Mar. 2021.

[12] C. Liu et al., “Learning-based predictive beamforming for integrated sensing and communication in vehicular networks,” IEEE J. Sel. Areas Commun., vol. 40, no. 8, pp. 2317–2334, Aug. 2022.

[13] X. Meng, F. Liu, C. Masouros, W. Yuan, Q. Zhang, and Z. Feng, “Vehicular connectivity on complex trajectories: Roadway-geometry aware ISAC beam-tracking,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 7408–7423, Nov. 2023.

[14] X. Zhang, W. Yuan, C. Liu, J. Wu, and D. W. K. Ng, “Predictive beamforming for vehicles with complex behaviors in ISAC systems: A deep learning approach,” IEEE J. Sel. Topics Signal Process., vol. 18, no. 5, pp. 828–841, Jul. 2024.

[15] Z. Wang, V. W. S. Wong, and R. Schober, “Integrated sensing and communications for end-to-end predictive beamforming design in vehicle-to-infrastructure networks,” IEEE J. Sel. Topics Signal Process., vol. 18, no. 5, pp. 933–949, Jul. 2024.

[16] Z. Du et al., “Integrated sensing and communications for V2I networks: Dynamic predictive beamforming for extended vehicle targets,” IEEE Trans. Wireless Commun., vol. 22, no. 6, pp. 3612–3627, Jun. 2023.

[17] C. Yanpeng et al., “Sensing-assisted accurate and fast beam management for cellular-connected mmWave UAV network,” China Commun., vol. 21, no. 6, pp. 271–289, Jun. 2024.

[18] J. Zhang et al., “Deep learning-empowered secure predictive beamforming design for integrated sensing and communications systems,” IEEE, vol. 24, no. 10, pp. 8565–8580, Oct. 2025.

[19] A. A. Al-Habob, O. A. Dobre, and Y. Jing, “Predictive beamforming approach for secure integrated sensing and communication with multiple aerial eavesdroppers,” IEEE Trans. Commun., vol. 73, no. 9, pp. 7887–7898, Sep. 2025.

[20] A. Khalili, A. Rezaei, D. Xu, F. Dressler, and R. Schober, “Efficient UAV hovering, resource allocation, and trajectory design for ISAC with limited backhaul capacity,” IEEE Trans. Wireless Commun., vol. 23, no. 11, pp. 17635–17650, Nov. 2024.

[21] A. Khalili, A. Rezaei, D. Xu, and R. Schober, “Energy-aware resource allocation and trajectory design for UAV-enabled ISAC,” in Proc. IEEE Global Commun. Conf., Dec. 2023, pp. 4193–4198.

[22] M. A. Richards, Fundamentals of Radar Signal Processing. New York, NY, USA: McGraw-Hill, 2005.

[23] D. Xu, Y. Sun, D. W. K. Ng, and R. Schober, “Multiuser MISO UAV communications in uncertain environments with no-fly zones: Robust trajectory and resource allocation design,” IEEE Trans. Commun., vol. 68, no. 5, pp. 3153–3172, May 2020.

[24] B. Chang, W. Tang, X. Yan, X. Tong, and Z. Chen, “Integrated scheduling of sensing, communication, and control for mmWave/THz communications in cellular connected UAV networks,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2103–2113, Jul. 2022.

[25] A. Goldsmith, Wireless Communications. Cambridge, U.K.: Cambridge Univ. Press, 2005.

[26] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[27] Y. Bar-Shalom, X. R. Li, and T. Kirubarajan, Estimation With Applications to Tracking and Navigation. Hoboken, NJ, USA: Wiley, 2001.

[28] J. Yan, H. Liu, B. Jiu, B. Chen, Z. Liu, and Z. Bao, “Simultaneous multibeam resource allocation scheme for multiple target tracking,” IEEE Trans. Signal Process., vol. 63, no. 12, pp. 3110–3122, Jun. 2015.

[29] Y. Jiang, Q. Wu, W. Chen, and K. Meng, “UAV-enabled integrated sensing and communication: Tracking design and optimization,” IEEE Commun. Lett., vol. 28, no. 5, pp. 1024–1028, May 2024.

[30] Q. Wu, J. Xu, and R. Zhang, “Capacity characterization of UAV-enabled two-user broadcast channel,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1955–1971, Sep. 2018.

[31] K. Meng, Q. Wu, S. Ma, W. Chen, K. Wang, and J. Li, “Throughput maximization for UAV-enabled integrated periodic sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 1, pp. 671–687, Jan. 2023.

[32] C. Huang et al., “Machine learning-enabled LOS/NLOS identification for MIMO systems in dynamic environments,” IEEE Trans. Wireless Commun., vol. 19, no. 6, pp. 3643–3657, Jun. 2020.

[33] S. M. Kay, Fundamentals of Statistical Signal Processing: Estimation Theory, vol. 1. Englewood Cliffs, NJ, USA: Prentice-Hall, 1998.

[34] M. Grant and S. Boyd. (2014). CVX: MATLAB Software for Disciplined Convex Programming. [Online]. Available: http://cvxr.com/cvx

[35] J. Kim, H. Lee, C. Song, T. Oh, and I. Lee, “Sum throughput maximization for multi-user MIMO cognitive wireless powered communication networks,” IEEE Trans. Wireless Commun., vol. 16, no. 2, pp. 913–923, Feb. 2017.

[36] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.

[37] K. Meng, Q. Wu, W. Chen, and D. Li, “Sensing-assisted communication in vehicular networks with intelligent surface,” IEEE Trans. Veh. Technol., vol. 73, no. 1, pp. 876–893, Jan. 2024.

[38] G. Welch et al., An Introduction to the Kalman Filter, Chapel Hill, NC, USA, 1995.

![](images/e0c646abe08cd97bc3f1f24df6591cbbe172ff039a5f7faff890777d4db9daf3.jpg)  
Yifan Jiang received the B.S. and M.S. degrees in science in electronics engineering from Beijing Institute of Technology (BIT), China, in 2018 and 2021, respectively. He is currently pursuing the Ph.D. degree with the State Key Laboratory of Internet of Things for Smart City, University of Macau, Macau, China. His research interests include unmanned aerial vehicles and integrated sensing and communications. He serves as a TPC Member for IEEE VTC2025-Spring and IEEE ICC 2026.

![](images/0a5a42a6cdede40270d2b74a9a967e4221b65b0832c283356596cd9811876546.jpg)

Qingqing Wu (Senior Member, IEEE) is currently an Associate Professor with Shanghai Jiao Tong University. He has co-authored more than 100 IEEE journal articles with more than 40 ESI highly cited articles, which have received more than 50 000 Google Scholar citations. His current research interests include intelligent reflecting surface (IRS), uncrewed aerial vehicle (UAV) communications, and MIMO transceiver design.

Dr. Wu was a recipient of the IEEE ComSoc Fred Ellersick Prize, the Best Tutorial Paper Award in

2023, Asia–Pacific Best Young Researcher Award and Outstanding Paper Award in 2022, the Young Author Best Paper Award in 2021 and 2024, the Outstanding Ph.D. Thesis Award of China Institute of Communications in 2017, the IEEE ICCC Best Paper Award in 2021, and the IEEE WCSP Best Paper Award in 2015. He has been listed as a Clarivate ESI Highly Cited Researcher since 2021, the Most Influential Scholar Award in AI-2000 by Aminer since 2021, the World’s Top 2% Scientist by Stanford University since 2020, and a Xiaomi Young Scholar. He is the Workshop Co-Chair of IEEE ICC (2019–2023) and IEEE GLOBECOM 2020. He serves as the Workshops and Symposia Officer for the Reconfigurable Intelligent Surfaces Emerging Technology Initiative and the Research Blog Officer for the Aerial Communications Emerging Technology Initiative. He served as the Chair for the IEEE ComSoc Young Professional AP Committee and the Chair for the IEEE VTS Drone Committee. He was an Exemplary Editor of IEEE COMMUNICATIONS LETTERS in 2019 and an exemplary reviewer of several IEEE journals. He serves as an Associate/Senior/Area Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE COMMUNICATIONS LETTERS, and IEEE WIRELESS COMMUNICATIONS LETTERS. He is a Lead Guest Editor of IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS.

![](images/0b345827bed40b7c22de0a1ac72b56bac1aed8c9aeceaeaccc8825b014aed5c7.jpg)

Hongxun Hui (Senior Member, IEEE) received the B.E. and Ph.D. degrees in electrical engineering from Zhejiang University, Hangzhou, China, in 2015 and 2020, respectively. From 2018 to 2019, he was a Visiting Scholar with the Advanced Research Institute, Virginia Tech, Blacksburg, VA, USA, and the CURENT Center, University of Tennessee, Knoxville, TN, USA. He is currently an Assistant Professor with the State Key Laboratory of Internet of Things for Smart City, University of Macau, Macau, SAR, China. His research focuses on smart grid optimization and control, demand response, power economics, carbon markets, and interdisciplinary energy-environment systems.

![](images/7dac60e59d6781b5cc89f39712b16e25479b4164b2d62caaa744cf66b33b965a.jpg)

Wen Chen (Senior Member, IEEE) received the B.S. and M.S. degrees from Wuhan University, China, in 1990 and 1993, respectively, and the Ph.D. degree from the University of Electro-Communications, Japan, in 1999. He is currently a tenured Professor with the Department of Electronic Engineering, Shanghai Jiao Tong University, China. His research interests cover green multiple access, ISAC networks, wireless AI, and RIS communications. He is a Clarivate Highly Cited Researcher and a fellow of Chinese Institute of Electronics. In his research area, he received the First-Tier Shanghai Natural Science Award in 2023. He is the Shanghai Chapter Chair of the IEEE Vehicular Technology Society and the Vice President of Shanghai Institute of Electronics. He was the Distinguished Lecturer of the IEEE Communications Society and the IEEE Vehicular Technology Society and an Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS and IEEE TRANSACTIONS ON COMMUNICATIONS.

![](images/bf2ba8ff67bc7c59feb2e332c0c9f020e458d00c2328c589cf305c9fc69c98a8.jpg)

Derrick Wing Kwan Ng (Fellow, IEEE) received the bachelor’s (Hons.) and the Master of Philosophy degrees in electronic engineering from The Hong Kong University of Science and Technology (HKUST), Hong Kong, in 2006 and 2008, respectively, and the Ph.D. degree from The University of British Columbia, Vancouver, BC, Canada, in November 2012.

Following his Ph.D. studies, he was a Senior Post-Doctoral Fellow at the Institute for Digital Communications, Friedrich-Alexander-University

Erlangen–Nurnberg (FAU), Germany. He is currently a Scientia Associate¨ Professor with the University of New South Wales, Sydney, NSW, Australia. His research interests include global optimization, integrated sensing and communication (ISAC), physical layer security, IRS-assisted communication, UAV-assisted communication, wireless information and power transfer, and green (energy-efficient) wireless communications. He has been recognized as a Highly Cited Researcher by Clarivate Analytics (Web of Science) since 2018. He was a recipient of Australian Research Council (ARC) Discovery Early Career Researcher Award in 2017; the IEEE Communications Society Leonard G. Abraham Prize in 2023; the IEEE Communications Society Stephen O. Rice Prize in 2022; the Best Paper Awards at the 2020 and 2021 WCSP; the IEEE TCGCC Best Journal Paper Award in 2018; the 2018 INISCOM; the IEEE International Conference on Communications (ICC) in 2018, 2021, 2023, and 2024; the IEEE International Conference on Computing, Networking and Communications (ICNC), in 2016; the IEEE Wireless Communications and Networking Conference (WCNC) in 2012; the IEEE Global Telecommunication Conference (Globecom) in 2011, 2021, 2023, and 2025; and the IEEE Third International Conference on Communications and Networking in China in 2008. From January 2012 to December 2019, he served as an Editorial Assistant to the Editor-in-Chief for IEEE TRANSACTIONS ON COMMUNICATIONS. He is an Area Editor of IEEE TRANSACTIONS ON COMMUNICATIONS, the Associate Editor-in-Chief of IEEE OPEN JOURNAL OF THE COMMUNICATIONS SOCIETY, and an Executive Editorial Committee Member of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS.