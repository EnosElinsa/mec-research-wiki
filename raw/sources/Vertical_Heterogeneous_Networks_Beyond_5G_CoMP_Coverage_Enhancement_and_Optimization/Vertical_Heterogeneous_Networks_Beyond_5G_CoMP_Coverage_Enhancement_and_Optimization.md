# Vertical Heterogeneous Networks Beyond 5G: CoMP Coverage Enhancement and Optimization

Tian Shi , Wenkun Wen , Member, IEEE, Peiran Wu , Member, IEEE, and Minghua Xia , Senior Member, IEEE

Abstract—Low-altitude wireless networks are increasingly vital for the low-altitude economy, enabling wireless coverage in highmobility and hard-to-reach environments. However, providing reliable connectivity to sparsely distributed aerial users in dynamic three-dimensional (3D) spaces remains a significant challenge. This paper investigates downlink coverage enhancement in vertical heterogeneous networks (VHetNets) beyond 5G, where uncrewed aerial vehicles (UAVs) operate as emerging aerial base stations (ABSs) alongside legacy terrestrial base stations (TBSs). To improve coverage performance, we propose a coordinated multi-point (CoMP) transmission framework that enables joint transmission from ABSs and TBSs. This approach mitigates the limitations of non-uniform user distributions and enhances reliability for sparse aerial users. Two UAV deployment strategies are considered: i) random UAV placement, analyzed using stochastic geometry to derive closed-form coverage expressions, and ii) optimized UAV placement using a coverage-aware weighted K-means clustering algorithm to maximize cooperative coverage in underserved areas. Theoretical analyses and Monte Carlo simulations demonstrate that the proposed CoMP-enabled VHetNet significantly improves downlink coverage probability, particularly in scenarios with sparse aerial users. These findings highlight the potential of intelligent UAV coordination and geometry-aware deployment to enable robust, adaptive connectivity in low-altitude wireless networks.

Index Terms—Coordinated multi-point transmission, lowaltitude wireless networks, stochastic geometry, uncrewed aerial vehicles, vertical heterogeneous networks.

## I. INTRODUCTION

L <sup>OW-ALTITUDE</sup> <sup>wireless</sup> <sup>networks</sup> <sup>are</sup> <sup>emerging</sup> <sup>as</sup> <sup>a</sup> cornerstone of the low-altitude economy, enabled by technological innovation and increasingly diverse applications [1]. Among the key enablers are aerial platforms, particularly uncrewed aerial vehicles (UAVs), which function as modern aerial base stations (ABSs) equipped with flexible deployment and high mobility, operating alongside legacy terrestrial base stations (TBSs). Together, they form a vertical heterogeneous network (VHetNet) that integrates the advantages of both air- and ground-based infrastructures. This integrated architecture has gained significant attention for its potential to provide seamless communication services to both aerial and ground users. Thanks to their mobility and deployment flexibility, UAVs are well-suited to a range of scenarios, particularly during emergency response [2], disaster recovery [3], and large-scale events [4].

However, aerial users are often sparsely distributed, especially in dynamic three-dimensional (3D) airspace. In such settings, cooperative operation among multiple UAVs becomes essential to ensure reliable service. This paper addresses two deployment strategies for ABSs tailored to such scenarios: random deployment and intentional placement. In the former, stochastic geometry tools are employed to analytically evaluate downlink coverage under a coordinated multi-point (CoMP) transmission framework. In the latter, a coverageaware weighted K-means clustering algorithm is proposed to optimize UAV placement, thereby improving coverage in underserved regions.

## A. Related Works and Motivation

CoMP transmission is a well-established technique designed to enhance spectral efficiency and mitigate inter-cell interference [5]. It has been extensively explored in heterogeneous networks, where cooperation among TBSs has been shown to improve both rate and reliability [6]. Simulation studies [7] and field trials [8] have further validated the benefits of CoMP. To reduce the overhead associated with TBS searching, efficient implementations using Poisson-Delaunay triangulation have also been proposed for TBS cooperation [9], [10].

Recently, CoMP strategies involving ABSs have gained significant attention. For instance, UAV swarms have been investigated for cooperative air-to-ground communications and formation control [11]. Additionally, CoMP-based handoff schemes have been proposed to improve mobility and reliability in UAV-assisted networks beyond 5G [12]. However, even with CoMP, aerial users may encounter coverage interruptions at certain altitudes due to altitude-dependent channel variability, which can degrade link quality.

VHetNets, which integrate ABSs and TBSs, have emerged as a promising solution for enhancing connectivity, coverage continuity, and link robustness. Previous studies have analyzed downlink performance using stochastic geometry under both line-of-sight (LoS) and non-line-of-sight (NLoS) conditions for ground users [13]. Other research has explored altitudeaware association behavior and the benefits of ABSs in dense areas [14]. Novel architectures, such as deploying ABSs on roadside infrastructure for optimized trajectory planning and enhanced aerial coverage, have also been proposed [15].

TABLE I  
COMPARISON OF RELATED WORKS ON VHETNETS
<table><tr><td rowspan=1 colspan=1>Ref.</td><td rowspan=1 colspan=1>ABSs</td><td rowspan=1 colspan=1>TBSs</td><td rowspan=1 colspan=1>G2A Model</td><td rowspan=1 colspan=1>Tx Scheme</td></tr><tr><td rowspan=1 colspan=1>[10]</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>LoS link</td><td rowspan=1 colspan=1>CoMP</td></tr><tr><td rowspan=1 colspan=1>[11], [12]</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>LoS link</td><td rowspan=1 colspan=1>CoMP</td></tr><tr><td rowspan=1 colspan=1>[13]</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>LoS/NLoS link</td><td rowspan=1 colspan=1>Single</td></tr><tr><td rowspan=1 colspan=1>[15]</td><td rowspan=1 colspan=1>PLCP</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>LoS/NLoS link</td><td rowspan=1 colspan=1>Single</td></tr><tr><td rowspan=1 colspan=1>[16], [17]</td><td rowspan=1 colspan=1>3D PPP</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>LoS link</td><td rowspan=1 colspan=1>Single</td></tr><tr><td rowspan=1 colspan=1>[18]</td><td rowspan=1 colspan=1>3D BPP</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>LoS link</td><td rowspan=1 colspan=1>CoMP</td></tr><tr><td rowspan=1 colspan=1>[22]</td><td rowspan=1 colspan=1>BPP</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>LoS link</td><td rowspan=1 colspan=1>Single</td></tr><tr><td rowspan=1 colspan=1>[24], [25]</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>LoS/NLoS link</td><td rowspan=1 colspan=1>Single</td></tr><tr><td rowspan=1 colspan=1>[14], [23], [26]</td><td rowspan=1 colspan=1>BPP</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>LoS/NLoS link</td><td rowspan=1 colspan=1>Single</td></tr><tr><td rowspan=1 colspan=1>This paper</td><td rowspan=1 colspan=1>BPP</td><td rowspan=1 colspan=1>PPP</td><td rowspan=1 colspan=1>LoS/NLoS link</td><td rowspan=1 colspan=1>CoMP</td></tr></table>

On a broader scale, stochastic geometry has been applied to satellite-integrated VHetNets to model uplink connectivity via terrestrial and aerial relays, considering terahertz propagation and association strategies [16]. A spherical stochastic geometry framework has also been introduced to study global-scale VHetNet connectivity [17]. However, transitioning from 2D to 3D space fundamentally alters the geometric structure—volume increases at a much faster rate than surface area, leading to increased data sparsity and reduced point density [18]. These challenges complicate reliable connectivity and necessitate the development of new analytical tools and deployment strategies.

Stochastic geometry provides a robust analytical framework for modeling such networks. The Poisson point process (PPP) [19] is commonly used for TBSs due to its mathematical tractability, while the binomial point process (BPP) [20], [21] is better suited for modeling finite ABS deployments. BPPbased models have been applied to UAV networks under Nakagami-m fading [22], as well as for joint uplink–downlink analysis in UAV networks [23]. A key challenge in modeling CoMP in VHetNets lies in analytically deriving the joint distance distributions between a typical user and multiple cooperating ABSs and TBSs in 3D space. For brevity, Table I compares the relevant works.

The sparse distribution of aerial users, combined with the analytical tractability of stochastic geometry, highlights both the necessity and feasibility of developing CoMP strategies for VHetNets. Such strategies are essential for enhancing system capacity, improving user experience, and ensuring robust, seamless connectivity across 3D space.

## B. Contributions

This paper presents a comprehensive study on CoMPenabled VHetNets, focusing on both analytical coverage analysis and UAV deployment optimization. The main contributions are as follows:

1) Novel Network Model: We propose a 3D VHetNet architecture that facilitates joint CoMP transmission among triads of ABSs and TBSs, using Poisson-Delaunay triangulation. This cooperative model significantly enhances service quality for spatially distributed aerial users while minimizing the overhead of cooperation.

2) Analytical Distance Distributions: In contrast to prior works that focus only on the nearest base station, we derive both marginal and joint probability density functions (PDFs) for distances to the general n-nearest ABSs and TBSs $( n \ge 1 )$ , laying the foundation for user association and coverage evaluation. Notably, a tworegime user association behavior is identified.

3) Deployment Optimization: We examine two deployment strategies: for randomly deployed ABSs, we evaluate performance analytically using stochastic geometry; for optimal deployment, we propose a coverage-aware weighted K-means clustering algorithm to guide ABS placement toward coverage-deficient regions.

4) Coverage Analysis: We derive closed-form expressions for the downlink coverage probability of aerial users under CoMP transmission. Monte Carlo simulations confirm the analytical accuracy and demonstrate the substantial performance gains enabled by the proposed UAV-based CoMP strategies.

The remainder of the paper is organized as follows: Section II describes the system and channel models. Section III characterizes the distributions of service distance and received signal. Sections IV and V analyze user association behavior and network coverage probability, respectively. Section VI presents an optimized UAV deployment strategy. Numerical results and discussions are given in Section VII, followed by conclusions in Section VIII.

## II. SYSTEM AND CHANNEL MODELS

We consider a VHetNet comprising legacy TBSs and emerging ABSs, with a focus on analyzing downlink performance under a CoMP transmission to sparse aerial user equipments (UEs).

## A. System Model

As illustrated in Fig. 1, the aerial network comprises N UAVs, each equipped with an ABS hovering at the same altitude of H. The locations of these ABSs are modeled as a finite BPP, denoted by $\Phi _ { \mathrm { A B S } }$ , uniformly distributed within a circular region of radius $r _ { C }$ , centered at (0, 0, H). In contrast, the TBSs are assumed to follow a homogeneous PPP, denoted by $\Phi _ { \mathrm { T B S } }$ with intensity $\lambda _ { \mathrm { T B S } }$ and located at height $h _ { \mathrm { T B S } }$ . The overall network is then defined as the union $\Phi = \Phi _ { \mathrm { A B S } } \cup \Phi _ { \mathrm { T B S } }$ , where $\Phi _ { \mathrm { A B S } }$ and $\Phi _ { \mathrm { T B S } }$ are assumed to be statistically independent, i.e., $\Phi _ { \mathrm { A B S } } \perp \Phi _ { \mathrm { T B S } }$

To distinguish between aerial and terrestrial base station tiers, we define a tier indicator function κ(x) for any node $x \in \Phi ;$

$$
\begin{array} { r } { \kappa ( x ) = \left\{ \begin{array} { l l } { \mathrm { A B S , } } & { \mathrm { i f ~ } x \in \Phi _ { \mathrm { A B S } } ; } \\ { \mathrm { T B S , } } & { \mathrm { i f ~ } x \in \Phi _ { \mathrm { T B S } } . } \end{array} \right. } \end{array}
$$

When an aerial UE communicates with a TBS, the wireless link may experience either LoS or NLoS propagation due to terrestrial obstructions, as depicted in Fig. 1. In contrast, the link between an aerial UE and an ABS is assumed always to be LoS. Let x denote the location of a transmitter and define the link distance as $r = \| x \|$ . We introduce an indicator variable $\zeta ( x ) \ \in \ \{ \mathrm { L } , \mathrm { N } \}$ to denote the propagation state of the link, where $\zeta ( x ) = \operatorname { I }$ if the link is LoS, and $\zeta ( x ) = \Nu$ otherwise. Conditioned on r, the variable ζ(x) is modeled as a Bernoulli random variable whose success probability depends on the tier of the transmitter:

![](images/523b4a88a8f74c363020fa85dd2b3c0e3e103801c349f450679a3ff9936f71f4.jpg)  
Fig. 1. An illustration of a vertical heterogeneous network (VHetNet) comprising legacy terrestrial base stations (TBSs) and emerging aerial base stations (ABSs). The air-to-air (A2A) links between spatial UEs and ABSs typically experience line-of-sight (LoS) propagation due to their elevated positions. In contrast, the ground-to-air (G2A) links between TBSs and spatial UEs may undergo either LoS or non-line-of-sight (NLoS) propagation, depending on the environment and obstructions. To enhance network coverage performance, a coordinated multi-point (CoMP) transmission strategy is adopted in this work.

$$
\mathbb { P } \big [ \zeta ( x ) = \mathbf { L } \mid r \big ] = \left\{ { \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } \kappa ( x ) = \mathbf { A } \mathbf { B } \mathbf { S } ; } \\ { P _ { \mathrm { L } } ( r ) , } & { { \mathrm { i f ~ } } \kappa ( x ) = \mathbf { T } \mathbf { B } \mathbf { S } , } \end{array} } \right.
$$

where $0 \leq P _ { \mathrm { L } } ( r ) \leq 1$ denotes the LoS probability for TBS links, and the corresponding NLoS probability is defined as $P _ { \mathrm { N } } ( r ) \triangleq 1 - P _ { \mathrm { L } } ( r )$

For any parameter or random variable X that depends on both the serving tier $\kappa \in \{ \mathrm { A B S } , \mathrm { T B S } \}$ and the propagation condition $\zeta \in \{ \mathrm { L } , \mathrm { N } \}$ , we adopt the unified notation:

$$
X _ { \kappa , \zeta } = \left\{ { \begin{array} { l l } { X _ { \mathrm { A B S } } , } & { { \mathrm { i f ~ } } \kappa = \mathrm { A B S } ; } \\ { X _ { \mathrm { T B S } , \zeta } , } & { { \mathrm { i f ~ } } \kappa = \mathrm { T B S } . } \end{array} } \right.
$$

This convention extends similarly for superscripts, $\mathrm { e . g . }$ $X ^ { ( \kappa , \zeta ) }$ . For instance, $\alpha _ { \kappa , \zeta }$ corresponds to the path loss exponent, which simplifies to $\alpha _ { \mathrm { A B S } }$ for ABS links, and distinguishes between $\alpha _ { \mathrm { T B S , L } }$ and α<sub>TBS,N</sub> for TBS links, depending on whether the propagation condition is LoS or NLoS.

Remarkably, our system model is primarily focused on providing downlink service to aerial users and does not explicitly account for terrestrial users. However, in the presence of cochannel terrestrial uplink activity, additional interference is introduced at ground level, leading to a decrease in the aerial signal-to-interference ratio (SIR). As the density or transmit power of these terrestrial uplink users increases, the coverage for aerial users degrades monotonically. In the PPP model, this additional interference is captured as an extra Laplace factor in the interference term, which results in a strictly lower success probability for aerial users.

## B. Channel Model

In this study, we assume that aerial users hover at altitudes above surrounding buildings. Consequently, the air-to-air (A2A) links between a typical aerial UE and the ABSs are modeled as LoS channels, consistent with prior works [18], [27]. In contrast, existing ground-to-air (G2A) models have primarily been developed for terrestrial users located at approximately 1.5 meters in height and, therefore, do not accurately reflect the propagation characteristics experienced by aerial users at higher altitudes. To address this, our model assumes TBSs are deployed at elevated positions, such as 30-meter macro base stations [28]. Under these conditions, G2A links are subject to both LoS and NLoS propagation, as supported by empirical studies [26].

To model the LoS probability for G2A links, we adopt a simplified expression proposed in [14]. Specifically, the LoS probability, denoted by $P _ { \mathrm { L } } ( z )$ , is given by

$$
P _ { \mathrm { L } } ( z ) = - a \exp { ( - b \delta ) } + c ,\tag{1}
$$

where $\delta = \arctan ( h / z )$ is the elevation angle, z represents the horizontal distance between the aerial user and the base station, and a, b, and c are environment-specific parameters that implicitly capture the relative height difference between the aerial user and the TBS. For instance, $( a , b , c ) = ( 1 , 6 . 5 8 1 , 1 )$ in subarban areas and $( a , b , c ) ~ = ~ ( 1 . 1 2 4 , 0 . 0 4 9 , 1 . 0 2 4 )$ in highrise urban areas [14].

Both A2A and G2A channels are assumed to undergo Nakagami-m fading. The fading amplitude, denoted by $\mathrm { H } ^ { ( \kappa , \bar { \zeta } ) }$ is modeled as a Nakagami random variable: $\mathrm { ~ \cal ~ H ( } \kappa , \zeta ) \sim$ Nakagam $\mathfrak { i } ( m _ { \kappa , \zeta } , \Omega )$ , where $m _ { \kappa , \zeta } \geq 0 . 5$ is the fading severity (shape) parameter and $\Omega = \mathbb { E } [ ( \bar { \mathrm { H } } ^ { ( \kappa , \zeta ) } ) ^ { 2 } ]$ denotes the average received power. The corresponding PDF is given by [29]:

$$
f _ { \mathrm { H } ^ { ( \kappa , \varsigma ) } } ( x ) = \frac { 2 m _ { \kappa , \zeta } ^ { m _ { \kappa , \zeta } } x ^ { 2 m _ { \kappa , \zeta } - 1 } } { \Gamma ( m _ { \kappa , \zeta } ) \Omega ^ { m _ { \kappa , \zeta } } } \exp \left( - \frac { m _ { \kappa , \zeta } } { \Omega } x ^ { 2 } \right) , x \geq 0 .\tag{2}
$$

Assuming all base stations transmit with equal power and that thermal noise is negligible compared to interference, the instantaneous SIR at a typical aerial UE can be expressed as

$$
\Gamma _ { \chi } \triangleq \frac { S _ { \chi } } { I } = \frac { \left( \sum _ { n \in \mathcal { C } _ { \chi } } \left| \mathrm { H } _ { n } ^ { ( \kappa _ { n } , \zeta _ { n } ) } \right| ( R _ { n } ) ^ { - \alpha _ { \kappa _ { n } , \zeta _ { n } } / 2 } \right) ^ { 2 } } { \sum _ { \Upsilon \in Q } \sum _ { k \in \Phi _ { \Upsilon } \backslash \mathcal { C } _ { \chi } } \mathrm { G } _ { k } ^ { ( \Upsilon , \zeta _ { k } ) } ( D _ { k } ) ^ { - \alpha _ { \Upsilon , \zeta _ { k } } } } , \chi \in Q ,\tag{3}
$$

where $R _ { n }$ and $D _ { k }$ denote the distances from a typical UE to the $n ^ { \mathrm { t h } }$ cooperating base station and the $k ^ { \mathrm { { t h } } }$ interferer, respectively; $\alpha _ { \kappa , \zeta }$ is the path loss exponent associated with tier $\kappa \in \mathsf { \Omega } \{ \mathsf { A B S } , \mathsf { T B S } \}$ and link state $\zeta ~ \in ~ \{ \mathrm { L } , \mathrm { N } \} ; ~ \mathrm { H } ^ { ( \kappa , \zeta ) }$ and $\mathbf { G } ^ { ( \kappa , \zeta ) } \overset { \circ } { = } ( \mathrm { \ddot { H } } ^ { ( \kappa , \zeta ) } ) ^ { 2 }$ represent the fading amplitude and channel power gain, respectively; $S _ { \chi }$ denotes the aggregated received signal power from cooperating base stations in the coordination set ${ \mathcal { C } } _ { \chi } ;$ I is the total interference from all other non-cooperating base stations, and Q is the set of all base station tiers.

TABLE II SUMMARY OF NOTATION
<table><tr><td rowspan=1 colspan=1>Notation</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>h</td><td rowspan=1 colspan=1>Height of the aerial user with referenceto the TBSs</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>Height of the ABSs with referenceto the TBSs</td></tr><tr><td rowspan=1 colspan=1> $r _ { C }$ </td><td rowspan=1 colspan=1>Radius of the circle where ABSsare distributed</td></tr><tr><td rowspan=1 colspan=1> $\kappa _ { n } , \zeta _ { n }$ </td><td rowspan=1 colspan=1>The tier label and the LoS/NLoS stateof the $n ^ { \mathrm { t h } }$ link</td></tr><tr><td rowspan=1 colspan=1> $R _ { n } ^ { \mathrm { A B S } } , R _ { n } ^ { \mathrm { T B S } }$ </td><td rowspan=1 colspan=1>Distance between the aerial userand its nth nearest ABS or TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $D _ { k } ^ { \mathrm { A B S } } , D _ { k } ^ { \mathrm { T B S } }$ </td><td rowspan=1 colspan=1>Distance between the aerial userand interfering ABS or LoS TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { L } } ( \cdot ) , P _ { \mathrm { N } } ( \cdot )$ </td><td rowspan=1 colspan=1>Probability of the aerial user beingin LoS and NLoS with TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $m _ { \mathrm { A B S } } , m _ { \mathrm { T B S , L } } , m _ { \mathrm { T B S , N } }$ </td><td rowspan=1 colspan=1>Nakagami-m fading parameter for ABS,LoS TBS, or NLoS TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $\alpha _ { \mathrm { A B S } } , \alpha _ { \mathrm { T B S } , \mathrm { L } } , \alpha _ { \mathrm { T B S } , \mathrm { N } }$ </td><td rowspan=1 colspan=1>Path loss parameter for ABS, LoS TBS,or NLoS TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $\overline { { \lambda _ { \mathrm { T B S } } } }$ </td><td rowspan=1 colspan=1>Density of terrestrial base stations</td></tr><tr><td rowspan=1 colspan=1> $\Phi _ { \mathrm { A B S } } , \Phi _ { \mathrm { T B S } } , \Phi$ </td><td rowspan=1 colspan=1>Tier of the ABSs, the TBSs,or the overall BSs, respectively</td></tr><tr><td rowspan=1 colspan=1> $\mathrm { H } _ { n } ^ { \mathrm { A B S } } , \mathrm { H } _ { n } ^ { \mathrm { ( T B S , L ) } } , \mathrm { H } _ { n } ^ { \mathrm { ( T B S , N ) } }$ </td><td rowspan=1 colspan=1>Channel fading amplitude of the $\overline { { n ^ { \mathrm { t h } } \operatorname* { l i n k } } }$ between the aerial user and an ABS, LoS TBS,or NLoS TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $\mathbf { G } _ { k } ^ { \mathrm { A B S } } , \mathbf { G } _ { k } ^ { ( \mathrm { T B S , L } ) } , \mathbf { G } _ { k } ^ { ( \mathrm { T B S , N } ) }$ </td><td rowspan=1 colspan=1>Channel power gain of the $\overline { { k ^ { \mathrm { t h } } \operatorname { l i n k } } }$ between the aerial user and an ABS, LoS TBS,or NLoS TBS, respectively</td></tr><tr><td rowspan=1 colspan=1> $\mathcal { A } _ { \mathrm { A B S } } , \mathcal { A } _ { \mathrm { T B S } }$ </td><td rowspan=1 colspan=1>Probability that the typical user is associatedwith three ABSs or TBSs</td></tr><tr><td rowspan=1 colspan=1> $I , { \mathcal { L } } _ { \sqrt { I } } , { \mathcal { L } } _ { I }$ </td><td rowspan=1 colspan=1>Interference, Laplace transform of ${ \overline { { \sqrt { I } } } } ,$ and Laplace transform of interference</td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { A B S } } , P _ { \mathrm { T B S } }$ </td><td rowspan=1 colspan=1>Coverage probability given that the typical useris associated with three ABSs or TBSs</td></tr></table>

Notably, the received power $\mathrm { G } ^ { ( \kappa , \zeta ) }$ follows a Gamma distribution with shape $m _ { \kappa , \zeta }$ and scale $\Omega / m _ { \kappa , \zeta } , \mathrm { i . e . , } \ \mathrm { G } ^ { ( \kappa , \zeta ) } \sim$ $\Gamma ( m _ { \kappa , \zeta } , \Omega / m _ { \kappa , \zeta } )$ . For convenience, the key notations used throughout this paper are summarized in Table II.

## III. MATHEMATICAL PRELIMINARY: DISTRIBUTIONS OF SERVICE DISTANCE AND RECEIVED SIGNAL

Due to the sparse and spatially dispersed distribution of aerial UEs in 3D space, ensuring reliable coverage often requires coordinated transmission from multiple base stations. However, to the best of our knowledge, the statistical characterization of service distances—specifically, the distribution of the distance to the $n ^ { \mathrm { t h } } .$ -nearest base station, and the joint distribution of distances to the nearest $n > 1$ base stations—has not been explicitly derived for 3D VHetNets. Such distributions are essential for accurately analyzing the performance of CoMP strategies and form the mathematical foundation for the subsequent analysis in this paper. Moreover, these results offer analytical tools for broader research on cooperative aerial networks.

## A. Distributions of Service Distance

We first characterize the service distance from a typical aerial UE to the $n ^ { \mathrm { t h } } .$ -nearest ABS.

Lemma 1 (ABS Case) The PDF of the distance from a typical aerial UE to the $n ^ { \mathrm { t h } }$ nearest ABS is given by

$$
f _ { R _ { n } } ^ { \mathrm { A B S } } ( r ) = \frac { N ! } { ( n - 1 ) ! ( N - n ) ! } \left( \frac { 2 r } { r _ { C } ^ { 2 } } \right) \left( \frac { r ^ { 2 } - ( H - h ) ^ { 2 } } { r _ { C } ^ { 2 } } \right) ^ { n - 1 }
$$

where $H - h \leq r \leq r _ { \operatorname* { m a x } } ,$ with $r _ { \mathrm { m a x } } \triangleq \sqrt { ( H - h ) ^ { 2 } + r _ { C } ^ { 2 } } .$ The joint PDF of the distances to the nearest $n > 1$ ABSs is given by

$$
\begin{array} { l } { { \displaystyle f _ { R _ { 1 } , R _ { 2 } , \cdots , R _ { n } } ^ { \mathrm { A B S } } \left( r _ { 1 } , r _ { 2 } , \cdots , r _ { n } \right) } \ ~ } \\ { { \displaystyle = \frac { N ! } { ( N - n ) ! } \left( \frac { 2 } { r _ { C } ^ { 2 } } \right) ^ { n } r _ { 1 } r _ { 2 } \cdots r _ { n } \left( \frac { r _ { \mathrm { m a x } } ^ { 2 } - r _ { n } ^ { 2 } } { r _ { C } ^ { 2 } } \right) ^ { N - n } , } } \end{array}\tag{5}
$$

where $H - h \leq r _ { 1 } \leq r _ { 2 } \leq \cdots \leq r _ { n } \leq r _ { \operatorname* { m a x } } .$

Proof: See Appendix A.

For the special case of n = 1, (4) simplifies to

$$
f _ { R _ { 1 } } ^ { \mathrm { A B S } } ( r ) = N \left( \frac { 2 r } { r _ { C } ^ { 2 } } \right) \left( \frac { r _ { \mathrm { m a x } } ^ { 2 } - r ^ { 2 } } { r _ { C } ^ { 2 } } \right) ^ { N - 1 } ,\tag{6}
$$

which matches the result reported in [22, Eq. (7)].

Next, we derive the corresponding distribution for TBSs.

Lemma 2 (TBS Case) The PDF of the distance from a typical aerial UE to the $n ^ { \mathrm { t h } }$ nearest TBS is given by

$$
\begin{array} { r } { f _ { R _ { n } } ^ { \mathrm { T B S } } ( r ) = \frac { 2 \left( \pi \lambda _ { \mathrm { T B S } } \right) ^ { n } r } { \Gamma \left( n \right) } \left( r ^ { 2 } - h ^ { 2 } \right) ^ { n - 1 } } \\ { \times \exp \left( - \pi \lambda _ { \mathrm { T B S } } ( r ^ { 2 } - h ^ { 2 } ) \right) , } \end{array}\tag{7}
$$

where $r > h$ . The joint PDF of the distances to the $n > 1$ nearest TBSs is given by

$$
\begin{array} { l } { { \displaystyle f _ { R _ { 1 } , R _ { 2 } , \cdots , R _ { n } } ^ { \mathrm { T B S } } \left( r _ { 1 } , r _ { 2 } , \cdots , r _ { n } \right) } \ ~ } \\ { { \displaystyle = ( 2 \pi \lambda _ { \mathrm { T B S } } ) ^ { n } \prod _ { i = 1 } ^ { n } r _ { i } \exp \left( - \pi \lambda _ { \mathrm { T B S } } ( r _ { n } ^ { 2 } - h ^ { 2 } ) \right) , } } \end{array}\tag{8}
$$

where $h \leq r _ { 1 } \leq r _ { 2 } \leq \cdot \cdot \cdot \leq r _ { n }$

Proof: See Appendix B.

For the special case of n = 1, (7) reduces to

$$
f _ { R _ { 1 } } ^ { \mathrm { T B S } } ( r ) = 2 \pi \lambda _ { \mathrm { T B S } } r \exp \left( - \pi \lambda _ { \mathrm { T B S } } ( r ^ { 2 } - h ^ { 2 } ) \right) ,\tag{9}
$$

which is consistent with [26, Eq. (6)] under the assumption $P _ { \mathrm { L } } ( \cdot ) = 1$

While the derived service distance distributions enable accurate performance evaluation, increasing the cooperation size n enhances coverage but also introduces additional coordination overhead. As shown in the literature [9], [10], [30], [31], cooperation among three base stations significantly improves coverage probability compared to single- or dual-base station CoMP. However, the marginal gain from adding a fourth or more base stations becomes negligible. Therefore, an effective trade-off is achieved when each aerial UE is served by exactly three base stations, forming the CoMP set $\mathcal { C } _ { \chi }$ with cardinality $| \mathcal { C } _ { \chi } | = 3$ . Specifically,

$$
\begin{array} { r l } & { \qquad \mathcal { C } _ { \boldsymbol { \chi } } = \{ x _ { 1 } , x _ { 2 } , x _ { 3 } \} \subset \Phi _ { \boldsymbol { \chi } } , \quad \boldsymbol { \chi } \in Q \triangleq \{ \operatorname { A B S } , \operatorname { T B S } \} , } \\ & { \qquad \| x _ { 1 } \| \leq \| x _ { 2 } \| \leq \| x _ { 3 } \| \leq \| x \| , \quad \forall \boldsymbol { x } \in \Phi _ { \boldsymbol { \chi } } \setminus \mathcal { C } _ { \boldsymbol { \chi } } . } \end{array}
$$

![](images/d6de024a9c0e8742b7f39181961e7571962cd13102cda547655ed3360963afb6.jpg)  
Fig. 2. An illustrative Poisson-Delaunay triangulation network where each CoMP set consists of either TBSs or ABSs located at the vertices of Delaunay triangles (outlined by blue solid edges). Red solid dots represent the positions of TBSs or ABSs. Blue stars denote aerial users, projected onto the 2D plane for association purposes. ABSs are distributed according to a finite Binomial Point Process (BPP) within a circular region of radius $r _ { \mathrm { C } } .$ At the same time, TBSs follow a homogeneous Poisson Point Process (PPP) over a normalized area of 1 km<sup>2</sup>.

For each $n = 1 , 2 , 3 ,$ , we define the link distance $r _ { n } = \| x _ { n } \|$ and the propagation condition $\zeta _ { n } = \zeta ( x _ { n } )$

In the presence of both ABSs and TBSs, if each aerial user associates with its closest base station, the resulting spatial partitioning follows a Poisson–Voronoi tessellation, as is typical in stochastic geometry. However, the mathematical treatment of such tessellations is challenging due to their structural complexity [9]. To address this, we consider the Poisson–Delaunay triangulation, which is the dual of the Voronoi diagram and offers more tractable analytical properties [9]. The Delaunay triangulation can be constructed using standard algorithms, e.g., Fortune’s sweep-line method, Bowyer–Watson insertion, or divide-and-conquer techniques [32].

Fig. 2 illustrates the 2D projection of the 3D scenario shown in Fig. 1, considering either the TBS or ABS tier. Red dots indicate base station locations, blue stars represent projected aerial users, and the yellow dashed lines mark the Poisson–Voronoi cell boundaries. The blue solid lines correspond to the edges of the dual Delaunay triangulation. Each triangle in the Delaunay graph defines a CoMP cluster composed of three base stations, such as the cluster $\mathcal { C } _ { \chi } ~ =$ $\{ A , B , C \}$ , which cooperatively serve users located within the interior of the triangle. Without loss of generality, we assume a typical aerial user is located at $( 0 , 0 , h )$ , where $0 \leq h \leq H$ and is served by its three nearest base stations, which may belong to either the TBS set $\Phi _ { \mathrm { T B S } }$ or the ABS set $\Phi _ { \mathrm { A B S } }$

## B. Distributions of Received Signal

As illustrated in Fig. 1, a CoMP set comprising either three ABSs or three TBSs forms a Delaunay triangle to cooperatively serve a typical aerial user. Let $\boldsymbol { \zeta } = ( \zeta _ { 1 } , \zeta _ { 2 } , \zeta _ { 3 } ) \in$ $\{ \mathrm { L } , \mathrm { N } \} ^ { 3 }$ denote the LoS or NLoS state of each serving base station (BS) in the CoMP set $\mathcal { C } _ { \chi }$

To facilitate the derivation of user association and coverage probability in subsequent sections, we define the aggregated

received signal strength as

$$
U _ { \mathcal { X } , \xi } \triangleq \sum _ { n \in \mathcal { C } _ { \boldsymbol { x } } } \left. \mathrm { H } _ { n } ^ { ( \chi , \zeta _ { n } ) } \right. ( R _ { n } ) ^ { - \alpha _ { \chi , \zeta _ { n } } / 2 } ,\tag{10}
$$

and the corresponding large-scale fading component as

$$
V _ { \chi , \zeta } \triangleq \sum _ { n \in \mathcal { C } _ { \chi } } ( R _ { n } ) ^ { - \alpha _ { \chi , \zeta n } / 2 } .\tag{11}
$$

To enable tractable analysis, the distributions of $U _ { \chi , \zeta }$ and $V _ { \chi , \zeta }$ are approximated using a Gamma distribution, as detailed in the following lemma.

Lemma 3: The PDFs of $U _ { x , \zeta }$ and $V _ { \chi , \zeta }$ can be approximated by Gamma distributions as

$$
f _ { U _ { x , \xi } } ( x ) = \frac { x ^ { \nu _ { x , \xi } - 1 } } { \theta _ { \chi , \xi } ^ { \nu _ { x , \xi } } \Gamma ( \nu _ { \chi , \xi } ) } \exp \left( - \frac { x } { \theta _ { \chi , \xi } } \right) ,\tag{12a}
$$

$$
f _ { V _ { \chi , \zeta } } ( x ) = \frac { x ^ { \nu _ { \chi , \zeta } ^ { \prime } - 1 } } { \left( \theta _ { \chi , \zeta } ^ { \prime } \right) ^ { \nu _ { \chi , \zeta } ^ { \prime } } \Gamma ( \nu _ { \chi , \zeta } ^ { \prime } ) } \exp \left( - \frac { x } { \theta _ { \chi , \zeta } ^ { \prime } } \right) ,\tag{12b}
$$

where the shape and scale parameters are given by

$$
\begin{array} { r l } & { \nu _ { x , \xi } = \frac { \left( \sum _ { n = 1 } ^ { 3 } A _ { n } \Delta _ { n } \right) ^ { 2 } } { \Omega \sum _ { n = 1 } ^ { 3 } B _ { n } + \sum _ { p \ne q } ^ { 3 } C _ { p , q } } - \left( \sum _ { n = 1 } ^ { 3 } A _ { n } \Delta _ { n } \right) ^ { 2 } } \\ & { \theta _ { x , \xi } = \frac { \Omega \sum _ { n = 1 } ^ { 3 } B _ { n } + \sum _ { p \ne q } ^ { 3 } \Delta _ { p } \Delta _ { q } C _ { p , q } - \left( \sum _ { n = 1 } ^ { 3 } A _ { n } \Delta _ { n } \right) ^ { 2 } } { \sum _ { n = 1 } ^ { 3 } A _ { n } \Delta _ { n } } , } \\ & { \nu _ { x , \xi } ^ { \prime } = \frac { \left( \sum _ { n = 1 } ^ { 3 } A _ { n } \right) ^ { 2 } } { \sum _ { n = 1 } ^ { 3 } B _ { n } + \sum _ { p \ne q } ^ { 3 } C _ { p , q } - \left( \sum _ { n = 1 } ^ { 3 } A _ { n } \right) ^ { 2 } } , \qquad ( 1 2 \ G ) } \\ & { \theta _ { x , \xi } ^ { \prime } = \frac { \sum _ { n = 1 } ^ { 3 } B _ { n } + \sum _ { p \ne q } ^ { 3 } C _ { p , q } - \left( \sum _ { n = 1 } ^ { 3 } A _ { n } \right) ^ { 2 } } { \sum _ { n = 1 } ^ { 3 } A _ { n } } , } \end{array}
$$

The intermediate terms used above are defined as follows:

$$
A _ { n } = \int _ { a _ { x } } ^ { b _ { x } } \left( r ^ { - \alpha _ { \chi , \zeta _ { n } } / 2 } P _ { \zeta _ { n } } ( r ) \right) f _ { R _ { n } } ^ { \chi } ( r ) \mathrm { d } r ,\tag{12e}
$$

$$
B _ { n } = \int _ { a _ { x } } ^ { b _ { x } } \left( r ^ { - \alpha _ { x , \zeta n } } P _ { \zeta _ { n } } ( r ) f _ { R _ { n } } ^ { \chi } ( r ) \mathrm { d } r , \right.\tag{12f}
$$

$$
C _ { p , q } = 2 \int _ { \substack { a _ { \chi } \leq r _ { 1 } \leq r _ { 2 } \leq r _ { 3 } \leq b _ { \chi } } } \bigg ( \sum _ { \zeta _ { p } , \zeta _ { q } \in Q } P _ { \zeta _ { p } } P _ { \zeta _ { q } }\tag{12g}
$$

$$
r _ { p } ^ { - \alpha _ { } { x } , \zeta _ { q } / 2 } r _ { q } ^ { - \alpha _ { } { x } , \zeta _ { p } / 2 } \bigg ) \times f _ { R _ { 1 } , R _ { 2 } , R _ { 3 } } ^ { \chi } \mathrm { d } r ,\tag{12h}
$$

$$
\Delta _ { n } = \frac { \Gamma \left( m _ { \chi , \zeta _ { n } } + \frac { 1 } { 2 } \right) } { \Gamma ( m _ { \chi , \zeta _ { n } } ) } \left( \frac { \Omega } { m _ { \chi , \zeta _ { n } } } \right) ^ { \frac { 1 } { 2 } }\tag{12i}
$$

with the integration bounds $( a _ { \chi } , b _ { \chi } )$ defined as

$$
( a _ { \chi } , b _ { \chi } ) = \left\{ \begin{array} { l l } { ( H - h , r _ { \mathrm { m a x } } ) , } & { \mathrm { i f ~ } \chi = \mathrm { A B S ; } } \\ { ( h , \infty ) , } & { \mathrm { i f ~ } \chi = \mathrm { T B S } . } \end{array} \right.\tag{12j}
$$

Proof: See Appendix C.

![](images/a19ff1d0ba41f3928c62b88c07969177ff105336ceae640b8c881a84ce1dbacb.jpg)  
Fig. 3. Association proportions of the three BS configurations (all ABS, all TBS, mixed) versus aerial user altitude h.

## IV. TWO-REGIME USER ASSOCIATION BEHAVIOR

Before analyzing the network coverage probability, we first derive the association probability. In general, a user is served by three base stations, which can be all ABSs, all TBSs, or a combination of both. Association is determined based on the long-term average received power, conditioned on the link being LoS or NLoS. A Monte Carlo simulation was conducted to model a network scenario with 50, 000 users uniformly distributed within a 3D rectangular prism of dimensions $1 0 0 0 \ \mathrm { m \times 1 0 0 0 \ \mathrm { m \times ( 3 0 - 3 0 0 ) } }$ m. The simulation considered 30 ABSs deployed within a circular area of radius 500 m, and TBSs were modeled with a density of 20 TBSs/km<sup>2</sup>. The TBS and ABS altitudes were fixed at 30 m and 320 m, respectively. The path loss exponents were set to $\alpha _ { \mathrm { A B S } } = \alpha _ { \mathrm { T B S , L } } = 2$ and $\alpha _ { \mathrm { T B S , N } } = 2 . 7$ . At each aerial user altitude, the proportions of users associated with three base stations were calculated for each of the following configurations: all ABSs, all TBSs, or a mix of both.

The results shown in Fig. 3 reveal that mixed configurations are rare, accounting for less than 10% of the cases and approximately 5% on average. Based on these observations, we limit our analysis to two mutually exclusive association scenarios: users are served by either i) three ABSs (A2A scenario) or ii) three TBSs (G2A scenario). Let $\mathcal { A } \chi = \mathbb { P } ( \mathcal { E } \chi )$ denote the probability of event $\mathcal { E } _ { \chi }$ , where $\chi \in \{ \mathrm { A B S } , \mathrm { T B S } \}$ In the A2A case, the user is associated with three ABSs, all of which have LoS links. In the G2A case, the three TBS links may exhibit any combination of LoS or NLoS conditions, resulting in 8 possible link state combinations.

Remark 1 (Practical Considerations for Adopting the Same-Layer Three-Site CoMP Strategy) We adopt the same-layer three-site CoMP strategy as the baseline for our analysis. In addition to the observations described above, this choice is motivated by several practical considerations: First, phaselevel synchronization and low-latency, deterministic backhaul are more readily achievable within the same operator/vendor domain, with a uniform frame configuration across all base stations. In contrast, cross-tier ABS–TBS CoMP faces challenges such as ABS clock drift in moving or semi-mobile scenarios, heterogeneous antenna and beam designs, and the complexities of combining air-to-ground and terrestrial backhaul with more stringent delay/jitter requirements. As a result, cross-tier cooperation is more commonly implemented as CS/CB-CoMP, while coherent CoMP is typically confined to same-tier clusters due to these operational challenges [31]. Thus, we treat cross-tier CoMP as a high-cost, less common extension.

![](images/c032c4955432b0d5b408faaf3c1c3451a472a457cb9c842bd809dcfd3408ac19.jpg)  
Fig. 4. LoS $( \zeta = \mathrm { L } )$ and NLoS (ζ = N) probabilities of the G2A channel versus aerial user altitude h in suburban and high-rise urban environments.

Based on the same-layer three-site CoMP strategy, the probability that a typical UE associates with three ABSs is given in the following lemma.

Lemma 4: The probabilities that a typical user is associated with three ABSs are given by

$$
\begin{array} { r l r } {  { A _ { \mathrm { A B S } } = \prod _ { \zeta \in \{ \mathrm { L } , \mathrm { N } \} ^ { 3 } } \prod _ { H - h \leq r _ { 1 } \leq r _ { 2 } } \frac { \gamma ( \nu _ { \mathrm { T B S } , \zeta } ^ { \prime } , ( \sum _ { n = 1 } ^ { 3 } r _ { n } ^ { - \frac { \alpha _ { \mathrm { A B S } } } { 2 } } ) / \theta _ { \mathrm { T B S } , \zeta } ^ { \prime } ) } { \Gamma ( \nu _ { \mathrm { T B S } , \zeta } ^ { \prime } ) } } } \\ & { } & { ~ r _ { 2 } \leq r _ { 3 } \leq r _ { \mathrm { m a x } } } \\ & { } & { \times f _ { R _ { 1 } , R _ { 2 } , R _ { 3 } } ^ { \mathrm { A B S } } \big ( r _ { 1 } , r _ { 2 } , r _ { 3 } \big ) \mathrm { d } r , ~ } & { ( 1 3 ) } \end{array}
$$

where $\gamma ( \cdot , \cdot )$ denotes the lower incomplete Gamma function. Proof: The association probability with ABSs is given by

$$
\begin{array} { r l } & { \mathcal { A } _ { \mathrm { A B S } } = \mathbb { P } \left( V _ { \mathrm { A B S } } > V _ { \mathrm { T B S } , \varsigma } , \forall \varsigma \in \{ \mathrm { L } , \mathrm { N } \} ^ { 3 } \right) } \\ & { \quad \quad = \displaystyle \prod _ { \zeta \in \{ \mathrm { L } , \mathrm { N } \} ^ { 3 } } \mathbb { P } \left( V _ { \mathrm { A B S } } > V _ { \mathrm { T B S } , \varsigma } \right) . } \end{array}\tag{14}
$$

Applying the law of total probability over the distance vectors to ABSs yields:

$$
\begin{array} { r l r } {  { \mathcal { A } _ { \mathrm { A B S } } = \prod _ { \zeta \in \{ \mathrm { L } , \mathrm { N } \} ^ { 3 } } \int _ { H - h \leq r _ { 1 } \leq r _ { 2 } } \mathbb { P } ( V _ { \mathrm { T B S } , \zeta } < \sum _ { n \in \mathcal { C } _ { \mathrm { A B S } } } r _ { n } ^ { - \alpha _ { \mathrm { A B S } } / 2 } ) } } \\ & { } & { \quad \quad \quad \quad \quad \quad r _ { 2 } \leq r _ { 3 } \leq r _ { \operatorname* { m a x } } } \\ & { } & { \quad \quad \times \ : f _ { R _ { 1 } , R _ { 2 } , R _ { 3 } } ^ { \mathrm { A B S } } \big ( r _ { 1 } , r _ { 2 } , r _ { 3 } \big ) \mathrm { d } r \quad \quad \quad ( 1 5 } \end{array}
$$

which, by evaluating the CDF of the Gamma-distributed variable $V _ { \mathrm { T B S } , \zeta }$ , becomes the desired (13). 

Using the complement rule, the TBS association probability is given by

$$
\mathcal { A } _ { \mathrm { T B S } } = 1 - \mathcal { A } _ { \mathrm { A B S } } .\tag{16}
$$

Fig. 4 illustrates the LoS and NLoS probabilities of the G2A channel as a function of user altitude h in suburban and dense high-rise urban environments. These propagation conditions significantly impact association behavior, as shown in Fig. 5.

![](images/d1e079ecc59f6a9abe8301f4e0e0bc0a421d46589f9a430b57031c61418ce9ed.jpg)  
Fig. 5. Association probabilities of an aerial user with the ABS and TBS versus aerial user altitude h, with ABS fixed at $H = 3 2 0$ m.

At low altitudes $( h = 3 0 ~ \mathrm { m } )$ , the NLoS probability exceeds 0.5 in the urban scenario and remains around 0.25 in the suburban one. Accordingly, the ABS maintains a dominant association probability of approximately 0.74 in the urban case but only 0.38 in the suburban one. As the user ascends (30 m $< \ h \ \leq \ 1 1 0$ m), the NLoS probability decreases, thereby improving the G2A link quality. Consequently, the TBS association probability peaks at 0.92 (suburban) and 0.65 (urban) around $h = 1 1 0 \mathrm { ~ m ~ }$ , while the ABS probability correspondingly declines.

For $h > 1 1 0 \textrm { m }$ , the G2A channel becomes predominantly LoS $( \mathrm { L o S } > 0 . 8 6 $ in both environments). Owing to geometric proximity advantages, the ABS increasingly dominates the association, with its probability reaching 0.95 at $h = 3 0 0 \mathrm { ~ m ~ }$ while the TBS probability falls below 0.05.

These observations reveal a clear two-regime behavior: at lower altitudes, link blockage is the dominant factor affecting association, whereas at higher altitudes, geometric path loss becomes the key determinant. This insight can guide the optimal deployment of ABSs and the design of association biasing in diverse urban morphologies, as formalized in the following proposition.

Proposition 1 (Two-Regime Association Behavior) The association behavior of aerial users exhibits a two-regime structure:

$$
\begin{array} { r } { \mathcal { A } _ { \mathrm { A B S } } ( h ) \left\{ \begin{array} { l l } { \mathrm { i n c r e a s e s ~ w i t h ~ } h , } & { \mathrm { i f ~ } h > h _ { \mathrm { t h } } ; } \\ { \mathrm { d e c r e a s e s ~ w i t h ~ } h , } & { \mathrm { i f ~ } h < h _ { \mathrm { t h } } , } \end{array} \right. } \end{array}
$$

where $h _ { \mathrm { t h } }$ is a critical threshold altitude $( { \mathrm { e . g . , ~ } } h _ { \mathrm { t h } } \approx 1 1 0$ m) that separates two distinct regimes:

• Low-altitude regime $( h \ < \ h _ { \mathrm { t h } } ) ;$ LoS blockage dominates, favoring TBS association due to reduced signal obstruction.

• High-altitude regime $( h > h _ { \mathrm { t h } } ) ;$ : LoS conditions dominate, and geometric proximity to ABSs leads to stronger signal reception and increased ABS association.

This threshold-based insight supports the design of altitudeaware association policies and optimized ABS management strategies in heterogeneous urban environments.

Building on the two-regime behavior identified in Proposition 1, we now examine the specific altitudes where the ABS association probability reaches exactly 0.5. The next proposition formalizes these heights, providing further insights into the dynamics of association at critical altitudes.

Proposition 2 (0.5-Association Height) Let $\begin{array} { r l } { A _ { \mathrm { A B S } } } & { { } : } \end{array}$ $[ H _ { \operatorname* { m i n } } , H _ { \operatorname* { m a x } } ] \to [ 0 , 1 ]$ be continuous and strictly U-shaped with unique minimize $h _ { \mathrm { t h } } ~ \in ~ ( H _ { \operatorname* { m i n } } , H _ { \operatorname* { m a x } } )$ . Set $m : =$ $\mathcal { A } _ { \mathrm { A B S } } ( h _ { \mathrm { t h } } ) , a _ { - } \ : = \ \mathcal { A } _ { \mathrm { A B S } } ( H _ { \mathrm { m i n } } ) , a _ { + } \ : = \ \mathcal { A } _ { \mathrm { A B S } } ( H _ { \mathrm { m a x } } ) _ { l }$ , and $\mathcal { H } _ { 0 . 5 } : = \{ h : \mathcal { A } _ { \mathrm { A B S } } ( h ) = 0 . 5 \}$

$$
\begin{array} { r l } & { 1 ) ~ \operatorname { I f } ~ m > 0 . 5 , ~ \operatorname { t h e n } ~ \mathcal { H } _ { 0 . 5 } = \varnothing . } \\ & { 2 ) ~ \operatorname { I f } ~ m = 0 . 5 , ~ \operatorname { t h e n } ~ \mathcal { H } _ { 0 . 5 } = \{ h _ { \operatorname { t h } } \} . } \\ & { 3 ) ~ \operatorname { I f } ~ m < 0 . 5 , ~ \operatorname { t h e n } } \\ & { \qquad | \mathcal { H } _ { 0 . 5 } | = \mathbf { 1 } \{ a _ { - } \ge 0 . 5 \} + \mathbf { 1 } \{ a _ { + } \ge 0 . 5 \} . } \end{array}
$$

Moreover, each contributing endpoint determines one solution on its side:

$\begin{array} { r } { { \mathrm { i f ~ } a _ { - } > 0 . 5 \ ( \mathrm { r e s p . ~ = 0 . 5 ) , ~ t } } } \\ { { \left( H _ { \operatorname* { m i n } } , h _ { \mathrm { t h } } \right) \ ( \mathrm { r e s p . ~ a t ~ } H _ { \operatorname* { m i n } } ) ; } } \end{array}$ here is one solution in

$\begin{array} { r } { \mathrm { i f } \ a _ { + } > 0 . 5 \ ( \mathrm { r e s p . } \ = 0 . 5 ) , \ \mathrm { t h } } \\ { \left( h _ { \mathrm { t h } } , H _ { \mathrm { m a x } } \right) \ ( \mathrm { r e s p . } \ \mathrm { a t } \ H _ { \mathrm { m a x } } ) . } \end{array}$ ere is one solution in

Physically, when two solutions to $\mathcal { A } _ { \mathrm { A B S } } ( h ) ~ = ~ 0 . 5$ exist, the larger root $h _ { 0 . 5 } ^ { + } ~ \in ~ \left( h _ { \mathrm { t h } } , H _ { \mathrm { m a x } } \right]$ can be interpreted as the handover-neutral height. At this altitude, ABS and TBS association probabilities are balanced in the regime where $\mathcal { A } _ { \mathrm { A B S } } ( h )$ is increasing with $h ,$ meaning that ABS dominance will continue to strengthen. Therefore, $h _ { 0 . 5 } ^ { + }$ is of particular importance for handover management: it serves as a natural reference point for setting hysteresis margins to mitigate ping-pong handovers and for designing altitude-aware biasing strategies that adapt BS selection to user height.

In contrast, the smaller root $h _ { 0 . 5 } ^ { - } \in ( H _ { \operatorname* { m i n } } , h _ { \mathrm { t h } } )$ lies in the regime where $\mathcal { A } _ { \mathrm { A B S } } ( h )$ is still decreasing. At this altitude, users are prone to frequent switching between ABS and TBS, as the association preference lacks stability. Hence, $h _ { 0 . 5 } ^ { - }$ represents an unfavorable operating point, highlighting the necessity of avoiding coverage configurations that force users to hover around this altitude region.

## V. NETWORK COVERAGE PROBABILITY ANALYSIS

This section analyzes the coverage probability of CoMP transmission in VHetNets. Let C be the event that a typical user is in coverage. Recalling the total probability formula, the coverage probability can be computed as

$$
P = \sum _ { \chi \in Q } \mathbb { P } ( \mathcal { C } | \mathcal { E } _ { \chi } ) \mathbb { P } ( \mathcal { E } _ { \chi } ) ,
$$

where the operator $\mathbb { P } ( x )$ denotes the probability of event x and $\mathbb { P } ( x | y )$ denotes the conditional probability of event x given y.

Before proceeding to the coverage analysis, we first investigate the conditional distance distribution of a typical aerial UE, given its association with either three serving ABSs or three serving TBSs. The following lemmas then characterize the resulting distances to the three serving base stations in each case.

Lemma 5: When an aerial UE is associated with either three ABSs or three TBSs (i.e., event $\mathcal { E } _ { \mathrm { A B S } }$ or $\mathcal { E } _ { \mathrm { T B S } }$ occurs), the joint PDF of the distances between the UE and the three ABSs or three TBSs is given, respectively, by

$$
f _ { R | \mathcal { E } _ { \mathrm { A B S } } } ^ { \mathrm { A B S } } ( \pmb { r } ) = \frac { 1 } { \mathcal { A } _ { \mathrm { A B S } } } \bar { F } _ { R } ^ { \mathrm { T B S } } ( \pmb { r } ) f _ { R } ^ { \mathrm { A B S } } ( \pmb { r } ) ,\tag{17a}
$$

$$
f _ { R | \mathcal { E } _ { \mathrm { T B S } } } ^ { \mathrm { T B S } } ( r ) = \frac { 1 } { \mathcal { A } _ { \mathrm { T B S } } } \bar { F } _ { R } ^ { \mathrm { A B S } } ( r ) f _ { R } ^ { \mathrm { T B S } } ( r ) ,\tag{17b}
$$

where

$$
\bar { F } _ { { \pmb R } } ^ { \mathrm { A B S } } ( { \pmb r } ) = 1 - \int _ { H - h } ^ { r _ { 1 } } \int _ { x } ^ { r _ { 2 } } \int _ { y } ^ { r _ { 3 } } f _ { \pmb R } ^ { \mathrm { A B S } } ( x , y , z ) \mathrm { d } z \mathrm { d } y \mathrm { d } x ,\tag{17c}
$$

$$
\bar { F } _ { R } ^ { \mathrm { T B S } } ( r ) = 1 - \int _ { h } ^ { r _ { 1 } } \int _ { x } ^ { r _ { 2 } } \int _ { y } ^ { r _ { 3 } } f _ { R } ^ { \mathrm { T B S } } ( x , y , z ) \mathrm { d } z \mathrm { d } y \mathrm { d } x .\tag{17d}
$$

Proof: Let $\pmb { r } = ( r _ { 1 } , r _ { 2 } , r _ { 3 } )$ be an ordered distance vector with $H - h \ \leq \ r _ { 1 } \ < \ r _ { 2 } \ < \ r _ { 3 } \ \leq \ r _ { \operatorname* { m a x } }$ . Define $R ^ { \mathrm { A B S } } ~ =$ $( R _ { 1 } ^ { \mathrm { A B S } } , R _ { 2 } ^ { \mathrm { A B S } } , R _ { 3 } ^ { \mathrm { A B S } } )$ and $R ^ { \mathrm { T B S } } ~ = ~ ( R _ { 1 } ^ { \mathrm { T B S } } , R _ { 2 } ^ { \mathrm { T B S } } , R _ { 3 } ^ { \mathrm { T B S } } )$ . The conditional joint CDF of $R _ { 1 } ^ { \mathrm { A B S } } , R _ { 2 } ^ { \mathrm { A B S } }$ , and $R _ { 3 } ^ { \mathrm { \bar { A } B S } }$ is given by

$$
\begin{array} { r l } & { \displaystyle { F _ { R | \mathcal { E } _ { \mathrm { A B S } } } ^ { \mathrm { A B S } } ( \boldsymbol { r } ) = \frac { 1 } { \mathcal { A } _ { \mathrm { A B S } } } \mathbb { P } \left( \boldsymbol { R } ^ { \mathrm { A B S } } < \boldsymbol { r } ; \boldsymbol { R } ^ { \mathrm { T B S } } > \boldsymbol { r } \right) } } \\ & { \quad \quad \quad \quad \quad \quad = \frac { 1 } { \mathcal { A } _ { \mathrm { A B S } } } F _ { R } ^ { \mathrm { A B S } } ( \boldsymbol { r } ) \bar { F } _ { R } ^ { \mathrm { T B S } } ( \boldsymbol { r } ) } \\ & { \quad \quad \quad \quad = \frac { 1 } { \mathcal { A } _ { \mathrm { A B S } } } \underset { H - h < x < r } { \int } \bar { F } _ { R } ^ { \mathrm { T B S } } ( \boldsymbol { r } ) f _ { R } ^ { \mathrm { A B S } } ( \boldsymbol { x } ) \mathrm { d } x , } \end{array}
$$

where $\mathcal { E } _ { \mathrm { A B S } } ~ = ~ \{ R ^ { \mathrm { T B S } } ~ > ~ r \}$ . Here, $\bar { F } _ { R } ^ { \mathrm { T B S } }$ denotes the joint CCDF given in (17d). The result follows by applying the multivariate Leibniz rule for differentiation under the integral sign [33]. A similar derivation yields the conditional joint PDF $F _ { R | \mathcal { E _ { \mathrm { T B S } } } } ^ { \mathrm { T B S } }$ 

The Laplace transform of ${ \sqrt { I } } ,$ serving as a key intermediate result for the coverage probability, can be derived as

$$
\begin{array} { r l } & { \qquad \mathscr { L } _ { \sqrt { I } | \mathcal { E } _ { x } } ( s ) = \mathbb { E } \left[ \exp \left( - s \sqrt { I } \right) \right] } \\ & { \qquad = \displaystyle \int _ { 0 } ^ { \infty } \frac { s } { 2 \sqrt { \pi } u ^ { 3 / 2 } } e ^ { - s ^ { 2 } / ( 4 u ) } \mathscr { L } _ { I | \mathcal { E } _ { x } } ( u ) \mathrm { d } u , } \end{array}\tag{18}
$$

where [34, Eq. (3.471.9)] is applied to derive (18), and $\mathcal { L } _ { I | \mathcal { E } _ { \chi } } ( u )$ can be explicitly computed as (19), shown at the bottom of the page, in which the parameters are defined as:

$$
l _ { 1 } ( r _ { 3 } ) = \left\{ \begin{array} { l l } { \sqrt { r _ { 3 } ^ { 2 } - h ^ { 2 } } , } & { \mathrm { i f ~ } \chi = \mathrm { T B S } ; } \\ { 0 , } & { \mathrm { i f ~ } \chi = \mathrm { A B S } , } \end{array} \right.
$$

$$
\begin{array} { r l r } {  { l _ { 2 } ( r _ { 3 } ) = \{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } \chi = \mathrm { T B S } ; } \\ { \sqrt { r _ { 3 } ^ { 2 } - ( H - h ) ^ { 2 } } , } & { \mathrm { i f ~ } \chi = \mathrm { A B S } , } \end{array}  } } \\ & { } & { k = \{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } \chi = \mathrm { T B S } ; } \\ { 3 , } & { \mathrm { i f ~ } \chi = \mathrm { A B S } . } \end{array}  } \end{array}
$$

We now present the main result for the overall coverage probability:

Theorem 1 (Network Coverage Probability) The network coverage probability P of a randomly located aerial UE in a VHetNet is given by the weighted sum of the conditional coverage probabilities under ABS and TBS association:

$$
\begin{array} { r } { P = P _ { \mathrm { A B S } } \mathcal { A } _ { \mathrm { A B S } } + P _ { \mathrm { T B S } } \mathcal { A } _ { \mathrm { T B S } } , } \end{array}\tag{20}
$$

where the association probabilities $\mathcal { A } _ { \mathrm { A B S } }$ and $\mathcal { A } _ { \mathrm { T B S } }$ are given by (13) and (16), respectively. The conditional coverage probabilities under the ABS-association event $\mathcal { E } _ { \mathrm { A B S } }$ and the TBS-association event $\mathcal { E } _ { \mathrm { T B S } }$ are given by

$$
\begin{array} { r l } & { P _ { \mathrm { A B S } } = \underset { H - h \leq r _ { 1 } \leq r _ { 2 } \leq r _ { 3 } \leq s } { \int } \underset { s = 0 } { \overset { \nu _ { \mathrm { A B S } } - 1 } { \sum } } \frac { ( - \sqrt { \gamma / \lambda \delta \mathbf { B S } } ) ^ { k } } { k ! \theta _ { \mathrm { A B S } } ^ { k } } \frac { \partial ^ { k } \mathcal { L } _ { \sqrt { T } | \mathcal { E } _ { \mathrm { A B S } } } ( s ) } { \partial s ^ { k } } \bigg \vert _ { s = \frac { \sqrt { r _ { \mathrm { A B S } } } } { \theta _ { \mathrm { A B S } } } } } \\ & { \qquad \times \underset { H \leq r _ { 1 } \leq s } { \int } \kappa \underset { H \leq r _ { 1 } } { \sum } \mathrm { A B S } } \\ & { P _ { \mathrm { T B S } } = \underset { h \leq r _ { 1 } \leq r _ { 2 } \leq r _ { 3 } \leq \infty } { \int } \underset { s \in \{ 1 , \mathbf { N } \} ^ { 3 } } { \sum } \left[ \underset { i = 1 } { \overset { 3 } { \prod } } P _ { \zeta _ { i } } ( r _ { i } ) \right] } \\ & { \qquad \stackrel { \tilde { \nu } _ { \mathrm { T B S } , \zeta ^ { - 1 } } } { \sum } \frac { ( - \sqrt { \gamma } \sqrt { \gamma _ { \mathrm { B S } } } ) ^ { k } } { k ! \theta _ { \mathrm { T B S } , \zeta } ^ { k } } \frac { \partial ^ { k } \mathcal { L } _ { \sqrt { T } | \mathcal { E } _ { \mathrm { B S } } } ( s ) } { \partial s ^ { k } } \bigg \vert _ { s = \frac { \sqrt { r _ { \mathrm { B S } } } } { \theta _ { \mathrm { T B S } , \zeta } } } \kappa | \varepsilon _ { \mathrm { T B S } } ( r ) \mathrm { d } r , } \end{array}
$$

where $\tilde { \nu } _ { \mathrm { A B S } } = \mathrm { r o u n d } ( \nu _ { \mathrm { A B S } } )$ and $\tilde { \nu } _ { \mathrm { T B S , } \zeta } = \mathrm { r o u n d } ( \nu _ { \mathrm { T B S , } \zeta } )$ , and the Laplace transform $\mathcal { L } _ { \underline { { \sqrt { I } } } | \mathcal { E } _ { \chi } } ( s )$ is given by (18). Proof: See Appendix D. 

Remark 2 (Altitude-Dependent Coverage Performance) While the association preference varies with user altitude, as established in Proposition 1, the overall coverage probability also exhibits altitude-dependent regimes, although its dynamics are governed by distinct interference and fading characteristics.

Low-altitude regime $\begin{array} { r } { ( h < h _ { \mathrm { t h } } ) ; } \end{array}$ : Even under frequent LoS blockage, the reduced path loss resulting from the shorter TBS link distance remains a key enabler of coverage. Additionally, the supplementary coverage provided by the ABS in lower-altitude regions mitigates the residual blockage effects. As a result, the overall network exhibits robust and satisfactory coverage performance.

$$
\begin{array} { r l } & { \mathcal { L } _ { I | \mathcal { E } _ { x } } ( u ) = \exp \Bigg ( - 2 \pi \lambda _ { \mathrm { T B S } } \int _ { l _ { 1 } ( r _ { 3 } ) } ^ { \infty } \left[ 1 - \left( \frac { m _ { \mathrm { T B S } , \perp } } { m _ { \mathrm { T B S } , \perp } + u \left( z ^ { 2 } + h ^ { 2 } \right) ^ { - \alpha _ { \mathrm { T B S } , \perp } } } \right) ^ { m _ { \mathrm { T B S } , \perp } } \right] z P _ { \mathrm { L } } \mathrm { d } z } \\ & { \quad \quad - 2 \pi \lambda _ { \mathrm { T B S } } \int _ { l _ { 1 } ( r _ { 3 } ) } ^ { \infty } \left[ 1 - \left( \frac { m _ { \mathrm { T B S } , \mathrm { N } } } { m _ { \mathrm { T B S } , \mathrm { N } } + u \left( z ^ { 2 } + h ^ { 2 } \right) ^ { - \alpha _ { \mathrm { T B S } , \mathrm { N } } } } \right) ^ { m _ { \mathrm { T B S } , \mathrm { N } } } \right] z P _ { \mathrm { N } } \mathrm { d } z } \\ & { \quad \quad - \left[ \frac { 2 } { r _ { C } ^ { 2 } } \int _ { l _ { 2 } ( r _ { 3 } ) } ^ { r _ { C } } \left( \frac { m _ { \mathrm { A B S } } } { m _ { \mathrm { A B S } } + u \left( z ^ { 2 } + ( H - h ) ^ { 2 } \right) ^ { - \alpha _ { \mathrm { A B S } } } } \right) ^ { m _ { \mathrm { A B S } } } z \mathrm { d } z \right] ^ { N - k } \Bigg ) . } \end{array}\tag{19}
$$

• High-altitude regime $( h \ > \ h _ { \mathrm { t h } } ) ;$ At higher altitudes, the network coverage primarily benefits from ABS connectivity. As LoS conditions become dominant and the path length to the ABSs shortens, the resulting favorable link budgets outweigh the impact of elevated co-channel interference, thereby enhancing the overall coverage performance.

This nuanced behavior highlights the importance of jointly optimizing user association strategies and physical-layer link performance in the design of altitude-aware VHetNet deployments, a promising research topic for the future.

## VI. ABS DEPLOYMENT OPTIMIZATION

The preceding analysis assumed randomly distributed base stations—a strategy well-suited for scenarios requiring rapid, uncoordinated deployment, such as disaster recovery or emergency coverage. While analytically tractable within the stochastic geometry framework, random deployment primarily serves as a performance baseline, providing theoretical insights into the average coverage probability and the spatial behavior of VHetNets.

In contrast, this section focuses on intentional ABS deployment, tailored to address known coverage deficiencies in a given area. To this end, we propose a coverage-aware optimization framework that leverages a weighted K-means clustering algorithm in conjunction with CoMP transmission to guide ABS placement for maximal coverage efficiency.

Consider a set of user or sampling locations $\begin{array} { r l } { \mathcal { X } } & { { } = } \end{array}$ $\{ x _ { 1 } , \cdots , x _ { N } \} \subset \mathbb { R } ^ { 2 }$ within a target region, along with a corresponding set of weights $\mathcal { W } = \{ w _ { 1 } , \cdot \cdot \cdot , w _ { N } \}$ that quantify the severity of coverage shortfall at each location. The objective is to position K ABSs at $\{ \mu _ { k } \} _ { k = 1 } ^ { K }$ so as to maximize the weighted average success probability:

$$
\operatorname* { m a x } _ { \{ C _ { k } \} , \{ \mu _ { k } \} } \sum _ { k = 1 } ^ { K } \sum _ { x _ { i } \in C _ { k } } w _ { i } \left( 1 + \frac { 1 } { m } \| x _ { i } - \mu _ { k } \| ^ { \alpha } \right) ^ { - m } ,\tag{21}
$$

where α is the path loss exponent, m is the Nakagami fading parameter, and $C _ { k }$ is the cluster of points associated with the $k ^ { \mathrm { t h } } ~ \mathrm { A B S }$ , and $w _ { i } = \mathrm { m a x } ( 0 , \gamma _ { \mathrm { T B S } } - \gamma _ { i } )$ reflects the SIR gap at location $x _ { i }$ relative to a threshold γ<sub>TBS</sub>. Locations experiencing poor terrestrial coverage $( \mathrm { i . e . , } \gamma _ { i } < \gamma _ { \mathrm { T B S } } )$ receive higher weights, prioritizing them in the optimization.

The objective in (21) generalizes several canonical formulations:

• Rayleigh fading (m = 1):

$$
\operatorname* { m a x } _ { \{ C _ { k } \} , \{ \mu _ { k } \} } \sum _ { k = 1 } ^ { K } \sum _ { x _ { i } \in C _ { k } } \frac { w _ { i } } { 1 + \Vert x _ { i } - \mu _ { k } \Vert ^ { \alpha } } .\tag{22}
$$

• Deterministic path loss $( m  \infty ) \mathrm { { : } }$

$$
\operatorname* { m a x } _ { \{ C _ { k } \} , \{ \mu _ { k } \} } \sum _ { k = 1 } ^ { K } \sum _ { x _ { i } \in C _ { k } } w _ { i } e ^ { - \left\| x _ { i } - \mu _ { k } \right\| ^ { \alpha } } .\tag{23}
$$

• Free-space propagation $( \alpha = 2 , m \to \infty ) ;$

$$
\operatorname* { m a x } _ { \{ C _ { k } \} , \{ \mu _ { k } \} } \sum _ { k = 1 } ^ { K } \sum _ { x _ { i } \in C _ { k } } w _ { i } e ^ { - \| x _ { i } - \mu _ { k } \| ^ { 2 } } ,\tag{24}
$$

Algorithm 1 Path-Loss & Fading-Aware Clustering for UAV   
Deployment   
Require: $\overline { { { \mathcal { X } } } } \colon$ user/hole coordinates,   
1: W: weights,   
2: $K \colon$ number of ${ \mathrm { U A V s } } ,$   
3: α: path loss parameter,   
4: m: Nakagami-m fading parameter,   
5: : convergence threshold,   
6: $T _ { \mathrm { m a x } } { \mathrm { : } }$ max iterations   
Ensure: Optimized UAV positions $\{ \mu _ { k } ^ { * } \}$   
7: Initialize $\{ \mu _ { k } ^ { ( 0 ) } \}$   
8: for $t = 0$ to $T _ { \mathrm { m a x } }$ do   
9: for each $x _ { i } \in \mathcal X$ do   
10: Assign $x _ { i }$ to cluster   
$\begin{array} { r } { k = \arg \operatorname* { m a x } _ { j } ~ w _ { i } \left( 1 + \frac { 1 } { m } \| x _ { i } - \mu _ { j } ^ { ( t ) } \| ^ { \alpha } \right) ^ { - m } } \end{array}$   
11: end for   
12: for $k = 1$ to $K$ do   
13: Update cluster center:   
$\mu _ { k } ^ { ( t + 1 ) } = \frac { \sum _ { x _ { i } \in C _ { k } } w _ { i } \left( 1 + \frac { 1 } { m } \| x _ { i } - \mu _ { k } ^ { ( t ) } \| ^ { \alpha } \right) ^ { - m } x _ { i } } { \ell }$   
$\begin{array} { r } { \sum _ { x _ { i } \in C _ { k } } w _ { i } \left( 1 + \frac { 1 } { m } \| x _ { i } - \mu _ { k } ^ { ( t ) } \| ^ { \alpha } \right) ^ { - m } } \end{array}$   
14: end for   
15: if All $\bar { \| \mu _ { k } ^ { ( t + 1 ) } - \mu _ { k } ^ { ( t ) } \| } < \epsilon$ then   
16: break   
17: end if   
18: end for   
19: return $\{ \mu _ { k } ^ { * } \} = \{ \mu _ { k } ^ { ( t + 1 ) } \}$

which behaves similarly to the classical weighted Kmeans objective

$$
\operatorname* { m i n } _ { \{ C _ { k } \} , \{ \mu _ { k } \} } \sum _ { k = 1 } ^ { K } \sum _ { x _ { i } \in C _ { k } } w _ { i } \| x _ { i } - \mu _ { k } \| ^ { 2 } ,\tag{25}
$$

since exp $( - d ^ { 2 } )$ ≈ $1 - d ^ { 2 }$ for small $d ^ { 2 }$

Thus, the objective function given by (21) can be viewed as a fading- and path-loss-aware extension of the traditional K-means strategy, grounded in physical-layer considerations.

The deployment procedure is formalized in Algorithm 1. The algorithm alternates between: $i )$ assigning each $x _ { i }$ to the ABS that maximizes its fading-aware kernel in (21), and ii) updating $\mu _ { k }$ as the weighted centroid of cluster $C _ { k } ,$ where weights incorporate both $w _ { i }$ and the fading-aware kernel. This process monotonically increases the objective and converges in a finite number of iterations.

This optimization framework ensures UAV-based ABSs are deployed exactly where they maximize users’ success probability, yielding substantial performance improvements over geometric clustering. It retains the efficiency of K-means while aligning the optimization objective with wireless coverage performance, enabling real-time adaptation in dynamic environments such as post-disaster recovery, rural connectivity, and hotspot offloading [35], [36], [37].

TABLE III  
SIMULATION PARAMETER SETTING
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>rC</td><td rowspan=1 colspan=1>1000 m</td></tr><tr><td rowspan=1 colspan=1> $h _ { \mathrm { T B S } }$ </td><td rowspan=1 colspan=1>30 m</td></tr><tr><td rowspan=1 colspan=1> $h$ </td><td rowspan=1 colspan=1>120 m</td></tr><tr><td rowspan=1 colspan=1> $H$ </td><td rowspan=1 colspan=1>320 m</td></tr><tr><td rowspan=1 colspan=1> $N$ </td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1> $\lambda _ { \mathrm { T B S } }$ </td><td rowspan=1 colspan=1> $\overline { { 2 0 \ k m ^ { - 2 } } }$ </td></tr><tr><td rowspan=1 colspan=1>γ</td><td rowspan=1 colspan=1>0 dB</td></tr><tr><td rowspan=1 colspan=1> $( \alpha _ { \mathrm { A B S } } , \alpha _ { \mathrm { T B S } , \mathrm { L } } , \alpha _ { \mathrm { T B S } , \mathrm { N } } )$ </td><td rowspan=1 colspan=1>(2, 2, 2.7)</td></tr><tr><td rowspan=1 colspan=1> $( m _ { \mathrm { A B S } } , m _ { \mathrm { T B S , L } } , m _ { \mathrm { T B S , N } } )$ </td><td rowspan=1 colspan=1>(2, 2, 1)</td></tr><tr><td rowspan=1 colspan=1>Suburban $( a , b , c )$ </td><td rowspan=1 colspan=1> $( 1 , 6 . 5 8 1 , 1 )$ </td></tr><tr><td rowspan=1 colspan=1>Highrise urban $( a , b , c )$ </td><td rowspan=1 colspan=1> $( 1 . 1 2 4 , 0 . 0 4 9 , 1 . 0 2 4 )$ </td></tr></table>

![](images/c5d9d7f6b2302143d98802bd31c79b6a3af47f439d659a73b4d106293e6b4928.jpg)  
r (m)

![](images/02c014b09aa126315d8cd3a49f77e2ee71e6ce5c76d43d31708bae7acf29d479.jpg)  
r (m)  
Fig. 6. The accuracy of the PDFs $R _ { n } ^ { \mathrm { A B S } }$ and $R _ { n } ^ { \mathrm { T B S } }$ , as defined in (4) and (7), is validated by simulation results.

## VII. NUMERICAL RESULTS AND DISCUSSIONS

This section presents Monte Carlo simulation results to validate the analytical expressions and examine the impact of key system parameters on the CoMP performance in VHet-Nets. Specifically, we assess how network coverage responds to variations in ABS/TBS densities, aerial user altitude, and spatial distributions of users.

By 3GPP guidelines [38], the maximum operational altitude for aerial users is set to 300 m. For simplicity, a unified SIR threshold is assumed across all transmission scenarios, i.e., $\gamma _ { \mathrm { A B S } } ~ = ~ \gamma _ { \mathrm { T B S } } ~ = ~ \gamma$ . Additionally, the path loss exponent is taken to be the same for A2A and LoS G2A links, i.e., $\alpha _ { \mathrm { A B S } } =$ α<sub>TBS</sub> ${ \mathrm { ~  ~ { ~ L ~ } ~ } } = \alpha$ . The key simulation parameters are summarized in Table III for reference.

## A. Distance and Received Signal Distributions

Fig. 6 depicts the PDFs of the distances $R _ { n } ^ { \mathrm { A B S } }$ and $R _ { n } ^ { \mathrm { T B S } }$ between a typical user and the n-th closest ABS or TBS, respectively. The curves derived analytically align closely with the simulation results, thereby validating the correctness of the derived joint distance distributions.

Fig. 7 shows the distributions of the received signal power $V _ { \mathrm { A B S } }$ and the aggregate terrestrial signal $V _ { \mathrm { T B S , L L L } }$ under the fully-LoS configuration. Both empirical histograms and their respective Gamma distribution fittings are displayed. As illustrated, the Gamma approximation closely matches the empirical data, confirming its suitability for accurately modeling these random variables in analytical expressions.

![](images/23ff0315f332258630314ac36155d96f3a111e24ca0b467f03258bb91a8f53ce.jpg)

![](images/00870ccadc4fe88835dc188aa7b5fdd9e64cbd30646c36d6e0e682db673208c7.jpg)  
Fig. 7. The accuracy of the PDFs $V _ { \mathrm { A B S } }$ and $V _ { \mathrm { T B S , L L L } }$ , defined in (12b), is verified through comparison with simulation results.

![](images/c9fde66c0605b15e523d39f37052ddd16ff5894cee3e901a18df818c24eb1ed7.jpg)

![](images/c32734c736550d200568872002b385ef12eb2e26bd4dbeafa921a4182e386728.jpg)  
SIR Threshold (dB)  
User Height h (m)  
Fig. 8. Coverage probability versus SIR threshold γ and user altitude $h ,$ with ABSs fixed at $\mathsf { \bar { H } } = 3 2 0$ m.

## B. Coverage Probability

Fig. 8 illustrates the coverage probability as a function of the SIR threshold γ and the aerial user altitude h. In the left subplot, for all altitudes considered $( 6 0 \mathrm { ~ - ~ } 2 4 0 \mathrm { ~ m } )$ , the coverage probability decreases monotonically with increasing $\gamma ,$ which is consistent with standard SIR behavior. Notably, for $\gamma < 3 \mathrm { d B }$ , the curves across different altitudes nearly coincide, indicating minimal sensitivity to user height. However, when $\gamma \ > \ 3 \ \mathrm { d B }$ , the trajectory corresponding to $h ~ = ~ 6 0$ m achieves the highest coverage probability, while curves for higher altitudes remain similar but lower. This implies that, under mild SIR requirements, altitude has a negligible impact on coverage. In contrast, lower altitudes provide a distinct advantage under more stringent conditions.

![](images/e34b50ca738c8f18d4d7a50908a7d79ad6936f692584196ca8963b4fbde6ca25.jpg)

![](images/49273063e8cb62c3e1933bd6c75617b0bae0d56c3f355e03212dd810284e55e5.jpg)  
SIR Threshold (dB)  
ABS Height H (m)  
Fig. 9. Coverage probability versus SIR threshold $\gamma$ and ABS altitude $H ,$ with the user fixed at $h = 3 0 ~ \mathrm { r }$ m.

The right subplot of Fig. 8 examines coverage as a function of user altitude h for several fixed SIR thresholds. The resulting curves are generally convex, suggesting that users positioned at either low or high altitudes experience better coverage than those at intermediate heights. This behavior aligns with the association policy discussed in Section IV, where users tend to associate exclusively with either three ABSs or three TBSs, with mixed associations being rare. Interestingly, the altitudes corresponding to minimum and maximum coverage vary with γ. For instance, at $\gamma = - 3 ~ \mathrm { d B }$ peak coverage occurs at 300 m and the minimum around 120 m; whereas for $\gamma = 9$ dB, the optimal altitude drops to 30 m, with the minimum near 210 m. This observation highlights the dynamic nature of coverage performance as a function of altitude and SIR threshold.

Fig. 9 presents the impact of ABS altitude on coverage probability, assuming a fixed aerial user height of $h = 3 0$ m. As shown in the left subplot, increasing the ABS height leads to a gradual decline in coverage probability. This trend becomes more subdued at higher ABS altitudes, where the rate of change diminishes. In the right subplot, coverage probability is plotted against ABS altitude for several fixed values of γ. When γ is either very low or high, the curves remain relatively flat, indicating insensitivity to ABS height. However, for moderate thresholds, particularly around $\gamma = 3$ dB, the coverage declines sharply over a mid-range of altitudes. This suggests that the coverage performance is most sensitive to ABS deployment height under moderate SIR conditions.

Fig. 10 illustrates the variation in coverage probability with the number of ABSs for different user altitudes and path loss exponents, where $\alpha _ { \mathrm { A B S } } ~ = ~ \alpha _ { \mathrm { T B S , L } } ~ = ~ \alpha .$ . All curves exhibit a concave shape, with coverage probability increasing at low ABS numbers. This is because, at lower ABS counts, the increase in aerial interference power is relatively small, and the improvement in the desired aerial signal is more significant. Conversely, at higher ABS numbers, the coverage probability gradually decreases. This decline is due to the growing interference from additional ABSs, which outweighs the benefit of signal improvement, leading to a reduction in coverage probability.

![](images/7edb1bb14e1b23ba28b169670a7598146a0231707f7172f34b470f4c92b01b0f.jpg)  
Fig. 10. Coverage probability versus the number of ABSs under different user altitudes and path loss exponents.

These results suggest that, for a given path loss and user altitude, there exists an optimal number of UAVs for deployment. Beyond this optimal point, increasing the number of ABSs results in diminishing returns due to the increased interference, which reduces the overall coverage probability. Therefore, optimizing the number of ABSs is crucial for maximizing system performance, particularly in high-density or high-demand areas.

## C. Comparison With the Conventional Schemes

Fig. 11 presents the coverage probability as a function of the SIR threshold γ for two representative path loss exponents: α = 2 and $\alpha = 3$ . Three transmission schemes are compared:

1) The proposed CoMP-based association strategy;

2) A single-link baseline following the model in [14];

3) A conventional heuristic that connects the user to the three strongest received-power base stations.

Across the entire range of SIR thresholds, the proposed CoMP strategy consistently outperforms the single-link baseline and roughly matches the performance of the strongestthree heuristic. The improvement over single-link association is especially pronounced at moderate SIR thresholds. For instance, at $\gamma = - 4$ dB with $\alpha = 3 .$ , the coverage probability rises from approximately 0.1 (single-link) to 0.9 (CoMP). Similar gains are observed when $\alpha = 2 .$

While the strongest-three heuristic achieves comparable coverage performance, it requires an exhaustive search over all potential base stations and a dynamic ranking of received power levels. In contrast, the proposed CoMP framework achieves equivalent or superior coverage with lower complexity, leveraging spatially optimized base station coordination and interference mitigation. This demonstrates its practical advantage, especially under dense deployments and harsh propagation environments.

## D. System-Level Performance Comparison

Fig. 12 compares four deployment strategies: i) TBS-only, ii) TBSs with randomly placed ABSs, iii) TBSs with ABSs positioned via the classical weighted K-means algorithm, and iv) TBSs with ABSs positioned using the proposed Algorithm 1. The heatmaps in Fig. 12 visually illustrate the coverage probabilities, with lighter colors indicating higher coverage and darker colors indicating lower coverage.

![](images/77a52be9dc63f312afa666b9b44b66d3c63941ce0fdb53162edb4fca2df10bbf.jpg)

Fig. 11. Coverage comparison among the single-link scheme in [14], the proposed CoMP scheme, and the strongest-three-BS rule under different path loss exponents.  
![](images/4efd121e99bd2f3264cf57038fd516ca96fdf5070d12bf90a6fcac5699c7f513.jpg)  
(a) TBS Only.

![](images/8f88ab29a34bcaa65ae4234de12896eb7dc546052cce74297dfd0a55ac09a9d7.jpg)

![](images/18d0e929a1f6277087ea25753c0842eb7178b5dadad16fbd81fb6ebfd16b2af9.jpg)  
(c) TBSs with intentionally deployed ABSs by classical K-means algorithm.

(b) TBSs with randomly deployed ABSs.  
![](images/84773c81207ecbe1631f180f54deae0cb28b0aa859e28f8ef0b40f036aa02843.jpg)  
(d) TBSs with intentionally deployed ABSs by the proposed Algorithm 1.  
Fig. 12. Coverage heatmaps for four distinct deployment strategies.

Progressing from Fig. 12a to 12d, a clear trend of color lightening is observed, indicating improved coverage. The TBS-only configuration in Fig. 12a exhibits relatively darker colors, corresponding to a coverage probability of 61.99%. With randomly deployed ABSs (Fig. 12b), coverage improves to 72.93%, as reflected by lighter colors. The classical weighted K-means (Fig. 12c) and our proposed Algorithm 1 (Fig. 12d) yield the lightest and most spatially uniform heatmaps, achieving the highest coverage probabilities of 79.85% and 81.42%, respectively.

This improvement stems from geometry-aware optimization rather than random diversity. By weighting local SIR deficiencies, Algorithm 1 reshapes the Voronoi partitions to approximate an acute Delaunay triangulation, which tends to minimize circumcircle radii [39]. Indeed, Figs. 12c and 12d contain far fewer obtuse triangles than Fig. 12b, increasing the likelihood that user locations fall within strong cooperative coverage zones. Consequently, the optimized ABS deployment more effectively addresses coverage gaps, significantly enhancing the spatial efficiency and reliability of the network.

## VIII. CONCLUSION

This paper presented a comprehensive analysis and optimization framework for downlink coverage in CoMPenabled VHetNets. A novel 3D network model based on Poisson–Delaunay triangulation was introduced to facilitate cooperative transmission among ABSs and TBSs. Using tools from stochastic geometry, we derived closed-form expressions for association probabilities, distance distributions, and coverage probabilities. Monte Carlo simulation experiments, conducted by 3GPP guidelines, validated the theoretical models and identified key performance trends related to user altitude, ABS height, base station density, and channel conditions. In particular, the proposed CoMP strategy markedly improved coverage over conventional single-link and heuristic methods, especially under challenging propagation environments. Furthermore, a coverage-aware weighted K-means deployment algorithm was shown to significantly outperform random UAV placement by targeting coverage-deficient regions. These findings underscore the benefits of cooperative transmission and geometry-aware UAV deployment in enhancing the reliability of low-altitude wireless access. Future research will integrate reinforcement learning with stochastic geometry to enable adaptive and real-time UAV positioning, supporting resilient, scalable, and self-organizing VHetNet infrastructures.

## APPENDIX A PROOF OF LEMMA 1

The distance from a typical aerial user located at the origin to its $n ^ { \mathrm { t h } }$ closest ABS is denoted by $D _ { n } .$ . According to [21], the CDF and PDF of $D _ { n }$ are respectively given by

$$
F _ { D _ { n } } ( r ) = \frac { r ^ { 2 } } { r _ { C } ^ { 2 } } , \quad f _ { D _ { n } } ( r ) = \frac { 2 r } { r _ { C } ^ { 2 } } ,
$$

where $H - h \leq r \leq r _ { \operatorname* { m a x } }$

The user associates with the $n ^ { \mathrm { t h } }$ closest base station. The CDF of $R _ { n } ^ { \mathrm { A B S } }$ can be computed as

$$
\begin{array} { r l } & { F _ { R _ { n } } ^ { \mathrm { A B S } } ( r ) = \mathbb { P } ( R _ { n } ^ { \mathrm { A B S } } < r ) } \\ & { \qquad = \mathbb { P } ( \mathrm { a t ~ l e a s t ~ } n \mathrm { ~ o f ~ t h e ~ } R _ { n } ^ { \mathrm { A B S } } \mathrm { ~ a r e ~ l e s s ~ t h a n ~ } r ) } \\ & { \qquad = \displaystyle \sum _ { k = n } ^ { N } ( { \binom { N } { k } } ( F _ { D _ { n } } ( r ) ) ^ { k } ( 1 - F _ { D _ { n } } ( r ) ) ^ { N - k } . } \end{array}
$$

By differentiating the above expression with respect to r, the PDF of the serving distance is obtained as

$$
\begin{array} { l } { { \displaystyle f _ { R _ { n } } ^ { \mathrm { A B S } } ( r ) = f _ { D _ { n } } \sum _ { k = n } ^ { N } \binom { N } { k } } } \\ { { \displaystyle \quad \times \left[ k F _ { D _ { n } } ^ { k - 1 } ( 1 - F _ { D _ { n } } ) ^ { N - k } - ( N - k ) F _ { D _ { n } } ^ { k } ( 1 - F _ { D _ { n } } ) ^ { N - k - 1 } \right] . } } \end{array}\tag{26}
$$

![](images/eb1b66bb2c867885d8c98ce0508bf971a9fa59669119a04f05d9846f621e8890.jpg)  
Fig. 13. Two different representations of the PDF of the variable $R _ { n } ^ { \mathrm { A B S } }$

Clearly, (26) is overly complex and not convenient for analytical or numerical computation. According to the theory of order statistics, a more concise closed-form expression can be obtained as follows [40]

$$
f _ { R _ { n } } ^ { \mathrm { A B S } } ( r ) = \frac { N ! } { ( n - 1 ) ! ( N - n ) ! } f _ { D _ { n } } \left[ F _ { D _ { n } } \right] ^ { n - 1 } \left[ 1 - F _ { D _ { n } } \right] ^ { N - n } .\tag{27}
$$

Substituting $F _ { D _ { n } }$ and $f _ { D _ { n } }$ into (27) yields (4) in Lemma 1. To demonstrate the equivalence of (26) and (27), a simulation was conducted with parameters set to $N = 2 0 , r _ { C } = 5 0 0 \ \mathrm { m }$ $h \ = \ 1 0 0 \ \mathrm { ~ m ~ }$ , and $H \ : = \ : 3 0 0$ m. As shown in Fig. 13, the resulting curves from the two expressions perfectly coincide, thereby confirming their analytical equivalence.

According to the theory of order statistics [40], the joint PDF of $R _ { n _ { 1 } } ^ { \mathrm { { A B } \bar { S } } } , R _ { n _ { 2 } } ^ { \mathrm { { A B S } } } , \cdot \cdot \cdot , \bar { R } _ { n _ { k } } ^ { \mathrm { { A B S } } } ( 1 \leq n _ { 1 } < \cdot \cdot \cdot < n _ { k } \leq N ; 1 \leq$ $k \leq n )$ is for $r _ { 1 } \le \cdots \le r _ { k }$

$$
f _ { R _ { n _ { 1 } } , R _ { n _ { 2 } } , \cdots , R _ { n _ { k } } } ^ { \mathrm { A B S } } ( r _ { 1 } , r _ { 2 } , \cdots , r _ { k } ) =
$$

$$
\begin{array} { l } { { \displaystyle \frac { N ! } { ( n _ { 1 } - 1 ) ! ( n _ { 2 } - n _ { 1 } - 1 ) ! \cdots ( N - n _ { k } ) ! } \prod _ { i = 1 } ^ { k } f _ { D _ { n _ { i } } } ( r _ { i } ) } } \\ { { \mathrm { } \times F _ { D _ { n _ { 1 } } } ^ { n _ { 1 } - 1 } ( r _ { 1 } ) \left[ F _ { D _ { n _ { 2 } } } ( r _ { 2 } ) - F _ { D _ { n _ { 1 } } } ( r _ { 1 } ) \right] ^ { n _ { 2 } - n _ { 1 } - 1 } \times \cdots \times } } \\ { { \displaystyle \left[ F _ { D _ { n _ { k } } } ( r _ { k } ) - F _ { D _ { n _ { k - 1 } } } ( r _ { k - 1 } ) \right] ^ { n _ { k } - n _ { k - 1 } - 1 } } } \\ { { \displaystyle \left[ 1 - F _ { D _ { n _ { k } } } ( r _ { k } ) \right] ^ { N - n _ { k } } . } } \end{array}
$$

For a sample of N i.i.d. continuous random variables with PDF $f _ { D _ { i } } ( x )$ and CDF $F _ { D _ { i } } ( x )$ , the joint PDF of the first n order statistics $R _ { 1 } ^ { \mathrm { A B S } } \leq R _ { 2 } ^ { \mathrm { A B S } } \leq \cdot \cdot \cdot \leq R _ { n } ^ { \mathrm { A B S } }$ is for $H - h \leq$ $r _ { 1 } \leq r _ { 2 } \leq \cdot \cdot \cdot \leq r _ { n } \leq r _ { \operatorname* { m a x } } ,$

$$
\begin{array} { l } { { f _ { R _ { 1 } , R _ { 2 } , \cdots , R _ { n } } ^ { \mathrm { A B S } } ( r _ { 1 } , r _ { 2 } , \cdots , r _ { n } ) = } } \\ { { { } } } \\ { { { \displaystyle \frac { N ! } { ( N - n ) ! } f _ { D _ { 1 } } ( r _ { 1 } ) f _ { D _ { 3 } } ( r _ { 2 } ) \cdots f _ { D _ { n } } ( r _ { n } ) \left[ 1 - F _ { D _ { n } } ( r _ { n } ) \right] ^ { N - n } . } } } \end{array}
$$

Finally, substituting $f _ { D _ { 1 } } , f _ { D _ { 2 } } , \cdot \cdot \cdot , f _ { D _ { n } }$ and $F _ { D _ { \eta } }$ <sub>n</sub> into the above expression yields (5) in Lemma 1.

## APPENDIX B PROOF OF LEMMA 2

The probability that less than n nodes are closer than r is:

$$
P _ { n } = \mathbb { P } ( 0 , \cdot \cdot \cdot , n - \mathrm { 1 n o d e s ~ w i t h i n ~ } r )
$$

$$
= \sum _ { k = 0 } ^ { n - 1 } \frac { ( \lambda B _ { m } ( r ) ) ^ { k } } { k ! } e ^ { \lambda B _ { m } ( r ) } ,
$$

where $B _ { m } ( r )$ is the area of the circle of radius r.

The CDF of $R _ { n } ^ { \mathrm { T B S } }$ can be expressed as:

$$
\begin{array} { c } { { \displaystyle F _ { R _ { n } } ^ { \mathrm { T B S } } ( r ) = 1 - \sum _ { k = 0 } ^ { n - 1 } \frac { \left( \pi \lambda _ { \mathrm { T B S } } ( r ^ { 2 } - h ^ { 2 } ) \right) ^ { k } } { k ! } } } \\ { { \displaystyle ~ \times \exp \left( \pi \lambda _ { \mathrm { T B S } } ( r ^ { 2 } - h ^ { 2 } ) \right) . } } \end{array}\tag{28}
$$

Taking differential of $F _ { R _ { n } } ^ { \mathrm { T B S } } ( r )$ with respect to r yields (7).

The PDF of distance $R _ { 1 } ^ { \mathrm { T B S } }$ to the nearest TBS is

$$
f _ { R _ { 1 } } ^ { \mathrm { T B S } } ( r _ { 1 } ) = 2 \pi \lambda _ { \mathrm { T B S } } r _ { 1 } \exp \left( - \pi \lambda _ { \mathrm { T B S } } \left( r _ { 1 } ^ { 2 } - h ^ { 2 } \right) \right) .
$$

Given $R _ { 1 } ^ { \mathrm { T B S } } = r _ { 1 }$ , the PDF of distance $R _ { 2 } ^ { \mathrm { T B S } }$ to the second nearest base station is

$$
f _ { R _ { 2 } | R _ { 1 } } ^ { \mathrm { T B S } } ( r _ { 2 } \mid r _ { 1 } ) = 2 \pi \lambda _ { \mathrm { T B S } } r _ { 2 } \exp \left( - \pi \lambda _ { \mathrm { T B S } } \left( r _ { 2 } ^ { 2 } - r _ { 1 } ^ { 2 } \right) \right) { } .
$$

By analogy, given $R _ { n - 1 } ^ { \mathrm { T B S } } = r _ { n - 1 }$ , the PDF of distance $R _ { n } ^ { \mathrm { T B S } }$ to the $n ^ { \mathrm { t h } }$ nearest base station is

$$
\begin{array} { r } { f _ { R _ { n } | R _ { n - 1 } } ^ { \mathrm { T B S } } ( r _ { n } \mid r _ { n - 1 } ) = 2 \pi \lambda _ { \mathrm { T B S } } r _ { n } \exp \left( - \pi \lambda _ { \mathrm { T B S } } \left( r _ { n } ^ { 2 } - r _ { n - 1 } ^ { 2 } \right) \right) . } \end{array}
$$

The joint PDF can be factorized using conditional probability as:

$$
\begin{array} { r l } & { f _ { R _ { 1 } , R _ { 2 } , \cdots , R _ { n } } ^ { \mathrm { T B S } } ( r _ { 1 } , r _ { 2 } , \cdots , r _ { n } ) } \\ & { = f _ { R _ { 1 } } ^ { \mathrm { T B S } } ( r _ { 1 } ) \times f _ { R _ { 2 } | R _ { 1 } } ^ { \mathrm { T B S } } ( r _ { 2 } \mid r _ { 1 } ) \times \cdots \times f _ { R _ { n } | R _ { n - 1 } } ^ { \mathrm { T B S } } ( r _ { n } \mid r _ { n - 1 } ) } \\ & { = ( 2 \pi \lambda _ { \mathrm { T B S } } ) ^ { n } r _ { 1 } r _ { 2 } \cdots r _ { n } \exp \left( - \pi \lambda _ { \mathrm { T B S } } \left( r _ { n } ^ { 2 } - h ^ { 2 } \right) \right) . } \end{array}
$$

## APPENDIX C PROOF OF LEMMA 3

The distribution of $\begin{array} { r } { U _ { \chi , \zeta } = \sum _ { n \in \mathcal { C } _ { \chi } } \left| \mathrm { H } _ { n } ^ { ( \chi , \zeta _ { n } ) } \right| ( R _ { n } ) ^ { - \alpha _ { \chi , \zeta _ { n } } / 2 } } \end{array}$ admits a Gamma approximation (12a) through the generalized central limit theorem [41], with shape and rate parameters defined explicitly as

$$
\nu _ { \chi , \zeta } = \frac { \mathbb { E } ^ { 2 } [ U _ { \chi , \zeta } ] } { \operatorname { V a r } ( U _ { \chi , \zeta } ) } , \ : \ : \ : \theta _ { \chi , \zeta } = \frac { \operatorname { V a r } ( U _ { \chi , \zeta } ) } { \mathbb { E } [ U _ { \chi , \zeta } ] } ,
$$

where $\mathbb { E } [ \cdot ]$ and Var(·) denote the expectation and variance, respectively.

Since $\big | \dot { \mathrm { H } } _ { n } ^ { ( \chi , \zeta _ { n } ) } \big |$ and $R _ { n }$ are independence of each other, the expectation of $U _ { \chi , \zeta } ^ { ' }$ can be written as

$$
\mathbb { E } [ U _ { \chi , \xi } ] = \sum _ { n = 1 } ^ { 3 } \mathbb { E } \left[ \Big | \mathrm { H } _ { n } ^ { ( \chi , \zeta _ { n } ) } \Big | \right] \mathbb { E } \left[ ( R _ { n } ) ^ { - \alpha / 2 } \right] ,
$$

and the variance of $U _ { x , \zeta }$ is

$$
\begin{array} { r l r } {  { \operatorname { V a r } [ U _ { \chi , \xi } ] = \sum _ { n = 1 } ^ { 3 } \mathbb { E } [ | \mathrm { H } _ { n } ^ { ( \chi , \zeta _ { n } ) } | ^ { 2 } ] \mathbb { E } [ ( R _ { n } ) ^ { - \alpha } ] - \mathbb { E } ^ { 2 } [ U _ { \chi , \xi } ] } } \\ & { } & { + \sum _ { p \neq q } ^ { 3 } \mathbb { E } [ | \mathrm { H } _ { p } ^ { ( \chi , \zeta _ { p } ) } | ] \mathbb { E } [ | \mathrm { H } _ { q } ^ { ( \chi , \zeta _ { q } ) } | ] \mathbb { E } [ ( R _ { p } R _ { q } ) ^ { - \alpha / 2 } ] , } \end{array}
$$

where $\begin{array} { r l r } { \mathbb { E } \left[ \left| \mathrm { H } _ { n } ^ { ( \chi , \zeta _ { n } ) } \right| \right] } & { { } = } & { \frac { \Gamma \left( m _ { \chi , \zeta _ { n } } + \frac { 1 } { 2 } \right) } { \Gamma \left( m _ { \chi , \zeta _ { n } } \right) } \left( \frac { \Omega } { m _ { \chi , \zeta _ { n } } } \right) ^ { \frac { 1 } { 2 } } } \end{array}$ and $\mathbb { E } \left[ \left| \mathrm { H } _ { n } ^ { ( \chi , \zeta _ { n } ) } \right| ^ { 2 } \right] = \Omega .$

## APPENDIX D PROOF OF THEOREM 1

Suppose that a typical user is associated with three ABSs. The conditional coverage probability $P _ { \mathrm { A B S } }$ is given by

$$
\begin{array} { r l } { P _ { \mathrm { A B S } } = \displaystyle \int _ { { r > 0 } } \mathbb { P } ( \Gamma _ { \mathrm { A B S } } > \gamma _ { \mathrm { A B S } } | { r } ) } \\ { \quad \times \displaystyle f _ { R _ { 1 } , R _ { 2 } , R _ { 3 } | \mathcal { E } _ { \mathrm { A B S } } } ^ { \mathrm { A B S } } ( { r } _ { 1 } , { r } _ { 2 } , { r } _ { 3 } ) \mathrm { d } { r } . } \end{array}
$$

The coverage probability can be expressed as

$$
\begin{array} { r l } & { \mathbb { P } \left( \Gamma _ { \mathrm { A B S } } > \gamma _ { \mathrm { A B S } } \middle | r \right) = \mathbb { P } \left( \frac { S _ { \mathrm { A B S } } } { I } > \gamma _ { \mathrm { A B S } } \middle | r \right) } \\ & { \qquad = \mathbb { E } _ { I } \left[ \mathbb { P } ( S _ { \mathrm { A B S } } > \gamma _ { \mathrm { A B S } } I \middle | r , I ) \right] . } \end{array}
$$

The PDF, CDF, and CCDF of $S _ { \mathrm { A B S } } = U _ { \mathrm { A B S } } ^ { 2 }$ can be approximately expressed as

$$
\begin{array} { r l } & { f _ { S _ { \mathrm { A B S } } } ( x ) \approx \displaystyle \frac { x ^ { ( \nu _ { \mathrm { A B S } } - 2 ) / 2 } } { 2 \Gamma ( \nu _ { \mathrm { A B S } } ) \theta _ { \mathrm { A B S } } ^ { \nu _ { \mathrm { A B S } } } } \exp \left( - \frac { \sqrt { x } } { \theta _ { \mathrm { A B S } } } \right) , } \\ & { F _ { S _ { \mathrm { A B S } } } ( x ) \approx \displaystyle \frac { \gamma \left( \nu _ { \mathrm { A B S } } , \frac { \sqrt { x } } { \theta _ { \mathrm { A B S } } } \right) } { \Gamma ( \nu _ { \mathrm { A B S } } ) } , } \\ & { \bar { F } _ { S _ { \mathrm { A B S } } } ( x ) \approx \displaystyle \frac { \Gamma \left( \nu _ { \mathrm { A B S } } , \frac { \sqrt { x } } { \theta _ { \mathrm { A B S } } } \right) } { \Gamma ( \nu _ { \mathrm { A B S } } ) } , } \end{array}
$$

where $\begin{array} { r l r } { \gamma ( \nu _ { \mathrm { A B S } } , z ) } & { { } = } & { \int _ { 0 } ^ { z } t ^ { \nu _ { \mathrm { A B S } } - 1 } e ^ { - t } \mathrm { d } t } \end{array}$ and $\begin{array} { r l } { \Gamma ( \nu _ { \mathrm { A B S } } , z ) } & { { } = } \end{array}$ $\int _ { z } ^ { \infty } t ^ { \nu _ { \mathrm { A B S } } - 1 } e ^ { - t }$ dt are the lower and upper imcomplete Gamma functions, respectively. Next, we have

$$
\begin{array} { r l } & { \mathbb { P } ( \Gamma _ { \mathrm { A B S } } > \gamma _ { \mathrm { A B S } } ) | ^ { r } ) } \\ & { = \mathbb { E } _ { I } \left[ \frac { \Gamma \left( \nu _ { \mathrm { A B S } } , \frac { \sqrt { \gamma _ { \mathrm { A B S } } } \Gamma } { \theta } \right) } { \Gamma \left( \nu _ { \mathrm { A B S } } \right) } \right] } \\ & { = \mathbb { E } _ { I } \left[ \exp \left( - \frac { \sqrt { \gamma _ { \mathrm { A B S } } / I } } { \theta } \right) ^ { k } \sum _ { k = 0 } ^ { \nu _ { \mathrm { B S K } } - 1 } \frac { \left( \sqrt { \gamma _ { \mathrm { A B S } } / I } \right) ^ { k } } { k ! \theta ^ { k } } \right] } \\ & { = \displaystyle \sum _ { k = 0 } ^ { \nu _ { \mathrm { A B } } - 1 } \frac { \left( \sqrt { \gamma _ { \mathrm { A B S } } / I } \right) ^ { k } } { k ! \theta ^ { k } } \mathbb { E } _ { I } \left[ \exp \left( - \frac { \sqrt { \gamma _ { \mathrm { A B S } } / I } } { \theta } \right) ( \sqrt { I } ) ^ { k } \right] } \\ & { = \displaystyle \sum _ { k = 0 } ^ { \nu _ { \mathrm { A B } } - 1 } \frac { \left( - \sqrt { \gamma _ { \mathrm { A B S } } / I } \right) ^ { k } } { k ! \theta ^ { k } } \frac { \partial ^ { k } \mathcal { L } _ { \sqrt { \Gamma } / \mathrm { A } \mathrm { A } } \left( s \right) } { \partial s ^ { k } } \bigg \rvert _ { s = \infty ^ { \prime } \infty ^ { \prime } \infty ^ { \prime } \mathrm { A } ^ { \prime } } , } \end{array}
$$

where $\tilde { \nu } _ { \mathrm { A B S } } = \mathrm { r o u n d } ( \nu _ { \mathrm { A B S } } )$ and $\mathcal { L } _ { \sqrt { I } | \mathcal { E } _ { \mathrm { A B S } } } ( s )$ is given in (18). A similar derivation yields the conditional probability $P _ { \mathrm { T B S } }$

## REFERENCES

[1] J. Wu et al., “Low-altitude wireless networks: A comprehensive survey,” 2025, arXiv:2509.11607.

[2] R. Singh, M. Thompson, S. A. Mathews, O. Agbogidi, K. Bhadane, and K. Namuduri, “Aerial base stations for enabling cellular communications during emergency situation,” in Proc. Int. Conf. Vis., Image Signal Process. (ICVISP), Sep. 2017, pp. 103–108.

[3] A. Merwaday, A. Tuncer, A. Kumbhar, and I. Guvenc, “Improved throughput coverage in natural disasters: Unmanned aerial base stations for public-safety communications,” IEEE Veh. Technol. Mag., vol. 11, no. 4, pp. 53–60, Dec. 2016.

[4] I. Bor-Yaliniz and H. Yanikomeroglu, “The new frontier in RAN heterogeneity: Multi-tier drone-cells,” IEEE Commun. Mag., vol. 54, no. 11, pp. 48–55, Nov. 2016.

[5] D. Lee et al., “Coordinated multipoint transmission and reception in LTE-advanced: Deployment scenarios and operational challenges,” IEEE Commun. Mag., vol. 50, no. 2, pp. 148–155, Feb. 2012.

[6] G. Nigam, P. Minero, and M. Haenggi, “Coordinated multipoint joint transmission in heterogeneous networks,” IEEE Trans. Commun., vol. 62, no. 11, pp. 4134–4146, Nov. 2014.

[7] M. Sawahashi, Y. Kishiyama, A. Morimoto, D. Nishikawa, and M. Tanno, “Coordinated multipoint transmission/reception techniques for LTE-advanced [coordinated and distributed MIMO],” IEEE Wireless Commun., vol. 17, no. 3, pp. 26–34, Jun. 2010.

[8] R. Irmer et al., “Coordinated multipoint: Concepts, performance, and field trial results,” IEEE Commun. Mag., vol. 49, no. 2, pp. 102–111, Feb. 2011.

[9] M. Xia and S. A¨ıssa, “Unified analytical volume distribution of Poisson–Delaunay simplex and its application to coordinated multipoint transmission,” IEEE Trans. Wireless Commun., vol. 17, no. 7, pp. 4912–4921, Jul. 2018.

[10] Y. Li and M. Xia, “Ground-to-air communications beyond 5G: A coordinated multipoint transmission based on Poisson–Delaunay triangulation,” IEEE Trans. Wireless Commun., vol. 22, no. 3, pp. 1841–1854, Mar. 2023.

[11] X. Fan, P. Wu, and M. Xia, “Air-to-ground communications beyond 5G: UAV swarm formation control and tracking,” IEEE Trans. Wireless Commun., vol. 23, no. 7, pp. 8029–8043, Jul. 2024.

[12] Y. Li, D. Guo, L. Luo, and M. Xia, “Air-to-ground communications beyond 5G: CoMP handoff management in UAV network,” IEEE Trans. Wireless Commun., vol. 23, no. 12, pp. 18822–18837, Dec. 2024.

[13] M. Alzenad and H. Yanikomeroglu, “Coverage and rate analysis for vertical heterogeneous networks (VHetNets),” IEEE Trans. Wireless Commun., vol. 18, no. 12, pp. 5643–5657, Dec. 2019.

[14] N. Cherif, M. Alzenad, H. Yanikomeroglu, and A. Yongacoglu, “Downlink coverage and rate analysis of an aerial user in vertical heterogeneous networks (VHetNets),” IEEE Trans. Wireless Commun., vol. 20, no. 3, pp. 1501–1516, Mar. 2021.

[15] Y. Qin, M. A. Kishk, and M.-S. Alouini, “Coverage analysis and trajectory optimization for aerial users with dedicated cellular infrastructure,” IEEE Trans. Wireless Commun., vol. 23, no. 4, pp. 3042–3056, Apr. 2024.

[16] Y. Gu, R. Wang, D. Wu, Y. Cui, P. He, and B. Yang, “Multi-dimensional modeling and connectivity analysis for THz space-air-ground integrated network,” IEEE Trans. Wireless Commun., vol. 24, no. 6, pp. 4549–4563, Jun. 2025.

[17] Y. Liu et al., “Space-air-ground integrated networks: Spherical stochastic geometry-based uplink connectivity analysis,” IEEE J. Sel. Areas Commun., vol. 42, no. 5, pp. 1387–1402, May 2024.

[18] Y. Li, N. I. Miridakis, T. A. Tsiftsis, G. Yang, and M. Xia, “Air-to-air communications beyond 5G: A novel 3D CoMP transmission scheme,” IEEE Trans. Wireless Commun., vol. 19, no. 11, pp. 7324–7338, Nov. 2020.

[19] J. G. Andrews, F. Baccelli, and R. K. Ganti, “A tractable approach to coverage and rate in cellular networks,” IEEE Trans. Commun., vol. 59, no. 11, pp. 3122–3134, Nov. 2011.

[20] M. Haenggi, Stochastic Geometry for Wireless Networks. Cambridge, U.K.: Cambridge Univ. Press, 2012.

[21] S. Srinivasa and M. Haenggi, “Distance distributions in finite uniformly random networks: Theory and applications,” IEEE Trans. Veh. Technol., vol. 59, no. 2, pp. 940–949, Feb. 2010.

[22] V. V. Chetlur and H. S. Dhillon, “Downlink coverage analysis for a finite 3-D wireless network of unmanned aerial vehicles,” IEEE Trans. Commun., vol. 65, no. 10, pp. 4543–4558, Oct. 2017.

[23] A. A. Zaid, B. E. Y. Belmekki, and M.-S. Alouini, “Aerial-terrestrial heterogeneous networks for urban air mobility: A performance analysis,” IEEE Open J. Veh. Technol., vol. 6, pp. 912–926, 2025.

[24] M. M. Azari, F. Rosas, and S. Pollin, “Cellular connectivity for UAVs: Network modeling, performance analysis, and design guidelines,” IEEE Trans. Wireless Commun., vol. 18, no. 7, pp. 3366–3381, Jul. 2019.

[25] M. M. Azari, F. Rosas, A. Chiumento, and S. Pollin, “Coexistence of terrestrial and aerial users in cellular networks,” in Proc. IEEE GLOBECOM Workshops (GC Wkshps), Dec. 2017, pp. 1–6.

[26] M. Alzenad and H. Yanikomeroglu, “Coverage and rate analysis for unmanned aerial vehicle base stations with LoS/NLoS propagation,” in Proc. IEEE GLOBECOM Workshops (GC Wkshps), Dec. 2018, pp. 1–7.

[27] N. Goddemeier and C. Wietfeld, “Investigation of air-to-air channel characteristics and a UAV specific extension to the Rice model,” in Proc. IEEE GLOBECOM Workshops (GC Wkshps), Dec. 2015, pp. 1–5.

[28] D. S. Baum, J. Hansen, G. D. Galdo, M. Milojevic, J. Salo, and P. Kyosti, “An interim channel model for beyond-3G systems extending the 3GPP spatial channel model (SCM),” in Proc. IEEE 61st Veh. Technol. Conf., vol. 5, Jul. 2005, pp. 3132–3136.

[29] M. Nakagami, “The m-distribution—A general formula of intensity distribution of rapid fading,” in Proc. Stat. Methods Radio Wave Propag. New York, NY, USA: Pergamon, 1960, pp. 3–36.

[30] J. Zhao, L. Yang, M. Xia, and M. Motani, “Unified analysis of coordinated multipoint transmissions in mmWave cellular networks,” IEEE Internet Things J., vol. 9, no. 14, pp. 12166–12180, Jul. 2022.

[31] J. Zheng, Z. Wang, and A. Jamalipour, “An aerial and ground base station cooperation strategy for UAV and cellular integrated networks,” IEEE Internet Things J., vol. 11, no. 6, pp. 10411–10424, Mar. 2024.

[32] Ø. Hjelle and M. Dæhlen, Triangulations and Applications. Berlin, Germany: Springer, 2006.

[33] W. Rudin, Principles of Mathematical Analysis, 3rd ed., New York, NY, USA: McGraw-Hill, 1976.

[34] I. S. Gradshteyn and I. M. Ryzhik, Table of Integrals, Series, and Products, 7th ed., New York, NY, USA: Academic, 2007.

[35] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2334–2360, 3rd Quart., 2019.

[36] A. Fotouhi et al., “Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3417–3442, 4th Quart., 2019.

[37] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.

[38] Technical Specification Group Radio Access Network: Study on Enhanced LTE Support for Aerial Vehicles (Release 15), document TR 36.777, 3GPP, Jun. 2018.

[39] C. Qiu and H. Shen, “A Delaunay-based coordinate-free mechanism for full coverage in wireless sensor networks,” IEEE Trans. Parallel Distrib. Syst., vol. 25, no. 4, pp. 828–839, Apr. 2014.

[40] H. A. David and H. N. Nagaraja, Order Statistics. Hoboken, NJ, USA: Wiley, 2004.

[41] A. Papoulis, The Fourier Integral and Its Applications. New York, NY, USA: McGraw-Hill, 1962.

![](images/246e844da4389af5a7d1cfc9db71ff03e91033fc9880bab74cb7fba5b45e2a7a.jpg)

Wenkun Wen (Member, IEEE) received the Ph.D. degree in telecommunications and information systems from Sun Yat-sen University, Guangzhou, China, in 2007.

Since 2020, he has been with Techphant Technologies Company Ltd., Guangzhou, as a Chief Engineer. From 2008 to 2009, he was with Guangdong-Nortel R&D Center, Guangzhou, where he worked as a System Engineer for 4G systems. From 2009 to 2012, he was with the LTE R&D Center, New Postcom Equipment Company Ltd.,

Guangzhou, where he was the 4G Standard Team Manager. From 2012 to 2018, he was with the 7th Institute of China Electronic Technology Corporation (CETC) as an Expert in wireless communications, where he was the Deputy Director of the 5G Innovation Center from 2018 to 2020. His research interests include 5G/B5G mobile communications, machinetype communications, narrow-band wireless communications, and signal processing.

![](images/97c0c55038ca112e95cdcb39455d839ab09a439c2a9980cad167683272b28f61.jpg)

Peiran Wu (Member, IEEE) received the Ph.D. degree in electrical and computer engineering from The University of British Columbia (UBC), Vancouver, Canada, in 2015.

From October 2015 to December 2016, he was a Post-Doctoral Fellow with UBC. In Summer 2014, he was a Visiting Scholar with the Institute for Digital Communications, Friedrich-Alexander-University Erlangen–Nuremberg (FAU), Erlangen, Germany. Since February 2017, he has been with Sun Yat-sen University, Guangzhou, China, where he is currently

an Associate Professor. Since 2019, he has been an Adjunct Associate Professor with the Southern Marine Science and Engineering Guangdong Laboratory, Zhuhai, China. His research interests include mobile edge computing, wireless power transfer, and energy-efficient wireless communications.

![](images/1beedba6e084fb8c225a00bc358e0c311aba0975a406ddc17d5de44720acc208.jpg)

Minghua Xia (Senior Member, IEEE) received the Ph.D. degree in telecommunications and information systems from Sun Yat-sen University, Guangzhou, China, in 2007.

![](images/141b6677c205cdcba58f68f862dfd4dac6f0a7e81195e36fd0abd9435c8b5b9a.jpg)  
Tian Shi received the B.Sc. degree in information and computing science and the M.Sc. degree in mathematics from Guilin University of Electronic Technology, Guilin, China, in 2019 and 2023, respectively. He is currently pursuing the Ph.D. degree in information and communication engineering with Sun Yat-sen University, Guangzhou, China. His research interests include stochastic geometry and cooperative UAV communications.

From 2007 to 2009, he was with the Electronics and Telecommunications Research Institute (ETRI) of South Korea, Beijing R&D Center, Beijing, China, where he worked as a member and then as a Senior Member of the Engineering Staff. From 2010 to 2014, he was in sequence with The University of Hong Kong, Hong Kong, China; King Abdullah

University of Science and Technology, Jeddah, Saudi Arabia; and the Institut National de la Recherche Scientifique (INRS), University of Quebec, Montreal, Canada, as a Post-Doctoral Fellow. Since 2015, he has been a Professor with Sun Yat-sen University. Since 2019, he has also been an Adjunct Professor with the Southern Marine Science and Engineering Guangdong Laboratory (Zhuhai). His research interests are in the general areas of wireless communications and signal processing.