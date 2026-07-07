# Corrections to “Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication”

Kaitao Meng , Member, IEEE, Qingqing Wu , Senior Member, IEEE, and Wen Chen , Senior Member, IEEE

Abstract—In our original paper, we omitted a key step involving the transformation of variable $\tilde { R } _ { k . i } ^ { I S A C } [ n ]$ . In this work, we recognize that our initial conclusion, stating that $^ { 6 6 } H _ { k , j }$ is a negative definite matrix in the feasible region” requires additional clarification and adjustments. To ensure the correctness of the work, we provide the necessary modifications and detailed discussions in this revised version.

Index Terms—Integrated sensing and communication, UAV, periodic sensing, user association, beamforming, trajectory optimization.

## I. INTRODUCTION

In the above article (31) of [1], there is a typographical error where the term $\alpha _ { k } | n |$ ] is mistakenly included in R, as it is already accounted for in $\underline { { R } } _ { k } [ \dot { n } ] .$ . To correct this, $\alpha _ { k } [ n ]$ should be removed, and the revised expression is provided in (1), shown at the bottom of the page. In Section II-A of [2], the claim that (P2.2) is non-convex arises from this typo. The corrected definition of $\underline { { R } } _ { k } [ n ]$ confirms that (P2.2) is a convex problem.

In [1], the statement that $\mathbf { \ddot { \Sigma } } ^ {  } \mathbf { H } _ { k , j }$ is a negative definite matrix” is incorrect. We need to remove the statements regarding $H _ { k , j }$ since they are irrelevant to the problem solving. In this paper, we include the transformation of the variable $\tilde { R } _ { k , j } ^ { I S A \smile } [ n ]$ which was previously omitted and insufficiently detailed in [1]. In Section II-B of [2], the claim that (P2.5) is non-convex arises from this omitted step. Specifically, (P2.4) in [1] should be transformed into the new (P2.5) in this work. While the resulting problem is technically different, it accurately reflects the solution process that was actually employed in [1]. After the process of equation (41) in [1], we have $\check { R } _ { k , j } ^ { I S A \dot { C } } [ n ] =$ log<sub>2</sub> $( z _ { c , k } \middle [ n ] + \gamma _ { 0 } M P _ { \mathrm { m a x } } - \gamma _ { 0 } z _ { r , j } \middle [ n \middle ] \Gamma ^ { t h } ) - \log _ { 2 } ( z _ { c , k } \middle [ n ] )$ . By introducing a new variable $u _ { c , k } [ n ]$ stratifying

$$
u _ { c , k } [ n ] \leq z _ { c , k } [ n ] + \gamma _ { 0 } M P _ { \operatorname* { m a x } } - z _ { r , j } [ n ] \Gamma ^ { t h } ,\tag{42}
$$

we have $\begin{array} { r c l } { \tilde { R } _ { k , j } ^ { I S A C } [ n ] } & { \geq } & { \log _ { 2 } { \left( u _ { c , k } [ n ] \right) } - \log _ { 2 } { \left( z _ { c , k } [ n ] \right) } } \end{array}$ . Using the first-order Taylor expansion, $\log _ { 2 } \left( z _ { c , k } [ n ] \right)$ can be transformed into a linear function of $z _ { c , k } [ n ]$ . Specifically, the transformed $\tilde { R } _ { k , j } ^ { I S A C } [ n ]$ is denoted by $\hat { R } _ { k , j } ^ { I S A C } [ n ] = \bar { \log } _ { 2 } \left( u _ { c , k } [ n ] \right) - \log z _ { c , k } ^ { ( r ) } [ n ] -$ $\frac { 1 } { z _ { c , k } ^ { ( r ) } [ n ] \ln 2 } \left( z _ { c , k } [ n ] - z _ { c , k } ^ { ( r ) } [ n ] \right)$ , and (P2.4) can be converted into

$$
( \mathrm { P 2 . 5 } ) : \qquad \operatorname* { m a x } _ { Q , \{ z _ { \mathrm { c } , \mathrm { k } } \} , \{ z _ { \mathrm { r } , \mathrm { j } } \} , \{ \mathrm { u } _ { \mathrm { c } , \mathrm { k } } \} } \quad \frac { 1 } { \mathrm { N } } \sum _ { \mathrm { n } = 1 } ^ { \mathrm { N } } \sum _ { \mathrm { k } = 1 } ^ { \mathrm { K } } \hat { \mathrm { R } } _ { \mathrm { k } } [ \mathrm { n } ]\tag{43}
$$

$$
\begin{array} { r l } { \mathrm { s . t . } } & { { } ( 1 2 e ) , ( 1 2 f ) , ( 2 7 ) , ( 3 9 ) , ( 4 0 ) , ( 4 2 ) , } \end{array}
$$

$$
\frac { 1 } { N _ { L } } \sum _ { n = ( l - 1 ) N _ { L } + 1 } ^ { l N _ { L } } \hat { R } _ { k } [ n ] \geq R _ { k } ^ { t h } , \forall k , l ,\tag{43a}
$$

where $\begin{array} { r } { \hat { R } _ { k } [ n ] = \alpha _ { k } [ n ] \hat { R } _ { k } ^ { C } [ n ] + \sum _ { i = 1 } ^ { J } e _ { k , j } [ n ] ( \hat { R } _ { k , j } ^ { I S A C } [ n ] - \tilde { R } _ { k } ^ { C } [ n ] ) } \end{array}$ To ensure consistency, we use the same equation indexing as in [1], except that constraint (42) in (P2.5) is replaced by equation (42) in this work. Based on the previous discussions, all of the constraints of (P2.5) are convex constraints. Thus, (P2.5) is a convex optimization problem that can be solved by convex optimization solvers.

Please notice that the original (P2.5) in [1] cannot be run directly on CVX. The simulations in [1] were conducted using the transformed problem (P2.5) described above, and thus the simulation results remain the same.

## REFERENCES

[1] K. Meng, Q. Wu, S. Ma, W. Chen, K. Wang, and J. Li, “Throughput maximization for UAV-enabled integrated periodic sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 1, pp. 671–687, Jan. 2023.

[2] S. Shin, S. Hwang, S. Kim, and I. Lee, “Comments on ‘throughput maximization for UAV-enabled integrated periodic sensing and communication,”’ IEEE Trans. Wireless Commun., vol. 24, no. 2, p. 1753, Feb. 2025, doi: 10.1109/TWC.2024.3509992.

Digital Object Identifier 10.1109/TWC.2025.3634306

$$
\begin{array} { l } { { \displaystyle { \cal R } = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \frac { R _ { k } [ n ] - \frac { 1 } { 2 \eta } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } ( \vert \alpha _ { k } [ n ] ( 1 - \bar { \alpha } _ { k } [ n ] ) \vert ^ { 2 } + \vert \alpha _ { k } [ n ] - \bar { \alpha } _ { k } [ n ] \vert ^ { 2 } ) } } } \\ { { \displaystyle ~ - \frac { 1 } { 2 \eta } \sum _ { n = 1 } ^ { N } \sum _ { j = 1 } ^ { J } \sum _ { k = 1 } ^ { K } ( \vert e _ { k , j } [ n ] ( 1 - \bar { e } _ { k , j } [ n ] ) \vert ^ { 2 } + \vert e _ { k , j } [ n ] - \bar { e } _ { k , j } [ n ] \vert ^ { 2 } ) , } } \end{array}\tag{1}
$$