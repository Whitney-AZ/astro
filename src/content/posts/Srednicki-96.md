---
title: 'Srednicki §96 最小超对称标准模型'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [96]
hideFromHome: true
draft: false
---

<span id="c96"></span>

上一节已给出构造超对称规范理论的方法：把物质装入手征超场，把规范场装入矢量超场，再用D项和全纯超势写出作用量。现在可以把第87–89章的标准模型放进这套结构。规范群仍然是$SU(3)\times SU(2)\times U(1)$，但每种已知场都要有与它配对的超伙伴；Higgs部分还需要两个手征二重态。这样得到的最小超对称标准模型（minimal supersymmetric standard model，MSSM），其新自由度和新耦合就有了明确的来源。

下面从场的表示写出作用量和软破缺项，随后求Higgs势的最低点及五个物理Higgs的树级质量。

<span id="c96-fields"></span>

## 把标准模型的场装入超多重态

三个规范群因子各需要一个矢量超场。它含原来的规范玻色子、伴随表示的Weyl规范微子以及实辅助场。物质超场则沿全左手记法取$L,\bar E,Q,\bar U,\bar D$，每种有三代。它们的Weyl分量正是原标准模型的轻子和夸克；标量分量称为超轻子（slepton）和超夸克（squark）。为把场名与表示一起看清，列成

| 手征超场          | $SU(3)\times SU(2)\times U(1)_Y$表示 | 标量与Weyl分量                           |
| ----------------- | ------------------------------------ | ---------------------------------------- |
| $L_{iI}$          | $(\mathbf1,\mathbf2,-1/2)$           | 左轻子二重态的超轻子、左轻子             |
| $\bar E_I$        | $(\mathbf1,\mathbf1,+1)$             | 带共轭电荷的超轻子、独立左Weyl场$\bar e$ |
| $Q_{\alpha iI}$   | $(\mathbf3,\mathbf2,+1/6)$           | 超夸克二重态、夸克二重态                 |
| $\bar U_I^\alpha$ | $(\bar{\mathbf3},\mathbf1,-2/3)$     | 共轭上型超夸克、左Weyl场$\bar u$         |
| $\bar D_I^\alpha$ | $(\bar{\mathbf3},\mathbf1,+1/3)$     | 共轭下型超夸克、左Weyl场$\bar d$         |
| $H_i$             | $(\mathbf1,\mathbf2,-1/2)$           | 一份Higgs标量、Higgs微子                 |
| $\bar H_i$        | $(\mathbf1,\mathbf2,+1/2)$           | 另一份Higgs标量、另一Higgs微子           |

横线都属于独立场名，不表示厄米共轭。特别是$H$与$\bar H$是两个独立的左手手征场；上指标$\bar H^i$则由$\bar H^i=\epsilon^{ij}\bar H_j$得到。弱指标的$\epsilon^{12}=+1$，所以标量分量可以按电荷排成
<span id="eq:c96-higgs-index-conventions"></span>

$$
H=\binom{H^0}{H^-},\qquad
\bar H=\binom{\bar H^+}{\bar H^0},\qquad
\bar H^1=\bar H_2,\quad \bar H^2=-\bar H_1.
\tag{96.1}
$$

两个Higgs的Weyl伙伴称为Higgs微子（higgsino）。[超势的全纯性与Higgs微子的反常相消](#ex96-1)共同要求这两个手征二重态。

各超场的动能直接用上一节的构造。若以$r=1,2,3$区分规范群因子，$\Phi$遍历表中所有场与代指标，则可紧凑写为
<span id="eq:c96-supersymmetric-kinetic-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}
={}&\sum_\Phi\left[\Phi^\dagger
       \exp\left(-2\sum_r g_rV_r^{A_r}T_{r,\Phi}^{A_r}\right)\Phi\right]_{22}\\
 &+\sum_r\left\{\frac14
       [\widehat W_r^{A_r a}\widehat W_{r a}^{A_r}]_F+\mathrm{h.c.}\right\}.
\end{aligned}
\tag{96.2}
$$

同一规范因子的伴随指标求和；不同群因子的生成元作用于不同槽，彼此对易。这里已把规范场强写成规范归一的伴随分量，等价于矩阵记法中的$\operatorname{Tr}/T(R)$。因而三个规范耦合及每个表示一经指定，规范微子与物质的耦合也由第95节固定。

<span id="c96-superpotential"></span>

## 超势给出的质量与相互作用

取三个一般三代Yukawa矩阵和一个Higgs质量参数，超势为
<span id="eq:c96-mssm-superpotential"></span>

$$
\begin{aligned}
W={}&-y_{IJ}\epsilon^{ij}H_iL_{jI}\bar E_J
       -y'_{IJ}\epsilon^{ij}H_iQ_{\alpha jI}\bar D_J^\alpha\\
 &-y''_{IJ}\bar H^iQ_{\alpha iI}\bar U_J^\alpha
       -\mu\epsilon^{ij}\bar H_iH_j.
\end{aligned}
\tag{96.3}
$$

第一、二项的弱单态使用反对称张量，第三项使用上指标$\bar H^i$，最后一项也是两个二重态的反对称缩并。每项的超荷和都为零，颜色槽也成对缩并。所有手征场维数为1，所以$y,y',y''$无量纲，而$[\mu]=1$。

怎样从这个超势读出普通的Yukawa作用？先看一般单项式$W=-\kappa XYZ$。它的交叉二阶导数为$W_{XY}=-\kappa z$及另两个循环项；每对在Hessian中出现两次。代入上一节的$-W_{rs}\psi_r\psi_s/2$，得到
<span id="eq:c96-cubic-superpotential-components"></span>

$$
\mathcal L_{\psi\psi}^{XYZ}
 =\kappa(x\psi_Y\psi_Z+y\psi_X\psi_Z+z\psi_X\psi_Y)+\mathrm{h.c.}
\tag{96.4}
$$

用小写$h,\bar h$表示Higgs最低标量，$\widetilde\ell,\widetilde e,\widetilde q,\widetilde u,\widetilde d$表示相应物质标量；横线场的标量仍取该横线场的规范表示。将式[（96.4）](#eq:c96-cubic-superpotential-components)分别用到三个Yukawa项，有
<span id="eq:c96-yukawa-and-partner-couplings"></span>

$$
\begin{aligned}
\mathcal L_{y}={}&y_{IJ}\epsilon^{ij}
 (h_i\ell_{jI}\bar e_J
  +\widetilde\ell_{jI}\psi_{H_i}\bar e_J
  +\widetilde e_J\psi_{H_i}\ell_{jI})\\
 &+y'_{IJ}\epsilon^{ij}
 (h_iq_{\alpha jI}\bar d_J^\alpha
  +\widetilde q_{\alpha jI}\psi_{H_i}\bar d_J^\alpha
  +\widetilde d_J^\alpha\psi_{H_i}q_{\alpha jI})\\
 &+y''_{IJ}
 (\bar h^iq_{\alpha iI}\bar u_J^\alpha
  +\widetilde q_{\alpha iI}\psi_{\bar H}^{\,i}\bar u_J^\alpha
  +\widetilde u_J^\alpha\psi_{\bar H}^{\,i}q_{\alpha iI})+\mathrm{h.c.}
\end{aligned}
\tag{96.5}
$$

每行第一项就是Higgs与两普通物质费米子的作用，另两项把一个物质费米子换成超伙伴，同时换入Higgs微子。超势中的负号使分量Yukawa项带正号。若对应分量场不改相位，与第88–89章所用的负Yukawa记号比较时，应取$y_{96}=-y_{88}$、$y'_{96}=-y'_{89}$、$y''_{96}=-y''_{89}$；这只是参数相位的转换。

再看$\mu$项。把其他标量置零，定义$I=\epsilon^{ij}\bar h_i h_j=\bar h_1h_2-\bar h_2h_1$，则$W_\mu=-\mu I$的四个一阶导数为
<span id="eq:c96-mu-f-potential"></span>

$$
\begin{aligned}
W_{h_1}&=\mu\bar h_2,&W_{h_2}&=-\mu\bar h_1,\\
W_{\bar h_1}&=-\mu h_2,&W_{\bar h_2}&=\mu h_1,\\
V_{F,H}&=|\mu|^2(h^\dagger h+\bar h^\dagger\bar h).
\end{aligned}
\tag{96.6}
$$

两个标量质量平方都为$|\mu|^2$。二阶导数还给Higgs微子的质量项
<span id="eq:c96-higgsino-mu-mass"></span>

$$
\mathcal L_{\widetilde h,\mu}
 =-\mu\psi_{H_1}\psi_{\bar H_2}
       +\mu\psi_{H_2}\psi_{\bar H_1}+\mathrm{h.c.}
\tag{96.7}
$$

每个相互配对的Weyl场都得到质量$|\mu|$。单独的超对称$\mu$项给不出负的Higgs质量平方，也不给标量$h\bar h+\mathrm{h.c.}$的混合质量；后者将由破缺效应产生。

<span id="c96-r-parity"></span>

## R宇称的选择

规范群还允许$\bar H^iL_{iI}$这样的手征双线性，它不在式[（96.3）](#eq:c96-mssm-superpotential)中。可用一个额外的离散对称性将它禁止，称为R宇称（R parity）。它要求所有通常的标准模型分量及两个Higgs标量为偶，所有超伙伴为奇。由于同一超场的标量与旋量取相反号，不能简单地给整个超场乘一个常数号；相容的超空间写法是
<span id="eq:c96-r-parity-superfield-law"></span>

$$
\Phi(x,\theta,\bar\theta)\mapsto
  \eta_\Phi\Phi(x,-\theta,-\bar\theta),\qquad
\eta_{L,\bar E,Q,\bar U,\bar D}=-1,\quad
\eta_{H,\bar H}=+1.
\tag{96.8}
$$

最低标量的号为$\eta_\Phi$，一次项Weyl分量的号为$-\eta_\Phi$，辅助$F$的号则为$\eta_\Phi$。对矢量超场取$V(\theta,\bar\theta)\mapsto V(-\theta,-\bar\theta)$：二次项中的规范玻色子为偶，三次项中的规范微子为奇，最高的$D$为偶。

每个超势Yukawa单项式含两个物质超场和一个Higgs，内禀号乘积为正；$\mu$项也为正。$\bar H L$却为负，所以被禁止。三个物质超场的规范单态$LL\bar E$、$LQ\bar D$和$\bar U\bar D\bar D$也都为奇，受到同一选择规则排除。动能与规范动能因配对或平方而为偶。

这一离散号还有一个直接的谱学后果。若作用量和真空都保持R宇称，一个R奇粒子的衰变末态必须含奇数个R奇粒子。对于完整可及谱中最轻的R奇态，末态只含普通粒子会违反R宇称，含另一个R奇态又没有可用的衰变相空间。因此最轻超伙伴（lightest supersymmetric particle，LSP）稳定。

<span id="c96-hidden-sector"></span>

## 用隐藏破缺背景描述软项

如果超对称在真空中精确保持，同一多重态中的玻色和费米质量必须相配。要使超伙伴与普通粒子具有不同质量，就需要超对称破缺。先看现有场为何没有自动解决这个问题。在不让超夸克、超轻子取得期望值的Higgs子空间，尚未加入破缺项时的势为
$V=|\mu|^2(x+y)+V_D$，其中$x=h^\dagger h$、$y=\bar h^\dagger\bar h$，$V_D\ge0$且为四次齐次函数。沿共同实缩放$(h,\bar h)\mapsto\rho(h,\bar h)$，有
<span id="eq:c96-visible-higgs-scaling"></span>

$$
V(\rho)=\rho^2|\mu|^2(x+y)+\rho^4V_D,\qquad
\left.\frac{dV}{d\rho}\right|_{\rho=1}
 =2|\mu|^2(x+y)+4V_D.
\tag{96.9}
$$

任何非零平稳点必须使右边两个非负项分别为零。若$\mu\ne0$，最低点只有两个Higgs都为零；若$\mu=0$，可有D平坦的Higgs真空，但全部$F,D$仍为零。这说明，在所选场配置和未加FI项的作用量中，现有Higgs本身不能给出所需的超对称破缺背景。

一种做法是让隐藏部分先发生自发破缺，再将效应传给可见场。将一个隐藏手征场的非零辅助期望冻结成赝场（spurion）
<span id="eq:c96-breaking-spurion"></span>

$$
S=tF_S,\qquad F_S=m_S^2,\qquad [S]=1,\quad[F_S]=2.
\tag{96.10}
$$

上一节的F判据说明非零$F_S$如何表示超对称破缺。将它作为固定背景后，可见场的拉格朗日量便出现显式的破缺参数。下面分别求出标量质量、规范微子质量及全纯软项；隐藏机制本身仍是模型输入。

<span id="c96-scalar-soft"></span>

### 标量质量

设传递相互作用的质量尺度为$m_M$，称为信使标度（messenger scale）。先加入$S^\dagger S$与物质实双线性的D项。为保持规范不变性，在两物质场之间放入相应的规范指数，并把带系数的实双线性记为$K_C$：
<span id="eq:c96-scalar-spurion-operator"></span>

$$
\begin{aligned}
K_C={}&C^{(H)}H^\dagger e^{-2\mathcal V_H}H
       +C^{(\bar H)}\bar H^\dagger e^{-2\mathcal V_{\bar H}}\bar H\\
 &+\sum_{\Phi=L,\bar E,Q,\bar U,\bar D}
       C^{(\Phi)}_{IJ}\Phi_I^\dagger e^{-2\mathcal V_\Phi}\Phi_J,\\
\mathcal L_{{\rm spur},D}&=\frac1{m_M^2}[S^\dagger S K_C]_{22},\qquad
\mathcal V_\Phi=\sum_r g_rV_r^{A_r}T_{r,\Phi}^{A_r}.
\end{aligned}
\tag{96.11}
$$

这里每个$C^{(\Phi)}$是代空间的无量纲厄米矩阵；两个Higgs的$C$为实数。因为$S^\dagger S=|F_S|^2t\bar t$已占满奇坐标次数，乘积中只需各物质超场的最低分量。在Wess–Zumino规范下$V|_0=0$，规范指数的最低分量为1，因此在求这个最低分量时，规范指数不改变结果：
<span id="eq:c96-soft-scalar-mass-matrix"></span>

$$
\begin{aligned}
\relax[S^\dagger S\Phi_I^\dagger e^{-2\mathcal V_\Phi}\Phi_J]_{22}
 &=|F_S|^2\phi_I^*\phi_J,\\
\mathcal L_{{\rm soft},\Phi}
 &=\frac{|F_S|^2}{m_M^2}C^{(\Phi)}_{IJ}\phi_I^*\phi_J
       =-(m_\Phi^2)_{IJ}\phi_I^*\phi_J,\\
m_\Phi^2&=-\frac{|F_S|^2}{m_M^2}C^{(\Phi)}.
\end{aligned}
\tag{96.12}
$$

赝场算符前的正号与惯用质量拉氏量前的负号，给出最后一行的负号。厄米性保证质量平方矩阵厄米，但不保证它的本征值为正。对绝对值为一量级的$C$本征值，质量尺度为
<span id="eq:c96-transmitted-mass-scale"></span>

$$
\sqrt{|m_\Phi^2|}\sim\frac{|F_S|}{m_M}
       =\frac{m_S^2}{m_M}.
\tag{96.13}
$$

Higgs的总二次参数还应加上式[（96.6）](#eq:c96-mu-f-potential)中的$|\mu|^2$。系数$C$允许不同的味结构，这些结构来自传递机制，而非由超对称单独决定。

<span id="c96-gaugino-soft"></span>

### 规范微子质量

规范微子质量可以由赝场乘规范场强平方的F项产生。以已经规范归一的伴随分量写规范收缩，有
<span id="eq:c96-gaugino-spurion-operator"></span>

$$
\mathcal L_{{\rm spur},\lambda}
 =\frac1{m_M}\left[S\sum_{r=1}^3C^{(r)}
       \widehat W_r^{A a}\widehat W_{r a}^{A}\right]_F+\mathrm{h.c.}
\tag{96.14}
$$

$S$已经带两个theta，故场强乘积只取最低的$\lambda_r^{A a}\lambda_{r a}^A$。与标准Majorana型Weyl质量项比较，得到
<span id="eq:c96-gaugino-masses"></span>

$$
\begin{aligned}
\mathcal L_{{\rm soft},\lambda}
 &=\sum_r C^{(r)}\frac{F_S}{m_M}\lambda_r^A\lambda_r^A+\mathrm{h.c.}\\
 &=-\frac12\sum_r(M_r\lambda_r^A\lambda_r^A+\mathrm{h.c.}),\qquad
 M_r=-2C^{(r)}\frac{F_S}{m_M}.
\end{aligned}
\tag{96.15}
$$

这里的2来自质量项的$1/2$归一；没有额外的$i$，因为第95节场强超场的最低分量是$+\lambda$。群收缩若改用矩阵迹，必须同时除以$T(R)$，才能使用本式的数值系数。三个$C^{(r)}$可以不同，但质量量级仍为$m_S^2/m_M$。

<span id="c96-holomorphic-soft"></span>

### 标量三次项与Higgs混合项

最后将赝场与超势的各项相乘。式[（96.3）](#eq:c96-mssm-superpotential)中三个$3\times3$矩阵各给9个独立项，另有一个$\mu$项，所以共有$9+9+9+1=28$个规范不变项。令$W_A$表示包括原系数在内的完整超势项，其维数为3，则
<span id="eq:c96-holomorphic-soft-terms"></span>

$$
\begin{aligned}
\mathcal L_{{\rm spur},F}
 &=\frac1{m_M}\left[S\sum_{A=1}^{28}C_AW_A(\Phi)\right]_F
       +\mathrm{h.c.}\\
 &=\frac{F_S}{m_M}\sum_{A=1}^{28}C_AW_A(\phi)+\mathrm{h.c.}
\end{aligned}
\tag{96.16}
$$

第二行只留下超势项的最低标量乘积，因而产生标量三次项和二次项，不再带物质费米子。把三类Yukawa项逐一代入，标量三次拉氏量为

$$
\begin{aligned}
\mathcal L_{{\rm soft},3}=-\frac{F_S}{m_M}\sum_{I,J}\Big\{
 &C_{IJ}^{(e)}y_{IJ}\epsilon^{ij}h_i\widetilde\ell_{jI}\widetilde e_J\\
 &+C_{IJ}^{(d)}y'_{IJ}\epsilon^{ij}h_i\widetilde q_{\alpha jI}\widetilde d_J^\alpha\\
 &+C_{IJ}^{(u)}y''_{IJ}\bar h^i\widetilde q_{\alpha iI}\widetilde u_J^\alpha
 \Big\}+\mathrm{h.c.}
\end{aligned}
$$

每个$I,J$可有独立的$C_{IJ}^{(e,d,u)}$。上型项仍使用升指标的$\bar h^i$，所以它的弱缩并和式[（96.3）](#eq:c96-mssm-superpotential)保持一致。

$\mu$项则给
<span id="eq:c96-higgs-mixing-soft-term"></span>

$$
\mathcal L_{{\rm soft},H\bar H}
 =-\left(b_{\rm c}\epsilon^{ij}\bar h_i h_j+\mathrm{h.c.}\right),\qquad
b_{\rm c}=C_\mu\mu\frac{F_S}{m_M},\qquad [b_{\rm c}]=2.
\tag{96.17}
$$

这就是此前没有出现的标量混合质量。若将$W_A$只定义成裸场单项式，Higgs双线性只有维数2，其系数必须另外带一个质量，不能仍把所有$C_A$都称为无量纲。按完整超势项乘$C_A$的参数化，严格为零的原耦合也使对应项为零；要容纳该耦合为零而软项独立非零的更一般情况，可以直接用有适当维数的独立软系数。

超势与规范动能指定了超对称相互作用，赝场背景则传入破缺参数。以上三类背景产生的项称为软破缺项（soft supersymmetry-breaking terms）：这里具体是标量质量、规范微子质量以及有质量量纲系数的标量三次和双线性作用。背景展开解释了共同质量量级，而不决定$C$的实际数值；若把它作为信使理论的局域展开，应在外部动量远低于$m_M$、$|F_S|/m_M^2\ll1$的范围内使用。

这些软项也保持已选R宇称：$S=tF_S$为偶，物质双线性、两个规范微子及每个原超势项的总号都为正。于是只要真空也保持该离散对称性，前面关于LSP的稳定性结论继续适用。把Higgs二次项与规范D项产生的四次项合在一起，就能求电弱真空及其附近的粒子谱。

<span id="ex96-1"></span>

## 为什么需要两个Higgs二重态

普通标准模型只有一个Higgs标量二重态，却能同时给上型和下型夸克质量，因为Yukawa作用可以分别使用它和它的复共轭。超势的情况不同。手征条件为$\overline{\mathcal D}_{\dot a}\Phi=0$，其共轭满足的是$\mathcal D_a\Phi^\dagger=0$；一般的$\overline{\mathcal D}_{\dot a}\Phi^\dagger$不为零。因此把$H^\dagger$放进超势，会破坏第95章构造F项所需的手征性。用$\epsilon$把弱指标转换，也不会改变这个超空间条件。

这一限制与超荷一起决定了第二个Higgs的表示。下型夸克项和带电轻子项需要超荷$-1/2$的$H$，上型夸克项则需要超荷$+1/2$的独立手征场：
<span id="eq:x96-holomorphic-hypercharges"></span>

$$
\begin{aligned}
Y(H)+Y(Q)+Y(\bar D)&=-\frac12+\frac16+\frac13=0,\\
Y(H)+Y(L)+Y(\bar E)&=-\frac12-\frac12+1=0,\\
Y(\bar H)+Y(Q)+Y(\bar U)&=\frac12+\frac16-\frac23=0.
\end{aligned}
\tag{96.18}
$$

所以当要求保留这些可重整Yukawa耦合时，不能只用一个手征Higgs二重态。

量子规范一致性给出相同的要求。普通Higgs是标量，不贡献手征三角反常；把它推广成手征超场以后，却新增一个左手Higgs微子二重态。[第89节](/posts/srednicki-89/)已逐表示算出一代夸克、轻子的反常相消。新标量仍不贡献，而新增费米子的系数必须另外相加。对于一个颜色单态、超荷为$Y$的弱二重态，相关群因子为
<span id="eq:x96-higgsino-anomalies"></span>

$$
\mathcal A_{SU(2)^2Y}=T(\mathbf2)Y=\frac Y2,\qquad
\mathcal A_{Y^3}=2Y^3,\qquad
\mathcal A_{{\rm grav}^2Y}=2Y.
\tag{96.19}
$$

第一个式子的$1/2$来自弱生成元的迹归一；后两个式子的2数出二重态中的两个左手分量。单独$Y=-1/2$的Higgs微子给出$-1/4,-1/4,-1$，都不能由已相消的原物质谱补偿。加入$Y=+1/2$的Higgs微子后，三个系数逐项反号，总和为零。它们也不带颜色，不新增色反常；规范微子处在实的伴随表示中，不引入新的手征规范反常。由此，两个Higgs既使超势能够产生所需的费米子质量，也使新增手征费米子的规范反常相消。

<span id="ex96-2"></span>

## Higgs势及电弱真空

以下用$H,\bar H$表示两个最低标量，其他物质标量置零。考察它们的树级势。两个范数项本来就厄米，只有复混合项需要加上共轭。将混合质量参数记为$m_3^2=b_{\rm c}$，先允许它为复，二次拉氏量为
<span id="eq:x96-hermitian-higgs-quadratic"></span>

$$
\begin{aligned}
\mathcal L_{H,2}&=-aH^\dagger H-c\bar H^\dagger\bar H
                 -(b_{\rm c}I+b_{\rm c}^*I^*),\\
a&=m_1^2=|\mu|^2+m_{H,\rm soft}^2,\qquad
c=m_2^2=|\mu|^2+m_{\bar H,\rm soft}^2,\\
I&=\epsilon^{ij}\bar H_iH_j=\bar H^+H^- -\bar H^0H^0.
\end{aligned}
\tag{96.20}
$$

$a,c$是可正可负的实质量平方参数。对一个Higgs作常相位重定义，可以把混合系数改写为$b=|b_{\rm c}|\ge0$；与它相连的其他耦合也随同改相位。这个选择仅是下面研究Higgs势的参数约定。

<span id="ex96-2a"></span>

### 从辅助场得到四次势

为整理弱指标，记$x=H^\dagger H$、$y=\bar H^\dagger\bar H$、$z=H^\dagger\bar H$，并令$J^a=H^\dagger\sigma^aH+\bar H^\dagger\sigma^a\bar H$。第95章的辅助场拉氏量在此成为
<span id="eq:x96-auxiliary-completion"></span>

$$
\begin{aligned}
\mathcal L_D={}&\frac12D_2^aD_2^a-\frac{g_2}{2}D_2^aJ^a
           +\frac12D_1^2-\frac{g_1}{2}D_1(-x+y)\\
={}&\frac12\left(D_2^a-\frac{g_2}{2}J^a\right)^2
 +\frac12\left(D_1-\frac{g_1}{2}(-x+y)\right)^2\\
 &-\frac{g_2^2}{8}J^aJ^a-\frac{g_1^2}{8}(x-y)^2.
\end{aligned}
\tag{96.21}
$$

弱生成元是$\sigma^a/2$，两个超荷是$\mp1/2$，这分别给两个线性项中的$1/2$。消去$D$后，最后一行留在拉氏量中；由$\mathcal L=-V+\cdots$，相应势取正号。

利用$\sigma^a_{ij}\sigma^a_{kl}=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}$，交叉项可以逐槽缩并为
<span id="eq:x96-pauli-quartic-reduction"></span>

$$
\begin{aligned}
(H^\dagger\sigma^aH)(\bar H^\dagger\sigma^a\bar H)
 &=H_i^*H_j\bar H_k^*\bar H_l
       (2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl})\\
 &=2|H^\dagger\bar H|^2-(H^\dagger H)(\bar H^\dagger\bar H)
 =2|z|^2-xy,\\
J^aJ^a&=x^2+y^2+2(2|z|^2-xy)=(x-y)^2+4|z|^2.
\end{aligned}
\tag{96.22}
$$

同一个收缩公式在两个场相同时给单场平方$x^2$或$y^2$。另一个有用恒等式来自两个复二重态的行列式：
<span id="eq:x96-gram-identity"></span>

$$
\begin{aligned}
|I|^2
 &=|\bar H_1H_2-\bar H_2H_1|^2\\
 &=(|H_1|^2+|H_2|^2)(|\bar H_1|^2+|\bar H_2|^2)
       -|H_1^*\bar H_1+H_2^*\bar H_2|^2
 =xy-|z|^2.
\end{aligned}
\tag{96.23}
$$

将二次势与四次势相加，得到
<span id="eq:x96-complete-higgs-potential"></span>

$$
\begin{gathered}
V=ax+cy+2b\operatorname{Re}I+\lambda_D(x-y)^2+k_D|z|^2,\\
\lambda_D=\frac{g_1^2+g_2^2}{8}>0,\qquad k_D=\frac{g_2^2}{2}>0.
\end{gathered}
\tag{96.24}
$$

这里$g_1$仍为普通超荷归一的耦合。超对称把四次耦合固定为规范耦合的平方，因而真空条件及Higgs质量之间会出现普通双Higgs模型所没有的关系。

<span id="ex96-2b"></span>

### 势有下界的条件

先固定两个场的长度$x,y$，只改变相对方向和相位。混合项在$I$为负实时最小。由式[（96.23）](#eq:x96-gram-identity)，若令$q=|z|^2\in[0,xy]$，与方向有关的势便为$-2b\sqrt{xy-q}+k_Dq$。在区间内部，其导数为$b/\sqrt{xy-q}+k_D>0$，所以最小值在$q=0$。这说明两双重态正交时能量最低；若其中一个场为零，结论仍连续成立。

把相对方向极小化后，令$\Sigma=x+y$、$\Delta=x-y$，则$\Sigma\ge|\Delta|$；再记$A=a+c$、$d=a-c$。势化为
<span id="eq:x96-orientation-minimized-potential"></span>

$$
V_{\rm red}=\frac A2\Sigma+\frac d2\Delta
 -b\sqrt{\Sigma^2-\Delta^2}+\lambda_D\Delta^2.
\tag{96.25}
$$

沿$\Delta=0$方向，四次势消失，$V=(A/2-b)\Sigma$。所以$A<2b$必使势无下界。反过来，用$\sqrt{\Sigma^2-\Delta^2}\le\Sigma$并完成平方，得到
<span id="eq:x96-global-lower-bound"></span>

$$
V\ge\left(\frac A2-b\right)\Sigma
 +\lambda_D\left(\Delta+\frac{d}{4\lambda_D}\right)^2
 -\frac{d^2}{16\lambda_D}.
\tag{96.26}
$$

若$A\ge2b$，右边已有一个与场值无关的有限下界。因此，势有下界的充要条件为
<span id="eq:x96-boundedness-condition"></span>

$$
m_1^2+m_2^2\ge2|m_3^2|.
\tag{96.27}
$$

等号处的势仍有下界。要在真空附近展开粒子场，还须确定这个下界是否在有限场值处取到。

<span id="ex96-2c"></span>

### 有限场值处的破缺真空

先取$A>2b$。此时式[（96.26）](#eq:x96-global-lower-bound)中的第一项随场范数增大而趋于正无穷，连续势必在有限场值达到最小。只须再判断原点是否最低。中性实部的二次矩阵为$\left(\begin{smallmatrix}a&-b\\-b&c\end{smallmatrix}\right)$，虚部及两组带电实部的矩阵只在混合项的号上有所不同。它们的特征多项式均为$(a-u)(c-u)-b^2$，所以本征值为
<span id="eq:x96-origin-quadratic-eigenvalues"></span>

$$
\lambda_\pm^{(0)}
 =\frac12\left(A\pm\sqrt{d^2+4b^2}\right),\qquad
\lambda_+^{(0)}\lambda_-^{(0)}=ac-b^2.
\tag{96.28}
$$

每支在八个规范化实标量中各出现四次。由于$A>0$，原点有负曲率恰好要求$ac<b^2$；沿该负方向取足够小的场值，负的二次项超过正的四次项，势就低于原点。因而通常的有限破缺域是
<span id="eq:x96-strict-breaking-domain"></span>

$$
a+c>2b,\qquad ac<b^2.
\tag{96.29}
$$

若$ac\ge b^2$，二次势半正定，四次势也非负，原点便是最低点。在$ac=b^2$的临界线上，二次核虽有零方向，四次势却仍把非零场值抬高。要使四次项也为零，须有$x=y,z=0$，而这个方向的二次系数$A/2-b$严格为正，所以此时原点仍是唯一最低点。

有界条件的等号需要直接使用原势。若$A=2b>0$，记$\Delta_*=-d/(4\lambda_D)$，则
<span id="eq:x96-positive-b-boundary"></span>

$$
V_{\rm red}=\lambda_D(\Delta-\Delta_*)^2
 -\frac{d^2}{16\lambda_D}
 +b\left(\Sigma-\sqrt{\Sigma^2-\Delta^2}\right).
\tag{96.30}
$$

当$d\ne0$时，第一项为零要求$\Delta=\Delta_*\ne0$；在任何有限$\Sigma$，最后一项仍为正。固定这个$\Delta$，其正差为
$b\Delta_*^2/(\Sigma+\sqrt{\Sigma^2-\Delta_*^2})$，只在$\Sigma\to\infty$时趋于零。所以势虽有下界，却没有有限最低真空。若$d=0$，则$a=c=b>0$，$\Delta=0$上的所有场尺度均给$V=0$；原点和非零真空共处一族平坦方向，树级势没有选出破缺尺度。

当$b=0,A=0$时，上述正差消失，情形随之改变。此时$c=-a$，完整势是
<span id="eq:x96-zero-b-flat-vacua"></span>

$$
\begin{gathered}
V=\lambda_D\left(\Delta+\frac{a}{2\lambda_D}\right)^2
 +k_D|z|^2-\frac{a^2}{4\lambda_D},\\
\Delta=-\frac{a}{2\lambda_D},\quad z=0,\quad
\Sigma\ge\frac{|a|}{2\lambda_D}.
\end{gathered}
\tag{96.31}
$$

第二行给出全部最小值，可以在有限场值达到。例如$a<0$时，$H=(\sqrt{-a/(2\lambda_D)},0)^T$、$\bar H=0$已经取到最低值；同时增加$x,y$并保持它们的差不变，又得到双场均非零的最低点。只要$a\ne0$，这一平坦族不含原点；若$a=c=b=0$，则退化成包含原点的D平坦族。

在式[（96.29）](#eq:x96-strict-breaking-domain)内，$b=0$也允许破缺，不过只有一个二次系数为负，只有相应的二重态凝聚。由这些结果可见，严格不等式给出尺度确定的通常破缺域；等号边界既可能只有无穷远处的下确界，也可能有有限的平坦真空族。

<span id="ex96-2d"></span>

### 破缺方向与五个物理Higgs

前面已证明，最低点可取两个二重态正交。若$H$非零，用弱规范转动把它转成第一分量非零，正交性便使$\bar H$只余第二分量。混合项选定两者乘积的相位；再利用剩余规范相位，可以写成
<span id="eq:x96-neutral-vacuum"></span>

$$
\langle H\rangle=\frac1{\sqrt2}\binom{v}{0},\qquad
\langle\bar H\rangle=\frac1{\sqrt2}\binom{0}{\bar v},\qquad
v,\bar v\ge0.
\tag{96.32}
$$

$b=0$时，势还不依赖两场乘积的相位；选择平坦族中的一个实成员即可使用同样写法。一个场为零的端点也能如此表示。

两非零真空分量的电荷分别为$+1/2-1/2=0$及$-1/2+1/2=0$，因此$Q=T^3+Y$不破缺。$T^1,T^2$把这些分量转向带电分量，另一个与$Q$独立的中性生成元改变它们的相位；只要$v^2+\bar v^2>0$，就有三个破缺规范方向。两复二重态原有八个实标量自由度，三个方向成为$W^\pm,Z$的纵向自由度，于是余下五个物理标量。

其中四个实带电分量减去两条带电规范方向，剩下一个复带电场，即一对$H^+,H^-$粒子。四个实中性分量减去一条中性规范方向，剩下三个中性粒子。这个计数适用于所选的非零真空；在原点规范群没有破缺，八个实标量仍全部保留。

<span id="ex96-2e"></span>

### 真空期望值之比

把式[（96.32）](#eq:x96-neutral-vacuum)代入势，得到
<span id="eq:x96-neutral-potential"></span>

$$
V_N=\frac a2v^2+\frac c2\bar v^2-bv\bar v
 +\frac G{32}(v^2-\bar v^2)^2,\qquad G=g_1^2+g_2^2.
\tag{96.33}
$$

分别对两个实真空参数求导，而不预先除以它们，有
<span id="eq:x96-undivided-stationarity"></span>

$$
\begin{aligned}
0&=av-b\bar v+\frac G8v(v^2-\bar v^2),\\
0&=c\bar v-bv-\frac G8\bar v(v^2-\bar v^2).
\end{aligned}
\tag{96.34}
$$

若$b>0$且真空非零，两个式子不允许$v,\bar v$中只有一个为零。此时才可分别除以$v,\bar v$，再相加消去四次项。取$\tan\beta=\bar v/v$，便得到
<span id="eq:x96-tan-beta-relation"></span>

$$
\tan\beta+\cot\beta=\frac{a+c}{b},\qquad
\sin2\beta=\frac{2b}{a+c}.
\tag{96.35}
$$

这里的$m_3^2$已按相位约定取正。对于$b=0$的真空，应该回到式[（96.34）](#eq:x96-undivided-stationarity)，不能在这个商中代入零。

为了同时确定真空尺度，记$v_T^2=v^2+\bar v^2$、$c_\beta=v/v_T$、$s_\beta=\bar v/v_T$。由两个Higgs的协变动能，各自的带电质量项贡献$g_2^2v_i^2/4$，中性二次型贡献$v_i^2(g_2W^3-g_1B)^2/8$，相加给出
<span id="eq:x96-vector-masses"></span>

$$
M_W^2=\frac{g_2^2v_T^2}{4},\qquad
M_Z^2=\frac{Gv_T^2}{4}.
\tag{96.36}
$$

驻定条件于是也可写成
<span id="eq:x96-soft-parameters-at-vacuum"></span>

$$
a=b\tan\beta-\frac{M_Z^2}{2}\cos2\beta,\qquad
c=b\cot\beta+\frac{M_Z^2}{2}\cos2\beta.
\tag{96.37}
$$

相减，并利用$b(\tan\beta-\cot\beta)=-A\cos2\beta$，得到$d=-(A+M_Z^2)\cos2\beta$。在通常的$b>0$严格破缺域中，$d$不为零，因此两支角度中应取
<span id="eq:x96-vacuum-angle-and-scale"></span>

$$
\begin{gathered}
\cos2\beta=-\operatorname{sgn}(d)\sqrt{1-\frac{4b^2}{A^2}},\\
M_Z^2=-\frac d{\cos2\beta}-A>0.
\end{gathered}
\tag{96.38}
$$

最后的不等式等价于$d^2>A^2-4b^2$，也就是$ac<b^2$，与前面从原点曲率得到的条件一致。若$b=0,A>0,a<0$，未相除的驻定方程直接给$v^2=-8a/G,\bar v=0$；若$c<0$则交换两个场。平坦边界上的$v_T$仍由所选真空成员给定。

<span id="ex96-spectrum"></span>

### 五个Higgs的质量

为了看清被规范场吸收的方向和留下的粒子，按规范化实场展开
<span id="eq:x96-canonical-real-fluctuations"></span>

$$
\begin{aligned}
H^0&=\frac{v+h_1+ia_1}{\sqrt2},&
\bar H^0&=\frac{\bar v+h_2+ia_2}{\sqrt2},\\
H^-&=\frac{c_1+id_1}{\sqrt2},&
\bar H^+&=\frac{c_2+id_2}{\sqrt2}.
\end{aligned}
\tag{96.39}
$$

各实场的动能均为$-\tfrac12(\partial q)^2$，所以势的二阶导数就是质量平方矩阵。中性混合项展开为$-b(v+h_1)(\bar v+h_2)+ba_1a_2$；中性四次项则为
$G[(v+h_1)^2+a_1^2-(\bar v+h_2)^2-a_2^2]^2/32$。前一式使偶、奇场的交叉二阶导数分别为$-b,+b$，后一式另给偶场交叉项$-Gv\bar v/4$。因此在尚未使用驻定条件时，有
<span id="eq:x96-neutral-hessians"></span>

$$
\begin{aligned}
\mathcal M_O^2&=
 \begin{pmatrix}a+G\delta_v/8&b\\b&c-G\delta_v/8\end{pmatrix},\\
\mathcal M_E^2&=
 \begin{pmatrix}
 a+G(3v^2-\bar v^2)/8&-b-Gv\bar v/4\\
 -b-Gv\bar v/4&c+G(3\bar v^2-v^2)/8
 \end{pmatrix},\qquad \delta_v=v^2-\bar v^2.
\end{aligned}
\tag{96.40}
$$

奇场矩阵作用于$(a_1,a_2)$，偶场矩阵作用于$(h_1,h_2)$。例如偶场第一对角元中的四次贡献，来自$\partial_{h_1}^2[(v+h_1)^2-\bar v^2]^2|_0=4(3v^2-\bar v^2)$，乘$G/32$后正是该项的系数。

带电涨落还要保留$k_D|z|^2$。它的二阶项由
<span id="eq:x96-charged-inner-product-expansion"></span>

$$
z=\frac12\{v(c_2+id_2)+\bar v(c_1-id_1)\}+O(q^2)
\tag{96.41}
$$

给出。在电荷为负一的复列$\chi=(H^-,(\bar H^+)^*)^T$中，二次势为$\chi^\dagger\mathcal K_C\chi$，其中
<span id="eq:x96-charged-hessian"></span>

$$
\mathcal K_C=
\begin{pmatrix}
a+G\delta_v/8+g_2^2\bar v^2/4&b+g_2^2v\bar v/4\\
b+g_2^2v\bar v/4&c-G\delta_v/8+g_2^2v^2/4
\end{pmatrix}.
\tag{96.42}
$$

这个矩阵也作用于实列$(c_1,c_2)$；虚列$(d_1,d_2)$的矩阵要在两边各乘$\operatorname{diag}(1,-1)$，因为$\chi$的第二个场取了复共轭。它们的本征值相同。

现在使用驻定条件。对于$b,v,\bar v$均非零的情形，式[（96.37）](#eq:x96-soft-parameters-at-vacuum)使奇场两个对角元化为$b\tan\beta,b\cot\beta$，再用$b=As_\beta c_\beta$，得到
<span id="eq:x96-vacuum-mass-projectors"></span>

$$
\begin{aligned}
n&=\binom{s_\beta}{c_\beta},\qquad
\mathcal M_O^2=A nn^T,\qquad
\mathcal K_C=(A+M_W^2)nn^T,\\
\mathcal M_E^2&=
A\begin{pmatrix}s_\beta^2&-s_\beta c_\beta\\-s_\beta c_\beta&c_\beta^2\end{pmatrix}
+M_Z^2\begin{pmatrix}c_\beta^2&-s_\beta c_\beta\\-s_\beta c_\beta&s_\beta^2\end{pmatrix}.
\end{aligned}
\tag{96.43}
$$

这些矩阵形式也适用于已分类的$b=0$有限真空，但要直接用未相除的方程验证。例如$\bar v=0$的端点满足$a+Gv^2/8=0$，奇场第二对角元变成$c-Gv^2/8=a+c=A$，第一对角元和非对角元均为零；这正是$s_\beta=0$的投影式。若$b=A=0$且两个真空值非零，两个奇场对角元都为零，带电和偶场矩阵只余规范耦合部分，同样给出式[（96.43）](#eq:x96-vacuum-mass-projectors)。

$n$是单位向量，其正交方向为$(c_\beta,-s_\beta)$。因此规范零方向和相应的物理组合为
<span id="eq:x96-goldstones-and-charged-mass"></span>

$$
\begin{aligned}
G^0&=c_\beta a_1-s_\beta a_2,&
A^0&=s_\beta a_1+c_\beta a_2,\\
G^-&=c_\beta H^- -s_\beta(\bar H^+)^*,&
H^-_{\rm phys}&=s_\beta H^-+c_\beta(\bar H^+)^*,\\
m_{A^0}^2&=A,&m_{H^\pm}^2&=A+M_W^2.
\end{aligned}
\tag{96.44}
$$

这里$G^-$包含两条实规范方向，与$G^0$合起来恰好是前面所数的三条。$A^0$是中性奇场，另两个中性粒子来自偶场矩阵的对角化。

偶场矩阵的迹为$A+M_Z^2$。计算行列式时，两个纯平方项各自相消，留下
<span id="eq:x96-even-mass-determinant"></span>

$$
\begin{aligned}
\det\mathcal M_E^2
 &=(As_\beta^2+M_Z^2c_\beta^2)
   (Ac_\beta^2+M_Z^2s_\beta^2)
   -(A+M_Z^2)^2s_\beta^2c_\beta^2\\
 &=A M_Z^2(s_\beta^4+c_\beta^4-2s_\beta^2c_\beta^2)
 =A M_Z^2\cos^22\beta.
\end{aligned}
\tag{96.45}
$$

因而特征方程为$u^2-(A+M_Z^2)u+A M_Z^2\cos^22\beta=0$。按$m_H^2\ge m_h^2$排列两根，得到
<span id="eq:x96-even-higgs-masses"></span>

$$
m_{H,h}^2=\frac12\left[A+M_Z^2
 \pm\sqrt{(A+M_Z^2)^2-4AM_Z^2\cos^22\beta}\right].
\tag{96.46}
$$

这样，三中性粒子为$h,H,A^0$，另有$H^\pm$。一般严格破缺域中五个物理质量平方均为正。若$b=0,A>0$且只有一个场凝聚，两个偶场质量平方直接成为$\{A,M_Z^2\}$。在$a=c=b>0$的平坦族中，$\cos2\beta=0$，故$m_h^2=0$；若$b=A=0$，则$m_h^2=m_A^2=0$。这些新增零模是树级平坦方向上的物理标量，不能再算作被规范场吸收的自由度。

四次耦合由规范耦合固定，还限制了最轻Higgs的树级质量。取沿真空的单位向量$u=(c_\beta,s_\beta)^T$，式[（96.43）](#eq:x96-vacuum-mass-projectors)中的$A$部分作用于它为零，因而
<span id="eq:x96-tree-higgs-upper-bound"></span>

$$
u^T\mathcal M_E^2u=M_Z^2\cos^22\beta,\qquad
m_h^2\le M_Z^2\cos^22\beta\le M_Z^2.
\tag{96.47}
$$

第一个不等式可把$u$展开在偶场矩阵的两个正交本征向量上来理解：二次型是两个本征值的加权平均，权重非负且和为1，故不小于较小的本征值。这个结果展示了超对称对Higgs势的约束；要比较量子理论的粒子质量，还需要把辐射修正加入同一质量矩阵。

---

[← 第 95 节](/posts/srednicki-95/) · [章节地图](/srednicki/) · [第 97 节 →](/posts/srednicki-97/)
