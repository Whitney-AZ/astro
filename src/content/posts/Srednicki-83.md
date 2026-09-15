---
title: 'Srednicki §83 手征对称性破缺'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [83]
hideFromHome: true
draft: false
---

<span id="c83"></span>

上一节讨论了没有夸克的杨—米尔斯理论。加入夸克以后，低能强作用还出现一个很突出的现象：质子和中子的质量接近1 GeV，而π介子轻得多。这些粒子都是色单态，禁闭本身并不说明它们之间为何有这样大的质量差别。现在要考察夸克的味对称性，以及这个对称性在真空和强子谱中怎样实现。

以下采用中译本的近似数值作计算示例；夸克质量参数连同其重整化方案和尺度使用。

<span id="c83-light-flavors"></span>

## 哪些夸克可以看作轻夸克

夸克共有六种味。每一种味都是色群$SU(3)$基本表示中的狄拉克场，电荷则决定它怎样参与电磁作用：

| 味     | 符号 | 中译本质量／GeV | 电荷／质子电荷 |
| ------ | ---- | --------------: | -------------: |
| 上夸克 | $u$  |          0.0017 |         $+2/3$ |
| 下夸克 | $d$  |          0.0039 |         $-1/3$ |
| 奇夸克 | $s$  |           0.076 |         $-1/3$ |
| 粲夸克 | $c$  |             1.3 |         $+2/3$ |
| 底夸克 | $b$  |             4.3 |         $-1/3$ |
| 顶夸克 | $t$  |             178 |         $+2/3$ |

表中列的是$\overline{\mathrm{MS}}$质量参数。轻三味取$\mu=2$ GeV，其余在各自质量标度处给值，例如表中的底夸克满足$m_b(4.3\,\mathrm{GeV})=4.3$ GeV。夸克质量与强作用尺度的比较使用这套约定。

沿[第73节](/posts/srednicki-73/#c73-physical)，降低能标会使规范耦合增大。只保留一圈$\beta=-b_1g^3$，并把积分常数写成质量尺度$\Lambda$，有
<span id="eq:c83-strong-scale"></span>

$$
\begin{aligned}
\frac{d}{d\ln\mu}\frac1{g^2}&=2b_1,\\
\frac1{g^2(\mu)}&=2b_1\ln\frac\mu\Lambda,\qquad
b_1=\frac{11-2n_F/3}{16\pi^2}.
\end{aligned}
\tag{83.1}
$$

这条微扰曲线在$\mu=\Lambda$发散，表明它已进入自身不能控制的区域。把截断$\beta$函数后出现的强尺度记作$\Lambda_{\rm QCD}$，取约0.2 GeV作为数量级示例；具体数值随方案、活跃味数及截断精度改变。对眼下的物理问题，关键是$m_u,m_d\ll\Lambda_{\rm QCD}$，所以可先令这两个质量为零。奇夸克也比强尺度轻一些，三味近似因而有用，但它的质量修正通常较大。

对于约1 GeV以下的强子过程，粲、底、顶夸克不再作为低能传播的自由度。将它们积掉以后，其作用保留在低能参数的匹配值和高维局域项中；这就是此处忽略重味的含义。我们先连奇夸克一起略去，研究$n_F=2$的无质量理论。

<span id="c83-flavor"></span>

## 左右味旋转与轴反常

把每个狄拉克场拆成两个左手外尔场。记$\chi_{\alpha i}$属于色$\mathbf3$，$\xi^{\alpha\bar\imath}$属于$\bar{\mathbf3}$；$\alpha=1,2,3$为色指标，$i,\bar\imath=1,2$为两套味指标，旋量指标暂时省去。第二套场的共轭恰好构成狄拉克右手分量。取厄米色生成元$t^A$、$\operatorname{Tr}_c(t^At^B)=\delta^{AB}/2$，共轭表示由$e^{i\theta^At^A}$的复共轭给出，故
<span id="eq:c83-weyl-lagrangian"></span>

$$
\begin{aligned}
t_{\bar3}^A&=-(t_3^A)^T,\\
D_\mu&=\partial_\mu-igt_3^AA_\mu^A,\qquad
\bar D_\mu=\partial_\mu-igt_{\bar3}^AA_\mu^A,\\
\mathcal L&=i\chi^{\dagger\alpha i}\bar\sigma^\mu
                (D_\mu)_\alpha{}^\beta\chi_{\beta i}\\
&\quad+i\xi^\dagger_{\bar\imath\alpha}\bar\sigma^\mu
                (\bar D_\mu)^\alpha{}_{\beta}\xi^{\beta\bar\imath}
 -\frac14F^{A\mu\nu}F^A_{\mu\nu}.
\end{aligned}
\tag{83.2}
$$

颜色作用对每个味都相同，且没有质量项连接两套外尔场。因此可以分别转动它们的味指标：
<span id="eq:c83-chiral-transformations"></span>

$$
\begin{aligned}
\chi_i&\longmapsto L_i{}^j\chi_j,\\
\xi^{\bar\imath}&\longmapsto
 (R^*)^{\bar\imath}{}_{\bar\jmath}\xi^{\bar\jmath},\\
\Psi_i&=\begin{pmatrix}\chi_i\\ \xi_i^\dagger\end{pmatrix},\\
P_L\Psi&\longmapsto LP_L\Psi,\qquad
P_R\Psi\longmapsto RP_R\Psi .
\end{aligned}
\tag{83.3}
$$

$L,R$是独立常数酉矩阵。对$\xi$取伴随后，系数中的$R^*$再共轭一次，右分量就按$R$变换，说明采用复共轭记号的便利。每个动能项中的味矩阵相邻成为$L^\dagger L$或$R^TR^*$，等于单位阵；导数不作用于常数矩阵。经典拉氏量于是有$U(2)_L\times U(2)_R$味对称性。以不同方式转动左右手分量的对称性，称为手征对称性（chiral symmetry）。

两个共同相位的作用不同。用$P_{L,R}=(1\mp\gamma_5)/2$，可以直接把左右分量重新合起来：
<span id="eq:c83-axial-vector-phases"></span>

$$
\begin{aligned}
L=R^*=e^{i\alpha}I:\quad
\Psi&\longmapsto
 (e^{i\alpha}P_L+e^{-i\alpha}P_R)\Psi
 =e^{-i\alpha\gamma_5}\Psi,\\
L=R=e^{-i\alpha}I:\quad
\Psi&\longmapsto e^{-i\alpha}\Psi .
\end{aligned}
\tag{83.4}
$$

第一种是轴向$U(1)_A$，第二种是矢量$U(1)_V$。第76、77章已经说明轴变换会改变费米积分测度。在味空间插入一个厄米矩阵$X$，令$j_{A,X}^\mu=\bar\Psi X\gamma^\mu\gamma_5\Psi$。两个胶子顶角对味都为单位阵，因此[既有反常结果](/posts/srednicki-77/#c77-background)中的迹分解为味迹与色迹，给出
<span id="eq:c83-flavor-anomaly"></span>

$$
\begin{aligned}
\partial_\mu j_{A,X}^\mu
&=-\frac{g^2}{16\pi^2}\operatorname{tr}_fX\,
 \epsilon^{\mu\nu\rho\sigma}
 \operatorname{Tr}_c(F_{\mu\nu}F_{\rho\sigma})\\
&=-\frac{g^2}{32\pi^2}\operatorname{tr}_fX\,
 \epsilon^{\mu\nu\rho\sigma}F^A_{\mu\nu}F^A_{\rho\sigma}.
\end{aligned}
\tag{83.5}
$$

半迹色归一给第二行的$1/2$。共同轴相位取$X=I_{n_F}$，所以有$n_F$份贡献；无迹味生成元则使这项纯色反常为零。共同矢量相位在两左手外尔场上取相反号，而$\mathbf3$与$\bar{\mathbf3}$的二次色迹相同，两项恰好抵消。量子强作用由此保留的连续味对称性是$SU(2)_L\times SU(2)_R\times U(1)_V$。这里讨论的是味流在强相互作用中的守恒；若另加背景味规范场，还须研究相应的反常。

取$L=R$就得到矢量子群$SU(2)_V$，即同位旋（isospin）。轴方向则以$R=L^\dagger$描述。对无穷小变换，定义$V^a=Q_L^a+Q_R^a$、$A^a=Q_L^a-Q_R^a$，两套荷彼此交换，便有
<span id="eq:c83-vector-axial-algebra"></span>

$$
\begin{aligned}
\relax [V^a,V^b]&=i\epsilon^{abc}V^c,\qquad
[V^a,A^b]=i\epsilon^{abc}A^c,\\
[A^a,A^b]&=i\epsilon^{abc}V^c .
\end{aligned}
\tag{83.6}
$$

最后一式说明轴方向并不单独闭合成另一个有限$SU(2)$子群。事实上，两个$(L,L^\dagger)$相乘后，右矩阵的次序通常不等于左矩阵乘积的伴随。后面需要辨认的是这三个轴方向是否改变真空。

$U(1)_V$的守恒荷数夸克减反夸克。重子含三个价夸克，介子含一夸克和一反夸克，因此
<span id="eq:c83-baryon-number"></span>

$$
Q_q=N_q-N_{\bar q}=3B .
\tag{83.7}
$$

强子按$SU(2)_V$组成多重态：质子0.938 GeV、中子0.940 GeV构成二重态，$\pi^0$的0.135 GeV和$\pi^\pm$的0.140 GeV构成三重态。$m_u-m_d$和电磁相互作用造成小的同位旋破缺。相形之下，完整手征对称性并没有表现为一套明显的等质量轴伙伴。这引导我们考虑真空已选择一个保持同位旋、却改变轴方向的取向。

<span id="c83-condensate"></span>

## 费米子凝聚与真空取向

真空的序参量须与未破缺的洛伦兹对称性和色对称性相容。QCD没有基本标量，但两个夸克场可以构成色单态的洛伦兹标量。将旋量指标$r$写出，最简单的候选是
<span id="eq:c83-order-parameter"></span>

$$
\begin{aligned}
\Phi_i{}^{\bar j}
&=\chi_{\alpha i}^{\,r}\xi_r^{\alpha\bar j}
 =\bar\Psi^{\alpha\bar j}P_L\Psi_{\alpha i},\\
\chi^r\xi_r
&=-\xi_r\chi^r
 =-\epsilon^{rs}\xi_r\chi_s
 =\xi^s\chi_s,\\
\Phi&\longmapsto L\Phi R^\dagger .
\end{aligned}
\tag{83.8}
$$

第二行说明这两个奇旋量的完整缩并对交换次序为偶：奇场交换的负号被反对称旋量度规的负号抵消。色指标缩并成单态，留下的只是左右味指标。

假定重整化后的复合算符取得
<span id="eq:c83-condensate"></span>

$$
\langle\Phi_i{}^{\bar j}\rangle=-v^3\delta_i{}^{\bar j},\qquad
\langle\bar\Psi_i\Psi_i\rangle=-2v^3
\quad\hbox{（每味，不对$i$求和）}.
\tag{83.9}
$$

右边的第二个2来自左右两个投影。$v$有质量量纲；在$\mu=2$ GeV的$\overline{\mathrm{MS}}$方案中，以$v\simeq0.23$ GeV作为示例。非零凝聚是这里的动力学输入，后续对称性分析从它出发。负号的物理选择将在加入正夸克质量时由真空能量说明。

和第32节一样，讨论自发破缺时要选定一个真空。可以先加微小外源选择取向，取无限体积，再移去外源。保持味对称的有限体积平均会把不同取向一起平均掉。在所选真空上，变换后的凝聚为$-v^3LR^\dagger$；保持它要求$L=R$，于是稳定子是$SU(2)_V$。$U(1)_V$在$\Phi$上原本就相互抵消，也保持不变。

共有$6-3=3$个连续破缺方向。[第32节的流极点论证](/posts/srednicki-32/#c32-ward-pole)因而在手征极限预言三个戈德斯通玻色子。π介子的数目与轻质量正符合这个图景；加入小的显式破缺后，它们成为赝戈德斯通玻色子（pseudo-Goldstone bosons）。这是一种以凝聚为基础的低能实现，前述强子谱为它提供了物理动机。

在保持手征对称的微扰真空中，$\langle\Phi\rangle$各阶都为零：若它不为零，独立左右旋转要求它同时等于任意$L\langle\Phi\rangle R^\dagger$，只有零矩阵满足这个条件。因此有限阶微扰展开不能从这个真空算出$v$。无质量QCD的尺度由$\Lambda_{\rm QCD}$产生，量纲分析预期$v$、核子质量等都是这一尺度的无量纲倍数；这些倍数仍需非微扰方法或实验来确定。

<span id="c83-pion-field"></span>

## 用缓变取向描述π介子

戈德斯通激发是在邻近时空区域中缓慢转动凝聚取向。凝聚的大小及其它强子激发可以暂时积掉，把低能背景记为
<span id="eq:c83-pion-coordinate"></span>

$$
\begin{aligned}
\Phi_{\rm low}(x)&=-v^3U(x),\qquad U^\dagger U=I,\quad\det U=1,\\
U(x)&=e^{2i\Pi(x)},\qquad
\Pi=\frac{\pi^aT^a}{f_\pi},\qquad T^a=\frac{\sigma^a}{2},\\
U&\longmapsto LUR^\dagger .
\end{aligned}
\tag{83.10}
$$

这里的时空依赖表示缓变的集体场配置；均匀真空本身仍对应常数$U$。这里用味生成元$T^a$与色生成元$t^A$作区别。只保留$SU(2)$的三个生成元，因为共同轴$U(1)$已被反常破坏，不再有由它保证的第四个无质量场。$U(1)_V$不必另行进入$U$的变换律，因为它在双线性序参量上作用平凡。

取$L=e^{i\alpha^aT^a}$、$R=e^{-i\alpha^aT^a}$，在$U=I$附近，
<span id="eq:c83-goldstone-shift"></span>

$$
\delta U=2i\alpha^aT^a
=\frac{2i}{f_\pi}\delta\pi^aT^a,\qquad
\delta\pi^a=f_\pi\alpha^a .
\tag{83.11}
$$

这就是角坐标在破缺方向上的常数平移。宇称交换左右投影，使$\Phi$变成$\Phi^\dagger$，故$U(t,\mathbf x)\to U^\dagger(t,-\mathbf x)$。在指数坐标中，$\pi^a$随之变号，所以这三个场为赝标量，和π介子的宇称一致。

<span id="c83-derivative"></span>

## 双导数拉氏量及其展开

我们用对称性组织$U$的有效拉氏量，称为手征拉格朗日量（chiral Lagrangian）。没有导数时，任意两个$SU(2)$矩阵都可由$U\to LUR^\dagger$相互联系，所以不变量只能是常数。这也说明为什么旋转取向不需势能。含两个导数时，先令$Y_\mu=U^\dagger\partial_\mu U$；它无迹、反厄米，并按$Y_\mu\to RY_\mu R^\dagger$变换。一个导数指标不能单独构成洛伦兹标量，两个导数则须相互收缩。

把$Y_\mu$展开在三个味生成元上，同位旋转动要求它们的双线性系数正比于$\delta^{ab}$：绕坐标轴的转动先消去非对角元，交换轴的转动再使三个对角元相等。双迹项因$\operatorname{tr}_fY_\mu=\partial_\mu\ln\det U=0$而消失。含$\partial^2U$的项经分部积分与$\partial(U^\dagger U)=0$回到同一形式。因此，除常数与全导数外，只有
<span id="eq:c83-two-derivative-action"></span>

$$
\mathcal L_2
=-\frac{f_\pi^2}{4}\operatorname{tr}_f
       (\partial^\mu U^\dagger\partial_\mu U)
=\frac{f_\pi^2}{4}\operatorname{tr}_f(Y^\mu Y_\mu).
\tag{83.12}
$$

系数的写法将使三个实场具有通常的动能归一。现在求出其中的第一项相互作用。

矩阵指数的微分不能直接当作可交换量来算。对任意矩阵场$X$，引入$F(t)=e^{-tX}\partial_\mu e^{tX}$。对参数$t$求导时，含$X\partial_\mu e^{tX}$的两项相消，留下$F'(t)=e^{-tX}(\partial_\mu X)e^{tX}$。又$F(0)=0$，故
<span id="eq:c83-exponential-differential"></span>

$$
\begin{aligned}
e^{-X}\partial_\mu e^X
&=\int_0^1dt\,e^{-tX}(\partial_\mu X)e^{tX}\\
&=\partial_\mu X-\frac12[X,\partial_\mu X]
 +\frac16[X,[X,\partial_\mu X]]+\cdots .
\end{aligned}
\tag{83.13}
$$

第二行可对被积矩阵再求$t$导数，每次产生$-[X,\cdot]$；泰勒系数$t^n/n!$积分后为$1/(n+1)!$。令$X=2i\Pi$，便得到
<span id="eq:c83-maurer-cartan-expansion"></span>

$$
Y_\mu=2i\partial_\mu\Pi
 +2[\Pi,\partial_\mu\Pi]
 -\frac{4i}{3}[\Pi,[\Pi,\partial_\mu\Pi]]+\cdots .
\tag{83.14}
$$

这里的三项分别含一、二、三份π场。平方后，三场项的迹为$\operatorname{tr}(\partial\Pi[\Pi,\partial\Pi])=0$。为算四场项，记$K_\mu=[\Pi,\partial_\mu\Pi]$，用迹的循环性把双重对易子的一层移到另一因子上：
<span id="eq:c83-quartic-trace"></span>

$$
\begin{aligned}
&\operatorname{tr}_f\bigl(\partial^\mu\Pi[\Pi,[\Pi,\partial_\mu\Pi]]\bigr)\\
&\quad=\operatorname{tr}_f\bigl([\partial^\mu\Pi,\Pi]K_\mu\bigr)
=-\operatorname{tr}_f(K^\mu K_\mu),\\
&\left.\operatorname{tr}_f(Y^\mu Y_\mu)\right|_{\pi^4}\\
&\quad=\left(4-\frac{16}{3}\right)\operatorname{tr}_f(K^\mu K_\mu)
=-\frac43\operatorname{tr}_f(K^\mu K_\mu).
\end{aligned}
\tag{83.15}
$$

四场部分的4来自两个二场项相乘；$-16/3$来自一场项与三场项的两种次序。再使用泡利生成元，
<span id="eq:c83-pauli-quartic"></span>

$$
\begin{aligned}
K_\mu&=\frac{i}{f_\pi^2}
 \epsilon^{abc}\pi^a\partial_\mu\pi^bT^c,\\
\operatorname{tr}_f(K^\mu K_\mu)
&=-\frac1{2f_\pi^4}
 (\delta^{ad}\delta^{be}-\delta^{ae}\delta^{bd})
 \pi^a\pi^d\partial^\mu\pi^b\partial_\mu\pi^e\\
&=-\frac1{2f_\pi^4}
 \left[\pi^2(\partial\pi)^2-(\pi\cdot\partial^\mu\pi)
                                      (\pi\cdot\partial_\mu\pi)\right].
\end{aligned}
\tag{83.16}
$$

其中$\epsilon^{abc}\epsilon^{dec}=\delta^{ad}\delta^{be}-\delta^{ae}\delta^{bd}$，味点积与时空指标的收缩分别写出。代回式[（83.12）](#eq:c83-two-derivative-action)，得到
<span id="eq:c83-four-pion-lagrangian"></span>

$$
\begin{aligned}
\mathcal L_2
&=-\frac12\partial^\mu\pi^a\partial_\mu\pi^a\\
&\quad+\frac1{6f_\pi^2}
 \left[\pi^a\pi^a\partial^\mu\pi^b\partial_\mu\pi^b
 -\pi^a\pi^b\partial^\mu\pi^a\partial_\mu\pi^b\right]\\
&\quad+O\!\left(\frac{\pi^4(\partial\pi)^2}{f_\pi^4}\right).
\end{aligned}
\tag{83.17}
$$

动能的$-1/2$给出实场的常规归一，第一个相互作用含两个导数。变换$U\leftrightarrow U^\dagger$使拉氏量不变，故指数坐标中的奇数π项消失；所列余项从六场开始，仍属于同一个双导数拉氏量。

这个展开按场数显示相互作用，而有效理论的精度还要按动量组织。设一个连通介子图有$\ell$圈、$I$条内线，顶角$v$带$d_v$个导数。每个圈积分给$p^4$，每个传播子给$p^{-2}$，所以总动量次数是
<span id="eq:c83-chiral-power-counting"></span>

$$
D=4\ell-2I+\sum_vd_v
 =2+2\ell+\sum_v(d_v-2),\qquad \ell=I-V+1 .
\tag{83.18}
$$

若只用双导数顶角，每个含$n_v$份场的顶角还带$f_\pi^{2-n_v}$。由$\sum_vn_v=2I+E$，$E$条外腿的图中$f_\pi$总幂为$2-E-2\ell$。再计四维每圈的$1/(16\pi^2)$，典型量级便是
<span id="eq:c83-loop-scale"></span>

$$
\mathcal T_E^{(\ell)}\sim
 \frac{p^2}{f_\pi^{E-2}}
 \left(\frac{p^2}{16\pi^2f_\pi^2}\right)^\ell .
\tag{83.19}
$$

各圈的对数和无量纲系数未在这条量级式中展开。它说明软动量时圈修正被$p^2/(4\pi f_\pi)^2$压低，也解释了约$4\pi f_\pi$的相互作用尺度。四导数及更高导数项各有独立低能常数；若这些常数取自然大小，在截止附近不同阶可能相当，而在低能区应逐阶保留。实际使用范围还受新强子态的出现限制。

取中译本的$f_\pi=92.4$ MeV，于是$4\pi f_\pi$约为1 GeV。$f_\pi$本身小于π介子质量并不妨碍低能展开，因为圈阶比较用的是后一个尺度。它被称为π介子衰变常数（pion decay constant），因为同一流—戈德斯通耦合还控制弱衰变；[第90节](/posts/srednicki-90/#c90)将用这一流耦合讨论弱衰变。

<span id="c83-mass"></span>

## 小夸克质量怎样进入有效理论

在严格手征极限，任意常数取向的能量相同，π介子因而无质量。真实的上、下夸克虽轻，质量却不为零。这些质量连接原来可以独立旋转的左右分量，从而偏爱某个凝聚取向；使取向偏离这个最低点便需要能量，π介子的质量就从这里产生。

最一般的两味质量矩阵$M$是复$2\times2$矩阵。用式[（83.8）](#eq:c83-order-parameter)已经算过的奇旋量缩并次序，微观质量项为
<span id="eq:c83-quark-mass"></span>

$$
\begin{aligned}
\mathcal L_{\rm mass}^{\rm quark}
&=-\xi^{\alpha\bar j}M_{\bar ji}\chi_{\alpha i}
  +\text{h.c.}\\
&=-M_{\bar ji}\chi_{\alpha i}\xi^{\alpha\bar j}
  +\text{h.c.}
 =-\operatorname{tr}_f(M\Phi+\Phi^\dagger M^\dagger).
\end{aligned}
\tag{83.20}
$$

这一步交换的是完整洛伦兹缩并，故两行之间没有新的负号。矩阵$M$的两个指标分别接到右、左味空间上。

先说明质量矩阵为什么还留下一个共同相位。对非奇异$M$，将正定矩阵$M^\dagger M$用酉矩阵$V_L$对角化，得到$V_L^\dagger M^\dagger M V_L=D^2$，其中$D=\operatorname{diag}(m_u,m_d)$且两个质量取正。定义$V_R=MV_LD^{-1}$，便有$V_R^\dagger V_R=I$以及$M=V_RDV_L^\dagger$。这就是此处所需的奇异值分解。再把两个酉矩阵的行列式相位分离出来：
<span id="eq:c83-mass-phase"></span>

$$
\begin{aligned}
V_R&=e^{ir/2}R_0,\qquad V_L=e^{i\ell/2}L_0,
 \qquad R_0,L_0\in SU(2),\\
R_0^\dagger M L_0
&=D\,e^{i(r-\ell)/2}=D\,e^{-i\theta/2},
 \qquad \theta=\ell-r,\\
\det M&=m_um_d\,e^{-i\theta}.
\end{aligned}
\tag{83.21}
$$

左右$SU(2)$变换不改变最后一行，所以不能消去这个相位。$\theta$改变$2\pi$所产生的共同负号可由$SU(2)$的中心吸收；若某个质量恰为零，上面的$D^{-1}$不再存在，该情形须单独处理。

轴相位能够改变$\det M$，但它也改变积分测度。具体地，在费米积分中令$\Psi_{\rm old}=e^{-i\alpha\gamma_5}\Psi_{\rm new}$，则$\Phi_{\rm old}=e^{2i\alpha}\Phi_{\rm new}$，质量矩阵变为$M_{\rm new}=Me^{2i\alpha}$。沿[第77节的测度计算](/posts/srednicki-77/#c77-ward)，每味贡献相同的色迹；两味时取$\alpha=\theta/4$，得到
<span id="eq:c83-axial-mass-transfer"></span>

$$
\begin{aligned}
M_{\rm new}&=D,\\
\mathcal D\Psi_{\rm old}\mathcal D\bar\Psi_{\rm old}
&=\mathcal D\Psi_{\rm new}\mathcal D\bar\Psi_{\rm new}\,
 \mathcal J_\alpha,\\
\mathcal J_\alpha
&=\exp\!\left[-\frac{i n_Fg^2\alpha}{32\pi^2}
 \int d^4x\,\epsilon^{\mu\nu\rho\sigma}
 F^A_{\mu\nu}F^A_{\rho\sigma}\right],\\
\Delta\mathcal L
&=-\frac{\theta g^2}{64\pi^2}
 \epsilon^{\mu\nu\rho\sigma}F^A_{\mu\nu}F^A_{\rho\sigma}
 \qquad(n_F=2).
\end{aligned}
\tag{83.22}
$$

这里把常数轴转动分成连续小步；规范场不随轴转动改变，每步测度的指数直接相加，所以第77节的无穷小结果积分成所写的有限相位。第一行使质量变实，最后一行却在规范作用量中留下了原来的相位。因此轴变换已不是量子对称性；作为变量代换仍然可做，物理相位随之转移。[第94节](/posts/srednicki-94/#c94)讨论它的可观测效应。眼下研究保持宇称和时间反演的近似，取$\theta=0$及$M=D>0$。

要把微观质量项带入π介子的理论，可先把$M$当作随味群变换的外源，规定$M\to RML^\dagger$。这样$\operatorname{tr}_f(MU)$在形式上不变。赋予外参数这种变换律的办法称为伪场法（spurion method）：先以对称性限制允许的项，最后再把外源固定为实际质量矩阵。只含一次$M$、不含导数的项为
<span id="eq:c83-mass-spurion"></span>

$$
\mathcal L_{\rm mass}
=v^3\operatorname{tr}_f(MU+M^\dagger U^\dagger).
\tag{83.23}
$$

其系数可用微观质量插入来匹配：对$M$求变分，式[（83.20）](#eq:c83-quark-mass)给$-\Phi$，而上式给$v^3U$，恰好再现$\Phi_{\rm low}=-v^3U$。这也说明质量系数为何与凝聚相同。

此时可以解释凝聚的负号，而不必把它仅当作记号。先将无质量理论中的均匀取向写成$\langle\Phi\rangle=v^3\Omega$，$\Omega\in SU(2)$。由于$I$与$-I$都在这个群内，这个写法尚未选择正负。质量项不含时间导数，它对哈密顿量的贡献是拉氏量的负值，于是正质量所引起的一阶真空能为
<span id="eq:c83-vacuum-alignment"></span>

$$
\begin{aligned}
\mathcal E_M(\Omega)
&=2v^3\operatorname{Re}\operatorname{tr}_f(M\Omega)\\
&=2v^3\bigl(m_u\operatorname{Re}\Omega_{11}
            +m_d\operatorname{Re}\Omega_{22}\bigr)
 \ \geq\ -2v^3(m_u+m_d).
\end{aligned}
\tag{83.24}
$$

酉矩阵的每个对角元模长不超过一，所以有此下界；$\Omega=-I$达到下界。两质量都正时，达到下界还要求两个对角元均为$-1$，酉性再使非对角元为零。故小的正质量选择$\langle\Phi\rangle=-v^3I$。把其附近的取向写成$\Omega=-U$，就是前面采用的坐标。凝聚是否形成仍由强作用动力学决定，这个能量计算确定的是已形成凝聚的取向。

<span id="c83-gmor"></span>

## Gell-Mann–Oakes–Renner关系

在所选最低点$U=I$附近，线性π项在$U+U^\dagger$中相消。展开质量项到二次，依次使用实场乘积的对称性和泡利生成元的反对易关系：
<span id="eq:c83-mass-expansion"></span>

$$
\begin{aligned}
\mathcal L_{\rm mass}
&=2v^3\operatorname{tr}_fM
  -4v^3\operatorname{tr}_f(M\Pi^2)+O(M\Pi^4),\\
\mathcal L_{\rm mass}^{(2)}
&=-\frac{4v^3}{f_\pi^2}
   \operatorname{tr}_f(MT^aT^b)\pi^a\pi^b\\
&=-\frac{2v^3}{f_\pi^2}
   \operatorname{tr}_f\!\left(M\{T^a,T^b\}\right)\pi^a\pi^b\\
&=-\frac{v^3}{f_\pi^2}(m_u+m_d)\pi^a\pi^a .
\end{aligned}
\tag{83.25}
$$

第二到第三行用$\pi^a\pi^b=\pi^b\pi^a$把生成元乘积对称化，因而带来$1/2$；最后一行用$\{T^a,T^b\}=\delta^{ab}I/2$。与已经归一的实场质量项$-\frac12m_\pi^2\pi^a\pi^a$比较，可得
<span id="eq:c83-gmor"></span>

$$
\begin{aligned}
B_0&\equiv\frac{2v^3}{f_\pi^2},\qquad
m_\pi^2=B_0(m_u+m_d),\\
f_\pi^2m_\pi^2
&=-(m_u+m_d)\langle\bar u u\rangle_0
 =-(m_u+m_d)\langle\bar d d\rangle_0 .
\end{aligned}
\tag{83.26}
$$

这里下标0表示共同手征极限中的每味凝聚，均为$-2v^3$。这就是Gell-Mann–Oakes–Renner关系。$B_0$有质量量纲一，右边因而确为质量平方；正夸克质量与所选负凝聚给出正$m_\pi^2$。当两质量一起趋于零，π介子恢复为无质量戈德斯通玻色子。

凝聚是重整化复合算符，夸克质量也是方案相关参数；二者必须在同一方案与尺度下使用。质量与标量密度相互共轭：若有限重定义将质量改为$m_q'=Z_m m_q$，微观质量项不变要求对应密度改为$(\bar q q)'=Z_m^{-1}\bar q q$。因此
<span id="eq:c83-mass-condensate-running"></span>

$$
m_q'\langle(\bar q q)'\rangle
=m_q\langle\bar q q\rangle,\qquad
m_q'v'^3=m_qv^3 .
\tag{83.27}
$$

质量与凝聚的方案依赖在乘积中抵消。在所用手征阶，$f_\pi$也是有效理论的共同常数；更高阶会同时修正质量关系、凝聚及衰变常数之间的联系。

一个有用的结果是，即使$m_u\ne m_d$，这一阶三个π介子的质量仍相同。原因已包含在上面的反对易关系中：无迹质量差无法与$\delta^{ab}I$的迹相接。纯强作用的劈裂要到更高阶才出现，电磁作用则已使实际$\pi^\pm$略重于$\pi^0$。由于$B_0m_q$与$p^2$同阶，加入质量以后，应把一次质量插入也按两个软动量计数。这样导数展开与质量展开便合为同一个手征展开。

<span id="c83-three-flavors"></span>

## 加入奇夸克：八重态与中性混合

把奇夸克一起看作轻味，就将左右味群扩大为$SU(3)_L\times SU(3)_R$。取三味凝聚仍正比于单位矩阵，未破缺群为对角$SU(3)_V$，破缺方向共有$16-8=8$个。这八个赝戈德斯通玻色子对应三个π介子、四个$K$介子和一个η介子。以近似质量作比较，$\pi^0$为0.135 GeV、$\pi^\pm$为0.140 GeV，$K^\pm$为0.494 GeV，$K^0,\bar K^0$为0.498 GeV，η为0.548 GeV。奇夸克质量较大，后五个粒子的质量也显著提高。

现在$T^a$取八个半Gell-Mann矩阵，仍有$\operatorname{tr}_f(T^aT^b)=\delta^{ab}/2$。把实场组合为带确定电荷的场：
<span id="eq:c83-meson-matrix"></span>

$$
\begin{aligned}
\Pi&=\frac{\mathsf P}{2f_\pi},\\
\mathsf P&=
\begin{pmatrix}
\pi_3+\eta_8/\sqrt3&\sqrt2\,\pi^+&\sqrt2\,K^+\\
\sqrt2\,\pi^-&-\pi_3+\eta_8/\sqrt3&\sqrt2\,K^0\\
\sqrt2\,K^-&\sqrt2\,\bar K^0&-2\eta_8/\sqrt3
\end{pmatrix}.
\end{aligned}
\tag{83.28}
$$

例如$\pi^\pm=(\pi^1\mp i\pi^2)/\sqrt2$；$(\pi^+)^\dagger=\pi^-$，其它非对角元也两两共轭。矩阵是厄米无迹的，故恰有八个实自由度。先以$\pi_3,\eta_8$表示两种对角场，因为质量差会使它们混合，尚不能直接当作质量本征态。共同轴单态不在这个无迹矩阵内，它没有无反常对称性所保证的轻质量。

下面把三味质量计算所需的矩阵乘法与归一一并展开。双导数项到二次为$-\frac14\operatorname{tr}_f(\partial^\mu\mathsf P\partial_\mu\mathsf P)$。每对非对角元在迹中出现两次，而两个对角实场的交叉项相消，得到
<span id="eq:c83-meson-kinetic"></span>

$$
\begin{aligned}
\mathcal L_{\rm kin}^{(2)}
={}&-\partial^\mu\pi^+\partial_\mu\pi^-
    -\partial^\mu K^+\partial_\mu K^-
    -\partial^\mu K^0\partial_\mu\bar K^0\\
&-\frac12\partial^\mu\pi_3\partial_\mu\pi_3
 -\frac12\partial^\mu\eta_8\partial_\mu\eta_8 .
\end{aligned}
\tag{83.29}
$$

所以复场质量项应与$-m^2\phi^\dagger\phi$比较，实场则与$-\frac12m^2\phi^2$比较。三味的最低阶有效作用仍用式[（83.12）](#eq:c83-two-derivative-action)及[（83.23）](#eq:c83-mass-spurion)，此处$f_\pi,v$理解为三味共同的低能参数。令$M=\operatorname{diag}(m_u,m_d,m_s)$，有$\mathcal L_{\rm mass}^{(2)}=-(v^3/f_\pi^2)\operatorname{tr}_f(M\mathsf P^2)$。逐行与逐列相乘，迹就是
<span id="eq:c83-three-flavor-trace"></span>

$$
\begin{aligned}
\operatorname{tr}_f(M\mathsf P^2)
={}&m_u\left[(\pi_3+\eta_8/\sqrt3)^2
                    +2\pi^+\pi^-+2K^+K^-\right]\\
&+m_d\left[(-\pi_3+\eta_8/\sqrt3)^2
                    +2\pi^+\pi^-+2K^0\bar K^0\right]\\
&+m_s\left[\frac43\eta_8^2
                    +2K^+K^-+2K^0\bar K^0\right].
\end{aligned}
\tag{83.30}
$$

由三个复场的系数立即读得六个粒子的质量：
<span id="eq:c83-charged-meson-masses"></span>

$$
\begin{gathered}
m_{\pi^\pm}^2=B_0(m_u+m_d),\qquad
m_{K^\pm}^2=B_0(m_u+m_s),\\
m_{K^0}^2=m_{\bar K^0}^2=B_0(m_d+m_s),
\qquad B_0=\frac{2v^3}{f_\pi^2}.
\end{gathered}
\tag{83.31}
$$

每个非对角场连接两种味，质量平方相应包含这两种夸克质量之和。剩下的对角场则同时涉及三个质量。将式[（83.30）](#eq:c83-three-flavor-trace)中的平方展开，得到
<span id="eq:c83-neutral-mass-matrix"></span>

$$
\begin{aligned}
\mathcal L_{\rm neutral}^{(2)}
&=-\frac12
  \begin{pmatrix}\pi_3&\eta_8\end{pmatrix}
  \mathsf M^2
  \begin{pmatrix}\pi_3\\\eta_8\end{pmatrix},\\
\mathsf M^2
&=B_0
\begin{pmatrix}
m_u+m_d&(m_u-m_d)/\sqrt3\\
(m_u-m_d)/\sqrt3&(m_u+m_d+4m_s)/3
\end{pmatrix}.
\end{aligned}
\tag{83.32}
$$

混合系数的号随$m_u-m_d$改变。在同位旋极限，它为零；离开这个极限，便须对角化整个二次型。

记$S=m_u+m_d$、$\delta=m_u-m_d$及$Q=2m_s-S$。质量层级$m_{u,d}\ll m_s$使$Q>0$。两对角元的平均为$2B_0(S+m_s)/3$，它们差的一半为$B_0Q/3$，非对角元为$B_0\delta/\sqrt3$。特征方程的两个根及对应旋转于是为
<span id="eq:c83-neutral-eigenstates"></span>

$$
\begin{gathered}
m_{\pi^0,\eta}^2
=\frac{B_0}{3}
 \left[2(S+m_s)\mp\sqrt{Q^2+3\delta^2}\right],\\
\begin{pmatrix}\pi^0\\\eta\end{pmatrix}
=
\begin{pmatrix}
\cos\vartheta&-\sin\vartheta\\
\sin\vartheta&\cos\vartheta
\end{pmatrix}
\begin{pmatrix}\pi_3\\\eta_8\end{pmatrix},
\qquad
\tan2\vartheta=\frac{\sqrt3\,\delta}{Q}.
\end{gathered}
\tag{83.33}
$$

角度选取$\delta\to0$时$\vartheta\to0$的支。将旋转矩阵代入二次型，其非对角元为$B\cos2\vartheta-(D-A)\sin2\vartheta/2$，这里$A,D$是原对角元、$B$是原混合元；令它为零便给出所列正切。这既确定混合角，也确定了轻态中$\eta_8$分量的号。

为按轻重质量比展开，把根号写成$Q\sqrt{1+3\delta^2/Q^2}$，再按$\delta/Q$展开：
<span id="eq:c83-neutral-hierarchy"></span>

$$
\begin{aligned}
m_{\pi^0}^2
&=B_0S-\frac{B_0\delta^2}{2Q}
 +O\!\left(\frac{B_0\delta^4}{Q^3}\right),\\
m_\eta^2
&=\frac{B_0}{3}(S+4m_s)+\frac{B_0\delta^2}{2Q}
 +O\!\left(\frac{B_0\delta^4}{Q^3}\right).
\end{aligned}
\tag{83.34}
$$

两态相互排斥，轻态下降而重态上升；迹保持不变。首个移位为$O(B_0m_{\rm light}^2/m_s)$，其中$m_{\rm light}=\max(m_u,m_d)$，是这一层级近似中要略去的阶。保留更低阶以后，八个质量平方整理如下：

| 粒子                | 数目 | $m_{u,d}\ll m_s$时所保留的质量平方 |
| ------------------- | ---: | ---------------------------------- |
| $\pi^+,\pi^-,\pi^0$ |    3 | $B_0(m_u+m_d)$                     |
| $K^+,K^-$           |    2 | $B_0(m_u+m_s)$                     |
| $K^0,\bar K^0$      |    2 | $B_0(m_d+m_s)$                     |
| $\eta$              |    1 | $B_0(m_u+m_d+4m_s)/3$              |

在$m_u=m_d=m$时，混合严格消失。这时令$m_K^2=B_0(m+m_s)$，还可消去两个夸克质量，得到
<span id="eq:c83-octet-mass-relation"></span>

$$
3m_\eta^2+m_\pi^2
=B_0(2m+4m_s)+2B_0m
=4m_K^2 .
\tag{83.35}
$$

这条八重态质量关系展示了同一低能作用量对不同粒子的联系。全部夸克质量趋零时，整个质量矩阵也归零，恢复八个戈德斯通玻色子。实际三味理论还存在高阶质量项、圈修正和电磁效应；这些效应应加到质量矩阵之后再比较观测值。式[（83.33）](#eq:c83-neutral-eigenstates)的平方根只对这里保留的最低阶矩阵作了完整对角化。

<span id="c83-nucleons"></span>

## 核子的手征拉氏量

回到两味理论。除了π介子，低能强作用还需要描述质子和中子，以及它们与π介子的相互作用。核子在夸克质量趋零时仍有强作用产生的质量。有效作用量中的质量项因而要与已选择的凝聚取向一起实现手征对称性。

把质子和中子组成狄拉克二重态$N=(p,n)^T$，并选用如下变换规律：
<span id="eq:c83-nucleon-chiral-transform"></span>

$$
N_L=P_LN\longmapsto LN_L,\qquad
N_R=P_RN\longmapsto RN_R,\qquad
P_{L,R}=\frac{1\mp\gamma_5}{2}.
\tag{83.36}
$$

标准动能分别连接同一手征部分，因而不变；$\bar NN=\bar N_RN_L+\bar N_LN_R$却连接独立旋转的左右味指标。由$U^\dagger\to RU^\dagger L^\dagger$，可用$U^\dagger$把第一个双线性中的两套指标接起来，另一个用其伴随，得到
<span id="eq:c83-nucleon-invariant-mass"></span>

$$
\begin{aligned}
\mathcal L_{N,\rm mass}
&=-m_N\left(\bar N_RU^\dagger N_L+\bar N_LUN_R\right)\\
&=-m_N\bar N(U^\dagger P_L+UP_R)N .
\end{aligned}
\tag{83.37}
$$

例如第一项变成$\bar N_RR^\dagger(RU^\dagger L^\dagger)LN_L$，中间矩阵两两相消。这里$m_N$是手征极限的核子质量，和凝聚一样由非微扰强作用确定。

再考虑含一个导数的核子双线性。$U\partial_\mu U^\dagger$按左味群共轭变换，$U^\dagger\partial_\mu U$按右味群共轭变换，因此可分别接到左、右核子流上。宇称交换这两部分，要求它们以相同系数组合。把这个独立实系数写成$g_A-1$，于是所用的拉氏量为
<span id="eq:c83-linear-nucleon-action"></span>

$$
\begin{aligned}
\mathcal L_N
={}&i\bar N\gamma^\mu\partial_\mu N
 -m_N\bar N(U^\dagger P_L+UP_R)N\\
&-\frac{i}{2}(g_A-1)\bar N\gamma^\mu
 \left(U\partial_\mu U^\dagger P_L
       +U^\dagger\partial_\mu U P_R\right)N .
\end{aligned}
\tag{83.38}
$$

导数矩阵反厄米，前面的$i$使系数与厄米作用量相容。这个作用量保留了眼下所需的核子双线性和最低导数项；多核子接触项及显式夸克质量修正各有另外的系数。$g_A$称为轴矢量耦合，可由中子弱衰变测定，以下取示例值$g_A=1.27$。对称性允许这个常数，却不固定其值。下面的场重定义将给出轴耦合的总系数$g_A$。

<span id="c83-redefinition"></span>

## 将凝聚取向移入导数耦合

在$U=I$附近取光滑平方根$u=e^{i\Pi}$，所以$U=u^2$。让核子的左右分量各吸收一半π场转动，定义
<span id="eq:c83-nucleon-redefinition"></span>

$$
\begin{aligned}
\mathcal N&=(u^\dagger P_L+uP_R)N,\qquad
N=\mathscr B\mathcal N,\\
\mathscr B&=uP_L+u^\dagger P_R,\qquad
\mathscr B^{-1}=\mathscr B^\dagger
 =u^\dagger P_L+uP_R .
\end{aligned}
\tag{83.39}
$$

酉性与$P_LP_R=0$给出所列逆矩阵；在所选平方根坐标片上，这是局部可逆的场重定义。

进行代换时，狄拉克伴随也须一起算。$u$作用于味空间，与伽马矩阵对易，而$\gamma^0P_L\gamma^0=P_R$，所以
<span id="eq:c83-redefined-adjoint"></span>

$$
\begin{aligned}
\bar N
&=\bar{\mathcal N}\gamma^0\mathscr B^\dagger\gamma^0
 =\bar{\mathcal N}\mathscr B,\\
\mathscr B\gamma^\mu
&=\gamma^\mu\mathscr B^{-1},\qquad
\mathscr B\gamma^\mu\mathscr B=\gamma^\mu .
\end{aligned}
\tag{83.40}
$$

第一行右边仍是$\mathscr B$，因为取伴随和交换左右投影同时发生。利用这个结果，质量项中的矩阵完全消去：
<span id="eq:c83-redefined-mass"></span>

$$
\begin{aligned}
\mathscr B(U^\dagger P_L+UP_R)\mathscr B
&=u(u^\dagger)^2uP_L+u^\dagger u^2u^\dagger P_R\\
&=P_L+P_R=I,\\
\mathcal L_{N,\rm mass}&=-m_N\bar{\mathcal N}\mathcal N .
\end{aligned}
\tag{83.41}
$$

随位置变化的π场现在包含在$\mathscr B$中，导数作用于$\mathscr B$时会产生相互作用。

为计算这些项，记两个反厄米矩阵$X_\mu=u^\dagger\partial_\mu u$、$Y_\mu=u\partial_\mu u^\dagger$，再定义它们的厄米和、差：
<span id="eq:c83-vector-axial-connections"></span>

$$
\begin{aligned}
v_\mu&=\frac{i}{2}(X_\mu+Y_\mu)
 =\frac{i}{2}\left(u^\dagger\partial_\mu u
                   +u\partial_\mu u^\dagger\right),\\
a_\mu&=\frac{i}{2}(X_\mu-Y_\mu)
 =\frac{i}{2}\left(u^\dagger\partial_\mu u
                   -u\partial_\mu u^\dagger\right),\\
i\mathscr B^{-1}\partial_\mu\mathscr B
&=i(X_\mu P_L+Y_\mu P_R)=v_\mu-a_\mu\gamma_5 .
\end{aligned}
\tag{83.42}
$$

例如$\partial_\mu(u^\dagger u)=0$给$X_\mu^\dagger=-X_\mu$，另一矩阵同理；故$v_\mu^\dagger=v_\mu$、$a_\mu^\dagger=a_\mu$。它们各含一个导数，质量量纲为一。导数同时作用于$\mathscr B$和新核子场，便有
<span id="eq:c83-redefined-kinetic"></span>

$$
\begin{aligned}
i\bar N\gamma^\mu\partial_\mu N
={}&i\bar{\mathcal N}\gamma^\mu\partial_\mu\mathcal N\\
&+i\bar{\mathcal N}\gamma^\mu
      (\mathscr B^{-1}\partial_\mu\mathscr B)\mathcal N\\
={}&i\bar{\mathcal N}\gamma^\mu\partial_\mu\mathcal N\\
&+\bar{\mathcal N}\gamma^\mu v_\mu\mathcal N
 -\bar{\mathcal N}\gamma^\mu a_\mu\gamma_5\mathcal N .
\end{aligned}
\tag{83.43}
$$

原动能已经产生一个系数为$-1$的轴矢量耦合。还要把式[（83.38）](#eq:c83-linear-nucleon-action)的最后一项变换过来。

令$K_\mu=U\partial_\mu U^\dagger P_L+U^\dagger\partial_\mu U P_R$。由式[（83.40）](#eq:c83-redefined-adjoint)，其中的味矩阵变为$\mathscr B^{-1}K_\mu\mathscr B$。逐个手征块计算，并对$U=u^2$使用乘积法则：
<span id="eq:c83-redefined-extra-coupling"></span>

$$
\begin{aligned}
u^\dagger(U\partial_\mu U^\dagger)u
&=u\left[(\partial_\mu u^\dagger)u^\dagger
            +u^\dagger(\partial_\mu u^\dagger)\right]u\\
&=u\partial_\mu u^\dagger+(\partial_\mu u^\dagger)u
 =Y_\mu-X_\mu,\\
u(U^\dagger\partial_\mu U)u^\dagger
&=u^\dagger\left[(\partial_\mu u)u
                 +u(\partial_\mu u)\right]u^\dagger\\
&=u^\dagger\partial_\mu u+(\partial_\mu u)u^\dagger
 =X_\mu-Y_\mu,\\
\mathscr B^{-1}K_\mu\mathscr B
&=(Y_\mu-X_\mu)P_L+(X_\mu-Y_\mu)P_R\\
&=(X_\mu-Y_\mu)\gamma_5=-2ia_\mu\gamma_5 .
\end{aligned}
\tag{83.44}
$$

因此原系数$-\frac{i}{2}(g_A-1)$乘以$-2i$后成为$-(g_A-1)$。与动能中的$-1$相加，轴耦合总系数为$-g_A$。所有项合起来，得到
<span id="eq:c83-nonlinear-nucleon-action"></span>

$$
\begin{aligned}
\mathcal L_N
={}&i\bar{\mathcal N}\gamma^\mu\partial_\mu\mathcal N
 -m_N\bar{\mathcal N}\mathcal N
 +\bar{\mathcal N}\gamma^\mu v_\mu\mathcal N\\
&-g_A\bar{\mathcal N}\gamma^\mu a_\mu\gamma_5\mathcal N .
\end{aligned}
\tag{83.45}
$$

这个形式与原作用量通过矩阵恒等式相等，尚不需要使用核子运动方程。

为找出最低π数的顶角，再将式[（83.13）](#eq:c83-exponential-differential)用于$u=e^{i\Pi}$。和先前的$U=e^{2i\Pi}$相比，此处指数中的2已消失，故
<span id="eq:c83-connections-expansion"></span>

$$
\begin{aligned}
X_\mu
&=i\partial_\mu\Pi+\frac12[\Pi,\partial_\mu\Pi]
 -\frac{i}{6}[\Pi,[\Pi,\partial_\mu\Pi]]+\cdots,\\
Y_\mu
&=-i\partial_\mu\Pi+\frac12[\Pi,\partial_\mu\Pi]
 +\frac{i}{6}[\Pi,[\Pi,\partial_\mu\Pi]]+\cdots,\\
v_\mu&=\frac{i}{2}[\Pi,\partial_\mu\Pi]+\cdots,\\
a_\mu&=-\partial_\mu\Pi
 +\frac16[\Pi,[\Pi,\partial_\mu\Pi]]+\cdots .
\end{aligned}
\tag{83.46}
$$

$v_\mu$从两个π场开始，$a_\mu$从一个π场开始。单π相互作用因而完全来自轴项，其负号与$a_\mu$首项的负号相消，给出
<span id="eq:c83-derivative-pion-nucleon"></span>

$$
\mathcal L_{\pi\mathcal N\mathcal N}^{(1)}
=\frac{g_A}{f_\pi}\partial_\mu\pi^a\,
 \bar{\mathcal N}T^a\gamma^\mu\gamma_5\mathcal N .
\tag{83.47}
$$

相互作用随π动量趋零而减弱，和戈德斯通场描述缓慢取向变化的性质一致。虽然新变量的质量项中没有π场，导数项已经完整保留了它的单π耦合。

### 新变量中的对称性

新核子$\mathcal N$的质量项具有通常形式，却仍与完整手征对称性相容。要看出这一点，令$u'$为变换后$U'=LUR^\dagger$的局部平方根，并定义
<span id="eq:c83-compensating-rotation"></span>

$$
\begin{aligned}
h&=u'^\dagger Lu=u'Ru^\dagger,\qquad h^\dagger h=I,\\
u'&=Luh^\dagger=huR^\dagger,\qquad
\mathcal N'=h\mathcal N .
\end{aligned}
\tag{83.48}
$$

两个$h$的表达式相等，可由$u'^2=Lu^2R^\dagger$左乘$u'^\dagger$、右乘$Ru^\dagger$得到。将$N_L'=LN_L$与$N_R'=RN_R$分别代入新场定义，左右分量都产生同一个$h$。它一般依赖π场及位置；当$L=R$时，则退化为通常的同位旋转动。

求$X_\mu'$时用$u'=Luh^\dagger$，求$Y_\mu'$时用$u'=huR^\dagger$，乘积法则分别给出
<span id="eq:c83-connection-transform"></span>

$$
\begin{aligned}
X_\mu'&=hX_\mu h^\dagger+h\partial_\mu h^\dagger,\qquad
Y_\mu'=hY_\mu h^\dagger+h\partial_\mu h^\dagger,\\
v_\mu'&=hv_\mu h^\dagger+ih\partial_\mu h^\dagger,\qquad
a_\mu'=ha_\mu h^\dagger,\\
(\partial_\mu-iv_\mu')\mathcal N'
&=h(\partial_\mu-iv_\mu)\mathcal N .
\end{aligned}
\tag{83.49}
$$

最后一行中$\partial_\mu h$与$h(\partial_\mu h^\dagger)h=-\partial_\mu h$相消。所以$v_\mu$将位置依赖的同位旋旋转接入导数，$a_\mu$则作齐次变换；式[（83.45）](#eq:c83-nonlinear-nucleon-action)的各项都保持不变。这称为手征对称性的非线性实现（nonlinear realization）：群在$\mathcal N$上的作用含有π场，但其物理内容与原变量相同。

这些核子耦合还保持宇称和时间反演。宇称的时空作用与平方根场变换为

$$
\mathcal P=\operatorname{diag}(1,-1,-1,-1),\qquad
u(x)\ \xrightarrow{P}\ u^\dagger(\mathcal Px).
$$

于是$X_\mu$与$Y_\mu$交换，并带上导数指标的$\mathcal P$，有
<span id="eq:c83-parity-connections"></span>

$$
v_\mu(x)\ \xrightarrow{P}\
 \mathcal P_\mu{}^\nu v_\nu(\mathcal Px),\qquad
a_\mu(x)\ \xrightarrow{P}\
 -\mathcal P_\mu{}^\nu a_\nu(\mathcal Px).
\tag{83.50}
$$

第40节已算过$\bar{\mathcal N}\gamma^\mu T^a\mathcal N$与$\bar{\mathcal N}\gamma^\mu\gamma_5T^a\mathcal N$的宇称，分别是矢量与轴矢量。它们与$v_\mu^a,a_\mu^a$收缩后都为宇称偶。

时间反演还要对显式的$i$和味矩阵取复共轭。沿[第40节](/posts/srednicki-40/#c40-bilinear-time)，记$\mathcal T=\operatorname{diag}(-1,1,1,1)$，并用$(T^a)^*=\rho_aT^a$，其中$\rho_1=\rho_3=1$、$\rho_2=-1$。π场是相应的赝标量味三重态，故
<span id="eq:c83-time-connections"></span>

$$
\begin{aligned}
T^{-1}\pi^a(x)T
&=-\rho_a\pi^a(\mathcal Tx)
 \quad\hbox{（不对$a$求和）},\\
T^{-1}\Pi(x)T&=-\Pi(\mathcal Tx),\qquad
T^{-1}u(x)T=u(\mathcal Tx),\\
(v_\mu^a,a_\mu^a)(x)
&\xrightarrow{T}
 -\rho_a\mathcal T_\mu{}^\nu
   (v_\nu^a,a_\nu^a)(\mathcal Tx),\\
(J_V^{a\mu},J_A^{a\mu})(x)
&\xrightarrow{T}
 -\rho_a\mathcal T^\mu{}_\nu
   (J_V^{a\nu},J_A^{a\nu})(\mathcal Tx).
\end{aligned}
\tag{83.51}
$$

这里$J_V,J_A$就是上段的两种核子流。第二行先将$\pi^a$与$T^a$同时变换，两次$\rho_a$相消；再用$i\to-i$，指数$u=e^{i\Pi}$便不变号。由$v_\mu,a_\mu$定义，显式的$i$使完整味矩阵各得$-\mathcal T_\mu{}^\nu$；将结果重新分解到$T^a$上，才得到第三行。最后一行来自第40节的旋量双线性变换，再乘味矩阵的$\rho_a$。两个因子收缩时$\rho_a^2=1$，两个负号也相消，因此两个耦合都是时间反演偶。

<span id="c83-goldberger"></span>

## 在壳核子与Goldberger–Treiman关系

单π导数耦合通常称为赝矢量耦合。核子外腿在壳时，可以将它改写成更熟悉的赝标量耦合。为说明适用的位置，先考虑两条外核子线在单π顶角处的矩阵元；这些外线服从自由狄拉克方程。沿既定的伽马约定，
<span id="eq:c83-external-nucleon-equations"></span>

$$
(i\gamma^\mu\partial_\mu-m_N)\mathcal N=0,\qquad
i(\partial_\mu\bar{\mathcal N})\gamma^\mu
   +m_N\bar{\mathcal N}=0 .
\tag{83.52}
$$

第二式可由第一式取狄拉克伴随得到，也可对自由作用量独立变分得到。它给$(\partial_\mu\bar{\mathcal N})\gamma^\mu=im_N\bar{\mathcal N}$，而第一式给$\gamma^\mu\partial_\mu\mathcal N=-im_N\mathcal N$。于是轴流的散度为
<span id="eq:c83-nucleon-axial-divergence"></span>

$$
\begin{aligned}
&\partial_\mu
 \left(\bar{\mathcal N}T^a\gamma^\mu\gamma_5\mathcal N\right)
\\
&\quad=(\partial_\mu\bar{\mathcal N})\gamma^\mu
       T^a\gamma_5\mathcal N
 +\bar{\mathcal N}T^a\gamma^\mu\gamma_5
       \partial_\mu\mathcal N\\
&\quad=im_N\bar{\mathcal N}T^a\gamma_5\mathcal N
 -\bar{\mathcal N}T^a\gamma_5
       (\gamma^\mu\partial_\mu\mathcal N)\\
&\quad=2im_N\bar{\mathcal N}T^a\gamma_5\mathcal N .
\end{aligned}
\tag{83.53}
$$

第二行将$\gamma_5$越过$\gamma^\mu$，反对易负号使两条核子腿各贡献同一个$im_N$。

现在对式[（83.47）](#eq:c83-derivative-pion-nucleon)作分部积分。散射波包的边界项消失，把上式用于外腿矩阵元，便得到
<span id="eq:c83-goldberger-treiman"></span>

$$
\begin{aligned}
\frac{g_A}{f_\pi}\partial_\mu\pi^aJ_A^{a\mu}
&\doteq-\frac{g_A}{f_\pi}\pi^a\partial_\mu J_A^{a\mu}\\
&\doteq-\frac{2ig_Am_N}{f_\pi}\pi^a
       \bar{\mathcal N}T^a\gamma_5\mathcal N\\
&=-ig_{\pi NN}\pi^a
       \bar{\mathcal N}\sigma^a\gamma_5\mathcal N,
\qquad
g_{\pi NN}=\frac{g_Am_N}{f_\pi}.
\end{aligned}
\tag{83.54}
$$

符号$\doteq$在这里表示除去全导数、并取上述在壳核子矩阵元后的等价。最后一行用$T^a=\sigma^a/2$消去了轴流散度中的2。π腿没有用到运动方程，所以可以离壳，这正适用于π交换的核子散射。若核子本身处在内线上，就应保留原导数作用量或一并变换由场重定义产生的其它顶角。

$\bar{\mathcal N}\sigma^a\gamma_5\mathcal N$是反厄米双线性，因为取狄拉克伴随时$\gamma^0\gamma_5\gamma^0=-\gamma_5$；前面的$-i$因而使相互作用厄米。耦合$g_{\pi NN}$没有量纲，所求比例的质量量纲也相互抵消。

这个结果称为Goldberger–Treiman关系。为作数值比较，以实际核子质量约0.939 GeV代入手征极限参数的位置，得到
<span id="eq:c83-goldberger-estimate"></span>

$$
g_{\pi NN}\simeq
\frac{1.27\times0.939}{0.0924}=12.906\ldots .
\tag{83.55}
$$

以中译本引用的π交换散射分析值$g_{\pi NN}=13.5$作比较，两者相差约4.4%。这个比较用实际核子质量近似$m_N$；夸克质量、较高导数项及圈修正会改变最低阶关系。弱衰变给出的$g_A,f_\pi$与强散射给出的π核子耦合能够如此接近，正体现了手征对称性对不同低能过程的共同约束。

<span id="c83-pipi-scattering"></span>

## ππ散射：三个味通道

现在用双导数拉氏量和最低阶质量项计算ππ散射。以下令 $f=f_\pi$、$M=mI$，采用 $(-+++)$ 度规。先把四条腿都指向顶角外，记其味指标为 $(a_1,a_2,a_3,a_4)=(a,b,c,d)$、动量为 $k_1,\ldots,k_4$，于是 $\sum_jk_j=0$。物理入射动量 $P_1,P_2$ 对应 $k_1=-P_1,k_2=-P_2$，出射动量直接取 $k_3=P_3,k_4=P_4$。沿既定定义，顶角给出的是 $i\mathcal T$，动量守恒的 $(2\pi)^4\delta^4(\sum k_j)$ 另列。

我们只需找出作用量中的四场项。由于动能和实质量项在 $U\leftrightarrow U^\dagger$，即 $\pi\mapsto-\pi$ 下不变，没有三π顶角，所以本阶四点树图就是一个局域四价顶角。导数四场项已在式[（83.17）](#eq:c83-four-pion-lagrangian)中求出；质量四场项还要从式[（83.23）](#eq:c83-mass-spurion)展开。

令 $r^2=\pi^a\pi^a$。泡利恒等式使 $(\pi^a\sigma^a)^2=r^2I$，因而
<span id="eq:c83-pipi-mass-expansion"></span>

$$
U=\cos(r/f)I+i\frac{\pi^a\sigma^a}{r}\sin(r/f),\qquad
\mathcal L_{\rm mass}=4mv^3\cos(r/f).
\tag{83.56}
$$

$r=0$ 处按连续极限理解。展开至 $r^4$，并用式[（83.26）](#eq:c83-gmor)在 $m_u=m_d=m$ 时的 $m_\pi^2=4mv^3/f^2$，得到
<span id="eq:c83-pipi-mass-quartic"></span>

$$
\mathcal L_{\rm mass}
=4mv^3-\frac12m_\pi^2\,\pi^a\pi^a
+\frac{m_\pi^2}{24f^2}(\pi^a\pi^a)^2+\cdots.
\tag{83.57}
$$

因此要使用的四场密度为
<span id="eq:c83-pipi-l4"></span>

$$
\begin{aligned}
\mathcal L_4={}&\frac1{6f^2}\left[
 \pi^r\pi^r(\partial_\mu\pi^s)(\partial^\mu\pi^s)
-\pi^r\pi^s(\partial_\mu\pi^s)(\partial^\mu\pi^r)\right]\\
&+\frac{m_\pi^2}{24f^2}\pi^r\pi^r\pi^s\pi^s.
\end{aligned}
\tag{83.58}
$$

这里 $r,s$ 是求和的内部味指标。外态已经由标准二次动能归一，各外腿的树级约化因子为1。

计算顶角时，四个带标签的外场要分配到每个单项式的四个位置上，共有 $4!=24$ 次分配。对全部向外的动量，外场平面波取 $e^{-ik_jx}$，一个导数给 $-ik_{j\mu}$，两个导数的收缩给 $-k_j\cdot k_l$。戴森展开的一阶 $i\int d^4x\,\mathcal L_4$ 再提供一个共同的 $i$。若 $\sigma$ 遍历24个排列，这三部分的完整顶角可以先写成
<span id="eq:c83-pipi-permutations"></span>

$$
\begin{aligned}
iV_{D_1}
&=-\frac{i}{6f^2}\sum_{\sigma\in S_4}
 \delta_{a_{\sigma(1)}a_{\sigma(2)}}
 \delta_{a_{\sigma(3)}a_{\sigma(4)}}
 k_{\sigma(3)}\cdot k_{\sigma(4)},\\
iV_{D_2}
&=+\frac{i}{6f^2}\sum_{\sigma\in S_4}
 \delta_{a_{\sigma(1)}a_{\sigma(4)}}
 \delta_{a_{\sigma(2)}a_{\sigma(3)}}
 k_{\sigma(3)}\cdot k_{\sigma(4)},\\
iV_M
&=\frac{im_\pi^2}{24f^2}\sum_{\sigma\in S_4}
 \delta_{a_{\sigma(1)}a_{\sigma(2)}}
 \delta_{a_{\sigma(3)}a_{\sigma(4)}}.
\end{aligned}
\tag{83.59}
$$

第二行的正号是密度中的负号与两次导数的负号相乘的结果。所有外标签分配已包括在排列和中。

这24项可以按三个配对 $(12|34)$、$(13|24)$、$(14|23)$ 分组。先取 $\delta_{ab}\delta_{cd}$，即 $(12|34)$。在第一种导数单项式中，导数落在3、4上有 $2!\,2!=4$ 次分配，落在1、2上又有4次，因此它给
<span id="eq:c83-pipi-first-pair"></span>

$$
-\frac{i}{6f^2}\,4\,
 (k_1\cdot k_2+k_3\cdot k_4)\,\delta_{ab}\delta_{cd}.
\tag{83.60}
$$

在第二种单项式中，每一对同味场有一个带导数、一个不带导数。从 $\{1,2\}$ 和 $\{3,4\}$ 各选一个导数腿，共有四种选法；交换内部求和名 $r,s$ 再给一个2。因此这一部分为
<span id="eq:c83-pipi-cross-pair"></span>

$$
+\frac{i}{6f^2}\,2\,
 (k_1\cdot k_3+k_1\cdot k_4+k_2\cdot k_3+k_2\cdot k_4)
 \,\delta_{ab}\delta_{cd}.
\tag{83.61}
$$

每个单项式在这一味配对下都有8项，三个配对正好用完24项。质量单项式也有这8种分配，于是
<span id="eq:c83-pipi-mass-vertex"></span>

$$
iV_M=\frac{im_\pi^2}{3f^2}
 (\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}
 +\delta_{ad}\delta_{bc}).
\tag{83.62}
$$

将两个导数结果相加，再用 $\sum k_j=0$。定义 $s_{12}=-(k_1+k_2)^2$，就有
<span id="eq:c83-pipi-momentum-relations"></span>

$$
\begin{aligned}
(k_1+k_2)\cdot(k_3+k_4)&=s_{12},\\
k_1\cdot k_2+k_3\cdot k_4
&=-s_{12}-\frac12\sum_{j=1}^4k_j^2.
\end{aligned}
\tag{83.63}
$$

所以 $\delta_{ab}\delta_{cd}$ 前的导数系数等于
<span id="eq:c83-pipi-derivative-vertex"></span>

$$
\frac{i}{6f^2}
 \left[4s_{12}+2\sum_j k_j^2+2s_{12}\right]
=\frac{i}{f^2}\left(s_{12}+\frac13\sum_j k_j^2\right).
\tag{83.64}
$$

其它两个味配对只需将 $s_{12}$ 换成 $s_{13}$ 或 $s_{14}$。共同的 $\sum k_j^2/3$ 将在取壳后变成质量项。

现在取四条外腿在壳，$k_j^2=-m_\pi^2$，并引入物理曼德尔斯塔姆变量
<span id="eq:c83-pipi-mandelstam"></span>

$$
\begin{gathered}
s=-(P_1+P_2)^2=s_{12},\quad
t=-(P_1-P_3)^2=s_{13},\\
u=-(P_1-P_4)^2=s_{14},\qquad
s+t+u=4m_\pi^2.
\end{gathered}
\tag{83.65}
$$

导数顶角在 $s$ 配对下给 $i(s-4m_\pi^2/3)/f^2$，质量顶角给 $+im_\pi^2/(3f^2)$。二者相加便得到
<span id="eq:c83-pipi-amplitude"></span>

$$
\begin{aligned}
\mathcal T(\pi^a\pi^b\to\pi^c\pi^d)
=\frac1{f_\pi^2}\bigl[&\delta_{ab}\delta_{cd}(s-m_\pi^2)\\
&+\delta_{ac}\delta_{bd}(t-m_\pi^2)\\
&+\delta_{ad}\delta_{bc}(u-m_\pi^2)\bigr].
\end{aligned}
\tag{83.66}
$$

该式对任意两条完整外标签的交换保持玻色对称，动量通道和味配对同时交换。对于四个味指标全相同的情形，三个导数贡献的和为零，而总振幅为 $m_\pi^2/f_\pi^2$；这与单一π方向上余弦质量势的四阶项一致。手征极限 $m_\pi\to0$ 时，振幅只剩由动量产生的相互作用。

这是最低手征阶 $O(p^2)$ 的树级结果，$m_\pi^2$ 也计作 $O(p^2)$。四导数有效项和一圈修正进入下一手征阶；使用范围是动量和π质量均低于有效理论的失效尺度。末态同粒子的相空间因子在计算截面时另行加入。

<span id="c83-nucleon-mass-corrections"></span>

## 夸克质量对核子的修正

此前的核子拉氏量是在$m_u=m_d=0$时写下的；现在要找出一阶夸克质量怎样改变核子质量及π–核子相互作用。仍沿本节的强作用理论保留重子数$U(1)_V$，并把手征对称性的显式破缺全部放进质量矩阵$M$中。保留零导数、一个$M$或$M^\dagger$、一个$\bar N$和一个$N$的局域项。[第94章](/posts/srednicki-94/#c94)将使用这些项讨论质量相位的物理效应。

### 四个允许的质量结构

沿式[（83.23）](#eq:c83-mass-spurion)的伪场变换及式[（83.36）](#eq:c83-nucleon-chiral-transform)的核子变换，先保留一般的$M$和$M^\dagger$，最后再取实对角质量。

没有导数或其他洛伦兹指标时，核子双线性只需标量与赝标量两种。它们也可写成$\bar N_R\mathsf A N_L$及其厄米共轭；这里$\bar N_R=\bar NP_L$，故要求$\mathsf A\mapsto R\mathsf A L^\dagger$。为说明允许的味结构已经找全，在任一点用手征变换将$U$带到$I$。这时剩余的矢量$SU(2)$使$M$按共轭变换，而一个二乘二矩阵分解为单态与三重态：
<span id="eq:c83-mass-flavor-decomposition"></span>

$$
X=\frac{\operatorname{tr}X}{2}I+
  \left(X-\frac{\operatorname{tr}X}{2}I\right).
\tag{83.67}
$$

在每个不可约分量上，协变的线性映射只能乘一个常数。因此，线性依赖$M,M^\dagger$的味矩阵由$M$、$M^\dagger$、$I\operatorname{tr}M$、$I\operatorname{tr}M^\dagger$张成。将它们恢复到任意$U$，得到
<span id="eq:c83-mass-covariant-basis"></span>

$$
\mathsf A\ \in\operatorname{span}
\left\{
M,\ U^\dagger M^\dagger U^\dagger,\
U^\dagger\operatorname{tr}(MU),\
U^\dagger\operatorname{tr}(M^\dagger U^\dagger)
\right\}.
\tag{83.68}
$$

例如第二项变成$R(U^\dagger M^\dagger U^\dagger)L^\dagger$，而两个迹都是手征单态。$SU(2)$的不变反对称张量对任意二乘二矩阵满足$\epsilon X^T\epsilon^{-1}=(\operatorname{tr}X)I-X$，所以用它缩并出的矩阵仍在上述空间内。这里按固定场变量分类，尚未作运动方程约化。

还须施加宇称和厄米性。令
<span id="eq:c83-mass-chiral-building-blocks"></span>

$$
\begin{aligned}
\mathcal I_1&=\bar N_RMN_L,&
\mathcal I_2&=\bar N_RU^\dagger M^\dagger U^\dagger N_L,\\
t&=\operatorname{tr}(MU),&
\mathcal B_L&=\bar N_RU^\dagger N_L .
\end{aligned}
\tag{83.69}
$$

宇称同时交换$L,R$以及$U,U^\dagger$；对伪场则交换$M,M^\dagger$。于是$\mathcal I_1,\mathcal I_2,t\mathcal B_L,t^*\mathcal B_L$都分别变成自己的厄米共轭。先将每一项与其共轭相加，再要求宇称不变，四个系数便可取实数。把后两个系数写成$c_3+c_4$和$c_3-c_4$，并选择质量项通常使用的整体负号，结果为
<span id="eq:c83-mass-original-action"></span>

$$
\begin{aligned}
\delta\mathcal L_M={}&
-c_1\bar N(MP_L+M^\dagger P_R)N\\
&-c_2\bar N(U^\dagger M^\dagger U^\dagger P_L
                  +UMUP_R)N\\
&-c_3\operatorname{tr}(MU+M^\dagger U^\dagger)
       \bar N(U^\dagger P_L+UP_R)N\\
&-c_4\operatorname{tr}(MU-M^\dagger U^\dagger)
       \bar N(U^\dagger P_L-UP_R)N .
\end{aligned}
\tag{83.70}
$$

例如最后两行中$t\mathcal B_L$的系数为$-(c_3+c_4)$，而$t^*\mathcal B_L$的系数为$-(c_3-c_4)$，所以这个改写保留四个自由参数。$c_i$均无量纲，因为$[M]=1$、$[\bar NN]=3$。

最后一行的两个因子各是反厄米的，它们的乘积为厄米。具体地，迹的复共轭使其变号，而$\bar N(U^\dagger P_L-UP_R)N$取厄米共轭时也变号；宇称同样使这两个因子各变一次号。对实对角$M$，[正文的时间反演规律](/posts/srednicki-83/#c83-redefinition)给$T^{-1}U(x)T=U(\mathcal Tx)$：π场的变号和反幺正变换的$i\to-i$相消，味矩阵的复共轭也已包含在这条规律中。[第40章的双线性变换](/posts/srednicki-40/#c40-bilinear-time)说明，无导数的标量及不带显式$i$的$\gamma_5$双线性在时间反演下为偶，四个实系数的组合因此也为时间反演偶。若给固定的物理$M$加上不能消去的复相位，宇称、时间反演本身可以被破坏；伪场的构造仍然指定了该相位应进入的位置。

### 非线性变量中的质量项

使用式[（83.39）](#eq:c83-nucleon-redefinition)至[（83.40）](#eq:c83-redefined-adjoint)的$N=\mathscr B\mathcal N$、$\bar N=\bar{\mathcal N}\mathscr B$，原双线性中的矩阵从两边各乘$\mathscr B$。定义
<span id="eq:c83-mass-C-definition"></span>

$$
C=uMu,\qquad C^\dagger=u^\dagger M^\dagger u^\dagger .
\tag{83.71}
$$

第一个质量块的左手部分是$uMuP_L$；右手部分是$u^\dagger M^\dagger u^\dagger P_R$。第二个质量块则给相反的安排。例如其左手部分为
$uU^\dagger M^\dagger U^\dagger uP_L
=u^\dagger M^\dagger u^\dagger P_L$，这里只约去了相邻的$u$与$u^\dagger$。两个完整结果为
<span id="eq:c83-mass-two-blocks"></span>

$$
\begin{aligned}
\mathscr B(MP_L+M^\dagger P_R)\mathscr B
 &=CP_L+C^\dagger P_R,\\
\mathscr B(U^\dagger M^\dagger U^\dagger P_L+UMUP_R)\mathscr B
 &=C^\dagger P_L+CP_R .
\end{aligned}
\tag{83.72}
$$

两个迹项中的核子质量块可同样计算：
<span id="eq:c83-mass-trace-blocks"></span>

$$
\begin{aligned}
\mathscr B(U^\dagger P_L+UP_R)\mathscr B&=P_L+P_R=I,\\
\mathscr B(U^\dagger P_L-UP_R)\mathscr B&=P_L-P_R=-\gamma_5,\\
\operatorname{tr}(MU\pm M^\dagger U^\dagger)
 &=\operatorname{tr}(C\pm C^\dagger).
\end{aligned}
\tag{83.73}
$$

最后一行只用了迹的循环性，例如$\operatorname{tr}(Mu^2)=\operatorname{tr}(uMu)$；一般的$M$与$u$并不对易。

记$c_\pm=c_1\pm c_2$。用$P_L,P_R$的定义展开式[（83.72）](#eq:c83-mass-two-blocks)，两项中乘$I$的系数相加，乘$\gamma_5$的系数相减，得到
<span id="eq:c83-mass-nonlinear-action"></span>

$$
\begin{aligned}
\delta\mathcal L_M={}&
-\frac{c_+}{2}\bar{\mathcal N}(C+C^\dagger)\mathcal N
+\frac{c_-}{2}\bar{\mathcal N}(C-C^\dagger)\gamma_5\mathcal N\\
&-c_3\operatorname{tr}(C+C^\dagger)
        \bar{\mathcal N}\mathcal N
+c_4\operatorname{tr}(C-C^\dagger)
        \bar{\mathcal N}\gamma_5\mathcal N .
\end{aligned}
\tag{83.74}
$$

$c_4$前面的正号来自式[（83.73）](#eq:c83-mass-trace-blocks)中的$P_L-P_R=-\gamma_5$。同时，$\bar{\mathcal N}\gamma_5\mathcal N$是反厄米双线性；这再次说明它应乘反厄米的$C-C^\dagger$或其迹。

对实对角$M$展开至两个π场。两个指数分别位于$M$的两侧，因此
<span id="eq:c83-mass-pion-expansion"></span>

$$
\begin{aligned}
C&=M+i\{\Pi,M\}
 -\frac12\{\Pi^2,M\}-\Pi M\Pi+O(\Pi^3),\\
C^\dagger&=M-i\{\Pi,M\}
 -\frac12\{\Pi^2,M\}-\Pi M\Pi+O(\Pi^3),\\
C+C^\dagger&=2M-\{\Pi^2,M\}-2\Pi M\Pi+O(\Pi^4),\\
C-C^\dagger&=2i\{\Pi,M\}+O(\Pi^3).
\end{aligned}
\tag{83.75}
$$

其中$\Pi M\Pi$来自两个一次项相乘，两个π矩阵分别位于$M$的两侧。取迹后，
<span id="eq:c83-mass-trace-expansion"></span>

$$
\begin{aligned}
\operatorname{tr}(C+C^\dagger)
 &=2\operatorname{tr}M-4\operatorname{tr}(M\Pi^2)+O(\Pi^4),\\
\operatorname{tr}(C-C^\dagger)
 &=4i\operatorname{tr}(M\Pi)+O(\Pi^3).
\end{aligned}
\tag{83.76}
$$

这给出零π、一个π及两个π的质量诱导相互作用：
<span id="eq:c83-mass-pion-couplings"></span>

$$
\begin{aligned}
\delta\mathcal L_M^{(0)}={}&
-\bar{\mathcal N}\bigl[c_+M+2c_3\operatorname{tr}M\bigr]\mathcal N,\\
\delta\mathcal L_M^{(1)}={}&
i c_-\bar{\mathcal N}\{\Pi,M\}\gamma_5\mathcal N
+4i c_4\operatorname{tr}(M\Pi)
        \bar{\mathcal N}\gamma_5\mathcal N,\\
\delta\mathcal L_M^{(2)}={}&
\frac{c_+}{2}\bar{\mathcal N}
 \bigl(\{\Pi^2,M\}+2\Pi M\Pi\bigr)\mathcal N
+4c_3\operatorname{tr}(M\Pi^2)
        \bar{\mathcal N}\mathcal N .
\end{aligned}
\tag{83.77}
$$

零π项改变核子质量；奇数个π的项配赝标量双线性，偶数个π的项配标量双线性，正好保留宇称。特别是令$m_\pm=(m_u\pm m_d)/2$，则$M=m_+I+m_-\sigma^3$，泡利矩阵的反对易式给
<span id="eq:c83-mass-isospin-pion-coupling"></span>

$$
\begin{gathered}
\{\Pi,M\}=\frac1{f_\pi}
 (m_+\pi^a\sigma^a+m_-\pi^3I),\qquad
\operatorname{tr}(M\Pi)=\frac{m_-\pi^3}{f_\pi},\\
\delta\mathcal L_M^{(1)}
=\frac{i}{f_\pi}\bar{\mathcal N}
 \bigl[c_-m_+\pi^a\sigma^a+(c_-+4c_4)m_-\pi^3I\bigr]
 \gamma_5\mathcal N .
\end{gathered}
\tag{83.78}
$$

所以即使质量差只测得$c_+$，其他组合仍在π–核子顶角中起作用。这里保留$O(M)$及至多两个π场。

同一重定义也可以围绕任意常数真空$U_0$进行。为把顺序说明清楚，取$u_0^2=U_0$并写
<span id="eq:c83-mass-shifted-vacuum-order"></span>

$$
\begin{gathered}
U=u_0u^2u_0,\qquad
N=\mathscr B_0\mathcal N,\qquad
\mathscr B_0=u_0uP_L+u_0^\dagger u^\dagger P_R,\\
\overline{\mathscr B}_0
=\gamma^0\mathscr B_0^\dagger\gamma^0
=uu_0P_L+u^\dagger u_0^\dagger P_R,\\
Q=u_0Mu_0,\qquad C_0=uQu .
\end{gathered}
\tag{83.79}
$$

按上述次序逐个手征块相乘，得到
<span id="eq:c83-mass-shifted-blocks"></span>

$$
\begin{aligned}
\overline{\mathscr B}_0(MP_L+M^\dagger P_R)\mathscr B_0
 &=C_0P_L+C_0^\dagger P_R,\\
\overline{\mathscr B}_0
(U^\dagger M^\dagger U^\dagger P_L+UMUP_R)\mathscr B_0
 &=C_0^\dagger P_L+C_0P_R,\\
\overline{\mathscr B}_0(U^\dagger P_L\pm UP_R)\mathscr B_0
 &=P_L\pm P_R .
\end{aligned}
\tag{83.80}
$$

例如第一行左手块就是$uu_0Mu_0u$，而第二行左手块中相邻的$u_0u_0^\dagger$及$uu^\dagger$依次约去，剩下$u^\dagger u_0^\dagger M^\dagger u_0^\dagger u^\dagger=C_0^\dagger$。此外$\operatorname{tr}(MU)=\operatorname{tr}(Qu^2)=\operatorname{tr}C_0$，故式[（83.74）](#eq:c83-mass-nonlinear-action)只需将$C$换成$C_0$。若选用对角$M,u_0$，才可进一步写$Q=MU_0$；这个简化不用于一般不对易的质量伪场。

### 用介子与核子质量作匹配

在$M>0$的真空取$u=I$。此时$C-C^\dagger=0$，所以$c_-$和$c_4$没有贡献，而$c_3$对质子、中子给相同移位。将式[（83.77）](#eq:c83-mass-pion-couplings)中的零π项与原来的$-m_N\bar{\mathcal N}\mathcal N$合并，得到
<span id="eq:c83-mass-nucleon-splitting"></span>

$$
\begin{aligned}
m_p&=m_N+c_+m_u+2c_3(m_u+m_d),\\
m_n&=m_N+c_+m_d+2c_3(m_u+m_d),\\
m_n-m_p&=c_+(m_d-m_u).
\end{aligned}
\tag{83.81}
$$

这里$m_N$仍是正文定义的手征极限核子质量。最后一式先略去核子的电磁质量差，并只保留当前的一阶质量作用量；在这一近似内，中译本采用的$1.293\,\mathrm{MeV}$全部归入右边。

还需要一个夸克质量比，才能确定质量差限制的系数组合。用[八重态质量式](#eq:c83-charged-meson-masses)及$B_0=2v^3/f_\pi^2$，再按中译本习题83.6的近似，取带电K的电磁质量平方移位为带电π的两倍。记
<span id="eq:c83-mass-meson-subtractions"></span>

$$
\begin{gathered}
D_{\rm EM}=m_{\pi^\pm}^2-m_{\pi^0}^2,\qquad
P=m_{\pi^0}^2,\\
K_+=m_{K^\pm}^2-2D_{\rm EM},\qquad
K_0=m_{K^0}^2 .
\end{gathered}
\tag{83.82}
$$

忽略$O(B_0m_{\rm light}^2/m_s)$后，三条强作用质量式为
$B_0(m_u+m_d)=P$、$B_0(m_u+m_s)=K_+$及$B_0(m_d+m_s)=K_0$。后两式相减消去$m_s$，再与第一式相加、相减，便有
<span id="eq:c83-mass-quark-ratio-bridge"></span>

$$
\begin{aligned}
B_0m_u&=\frac{P+K_+-K_0}{2},&
B_0m_d&=\frac{P-K_++K_0}{2},\\
B_0m_s&=\frac{K_++K_0-P}{2},\\
r\equiv\frac{m_u}{m_d}
&=\frac{P+K_+-K_0}{P-K_++K_0}.
\end{aligned}
\tag{83.83}
$$

取中译本采用的舍入质量
$m_{\pi^\pm}=0.140$、$m_{\pi^0}=0.135$、$m_{K^\pm}=0.494$、$m_{K^0}=0.498$，单位均为$\mathrm{GeV}$。按这些实际输入，
<span id="eq:c83-mass-quark-ratio-source-values"></span>

$$
\begin{aligned}
D_{\rm EM}&=0.001375\ \mathrm{GeV}^2,&
K_+-K_0&=-0.006718\ \mathrm{GeV}^2,\\
B_0m_u&=0.0057535\ \mathrm{GeV}^2,&
B_0m_d&=0.0124715\ \mathrm{GeV}^2,\\
B_0m_s&=0.2355325\ \mathrm{GeV}^2,\\
r&=\frac{11507}{24943}\simeq0.461 .
\end{aligned}
\tag{83.84}
$$

在这一电磁估计和最低阶手征关系下，得到$m_u/m_d\simeq0.46$、$m_s/m_d\simeq19$。由$B_0=2v^3/f_\pi^2$，各个$m_qv^3/f_\pi^2$等于上式$B_0m_q$的一半。把这些值代入中性质量式，$m_\eta^2=(P+4B_0m_s)/3$给$m_\eta\simeq0.566\,\mathrm{GeV}$，比所用的$0.548\,\mathrm{GeV}$高约3.2%。差别反映了本阶质量关系及电磁模型的精度。

令$\Delta_N=1.293\,\mathrm{MeV}$。式[（83.81）](#eq:c83-mass-nucleon-splitting)现在可以确定
<span id="eq:c83-mass-determined-combinations"></span>

$$
\begin{aligned}
c_+m_d&=\frac{\Delta_N}{1-r}\simeq2.400\ \mathrm{MeV},\\
c_+m_u&=\frac{r\Delta_N}{1-r}\simeq1.107\ \mathrm{MeV},\\
c_+(m_u+m_d)&=\frac{1+r}{1-r}\Delta_N
 \simeq3.508\ \mathrm{MeV},\\
\frac{c_+}{B_0}
&=\frac{\Delta_N}{K_0-K_+}
 \simeq0.1925\ \mathrm{GeV}^{-1}.
\end{aligned}
\tag{83.85}
$$

最后一行在分子使用$\Delta_N=0.001293\,\mathrm{GeV}$。在同一QCD重整化方案内改变夸克质量的归一时，$B_0$和$c_+$都按质量的逆比例改变，上式的乘积与比值保持不变。另给绝对夸克质量后，才可单独确定无量纲的$c_+$。

质量差测得$c_1+c_2$；$c_4$及$c_-$需由其他过程确定。$c_3$改变共同核子质量，与手征极限质量$m_N$一起进入
<span id="eq:c83-mass-common-nucleon-shift"></span>

$$
\frac{m_p+m_n}{2}
=m_N+\left(\frac{c_+}{2}+2c_3\right)(m_u+m_d).
\tag{83.86}
$$

质量差与夸克质量比确定的组合见式[（83.85）](#eq:c83-mass-determined-combinations)。质量差选出的是味三重态方向，共同质量和赝标量耦合则保留为不同的低能参数。

---

[← 第 82 节](/posts/srednicki-82/) · [章节地图](/srednicki/) · [第 84 节 →](/posts/srednicki-84/)
