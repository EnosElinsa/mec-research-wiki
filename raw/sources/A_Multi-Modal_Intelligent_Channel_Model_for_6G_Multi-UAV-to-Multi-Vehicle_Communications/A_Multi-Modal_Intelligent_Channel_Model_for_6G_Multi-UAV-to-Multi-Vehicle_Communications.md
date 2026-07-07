# A Multi-Modal Intelligent Channel Model for 6G Multi-UAV-to-Multi-Vehicle Communications

Lu Bai , Senior Member, IEEE, Mengyuan Lu , Ziwei Huang , Member, IEEE, and Xiang Cheng , Fellow, IEEE

Abstract—In this paper, a novel multi-modal intelligent channel model for sixth-generation (6G) multiple-uncrewed aerial vehicle (multi-UAV)-to-multi-vehicle communications is proposed. To thoroughly explore the mapping relationship between the physical environment and the electromagnetic space in the complex multi-UAV-to-multi-vehicle scenario, two new parameters, i.e., terrestrial traffic density (TTD) and aerial traffic density (ATD), are developed and a new sensing-communication intelligent integrated dataset is constructed in suburban scenario under different TTD and ATD conditions. With the aid of sensing data, i.e., light detection and ranging (LiDAR) point clouds, the parameters of static scatterers, terrestrial dynamic scatterers, and aerial dynamic scatterers in the electromagnetic space, e.g., number, distance, angle, and power, are quantified under different TTD and ATD conditions in the physical environment. In the proposed model, the channel non-stationarity and consistency on the time and space domains and the channel non-stationarity on the frequency domain are simultaneously mimicked. The channel statistical properties, such as time-space-frequency correlation function (TSF-CF), time stationary interval (TSI), and Doppler power spectral density (DPSD), are derived and simulated. Simulation results match ray-tracing (RT) results well, which verifies the accuracy of the proposed multi-UAV-to-multi-vehicle channel model.

Index Terms—Multi-modal intelligent channel model, 6G multi-UAV-to-multi-vehicle communications, sensing-

communication intelligent integrated dataset, terrestrial traffic density (TTD), aerial traffic density (ATD).

## I. INTRODUCTION

W <sup>ITH</sup> <sup>the</sup> <sup>wide</sup> <sup>popularization</sup> <sup>of</sup> <sup>the</sup> <sup>low-altitude</sup>economy, intelligent low-altitude transportation has economy, intelligent low-altitude transportation has received considerable attention. As an emerging sixthgeneration (6G) intelligent networked scenario, intelligent low-altitude transportation involves a variety of low-altitude uncrewed aerial vehicles (UAVs), all types of vehicles, roadside units, and pedestrians. Considering the security of UAVs and autonomous vehicles as well as more convenient and more efficient information service, more reliable and lower latency communication requirements of 6G intelligent networked low-altitude transportation communications can no longer be efficiently addressed by the conventional communication networks [1], [2]. To better design and analyze the 6G intelligent networked low-altitude transportation communication system, the research on the underlying propagation characteristics and corresponding channel modeling is essential [3].

So far, many researchers have worked on UAV-to-ground channel measurement campaigns, channel characteristic analysis, and channel modeling, which can to some extent investigate 6G intelligent networked low-altitude channels. The UAV-to-ground channel characteristics at 5.8 GHz in suburban scenarios were measured and analyzed in [4]. The authors in [5] and [6] conducted the UAV-to-ground channel measurement campaigns at 1 GHz, 3.9 GHz and 4 GHz, and analyzed the time non-stationarity in UAV-to-ground channels. The spatial channel characterizations of UAV-toground channel at 1.8 GHz and 2.5 GHz were respectively investigated based on the measurement campaigns in [7] and [8]. Based upon these channel measurement campaigns and characteristic analysis, extensive UAV-to-ground channel models were proposed. According to the electromagnetic wave theory and ray-tracing (RT) technology, the deterministic UAVto-ground channel models [9], [10] were proposed. However, the deterministic channel models are limited to certain physical environments. To apply to more diverse UAV-to-ground physical environments, the geometry-based stochastic models (GBSMs), whose parameters can be adjusted with the UAV-to-ground physical environment, are proposed, including regular-shaped GBSMs (RS-GBSMs) and irregular-shaped GBSMs (IS-GBSMs). In UAV-to-ground RS-GBSMs [11], [12] the scattering clusters were modeled on two-dimensional (2D) rings, 2D ellipses, three-dimensional (3D) cylinders,

Ziwei Huang and Xiang Cheng are with the State Key Laboratory of Photonics and Communications, School of Electronics, Peking University, Beijing 100871, China (e-mail: ziweihuang@pku.edu.cn; xiangcheng@pku.edu.cn). Digital Object Identifier 10.1109/TWC.2025.3630319

and 3D ellipsoids to calculate propagation paths and channel parameters. However, the scattering clusters in RS-GBSMs are too restricted on regular shapes to mimic the high-dynamic UAV channels. Therefore, more suitable and flexible IS-GBSMs [13], [14], [15] were proposed for UAV-to-ground channels.

Nevertheless, the aforementioned UAV-to-ground channe models are limited and insufficient to describe the 6G intelligent networked low-altitude transportation channel. With the development of the low-altitude economy and the maturation of 6G technology, the requirements for application scenarios involving multiple-UAV (multi-UAV) and multi-vehicle cooperative communications, such as intelligent transportation systems (ITSs), urban air mobility (UAM), and uncrewed delivery, are significantly increasing. The single-UAV channel models are usually reduplicated to support the design of multi-UAV cooperative communication systems. However, the method of reduplicated usage of single-UAV channel models cannot mimic the consistent and integrated propagation environment of multi-UAV cooperative communications and cannot calculate the channel impulse response (CIR) of each channel from each UAV to ground station in a targeted manner and analyze channel properties, which are significantly important to system design. Meanwhile, the high-mobility of UAVs and vehicles, the infinity of intelligent agents equipped with communication equipment, and the intricacy of pervasive connectivity bring new challenges for channel modeling. Furthermore, more reliable and lower latency communication requirements of 6G intelligent networked low-altitude transportation communications rely on a more in-depth understanding of the propagation environment and more accurate channel modeling, which the conventional channel modeling method can no longer satisfy. The aforementioned channel model ignored the benefit of sensing data and solely utilized radio-frequency (RF) communication information. This paper focuses on three typical 6G application scenarios, i.e., integrated sensing and communications, integrated artificial intelligence (AI) and communications, and ubiquitous connectivity. Fortunately, in low-altitude intelligent transportation, the multiple intelligent networked UAVs, autonomous vehicles, and roadside units are simultaneously deployed with communication devices and multi-modal sensors. In this case, the communication capability and sensing capability coexist symbiotically, which brings more opportunities for 6G intelligent networked low-altitude transportation channel modeling. Inspired by human synesthesia, Synesthesia of Machines (SoM) was proposed in [16] for the technology development of intelligent multi-modal sensing-communication integration. Unlike integrated sensing and communications (ISAC) [17], which focuses on RF radar sensing and communications, SoM refers to the intelligent integration of multi-modal sensing and RF communications, including RF communications, RF sensing, i.e., millimeter wave (mmWave) radar, and non-RF sensing, i.e., light detection and ranging (LiDAR) and RGB-Depth (RGB-D) cameras, etc. Similar to the way humans sense the environment via multiple organs, i.e., the environ mental information obtained by multiple organs is mutually facilitated via biological neural networks, multi-modal sen sors and communication devices, i.e., machine senses, can assist mutually and capture more detailed and more accurate environmental information based on machine learning (ML). Therefore, the intelligent networked agents can utilize ML algorithms to improve the efficiency of data processing. Since channel modeling essentially describes the electromagnetic environment that is closely related to the physical environment, channel modeling with the help of intelligent multi-modal sensing-communication integration has the potential to handle the high-mobility and intricacy of pervasive connectivity in 6G intelligent networked low-altitude transportation communications. Therefore, multi-modal intelligent channel modeling (MMICM) was proposed in [18].

In this paper, inspired by MMICM, we explore the mutual facilitation of multi-modal sensing-communication integration in channel modeling of 6G intelligent networked low-altitude transportation communications, investigate the mapping relationship between the physical environment and the electromagnetic space with channel information and LiDAR point clouds, and propose a novel multi-modal intelligent channel model for 6G multi-UAV-to-multi-vehicle communications. The main contributions and novelties of this paper are summarized below.

1) To more accurately mimic intelligent networked lowaltitude transportation channels, a novel multi-modal intelligent channel model is proposed for 6G multi-UAV-to-multi-vehicle communications. In the proposed model, the impact of terrestrial traffic density (TTD) and aerial traffic density (ATD) is considered for the first time in UAV-to-ground channel modeling. Furthermore, a novel LiDAR-aided temporal and spatial non-stationarity and consistent algorithm is developed to simultaneously depict the channel non-stationarity and consistency on the time and space domains and the channel non-stationarity on the frequency domain.

2) To thoroughly explore the mapping relationship between the physical environment and the electromagnetic space in the complex multi-UAV-to-multi-vehicle scenario, a new multi-UAV-to-multi-vehicle cooperative sensingcommunication integration (MUMV-CSCI) dataset in suburban forking road scenarios is constructed, including the channel information and LiDAR point clouds. In the constructed dataset, the diversity in the electromagnetic space, i.e., the channels among multiple UAVs and vehicles, and the variety in the physical environment, i.e., the environment under different TTD and ATD conditions, are considered.

3) With the help of sensing information in the physical environment, i.e., LiDAR point clouds, scatterers of multi-UAV-to-multi-vehicle channels in the electromagnetic space can be for the first time divided into static scatterers, terrestrial dynamic scatterers, and aerial dynamic scatterers. In this case, a novel multi-UAVto-multi-vehicle channel parameter table, e.g., number, distance, angle, and power of dynamic and static scatterers, is developed under different TTD and ATD conditions in the suburban scenario.

TABLE I  
NUMBERS OF LIDAR POINT CLOUDS AND LINKS WITH SCATTERERS UNDER LOW, MEDIUM, AND HIGH TTD AND ATD CONDITIONS
<table><tr><td>Conditions</td><td>LiDAR point clouds</td><td>Communication links</td></tr><tr><td>High TTD and ATD</td><td>45,000</td><td>337,500</td></tr><tr><td>Medium TTD and ATD</td><td>34,500</td><td>180,000</td></tr><tr><td>Low TTD and ATD</td><td>16,500</td><td>36,000</td></tr><tr><td>Total</td><td>96,000</td><td>553,500</td></tr></table>

4) The multi-UAV-multi-vehicle channel statistical properties, including time-space-frequency correlation function (TSF-CF), time stationary interval (TSI), and Doppler power spectral density (DPSD), are derived and simulated. Based on the simulation result, the impact of different TTD and ATD conditions on channel statistics is investigated. Simulation results have close agreement with RT-based results, which verify the proposed multi-UAV-multi-vehicle channel model.

The remainder of this paper is organized as follows. Section II describes the MUMV-CSCI dataset in the suburban forking road scenario and presents the quantified channel parameters under different TTD and ATD conditions. In Section III, a novel multi-modal intelligent channel model for 6G multiple-UAV (multi-UAV)-to-multi-vehicle communications is proposed. The multi-UAV-to-multi-vehicle channel statistical properties are given in Section IV. Section V presents the corresponding simulation result, which is further compared with the RT-based result. At last, the conclusions are obtained in Section VI.

## II. MUMV-CSCI DATASET AND CHANNEL PARAMETERIZATION IN SUBURBAN SCENARIO

In real-world scenarios, particularly in complex and dynamic environments involving cooperative communications among multi-UAV and multi-vehicle, the capability of cooperative sensing and communication among multiple terminals plays a pivotal role. Multi-UAV and multivehicle cooperative communications is presented as a representative application scenario of intelligent multi-modal sensing–communication integration. Therefore, the multi-UAV-to-multi-vehicle sensing-communication intelligent integrated measurement campaign is conducted in a suburban forking road scenario. To investigate the impact of traffic density conditions in both terrestrial and aerial areas, the TTD and ATD are developed. TTD describes the traffic density of ground transportation, e.g., ground vehicles. ATD describes the traffic density of air traffic, e.g., UAVs and aerial vehicles. In multi-UAV-to-multi-vehicle communication systems, traffic density directly affects interference and congestion in communication networks. Therefore, the measurement campaign is carried out under different TTD and ATD conditions.

Since the multi-UAV-to-multi-vehicle channel is highly dynamic, complicated, and changeable, it is significant to explore the static, terrestrial dynamic, and aerial dynamic scatterers. Moreover, investigating the impact of TTD and ATD conditions is essential for the design of 6G multi-UAVto-multi-vehicle sensing-communication intelligent integrated communication systems. Nevertheless, the conventional channel measurement campaigns that solely process Doppler information in channels cannot distinguish static, terrestrial dynamic, and aerial dynamic scatterers [19]. To fill this gap, the statistical distributions of key channel parameters related to static, terrestrial dynamic, aerial dynamic scatterers in the multi-UAV-to-multi-vehicle channels are for the first time investigated under high, medium, and low TTD and ATD conditions, which are presented in Table II.

## A. MUMV-CSCI Dataset and Mapping Relationship Between Electromagnetic Space and Physical Environment in Suburban Forking Road Scenarios

Currently, there is no real-world datasets available to cover multi-UAV-to-multi-vehicle communication scenarios, which include RF communication information and sensing data. Due to the lack of measurement data, our research on multi-UAV-to-multi-vehicle communication channel modeling relies primarily on simulation data. Since no software can simultaneously collect integrated sensing data and communication data, two simulation platforms, i.e., AirSim [20] and Wireless InSite [21], are fused to fulfill the in-depth integration between sensing and communications as well as the precise alignment between the physical environment and electromagnetic space. To address the data collection discrepancies between Wireless InSite and AirSim, a comprehensive integration of both software systems is implemented. Data consistency and accuracy in both the physical environment and electromagnetic space are ensured through four steps, including the construction of simulation scenarios at the initial time, trajectory deter mination, batch generation of dynamic simulation scenarios, and raw-data acquisition. Similar to the vehicular sensing communication integration dataset in [22], to develop the MUMV-CSCI dataset focused on multi-UAV-to-multi-vehicle communications, the first step is to construct the simulation scenario with aligned physical and electromagnetic environ ments. Suburban forking road 3D models are constructed in AirSim and imported into Wireless InSite to generate accurate channel data. The second step determines the trajectories of vehicles and UAVs utilizing the Simulation of Urban MObility (SUMO) simulation platform, to ensure precise alignment between physical and electromagnetic spaces for accurate movement simulations. The third step generates 1500 dynamic suburban forking road scenarios by modifying 3D coordinates of dynamic objects and sensors in both AirSim and Wireless InSite. Finally, the fourth step efficiently acquires sensing data and communication data, where AirSim is utilized to collect sensing data and Wireless InSite is utilized to simulate and export CIR matrices for the generated scenarios. This process realizes centimeter-level spatial consistency and frame-level time synchronization. Each transceiver is equipped with communication equipment and a LiDAR device to collect communication data and sensing data. The carrier frequency of communication equipment is $f _ { \mathrm { c } } ~ = ~ 2 8$ GHz with the bandwidth of 2 GHz. All of the transceivers are equipped with one antenna. To investigate the impact of traffic density conditions in both terrestrial and aerial areas, the TTD and ATD are developed for the first time. TTD and ATD represent the respective impacts of ground and aerial traffic densities on the communication channels. In complex communication environments involving multiple UAVs and multiple vehicles, these impacts are often intertwined. Considering the trade-off between computational resources and modeling complexity, both TTD and ATD are generally classified into three levels, i.e., low TTD and ATD, medium TTD and ATD, as well as high TTD and ATD conditions. In this paper, the numbers of vehicles under low, medium, and high TTD conditions in the terrestrial areas are 8, 15, and 25, respectively. The numbers of UAVs under low, medium, and high ATD conditions in the aerial areas are 3, 8, and 15, respectively.

TABLE II  
KEY STATISTICAL PARAMETERS IN MULTI-UAV-TO-MULTI-VEHICLE SENSING AND COMMUNICATION INTELLIGENT INTEGRATION CHANNELS
<table><tr><td rowspan=1 colspan=2>Parameter</td><td rowspan=1 colspan=1>Distribution</td><td rowspan=1 colspan=1>Type</td><td rowspan=1 colspan=1>TTD and ATD Conditions</td><td rowspan=1 colspan=3>Value</td></tr><tr><td rowspan=16 colspan=2>Number</td><td rowspan=16 colspan=1>Logistic</td><td rowspan=3 colspan=1>Static cluster</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { { \m</td><td rowspan=1 colspan=1>u _ { \mathrm { s } } ^ { \mathrm { c } , \mathrm { L } } = 0 . 1 5 1 1 , \gamma _ { \mathrm { s } } ^ { \mathrm { c } , \mathrm { L } } = 0 . 0 5 2 0 } }$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { { \mu</td><td rowspan=1 colspan=1>_ { \mathrm { s } } ^ { \mathrm { c } , \mathrm { L } } } } = 0 . 0 9 1 5 , \gamma _ { \mathrm { s } } ^ { \mathrm { c } , \mathrm { L } } = 0 . 0 4 5 5$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \m</td><td rowspan=1 colspan=1>u _ { \mathrm { s } } ^ { \mathrm { c } , \mathrm { L } } } } = 0 . 0 6 2 0 , \gamma _ { \mathrm { s } } ^ { \mathrm { c } , \mathrm { L } } = 0 . 0 8 2 1$ </td></tr><tr><td rowspan=3 colspan=1>Terrestrial dynamic cluster</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { {</td><td rowspan=1 colspan=1>\mu _ { \mathrm { t d } } ^ { \mathrm { c , L } } } } = 0 . 1 1 2 6 , \gamma _ { \mathrm { t d } } ^ { \mathrm { c , L } } = 0 . 1 0 1 5$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { {</td><td rowspan=1 colspan=1>\mu _ { \mathrm { t d } } ^ { \mathrm { c , L } } } } = 0 . 1 1 3 8 , \gamma _ { \mathrm { t d } } ^ { \mathrm { c , L } } = 0 . 0 8 5 1$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\begin{array} { r } {</td><td rowspan=1 colspan=1>\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { c } , \mathrm { L } } } } = 0 . 0 8 4 2 , \gamma _ { \mathrm { t d } } ^ { \mathrm { c } , \mathrm { L } } = 0 . 0 2 8 9 } \end{array}$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic cluster</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { {</td><td rowspan=1 colspan=1>\mu _ { \mathrm { a d } } ^ { \mathrm { c , L } } } } = 0 . 2 3 5 6 , \gamma _ { \mathrm { a d } } ^ { \mathrm { c , L } } = 0 . 0 3 2 1$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\mu _ { \mat</td><td rowspan=1 colspan=1>hrm { a d } } ^ { \mathrm { c , L } } = 0 . 1 8 2 5 , \gamma _ { \mathrm { a d } } ^ { \mathrm { c , L } } = 0 . 0 5 2 8$ </td></tr><tr><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { {</td><td rowspan=1 colspan=1>\mu _ { \mathrm { s } } ^ { \mathrm { s , L } } } } = 0 . 7 5 3 4 , \gamma _ { \mathrm { s } } ^ { \mathrm { s , L } } = 0 . 5 2 3 6$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\ddot { \mu _ { \</td><td rowspan=1 colspan=1>mathrm { s } } ^ { \mathrm { s } , \mathrm { L } } } = 0 . 6 0 2 4 , \gamma _ { \mathrm { s } } ^ { \mathrm { s } , \mathrm { L } } = 0 . 4 7 2 6$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \m</td><td rowspan=1 colspan=1>u _ { \mathrm { e } } ^ { \mathrm { s } , \mathrm { L } } } } = 0 . 3 4 2 5 , \gamma _ { \mathrm { s } } ^ { \mathrm { s } , \mathrm { L } } = 0 . 3 8 5 5$ </td></tr><tr><td rowspan=3 colspan=1>Terrestrial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\mu _ { { \mathrm</td><td rowspan=1 colspan=1>{ t d } } } ^ { { \mathrm { s } , \mathrm { L } } } = 0 . 4 4 6 1 , \gamma _ { { \mathrm { t d } } } ^ { { \mathrm { s } , \mathrm { L } } } = 0 . 3 9 2 1$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { {</td><td rowspan=1 colspan=1>\mu _ { \mathrm { t d } } ^ { \mathrm { s , L } } } } = 0 . 3 9 2 8 , \gamma _ { \mathrm { t d } } ^ { \mathrm { s , L } } = 0 . 2 5 1 1$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\begin{array} { r } {</td><td rowspan=1 colspan=1>\frac { \mathrm { ~  ~ \cdot ~ } } { \mu _ { \mathrm { t d } } ^ { \mathrm { s , L } } } = 0 . 3 2 1 3 , \gamma _ { \mathrm { t d } } ^ { \mathrm { s , L } } = 0 . 1 8 6 3 } \end{array}$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { {</td><td rowspan=1 colspan=1>mathrm { a d } } ^ { \mathrm { s , L } } = 0 . 4 2 6 1$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2>µs,d</td><td rowspan=1 colspan=1>d = 0.3925</td></tr><tr><td rowspan=8 colspan=2>Distance</td><td rowspan=3 colspan=1>Gamma</td><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline</td><td rowspan=1 colspan=1>{ { \alpha _ { \mathrm { s } } ^ { \mathrm { G } } = 0 . 8 2 2 3 , \beta _ { \mathrm { s } } ^ { \mathrm { G } } = 1 . 9 2 3 2 } }$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline</td><td rowspan=1 colspan=1>{ { \alpha _ { \mathrm { s } } ^ { \mathrm { G } } = 0 . 6 9 8 2 , \beta _ { \mathrm { s } } ^ { \mathrm { G } } = 2 . 0 2 6 3 } }$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\begin{array</td><td rowspan=1 colspan=1>} { r } { \frac { \partial \mathrm { \ddot { G } } } { \partial \mathrm { s } } = 0 . 6 2 4 1 , \beta _ { \mathrm { s } } ^ { \mathrm { G } } = 2 . 4 5 8 1 } \end{array}$ </td></tr><tr><td rowspan=3 colspan=1>Rayleigh</td><td rowspan=3 colspan=1>Terrestrial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=3> $\overline { { \sigma _ { \mathrm { t d } } ^ { \mathrm { R } } = 0 . 3 5 4 1 } }$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\sigma _ { \mathrm { t d } } ^ { \mathrm { R } } = 0 . 3 0 2 6$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=3> $\frac { \mathrm { R } } { \sigma _ { \mathrm { t d } } ^ { \mathrm { k d } } } = 0 . 2 0 2 5$ </td></tr><tr><td rowspan=2 colspan=1>Rayleigh</td><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=3> $\sigma _ { \mathrm { a d } } ^ { \mathrm { R } } = 0 . 3 3 5 6$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\sigma _ { \mathrm { a d } } ^ { \mathrm { R } } = 0 . 2 2 8 7$ </td></tr><tr><td rowspan=32 colspan=1>Angle</td><td rowspan=8 colspan=1>AAoD</td><td rowspan=8 colspan=1>Gaussian</td><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mat</td><td rowspan=1 colspan=1>hrm { s } } ^ { \mathrm { A A o D } } } } = 0 . 8 2 5 4 , \sigma _ { \mathrm { s } } ^ { \mathrm { A A o D } } = 0 . 9 2 5 4$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mat</td><td rowspan=1 colspan=1>hrm { s } } ^ { \mathrm { A A o D } } } } = 0 . 7 6 1 2 , \sigma _ { \mathrm { s } } ^ { \mathrm { A A o D } } = 0 . 8 7 2 3$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mat</td><td rowspan=1 colspan=1>hrm { s } } ^ { \mathrm { A A o D } } } } = 0 . 7 0 2 5 , \sigma _ { \mathrm { s } } ^ { \mathrm { A A o D } } = 0 . 7 5 6 6$ </td></tr><tr><td rowspan=3 colspan=1>Terrestrial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=3> $\overline { { \mu _ { \mathrm { t } \mathrm { d } } ^ { \mathrm { A A o D } } } } = 0 . 9 2 1 3 , \sigma _ { \mathrm { t } \mathrm { d } } ^ { \mathrm { A A o D } } = 1 . 9 2 5 3$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { A A o D } } } } = 0 . 8 1 9 0 , \sigma _ { \mathrm { t d } } ^ { \mathrm { A A o D } } = 1 . 7 6 2 2$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=3> $\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { A A o D } } } } = 0 . 7 6 2 3 , \sigma _ { \mathrm { t d } } ^ { \mathrm { A A o D } } = 1 . 2 1 0 1$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { a d } } ^ { \mathrm { A A o D } } } } = 0 . 3 2 4 1 , \sigm</td><td rowspan=1 colspan=1>a _ { \mathrm { a d } } ^ { \mathrm { A A o D } } = 1 . 0 1 2 5$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\mu _ { \mathrm { a d } } ^ { \mathrm { A A o D } } = 0 . 2 0 1 5 , \sigma _ { \m</td><td rowspan=1 colspan=1>athrm { a d } } ^ { \mathrm { A A o D } } = 0 . 9 2 1 5$ </td></tr><tr><td rowspan=8 colspan=1>AAoA</td><td rowspan=8 colspan=1>Gaussian</td><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { A A o A } } } } = 0 . 4 5 2 1 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { s } } ^ { \mathrm { A A o A } } = 0 . 4 8 3 4$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { A A o A } } } } = 0 . 4 0 2 5 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { s } } ^ { \mathrm { A A o A } } = 0 . 4 5 1 2$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { A A o A } } } } = 0 . 3 8 1 6 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { s } } ^ { \mathrm { A A o A } } = 0 . 3 2 6 6$ </td></tr><tr><td rowspan=3 colspan=1>Terrestral dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { A A o A } } } } = - 0 . 3 2 1 5 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { t d } } ^ { \mathrm { A A o A } } = 0 . 5 1 2 4$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { A A o A } } } } = - 0 . 4 1 5 6 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { t d } } ^ { \mathrm { A A o A } } = 0 . 4 2 6 6$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { A A o A } } } } = - 0 . 2 5 1 1 , \si</td><td rowspan=1 colspan=1>gma _ { \mathrm { t d } } ^ { \mathrm { A A o A } } = 0 . 1 7 5 6$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { a d } } ^ { \mathrm { A A o A } } } } = 0 . 5 4 1 6 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { a d } } ^ { \mathrm { A A o A } } = 0 . 6 5 2 4$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\begin{array} { r } { \frac { \partial \cdot \mathrm { \partial } ^ { 4 . 4 . 4 } } { \mu _ { \mathrm { a d } } ^ { \mathrm { A d } }</td><td rowspan=1 colspan=1>} = 0 . 4 2 1 1 , \sigma _ { \mathrm { a d } } ^ { \mathrm { A A o A } } = 0 . 5 8 1 5 } \end{array}$ </td></tr><tr><td rowspan=8 colspan=1>EAoD</td><td rowspan=8 colspan=1>Gaussian</td><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\textstyle \overbrace { \mu _ { \mathrm { s } } ^ { \mathrm { E A o D } } = 0 . 7 5 1 4 , \sigma _ { \ma</td><td rowspan=1 colspan=1>thrm { s } } ^ { \mathrm { E A o D } } = 0 . 8 5 1 2 } ^ { \mathrm { s u s } }$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { E A o D } } } } = 0 . 7 1 4 2 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { s } } ^ { \mathrm { E A o D } } = 0 . 6 2 1 5$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { E A o D } } } } = 0 . 7 8 3 6 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { s } } ^ { \mathrm { E A o D } } = 0 . 4 3 1 5$ </td></tr><tr><td rowspan=3 colspan=1>Terrestrial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\begin{array} { r } { \overline { { \mu } } _ { { \sf t } , d } ^ { \mathrm { E A o D } } = 0 . 1 5 4 5 , \sigma</td><td rowspan=1 colspan=1>_ { { \sf t } { \sf d } } ^ { \mathrm { E A o D } } = 0 . 7 8 5 1 } \end{array}$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { E A o D } } } } = 0 . 1 9 5 1 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { t d } } ^ { \mathrm { E A o D } } = 0 . 7 0 1 1$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=1> $\over</td><td rowspan=1 colspan=1>line { { \mu _ { \mathrm { t d } } ^ { \mathrm { E A o D } } } } = 0 . 1 7 6 6 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { t d } } ^ { \mathrm { E A o D } } = 0 . 6 7 8 9$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=1> $\begin{</td><td rowspan=1 colspan=1>array} { r } { \dot { \overline { { \mu } } } _ { \mathrm { a d } } ^ { \mathrm { E A o D } } = 0 . 9 5 1 1 ,</td><td rowspan=1 colspan=1>\sigma _ { \mathrm { a d } } ^ { \mathrm { E A o D } } = 1 . 8 2 5 1 } \end{array}$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=1> $\over</td><td rowspan=1 colspan=1>line { { \mu _ { \mathrm { a d } } ^ { \mathrm { E A o D } } } } = 0 . 9 1 5 1 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { a d } } ^ { \mathrm { E A o D } } = 1 . 6 4 3 5$ </td></tr><tr><td rowspan=8 colspan=1>EAoA</td><td rowspan=8 colspan=1>Gaussian</td><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=1> $\texts</td><td rowspan=1 colspan=1>tyle \overbrace { \mu _ { \mathrm { s } } ^ { \mathrm { E A o A } } = 0 . 8 5 1 6 , \sigma _ { \</td><td rowspan=1 colspan=1>mathrm { s } } ^ { \mathrm { E A o A } } = 0 . 7 6 1 2 } ^ { \mathrm { * } . }$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=1> $\dot {</td><td rowspan=1 colspan=1>\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { E A o A } } } } } = 0 . 8 7 8 1 ,</td><td rowspan=1 colspan=1>\sigma _ { \mathrm { s } } ^ { \mathrm { E A o A } } = 0 . 6 9 2 1$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { s } } ^ { \mathrm { E A o A } } } } = 0 . 8 4 2 3 , \si</td><td rowspan=1 colspan=1>gma _ { \mathrm { s } } ^ { \mathrm { E A o A } } = 0 . 5 5 1 6$ </td></tr><tr><td rowspan=3 colspan=1>Terrestrial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\dot { \overline { { \mu _ { \mathrm { t d } } ^ { \mathrm { E A o A } } } } } = 0 . 2 5 1 1 , \</td><td rowspan=1 colspan=1>sigma _ { \mathrm { t d } } ^ { \mathrm { E A o A } } = 0 . 9 2 1 8$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=2> $\textstyle \overbrace { \mu _ { \mathrm { t d } } ^ { \mathrm { E A o A } } } ^ { \mathrm { * * } } = 0</td><td rowspan=1 colspan=1>. 1 9 2 1 , \sigma _ { \mathrm { t d } } ^ { \mathrm { * A o A } } = 0 . 9 0 5 5$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=2> $\overline { { \mu _ { \mathrm { t d . } } ^ { \mathrm { E A o A } } } } = 0 . 2 2 4 9 , \sig</td><td rowspan=1 colspan=1>ma _ { \mathrm { t d . } } ^ { \mathrm { E A o A } } = 0 . 8 1 2 7$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=2> $\mu _ { \mathrm { a d } } ^ { \mathrm { E A o A } } = 0 . 8 9 1 5 , \sigma _ { \</td><td rowspan=1 colspan=1>mathrm { a d } } ^ { \mathrm { E A o A } } = 1 . 9 6 2 7$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\overline { { \mu _ { \mathrm { a d } } ^ { \mathrm { E A o A } } } } = 0 . 7 8 1 2 , \sigma _ { \mathrm { a d } } ^ { \mathrm { E A o A } } = 1 . 8 5 4 1$ </td></tr><tr><td rowspan=8 colspan=2>Power-Delay</td><td rowspan=8 colspan=1>Exponential</td><td rowspan=3 colspan=1>Static scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=3> $\xi _ { \mathrm { s } } = 2 . 6 8 8 1 \times 1 0 ^ { 6 } , \eta _ { \mathrm { s } } = 3 1 . 9 2 0 4 , \sigma _ { \mathrm { E , s } } = 1 9 . 9 3 5 0$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\xi _ { \mathrm { s } } = 4 . 8 0 4 3 \times 1 0 ^ { 6 } , \eta _ { \mathrm { s } } = 3 0 . 4 2 5 1 , \sigma _ { \mathrm { E , s } } = 2 2 . 3 5 8 1$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=3> $\overline { { \xi _ { \mathrm { s } } = 2 . 2 9 7 8 \times 1 0 ^ { 6 } , \eta _ { \mathrm { s } } = 3 0 . 0 1 1 2 , \sigma _ { \mathrm { E , s } } = 1 6 . 1 6 0 3 } }$ </td></tr><tr><td rowspan=3 colspan=1>Terrestrial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=3> $\xi _ { \mathrm { t d } } = 2 . 1 9 3 1 \times 1 0 ^ { 6 } , \eta _ { \mathrm { t d } } = 3 1 . 3 9 3 4 , \sigma _ { \mathrm { E , t d } } = 1 1 . 6 4 7 2$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\xi _ { \mathrm { t d } } = 3 . 6 5 5 4 \times 1 0 ^ { 6 } , \eta _ { \mathrm { t d } } = 3 0 . 5 1 3 6 , \sigma _ { \mathrm { E , t d } } = 1 3 . 6 7 5 8$ </td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=3> $\xi _ { \mathrm { t d } } = 1 . 2 0 3 0 \times 1 0 ^ { 6 } , \eta _ { \mathrm { t d } } = 3 1 . 4 6 1 0 , \sigma _ { \mathrm { E , t d } } = 0 . 2 2 2 2$ </td></tr><tr><td rowspan=2 colspan=1>Aerial dynamic scatterer</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=3> $\xi _ { \mathrm { a d } } = 3 . 9 7 9 7 \times 1 0 ^ { 6 } , \eta _ { \mathrm { a d } } = 2 9 . 2 9 0 0 , \sigma _ { \mathrm { E , a d } } = 1 2 . 0 0 1 4$ </td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=3> $\overline { { \xi _ { \mathrm { a d } } = 5 . 5 3 4 6 \times 1 0 ^ { 6 } , \eta _ { \mathrm { a d } } = 2 8 . 5 7 9 8 , \sigma _ { \mathrm { E , a d } } = 9 . 8 2 9 3 } }$ </td></tr></table>

![](images/7e58b2a62e80c0efb7824f21cd587570a2b1d86646a2cd16dd11c72b5b6afe91.jpg)

![](images/eae7f76ff78cf30fddbb000d72f3e82a7e9f3609cfc414907cd44de985b53694.jpg)  
Raw LiDAR point clouds and scatterers

![](images/1a5b0af3dc1d01452fbfbe39a17d662583a65323e7f8b50d03c05c81e0cf5216.jpg)  
LiDAR point clouds after clustering and scatterers

![](images/29c4fd08ddf03895b96b252536a61ab227d936251719572b55384f8b3d721f3e.jpg)  
Processed LiDAR point clouds with static, terrestrial dynamic, aerial dynamic scatterers, and unknown scatterers

Fig. 1. LiDAR point clouds and scatterers in multi-UAV-to-multi-vehicle suburban forking road scenarios under high TTD and ATD conditions in Airsim and Wireless InSite.  
![](images/4ed20a2e81bd8030954df8c91836a7e4f3f74135b7310ba4f402548242a817d7.jpg)  
(a)

![](images/172cd5a34db436b8e52dfbfb5c840ea00d3106cd21b3b90c089c1facc8650655.jpg)  
(b)

![](images/14fd51ca06e7528ab502d900ada19bc5d5048c2bcd0b6f83a080e6dd20d3e01e.jpg)  
(c)  
Fig. 2. UAV flight trajectories under multi-UAV-to-multi-vehicle scenarios. Figs. (a)–(c) are the UAV flight trajectories in Wireless InSite under high, medium, and low TTD and ATD conditions, respectively.

The scenarios under high TTD and ATD conditions in AirSim and Wireless InSite are shown in Fig. 1. The objects, i.e., vehicles and UAVs, have the same size and initial position and follow the same trajectories in AirSim and Wireless InSite. In the low TTD and ATD conditions, the channel data of the links between the 1-st to 3-rd UAV and the 1-st to 8-th vehicles is collected. In the medium TTD and ATD conditions, the channel data of the links between the 1-st to 8-th UAV and the 1-st to 15-th vehicles is collected. In the high TTD and ATD conditions, the channel data of the links between the 1-st to 15-th UAV and the 1-st to 15-th vehicles is collected. This configuration is designed to maintain a consistent number of core communication nodes, i.e., 15 vehicles, across medium and high TTD conditions, thereby isolating the impact of the additional 10 environmental vehicles as dynamic scatterers on channel characteristics. The flight trajectory and height of UAVs under different TTD and ATD are shown in Fig. 2. The flight height of all UAVs is set between 10 and 15 m. Therefore, a new MUMV-CSCI dataset in the suburban forking road is constructed. For clarity, Table I summarizes the data volume size of the sensing data and communication data.

The high mobility of multiple transceivers and scatterers leads to complicated characteristics. Therefore, the detection of dynamic scatterers is of great significance. With the aid of sensing data, i.e., LiDAR point clouds, the static, terrestrial dynamic, and aerial dynamic scatterers are detected and matched with the static, terrestrial dynamic, and aerial dynamic objects. The raw LiDAR point clouds are redundant and full of useless ground points, which need to be eliminated. There is solely information related to static objects and dynamic objects in the pre-processed LiDAR point clouds, which represent static buildings/facilities and dynamic

![](images/7077ed218cd47e3b993e78bfe2d0302e704029d0c607cda96c7e8ef840dd3fdf.jpg)  
(a)

![](images/04c1731bb9da23988181e34c12ee50351143851ee4500c31a91635e3c7929427.jpg)  
(b)

![](images/67943773511499695483d426f5dd9a48bbaac95f9ee8f9be4e753dc509496c15.jpg)

![](images/71defce6582dfca42f4e8adcf5b8a4d97d3de7475c999ddfe6d20e84d7bdd15c.jpg)  
(d)

(c)  
![](images/bd156cd88b17903ad01904132dc244c5eaafab2560b6e096299a0544c3f299e2.jpg)  
(e)

![](images/0795622a854e5f9101eaff1d7c3192f6493c35d9784c8a4d6203c9e0f89fbad6.jpg)  
(f)  
Fig. 3. CDFs of static/terrestrial dynamic/aerial dynamic scatterer and cluster number parameters with the Logistic distribution fitting under different TTD and ATD conditions. Figs. (a)–(c) show the CDFs of scatterer number parameters under high, medium, and low TTD and ATD conditions, respectively Figs. (d)–(f) show the CDFs of cluster number parameters under high, medium, and low TTD and ATD conditions, respectively.

UAVs/vehicles in the physical environment. By exploiting typical density-based spatial clustering of applications with noise (DBSCAN) [23], the objects in the physical environment are extracted. According to the sizes of extracted objects, the objects can be classified into static, terrestrial dynamic, and aerial dynamic objects. To intuitively show the alignment accuracy between the two domains, Fig. 1 demonstrates the matching of LiDAR point clouds with scatterer locations. Fig. 1 clearly shows LiDAR point clouds of a vehicle and an UAV, represented by blue and green point clouds, and displays the corresponding scatterer locations, represented by red scatter points. By comparing the positions of LiDAR point clouds and scatterers, it is obvious that the physical environment and the electromagnetic propagation space are precisely synchronized. The matching of the building edge positions detected by point clouds with the scatterers further demonstrates the accurate alignment of sensing data and communication data. The positions of scatterers are obtained from the reflection and scattering point coordinates of each link, outputted by the Wireless InSite simulation. Scatterers coincide with a static/terrestrial dynamic/aerial dynamic object detected from the LiDAR point clouds in the physical environment, thus the scatterers are determined as a static/terrestrial dynamic/aerial dynamic scatterer in the electromagnetic space.

## B. Channel Parameterization and Characterization

1) Numbers of Scatterers and Clusters: Currently, the numbers of static, terrestrial dynamic, and aerial dynamic scatterers in standardized models [24], [25], [26], [27] are not differentiated modeling. Meanwhile, cooperation communications between multi-UAVs and multi-vehicles are also not considered. With the aid of LiDAR point clouds, static, terrestrial dynamic, and aerial dynamic scatterers can be accurately distinguished. The numbers of static, terrestrial dynamic, aerial dynamic scatterers in the transmission link from the i-th UAV $( i ~ = ~ 1 , 2 , \ldots , I )$ , i.e., transmitter (Tx), to the j-th vehicle $( j = 1 , 2 , \ldots , J ) , \mathrm { i . e . }$ , receiver (Rx), are denoted as $B _ { \mathrm { s } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ $\bar { B } _ { \mathrm { t d } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ , and $B _ { \mathrm { a d } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ . Considering the impact of transmission distance, the static, terrestrial dynamic, aerial dynamic scatterer ratios, i.e., $N _ { \mathrm { s } } ^ { \dot { \mathrm { U } } _ { i } , \mathrm { C } _ { j } } ( t ) , ~ N _ { \mathrm { t d } } ^ { \mathrm { U } _ { i } ^ { \times } , \mathrm { C } _ { j } } ( t )$ , and $N _ { \mathrm { a d } } ^ { \mathrm { U } _ { i } ^ { \bullet } , \mathrm { C } _ { j } } ( t )$ are introduced. The static/terrestrial dynamic/aerial dynamic scatterer number ratio represents the ratio of static/terrestrial dynamic/aerial dynamic scatterer number to the distance between the i-th UAV and the j-th vehicle, which is calculated by

$$
N _ { \mathrm { s } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { B _ { \mathrm { s } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) } { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert }\tag{1}
$$

$$
N _ { { \mathrm { t d } } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { B _ { { \mathrm { t d } } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) } { \| \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \| }\tag{2}
$$

$$
N _ { \mathrm { a d } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { B _ { \mathrm { a d } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) } { \| \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \| }\tag{3}
$$

where $\mathbf { T } ^ { \mathrm { U } _ { i } } ( t )$ and $\mathbf { R } ^ { \mathrm { C } _ { j } } ( t )$ are the locations of the i-th UAV and the j-th vehicle. Moreover, based on the constructed MUMV-CSCI dataset, the static, terrestrial dynamic, and aerial dynamic scatterer number ratios in each communication link at each snapshot are calculated and analyzed. Figs. 3(a)–(c)

gives the cumulative distribution functions (CDFs) of static, terrestrial dynamic, and aerial dynamic scatterer number ratios under low, medium, and high TTD and ATD, respectively. The CDF of static/terrestrial dynamic/aerial dynamic scatterer number ratio fits well with the Logistic distribution, which is given by

$$
F _ { \mathrm { s / t d / a d } } ^ { \mathrm { s , L } } ( x ) = \frac { 1 } { 1 + e ^ { - ( x - \mu _ { \mathrm { s / t d / a d } } ^ { \mathrm { s , L } } ) / \gamma _ { \mathrm { s / t d / a d } } ^ { \mathrm { s , L } } } }\tag{4}
$$

where $\mu _ { \mathrm { s / t d / a d } } ^ { \mathrm { s , L } }$ and $\gamma _ { \mathrm { s / t d / a d } } ^ { \mathrm { s , L } }$ are the mean value and the scale parameter of the Logistic distribution for static/terrestrial dynamic/aerial dynamic scatterers. From Table II and Fig. 3, it can be seen that as the TTD and ATD conditions increase, the mean value and variance value of the Logistic distribution for the CDF of dynamic scatterers increase. This phenomenon can be explained that the number of dynamic scatterers increases as the number of dynamic vehicles and UAVs around the transceiver increases.To further investigate channel characteristics, the static/terrestrial dynamic/aerial dynamic scatterers are clustered to explore the statistical distribution of the numbers of static/terrestrial dynamic/aerial dynamic clusters. Three new cluster number parameters, $M _ { \mathrm { s } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } ^ { \bullet } } ( t ) , M _ { \mathrm { t d } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ and $M _ { \mathrm { a d } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ , which represent the ratios of static, terrestrial dynamic, and aerial dynamic cluster numbers to the distance between the i-th UAV and the j-th vehicle, are introduced. The number of parameters of static, terrestrial dynamic, and aerial dynamic clusters for each communication link at each snapshot is calculated. Figs. 3(d)–(f) illustrate the CDFs of static, terrestrial dynamic, and aerial dynamic clusters under high, medium, and low TTD and ATD conditions. The Logistic distribution for the CDF of static/terrestrial dynamic/aerial dynamic scatterer clusters can be represented as

$$
F _ { \mathrm { s / t d / a d } } ^ { \mathrm { c , L } } ( x ) = \frac { 1 } { 1 + e ^ { - ( x - \mu _ { \mathrm { s / t d / a d } } ^ { \mathrm { c , L } } ) / \gamma _ { \mathrm { s / t d / a d } } ^ { \mathrm { c , L } } } }\tag{5}
$$

where $\mu _ { \mathrm { s / t d / a d } } ^ { \mathrm { c } , \mathrm { L } }$ and $\gamma _ { \mathrm { s / t d / a d } } ^ { \mathrm { c } , \mathrm { L } }$ are the mean value and scale parameter of the Logistic distribution for static/terrestrial dynamic/aerial dynamic clusters. From Table II and Fig. 3, it can be seen that the observation of static/terrestrial dynamic/aerial dynamic cluster number parameters is similar to that of static/terrestrial dynamic/aerial dynamic scatterer number parameters.

2) Distance Parameters: At present, there is no channel measurement or channel model considering the distinction among distance parameters of static, terrestrial dynamic, and aerial dynamic scatterers/clusters. Based on the constructed MUMV-CSCI dataset, the distance parameters of static, terrestrial dynamic, and aerial dynamic scatterers in multi-UAV-to-multi-vehicle channels are analyzed under high, medium, and low TTD and ATD conditions. The distance parameters from the Txs, i.e., the i-th UAV and the $j -$ th vehicle, to the l/m/n-th static/terrestrial dynamic/aerial dynamic scatterer, i.e., $D _ { \mathrm { S } _ { l } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) , ~ D _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ , and $D _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } }$ are introduced and expressed as $( 6 ) – ( 8 )$ , shown at the bottom of the page, where $\mathbf { S } _ { \mathrm { S } _ { l } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) / \mathbf { S } _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } ^ { \prime } , \mathrm { C } _ { j } } ( t ) / \mathbf { S } _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ is the location of the $l / m / n { \cdot } \mathrm { t h }$ static/terrestrial dynamic/aerial dynamic scatterer in the transmission link between the i-th UAV and the j-th vehicle. k · k denotes the calculation of the Frobenius norm. Moreover, based on the constructed MUMV-CSCI dataset, the distance parameter of each static/terrestrial dynamic/aerial dynamic scatterer is calculated and analyzed. Figs. 4(a)–(c) show the CDFs of distance parameters of static, terrestrial dynamic, and aerial dynamic scatterers under high, medium, and low TTD and ATD conditions, respectively. The CDFs of distance parameters of static, terrestrial dynamic, and aerial dynamic scatterer match well with the Gamma distribution, Rayleigh distribution, and Rayleigh distribution, respectively. The CDFs of the Gamma distribution and the Rayleigh distribution are represented as

$$
F _ { \mathrm { s } } ^ { \mathrm { G } } ( x ) = \frac { \gamma ( \alpha _ { \mathrm { s } } ^ { \mathrm { G } } , \beta _ { \mathrm { s } } ^ { \mathrm { G } } x ) } { \Gamma ( \alpha _ { \mathrm { s } } ^ { \mathrm { G } } ) }\tag{9}
$$

$$
F _ { \mathrm { t d / a d } } ^ { \mathrm { R } } ( x ) = 1 - e ^ { - \frac { x ^ { 2 } } { 2 ( \sigma _ { \mathrm { t d / a d } } ^ { \mathrm { R } } ) ^ { 2 } } }\tag{10}
$$

where $\alpha _ { \mathrm { s } } ^ { \mathrm { G } }$ and $\beta _ { \mathrm { s } } ^ { \mathrm { G } }$ denote the shape parameter and the rate parameter of Gamma distribution. Γ(·) and $\gamma ( \cdot , \cdot )$ denote the Gamma function and the lower incomplete Gamma function. $\sigma _ { \mathrm { t d / a d } } ^ { \mathrm { R } }$ denotes the scale parameter of Rayleigh distribution. As shown in Fig. 4, the distance parameter of dynamic scatterers is smaller than that of static scatterers. This phenomenon is because the static scatterers, i.e., trees and buildings, are farther than dynamic scatterers, i.e., dynamic vehicles and UAVs surrounding the transceiver.

3) Angle Parameters: There is currently no channel measurement or channel model considering the distinction among angle parameters of static, terrestrial dynamic, and aerial dynamic scatterers/clusters. The angle parameters in multi-UAV-to-multi-vehicle channels are for the first time analyzed under high, medium, and low TTD and ATD conditions, including azimuth angle of departure (AAoD), azimuth angle of arrival (AAoA), elevation angle of departure (EAoD), and elevation angle of arrival (EAoA) of static, terrestrial dynamic, aerial dynamic scatterers. AAoD ratios of the $l / m / n$ -th static/terrestrial dynamic/aerial dynamic scatterer in

$$
D _ { \mathbf { S } _ { l } } ^ { \mathbf { U } _ { i } , \mathbf { C } _ { j } } ( t ) = \frac { \| \mathbf { T } ^ { \mathbf { U } _ { i } } ( t ) - \mathbf { S } _ { \mathbf { S } _ { l } } ^ { \mathbf { U } _ { i } , \mathbf { C } _ { j } } ( t ) \| + \| \mathbf { R } ^ { \mathbf { C } _ { j } } ( t ) - \mathbf { S } _ { \mathbf { S } _ { l } } ^ { \mathbf { U } _ { i } , \mathbf { C } _ { j } } ( t ) \| - \| \mathbf { T } ^ { \mathbf { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathbf { C } _ { j } } ( t ) \| } { \| \mathbf { T } ^ { \mathbf { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathbf { C } _ { j } } ( t ) \| }\tag{6}
$$

$$
D _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { S } _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) \Vert + \Vert \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) - \mathbf { S } _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) \Vert - \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert } { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert }\tag{7}
$$

$$
D _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { S } _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) \Vert + \Vert \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) - \mathbf { S } _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) \Vert - \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert } { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert }\tag{8}
$$

![](images/688efab19ef23a38f8ee80d0ecdcab10b942f8994dd13cb42013d4cf0d590487.jpg)  
(a)

![](images/a48531b46fa1fafdfe910187b2e789c9e66ac0e439fccc11b1cf8e4a92adbe98.jpg)  
(b)

![](images/6c9fbbd6d7961ef8db9f47f8bd339d73ee6f5dd99ebc57f61dfbdc83ead40ed5.jpg)  
(c)

Fig. 4. CDFs of static/terrestrial dynamic/aerial dynamic scatterer distance parameters with the Gamma/Rayleigh distribution fitting under different TTD and ATD conditions. Figs. (a)–(c) show the CDFs of distance parameters under high, medium, and low TTD and ATD conditions, respectively.  
![](images/84df6efdf27fe1c5ffe30844274fb59343322285489fc41de6badd135b4adf23.jpg)  
(a)

![](images/151dc6eb46d33e5473479e0af18c59dd5fb995a48a0b05419d2ff5b203b70590.jpg)  
(b)

![](images/c50967e1a265a2f9267689d227dca6ae03cb736836d9c396c8ad101df48b356b.jpg)  
(c)

Fig. 5. CDFs of static/terrestrial dynamic/aerial dynamic scatterer angle parameters, i.e., AAoD, with the Gaussian distribution fitting under different TTD and ATD conditions. Figs. (a)–(c) show the CDFs of angle parameters under high, medium, and low TTD and ATD conditions, respectively.  
![](images/8daf2ff7bd945ef8d91c0296002924566ca586e252341e3b2ff0485c1deb26b3.jpg)  
(a)

![](images/238718a7c4800f489c8caa67451a232e779938398ddbadee8e1d9d35beec0033.jpg)  
(b)

![](images/1a59f56ad12646dab3d43f0da59476cb78205789d912bb4eaf870c5c1b8f659c.jpg)  
(c)  
Fig. 6. CDFs of the ratios of static/terrestrial dynamic/aerial dynamic scatterer power to static/terrestrial dynamic/aerial dynamic scatterer delay with the Exponential expression fitting under different TTD and ATD conditions. Figs. (a)–(c) show the CDFs of power to delay parameters under high, medium, and low TTD and ATD conditions, respectively.

the transmission link from the i-th UAV to the j-th vehicle, $\alpha _ { \mathrm { S } _ { l } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) , \alpha _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ , and $\alpha _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ , are expressed as

$$
\alpha _ { \mathrm { S } _ { l } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { \gamma _ { \mathrm { S } _ { l } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) } { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert }
$$

$$
\alpha _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { \gamma _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) } { \Vert \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \Vert }\tag{11}
$$

$$
\alpha _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) = \frac { \gamma _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) } { \| \mathbf { T } ^ { \mathrm { U } _ { i } } ( t ) - \mathbf { R } ^ { \mathrm { C } _ { j } } ( t ) \| }\tag{12}
$$

(13)

where $\gamma _ { \mathrm { S } _ { l } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) / \gamma _ { \mathrm { T D } _ { m } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t ) / \gamma _ { \mathrm { A D } _ { n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ represents the AAoDs of the $l / m / n { \cdot } { \mathrm { t h } }$ static/terrestrial dynamic/aerial dynamic scatterer in the communication link from the i-th UAV to the j-th vehicle. Moreover, based on the constructed MUMV-CSCI dataset, the AAoDs of each static/terrestrial dynamic/aerial dynamic scatterer in each communication link at each snapshot are calculated and analyzed. Figs. 5(a)–(c) show the CDFs of all AAoDs of static, terrestrial dynamic, and aerial dynamic scatterers under high, medium, and low TTD and ATD conditions, respectively. The CDF of AAoDs matches the Gaussian distribution. The CDF of the Gaussian distribution for AAoDs related to static/terrestrial dynamic/aerial dynamic scatterers is represented by

$$
F _ { \mathrm { s / t d / a d } } ^ { \mathrm { A A o D } } ( x ) = \frac { 1 } { 2 } \left[ 1 + \mathrm { e r f } \left( \frac { x - \mu _ { \mathrm { s / t d / a d } } ^ { \mathrm { A A o D } } } { \sigma _ { \mathrm { s / t d / a d } } ^ { \mathrm { A A o D } } \sqrt { 2 } } \right) \right]\tag{14}
$$

where $\mu _ { \mathrm { s / t d / a d } } ^ { \mathrm { A A o D } }$ and $\sigma _ { \mathrm { s / t d / a d } } ^ { \mathrm { A A o D } }$ denote the mean value and the standard deviation of the Gaussian distribution for AAoDs related to static/terrestrial dynamic/aerial dynamic scatterers. $\mathrm { e r f } \left( { \cdot } \right)$ is the error function. Similarly, the other static/terrestrial dynamic/aerial dynamic scatterer angle parameters, i.e., AAoA $\theta _ { \mathrm { S / T D / A D } _ { l / m / n } } ^ { \check { \mathrm { U } } _ { i } , \mathrm { C } _ { j } } ( \check { t } )$ EAoD $\beta _ { \mathrm { S / T D / A D } _ { l / m / n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ and EAoA $\phi _ { \mathrm { S / T D / A D } _ { l / m / n } } ^ { \mathrm { U } _ { i } , \mathrm { C } _ { j } } ( t )$ are calculated in the same way, which also obey the Gaussian distribution and their corresponding statistical values are given in Table II. Compared with static scatterers, dynamic scatterers have larger variances in angle parameters. This is because that, the position of dynamic scatterers has more significant changes than that of static scatterers. Moreover, aerial dynamic scatterers have larger variances in angle parameters than terrestrial dynamic scatterers. This phenomenon is explained that UAVs have different flight heights, whereas vehicles on the ground are all located on the road at the same height. Furthermore, this phenomenon differs from the conclusions in vehicular communication presented in [28], as the UAV’s height has a significant impact on the distribution of scatterers.

4) Power-Delay Characteristics: The relationship between delay and power in multipath is a key channel characteristic in channel realization. In standardized model [29], the path power is an exponential function of the path delay. The path power is separated into static, terrestrial dynamic, and aerial dynamic path power. The path power through $l / m /$ n-th static/terrestrial dynamic/aerial dynamic scatterer is expressed by

$$
\begin{array} { r } { P _ { \mathrm { S } _ { l } } ( t ) = \exp \left( - \xi _ { \mathrm { s } } \tau _ { \mathrm { S } _ { l } } ( t ) - \eta _ { \mathrm { s } } \right) 1 0 ^ { - \frac { Z _ { \mathrm { s } } } { 1 0 } } } \end{array}\tag{15}
$$

$$
\begin{array} { r } { P _ { \mathrm { T D } _ { m } } ( t ) = \exp \left( - \xi _ { \mathrm { t d } } \tau _ { \mathrm { T D } _ { m } } ( t ) - \eta _ { \mathrm { t d } } \right) 1 0 ^ { - \frac { Z _ { \mathrm { t d } } } { 1 0 } } } \end{array}\tag{16}
$$

$$
\begin{array} { r } { P _ { \mathrm { A D } _ { n } } ( t ) = \exp \left( - \xi _ { \mathrm { a d } } \tau _ { \mathrm { A D } _ { n } } ( t ) - \eta _ { \mathrm { a d } } \right) 1 0 ^ { - \frac { Z _ { \mathrm { a d } } } { 1 0 } } } \end{array}\tag{17}
$$

where $\xi _ { \mathrm { s / t d / a d } }$ and $\eta _ { \mathrm { s / t d / a d } }$ are the delay-related parameters of static/terrestrial dynamic/aerial dynamic scatterers. $\tau _ { \mathrm { S / T D / A D } _ { l / m / n } } ( t )$ is the delay of the path through the $l / m / n { \cdot } { \mathrm { t h } }$ static/terrestrial dynamic/aerial dynamic scatterer. $Z _ { \mathrm { s / t d / a d } }$ follows the Gaussian distribution $\mathcal { N } \left( 0 , \sigma _ { \mathrm { E , s / t d / a d } } ^ { 2 } \right)$ For proper linear fitting, we transform (15), (16), and (17) as

$$
- \mathrm { l n } P _ { \mathrm { S } _ { l } } ( t ) = \xi _ { \mathrm { s } } \tau _ { \mathrm { S } _ { l } } ( t ) + \eta _ { \mathrm { s } } + \frac { \ln 1 0 } { 1 0 } Z _ { \mathrm { s } }\tag{18}
$$

$$
- \mathrm { l n } P _ { \mathrm { T D } _ { m } } ( t ) = \xi _ { \mathrm { t d } } \tau _ { \mathrm { T D } _ { m } } ( t ) + \eta _ { \mathrm { t d } } + \frac { \ln 1 0 } { 1 0 } Z _ { \mathrm { t d } }\tag{19}
$$

$$
- \mathrm { l n } P _ { \mathrm { A D } _ { n } } ( t ) = \xi _ { \mathrm { a d } } \tau _ { \mathrm { A D } _ { n } } ( t ) + \eta _ { \mathrm { a d } } + \frac { \ln { 1 0 } } { 1 0 } Z _ { \mathrm { a d } } .\tag{20}
$$

The power and delay of each path through each static/terrestrial dynamic/aerial dynamic scatterer at each snapshot are calculated and fitted. The fitted parameters are summarized in Table II. Figs. 6(a)–(c) show the fitting results under high, medium, and low TTD and ATD conditions, which can validate the accuracy of the fitted parameters. Compared to static and terrestrial dynamic scatterers, the power of aerial dynamic scatterers is more sensitive to the change of delay, and thus the increase in the delay of aerial dynamic scatterers significantly reduces their power.

![](images/943cf245a19672e9ac33f34870a3c5c3fd99b141ad7f7498034232eca892338e.jpg)  
Fig. 7. Geometry of the proposed channel model for multi-UAV-tomulti-vehicle intelligent sensing-communication integration and effective scatterers/clusters for the transmission links at T1 and T2.

## III. MULTI-MODAL INTELLIGENT CHANNEL MODEL FOR 6G MULTI-UAV-TO-MULTI-VEHICLE COMMUNICATIONS

With the aid of LiDAR point clouds, static, terrestrial dynamic, and aerial dynamic scatterers can be distinguished. Based on the statistical distributions, a novel LiDAR-aided multi-UAV-to-multi-vehicle channel model is proposed, which considers the impact of different TTD and ATD conditions for the first time. Channel non-stationarity and consistency on the time and space domains and channel non-stationarity on the frequency domain are simultaneously depicted.

$$
\begin{array} { l l } { { A . } } & { { F r a m e w o r k \ o f t h e \ P r o p o s e d M u l t i - U A V - t o - M u l t i - V e h i c l e } } \\ { { } } & { { C h a n n e l \ M o d e l } } \end{array}
$$

In the proposed channel model, as shown in Fig. 7, the Txs and the Rxs are I UAVs and J vehicles, which are equipped with mmWave communication devices and LiDAR devices. The integrated CIR of the multi-UAV-to-multi-vehicle channel $H ( t , \tau )$ is represented as

$$
\mathbf { H } ( t , \tau ) = \left[ { \begin{array} { c c c c c } { h _ { 1 , 1 } ( t , \tau ) } & { h _ { 1 , 2 } ( t , \tau ) } & { \cdot \cdot \cdot } & { h _ { 1 , I } ( t , \tau ) } \\ { h _ { 2 , 1 } ( t , \tau ) } & { h _ { 2 , 2 } ( t , \tau ) } & { \cdot \cdot \cdot } & { h _ { 2 , I } ( t , \tau ) } \\ { \vdots } & { \vdots } & { \cdot } & { \vdots } \\ { h _ { J , 1 } ( t , \tau ) } & { h _ { J , 2 } ( t , \tau ) } & { \cdot \cdot \cdot } & { h _ { J , I } ( t , \tau ) } \end{array} } \right]\tag{21}
$$

where the element $h _ { j , i } ( t , \tau )$ , i.e., the CIR of transmission link from the i-th UAV to the j-th vehicle, is obtained by (22), shown at the bottom of the next page.

In (22), $\Omega _ { j i } ( t )$ represents Ricean factor of transmission link from the i-th UAV to the j-th vehicle. $\eta _ { j i } ^ { \mathrm { G R } } ( t )$ and $\eta _ { j i } ^ { \mathrm { N L o S } } ( t )$ are the power ratios of ground reflection component and non-line-of-sight (NLoS) component of transmission link from the i-th UAV to the j-th vehicle, as well as satisfy $\eta _ { j i } ^ { \mathrm { G R } } ( t ) + \eta _ { j i } ^ { \mathrm { N L o S } } ( t ) = 1$

1) For the LoS Component: The line-of-sight (LoS) complex channel gain of transmission link from the i-th UAV to the j-th vehicle can be represented as

$$
h _ { j , i } ^ { \mathrm { L o S } } ( t ) = Q ( t ) \mathrm { e x p } \left[ j 2 \pi \int _ { t _ { 0 } } ^ { t } f _ { j , i } ^ { \mathrm { L o S } } ( t ) \mathrm { d } t + j \varphi _ { j , i } ^ { \mathrm { L o S } } ( t ) \right]\tag{23}
$$

where $Q ( t )$ is a rectangular window function [30]. It is equal to 1 when $t _ { 0 } ~ \leqslant ~ t ~ \leqslant ~ T _ { 0 }$ , otherwise it is equal to 0. The Doppler frequency, phase shift, and delay of LoS component of transmission link from the i-th UAV to the j-th vehicle are obtained by

$$
f _ { j , i } ^ { \mathrm { L o S } } ( t ) = \frac { 1 } { \lambda } \frac { \left. \mathbf { D } _ { j , i } ^ { \mathrm { L o S } } ( t ) , \mathbf { v } ^ { \mathrm { C } _ { j } } ( t ) - \mathbf { v } ^ { \mathrm { U } _ { i } } ( t ) \right. } { \left\| \mathbf { D } _ { j , i } ^ { \mathrm { L o S } } ( t ) \right\| }\tag{24}
$$

$$
\varphi _ { j , i } ^ { \mathrm { L o S } } ( t ) = \varphi _ { 0 } + \frac { 2 \pi } { \lambda } \left\| \mathbf { D } _ { j , i } ^ { \mathrm { L o S } } ( t ) \right\|\tag{25}
$$

$$
\tau _ { j , i } ^ { \mathrm { L o S } } ( t ) = \frac { \| \mathbf { D } _ { j , i } ^ { \mathrm { L o S } } ( t ) \| } { c }\tag{26}
$$

where $\langle \cdot , \cdot \rangle , \varphi _ { 0 }$ , and λ are the inner product, initial phase shift, and carrier wavelength. $\mathbf { v } ^ { \mathrm { U } _ { i } } ( t )$ and $\mathbf { v } ^ { \mathrm { C } _ { j } } ( t )$ are the velocity vectors of the i-th UAV and the j-th vehicle. The distance vector from the i-th UAV to the j-th vehicle $\mathbf { D } _ { \mathit { i } , \mathit { i } } ^ { \mathrm { L o S } } ( t )$ is obtained by $\begin{array} { r } { \mathbf { D } _ { j , i } ^ { \mathrm { L o S } } ( t ) = \mathbf { D } _ { j , i } ^ { \mathrm { L o S } } ( t _ { 0 } ) + \int _ { t _ { 0 } } ^ { t } \mathbf { v } ^ { \mathrm { C } _ { j } } ( t ) \mathrm { d } t - \int _ { t _ { 0 } } ^ { t } \mathbf { v } ^ { \mathrm { U } _ { i } } ( t ) \mathrm { d } t } \end{array}$

2) For the Ground Reflection Component: The complex channel gain of transmission link from the i-th UAV to the j-th vehicle can be represented as

$$
\begin{array} { r l r } {  { h _ { j , i } ^ { \mathrm { G R } } ( t ) } } \\ & { = Q ( t ) \sqrt { P _ { j , i } ^ { \mathrm { G R } } ( t ) } } \\ & { \times } & { \times \exp \biggl \{ j 2 \pi [ \int _ { t _ { 0 } } ^ { t } f _ { j , i } ^ { \mathrm { G R , T } } ( t ) \mathrm { d } t + \int _ { t _ { 0 } } ^ { t } f _ { j , i } ^ { \mathrm { G R , R } } ( t ) \mathrm { d } t ] + j \varphi _ { j , i } ^ { \mathrm { G R } } ( t ) \biggr \} } \end{array}\tag{27}
$$

where $P _ { j , i } ^ { \mathrm { G R } } ( t ) , \ f _ { j , i } ^ { \mathrm { G R , T / R } } ( t ) , \ \varphi _ { j , i } ^ { \mathrm { G R } } ( t )$ , and $\tau _ { j , i } ^ { \mathrm { G R } } ( t )$ denote power, Doppler frequency at the i/j-th UAV/vehicle, phase, and delay of ground reflection component from the i-th UAV to the j-th vehicle, respectively. Considering the limitation of paper length, these parameters can be calculated according to our previous work in [31].

3) For the NLoS Component: The complex channel gain from the i-th UAV to the j-th vehicle via the l-th cluster by the $g _ { l }$ -th scatterer $h _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t )$ is calculated by – if the l-th cluster – if the l-th cluster $\in G _ { j , i } ^ { \mathrm { V R } } ( t )$ (∀o) (Ao)

$$
h _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right)
$$

$$
\begin{array} { l } { { \displaystyle = Q ( t ) \sqrt { P _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) } } } \\ { { \displaystyle \times \exp \bigg \{ j \ 2 \pi \left[ \int _ { t _ { 0 } } ^ { t } f _ { j , i } ^ { \mathrm { T } _ { l , g _ { l } } } ( t ) \mathrm { d } t + \int _ { t _ { 0 } } ^ { t } f _ { j , i } ^ { \mathrm { R } _ { l , g _ { l } } } ( t ) \mathrm { d } t \right] } }  \\ { { \displaystyle \qquad + j \varphi _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \bigg \} } }  \end{array}\tag{28}
$$

– otherwise

$$
h _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right) = 0\tag{29}
$$

where $G _ { j , i } ^ { \mathrm { V R } } ( t )$ is the set of visible twin-cluster in the transmission link from the i-th UAV to the j-th vehicle at time t, which can be obtained in Section III-B. The Doppler frequency at Tx $f _ { j , i } ^ { \mathrm { T } _ { l , g _ { l } } } ( t )$ , the Doppler frequency at Rx $\mathbf { \bar { \rho } } _ { f _ { j , i } } ^ { \mathrm { R } _ { l , g _ { l } } } ( t )$ , the phase shift $\varphi _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right)$ , the delay $\tau _ { j , i } ^ { \mathrm { { N L o S } } _ { l , g _ { l } } } ( t )$ , and the distance $\mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t )$ are obtained by

$$
\begin{array} { r l } & { f _ { j , i } ^ { \mathrm { T } _ { l , g _ { l } } } \left( t \right) } \\ & { = \cfrac { 1 } { \lambda } \frac { \left. \left( \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right) \right) , \mathbf { v } ^ { \mathrm { U } _ { i } } \left( t \right) \right. } { \left\| \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right) \right\| } } \end{array}\tag{30}
$$

$$
\begin{array} { r l } & { f _ { j , i } ^ { \mathrm { R L } , { \boldsymbol \sigma } _ { l } } ( t ) } \\ & { \quad = \displaystyle \frac { 1 } { \lambda } \frac {  \mathbf { D } ( t ) - \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , { \boldsymbol \sigma } _ { l } } } ( t ) , \mathbf { v } ^ { \mathrm { C } _ { j } } ( t )  } { \| \mathbf { D } ( t ) - \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , { \boldsymbol \sigma } _ { l } } } ( t ) \| } ( 3 1 ) } \\ & { \quad \varphi _ { j , i } ^ { \mathrm { N L o S } _ { l , { \boldsymbol \sigma } _ { l } } } ( t ) = \varphi _ { 0 } } \\ & { \quad \quad + \displaystyle \frac { 2 \pi } { \lambda } \| \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , { \boldsymbol \sigma } _ { l } } } ( t ) \| + \| \mathbf { D } ( t ) - \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , { \boldsymbol \sigma } _ { l } } } ( t ) \| + c \tilde { \tau } ^ { \mathrm { S } _ { \boldsymbol \sigma } } ( t ) ] } \end{array}\tag{32}
$$

$$
\begin{array} { r l } & { \tau _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) } \\ & { = \frac { \left[ \left. \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \right. + \left. \mathbf { D } ( t ) - \mathbf { D } _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \right. \right] } { c } + \tilde { \tau } ^ { \mathrm { S } _ { o } } ( t ) } \end{array}\tag{33}
$$

$$
\begin{array} { r l r } & { } & { = D _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \left( \begin{array} { l } { \mathrm { c o s } \alpha _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \mathrm { c o s } \beta _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) } \\ { \mathrm { s i n } \alpha _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \mathrm { c o s } \beta _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) } \\ { \mathrm { s i n } \beta _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) } \end{array} \right) } \end{array}\tag{34}
$$

where $\tilde { \tau } ^ { \mathrm { S } _ { o } } ( t )$ denotes the delay of virtual link in the oth static cluster, which follows the Exponential distribution. The power parameter $P _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right)$ , and the distance parameter $D _ { i , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t )$ , the angle parameters $\alpha _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \left( t \right)$ , and $\beta _ { j , i } ^ { \mathrm { { N L o S } } _ { l , g _ { l } } } ( t )$ are generated according to Table II.

$$
\begin{array} { r l } & { h _ { j , i } ( t , \tau ) = \underbrace { \sqrt { \frac { \Omega _ { j i } ( t ) } { \Omega _ { j i } ( t ) + 1 } } h _ { j , i } ^ { \mathrm { L o S } } ( t ) \delta \left( \tau - \tau _ { j , i } ^ { \mathrm { L o S } } ( t ) \right) } _ { \mathrm { L o S } } + \underbrace { \sqrt { \frac { \eta _ { j i } ^ { \mathrm { G R } } ( t ) } { \Omega ( t ) + 1 } } h _ { j , i } ^ { \mathrm { G R } } ( t ) \delta \left( \tau - \tau _ { j , i } ^ { \mathrm { G R } } ( t ) \right) } _ { \mathrm { G r o u n d R e f l e c t i o n } } } \\ & { \quad + \underbrace { \sum _ { l = 1 } ^ { \mathrm { c l u } } \displaystyle \sum _ { g _ { l l } = 1 } ^ { G ^ { \mathrm { s c a } } ( t ) } \sqrt { \frac { \eta _ { j i } ^ { \mathrm { N L o S } } ( t ) } { \Omega ( t ) + 1 } } h _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \delta \left( \tau - \tau _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \right) } _ { \mathrm { N L o S } } . } \end{array}\tag{22}
$$

## B. Modeling of Channel Appearance and Disappearance in Multi-UAV-to-Multi-Vehicle Channel

The objects, such as buildings, trees, UAVs, and vehicles, always exist. However, the scatterers/clusters are not effective for the transmission link if they are far away from transceivers. Based on the MUMV-CSCI dataset, as the analysis shown in Fig. 7, it is obvious that the scatterers/clusters are not always effective. In the transmission links among different UAVs and vehicles, the sets of effective clusters are different, which results in the non-stationarity of scatterers/clusters on the space domain in the multi-UAV-to-multi-vehicle channel. The appearance and disappearance of scatterers/clusters in the electromagnetic space are smooth as time and space evolve, resulting in the scatterer/cluster consistency on the time and space domains in the multi-UAV-to-multi-vehicle channel.

To accurately and simultaneously model the scatterer/cluster appearance and disappearance on the time and space domains in the multi-UAV-to-multi-vehicle channel, a novel LiDARaided temporal and spatial non-stationarity and consistent algorithm is developed as follows.

Step 1: Initial setup of scatterers in the environment. The parameters of static, terrestrial dynamic, and aerial dynamic scatterers under high, medium, and low TTD and ATD conditions are generated according to Table II. For $\forall i , j$ $( i ~ = ~ 1 , 2 , \ldots , I ; ~ j ~ = ~ 1 , 2 , \ldots , J )$ , the numbers of static, terrestrial dynamic, and aerial dynamic scatterers between the i-th UAV and the j-th vehicle at initial time $t _ { 0 }$ are generated by following the Logistic distribution. The distances at initial time $t _ { 0 }$ are generated by following the Gamma distribution and Rayleigh distribution. The departure and arrival angles of each static, terrestrial dynamic, and aerial dynamic scatterers at initial time $t _ { 0 } ,$ i.e., AAoDs, AAoAs, EAoDs, and EAoAs are generated by following the Gaussian distribution. According to the generated distances and angles of each static, terrestrial dynamic, and aerial dynamic scatterers, the locations of each static, terrestrial dynamic, and aerial dynamic scatterer at initial time $t _ { 0 }$ are obtained.

Step 2: Obtaining all the clusters in the environment at initial time $t _ { 0 } .$ Based on the K-Means clustering algorithm, the generated static, terrestrial dynamic, and aerial dynamic scatterers are respectively clustered as static, terrestrial dynamic, and aerial dynamic clusters.

Step 3: Obtaining the visible clusters for certain transmission links at initial time $t _ { 0 } .$ The visibility regions (VRs) of each UAV/vehicle are assumed as a semi-sphere with the center of the UAV/vehicle. The radii of the VR of the i/j-th UAV/vehicle is $R _ { \mathrm { v r } } ^ { \mathrm { U } _ { i } } / R _ { \mathrm { v r } } ^ { \mathrm { C } _ { j } }$ , which is the maximum value of distances between initial generated static/terrestrial dynamic/aerial dynamic clusters and the i/j-th UAV/vehicle at initial time $t _ { 0 } ,$ , which is determined by Rayleigh distribution in Table II. They are obtained as

$$
R _ { \mathrm { v r } } ^ { \mathrm { U } _ { i } } = \operatorname* { m a x } _ { \forall o , q } \left\{ \left\| \mathbf { D } _ { \mathrm { U } _ { i } } ^ { \mathrm { S } _ { o } } ( t _ { 0 } ) \right\| , \left\| \mathbf { D } _ { \mathrm { U } _ { i } } ^ { \mathrm { A D } _ { q } } ( t _ { 0 } ) \right\| \right\}\tag{35}
$$

$$
R _ { \mathrm { v r } } ^ { \mathrm { C } _ { j } } = \operatorname* { m a x } _ { \forall o , p } \left\{ \left\| \mathbf { D } _ { \mathrm { C } _ { j } } ^ { \mathrm { S } _ { o } } ( t _ { 0 } ) \right\| , \left\| \mathbf { D } _ { \mathrm { C } _ { j } } ^ { \mathrm { T D } _ { p } } ( t _ { 0 } ) \right\| \right\}\tag{36}
$$

where $\mathbf { D } _ { \mathrm { U } _ { i } / \mathrm { C } _ { j } } ^ { \mathrm { S } _ { o } } ( t _ { 0 } ) / \mathbf { D } _ { \mathrm { U } _ { i } / \mathrm { C } _ { j } } ^ { \mathrm { T D } _ { p } } ( t _ { 0 } ) / \mathbf { D } _ { \mathrm { U } _ { i } / \mathrm { C } _ { j } } ^ { \mathrm { T D } _ { p } } ( t _ { 0 } )$ are the distance between the $o / p / q \cdot$ -th static/terrestrial dynamic/aerial dynamic cluster and the $i / j { \cdot } \mathrm { t h }$ UAV/vehicle at initial time $t _ { 0 } .$ The cluster in the VRs of the $i / j { \cdot } \mathrm { t h }$ UAV/vehicle at time t, i.e., $R _ { \mathrm { v r } } ^ { \mathrm { U } _ { i } } / R _ { \mathrm { v r } } ^ { \mathrm { C } _ { j } }$ is the visible cluster for the $i / j { \cdot } \mathrm { t h }$ UAV/vehicle at time t. In this case, as the movement of UAVs and vehicles in the environment, the clusters are not always in the VRs of certain transceivers, which can mimic the cluster appearance and disappearance in the time domain. As each transceiver, i.e., UAV/vehicle, has its own location and VR, different transmission links have different visible clusters, which can mimic the cluster appearance and disappearance in the space domain. Meanwhile, the VRs of UAVs and vehicles move as time evolves and share an integrated and consistent environment, leading to channel consistency in the time and space domains. The visible cluster not limited to a single transmission link and can be shared across multiple links while affecting different links.

Step 4: Obtaining the visible clusters for certain transmission links at time $\scriptstyle t = t _ { 0 } + \Delta \ t ,$ including survived clusters and newly generated clusters. If the movement of clusters is still in the VRs of transceivers at time $t _ { 0 } + \Delta t .$ , i.e., the distance between cluster and transceiver at time $t _ { 0 } + \Delta t$ is still shorter than the radii of the VRs. The number of survived static/terrestrial dynamic/aerial dynamic clusters for the transmission between the i-th UAV and j-th vehicle at time $t _ { 0 } + \Delta t ,$ i.e., visible static/terrestrial dynamic/aerial dynamic clusters at time $t _ { 0 }$ that are still visible at time $t _ { 0 } + \Delta t ,$ is denoted as $M _ { \mathrm { s } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t )$ In addition to the survival clusters, there are some newly generated clusters for the transmission between the i-th UAV and the j-th vehicle at time $t _ { 0 } + \Delta t$ . For a certain distance between the i-th UAV and the j-th vehicle at time $t _ { 0 } + \Delta t$ , the number parameter $M _ { \mathrm { s } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t )$ related to static/terrestrial dynamic/aerial dynamic clusters is randomly generated by obeying the Logistic distribution in Table II. If the value $M _ { \mathrm { s } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t )$ is greater than the number of survived clusters at time $t _ { 0 } + \Delta t$ i.e., $M _ { \mathrm { s } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t )$ , the number of newly generated static/terrestrial dynamic/aerial dynamic clusters is given by

$$
M _ { \mathrm { s / t d / a d } } ^ { \mathrm { n e w } } ( t ) = M _ { \mathrm { s / t d / a d } } ^ { \mathrm { L } } ( t ) - M _ { \mathrm { s / t d / a d } } ^ { \mathrm { S } } ( t ) .\tag{37}
$$

In this case, there are totally $M _ { \mathrm { s } } ^ { \mathrm { L } } ( t _ { 0 } \ + \ \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { L } } ( t _ { 0 } \ +$ $\Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t )$ static/terrestrial dynamic/aerial dynamic clusters that contribute to channel realization. On the contrary, if $M _ { \mathrm { s } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { L } } ( t _ { 0 } + \Delta t )$ is less than $\begin{array} { r } { M _ { \mathrm { s } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { a d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) } \end{array}$ , the number of newly generated clusters is equal to zero, i.e., $M _ { \mathrm { s / t d / a d } } ^ { \mathrm { n e w } } ( t ) = 0$ . In this case, there are $M _ { \mathrm { s } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t ) / M _ { \mathrm { t d } } ^ { \mathrm { S } } ( t _ { 0 } + \dot { \Delta t } ) / M _ { \mathrm { a d } } ^ { \mathrm { S } } ( t _ { 0 } + \Delta t )$ static/terrestrial dynamic/aerial clusters that contribute to channel realization. It is noteworthy that in this mechanism, the logistic clusters represent the expected number of clusters at the current time step, the survived clusters are those retained from the previous time step due to their presence in the visible regions, and the new clusters are generated only when the number of survived clusters is insufficient to meet the expected value given by the logistic distribution. This joint mechanism adequately captures the dynamic evolution of clusters in complex low-altitude UAV scenarios and achieves a balance between modeling accuracy and computational overhead. In addition, it prevents the continuous reduction of clusters that can otherwise lead to the loss of multipath components.

Step 5: Randomly matching the mixed twin-clusters. The visible static and aerial dynamic clusters for the transmission link from the i-th UAV to the j-th vehicle at time $t _ { 0 } + \Delta t$ are the sub-cluster around Tx, i.e., the i-th UAV, and the visible static and terrestrial dynamic clusters for the transmission link from the i-th UAV to the j-th vehicle at time $t _ { 0 } + \Delta t$ are the sub-cluster around Rx, i.e., the j-th vehicle. The sub-cluster around the i-th UAV to the j-th vehicle is matched randomly as the set of visible twin-cluster in the transmission link from the i-th UAV to the j-th vehicle at time $t _ { 0 } + \Delta t , \mathrm { i . e . , } G _ { i . i } ^ { \mathrm { V R } } ( t _ { 0 } { + } \Delta t )$

Step 6: Modeling the channel non-stationarity on the frequency domain. The CIR of transmission link from the ith UAV to the j-th vehicle at time $t = t _ { 0 } + \Delta t , \mathrm { i . e . , } h _ { j , i } ( t , \tau )$ is obtained by (22). The Fourier transform of $h _ { j , i } ( t , \tau )$ in respect of τ , i.e., the time-varying transfer function $H _ { j , i } ^ { \prime } ( t , f )$ is calculated, which is expressed as

$$
H _ { j , i } ^ { \prime } ( t , f ) = \int _ { - \infty } ^ { \infty } h ( t , \tau ) \mathrm { e x p } \left( - j 2 \pi f \tau \right) \mathrm { d } \tau .\tag{38}
$$

Considering the frequency-dependent factor $\left( \frac { f } { f _ { c } } \right) ^ { \chi }$ , the timevarying transfer function is calculated by (39), shwon at the bottom of the page, where χ is the frequency-dependent parameter [32].

Cycling Step 4–Step 6 by t=t+∆ t.

## IV. CHANNEL STATISTICAL PROPERTIES

In this section, the key statistical properties for the proposed multi-UAV-to-multi-vehicle channel model are obtained, including the TSF-CF, TSI, and DPSD.

## A. Time-Space-Frequency Correlation Function

The TSF-CF of the transmission from the i-th UAV to the j-th vehicle on the ground can be calculated as [33]

$$
R _ { j i , j ^ { \prime } i ^ { \prime } } ( t , f ; \Delta t , \Delta f ) = \mathbb { E } [ h _ { j i } ^ { * } ( t , f ) h _ { j ^ { \prime } i ^ { \prime } } ( t + \Delta t , f + \Delta f ) ]
$$

where <sup>E</sup>[·] and $( \cdot ) ^ { * }$ denote the expectation operation and complex conjugate operation, respectively. Since the TSF-CFs of LoS component, ground reflection component, and NLoS component can be assumed as independent of each

(40)

other, the TSF-CF can be further obtained by the sum of the TSF-CFs of LoS component, ground reflection component, and NLoS component, i.e., (41), shown at the bottom of the page, where the correlation of LoS component, ground reflection component, and NLoS component can be computed as (42)–(44), shown at the bottom of the next page.

For a certain UAV, the TSF-CFs can be simplified to the cooperative space cross-correlation function (CCF) between different vehicles by setting $i = i ^ { \prime } , j \neq j ^ { \prime } , \Delta t = 0 ,$ , and $\Delta f = 0$ . For a certain vehicle, the TSF-CFs can be simplified to the space CCF between different UAVs by setting $j = j ^ { \prime } ,$ $i \neq i ^ { \prime } , \Delta t = 0$ , and $\Delta f = 0$ . The TSF-CF can be simplified to the time auto-correlation function (ACF) by setting $i = i ^ { \prime } , j =$ $j ^ { \prime } ,$ and $\Delta f = 0$ . Furthermore, the TSF-CF can be simplified to the frequency correlation function (FCF) by setting $i = i ^ { \prime } ,$ $j = j ^ { \prime }$ , and $\Delta t = 0$

## B. Time Stationary Interval

If the absolute value of the relative error of the delay spread is not more than 10%, the CIR can be regarded as stationary [34]. In this case, the corresponding minimum time interval of stationary CIR is TSI. The TSI of the proposed multi-UAVto-multi-vehicle channel model is obtained by

$$
\begin{array} { r } { T _ { s } ( t ) = \operatorname* { i n f } \left\{ \Delta t \big | _ { \frac { \left\| A _ { \tau ^ { \prime } } ^ { ( 2 ) } ( t + \Delta t ) - A _ { \tau ^ { \prime } } ^ { ( 2 ) } ( t ) \right\| } { A _ { \tau ^ { \prime } } ^ { ( 2 ) } ( t ) } \leq 0 . 1 } \right\} } \end{array}\tag{45}
$$

where inf{·} is the infimum of a certain function. $A _ { \tau ^ { \prime } } ^ { ( 2 ) } ( t )$ denotes the time-variant delay spread and can be obtained by (46), shown at the bottom of the next page.

In 46, $c _ { j i , l , g _ { l } }$ is the path gain of the g<sub>l</sub>-th ray in the l-th twin-cluster between the i-th UAV and the j-th vehicle.

## C. Doppler Power Spectral Density

Based on the Fourier transform of the time ACF, the DPSD can be obtained by

$$
\Upsilon ( t ; f _ { \mathrm { { D } } } ) = \int _ { - \infty } ^ { + \infty } \zeta ( t ; \Delta t ) e ^ { - j 2 \pi f _ { \mathrm { { D } } } \Delta t } \mathrm { d } ( \Delta t )\tag{47}
$$

where $f _ { \mathrm { D } }$ and $\zeta ( t ; \Delta t )$ denote the Doppler frequency and time ACF. The time-varying DPSD illustrates the time-varying characteristic of the proposed channel.

$$
\begin{array} { r l } & { H _ { j , i } ( t , f ) = \underbrace { \sqrt { \displaystyle { \frac { \Omega ( t ) } { \Omega ( t ) + 1 } } h _ { j , i } ^ { \mathrm { L o S } } ( t ) \exp \left[ - j 2 \pi f \tau _ { j , i } ^ { \mathrm { L o S } } ( t ) \right] } } _ { \mathrm { L o S } } + \underbrace { \sqrt { \frac { \eta ^ { \mathrm { G R } } ( t ) } { \Omega ( t ) + 1 } } \left( \frac { f } { f _ { c } } \right) ^ { \chi } h _ { j , i } ^ { \mathrm { G R } } ( t ) \exp \left[ - j 2 \pi f \tau _ { j , i } ^ { \mathrm { G R } } ( t ) \right] } _ { \mathrm { G r o u n d M e f l e c t i o n } } } \\ & { \quad + \underbrace { \sqrt { \displaystyle { \frac { \eta ^ { \mathrm { N L o S } } ( t ) } { \Omega ( t ) + 1 } } \left( \frac { f } { f _ { c } } \right) ^ { \chi } \sum _ { l = 1 } ^ { G ^ { \mathrm { c l u } } ( t ) } \sum _ { g _ { l } = 1 } ^ { G ^ { \mathrm { s e a } } } h _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } ( t ) \exp \left[ - j 2 \pi f \tau _ { j , i } ^ { \mathrm { N L o S } _ { l , g _ { l } } } \right] } } _ { \mathrm { N L o S } } } \end{array}\tag{39}
$$

$$
R _ { j i , j ^ { \prime } i ^ { \prime } } ( t , f ; \Delta t , \Delta f ) = R _ { j i , j ^ { \prime } i ^ { \prime } } ^ { \mathrm { { L o S } } } ( t , f ; \Delta t , \Delta f ) + R _ { j i , j ^ { \prime } i ^ { \prime } } ^ { \mathrm { { G R } } } ( t , f ; \Delta t , \Delta f ) + R _ { j i , j ^ { \prime } i ^ { \prime } } ^ { \mathrm { { N L o S } } } ( t , f ; \Delta t , \Delta f )\tag{41}
$$

![](images/2dc39ad5f73ea70ee7577a1c9963e15d7c6c17e23f5bea91865349e37cf8e792.jpg)  
Fig. 8. Time ACFs under different TTD and ATD conditions and different time instants.

## V. SIMULATION RESULTS AND ANALYSIS

The key statistical properties of the channels are simulated and compared with precise RT-based results. Carrier frequency is $f _ { \mathrm { c } } = 2 8$ GHz and the bandwidth is 2 GHz. The azimuth and elevation angles of the Tx and Rx are $\phi _ { \mathrm { T } } ^ { \mathrm { E } } = \phi _ { \mathrm { R } } ^ { \mathrm { E } } = \pi / 4$ $\theta _ { \mathrm { T } } ^ { \mathrm { A } } \ = \ \pi / 3$ , and $\theta _ { \mathrm { R } } ^ { \mathrm { A } } \ = \ 3 \pi / 4$ . Delays of virtual links $\tau _ { i } ( t )$ and $\tau _ { j } ( t )$ obey the Exponential distribution with the mean and variance 80 ns and 15 ns to imitate the complex transmission between twin-clusters. The environment-dependent factor is set to $\chi = 1 . 3 5 ~ [ 3 2 ]$ . The aforementioned parameters remain unchanged unless otherwise stated.

Fig. 8 shows the absolute normalized time ACFs under low, medium, and high TTD and ATD conditions, at $t = 0 ~ \mathrm { s }$ and $t = 2 \mathrm { ~ s ~ }$ . From Fig. 8, time ACFs depend on time instants and time separations. Meanwhile, time non-stationarity is depicted.

![](images/dd11b1cfa7879c73843c291c98fcaf743c5b6bc6e867709a7c19c4576bc5532f.jpg)  
Fig. 9. Comparison of simulated DPSDs and RT-based DPSDs under different TTD and ATD conditions.

In addition, the time ACF decreases as the TTD and ATD increase. This is because that, as the number of vehicles and UAVs increases, the channel becomes more variable and the temporal correlation decreases.

We obtain RT-based CIRs collected in Wireless InSite with the scenario shown in Fig. 1. As shown in Fig. 9, DPSD is derived based on the CIR data under the high TTD and ATD conditions and is further compared with the simulated DPSD in high, medium, and low TTD and ATD conditions. In Fig. 9, in high TTD and ATD conditions, the RT-based DPSD is much closer to the simulated DPSD. The DPSD is flatter in high and medium TTD and ATD conditions compared to low TTD and ATD conditions. Since UAVs and vehicles are denser and channels are more complex in high TTD and ATD conditions. Therefore, the comparison of different TTD and

(42)

$$
\begin{array} { r l } & { R _ { j _ { i } , j _ { i } ^ { \mathrm { o S } } \prime ^ { \prime \prime } } ^ { \mathrm { L o S } } ( t , f ; \Delta t , \Delta f ) = \sqrt { \frac { \Omega _ { j i } ( t ) } { \Omega _ { j i } ( t ) + 1 } + \frac { \Omega _ { j ^ { \prime \prime } } ( t + \Delta t ) } { \Omega _ { j ^ { \prime \prime } } ( t + \Delta t ) + 1 } } h _ { j _ { i } , i } ^ { \mathrm { L o S } } ( t ) h _ { j _ { i } ^ { \prime \prime } , i ^ { \prime \prime } } ^ { \mathrm { L o S } } ( t + \Delta t ) e ^ { j _ { 2 } \pi \left( f _ { j _ { i } ^ { \prime \prime } , i } ^ { \mathrm { r o S } } ( t ) - ( f + \Delta f ) \tau _ { j _ { i } ^ { \prime \prime } , i ^ { \prime \prime } } ^ { \mathrm { C S } } ( t + \Delta t ) \right) } } \\ & { R _ { j _ { i } , j ^ { \prime \prime \prime } } ^ { \mathrm { G R } } ( t , f ; \Delta t , \Delta f ) = \sqrt { \frac { \eta _ { j i } ^ { \mathrm { G R } } ( t ) } { \Omega _ { j i } ( t ) + 1 } - \frac { \eta _ { j ^ { \prime \prime } , i ^ { \prime \prime } } ^ { \mathrm { G R } } ( t + \Delta t ) } { \Omega _ { j ^ { \prime \prime } , i ^ { \prime \prime } } ( t + \Delta t ) + 1 } } h _ { j _ { i } , i } ^ { \mathrm { G R } } ( t ) h _ { j _ { i } ^ { \prime \prime \prime } , i ^ { \prime } } ^ { \mathrm { G R } } ( t + \Delta t ) e ^ { j _ { 2 } \pi \left( f _ { j _ { i } ^ { \prime \prime } , i ^ { \prime } } ^ { \mathrm { G R } } ( t ) - ( f + \Delta f ) \tau _ { j ^ { \prime \prime } , i ^ { \prime \prime } } ^ { \mathrm { G R } } ( t + \Delta t ) \right) } } \\ &  R _ { j _ { i } , j ^ { \prime \prime \prime } } ^ { \mathrm { N L S } } ( t , f ; \Delta t , \Delta f ) = \sqrt  \frac  \eta _ \end{array}\tag{43}
$$

(44)

$$
\begin{array} { r l } & { A _ { \tau ^ { \prime \prime } } ^ { ( 2 ) } ( t ) = } \\ &  \sqrt  \frac { \sum _ { j = 1 } ^ { J } \sum _ { i = 1 } ^ { I } \sum _ { l = 1 } ^ { G ^ { \mathrm { r i a t } } ( t ) } \sum _ { g = 1 } ^ { G ^ { \mathrm { e s o } ( t ) } ( c _ { j , i , g , \ell } ( l ) ) ^ { 2 } ( \tau _ { j , i } ^ { \mathrm { N . o s . s . } _ { u } } ( l ) ) ^ { 2 } } - \left( \frac { \sum _ { j = 1 } ^ { J } \sum _ { i = 1 } ^ { I } \sum _ { l = 1 } ^ { G ^ { \mathrm { e s o } ( t ) } } ( t ) \sum _ { g = 1 } ^ { G ^ { \mathrm { e s o } ( t ) } ( c _ { j , i , g , \ell } ( l ) ) ^ { 2 } \tau _ { j , i } ^ { \mathrm { N . o s . s . } _ { u } } ( \ell ) } { \sum _ { j = 1 } ^ { J } \sum _ { i = 1 } ^ { I } \sum _ { g = 1 } ^ { G ^ { \mathrm { e s o } ( t ) } } ( c _ { j , i , g , \ell } ( t ) ) ^ { 2 } }  ^ { 2 } } . } \end{\right)array} \end{array}\tag{46}
$$

![](images/3ce8b99e130d111dd957790cf167be9b337e87b6beadd0e0dd02ebb43d598336.jpg)  
Fig. 10. CDFs of TSIs under different TTD and ATD conditions.

ATD conditions is significant for the proposed multi-UAV-tomulti-vehicle channel model.

Fig. 10 presents the CDFs of channel TSIs under different TTD and ATD conditions. In Fig. 10, the TSI of the multi-UAV-to-multi-vehicle channel decreases as TTD and ATD conditions increase. This is attributable to the fact that more UAVs and vehicles lead to a more complex multi-UAV-to-multi-vehicle channel. Therefore, the multi-UAV-to-multi-vehicle channel under high TTD and ATD conditions is more sophisticated and more variable, which results in a lower TSI.

The proposed model integrates communication information and sensing data, i.e., LiDAR data, and improves the accuracy of scatterer class differentiation. The accuracy of the proposed model is seen to be high through the simulation results and different TTD and ATD affect the channel characteristics differently. Therefore, suitable channel parameters can be selected according to different environmental conditions for multi-UAV-to-multi-vehicle scenario. Moreover, in the future work, more refined partitioning strategies will be considered, such as independently varying TTD or ATD, to enable a more in-depth analysis of the respective impacts on the communication channels.

## VI. CONCLUSION

This paper has proposed a novel multi-modal intelligent channel model for 6G multi-UAV-to-multi-vehicle communications. The proposed model has incorporated both TTD and ATD, which can capture channel non-stationarity and the consistent nature of the channel on time, space, and frequency domains. A new MUMV-CSCI dataset, including channel information and LiDAR point clouds, has been constructed to parameterize the proposed model under different TTD and ATD conditions. The proposed model has accurately characterized static scatterers, terrestrial dynamic scatterers, and aerial dynamic scatterer and utilized statistical distributions to describe the properties. Simulation results, validated against the RT-based data, have demonstrated the model’s ability to capture key channel statistics and its suitability for future

6G low-altitude transportation communication systems. In the future, we will leverage both real-world data and RT-based data to enhance and validate the accuracy of the proposed model.

## ACKNOWLEDGMENT

The authors would like to thank Xuanyu Liu and Xu Wang for their help in the collection of LiDAR point clouds in AirSim simulation platform.

## REFERENCES

[1] C. Huang, C.-X. Wang, Z. Li, Z. Qian, J. Li, and Y. Miao, “A frequency domain predictive channel model for 6G wireless MIMO communications based on deep learning,” IEEE Trans. Commun., vol. 72, no. 8, pp. 4887–4902, Aug. 2024.

[2] Z. Li et al., “A GAN-GRU based space-time predictive channel model for 6G wireless communications,” IEEE Trans. Veh. Technol., vol. 73, no. 7, pp. 9370–9386, Jul. 2024.

[3] T. S. Rappaport, Wireless Communications: Principles and Practice. Cambridge, U.K.: Cambridge Univ. Press, 2024.

[4] C. Ge, R. Zhang, Y. Yang, Y. Jiang, and B. Li, “Clutter loss of lowaltitude UAV channel in suburban scenario at 5.8 GHz,” IEEE Antennas Wireless Propag. Lett., vol. 21, no. 4, pp. 651–655, Apr. 2022.

[5] Z. Cui, C. Briso-Rodr´ıguez, K. Guan, C. Calvo-Ram´ırez, B. Ai, and Z. Zhong, “Measurement-based modeling and analysis of UAV airground channels at 1 and 4 GHz,” IEEE Antennas Wireless Propag. Lett., vol. 18, no. 9, pp. 1804–1808, Sep. 2019.

[6] Z. Cui et al., “Low-altitude UAV air-ground propagation channel measurement and analysis in a suburban environment at 3.9 GHz,” IET Microw., Antennas Propag., vol. 13, no. 9, pp. 1503–1508, Apr. 2019.

[7] X. Cai et al., “Empirical low-altitude air-to-ground spatial channel characterization for cellular networks connectivity,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2975–2991, Oct. 2021.

[8] X. Cai et al., “An empirical air-to-ground channel model based on passive measurements in LTE,” IEEE Trans. Veh. Technol., vol. 68, no. 2, pp. 1140–1154, Feb. 2019.

[9] Y. Chen, Y. Li, C. Han, Z. Yu, and G. Wang, “Channel measurement and ray-tracing-statistical hybrid modeling for low-terahertz indoor communications,” IEEE Trans. Wireless Commun., vol. 20, no. 12, pp. 8163–8176, Dec. 2021.

[10] Q. Hu, Y. Cai, A. Liu, G. Yu, and G. Y. Li, “Low-complexity joint resource allocation and trajectory design for UAV-aided relay networks with the segmented ray-tracing channel model,” IEEE Trans. Wireless Commun., vol. 19, no. 9, pp. 6179–6195, Sep. 2020.

[11] H. Jiang, Z. Zhang, L. Wu, and J. Dang, “Three-dimensional geometry-based UAV-MIMO channel modeling for A2G communication environments,” IEEE Commun. Lett., vol. 22, no. 7, pp. 1438–1441, Jul. 2018.

[12] H. Jiang, Z. Zhang, and G. Gui, “Three-dimensional non-stationary wideband geometry-based UAV channel model for A2G communication environments,” IEEE Access, vol. 7, pp. 26116–26122, 2019.

[13] H. Chang et al., “A novel nonstationary 6G UAV-to-ground wireless channel model with 3-D arbitrary trajectory changes,” IEEE Internet Things J., vol. 8, no. 12, pp. 9865–9877, Jun. 2021.

[14] L. Bai, Z. Huang, L. Cui, and X. Cheng, “A non-stationary multi-UAV cooperative channel model for 6G massive MIMO mmWave communications,” IEEE Trans. Wireless Commun., vol. 22, no. 12, pp. 9233–9247, Dec. 2023.

[15] Y. Liu, C.-X. Wang, H. Chang, Y. He, and J. Bian, “A novel nonstationary 6G UAV channel model for maritime communications,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2992–3005, Oct. 2021.

[16] X. Cheng et al., “Intelligent multi-modal sensing-communication integration: Synesthesia of machines,” IEEE Commun. Surveys Tuts., vol. 26, no. 1, pp. 258–301, 1st Quart., 2024.

[17] Y. Chen, H. Hua, J. Xu, and D. W. K. Ng, “ISAC meets SWIPT: Multi-functional wireless systems integrating sensing, communication, and powering,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 8264–8280, Aug. 2024.

[18] L. Bai, Z. Huang, M. Sun, X. Cheng, and L. Cui, “Multi-modal intelligent channel modeling: A new modeling paradigm via synesthesia of machines,” IEEE Commun. Surveys Tuts., early access, Apr. 2025, doi: 10.1109/COMST.2025.3558046.

[19] L. Bai, Z. Huang, T. Feng, and X. Cheng, “A non-stationary channel model for 6G multi-UAV cooperative communication,” IEEE Trans. Wireless Commun., vol. 23, no. 2, pp. 949–961, Feb. 2024.

[20] S. Shah, D. Dey, C. Lovett, and A. Kapoor, “AirSim: High-fidelity visual and physical simulation for autonomous vehicles,” in Field and Service Robotics, M. Hutter and R. Siegwart, Eds., Cham, Switzerland: Springer, Nov. 2017, pp. 621–635.

[21] Remcom. (Jan. 2017). Wireless InSite. Accessed: Mar. 2022. [Online]. Available: https://www.remcom.com/wireless-insite-em-propagationsoftware

[22] X. Cheng et al., “M<sup>3</sup>SC: A generic dataset for mixed multi-modal (MMM) sensing and communication integration,” China Commun., vol. 20, no. 11, pp. 13–29, Nov. 2023.

[23] E. Schubert, J. Sander, M. Ester, H. P. Kriegel, and X. Xu, “DBSCAN revisited, revisited: Why and how you should (still) use DBSCAN,” ACM Trans. Database Syst., vol. 42, no. 3, pp. 1–21, Sep. 2017.

[24] V. Nurmela et al., METIS Channel Models, METIS, New York, NY, USA, document ICT-317669-METIS/D1.4, Jul. 2015.

[25] Preliminary Draft New Report ITU-R M.[IMT-2020.EVAL], Int. Telecommun. Union, Niagara Falls, ON, Canada, document R15-WP5D-170613-TD-0332, Jun. 2017.

[26] Measurement Results and Final mmMAGIC Channel Models, mmMAGIC, document H2020-ICT-671650-mmMAGIC/D2.2, Dec. 2017.

[27] S. Jaeckel, L. Raschkowski, K. Borner, and L. Thiele, “QuaDRiGa-quasi deterministic radio channel generator, user manual and documentation,” Fraunhofer Heinrich Hertz Institute, Tech. Rep. v2.0.0, v2.0.0, Aug. 2017. [Online]. Available: https://quadriga-channelmodel.de/wpcontent/ uploads/2017/08/quadriga documentation v2.0.0-664.pdf

[28] Z. Huang, L. Bai, M. Sun, and X. Cheng, “A LiDAR-aided channel model for vehicular intelligent sensing-communication integration,” IEEE Trans. Intell. Transp. Syst., vol. 25, no. 12, pp. 20105–20119, Dec. 2024.

[29] P. Kyostiet et al.. (Sep. 2007). WINNER II Channel Models, Version 1.1. [Online]. Available: http://www.ist-winner.org/WINNER2-Deliverables/ D1.1.2v1.1.pdf

[30] C. A. Gutierrez, M. Patzold, W. Dahech, and N. Youssef, “A non-WSSUS mobile-to-mobile channel model assuming velocity variations of the mobile stations,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), San Francisco, CA, USA, Mar. 2017, pp. 1–6.

[31] L. Bai, Z. Huang, and X. Cheng, “A non-stationary model with timespace consistency for 6G massive MIMO mmWave UAV channels,” IEEE Trans. Wireless Commun., vol. 22, no. 3, pp. 2048–2064, Mar. 2023.

[32] A. F. Molisch, “A comprehensive model for ultrawideband propagation channels,” in Proc. IEEE Global Telecommun. Conf., St. Louis, MO, USA, Nov./Dec. 2005, pp. 3648–3653.

[33] M. Patzold, Mobile Radio Channels, 2nd ed. West Sussex, U.K.: Wiley, 2012.

[34] M. Patzold and C. A. Gutierrez, “Definition and analysis of quasistationary intervals of mobile radio channels-invited paper,” in Proc. IEEE 87th Veh. Technol. Conf. (VTC Spring), Porto, Portugal, Jun. 2018, pp. 1–6.

![](images/fe60d7075bf852e103254006a7020f6def895160cc087ae01aef25b6fa2c1130.jpg)

Lu Bai (Senior Member, IEEE) received the Ph.D. degree in information and communication engineering from Shandong University, China in 2019. From 2017 to 2019, she was a Visiting Ph.D. Student with Heriot-Watt University, U.K. From 2019 to 2022, she was a Post-Doctoral Researcher with Beihang University, China. She is currently a Professor with Shandong University. Her general research interests are in areas of wireless communications and artificial intelligence, subject on which she has published more than 50 journal and conference papers, two books, holds eight patents, and participated in formulating seven Chinese standards. She has served as the member of the Technical Program Committee and the session chair for several international conferences. She is a member of IEEE P1944 Standard Group. She has received the IEEE VR Best Paper Award, Science and Technology Progress Award of China Transport and Logistics Association, and Taishan Scholar Award. She was a recipient of the Young Elite Scientist Sponsorship Program by China Association for Science and Technology. She is currently an Associate Editor of IET Communications.

![](images/5ddf9100aaf6c2e71c1772bf7db62cf42235bd75b158ba5e3830d885bcefdde9.jpg)

Mengyuan Lu received the B.S. degree in engineering from the School of Software, Shandong University, China in 2024, where she is currently pursuing the master’s degree. Her research interests include AI-based 6G vehicular communications.

![](images/2ad8eda40644edafd547ec1570f95b7265b0a718a07ca1ea20fb39cb11571579.jpg)

Ziwei Huang (Member, IEEE) received the Ph.D. degree in information and communication engineering from Peking University, Beijing, China, in 2024. He is currently a Boya Post-Doctoral Fellow with Peking University. His general research interests are in areas of wireless communications and artificial intelligence, subject on which he has published more than 40 journal and conference papers and two books. He has served as the member of the Technical Program Committee and the session chair for several international conferences. He was a recipient of

China National Postdoctoral Program for Innovative Talents. He was a corecipient of the IET Communications Best Paper Award: Premium Award and was honored with the Doctoral Dissertation Incentive Program by China Institute of Communications (CIC).

![](images/eacfaa1cf6c5d8ad5870e693aed04402fedcd0c445646594e0a38916fbc1d55e.jpg)

Xiang Cheng (Fellow, IEEE) received the joint Ph.D. degree from Heriot-Watt University and The University of Edinburgh, Edinburgh, U.K., in 2009. He is currently a Boya Distinguished Professor with Peking University. He led the establishment of four Chinese standards (including industry standards and group standards) and participated in the formulation of ten 3GPP international standards and two Chinese industry standards. His research focuses on the indepth integration of communication networks and artificial intelligence, including intelligent commu-

nication networks and connected intelligence, the subject on which he has published more than 280 journals and conference papers, 11 books, and holds 35 patents. He was a recipient of the IEEE Asia-Pacific Outstanding Young Researcher Award in 2015 and the Xplorer Prize in 2023. He was a co-recipient of the 2021 IET Communications Best Paper Award: Premium Award and the 2016 IEEE Journal on Selected Areas in Communications Best Paper Award: Leonard G. Abraham Prize. He has also received the Best Paper Awards from IEEE ITST’12, ICCC’13, ITSC’14, ICC’16, ICNC’17, GLOBECOM’18, ICCS’18, and ICC’19. He has been a Highly Cited Chinese Researcher since 2020. In 2021 and 2023, he was selected into two world scientist lists, including the World’s Top 2% Scientists released by Stanford University and top computer science scientists released by Guide2Research. He has served as the symposium lead chair, the co-chair, and a member of the technical program committee for several international conferences. He is currently a Subject Editor of IET Communications and an Associate Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANS-ACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, IEEE WIRELESS COMMUNICATIONS LETTERS, and Journal of Communications and Information Networks. He was a Distinguished Lecturer of the IEEE Vehicular Technology Society.