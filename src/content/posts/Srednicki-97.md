---
title: 'Srednicki §97 大统一'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [97]
hideFromHome: true
draft: false
---

<span id="c97"></span>

标准模型把强、弱和电磁相互作用放在同一个量子场论框架中，却仍使用三个独立的规范耦合。一代左Weyl场也分散在五个不同的表示里。大统一（grand unification）的想法是把这些表示和耦合放进一个更大的规范群，再借助自发对称性破缺得到低能标准模型。这样做是否有用，要看新增的联系能否经受实验检验。规范耦合的跑动、夸克与轻子的质量关系，以及质子衰变，正好提供三种不同的检验。

先研究最小的非超对称$SU(5)$模型，再讨论上一节的超伙伴怎样改变统一预言。模型将夸克与轻子装入共同表示，因而同时约束规范耦合、质量和重子数破坏作用。后半节继续求反常、重标量交换与有效系数运行，并将四费米作用接到质子衰变和夸克、轻子质量比上。

<span id="c97-embedding"></span>

## 把标准模型嵌入SU(5)

本节先取第87–89章的可重整标准模型：给定三个规范群因子、三代左Weyl场和一个Higgs双重态，拉格朗日量只含规范及洛伦兹不变、质量维数不超过四的项。将拉氏量中的系数列出，共有20个实参数：三个规范耦合、九个对角Yukawa参数、CKM矩阵的三个角和一个相位、强与弱两个真空角，以及Higgs势的两个参数。这个数目表达了模型仍有许多输入；若要进一步数独立的可观测参数，还要考虑反常相位变换。没有显式$B+L$破坏项时，标准模型的Yukawa作用保持重子数和轻子数，而$B+L$变换的测度相位可以移去弱真空角。由一代场表直接算得
<span id="eq:c97-theta-count"></span>

$$
\begin{aligned}
\mathcal A_{SU(2)^2(B+L)}
 &=3\left(\frac13\right)T(\mathbf2)+T(\mathbf2)=1,\\
\mathcal A_{SU(3)^2B}
 &=2\left(\frac13\right)T(\mathbf3)
   -\frac13T(\bar{\mathbf3})-\frac13T(\bar{\mathbf3})=0,
\qquad T(\mathbf n)=\frac12.
\end{aligned}
\tag{97.1}
$$

因此这种旋转改变弱角而不改变强角。到本节加入破坏$B,L$的相互作用时，同一旋转也会改变新耦合的相位；应对完整模型重新计数。下面先研究由更大群所强制的耦合联系。

一个最小的例子是Georgi–Glashow $SU(5)$模型。取一个实伴随标量$\Phi=\Phi^aT^a$，并设其真空期望值为
<span id="eq:c97-adjoint-vev"></span>

$$
\langle\Phi\rangle=VY,\qquad
Y=\operatorname{diag}\left(-\frac13,-\frac13,-\frac13,
                           \frac12,\frac12\right),\qquad V\gg v.
\tag{97.2}
$$

这里$V$是大统一破缺标度，$v$仍是电弱标度。为什么这个方向留下所需群？与$Y$对易的幺正矩阵不能混合两个不同本征值的子空间，只能是一个$3\times3$块和一个$2\times2$块；整个矩阵的行列式为1。因此稳定子是$S(U(3)\times U(2))$，其李代数为$su(3)\oplus su(2)\oplus u(1)$。局部规范相互作用可以按$SU(3)\times SU(2)\times U(1)$的李代数描述；全局群结构还要进一步确定。

若要保留全局群的信息，具体嵌入可写成
<span id="eq:c97-subgroup-map"></span>

$$
(g_3,g_2,z)\longmapsto
 \operatorname{diag}(z^{-2}g_3,z^3g_2),\qquad |z|=1.
\tag{97.3}
$$

映到单位阵要求$g_3=z^2I_3$、$g_2=z^{-3}I_2$和$z^6=1$，所以它的核为$\mathbb Z_6$。稳定子因而是上述直积的$\mathbb Z_6$商。这个区别在讨论磁荷等全局问题时才需要特别保留。

半迹归一$\operatorname{Tr}T^aT^b=\delta^{ab}/2$还决定了超荷方向的尺度。因为
<span id="eq:c97-hypercharge-normalization"></span>

$$
\operatorname{Tr}Y^2=3\left(\frac19\right)+2\left(\frac14\right)=\frac56,
\qquad T^{24}=cY,\qquad
c^2\frac56=\frac12,\qquad c=\sqrt{\frac35},
\tag{97.4}
$$

不能把标准模型的$Y$直接当成半迹归一的$SU(5)$生成元。耦合关系中的$\sqrt{3/5}$正来自这一步归一。

<span id="c97-representations"></span>

## 一代费米子怎样组成完整表示

基本空间分成颜色三维空间$C$与弱二维空间$W$。$Y$在两个子空间上的本征值已经给出，因此
<span id="eq:c97-five-branching"></span>

$$
\begin{aligned}
\mathbf5&\longrightarrow
 (\mathbf3,\mathbf1,-\tfrac13)\oplus(\mathbf1,\mathbf2,+\tfrac12),\\
\bar{\mathbf5}&\longrightarrow
 (\bar{\mathbf3},\mathbf1,+\tfrac13)\oplus(\mathbf1,\mathbf2,-\tfrac12).
\end{aligned}
\tag{97.5}
$$

第二行是复共轭表示；$SU(2)$的共轭双重态可用epsilon张量换成通常双重态。于是$\bar d$和$\ell$已经恰好填满一个$\bar{\mathbf5}$。

余下的场可从$\mathbf5\otimes\mathbf5$寻找。先区分张量交换的对称、反对称子空间，再分别把$C\oplus W$代入：
<span id="eq:c97-tensor-subspaces"></span>

$$
\begin{aligned}
\operatorname{Sym}^2(C\oplus W)
 &=\operatorname{Sym}^2 C\oplus(C\otimes W)\oplus\operatorname{Sym}^2W,\\
\wedge^2(C\oplus W)
 &=\wedge^2 C\oplus(C\otimes W)\oplus\wedge^2W.
\end{aligned}
\tag{97.6}
$$

交叉空间的两种基分别是$c\otimes w+w\otimes c$和$c\otimes w-w\otimes c$，各有六维。两个颜色指标的对称部分有六维，反对称部分可由$\epsilon_{\alpha\beta\gamma}$变成反三重态。两个弱指标的对称部分有三维，反对称部分只有$\epsilon_{ij}$这一个方向。各槽的超荷相加，得到
<span id="eq:c97-ten-fifteen-branching"></span>

$$
\begin{aligned}
\mathbf{15}&\longrightarrow
 (\mathbf6,\mathbf1,-\tfrac23)\oplus(\mathbf3,\mathbf2,+\tfrac16)
       \oplus(\mathbf1,\mathbf3,+1),\\
\mathbf{10}&\longrightarrow
 (\bar{\mathbf3},\mathbf1,-\tfrac23)\oplus(\mathbf3,\mathbf2,+\tfrac16)
       \oplus(\mathbf1,\mathbf1,+1),\\
\mathbf5\otimes\mathbf5&=\mathbf{15}_{\rm S}\oplus\mathbf{10}_{\rm A}.
\end{aligned}
\tag{97.7}
$$

维数分别是$6+6+3=15$和$3+6+1=10$。十表示的三个部分就是$\bar u,q,\bar e$。因此一代全部15个左Weyl分量组成$\bar{\mathbf5}\oplus\mathbf{10}$，还没有增加新的轻费米子。

把场装入群表示以后，还须检查手征规范反常。[十表示的三次迹](#ex97-1)给出$A(\mathbf{10})=1$、$A(\bar{\mathbf5})=-1$。每代都分别相消，因此复制三代不会破坏这一相容性。

<span id="c97-covariant"></span>

## 协变导数与分量场

用大写$A,B=1,\ldots,5$表示大群指标，定义$\psi^A\in\bar{\mathbf5}$和$\chi_{AB}=-\chi_{BA}\in\mathbf{10}$。前者的生成元是$-T^{aT}$，后者在两个基本槽上分别作用。将这两种表示代入协变导数，得到
<span id="eq:c97-covariant-derivatives"></span>

$$
\begin{aligned}
(D_\mu\psi)^A
 &=\partial_\mu\psi^A+ig_5(A_\mu)_B{}^A\psi^B,\\
(D_\mu\chi)_{AB}
 &=\partial_\mu\chi_{AB}
   -ig_5\big[(A_\mu)_A{}^C\chi_{CB}
                 +(A_\mu)_B{}^C\chi_{AC}\big],
\qquad A_\mu=A_\mu^aT^a.
\end{aligned}
\tag{97.8}
$$

这也可以直接从$\psi\mapsto U^*\psi$和$\chi\mapsto U\chi U^T$得到：无穷小变换的一阶项分别作用在一个或两个指标上。

全指标求和把反对称矩阵的每个独立分量数了两遍，所以动能必须写为
<span id="eq:c97-fermion-kinetic"></span>

$$
\mathcal L_{\rm kin}
 =i\psi_A^\dagger\bar\sigma^\mu(D_\mu\psi)^A
  +\frac i2\chi^{\dagger AB}\bar\sigma^\mu(D_\mu\chi)_{AB}.
\tag{97.9}
$$

代入协变导数时，$\chi$的两个槽给相同贡献。第二槽一项交换哑指标$A,B$，再用$\chi_{AC}=-\chi_{CA}$、$\chi^{\dagger BA}=-\chi^{\dagger AB}$，两个负号相消，恰与第一槽相同。它们抵消原来的$1/2$，得到
<span id="eq:c97-matrix-interaction"></span>

$$
\begin{aligned}
\mathcal L_{\rm int}
 &=g_5\chi^{\dagger AB}(A_\mu)_A{}^C\bar\sigma^\mu\chi_{CB}
   -g_5\psi_A^\dagger(A_\mu^T)^A{}_B\bar\sigma^\mu\psi^B\\
 &=-g_5\left[
 \psi_A^\dagger(A_\mu^T)^A{}_B\bar\sigma^\mu\psi^B
 +\chi^{\dagger BA}(A_\mu)_A{}^C\bar\sigma^\mu\chi_{CB}\right].
\end{aligned}
\tag{97.10}
$$

第二行只把$\chi^\dagger$的两个内部指标反序，没有交换两个格拉斯曼场；矩阵次序和前面的负号由此固定。

选取以下分量相位，写成
<span id="eq:c97-matter-components"></span>

$$
\psi^A=(\bar d^r,\bar d^b,\bar d^g,e,-\nu),\qquad
\chi_{AB}=\begin{pmatrix}
0&\bar u^g&-\bar u^b&u_r&d_r\\
-\bar u^g&0&\bar u^r&u_b&d_b\\
\bar u^b&-\bar u^r&0&u_g&d_g\\
-u_r&-u_b&-u_g&0&\bar e\\
-d_r&-d_b&-d_g&-\bar e&0
\end{pmatrix}.
\tag{97.11}
$$

$r,b,g$依次为三色。特别是$\psi$的弱部分是$(e,-\nu)$，不是$(\nu,e)$；epsilon将反双重态转成双重态时正好产生这个次序。以后所有相互作用都沿用这些相位。

<span id="c97-gauge-block"></span>

## 轻规范场与重X玻色子

规范矩阵也按同样的$3+2$分块：
<span id="eq:c97-gauge-blocks"></span>

$$
A_\mu=\begin{pmatrix}
 G_\mu-\frac c3B_\mu I_3&X_\mu/\sqrt2\\
 X_\mu^\dagger/\sqrt2&W_\mu+\frac c2B_\mu I_2
\end{pmatrix},\qquad
W_\mu=\begin{pmatrix}W_\mu^3/2&W_\mu^+/\sqrt2\\
 W_\mu^-/\sqrt2&-W_\mu^3/2\end{pmatrix},\quad
\operatorname{Tr}G_\mu=0.
\tag{97.12}
$$

$G,W,B$分别是八个胶子、三个弱规范场和超荷场。$X$是$3\times2$复矩阵，共十二个实自由度，恰为$24-(8+3+1)$个破缺方向。沿第87节的Pauli基，$W^\pm=(W^1\mp iW^2)/\sqrt2$，它与上述矩阵中带电分量的槽位一致。

$X$前的$1/\sqrt2$来自两个实规范场组成一个复场。若$E_{AB}$只有第$A,B$元为1，则一对半迹归一生成元可取
<span id="eq:c97-complex-vector-normalization"></span>

$$
T_1=\frac{E_{\alpha,3+i}+E_{3+i,\alpha}}2,\qquad
T_2=\frac{-iE_{\alpha,3+i}+iE_{3+i,\alpha}}2,
\qquad X_\alpha{}^i=\frac{A^1-iA^2}{\sqrt2}.
\tag{97.13}
$$

其上方非对角元为$(A^1-iA^2)/2=X/\sqrt2$。在未破缺群下，该块按颜色基本、弱反基本变换，超荷等于两个槽的本征值差$-1/3-1/2=-5/6$；弱反双重态与双重态等价，所以这一块的表示可记作$(\mathbf3,\mathbf2,-5/6)$。

质量可直接从伴随动能求出。保持[第84节](/posts/srednicki-84/#c84)的实场归一$\mathcal L_{\Phi,\rm kin}=-\operatorname{Tr}(D_\mu\Phi D^\mu\Phi)$，有$D_\mu\langle\Phi\rangle=-ig_5[A_\mu,VY]$。设$\Delta=5V/6$，由上述两矩阵求迹得
<span id="eq:c97-x-mass"></span>

$$
\begin{aligned}
\operatorname{Tr}[T_a,VY][T_b,VY]&=-\frac{\Delta^2}{2}\delta_{ab},
                   &&a,b=1,2,\\
\mathcal L_{X,\rm mass}
 &=-\frac{g_5^2\Delta^2}{2}\big[A^1_\mu A^{1\mu}+A^2_\mu A^{2\mu}\big]
   =-g_5^2\Delta^2X_\mu^\dagger X^\mu,\\
M_X&=\frac56g_5V.
\end{aligned}
\tag{97.14}
$$

后面的匹配直接用物理质量$M_X$，势参数则始终对应上述规范归一的$V$；

最后看轻场耦合。色块和弱块已按各自群的半迹归一，所以其系数都是$g_5$。超荷块却是$cB Y$，因而$g_5c$才等于通常的$g_1$。因此统一尺度处的树级匹配关系为
<span id="eq:c97-tree-unification"></span>

$$
\sqrt{\frac53}\,g_1=g_2=g_3=g_5.
\tag{97.15}
$$

例如$\psi$色分量的相互作用含$+g_5cB\bar d^\dagger\bar\sigma\bar d/3$，正是$Y_{\bar d}=1/3$；$\chi_{\alpha,3+i}$的两个对角槽相加，得到$-1/3+1/2=1/6$，也是$q$的超荷。这样，表示分解与实际拉氏量相互核对。

<span id="c97-x-current"></span>

## 重规范场的流与质子衰变

取式[（97.10）](#eq:c97-matrix-interaction)中一个$X^\dagger$槽，可以逐项看出它连接哪些场。$\psi$项给$\bar d^\dagger(e,-\nu)$。$\chi$项若剩下的求和槽是另一个弱槽，分别给$-\bar e^\dagger d$和$+\bar e^\dagger u$；若剩下的是颜色槽，则用$\chi_{\alpha\beta}=\epsilon_{\alpha\beta\gamma}\bar u^\gamma$，给$q^\dagger\bar u$。因此
<span id="eq:c97-x-component-currents"></span>

$$
\begin{aligned}
J_\alpha^{1\mu}
 &=\bar d_\alpha^\dagger\bar\sigma^\mu e
    -\bar e^\dagger\bar\sigma^\mu d_\alpha
    +\epsilon_{\alpha\beta\gamma}u^{\dagger\beta}\bar\sigma^\mu\bar u^\gamma,\\
J_\alpha^{2\mu}
 &=-\bar d_\alpha^\dagger\bar\sigma^\mu\nu
    +\bar e^\dagger\bar\sigma^\mu u_\alpha
    +\epsilon_{\alpha\beta\gamma}d^{\dagger\beta}\bar\sigma^\mu\bar u^\gamma,\\
\mathcal L_X&=-\frac{g_5}{\sqrt2}X_{i\mu}^{\dagger\alpha}J_\alpha^{i\mu}
                 +\mathrm{h.c.}
\end{aligned}
\tag{97.16}
$$

将$\ell=(\nu,e)$、$q=(u,d)$重新装成弱双重态，就得到按未破缺群指标收缩的流
<span id="eq:c97-x-invariant-current"></span>

$$
J_\alpha^{i\mu}
 =\epsilon^{ij}\bar d_\alpha^\dagger\bar\sigma^\mu\ell_j
  -\epsilon^{ij}\bar e^\dagger\bar\sigma^\mu q_{\alpha j}
  +\epsilon_{\alpha\beta\gamma}q^{\dagger\beta i}\bar\sigma^\mu\bar u^\gamma.
\tag{97.17}
$$

有三代时，每个双线性增加同一个代指标，再对代求和。

前两项的$(B,L)$为$(1/3,1)$，第三项为$(-2/3,0)$。同一个$X$同时耦合这两种流，因而不能给它指定一个同时使所有顶角守恒的重子数和轻子数。交换$X$形成的交叉项具有$\Delta B=\Delta L=\pm1$；$B-L$仍然守恒。质子于是可以变成正电子和介子。

先估计这个新作用会产生多快的质子衰变。低动量$X$传播子给$1/M_X^2$，两个顶角给$g_5^2$，有效四费米系数的维数是$-2$。若强子矩阵元只由$m_p$定标，平方并乘两体相空间便给
<span id="eq:c97-naive-proton-width"></span>

$$
\Gamma(p\to e^+\pi^0)\sim\frac{g_5^4m_p^5}{8\pi M_X^4}.
\tag{97.18}
$$

这里的系数只是粗估；$m_p^5$则由量纲固定。以历史上使用的寿命限制$\tau>10^{33}$年为例，取$g_5\sim0.6$，得到$M_X$须高于几乘$10^{15}$ GeV。按$m_p=0.938$ GeV和一年$365.25$日逐项换算，粗式给$3.66\times10^{15}$ GeV。要把这种估计变成计算，必须求出有效算符、把它的系数运行到低能，再接上三夸克的强子矩阵元。[系数运行](#ex97-3)和[强子匹配](#ex97-4)将依次完成这些步骤。

<span id="c97-yukawa"></span>

## Higgs表示与完整的Yukawa展开

电弱破缺还需要$(\mathbf1,\mathbf2,-1/2)$标量。能容纳它的最小完整$SU(5)$表示又是$\bar{\mathbf5}$，所以加入
<span id="eq:c97-higgs-components"></span>

$$
H^A=(\phi^r,\phi^b,\phi^g,\varphi^-,-\varphi^0),\qquad
\varphi=\binom{\varphi^0}{\varphi^-},\qquad
\phi\sim(\bar{\mathbf3},\mathbf1,+\tfrac13).
\tag{97.19}
$$

$H$在本节是普通标量场。除了熟悉的电弱Higgs，它还带来三个有色标量分量。

为了找出全部可重整Yukawa项，可以先用中心变换筛选。若$z^5=1$，$H,\psi,\chi$分别带中心因子$z^{-1},z^{-1},z^2$。一个标量与两个左Weyl场的六种组合中，$H\psi\psi$、$H\chi\chi$、$H^\dagger\psi\psi$、$H^\dagger\psi\chi$的因子分别是$z^{-3},z^3,z^{-1},z^2$，均不能成为单态；只剩$H\psi\chi$和$H^\dagger\chi\chi$。前者以两个上下指标配对，后者以五维体积张量收缩，各只有一个独立单态。右手共轭项再由h.c.给出，因此允许的Yukawa相互作用恰由两个不变量组成：
<span id="eq:c97-su5-yukawa"></span>

$$
\mathcal L_Y
 =-yH^A\psi^B\chi_{AB}
  -\frac{y''}{8}\epsilon^{ABCDE}H_A^\dagger\chi_{BC}\chi_{DE}
  +\mathrm{h.c.}
\tag{97.20}
$$

第一项的上下指标直接配对；第二项的五个基本指标用体积张量缩并。两项各含一个标量和两个Weyl场，维数为$1+3/2+3/2=4$，所以$y,y''$无量纲。旋量指标仍用洛伦兹反对称张量收缩。

先展开第一项。弱槽的贡献为
$H^4\psi^5\chi_{45}+H^5\psi^4\chi_{54}
=(\varphi^0 e-\varphi^-\nu)\bar e$。
$H$在弱槽、$\psi$在颜色槽的贡献为
$(\varphi^0 d_\alpha-\varphi^-u_\alpha)\bar d^\alpha$。
余下$H$在颜色槽时，分别与两个颜色槽或一个弱槽相接。四种贡献于是合成
<span id="eq:c97-first-yukawa-expanded"></span>

$$
\begin{aligned}
H^A\psi^B\chi_{AB}
={}&\epsilon^{ij}\varphi_i\ell_j\bar e
  +\epsilon^{ij}\varphi_iq_{\alpha j}\bar d^\alpha\\
 &+\epsilon_{\alpha\beta\gamma}\phi^\alpha\bar d^\beta\bar u^\gamma
  +\epsilon^{ij}\phi^\alpha q_{\alpha i}\ell_j.
\end{aligned}
\tag{97.21}
$$

第一行给带电轻子和下型夸克质量，第二行给新标量的耦合。

第二项的组合因子更容易在固定$H_A^\dagger$后看清。定义
$P_A=\epsilon^{ABCDE}\chi_{BC}\chi_{DE}/8$。
两个奇Weyl场组成的洛伦兹标量满足$(ab)=(ba)$：交换场和交换旋量epsilon各给一个负号。于是对固定的四个内部指标，每种配对有两对各反序及交换两对所产生的$2\times2\times2=8$个相等贡献。举例说，
<span id="eq:c97-pfaffian-first"></span>

$$
P_1=\chi_{23}\chi_{45}-\chi_{24}\chi_{35}+\chi_{25}\chi_{34}
   =\bar u^r\bar e-u_b d_g+d_bu_g.
\tag{97.22}
$$

其余四个槽也须保留相对号。按$\epsilon^{12345}=+1$逐一展开，得到
<span id="eq:c97-all-pfaffian-components"></span>

$$
\begin{aligned}
P_2&=\bar u^b\bar e+u_r d_g-d_r u_g,&
P_3&=\bar u^g\bar e-u_r d_b+d_r u_b,\\
P_4&=-\big(d_r\bar u^r+d_b\bar u^b+d_g\bar u^g\big),&
P_5&=u_r\bar u^r+u_b\bar u^b+u_g\bar u^g.
\end{aligned}
\tag{97.23}
$$

例如$P_4=-(\chi_{12}\chi_{35}-\chi_{13}\chi_{25}+\chi_{15}\chi_{23})$；前面的负号来自把4从第四槽移到第一槽的三次交换。$P_5$则需四次交换，号为正。这些符号决定弱Higgs项与有色Higgs项的相对相位。

将五项与式[（97.19）](#eq:c97-higgs-components)相乘，完整结果为
<span id="eq:c97-complete-yukawa-components"></span>

$$
\begin{aligned}
\mathcal L_Y={}&-y\epsilon^{ij}\varphi_i\ell_j\bar e
 -y\epsilon^{ij}\varphi_iq_{\alpha j}\bar d^\alpha
 +y''\varphi^{\dagger i}q_{\alpha i}\bar u^\alpha\\
 &-y\epsilon_{\alpha\beta\gamma}\phi^\alpha\bar d^\beta\bar u^\gamma
 -y\epsilon^{ij}\phi^\alpha q_{\alpha i}\ell_j
 -y''\phi_\alpha^\dagger\bar u^\alpha\bar e\\
 &+\frac{y''}{2}\epsilon^{\alpha\beta\gamma}\epsilon^{ij}
       \phi_\alpha^\dagger(q_{\beta i}q_{\gamma j})+\mathrm{h.c.}
\end{aligned}
\tag{97.24}
$$

最后一行的$1/2$是因为两个颜色、弱指标共同求和给
$\epsilon^{r\beta\gamma}\epsilon^{ij}q_{\beta i}q_{\gamma j}
=2(u_b d_g-d_bu_g)$。这一耦合与其余有色项一起参与[重标量交换](#ex97-2)。

固定场矩阵中的相位以后，上型项的正号便与两个有色项的相对号一起由大群不变量确定。若把$y''$整体改号，三个项会同时变号。因而使用式[（97.24）](#eq:c97-complete-yukawa-components)时，与[第89节的负号定义](/posts/srednicki-89/#c89-fields)比较应记$Y_u=-y''$；这一相位约定不改变上型质量的奇异值。

<span id="c97-mass-matching"></span>

## 夸克与轻子的质量联系

三代时应保持每个矩阵的行、列所指场不变。若大群第一项定义成$-y_{IJ}H^A\psi_I^B\chi_{AB,J}$，则弱展开给$\ell_I\bar e_J$及$q_J\bar d_I$。按第88、89章分别以$\ell_I\bar e_J$、$q_I\bar d_J$排序，匹配关系是
<span id="eq:c97-yukawa-matrix-matching"></span>

$$
Y_e=y,\qquad Y_d=y^T,\qquad Y_u=-y'',\qquad y''=y''{}^T.
\tag{97.25}
$$

最后的对称性来自第二个不变量交换两个$\chi$时不变，故反对称代矩阵没有贡献。前两个矩阵之间的转置则来自下型项与轻子项中代指标的固定排序。

转置不改变奇异值。若$y=UdV^\dagger$，那么$y^T=V^*dU^T$，其中$d$可取实非负对角。因此乘上共同的Higgs真空值后，在统一尺度得到
<span id="eq:c97-mass-boundaries"></span>

$$
m_b(M_X)=m_\tau(M_X),\qquad
m_s(M_X)=m_\mu(M_X),\qquad
m_d(M_X)=m_e(M_X).
\tag{97.26}
$$

这些是共同方案中的树级边界关系。夸克与轻子的低能质量并不直接相等，因为从$M_X$向下运行时，夸克还受到强作用的修正。[质量比的运行](#ex97-5)将给出这一步的结果。

有色$\phi$的作用也破坏$B,L$守恒，相应的四费米项由[标量源消元](#ex97-2)得到。第一代Yukawa耦合比规范耦合约小$10^5$倍，所以同一寿命限制中$y^4/M_\phi^4$与$g_5^4/M_X^4$相比，只要求$M_\phi$约大于$10^{-5}M_X$，也就是$10^{10}$ GeV量级。虽比重规范场的界弱，它仍远高于电弱尺度。

<span id="c97-potential"></span>

## 真空方向与双重态、三重态的质量分离

要使$\varphi$保持轻而$\phi$足够重，需要看标量势。再要求$\Phi\mapsto-\Phi$的离散对称性，先研究如下势：
<span id="eq:c97-restricted-potential"></span>

$$
\begin{aligned}
\mathcal V(\Phi,H)={}&-\frac{m_\Phi^2}{2}\operatorname{Tr}\Phi^2
 +\frac{\lambda_1}{4}\operatorname{Tr}\Phi^4
 +\frac{\lambda_2}{4}(\operatorname{Tr}\Phi^2)^2\\
 &+m_H^2H^\dagger H+\frac{\kappa_1}{4}(H^\dagger H)^2
 -\frac{\kappa_2}{2}H^\dagger\Phi_{\bar5}^{2}H,
\qquad \Phi_{\bar5}=-\Phi^T.
\end{aligned}
\tag{97.27}
$$

以反基本矩阵作用于$H$保证缩并的表示相容；平方的本征值与基本矩阵相同。这还不是所给对称性允许的一般势：$\eta(H^\dagger H)\operatorname{Tr}\Phi^2$同样可重整、同样为偶。它只依赖两个场的长度，而最后一项依赖$H$相对$\Phi$的取向，所以两者独立。以下先研究$\eta=0$的参数选择。

先置$H=0$，取$m_\Phi^2,\lambda_1,\lambda_2>0$。[第84节的本征值极小化](/posts/srednicki-84/#c84-vacuum-potential)给出所有无迹厄米方向的比较：任意无迹厄米$5\times5$矩阵满足
<span id="eq:c97-adjoint-sharp-bound"></span>

$$
\frac{\operatorname{Tr}\Phi^4}{(\operatorname{Tr}\Phi^2)^2}
 \ge\frac7{30},\qquad
\text{等号的两个本征值重数为3和2。}
\tag{97.28}
$$

证明的关键是先求约束驻点，再排除所有含三个不同本征值的极小点；余下两值谱的重数越接近，四次迹越小。这样选出$Y$以后，径向求解才确定尺度。

具体说，令$\rho^2=\operatorname{Tr}\Phi^2$。在最低方向上，势为
$-m_\Phi^2\rho^2/2+(7\lambda_1/30+\lambda_2)\rho^4/4$。
取非零径向驻点，并用$\rho^2=5V^2/6$，得到
<span id="eq:c97-gut-vev-scale"></span>

$$
\rho^2=\frac{30m_\Phi^2}{7\lambda_1+30\lambda_2},\qquad
V^2=\frac{36m_\Phi^2}{7\lambda_1+30\lambda_2}.
\tag{97.29}
$$

两个离散分支是$\Phi=\pm VUYU^\dagger$；每个分支都留下前面已求出的标准模型李代数。

在这一背景上，$\Phi^2$的弱本征值为$V^2/4$，颜色本征值为$V^2/9$。直接读出二次项，就有
<span id="eq:c97-doublet-triplet-masses"></span>

$$
\begin{aligned}
m_\varphi^2&=m_H^2-\frac18\kappa_2V^2,\\
M_\phi^2&=m_H^2-\frac1{18}\kappa_2V^2,\\
M_\phi^2-m_\varphi^2&=\frac5{72}\kappa_2V^2.
\end{aligned}
\tag{97.30}
$$

若恢复$\eta$项，两质量都加上$5\eta V^2/6$，质量差仍不变。

即使把六个参数都取正，也不足以保证两个场一起变大时势有下界。设$\Phi=tX$，$H$沿$X$的某个本征值$x_j$方向，长度为$h$，并记
$Q(X)=\lambda_1\operatorname{Tr}X^4+\lambda_2(\operatorname{Tr}X^2)^2$。
四次部分可以配成
<span id="eq:c97-joint-quartic-bound"></span>

$$
\begin{aligned}
\mathcal V_4
 &=\frac{Q(X)}4t^4+\frac{\kappa_1}4h^4
       -\frac{\kappa_2x_j^2}{2}t^2h^2\\
 &=\frac14\big(\sqrt{Q(X)}t^2-\sqrt{\kappa_1}h^2\big)^2
   +\frac12\big(\sqrt{\kappa_1Q(X)}-\kappa_2x_j^2\big)t^2h^2.
\end{aligned}
\tag{97.31}
$$

因此所有方向至少须满足$\kappa_2x_j^2\le\sqrt{\kappa_1Q(X)}$。严格不等号给出四次势的正下界；等号方向还要查看二次项。以$X=Y$、$x_j=1/2$为例，若$\kappa_2^2/16>\kappa_1(35\lambda_1/216+25\lambda_2/36)$，便能沿第一平方为零的射线把势降至负无穷，尽管各参数仍为正。所以下面的质量分离讨论还需选择联合势稳定的参数区间。

为了有电弱破缺，要求$m_\varphi^2$为约$-(100\,\mathrm{GeV})^2$的负数；质子寿命却要求$M_\phi^2\gtrsim10^{20}\,\mathrm{GeV}^2$。由式[（97.30）](#eq:c97-doublet-triplet-masses)，两个量都来自大数$m_H^2$与$\kappa_2V^2$的组合，轻的那个需要至少约$10^{-16}$的相对抵消。这就是双重态—三重态分离中的精细调节（fine tuning）。若进一步按量级取$\kappa_2\sim g_5^2$，$M_\phi$还会接近$M_X$，抵消要求更强；这个量级选择是启发式估计，并非群对称性强制的等式。

在$V\gg v$且伴随径向没有平坦方向时，电弱真空对大背景的相对反馈为$v^2/V^2$阶，式[（97.30）](#eq:c97-doublet-triplet-masses)是这一展开的领头质量参数。为何两个破缺尺度相差如此悬殊，便是更广义的规范层级问题（gauge hierarchy problem）。本模型把问题具体落实到势参数上，却没有给出迫使这种抵消发生的动力学原因。

<span id="c97-x-matching"></span>

## 从重X交换得到低能算符

在外部不变量远小于$M_X^2$时，可以沿[第29节](/posts/srednicki-29/#c29)的方法把重场消去。领头近似只保留其质量和线性流耦合。令$a=g_5/\sqrt2$，则
<span id="eq:c97-complex-vector-elimination"></span>

$$
\begin{aligned}
\mathcal L_{X,0}
 &=-M_X^2X_\mu^\dagger X^\mu-a(X_\mu^\dagger J^\mu+J_\mu^\dagger X^\mu)\\
 &=-M_X^2\left(X_\mu+\frac a{M_X^2}J_\mu\right)^\dagger
           \left(X^\mu+\frac a{M_X^2}J^\mu\right)
   +\frac{g_5^2}{2M_X^2}J_\mu^\dagger J^\mu,\\
X_\mu&=-\frac{g_5}{\sqrt2M_X^2}J_\mu,\qquad
\mathcal L_{X,\rm eff}=\frac{g_5^2}{2M_X^2}J_\mu^\dagger J^\mu.
\end{aligned}
\tag{97.32}
$$

表示指标在每个乘积中也按式[（97.17）](#eq:c97-x-invariant-current)配对。这个复场消元没有额外的$1/2$，显示出来的$1/2$完全来自两个顶角的$1/\sqrt2$。系数中的$g_5^2$来自两个规范顶角；定义流$J$时只组合了场，因此$J$中没有另一个耦合系数。

恢复动能再迭代运动方程，会产生$g_5^2\partial^2/M_X^4$的高导数项；重粒子圈则给更高耦合阶的匹配修正。式[（97.32）](#eq:c97-complex-vector-elimination)保留的是树级、最低逆质量阶，等价于一个重$X$传播子的低动量展开。

从三类流中挑出重子数不同的交叉项，一代结果为
<span id="eq:c97-baryon-violating-vector-form"></span>

$$
\begin{aligned}
\mathcal L_{X,\rm eff}^{|\Delta B|=1}
 =\frac{g_5^2}{2M_X^2}\epsilon^{ij}\epsilon^{\alpha\beta\gamma}
 \big(\bar d_\alpha^\dagger\bar\sigma^\mu\ell_i
        -\bar e^\dagger\bar\sigma^\mu q_{\alpha i}\big)
       \bar u_\beta^\dagger\bar\sigma_\mu q_{\gamma j}
       +\mathrm{h.c.}
\end{aligned}
\tag{97.33}
$$

为了把旋量收缩化为质量型双线性，使用本书的奇场Fierz恒等式
<span id="eq:c97-odd-fierz"></span>

$$
(a^\dagger\bar\sigma^\mu b)(c^\dagger\bar\sigma_\mu d)
 =-2(a^\dagger c^\dagger)(bd).
\tag{97.34}
$$

其号可以沿[第35节](/posts/srednicki-35/#c35)的指标约定逐次追踪：两个$\bar\sigma$先缩成$-2\epsilon^{\dot a\dot c}\epsilon^{bd}$；把$b$移过$c^\dagger$给一个负号，再将剩余未点epsilon收缩换成定义的$(bd)$又给一个负号。两个重排号相消，保留式中的$-2$。

第一项于是变为$-2(\bar d^\dagger\bar u^\dagger)(\ell q)$。第二项本已有负号，Fierz后为$+2(\bar e^\dagger\bar u_\beta^\dagger)(q_{\alpha i}q_{\gamma j})$；再交换哑颜色指标$\beta,\gamma$，epsilon翻号，使两项具有共同的负系数。定义
<span id="eq:c97-wilson-operators"></span>

$$
\begin{aligned}
\mathcal O_1&=\epsilon^{ij}\epsilon^{\alpha\beta\gamma}
       (\ell_iq_{\gamma j})(\bar d_\alpha^\dagger\bar u_\beta^\dagger),\\
\mathcal O_2&=\epsilon^{ij}\epsilon^{\alpha\beta\gamma}
       (\bar e^\dagger\bar u_\gamma^\dagger)(q_{\alpha i}q_{\beta j}),\\
\mathcal L_{\not B}&=-C_1\mathcal O_1-C_2\mathcal O_2+\mathrm{h.c.},\qquad
C_1(M_X)=C_2(M_X)=\frac{g_5^2}{M_X^2}.
\end{aligned}
\tag{97.35}
$$

每个算符有四个费米场，维数为6；$[C_i]=-2$。这两个算符构成[系数运行](#ex97-3)所用的算符基。它们的低能系数不再固定等于匹配时的共同值，规范圈对两种超荷收缩的作用不同。

同时还应消去伴随标量的重分量。由$3+2$分块，伴随的对角部分给$(\mathbf8,\mathbf1,0)\oplus(\mathbf1,\mathbf3,0)\oplus(\mathbf1,\mathbf1,0)$；十二个非对角方向已成为重规范场的纵向分量。剩下的这十二个标量不直接与本模型的费米子作Yukawa耦合：在$SU(5)$中心$z^5=1$下，$\Phi$中性，$\psi$带$z^{-1}$、$\chi$带$z^2$，三个可能的费米双线性分别带$z^{-2},z,z^4$，都不是单态。因此这些重伴随场会影响阈值匹配，却不产生同类的直接树级四费米交换。

<span id="c97-beta"></span>

## 去掉重场以后的规范耦合跑动

全$SU(5)$理论中，式[（97.15）](#eq:c97-tree-unification)只是同一规范连接的分量归一。低能有效理论却有三个独立的耦合，因为圈里已没有全部$SU(5)$多重态。$\overline{\mathrm{MS}}$本身不会自动删除重粒子；应先匹配到轻场理论，再用轻场的beta函数运行。在领头近似中，把重标量和重规范场的阈值放在共同的$M_X$，忽略有限匹配及更高圈项。

[第66节](/posts/srednicki-66/#c66)和[第73节](/posts/srednicki-73/#c73)已分别算出阿贝尔、非阿贝尔的一圈贡献。换成左Weyl和复标量计数，可统一写为
<span id="eq:c97-one-loop-counting"></span>

$$
\mu\frac{dg_a}{d\mu}=\frac{b_a}{16\pi^2}g_a^3+O(g^5),\qquad
b_a=-\frac{11}{3}C_A
 +\frac23\sum_{\text{左Weyl}}T_a(R_f)
 +\frac13\sum_{\text{复标量}}T_a(R_s).
\tag{97.36}
$$

一个Weyl是Dirac贡献的一半，一个复标量是实标量贡献的两倍。每个$T_a$还须乘上其他群因子的维数。

对一代，颜色迹为$2T(\mathbf3)+T(\bar{\mathbf3})+T(\bar{\mathbf3})=2$；弱迹为$3T(\mathbf2)+T(\mathbf2)=2$。阿贝尔生成元就是各分量的超荷，因此
<span id="eq:c97-hypercharge-trace"></span>

$$
\sum_f d_3d_2Y_f^2
 =2\left(-\frac12\right)^2+1
 +6\left(\frac16\right)^2
 +3\left(-\frac23\right)^2+3\left(\frac13\right)^2
 =\frac{10}{3}.
\tag{97.37}
$$

唯一的复Higgs双重态给弱迹$1/2$、超荷平方和$1/2$，再乘复标量系数$1/3$，各给$1/6$。将各类场的贡献相加，三群的系数为
<span id="eq:c97-sm-beta-coefficients"></span>

$$
\begin{aligned}
b_3&=-11+\frac43n,&
b_2&=-\frac{22}{3}+\frac43n+\frac16,&
b_1&=\frac{20}{9}n+\frac16,\\
n=3:&\qquad (b_1,b_2,b_3)=\left(\frac{41}{6},-\frac{19}{6},-7\right).
\end{aligned}
\tag{97.38}
$$

若另外用统一归一的$g_{1G}=\sqrt{5/3}g_1$，求导后会得到$b_{1G}=(3/5)b_1=41/10$。本节始终使用乘通常$Y$的$g_1$，所以应保留$41/6$。

<span id="c97-unification-solution"></span>

## 用两个测量值求统一尺度并预言弱角

令$\alpha_a=g_a^2/(4\pi)$，一圈方程可以直接积分：
<span id="eq:c97-inverse-alpha-running"></span>

$$
\frac{d\alpha_a}{d\ln\mu}=\frac{b_a}{2\pi}\alpha_a^2,\qquad
\frac{d\alpha_a^{-1}}{d\ln\mu}=-\frac{b_a}{2\pi},\qquad
\alpha_a^{-1}(\mu)=\alpha_a^{-1}(M_X)
                    +\frac{b_a}{2\pi}\ln\frac{M_X}{\mu}.
\tag{97.39}
$$

负的$b_3$使能量降低时$\alpha_3^{-1}$减小，强耦合增大，符号与渐近自由一致。在$M_X$施加树级匹配，再用$g_2=e/s_W$、$g_1=e/c_W$，有
<span id="eq:c97-three-inverse-couplings"></span>

$$
\begin{aligned}
\alpha_3^{-1}(\mu)&=a+\frac{b_3}{2\pi}L,\\
\frac{s_W^2(\mu)}{\alpha(\mu)}&=a+\frac{b_2}{2\pi}L,\\
\frac{c_W^2(\mu)}{\alpha(\mu)}&=\frac53a+\frac{b_1}{2\pi}L,
\qquad a=\alpha_5^{-1}(M_X),\quad L=\ln\frac{M_X}{\mu}.
\end{aligned}
\tag{97.40}
$$

$5/3$来自统一尺度处的超荷归一；低能$\alpha_1$仍按通常的$Y$定义。

令$A=\alpha^{-1}(\mu)$、$B=\alpha_3^{-1}(\mu)$。后两式相加消去弱角，剩下两个线性方程：
<span id="eq:c97-two-input-equations"></span>

$$
B=a+\frac{b_3}{2\pi}L,\qquad
A=\frac83a+\frac{b_1+b_2}{2\pi}L.
\tag{97.41}
$$

用第二式减去第一式的$8/3$倍，先得$L$；再代回第一式得$a$。记$D=b_1+b_2-8b_3/3$，结果为
<span id="eq:c97-unified-scale-solution"></span>

$$
L=\frac{2\pi}{D}\left(A-\frac83B\right),\qquad
 a=\frac{-b_3A+(b_1+b_2)B}{D}.
\tag{97.42}
$$

标准模型与MSSM场谱都给$D\ne0$，因而两个输入唯一确定$a,L$。

最后把解放入$s_W^2=\alpha[a+b_2L/(2\pi)]$，整理$A$和$B$的系数，得到
<span id="eq:c97-weak-angle-prediction"></span>

$$
s_W^2(\mu)
 =\frac{b_2-b_3+(b_1-5b_2/3)B/A}{D}.
\tag{97.43}
$$

三个低能耦合只有两个高能输入$a,L$，所以第三个组合成为预言。这是统一模型可以被检验的原因。

在$\mu=M_Z$处，用以下历史测量值作数值示例：
<span id="eq:c97-historical-inputs"></span>

$$
\alpha_3=0.1187\pm0.0020,\qquad
\alpha^{-1}=127.91\pm0.02,\qquad
(s_W^2)_{\rm obs}=0.23120\pm0.00015.
\tag{97.44}
$$

只用前两个作边界，第三个用来比较。代入非超对称系数，式[（97.42）](#eq:c97-unified-scale-solution)、[（97.43）](#eq:c97-weak-angle-prediction)化为
<span id="eq:c97-sm-unification-evaluated"></span>

$$
 a=\frac{21A+11B}{67},\qquad
L=\frac{2\pi(3A-8B)}{67},\qquad
s_W^2=\frac{69+218B/A}{402}.
\tag{97.45}
$$

取中央值及$M_Z=91.2$ GeV，得到$a=41.4743$、$L=29.6654$，所以$M_X=6.97\times10^{14}$ GeV、$s_W^2=0.20736$。前者偏低，难以压低质子衰变；后者也比上述历史观测弱角小约10%。两个检验指向相同的问题。

作为比较，一组历史两圈评价给出$M_X\simeq4\times10^{14}$ GeV、$s_W^2=0.210\pm0.001$。这种精度还依赖两圈beta函数、重质量分裂和有限阈值匹配，这两个数值作为高阶比较输入使用。以上显式求出的一圈结果已经表明最小模型的困难，后面的质子计算也统一采用这套一圈边界。

<span id="c97-susy-unification"></span>

## 超伙伴怎样改变统一

把第96节的超伙伴加入以后，一圈系数可以重新由场内容计算。一个矢量超多重态含规范玻色子和一个伴随Weyl场，给$-11C_A/3+2C_A/3=-3C_A$；一个手征超多重态含Weyl场和复标量，给$(2/3+1/3)T(R)=T(R)$。每代的三个群迹仍是此前的$2,2,10/3$，但Higgs现在有两个手征双重态。于是
<span id="eq:c97-mssm-beta"></span>

$$
\begin{aligned}
b_3&=-9+2n,&b_2&=-6+2n+1,&b_1&=\frac{10}{3}n+1,\\
n=3:&\qquad (b_1,b_2,b_3)=(11,1,-3).
\end{aligned}
\tag{97.46}
$$

这些系数假定所列多重态在考察的能区内都活跃；若超伙伴质量分散，便要分段使用相应的场清单。

把新系数放进同一组线性方程，得到
<span id="eq:c97-mssm-unification-solution"></span>

$$
a=\frac{3A+12B}{20},\qquad
L=\frac\pi{10}\left(A-\frac83B\right),\qquad
s_W^2=\frac15+\frac7{15}\frac BA.
\tag{97.47}
$$

若将超对称谱的共同低阈值近似放在$M_Z$，弱角变为约$0.2307$，统一尺度升至约$2\times10^{16}$ GeV。改变的是三个逆耦合的斜率，所需的交汇点因而移高，预言的弱角也更接近上述历史观测值。

另一个历史两圈比较值是弱角约$0.234$，其不确定性还与超伙伴质量有关。要达到这种精度，阈值位置与有限匹配都应一起指定。本节的较高$M_X$会显著压低已经计算的重$X$维数六交换；若研究完整超对称大统一模型，还应另计其余重场产生的衰变算符。

<span id="c97-extensions"></span>

## 质量比与更大的统一群

回到非超对称模型，式[（97.26）](#eq:c97-mass-boundaries)的三个关系受到规范运行修正。[下型Yukawa与轻子Yukawa之比](#ex97-5)的运行表明，强作用使低能下型质量相对增大。然而，同类场的三代具有相同规范荷，只保留规范玻色子的一圈贡献时，它们满足相同的乘法运行方程。因此在同一尺度、同一方案中，两代之比的共同因子抵消，仍预言
<span id="eq:c97-generation-mass-ratios"></span>

$$
\frac{m_e}{m_\mu}=\frac{m_d}{m_s},\qquad
\frac{m_\mu}{m_\tau}=\frac{m_s}{m_b}.
\tag{97.48}
$$

这些关系只用了所述规范修正的抵消，Yukawa本身引起的味依赖修正不在这个近似内。与前面列出的[夸克质量](/posts/srednicki-83/#c83-light-flavors)及带电轻子质量比较，第一项的差别尤其明显。因而最小模型即使借助运行改善$b$与$\tau$的单个关系，也还不能给出完整的费米子质量谱。

一种改法是增加不同表示的Higgs，使一个低能质量矩阵可由不止一个大群不变量组成；另一种改法是加入由更高尺度$\Lambda>M_X$压低的高维项。它们打破了式[（97.25）](#eq:c97-yukawa-matrix-matching)的简单联系，也带来新系数。例如可用约$1.2\times10^{19}$ GeV的Planck质量作为可能的高尺度，这里只用来说明有效展开的层次。

中微子质量也可以沿[第91节](/posts/srednicki-91/#c91)接入。加入$SU(5)$单态左Weyl场$\bar\nu_J$后，有
<span id="eq:c97-singlet-neutrinos"></span>

$$
\mathcal L_\nu
 =-\widetilde y_{IJ}H_A^\dagger\psi_I^A\bar\nu_J
  -\frac12M_{IJ}\bar\nu_I\bar\nu_J+\mathrm{h.c.},
\qquad M=M^T.
\tag{97.49}
$$

大群不变量的弱部分是$\varphi^\dagger\ell$，于是第91节的Dirac质量和重Majorana消元直接适用。加入单态给出了一种可重整的最小扩充；若已允许上一段的高维作用，$(H^\dagger\psi_I)(H^\dagger\psi_J)/\Lambda$本身也是规范不变的维数五算符，可在不显写单态场的有效理论中产生中微子质量。

还可以考虑$SO(10)$统一。要容纳16维旋量表示，严格的群应取双覆盖$\operatorname{Spin}(10)$；通常的“SO(10)大统一”名称在此沿用其李代数。16为何恰能容纳$\bar\nu\oplus\bar5\oplus10$，可以用一个简短构造看出。引入五对费米振子$b_A,b_A^\dagger$，满足$\{b_A,b_B^\dagger\}=\delta_{AB}$，并定义十个内部欧氏Clifford矩阵
<span id="eq:c97-spin10-clifford"></span>

$$
\Gamma_{2A-1}=b_A+b_A^\dagger,\qquad
\Gamma_{2A}=i(b_A-b_A^\dagger),\qquad
\{\Gamma_M,\Gamma_N\}=2\delta_{MN}.
\tag{97.50}
$$

这套$\Gamma$只作用于内部空间，与四维Dirac矩阵分开。振子的反对易关系使相同$A$的两个平方为1，交叉反对易子为零，从而十个矩阵满足所需Clifford代数；双线性对易子产生$so(10)$。Fock空间是$\bigoplus_{k=0}^5\wedge^k\mathbf5$，共有$2^5=32$维。双线性生成元保持占据数的奇偶，因此分成两个16维手征旋量。

令$SU(5)$按基本表示作用于五个产生算符。偶占据子空间便分解为
<span id="eq:c97-spinor-branching"></span>

$$
\mathbf{16}\big|_{SU(5)}
 =\wedge^0\mathbf5\oplus\wedge^2\mathbf5\oplus\wedge^4\mathbf5
 =\mathbf1\oplus\mathbf{10}\oplus\bar{\mathbf5},
\qquad 1+10+5=16.
\tag{97.51}
$$

最后一步用五维epsilon将四个反对称基本指标换成一个反基本指标。另一手征的奇占据空间给复共轭表示。这样，一代连同中微子单态恰好装进一个不可约旋量。

十维实矢量在$SU(5)$下复化为$\mathbf5\oplus\bar{\mathbf5}$，能容纳电弱Higgs；但把统一群实际破缺到标准模型，还需额外标量与合适的势。例如可选45维伴随和16维标量，再通过它们的势确定破缺方向及稳定性。由此可以构造许多具有不同谱和阈值的大统一模型。它们把规范、味和重子数问题联系起来，也同时接受这些方面的检验；是否有某一种描述自然界，最终仍须由这些检验来决定。

<span id="ex97-1"></span>

## 一代SU(5)费米子的反常

第75节已经说明，四维局部微扰规范反常由左Weyl表示的对称三生成元迹控制。这里只需比较$\bar{\mathbf5}$与$\mathbf{10}$的这个迹，而不必重新计算三角图。这个迹可以从表示的本征值直接求出。取基本表示中任意无迹厄米矩阵$X$，将其本征值记为$x_i$，有$\sum_i x_i=0$。

在$\wedge^2\mathbf N$的基$e_i\wedge e_j$上，生成元分别作用在两个槽，故$X$的本征值是$x_i+x_j$，其中$i<j$。展开三次迹，
<span id="eq:x97-antisymmetric-cubic-trace"></span>

$$
\begin{aligned}
\operatorname{Tr}_{\wedge^2N}X^3
 &=\sum_{i<j}(x_i+x_j)^3\\
 &=(N-1)\sum_i x_i^3+3\sum_{i\ne j}x_i^2x_j\\
 &=(N-1)\sum_i x_i^3
       +3\sum_i x_i^2\left(\sum_jx_j-x_i\right)\\
 &=(N-4)\sum_i x_i^3.
\end{aligned}
\tag{97.52}
$$

每个$x_i^3$在$N-1$个配对中出现；交叉项在第二行已经把两个方向的有序配对合并。迹零条件给出最后的$-3$，所以系数是$N-4$。

这个恒等式对任意厄米$X$成立。令$X=sT^a+tT^b+uT^c$，比较$s\,t\,u$的系数，就得到三个生成元完全对称迹的同一比例；这一步通常称为三次多项式的极化。反基本生成元为$-T^{aT}$，三次迹另带负号。因此以基本表示的反常系数为1，
<span id="eq:x97-generation-anomaly-cancellation"></span>

$$
A(\bar{\mathbf5})=-1,\qquad
A(\mathbf{10})=5-4=1,\qquad
A(\bar{\mathbf5}\oplus\mathbf{10})=0.
\tag{97.53}
$$

一代已经相消，三代只是将零重复三次。对称三次迹相消，使这组手征表示通过局部微扰规范反常的检验。

<span id="ex97-2"></span>

## 有色标量的重子数破坏作用

从[完整Yukawa展开](#c97-yukawa)出发，同时保留$\phi^\dagger qq$及其余有色耦合。先保留颜色指标，定义四种格拉斯曼偶双线性
<span id="eq:x97-scalar-sources"></span>

$$
\begin{aligned}
A_\alpha&=\epsilon_{\alpha\beta\gamma}
                 (\bar d^\beta\bar u^\gamma),&
B_\alpha&=\epsilon^{ij}(q_{\alpha i}\ell_j),\\
C^\alpha&=(\bar u^\alpha\bar e),&
D^\alpha&=\epsilon^{\alpha\beta\gamma}\epsilon^{ij}
                 (q_{\beta i}q_{\gamma j}),\\
S_\alpha&=y(A_\alpha+B_\alpha),&
T^\alpha&=y''(C^\alpha-D^\alpha/2).
\end{aligned}
\tag{97.54}
$$

以下只在重标量消元中使用这组源记号。重标量的低动量拉氏量为
<span id="eq:x97-complex-scalar-square"></span>

$$
\begin{aligned}
\mathcal L_{\phi,0}
 &=-M_\phi^2\phi_\alpha^\dagger\phi^\alpha
       -(\phi^\alpha S_\alpha+\phi_\alpha^\dagger T^\alpha+\mathrm{h.c.})\\
 &=-M_\phi^2\left(\phi+\frac K{M_\phi^2}\right)^\dagger
                    \left(\phi+\frac K{M_\phi^2}\right)
       +\frac{K^\dagger K}{M_\phi^2},\qquad
K^\alpha=T^\alpha+S^{\dagger\alpha}.
\end{aligned}
\tag{97.55}
$$

对$\phi^\dagger$求变分得到$\phi=-K/M_\phi^2$；代回以后便只留下$K^\dagger K/M_\phi^2$。两个独立实分量组成的复场，使源平方的系数为$1/M_\phi^2$。

要挑出$|\Delta B|=1$，分别数四个双线性的荷：
<span id="eq:x97-scalar-source-charges"></span>

$$
\begin{array}{c|rrrr}
 &A&B&C&D\\ \hline
 B&-2/3&1/3&-1/3&2/3\\
 L&0&1&-1&0
\end{array}
\tag{97.56}
$$

在$S S^\dagger$中，$AB^\dagger$与其共轭的荷差为$(\mp1,\mp1)$；在$T^\dagger T$中，$C^\dagger D$与其共轭为$(\pm1,\pm1)$。余下$ST$及其共轭里，$AC$和$BD$也破坏两种荷，而$AD$、$BC$守恒。于是
<span id="eq:x97-scalar-baryon-operators"></span>

$$
\begin{aligned}
\mathcal L_{\phi,\mathrm{eff}}^{|\Delta B|=1}
=\frac1{M_\phi^2}\Big[
 &|y|^2 A_\alpha B^{\dagger\alpha}
 -\frac{|y''|^2}{2}C_\alpha^\dagger D^\alpha\\
 &+yy''\left(A_\alpha C^\alpha-\frac12B_\alpha D^\alpha\right)
 +\mathrm{h.c.}\Big].
\end{aligned}
\tag{97.57}
$$

各乘积的格拉斯曼因子已经组成偶双线性，因而相互交换不再产生统计负号。所有项都满足$\Delta B=\Delta L$，但具有不同的手征结构和Yukawa系数。其中含$D$的两项正来自上面单列的双夸克耦合，应与其余项一起保留。这一结果保留树级$y^2/M_\phi^2$，更高导数项从$\phi$动能迭代产生，要求外部不变量远小于$M_\phi^2$。

<span id="ex97-3"></span>

## 重子数破坏系数的一圈运行

[正文](#c97-x-matching)已经把重$X$交换匹配到$\mathcal O_1,\mathcal O_2$。这里求的是它们在轻场理论中的系数运行，采用$d=4-\varepsilon$、$\overline{\mathrm{MS}}$，规范固定取本书$R_\xi$族中的Landau极限$\xi=0$。为看出哪些项在这个极限消失，先保留$\xi$。

<span id="ex97-3ab"></span>

### 规范交换的两个基本分子

交换规范玻色子的开链图有两种自旋结构：两个同洛伦兹手征槽连接时是标量插入，连接一个有点槽与一个无点槽时可以Fierz成矢量插入。下面直接求这两类的UV极点，再按这里的颜色和超荷替换。

令$\Gamma$是局部插入，规范传播子的分子为
<span id="eq:x97-uv-chain"></span>

$$
P_{\mu\nu}^{(\xi)}(\ell)
 =g_{\mu\nu}-(1-\xi)\frac{\ell_\mu\ell_\nu}{\ell^2},\qquad
N_\Gamma(\ell)
 =\gamma^\mu\slashed\ell\,\Gamma\,\slashed\ell\gamma^\nu
                  P_{\mu\nu}^{(\xi)}(\ell).
\tag{97.58}
$$

两条费米内线各给$-\slashed\ell$，两个负号相消。沿开链保留外端的Weyl投影，便可使用同一分子计算手征插入。

先把UV尾的径向积分明确算出。保留交换图的一般非例外欧氏外动量，在减除项中引入辅助质量$M>0$，将三个领先分母统一为$(\ell^2+M^2-i0)^3$。它与真实大动量尾只差UV可积项，因而不改变极点，却避免把无标度积分的零误认成没有UV发散。Wick转动$\ell^0=iL^4$给
<span id="eq:x97-local-uv-integral"></span>

$$
\begin{aligned}
I_M&=\widetilde\mu^\varepsilon
 \int\frac{d^d\ell}{(2\pi)^d}
       \frac{\ell^2}{(\ell^2+M^2-i0)^3}=iI_{M,E},\\
I_{M,E}
 &=\frac{\widetilde\mu^\varepsilon}{2}
   \int_0^\infty ds\,s^2e^{-sM^2}
      \frac d{2s}(4\pi s)^{-d/2}\\
 &=\frac d4
   \frac{\widetilde\mu^\varepsilon(M^2)^{-\varepsilon/2}}
        {(4\pi)^{d/2}}\Gamma(\varepsilon/2)
 =\frac1{8\pi^2\varepsilon}+O(1).
\end{aligned}
\tag{97.59}
$$

第二行用Schwinger参数，并对Gaussian积分求$s$导数产生$L^2$。辅助质量只决定有限部分，极点与它无关。

对标量插入，$\slashed\ell^2=-\ell^2$和$\gamma^\mu\gamma_\mu=-d$直接给
<span id="eq:x97-scalar-vertex-numerator"></span>

$$
\begin{aligned}
\gamma^\mu\slashed\ell^2\gamma_\mu&=d\ell^2,\\
\ell^{-2}\slashed\ell\slashed\ell\,\slashed\ell\slashed\ell&=\ell^2,\\
N_1&=(d-1+\xi)\ell^2.
\end{aligned}
\tag{97.60}
$$

Landau规范的横向投影减去一个$\ell^2$，所以最后留下$3\ell^2$乘极点。

对矢量插入，先用角平均$\overline{\ell_\alpha\ell_\beta}=\ell^2g_{\alpha\beta}/d$，再两次使用$\gamma^\alpha\gamma^\rho\gamma_\alpha=(d-2)\gamma^\rho$，得到
<span id="eq:x97-vector-vertex-numerator"></span>

$$
\begin{aligned}
\overline{\gamma^\mu\slashed\ell\gamma^\rho\slashed\ell\gamma_\mu}
 &=\frac{(d-2)^2}{d}\ell^2\gamma^\rho,\\
\ell^{-2}\slashed\ell\slashed\ell\gamma^\rho
                         \slashed\ell\slashed\ell&=\ell^2\gamma^\rho,\\
\overline{N_{\gamma^\rho}}
 &=\left[\frac{(d-1)(d-4)}d+\xi\right]\ell^2\gamma^\rho.
\end{aligned}
\tag{97.61}
$$

在$\xi=0$时，括号是$-\varepsilon(3-\varepsilon)/(4-\varepsilon)$，乘单极点只留下有限项。因此它在这一圈精度不产生物理矢量算符的MS极部。

还要跟踪整体号。相对于固定的树插入$-i\kappa\Gamma$，两个规范顶角与三条内线给$(ig)^2(1/i)^3=-ig^2$，再乘$I_M=iI_{M,E}$成为$+g^2I_{M,E}$。把算符内两个同手征Weyl场之一改成电荷共轭开链时，生成元为$-T^T$；将转置恢复到原不变张量上，又给一个负号。对异手征的一对，Fierz后的开链形如$\eta^\dagger\bar\sigma^\mu\psi$；链左端用$T_\eta$，原算符的有点槽却按$-T_\eta^T$变换。把开链生成元改写成原场槽的作用时，同样多出负号。因此这个号对同手征和异手征连接一致。令$\mathcal T_{rs}=\sum_aT_r^aT_s^a$作用在原算符的两个槽上，便有
<span id="eq:x97-pair-counterterm-sign"></span>

$$
\left.\frac{\mathcal G_{rs,\rm loop}}{\mathcal G_{\rm tree}}\right|_{\rm UV}
 =-\frac{K_{rs}g^2}{8\pi^2\varepsilon}\mathcal T_{rs},
\qquad
\delta Z_{rs}\mathcal O
 =+\frac{K_{rs}g^2}{8\pi^2\varepsilon}\mathcal T_{rs}\mathcal O.
\tag{97.62}
$$

第二式的反项抵消第一式的极点。以QED质量双线性的$(-1,+1)$两荷代入，在Landau规范得到$-3e^2/(8\pi^2\varepsilon)$，恰与[第62节的一般规范反项](/posts/srednicki-62/#eq:c62-ex-2-electron-counterterms)已求出的质量反项相同。

为确认没有遗漏另外四种连接，把自旋结构记为$(\psi\chi)(\eta^\dagger\zeta^\dagger)$，依次编号1至4。正文的奇场Fierz式给
$(\psi\chi)(\eta^\dagger\zeta^\dagger)
=-(\eta^\dagger\bar\sigma^\mu\psi)(\zeta^\dagger\bar\sigma_\mu\chi)/2$。
连接1、3时就是第一矢量流的顶角修正；交换两个无点槽或两个有点槽，又得到其余三个跨对。因此六对的极部系数为
<span id="eq:x97-six-pair-kernels"></span>

$$
K_{12}=K_{34}=3+\xi,\qquad
K_{13}=K_{14}=K_{23}=K_{24}=\xi.
\tag{97.63}
$$

这说明Landau规范下只需保留两个标量对。每个固定槽对的权重为1：相互作用展开中的$1/2!$由两个规范端点的分配抵消。$\mathcal O_2$中两个$q$槽先临时区分，最后取为同一场；树和圈的共同外腿重数相同，反项系数不再额外乘2。

这里所作Fierz投影取四维物理Weyl算符的一圈极部。若继续到更高圈，必须同时定义在四维消失的算符（evanescent operators），因为它们可影响有限重定义及后续混合；这里的一圈物理反常维数不需要那些高阶数据。

外费米场的归一也要一致。将[第62节一般规范反项](/posts/srednicki-62/#eq:c62-ex-2-electron-counterterms)中的$e^2$替换为$g_a^2C_2(R_{f,a})$，并取相应的开Weyl块，有
<span id="eq:x97-landau-field-factors"></span>

$$
Z_f=1-\frac1{8\pi^2\varepsilon}
       \sum_a\xi_a g_a^2C_2(R_{f,a})+O(g^4).
\tag{97.64}
$$

一圈自能不含闭Weyl迹，因而这个替换同样没有$1/2$。在所用Landau规范中，它的MS极部为零。

<span id="ex97-3-group"></span>

### 将群生成元放回两个算符

半迹归一的$SU(N)$生成元满足
<span id="eq:x97-generator-pair-completeness"></span>

$$
\sum_a(T^a)_{i'i}(T^a)_{j'j}
 =\frac12\left(\delta_{i'j}\delta_{j'i}
                 -\frac1N\delta_{i'i}\delta_{j'j}\right).
\tag{97.65}
$$

作用在反对称指标对上，第一项交换两槽给负号，第二项保留原张量，所以系数为$-(N+1)/(2N)$。对于色epsilon得到$-2/3$，对于弱epsilon得到$-3/4$。这是一条张量等式：生成元对整个反对称张量的作用与原张量成比例，无须对它的零分量作除法。

在$\mathcal O_1=(\ell q)(\bar d^\dagger\bar u^\dagger)$中，第一标量对给弱$-3/4$和超荷$(-1/2)(1/6)=-1/12$；第二对给色$-2/3$和超荷$(-1/3)(2/3)=-2/9$。共轭把后两场的荷同时反号，所以乘积与未共轭两场的$(1/3)(-2/3)$相同。在$\mathcal O_2=(qq)(\bar e^\dagger\bar u^\dagger)$中，$qq$对同时给色$-2/3$、弱$-3/4$，超荷为$1/36$；另一对只有超荷$(-1)(2/3)=-2/3$。因此两个算符各自的群因子和为
<span id="eq:x97-two-group-sums"></span>

$$
\begin{aligned}
(-1)(+1)e^2\longrightarrow\mathscr S_1
 &=-\frac23g_3^2-\frac34g_2^2-\frac{11}{36}g_1^2,\\
(-1)(+1)e^2\longrightarrow\mathscr S_2
 &=-\frac23g_3^2-\frac34g_2^2-\frac{23}{36}g_1^2.
\end{aligned}
\tag{97.66}
$$

乘式[（97.62）](#eq:x97-pair-counterterm-sign)中的共同系数，得到
<span id="eq:x97-wilson-poles"></span>

$$
\ln Z_{C_i}=\frac{3\mathscr S_i}{8\pi^2\varepsilon}
 =-\frac{4g_3^2+\frac92g_2^2+a_i g_1^2}{16\pi^2\varepsilon}
       +O(g^4),\qquad
a_1=\frac{11}{6},\quad a_2=\frac{23}{6}.
\tag{97.67}
$$

它们的差完全来自超荷；规范修正没有把两个不同的外场组互相变换。

<span id="ex97-3c"></span>

### 从反项到反常维数

在$d$维中，四费米算符维数为$6-2\varepsilon$。保持$[C_i]=-2$，裸系数关系为
<span id="eq:x97-bare-wilson-coefficients"></span>

$$
C_{i0}=\widetilde\mu^\varepsilon
       \frac{Z_{C_i}}{\prod_{r=1}^4 Z_{f_r}^{1/2}}C_i.
\tag{97.68}
$$

Landau一圈下分母没有UV极点。写$\ln Z_{C_i}=F_i(g)/\varepsilon$，其中$F_i$是式[（97.67）](#eq:x97-wilson-poles)的二次分子。对固定裸规范耦合求导时，应包括$d$维的工程项$dg_a/d\ln\mu=-\varepsilon g_a/2+O(g^3)$，因此$d\ln Z_{C_i}/d\ln\mu=-F_i+O(g^4)$。再对裸$C_i$求导，得$0=\varepsilon+d\ln C_i/d\ln\mu-F_i$。取四维极限，便得到反常维数
<span id="eq:x97-wilson-anomalous-dimensions"></span>

$$
\gamma_{C_i}\equiv\frac{d\ln C_i}{d\ln\mu}
 =-\frac{4g_3^2+\frac92g_2^2+a_i g_1^2}{16\pi^2}+O(g^4).
\tag{97.69}
$$

负的$\gamma_C$意味着向低能运行时$C_i$增大。

规范参数还提供一个号的检验。任意规范不变量都满足$\sum_rT_r\mathcal O=0$，平方以后给$\sum_{r<s}\mathcal T_{rs}=-\sum_r C_2(R_r)/2$。式[（97.63）](#eq:x97-six-pair-kernels)的$\xi$部分对所有六对相同，所以$Z_C$的规范参数极点为$-\xi g^2\sum_rC_2(R_r)/(16\pi^2\varepsilon)$。式[（97.68）](#eq:x97-bare-wilson-coefficients)分母中四个$Z_f^{1/2}$给相反的贡献，二者相消，留下上面的规范无关反常维数。

<span id="ex97-3d"></span>

### 运行到2 GeV

由正文$d\ln\alpha_a/d\ln\mu=b_a\alpha_a/(2\pi)$，把式[（97.69）](#eq:x97-wilson-anomalous-dimensions)除以它，可以逐群积分。若分子写成$A_{ia}g_a^2$，每个幂就是$-A_{ia}/(2b_a)$。对非超对称标准模型的三种$b_a$，得到
<span id="eq:x97-wilson-high-running"></span>

$$
\begin{aligned}
C_i(M_Z)=C_X
 &\left[\frac{\alpha_3(M_Z)}{\alpha_5}\right]^{2/7}
  \left[\frac{\alpha_2(M_Z)}{\alpha_5}\right]^{27/38}
  \left[\frac{\alpha_1(M_Z)}{(3/5)\alpha_5}\right]^{-3a_i/41},\\
C_X&=\frac{4\pi\alpha_5}{M_X^2}.
\end{aligned}
\tag{97.70}
$$

超荷分母是$(3/5)\alpha_5$，不是$\alpha_5$，因为仍沿通常的$Y$归一。

为得到一个简单的低能算例，假定顶夸克在$M_Z$脱耦，其余五个夸克一直活跃到2 GeV，并忽略低能电磁修正。在这一阈值近似中，$b_3=-11+2(5)/3=-23/3$，于是
<span id="eq:x97-wilson-low-running"></span>

$$
\begin{aligned}
\alpha_3^{-1}(\mu)
 &=\alpha_3^{-1}(M_Z)+\frac{23}{6\pi}\ln\frac{\mu}{M_Z},\\
C_i(2\,\mathrm{GeV})
 &=C_i(M_Z)\left[
    \frac{\alpha_3(2\,\mathrm{GeV})}{\alpha_3(M_Z)}
                 \right]^{6/23}.
\end{aligned}
\tag{97.71}
$$

指数$6/23$来自同一$4g_3^2$分子与五味beta；这个算例的五味阈值选择在整段运行中保持不变。

采用正文由$\alpha^{-1}=127.91$、$\alpha_3=0.1187$求出的统一边界，先得$\alpha_5=0.0241113$、$M_X=6.97435\times10^{14}$ GeV。再沿边界运行，$\alpha_1(M_Z)=0.00986322$、$\alpha_2(M_Z)=0.03770275$，$\alpha_3(2)=0.2657034$。各因子为

| 因子         |   $C_1$ |   $C_2$ |
| ------------ | ------: | ------: |
| 高能QCD      | 1.57681 | 1.57681 |
| 弱规范作用   | 1.37389 | 1.37389 |
| 超荷作用     | 1.05273 | 1.11342 |
| $M_Z$以下QCD | 1.23393 | 1.23393 |
| 总因子       | 2.81408 | 2.97633 |

故所需系数为
<span id="eq:x97-wilson-numerical-values"></span>

$$
\begin{aligned}
C_X&=6.22907\times10^{-31}\ \mathrm{GeV}^{-2},\\
C_1(2\,\mathrm{GeV})&=1.75291\times10^{-30}\ \mathrm{GeV}^{-2},\\
C_2(2\,\mathrm{GeV})&=1.85398\times10^{-30}\ \mathrm{GeV}^{-2}.
\end{aligned}
\tag{97.72}
$$

这里的弱角是统一模型预言的$0.20736$；若再把历史观测$0.23120$作为第三个精确边界，三条一圈关系便不再能同时满足。保持同一模型边界，才能把下一小节的寿命与本章统一预言作一致的比较。

<span id="ex97-4"></span>

## 质子衰变为正电子和中性π介子

上一小节给出的短程系数乘在四费米算符上。质子是强作用束缚态，三夸克部分在低能应匹配到第83节的手征有效理论，再由核子和π介子的场计算衰变过程。

<span id="ex97-4ab"></span>

### 三夸克算符的手征匹配

从$\ell=(\nu,e)$和$q=(u,d)$中选出所需分量。$\mathcal O_1$的$eu$项带$\epsilon^{21}=-1$，与拉氏量前的负号相消。对$\mathcal O_2$，两Weyl场的标量缩并对交换对称，故
$\epsilon^{\alpha\beta\gamma}[(u_\alpha d_\beta)-(d_\alpha u_\beta)]
=-2\epsilon^{\alpha\beta\gamma}(d_\alpha u_\beta)$。
将两个算符展开到这些分量，得到
<span id="eq:x97-proton-quark-operators"></span>

$$
\mathcal L_{eud}
 =C_1\epsilon^{\alpha\beta\gamma}(eu_\gamma)
                 (\bar d_\alpha^\dagger\bar u_\beta^\dagger)
 +2C_2\epsilon^{\alpha\beta\gamma}
                 (\bar e^\dagger\bar u_\gamma^\dagger)(d_\alpha u_\beta)
 +\mathrm{h.c.}
\tag{97.73}
$$

第二项的2已经包含两个弱分量的贡献。

这里所用的$SU(2)_L\times SU(2)_R$是低能QCD的味群。第83节定义$u=\exp[i\pi^aT^a/f_\pi]$，其中$T^a=\sigma^a/2$，并用补偿变换$h$使核子$\mathcal N=(p,n)^T$按$\mathcal N\mapsto h\mathcal N$变换。由
<span id="eq:x97-hadronic-chiral-transformations"></span>

$$
u'=Luh^\dagger=huR^\dagger,\qquad
u'\mathcal N'=L(u\mathcal N),\qquad
u'^\dagger\mathcal N'=R(u^\dagger\mathcal N)
\tag{97.74}
$$

可见$u\mathcal N$和$u^\dagger\mathcal N$分别按$(\mathbf2,\mathbf1)$、$(\mathbf1,\mathbf2)$变换。再取$P_L$和$P_R$，就得到与三夸克算符相配的洛伦兹手征；两种场的重子数也都是1。第一味分量对应质子量子数。

以宇称联系两个三夸克矩阵元，取共同匹配常数$A$，则最低阶强子作用为
<span id="eq:x97-hadronic-proton-operator"></span>

$$
\mathcal L_{\not B}
 =A\overline{\mathcal E^C}\left[
       C_1P_L(u\mathcal N)_1
       +2C_2P_R(u^\dagger\mathcal N)_1\right]+\mathrm{h.c.}
\tag{97.75}
$$

$\mathcal E^C$是电子Dirac场的电荷共轭，其粒子是正电子。一个三夸克算符的维数为$9/2$，核子场为$3/2$，所以$[A]=3$。对称性固定了式子的场结构，$A$的大小则由强动力学决定。以下采用历史晶格估计$A(2\,\mathrm{GeV})=0.0090\,\mathrm{GeV}^3$作为示例输入，将它与同尺度、同算符归一的$C_i$配用。颜色epsilon已包含在$A$所匹配的算符中，不再另乘$3!$。

<span id="ex97-4c"></span>

### 零个与一个π介子的顶角

记$K=C_1P_L+2C_2P_R$和$K_-=C_1P_L-2C_2P_R=-K\gamma_5$。在中性方向，$T^3_{11}=1/2$，所以$u_{11}=1+i\pi^0/(2f_\pi)+\cdots$，$u^\dagger_{11}$中的号相反。式[（97.75）](#eq:x97-hadronic-proton-operator)给
<span id="eq:x97-proton-pion-vertices"></span>

$$
\begin{aligned}
\mathcal L_0&=A\overline{\mathcal E^C}Kp+\mathrm{h.c.},\\
\mathcal L_{\pi^0}
 &=\frac{iA}{2f_\pi}\pi^0\overline{\mathcal E^C}K_-p+\mathrm{h.c.},\\
\mathcal L_{\pi^0pp}
 &=\frac{g_A}{2f_\pi}\partial_\mu\pi^0\,\bar p\gamma^\mu\gamma_5p.
\end{aligned}
\tag{97.76}
$$

最后一行由第83节的式[（83.47）](/posts/srednicki-83/#eq:c83-derivative-pion-nucleon)取中性分量得到。它连接内部核子线，计算中保留这一导数顶角。

<span id="ex97-4d"></span>

### 两张图和相对号

令初态质子动量为$p$，末态正电子为$r$，π介子为$k=p-r$。取$p^2=-m_p^2$、$r^2=0$、$k^2=-m_\pi^2$，忽略正电子质量。最低阶有两张图：一张直接使用$\mathcal L_{\pi^0}$；另一张先由轴向核子作用发射π，再由$\mathcal L_0$把内部核子转成正电子。

<img src="/images/srednicki/97-proton-decay.svg" alt="质子衰变的接触图与核子交换图" style="width:760px;max-width:100%;height:auto;margin:1.5rem auto;" />

接触作用与核子交换对质子衰变的贡献。实线标出核子与正电子，虚线为π介子；箭头标示所取动量方向。右图内部动量是$r$，内部质量仍为$m_p$，所以该核子并不在壳。

用$\mathcal E^C$的正能外旋量$w_t(r)$描述正电子，满足$\bar w\slashed r=0$。出π产生波为$e^{-ikx}$，导数给$-ik_\mu$；再将相互作用密度乘$i$，轴向顶角为$+g_A\slashed k\gamma_5/(2f_\pi)$。接触项中已有一个$i$，图顶角再乘$i$成为负号。因此按$S_{\rm conn}=(2\pi)^4\delta^{(4)}i\mathcal T$，两条矩阵链是
<span id="eq:x97-two-proton-amplitudes"></span>

$$
\begin{aligned}
i\mathcal T_d
 &=-\frac{A}{2f_\pi}\bar wK_-u_s(p),\\
i\mathcal T_p
 &=(iA)\bar wK
   \frac{-\slashed r+m_p}{i(r^2+m_p^2-i0)}
   \frac{g_A\slashed k\gamma_5}{2f_\pi}u_s(p).
\end{aligned}
\tag{97.77}
$$

这里用物理$m_p$作为最低阶核子质量。内部线携带正电子的动量$r$，而传播的仍是核子，所以$r^2=0$时分母为$m_p^2$。

为了化简右图，先用$K\slashed r=\slashed r(C_1P_R+2C_2P_L)$把$\slashed r$移向左外线。再用$\slashed p\,u_s=-m_pu_s$以及$\{\gamma_5,\gamma^\mu\}=0$，逐步得到
<span id="eq:x97-nucleon-pole-reduction"></span>

$$
\begin{aligned}
\bar wK(-\slashed r+m_p)\slashed k\gamma_5u_s
 &=m_p\bar wK(\slashed p-\slashed r)\gamma_5u_s\\
 &=m_p\bar wK\slashed p\gamma_5u_s\\
 &=m_p^2\bar wK\gamma_5u_s
 =-m_p^2\bar wK_-u_s.
\end{aligned}
\tag{97.78}
$$

第一、二行分别在两个位置用到了左外线方程；第三行用$\slashed p\gamma_5u_s=-\gamma_5\slashed p u_s=m_p\gamma_5u_s$。整个过程没有给内部核子强加在壳条件。

代回两图，可见它们相长干涉：
<span id="eq:x97-proton-total-amplitude"></span>

$$
i\mathcal T_p=g_A\,i\mathcal T_d,\qquad
i\mathcal T=-\frac{A(1+g_A)}{2f_\pi}\bar wK_-u_s.
\tag{97.79}
$$

因子$1+g_A$因此来自两个不同的顶角结构。零π转换顶角与轴向发射顶角所组成的核子交换，增强了直接接触作用；共同的外态相位不会改变两图的相对号。

<span id="ex97-4e"></span>

### 自旋平均和相空间

定义$\overline K_-=\gamma^0K_-^\dagger\gamma^0=C_1^*P_R-2C_2^*P_L$。用$\sum_su_s\bar u_s=-\slashed p+m_p$、$\sum_tw_t\bar w_t=-\slashed r$，并平均初态的两个自旋，
<span id="eq:x97-proton-spin-trace"></span>

$$
\frac12\sum_{s,t}|\bar w_tK_-u_s|^2
 =\frac12\operatorname{tr}
 \left[K_-(-\slashed p+m_p)\overline K_-(-\slashed r)\right].
\tag{97.80}
$$

$|C_1|^2$项中，$P_L(-\slashed p+m_p)P_R=-\slashed pP_R$。由$\operatorname{tr}(\slashed p\slashed r)=-4p\cdot r$及含$\gamma_5$的二矩阵迹为零，计入外面的$1/2$后得到$-p\cdot r$。右手项相同，系数是$4|C_2|^2$。交叉项中$P_L(-\slashed p+m_p)P_L=m_pP_L$，再乘$\slashed r$取迹为零。于是
<span id="eq:x97-proton-spin-average"></span>

$$
\overline{|\mathcal T|^2}
 =\frac{|A|^2(1+g_A)^2}{4f_\pi^2}
       (-p\cdot r)(|C_1|^2+4|C_2|^2),\qquad
-p\cdot r=\frac{m_p^2-m_\pi^2}{2}.
\tag{97.81}
$$

若两个系数都实，最后的组合便化为$C_1^2+4C_2^2$；上式同时适用于复系数。交叉项消失也对应于无质量正电子的两个手征末态正交。

从相对论归一的两体测度出发，在质子静止系先用空间delta消去$\boldsymbol k$，令$\ell=|\boldsymbol r|$：
<span id="eq:x97-proton-two-body-measure"></span>

$$
\begin{aligned}
d\Phi_2
 &=(2\pi)^4\delta^{(4)}(p-r-k)
       \frac{d^3r}{(2\pi)^3\,2E_r}
       \frac{d^3k}{(2\pi)^3\,2E_k}\\
 &=\frac1{16\pi^2}\frac{\ell^2\,d\ell\,d\Omega}{E_rE_k}
                 \delta(m_p-E_r-E_k),\\
E_r&=\ell,\qquad E_k=\sqrt{\ell^2+m_\pi^2}.
\end{aligned}
\tag{97.82}
$$

剩下的能量delta有唯一正根，其Jacobian为
<span id="eq:x97-proton-phase-space-jacobian"></span>

$$
\ell_*=\frac{m_p^2-m_\pi^2}{2m_p},\qquad
\left.\frac{d(E_r+E_k)}{d\ell}\right|_*
 =\ell_*\left(\frac1{E_r}+\frac1{E_k}\right)_*,\qquad
d\Phi_2=\frac{\ell_*}{16\pi^2m_p}d\Omega.
\tag{97.83}
$$

末态为不同粒子，不需要$1/2!$。将测度乘初态归一$1/(2m_p)$并积分$4\pi$，便得
<span id="eq:x97-proton-decay-width"></span>

$$
\begin{aligned}
\Gamma(p\to e^+\pi^0)
 &=\frac{\ell_*}{8\pi m_p^2}\overline{|\mathcal T|^2}\\
 &=\frac{|A|^2(1+g_A)^2m_p}{128\pi f_\pi^2}
       \left(1-\frac{m_\pi^2}{m_p^2}\right)^2
       (|C_1|^2+4|C_2|^2).
\end{aligned}
\tag{97.84}
$$

它的维数为$6-2+1-4=1$，在$m_\pi\to m_p$时有二次阈值零。$128$同时包含单π顶角中的$1/2$、初态自旋平均和两体相空间；若把$f_\pi$改成另一常用的$\sqrt2f_\pi$归一，分母也须同时换算。

使用第83节的$m_p=0.938$ GeV、$m_{\pi^0}=0.135$ GeV、$f_\pi=0.0924$ GeV、$g_A=1.27$及上述匹配常数$A$，再代入上一小节的两个系数，得到
<span id="eq:x97-proton-lifetime-evaluated"></span>

$$
\begin{aligned}
\Gamma&=1.83960\times10^{-63}\ \mathrm{GeV},\\
\tau&=\frac{\hbar}{\Gamma}
       =3.57802\times10^{38}\ \mathrm s
       =1.13381\times10^{31}\ \mathrm{yr}.
\end{aligned}
\tag{97.85}
$$

换算取$\hbar=6.5821195695\times10^{-25}$ GeV s以及一年$365.25\times86400$秒。相同$g_5=0.55045$、$M_X$的朴素式给$1.86055\times10^{30}$年，故这个计算使寿命增加约6.09倍，但仍低于前面用作比较的历史限制$10^{33}$年。

这一比较中包含了强子矩阵元与短程运行两种效应。若在同一强子式里将$C_i(2)$换成未运行的$C_X$，宽度反而更小；一圈系数运行把它增大约8.67倍。因而相对朴素估计的寿命增长主要不能归因于运行本身。这里采用一圈短程系数与最低阶手征矩阵元，π动量约$0.459$ GeV，约为$4\pi f_\pi$的0.40；要给更精确的寿命，还需相应的高阶强子参数和阈值资料。

<span id="ex97-5"></span>

## 下型夸克与带电轻子的质量运行

先取一代，令两个Yukawa耦合均非零，将相互作用写成
<span id="eq:x97-mass-ratio-yukawa-input"></span>

$$
\mathcal L_Y
 =-Z_y y\,\epsilon^{ij}\varphi_i\ell_j\bar e
  -Z_{y'}y'\,\epsilon^{ij}\varphi_iq_{\alpha j}\bar d^\alpha
  +\mathrm{h.c.},\qquad r=\frac{y'}y.
\tag{97.86}
$$

高能匹配给$r(M_X)=1$。这里只求规范玻色子的一圈贡献，先不加入Yukawa自作用和味混合。由于两个质量都正比于同一个Higgs真空值，$r$也是共同方案、共同尺度上的下型夸克与带电轻子质量之比。

<span id="ex97-5a"></span>

### 为什么标量端点的图在比值中消去

一个Yukawa顶角含一个标量和两个费米场。规范玻色子可以连接两条费米腿，也可以从标量腿连向任一费米腿。先看后两图，统一把顶角记为$\varphi f h$。在其局部UV尾中令外标量动量为零，入射规范动量为$\ell$；标量顶角给$\ell_\mu$，内部费米动量为$-\ell$，领先分子给$+\slashed\ell$。于是
<span id="eq:x97-scalar-fermion-uv-kernel"></span>

$$
\ell_\mu P^{(\xi)\mu\nu}(\ell)=\xi\ell^\nu,\qquad
N_{\varphi f}
 =\slashed\ell\gamma_\nu P^{(\xi)\mu\nu}\ell_\mu
 =-\xi\ell^2.
\tag{97.87}
$$

另一条费米腿给相同的自旋核。与前面相同的两个顶角、三条内线和径向极点，使反项之和正比于
$\xi[T_\varphi\cdot T_f+T_\varphi\cdot T_h]$。规范不变性又给
<span id="eq:x97-common-higgs-pair-factor"></span>

$$
(T_\varphi+T_f+T_h)(\varphi f h)=0,\qquad
T_\varphi\cdot(T_f+T_h)(\varphi f h)
 =-C_2(\varphi)(\varphi f h).
\tag{97.88}
$$

两个Yukawa项使用同一个$\varphi$，其颜色Casimir为0、弱Casimir为$3/4$、超荷平方为$1/4$。所以标量—费米两图之和对两种耦合相同，在$Z_{y'}/Z_y$中消去；Landau规范中它们各自的局部极点已经为零。这一抵消只用了局部极点的共同群因子，并不要求不同外场的有限修正相等。

<span id="ex97-5b"></span>

### 两费米腿给出的差别

两费米交换可直接用式[（97.60）](#eq:x97-scalar-vertex-numerator)的标量核。在下型耦合中，颜色基本与反基本以delta收缩，$(T_q+T_{\bar d})\delta=0$，所以$T_q\cdot T_{\bar d}=-C_F=-4/3$。带电轻子没有颜色。两个耦合的第二费米腿都是弱单态，故这一类图没有弱因子。超荷积分别为$(1/6)(1/3)=1/18$与$(-1/2)(1)=-1/2$，从而两类耦合的群因子分别为
<span id="eq:x97-yukawa-group-difference"></span>

$$
\begin{aligned}
(-1)(+1)e^2&\longrightarrow
  \mathscr S_d=-\frac43g_3^2+\frac1{18}g_1^2
                    &&\text{（下型）},\\
(-1)(+1)e^2&\longrightarrow
  \mathscr S_e=-\frac12g_1^2
                    &&\text{（轻子）},\\
\mathscr S_d-\mathscr S_e
 &=-\frac43g_3^2+\frac59g_1^2.
\end{aligned}
\tag{97.89}
$$

因此在Landau规范中
<span id="eq:x97-yukawa-ratio-pole"></span>

$$
\ln\frac{Z_{y'}}{Z_y}
 =\frac{3(\mathscr S_d-\mathscr S_e)}{8\pi^2\varepsilon}
 =\frac{-4g_3^2+\frac53g_1^2}{8\pi^2\varepsilon}+O(g^4).
\tag{97.90}
$$

各超荷均取顶角中左Weyl场的值，与表中的表示一致。

<span id="ex97-5c"></span>

### 比值的反常维数

裸Yukawa还含外场归一：
<span id="eq:x97-bare-yukawa-ratio"></span>

$$
\begin{aligned}
y_0&=\widetilde\mu^{\varepsilon/2}
   \frac{Z_y}{(Z_\varphi Z_\ell Z_{\bar e})^{1/2}}\,y,\\
y'_0&=\widetilde\mu^{\varepsilon/2}
   \frac{Z_{y'}}{(Z_\varphi Z_qZ_{\bar d})^{1/2}}\,y',\\
r_0&=r\,\frac{Z_{y'}}{Z_y}
             \left(\frac{Z_\ell Z_{\bar e}}{Z_qZ_{\bar d}}\right)^{1/2}.
\end{aligned}
\tag{97.91}
$$

共同Higgs因子和两个工程尺度因子精确消去。其余费米因子不必彼此相同，但式[（97.64）](#eq:x97-landau-field-factors)表明它们在Landau规范的这一圈极部中都没有贡献。对固定$r_0$求导，仍用$dg_a/d\ln\mu=-\varepsilon g_a/2+O(g^3)$处理反项的二次分子，得到
<span id="eq:x97-mass-ratio-anomalous-dimension"></span>

$$
\gamma_r\equiv\frac{d\ln r}{d\ln\mu}
 =\frac{-8g_3^2+\frac{10}{3}g_1^2}{16\pi^2}+O(g^4).
\tag{97.92}
$$

色作用使$r$向低能增大，超荷贡献则稍微抵消这一趋势。

也可以用一般$\xi$核对这一步。由规范单态条件，
$2T_f\cdot T_h=C_2(\varphi)-C_2(f)-C_2(h)$。
两个Yukawa共有$C_2(\varphi)$，故它们费米Casimir和的差为$-2(\mathscr S_d-\mathscr S_e)$所对应的群系数。顶角比的$(3+\xi)$项与式[（97.91）](#eq:x97-bare-yukawa-ratio)中外费米因子的$-\xi$项相加，只留下3。这与直接取Landau极限相同。

<span id="ex97-5de"></span>

### 运行到弱标度和底夸克标度

把式[（97.92）](#eq:x97-mass-ratio-anomalous-dimension)改写成各逆耦合方程的积分。对$M_Z<\mu<M_X$，$b_3=-7$、$b_1=41/6$，因而
<span id="eq:x97-mass-ratio-high-running"></span>

$$
\begin{aligned}
d\ln r&=\frac47\,d\ln\alpha_3+\frac{10}{41}\,d\ln\alpha_1,\\
r(M_Z)&=
 \left[\frac{\alpha_3(M_Z)}{\alpha_5}\right]^{4/7}
 \left[\frac{\alpha_1(M_Z)}{(3/5)\alpha_5}\right]^{10/41}.
\end{aligned}
\tag{97.93}
$$

例如$(4/7)b_3/(2\pi)=-2/\pi$，正好恢复$-8g_3^2/(16\pi^2)$；超荷项同理。积分的边界值也同时保留了统一超荷的归一。

在$M_Z$以下移去顶夸克，并忽略电磁，五味QCD的$b_3=-23/3$给
<span id="eq:x97-mass-ratio-low-running"></span>

$$
\begin{aligned}
\alpha_3^{-1}(m_b)
 &=\alpha_3^{-1}(M_Z)+\frac{23}{6\pi}\ln\frac{m_b}{M_Z},\\
r(m_b)&=r(M_Z)
       \left[\frac{\alpha_3(m_b)}{\alpha_3(M_Z)}\right]^{12/23}.
\end{aligned}
\tag{97.94}
$$

两段的指数不同，因为顶夸克改变了规范耦合的跑动，而这里的质量反常维数分子仍是$-8g_3^2$。

使用与[系数的一圈运行](#ex97-3)相同的非超对称统一边界，并取历史示例输入$m_b(m_b)=4.3$ GeV，算得
<span id="eq:x97-tau-mass-prediction"></span>

$$
\begin{aligned}
r(M_Z)&=2.26457,\qquad \alpha_3(m_b)=0.212874,\\
\frac{r(m_b)}{r(M_Z)}&=1.35628,\qquad r(m_b)=3.07140,\\
m_\tau^{\rm pred}&=\frac{4.3\ \mathrm{GeV}}{r(m_b)}
                    =1.40001\ \mathrm{GeV}.
\end{aligned}
\tag{97.95}
$$

数值还可以通过高能段的$g_a$与$r$方程和低能段的$g_3,r$方程直接积分求得。与用作历史比较值的τ轻子质量约1.8 GeV相比，这个预言低约22%。这里忽略了电磁及有限匹配，把低能轻子质量参数直接与观测值比较；Yukawa自身的修正和统一阈值也还没有包含在所指定的一圈规范近似中。

这项结果说明，夸克与轻子的统一尺度质量相等，可以经过规范跑动变成低能约三倍的质量比。不过同类三代的规范荷相同，这种共同的乘法因子会在两代之比中消去；它不能自动修复正文式[（97.48）](#eq:c97-generation-mass-ratios)的错误质量关系。这正是最小模型还需要增加味结构的原因。

---

[← 第 96 节](/posts/srednicki-96/) · [章节地图](/srednicki/)
