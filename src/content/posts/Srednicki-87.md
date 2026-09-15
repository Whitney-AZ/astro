---
title: 'Srednicki §87 标准模型：规范与 Higgs 扇区'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [87]
hideFromHome: true
draft: false
---

<span id="c87"></span>

现在把前面建立的规范理论用于标准模型（Standard Model）。它的规范群和物质表示先作为模型的输入给定，再由规范不变性限制相互作用。本节从电弱规范场与Higgs场开始：Higgs真空决定哪些矢量场获得质量，剩下的无质量组合则与电磁作用相联系。随后将所有规范动能改写到这个质量基中，就能得到适于树级计算的拉格朗日量。

<span id="c87-model"></span>

## 模型的场内容和Higgs真空

标准模型取规范群$SU(3)\times SU(2)\times U(1)$。一代左手Weyl场处于表示
<span id="eq:c87-matter-input"></span>

$$
\begin{aligned}
R_{\mathrm{one}}
={}&(1,2,-\tfrac12)\oplus(1,1,+1)
 \oplus(3,2,+\tfrac16)\\
&\oplus(\bar3,1,-\tfrac23)\oplus(\bar3,1,+\tfrac13),
\end{aligned}
\tag{87.1}
$$

这样的物质场有三代，另有一个$(1,2,-1/2)$复标量。每个三元组的前两个位置指定色群和弱群的表示，最后一个位置是$U(1)$生成元的本征值，称为超荷（hypercharge）。两个$\bar3$是色反三重态，须与色基本三重态区分。物质内容、三代重复和超荷的选择共同定义了所讨论的模型，随后各章再说明它们怎样描述轻子与夸克。

拉格朗日量包含与这些场相容、满足Lorentz和规范不变性且质量量纲不超过4的项。这限定了四维可重整化模型的范围。其电弱部分也称为Glashow–Weinberg–Salam模型；以下从$SU(2)\times U(1)$规范场和Higgs双重态$\varphi$开始。

Higgs场对色群为单态。它的电弱生成元和协变导数为
<span id="eq:c87-doublet-connection"></span>

$$
\begin{aligned}
T^a&=\frac{\sigma^a}{2},\qquad Y=-\frac12I_2,\\
D_\mu\varphi&=(\partial_\mu-iC_\mu)\varphi,\qquad
C_\mu=g_2A_\mu^aT^a+g_1B_\mu Y .
\end{aligned}
\tag{87.2}
$$

$A_\mu^a$是三个弱规范场，$B_\mu$是超荷规范场；$g_2$与$g_1$是两个独立的正耦合。将三个Pauli矩阵逐个代入，得到显式连接矩阵
<span id="eq:c87-connection-matrix"></span>

$$
C_\mu=\frac12
\begin{pmatrix}
g_2A_\mu^3-g_1B_\mu&g_2(A_\mu^1-iA_\mu^2)\\
g_2(A_\mu^1+iA_\mu^2)&-g_2A_\mu^3-g_1B_\mu
\end{pmatrix}.
\tag{87.3}
$$

这里$g_1$直接乘超荷$Y$，其归一与第84节讨论GUT匹配时另行归一的生成元不同。

取势
<span id="eq:c87-higgs-potential"></span>

$$
V(\varphi)=\frac{\lambda}{4}
 \left(\varphi^\dagger\varphi-\frac{v^2}{2}\right)^2,
\qquad \lambda>0,\quad v>0 .
\tag{87.4}
$$

它在$\varphi^\dagger\varphi=v^2/2$处达到最低值。所有这样的双重态都可以旋转到上分量。事实上，若$\varphi_0=vn/\sqrt2$，$n=(a,b)^T$、$|a|^2+|b|^2=1$，则
<span id="eq:c87-vacuum-alignment"></span>

$$
\begin{aligned}
U_n&=\begin{pmatrix}a^*&b^*\\-b&a\end{pmatrix},
&U_nn&=\begin{pmatrix}1\\0\end{pmatrix},\\
U_n^\dagger U_n&=I,&\det U_n&=1 .
\end{aligned}
\tag{87.5}
$$

两个行向量的内积为零，范数均为1，乘上$n$又使第二分量为$-ba+ab=0$，所以这个$SU(2)$矩阵已经完成所需的旋转。选取这个规范代表，真空值便是
$\langle0|\varphi(x)|0\rangle=v(1,0)^T/\sqrt2$。以下先以这个经典真空值求树级质量。

<span id="c87-masses"></span>

## 从质量矩阵找出W、Z和光子

令$u=(1,0)^T$。真空是常数，因而$D_\mu\varphi_0=-ivC_\mu u/\sqrt2$。标准复场动能$-(D_\mu\varphi)^\dagger D^\mu\varphi$给
<span id="eq:c87-mass-quadratic-form"></span>

$$
\begin{aligned}
C_\mu u&=\frac12
 \begin{pmatrix}
 g_2A_\mu^3-g_1B_\mu\\
 g_2(A_\mu^1+iA_\mu^2)
 \end{pmatrix},\\
\mathcal L_{\mathrm{mass}}
 &=-\frac{v^2}{2}u^\dagger C^\mu C_\mu u\\
 &=-\frac{v^2}{8}
 \left[g_2^2(A^1\cdot A^1+A^2\cdot A^2)
 +(g_2A^3-g_1B)^2\right].
\end{aligned}
\tag{87.6}
$$

下分量与其复共轭相乘时，$A^1\cdot A^2$的两个交叉项相消。其中$C^\mu C_\mu$同时包含连接的矩阵乘法和Lorentz收缩。

将四个实规范场依次排为$(A^1,A^2,A^3,B)$，按$-\tfrac12A^AM^2_{AB}A^B$读取质量平方矩阵，得到
<span id="eq:c87-real-vector-mass-matrix"></span>

$$
M^2=\frac{v^2}{4}
\begin{pmatrix}
g_2^2&0&0&0\\
0&g_2^2&0&0\\
0&0&g_2^2&-g_1g_2\\
0&0&-g_1g_2&g_1^2
\end{pmatrix}.
\tag{87.7}
$$

前两个场已经对角，而且质量相同。提出共同因子$v^2/4$后，中性两场的矩阵是$(g_2,-g_1)^T$与其转置的外积：它作用于$(g_2,-g_1)^T$给$g_1^2+g_2^2$倍原向量，作用于$(g_1,g_2)^T$则为零。因此定义弱混合角（weak mixing angle）
<span id="eq:c87-neutral-rotation"></span>

$$
\begin{aligned}
\tan\theta_W&=\frac{g_1}{g_2},\qquad
s_W=\frac{g_1}{\sqrt{g_1^2+g_2^2}},\quad
c_W=\frac{g_2}{\sqrt{g_1^2+g_2^2}},\\
Z_\mu&=c_WA_\mu^3-s_WB_\mu,\qquad
A_\mu=s_WA_\mu^3+c_WB_\mu,\\
A_\mu^3&=c_WZ_\mu+s_WA_\mu,\qquad
B_\mu=-s_WZ_\mu+c_WA_\mu .
\end{aligned}
\tag{87.8}
$$

这给出了中性场的旋转及其逆变换。$Z$沿着正质量方向，$A$沿着零方向。旋转矩阵正交，所以两个场的标准动能归一也保持不变。

对于简并的$A^1,A^2$，取复组合
<span id="eq:c87-charged-fields"></span>

$$
\begin{aligned}
W_\mu^\pm&=\frac{A_\mu^1\mp iA_\mu^2}{\sqrt2},\\
A_\mu^1&=\frac{W_\mu^++W_\mu^-}{\sqrt2},\qquad
A_\mu^2=\frac{i(W_\mu^+-W_\mu^-)}{\sqrt2},\\
A^1\cdot A^1+A^2\cdot A^2&=2W^+\cdot W^- .
\end{aligned}
\tag{87.9}
$$

由于旧场实，$W^-=(W^+)^\dagger$，它们合起来仍是两个实场的自由度。代入质量二次型，得到
<span id="eq:c87-vector-masses"></span>

$$
\begin{aligned}
\mathcal L_{\mathrm{mass}}
 &=-M_W^2W_\mu^+W^{-\mu}
   -\frac12M_Z^2Z_\mu Z^\mu,\\
M_W&=\frac{g_2v}{2},\qquad
M_Z=\frac{v}{2}\sqrt{g_1^2+g_2^2}
 =\frac{M_W}{c_W},\qquad M_A=0 .
\end{aligned}
\tag{87.10}
$$

复$W$质量项前没有额外的$1/2$，因为两个实场已经合在其中；实$Z$仍保留$1/2$。这些质量项都含两份连接，是式[（87.6）](#eq:c87-mass-quadratic-form)在新基底中的同一个二次型。

例如取中译本的近似质量输入$M_W=80.4$ GeV、$M_Z=91.2$ GeV，便得$c_W=67/76\simeq0.882$和$s_W^2\simeq0.223$。这个角的定义取决于重整化方案：树级时耦合比和质量比确定同一个角，圈阶时则必须说明采用哪个定义。例如
<span id="eq:c87-angle-schemes"></span>

$$
c_{W,\mathrm{OS}}=\frac{M_W^{\mathrm{phys}}}{M_Z^{\mathrm{phys}}},
\qquad
\tan\theta_{W,\overline{\mathrm{MS}}}(\mu)
 =\frac{g_{1,\overline{\mathrm{MS}}}(\mu)}
 {g_{2,\overline{\mathrm{MS}}}(\mu)} .
\tag{87.11}
$$

中译本另取$s_W^2=0.231$作为$\overline{\mathrm{MS}}$角在$\mu=M_Z$的示例输入。它与质量比角的数值差来自圈修正。若$g_1,g_2$另由指定的重整化条件定义，它们与在壳角的树关系会有圈修正；也可以反过来以电荷和在壳角定义相应耦合，此时被选作定义的关系按定义成立。下面的拉格朗日量先使用共同的树级关系。

<span id="c87-parameters"></span>

## 电弱参数和费米常数

中译本习题87.2取$\alpha(M_Z)=1/127.9$、$s_W^2=0.231$。同时取$M_W=80.4$ GeV，先用电磁耦合确定$e$，再由混合角分开两个规范耦合，最后用矢量质量确定真空值。

依次代入
<span id="eq:x87-parameter-substitution"></span>

$$
\begin{aligned}
e&=\sqrt{4\pi\alpha}
 =\sqrt{\frac{4\pi}{127.9}},\\
g_2&=\frac{e}{s_W}
 =\frac{e}{\sqrt{0.231}},\qquad
g_1=\frac{e}{c_W}
 =\frac{e}{\sqrt{1-0.231}},\\
v&=\frac{2M_W}{g_2}.
\end{aligned}
\tag{87.35}
$$

计算得到$e=0.313451$、$g_1=0.357443$、$g_2=0.652174$和$v=246.560$ GeV。前三个量无量纲，最后一个与$M_W$同量纲。由这组参数算出的树级质量为$M_W/c_W=91.684$ GeV。中译本另给的$M_Z=91.2$ GeV来自质量输入；这里按题意把运行角用于树级估计。

在树级定义费米常数。将$e/s_W=g_2$代入，再使用$M_W=g_2v/2$，得到
<span id="eq:x87-fermi-constant"></span>

$$
\begin{aligned}
G_F&:=\frac{e^2}{4\sqrt2\,s_W^2M_W^2}
 =\frac{g_2^2}{4\sqrt2\,M_W^2}\\
 &=\frac{g_2^2}{4\sqrt2\,(g_2^2v^2/4)}
 =\frac1{\sqrt2\,v^2}
 =1.16316\times10^{-5}\ {\rm GeV}^{-2}.
\end{aligned}
\tag{87.36}
$$

所以$G_F$的质量量纲为$-2$，由对称性破缺尺度的平方倒数决定。第88节将积分掉低能过程中的重$W$内线，得到以$G_F$为系数的四费米作用。

<span id="c87-charge"></span>

## 未破缺生成元和电荷归一

无质量中性场意味着真空保留一个连续规范方向。它的生成元由保持真空的条件求出。设
$Q=q_aT^a+q_YY$，厄米性要求$q_a,q_Y$为实数。保持真空不动的条件给
<span id="eq:c87-unbroken-generator"></span>

$$
Qu=\frac12
\begin{pmatrix}q_3-q_Y\\q_1+iq_2\end{pmatrix}=0
\quad\Longrightarrow\quad
q_1=q_2=0,\qquad q_3=q_Y .
\tag{87.12}
$$

因此只剩$T^3+Y$这一个方向。以质子电荷作为单位固定整体比例，就取$Q=T^3+Y$。在本Higgs双重态上，$Q=\operatorname{diag}(0,-1)$；所选上分量真空的电荷确实为零。

这个生成元也直接出现在无质量场的连接中。对于任意给定的电弱表示，将式[（87.8）](#eq:c87-neutral-rotation)代入原连接，有
<span id="eq:c87-neutral-couplings"></span>

$$
\begin{aligned}
g_2A_\mu^3T^3+g_1B_\mu Y
={}&A_\mu(g_2s_WT^3+g_1c_WY)\\
 &+Z_\mu(g_2c_WT^3-g_1s_WY)\\
={}&eA_\mu Q+\frac{g_2}{c_W}
 Z_\mu(T^3-s_W^2Q),\\
e&=g_2s_W=g_1c_W>0 .
\end{aligned}
\tag{87.13}
$$

第二个等号中的$Z$系数可这样整理：将$Y=Q-T^3$代入，$T^3$的系数为$g_2c_W+g_1s_W=g_2/c_W$，$Q$的系数为$-g_1s_W=-(g_2/c_W)s_W^2$。因而同一个光子$A_\mu$确实以共同耦合$e$乘各场的电荷$Q$。

从这里开始使用正的$e$。前面QED各章将电子本身的电荷记成负的$e_{\mathrm{QED}}$；两者满足$e=-e_{\mathrm{QED}}$，电子在现在的记法中取$Q=-1$。这使$W^+$、$W^-$的电荷可以由$Q$的符号直接标明，下面从规范场强还会得到相同的耦合。

<span id="c87-higgs"></span>

## 幺正规范中剩下的Higgs场

质量矩阵有三个正本征值，因而四个实标量中的三个轨道方向与$W^\pm,Z$的第三个偏振相配，留下一个径向标量。对真空附近$v+H>0$的局部片，使用幺正规范写
<span id="eq:c87-unitary-higgs"></span>

$$
\varphi(x)=\frac1{\sqrt2}
\begin{pmatrix}v+H(x)\\0\end{pmatrix},\qquad H=H^\dagger .
\tag{87.14}
$$

四个实标量加四个无质量规范场原有$4+4\times2=12$个物理自由度；现在三个有质量矢量给9个、光子给2个、$H$给1个，总数仍是12。幺正规范让这组物理粒子在树级作用量中直接出现。

径向场进入势的方式与第85节相同，但现在它属于电弱双重态。先算
$\varphi^\dagger\varphi-v^2/2=vH+H^2/2$，再平方，得到
<span id="eq:c87-higgs-self-couplings"></span>

$$
\begin{aligned}
V(H)&=\frac{\lambda v^2}{4}H^2
 +\frac{\lambda v}{4}H^3+\frac{\lambda}{16}H^4,\\
m_H^2&=\frac{\lambda v^2}{2},\qquad
\lambda=\frac{2m_H^2}{v^2}.
\end{aligned}
\tag{87.15}
$$

实标量质量项按$-\tfrac12m_H^2H^2$读取，势中$\lambda/4$的归一由此进入质量公式。质量公式来自势在径向上的曲率；数值大小仍由模型参数$\lambda,v$决定。

令$r=v+H$。协变导数为$(u\,\partial_\mu H-irC_\mu u)/\sqrt2$。在动能的共轭乘积中，两项交叉贡献分别正比于$+ir\,u^\dagger C_\mu u\,\partial^\mu H$和它的负值，因为$C_\mu$厄米而相消。因此
<span id="eq:c87-higgs-vector-couplings"></span>

$$
\begin{aligned}
-(D_\mu\varphi)^\dagger D^\mu\varphi
 &=-\frac12(\partial H)^2-\frac{(v+H)^2}{2}
 u^\dagger C^\mu C_\mu u\\
 &=-\frac12(\partial H)^2
 -\left(M_W^2W^+\cdot W^-+\frac12M_Z^2Z^2\right)
 \left(1+\frac Hv\right)^2 .
\end{aligned}
\tag{87.16}
$$

于是$H$已经标准归一，质量项中的$v^2$也确实整体变成$(v+H)^2$。同一个式子固定了$HWW,HZZ$及两个Higgs插入的耦合；规范粒子的质量越大，它与径向场的耦合也越强。

<span id="c87-real-mass-basis"></span>

## 实标量、戈德斯通方向和质量基

将第86节的一般构造应用于这个双重态。固定实分量的次序为
<span id="eq:x87-real-field-order"></span>

$$
\varphi=\frac1{\sqrt2}
\begin{pmatrix}\phi_1+i\phi_3\\\phi_2+i\phi_4\end{pmatrix},
\qquad
\phi=(\phi_1,\phi_2,\phi_3,\phi_4)^T,\qquad
\phi_0=(v,0,0,0)^T.
\tag{87.37}
$$

前两个分量是全部实部，后两个是全部虚部，这与[实表示的构造](/posts/srednicki-86/#c86-realification)的排列相同。

若复厄米生成元分解为$T_R=A+iB$，则由$\delta\varphi=-i\alpha T_R\varphi$分别取实、虚部，有
$\delta x=\alpha(Bx+Ay)$、$\delta y=\alpha(-Ax+By)$。因此作用在$\phi$上的厄米生成元为
$\mathsf T=i\left(\begin{smallmatrix}B&A\\-A&B\end{smallmatrix}\right)$。在$T^1,T^3,Y$中，$B=0$，只需将实矩阵放入两个非对角块；$T^2$则只有虚部$B=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)/2$，放入两个对角块。四个结果是
<span id="eq:x87-real-generators"></span>

$$
\begin{aligned}
\mathsf T^1&=\frac i2
\begin{pmatrix}
0&0&0&1\\
0&0&1&0\\
0&-1&0&0\\
-1&0&0&0
\end{pmatrix},&
\mathsf T^2&=\frac i2
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},\\
\mathsf T^3&=\frac i2
\begin{pmatrix}
0&0&1&0\\
0&0&0&-1\\
-1&0&0&0\\
0&1&0&0
\end{pmatrix},&
\mathsf Y&=\frac i2
\begin{pmatrix}
0&0&-1&0\\
0&0&0&-1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}.
\end{aligned}
\tag{87.38}
$$

每个矩阵都纯虚且反对称，故仍为厄米矩阵；相应的有限变换$e^{-i\alpha\mathsf T}$却是实正交的。第86节已经证明这个实化映射保持乘法与对易关系，因此它们满足$[\mathsf T^a,\mathsf T^b]=i\epsilon^{abc}\mathsf T^c$及$[\mathsf T^a,\mathsf Y]=0$。

用第86节的定义$\tau^a=ig_a\mathsf T^a$、$F_{ai}=(\tau^a\phi_0)_i$，前三行的耦合是$g_2$，超荷一行的耦合是$g_1$。因为背景只有第一分量非零，只须取上面四个矩阵的第一列，再乘$ig_av$。例如$\mathsf T^2$的第一列是$(0,i/2,0,0)^T$，给$F_{2i}=(0,-g_2v/2,0,0)$；超荷的第一列是$(0,0,i/2,0)^T$，给$F_{Yi}=(0,0,-g_1v/2,0)$。全部四行组成
<span id="eq:x87-vacuum-orbit-matrix"></span>

$$
F=\frac v2
\begin{pmatrix}
0&0&0&g_2\\
0&-g_2&0&0\\
0&0&g_2&0\\
0&0&-g_1&0
\end{pmatrix}.
\tag{87.39}
$$

三个非零列互相独立，故$F$的秩为3。它的第一列为零，正对应未被规范轨道占据的径向Higgs方向。

按行作内积，$FF^T$就得到式[（87.7）](#eq:c87-real-vector-mass-matrix)。它的中性二阶块行列式为零，迹为$(g_1^2+g_2^2)v^2/4$；完整本征值为$M_W^2,M_W^2,M_Z^2,0$。

这个$F$还直接给出标量方向。按下面的顺序取新场：
<span id="eq:c87-explicit-svd"></span>

$$
\begin{aligned}
\widetilde A_\mu&=(A_\mu^1,A_\mu^2,Z_\mu,A_\mu)^T=S^TA_{\mathrm{old},\mu},\\
\chi&=(\phi_1-v,\phi_2,\phi_3,\phi_4)^T,\\
\widetilde\chi&=(\phi_4,-\phi_2,\phi_3,\phi_1-v)^T=R\chi,\\
S^TFR^T&=\operatorname{diag}(M_W,M_W,M_Z,0),\\
RH_\xi R^T&=\operatorname{diag}(\xi M_W^2,\xi M_W^2,
 \xi M_Z^2,m_H^2).
\end{aligned}
\tag{87.40}
$$

前三个标量沿真空的规范轨道，最后一个是径向方向。第二个标量分量的负号使第二个奇异值为正；中性规范旋转则把第三、第四行合成$M_Z$和零。于是$R_\xi$规范中的三个戈德斯通质量、三个有质量鬼场的质量及非物理矢量极点，都由已经求出的$M_W,M_Z$决定。幺正规范将前三个标量置零，回到式[（87.14）](#eq:c87-unitary-higgs)的一个径向场。

<span id="c87-curvatures"></span>

## 把规范曲率写成带电和中性场

标量部分已经齐备，现在处理规范动能
<span id="eq:c87-gauge-kinetic-input"></span>

$$
\mathcal L_{\mathrm{gauge}}
 =-\frac14F_{\mu\nu}^aF^{a\mu\nu}
  -\frac14B_{\mu\nu}B^{\mu\nu}.
\tag{87.17}
$$

弱群的结构常数是$\epsilon^{abc}$。对固定的$a$，其余两个不同指标各有一个排列，符号相反，所以三个分量分别为
<span id="eq:c87-component-curvatures"></span>

$$
\begin{aligned}
F_{\mu\nu}^1
 &=\partial_\mu A_\nu^1-\partial_\nu A_\mu^1
   +g_2(A_\mu^2A_\nu^3-A_\nu^2A_\mu^3),\\
F_{\mu\nu}^2
 &=\partial_\mu A_\nu^2-\partial_\nu A_\mu^2
   +g_2(A_\mu^3A_\nu^1-A_\nu^3A_\mu^1),\\
F_{\mu\nu}^3
 &=\partial_\mu A_\nu^3-\partial_\nu A_\mu^3
   +g_2(A_\mu^1A_\nu^2-A_\nu^1A_\mu^2),\\
B_{\mu\nu}&=\partial_\mu B_\nu-\partial_\nu B_\mu .
\end{aligned}
\tag{87.18}
$$

超荷群阿贝尔，最后一行没有二次连接项。

先组成$F^1-iF^2$。它的导数部分为$\sqrt2(\partial_\mu W_\nu^+-\partial_\nu W_\mu^+)$，二次部分则可按$A^3$的位置合并成
<span id="eq:c87-charged-curvature-combination"></span>

$$
\begin{aligned}
&g_2\left[
 A_\mu^2A_\nu^3-A_\nu^2A_\mu^3
 -iA_\mu^3A_\nu^1+iA_\nu^3A_\mu^1\right]\\
&\qquad=-ig_2\left[
 A_\mu^3(A_\nu^1-iA_\nu^2)
 -A_\nu^3(A_\mu^1-iA_\mu^2)\right]\\
&\qquad=-i\sqrt2g_2
 (A_\mu^3W_\nu^+-A_\nu^3W_\mu^+).
\end{aligned}
\tag{87.19}
$$

第二行中的$(-i)(-i)=-1$给$-A_\mu^3A_\nu^2$，正好与第一行的相应项相同。于是定义
<span id="eq:c87-charged-curvatures"></span>

$$
\begin{aligned}
C_\mu^{\mathrm n}
 &=g_2A_\mu^3=e(A_\mu+\cot\theta_WZ_\mu),\\
D_\mu&=\partial_\mu-iC_\mu^{\mathrm n},\qquad
D_\mu^*=\partial_\mu+iC_\mu^{\mathrm n},\\
W_{\mu\nu}^+
 &:=\frac{F_{\mu\nu}^1-iF_{\mu\nu}^2}{\sqrt2}
 =D_\mu W_\nu^+-D_\nu W_\mu^+,\\
W_{\mu\nu}^-
 &:=\frac{F_{\mu\nu}^1+iF_{\mu\nu}^2}{\sqrt2}
 =D_\mu^*W_\nu^--D_\nu^*W_\mu^- .
\end{aligned}
\tag{87.20}
$$

最后一行也可以由前一行取复共轭得到。这里的星号表示取电荷共轭，导数仍为$+\partial_\mu$。

式[（87.20）](#eq:c87-charged-curvatures)还直接表明：$W^+$的光子连接是$\partial_\mu-ieA_\mu$，正对应$Q=+1$。也可直接看规范代数，令$T^\pm=T^1\pm iT^2$，则
<span id="eq:c87-w-charges"></span>

$$
\begin{aligned}
A_\mu^1T^1+A_\mu^2T^2
 &=\frac1{\sqrt2}(W_\mu^+T^++W_\mu^-T^-),\\
\relax[Q,T^\pm]&=[T^3,T^\pm]=\pm T^\pm .
\end{aligned}
\tag{87.21}
$$

这与前面由双重态稳定子得到的电荷归一一致。

第一、第二曲率分量的平方现在可以相加。复组合的归一给
$(F^1)^2+(F^2)^2=2W^-_{\mu\nu}W^{+\mu\nu}$；再将两个反对称差各自展开，四个乘积两两相同，于是
<span id="eq:c87-charged-kinetic"></span>

$$
\begin{aligned}
-\frac14\big[(F^1)^2+(F^2)^2\big]
 &=-\frac12W^-_{\mu\nu}W^{+\mu\nu}\\
 &=-(D^{*\mu}W^{-\nu})(D_\mu W_\nu^+)
   +(D^{*\mu}W^{-\nu})(D_\nu W_\mu^+).
\end{aligned}
\tag{87.22}
$$

例如第一、第四个乘积交换$\mu,\nu$后相等，第二、第三个乘积也如此；前面的$1/2$被每组的两个相同项消去。这就是最终拉格朗日量中两个带电矢量动能结构的来由。

中性曲率还含一个带电双线性。利用式[（87.9）](#eq:c87-charged-fields)的逆变换，
<span id="eq:c87-charged-bilinear"></span>

$$
\begin{aligned}
A_\mu^1A_\nu^2-A_\nu^1A_\mu^2
 &=\frac i2\left[
 (W_\mu^++W_\mu^-)(W_\nu^+-W_\nu^-)
 -(\mu\leftrightarrow\nu)\right]\\
 &=-i(W_\mu^+W_\nu^--W_\nu^+W_\mu^-)
 =:-iX_{\mu\nu}.
\end{aligned}
\tag{87.23}
$$

同号的两个$W$乘积在反对称差中消去，异号的两个乘积各出现两次。因此负的$i$由复基的定义固定。再记
<span id="eq:c87-neutral-curvatures"></span>

$$
\begin{aligned}
F_{\mu\nu}&=\partial_\mu A_\nu-\partial_\nu A_\mu,\qquad
Z_{\mu\nu}=\partial_\mu Z_\nu-\partial_\nu Z_\mu,\\
N_{\mu\nu}&=s_WF_{\mu\nu}+c_WZ_{\mu\nu},\\
F_{\mu\nu}^3&=N_{\mu\nu}-ig_2X_{\mu\nu},\qquad
B_{\mu\nu}=c_WF_{\mu\nu}-s_WZ_{\mu\nu}.
\end{aligned}
\tag{87.24}
$$

$Z_{\mu\nu}$表示$Z$场的旋度；$Z$与$W$的相互作用由$X$和带电连接给出。

现在把两份中性曲率平方相加，以下$F^2,B^2,(F^3)^2$均表示两个曲率指标的完整收缩：
<span id="eq:c87-neutral-kinetic-expanded"></span>

$$
\begin{aligned}
-\frac14\big[(F^3)^2+B^2\big]
 &=-\frac14F^2-\frac14Z_{\mu\nu}Z^{\mu\nu}\\
 &\quad+\frac{ig_2}{2}N^{\mu\nu}X_{\mu\nu}
   +\frac{g_2^2}{4}X^{\mu\nu}X_{\mu\nu},\\
N^{\mu\nu}X_{\mu\nu}
 &=2N^{\mu\nu}W_\mu^+W_\nu^-,\\
X^{\mu\nu}X_{\mu\nu}
 &=2\left[
 (W^+\cdot W^+)(W^-\cdot W^-)
 -(W^+\cdot W^-)^2\right].
\end{aligned}
\tag{87.25}
$$

平方相加时，$FZ$的交叉项因正交旋转相消，而$(-ig_2X)^2=-g_2^2X^2$与外面的$-1/4$相乘给正号。随后的$NX$收缩用了$N^{\mu\nu}$的反对称性。最后把$X$的两个乘积各自相乘：两个同向配对给$(W^+)^2(W^-)^2$，两个交叉配对给$(W^+\cdot W^-)^2$，后者带负号。所有四次项的相对号和因子2由此确定。

<span id="c87-lagrangian"></span>

## 完整电弱拉格朗日量和残余规范变换

将带电动能、中性曲率平方以及Higgs部分合在一起，再用$g_2=e/s_W$、$\lambda=2m_H^2/v^2$，便得到完整电弱密度：
<span id="eq:c87-complete-electroweak-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_{\mathrm{EW},H}={}&
 -\frac14F_{\mu\nu}F^{\mu\nu}
 -\frac14Z_{\mu\nu}Z^{\mu\nu}\\
&-(D^{*\mu}W^{-\nu})(D_\mu W_\nu^+)
 +(D^{*\mu}W^{-\nu})(D_\nu W_\mu^+)\\
&+ie(F^{\mu\nu}+\cot\theta_WZ^{\mu\nu})W_\mu^+W_\nu^-\\
&-\frac{e^2}{2s_W^2}
 \left[(W^+\cdot W^-)^2
 -(W^+\cdot W^+)(W^-\cdot W^-)\right]\\
&-\left(M_W^2W^+\cdot W^-+\frac12M_Z^2Z^2\right)
 \left(1+\frac Hv\right)^2\\
&-\frac12(\partial H)^2-\frac12m_H^2H^2
 -\frac{m_H^2}{2v}H^3-\frac{m_H^2}{8v^2}H^4,
\end{aligned}
\tag{87.26}
$$

其中$D_\mu=\partial_\mu-ie(A_\mu+\cot\theta_WZ_\mu)$已经在式[（87.20）](#eq:c87-charged-curvatures)中求出。第三行来自$N^{\mu\nu}X_{\mu\nu}$，给带电矢量在最小耦合之外的场强耦合；第四行则保留了弱群曲率的四$W$相互作用。

这个作用量的电磁规范不变性现在可以逐项看出。取任意局部参数$\Gamma(x)$，
<span id="eq:c87-residual-electromagnetism"></span>

$$
\begin{aligned}
A_\mu'&=A_\mu-\partial_\mu\Gamma,\qquad
W_\mu^{\pm\prime}=e^{\mp ie\Gamma}W_\mu^\pm,\\
Z_\mu'&=Z_\mu,\qquad H'=H,\\
D_\mu'W_\nu^{+\prime}
 &=\bigl[\partial_\mu-iC_\mu^{\mathrm n}
          +ie\partial_\mu\Gamma\bigr]
   e^{-ie\Gamma}W_\nu^+\\
 &=e^{-ie\Gamma}D_\mu W_\nu^+ .
\end{aligned}
\tag{87.27}
$$

导数作用于相位所生的$-ie\partial_\mu\Gamma$与连接变化相消。于是两个带电动能因子共轭相乘时相位消去，$F_{\mu\nu}$和$Z_{\mu\nu}$本身不变，所有$W^+W^-$组合也不变。幺正规范固定的是破缺的三个方向，保留了这个电磁方向；完整$SU(2)\times U(1)$结构则通过各耦合之间的关系体现在式[（87.26）](#eq:c87-complete-electroweak-lagrangian)中。

为作当前的树级计算，可以直接使用这些物理场。若将计算推进到圈阶，就回到前两章所建立的$R_\xi$量子化和相应测度处理。

<span id="c87-rules"></span>

## 从作用量读出费曼规则

沿用第86节的办法，对每条外腿所对应的场取一次导数，再乘作用量中的$i$。所有动量都指向顶点，傅里叶因子取$e^{ipx}$，因而$\partial_\mu$给$ip_\mu$。以下顶角的Lorentz下指标与相应的上指标矢量场相接。

自由$W$场是两个实Proca场的复组合；将第85节的质量换成$M_W$便得到它的传播子。$Z$取$M_Z$，$H$取标量传播子。光子的剩余规范自由度另用费曼规范固定，即加入$-(\partial\cdot A)^2/2$。以下括号表示协变时间编序$T^*$的自由二点傅里叶核，也是实际内部线因子：
<span id="eq:c87-propagators"></span>

$$
\begin{aligned}
\langle W_\mu^+W_\nu^-\rangle_0(k)
 &=-i\,\frac{g_{\mu\nu}+k_\mu k_\nu/M_W^2}
 {k^2+M_W^2-i0},\\
\langle Z_\mu Z_\nu\rangle_0(k)
 &=-i\,\frac{g_{\mu\nu}+k_\mu k_\nu/M_Z^2}
 {k^2+M_Z^2-i0},\\
\langle A_\mu A_\nu\rangle_0(k)
 &=-i\,\frac{g_{\mu\nu}}{k^2-i0},\qquad
\langle HH\rangle_0(k)=-i\,\frac1{k^2+m_H^2-i0}.
\end{aligned}
\tag{87.28}
$$

$W^+W^+$与$W^-W^-$的自由收缩为零，这也可将两个等质量实场的收缩直接代入复组合验证。每条外部矢量腿乘相应偏振矢量，入射为$\varepsilon_\mu$，出射为$\varepsilon_\mu^*$；实标量外腿在当前树级归一下给1。有质量矢量有三个物理偏振，光子有两个。传播子分子中含有$k_\mu k_\nu/M^2$的理由已在[Proca核的求逆](/posts/srednicki-85/#c85-propagator)中给出。

先看不含导数的Higgs相互作用。$HWW$项为$-2M_W^2HW^+\cdot W^-/v$，两条$W$腿可区分；$HZZ$项为$-M_Z^2HZ^2/v$，但两次$Z$场微分带来$2!$。两者因此有相同的质量依赖：
<span id="eq:c87-higgs-vertices"></span>

$$
\begin{aligned}
iV_{H W^+_\alpha W^-_\beta}
 &=-\frac{2iM_W^2}{v}g_{\alpha\beta},&
iV_{H Z_\alpha Z_\beta}
 &=-\frac{2iM_Z^2}{v}g_{\alpha\beta},\\
iV_{HH W^+_\alpha W^-_\beta}
 &=-\frac{2iM_W^2}{v^2}g_{\alpha\beta},&
iV_{HH Z_\alpha Z_\beta}
 &=-\frac{2iM_Z^2}{v^2}g_{\alpha\beta},\\
iV_{HHH}&=-\frac{3im_H^2}{v},&
iV_{HHHH}&=-\frac{3im_H^2}{v^2}.
\end{aligned}
\tag{87.29}
$$

第二行的两个$H$再给$2!$；在$HHZZ$中，它与两个$Z$的$2!$共同乘原密度的$-M_Z^2/(2v^2)$。最后一行则分别由$3!$、$4!$乘$-m_H^2/(2v)$、$-m_H^2/(8v^2)$而来。三点耦合质量维数为1，四点为0，与四维场的量纲一致。

规范三点顶角需要保留导数作用在哪一条腿上。为同时处理光子和$Z$，记$V=A$或$Z$，相应耦合为$q_A=e$、$q_Z=e\cot\theta_W$。在式[（87.26）](#eq:c87-complete-electroweak-lagrangian)的两个带电动能中各取一次连接，再加上中性曲率项，得到
<span id="eq:c87-cubic-density"></span>

$$
\begin{aligned}
\mathcal L_{3,V}=iq_V\big[&
 V_\mu(\partial^\mu W^{-\nu})W_\nu^+
 -V^\mu W^{-\nu}\partial_\mu W_\nu^+\\
&-V_\nu(\partial^\mu W^{-\nu})W_\mu^+
 +V^\mu W^{-\nu}\partial_\nu W_\mu^+\\
&+(\partial^\mu V^\nu-\partial^\nu V^\mu)
 W_\mu^+W_\nu^-\big].
\end{aligned}
\tag{87.30}
$$

取三条腿依次为$(W^{+\alpha},p)$、$(W^{-\beta},q)$、$(V^\rho,k)$。第一行的两个导数给$i q^\mu$和$i p_\mu$，与前面的$i$相乘后，密度系数是$q_V(p-q)_\rho g_{\alpha\beta}$。第二行依次给$q_Vq_\alpha g_{\beta\rho}$和$-q_Vp_\beta g_{\alpha\rho}$。最后一行的导数作用于中性腿，给$q_V(-k_\alpha g_{\beta\rho}+k_\beta g_{\alpha\rho})$。将三组相加，再乘作用量的$i$，便得
<span id="eq:c87-triple-vector-vertex"></span>

$$
\begin{aligned}
iV_{\alpha\beta\rho}^{W^+W^-V}(p,q,k)
 =iq_V\big[&
 (p-q)_\rho g_{\alpha\beta}
 +(q-k)_\alpha g_{\beta\rho}\\
 &+(k-p)_\beta g_{\rho\alpha}\big],
\qquad p+q+k=0 .
\end{aligned}
\tag{87.31}
$$

中性曲率项补上的正是含$k$的两个结构。因此完整三点顶角的动量组合由非阿贝尔规范动能共同确定，同时包含带电动能和中性曲率平方的贡献。

两条中性腿的四点作用来自两个协变导数各取一次连接。前一个带电动能给$-(C^{\mathrm n})^2W^+\cdot W^-$，后一个给$(C^{\mathrm n}\cdot W^+)(C^{\mathrm n}\cdot W^-)$，合起来是
<span id="eq:c87-neutral-quartic-density"></span>

$$
\mathcal L_{C^2}
 =-(C^{\mathrm n}\cdot C^{\mathrm n})(W^+\cdot W^-)
 +(C^{\mathrm n}\cdot W^+)(C^{\mathrm n}\cdot W^-).
\tag{87.32}
$$

令四条腿依次为$W^{+\alpha},W^{-\beta},V^\rho,V'^\sigma$。第一项中两条中性腿分配给两个$C^{\mathrm n}$，两种分配都给$-q_Vq_{V'}g_{\alpha\beta}g_{\rho\sigma}$；第二项的两种分配分别给$q_Vq_{V'}g_{\alpha\rho}g_{\beta\sigma}$和$q_Vq_{V'}g_{\alpha\sigma}g_{\beta\rho}$。所以
<span id="eq:c87-neutral-quartic-vertex"></span>

$$
iV_{\alpha\beta\rho\sigma}^{W^+W^-VV'}
 =-iq_Vq_{V'}\left[
 2g_{\alpha\beta}g_{\rho\sigma}
 -g_{\alpha\rho}g_{\beta\sigma}
 -g_{\alpha\sigma}g_{\beta\rho}\right].
\tag{87.33}
$$

它包括$AA,AZ,ZZ$三种情况。若两种中性腿相同，两种分配就是两次相同场微分；若不同，它们来自连接平方的交叉项。因此通式中已经包含两种情形所需的组合因子。

最后处理四$W$项。给两条正电荷腿指标$\alpha,\rho$，两条负电荷腿指标$\beta,\sigma$。$(W^+\cdot W^-)^2$有两种跨电荷配对，每种在两个相同括号中的分配数为2；$(W^+\cdot W^+)(W^-\cdot W^-)$则有$2!\,2!=4$种分配。乘上原密度中的$-g_2^2/2$及相对负号，得到
<span id="eq:c87-four-w-vertex"></span>

$$
iV_{\alpha\beta\rho\sigma}^{W^+W^-W^+W^-}
 =ig_2^2\left[
 2g_{\alpha\rho}g_{\beta\sigma}
 -g_{\alpha\beta}g_{\rho\sigma}
 -g_{\alpha\sigma}g_{\rho\beta}\right].
\tag{87.34}
$$

交换两条$W^+$或两条$W^-$时，这个张量保持不变，正如相同玻色子所要求的那样。三、四矢量顶角的量纲分别为1和0，也与前面的Higgs顶角相合。

<span id="c87-higgs-decays"></span>

## Higgs 衰变成两个有质量矢量

取$m_H>2M_Z$，使$W^+W^-$和$ZZ$两条通道都能产生实在壳粒子。对任一通道暂记矢量质量为$M_V$，初态Higgs动量为$p=k_1+k_2$，有
<span id="eq:x87-decay-kinematics"></span>

$$
\begin{aligned}
p^2&=-m_H^2,\qquad k_1^2=k_2^2=-M_V^2,\\
k_1\cdot k_2
 &=\frac12(p^2-k_1^2-k_2^2)
 =M_V^2-\frac{m_H^2}{2}.
\end{aligned}
\tag{87.41}
$$

由$HVV$顶角，对指定的两个出射偏振，
<span id="eq:x87-decay-amplitude"></span>

$$
\mathcal T_{r_1r_2}
 =-\frac{2M_V^2}{v}\,
 \varepsilon_{r_1}^{*\mu}(k_1)
 \varepsilon_{r_2\mu}^*(k_2).
\tag{87.42}
$$

两个顶角在$W$、$Z$情形有相同形式，是因为$HZZ$的相同场因子已经在读取顶角时算过。现在求未分辨偏振的衰变率，需要对三个物理偏振求和。用有质量矢量的完备关系
$\sum_r\varepsilon_r^\mu(k)\varepsilon_r^{*\nu}(k)=g^{\mu\nu}+k^\mu k^\nu/M_V^2$，得到
<span id="eq:x87-polarization-sum"></span>

$$
\begin{aligned}
\sum_{r_1,r_2}|\mathcal T_{r_1r_2}|^2
 &=\frac{4M_V^4}{v^2}
 \left(g^{\mu\nu}+\frac{k_1^\mu k_1^\nu}{M_V^2}\right)
 \left(g_{\mu\nu}+\frac{k_{2\mu}k_{2\nu}}{M_V^2}\right)\\
 &=\frac{4M_V^4}{v^2}
 \left[4+\frac{k_1^2}{M_V^2}+\frac{k_2^2}{M_V^2}
       +\frac{(k_1\cdot k_2)^2}{M_V^4}\right]\\
 &=\frac{4M_V^4}{v^2}
 \left[2+\left(1-\frac{m_H^2}{2M_V^2}\right)^2\right]\\
 &=\frac{m_H^4}{v^2}(1-4x_V+12x_V^2),
 \qquad x_V:=\frac{M_V^2}{m_H^2}.
\end{aligned}
\tag{87.43}
$$

中间两个收缩各给$-1$，这是当前度规下$k_i^2=-M_V^2$的直接结果。最后一行展开平方，并把$4M_V^4$乘入；常数$12M_V^4$由前一行中的$2+1$共同产生。

偏振求和后的振幅只依赖质量，在初态静止系中各向同性。将第11节两体相空间的已积结果用于$\sqrt s=m_H$、两个相同质量$M_V$，出射动量大小为
$|\mathbf k|=\sqrt{m_H^2-4M_V^2}/2$。于是
<span id="eq:x87-decay-phase-space"></span>

$$
\begin{aligned}
\int d{\rm LIPS}_2
 &=\frac{|\mathbf k|}{4\pi m_H}
 =\frac1{8\pi}\sqrt{1-4x_V},\\
\Gamma_V
 &=\frac{1}{2m_HS_V}
 \left(\sum_{r_1,r_2}|\mathcal T_{r_1r_2}|^2\right)
 \int d{\rm LIPS}_2 .
\end{aligned}
\tag{87.44}
$$

第一行中的$4\pi$来自全角积分，径向能量 δ 函数的雅可比因子已在[两体能量 δ 函数的积分](/posts/srednicki-11/#eq:c11-energy-jacobian)中求出；这里的新代入是$E_1=E_2=m_H/2$。第二行前的$1/(2m_H)$来自单个初态的归一。$W^+$、$W^-$有不同电荷，所以$S_W=1$；两个$Z$相同，有序的$(k_1,r_1),(k_2,r_2)$把同一末态数了两次，所以$S_Z=2!$。这与顶角中对$Z$场求导产生的$2!$各有自己的来源。

代入后两条宽度为
<span id="eq:x87-higgs-widths"></span>

$$
\begin{aligned}
\Gamma(H\to W^+W^-)
 &=\frac{m_H^3}{16\pi v^2}
 \sqrt{1-4x_W}\,(1-4x_W+12x_W^2),\\
\Gamma(H\to ZZ)
 &=\frac{m_H^3}{32\pi v^2}
 \sqrt{1-4x_Z}\,(1-4x_Z+12x_Z^2).
\end{aligned}
\tag{87.45}
$$

宽度的量纲是1。接近各通道阈值时，偏振多项式保持有限，宽度由相空间的平方根趋于零；在$m_H^2\gg M_V^2$时，多项式和平方根都趋于1，因此两通道宽度之比趋于2。这一极限下两个纵向偏振贡献最大：在Higgs静止系取它们沿相反动量方向，内积为$1-m_H^2/(2M_V^2)$，其平方正是式[（87.43）](#eq:x87-polarization-sum)第三行中的大项。两个偏振矢量各带一个能量与质量之比，因而抵消了顶角的$M_V^2$抑制，最后使宽度按$m_H^3/v^2$增长。

按中译本习题87.5，设想$m_H=200$ GeV，并用上面的$v=246.560$ GeV及中译本分别给出的$M_W=80.4$ GeV、$M_Z=91.2$ GeV，计算为

| 通道     | $x_V$    | $\sqrt{1-4x_V}$ | $1-4x_V+12x_V^2$ | $\Gamma$／GeV |
| -------- | -------- | --------------- | ---------------- | ------------- |
| $W^+W^-$ | 0.161604 | 0.594629        | 0.666974         | 1.03832       |
| $ZZ$     | 0.207936 | 0.410190        | 0.687105         | 0.368938      |

按输入的精度，可写$\Gamma_{WW}\simeq1.04$ GeV、$\Gamma_{ZZ}\simeq0.369$ GeV。这是中译本设定质量为200 GeV的树级算例。这里将$W,Z$按零宽度近似放在壳上；阈值以下的通道则由离壳矢量衰变成费米子的多体末态描述。

---

[← 第 86 节](/posts/srednicki-86/) · [章节地图](/srednicki/) · [第 88 节 →](/posts/srednicki-88/)
