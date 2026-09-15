---
title: 'Srednicki §78 背景场规范'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [78]
hideFromHome: true
draft: false
---

<span id="c78"></span>

第73节求出了杨—米尔斯理论的一圈贝塔函数。那次计算分别确定了物质场、规范场以及顶角的重整化因子，再把它们组合成同一个裸耦合。最终结果很简单，中间步骤却不短。现在改选一种规范，使量子作用量显式保持对外部规范场的规范不变性。这样，耦合常数的重整化就能完全归结为这个外部场的二点函数。更有意思的是，规范场的一圈贡献将分成两部分：一部分和标量场相似，另一部分直接来自自旋与背景场强的耦合。渐近自由的负号主要由后一部分决定。

以下沿用[第73节](/posts/srednicki-73/#c73)的规范场归一。局域变换参数$\theta$没有吸收耦合，故它与第77节的无量纲参数相差一个$g$。取度规$(-,+,+,+)$、$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$和$d=4-\epsilon$，圈积分中的耦合为$g_d=g\widetilde\mu^{\epsilon/2}$。先考虑一个简单规范群因子，物质表示可以是若干不可约表示的直和。

<span id="c78-background"></span>

## 让规范固定条件随背景协变

从规范固定后的杨—米尔斯理论开始：

<span id="eq:c78-action"></span>

$$
\begin{gathered}
\mathcal L_{\rm YM}=-\frac14F_{\mu\nu}^aF^{a\mu\nu},
\qquad
F_{\mu\nu}^a=\partial_\mu A_\nu^a-\partial_\nu A_\mu^a
             +gf^{abc}A_\mu^bA_\nu^c,\\
\mathcal L_{\rm gf}=-\frac1{2\xi}G^aG^a,\qquad
\mathcal L_{\rm gh}
=\bar c^a\frac{\delta G^a}{\delta A_\mu^b}D_\mu^{bc}c^c,\\
D_\mu^{bc}
=\delta^{bc}\partial_\mu+gf^{bac}A_\mu^a,
\qquad (T_A^a)^{bc}=-if^{abc}.
\end{gathered}
\tag{78.1}
$$

这里$\delta G/\delta A$应按微分算符理解。若$G$含有作用在$A$上的导数，这个导数在鬼核中就继续作用于右侧。[第71节的法捷耶夫—波波夫构造](/posts/srednicki-71/)已经说明，选定规范函数以后，规范固定项和鬼项须一起加入。通常的$R_\xi$规范取$G^a=\partial^\mu A_\mu^a$；它便于求传播子，却使规范固定后的作用量失去普通规范不变性。

为改变这一点，引入一个任意但固定的经典场$\bar A_\mu^a$。它是路径积分的参数，$A$仍是积分变量。用背景场构造协变导数，再用它对两场之差取散度：

<span id="eq:c78-gauge-choice"></span>

$$
\bar D_\mu=\partial_\mu-igT_A^a\bar A_\mu^a,\qquad
q_\mu^a=A_\mu^a-\bar A_\mu^a,\qquad
G^a=(\bar D^\mu q_\mu)^a.
\tag{78.2}
$$

$q$表示相对于背景的量子涨落；用它可以清楚地说明规范函数怎样变换。计算法捷耶夫—波波夫行列式时只改变积分场，背景保持不动。由$\delta_GA=-D\theta$得到

<span id="eq:c78-ghost"></span>

$$
\begin{aligned}
\delta_GG^a&=-\bar D^{\mu ab}D_\mu^{bc}\theta^c,\\
\mathcal L_{\rm gh}
&=\bar c^a\bar D^{\mu ab}D_\mu^{bc}c^c
 \doteq-(\bar D^\mu\bar c)^a(D_\mu c)^a .
\end{aligned}
\tag{78.3}
$$

符号$\doteq$表示两边的作用量相等，密度可相差一个全导数。具体地，伴随连接是实反对称矩阵，因此在紧支撑场或没有边界流出的条件下，
$\int X^a(\bar D_\mu Y)^a=-\int(\bar D_\mu X)^aY^a$。把$X=\bar c$、$Y=Dc$代入就给出最后一式。这里移动的是偶微分算符，$\bar c$始终在$c$之前，没有另一次奇变量交换。

接着区分两种变换。普通变换$\delta_G$只变换$A,c,\bar c$；另一种$\delta_{\rm BG}$只变换背景：

<span id="eq:c78-two-transformations"></span>

$$
\begin{array}{c|cc}
 &\delta_G&\delta_{\rm BG}\\ \hline
A_\mu&-D_\mu\theta&0\\
\bar A_\mu&0&-\bar D_\mu\theta\\
c&-ig\theta^aT_A^ac&0\\
\bar c&-ig\theta^aT_A^a\bar c&0
\end{array}
\tag{78.4}
$$

反鬼也按同一伴随表示变换；它与$c$是独立的奇变量，而伴随表示本身是实的。单独作$\delta_G$时，固定的$\bar A$不能随$A$转动，故规范固定项和鬼项一般改变。单独作$\delta_{\rm BG}$时，$\mathcal L_{\rm YM}$不变，因为它只含$A$，但另两项仍会改变。把这两种变换相加以后，情况不同：两个连接的非齐次部分正好在差场中抵消。

<span id="eq:c78-homogeneous-q"></span>

$$
\begin{aligned}
\delta q_\mu^b
&=-(D-\bar D)_\mu^{ba}\theta^a
 =igq_\mu^c(T_A^c)^{ba}\theta^a\\
&=-ig\theta^a(T_A^a)^{bc}q_\mu^c,\qquad
\delta=\delta_G+\delta_{\rm BG}.
\end{aligned}
\tag{78.5}
$$

最后一个等号用了$f^{cba}$的全反对称性。因此，两连接之差是一个普通伴随场。于是$\bar Dq$、$\bar D\bar c$和$Dc$在联合变换下都齐次变换。记$R_\theta=-ig\theta^aT_A^a$，有$R_\theta^T=-R_\theta$；任意两个这样的列$X,Y$满足
$\delta(X^TY)=X^T(R_\theta^T+R_\theta)Y=0$。所以$G^aG^a$与鬼动能的群指标缩并都不变。杨—米尔斯项也保持不变，完整作用量便有了这种联合规范对称性。

<span id="c78-effective"></span>

## 从背景沃德恒等式得到一个重整化因子

量子作用量$\Gamma$由去掉外传播子的1PI图组成，各外腿用相应的平均场代替。背景$\bar A$又出现在所有内线和顶角中，因此应把它单独列在分号之后，写成$\Gamma(A,c,\bar c;\bar A)$。前一个$A$是勒让德变换的平均场，后一个$\bar A$是定义积分时给定的参数。

经典的联合对称性怎样传给$\Gamma$？以$q$为积分变量，给它加入源$\int Jq$。联合变换下让$J$也按伴随表示转动，源项就保持不变。在测度、调节和反项保持这一对称性的条件下，改变积分变量得到

<span id="eq:c78-legendre"></span>

$$
\begin{gathered}
Z[J;\bar A]
=\int\mathcal Dq\,\mathcal Dc\,\mathcal D\bar c\,
 e^{\,iS[\bar A+q,c,\bar c;\bar A]+i\int Jq},
\qquad W=-i\ln Z,\\
\widehat q=\frac{\delta W}{\delta J},\qquad
\Gamma[\widehat q;\bar A]=W[J;\bar A]-\int J\widehat q,\\
\delta W=0,\qquad
\delta\widehat q=R_\theta\widehat q,\qquad
\delta\Gamma=0 .
\end{gathered}
\tag{78.6}
$$

为简洁省去了鬼的源；加上它们时，论证完全相同。关键在于$q$的变换是线性的，因而对变换后的场取平均与先取平均再变换相同。总场$A$虽有一个$\partial\theta$项，它不依赖积分变量，也不妨碍这个结论。这也是[第21节有效作用量对称性证明](/posts/srednicki-21/#c21-symmetry)在背景场中的应用。纯杨—米尔斯和向量型物质可采用相容的背景规范调节；若加入外尔物质，须先满足第75–77节的规范反常消除条件。

现在令平均场$A=\bar A$，即$\widehat q=0$。这一限制在联合变换下保持，因为零伴随场仍变为零。保留鬼平均场时，将量子作用量分成树项与圈项：

<span id="eq:c78-diagonal"></span>

$$
\begin{aligned}
\Gamma(\bar A,c,\bar c;\bar A)
={}&\int d^4x\left[
 -\frac14\bar F_{\mu\nu}^a\bar F^{a\mu\nu}
 -(\bar D^\mu\bar c)^a(\bar D_\mu c)^a\right]\\
&+\Gamma_{\rm loops}(\bar A,c,\bar c;\bar A).
\end{aligned}
\tag{78.7}
$$

规范固定项在这条对角线上为零。背景仍按$\delta\bar A=-\bar D\theta$变换，鬼仍齐次变换，故整个表达式具有普通的背景规范不变性。再令外鬼为零，记$\Gamma_{\rm bg}[\bar A]=\Gamma(\bar A,0,0;\bar A)$，任意$\theta(x)$的系数给出

<span id="eq:c78-background-ward"></span>

$$
0=-\int d^4x\,\frac{\delta\Gamma_{\rm bg}}{\delta\bar A_\mu^a}
                 (\bar D_\mu\theta)^a
=\int d^4x\,\theta^a\bar D_\mu^{ab}
                 \frac{\delta\Gamma_{\rm bg}}{\delta\bar A_\mu^b}.
\tag{78.8}
$$

这一沃德恒等式约束了紫外反项。对本节的四维可重整理论，CP偶的纯背景动能反项须与$\bar F^2$成正比；它展开后的二、三、四点项同乘一个系数。有限量子作用量还可含非局域项，但求耦合重整化只需上述局域极部。

为了和第73节普通量子规范场的归一区别，把背景场归一因子记为$Z_B$。背景裸场与耦合应组合成同一个协变导数，因此

<span id="eq:c78-bare-background"></span>

$$
\begin{gathered}
\bar A_{0\mu}=Z_B^{1/2}\bar A_\mu,\qquad
g_0\bar A_{0\mu}=g_d\bar A_\mu,\qquad
g_d=g\widetilde\mu^{\epsilon/2},\\
g_0=Z_B^{-1/2}g\widetilde\mu^{\epsilon/2},\qquad
\bar F_{0\mu\nu}=Z_B^{1/2}\bar F_{\mu\nu},\qquad
g_0^2=Z_B^{-1}g^2\widetilde\mu^\epsilon .
\end{gathered}
\tag{78.9}
$$

场强中导数项和二次背景项具有同一个$Z_B^{1/2}$，恰好需要第二个关系。例如二次项给
$g_0\bar A_0\bar A_0=Z_B^{1/2}g_d\bar A\bar A$。这样$-\bar F_0^2/4$展开后的各背景顶角自动共用$Z_B$。

物质项也有相同特点。将$\Psi_0=Z_\Psi^{1/2}\Psi$代入裸动能，再用[（78.9）](#eq:c78-bare-background)，得到
$Z_\Psi\bar\Psi i\gamma^\mu(\partial_\mu-ig_d\bar A_\mu^aT_R^a)\Psi$，动能与一个背景场顶角同乘$Z_\Psi$。鬼动能则整体乘$Z_c$，其中一个、两个背景场顶角随它共同重整化。因此，背景顶角与相应动能项的重整化因子满足

<span id="eq:c78-background-z-identities"></span>

$$
Z_1=Z_2,\qquad Z_1'=Z_2',\qquad
Z_3=Z_{3g}=Z_{4g}=Z_B
\quad\text{（背景外腿）}.
\tag{78.10}
$$

量子涨落$q$可以有另一个归一系数$Z_q$，含量子外腿的顶角也另有相应关系。这里之所以简化，是因为所求$\Gamma_{\rm bg}$的外腿全是背景场。由[（78.9）](#eq:c78-bare-background)，只要算出背景二点函数的$Z_B$，就能求出$g$的贝塔函数。

<span id="c78-quadratic"></span>

## 一圈只需二次涨落

下面实施平移$A=\bar A+q$。平移的雅可比因子为一；背景不再出现在自由积分变量中，而是作为外部插入进入顶角。若把$\bar A$设为零，传播子和纯量子顶角立即回到第72节的$R_\xi$规则。带背景外腿的顶角还得到规范固定项和鬼项的贡献，下面将从这些附加项求出完整规则。

先展开场强。把含一个$q$和两个$q$的部分分别记为$Q,H$，直接由[（78.1）](#eq:c78-action)得到

<span id="eq:c78-strength-expansion"></span>

$$
\begin{gathered}
F_{\mu\nu}^a=\bar F_{\mu\nu}^a+Q_{\mu\nu}^a+H_{\mu\nu}^a,\\
Q_{\mu\nu}^a=(\bar D_\mu q_\nu)^a-(\bar D_\nu q_\mu)^a,
\qquad H_{\mu\nu}^a=gf^{abc}q_\mu^bq_\nu^c,\\
\mathcal L_{\rm gf}=-\frac1{2\xi}(\bar D^\mu q_\mu)^a
                                     (\bar D^\nu q_\nu)^a .
\end{gathered}
\tag{78.11}
$$

两个含$\bar A q$的交叉项恰好组成$\bar Dq$。平方时把各次数保留到最后，得到

<span id="eq:c78-all-powers"></span>

$$
-\frac14F^2
=-\frac14\bar F^2-\frac12\bar FQ
-\frac14Q^2-\frac12\bar FH
-\frac12QH-\frac14H^2 .
\tag{78.12}
$$

一次项$-\bar FQ/2$经分部积分给$\int q_\nu^a(\bar D_\mu\bar F^{\mu\nu})^a$。任意背景一般不满足经典场方程，所以它并不自行消失。我们计算的是固定$\widehat q=0$的勒让德有效作用量；[（78.6）](#eq:c78-legendre)中的树级源正是
$J^{a\nu}=-(\bar D_\mu\bar F^{\mu\nu})^a$，它抵消这个一次项。图形上，一个只有一条量子腿的顶角通过单条桥边连到其余部分，属于1PI构造已经排除的可约贡献。

三次和四次量子项为何也不用保留？对没有量子外腿的连通背景图，若顶角$v$带$n_v$条量子内腿，则

<span id="eq:c78-loop-counting"></span>

$$
2I=\sum_v n_v,\qquad
L=I-V+1=1+\frac12\sum_v(n_v-2).
\tag{78.13}
$$

一次顶角已由勒让德构造去除，因此$n_v\ge2$。要使$L=1$，每个顶角都必须恰有两条量子腿。背景外腿的个数不受这个计数限制。于是$QH$、$H^2$以及鬼项中的$\bar cqc$都不进入当前的一圈$\Gamma_{\rm bg}$。保留的杨—米尔斯二次项为

<span id="eq:c78-quadratic-before-ibp"></span>

$$
\begin{aligned}
\mathcal L_{{\rm YM},2}
={}&-\frac12(\bar D^\mu q^\nu)^a(\bar D_\mu q_\nu)^a
 +\frac12(\bar D^\mu q^\nu)^a(\bar D_\nu q_\mu)^a\\
&-\frac g2f^{abc}\bar F^{a\mu\nu}q_\mu^bq_\nu^c .
\end{aligned}
\tag{78.14}
$$

第一行来自$-Q^2/4$；$Q$的两个反对称项给两个相同的平方项及两个交叉项。最后一行则来自$-\bar FH/2$。因此，被略去的高次量子项只在更高圈的背景图中出现。

交叉导数项还能提供另一个场强耦合。把两次分部积分明确写在积分内：

<span id="eq:c78-ibp"></span>

$$
\begin{aligned}
&\int d^dx\,(\bar D^\mu q^\nu)^a(\bar D_\nu q_\mu)^a\\
&=-\int d^dx\,q_\mu^b(\bar D^\nu\bar D^\mu)^{bc}q_\nu^c\\
&=\int d^dx\left[-q_\mu^b(\bar D^\mu\bar D^\nu)^{bc}q_\nu^c
                   +q_\mu^b[\bar D^\mu,\bar D^\nu]^{bc}q_\nu^c\right]\\
&=\int d^dx\left[(\bar D^\mu q_\mu)^a(\bar D^\nu q_\nu)^a
                   -gf^{abc}\bar F^{a\mu\nu}q_\mu^bq_\nu^c\right].
\end{aligned}
\tag{78.15}
$$

这里$[\bar D^\mu,\bar D^\nu]=-igT_A^a\bar F^{a\mu\nu}$，而$-i(T_A^a)^{bc}=-f^{abc}$，所以最后一项的号是负的。乘回[（78.14）](#eq:c78-quadratic-before-ibp)交叉项的$1/2$，它与原有$-g/2$相加成$-g$。规范固定项又与散度平方合并，二次密度成为

<span id="eq:c78-general-quadratic"></span>

$$
\begin{aligned}
\mathcal L_2\doteq{}&
-\frac12(\bar D^\mu q^\nu)^a(\bar D_\mu q_\nu)^a
 +\frac12(1-\xi^{-1})(\bar D^\mu q_\mu)^a(\bar D^\nu q_\nu)^a\\
&-gf^{abc}\bar F^{a\mu\nu}q_\mu^bq_\nu^c
 -(\bar D^\mu\bar c)^a(\bar D_\mu c)^a .
\end{aligned}
\tag{78.16}
$$

现在取背景费曼规范$\xi=1$。散度平方消失，只剩一个标量型协变拉普拉斯算符和一个不含量子场导数的自旋势。加上背景树项，用于一圈计算的密度便是

<span id="eq:c78-minimal-density"></span>

$$
\begin{aligned}
\mathcal L_{\rm bg,1}
={}&-\frac14Z_B\bar F_{\mu\nu}^a\bar F^{a\mu\nu}
 -\frac12(\bar D^\mu q^\nu)^a(\bar D_\mu q_\nu)^a\\
&-gf^{abc}\bar F^{a\mu\nu}q_\mu^bq_\nu^c
 -(\bar D^\mu\bar c)^a(\bar D_\mu c)^a .
\end{aligned}
\tag{78.17}
$$

即使在内部$q$二次项前保留共同的$Z_q$，也可把$q$作常数缩放以消去它：一圈每个顶角有两条$q$腿，一个环上的顶角数与内线数相等，顶角和传播子的缩放因子成对抵消。等价地，$\operatorname{Tr}\ln(Z_qK)=\operatorname{Tr}\ln K+\operatorname{Tr}\ln Z_q$，后一项只影响背景无关的归一。无外鬼时鬼的常数归一也一样。因此背景树项的$Z_B$要保留，内部共同归一却不影响下面所求的背景依赖。

为便于认识自旋势，把矢量二次核升一个洛伦兹指标，写成作用在$q_\beta^c$上的算符：

<span id="eq:c78-vector-kernel"></span>

$$
\mathscr K_{b\alpha}{}^{c\beta}
=(\bar D^2)^{bc}\delta_\alpha{}^\beta
 -2ig(T_A^a)^{bc}\bar F_\alpha{}^{a\beta}.
\tag{78.18}
$$

它来自双线性型的核$g_{\alpha\beta}(\bar D^2)^{bc}
-2gf^{abc}\bar F_{\alpha\beta}^a$。先升指标再作矩阵乘法，洛伦兹迹就是$\delta_\alpha{}^\alpha=d$。后面将用这个算符计算高斯积分。

<span id="c78-minimal-loops"></span>

## 鬼圈与标量型的规范场涨落

[（78.17）](#eq:c78-minimal-density)把一圈问题分成了三个拓扑，如[图78.1](#fig:c78-background-loops)。前两图来自$\bar D^2$：展开协变导数时，有一个背景场的三点顶角，也有两个背景场的海鸥顶角。右图则由两个自旋场强插入组成。先看最小耦合的两图，再单独计算自旋项。

![第 78 节的场论图示](/images/srednicki/s78_background_loops.svg)

背景场一圈修正的三种拓扑。左、中图的虚内线分别可取鬼场或量子矢量场的最小动能部分，波浪外腿是$\bar A$。右图两黑点各代表一个$\bar Fqq$插入，波浪内线是$q$，没有外部传播子。为说明非零外动量的计算，左图标出两内线动量；右图的两个场强插入也先取相反的非零动量。

<span id="fig:c78-background-loops"></span>

<span id="c78-mixed-vertices"></span>

### 六类含背景场的混合顶角

先保留一般的非零$\xi$求规则，再取一圈计算所需的$\xi=1$。以下动量全流入顶角，局部傅里叶因子为$e^{ikx}$，导数给$ik_\mu$。顶角核按上指标场作泛函微分，所有洛伦兹指标均取下标，省去共同的$(2\pi)^4\delta^{(4)}(\sum k)$。图中使用的$iV$已含作用量指数的$i$；进入圈积分时统一将$g$恢复成$g_d$。

先看胶子顶角。将$A=\bar A+q$代入杨—米尔斯密度，三价和四价系数仍由[第72节的场收缩](/posts/srednicki-72/#c72-three)给出，只是外腿现在分别标明$\bar A$或$q$。新的贡献来自

<span id="eq:c78-ex-gf-expansion"></span>

$$
\begin{aligned}
\mathcal L_{\rm gf}
={}&-\frac1{2\xi}(\partial\cdot q^e)^2\\
&-\frac g\xi f^{eac}(\partial\cdot q^e)
                    \bar A^{a\mu}q_\mu^c\\
&-\frac{g^2}{2\xi}f^{eac}f^{ebd}
             \bar A_\mu^a q^{c\mu}\bar A_\nu^bq^{d\nu}.
\end{aligned}
\tag{78.37}
$$

这里交叉项的2抵消了前面的$1/2$。由于$G$对$q$是一次的，规范固定只增加$\bar A q^2$和$\bar A^2q^2$两类顶角。

在三点顶角上，依次放置$\bar A^{a\mu}(k)$、$q^{b\nu}(p)$、$q^{c\rho}(r)$，其中$k+p+r=0$。杨—米尔斯项给出

<span id="eq:c78-ex-three-ym"></span>

$$
iV_{\rm YM}
 =-g f^{abc}\big[
 (p-r)_\mu g_{\nu\rho}
 +(r-k)_\nu g_{\rho\mu}
 +(k-p)_\rho g_{\mu\nu}\big].
\tag{78.38}
$$

规范固定的交叉项中，被微分的$q$有两种分配。若它接$(b,\nu,p)$，则$f^{bac}=-f^{abc}$；若它接$(c,\rho,r)$，则$f^{cab}=f^{abc}$。把导数和指数中的$i$一起算入，分别得到

<span id="eq:c78-ex-three-gf-assignments"></span>

$$
\begin{aligned}
i\!\left(-\frac g\xi\right)f^{bac}(ip_\nu)g_{\mu\rho}
 &=-\frac g\xi f^{abc}p_\nu g_{\mu\rho},\\
i\!\left(-\frac g\xi\right)f^{cab}(ir_\rho)g_{\mu\nu}
 &=+\frac g\xi f^{abc}r_\rho g_{\mu\nu}.
\end{aligned}
\tag{78.39}
$$

所以完整的背景三胶子顶角是

<span id="eq:c78-ex-background-three"></span>

$$
\begin{aligned}
iV_{\bar Aqq,\mu\nu\rho}^{abc}(k,p,r)
&=-g f^{abc}\Big[
 (p-r)_\mu g_{\nu\rho}
 +(r-k)_\nu g_{\rho\mu}\\
&\qquad +(k-p)_\rho g_{\mu\nu}
 +\xi^{-1}
   (p_\nu g_{\mu\rho}-r_\rho g_{\mu\nu})\Big].
\end{aligned}
\tag{78.40}
$$

两个$q$的完整标签互换时，括号和$f^{abc}$各反号，顶角保持不变。

在$\xi=1$时，用$k+p+r=0$整理后两项，得到

<span id="eq:c78-bqq-vertex"></span>

$$
iV_{\mu\nu\rho}^{abc}
=-gf^{abc}\left[
 (p-r)_\mu g_{\nu\rho}
 +2k_\rho g_{\mu\nu}-2k_\nu g_{\mu\rho}\right]
\qquad(\xi=1).
\tag{78.19}
$$

其中$(p-r)_\mu g_{\nu\rho}$来自最小动能，另两项来自自旋势。收缩背景动量时，自旋两项相消，$k\cdot(p-r)=-p^2+r^2$，所以

<span id="eq:c78-vertex-ward"></span>

$$
k^\mu iV_{\mu\nu\rho}^{abc}
=gf^{abc}(p^2-r^2)g_{\nu\rho}.
\tag{78.20}
$$

这正是两条自由最小量子逆核之差。背景对称性在单个树顶角上已有明确的表现。

还可以不令$\xi=1$而收缩背景动量。定义去掉颜色单位阵的自由逆核

<span id="eq:c78-ex-background-three-ward"></span>

$$
\begin{aligned}
K_{\nu\rho}(p)
 &=p^2g_{\nu\rho}-(1-\xi^{-1})p_\nu p_\rho,\\
k^\mu iV_{\bar Aqq,\mu\nu\rho}^{abc}
 &=-g f^{abc}\big[K_{\nu\rho}(r)-K_{\nu\rho}(p)\big].
\end{aligned}
\tag{78.41}
$$

直接验证时，$k\cdot(p-r)=r^2-p^2$，而剩余的纵向部分由
$p_\nu k_\rho-r_\rho k_\nu=r_\nu r_\rho-p_\nu p_\rho$给出。背景腿的收缩因而等于两条量子腿逆核之差。

四点杨—米尔斯顶角没有动量。为同时表示两种外腿分配，记

<span id="eq:c78-ex-four-tensor"></span>

$$
\begin{aligned}
\mathcal Q_{\mu\nu\rho\sigma}^{abcd}
={}&f^{abe}f^{cde}
 (g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})\\
&+f^{ace}f^{bde}
 (g_{\mu\nu}g_{\rho\sigma}-g_{\mu\sigma}g_{\nu\rho})\\
&+f^{ade}f^{bce}
 (g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}).
\end{aligned}
\tag{78.42}
$$

第72节已经从$-g^2f^{abe}f^{cde}A_\mu^aA_\nu^bA^{c\mu}A^{d\nu}/4$的24种分配得到$iV_{\rm YM,4}=-ig^2\mathcal Q$。把其中两条腿指定为背景时，场展开中有$\binom42=6$种位置选择，而两条背景腿及两条量子腿各有$2!$种收缩，仍是$6\times2!\times2!=24$种。因此这一部分的顶角不再附加二分之一。

令四条腿依次为$\bar A^{a\mu}$、$\bar A^{b\nu}$、$q^{c\rho}$、$q^{d\sigma}$。[（78.37）](#eq:c78-ex-gf-expansion)最后一项中，每个背景场与同一括号内的$q$相接。有两种配对，每种配对又有两个相等的分配：

<span id="eq:c78-ex-four-gf-assignments"></span>

$$
\begin{aligned}
(\bar A^a,q^c)(\bar A^b,q^d)
 &:\quad2f^{eac}f^{ebd}g_{\mu\rho}g_{\nu\sigma},\\
(\bar A^a,q^d)(\bar A^b,q^c)
 &:\quad2f^{ead}f^{ebc}g_{\mu\sigma}g_{\nu\rho}.
\end{aligned}
\tag{78.43}
$$

这些2恰好抵消密度中的$1/2$，故

<span id="eq:c78-ex-background-four"></span>

$$
\begin{aligned}
iV_{\bar A\bar Aqq,\mu\nu\rho\sigma}^{abcd}
&=-ig^2\Big[
 \mathcal Q_{\mu\nu\rho\sigma}^{abcd}\\
&\qquad +\xi^{-1}\big(
 f^{ace}f^{bde}g_{\mu\rho}g_{\nu\sigma}
 +f^{ade}f^{bce}g_{\mu\sigma}g_{\nu\rho}
 \big)\Big].
\end{aligned}
\tag{78.44}
$$

这个表达式分别对两条背景腿和两条量子腿的交换对称。若只有第一条腿是背景，另外三条都是$q$，规范固定项不能贡献；杨—米尔斯展开的$4\times3!$种分配给出

<span id="eq:c78-ex-background-three-quantum"></span>

$$
iV_{\bar Aqqq,\mu\nu\rho\sigma}^{abcd}
 =-ig^2\mathcal Q_{\mu\nu\rho\sigma}^{abcd}.
\tag{78.45}
$$

接着看鬼场。鬼线是有向的，保留反鬼在前、鬼在后的$\bar c^i c^j$次序，就能把每一条线上色矩阵的行、列固定下来。为展开鬼密度$-(\bar D_\mu\bar c)^a(D^\mu c)^a$，引入偶矩阵
$\mathcal B_\mu=-igT^a\bar A_\mu^a$和
$\mathcal C_\mu=-igT^a q_\mu^a$。它们在伴随颜色指标上均为反对称矩阵，于是

<span id="eq:c78-ex-ghost-expansion"></span>

$$
\begin{aligned}
\mathcal L_{\rm gh}
={}&-\partial_\mu\bar c^{\,T}\partial^\mu c
 -\partial_\mu\bar c^{\,T}\mathcal B^\mu c
 +\bar c^{\,T}\mathcal B_\mu\partial^\mu c
 +\bar c^{\,T}\mathcal B_\mu\mathcal B^\mu c\\
&-\partial_\mu\bar c^{\,T}\mathcal C^\mu c
 +\bar c^{\,T}\mathcal B_\mu\mathcal C^\mu c .
\end{aligned}
\tag{78.46}
$$

这里的转置符号$T$与生成元$T^a$的颜色标签无关。推导例如第二个含导数的背景项时，
$-(\mathcal B_\mu\bar c)^T\partial^\mu c
=-\bar c^T\mathcal B_\mu^T\partial^\mu c
=+\bar c^T\mathcal B_\mu\partial^\mu c$；
偶矩阵的移动没有交换两个鬼变量。

含一条背景线的两个导数项合起来是

<span id="eq:c78-ex-background-ghost-density"></span>

$$
\mathcal L_{\bar A\bar c c}
=ig\bar A_\mu^a
\big[(\partial^\mu\bar c^i)(T^a)_{ij}c^j
       -\bar c^i(T^a)_{ij}\partial^\mu c^j\big].
\tag{78.47}
$$

对$\bar A^{a\mu}(k)$、$\bar c^i(r)$、$c^j(s)$取$k+r+s=0$。两个导数分别给$ir_\mu$和$is_\mu$，从而

<span id="eq:c78-ex-background-ghost-three"></span>

$$
\begin{aligned}
iV_{\bar A\bar cc,\mu}^{a;ij}(k,r,s)
 &=-ig(T^a)_{ij}(r-s)_\mu\\
 &=-g f^{aij}(r-s)_\mu .
\end{aligned}
\tag{78.48}
$$

相比之下，[（78.46）](#eq:c78-ex-ghost-expansion)中只含$q$的导数项只有反鬼被微分，给出$-ig(T^a)_{ij}r_\mu$，正好还原第72节的普通鬼顶角。背景势在两个协变导数中都出现，所以背景顶角含两个端点动量之差。

余下两种鬼顶角由没有导数的项给出：

<span id="eq:c78-ex-ghost-four-densities"></span>

$$
\begin{aligned}
\mathcal L_{\bar A\bar A\bar cc}
 &=-g^2\bar c^i(T^aT^b)_{ij}c^j
                  \bar A_\mu^a\bar A^{b\mu},\\
\mathcal L_{\bar A q\bar cc}
 &=-g^2\bar c^i(T^aT^b)_{ij}c^j
                  \bar A_\mu^a q^{b\mu}.
\end{aligned}
\tag{78.49}
$$

第一行的两条背景腿可以交换位置，必须把$T^aT^b$与$T^bT^a$相加：

<span id="eq:c78-ex-background-ghost-four"></span>

$$
iV_{\bar A\bar A\bar cc,\mu\nu}^{ab;ij}
 =-ig^2\{T^a,T^b\}_{ij}g_{\mu\nu}.
\tag{78.50}
$$

第二行的背景场来自作用在反鬼一侧的$\bar D$，量子场来自作用在鬼一侧的$D$。两者的角色已由作用量规定，因而结果保留有序乘积

<span id="eq:c78-ex-mixed-ghost-four"></span>

$$
iV_{\bar A q\bar cc,\mu\nu}^{ab;ij}
 =-ig^2(T^aT^b)_{ij}g_{\mu\nu}.
\tag{78.51}
$$

这项没有第二种背景、量子交换收缩。作为一个具体例子，取$SU(2)$的伴随生成元$(T^a)_{bc}=-i\epsilon^{abc}$，以$E_{ij}$记矩阵单位，则

<span id="eq:c78-ex-ghost-order-example"></span>

$$
T^1T^2=-E_{21},\qquad
T^2T^1=-E_{12},\qquad
[T^1,T^2]=iT^3=E_{12}-E_{21}.
\tag{78.52}
$$

这个有序乘积因此确定了颜色流。[（78.50）](#eq:c78-ex-background-ghost-four)的反对易子则确实是两条相同背景腿所要求的结果。

共有三类胶子顶角和三类鬼顶角。杨—米尔斯密度至多四次，规范固定至多含两个$q$，鬼密度至多含两个规范场，故满足“至少一条背景腿、至少两条量子腿”的顶角均已列出。其中$\bar A q^3$和$\bar A q\bar c c$各有三条量子腿；另外四类各有两条量子腿。按[（78.13）](#eq:c78-loop-counting)的圈数关系，一圈只用$n_v=2$的顶点，正是[图78.1](#fig:c78-background-loops)采用的四类规则。

### 最小动能部分的二点核

计算二点函数时仍用第73节的定义，

<span id="eq:c78-polarization-convention"></span>

$$
\Pi_{\mu\nu}^{ab}(k)
=\delta^{ab}(k^2g_{\mu\nu}-k_\mu k_\nu)\Pi(k^2),
\qquad
\Pi_{\rm ct}(k^2)=-(Z_B-1).
\tag{78.21}
$$

实际插入为$i\Pi_{\mu\nu}^{ab}$。反项的负号可直接从$-\delta Z_B\bar F^2/4$的二次部分看出：对两个背景场取导数，所得正是$-i\delta Z_B(k^2g_{\mu\nu}-k_\mu k_\nu)\delta^{ab}$。

[第73节](/posts/srednicki-73/#c73-scalar)已把复标量泡和海鸥相加，求得横向核。这里只需把其表示换成当前内部场的表示。保留相同的极点处方与工程因子，复标量贡献为

<span id="eq:c78-scalar-input"></span>

$$
\begin{aligned}
\Pi_{\rm CS}(k^2)
&=-\frac{g^2T(R_{\rm CS})}{i}
 \int_0^1dx\,(1-2x)^2J_2\bigl(m_s^2+x(1-x)k^2\bigr),\\
J_2(D)
&=\frac{i}{16\pi^2}
 \left[\frac2\epsilon-\ln\frac{D-i0}{\mu^2}+O(\epsilon)\right],\\
\int_0^1(1-2x)^2dx
&=\left[x-2x^2+\frac43x^3\right]_0^1=\frac13,\\
\Pi_{\rm CS}\big|_{\rm UV}
&=-\frac{g^2T(R_{\rm CS})}{24\pi^2\epsilon}.
\end{aligned}
\tag{78.22}
$$

分母积分和横向组合沿用前节的结果，参数权重积分给$1/3$。紫外极点与$m_s$无关，质量只进入有限部分。下面的鬼场和$q$都是无质量的；取$k^2>0$可以在求极点时保持离壳。

鬼由两套独立的格拉斯曼变量构成，闭圈比复标量多一个负号。因此把$R_{\rm CS}$换成伴随表示，再反号，便得到鬼圈贡献：

<span id="eq:c78-ghost-pole"></span>

$$
\Pi_{\rm gh}\big|_{\rm UV}
=+\frac{g^2C_A}{24\pi^2\epsilon},
\qquad C_A=T(A).
\tag{78.23}
$$

复标量的粒子与反粒子已包含在同一个复场中，鬼也按这一整套核比较，不再多乘二。图中海鸥在当前无质量维数正规化下正比于$\int d^d\ell/\ell^2$，是无尺度积分，因而为零。它仍属于从协变动能展开得到的完整规则，在引入质量的其他红外整理中不能预先删去。

暂不考虑自旋势，$q_\nu$的每个洛伦兹分量都有实标量型的动能。沿圈缩并这个附加指标给$d$；每个实场相对于复场有一个$1/2$，也就是交换两条相同实内线的对称因子。因此，量子矢量的最小动能部分给出

<span id="eq:c78-orbital-pole"></span>

$$
\begin{aligned}
\Pi_{\rm orb}\big|_{\rm pole}
&=\left.\frac d2\,\Pi_{\rm CS}\right|_{R_{\rm CS}=A,\ {\rm pole}},\\
\frac{4-\epsilon}{2}
 \left(-\frac{g^2C_A}{24\pi^2\epsilon}\right)
&=-\frac{g^2C_A}{12\pi^2\epsilon}
  +\frac{g^2C_A}{48\pi^2}.
\end{aligned}
\tag{78.24}
$$

第二行的有限项来自$d-4$乘极点；因此求极点留数时可取$d=4$，求有限部分时须保留$d$。升起一个指标后，洛伦兹迹为$\delta_\nu{}^\nu=d$。鬼与轨道部分合起来，在$g^2C_A/(24\pi^2\epsilon)$单位下给$1-2=-1$。要得到完整规范场贡献，还须计入[（78.18）](#eq:c78-vector-kernel)的自旋势。

<span id="c78-spin-loop"></span>

## 自旋与场强耦合产生的紫外项

把$\bar F$当作外源，可以直接计算[图78.1](#fig:c78-background-loops)右侧的真空泡。由
$-gf^{abc}\bar F^{a\mu\nu}q_\mu^bq_\nu^c$对两个$q$求导时，同时交换$(b,\mu)$与$(c,\nu)$，结构常数和场强各反号，乘积不变；两个槽给相同贡献。因此场强插入的图因子是

<span id="eq:c78-spin-vertex"></span>

$$
\mathcal V_{\mu\nu}^{bc}[\bar F]
=-2igf^{abc}\bar F_{\mu\nu}^a.
\tag{78.25}
$$

两次插入的真空图除以$S=2\times2=4$。一个二来自交换两条相同的实内线，另一个二来自交换两个相同类型的外源，也可从指数展开的$2!$得到。把所有因子分别算出，

<span id="eq:c78-spin-factors"></span>

$$
\begin{gathered}
\frac14(-2ig)^2\left(\frac1i\right)^2=+g^2,\\
\operatorname{Tr}(T_A^aT_A^b)
=(-i)^2f^{acd}f^{bdc}
=f^{acd}f^{bcd}=C_A\delta^{ab}.
\end{gathered}
\tag{78.26}
$$

第一行的两个$1/i$来自两条内线，第二行用了$f^{bdc}=-f^{bcd}$。洛伦兹收缩则把两场强变成$\bar F_{\mu\nu}^a\bar F^{a\mu\nu}$，所以所余困难只有一个对数发散积分。

取两个场强插入的动量为$k$和$-k$，并令$k^2>0$。这一离壳选择控制了红外端点，使紫外极点可以单独提取。若先取常场，得到的无尺度积分$\int d^d\ell/(\ell^2)^2$会把紫外与红外极点一并抵消。所需积分为

<span id="eq:c78-offshell-bubble"></span>

$$
I(k)=\widetilde\mu^\epsilon
 \int\frac{d^d\ell}{(2\pi)^d}
 \frac1{(\ell^2-i0)((\ell+k)^2-i0)},
\qquad d=4-\epsilon .
\tag{78.27}
$$

在$0<\operatorname{Re}\epsilon<2$时，紫外区域和两个无质量内线端点都可积；所得函数再解析延拓到$\epsilon=0$附近。使用$1/(ab)=\int_0^1dx/[xa+(1-x)b]^2$，分母中完成平方：

<span id="eq:c78-bubble-parameter"></span>

$$
\begin{aligned}
x\ell^2+(1-x)(\ell+k)^2
&=[\ell+(1-x)k]^2+x(1-x)k^2,\\
I(k)
&=\widetilde\mu^\epsilon\int_0^1dx
 \int\frac{d^dL}{(2\pi)^d}
 \frac1{[L^2+x(1-x)k^2-i0]^2}.
\end{aligned}
\tag{78.28}
$$

平移$L=\ell+(1-x)k$的雅可比因子为一。在共同费曼处方下作威克旋转，积分测度给一个$i$；第62、73节已求出的欧氏径向$\Gamma$函数积分可直接用于这里的正量$D=x(1-x)k^2$。再把参数积分真正求完，得到

<span id="eq:c78-bubble-evaluated"></span>

$$
\begin{aligned}
I(k)
&=\frac{i\widetilde\mu^\epsilon}{(4\pi)^{2-\epsilon/2}}
 \Gamma(\epsilon/2)(k^2)^{-\epsilon/2}
 \int_0^1dx\,[x(1-x)]^{-\epsilon/2}\\
&=\frac{i\widetilde\mu^\epsilon}{(4\pi)^{2-\epsilon/2}}
 \frac{\Gamma(\epsilon/2)\Gamma(1-\epsilon/2)^2}
      {\Gamma(2-\epsilon)}(k^2)^{-\epsilon/2}\\
&=\frac{i}{16\pi^2}
 \left[\frac2\epsilon-\ln\frac{k^2}{\mu^2}+2+O(\epsilon)\right].
\end{aligned}
\tag{78.29}
$$

第二行用了贝塔函数积分$B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$，此处$a=b=1-\epsilon/2$。最后一行也可直接展开参数式核对：$\Gamma(\epsilon/2)=2/\epsilon-\gamma_E+\cdots$，尺度因子提供$\ln(4\pi\widetilde\mu^2/k^2)$，而
$\int_0^1\ln[x(1-x)]dx=-2$。用$\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2$合并常数，恰好得到显示的有限项。

因此紫外留数是$i/(8\pi^2)$，与非零$k$无关。此时才把这个极部写成局域的场强平方，或者在它的系数中取常场极限。将[（78.26）](#eq:c78-spin-factors)的因子与这一积分相乘，得到：

<span id="eq:c78-spin-effective-action"></span>

$$
\begin{aligned}
\frac{i\Gamma_{\rm spin}^{\rm UV}}{VT}
&=\frac14(-2ig)^2\left(\frac1i\right)^2
 f^{acd}f^{bcd}\bar F_{\mu\nu}^a\bar F^{b\mu\nu}
 \frac{i}{8\pi^2\epsilon}\\
&=\frac{ig^2C_A}{8\pi^2\epsilon}\bar F_{\mu\nu}^a\bar F^{a\mu\nu}.
\end{aligned}
\tag{78.30}
$$

$VT$是取常场后的时空体积。这个局域写法只用于极部；[（78.29）](#eq:c78-bubble-evaluated)中的$\ln k^2$还保存着有限作用量的非局域信息，不能一起令$k=0$。

现在将有效作用量密度转成[（78.21）](#eq:c78-polarization-convention)的$\Pi$。由[（78.30）](#eq:c78-spin-effective-action)可知$\Gamma$中有正的
$g^2C_A\bar F^2/(8\pi^2\epsilon)$。若一个二点圈的标量系数为$\Pi_{\rm loop}$，相应局域作用量是$+\Pi_{\rm loop}\bar F^2/4$；它与反项$-\delta Z_B\bar F^2/4$相消。因此场强平方系数须乘四，得到

<span id="eq:c78-spin-pole"></span>

$$
\Pi_{\rm spin}\big|_{\rm UV}
=\frac{g^2C_A}{2\pi^2\epsilon}
=\frac{g^2}{24\pi^2\epsilon}\,12C_A .
\tag{78.31}
$$

还可能画出一个最小顶角和一个自旋顶角的混合泡。最小项在洛伦兹空间为单位阵，自旋项为$\bar F_\alpha{}^\beta$，所以闭圈给$\bar F_\alpha{}^\alpha=0$。只含一次自旋插入的圈也因同一迹而为零。这两个零在积分之前已由反对称指标决定，与无尺度积分归零的理由不同。至此，[图78.1](#fig:c78-background-loops)包含的一圈贡献已经全部确定。

<span id="c78-determinants"></span>

## 用高斯积分合并一圈图

二次涨落还能把上述图形统一写成四个行列式。取$\xi=1$，量子场、鬼场和物质场的平均值均为零；背景的一次项由[（78.6）](#eq:c78-legendre)中的源抵消。先考虑无质量物质。

把矢量生成元的第二个指标升起后，[（78.18）](#eq:c78-vector-kernel)的二次核可写成

<span id="eq:c78-ex-vector-lorentz-generator"></span>

$$
\begin{aligned}
(S_v^{\mu\nu})_\alpha{}^\beta
 &=-i(\delta^\mu{}_\alpha g^{\nu\beta}
            -\delta^\nu{}_\alpha g^{\mu\beta}),\\
gT^a\bar F_{\mu\nu}^a(S_v^{\mu\nu})_\alpha{}^\beta
 &=-2igT^a\bar F_\alpha{}^{a\beta},\\
\mathscr K&=\bar D_A^2 I_v
                  +gT_A^a\bar F_{\mu\nu}^aS_v^{\mu\nu}.
\end{aligned}
\tag{78.53}
$$

这把矢量表示$(2,2)$中的自旋耦合显式写了出来。若保留一般$\xi$，[（78.18）](#eq:c78-vector-kernel)还会多出
$-(1-\xi^{-1})(\bar D_\alpha\bar D^\beta)^{bc}$；
这些协变导数按所写次序作用。只有$\xi=1$时才得到这一最小矢量算符。

鬼场和无质量复标量的二次型更直接。把导数移到右边后，它们与狄拉克二次型一起写成

<span id="eq:c78-ex-matter-quadratic-actions"></span>

$$
\begin{aligned}
\bar D_{R\mu}
 &=\partial_\mu-igT_R^a\bar A_\mu^a,\\
S_{{\rm gh},2}&=\int d^4x\,\bar c^a(\bar D_A^2)^{ab}c^b,\\
S_{{\rm CS},2}&=\int d^4x\,\phi^\dagger\bar D_{R_{\rm CS}}^2\phi,\\
S_{{\rm DF},2}&=\int d^4x\,\bar\Psi Q_D\Psi,
\qquad Q_D=i\gamma^\mu\bar D_\mu .
\end{aligned}
\tag{78.54}
$$

标量与鬼场都取洛伦兹标量表示，故$S_{(1,1)}^{\mu\nu}=0$。表示$R$的生成元作用于颜色空间，洛伦兹生成元作用于另一个因子；这两个矩阵空间之间可交换。$\bar D$与背景场的乘法算符之间则仍须保持次序。

现在对二次型积分。在有限模式调节下，一组实玻色变量、一个复玻色列及一对独立格拉斯曼列分别给出

<span id="eq:c78-ex-finite-gaussians"></span>

$$
\begin{aligned}
\int dx\,e^{\,ix^TKx/2}
 &\propto(\det K)^{-1/2},\\
\int dz^*dz\,e^{\,iz^*Kz}
 &\propto(\det K)^{-1},\\
\int d\bar\eta\,d\eta\,e^{\,i\bar\eta K\eta}
 &\propto\det K.
\end{aligned}
\tag{78.55}
$$

第一行逐实本征模式给一个平方根；第二行的一复模式有两个实积分，平方根合成一次幂。第三行取每一对奇变量的最高次系数，排列求和形成行列式。因此实量子胶子给$-1/2$，复标量给$-1$，鬼与狄拉克场各先给$+1$。其中所有常数、$i$的背景无关幂及零背景真空因子都在归一化比值中消去。

各高斯积分采用共同的费曼处方，在零背景附近取连续的微扰支；零模用同一红外规定处理。

为了与玻色核直接比较，也把狄拉克算符写成二阶形式。用克利福德关系$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$逐步计算：

<span id="eq:c78-ex-dirac-square"></span>

$$
\begin{aligned}
Q_D^2
 &=-\gamma^\mu\gamma^\nu\bar D_\mu\bar D_\nu\\
 &=-\frac12\{\gamma^\mu,\gamma^\nu\}\bar D_\mu\bar D_\nu
   -\frac14[\gamma^\mu,\gamma^\nu]
                   [\bar D_\mu,\bar D_\nu]\\
 &=\bar D^2+\frac{ig}{4}T_R^a\bar F_{\mu\nu}^a
                         [\gamma^\mu,\gamma^\nu]\\
 &=\bar D^2+gT_R^a\bar F_{\mu\nu}^aS_D^{\mu\nu},
\qquad
S_D^{\mu\nu}=\frac i4[\gamma^\mu,\gamma^\nu].
\end{aligned}
\tag{78.56}
$$

最后一行把最小耦合与自旋势分开。平方后的行列式怎样取根，可以在一个连续的、可逆的调节算符族$Q_D(t)$上明确检查：

<span id="eq:c78-ex-dirac-determinant-branch"></span>

$$
\begin{aligned}
\frac d{dt}\operatorname{Tr}\ln Q_D^2
 &=\operatorname{Tr}\!\left[
 Q_D^{-2}(Q_D\dot Q_D+\dot Q_D Q_D)\right]\\
 &=2\operatorname{Tr}(Q_D^{-1}\dot Q_D)
 =2\frac d{dt}\operatorname{Tr}\ln Q_D .
\end{aligned}
\tag{78.57}
$$

两个对数因此相差一个与背景无关的常数。以零背景固定这个常数及连续支，狄拉克行列式成为二阶算符行列式的$+1/2$次幂。

令$\square_{R,L}=\bar D_R^2 I_L+gT_R^a\bar F_{\mu\nu}^aS_L^{\mu\nu}$，便得到一圈背景作用量的行列式形式

<span id="eq:c78-ex-one-loop-determinants"></span>

$$
\begin{aligned}
e^{i\Gamma_1(\bar A,0,0;\bar A)}
\propto{}&
 (\det\square_{A,(1,1)})^{+1}
 (\det\square_{A,(2,2)})^{-1/2}\\
&\times
 (\det\square_{R_{\rm DF},(2,1)\oplus(1,2)})^{+1/2}
 (\det\square_{R_{\rm CS},(1,1)})^{-1}.
\end{aligned}
\tag{78.58}
$$

这里的$(1,1)$、$(2,1)\oplus(1,2)$和$(2,2)$是第33节的洛伦兹表示维数记号。若物质有质量，复标量核变为$\bar D^2-m_s^2$。对这里的向量型狄拉克场，$\gamma_5Q_D\gamma_5=-Q_D$把两个质量符号的行列式联系起来；在选定的参考背景附近，它们只差背景无关号。再用
$(Q_D-m_f)(Q_D+m_f)=Q_D^2-m_f^2$，取相同连续支后相应替换为$\square_D-m_f^2$。这些质量改变完整有限作用量；本节$\bar F^2$的质量无关紫外极部可以在有共同红外控制时单独提取。

最后核对行列式与图解的权重。对[（78.58）](#eq:c78-ex-one-loop-determinants)取对数，$\operatorname{Tr}$同时包括时空、颜色和洛伦兹标签：

<span id="eq:c78-ex-one-loop-traces"></span>

$$
\begin{aligned}
i\Gamma_1
={}&\operatorname{Tr}\ln K_{\rm gh}
 -\frac12\operatorname{Tr}\ln K_v\\
&+\frac12\operatorname{Tr}\ln K_D^{(2)}
 -\operatorname{Tr}\ln K_{\rm CS}
 +\text{背景无关常数}.
\end{aligned}
\tag{78.59}
$$

标量型算符$K_s=\bar D^2$展开到$\bar A^2$，恰好给出两个三点顶角组成的泡图，以及一个四点顶角组成的海鸥图。鬼项与复标量的算符相同而对数系数相反，所以每个闭鬼圈相对复标量多一个负号。矢量最小部分为$K_sI_v$，洛伦兹单位阵的迹给$d$，再乘实场的$1/2$；它相当于$d/2$个复标量。沿$d=4-\epsilon$取极部时才可令$d=4$，被省去的$-\epsilon$只影响有限项。

自旋耦合由$V_F=gT^a\bar F_{\mu\nu}^a S^{\mu\nu}$表示。将$K_sI+V_F$先分解为$K_s(I+K_s^{-1}V_F)$，再取对数，有

<span id="eq:c78-ex-ordered-log-expansion"></span>

$$
\begin{aligned}
\operatorname{Tr}\ln(K_sI+V_F)
={}&\operatorname{Tr}\ln(K_sI)
 +\operatorname{Tr}(K_s^{-1}V_F)\\
&-\frac12\operatorname{Tr}
       (K_s^{-1}V_FK_s^{-1}V_F)+\cdots .
\end{aligned}
\tag{78.60}
$$

时空核与场强相乘的顺序保留在每一项中。单个$V_F$的洛伦兹迹为零，因此一个最小顶角与一个自旋顶角的混合圈也为零。对矢量场，[（78.53）](#eq:c78-ex-vector-lorentz-generator)进一步给出

<span id="eq:c78-ex-vector-spin-trace"></span>

$$
\begin{aligned}
\operatorname{tr}_{A,v}(V_F^2)
 &=(-2ig)^2
   \operatorname{tr}_A(T^aT^b)
       \bar F_\alpha{}^{a\beta}\bar F_\beta{}^{b\alpha}\\
 &=4g^2T(A)\bar F_{\alpha\beta}^a\bar F^{a\alpha\beta}.
\end{aligned}
\tag{78.61}
$$

第二步用了$\bar F_\alpha{}^\beta\bar F_\beta{}^\alpha=-\bar F_{\alpha\beta}\bar F^{\alpha\beta}$。[（78.59）](#eq:c78-ex-one-loop-traces)的$-1/2$乘对数展开的$-1/2$，给两次插入的$+1/4$，对应[图78.1](#fig:c78-background-loops)右图的两个源交换和两条实内线交换。

在两次场强插入这一阶，以自由逆核$K_0^{-1}(\ell)=-1/(\ell^2-i0)$代替$K_s^{-1}$。对数展开中的逆核已经由高斯积分产生，两项的负号相消，得到

$$
i\Gamma_{v,F^2}=\frac14\int\frac{d^4k}{(2\pi)^4}\,I(k)\,\operatorname{tr}[V_F(k)V_F(-k)].
$$

代入[（78.29）](#eq:c78-bubble-evaluated)的极部和上面的矢量自旋迹，正好恢复[（78.30）](#eq:c78-spin-effective-action)的系数，再将场强平方系数乘四得到[（78.31）](#eq:c78-spin-pole)。

狄拉克平方算符可以作同样的检查。沿$\operatorname{tr}_D I=4$的维数续接，先由四个gamma矩阵的迹得到

<span id="eq:c78-ex-dirac-spin-trace"></span>

$$
\begin{aligned}
\operatorname{tr}_D
 [\gamma^\mu,\gamma^\nu][\gamma^\rho,\gamma^\sigma]
 &=16(g^{\mu\sigma}g^{\nu\rho}
              -g^{\mu\rho}g^{\nu\sigma}),\\
\operatorname{tr}_D(S_D^{\mu\nu}S_D^{\rho\sigma})
 &=g^{\mu\rho}g^{\nu\sigma}
              -g^{\mu\sigma}g^{\nu\rho},\\
\operatorname{tr}_{R,D}(V_F^2)
 &=2g^2T(R)\bar F_{\mu\nu}^a\bar F^{a\mu\nu}.
\end{aligned}
\tag{78.62}
$$

第二行的号来自$(i/4)^2=-1/16$，第三行的2来自两个反对称场强的缩并。这次对数前的系数为$+1/2$，两次插入则给$-1/4$，所以

<span id="eq:c78-ex-dirac-spin-pole"></span>

$$
\begin{aligned}
i\Gamma_{D,F^2}\big|_{\rm pole}
 &=-\frac{ig^2T(R)}{16\pi^2\epsilon}\int d^4x\,\bar F^2,\\
\Pi_{D,\rm spin}\big|_{\rm pole}
 &=-\frac{g^2T(R)}{4\pi^2\epsilon}.
\end{aligned}
\tag{78.63}
$$

狄拉克最小算符的迹给4，再乘$+1/2$，相对复标量的$-1$是$-2$倍。将复标量已得的
$\Pi_{\rm CS}|_{\rm pole}=-g^2T(R)/(24\pi^2\epsilon)$代入，最小部分给$+2$单位，自旋部分给$-6$单位，合成$-4$单位，正好还原狄拉克圈的完整贡献。

对于实表示中的马约拉纳场，以$C$记电荷共轭矩阵，高斯积分给普法夫式$\operatorname{Pf}(CQ_D)$，其平方为$\det(CQ_D)$，故连续支上的对数是狄拉克场的一半。实标量的$-1/2$次幂也直接是复标量$-1$次幂的一半。外尔场在两点函数的偶宇称部分保留半个狄拉克迹；含$\gamma_5$的部分在积分后只能正比于$\epsilon^{\mu\nu\rho\sigma}k_\rho k_\sigma=0$。由此得到后面物种计数中的三个半因子。

<span id="c78-beta"></span>

## 合并各场的贡献并求贝塔函数

狄拉克物质圈沿[第73节的夸克闭圈](/posts/srednicki-73/#c73-gluon-counterterm)已经求出的结果，只须将二次群迹换成完整物质表示；复标量圈则由[（78.22）](#eq:c78-scalar-input)给出。为把不同来源放在同一归一下，将紫外极点写成下表。这里$T(R_{\rm DF})$、$T(R_{\rm CS})$对所有相应物种求和，因直和表示的迹等于各块迹之和。

<span id="eq:c78-pole-table"></span>

$$
\begin{array}{c|c}
\text{圈的来源}&
\Pi|_{\rm UV}\big/\bigl[g^2/(24\pi^2\epsilon)\bigr]\\ \hline
\text{伴随鬼}&+C_A\\
\text{量子矢量最小动能}&-2C_A\\
\text{量子矢量自旋势}&+12C_A\\
\text{狄拉克物质}&-4T(R_{\rm DF})\\
\text{复标量物质}&-T(R_{\rm CS})
\end{array}
\tag{78.32}
$$

其中狄拉克项为$-g^2T(R_{\rm DF})/(6\pi^2\epsilon)$。加上$-(Z_B-1)$以后，要求总二点核没有紫外极点，在$\overline{\mathrm{MS}}$方案下得到：

<span id="eq:c78-background-counterterm"></span>

$$
\begin{aligned}
Z_B
&=1+\frac{g^2}{24\pi^2\epsilon}
 \left[(1-2+12)C_A-4T(R_{\rm DF})-T(R_{\rm CS})\right]+O(g^4)\\
&=1+\frac{bg^2}{\epsilon}+O(g^4),\qquad
b=\frac{11C_A-4T(R_{\rm DF})-T(R_{\rm CS})}{24\pi^2}.
\end{aligned}
\tag{78.33}
$$

这里的$\overline{\mathrm{MS}}$尺度已由$\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2$固定。由于用的是$\epsilon=4-d$，极点系数也须沿这一约定保留。

最后固定[（78.9）](#eq:c78-bare-background)中的裸耦合，对$t=\ln\mu$求导。先保留$d$维工程项，记$B_g=dg/dt=-\epsilon g/2+\beta(g)$，则

<span id="eq:c78-beta-derived"></span>

$$
\begin{aligned}
0&=\epsilon+\frac{2B_g}{g}
       -B_g\partial_g\ln Z_B,\\
\partial_g\ln Z_B&=\frac{2bg}{\epsilon}+O(g^3),\\
0&=\frac{2\beta(g)}g
   -\left(-\frac{\epsilon g}{2}\right)\frac{2bg}{\epsilon}
   +O(g^4)
 =\frac{2\beta(g)}g+bg^2+O(g^4),\\
\beta(g)
&=-\frac{g^3}{48\pi^2}
 \left[11C_A-4T(R_{\rm DF})-T(R_{\rm CS})\right]+O(g^5).
\end{aligned}
\tag{78.34}
$$

第三行只保留一圈所需的$g^2$阶；$\beta$乘一圈极点等项从$g^4$起，需要和高圈反项一并处理。有限的$bg^2$正是工程项乘极点留下的量，所以求导之前不能先令$\epsilon=0$。这就由一个背景二点函数得到了贝塔函数，与第73节通过几个独立反项组合求得的答案相同。

若物质是同表示的外尔或马约拉纳场，二点函数的自由度权重为狄拉克的一半；实标量也是复标量的一半。于是对分别列出的物种，

<span id="eq:c78-real-weyl-counting"></span>

$$
\beta(g)
=-\frac{g^3}{16\pi^2}\left[
 \frac{11}{3}C_A-\frac23\sum_{\text{外尔}}T(R_f)
                  -\frac16\sum_{\rm real}T(R_s)\right]+O(g^5).
\tag{78.35}
$$

一个复标量等于两个实标量，一个狄拉克场等于两套外尔自由度，代回便恢复[（78.34）](#eq:c78-beta-derived)。对单独的马约拉纳或独立实标量，规范变换还须保持相应实条件，因而需要合适的实表示。一般外尔表示不受同样的实条件限制，但它们组成的规范理论须满足前章的反常条件。这些半因子也与前面的高斯积分一致。

作为阿贝尔极限，把$C_A$设为零并保留一个单位电荷狄拉克场，[（78.34）](#eq:c78-beta-derived)给$\beta(g)=g^3/(12\pi^2)+O(g^5)$，恢复第66节的电动力学结果。自旋行列式也提供了另一种比较：由狄拉克二阶核求出的最小部分$+2$与自旋部分$-6$，其和正好是表中的$-4$。

对QCD，规范群是$SU(3)$，有$n_F$个基本表示狄拉克夸克味，没有基本标量。代入$C_A=3$、$T(R_{\rm DF})=n_F/2$，得到

<span id="eq:c78-qcd"></span>

$$
\begin{gathered}
\beta_{\rm QCD}(g)
=-\frac{g^3}{16\pi^2}\left(11-\frac23n_F\right)+O(g^5),\\
\frac1{g^2(\mu)}
=\frac1{g^2(\mu_0)}
 +\frac{11-2n_F/3}{8\pi^2}\ln\frac{\mu}{\mu_0}
\qquad\text{（一圈，固定活跃味数）}.
\end{gathered}
\tag{78.36}
$$

第二行由$d(g^{-2})/dt=-2g^{-3}\beta$直接积分得到。对整数$n_F\le16$，对数项系数为正，能标增大时耦合减小，这就是紫外渐近自由。取$n_F=6$时，括号为7；在跨越夸克质量阈值的实际应用中，应按第28、29节的方法匹配活跃物种。在低能耦合变大以后，一圈式便不再提供受控的近似。

背景方法还解释了答案为何会有这样的号。标量型的轨道运动与鬼合计只给$-C_A$，场强对自旋的耦合却给$+12C_A$；它们组成$11C_A$，再由裸耦合的关系转成负的贝塔函数。物质场产生相反方向的贡献，物种足够多时可以抵消规范场的作用。这里的分解依赖所选背景规范，但最后的一圈贝塔系数与先前计算一致。背景场因此既减少了所需的图，也把规范场自相互作用中起决定作用的部分显露出来。

---

[← 第 77 节](/posts/srednicki-77/) · [章节地图](/srednicki/) · [第 79 节 →](/posts/srednicki-79/)
