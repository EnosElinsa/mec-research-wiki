# Learned Off-Grid Imager for Low-Altitude Economy With Cooperative ISAC Network

Yixuan Huang , Graduate Student Member, IEEE, Jie Yang , Member, IEEE, Shuqiang Xia, Chao-Kai Wen , Fellow, IEEE, and Shi Jin , Fellow, IEEE

Abstract—The low-altitude economy is emerging as a key driver of future economic growth, necessitating effective flight activity surveillance using existing mobile cellular network sensing capabilities. However, traditional monostatic and localizationbased sensing methods face challenges in fusing sensing results and matching channel parameters. To address these challenges, we model low-altitude surveillance as a compressed sensing (CS)- based imaging problem by leveraging the cooperation of multiple base stations and the inherent sparsity of aerial images. Additionally, we derive the point spread function to analyze the influences of different antenna, subcarrier, and resolution settings on the imaging performance. Given the random spatial distribution of uncrewed aerial vehicles (UAVs), we propose a physics-embedded learning method to mitigate off-grid errors in traditional CSbased approaches. Furthermore, to enhance rare UAV detection in vast low-altitude airspace, we integrate an online hard example mining scheme into the loss function design, enabling the network to adaptively focus on samples with significant discrepancies from the ground truth during training. Simulation results demonstrate the effectiveness of the proposed low-altitude surveillance framework. The proposed physics-embedded learning algorithm

Digital Object Identifier 10.1109/TWC.2025.3603255

achieves a 97.55% detection rate, significantly outperforming traditional CS-based methods under off-grid conditions. Part of the source code for this paper can be accessed at https:// github.com/kiwi1944/LAEImager

Index Terms—Low-altitude surveillance, wireless imaging, compressed sensing, off-grid, physics-embedded learning.

## I. INTRODUCTION

itoring, and agricultural irrigation [2], [3], [4]. Currently, LAE primarily operates in uncontrolled airspace below 300 meters [5]. The surge in uncrewed aerial vehicle (UAV) deployments necessitates advanced surveillance techniques to ensure flight safety. According to 3GPP specifications [5], [6], UAV localization with meter-level accuracy is essential for intrusion detection and trajectory planning. However, UAVs low radar cross-section (RCS) and high mobility pose significant challenges for real-time sensing algorithm design [2]. This study aims to develop all-weather, around-the-clock sensing techniques for aerial surveillance.

Conventional UAV localization relies on the global navigation satellite system (GNSS), which is vulnerable to blockage and jamming, often resulting in positioning failures [7], [8]. Unauthorized UAVs may also disable GNSS receivers or reject localization signals, further complicating surveillance. Visiblelight cameras have been integrated with radio frequency (RF) sensing via attention-based spatio-temporal fusion techniques [2]. However, their performance degrades under low-visibility conditions, such as nighttime or haze, and they struggle with long-range target detection [9]. Moreover, these approaches require additional sensing hardware, increasing deployment costs for large-scale networks. Integrated sensing and communication (ISAC) provides a cost-effective alternative by leveraging existing cellular infrastructure without the need for extra sensors or hardware [10], [11], [12], [13].

Related Work—UAV sensing using cellular networks can be categorized into active and passive paradigms [2].

In the active paradigm, UAVs act as cooperative devices that establish communication links with base stations (BSs). By utilizing pilot transmissions and channel estimation, delay and angular parameters can be extracted and mapped to UAV locations using geometric relationships [8]. Deep supervised learning and reinforcement learning techniques have been applied to achieve 3D UAV localization based on received signal strength measurements from surrounding BSs [14].

Although conventional user localization algorithms can be adapted for UAV tracking [4], [15], they are ineffective for monitoring uncooperative UAVs.

The passive sensing paradigm addresses this limitation by eliminating the need for target cooperation. Analogous to monostatic radar systems, beamforming and scanning can generate “range-angle” maps of the airspace [16], [17], but require large antenna arrays to ensure high sensing accuracy. Graph neural networks have been adopted to design ISAC beamformers for enhanced sensing [18], while UAV location features can be extracted using convolutional neural networks (CNNs) [19]. However, beam scanning is time-consuming [20], and fusing multi-BS sensing data involves complex decision-level algorithms [17].

To improve sensing efficiency, bistatic and multi-static configurations enable BSs to jointly transmit and receive sensing signals [11], [18]. Most passive localization approaches estimate delay and angular parameters before mapping them to location coordinates [11], [15], [20]. This two-step process, however, is vulnerable to error propagation, where estimation inaccuracies degrade localization performance [21]. Furthermore, in multi-target scenarios, data association becomes challenging, requiring complex matching of multi-dimensional channel parameters to the corresponding UAVs [22], [23].

Proposed Approach—Given the relatively small UAV size compared to the vast low-altitude 3D space, we formulate UAV surveillance as a compressed sensing (CS)-based passive imaging problem by discretizing the aerial space into grids, fundamentally differing from previous studies. Specifically, “imaging” here refers to obtaining the scattering coefficient image of the aerial space, capturing the existence, location, scattering, and swarm shape information of low-altitude targets. Using CS-based imaging algorithms [24], [25], [26], raw channel state information (CSI) measurements are directly processed to generate images, enabling multi-static cooperation while mitigating error propagation and data association challenges. Despite these advantages, three major challenges remain: system configuration, on-grid approximation errors, and the high sparsity of low-altitude images.

First, traditional cellular networks are designed for ground communication and must be adapted for low-altitude sensing. The required hardware configuration to ensure high sensing performance remains unclear. In this study, we introduce the point spread function (PSF), a noise-free and targetindependent metric derived from the sensing matrix, to evaluate aerial imaging performance and analyze the impact of system parameters. PSF analysis guides ISAC system configuration and algorithm design, including antenna array layout, subcarrier and bandwidth selection, and imaging region and resolution.

Second, traditional CS models assume that targets lie exactly on predefined grid points [24], while UAV trajectories are inherently continuous, leading to off-grid modeling errors that distort the imaging results [27]. A common solution is to generate an initial estimate using on-grid models and refine it iteratively toward off-grid locations [28], [29]. However, this approach relies heavily on the accuracy of the initial estimate [20]. Alternatively, off-grid deviations can be modeled as unknown parameters embedded in the sensing matrix and estimated jointly with the sparse vector [30], [31], though this method involves complex Taylor expansion and derivative computation in Cartesian coordinates. Gridless methods such as atomic norm minimization (ANM) address off-grid errors through convex optimization in continuous domains [32], [33], but incur heavy computational costs and memory usage, especially in high-dimensional settings.

To address these limitations, deep learning (DL) has been applied in off-grid CS problems, particularly for channel estimation [34], [35], where deep neural networks (DNNs) learn the mapping between CSI and sparse representations. Although DNN-based techniques have been developed for low-altitude surveillance [2], [14], [18], [19], black-box DNNs suffer from limited interpretability and high sensitivity to training data. Thus, researchers have incorporated physical models into learning, categorized into three approaches [36], [37]: 1) Learning after physics processing uses on-grid models for initial outputs, which are refined by DNNs [38]; 2) Learning with physics loss embeds physical models into the loss function, but remains sensitive to off-grid mismatches; 3) Learning with physics models unfolds model-based CS algorithms into DNN layers, but suffers from high complexity due to intricate model expressions [39], [40].

Building on these insights, we propose a learned physicsembedded off-grid imager for UAV surveillance. This hybrid framework first applies on-grid models for coarse results and then refines them using DNNs to mitigate off-grid errors while maintaining computational efficiency.

Finally, extreme sparsity in low-altitude images poses a major challenge. Unlike target images like those in MNIST dataset, where structured features aid in object detection, lowaltitude images consist mostly of zero-valued voxels, with only a few non-zero points corresponding to UAVs. This severe imbalance between zero and non-zero voxels poses challenges for neural network training. Previous studies in channel estimation fields typically employ the mean square error (MSE) loss function for DNN training [34], [35], [38], [39], [40]. However, it may not be effective in low-altitude imaging scenarios. Cross-entropy loss, used in [41] and [42], detects target presence and generates binary (“0-1”) images but fails to preserve scattering coefficient information, which is essential for target characterization.

To overcome these limitations, we adopt online hard example mining (OHEM) [43], a computer vision technique prioritizing samples with large discrepancies from the ground truth, to develop tailored loss functions. This approach effectively optimizes the DNN to simultaneously enhance target detection and preserve scattering information, achieving high detection rates (DRs) and low false alarm rates (FARs).

In summary, this study makes the following contributions:

Cooperative Low-Altitude Imaging: We reformulate aerial surveillance as a CS-based imaging problem through space discretization. Our approach fully exploits the sensing capabilities of cooperative ISAC networks, mitigating error propagation and data association challenges. We also derive the PSF to analyze the impact of system parameters and qualitatively evaluate imaging capability.

![](images/f17cdd44d00e6e2afa12c40a25d547b059e8d13e32b6f9b2b17e28b6c70b2081.jpg)

![](images/af06f6961a96822f2a4fb0221cfea50537cd76c5acb936996ba43a05374f7af9.jpg)  
(b) Side view

![](images/b545eaa23b1991f74458f7339b478e4dd6c5487c481dd214af8e3d4967655001.jpg)  
(c) Bird view  
Fig. 1. Illustration of the cooperative ISAC network.

• Learned Physics-Embedded Off-Grid Imager: We address off-grid challenges by integrating physical and data-driven models. Our method first applies on-grid models, then refines the results using DNNs. We also propose novel OHEM-based loss functions tailored for low-altitude imaging. Simulation results demonstrate significant improvements over conventional methods.

The remainder of this paper is structured as follows: Sec. II introduces the ISAC system model. Sec. III formulates the imaging-based low-altitude surveillance problem. Sec. IV presents the proposed imaging algorithms, particularly for offgrid scenarios. Sec. V provides extensive simulation results. Sec. VI concludes this paper.

Notations—Scalars $( \mathrm { e } . \mathrm { g } . , a )$ are denoted in italics, vectors (e.g., a) in bold lowercase, and matrices $( \mathrm { e . g . , \ \mathbf { A } } )$ in bold uppercase. The modulus of $a$ is represented as |a|, and the imaginary unit is denoted by $j = \sqrt { - 1 }$ . The \`<sub>1</sub>- and \`<sub>2</sub>-norm of a are given by $\left\| \mathbf { a } \right\| _ { 1 }$ and $\| \mathbf { a } \| _ { 2 } ,$ , respectively. The notation diag(a) constructs a diagonal matrix with the elements of a. The transpose and Hermitian (conjugate transpose) operators are denoted by $( \cdot ) ^ { \mathrm { T } }$ and $( \cdot ) ^ { \mathrm { H } }$ , respectively. The inner product of two vectors a and b is represented by ha, bi.

## II. SYSTEM MODEL

We consider an ISAC system operating within a 3D space, represented as $[ x , y , z ] ^ { \mathrm { T } } \in \mathbb { R } ^ { 3 }$ , as illustrated in Fig. 1. The system comprises $N _ { \mathfrak { b } }$ BSs deployed at an altitude of $\hbar _ { \mathrm { b s } } ,$ forming a convex region with $N _ { \mathfrak { b } }$ edges in the horizontal plane. Each BS is equipped with a full-duplex uniform planar array (UPA) consisting of $N _ { 0 } \times N _ { 0 }$ antennas. The UPAs are vertically aligned to the ground, with their normal vectors directed toward the convex region’s center. The antenna spacing is given by $( \lambda _ { 0 } / 2 ) \cdot \xi ,$ , where $\lambda _ { 0 }$ denotes the wavelength corresponding to the center carrier frequency $f _ { 0 } .$ To enhance spatial resolution, we may consider sparse antenna arrays [44], [45], where $\xi \ge 1$ . Self-interference at the full-duplex BSs is mitigated through antenna separation and optimized beamforming [46]. The $N _ { \mathfrak { b } }$ BSs are synchronized via optical fiber to ensure precise timing. The region of interest (ROI), depicted in Fig. 1, represents a large surveillance area at altitude $\hbar _ { \mathrm { r o i } }$ . Its boundaries are predefined based on sensing requirements [12]. Specifically, the BSs are properly mounted and selected to ensure a line-of-sight (LOS) path between them and the ROI. For signal transmission, the system employs orthogonal frequency division multiplexing (OFDM) with $N _ { \mathrm { f } }$ subcarriers and a total bandwidth of B. The key variables in the system model are summarized in Table I.

## A. Transmit Signal Model

We consider a scenario where the BSs simultaneously sense low-altitude flight activities while communicating with $K$ single-antenna users in the downlink mode [12], [18]. To achieve this, the BSs form a wide beam to cover the ROI. At the $n _ { \mathrm { b } } .$ -th BS, the $n _ { \mathrm { f } ^ { - } } \mathrm { t h }$ subcarrier, and the $n _ { \mathrm { s } }$ -th symbol interval, the communication and sensing signals are designed to be spatially orthogonal, given by [12]:

$$
\bar { \mathbf { x } } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } } = \sum _ { k = 1 } ^ { K } \mathbf { w } _ { n _ { \mathrm { b } } , k } s _ { k , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ,\tag{1a}
$$

$$
\bar { \mathbf { x } } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } } = \sum _ { n _ { 0 } = K + 1 } ^ { N _ { 0 } ^ { 2 } } \mathbf { w } _ { n _ { \mathrm { b } } , n _ { 0 } } s _ { n _ { \mathrm { b } } , n _ { 0 } , n _ { \mathrm { f } } , n _ { s } } ,\tag{1b}
$$

where $s _ { k , n _ { \mathrm { f } } , n _ { \mathrm { s } } }$ is the information-bearing data for the k-th user, and $s _ { n \mathrm { b } , n _ { 0 } , n \mathrm { f } , n _ { s } }$ represents the dedicated sensing signal processed by the n<sub>0</sub>-th RF chain of the n<sub>b</sub>-th BS. The beamforming matrix is defined as $\mathbf { W } _ { n _ { \mathrm { b } } } = [ \mathbf { w } _ { n _ { \mathrm { b } } , 1 } , \dots , \mathbf { w } _ { n _ { \mathrm { b } } , N _ { 0 } ^ { 2 } } ] \in$ $\mathbb { C } ^ { N _ { 0 } ^ { 2 } \times N _ { 0 } ^ { 2 } }$ and can be designed based on the approaches proposed in [12] and [18]. Consequently, the transmitted ISAC signal at the $n _ { \mathrm { b } } .$ -th BS can be expressed as

$$
\begin{array} { r } { \mathbf { x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } = \sqrt { P _ { \mathrm { c } } } \mathbf { x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } } + \sqrt { P _ { \mathrm { s } } } \mathbf { x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } } , } \end{array}\tag{2}
$$

where ${ \bf x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } }$ and ${ \bf x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } }$ are the normalized versions of $\bar { \mathbf { x } } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } }$ and $\bar { \mathbf { x } } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } }$ , respectively. Here, $P _ { \mathrm { c } }$ and $P _ { \mathrm { ~ s ~ } }$ represent the power allocated to communication and sensing, respectively. The total transmit power at the n -th BS is $P _ { \mathrm { t } } = P _ { \mathrm { c } } { + } P _ { \mathrm { s } }$ For simplicity, we assume that $P _ { \mathrm { t } } , \ P _ { \mathrm { c } } ,$ , and $P _ { \mathrm { ~ s ~ } }$ are identical across all BSs, and that the signals ${ \bf x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } }$ transmitted by different BSs are orthogonal [11], [17]. Furthermore, specially designed protocols can assist in suppressing collaborative sensing interference [20].

## B. Communication Model

The wireless channel between the $n _ { \mathrm { b } }$ -th BS and the k-th user on the $n _ { \mathrm { f } } .$ -th subcarrier is denoted as $\mathbf { h } _ { n _ { \mathrm { b } } , k , n _ { \mathrm { f } } } ^ { \mathrm { H } }$ , which includes both direct BS-user multipaths and BS-ROI-user interference paths. Given the transmitted signal ${ \bf x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } }$ , the received signal at the k-th user is expressed in $( 3 )$ , shown at the bottom of the next page, [12], [18], where $\tilde { z } _ { k , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } }$ represents additive white Gaussian noise (AWGN) with variance $\zeta _ { \mathrm { c } } ^ { 2 }$ .The signalto-interference-plus-noise ratio (SINR) for the k-th user on the $n _ { \mathrm { f } } .$ -th subcarrier is given by

$$
\gamma _ { k , n _ { \mathrm { f } } } = \frac { | \mathbf { h } _ { k , n _ { \mathrm { f } } } ^ { \mathrm { H } } \mathbf { w } _ { k } | ^ { 2 } } { \sum _ { i = 1 \atop i \neq k } ^ { K } | \mathbf { h } _ { k , n _ { \mathrm { f } } } ^ { \mathrm { H } } \mathbf { w } _ { i } | ^ { 2 } + \sum _ { n _ { 0 } = K + 1 } ^ { N _ { 0 } ^ { 2 } } | \mathbf { h } _ { k , n _ { \mathrm { f } } } ^ { \mathrm { H } } \mathbf { w } _ { n _ { 0 } } | ^ { 2 } + \zeta _ { \mathrm { c } } ^ { 2 } } ,\tag{4}
$$

TABLE I  
NOTATIONS OF IMPORTANT VARIABLES
<table><tr><td>Notation</td><td>Definition</td><td>Notation</td><td>Definition</td></tr><tr><td> $N _ { \mathfrak { b } }$ </td><td>number of BSs</td><td> $N _ { 0 }$ </td><td>number of antennas in BS UPAs along one dimension</td></tr><tr><td> $f _ { 0 }$ </td><td>center carrier frequency</td><td> $\lambda _ { 0 }$ </td><td>center carrier wavelength</td></tr><tr><td> $K$ </td><td>number of communication users</td><td> $\xi$ </td><td>antenna spacing scale for sparse arrays</td></tr><tr><td> $B$ </td><td>signal bandwidth</td><td> $N _ { \mathrm { f } }$ </td><td>number of subcarriers</td></tr><tr><td> ${ \bf w } _ { n _ { \mathrm { b } } , n _ { \mathrm { 0 } } }$ </td><td>beamforming vector of the  $n _ { 0 } .$  th RF chain at the  $n _ { \mathrm { b } } { \cdot }$  -th BS</td><td> $\mathbf { W } _ { n _ { \mathrm { b } } }$ </td><td> $\mathbf { W } _ { n _ { \mathrm { b } } } = [ \mathbf { w } _ { n _ { \mathrm { b } } , 1 } , \dots , \mathbf { w } _ { n _ { \mathrm { b } } , N _ { 0 } ^ { 2 } } ] .$  , beamforming matrix</td></tr><tr><td> ${ \bf x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } }$ </td><td>normalized communication signal at the  $n _ { \mathrm { b } } – \mathrm { t h ~ B S }$  the  $n _ { \mathrm { f } ^ { - } } \mathrm { t h }$  subcarrier, and the  $n _ { \mathrm { s } } \mathrm { - } \mathrm { t h }$  symbol interval</td><td> $\mathbf { x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } }$ </td><td>normalized sensing signal at the  $n _ { \mathrm { b } ^ { + } }$  th BS, the nf-th sub- carrier, and the ns-th symbol interval</td></tr><tr><td> ${ \bf x } _ { n _ { \mathrm { b } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } }$ </td><td>ISAC signal at the  $n _ { \mathrm { b } } { \mathrm { - } } \mathrm { t h }$  BS, the  $n _ { \mathrm { f } } .$  th subcarrier, and the ns-th symbol interval</td><td> $P _ { \mathrm { { t } } }$ </td><td>total transmit power of one BS</td></tr><tr><td> $\mathbf { h } _ { n _ { \mathrm { b } } , k , n _ { \mathrm { f } } }$ </td><td>channel between the  $n _ { \mathrm { b } } { \cdot }$  -th BS and the k-th user on the th subcarrier</td><td> $\tilde { z } _ { k , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } }$ </td><td>AWGN at the k-th user, the  $n _ { \mathrm { f } ^ { \cdot } }$  th subcarrier, and the  $n _ { \mathrm { s } }$  symbol interval</td></tr><tr><td> $\zeta _ { \mathrm { c } } ^ { 2 }$ </td><td>variance of  $\tilde { z } _ { k , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { c } }$ </td><td> $\gamma _ { k , n _ { \mathrm { f } } }$ </td><td>SINR of the k-th user on the nf-th subcarrier</td></tr><tr><td> $\mathbf { h } _ { k , n _ { \mathrm { f } } }$ </td><td> $\mathbf { h } _ { k , n _ { \mathrm { f } } } = [ \mathbf { h } _ { 1 , k , n _ { \mathrm { f } } } ^ { \mathrm { T } } , \cdot \cdot \cdot , \mathbf { h } _ { N _ { \mathrm { b } } , k , n _ { \mathrm { f } } } ^ { \mathrm { T } } ] ^ { \mathrm { T } }$ </td><td> $\mathbf { w } _ { k }$ </td><td> $\mathbf w _ { k } = [ \mathbf w _ { 1 , k } ^ { \mathrm T } , \ldots , \mathbf w _ { N _ { \mathrm { b } } , k } ^ { \mathrm T } ] ^ { \mathrm T }$ </td></tr><tr><td></td><td>received sensing signal at the  $n _ { \mathrm { b } 2 } \mathrm { - t h }$  BS, transmitted by the  $n _ { s }$ </td><td> ${ \bf H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ </td><td>channel from the  $n _ { \mathrm { b 1 } } \mathrm { - t h } \mathrm { ~ B S } ,$  scattered by the ROI, and received at the nb2-th BS</td></tr><tr><td> ${ \bf F } _ { n _ { \mathrm { b 2 } } }$ </td><td>combiner at the  $n _ { \mathrm { b } 2 } { \mathrm { - } } \mathrm { t h }$  BS</td><td> $\tilde { \mathbf { z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } }$ </td><td>additive noise in  ${ \bf r } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } }$ </td></tr><tr><td> $h _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { \mathrm { s } }$ </td><td> $( n _ { \mathrm { t } } , n _ { \mathrm { r } } )$  -th element in  ${ \bf H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ </td><td> $G _ { \mathrm { s } }$ </td><td>combined antenna gain at the transmitter and receiver</td></tr><tr><td> $\breve { \sigma } ( x , y , z )$ </td><td>continuous ROI image</td><td> $\lambda _ { n _ { \mathrm { f } } }$ </td><td>wavelength of the nf-th subcarrier</td></tr><tr><td> $d _ { 1 } ( x , y , z )$ </td><td>distances from  $[ x , y , z ] ^ { \mathrm { T } }$  to the  $n _ { \mathrm { t } }$  -th transmitting antenna</td><td> $d _ { 2 } ( x , y , z )$ </td><td>distances from [x  $, y , z ] ^ { \mathrm { T } }$  to the  $n _ { \mathrm { r } } .$  -th receiving antenna</td></tr><tr><td> $N _ { \mathrm { s } }$ </td><td> $N _ { \mathrm { s } } = N _ { 0 } ^ { 2 } ,$  number of symbol intervals</td><td> ${ \bf R } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } }$ </td><td> $\mathbf { R } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } } = [ \mathbf { r } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , 1 } ^ { \mathrm { s } } , \dots , \mathbf { r } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , N _ { \mathrm { s } } } ^ { \mathrm { s } } ]$ </td></tr><tr><td> $\mathbf { X } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { f } } }$ </td><td> $\mathbf { X } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { f } } } = [ \mathbf { x } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { f } } , 1 } , \dots , \mathbf { x } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { f } } , N _ { \mathrm { s } } } ]$ </td><td> $\tilde { \mathbf { Z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } }$ </td><td> $\tilde { \mathbf { Z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } } = [ \tilde { \mathbf { z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , 1 } ^ { \mathrm { s } } , \dots , \tilde { \mathbf { z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , N _ { \mathrm { s } } } ^ { \mathrm { s } } ]$ </td></tr><tr><td> $\widehat { \mathbf { H } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ </td><td>estimate of  ${ \bf H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ </td><td> $y _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } }$ </td><td> $( n _ { \mathrm { t } } , n _ { \mathrm { r } } ) – \mathrm { t h }$  element of  $\widehat { \mathbf { H } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ </td></tr><tr><td> $N _ { \mathrm { v } }$ </td><td>number of voxels in the ROI</td><td> $\sigma$ </td><td> $\pmb { \sigma } = [ \sigma _ { 1 } , \ldots , \sigma _ { N _ { \mathrm { v } } } ] ^ { \mathrm { T } } ,$  discretized version of  $\breve { \sigma } ( x , y , z )$ </td></tr><tr><td> $\sigma _ { n _ { \mathrm { V } } }$ </td><td>scattering coefficient of the ny-th voxel</td><td> $M$ </td><td>number of UAVs in the ROI</td></tr><tr><td> $\mathbf { y }$ </td><td>CSI measurements of all BSs</td><td> $\mathbf { A }$ </td><td>sensing matrix related to all BSs</td></tr><tr><td> $\mathbf { z }$ </td><td>AWGN involved in y</td><td> $\zeta _ { \mathrm { s } } ^ { 2 }$ </td><td>variance of z</td></tr><tr><td> $\hat { \pmb { \sigma } }$ </td><td>estimate of σ</td><td> $\varepsilon$ </td><td>reconstruction accuracy threshold</td></tr></table>

where $\mathbf { h } _ { k , n _ { \mathrm { f } } } = [ \mathbf { h } _ { 1 , k , n _ { \mathrm { f } } } ^ { \mathrm { T } } , \dots , \mathbf { h } _ { N _ { \mathrm { b } } , k , n _ { \mathrm { f } } } ^ { \mathrm { T } } ] ^ { \mathrm { T } } \in \mathbb { C } ^ { N _ { \mathrm { b } } N _ { 0 } ^ { 2 } }$ , and $\mathbf { w } _ { k } ~ =$ $[ \mathbf { w } _ { 1 , k } ^ { \mathrm { T } } , \ldots , \mathbf { w } _ { N _ { \mathrm { b } } , k } ^ { \mathrm { T } } ] ^ { \mathrm { T } } \in \mathbb { C } ^ { N _ { \mathrm { b } } N _ { 0 } ^ { 2 } }$ . Finally, the spectral efficiency (SE) of the communication system is expressed as

$$
\mathrm { S E } = \sum _ { k = 1 } ^ { K } \sum _ { n _ { \mathrm { f } } = 1 } ^ { N _ { \mathrm { f } } } \log _ { 2 } ( 1 + \gamma _ { k , n _ { \mathrm { f } } } ) .\tag{5}
$$

## C. Sensing Model

When the $n _ { \mathrm { b l } } { \mathrm { - } } \mathrm { t h }$ BS transmits $\mathbf { x } _ { n _ { \mathrm { b l } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ,$ the signal is scattered by UAVs and received by the $n _ { \mathrm { b } 2 } \mathrm { - t h }$ BS. The received signal is given by

$$
\begin{array} { r } { \mathbf { r } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } } = \mathbf { F } _ { n _ { \mathrm { b } 2 } } \mathbf { H } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } } \mathbf { x } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } + \tilde { \mathbf { z } } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } } , } \end{array}\tag{6}
$$

where $\mathbf { H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ~ \in ~ \mathbb { C } ^ { N _ { 0 } ^ { 2 } \times N _ { 0 } ^ { 2 } }$ represents the channel from the $n _ { \mathrm { b 1 } }$ -th BS, scattered by the targets in the ROI, and received at the $n _ { \mathrm { b } 2 } – \mathrm { t h } \mathrm { ~ B S } .$ . The matrix $\mathbf { F } _ { n _ { \mathrm { b 2 } } }$ is the combiner at the n<sub>b2</sub>-th BS, designed to filter out direct signals and retain only scattered signals from the ROI. By employing advanced beamforming methods [12], the sensing beampattern can be accurately oriented to cover the ROI with significantly suppressed sidelobes, making the interference signal power originating from targets outside the ROI and from the LOS path between BSs negligible [4]. Additionally, the background interference scattered by static buildings can be measured in a calibration process and eliminated from the received signals during algorithm implementation [47]. Furthermore, given the sparsity of the low-altitude space, where rare scatterers may result in limited interference, we focus only on the signals passing through ${ \mathbf { H } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ in (6), while other potential multipath components are treated as part of the additive noise $\tilde { \mathbf { z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } , n _ { \mathrm { s } } } ^ { \mathrm { s } }$ [11], [18].

$$
r _ { k , n _ { k } , n _ { k } = 0 } ^ { \mathrm { c } } = \underbrace { \sum _ { n _ { b } = 1 } ^ { N _ { b } } { \bf h } _ { n _ { b } , k , n _ { t } } ^ { \mathrm { u l } } { \bf w } _ { n _ { b } , k } { s } _ { k , n _ { t } , n _ { s } } } _ { \mathrm { n _ { b e s i r d } ~ c o m m u n i c a l i o n ~ s p a r a t } } + \underbrace { \sum _ { n = 1 } ^ { N _ { b } } \sum _ { i = 1 } ^ { K } { \bf h } _ { n _ { b } , k , n _ { t } } ^ { \mathrm { u l } } { \bf w } _ { n _ { b } , i } { s } _ { i , n _ { t } , n _ { s } } } _ { \mathrm { M u l i : n e r ~ i n e r f e r e n c e } } + \underbrace { \sum _ { n _ { b } = 1 } ^ { N _ { b } } \sum _ { n _ { 0 } = K + 1 } ^ { N _ { a } ^ { 2 } } { \bf h } _ { n _ { b } , k , n _ { t } } ^ { \mathrm { u l } } { \bf w } _ { n _ { b } , n _ { 0 } } { s } _ { n _ { b } , n _ { 0 } } { s } _ { n _ { t } , n _ { 0 } } { , n _ { t } , n _ { s } } } _ { \mathrm { S e n s i r d } } + \underbrace { \overbrace { \sum _ { k , n _ { d } , n _ { d } } ^ { \mathrm { c } } { \bf h } _ { n _ { d } , n _ { s } } } ^ { \mathrm { a c } } { \bf h } _ { n _ { d } , n _ { d } } ^ { \mathrm { s i r d } } { \bf h } _ { n _ { d } , n _ { s } } } _ { \mathrm { S e n s i r d } } ,\tag{3}
$$

The $( n _ { \mathrm { t } } , n _ { \mathrm { r } } ) { \mathrm { - t h } }$ element in ${ \bf H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ,$ representing the channel between the $n _ { \mathrm { t } } { \mathrm { - } } \mathrm { t h }$ transmitting antenna of the $n _ { \mathrm { b l } ^ { - } }$ th BS and the $n _ { \mathrm { r } }$ -th receiving antenna of the $n _ { \mathrm { b } 2 } \mathrm { - t h }$ BS on the $n _ { \mathrm { f } ^ { - } } \mathrm { t h }$ subcarrier, is given by [48], [49]:

$$
\begin{array} { l l l } { h _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { s } = \displaystyle { \iint \int \frac { \lambda _ { 0 } \sqrt { G _ { s } } } { \sqrt { 4 \pi } } \times \frac { \breve { \sigma } ( x , y , z ) } { 4 \pi d _ { 1 } ( x , y , z ) d _ { 2 } ( x , y , z ) } } } \\ { \times e ^ { - j 2 \pi \frac { d _ { 1 } ( x , y , z ) + d _ { 2 } ( x , y , z ) } { \lambda _ { n _ { \mathrm { f } } } } } d x d y d z , } \end{array}\tag{7}
$$

where $G _ { \mathrm { s } }$ is the combined antenna gain at the transmitter and receiver. $\breve { \sigma } ( x , y , z )$ represents the continuous ROI image, where each value corresponds to the scattering coefficient at position $[ x , y , z ] ^ { \mathrm { T } } . ~ d _ { 1 } ( x , \bar { y } , z )$ and $d _ { 2 } ( x , y , z )$ are the distances from the scattering point to the $n _ { \mathrm { t } ^ { - } } \mathrm { t h }$ transmitting antenna and the $n _ { \mathrm { r } }$ -th receiving antenna, respectively. $\lambda _ { n \mathrm { f } }$ is the wavelength of the $n _ { \mathrm { f } } .$ -th subcarrier. $h _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { \mathrm { s } }$ includes the multipath channels scattered by all targets in the ROI.

Given the relatively slow velocity of UAVs, we assume that their positions and the channel ${ \bf H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ remain constant over $N _ { \mathrm { s } } = N _ { 0 } ^ { 2 }$ ISAC symbol intervals [11], [13].<sup>1</sup> By stacking the $N _ { \mathrm { s } }$ received signals, we can obtain

$$
\mathbf { R } _ { n _ { \mathrm { b l } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } } = \mathbf { F } _ { n _ { \mathrm { b 2 } } } \mathbf { H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } \mathbf { X } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { f } } } + \tilde { \mathbf { Z } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } } ,\tag{8}
$$

where $\begin{array} { c c l } { { \bf R } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } } ^ { \mathrm { s } } } & { = } & { [ { \bf r } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } , 1 } ^ { \mathrm { s } } , \ldots , { \bf r } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } , N _ { \mathrm { s } } } ^ { \mathrm { s } } ] , } \end{array}$ and ${ \bf X } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { f } } }$ and ${ \bf Z } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } }$ are similarly defined. Given the high degrees of design freedom in $\mathbf { F } _ { n _ { \mathrm { b 2 } } }$ and $\mathbf { X } _ { n _ { \mathrm { b l } } , n _ { \mathrm { f } } } ,$ , they can be full-rank matrices. Consequently, by transmitting ${ \bf R } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } } ^ { \mathrm { s } }$ to the central processing unit (CPU), ${ \bf H } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ can be estimated using the least squares (LS) method [11], given as

$$
\widehat { \mathbf { H } } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } } = \mathbf { F } _ { n _ { \mathrm { b } 2 } } ^ { - 1 } \mathbf { R } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { b } 2 } , n _ { \mathrm { f } } } ^ { \mathrm { s } } \mathbf { X } _ { n _ { \mathrm { b } 1 } , n _ { \mathrm { f } } } ^ { - 1 } .\tag{9}
$$

Assuming that each BS’s transmitted sensing signals are received by all BSs, both monostatic and multi-static sensing modes can be realized. Compared to solely monostatic [16] or bistatic [11] sensing modes, this approach enables more comprehensive CSI measurements. In the subsequent sections, the CSI measurement $\widehat { \mathbf { H } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ is utilized for low-altitude image reconstruction, realizing flight activity surveillance.

## III. CS-BASED PROBLEM FORMULATION AND ANALYSIS

In this section, we formulate the low-altitude surveillance problem using CS techniques, allowing for the simultaneous detection of multiple UAVs within a cooperative ISAC network. Furthermore, we evaluate the system’s sensing capabilities by deriving the PSF. Finally, we analyze the off-grid errors, which are critical for understanding the limitations and potential improvements in imaging performance.

## A. On-Grid Problem Formulation

In (7), the low-altitude image is represented as the continuous function $\breve { \sigma } ( x , y , z )$ . To enable aerial surveillance, we reconstruct the ROI image by discretizing it into $\begin{array} { r l } { N _ { \mathrm { v } } } & { { } = } \end{array}$ $N _ { \mathrm { x } } \times N _ { \mathrm { y } } \times N _ { \mathrm { z } }$ voxels, each with a size of $d _ { \mathrm { x } } \times d _ { \mathrm { y } } \times d _ { \mathrm { z } }$

![](images/9de5139ebd14ee466259c24c0b4188c703545cacb1fbec36d1b908fc37c9583b.jpg)  
Fig. 2. 2D illustration of low-altitude space discretization in the xOy plane.

Consequently, $\breve { \sigma } ( x , y , z )$ is sampled into an $N _ { \mathrm { v } }$ -dimensional vector $\pmb { \sigma } = [ \sigma _ { 1 } , \ldots , \sigma _ { N _ { \mathrm { v } } } ] ^ { \mathrm { T } }$ , representing the unknown image to be estimated. A 2D slice of the low-altitude image in the $x O y$ plane is shown in Fig. 2. We assume that M UAVs, modeled as point targets [50], are randomly located within the ROI, occupying M voxels, where $M \ll N _ { \mathrm { v } }$ . The scattering coefficient of the $n _ { \mathrm { v } } .$ -th voxel, denoted as $\sigma _ { n _ { \mathrm { v } } } .$ , characterizes the UAV’s scattering property if a UAV is present (pink voxels in Fig. 2). Otherwise, $\sigma _ { n _ { \mathrm { v } } } = 0$ (white voxels in Fig. 2).

Initially, we assume UAVs are exactly located at predefined voxel centers when $\sigma _ { n _ { \mathrm { v } } } > 0$ , treating them as “on-grid” scatterers [25]. This assumption facilitates modeling and performance analysis, providing insights for system configuration. However, as illustrated in Fig. 2, the true UAV location may deviate from voxel centers, introducing “off-grid” errors, which are analyzed in Sec. III-C and addressed in Sec. IV.

According to the cascaded channel model, the discrete form of (7) is given as [25], [48], [49]

$$
\begin{array} { l } { { \displaystyle h _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { \mathrm { s } } = \sum _ { n _ { \mathrm { v } } = 1 } ^ { N _ { \mathrm { v } } } \frac { \lambda _ { 0 } \sqrt { G _ { \mathrm { s } } } } { \sqrt { 4 \pi } } h _ { n _ { \mathrm { t } } , n _ { \mathrm { v } } , n _ { \mathrm { f } } } \sigma _ { n _ { \mathrm { v } } } h _ { n _ { \mathrm { r } } , n _ { \mathrm { v } } , n _ { \mathrm { f } } } } } \\ { { \displaystyle \ = \frac { \lambda _ { 0 } \sqrt { G _ { \mathrm { s } } } } { \sqrt { 4 \pi } } \mathbf { h } _ { n _ { \mathrm { t } } , n _ { \mathrm { f } } } ^ { \mathrm { H } } \mathrm { d i a g } ( \sigma ) \mathbf { h } _ { n _ { \mathrm { r } } , n _ { \mathrm { f } } } } , } \end{array}\tag{10}
$$

where $\mathbf { h } _ { n _ { \mathrm { t } } , n _ { \mathrm { f } } } = [ h _ { n _ { \mathrm { t } } , 1 , n _ { \mathrm { f } } } , \dots , h _ { n _ { \mathrm { t } } , N _ { \mathrm { v } } , n _ { \mathrm { f } } } ] ^ { \mathrm { T } }$ , with each element given by

$$
h _ { n _ { \mathrm { t } } , n _ { \mathrm { v } } , n _ { \mathrm { f } } } = \frac { e ^ { - j 2 \pi d _ { n _ { \mathrm { t } } , n _ { \mathrm { v } } } / \lambda _ { n _ { \mathrm { f } } } } } { \sqrt { 4 \pi } d _ { n _ { \mathrm { t } } , n _ { \mathrm { v } } } } ,\tag{11}
$$

where $d _ { n _ { 1 } , n _ { 1 } }$ represents the distance from the $n _ { \mathrm { t } } { \mathrm { - } } \mathrm { t h }$ transmitting antenna to the $n _ { \mathrm { v } } { \cdot } \mathrm { t h }$ voxel. Similar definitions apply for $\mathbf { h } _ { n _ { \mathrm { r } } , n _ { \mathrm { f } } }$ and $h _ { n _ { \mathrm { r } } , n _ { \mathrm { v } } , n _ { \mathrm { f } } } .$ . Consequently, the $( n _ { \mathrm { t } } , n _ { \mathrm { r } } )$ -th element of ${ \bf { H } } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } , n _ { \mathrm { f } } }$ is given by

$$
y _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } = h _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { s } + z _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } = \mathbf { a } _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { \mathrm { H } } \pmb { \sigma } + z _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ,\tag{12}
$$

where $\begin{array} { r } { \mathbf { a } _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { \mathrm { H } } = \frac { \lambda _ { 0 } \sqrt { G _ { \mathrm { s } } } } { \sqrt { 4 \pi } } \mathbf { h } _ { n _ { \mathrm { t } } , n _ { \mathrm { f } } } ^ { \mathrm { H } } \mathrm { d i a g } ( \mathbf { h } _ { n _ { \mathrm { r } } , n _ { \mathrm { f } } } ) } \end{array}$ , and $z _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } }$ represents additive noise from channel estimation. By aggregating the measurements from all transmitting antennas, receiving antennas, and subcarriers, the CSI measurements related to the $n _ { \mathrm { b l } }$ -th BS transmitter and the $n _ { \mathrm { b } 2 }$ -th BS receiver is expressed as

$$
\begin{array} { r } { { \bf y } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } } = { \bf A } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } } \pmb { \sigma } + \mathbf { z } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } } , } \end{array}\tag{13}
$$

where $\mathbf { A } _ { n _ { \mathrm { b 1 } } , n _ { \mathrm { b 2 } } } \in \mathbb { C } ^ { N _ { \mathrm { f } } N _ { 0 } ^ { 4 } \times N _ { \mathrm { v } } }$ , with its $( n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } )$ -th row given by $\mathbf { a } _ { n _ { \mathrm { t } } , n _ { \mathrm { r } } , n _ { \mathrm { f } } } ^ { \mathrm { H } } .$ The cellular network with $N _ { \mathfrak { b } }$ BSs can effectively generate $\dot { N } _ { \mathfrak { b } } ( N _ { \mathfrak { b } } + 1 ) / 2$ independent measurement sets, each adhering to the model in (13). By stacking all measurements, the system equation is given by

$$
{ \bf y } = { \bf A } \sigma + { \bf z } ,\tag{14}
$$

where $\mathbf { A } \in \mathbb { C } ^ { N _ { \mathrm { f } } N _ { 0 } ^ { 4 } N _ { \mathrm { b } } ( N _ { \mathrm { b } } + 1 ) / 2 \times N _ { \mathrm { v } } }$ is the overall sensing matrix, and z is modeled as zero-mean AWGN with variance $\zeta _ { \mathrm { s } } ^ { 2 }$

Our objective is to reconstruct the image $\sigma$ from the measurement y using the sensing matrix A. Given that UAVs occupy only a small fraction of the total voxels $( M \ll N _ { \mathrm { v } } )$ , σ exhibits high sparsity. We leverage CS theory to formulate the low-altitude sensing problem, given as [24], [25]:

$$
( \operatorname { P } 1 ) \quad { \hat { \pmb { \sigma } } } = \underset { \pmb { \sigma } } { \arg \operatorname* { m i n } } \| { \pmb { \sigma } } \| _ { 1 } , \quad \mathrm { s . t . ~ } \| \mathbf { y } - \mathbf { A } { \pmb { \sigma } } \| ^ { 2 } \leq \varepsilon ,\tag{15}
$$

where ε is a small threshold ensuring reconstruction accuracy. Note that problem (P1) differs from traditional CS problems in two key aspects. First, the sensing matrix A may have a high condition number due to channel correlations among compactly arranged antennas. Second, its row count, determined by $N _ { 0 } , N _ { \mathfrak { b } }$ , and $N _ { \mathrm { f } } ,$ may exceed its column count $N _ { \mathrm { v } } .$ , depending on system configurations. The abundance of measurements enhances low-altitude space sensing, mitigating uncertainties from A’s large condition number and improving sparse vector recovery.

Remark 1: The proposed problem formulation for lowaltitude surveillance offers several advantages:

• Non-Cooperative Target Sensing: UAV detection is achieved without any target cooperation.

• Direct CSI Utilization: CSI is directly used for image formation, eliminating the need for delay and angular parameter estimation as required in localization-based methods. This mitigates error propagation issues [21].

• Efficient Data Fusion: Measurements from multiple BSs are directly stacked and fused in their raw form, avoiding the need for time-consuming beam scanning and complex decision-level image fusion [17], [20].

• Scalability: Multiple targets can be detected simultaneously, with computational complexity independent of the number of targets.

• Comprehensive Target Characterization: Both target existence and scattering coefficients are estimated, providing valuable information for low-altitude surveillance.

In this study, precise UAV localization is not the primary objective, since meter-to-ten-meter level accuracy is adequate for intrusion detection and trajectory planning [5], [6]. Instead, we focus on detecting non-zero voxels and estimating their scattering coefficients. The localization accuracy depends on voxel grid resolution, which should be chosen based on sensing capabilities and application needs, as discussed next.

## B. Sensing Ability Analysis With PSF

The PSF is a target-independent metric used to evaluate the imaging capability of a given system and is widely employed in radar imaging systems with Fourier transform operations [49]. In [51], the PSF was adopted for CS-based imaging ability analysis by treating the columns of the sensing matrix as “steering vectors”. Accordingly, the PSF is defined as

$$
\mathrm { P S F } \left( n _ { 1 } , n _ { 2 } \right) = \frac { \left| \left. \mathbf { A } \left( : , n _ { 1 } \right) , \mathbf { A } \left( : , n _ { 2 } \right) \right. \right| } { \left\| \mathbf { A } \left( : , n _ { 1 } \right) \right\| _ { 2 } \left\| \mathbf { A } \left( : , n _ { 2 } \right) \right\| _ { 2 } } ,\tag{16}
$$

where $n _ { 1 } , n _ { 2 } = 1 , 2 , \ldots , N _ { \mathrm { v } }$ , and $\mathbf { A } \left( : , n _ { 1 } \right)$ represents the $n _ { 1 } \cdot$ th column of A. The PSF quantifies the mutual coherence between steering vectors, where lower coherence indicates improved imaging capabilities. Thus, analyzing the PSF can provide guidelines for system configurations to achieve high sensing performance.

![](images/7262cb6daaec6f94390e11a44b4fad2ba45130d006acc3cffe741234ddd1d67e.jpg)  
(a)

![](images/20c549d8a49e915ae729a8bdd96e0cefd0caf1cda79e0e42bd949ffdc7ec0243.jpg)  
(b)  
Fig. 3. Illustration of the 2D PSF (a) and its 1D slice (b), with (b) representing the blue line in (a).

Using the simulation parameters described in Sec. V-B.1, Fig. 3(a) presents the PSF with $N _ { \mathrm { v } } = 1 6 0 0$ , revealing strong correlations among the steering vectors of adjacent voxels. A one-dimensional PSF slice with $n _ { 1 } = 8 0 0$ is shown in Fig. (b). According to CS theory, orthogonal columns in the sensing matrix enable sparse vector recovery with minimal uncertainty. However, high channel correlations among adjacent antennas and subcarriers result in elevated PSF sidelobes, as depicted in Fig. 3, thereby making voxel discrimination challenging. To achieve high-resolution and high-accuracy imaging, small voxel sizes and large measurement sets are generally preferred. However, these configurations may lead to increased PSF sidelobes and expanded sensing matrix dimensions, which in turn reduce imaging accuracy and impose substantial computational burdens.

We next analyze the effects of different system parameters on the maximum PSF sidelobe, defined as $\mathcal { P } ( n _ { 1 } ) ~ =$ max $\mathsf { \Omega } _ { \mathrm { { \ell } } } ( \mathrm { P S F } ( n _ { 1 } , n _ { 2 } ) )$ , where $n _ { 1 } \neq n _ { 2 } .$ . A lower $\mathcal { P } ( n _ { 1 } )$ typically indicates improved imaging performance. Key observations from the simulation results in Fig. 4 are summarized as follows:

1) Antenna Configuration (Fig. 4(a)): Increasing $N _ { 0 }$ reduces $\mathcal { P } ( n _ { 1 } )$ by aggregating more CSI measurements for image reconstruction. However, the sensing matrix size increases exponentially, surpassing 1 GB storage at $N _ { 0 } = 8 .$ , which results in high computational complexity. Enlarging the antenna spacing to $( \lambda _ { 0 } / 2 ) \cdot \xi$ significantly lowers $\mathcal { P } ( n _ { 1 } )$ indicating that sparse arrays enhance spatial resolution and improve low-altitude imaging performance.

2) Voxel Size and ROI Coverage (Fig. 4(b)): When $d _ { 0 } =$ $d _ { \mathrm { x } } = d _ { \mathrm { y } } = d _ { \mathrm { z } } $ , larger voxel sizes reduce PSF sidelobes by increasing the spacing between voxels and decreasing channel correlation. However, this comes at the cost of reduced image resolution, although the sensing matrix becomes smaller. Therefore, a trade-off exists between imaging resolution and reconstruction accuracy.

3) Subcarrier and Bandwidth Configuration (Fig. 4(c)): Increasing the bandwidth and number of subcarriers improves PSF performance by enriching the available information from the ROI, thereby lowering $\mathcal { P } ( n _ { 1 } )$

![](images/14588f9095e5a6ec19be455180172f79b303f2e0c5493c17e883780de91e9d01.jpg)  
(a)

![](images/959acb6e22cff16179a9ea0141c7c668276c2fbb410827cbda8c41467b9599cc.jpg)  
(b)

![](images/19e174d677277dc81970e79c49522e87067a189bbc45e468fbd47be315f6e676.jpg)  
(c)

Fig. 4. Maximum PSF sidelobe $\mathcal { P } ( n _ { 1 } )$ under varying system parameters: (a) Antenna number $N _ { 0 }$ and antenna spacing scale ξ; (b) Voxel size $d _ { \mathrm { 0 } }$ and ROI size; (c) Subcarrier number $N _ { \mathrm { f } }$ and bandwidth B.  
![](images/1e5f65accba0739be2e663b2cf86861679fd5900209521807d312a68c910a938.jpg)  
Fig. 5. Relationship between off-grid error ∆b and location discrepancy $\Delta p .$

However, if the bandwidth remains fixed while $N _ { \mathrm { f } }$ increases, $\mathcal { P } ( n _ { 1 } )$ eventually saturates due to decreased subcarrier spacing and increased channel correlation. As a result, further increases in $N _ { \mathrm { f } }$ do not necessarily enhance imaging accuracy but substantially raise computational costs.

These findings provide practical guidelines for configuring ISAC networks, facilitating a balance among imaging resolution, reconstruction accuracy, and computational efficiency. Additional analysis involving other system parameters can be conducted using the PSF formulation given in (16).

## C. Off-Grid Error Analysis and Problem Reformulation

Sec. III-A formulated the on-grid imaging problem, where the sensing matrix A was constructed using predefined voxel center positions. However, only on-grid targets (blue points in Fig. 2) can be accurately detected, as their steering vectors are included in A. As illustrated in Fig. 2, UAVs rarely align perfectly with the predefined grid, introducing off-grid errors where the steering vectors in A fail to match the true UAV positions. Specifically, $\sigma _ { n _ { \mathrm { v } } } ~ > ~ 0$ only states that the $n _ { \mathrm { v } } .$ -th voxel include a UAV but it may not locate at the voxel center. Consequently, the equality in (14) no longer holds.

A direct approach to reduce off-grid errors is increasing grid density. Let p and $\mathbf { p } ^ { * }$ denote the true UAV location and the nearest grid center, respectively. Using the formulation in Sec. III-A and the simulation parameters in Sec. V-B.1, we compute the corresponding steering vectors b and $\mathbf { b } ^ { * }$ respectively. The off-grid error can then be quantified by

$$
\Delta b = \| \mathbf b - \mathbf b ^ { * } \| _ { 2 } / \| \mathbf b \| _ { 2 } .\tag{17}
$$

Fig. 5 depicts the relationship between ∆b and the location discrepancy $\Delta p = \| \mathbf { p } - \mathbf { p } ^ { * } \| _ { 2 }$ . The results show that reducing $\Delta b$ below −10 dB requires $\Delta p < 1 \ \mathrm { m m }$ . Achieving such dense grids results in 1) large sensing matrices and high computational costs, and 2) amplified PSF sidelobes (Fig. 4(b)), reducing imaging accuracy. Thus, increasing grid density alone is impractical for mitigating off-grid errors.

The above analysis highlights that off-grid errors introduce significant challenges for low-altitude imaging. Specifically, the constraint in problem (P1) becomes ineffective due to the invalidity of (14). Moreover, existing off-grid formulations based on Taylor expansion or ANM [30], [31], [32], [33] are unsuitable for low-altitude imaging due to their complex mathematical structures and high computational costs. To address the off-grid issues, we generalize the imaging problem as follows:

$$
( \mathrm { P 2 } ) \hat { \boldsymbol { \sigma } } = \underset { \boldsymbol { \theta } } { \arg \operatorname* { m i n } } \| \hat { \boldsymbol { \sigma } } - \boldsymbol { \sigma } \| _ { 2 } , \mathrm { s . t . } \hat { \boldsymbol { \sigma } } = f _ { \boldsymbol { \theta } } ( \mathbf { y } , \mathbf { A } ) ,\tag{18}
$$

where $\hat { \pmb { \sigma } }$ is the estimated sparse image, and $f _ { \pmb { \theta } } ( \mathbf { y } , \mathbf { A } )$ is an imaging function parameterized by θ. The off-grid issues have been released in the objective function of (P2), since it only cares which voxel includes a UAV rather than the UAV’s exact location. Despite these modifications, the on-grid imaging models introduced in Sec. III-A remain essential for PSFbased analysis shown in Sec. III-B and algorithm development discussed in the next section.

## IV. IMAGING ALGORITHMS

The previous section formulated on-grid and off-grid imaging problems for low-altitude surveillance. In this section, we first introduce a traditional CS-based on-grid imaging algorithm to solve (P1). Then, to address (P2), we propose a learned physics-embedded off-grid imager, incorporating novel loss functions based on the OHEM scheme.

## A. CS-Based On-Grid Imaging Algorithm

Various algorithms can be employed to solve (P1) [52]. Considering the tradeoff between estimation accuracy, computational complexity, and prior knowledge requirements, we adopt the subspace pursuit (SP) algorithm [24], which incorporates iterative refinement to improve reconstruction accuracy.

We define the residual signal computation as

$$
\mathbf { y } _ { \mathrm { r e s } } ( S ) = \mathbf { y } - \mathbf { A } _ { \mathcal { S } } f _ { \mathrm { L S } } ( \mathbf { y } , \mathbf { A } _ { \mathcal { S } } ) ,\tag{19}
$$

Algorithm 1 The SP Algorithm [24]   
1: input : A, y, and prior-based sparsity ${ \overline { { M ^ { \circ } } } } .$   
2: initialize : Calculate initial support $S _ { 0 } = f _ { \mathrm { s e l } , M ^ { \circ } } ( \mathbf { y } , \mathbf { A } )$   
derive the residual $\mathbf { y } _ { \mathrm { r e s } } ( S _ { 0 } )$ , and set $i = 0 .$   
3: while $\| \mathbf { y } _ { \mathrm { r e s } } ( S _ { i } ) \| _ { 2 } > \varepsilon$ or $S _ { i - 1 } \neq S _ { i } \ ( i \geq 1 )$ do   
4: $i = i + 1 .$   
5: Derive $\tilde { S } _ { i } = \cup ( S _ { i - 1 } , f _ { \mathrm { s e l } , M ^ { \circ } } ( \mathbf { y } _ { \mathrm { r e s } } ( S _ { i - 1 } ) , \mathbf { A } ) )$   
6: Renew the support as $S _ { i } = f _ { \mathrm { s e l } , M ^ { \circ } } ( \mathbf { y } , \mathbf { A } _ { \tilde { S } _ { i } } )$   
7: Update the residual as $\mathbf { y } _ { \mathrm { r e s } } ( S _ { i } )$   
8: end while   
9: output : the estimated ROI image $\hat { \pmb { \sigma } } .$

where $s$ represents the support set of the sparse signal, and $\mathbf { A } _ { \mathcal { S } }$ is the corresponding sub-matrix of A. The function $f _ { \mathrm { L S } } ( \mathbf { y } , \mathbf { A } _ { S } )$ computes the LS estimate of the non-zero values in $\pmb { \sigma } .$ Additionally, the function $f _ { \mathrm { s e l } , M } ( \mathbf { y } , \mathbf { A } )$ selects the indices corresponding to the largest M absolute values of $\mathbf { A } ^ { \mathrm { H } } \mathbf { y } .$ , effectively selecting the potential signal support.

The SP algorithm initializes by generating an initial support $ { \boldsymbol { S } } _ { 0 }$ using $f _ { \mathrm { s e l } , M } ( \mathbf { y } , \mathbf { A } )$ and computing the corresponding residual $\mathbf { y } _ { \mathrm { r e s } } ( S _ { 0 } )$ . In the i-th iteration, the following steps are performed:

1) Expand the support: Augment $\boldsymbol { S } _ { i - 1 }$ by adding the indices obtained from $f _ { \mathrm { s e l } , M } ( \mathbf { y } _ { \mathrm { r e s } } ( S _ { i - 1 } ) , \mathbf { A } )$ , forming ${ \tilde { S } } _ { i } .$

2) Update the support: Refine the support as $\begin{array} { r l } { S _ { i } } & { { } = } \end{array}$ $f _ { \mathrm { s e l } , M } \left( \mathbf { y } , \mathbf { A } _ { \tilde { S } _ { i } } \right)$

3) Update the residual: Compute the new residual $\mathbf { y } _ { \mathrm { r e s } } ( S _ { i } )$

The process repeats until the residual falls below a threshold ε or the support set stabilizes. Finally, the estimated nonzero values in σ are computed as $f _ { \mathrm { L S } } ( \mathbf { y } , \mathbf { A } _ { S _ { \mathrm { f i n a l } } } )$ , where $S _ { \mathrm { f i n a l } }$ denotes the final support set. Since the exact number of UAVs is unknown, the algorithm uses a prior-based sparsity value $M ^ { \circ }$ . The SP algorithm is summarized in Algorithm 1, with a computational complexity of $O ( N _ { \mathrm { i } } ( N _ { 1 } N _ { \mathrm { v } } + N _ { 1 } M ^ { \circ 2 } ) )$ , primarily due to the least squares (LS) estimation and matrix-vector multiplications. Here, $N _ { \mathrm { i } }$ denotes the number of iterations, and $N _ { 1 } = N _ { \mathrm { f } } N _ { 0 } ^ { 4 } N _ { \mathrm { b } } ( N _ { \mathrm { b } } + 1 ) / 2$ represents the total number of measurements. The value $M ^ { \circ }$ serves as the prior-based sparsity input to the SP algorithm.

## B. Physics-Embedded Learning Under Off-Grid Conditions

Traditional CS-based algorithms have demonstrated high performance in on-grid imaging tasks [25]. However, their effectiveness degrades under off-grid conditions due to modeling errors, as discussed in Sec. III-C. To address (P2), we leverage DNNs while recognizing the limitations of Taylor expansion and ANM-based approaches for low-altitude imaging [30], [31], [32], [33]. Since black-box DNNs often overlook physical constraints [34], [35], we adopt the physicsembedded learning framework [36], [37], [38], integrating model-based priors with data-driven learning to enhance imaging accuracy. As shown in Fig. 6, the proposed approach comprises two stages:

![](images/947298a99154082bd3023c3359e4aa30c39dbc9d5beed2dd2c54ba4b0bb2d1be.jpg)  
(a) Algorithm flows of different methods

![](images/5988d7ae4337234875aa1bc87cc2cc61c1ae1a81136629162c81a3565941e884.jpg)  
(b) DNN structure  
Fig. 6. Algorithm flow and DNN structure illustrations.

1) Step 1—Primary Model-Based Processing: Although the on-grid model does not perfectly represent the off-grid scenario, an initial estimate can be obtained $\mathsf { b y } ^ { 2 }$

$$
\sigma _ { \mathrm { { p r i } } } = \mathbf { A } ^ { \mathrm { H } } \mathbf { y } ,\tag{20}
$$

where the matrix A can be calculated based on known BS antenna locations and predefined ROI grid positions. This step is commonly used in CS-based algorithms [24], [25], [52] for identifying sparse signal components. Unlike the SP algorithm, which applies thresholding and may discard useful information, this step directly projects the measurement data into the image domain without enforcing sparsity constraints. While (20) provides an initial image, it lacks spatial accuracy due to off-grid errors in A.

2) Step 2—DNN Refinement: To refine the initial estimate $\sigma _ { \mathrm { { p r i } } }$ , we employ a DNN-based imaging model trained to reconstruct low-altitude images. As illustrated in Fig. 6, the DNN takes $\pmb { \sigma } _ { \mathrm { p n } }$ as input and is trained with the ground truth σ as labels. The network learns to extract underlying image information from $\pmb { \sigma } _ { \mathrm { p r i } }$ and outputs a refined estimate ${ \hat { \sigma } } ,$ accurately detecting UAV locations in 3D space. The DNN architecture integrates convolutional layers with residual connections, improving training convergence and mitigating issues like gradient vanishing and gradient explosion [38]. Implementation of the DNN requires an offline training procedure using collected or simulated datasets, followed by an online inference step using optimized DNN parameters. The computational complexity of the DNN inference is $\begin{array} { r } { O \left( \sum _ { n _ { \mathrm { c } } = 1 } ^ { N _ { \mathrm { c } } } N _ { \mathrm { v } } N _ { \mathrm { k } , n _ { \mathrm { c } } } C _ { \mathrm { i n } , n _ { \mathrm { c } } } C _ { \mathrm { o u t } , n _ { \mathrm { c } } } \right) } \end{array}$ [53], where $N _ { \mathrm { c } }$ is the number of CNN layers, $N _ { \mathbf { k } , n _ { \mathrm { c } } }$ is the number of variables in the convolutional kernel of the $n _ { \mathrm { c } } { \mathrm { - } } \mathrm { t h }$ layer, and $C _ { \mathrm { i n } , n _ { \mathrm { c } } }$ and $C _ { \mathrm { o u t } , n _ { \mathrm { c } } }$ are the input and output channel counts, respectively.

Although the computational complexity may be higher than that of Algorithm 1, the efficient computation capabilities of GPUs can enable near real-time inference after training.

Remark 2: Training data for real-world deployments can be collected using cooperative UAVs equipped with onboard localization devices. The CSI measurements can be acquired through signal transmission and reception by the ISAC network, while the ground-truth low-altitude image is generated based on the cooperative UAV locations. The dataset can be reused across different scenarios, provided that the ISAC network topology and the relative positions of the ROI and BSs remain unchanged. Additionally, synthetic datasets can be generated via computer simulations based on small realworld datasets, thereby reducing the need for extensive field data collection [54].

## C. Loss Function Design Based on OHEM

To refine $\sigma _ { \mathrm { { p r i } } }$ towards the ground truth $\sigma ,$ previous studies have employed the MSE loss function [34], [35], [38]. However, in low-altitude imaging, this approach faces significant challenges due to the extreme sparsity of $\sigma ,$ where nearly all voxel values are zero, with only a few non-zero points. Consequently, the DNN may converge to an all-zero output, achieving relatively low MSE values but failing to detect UAVs. Furthermore, low-altitude images consist of isolated points rather than structured features, making it difficult for CNNs to extract meaningful spatial information. This increases the challenge of detecting UAVs and requires careful DNN training using specially designed loss functions.

To improve DRs and training efficiency, we adopt the simple and intuitive OHEM scheme [43] to design effective loss functions. Originally developed to mitigate class imbalance in dataset, OHEM can help the DNN to focus on hard-todetect targets, which are underrepresented in training samples. Following the OHEM principle, voxels in each training image are categorized as:

• Positive Samples (Hard Samples): Non-zero voxels representing UAVs (pink in Fig. 2), which form a small fraction of the total voxels.

• Negative Samples (Easy Samples): Zero voxels representing empty space (white in Fig. 2), which dominate the voxel distribution.

For each predicted image, we define the loss contributions as follows:

• Positive Sample Loss: $\begin{array} { r } { L _ { \mathrm { p o s } } = \sum _ { \imath = 1 } ^ { M } l _ { \mathrm { p o s } , \imath } } \end{array}$ , where $l _ { \mathrm { p o s } , \ i }$ represents the MSE loss of the ı-th positive voxel.

• Negative Sample Loss: $\begin{array} { r } { L _ { \mathrm { n e g } } = \sum _ { j = 1 } ^ { \eta M } l _ { \mathrm { n e g } , j } , } \end{array}$ , where $l _ { \mathrm { n e g } , \mathcal { I } }$ is the MSE loss of the -th sorted negative voxel. Only the largest $\eta M$ MSE values of negative samples, determined by the hyper-parameter $\eta ,$ are selected.

We introduce two OHEM-based loss functions:

$$
L _ { \mathrm { o h e m 1 } } = \frac { L _ { \mathrm { p o s } } + L _ { \mathrm { n e g } } } { N _ { \mathrm { p o s } } + N _ { \mathrm { n e g } } } , \quad L _ { \mathrm { o h e m 2 } } = \frac { L _ { \mathrm { p o s } } } { N _ { \mathrm { p o s } } } + \frac { L _ { \mathrm { n e g } } } { N _ { \mathrm { n e g } } } ,\tag{21}
$$

where $N _ { \mathrm { p o s } } ~ = ~ M$ and $N _ { \mathrm { n e g } } ~ = ~ \eta M$ denote the numbers of positive and selected negative samples. As a result, the model parameter update $\Delta \theta$ in each training batch is mainly influenced by the limited positive samples and the selected negative samples with large MSE values. This satisfies $\Delta \pmb { \theta } \propto$ $- \nabla _ { \theta } L _ { \mathrm { o h e m } \star }$ where $\star \in \{ 1 , 2 \}$ and $\nabla _ { \theta }$ denotes the gradient with respect to θ. Well-predicted negative samples are excluded from consideration. This prevents $\Delta \theta$ from being dominated by a potentially large number of easy negatives and acts similarly to a thresholding operation. By adjusting $\eta ,$ the value of $N _ { \mathrm { n e g } }$ changes, which modifies the threshold that determines which negative samples are selected or excluded in $L _ { \mathrm { o h e m \star } }$ during training. Therefore, η affects the optimization of θ by balancing the influences of positive and negative samples. This results in different numbers of non-zero voxels in the predicted output.

However, the two loss functions in (21) behave differently as $\eta$ varies, requiring careful tuning. For $L _ { \mathrm { o h e m 1 } }$ , MSE contributions from positive and selected negative samples $( l _ { \mathrm { p o s } , \imath }$ and $l _ { \mathrm { n e g } , j } )$ receive equal weight in backpropagation. Increasing $N _ { \mathrm { n e g } }$ amplifies the effect of $L _ { \mathrm { n e g } } ,$ , causing the network to favor zero voxel predictions. If all negative samples are selected, $L _ { \mathrm { o h e m 1 } }$ converges to traditional MSE loss. In contrast, $L _ { \mathrm { o h e m 2 } }$ separately normalizes $L _ { \mathrm { p o s } }$ and $L _ { \mathrm { n e g } } ,$ giving both normalized terms equal weight. However, as $N _ { \mathrm { n e g } }$ increases, the contribution of each negative sample diminishes, reducing the DNN’s bias toward zero predictions. This property makes $L _ { \mathrm { o h e m 2 } }$ more effective for achieving higher DRs.

Given the sparse nature of low-altitude images, we can add a sparse regularization term to derive the final loss function:

$$
L = L _ { \mathrm { o h e m } \star } + \alpha \| \hat { \pmb { \sigma } } \| _ { 1 } ,\tag{22}
$$

where $\alpha$ is a hyper-parameter controlling the weight of the regularization term.

## V. NUMERICAL RESULTS

## A. Simulation Settings and Metrics

We consider a cellular network comprising $N _ { \mathrm { b } } = 4$ BSs that simultaneously serve communication users and monitor aerial flight activities. The center carrier frequency is set to $f _ { 0 } =$ 2.6 GHz. Each BS, positioned at the corners of a square, has a height of $\hbar _ { \mathrm { b s } } = 2 0 ~ $ m. The integrated antenna gain is $G _ { \mathrm { s } } = 4$ [55]. The additive noise power per receiving antenna is $P _ { \mathrm { { n } } } =$ −110 dBm [12], with total noise power scaling according to the number of antennas. The UAV RCS is randomly generated according to a Gaussian distribution with the mean 0.01 m<sup>2</sup> [11] and the variance 0.001. The UAV scattering coefficient is derived as the square root of its RCS [15].

We evaluate both 2D and 3D ROIs. Unless otherwise stated, the 2D ROI is positioned at $\hbar _ { \mathrm { r o i } } = 4 0$ m with dimensions of 120 m × 120 ${ \mathrm { m } } ,$ discretized into $\textbf { a } 4 0 \times 4 0$ image with a voxel size of $d _ { 0 } ~ = ~ 3 ~ \mathrm { ~ m ~ }$ . The 3D ROI has dimensions 100 $\mathbf { m } \times 1 0 0 \ \mathbf { m } \times 8 0$ m and is discretized into a $2 0 \times 2 0 \times 1 6$ image with a voxel size of $d _ { 0 } = 5$ m. The imaging resolution $d _ { 0 }$ is deemed sufficient for intrusion detection and trajectory planning applications [5], [6].

To assess sensing performance, we employ the following five metrics:

![](images/a752da42ad99f217660f193b618aa0c8c1b38de6a90fff1416d93a57ae490482.jpg)  
Fig. 7. Sensing performance under on-grid conditions with varying antenna numbers, BS distances, and transmit powers.

(1) MSE: Measures the per-voxel difference between the predicted σˆ and ground truth σ images:

$$
\begin{array} { r } { \mathbf { M S E } = \| \hat { \pmb { \sigma } } - \pmb { \sigma } \| _ { 2 } ^ { 2 } / N _ { \mathrm { v } } . } \end{array}\tag{23}
$$

(2) Structural similarity index measure (SSIM): Assesses the structural similarity between $\hat { \pmb { \sigma } }$ and σ [42]:

$$
\mathrm { S S I M } = \frac { \left( 2 \mu _ { \sigma } \mu _ { \hat { \sigma } } + c _ { 1 } \right) \left( 2 \theta _ { \sigma \hat { \sigma } } + c _ { 2 } \right) } { \left( \mu _ { \sigma } ^ { 2 } + \mu _ { \hat { \sigma } } ^ { 2 } + c _ { 1 } \right) \left( \theta _ { \sigma } ^ { 2 } + \theta _ { \hat { \sigma } } ^ { 2 } + c _ { 2 } \right) } ,\tag{24}
$$

where $\mu _ { \sigma } \left( \mu _ { \hat { \sigma } } \right)$ and $\theta _ { \sigma } ^ { 2 } ( \theta _ { \hat { \sigma } } ^ { 2 } )$ are the average and variance of σ (σˆ ), respectively. $\theta _ { { \pmb { \sigma } } \hat { \pmb { \sigma } } }$ is the covariance of $\pmb { \sigma }$ and σˆ . Constants c and $c _ { 2 }$ use MATLAB’s default settings. SSIM ranges from 0 to 1, with higher values indicating better similarity.

(3) Optimal sub-pattern assignment (OSPA): Evaluates target position and number estimation accuracy [56]:

$$
\mathrm { O S P A } = \frac { 1 } { M _ { \mathrm { M a x } } } \left( \operatorname* { m i n } _ { \varrho \in \Pi _ { M _ { \mathrm { M i n } } } } \sum _ { m = 1 } ^ { M _ { \mathrm { M i n } } } \left\| \hat { \mathbf { p } } _ { m } - \mathbf { p } _ { \varrho ( m ) } \right\| _ { 2 } + c _ { 3 } M _ { \Delta } \right) .\tag{25}
$$

Here, $M _ { \mathrm { M a x } } \ = \ \operatorname* { m a x } \{ M , \hat { M } \} , \ M _ { \mathrm { M i n } } \ = \ \operatorname* { m i n } \{ M , \hat { M } \}$ , and $M _ { \Delta } \ = \ | M - \hat { M } |$ , where M<sup>ˆ</sup> is the number of detected targets in the estimated image $\hat { \pmb { \sigma } } . \mathrm { ~ \ } \varrho$ is one element in the set $\Pi _ { M _ { \mathrm { M i n } } } ,$ which represents all possible permutations on $\{ 1 , 2 , \ldots , M _ { \mathrm { M i n } } \} . \mathbf { p } _ { m }$ and $\hat { \mathbf { p } } _ { m }$ denote true and estimated target locations. The penalty term $c _ { 3 } M _ { \Delta }$ with constant $c _ { 3 } = 1$ is considered to measure the target number estimation error.

(4) DR: Represents the proportion of correctly identified targets in the reconstructed image.

(5) FAR: Indicates the proportion of falsely detected targets that do not exist in the ground truth.

## B. On-Grid Simulation Results

This subsection utilizes Algorithm 1 to discuss the influences of system configurations on sensing performance under on-grid conditions.

1) Sensing Performance With Varying Antenna Numbers, BS Distances, and Transmit Powers: We evaluate the sensing performance of the proposed imaging-based surveillance method using the MSE and SSIM metrics. The results in Fig. 7 represent the average of 10,000 Monte Carlo simulations. The number of UAVs is set to $M \ = \ 6 .$ As the number of BS antennas increases, more CSI measurements can be leveraged for reconstructing low-altitude images. Consequently, the MSE decreases while the SSIM improves, indicating enhanced sensing performance. However, increasing the distance between BSs can degrade sensing performance due to stronger channel correlations among antennas, which enlarge the condition number of the sensing matrix. Nevertheless, these negative effects can be partially mitigated by increasing the sensing signal power or deploying larger transceiving antenna arrays. Therefore, wireless imaging-based surveillance of low-altitude airspace remains effective with proper system configurations.

TABLE II  
SENSING PERFORMANCE UNDER ON-GRID CONDITIONS WITH VARYING SENSING MODES AND VOXEL SIZES
<table><tr><td colspan="2"> $\sum \mathrm { ~ \sum ~ } d _ { 0 }$  mode</td><td>1 m</td><td>2 m</td><td>3 m</td><td>4 m</td><td>5 m</td></tr><tr><td rowspan="3">MSE  $( \times 1 0 ^ { - 4 } )$ </td><td>A</td><td>1.8598</td><td>0.3293</td><td>0.0574</td><td>0.0444</td><td>0.0429</td></tr><tr><td>B</td><td>60.741</td><td>2.0121</td><td>0.7762</td><td>0.4432</td><td>0.2236</td></tr><tr><td>C</td><td>466.72</td><td>21.370</td><td>13.519</td><td>7.9370</td><td>4.6723</td></tr><tr><td rowspan="4">DR</td><td>A</td><td>40.78%</td><td>83.22%</td><td>96.47%</td><td>98.99%</td><td>99.78%</td></tr><tr><td>B</td><td>24.07%</td><td>63.63%</td><td>86.34%</td><td>95.27%</td><td>98.02%</td></tr><tr><td>C</td><td>0.32%</td><td>2.25%</td><td>8.67%</td><td>22.58%</td><td>43.24%</td></tr><tr><td>A</td><td>70.92%</td><td>34.04%</td><td>12.60%</td><td>5.37%</td><td>1.18%</td></tr><tr><td rowspan="2">FAR</td><td>B</td><td>81.63%</td><td>54.15%</td><td>31.76%</td><td>18.73%</td><td>8.88%</td></tr><tr><td>C</td><td>98.77%</td><td>93.26%</td><td>78.99%</td><td>60.44%</td><td>44.09%</td></tr></table>

2) Sensing Performance With Different Sensing Modes and Voxel Sizes: We analyze the sensing performance of different sensing modes with varying imaging resolution $d _ { 0 } ,$ , setting $N _ { 0 } ~ = ~ 4$ , and $P _ { \mathrm { ~ s ~ } } = ~ 4 0 ~ $ dBm. The BS distance is fixed at 140 m. Table II presents the simulation results. Mode $\mathbf { \ddot { \theta } } ^ { 6 6 } ( \mathbf { A } ^ { \prime \prime }$ refers to the proposed joint monostatic and multi-static sensing scheme, where all BSs receive sensing signals transmitted by any of them. In Mode $\mathbf { \ddot { \delta B } } ^ { \prime \prime }$ , signals transmitted by one BS can only be received by other BSs [11], while in Mode $\mathbf { \tilde { C } } ^ { \prime \prime }$ , each BS can only receive signals transmitted by itself [17]. Among the three, Mode $\mathbf { \ddot { \theta } } ^ { 6 6 } ( \mathbf { A } ^ { \prime \prime }$ achieves the best sensing performance by aggregating the highest number of CSI measurements for image reconstruction. This demonstrates that integrating monostatic and multi-static sensing capabilities is essential for high-performance imaging. Additionally, all three modes exhibit improved imaging accuracy with increasing $d _ { 0 } .$

Fig. 8 illustrates true and predicted images under Mode $\mathbf { \ddot { \beta } A } . \mathbf { \vec { \beta } }$ Perfect image reconstruction is achieved at $d _ { 0 } = 3 \ \mathrm { m } ,$ , as seen in Fig. 8(f). However, reducing $d _ { 0 }$ increases channel correlations among voxels, making them harder to be distinguished, as analyzed in Sec. III-B using the PSF. For example, one target is lost at $d _ { 0 } = 2$ m, as seen in Fig. 8(e), while nearly no targets are accurately detected at $d _ { 0 } = 1$ m, as shown in Fig. 8(d). This indicates that an excessively fine imaging resolution may degrade performance due to increased correlations among voxels’ steering vectors. In summary, the proposed joint monostatic and multi-static sensing scheme provides superior imaging performance, and selecting an appropriate imaging resolution is critical to ensure accurate surveillance.

3) Sensing Performance With Varying Subcarrier Numbers, Bandwidths, and Antenna Spacings: We investigate the impact of subcarrier number $N _ { \mathrm { f } } ,$ bandwidth B, and antenna spacing $( \lambda _ { 0 } / 2 ) \cdot \xi$ on the 3D imaging performance. The ROI center is at $\hbar _ { \mathrm { r o i } } ~ = ~ 8 0$ m, and the number of UAVs is increased to $M \ = \ 2 4 .$ Since a larger $N _ { \mathrm { f } }$ provides more CSI measurements, we employ UPAs with $2 \times 2$ antennas to derive the simulation results presented in Fig. 9. The total sensing signal power is set to $\mathrm { \mathit { P } _ { s } } = 4 0 ~ \mathrm { d B m }$ . Although increasing $N _ { \mathrm { f } }$ reduces the power allocated per subcarrier, it leads to a lower MSE and a higher DR. This suggests that utilizing multiple subcarriers is advantageous for imaging, as it enables the acquisition of richer environmental information. However, similar to the observations in Fig. 4(c), a continuous increase in $N _ { \mathrm { f } }$ does not necessarily enhance imaging accuracy when $B$ is limited. Additionally, larger bandwidths can further improve sensing performance. Finally, deploying sparse arrays effectively reduces the MSE and increases the DR, as the enlarged imaging aperture facilitates the collection of more environmental details and enhances spatial resolution.

![](images/ede012dc941eaa59a3e69b5355c1a4ae70ee666e1f4196887dee3068fb29c326.jpg)  
(d) Estimate, d0 = 1m

(a) True image, d0 = 1m  
(b) True image, d0 = 2m  
(c) True image, d0 = 3m  
(e) Estimate, d0 = 2m  
(f) Estimate, d0 = 3m  
Fig. 8. Imaging results under on-grid conditions for different voxel sizes.  
![](images/15a399f1ca04ad2bf2f1cb0e463d345555d109f599de28b07f91acca8fdc250d.jpg)  
Fig. 9. Sensing performance of the 3D ROI with varying subcarrier numbers, bandwidths, and antenna spacings.

4) Tradeoff Between Communication and Sensing Performance: We consider an ISAC system in which one aerial image is captured per frame, utilizing $N _ { \mathrm { s } } = N _ { 0 } ^ { 2 } = 4 ~ \mathrm { I S A C }$ symbol intervals out of a total of 140 symbols per frame. The sensing signal power is set to $P _ { \mathrm { { s } } } = 0$ during pure communication intervals. During the ISAC period, BSs simultaneously direct beams toward both the ROI and the communication users. The beamforming matrix $\mathbf { W } _ { n _ { \mathrm { b } } }$ is designed according to [12] and [18] to minimize power leakage across different beams. This ensures that the multi-user interference term in (3) remains negligible. Similar to Sec. V-B.3, we employ $N _ { \mathrm { f } } = 6$ subcarriers within a bandwidth of $B = 4 0$ MHz to construct the 3D ROI image. The antenna spacing is set to $\lambda _ { 0 } / 2$ . For simplicity, we analyze a single communication user positioned at $[ 0 , 0 , 0 ] ^ { \mathrm { T } }$

![](images/a84f23d669cf847e3cdd662a6b6c197d631c81cc3a969f54455c757adda3aec1.jpg)  
Fig. 10. Tradeoff between communication and sensing performances.

Fig. 10 presents the simulation results for a total transmission power of $P _ { \mathrm { ~ t ~ } } = ~ 6 0$ dBm. The DR increases with $P _ { \mathrm { { s } } }$ and reaches 100% when $P _ { \mathrm { ~ s ~ } } = ~ 4 0 ~ $ dBm and the ROI center height is $\hbar _ { \mathrm { r o i } } ~ = ~ 8 0$ m. As $\hbar _ { \mathrm { r o i } }$ increases, achieving perfect target detection requires higher sensing signal power. This increase in $P _ { \mathrm { ~ s ~ } }$ slightly degrades the communication SE. However, the degradation remains minimal because the imaging function occupies only a small portion of the available communication resources. Our simulation results show that when $P _ { \mathrm { s } } = 4 0$ dBm, the desired communication signal power received by the user is approximately 24 dB higher than the interference caused by the sensing signals. As a result, the impact of sensing signals on communication performance is negligible. This is mainly due to the low UAV RCS and the long signal transmission distance. Therefore, the SE is primarily determined by the communication signal power $P _ { \mathrm { c } } ,$ highlighting the need to balance $P _ { \mathrm { { s } } }$ and $P _ { \mathrm { c } }$ to optimize ISAC performance.

## C. Off-Grid Simulation Results

This section evaluates the proposed imaging algorithms from Sec. IV under off-grid conditions. The BS distance is set to 140 m, the antenna array size is $5 \times 5 ,$ and the transmit power is $P _ { \mathrm { t } } = 4 0 ~ \mathrm { d B m } . ^ { 3 }$ The DNN used in this subsection consists of six residual blocks. The number of channels in the convolutional layers is set to [64, 128, 128, 128, 64, 32]. Network parameters are optimized via RMSprop on an Nvidia

TABLE III  
SENSING RESULTS OF DIFFERENT ALGORITHMS FOR OFF-GRID TARGETS
<table><tr><td>Methods</td><td>MSE</td><td>SSIM</td><td>OSPA</td><td>DR</td><td>FAR</td><td>Run Time (ms)</td></tr><tr><td>SP</td><td>0.0067</td><td>0.6909</td><td>27.7465</td><td>46.52%</td><td>69.41%</td><td>52.05 (CPU)</td></tr><tr><td> $\mathbf { A } ^ { \mathrm { H } } \mathbf { y }$ </td><td>0.0308</td><td>0.0534</td><td>72.5825</td><td>45.56%</td><td>85.99%</td><td>0.08 (GPU)</td></tr><tr><td> $\mathrm { D N N } { \sphericalangle \mathbf { y } }$ </td><td>0.0037</td><td>0.6895</td><td>50</td><td>0</td><td>0</td><td>11.41 (GPU)</td></tr><tr><td> $\mathrm { M o d e l + D N N { \_ } S P }$ </td><td>0.0033</td><td>0.7778</td><td>29.2561</td><td>35.06%</td><td>15.28%</td><td>65.07 (GPU)</td></tr><tr><td> $\mathbf { M o d e l + D N N \mathcal { A } A } ^ { \mathrm { H } } \mathbf { y }$ </td><td>0.0009</td><td>0.9186</td><td>7.5957</td><td>86.24%</td><td>3.29%</td><td>13.35 (GPU)</td></tr></table>

![](images/7af88e1b71cd6915f4e83873fd2974842b9bf51b9329ba4772fc410d70206a67.jpg)  
Fig. 11. Imaging results of different methods under off-grid conditions.

A100 GPU using PyTorch, trained for 200 epochs with an initial learning rate of 0.001, halving if the loss stagnates for five epochs. The dataset includes 100,000 MATLAB-generated images (10% for validation), with an additional 10,000 test images. The average UAV count is 6 for 2D and 12 for 3D ROIs, as detailed in Secs. V-C.1 to V-C.4 and Sec. V-C.5, respectively.

1) Sensing Performance Comparison Across Different Algo rithms: We compare the sensing performance of various imaging methods for off-grid UAV positions, including: the SP algorithm with on-grid sensing matrix, the intermediate sensing result $\mathbf { A } ^ { \mathrm { H } } \bar { \mathbf { y } } .$ , and a DNN trained using the CSI measurement y as the input (DNN<sup>^</sup>y). The proposed physics-embedded learning method in Sec. IV-B is validated by training DNNs using the outputs of the SP algorithm (Model+DNN<sup>^</sup>SP) and using $\mathbf { A } ^ { \mathrm { H } } \mathbf { y }$ $( \mathbf { M o d e l + D N N } \mathbf { \triangleleft A ^ { H } y } )$ . All DNN models are designed with a comparable number of trainable parameters and are trained using the same strategy. According to the simulation results in Table III, the proposed method $\mathrm { \mathrm { ^ { * } M o d e l + D N N \mathrm { \ 4 } A ^ { H } y ^ { , * } } }$ achieves the best performance across all evaluation metrics. Moreover, the execution time of the proposed method shows that it can achieve nearly real-time inference, primarily due to the high computational efficiency of the GPU. In contrast, the iteration-based SP algorithm executed on the CPU requires the longest computation time.

Fig. 11 further illustrates the imaging results produced by these methods. The SP algorithm struggles to correctly identify target voxels, often producing false detections due to model mismatch. The intermediate result $\mathbf { A } ^ { \mathrm { H } } \mathbf { y }$ and the DNN trained with y exhibit substantial visual noise, capturing little to no meaningful image information. While the “Model+DNN<sup>^</sup>SP” method partially detects targets, it frequently misplaces them due to distortions introduced by the SP algorithm. In contrast, the proposed “Model+DNN<sup>^</sup> $\bar { \mathbf { A } } ^ { \mathrm { H } } \mathbf { y } ^ { \mathrm { , , , } }$ method achieves precise image reconstruction and accurate non-zero voxel detection, demonstrating its superior capability in off-grid sensing.

![](images/27f8b4e92de868dc3576bb1166d1695bfc7f2e57b102225c5f716cbbc04c0dc3.jpg)  
Fig. 12. MSE and learning rate over training epochs.

2) Sensing Performance Comparison Across Different DNN Structures and Loss Functions: This section examines how different DNN architectures and loss functions affect training performance. The “resCNN” model employs the residual structure illustrated in Fig. 6(b). Additionally, an image denoising approach is tested, where the DNN is trained to estimate the noise component $\sigma _ { \mathrm { p r i } } - \sigma$ (Dn-CNN and Dn-resCNN). The simulation results in Table IV reveal that the Dn-CNN does not perform well in this imaging scenario, indicating that the noise in $\pmb { \sigma } _ { \mathrm { p n } }$ lacks a structured probability distribution that can be effectively learned by the DNN. Introducing a residual structure improves sensing performance, as seen in the comparison of different architectures. However, when sparse regularization is applied, as in Net-4 and Net-6, the networks tend to output all-zero images, leading to a failure in detecting low-altitude targets.

Training the DNNs with the proposed OHEM loss functions significantly enhances performance across all test metrics, particularly when comparing Net-5 and Net-8. The inclusion of a sparse regularization term further enhances the network’s effectiveness, as demonstrated by Net-9 and Net-10. The MSEs and learning rates of the last four DNNs during training, shown in Fig. 12, highlight the crucial role of the loss function in determining DNN performance. Among these models, Net-9, trained with the OHEM-1 loss function and $\alpha = 1$ , achieves the lowest MSE and OSPA while obtaining the highest SSIM.

TABLE IV  
SENSING PERFORMANCE ACROSS DIFFERENT DNN STRUCTURES AND LOSS FUNCTIONS
<table><tr><td>Network</td><td>DNN Structure</td><td>Loss Fun.</td><td>α</td><td>MSE</td><td>SSIM</td><td>OSPA</td><td>DR</td><td>FAR</td></tr><tr><td>Net-1</td><td>Dn-CNN</td><td>MSE</td><td>0</td><td>0.0021</td><td>0.8117</td><td>21.1022</td><td>73.99%</td><td>3.97%</td></tr><tr><td>Net-2</td><td>Dn-resCNN</td><td>MSE</td><td>0</td><td>0.0021</td><td>0.8200</td><td>20.6430</td><td>75.19%</td><td>4.09%</td></tr><tr><td>Net-3</td><td>CNN</td><td>MSE</td><td>0</td><td>0.0019</td><td>0.8352</td><td>19.1941</td><td>76.25%</td><td>3.91%</td></tr><tr><td>Net-4</td><td>CNN</td><td>MSE</td><td>1</td><td>0.0037</td><td>0.7699</td><td>50</td><td>0</td><td>0</td></tr><tr><td>Net-5</td><td>resCNN</td><td>MSE</td><td>0</td><td>0.0017</td><td>0.8457</td><td>17.5013</td><td>78.29%</td><td>3.93%</td></tr><tr><td>Net-6</td><td>resCNN</td><td>MSE</td><td>1</td><td>0.0037</td><td>0.7699</td><td>50</td><td>0</td><td>0</td></tr><tr><td>Net-7</td><td>resCNN</td><td>OHEM-1</td><td>0</td><td>0.0018</td><td>0.8658</td><td>16.7250</td><td>76.24%</td><td>3.95%</td></tr><tr><td>Net-8</td><td>resCNN</td><td>OHEM-2</td><td>0</td><td>0.0012</td><td>0.9156</td><td>8.7960</td><td>86.48%</td><td>4.01%</td></tr><tr><td>Net-9</td><td>resCNN</td><td>OHEM-1</td><td>1</td><td>0.0009</td><td>0.9186</td><td>7.5957</td><td>86.24%</td><td>3.29%</td></tr><tr><td>Net-10</td><td>resCNN</td><td>OHEM-2</td><td>1</td><td>0.0029</td><td>0.8546</td><td>29.9405</td><td>97.55%</td><td>3.22%</td></tr></table>

![](images/d441dde6ca8f4f8bd338c2c68e8aff06225e7735e88bedefee1a4f41f8a6772e.jpg)  
(a) OHEM-1

![](images/dc9611f9864978e94017f0bb954f43d714447473d39b7ba8e2624747db19a7d7.jpg)  
(b) OHEM-2  
Fig. 13. Sensing performance variation with different ratios (η) of selected passive to positive sample numbers.

In contrast, Net-10 achieves the best DR, identifying 97.55% of targets in the test dataset while maintaining a low FAR of 3.22%. This suggests that while Net-9 is optimal for accuracyfocused applications, Net-10 is preferable when maximizing the DR and minimizing missed targets.

3) Influence of η on OHEM-Based DNN Training: This section examines how the negative sample ratio η affects sensing performance by training a series of DNNs. The Fig. 13(a) and Fig. 13(b), respectively.

For OHEM-1, the three evaluation metrics, namely MSE, SSIM, and DR, exhibit different trends as η varies. When η is small, the network tends to generate a large number of non-zero voxels in the reconstructed images, which leads to inconsistencies with the true labels. As a result, the MSE remains high and the SSIM is low when $\eta = 1$ , indicating poor sensing performance, although the DR reaches its peak. As η increases, the number of selected negative samples $N _ { \mathrm { n e g } }$ grows, enhancing the loss function’s focus on negative samples, as described in (21). When $\eta = 1 0 .$ , a balance is achieved between attention to positive and negative samples, yielding the lowest MSE and highest SSIM while maintaining a DR only slightly lower than its peak value. Beyond this point, further increases in η cause the network to output images with more zerovalue voxels, leading to a degradation in DR and SSIM. When $\eta \geq 3 0$ , the network outputs all-zero images, capturing no target information.

For OHEM-2, the trends in MSE and SSIM are similar to those observed in OHEM-1. However, $\eta = 5$ achieves the best tradeoff between positive and negative samples in this case. Unlike OHEM-1, the DR continuously increases with growing η due to the weakened contribution of each passive sample, as reflected in the second term of (21). The DR saturates at approximately 98% when $\eta \geq 2 5$ , which marks the most significant difference in training behavior between OHEM-1 and OHEM-2.

TABLE V  
OSPA PERFORMANCE ACROSS VARYING ENVIRONMENTS (UNITS: OSPA IN METER, $P _ { \mathrm { { N } } }$ IN DBM)
<table><tr><td>Dataset</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>UAV number</td><td>6</td><td>6</td><td>6</td><td>4</td><td>8</td></tr><tr><td> $P _ { \mathfrak { n } }$ </td><td>-120</td><td>-110</td><td>-100</td><td>1</td><td>1</td></tr><tr><td>OSPA-A</td><td>9.6810</td><td>10.2537</td><td>12.1318</td><td>6.9136</td><td>11.3106</td></tr><tr><td>OSPA-B</td><td>9.0680</td><td>10.5033</td><td>12.3616</td><td>6.5370</td><td>11.2219</td></tr></table>

These results underscore the critical role of η in optimizing sensing performance. The optimal η depends on the specific loss function and application, requiring careful selection to balance detection accuracy and robustness.

4) Evaluation of the Adaptability of the Proposed DNN to Different Environments: To assess the adaptability of the proposed DNN, six new datasets are generated for training and testing. The first dataset is constructed with a ROI containing six UAVs, with the additive noise power set to $P _ { \mathrm { ~ n ~ } } = \mathrm { ~ 0 ~ }$ The parameter settings for the remaining five datasets are provided in Table V. Using the OHEM-1 loss function with α = 1, the proposed DNN is trained on the first dataset and achieves an OSPA of 9.6159 m on the corresponding test set. Without additional retraining, the same DNN is directly tested on the other five datasets, and the OSPA results are listed in the $\mathrm { ^ { 6 6 } O S P A { - } A { ^ { , } } }$ row of Table V. Additionally, five separate DNNs are trained using the respective datasets and evaluated using their corresponding test data, with the results presented in the $\mathrm { ^ { 6 6 } O S P A { - } B { ^ { , } } }$ row of Table V. The comparison reveals that the DNN trained on the first dataset performs well on unseen datasets with varying noise powers and UAV numbers, achieving results comparable to those of DNNs specifically trained on each dataset. This demonstrates that the proposed method exhibits strong adaptability to diverse environments. The enhanced generalization capability is likely attributed to the embedded physics-based information in the input primary result, as formulated in (20). Furthermore, sensing performance degrades with the noise power and UAV number increasing, owing to the corresponding higher difficulty in lowaltitude imaging.

![](images/59fee1057a7b9b7854e052deb237926dad2023d708e39e6990bf9ba23180edbf.jpg)

![](images/6d0f8621a306c1b18c554d45a000a251976122cede0fb0700bd508750c8f648b.jpg)  
Fig. 14. The simulation scenario of urban canyon environments in Sionna.

5) 3D ROI Imaging in Sionna: This subsection employs Sionna, a widely used ray tracing channel emulator in both academic and industrial fields, to generate the sensing channels required by the proposed algorithms. Specifically, we use a real-world road and its surroundings in Hong Kong to simulate urban canyon environments. The data is downloaded from OpenStreetMap, processed in Blender, and then used by Sionna. The scenario is depicted in Fig. 14, where the canyon is 50 m wide and 130 m long, and the buildings are approximately 60 m high. Four BSs are mounted at the four corners of the canyon at an altitude of $\hbar _ { \mathrm { b s } } = 1 0$ m. The 3D ROI has dimensions of $4 0 \ : \mathrm { m } \times 1 2 0 \ : \mathrm { m } \times 4 0$ m and is discretized into an $8 \times 2 4 \times 8$ image with a voxel size of $d _ { 0 } = 5$ m. The number of UAVs in the ROI is set to $M = 8 .$ . We use 3D convolutional kernels to generate 3D images of the ROI.

Considering the interference caused by surrounding buildings, dedicated beamformers oriented toward the ROI [12] and calibration processes [47] should be employed to suppress interference. Table VI presents the sensing performance with varying levels of residual interference, where increasing interference results in degraded performance across all evaluated metrics. Specifically, the DR exceeds 80% with 0.1% residual interference but can decrease by more than 25% when no interference suppression techniques are applied. Fig. 15 illustrates the 3D imaging results under various interference levels. Nearly perfect image formation is achieved in Fig. 15(a) when no interference is present. In Fig. 15(b), the DNN successfully detects all UAVs under 0.1% residual interference, although the estimated scattering coefficients may deviate from the ground truth. With higher levels of interference, detection errors increase and falsely detected targets appear, as shown in Fig. 15(c) and Fig. 15(d). These results demonstrate that interference suppression using beamforming and background removal is critical to the proposed algorithms. Effective suppression enables high sensing performance.

![](images/58239122c552ca20ac89d95b4663dd6151a978df56d55f90dd6a11d1f5640d1e.jpg)  
(c) 1% interference  
Fig. 15. 3D imaging results for different residual interference ratios.

TABLE VI  
3D SENSING PERFORMANCE IN SIONNA VS. RATIO OF RESIDUAL INTERFERENCE
<table><tr><td>Ratio of residual interference</td><td>0</td><td>0.1%</td><td>1%</td><td>10%</td><td>100%</td></tr><tr><td>MSE</td><td>0.0034</td><td>0.0034</td><td>0.0035</td><td>0.0035</td><td>0.0041</td></tr><tr><td>SSIM</td><td>0.9006</td><td>0.7695</td><td>0.7437</td><td>0.6653</td><td>0.2540</td></tr><tr><td>DR</td><td>83.37%</td><td>80.35%</td><td>77.40%</td><td>69.88%</td><td>57.85%</td></tr><tr><td>FAR</td><td>3.57%</td><td>3.80%</td><td>4.03%</td><td>3.65%</td><td>4.10%</td></tr></table>

## VI. CONCLUSION AND FUTURE RESEARCH DIRECTIONS

This study investigates flight activity surveillance in emerging LAE scenarios by leveraging existing ISAC cellular networks. A CS-based imaging problem is formulated under on-grid conditions, with the PSF assessing the system’s sensing capabilities. To address the challenges posed by off-grid errors, a physics-embedded learning method is introduced, combining primary results obtained from the traditional sensing matrix with refinements via DL techniques. The proposed approach enhances DNN training through OHEM-based loss functions, improving DRs. Simulation results validate the effectiveness of the proposed imaging-based surveillance framework. The physics-embedded learning method accurately reconstructs both 2D and 3D images in off-grid scenarios, outperforming conventional CS-based algorithms. These findings highlight the potential of ISAC-based imaging for high-precision, real-time low-altitude surveillance, offering a scalable solution for future airspace monitoring applications.

Our future work may include optimizing the algorithm design to enhance DRs in complex environments and reduce the training overhead of the DNN. In addition, dynamic imaging through UAV tracking across successive time instants is anticipated to improve the quality of low-altitude surveillance. Validation through field trials conducted in live commercial network environments is also required to verify the practical applicability of the proposed algorithms. Finally, the proposed analytical framework and algorithms are expected to be applicable to other CS-based off-grid problems, such as CS-based channel estimation.

## REFERENCES

[1] Y. Huang, J. Yang, C.-K. Wen, S. Xia, X. Li, and S. Jin, “Cooperative ISAC network for off-grid imaging-based low-altitude surveillance,” in Proc. IEEE 101st Veh. Technol. Conf., Jun. 2025, pp. 1–7, doi: 10.1109/ VTC2025-Spring65109.2025.11174673.

[2] G. Wu, F. Zhou, K. K. Wong, and X.-Y. Li, “A vehicle-mounted radarvision system for precisely positioning clustering UAVs,” IEEE J. Sel. Areas Commun., vol. 42, no. 10, pp. 2688–2703, Oct. 2024.

[3] B. Zheng and F. Liu, “Random signal design for joint communication and SAR imaging towards low-altitude economy,” IEEE Wireless Commun. Lett., vol. 13, no. 10, pp. 2662–2666, Oct. 2024.

[4] J. He, C. Vanwynsberghe, H. Chen, C. Huang, and A. Fakhreddine, “Device-free 3D drone localization in RIS-assisted mmWave MIMO networks,” in Proc. IEEE Global Commun. Conf., Dec. 2024, pp. 4436–4441.

[5] China Mobile.(2024). White Paper on Technical Solutions for Typical Scenarios of 5G-A Integrated Sensing and Comunication. [Online]. Available: http://www.cww.net.cn

[6] Study on Integrated Sensing and Comunication (Release 19), document TR 22.837, V19.2.0, 3GPP, Dec. 2023.

[7] L. Ruan et al., “Cooperative relative localization for UAV swarm in GNSS-denied environment: A coalition formation game approach,” IEEE Internet Things J., vol. 9, no. 13, pp. 11560–11577, Jul. 2022.

[8] M. Meles, A. Rajasekaran, L. Mela, R. Ghazalian, K. Ruttik, and R. Jantti, “Performance evaluation of measurement based GPS denied¨ 3D drone localization and tracking,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), Mar. 2023, pp. 1–6.

[9] J. Zhao, J. Zhang, D. Li, and D. Wang, “Vision-based anti-UAV detection and tracking,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 12, pp. 25323–25334, Dec. 2022.

[10] Y. Huang, J. Yang, C.-K. Wen, and S. Jin, “Integrated communication and learned recognizer with customized RIS phases and sensing durations,” IEEE Trans. Commun., early access, Mar. 6, 2025, doi: 10.1109/TCOMM.2025.3548768.

[11] G. Liu et al., “Cooperative sensing for 6G mobile cellular networks: Feasibility, performance, and field trial,” IEEE J. Sel. Areas Commun., vol. 42, no. 10, pp. 2863–2876, Oct. 2024.

[12] R. Li, Z. Xiao, and Y. Zeng, “Toward seamless sensing coverage for cellular multi-static integrated sensing and communication,” IEEE Trans. Wireless Commun., vol. 23, no. 6, pp. 5363–5376, Jun. 2024.

[13] G. Cheng, X. Song, Z. Lyu, and J. Xu, “Networked ISAC for low-altitude economy: Coordinated transmit beamforming and UAV trajectory design,” IEEE Trans. Commun., vol. 73, no. 8, pp. 5832–5847, Aug. 2025.

[14] G. Afifi and Y. Gadallah, “Autonomous 3-D UAV localization using cellular networks: Deep supervised learning versus reinforcement learning approaches,” IEEE Access, vol. 9, pp. 155234–155248, 2021.

[15] Y. Huang, J. Yang, W. Tang, C.-K. Wen, S. Xia, and S. Jin, “Joint localization and environment sensing by harnessing NLOS components in RIS-aided mmWave communication systems,” IEEE Trans. Wireless Commun., vol. 22, no. 12, pp. 8797–8813, Dec. 2023.

[16] J. Guan, A. Paidimarri, A. Valdes-Garcia, and B. Sadhu, “3-D imaging using millimeter-wave 5G signal reflections,” IEEE Trans. Microw. Theory Techn., vol. 69, no. 6, pp. 2936–2948, Jun. 2021.

[17] J. Tang et al., “Cooperative ISAC-empowered low-altitude economy,” IEEE Trans. Wireless Commun., vol. 24, no. 5, pp. 3837–3853, May 2025.

[18] Z. Wang and V. Wong, “Heterogeneous graph neural network for cooperative ISAC beamforming in cell-free MIMO systems,” in Proc. 30th Annu. Int. Conf. Mobile Comput. Netw., Dec. 2024, pp. 2161–2172.

[19] C. Wang, J. Tian, J. Cao, and X. Wang, “Deep learning-based UAV detection in pulse-Doppler radar,” IEEE Trans. Geosci. Remote Sens., vol. 60, 2022, Art. no. 5105612.

[20] Y. Ma, S. Xia, C. Bai, Z. Wang, and S. Li, “Networked collaborative sensing using multi-domain measurements: Architectures, performance limits and algorithms,” IEEE Trans. Veh. Technol., vol. 74, no. 4, pp. 6330–6345, Apr. 2025.

[21] S.-L. Shih, C.-K. Wen, C. Yuen, and S. Jin, “Machine learning-based direct source localization for passive movement-driven virtual large array,” IEEE Trans. Wireless Commun., vol. 24, no. 3, pp. 2498–2513, Mar. 2025.

[22] Q. Shi, L. Liu, S. Zhang, and S. Cui, “Device-free sensing in OFDM cellular network,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1838–1853, Jun. 2022.

[23] Q. Shi and L. Liu, “Joint LOS identification and data association for 6Genabled networked device-free sensing,” IEEE Trans. Commun., vol. 72, no. 8, pp. 5117–5129, Aug. 2024.

[24] W. Dai and O. Milenkovic, “Subspace pursuit for compressive sensing signal reconstruction,” IEEE Trans. Inf. Theory, vol. 55, no. 5, pp. 2230–2249, May 2009.

[25] X. Tong, Z. Zhang, J. Wang, C. Huang, and M. Debbah, “Joint multi-user communication and sensing exploiting both signal and environment sparsity,” IEEE J. Sel. Topics Signal Process., vol. 15, no. 6, pp. 1409–1422, Nov. 2021.

[26] Y. Huang, J. Yang, C.-K. Wen, and S. Jin, “RIS-aided single-frequency 3D imaging by exploiting multi-view image correlations,” IEEE Trans. Commun., vol. 72, no. 8, pp. 5003–5018, Aug. 2024.

[27] X. Jing, F. Liu, C. Masouros, and Y. Zeng, “ISAC from the sky: UAV trajectory design for joint communication and target localization,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 12857–12872, Oct. 2024.

[28] X. Shang, R. Lin, and Y. Cheng, “Mixed-ADC based PMCW MIMO radar angle-Doppler imaging,” IEEE Trans. Signal Process., vol. 72, pp. 883–895, 2024.

[29] Y. You, C. Zhang, and L. Zhang, “Bayesian matching pursuit based estimation of off-grid channel for millimeter wave massive MIMO system,” IEEE Trans. Veh. Technol., vol. 71, no. 11, pp. 11603–11614, Nov. 2022.

[30] Z. Yang, L. Xie, and C. Zhang, “Off-grid direction of arrival estimation using sparse Bayesian inference,” IEEE Trans. Signal Process., vol. 61, no. 1, pp. 38–43, Jan. 2013.

[31] Z. Wei, W. Yuan, S. Li, J. Yuan, and D. W. K. Ng, “Off-grid channel estimation with sparse Bayesian learning for OTFS systems,” IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 7407–7426, Sep. 2022.

[32] R. Li, S. Sun, and M. Tao, “Atomic norm minimization-based DoA estimation for IRS-assisted sensing systems,” IEEE Wireless Commun. Lett., vol. 13, no. 10, pp. 2672–2676, Oct. 2024.

[33] S. Gao et al., “A robust super-resolution gridless imaging framework for UAV-borne SAR tomography,” IEEE Trans. Geosci. Remote Sens., vol. 62, 2024, Art. no. 5210917.

[34] Y. Huang, Y. Zhang, J. Tao, C. Wen, G. Liao, and W. Hong, “Off-grid DOA estimation via a deep learning framework,” Sci. China Inf. Sci., vol. 66, no. 12, Nov. 2023, Art. no. 222305.

[35] Y. Zhang, Y. Huang, J. Tao, S. Tang, H. C. So, and W. Hong, “A two-stage multi-layer perceptron for high-resolution DOA estimation,” IEEE Trans. Veh. Technol., vol. 73, no. 7, pp. 9616–9631, Jul. 2024.

[36] R. Guo, T. Huang, M. Li, H. Zhang, and Y. C. Eldar, “Physics-embedded machine learning for electromagnetic data imaging: Examining three types of data-driven imaging methods,” IEEE Signal Process. Mag., vol. 40, no. 2, pp. 18–31, Mar. 2023.

[37] X. Chen, Z. Wei, M. Li, and P. Rocca, “A review of deep learning approaches for inverse scattering problems,” Prog. Electromagn. Res., vol. 167, pp. 67–81, 2020.

[38] L. Wu, Z.-M. Liu, and Z.-T. Huang, “Deep convolution network for direction of arrival estimation with sparse prior,” IEEE Signal Process. Lett., vol. 26, no. 11, pp. 1688–1692, Nov. 2019.

[39] L. Wan, K. Liu, and W. Zhang, “Deep learning-aided off-grid channel estimation for millimeter wave cellular systems,” IEEE Trans. Wireless Commun., vol. 21, no. 5, pp. 3333–3348, May 2022.

[40] X. Su, Z. Liu, J. Shi, P. Hu, T. Liu, and X. Li, “Real-valued deep unfolded networks for off-grid DOA estimation via nested array,” IEEE Trans. Aerosp. Electron. Syst., vol. 59, no. 4, pp. 4049–4062, Aug. 2023.

[41] J. Hu, H. Zhang, K. Bian, M. D. Renzo, Z. Han, and L. Song, “MetaSensing: Intelligent metasurface assisted RF 3D sensing by deep reinforcement learning,” IEEE J. Sel. Areas Commun., vol. 39, no. 7, pp. 2182–2197, Jul. 2021.

[42] F. Wang et al., “Dreamer: Dual-RIS-aided imager in complementary modes,” IEEE Trans. Antennas Propag., vol. 73, no. 7, pp. 4863–4878, Jul. 2025.

[43] A. Shrivastava, A. Gupta, and R. Girshick, “Training region-based object detectors with online hard example mining,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2016, pp. 761–769.

[44] H. Lu et al., “A tutorial on near-field XL-MIMO communications toward 6G,” IEEE Commun. Surveys Tuts., vol. 26, no. 4, pp. 2213–2257, 4th Quart., 2024.

[45] K. Chen, C. Qi, G. Y. Li, and O. A. Dobre, “Near-field multiuser communications based on sparse arrays,” IEEE J. Sel. Topics Signal Process., vol. 18, no. 4, pp. 619–632, May 2024.

[46] Z. Zhang, X. Chai, K. Long, A. V. Vasilakos, and L. Hanzo, “Full duplex techniques for 5G networks: Self-interference cancellation, protocol design, and relay selection,” IEEE Commun. Mag., vol. 53, no. 5, pp. 128–137, May 2015.

[47] Z. Li, A. Dubey, S. Shen, N. K. Kundu, J. Rao, and R. Murch, “Radio tomographic imaging with reconfigurable intelligent surfaces,” IEEE Trans. Wireless Commun., vol. 23, no. 11, pp. 15784–15797, Nov. 2024.

[48] A. Goldsmith, Wireless Communications. Cambridge, U.K.: Cambridge Univ. Press, 2005.

[49] Y. Huang, J. Yang, W. Tang, C.-K. Wen, and S. Jin, “Fourier transform-based wavenumber domain 3D imaging in RIS-aided communication systems,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 13872–13888, Oct. 2024.

[50] C. Zhao et al., “BUPTCMCC-6G-CMG+: A GBSM-based ISAC standard channel model generator,” Sci. China Inf. Sci., vol. 68, no. 5, pp. 1–15, Apr. 2025.

[51] V. M. Patel, G. R. Easley, D. M. Healy, and R. Chellappa, “Compressed synthetic aperture radar,” IEEE J. Sel. Topics Signal Process., vol. 4, no. 2, pp. 244–254, Mar. 2010.

[52] Q. Zou and H. Yang, “A concise tutorial on approximate message passing,” 2022, arXiv:2201.07487.

[53] K. Nakata, D. Miyashita, J. Deguchi, and R. Fujimoto, “Adaptive quantization method for CNN with computational-complexity-aware regularization,” in Proc. IEEE Int. Symp. Circuits Syst. (ISCAS), May 2021, pp. 1–5.

[54] S. Ohta, T. Nishio, R. Kudo, K. Takahashi, and H. Nagata, “Real2Sim2Real for point cloud-based mmWave link quality prediction: An empirical study,” IEEE Trans. Veh. Technol., vol. 74, no. 3, pp. 5270–5275, Mar. 2025.

[55] P. Sharma, R. N. Tiwari, P. Singh, P. Kumar, and B. K. Kanaujia, “MIMO antennas: Design approaches, techniques and applications,” Sensors, vol. 22, no. 20, p. 7813, Oct. 2022.

[56] D. Schuhmacher, B.-T. Vo, and B.-N. Vo, “A consistent metric for performance evaluation of multi-object filters,” IEEE Trans. Signal Process., vol. 56, no. 8, pp. 3447–3457, Aug. 2008.

![](images/4cfc179d05d97036c4cc75af6b9312b36a4d389b0929931f015df2ef16b04152.jpg)

Yixuan Huang (Graduate Student Member, IEEE) received the B.E. degree in electronics and information engineering from Northwestern Polytechnical University, Xi’an, China, in 2021. He is currently pursuing the Ph.D. degree in information and communications engineering with Southeast University, Nanjing, China. His current research interests include integrated sensing and communication, wireless imaging, and reconfigurable intelligent surface.

![](images/5caed6bbc2ebab2ce0821db4ce704961a2a1c2e3380e994eb5318a3a3e4c18a2.jpg)

Jie Yang (Member, IEEE) received the B.S. degree in communication engineering from Nanjing University of Science and Technology, Nanjing, China, in 2015, and the M.S. and Ph.D. degrees in information and communications engineering from Southeast University, Nanjing, China, in 2018 and 2022, respectively. In 2022, she joined the School of Automation, Southeast University, where she is currently an Assistant Professor. Her current research interests include signal processing for wireless communications, massive MIMO, millimeter-wave wireless communications, and integrated sensing and communications.

![](images/3c5c620cb79040db362d90af5d191fa57c06f5c979f0a2b86a8da8f156a3c253.jpg)

Shuqiang Xia received the master’s degree in signal and information processing from Nanjing University of Science and Technology, China, in 2002. He is a Senior Communication Research Expert with ZTE Corporation. His research interests focus on integrated sensing and communications (ISAC), carrier aggregation (CA), and ultra-reliable low-latency communications (URLLC). He was a recipient of the China Patent Gold Award and the Second Prize of National Technological Invention Award.

![](images/c6d365fbb35d2669d7e1f5650e830ee64c0ea8354654fa57457ffad6d7cc469f.jpg)

Chao-Kai Wen (Fellow, IEEE) received the Ph.D. degree from the Institute of Communications Engineering, National Tsing Hua University, Taiwan, in 2004. From 2004 to 2009, he was with the Industrial Technology Research Institute and MediaTek Inc., Hsinchu, Taiwan, where he focused on broadband digital transceiver design. In 2009, he joined the Institute of Communications Engineering, National Sun Yat-sen University, Kaohsiung, Taiwan, where he currently holds the position of a Professor. His research interests revolve around the optimization of wireless multimedia networks.

![](images/8045d916cd77a6bca8e96192e1f08e3af63cd43b6c5b2e05460359d6e093f535.jpg)

Shi Jin (Fellow, IEEE) received the B.S. degree in communications engineering from Guilin University of Electronic Technology, Guilin, China, in 1996, the M.S. degree from Nanjing University of Posts and Telecommunications, Nanjing, China, in 2003, and the Ph.D. degree in information and communications engineering from Southeast University, Nanjing, in 2007. From June 2007 to October 2009, he was a Research Fellow with University College London, Adastral Park Research Campus, London, U.K. He is currently with the faculty of the National

Mobile Communications Research Laboratory, Southeast University. His research interests include wireless communications, random matrix theory, and information theory. He and his co-authors were received the 2011 IEEE Communications Society Stephen O. Rice Prize Paper Award in the field of communication theory, the 2022 Best Paper Award, the 2010 Young Author Best Paper Award by the IEEE Signal Processing Society, the 2023 Jack Neubauer Memorial Award by the IEEE Vehicular Technology Society, and the 2024 Marconi Prize Paper Award by the IEEE Communications Society and IEEE Signal Processing Society. He is serving as an Area Editor for IEEE TRANSACTIONS ON COMMUNICATIONS and IET Electronics Letters. He was an Associate Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICA-TIONS, IEEE COMMUNICATIONS LETTERS, and IET Communications.