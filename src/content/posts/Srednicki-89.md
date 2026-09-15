---
title: 'Srednicki §89 标准模型：夸克部分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [89]
hideFromHome: true
draft: false
---

<span id="c89"></span>

夸克与轻子一样由自旋二分之一的场描述，不过它还带有颜色。六种夸克按$(u,d)$、$(c,s)$、$(t,b)$分为三代；[第83节](/posts/srednicki-83/#c83)已经列出用于低能讨论的质量输入及其尺度。先只保留第一代，求出它与Higgs场、电弱规范场的相互作用。到三代时，上型和下型夸克的质量需要分别对角化，两次换基的差别便会留在带电流中。这就是夸克混合的来源。

<span id="c89-fields"></span>

## 一代夸克及两个汤川耦合

沿上一节全部采用左Weyl场。一代夸克及Higgs的表示为
<span id="eq:c89-representations"></span>

$$
\begin{aligned}
q&\sim(\mathbf3,\mathbf2,+\tfrac16),
&\bar u&\sim(\overline{\mathbf3},\mathbf1,-\tfrac23),\\
\bar d&\sim(\overline{\mathbf3},\mathbf1,+\tfrac13),
&\varphi&\sim(\mathbf1,\mathbf2,-\tfrac12).
\end{aligned}
\tag{89.1}
$$

各括号依次指$SU(3)$、$SU(2)$和$U(1)$。$\bar u,\bar d$的横线属于场名；它们是独立左手场，处于反色三重态。若基本表示的矩阵为$R=e^{i\theta^At^A}$，其复共轭表示就是
<span id="eq:c89-antifundamental"></span>

$$
R^*=e^{-i\theta^At^{A*}}
     =e^{i\theta^A\bar t^A},\qquad
\bar t^A=-t^{A*}=-t^{AT},\qquad
\operatorname{Tr}t^At^B=\frac12\delta^{AB}.
\tag{89.2}
$$

最后一个转置用到了$t^A$的厄米性。因此反色场的协变导数必须用$\bar t^A$。为了分清两个非阿贝尔群，把色规范场和弱规范场分别写作$G_\mu^A$、$A_\mu^a$。色指标为$\alpha,\beta$，弱指标为$i,j$，则
<span id="eq:c89-covariant-derivatives"></span>

$$
\begin{aligned}
(D_\mu q)_{\alpha i}
 &=\partial_\mu q_{\alpha i}
 -ig_3G_\mu^A(t^A)_\alpha{}^\beta q_{\beta i}\\
 &\quad-ig_2A_\mu^a(T^a)_i{}^j q_{\alpha j}
 -\frac{i g_1}{6}B_\mu q_{\alpha i},\\
(D_\mu\bar u)^\alpha
 &=\partial_\mu\bar u^\alpha
 -ig_3G_\mu^A(\bar t^A)^\alpha{}_{\beta}\bar u^\beta
 +\frac{2i g_1}{3}B_\mu\bar u^\alpha,\\
(D_\mu\bar d)^\alpha
 &=\partial_\mu\bar d^\alpha
 -ig_3G_\mu^A(\bar t^A)^\alpha{}_{\beta}\bar d^\beta
 -\frac{i g_1}{3}B_\mu\bar d^\alpha,
\qquad T^a=\frac{\sigma^a}{2}.
\end{aligned}
\tag{89.3}
$$

弱生成元不作用于颜色，故第一行的弱项保留自由色指标$\alpha$。色生成元则必须按场所属的表示选取：$q$用$t^A$，$\bar u,\bar d$用$\bar t^A$。

选取标准动能归一，一代费米动能为
<span id="eq:c89-kinetic"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}
 &=i q^{\dagger\alpha i}\bar\sigma^\mu(D_\mu q)_{\alpha i}
 +i\bar u^\dagger_\alpha\bar\sigma^\mu(D_\mu\bar u)^\alpha\\
 &\quad+i\bar d^\dagger_\alpha\bar\sigma^\mu(D_\mu\bar d)^\alpha.
\end{aligned}
\tag{89.4}
$$

这些左手表示的直和不是实表示：例如$q$的共轭表示$(\overline{\mathbf3},\mathbf2,-1/6)$并未出现在原场组中。宇称把左手变成右手，而右手共轭场的规范表示不能按同一组场配对，所以完整电弱理论是手征的。QCD本身的情况将在组成狄拉克场后看得更清楚。

Higgs取真空值之前，不能直接写一个夸克质量项。两个左Weyl场组成洛伦兹标量后，其内部表示还必须含规范单态。两个色三重态或两个反三重态分别给$3\otimes3=6\oplus\bar3$、$\bar3\otimes\bar3=\bar6\oplus3$，都没有色单态。余下可能含色单态的双线性只有
<span id="eq:c89-mass-obstruction"></span>

$$
q\bar d\sim(\mathbf1\oplus\mathbf8,\mathbf2,+\tfrac12),
\qquad
q\bar u\sim(\mathbf1\oplus\mathbf8,\mathbf2,-\tfrac12).
\tag{89.5}
$$

它们仍是弱双重态，不能单独组成规范不变的质量项。

乘入一个Higgs场便有了所需单态。$q\bar d$应乘超荷$-1/2$的$\varphi$，两个弱双重态用$\epsilon^{ij}$收缩；$q\bar u$应乘超荷$+1/2$的$\varphi^\dagger$，用共轭指标直接收缩。两个超荷和分别为
<span id="eq:c89-yukawa-hypercharges"></span>

$$
-\frac12+\frac16+\frac13=0,\qquad
+\frac12+\frac16-\frac23=0.
\tag{89.6}
$$

在$3\otimes\bar3$以及所需的两个弱双重态乘积中，单态都只出现一次。因此两个允许的汤川相互作用为
<span id="eq:c89-yukawa"></span>

$$
\mathcal L_Y
 =-y'\epsilon^{ij}\varphi_iq_{\alpha j}\bar d^\alpha
  -y''\varphi^{\dagger i}q_{\alpha i}\bar u^\alpha
  +\mathrm{h.c.},\qquad \epsilon^{12}=+1.
\tag{89.7}
$$

两个Weyl场的旋量指标沿第35节缩并；这里的$\epsilon^{ij}$只收缩弱同位旋。

还可以按量纲证明这些相互作用已经穷尽所有可能，其原因如下。四维中$[q]=[\bar u]=[\bar d]=3/2$，洛伦兹标量含偶数个旋量因子，故量纲不超过4时只能有两个费米场，最多再带一个导数或一个标量。无导数、无标量的情形已由式[（89.5）](#eq:c89-mass-obstruction)排除。一个导数必须和场及其厄米共轭构成矢量双线性，规范协变后给出式[（89.4）](#eq:c89-kinetic)。不同规范表示之间的动能混合也不允许：例如$\bar u^\dagger\bar d$虽可缩颜色，却有超荷$+1$。一个标量的情形恰由式[（89.7）](#eq:c89-yukawa)给尽。两个同色方向的场不能靠色单态Higgs消去颜色，夸克与轻子的双线性也留下颜色。两个费米场乘场强的量纲至少为5，四费米算符至少为6。因此在给定场内容及可重整性要求下，没有额外的含夸克相互作用。

<span id="c89-masses"></span>

## 质量及Higgs相互作用

进入幺正规范，把弱双重态分量称为上、下夸克：
<span id="eq:c89-unitary-yukawa"></span>

$$
\begin{gathered}
q_\alpha=\begin{pmatrix}u_\alpha\\d_\alpha\end{pmatrix},
\qquad
\varphi=\frac1{\sqrt2}\begin{pmatrix}v+H\\0\end{pmatrix},\\
\mathcal L_Y=-\frac{v+H}{\sqrt2}
 (y'd_\alpha\bar d^\alpha+y''u_\alpha\bar u^\alpha)
 +\mathrm{h.c.}
\end{gathered}
\tag{89.8}
$$

两个质量参数各由一个汤川耦合给出，彼此不受规范群的关系约束。一般$y',y''$是复数。写$y'=|y'|e^{i\eta_d}$、$y''=|y''|e^{i\eta_u}$，以$\bar d_{\rm old}=e^{-i\eta_d}\bar d$、$\bar u_{\rm old}=e^{-i\eta_u}\bar u$作恒定重定义，动能不变，汤川密度成为
<span id="eq:c89-real-mass-basis"></span>

$$
\begin{aligned}
\mathcal L_Y
 =-\frac{v+H}{\sqrt2}\big[&|y'|(d_\alpha\bar d^\alpha
                    +\bar d^\dagger_\alpha d^{\dagger\alpha})\\
                    +&|y''|(u_\alpha\bar u^\alpha
                    +\bar u^\dagger_\alpha u^{\dagger\alpha})\big].
\end{aligned}
\tag{89.9}
$$

以下在实质量基中计算，因此可以把两个实耦合分别提出包含厄米共轭的括号。

定义两种狄拉克场，并应用[两个Weyl场组成狄拉克场的恒等式](/posts/srednicki-36/#c36-two-weyl)，得到
<span id="eq:c89-dirac-masses"></span>

$$
\begin{gathered}
\mathcal D_\alpha=\begin{pmatrix}d_\alpha\\\bar d^\dagger_\alpha\end{pmatrix},
\qquad
\mathcal U_\alpha=\begin{pmatrix}u_\alpha\\\bar u^\dagger_\alpha\end{pmatrix},
\qquad
m_d=\frac{|y'|v}{\sqrt2},\quad m_u=\frac{|y''|v}{\sqrt2},\\
\mathcal L_Y
 =-m_d\left(1+\frac Hv\right)\bar{\mathcal D}^{\alpha}\mathcal D_\alpha
  -m_u\left(1+\frac Hv\right)\bar{\mathcal U}^{\alpha}\mathcal U_\alpha.
\end{gathered}
\tag{89.10}
$$

右块原来是反色场的共轭，因而重新处于色三重态，和左块相同。把两种Weyl动能合起来时，右块的一次分部积分及奇场交换正好恢复原动能，于是纯QCD部分为
<span id="eq:c89-vector-color"></span>

$$
\mathcal L_{\rm QCD,quark}
 =\sum_{\Psi=\mathcal U,\mathcal D}
 \bar\Psi\big[i\gamma^\mu(\partial_\mu-ig_3G_\mu^At^A)-m_\Psi\big]\Psi.
\tag{89.11}
$$

胶子对左右手使用同一个色生成元，故这个相互作用是矢量型的。电弱作用的手征性并未因此消失；它仍由左、右块不同的弱同位旋与超荷体现。

取实质量时还要沿用[第77节的测度变换](/posts/srednicki-77/#c77)：只转动一个Weyl分量的相位，在狄拉克语言中含轴向转动，能够把相位移到QCD拓扑项的系数中。本节接下来计算的是带电弱流中有多少独立混合参数；质量对角化并未消去强作用中可能的CP参数。

<span id="c89-currents"></span>

## 电弱规范场所耦合的夸克流

由$W^\pm,Z,A$的定义，上一节已经求出两种连接：
<span id="eq:c89-electroweak-connection"></span>

$$
\begin{aligned}
g_2(A_\mu^1T^1+A_\mu^2T^2)
 &=\frac{g_2}{\sqrt2}
 \begin{pmatrix}0&W_\mu^+\\W_\mu^-&0\end{pmatrix},\\
g_2A_\mu^3T^3+g_1B_\mu Y
 &=eQA_\mu+\frac e{s_Wc_W}(T^3-s_W^2Q)Z_\mu,
\qquad Q=T^3+Y.
\end{aligned}
\tag{89.12}
$$

这里不必重新旋转规范场，只须把新的物质生成元代入[已建立的连接分解](/posts/srednicki-88/#c88-currents)。四种左场的电荷逐项为
<span id="eq:c89-left-charges"></span>

$$
\begin{array}{c|rrrr}
&u&d&\bar u&\bar d\\\hline
T^3&+1/2&-1/2&0&0\\
Y&+1/6&+1/6&-2/3&+1/3\\
Q&+2/3&-1/3&-2/3&+1/3
\end{array}
\tag{89.13}
$$

狄拉克右块是反色左场的共轭，它的超荷也随共轭反号。因此四分量生成元应写成
<span id="eq:c89-dirac-charges"></span>

$$
\begin{aligned}
T^3_{\mathcal U}&=\tfrac12P_L,
&Y_{\mathcal U}&=\tfrac16P_L+\tfrac23P_R,
&Q_{\mathcal U}&=\tfrac23 I,\\
T^3_{\mathcal D}&=-\tfrac12P_L,
&Y_{\mathcal D}&=\tfrac16P_L-\tfrac13P_R,
&Q_{\mathcal D}&=-\tfrac13 I.
\end{aligned}
\tag{89.14}
$$

物理上、下夸克的电荷便分别为$+2e/3$、$-e/3$，其中$e>0$。代回式[（89.12）](#eq:c89-electroweak-connection)，有
<span id="eq:c89-neutral-couplings"></span>

$$
\begin{aligned}
C_{\mu,\mathcal U}^{\rm neutral}
 &=\frac23eA_\mu+
 \frac e{s_Wc_W}\left(\frac12P_L-\frac23s_W^2\right)Z_\mu,\\
C_{\mu,\mathcal D}^{\rm neutral}
 &=-\frac13eA_\mu+
 \frac e{s_Wc_W}\left(-\frac12P_L+\frac13s_W^2\right)Z_\mu.
\end{aligned}
\tag{89.15}
$$

光子耦合是矢量型，$Z$则区别左右手。动能的相互作用部分由$i(-i)=+1$给正号。把同一规范场的系数收集起来，得到
<span id="eq:c89-one-generation-currents"></span>

$$
\begin{aligned}
\mathcal L_{\rm EW,quark}
 &=\frac{g_2}{\sqrt2}(W_\mu^+J^{-\mu}+W_\mu^-J^{+\mu})
   +\frac e{s_Wc_W}Z_\mu J_Z^\mu+eA_\mu J_{\rm EM}^\mu,\\
J^{+\mu}&=\bar{\mathcal D}_{L}^{\alpha}\gamma^\mu\mathcal U_{L\alpha},
\qquad
J^{-\mu}=\bar{\mathcal U}_{L}^{\alpha}\gamma^\mu\mathcal D_{L\alpha},\\
J_3^\mu&=\frac12\bar{\mathcal U}_{L}^{\alpha}\gamma^\mu\mathcal U_{L\alpha}
        -\frac12\bar{\mathcal D}_{L}^{\alpha}\gamma^\mu\mathcal D_{L\alpha},\\
J_{\rm EM}^\mu&=\frac23\bar{\mathcal U}^{\alpha}\gamma^\mu\mathcal U_\alpha
        -\frac13\bar{\mathcal D}^{\alpha}\gamma^\mu\mathcal D_\alpha,
\qquad J_Z^\mu=J_3^\mu-s_W^2J_{\rm EM}^\mu.
\end{aligned}
\tag{89.16}
$$

各色都以相同电弱耦合进入，流中的$\alpha$必须求和。这里将规范耦合常数提到了各流之外。$J^+$与$J^-$互为厄米共轭，因而同时保留$W^-J^+$和$W^+J^-$使相互作用厄米。轻子与夸克流相加后，可直接代入上一节的低能费米相互作用。

<span id="c89-mixing"></span>

## 三代质量矩阵与CKM矩阵

现在给每个场添上代指标$I=1,2,3$。规范群在代空间中作用为单位矩阵，因此动能逐代求和；汤川耦合则允许任意两代相连：
<span id="eq:c89-three-generation-action"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}
 &=\sum_I\big[iq_I^\dagger\bar\sigma^\mu D_\mu q_I
  +i\bar u_I^\dagger\bar\sigma^\mu D_\mu\bar u_I
  +i\bar d_I^\dagger\bar\sigma^\mu D_\mu\bar d_I\big],\\
\mathcal L_Y
 &=-\epsilon^{ij}\varphi_i q_{\alpha jI}y'_{IJ}\bar d_J^\alpha
   -\varphi^{\dagger i}q_{\alpha iI}y''_{IJ}\bar u_J^\alpha
   +\mathrm{h.c.}
\end{aligned}
\tag{89.17}
$$

两个$y$矩阵各为一般复$3\times3$矩阵。内部指标在第一行暂省，第二行完整写出；代指标的相乘次序决定了随后的转置。幺正规范给
<span id="eq:c89-two-mass-matrices"></span>

$$
\mathcal L_Y=-\frac{v+H}{\sqrt2}
 \left(d_{\alpha I}y'_{IJ}\bar d_J^\alpha
       +u_{\alpha I}y''_{IJ}\bar u_J^\alpha\right)
 +\mathrm{h.c.}
\tag{89.18}
$$

这时上下型质量需要分别对角化。用下标“旧”和“m”分别指原弱基与新质量基：
<span id="eq:c89-mass-rotations"></span>

$$
\begin{aligned}
d_{\rm old}&=D d_{\rm m},&
\bar d_{\rm old}&=\bar D\bar d_{\rm m},\\
u_{\rm old}&=U u_{\rm m},&
\bar u_{\rm old}&=\bar U\bar u_{\rm m},
\qquad D,\bar D,U,\bar U\in U(3).
\end{aligned}
\tag{89.19}
$$

这里$D$和$\bar D$是两个独立的代空间矩阵，$U$与$\bar U$也一样。以第一种质量项为例，逐指标代入得
<span id="eq:c89-transposed-yukawa"></span>

$$
\begin{aligned}
d_{{\rm old},I}y'_{IJ}\bar d_{{\rm old},J}
 &=d_{{\rm m},K}\left(\sum_{I,J}D_{IK}y'_{IJ}\bar D_{JL}\right)
   \bar d_{{\rm m},L},\\
y'_m&=D^Ty'\bar D,\qquad y''_m=U^Ty''\bar U.
\end{aligned}
\tag{89.20}
$$

两个费米场没有互换次序，代空间数值矩阵可直接移过它们。两个未共轭左手场的变换使左侧矩阵以$D^T$出现。

[上一节已经构造的奇异值分解](/posts/srednicki-88/#c88-generations)可以分别用于这两个矩阵。写
<span id="eq:c89-two-svd"></span>

$$
\begin{aligned}
y'&=X_d d_dY_d^\dagger,
&D&=X_d^*,&\bar D&=Y_d,\\
y''&=X_u d_uY_u^\dagger,
&U&=X_u^*,&\bar U&=Y_u,
\end{aligned}
\tag{89.21}
$$

其中$X_{u,d},Y_{u,d}$幺正，$d_{u,d}$为实非负对角矩阵。因为$(X_d^*)^T=X_d^\dagger$，式[（89.20）](#eq:c89-transposed-yukawa)立即给$y'_m=d_d$、$y''_m=d_u$。还可用左质量平方矩阵检查共轭的位置：
<span id="eq:c89-left-mass-squares"></span>

$$
\begin{aligned}
H_d&=y'^*y'^T=X_d^*d_d^2X_d^T,
&D^\dagger H_dD&=d_d^2,\\
H_u&=y''^*y''^T=X_u^*d_u^2X_u^T,
&U^\dagger H_uU&=d_u^2.
\end{aligned}
\tag{89.22}
$$

质量和Higgs耦合带同一个$y$，所以二者同时变为代对角。此后省去质量基的“m”，便有
<span id="eq:c89-diagonal-mass-higgs"></span>

$$
\begin{gathered}
m_{dI}=\frac{v(d_d)_I}{\sqrt2},\qquad
m_{uI}=\frac{v(d_u)_I}{\sqrt2},\\
\mathcal L_Y=-\sum_I\left(1+\frac Hv\right)
 \left(m_{dI}\bar{\mathcal D}_I\mathcal D_I
      +m_{uI}\bar{\mathcal U}_I\mathcal U_I\right).
\end{gathered}
\tag{89.23}
$$

满秩的两个汤川矩阵给六个正质量，零奇异值则对应零质量。

自由动能以及中性规范耦合在换基后保持代对角。例如左下型流的代系数为$D^\dagger D$。狄拉克右块由$\bar d^\dagger$组成，旧右场则乘$\bar D^*$，因此右下型流的系数为
<span id="eq:c89-neutral-diagonality"></span>

$$
D^\dagger D=I,\qquad
\bar D^T\bar D^*=(\bar D^\dagger\bar D)^*=I;
\qquad
U^\dagger U=\bar U^T\bar U^*=I.
\tag{89.24}
$$

光子、胶子和$Z$的每个生成元都与这些代矩阵对易。因此式[（89.16）](#eq:c89-one-generation-currents)中的$J_3,J_{\rm EM}$只须逐代求和，树级没有改变味的中性流。Higgs也因式[（89.23）](#eq:c89-diagonal-mass-higgs)而保持对角。这个结论说的是当前拉格朗日量中的树级顶角；带电流在圈中出现时还会产生别的味过程。

带电流把上型和下型的左场相连，故它会同时遇到两种旋转。其代系数不再是同一矩阵与其逆，而是
<span id="eq:c89-ckm-currents"></span>

$$
\begin{aligned}
V&\equiv U^\dagger D,\qquad
V^\dagger V=D^\dagger UU^\dagger D=I,\\
J^{-\mu}&=\sum_\alpha
 \bar{\mathcal U}_{L I}^{\alpha}V_{IJ}\gamma^\mu\mathcal D_{L\alpha J},\\
J^{+\mu}&=\sum_\alpha
 \bar{\mathcal D}_{L I}^{\alpha}(V^\dagger)_{IJ}\gamma^\mu\mathcal U_{L\alpha J}.
\end{aligned}
\tag{89.25}
$$

这就是Cabibbo–Kobayashi–Maskawa矩阵，简称CKM矩阵。它给出质量本征态与弱流所连接的组合之间的关系。其中$V$的行、列指标分别连接上型和下型质量场。

若上下型的左质量平方矩阵可在同一个基中对角化，就在适当排列质量本征态后取$U=D$，使$V=I$。一般情形下，两种质量矩阵选出的左基不同，这一差别会出现在所有带电弱过程。上一节的轻子没有第二种汤川矩阵来限定中微子的基，因而可以让无质量中微子和带电轻子共用左旋转，流中只剩单位矩阵。这个区别依赖上一节采用的无质量中微子模型。

<span id="c89-parameters"></span>

## 剩下几个混合参数

一个$3\times3$幺正矩阵有九个实参数。可以在单位矩阵附近写$V=e^{iK}$，$K=K^\dagger$；$K$有三个实对角元，三个非对角复元，合计$3+2\times3=9$。不过质量对角化并没有唯一固定每个狄拉克场的相位。取非零、互不简并的夸克质量，保持实质量的余下变换可写成
<span id="eq:c89-vector-rephasings"></span>

$$
\mathcal D_{{\rm old},J}=e^{i\alpha_J}\mathcal D_J,
\qquad
\mathcal U_{{\rm old},I}=e^{i\beta_I}\mathcal U_I,
\qquad
V'_{IJ}=e^{-i\beta_I}V_{IJ}e^{i\alpha_J}.
\tag{89.26}
$$

场与其伴随相位相消，所以自由动能、质量和中性流均不变；带电流中只改写$V$的相位。若六个相位全取同一个数，它们在$V$中也完全相消。因此一般情形只能用去五个独立相位，留下九减五共四个物理参数。

具体地，在第一行与第一列各元均非零的一片参数区域，记$\phi_{IJ}=\arg V_{IJ}$。先任取$\beta_1$，再令
<span id="eq:c89-first-row-column"></span>

$$
\alpha_J=\beta_1-\phi_{1J},\qquad
\beta_I=\alpha_1+\phi_{I1}.
\tag{89.27}
$$

于是第一行和第一列都变成实数：第一行的相位为$-\beta_1+\phi_{1J}+\alpha_J=0$，第一列同样为零；交点的两种规定一致。还可把第二、第三行各乘$-1$，使第一列后两项为负。若某元为零，就无需固定它的相位，可改选其他非零元；质量简并时还允许简并子空间内的旋转，需要另作参数计数。

下面从幺正性本身求出一种方便的四参数形式。第一行、第一列都是实单位向量，故可写
<span id="eq:c89-unitary-block"></span>

$$
V=\begin{pmatrix}c_1&s_1 b^T\\-s_1 a&B\end{pmatrix},
\qquad
a=\begin{pmatrix}c_2\\s_2\end{pmatrix},
\quad b=\begin{pmatrix}c_3\\s_3\end{pmatrix},
\quad c_i=\cos\theta_i,\quad s_i=\sin\theta_i.
\tag{89.28}
$$

第一行后两项的长度是$s_1$，第一列后两项也一样；各自的方向用$\theta_3,\theta_2$表示。$B$是尚未确定的$2\times2$复矩阵。将$VV^\dagger=V^\dagger V=I$按块相乘，并先在$s_1\ne0$时除以$s_1$，得到
<span id="eq:c89-block-constraints"></span>

$$
Bb=c_1a,\qquad a^TB=c_1b^T,
\qquad BB^\dagger=I_2-s_1^2aa^T.
\tag{89.29}
$$

取垂直的两个单位向量$a_\perp=(-s_2,c_2)^T$、$b_\perp=(-s_3,c_3)^T$。第一式固定$B$沿$b$的作用；第二式又说$Bb_\perp$与$a$正交，因此只可能沿$a_\perp$。于是
<span id="eq:c89-block-reconstruction"></span>

$$
B=c_1ab^T+z\,a_\perp b_\perp^T,
\qquad
BB^\dagger=c_1^2aa^T+|z|^2a_\perp a_\perp^T.
\tag{89.30}
$$

式[（89.29）](#eq:c89-block-constraints)的右边为$c_1^2aa^T+a_\perp a_\perp^T$，所以$|z|=1$。选择相位参数$z=-e^{i\delta}$，把四个外积逐项展开，便得到
<span id="eq:c89-source-parameterization"></span>

$$
V=\begin{pmatrix}
c_1&s_1c_3&s_1s_3\\
-s_1c_2&c_1c_2c_3-s_2s_3e^{i\delta}
       &c_1c_2s_3+s_2c_3e^{i\delta}\\
-s_1s_2&c_1s_2c_3+c_2s_3e^{i\delta}
       &c_1s_2s_3-c_2c_3e^{i\delta}
\end{pmatrix}.
\tag{89.31}
$$

块计算同时证明了它的幺正性，而不必另算九个行列内积。式中三个角控制实方向，$\delta$控制剩下的复相位；$s_1=0$等边界可由连续极限取得，那里的参数未必各自可观测。对一般$n$代，同样的计数给$n^2-(2n-1)=(n-1)^2$个参数，其中实正交混合角有$n(n-1)/2$个，余下相位为$(n-1)(n-2)/2$个。两代只留一个角，三代才开始留有一个这种弱相位。

作为本参数化的一个数值例，取$s_1=0.224$、$s_2=0.041$、$s_3=0.016$、$\delta=40^\circ$。这些数沿用中译本在式[（89.31）](#eq:c89-source-parameterization)中的示例；$\theta_1$称为Cabibbo角。换用其他CKM参数化时，角的定义也随之改变。

<span id="c89-cp"></span>

## 不可去相位与CP破坏

剩下的复相位使我们需要考察时间反演。这个变换反幺正，满足$T^{-1}iT=-i$。复共轭会把$e^{i\delta}$变成$e^{-i\delta}$；但判断对称性时还须允许式[（89.26）](#eq:c89-vector-rephasings)中的场相位，否则单看某个矩阵元有虚部便可能把基的选择误作物理效应。

按[第40节的双线性变换](/posts/srednicki-40/#c40-charge)，CP把$W^+\bar{\mathcal U}_L\gamma\mathcal D_L$变为对应的$W^-\bar{\mathcal D}_L\gamma\mathcal U_L$；洛伦兹指标的宇称变换在收缩中相消，场的共同本征相位可选在$W$的相位中。原作用量里后一项的系数是$V^*$，而前一项在幺正CP变换中仍带原系数$V$。因此普通的相位选择要求$V$为实。若再允许非简并质量基中的两组味相位，条件就推广为存在对角幺正$P_u,P_d$使

$$
V^*=P_u^\dagger V P_d.
$$

这个条件也说明为何可以在适当基中检验矩阵是否为实。若它成立，令$V_{\rm r}=P_u^{-1/2}VP_d^{1/2}$，逐项取共轭便有$V_{\rm r}^*=P_u^{1/2}V^*P_d^{-1/2}=V_{\rm r}$。由此可选一个不必显式寻找这些相位的检验量：
<span id="eq:c89-rephasing-invariant"></span>

$$
J=\operatorname{Im}(V_{11}V_{22}V_{12}^*V_{21}^*).
\tag{89.32}
$$

重相位后四个因子的相位依次为$-\beta_1+\alpha_1$、$-\beta_2+\alpha_2$、$+\beta_1-\alpha_2$、$+\beta_2-\alpha_1$，总和为零；所以$J$不依赖这些相位选择。与CP共轭过程比较时，CKM系数被复共轭，因而$J\to-J$。因此$J\ne0$便排除了这种CP对称性。

对式[（89.31）](#eq:c89-source-parameterization)，这一个四元积已经足以看出不可去相位：
<span id="eq:c89-jarlskog-value"></span>

$$
\begin{aligned}
V_{11}V_{22}V_{12}^*V_{21}^*
 &=-c_1s_1^2c_2c_3
    (c_1c_2c_3-s_2s_3e^{i\delta}),\\
J&=c_1s_1^2c_2s_2c_3s_3\sin\delta.
\end{aligned}
\tag{89.33}
$$

对一般非零混合角，$\delta$不等于$0$或$\pi$时这一量便非零。反过来，一个实混合矩阵即使经行、列重相位变成复矩阵，它的$J$仍为零，物理内容仍然守恒CP。角退化或质量简并时，可用的场变换增多，应在去掉这些自由度后检验CP。

带电弱相互作用因而能够破坏时间反演及CP。这里使用的联系是[第40节的CPT结果](/posts/srednicki-40/#c40)：在局域、洛伦兹协变、厄米并满足该章谱条件的量子场论中，CPT仍为对称性；CP与T的破坏相互对应。$\delta$也因此称为CP破坏相位。具体衰变中的可测不对称还要计算相应过程的振幅和干涉项，本节得到的是相互作用中允许这种效应的参数。

<span id="c89-anomalies"></span>

## 一代场如何消去规范反常

由[第75节的三角图](/posts/srednicki-75/#c75-groups)，反常的群系数为各左Weyl表示的完全对称三次迹之和。圈积分的系数已知，下面计算每种规范生成元的群迹。先列出一代场及旁观重数：

| 左Weyl场 | 色表示                | 弱表示     | 超荷$Y$ | Weyl分量重数 |
| -------- | --------------------- | ---------- | ------: | -----------: |
| $q$      | $\mathbf3$            | $\mathbf2$ |   $1/6$ |            6 |
| $\bar u$ | $\overline{\mathbf3}$ | $\mathbf1$ |  $-2/3$ |            3 |
| $\bar d$ | $\overline{\mathbf3}$ | $\mathbf1$ |   $1/3$ |            3 |
| $\ell$   | $\mathbf1$            | $\mathbf2$ |  $-1/2$ |            2 |
| $\bar e$ | $\mathbf1$            | $\mathbf1$ |     $1$ |            1 |

最后一列用于$Y^3$迹。非阿贝尔表示的维数已计入相应矩阵迹，其外再乘其余群的重数。全部场已经是左手，反色场的贡献由其生成元确定。

先看$3$–$3$–$3$反常。以基本表示的对称三次迹为单位，第75节已从$\bar t^A=-(t^A)^T$得到$A(\bar3)=-A(3)$。$q$中有两个色三重态，$\bar u,\bar d$各有一个反三重态，故
<span id="eq:x89-color-anomaly"></span>

$$
\mathcal A_{333}=2A(\mathbf3)+A(\overline{\mathbf3})
 +A(\overline{\mathbf3})=2-1-1=0.
\tag{89.35}
$$

弱群的局域$2$–$2$–$2$反常逐个双重态就为零。因为$T^a=\sigma^a/2$满足
<span id="eq:x89-weak-local-anomaly"></span>

$$
\frac12\operatorname{Tr}\big(\{T^a,T^b\}T^c\big)
 =\frac14\delta^{ab}\operatorname{Tr}T^c=0.
\tag{89.36}
$$

弱单态也不贡献。

混合$3$–$3$–$1$的生成元在直积空间中可分开取迹。它给$Y\operatorname{Tr}_3(t^At^B)$，再乘弱表示维数。反基本的二次迹仍为正的$\delta^{AB}/2$，因为两个生成元的负号相消。因此除去共同的$\delta^{AB}$，有
<span id="eq:x89-color-hypercharge"></span>

$$
\mathcal A_{331}
 =\frac12\left[2\left(\frac16\right)-\frac23+\frac13\right]=0.
\tag{89.37}
$$

同理，$2$–$2$–$1$只接触$q$与$\ell$。此时旁观重数是颜色，得到
<span id="eq:x89-weak-hypercharge"></span>

$$
\mathcal A_{221}
 =\frac12\left[3\left(\frac16\right)-\frac12\right]=0.
\tag{89.38}
$$

前一项来自三个颜色的夸克双重态，后一项来自轻子双重态。

三个$U(1)$外场的群因子是每个Weyl分量的$Y^3$之和，故
<span id="eq:x89-hypercharge-cubic"></span>

$$
\begin{aligned}
\mathcal A_{111}
 &=6\left(\frac16\right)^3
  +3\left(-\frac23\right)^3
  +3\left(\frac13\right)^3
  +2\left(-\frac12\right)^3+1\\
 &=\frac1{36}-\frac89+\frac19-\frac14+1=0.
\end{aligned}
\tag{89.39}
$$

这与上一节分别得到的夸克$-3/4$、轻子$+3/4$相合。

其余规范群组合也可以直接列出。三个外腿所属群的无序组合一共十种；除刚才的五种以外，余下的是$332,322,321,311,211$。每一种至少含一个只出现一次的非阿贝尔生成元。比如$332$的迹分解为$\operatorname{Tr}_3(t^At^B)\operatorname{Tr}_2T^a$，$311$给$Y^2\operatorname{Tr}_3t^A$，$321$给$Y\operatorname{Tr}_3t^A\operatorname{Tr}_2T^a$；均由单个生成元无迹而消失。$322$、$211$同样分别含$\operatorname{Tr}_3t^A$或$\operatorname{Tr}_2T^a$。这就列完了三个规范外腿的全部组合。

若把规范场与引力同时考虑，还应使用第75节的超荷迹条件。一代给
<span id="eq:x89-mixed-gravity"></span>

$$
\begin{aligned}
\mathcal A_{{\rm grav}^2Y}
 &=6\left(\frac16\right)+3\left(-\frac23\right)
  +3\left(\frac13\right)+2\left(-\frac12\right)+1\\
 &=1-2+1-1+1=0.
\end{aligned}
\tag{89.40}
$$

非阿贝尔混合引力迹同样因生成元无迹而消失。普通四维自旋时空上还存在[第75节的整体$SU(2)$条件](/posts/srednicki-75/#c75-global)：基本双重态的数目必须为偶数。每代有三个颜色的夸克双重态与一个轻子双重态，共四个；三代共有十二个，满足条件。

相消逐代成立，三代相加仍为零。Higgs标量不贡献手征费米三角反常。结合第75节的微扰规范反常条件以及这里的整体$SU(2)$计数，所构造的标准模型满足这些量子规范一致性条件。全局重子数、轻子数的流则由各自的生成元另行计算。

<span id="c89-beta-functions"></span>

## 三个规范耦合的一圈演化

同一张场表也足以求出三个规范耦合的一圈贝塔函数。[第73节的物质圈计算](/posts/srednicki-73/#c73-general-matter)给每个狄拉克场权重$4/3$、每个复标量权重$1/3$。一个左手 Weyl 场在宇称偶的规范二点函数中贡献狄拉克场的一半，因此对三个群因子分别有
<span id="eq:c89-general-beta"></span>

$$
\beta_{g_i}:=\mu\frac{dg_i}{d\mu}
 =-\frac{g_i^3}{16\pi^2}
 \left[\frac{11}{3}C_{A_i}
       -\frac23\sum_{\text{Weyl}}T_i(R)
       -\frac13\sum_{\text{复标量}}T_i(R)\right]
 +\text{更高圈}.
\tag{89.41}
$$

这里$T_i(R)$包含其余群的表示维数。对超荷群，$C_{A_1}=0$，相应的迹是每个分量的$Y^2$之和。一代的三个费米迹分别为
<span id="eq:c89-matter-indices"></span>

$$
\begin{aligned}
\sum_{\text{一代}}T_1
 &=6\left(\frac16\right)^2+3\left(-\frac23\right)^2
 +3\left(\frac13\right)^2+2\left(-\frac12\right)^2+1
 =\frac{10}{3},\\
\sum_{\text{一代}}T_2&=3\cdot\frac12+\frac12=2,\\
\sum_{\text{一代}}T_3&=2\cdot\frac12+\frac12+\frac12=2.
\end{aligned}
\tag{89.42}
$$

将费米部分乘三代，得到$(10,6,6)$。一个 Higgs 复双重态给$(T_1,T_2,T_3)=(1/2,1/2,0)$，伴随 Casimir 则为$(0,2,3)$。逐项代入：
<span id="eq:c89-standard-model-betas"></span>

$$
\begin{aligned}
\beta_{g_1}
 &=\frac{g_1^3}{16\pi^2}
       \left(\frac23\cdot10+\frac13\cdot\frac12\right)
 =\frac{41}{6}\frac{g_1^3}{16\pi^2}+\text{更高圈},\\
\beta_{g_2}
 &=-\frac{g_2^3}{16\pi^2}
       \left(\frac{22}{3}-4-\frac16\right)
 =-\frac{19}{6}\frac{g_2^3}{16\pi^2}+\text{更高圈},\\
\beta_{g_3}
 &=-\frac{g_3^3}{16\pi^2}(11-4)
 =-7\frac{g_3^3}{16\pi^2}+\text{更高圈}.
\end{aligned}
\tag{89.43}
$$

$g_1$仍是直接乘超荷$Y$的耦合。[第84节](/posts/srednicki-84/#eq:c84-su5-traces)给$\operatorname{Tr}Y^2=5/6$，因此$T_1=\sqrt{3/5}Y$才具有$\operatorname{Tr}T_1^2=1/2$的归一。保持连接$g_1Y$不变，就得到大统一归一$g_{1,\mathrm{GUT}}=\sqrt{5/3}\,g_1$，链式法则使第一条的系数变成$(3/5)(41/6)=41/10$。上面三条属于包含完整标准模型场内容的质量无关重整化方案，例如$\overline{\mathrm{MS}}$；在低于某些粒子质量的有效理论中，要在质量阈值处匹配，并按留下的场重新计算各个迹。

<span id="c89-hadrons"></span>

## 从高能夸克过程到低能强子流

在$M_W,M_Z$量级，QCD耦合已经较小。例如沿用中译本的$\alpha_3(M_Z)=g_3^2(M_Z)/(4\pi)=0.12$，便可用微扰论计算$W$、$Z$的夸克衰变，并把QCD圈修正的量级估为百分之几。这里所指的是短距离振幅以及与之相联系的包容强子衰变率：硬过程产生夸克后，它们仍要形成强子。小耦合使硬尺度的圈展开可控，而具体的修正系数还须由相应实、虚图求出；它们由具体过程决定。

能量降到强相互作用尺度附近时，不能再把孤立夸克当作可观测外态。弱耦合仍然很小，但弱流的强子矩阵元需要另行求取。下一节将把这里的夸克流接到第83节建立的低能强子理论。作为起点，先只保留最轻的$u,d$质量本征态。按本节的参数化$V_{ud}=c_1$为实，两个带电流便成为
<span id="eq:c89-light-quark-currents"></span>

$$
J^{+\mu}_{ud}=c_1\bar{\mathcal D}_{L}^{\alpha}\gamma^\mu\mathcal U_{L\alpha},
\qquad
J^{-\mu}_{ud}=c_1\bar{\mathcal U}_{L}^{\alpha}\gamma^\mu\mathcal D_{L\alpha}.
\tag{89.34}
$$

以中子衰变为例，要计算的是$\langle p|J^{-\mu}_{ud}|n\rangle$，再把它与轻子流收缩。单个夸克顶角中的$c_1$保留下来；其余结构由核子态和强作用决定。这也说明低能弱衰变为何同时提供夸克混合与强子内部结构的信息。

---

[← 第 88 节](/posts/srednicki-88/) · [章节地图](/srednicki/) · [第 90 节 →](/posts/srednicki-90/)
