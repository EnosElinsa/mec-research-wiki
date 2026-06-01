# Placement Optimization of UAV-Mounted Mobile Base Stations

Jiangbin Lyu, Member, IEEE, Yong Zeng, Member, IEEE, Rui Zhang, Fellow, IEEE, and Teng Joon Lim, Fellow, IEEE

Abstract— In terrestrial communication networks without fixed infrastructure, unmanned aerial vehicle-mounted mobile base stations (MBSs) provide an efficient solution to achieve wireless connectivity. This letter aims to minimize the number of MBSs needed to provide wireless coverage for a group of distributed ground terminals (GTs), ensuring that each GT is within the communication range of at least one MBS. We propose a polynomial-time algorithm with successive MBS placement, where the MBSs are placed sequentially starting on the area perimeter of the uncovered GTs along a spiral path toward the center, until all GTs are covered. Numerical results show that the proposed algorithm performs favorably compared with other schemes in terms of the number of required MBSs as well as time complexity.

Index Terms— Unmanned aerial vehicles, mobile base station placement, user coverage, geometric disk cover problem.

# I. INTRODUCTION

W ITH their maneuverability and increasing affordability,unmanned aerial vehicles (UAVs) have many potential unmanned aerial vehicles (UAVs) have many potential applications in wireless communication systems [1]. In particular, UAV-mounted mobile base stations (MBSs) can be deployed to provide wireless connectivity in areas without infrastructure coverage such as battlefields or disaster scenes. Unlike terrestrial base stations (BSs), even those mounted on ground vehicles, UAV-mounted MBSs can be deployed in any location and move along any trajectory constrained only by their aeronautical characteristics, in order to cover the ground terminals (GTs) in a given area based on their known locations. When the UAV-GT channels are dominated by line-of-sight (LOS) links, the authors in [2] use a K-means clustering algorithm to partition the GTs to be served by p UAVs, while each UAV has a capacity constraint and the unsupported GTs are served by the fixed ground BSs. The authors in [3] adopt a probabilistic LOS channel model and study the 3-dimensional (3D) placement of a single aerial BS to offload as many GTs as possible from the ground BS.

In this letter, we assume that the GT locations are known and the UAVs are flying at a fixed altitude H , while the UAV-GT channels are dominated by LOS links whose channel quality mainly depends on the UAV-GT distance. We consider the scenario where no ground BSs are available and the UAV-mounted MBSs are backhaul-connected via satellite links, while each MBS has an equivalent coverage radius of r projected on the ground, as shown in Fig. 1. We thereby focus on the MBS placement problem to provide wireless coverage

Manuscript received October 26, 2016; revised November 21, 2016; accepted November 22, 2016. Date of publication November 29, 2016; date of current version March 8, 2017. The associate editor coordinating the review of this letter and approving it for publication was E. Bedeer.

The authors are with the Department of Electrical and Computer Engineering, National University of Singapore, 117583 (e-mail: elelujb@nus.edu.sg; elezeng@nus.edu.sg; elezhang@nus.edu.sg; eleltj@nus.edu.sg).

Digital Object Identifier 10.1109/LCOMM.2016.2633248

![](images/84db5030a009071b3ad9d747929fb11d35872ca73c7b7217e6518058230c7294.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Satellite"] --> B["UAV"]
    B --> C["H"]
    C --> D["GT"]
    D --> E["r"]
    E --> F["Satellite"]
    F --> G["Satellite"]
    G --> H["Satellite"]
    H --> I["Satellite"]
    I --> J["Satellite"]
    J --> K["Satellite"]
    K --> L["Satellite"]
    L --> M["Satellite"]
    M --> N["Satellite"]
    N --> O["Satellite"]
    O --> P["Satellite"]
    P --> Q["Satellite"]
    Q --> R["Satellite"]
    R --> S["Satellite"]
    S --> T["Satellite"]
    T --> U["Satellite"]
    U --> V["Satellite"]
    V --> W["Satellite"]
    W --> X["Satellite"]
    X --> Y["Satellite"]
    Y --> Z["Satellite"]
```
</details>

Fig. 1. A wireless communication system with UAV-mounted MBSs.

for all GTs in a given area. This can be formulated as the Geometric Disk Cover (GDC) problem [4], whose objective is to cover a set of K nodes (GTs) in a region with the minimum number of disks of given radius r. The GDC problem can be optimally solved by the core-sets method [5] whose theoretical bounds on the running time are exponential in K . Since the GDC problem is NP-hard in general, a strip-cover-with-disks algorithm was proposed in [4], which divides the plane into equal-width strips and solves the problem locally over the GTs within each strip. The computational complexity is reduced thanks to this strip-based partitioning, which, however, may lead to significant performance loss since the GTs in different strips are independently considered though certain GTs in adjacent strips could in fact be covered by the same MBS.

This letter proposes a new MBS placement algorithm by placing the MBSs sequentially, starting from the perimeter of the area boundary in an inward spiral manner until all GTs are covered. In the proposed spiral placement algorithm, each MBS is first positioned to cover at least one uncovered GT near the area boundary, and then its position is adjusted inwards toward the area center to cover as many additional uncovered GTs as possible. This localized strategy has low complexity and does not partition the coverage area into independent regions, hence overcoming the limitations of the strip-based algorithm. Our proposed algorithm has a polynomial-time complexity $O ( K ^ { 3 } )$ in the worst case, which is comparable to the strip-based algorithm but much lower than the coresets method. Numerical results show that for small networks requiring only a few MBSs, where the theoretical minimum can be found by the core-sets method, the proposed algorithm provides the near-optimal performance in terms of the number of required MBSs. Moreover, the proposed algorithm also outperforms other heuristic schemes in terms of the number of required MBSs and average time complexity for networks of different sizes. Note that the proposed algorithm can be considered as a new approach to solve the GDC problem in general and thus can be used in other pertinent applications as well.

# II. SYSTEM MODEL AND PROBLEM FORMULATION

We consider a wireless system with K GTs, which are denoted by the set $\mathcal { K } = \{ 1 , 2 , \cdots , K \}$ and at known locations given by $\{ \mathbf { w } _ { k } \} _ { k \in \mathcal K }$ , where $\mathbf { w } _ { k } \ \in \ \mathbb { R } ^ { 2 \times 1 }$ represents the two-dimensional (2D) coordinates of the k-th GT on the horizontal plane (ground). For simplicity, we assume that the UAV-GT communication channels are dominated by LOS links. We also assume that the transmit power is fixed and the minimum required signal-to-noise ratio (SNR) at the receiver for reliable communications is given. Under the LOS model, the UAV-GT channel power gain follows the free-space pathloss model, which is determined by the UAV-GT link distance. Furthermore, we assume that the UAVs are flying at a given altitude H and their maximum coverage radius projected on the ground plane corresponding to the SNR threshold is specified by r , as shown in Fig. 1.

For cost minimization, we aim to deploy the minimum number of MBSs (UAVs) so that each GT is served by at least one MBS within its communication radius $r .$ Note that this does not preclude the possibility that some GTs may be covered by more than one MBSs. In such scenarios, the inter-cell interference issue needs to be addressed by, $\mathrm { e . g . }$ , proper channel assignment and power control after deploying the MBSs. Denoting by $\mathcal { M } = \{ 1 , \ldots , M \}$ the set of MBSs to be deployed, the problem can be formulated as follows.

$$
\text {(P1)}: \left\{ \begin{array}{l l} \min _ {\{\mathbf {u} _ {m} \} _ {m \in \mathcal {M}}} & | \mathcal {M} | \\ \text {s.t.} & \min _ {m \in \mathcal {M}} \| \mathbf {w} _ {k} - \mathbf {u} _ {m} \| \leq r, \forall k \in \mathcal {K}, \end{array} \right.
$$

where $| { \mathcal { M } } | \ = \ M$ denotes the cardinality of the set M , $\mathbf { u } _ { m } \in \mathbb { R } ^ { 2 \times 1 }$ denotes the horizontal coordinates of MBS m, and the Euclidean norm $\| \mathbf { w } _ { k } - \mathbf { u } _ { m } \|$ is the distance between GT k and MBS m projected on the ground plane.

(P1) is also known as the GDC problem [4], which is NP hard in general. The GDC problem is also related to the p-center problem [6], which aims to locate p centers (MBS locations) of the smallest disks to cover all K nodes (GTs), given by

$$
\text {(P2)}: \left\{ \begin{array}{l l} \min _ {\{\mathbf {u} _ {m} \} _ {m = 1} ^ {p}} & \rho \\ \text {s.t.} & \min _ {m = 1, \dots , p} \| \mathbf {w} _ {k} - \mathbf {u} _ {m} \| \leq \rho , \forall k \in \mathcal {K}, \end{array} \right.
$$

whose optimal value $\rho ^ { * }$ is the smallest radius of the p disks required to cover all K GTs. If $\boldsymbol { \rho } ^ { * } \le \boldsymbol { r }$ , then all GTs can be covered by the $p$ MBSs in (P1) and $M _ { \mathrm { { m i n } } } \leq p _ { \mathrm { { m } } }$ where $M _ { \mathrm { m i n } }$ denotes the optimal value of (P1). The GDC problem (P1) can thus be converted into a series of p-center problems with increasing $p$ values, until the smallest number of MBSs required to cover all GTs is found. Unfortunately, (P2) is in general difficult to solve optimally due to the non-convex constraint min $\| \mathbf { w } _ { k } - \mathbf { u } _ { m } \| \leq \rho , \forall k \in \mathcal { K } .$ In fact, the p-center $m { = } 1 , \cdots , p$ problem is also NP-hard, whose optimal solution requires computational complexity of $O ( p ^ { K } )$ using brute force search [7], which is infeasible even for moderate values of p and K .

# III. SPIRAL MBS PLACEMENT ALGORITHM

In this section, we propose an efficient heuristic algorithm to solve (P1) approximately based on successive MBS placement. The main idea is to place the MBSs sequentially along the area perimeter, which is defined as the path connecting the extreme points (referred to as the boundary GTs) of the convex hull of all uncovered GTs. Each MBS m is guaranteed to cover at

# Algorithm 1 Spiral MBS Placement Algorithm

Input: GT set ${ \mathcal { K } } ,$ with known locations $\{ \mathbf { w } _ { k } \} _ { k \in \mathcal K } .$

$\{ \bar { \mathbf { u } } _ { m } \} _ { m \in \mathcal { M } } .$

Initialization: Uncovered GT set $\begin{array} { r l r l r l } { { \mathcal K } _ { U } } & { { }  } & { { \mathcal K } ; } & { { } { \mathcal M } } & { = } & { { } { \mathcal G } ; } \end{array}$ m=1.

1: while $\mathcal { K } \sigma \neq \emptyset$ do   
2: Find boundary GT set $\mathcal { K } _ { U , b o } \subseteq \mathcal { K } _ { U }$ and list them in counterclockwise order. Update inner GT set $\mathcal { K } _ { U , i n }  \mathcal { K } _ { U } \setminus \mathcal { K } _ { U , b o }$ . If $m = 1 ,$ , randomly pick a GT k0 $\in \mathcal { K } _ { U , b o } .$   
3: Refine MBS location u to cover $k _ { 0 }$ and as many boundary GTs as possible, by calling [u, $\begin{array} { r } { \mathcal { P } _ { p r i o } ] = } \end{array}$ LocalCover $\mathbf { \langle w } _ { k _ { 0 } } , \{ k _ { 0 } \}$ $\mathcal { K } _ { U , b o } \setminus \{ k _ { 0 } \} )$ . Let $\begin{array} { r } { \mathcal { K } _ { n e w , b o }  \dot { \mathcal { P } } _ { p r i o } . } \end{array}$   
4: Refine MBS location u to cover $\mathcal { K } _ { u e w , b o }$ and as many inner GTs as possible, by calling [u, $\begin{array} { r } { \mathcal { P } _ { p r i o } ] = . } \end{array}$ LocalCover(u, $\mathcal { K } _ { u e w , b o } ,$ $\mathcal { K } _ { }$ Let $\mathbf { u } _ { m } = \mathbf { u } ,$ Knew $\dot { } \gets \varPsi _ { p r i o } .$   
5: M ← M ∪ {m}, KU ← KU \ Knew, m $ m + 1 .$   
6: From $\mathcal { K } _ { U , b o } \ \backslash \ \mathcal { K } _ { n e w , b o } ,$ pick the first uncovered boundary GT $k _ { 0 } ^ { \prime }$ counterclockwisely next to $k _ { 0 } .$ . Let $k _ { 0 } \gets k _ { 0 } ^ { \prime } .$ .   
7: end while

# Algorithm 2 LocalCover Procedure

Procedure [u, $\begin{array} { r l r l } { \mathcal { P } _ { p r i o } ] } & { { } = } & { } & { { } } \end{array}$ LocalCover(u, $\begin{array} { r l r } { \mathcal { P } _ { p r i o } , } & { { } } & { \mathcal { P } _ { s e c } ) } \end{array}$

1: while $\mathcal { P } _ { s e c } \neq \emptyset$ do

2: Update $\mathcal { P } _ { s e c }$ by excluding GTs more than 2r away from any GT in $\mathcal { P } _ { p r i o } .$ . Update $\mathcal { P } _ { p r i o } \left( \mathcal { P } _ { s e c } \right)$ by including (excluding) GTs within distance r to u.

3: Find GT $k _ { 1 } \in \mathcal { P } _ { s e c }$ with shortest distance to u. Add (remove) $k _ { 1 }$ to (from) $\mathcal { P } _ { p r i o } \left( \mathcal { P } _ { s e c } \right)$ if it can be covered by refining u via solving the 1-center problem. Stop otherwise.

4: end while

least one boundary GT $k _ { 0 } ,$ and those GTs at a distance of more than 2r away from $k _ { 0 }$ are removed from consideration, since they cannot be jointly covered with $k _ { 0 }$ by the same MBS m. Since $k _ { 0 }$ is at the boundary, MBS m will be placed inwards toward the area center to cover as many uncovered GTs as possible, with higher priority given to the GTs on the boundary to reduce the occurrence of outlier GTs that each may require one dedicated MBS for its coverage. After MBS m is placed, the area perimeter of the remaining uncovered GTs shrinks at the local region near $k _ { 0 }$ . The above process repeats to place the next MBS $m + 1$ counterclockwisely next to MBS m, and the area perimeter gradually shrinks until all GTs are covered. As a result, the connecting line of the placed MBSs looks like a spiral which starts from the area boundary and counterclockwisely revolves inwards toward the area center. We therefore name our proposed algorithm as the spiral MBS placement algorithm, which is summarized in Algorithm 1.

We use the example in Fig. 2 to illustrate the notations and the main steps of our spiral algorithm. Denote by ${ \mathcal { K } } \subseteq { \mathcal { K } }$ the subset of uncovered GTs, which is initialized to K at the beginning of Algorithm 1. KU is partitioned into the inner GT subset $\mathcal { K } _ { U , i n }$ and the boundary GT subset ${ \mathcal { K } } _ { U , b o } ,$ where the boundary GTs can be listed in counterclockwise order as $\mathcal { K } _ { U , b o } ~ = ~ \{ 1 , 2 , 3 , 4 , 5 , 6 , \cdot \cdot \cdot \}$ initially (dark blue triangles), and ${ \mathcal K } _ { U , i n } ~ = ~ { \mathcal K } _ { U } ~ \backslash ~ { \mathcal K } _ { U , b o }$ (light blue triangles). The path connecting these boundary GTs is referred to as the area perimeter of the uncovered GTs, as shown in Fig. 2. We use the convex hull to define the boundary GTs, whereas other boundary definitions [8] can also be used which produce similar results.

![](images/fe6c49d1311a6841b418fcb271edbffc02538c7f764b7b1c7330e87d9e4b439e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    GT1["GT1"] -->|2r| GT2["GT2"]
    GT2 --> MBS1["MBS1"]
    GT3["GT3"] --> GT4["GT4"]
    GT4 --> NextUncoveredBoundary["Next Uncovered Boundary GT k₀"]
    GT5["GT5"] --> GT6["GT6"]
    GT6 --> BoundaryGT["Boundary GT"]
    GT7["GT7"] --> GT8["GT8"]
    GT8 --> InnerGT["Inner GT"]
    GT9["GT9"] --> GT10["GT10"]
    GT10 --> MBS2["MBS2"]
    GT11["GT11"] --> MBS2
    MBS2 --> CoverageRadius["Coverage radius r"]
    CoverageRadius --> AreaPerimeter["Area perimeter"]
```
</details>

Fig. 2. Illustration of the spiral algorithm.

We give higher priority to the boundary GTs in the way that a certain subset of boundary GTs are guaranteed to be covered by each newly placed MBS. To place the first MBS, we randomly choose a boundary GT k0 which is guaranteed to be covered, e.g., GT 3 at the lower left corner denoted by a red triangle (step 2 in Algorithm 1). Then we refine the MBS location u to cover $k _ { 0 }$ and as many boundary GTs as possible (step 3). In this case, the boundary GTs 2 and 4 can be covered, and hence are added into the prioritized set $\mathcal { P } _ { p r i o } = \{ 2 , 3 , 4 \}$ which is guaranteed to be covered first. Then we proceed to cover GTs from $\mathcal { P } _ { p r i o }$ and as many inner GTs as possible (step 4). In this case, the inner GTs 7 and 8 can be covered. The final location of the first MBS is denoted by a green square, which is the center of the covering disk of radius r, denoted by a dashed green circle. After placing the first MBS, the area perimeter shrinks at the local region near GT $k _ { 0 } .$ , with GT 1 directly connected to GT 5 in this case. To place the next MBS, we pick the first uncovered boundary GT $k _ { 0 } ^ { \prime }$ counterclockwisely next to $k _ { 0 } ,$ , which in this case is GT 5, and update $k _ { 0 }  k _ { 0 } ^ { \prime }$ (step 6). Then the above steps are repeated to place the second MBS which covers GTs 5, 6 and 11. The above process repeats until all GTs are covered.

Note that we have used a LocalCover procedure in steps 3 and 4 of Algorithm 1, which refines the new MBS location u to guarantee to cover GTs from the given prioritized set $\mathcal { P } _ { p r i o }$ (e.g., the initial boundary GT $k _ { 0 } )$ , and then to cover as many GTs as possible from the secondary set of GTs (e.g., uncovered inner GTs), denoted as $\mathcal { P } _ { s e c } .$ . Mathematically, this can be formulated as the following optimization problem.

$$
\text {(P3)}: \left\{ \begin{array}{l l} \max _ {\mathbf {u}, \mathcal {K} _ {n e w}} & | \mathcal {K} _ {n e w} | \\ \text {s.t.} & \| \mathbf {u} - \mathbf {w} _ {k} \| \leq r, \forall k \in \mathcal {K} _ {n e w} \cup \mathcal {P} _ {p r i o}, \\ & \mathcal {K} _ {n e w} \subseteq \mathcal {P} _ {s e c}, \end{array} \right.
$$

where u denotes the location of the new MBS to be placed, ${ \mathcal { K } } _ { u e w } \subseteq { \mathcal { P } } _ { s e c }$ denotes the set of GTs newly covered by this new MBS. Note that the first constraint in (P3) ensures that all GTs in $\mathcal { K } _ { u e w }$ and $\mathcal { P } _ { p r i o }$ are covered by this new MBS. (P3) is a combinatorial optimization problem, which in general requires exhaustive search over all $\overline { { 2 ^ { | \mathcal { P } _ { s e c } | } } }$ subsets of $\mathcal { P } _ { s e c }$ in order to obtain the optimal solution, which is prohibitive even for moderately large systems. Therefore, we propose a LocalCover procedure with possibly sub-optimal solutions to (P3) for low-complexity implementation, as summarized in Algorithm 2.

We continue to use the example in Fig. 2 to illustrate Algorithm 2. Firstly, for any given $\mathcal { P } _ { p r i o } , \mathcal { P } _ { s e c }$ can be reduced by excluding those GTs more than $2 r$ away from any GT in $\mathcal { P } _ { p r i o } ,$ since the same MBS cannot cover two GTs that are more than 2r away from each other. This confines the search space to a local region near $\mathcal { P } _ { p r i o }$ . For example, since the first MBS is guaranteed to cover GT 3, we can draw a dashed red circle centered at GT 3 with radius 2r as shown in Fig. 2, and exclude those GTs that are outside of this circle from consideration, after which only GTs 2, 3, 4, 7, 8, and 9 are left. This greatly reduces the problem size in (P3). Secondly, the remaining GTs in $\mathcal { P } _ { s e c }$ are sorted in ascending order of the distance to the current MBS location u, and are then successively included based on this order until they cannot be covered by the same MBS. Intuitively, the number of newly covered GTs in $\mathcal { P } _ { s e c }$ is approximately maximized. Moreover, in step 2 of Algorithm 2, we update $\mathcal { P } _ { p r i o } ~ ( \mathcal { P } _ { s e c } )$ by including (excluding) GTs within distance r to u. This simple check reduces the times that the 1-center subroutine in step 3 of Algorithm 2 needs to be executed. For example, after MBS 1 covers the boundary GTs 2, 3 and 4, the algorithm finds that GT 7 is already covered and hence does not need to call the 1-center subroutine for GT 7 subsequently.

![](images/590312b6975fc6d40b372fd5ffbe2ee05d3a3f41ecd802b8c7aff44cf2f2a437.jpg)

<details>
<summary>scatter</summary>

| Point | Type          | x (km) | y (km) |
|-------|---------------|--------|--------|
| 1     | MBS(spiral)   | 0.5    | 0.5    |
| 2     | MBS东部点   | 1.7    | 0.3    |
| 3     | MBS东部点   | 2.5    | 0.8    |
| 4     | MBS东部点   | 2.9    | 2.4    |
| 5     | MBS东部点   | 1.9    | 2.6    |
| 6     | MBS东部点   | 0.4    | 2.6    |
| 7     | MBS东部点   | 0.5    | 1.6    |
| 8     | MBS东部点   | 1.1    | 1.3    |
| 9     | MBS东部点   | 2.5    | 1.6    |
| 10    | MBS东部点   | 1.9    | 1.6    |
| 11    | MBS东部点   | 1.3    | 2.0    |
</details>

Fig. 3. Solutions of the spiral, strip-based and core-sets methods to the GDC problem with 80 GTs and MBS coverage radius $r = 0 . 5$ km.

In step 3 of Algorithm 2, to check whether a set P of K points can be covered by a single disk of radius r, we need to solve the 1-center problem, which finds the location u of the center from which the maximum distance to any point in P is minimized. Several algorithms exist to solve the 1-center problem, such as that in [9] with O(K ) complexity, and a more straightforward one in [10] with $O ( K ^ { 2 } )$ complexity.

For our spiral algorithm, each of the MBSs to be placed needs to run the convex hull algorithm to find the boundary GTs and list them in counterclockwise order, which has complexity O(K log b) with $b \ \leq \ K$ being the number of extreme points of the convex hull. Moreover, each MBS may also need to execute the 1-center subroutine for up to $O ( K )$ times. Since the number of placed MBSs is at most $O ( K )$ , the overall computational complexity is upper-bounded by $O ( K [ K$ log $K + K \cdot C ( K ) ] )$ ), where C(K ) is the running time of the 1-center subroutine. Note that the actual running time could be much less than this worst-case complexity, since the size of each 1-center subroutine and the times to be executed are greatly reduced, thanks to the strategy of excluding faraway GTs and including nearby GTs in step 2 of Algorithm 2.

To illustrate the final MBS placement results, we apply our spiral algorithm to a numerical example with $K = 8 0 ~ \mathrm { G T s }$ (denoted as triangles) randomly and independently scattered in a square region of area 10 km2, where each MBS has a coverage radius $r ~ = ~ 0 . 5$ km, as shown in Fig. 3. We use dash-dotted red arrows to connect the MBSs which are successively placed along the area perimeter. In this case, a total of 11 MBSs (denoted as green squares) are required and their connecting line looks like a spiral which starts from the area boundary and counterclockwisely revolves inwards toward the area center.

TABLE I COMPARISON BETWEEN SPIRAL ALGORITHM AND OTHER SCHEMES 

<table><tr><td colspan="2">K</td><td colspan="5">80</td><td colspan="5">400</td></tr><tr><td colspan="2">D/r</td><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td><td>4</td><td>8</td><td>12</td><td>16</td><td>20</td></tr><tr><td rowspan="2">Core-sets</td><td>M</td><td>2.2</td><td>5.8</td><td>10.4</td><td>-</td><td>-</td><td>7.8</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>t(s)</td><td>0.460</td><td>5.754</td><td>10193</td><td>-</td><td>-</td><td>8004</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Spiral</td><td>M</td><td>2.2</td><td>5.8</td><td>10.6</td><td>15.4</td><td>20.8</td><td>8.0</td><td>22.8</td><td>41.6</td><td>62.8</td><td>85.6</td></tr><tr><td>t(s)</td><td>0.116</td><td>0.141</td><td>0.158</td><td>0.154</td><td>0.151</td><td>0.175</td><td>0.232</td><td>0.280</td><td>0.300</td><td>0.301</td></tr><tr><td rowspan="2">Strip</td><td>M</td><td>2.4</td><td>6.8</td><td>12.4</td><td>18.6</td><td>26.8</td><td>8.8</td><td>25.2</td><td>49.6</td><td>79.8</td><td>111.0</td></tr><tr><td>t(s)</td><td>0.137</td><td>0.130</td><td>0.128</td><td>0.116</td><td>0.105</td><td>0.338</td><td>0.308</td><td>0.274</td><td>0.237</td><td>0.201</td></tr><tr><td rowspan="2">K-means</td><td>M</td><td>2.6</td><td>6.6</td><td>11.6</td><td>17.2</td><td>23.0</td><td>8.4</td><td>26.4</td><td>51.2</td><td>84.4</td><td>120.2</td></tr><tr><td>t(s)</td><td>7.558</td><td>9.151</td><td>10.88</td><td>11.19</td><td>11.21</td><td>34.13</td><td>46.37</td><td>61.97</td><td>69.83</td><td>72.58</td></tr><tr><td rowspan="2">Ran-dom</td><td>M</td><td>3.0</td><td>8.8</td><td>17.2</td><td>26.0</td><td>35.2</td><td>10.6</td><td>36.8</td><td>75.2</td><td>116.6</td><td>162.2</td></tr><tr><td>t(s)</td><td>0.083</td><td>0.329</td><td>1.018</td><td>1.891</td><td>3.507</td><td>1.246</td><td>14.23</td><td>39.00</td><td>87.03</td><td>122.8</td></tr></table>

To check the optimality of our spiral algorithm, we apply the core-sets method of exponential complexity in [5] with stacked-depth-first branch-and-bound search to the 80 GTs’ topology in Fig. 3, which yields a minimum coverage radius of 0.5231 km and 0.4829 km for 10-center and 11-center problems, respectively. Therefore, it requires a minimum of 11 MBSs to cover all 80 GTs with a coverage radius of 0.5 km, which is the same as that achieved by our spiral algorithm. The placed MBS locations are denoted as $" \times "$ in Fig. 3. As a benchmark comparison, we also apply the strip-based algorithm in [4] to the 80 GTs’ topology in Fig. 3. It requires a total number of 13 MBSs (denoted as $" + "$ in Fig. 3) to cover all GTs, which is more than that obtained by our spiral algorithm.

# IV. NUMERICAL RESULTS

In this section, we test the algorithms for two cases with $K ~ = ~ 8 0$ and $K \ = \ 4 0 0 \ { \mathrm { ~ G T s } }$ , respectively. In each case, we randomly and independently generate 5 topologies with K GTs in a square region of side length D, and apply the algorithms to these topologies with different coverage radius r . For each algorithm and each $D / r$ ratio, the total number of required MBSs M and the running time t in seconds are averaged over the 5 topologies, respectively. Besides the coresets method and the strip-based algorithm, we also compare with two other heuristic schemes. The first one is random placement, which randomly selects a location to place an MBS and removes the covered region from consideration when placing the next MBS. The process repeats until all GTs are covered. The second one is to run the K-means algorithm to partition the GTs to be covered by p MBSs. Bisection search is performed to find the minimum number $p$ to cover all GTs. Each of these two heuristics is executed for 100 trials on each topology and $D / r$ ratio to find the best trial with the minimum number of MBSs. Note that the more trials of these two heuristics (hence a longer running time), the higher likelihood of finding a solution with smaller number of required MBSs. We used the 1-center sub-routine in [10] and the default initialization of the K-means function in MATLAB 2015b, which runs on Windows 10 with Intel-i5 3.5GHz PC and 8GB RAM. The results are summarized in TABLE I.

As observed from TABLE I, the theoretical minimum $M _ { \mathrm { m i n } }$ obtained by the core-sets method can only be found for small networks requiring only a few MBSs, e.g., $K \ = \ 8 0$ and $M _ { \mathrm { m i n } } ~ \leq ~ 1 1$ or $K \ = \ 4 0 0$ and $M _ { \mathrm { { m i n } } } ~ \leq ~ 8 ,$ , due to the prohibitive computational complexity of the core-sets method. In these cases, the spiral algorithm provides the near-optimal performance in terms of M, but is much more time-efficient than the core-sets method. Moreover, the spiral algorithm outperforms the strip-based algorithm in terms of M while having comparable t on average. Note that the gap in M between the strip-based algorithm and the spiral algorithm becomes larger as the ratio $D / r$ increases. This is expected since a larger $D / r$ ratio means more strips in the stripbased algorithm, and consequently larger performance loss. Our spiral algorithm outperforms the strip-based algorithm since each MBS is not restricted to cover GTs within each of the independent fixed strips, but instead can be flexibly placed to reduce outlier GTs and hence the total number of required MBSs. Finally, the spiral algorithm also outperforms the other two heuristic schemes in terms of M and t on average for networks of different sizes.

# V. CONCLUSIONS

This letter proposed a new polynomial-time successive MBS placement solution for UAV-GT communications, termed as the spiral algorithm. The proposed algorithm is compared favorably against well-known benchmark schemes in terms of the minimum number of required MBSs to cover all GTs. Future work could extend to the cases with additional backhaul connectivity constraint between MBSs and adaptive MBS placement subject to moving GTs.

# REFERENCES

[1] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.   
[2] B. Galkin, J. Kibilda, and L. A. DaSilva, “Deployment of UAV-mounted access points according to spatial user locations in two-tier cellular networks,” in Proc. Wireless Days (WD), Mar. 2016, pp. 1–6.   
[3] R. I. Bor-Yaliniz, A. El-Keyi, and H. Yanikomeroglu, “Efficient 3-D placement of an aerial base station in next generation cellular networks,” in Proc. IEEE Int. Conf. Commun. (ICC), May 2016, pp. 1–5.   
[4] A. Srinivas, G. Zussman, and E. Modiano, “Construction and maintenance of wireless mobile backbone networks,” IEEE/ACM Trans. Netw., vol. 17, no. 1, pp. 239–252, Feb. 2009.   
[5] H. A. Fayed and A. F. Atiya, “A mixed breadth-depth first strategy for the branch and bound tree of Euclidean k-center problems,” Comput. Optim. Appl., vol. 54, no. 3, pp. 675–703, 2013.   
[6] P. K. Agarwal and C. M. Procopiuc, “Exact and approximation algorithms for clustering,” in Proc. 9th Annu. ACM-SIAM Symp. Discrete Algorithms, Jan. 1998, pp. 658–667.   
[7] N. Megiddo and K. J. Supowit, “On the complexity of some common geometric location problems,” SIAM J. Comput., vol. 13, no. 1, pp. 182–196, 1984.   
[8] M. Duckham, L. Kulik, M. Worboys, and A. Galton, “Efficient generation of simple polygons for characterizing the shape of a set of points in the plane,” Pattern Recognit., vol. 41, no. 10, pp. 3224–3236, 2008.   
[9] N. Megiddo, “Linear-time algorithms for linear programming in R3 and related problems,” SIAM J. Comput., vol. 12, no. 4, pp. 759–776, 1983.   
[10] J. Elzinga and D. W. Hearn, “Geometrical solutions for some minimax location problems,” Transp. Sci., vol. 6, no. 4, pp. 379–394, 1972.