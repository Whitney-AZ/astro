---
title: 'Srednicki §73 非阿贝尔规范理论中的贝塔函数'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [73]
hideFromHome: true
draft: false
---

<span id="c73"></span>

上一节已经给出了计算圈图所需的规则。现在要回答的问题是：杨—米尔斯耦合常数
怎样随能标改变？在电动力学中，电子场与顶角的重整化因子相消，电荷的运行由
光子自能决定。非阿贝尔理论多出规范场的自相互作用，这个相消关系随之改变。
先求夸克场和夸克—胶子顶角的反项，再计算胶子自能，
最后把三个结果组合成同一个裸耦合。

计算取费曼规范和$\overline{\mathrm{MS}}$方案，时空维数为$d=4-\epsilon$，标度约定为$\mu^2=4\pi e^{-\gamma_E}\widetilde\mu^2$。
以下$C_R=C(R)$、$C_A=T(A)$，生成元归一由第70节固定；
先考虑一个简单规范群因子，以及$n_F$个属于同一不可约表示$R$的狄拉克味。
可约物质按不可约块分开计算，最后相加。圈积分简记为
$\int_\ell=\int d^d\ell/(2\pi)^d$，鬼场记为$c,\bar c$。

<span id="c73-bare"></span>

## 从各个顶角回到同一个耦合

把上一节的每一类动能和相互作用分别乘以重整化因子。
为简化书写，这一式暂在四维记号中列出；延拓时每个$g$都带
$\widetilde\mu^{\epsilon/2}$：

<span id="eq:c73-renormalized-density"></span>

$$
\begin{aligned}
\mathcal L
&=\frac12 Z_3 A_\mu^a
 (g^{\mu\nu}\partial^2-\partial^\mu\partial^\nu)A_\nu^a
 +\frac1{2\xi}A_\mu^a\partial^\mu\partial^\nu A_\nu^a\\
&\quad-Z_{3g}g f^{abc}A_\mu^aA_\nu^b\partial^\mu A^{c\nu}
 -\frac14 Z_{4g}g^2 f^{abe}f^{cde}
 A_\mu^aA_\nu^bA^{c\mu}A^{d\nu}\\
&\quad-Z_2'\partial^\mu\bar c^a\partial_\mu c^a
 +Z_1'g f^{abc}A_\mu^c(\partial^\mu\bar c^a)c^b\\
&\quad+iZ_2\bar\Psi_i\not\partial\Psi_i
 -Z_m m\bar\Psi_i\Psi_i
 +Z_1g A_\mu^a\bar\Psi_i\gamma^\mu T^a_{ij}\Psi_j .
\end{aligned}
\tag{73.1}
$$

这里$Z_1',Z_2'$中的撇号用来区分鬼场与夸克，并非导数。看似各处都有不同的
耦合，实际上它们应当来自同一个裸杨—米尔斯作用量。先用动能定义裸场和裸质量：

<span id="eq:c73-bare-fields"></span>

$$
\begin{gathered}
A_{0\mu}^a=Z_3^{1/2}A_\mu^a,\qquad
\Psi_0=Z_2^{1/2}\Psi,\qquad m_0=m\,\frac{Z_m}{Z_2},\\
c_0=(Z_2')^{1/2}c,\qquad
\bar c_0=(Z_2')^{1/2}\bar c,\qquad \xi_0=Z_3\xi .
\end{gathered}
\tag{73.2}
$$

最后一个选择使裸规范固定项
$-(\partial\cdot A_0)^2/(2\xi_0)$正好成为
$-(\partial\cdot A)^2/(2\xi)$，所以它在式[（73.1）](#eq:c73-renormalized-density)
中不用再乘一个$Z$。纵向传播核保持原来的形式，规范参数的变化则包含在
$\xi_0=Z_3\xi$之中。下面会直接检查本次一圈自能的横向性。

以夸克顶角为例，裸作用量中$g_0\bar\Psi_0\gamma^\mu A_{0\mu}\Psi_0$
的系数变为$g_0Z_2Z_3^{1/2}$，必须等于
$g\widetilde\mu^{\epsilon/2}Z_1$。鬼顶角有两个鬼场和一个规范场，
三胶子顶角有三个规范场，四胶子顶角则有四个。分别数出这些场因子，有

<span id="eq:c73-vertex-bare-matching"></span>

$$
\begin{aligned}
g_0Z_2Z_3^{1/2}&=g\widetilde\mu^{\epsilon/2}Z_1,&
g_0Z_2'Z_3^{1/2}&=g\widetilde\mu^{\epsilon/2}Z_1',\\
g_0Z_3^{3/2}&=g\widetilde\mu^{\epsilon/2}Z_{3g},&
g_0^2Z_3^2&=g^2\widetilde\mu^\epsilon Z_{4g}.
\end{aligned}
\tag{73.3}
$$

将前三式平方并除去场因子，便得到各个顶角必须满足的关系：

<span id="eq:c73-common-bare-coupling"></span>

$$
\begin{aligned}
g_0^2
&=g^2\widetilde\mu^\epsilon\frac{Z_1^2}{Z_2^2Z_3}
 =g^2\widetilde\mu^\epsilon\frac{(Z_1')^2}{(Z_2')^2Z_3}\\
&=g^2\widetilde\mu^\epsilon\frac{Z_{3g}^2}{Z_3^3}
 =g^2\widetilde\mu^\epsilon\frac{Z_{4g}}{Z_3^2}.
\end{aligned}
\tag{73.4}
$$

这段代数说明同一个裸耦合要求哪些关系。量子反项能否同时满足它们，
还需要非阿贝尔的Slavnov–Taylor恒等式及无规范异常的条件，其根据见
[第74节](/posts/srednicki-74/#c74-st)。先以这一量子关系为条件，任选一个顶角就能
确定$g_0$。夸克顶角可复用第62节的大部分积分，因而这里只需求$Z_1,Z_2,Z_3$。

<span id="c73-quark"></span>

## 夸克自能的颜色因子

[下图](#fig:c73-quark-self-energy)左边只有一条内部胶子线。
它把两个生成元的颜色指标相接，留下
$\sum_a(T^aT^a)_{ij}=C_R\delta_{ij}$。其余的动量与伽马矩阵运算
同[电子自能](/posts/srednicki-62/#c62-electron-loop)完全一样。

![夸克一圈自能和动能、质量反项](/images/srednicki/s73_quark_self_energy.svg)

夸克自能与局部反项。
实线箭头从$j$到$i$，两顶点间带$p+\ell$；
上方胶子从右向左带$\ell$。叉号包括动能和质量反项。

<span id="fig:c73-quark-self-energy"></span>

具体地，把式[（62.25）](/posts/srednicki-62/#eq:c62-electron-parameters)中的$e^2$换成$g^2C_R$，并取零胶子质量。
平移$q=\ell+xp$后，奇的$\not q$项积分为零，于是

<span id="eq:c73-quark-parameter-integral"></span>

$$
\begin{aligned}
i\Sigma_{ij}(p)
&=-g^2C_R\delta_{ij}\widetilde\mu^\epsilon
\int_0^1dx\int\frac{d^dq}{(2\pi)^d}
\frac{(d-2)(1-x)\not p+dm}
 {[q^2+xm^2+x(1-x)p^2-i0]^2}\\
&\quad-i\delta_{ij}
 \bigl(\delta Z_2\not p+\delta Z_m m\bigr)+O(g^4).
\end{aligned}
\tag{73.5}
$$

为提取UV极点，可以在欧氏离壳动量或$m>0$下进行。第62节的主积分极部为
$i/(8\pi^2\epsilon)$，与参数质量无关。极点系数中令$d=4$，再用
$\int_0^1(1-x)dx=1/2$，便得到

<span id="eq:c73-quark-counterterms"></span>

$$
\begin{aligned}
\Sigma_{ij}\big|_{\rm pole}
&=-\delta_{ij}\left[
 \frac{g^2C_R}{8\pi^2\epsilon}(\not p+4m)
 +\delta Z_2\not p+\delta Z_m m\right],\\
Z_2&=1-\frac{C_Rg^2}{8\pi^2\epsilon}+O(g^4),\qquad
Z_m=1-\frac{4C_Rg^2}{8\pi^2\epsilon}+O(g^4).
\end{aligned}
\tag{73.6}
$$

第一行的两个独立矩阵结构分别确定动能和质量反项。
质量项还将用于[夸克质量的尺度演化](#c73-anomalous)。
这里保留的是$\overline{\mathrm{MS}}$极部。第62节为满足壳上质量和留数条件
加入的有限项，不能一同带到本节。

<span id="c73-vertex"></span>

## 两幅夸克顶角图

延拓到$d$维后，整个三点顶角有一个与树顶角相同的
$\widetilde\mu^{\epsilon/2}$。以下将它共同提出，只在每一圈积分中保留
$\widetilde\mu^\epsilon$，这样反项系数可直接同四维记号比较。

[下图](#fig:c73-quark-vertices)左边是已经算过的电动力学顶角图。
但沿有向费米线依次相乘的颜色矩阵为$T^bT^aT^b$，中间的$T^a$
一般不能移到求和外。由$T^aT^b=T^bT^a+if^{abc}T^c$，有

<span id="eq:c73-abelian-color-chain"></span>

$$
\begin{aligned}
\sum_bT^bT^aT^b
&=C_RT^a+if^{abc}T^bT^c\\
&=C_RT^a+\frac i2f^{abc}[T^b,T^c]\\
&=C_RT^a-\frac12f^{abc}f^{bcd}T^d
=\left(C_R-\frac12C_A\right)T^a .
\end{aligned}
\tag{73.7}
$$

第二行用$f$在$b,c$下反对称，使反对易部分消失；最后一行将
$f^{bcd}=f^{dbc}$后，用第70节的伴随迹
$f^{abc}f^{dbc}=C_A\delta^{ad}$。这将有序的三个生成元约化为一个生成元。
把[第62节已求出的顶角极部](/posts/srednicki-62/#c62-vertex-uv)乘上这个颜色因子，
第一幅图给

<span id="eq:c73-abelian-vertex-pole"></span>

$$
\left.iV^{a\mu}_{ij}\right|_{\rm QED\ type,\ pole}
=\left(C_R-\frac12C_A\right)
\frac{g^2}{8\pi^2\epsilon}\,igT^a_{ij}\gamma^\mu .
\tag{73.8}
$$

第62节计算中，两个费米传播子的分子产生
$(d-2)^2q^2\gamma^\mu/d$，带$q^2$的三分母积分的极部为
$i/(8\pi^2\epsilon)$；费曼参数的总权重为1。
本次只改变有序颜色链和耦合，故没有新的自旋迹或味数因子。
费米线仍是开链，也没有闭圈负号。

![类电动力学顶角圈与含三胶子顶角的非阿贝尔圈](/images/srednicki/s73_quark_vertices.svg)

夸克—胶子顶角的两种一圈修正。
外胶子为$(a,\mu)$。左图的内部胶子颜色为$b$；
右图两胶子的颜色为$b,c$，它们在下方三胶子顶角会合。
右图按零外动量标记，内部费米线带$\ell$，三胶子端的两个内部出动量为$\ell,-\ell$。

<span id="fig:c73-quark-vertices"></span>

右图含有三胶子顶角，是本节第一个新的积分。它的UV发散度为零，
局部发散项因而不能含外动量。取$m>0$并令外动量为零，就能直接取出该系数；
保留$m$也使约分后的积分在红外可积。无质量理论可先保留非零离壳动量
或一个辅助红外尺度，UV减除后再去掉它。
图中左、右端的内部洛伦兹指标标为$\rho,\nu$；
下面的积分将这两个虚指标同时互换，所有出现都随之换名。

沿有向费米线依次读取矩阵，两个夸克顶角给$(ig)^2T^cT^b$，
三胶子顶角给$gf^{abc}$，三条内线各给$1/i$。因此

<span id="eq:c73-nonabelian-vertex-integral"></span>

$$
\begin{aligned}
iV_{\rm NA}^{a\mu}(0,0)
&=(ig)^2g f^{abc}T^cT^b
 \left(\frac1i\right)^3
 \widetilde\mu^\epsilon\int\frac{d^d\ell}{(2\pi)^d}
 \frac{N^\mu}{(\ell^2-i0)^2(\ell^2+m^2-i0)},\\
N^\mu
&=\gamma_\rho(-\not\ell+m)\gamma_\nu
 \left(2\ell^\mu g^{\nu\rho}
       -\ell^\nu g^{\rho\mu}-\ell^\rho g^{\mu\nu}\right).
\end{aligned}
\tag{73.9}
$$

两条内部胶子接在有向费米线的两个不同端点上，交换它们会改变色矩阵次序；
这幅顶角图的对称因子为1。先化简颜色：

<span id="eq:c73-nonabelian-color"></span>

$$
f^{abc}T^cT^b
=\frac12f^{abc}[T^c,T^b]
=\frac i2f^{abc}f^{cbd}T^d
=-\frac i2 C_AT^a .
\tag{73.10}
$$

最后一个负号来自$f^{cbd}=-f^{dbc}$。再看分子：含$m$的部分对$\ell$为奇，
在共同的维数积分中为零；其余部分用
$\ell^\sigma\ell^\mu\longrightarrow\ell^2g^{\sigma\mu}/d$作角平均。
由$\{\gamma^\mu,\gamma^\nu\}=-2g^{\mu\nu}$，
$\gamma_\nu\gamma^\nu=-d$、
$\gamma_\nu\gamma^\mu\gamma^\nu=(d-2)\gamma^\mu$，所以

<span id="eq:c73-nonabelian-numerator"></span>

$$
\begin{aligned}
N^\mu&\longrightarrow
-\frac{\ell^2}{d}
\left(2\gamma_\nu\gamma^\mu\gamma^\nu
 -\gamma^\mu\gamma_\nu\gamma^\nu
 -\gamma_\rho\gamma^\rho\gamma^\mu\right)\\
&=-\frac{\ell^2}{d}\,[2(d-2)+d+d]\gamma^\mu\\
&=-\frac{4(d-1)}d\,\ell^2\gamma^\mu
=-\bigl[3+O(\epsilon)\bigr]\ell^2\gamma^\mu .
\end{aligned}
\tag{73.11}
$$

这就完成了分子的伽马缩并。因为现在只求简单UV极点，
$O(\epsilon)$的分子只改变有限项，取系数3已经足够。
它同时约掉原分母中的一个$\ell^2$。把常数相乘，
$(ig)^2(1/i)^3=-ig^2$，再乘颜色的$-iC_A/2$和分子的$-3$，
总系数成为$+3g^3C_A/2$：

<span id="eq:c73-cancelled-vertex-denominator"></span>

$$
\left.iV_{\rm NA}^{a\mu}\right|_{\rm pole}
=\frac32 C_Ag^3T^a\gamma^\mu
\left[\widetilde\mu^\epsilon\int\frac{d^d\ell}{(2\pi)^d}
\frac1{(\ell^2-i0)(\ell^2+m^2-i0)}\right]_{\rm pole}.
\tag{73.12}
$$

分子约去一个$\ell^2$以后，剩下的$I_m$在四维具有零质量维数，
紫外径向行为为$\int^\infty d\ell/\ell$，正是决定顶角反项的对数积分。

利用两分母的费曼参数公式，有

<span id="eq:c73-vertex-master-evaluation"></span>

$$
\begin{aligned}
I_m&:=\widetilde\mu^\epsilon\int_\ell
\frac1{(\ell^2-i0)(\ell^2+m^2-i0)}\\
&=\int_0^1dx\,
\frac{i\Gamma(\epsilon/2)}{(4\pi)^{d/2}}\,
\widetilde\mu^\epsilon(xm^2-i0)^{-\epsilon/2}\\
&=\frac{i\Gamma(\epsilon/2)}{16\pi^2}
\left(\frac{4\pi\widetilde\mu^2}{m^2}\right)^{\epsilon/2}
\frac1{1-\epsilon/2}\\
&=\frac{i}{8\pi^2}
\left[\frac1\epsilon-\frac12\ln\frac{m^2}{\mu^2}
 +\frac12\right]+O(\epsilon).
\end{aligned}
\tag{73.13}
$$

第三行用了$\int_0^1x^{-\epsilon/2}dx=(1-\epsilon/2)^{-1}$。
威克旋转、径向Gamma积分及$\mu$的换算均与式[（62.15）](/posts/srednicki-62/#eq:c62-master-integral)相同。
所以$I_m$的极点为$i/(8\pi^2\epsilon)$。式中虽列出$I_m$的有限项，
完整顶角的有限部分还会接收式[（73.11）](#eq:c73-nonabelian-numerator)中
$O(\epsilon)$系数的贡献；求反项只取这里的极点。

将两幅图与树顶角相加，极部的系数为

<span id="eq:c73-vertex-counterterm"></span>

$$
\begin{aligned}
iV^{a\mu}_{ij}
&=igT^a_{ij}\gamma^\mu
\left[Z_1+\left(C_R-\frac12C_A+\frac32C_A\right)
\frac{g^2}{8\pi^2\epsilon}\right]
+\hbox{有限圈项},\\
Z_1&=1-(C_R+C_A)\frac{g^2}{8\pi^2\epsilon}+O(g^4),\\
Z_1-Z_2&=-C_A\frac{g^2}{8\pi^2\epsilon}+O(g^4).
\end{aligned}
\tag{73.14}
$$

多出的$C_A$正是规范场自相互作用的结果。
在电动力学中，沃德恒等式使$Z_1=Z_2$；这里规范固定及鬼作用量同时含普通导数
和协变导数，不能只从物质动能的形式照搬那个结论。
本节使用的是式[（73.4）](#eq:c73-common-bare-coupling)的各比值相等，
它容许单独的$Z_1,Z_2$不同。下面还需求出其中的$Z_3$。

<span id="c73-gluon"></span>

## 胶子自能：两个三胶子顶角的缩并

胶子二点函数包含胶子蝌蚪、胶子泡、鬼泡、夸克泡和局部反项，
如[下图](#fig:c73-gluon-self-energy)所示。先看蝌蚪：四胶子顶角不含导数，
圈内只有一个无质量传播子，因此它正比于$\int_\ell1/\ell^2$。
这个无尺度积分在维数正规化中为零。其径向形式也说明了这里的含义：
引入任意分界尺度$M$，分别延拓低端和高端积分，

<span id="eq:c73-scaleless-tadpole"></span>

$$
\begin{aligned}
\int_0^Mdr\,r^{d-3}&=\frac{M^{d-2}}{d-2},\\
\int_M^\infty dr\,r^{d-3}&=-\frac{M^{d-2}}{d-2},\\
\int_0^\infty dr\,r^{d-3}&=0
\qquad\hbox{（两部分的共同亚纯延拓）}.
\end{aligned}
\tag{73.15}
$$

前两行原来分别在$\operatorname{Re}d>2$和$\operatorname{Re}d<2$收敛；
延拓后的和不依赖$M$。这沿用第65节的无尺度积分约定。
后面的泡图含外动量$k$，不能按同样理由消去；先取$k^2>0$的欧氏区域。

![胶子蝌蚪、胶子泡、鬼泡、夸克泡和胶子动能反项](/images/srednicki/s73_gluon_self_energy.svg)

胶子二点函数的一圈图及反项。
上排为四胶子蝌蚪和胶子泡，下排为鬼泡、夸克泡及反项。
两条外线的动量$k$均向右，内部泡的上支带$\ell+k$、下支带$\ell$。
鬼泡的点线和夸克泡的实线均有连续箭头；胶子泡的两条无向内线可交换。

<span id="fig:c73-gluon-self-energy"></span>

胶子泡的两条内部胶子连接同一对顶点，可以彼此交换，故有对称因子$1/2$。
也可以从收缩计数得到这一因子：两个有标签的外端分配到两顶点有$2!$种，
各顶点选择外腿插槽有$3$种，剩下两内腿的配对有$2!$种。
除以微扰展开的$2!$及两只对称三价顶角的$(3!)^2$，
得到$2!\,3^2\,2!/[2!(3!)^2]=1/2$。
两只结构常数缩并为$f^{acd}f^{bcd}=C_A\delta^{ab}$。
按上一节的全部出顶规则，把两只三胶子顶角相乘，得到

<span id="eq:c73-gluon-bubble-integral"></span>

$$
\begin{aligned}
i\Pi^{\mu\nu}_{G,ab}(k)
&=\frac12g^2C_A\delta^{ab}\left(\frac1i\right)^2
\widetilde\mu^\epsilon\int_\ell
\frac{N^{\mu\nu}}{(\ell^2-i0)[(\ell+k)^2-i0]},\\
N^{\mu\nu}
&=-V^\mu{}_{\rho\sigma}V^{\nu\rho\sigma},\\
V^\mu{}_{\rho\sigma}
&=L^\mu g_{\rho\sigma}
-B_\rho\delta^\mu_\sigma-C_\sigma\delta^\mu_\rho,\\
L&=2\ell+k,\qquad B=\ell-k,\qquad C=\ell+2k,\qquad L=B+C .
\end{aligned}
\tag{73.16}
$$

第二个顶角的全部出动量与第一个相反，三胶子顶角对动量为奇，
所以分子前出现负号；两传播子的$(1/i)^2=-1$仍另列在第一行。
第一只顶角的内部指标统一置下，第二只统一置上，
使每个内部指标以一上一下的方式缩并。
将三个分量逐项相乘，得到下面九项。行对应第一只$V$的三项，
列对应第二只$V$的三项；此表尚未乘$N$前的总负号。

<span id="eq:c73-nine-contractions"></span>

$$
\begin{array}{c|ccc}
 &L^\nu g^{\rho\sigma}
 &-B^\rho g^{\nu\sigma}
 &-C^\sigma g^{\nu\rho}\\ \hline
L^\mu g_{\rho\sigma}
 &dL^\mu L^\nu&-L^\mu B^\nu&-L^\mu C^\nu\\
-B_\rho\delta^\mu_\sigma
 &-B^\mu L^\nu&B^2g^{\mu\nu}&B^\nu C^\mu\\
-C_\sigma\delta^\mu_\rho
 &-C^\mu L^\nu&C^\nu B^\mu&C^2g^{\mu\nu}
\end{array}
\tag{73.17}
$$

例如第一项用$g_{\rho\sigma}g^{\rho\sigma}=d$；
第二行第三列把$\rho$置为$\nu$、$\sigma$置为$\mu$，因而是$B^\nu C^\mu$。
四个带$L$的交叉项合为
$-L^\mu(B+C)^\nu-(B+C)^\mu L^\nu=-2L^\mu L^\nu$。
乘回总负号后，九项缩并成为

<span id="eq:c73-contracted-numerator"></span>

$$
N^{\mu\nu}
=-\left[(d-2)L^\mu L^\nu
 +(B^2+C^2)g^{\mu\nu}
 +B^\mu C^\nu+C^\mu B^\nu\right].
\tag{73.18}
$$

现在合并分母，让第二个分母占权重$x$，有

<span id="eq:c73-gluon-parameter-shift"></span>

$$
\begin{aligned}
(1-x)\ell^2+x(\ell+k)^2
&=(\ell+xk)^2+x(1-x)k^2,\\
q&=\ell+xk,\qquad D=x(1-x)k^2,\qquad d^d\ell=d^dq,\\
i\Pi^{\mu\nu}_{G,ab}
&=-\frac12g^2C_A\delta^{ab}
\widetilde\mu^\epsilon\int_0^1dx\int_q
\frac{N^{\mu\nu}}{(q^2+D-i0)^2},\\
L&=2q+(1-2x)k,\quad
B=q-(1+x)k,\quad C=q+(2-x)k .
\end{aligned}
\tag{73.19}
$$

平移的雅可比因子为1。把最后一行代入式[（73.18）](#eq:c73-contracted-numerator)，
奇的$q$项积分为零。$q^\mu q^\nu$的系数由
$4(d-2)+2=4d-6$给出；其余偶项为

<span id="eq:c73-even-numerator"></span>

$$
\begin{aligned}
N^{\mu\nu}\longrightarrow&
-2q^2g^{\mu\nu}-(4d-6)q^\mu q^\nu\\
&-\bigl[(1+x)^2+(2-x)^2\bigr]k^2g^{\mu\nu}\\
&-\bigl[(d-2)(1-2x)^2
 -2(1+x)(2-x)\bigr]k^\mu k^\nu .
\end{aligned}
\tag{73.20}
$$

含$(1-2x)$的两个交叉项可用$1-2x=(2-x)-(1+x)$合并，
给出$-2(1-2x)^2$；它与$d(1-2x)^2$相加，产生上式的$d-2$。
在取$d=4$以前，维数依赖的每一项都须保留。

本次仍使用第62节已经求出的两个径向积分，记

<span id="eq:c73-radial-integrals"></span>

$$
\begin{aligned}
I_2(D)&:=\widetilde\mu^\epsilon
\int_q\frac1{(q^2+D-i0)^2}\\
&=\frac{i\widetilde\mu^\epsilon}{(4\pi)^{d/2}}
\Gamma(2-d/2)(D-i0)^{d/2-2}\\
&=\frac{i}{8\pi^2}\left[
\frac1\epsilon-\frac12\ln\frac{D-i0}{\mu^2}\right]+O(\epsilon),\\
J(D)&:=\widetilde\mu^\epsilon
\int_q\frac{q^2}{(q^2+D-i0)^2}
=-\frac d{d-2}D\,I_2(D).
\end{aligned}
\tag{73.21}
$$

$J$的关系来自式[（62.13）](/posts/srednicki-62/#eq:c62-radial-identity)：先在固定$D>0$、$0<\operatorname{Re}d<2$
的收敛域积分总导数$\partial_{q^\mu}[q^\mu/(q^2+D)]$，再延拓到$d=4-\epsilon$。
具体地，若$I_1=\widetilde\mu^\epsilon\int_q(q^2+D)^{-1}$，
则$dI_1=2J$且$J=I_1-DI_2$，消去$I_1$就得到最后一行。
因而将$J$写成$I_2$时，系数为$(2/d-1)^{-1}D$，在极点系数中成为$-2D$。
这个负号来自维数积分的延拓。

为了取简单极点，先在式[（73.20）](#eq:c73-even-numerator)中用
$q^\mu q^\nu\to q^2g^{\mu\nu}/4$，并令$d=4$。三个系数分别算为
$-2-(16-6)/4=-9/2$、
$-(1+x)^2-(2-x)^2=-5+2x-2x^2$和
$-2(1-2x)^2+2(1+x)(2-x)=2+10x-10x^2$，所以

<span id="eq:c73-four-dimensional-numerator"></span>

$$
\begin{aligned}
N^{\mu\nu}\longrightarrow&
-\frac92q^2g^{\mu\nu}
-(5-2x+2x^2)k^2g^{\mu\nu}\\
&+(2+10x-10x^2)k^\mu k^\nu .
\end{aligned}
\tag{73.22}
$$

在二次分母的积分内，将$q^2$项换成$-2D=-2x(1-x)k^2$；
它给度规项增加$9x(1-x)k^2$。于是积分内剩下的张量成为

<span id="eq:c73-reduced-pole-numerator"></span>

$$
\widehat N^{\mu\nu}(x)
=-(5-11x+11x^2)k^2g^{\mu\nu}
 +(2+10x-10x^2)k^\mu k^\nu ,
\tag{73.23}
$$

其中帽号表示径向积分已经约化到$I_2$。乘上其极点并对$x$积分：

<span id="eq:c73-gluon-bubble-pole"></span>

$$
\begin{aligned}
\int_0^1(5-11x+11x^2)dx
&=5-\frac{11}{2}+\frac{11}{3}=\frac{19}{6},\\
\int_0^1(2+10x-10x^2)dx
&=2+5-\frac{10}{3}=\frac{11}{3},\\
\left.i\Pi^{\mu\nu}_{G,ab}\right|_{\rm pole}
&=-\frac{ig^2C_A\delta^{ab}}{16\pi^2\epsilon}
\left[-\frac{19}{6}k^2g^{\mu\nu}
 +\frac{11}{3}k^\mu k^\nu\right].
\end{aligned}
\tag{73.24}
$$

两个张量的系数绝对值不相等，
单独这幅图的纵向缩并尚不为零。鬼圈将补上缺少的部分。

<span id="c73-ghost"></span>

## 鬼圈与横向性

鬼泡与胶子泡的分母相同，分子只有两只导数顶角给出的动量。
按图中的连续箭头排列颜色矩阵与动量，得到

<span id="eq:c73-ghost-bubble-integral"></span>

$$
\begin{aligned}
i\Pi^{\mu\nu}_{H,ab}
&=(-1)g^2f^{acd}f^{bdc}
\left(\frac1i\right)^2\widetilde\mu^\epsilon
\int_\ell\frac{(\ell+k)^\mu\ell^\nu}
 {(\ell^2-i0)[(\ell+k)^2-i0]}\\
&=-g^2C_A\delta^{ab}\widetilde\mu^\epsilon
\int_\ell\frac{(\ell+k)^\mu\ell^\nu}
 {(\ell^2-i0)[(\ell+k)^2-i0]} .
\end{aligned}
\tag{73.25}
$$

这里有三个负号：闭鬼圈的$-1$、
$f^{acd}f^{bdc}=-C_A\delta^{ab}$及两传播子的$(1/i)^2=-1$。
它们相乘仍为负。鬼线有方向，不能交换两内线而保持全部有序顶角，
所以没有胶子泡的$1/2$。

使用相同的$q=\ell+xk$，分子变为
$[q+(1-x)k]^\mu(q-xk)^\nu$。
奇项消失后，在任意$d$下约化为

<span id="eq:c73-ghost-tensor-reduction"></span>

$$
\begin{aligned}
\widetilde\mu^\epsilon\int_q
\frac{(\ell+k)^\mu\ell^\nu}{(q^2+D-i0)^2}
&=\frac{g^{\mu\nu}}dJ(D)-x(1-x)k^\mu k^\nu I_2(D)\\
&=-x(1-x)\left[
\frac{k^2g^{\mu\nu}}{d-2}+k^\mu k^\nu\right]I_2(D).
\end{aligned}
\tag{73.26}
$$

在极点系数中取$d=4$，再用
$\int_0^1x(1-x)dx=1/6$，得到

<span id="eq:c73-gauge-ghost-pole"></span>

$$
\begin{aligned}
\left.i\Pi^{\mu\nu}_{H,ab}\right|_{\rm pole}
&=-\frac{ig^2C_A\delta^{ab}}{8\pi^2\epsilon}
\left[-\frac1{12}k^2g^{\mu\nu}-\frac16k^\mu k^\nu\right],\\
\left.i(\Pi_G+\Pi_H)^{\mu\nu}_{ab}\right|_{\rm pole}
&=\frac{ig^2C_A\delta^{ab}}{8\pi^2\epsilon}
\left[\left(\frac{19}{12}+\frac1{12}\right)k^2g^{\mu\nu}
 +\left(-\frac{11}{6}+\frac16\right)k^\mu k^\nu\right]\\
&=\frac{ig^2C_A\delta^{ab}}{8\pi^2\epsilon}\,
\frac53(k^2g^{\mu\nu}-k^\mu k^\nu).
\end{aligned}
\tag{73.27}
$$

鬼场的闭圈负号和颜色次序在这里共同发挥作用。它补足了胶子泡的两个系数，
使发散部分具有规范动能的张量形式，因而可由一个$Z_3$吸收。

<span id="c73-transverse"></span>

### 保留维数后的一圈横向性

还要考察整个一圈自能的横向性。只比较极点不足以确定有限部分是否横向，不过前面的计算已经保留了所需的$d$维分子，只须再作一次参数积分。
令$u=x(1-x)$，将式[（73.20）](#eq:c73-even-numerator)中的
$q^\mu q^\nu$换成$g^{\mu\nu}q^2/d$，并用式[（73.21）](#eq:c73-radial-integrals)
的精确关系。胶子泡的度规系数是
$-5+(8d-10)u/(d-2)$，$k^\mu k^\nu$系数是$6-d+(4d-6)u$。
在共同前因子$-g^2C_A/2$下，鬼泡须加两倍式[（73.26）](#eq:c73-ghost-tensor-reduction)，
于是

<span id="eq:c73-full-dimensional-tensor"></span>

$$
\begin{aligned}
i(\Pi_G+\Pi_H)^{\mu\nu}_{ab}
&=-\frac12g^2C_A\delta^{ab}
\int_0^1dx\,I_2(uk^2)
\left[G_d(x)k^2g^{\mu\nu}+H_d(x)k^\mu k^\nu\right],\\
G_d(x)&=-5+\frac{4(2d-3)}{d-2}u,\qquad
H_d(x)=6-d+4(d-2)u,\\
G_d+H_d
&=-(d-1)+\frac{4(d-1)^2}{d-2}u .
\end{aligned}
\tag{73.28}
$$

所有$x$依赖的权重为$I_2(uk^2)\propto u^{d/2-2}$。
记$a=d/2-2$，用欧拉贝塔函数$B(p,q)=\int_0^1dx\,x^{p-1}(1-x)^{q-1}=\Gamma(p)\Gamma(q)/\Gamma(p+q)$表示这两个单参数积分，其归一加权平均为

<span id="eq:c73-transverse-beta-integral"></span>

$$
\begin{aligned}
\langle u\rangle_a
&=\frac{\int_0^1dx\,[x(1-x)]^{a+1}}
        {\int_0^1dx\,[x(1-x)]^a}
=\frac{B(a+2,a+2)}{B(a+1,a+1)}\\
&=\frac{(a+1)^2}{(2a+3)(2a+2)}
=\frac{d-2}{4(d-1)},\\
\int_0^1dx\,I_2(uk^2)(G_d+H_d)&=0 .
\end{aligned}
\tag{73.29}
$$

第二行只用了$\Gamma(z+1)=z\Gamma(z)$。这个平均值也可直接由分部积分求出：对$\operatorname{Re}a>-1$，$u^{a+1}(1-2x)$在两个端点均为零，故

<span id="eq:c73-transverse-integration-by-parts"></span>

$$
\begin{aligned}
0&=\int_0^1dx\,\frac d{dx}\bigl[u^{a+1}(1-2x)\bigr]\\
 &=\int_0^1dx\,u^a\bigl[(a+1)-(4a+6)u\bigr],\\
\langle u\rangle_a&=\frac{a+1}{4a+6}
 =\frac{d-2}{4(d-1)}.
\end{aligned}
\tag{73.41}
$$

将此值代入式[（73.28）](#eq:c73-full-dimensional-tensor)，
常数项与$u$项正好抵消。这些参数积分可先在
$2<\operatorname{Re}d<4$、$k^2>0$下建立，再与先前完成的径向亚纯函数
一同延拓。于是$k_\mu(\Pi_G+\Pi_H)^{\mu\nu}=0$对完整的一圈函数成立，
并沿同一$i0$取到物理区域。径向张量积分的平移及分部积分沿用此前的维数延拓。

<span id="c73-gluon-counterterm"></span>

## 夸克闭圈与胶子反项

剩下的夸克泡可复用[第62节的完整横向分子](/posts/srednicki-62/#c62-photon-loop)。
旋量迹仍为4，但颜色迹独立给
$\operatorname{Tr}_R(T^aT^b)=T(R)\delta^{ab}$。
每一味可分别围成闭圈，因此还要对味求和。
将式[（62.14）](/posts/srednicki-62/#eq:c62-loop-transverse)中的$2x(1-x)$和四伽马迹的4一并保留，得到

<span id="eq:c73-fermion-polarization"></span>

$$
\begin{aligned}
i\Pi^{\mu\nu}_{F,ab}(k)
&=-8g^2n_FT(R)\delta^{ab}
(k^2g^{\mu\nu}-k^\mu k^\nu)
\int_0^1dx\,x(1-x)I_2\!\left(m^2+x(1-x)k^2\right),\\
\left.i\Pi^{\mu\nu}_{F,ab}\right|_{\rm pole}
&=-\frac{ig^2n_FT(R)\delta^{ab}}{6\pi^2\epsilon}
(k^2g^{\mu\nu}-k^\mu k^\nu).
\end{aligned}
\tag{73.30}
$$

第二行的$1/6$来自参数积分，极点不依赖$m$。
若各味质量不同，第一行分别使用$m_f$再求和，极点系数依旧按味数计。
颜色迹已经包含一味的全部色分量，不能在$T(R)$之外再乘一个$D(R)$。
闭费米圈的负号与第62节一致。

由规范动能反项产生的插入是
$-i\delta Z_3\delta^{ab}(k^2g^{\mu\nu}-k^\mu k^\nu)$。
将它同式[（73.27）](#eq:c73-gauge-ghost-pole)和式[（73.30）](#eq:c73-fermion-polarization)相加，
得到圈图与反项之和：

<span id="eq:c73-gluon-counterterm"></span>

$$
\begin{aligned}
\Pi^{\mu\nu}_{ab}(k)
&=\delta^{ab}(k^2g^{\mu\nu}-k^\mu k^\nu)\Pi(k^2),\\
\left.\Pi(k^2)\right|_{\rm pole}
&=-\delta Z_3+
\left[\frac53C_A-\frac43n_FT(R)\right]\frac{g^2}{8\pi^2\epsilon},\\
Z_3&=1+\left[\frac53C_A-\frac43n_FT(R)\right]
\frac{g^2}{8\pi^2\epsilon}+O(g^4).
\end{aligned}
\tag{73.31}
$$

横向结构已分别由规范场加鬼场的参数积分、以及夸克泡的径向恒等式得到。
一个$Z_3$因而足以减去本次胶子二点函数的UV极部；
无质量蝌蚪按同一维数方案为零，没有留下质量反项。
至此，求规范耦合所需的三个因子都已确定。

<span id="c73-beta"></span>

## 简单极点怎样决定贝塔函数

先汇总夸克动能、夸克顶角和胶子动能的反项：

<span id="eq:c73-three-renormalization-factors"></span>

$$
\begin{aligned}
Z_1&=1-(C_R+C_A)\frac{g^2}{8\pi^2\epsilon}+O(g^4),\\
Z_2&=1-C_R\frac{g^2}{8\pi^2\epsilon}+O(g^4),\\
Z_3&=1+\left[\frac53C_A-\frac43n_FT(R)\right]
\frac{g^2}{8\pi^2\epsilon}+O(g^4).
\end{aligned}
\tag{73.32}
$$

这三个因子各自依赖场的归一和规范选择。规范耦合所要求的组合则是
$Z_1^2/(Z_2^2Z_3)$。同第66节一样，改用正的无量纲变量
$\alpha=g^2/(4\pi)$，并定义$\alpha_0=g_0^2/(4\pi)$，有

<span id="eq:c73-bare-alpha-log"></span>

$$
\begin{aligned}
\alpha_0&=\alpha\widetilde\mu^\epsilon
\frac{Z_1^2}{Z_2^2Z_3},\\
\ln\frac{Z_1^2}{Z_2^2Z_3}
&=\sum_{n\ge1}\frac{G_n(\alpha)}{\epsilon^n},\\
\ln\alpha_0
&=\ln\alpha+\epsilon\ln\widetilde\mu
+\sum_{n\ge1}\frac{G_n(\alpha)}{\epsilon^n}.
\end{aligned}
\tag{73.33}
$$

$G_n$是极点展开的系数，不是另一个物理耦合。
对有量纲的裸量取对数时，可先用一个固定单位除去其量纲；该单位在尺度微分中
不出现。用$\ln(1+\delta Z)=\delta Z+O(g^4)$，简单极点为

<span id="eq:c73-simple-pole"></span>

$$
\begin{aligned}
G_1(\alpha)
&=\left[-2(C_R+C_A)+2C_R
-\frac53C_A+\frac43n_FT(R)\right]\frac{\alpha}{2\pi}
+O(\alpha^2)\\
&=-b_0\frac{\alpha}{2\pi}+O(\alpha^2),\qquad
b_0:=\frac{11}{3}C_A-\frac43n_FT(R).
\end{aligned}
\tag{73.34}
$$

第一行依次来自$2\ln Z_1,-2\ln Z_2,-\ln Z_3$。
开放夸克线的$C_R$项在这里相消；闭夸克圈的$T(R)$则留下来。
因而用哪一种夸克顶角定义耦合，并不会给规范部分引入一个额外的外腿卡西米尔。

现在固定裸参数，令$t=\ln\mu$。由于$\widetilde\mu$与$\mu$只差固定倍数，
$d\ln\widetilde\mu/dt=1$。保留$d$维工程项，写
$B_\alpha=d\alpha/dt=-\epsilon\alpha+\beta_\alpha$。
对式[（73.33）](#eq:c73-bare-alpha-log)求导，按极点次数整理：

<span id="eq:c73-bare-scale-derivative"></span>

$$
\begin{aligned}
0&=\epsilon+\frac{B_\alpha}{\alpha}
+B_\alpha\sum_{n\ge1}\frac{G_n'(\alpha)}{\epsilon^n}\\
&=\frac{\beta_\alpha}{\alpha}-\alpha G_1'
+\sum_{n\ge1}\frac{\beta_\alpha G_n'
-\alpha G_{n+1}'}{\epsilon^n}.
\end{aligned}
\tag{73.35}
$$

这里的撇号才表示对$\alpha$求导。第一行的显式$\epsilon$与
$B_\alpha/\alpha$的工程项抵消；工程项再乘$G_1'/\epsilon$，留下有限的
$-\alpha G_1'$。更高极点的次数则降低一级，所以第二行出现$n+1$。
这正是[第28节的固定裸量分析](/posts/srednicki-28/#c28-beta)在本次耦合上的应用。
若暂保留$G_n$对规范参数的依赖，链式法则还要加入
$B_\xi\sum_n(\partial_\xi G_n)/\epsilon^n$；$\xi$没有工程量纲，
这些项进入极点抵消关系，不改变此处的有限项。

有限部分给$\beta_\alpha=\alpha^2G_1'$，代入式[（73.34）](#eq:c73-simple-pole)，
便得到贝塔函数：

<span id="eq:c73-alpha-beta"></span>

$$
\beta_\alpha
=-\left[\frac{11}{3}C_A-\frac43n_FT(R)\right]
\frac{\alpha^2}{2\pi}+O(\alpha^3).
\tag{73.36}
$$

最后改回$g$。由$\alpha=g^2/(4\pi)$，
$\beta_\alpha=g\beta_g/(2\pi)$，所以

<span id="eq:c73-gauge-beta"></span>

$$
\begin{aligned}
\beta_g
&=\frac{2\pi}{g}\left[-\frac{b_0}{2\pi}
\left(\frac{g^2}{4\pi}\right)^2\right]+O(g^5)\\
&=-\left[\frac{11}{3}T(A)-\frac43n_FT(R)\right]
\frac{g^3}{16\pi^2}+O(g^5).
\end{aligned}
\tag{73.37}
$$

分母$16\pi^2$来自两次变量转换，不能把本节
$\epsilon=4-d$的$1/(8\pi^2\epsilon)$直接替成使用$4-2\epsilon$时的写法。
阿贝尔极限中$C_A=0$，若生成元在一个电荷空间上为$t$，
再用$gt=e$，便恢复一味狄拉克电动力学的结果
$\beta_e=e^3/(12\pi^2)$，即电荷大小随能标增加。纯规范部分的符号则相反。

<span id="c73-physical"></span>

## 从渐近自由到低能问题

对QCD代入第70节的$T(A)=3$、$T(R)=1/2$，有

<span id="eq:c73-qcd-coefficient"></span>

$$
b_0=11-\frac23n_F,\qquad
\beta_g=-\left(11-\frac23n_F\right)\frac{g^3}{16\pi^2}
+O(g^5).
\tag{73.38}
$$

当整数味数$n_F\le16$时，$b_0>0$；在弱耦合区域，提高能标使规范耦合变小。
这称为渐近自由。为了看清这一结论的尺度含义，
保留一圈项并在味数不变的区间积分：

<span id="eq:c73-one-loop-running"></span>

$$
\begin{aligned}
\frac{d}{d\ln\mu}\frac1{\alpha(\mu)}
&=\frac{b_0}{2\pi},\\
\frac1{\alpha(\mu)}
&=\frac1{\alpha(\mu_0)}+\frac{b_0}{2\pi}\ln\frac{\mu}{\mu_0},\\
\alpha(\mu)
&=\frac{\alpha(\mu_0)}
 {1+\dfrac{b_0\alpha(\mu_0)}{2\pi}\ln(\mu/\mu_0)}.
\end{aligned}
\tag{73.39}
$$

向高能走，分母增加，原来由小耦合控制的圈展开越来越可靠；
向低能走，分母减小，更高圈项逐渐不能忽略。
将积分常数改记为一个质量尺度，可以写成

<span id="eq:c73-generated-scale"></span>

$$
\Lambda
=\mu_0\exp\!\left[-\frac{2\pi}{b_0\alpha(\mu_0)}\right],
\qquad
\alpha(\mu)=\frac{2\pi}{b_0\ln(\mu/\Lambda)} .
\tag{73.40}
$$

这是本次一圈运行所引出的尺度。公式适用于$\alpha(\mu)$足够小的区域；
靠近$\Lambda$时，解所显示的增长提示微扰方法已到边界。
在$\overline{\mathrm{MS}}$完整理论中，重味不会自动从$b_0$消失。
若跨越物质质量后采用较低能的有效理论，应按第66节的阈值办法重新匹配，
再在各自味数固定的区间使用此式。

低能强耦合引出了色禁闭的问题。夸克、胶子用于描述短距离过程，
而可孤立制备的强子按色单态组织；没有观察到孤立带色粒子，是这一物理图像的经验动机。
将有限能量物理态的整体色不变性作为禁闭的表述，还需要非微扰动力学来支持。
上面的圈积分建立了高能渐近自由，并说明向低能推进时微扰展开为何失去控制，
却不能在失去控制的区域继续用一圈解证明禁闭。

复标量和多种物质表示也会改变贝塔函数。下面继续计算这些贡献，并从已有的极点求质量与场的反常维数。

<span id="c73-scalar"></span>

## 一个复标量的贡献

把[第72节的复标量顶角](/posts/srednicki-72/#c72-scalar)接成圈。取$D_\mu=\partial_\mu-ig_d A_\mu^aT_R^a$，其中$g_d=g\widetilde\mu^{\epsilon/2}$，所有标度导数都固定裸参数。沿用一胶子的动量和式顶角、两胶子的反对易子接触顶角。

规范场二点函数有两种标量图：两只三价顶角连成的泡图，以及一只四价顶角上闭合标量线的接触图。泡图的色指标沿闭线求和，接触图则对反对易子取迹，分别给出
<span id="eq:c73-ex-scalar-color-traces"></span>

$$
\begin{aligned}
\sum_{i,j}(T_R^a)_{ij}(T_R^b)_{ji}
 &=\operatorname{Tr}_R(T_R^aT_R^b)=T(R)\delta^{ab},\\
\operatorname{Tr}_R\{T_R^a,T_R^b\}
 &=2T(R)\delta^{ab}.
\end{aligned}
\tag{73.42}
$$

与标量电动力学比较，两幅图都只需把$e^2$换成$g^2T(R)\delta^{ab}$。第二行的$2$正是阿贝尔海鸥顶角已有的$2$，不再增加一次。标量是复玻色场，没有闭费米圈的负号，也不再把反粒子单独计成另一个复场。

[第65节](/posts/srednicki-65/#c65-photon)已经将这两幅图相加，利用参数移位和径向分部积分得到横向结果。这里没有内部规范场线，所以移用这一标量圈结果不涉及把朗道规范的物质场因子换成费曼规范。把它按上述色因子改写为
<span id="eq:c73-ex-scalar-polarization"></span>

$$
\begin{aligned}
\Pi_{\mu\nu,{\rm s}}^{ab}(k)
 &=\delta^{ab}(k^2g_{\mu\nu}-k_\mu k_\nu)
                  \Pi_{\rm s}(k^2),\\
\Pi_{\rm s}(k^2)
 &=-\frac{g^2T(R)}{i}\int_0^1dx\,(1-2x)^2J_2(D),\\
D&=m_{\rm s}^2+x(1-x)k^2-i0,\qquad
J_2(D)=\widetilde\mu^\epsilon
       \int\frac{d^d\ell}{(2\pi)^d}\frac1{(\ell^2+D)^2}.
\end{aligned}
\tag{73.43}
$$

这里$\Pi_{\rm s}$只含圈图，一粒子不可约插入是$i\Pi_{\mu\nu,{\rm s}}^{ab}$。提取紫外极点时可先保留$m_{\rm s}>0$并取欧氏型离壳外动量，以免混入无标度积分的红外零点。第65节的积分公式和这里的色因子给
<span id="eq:c73-ex-scalar-pole"></span>

$$
\begin{aligned}
J_2(D)&=\frac{i}{16\pi^2}
 \left[\frac2\epsilon-\ln\frac D{\mu^2}
                                  +O(\epsilon)\right],\\
\int_0^1(1-2x)^2dx
 &=\left[x-2x^2+\frac43x^3\right]_0^1=\frac13,\\
\left.\Pi_{\rm s}(k^2)\right|_{\rm pole}
 &=-\frac{g^2T(R)}{24\pi^2\epsilon}.
\end{aligned}
\tag{73.44}
$$

圈积分的$i$与式中$1/i$相消。规范动能反项对横向标量系数的贡献为$-\delta Z_3$，所以新增的标量极点由
<span id="eq:c73-ex-scalar-z3"></span>

$$
\Delta_{\rm s}Z_3
 =-\frac{g^2T(R)}{24\pi^2\epsilon}
 =-\frac13T(R)\frac{g^2}{8\pi^2\epsilon}
\tag{73.45}
$$

消去。符号$\Delta_{\rm s}$表示加入这个标量后的一圈增量。

接下来要从场的反项得到公共规范耦合的反项。使用式[（73.4）](#eq:c73-common-bare-coupling)中不同顶角给出同一个裸耦合的Slavnov–Taylor关系。其无规范反常及相容重整化条件见[第74节](/posts/srednicki-74/#c74-st)；仅用标量电动力学中的$Z_1=Z_2$不足以代替这一非阿贝尔关系。选择鬼—鬼—胶子顶角定义公共耦合，有
<span id="eq:c73-ex-ghost-bare-coupling"></span>

$$
g_0=\widetilde\mu^{\epsilon/2}g\,\mathcal Z_g,
\qquad
\mathcal Z_g=\frac{Z_1'}{Z_2'\sqrt{Z_3}} .
\tag{73.46}
$$

撇号标一粒子不可约鬼顶角和鬼动能的重整化因子。鬼没有直接的标量顶角；要在鬼二点或一粒子不可约鬼三点图中加入标量闭圈，至少需要两圈。外胶子腿上的一圈标量自能则属于$Z_3$。因此新增物质在一圈只改变这个比值中的$Z_3$，从而
<span id="eq:c73-ex-scalar-coupling-pole"></span>

$$
\Delta_{\rm s}\ln\mathcal Z_g
 =-\frac12\Delta_{\rm s}Z_3
 =\frac{g^2T(R)}{48\pi^2\epsilon}.
\tag{73.47}
$$

把它加到[上面求得的纯杨—米尔斯结果](#c73-beta)，便有
<span id="eq:c73-ex-scalar-total-pole"></span>

$$
\begin{aligned}
\ln\mathcal Z_g&=\frac{a(g)}{\epsilon}
                         +\text{更高圈极点},\\
a(g)&=-\frac{g^2}{16\pi^2}b_{\rm s},\qquad
b_{\rm s}=\frac{11}{3}T(A)-\frac13T(R).
\end{aligned}
\tag{73.48}
$$

最后在固定非零$g$的定号区间，对$\ln|g_0|$求导。由本节的$d$维运行式$B_g:=dg/dt=-\epsilon g/2+\beta_g$，
<span id="eq:c73-ex-scalar-beta"></span>

$$
\begin{aligned}
0&=\frac{B_g}{g}+\frac{\epsilon}{2}
                          +\frac{a'(g)}{\epsilon}B_g+\cdots,\\
0\big|_{\text{一圈有限}}
 &=\frac{\beta_g}{g}-\frac g2a'(g),\\
\beta_g&=\frac{g^2}{2}a'(g)
        =-\left[\frac{11}{3}T(A)-\frac13T(R)\right]
                       \frac{g^3}{16\pi^2}
          +\text{更高圈}.
\end{aligned}
\tag{73.49}
$$

第二行保留了工程项$-\epsilon g/2$与简单极点相乘得到的有限贡献。量子$\beta_g$再作用于一圈极点属于更高圈，须与那一阶的极点一起组织。贝塔函数在$g=0$处由最后的多项式连续延拓。

这里的计数单位是一个复标量。若表示允许施加与规范变换相容的实条件，同一表示中的一个复场可写成$\varphi=(\varphi_1+i\varphi_2)/\sqrt2$，其动能分成两份各带$1/2$的实场动能。每份实场的高斯积分给$(\det K)^{-1/2}$，两份相乘才是复场的$(\det K)^{-1}$。因此一个实标量的系数为$T(R)/6$，一个复标量的系数为$T(R)/3$。真复表示上的复场不能直接施加该实条件；若改用实化表示，其迹指标为$T(R_{\mathbb R})=2T(R)$，故$T(R_{\mathbb R})/6=T(R)/3$，最终计数相同。

<span id="c73-general-matter"></span>

## 不同表示的物质场

现在令$\Psi_i$为表示$R_i$中的狄拉克场，$\varphi_j$为表示$R'_j$中的复标量。指标$i,j$在这里列举物质多重态，同一个表示出现多次就列多次。各个闭圈只能沿着同一种场闭合，所以不同场的贡献相加；每个圈的群因子分别为$T(R_i)$或$T(R'_j)$。

狄拉克圈的闭圈负号和旋量迹已经包含在[第66节的参数权重](/posts/srednicki-66/#eq:c66-spin-weights)中。与复标量并列，它们是
<span id="eq:c73-ex-matter-weights"></span>

$$
w_{\rm F}=\int_0^1 8x(1-x)\,dx=\frac43,
\qquad
w_{\rm s}=\int_0^1(1-2x)^2dx=\frac13 .
\tag{73.50}
$$

这里$w_{\rm F}$对应一个完整狄拉克场，$w_{\rm s}$对应一个复标量，已经分别计入旋量分量与两种标量荷支。把这些权重乘上各自的表示迹，再与[胶子和鬼圈](#c73-gluon)相加，费曼规范下的规范场因子为
<span id="eq:c73-ex-general-z3"></span>

$$
Z_3=1+\left[
 \frac53T(A)-\frac43\sum_iT(R_i)-\frac13\sum_jT(R'_j)
 \right]\frac{g^2}{8\pi^2\epsilon}
 +\text{更高圈}.
\tag{73.51}
$$

一圈鬼顶角比值仍没有新增的物质圈，因此与单个复标量的计算相同，每个物质项只通过$-\,\tfrac12\ln Z_3$进入$\ln\mathcal Z_g$。定义
<span id="eq:c73-ex-general-b0"></span>

$$
\begin{aligned}
b_0&=\frac{11}{3}T(A)
       -\frac43\sum_iT(R_i)-\frac13\sum_jT(R'_j),\\
\ln\mathcal Z_g&=-\frac{b_0g^2}{16\pi^2\epsilon}
                       +\text{更高圈极点}.
\end{aligned}
\tag{73.52}
$$

在式[（73.49）](#eq:c73-ex-scalar-beta)中以$b_0$代替$b_{\rm s}$，得到
<span id="eq:c73-ex-general-beta"></span>

$$
\begin{aligned}
\beta_g&=-\frac{g^3}{16\pi^2}
 \left[\frac{11}{3}T(A)-\frac43\sum_iT(R_i)
                         -\frac13\sum_jT(R'_j)\right]
 +\text{更高圈},\\
\beta_\alpha&=\frac{g}{2\pi}\beta_g
 =-\frac{b_0}{2\pi}\alpha^2+\text{更高圈},
\qquad \alpha=\frac{g^2}{4\pi}.
\end{aligned}
\tag{73.53}
$$

第一行中若有$n_F$个相同的狄拉克表示$R$而没有标量，便恢复式[（73.37）](#eq:c73-gauge-beta)；若没有狄拉克场而只有一个复标量，便恢复单个复标量的结果。也可把颜色因子换成阿贝尔电荷因子$T(A)=0$、$T(R_i)=Q_i^2$、$T(R'_j)=Q_j^2$，于是
<span id="eq:c73-ex-abelian-check"></span>

$$
\beta_e=\frac{e^3}{12\pi^2}
 \left(\sum_iQ_i^2+\frac14\sum_jQ_j^2\right)
 +\text{更高圈}.
\tag{73.54}
$$

这与第66节的结果一致。在其$e<0$的荷号约定下，$\beta_e<0$而$\beta_\alpha>0$，物质贡献仍使电荷的绝对值随能标增大。

式[（73.53）](#eq:c73-ex-general-beta)属于给定场内容的$\overline{\mathrm{MS}}$理论。由于简单极点与物质质量无关，重粒子不会在这条公式里自行退耦；若能标降到某些质量以下，要另作有效理论匹配并改变求和的场内容。对于弱耦合的高能区，$b_0>0$给出渐近自由，物质场的增加则减小$b_0$。

<span id="c73-anomalous"></span>

## 质量、夸克场和胶子场的反常维数

现在回到只含狄拉克物质的理论：$n_F$个狄拉克场都处在表示$R$中，不另加标量。$m$指其中一个夸克的重整化质量，取$m>0$以便使用对数导数。式[（73.2）](#eq:c73-bare-fields)已经给出$m_0=mZ_m/Z_2$及两个裸场的平方根因子。沿[第66节](/posts/srednicki-66/#c66-anomalous)的约定，定义
<span id="eq:c73-ex-gamma-definitions"></span>

$$
\begin{aligned}
\gamma_m&=\frac{d\ln m}{dt},&
\gamma_\Psi&=\frac12\frac{d\ln Z_2}{dt},&
\gamma_A&=\frac12\frac{d\ln Z_3}{dt},\\
\left.\frac{d\Psi}{dt}\right|_{\Psi_0}
 &=-\gamma_\Psi\Psi,&
\left.\frac{dA_\mu^a}{dt}\right|_{A_0}
 &=-\gamma_AA_\mu^a .
\end{aligned}
\tag{73.55}
$$

场的运行式有负号，来自固定裸场后对平方根求导。$\gamma_m$定义中的$m$是有量纲的质量；若考察$m/\mu$，其对数导数才是$\gamma_m-1$。

由式[（73.6）](#eq:c73-quark-counterterms)，$Z_m$中的质量极点系数为$4C_R$，$Z_2$中的动能极点系数为$C_R$，所以$\ln(Z_m/Z_2)=-3C_Rg^2/(8\pi^2\epsilon)+O(g^4)$。

对于一圈简单极点$\ln Z=a(g)/\epsilon+\cdots$，让本节的$d$维运行式$dg/dt=-\epsilon g/2+\beta_g$中的工程项作用于它，可得
<span id="eq:c73-ex-pole-derivative"></span>

$$
\left.\frac{d\ln Z}{dt}\right|_{\text{一圈有限}}
 =\frac1\epsilon\left(-\frac{\epsilon g}{2}\right)
                         \frac{da}{dg}
 =-\frac g2\frac{da}{dg}.
\tag{73.56}
$$

规范参数在固定裸规范参数时也有量子运行，但其导数作用于一圈极点的贡献从更高圈开始。因此可将所需一圈系数直接在$\xi=1$处评价。

把式[（73.6）](#eq:c73-quark-counterterms)的$Z_2$代入，得到
<span id="eq:c73-ex-quark-gamma"></span>

$$
\begin{aligned}
\gamma_\Psi
 &=-\frac14g\frac{d}{dg}
           \left(-\frac{C(R)g^2}{8\pi^2}\right)\\
 &=\frac{C(R)g^2}{16\pi^2}+O(g^4)
  =\frac{C(R)\alpha}{4\pi}+O(\alpha^2).
\end{aligned}
\tag{73.57}
$$

胶子因子取式[（73.32）](#eq:c73-three-renormalization-factors)中的$Z_3$。它既含纯规范圈，又含$n_F$个狄拉克圈，所以
<span id="eq:c73-ex-gluon-gamma"></span>

$$
\begin{aligned}
\gamma_A
 &=-\frac14g\frac{d}{dg}
 \left\{\left[\frac53T(A)-\frac43n_FT(R)\right]
                                  \frac{g^2}{8\pi^2}\right\}\\
 &=-\left[\frac53T(A)-\frac43n_FT(R)\right]
                         \frac{g^2}{16\pi^2}+O(g^4).
\end{aligned}
\tag{73.58}
$$

这两个场反常维数依赖规范选择，以上数值对应费曼规范。它们描述重整化场随标度的归一变化，不能直接当作某个规范不变可观测量的标度指数。

质量的导数再由$m_0$固定给出：
<span id="eq:c73-ex-mass-gamma"></span>

$$
\begin{aligned}
0=\frac{d\ln m_0}{dt}
 &=\gamma_m+\frac{d}{dt}\ln\frac{Z_m}{Z_2},\\
\frac{d}{dt}\ln\frac{Z_m}{Z_2}
 &=-\frac g2\frac{d}{dg}
            \left(-\frac{3C(R)g^2}{8\pi^2}\right)+O(g^4)\\
 &=\frac{3C(R)g^2}{8\pi^2}+O(g^4),\\
\gamma_m&=-\frac{3C(R)g^2}{8\pi^2}+O(g^4)
          =-\frac{3C(R)\alpha}{2\pi}+O(\alpha^2).
\end{aligned}
\tag{73.59}
$$

因此在上述反常维数定义下，弱耦合区的$\overline{\mathrm{MS}}$夸克质量随能标升高而减小。无质量点用$\beta_m=\gamma_m m$表达这一乘法运行。若将$T(A)$设为零并取一个单位电荷狄拉克场，式[（73.57）](#eq:c73-ex-quark-gamma)、[（73.58）](#eq:c73-ex-gluon-gamma)和[（73.59）](#eq:c73-ex-mass-gamma)分别还原[第66节](/posts/srednicki-66/#c66-anomalous)的$\gamma_\Psi=e^2/(16\pi^2)$、$\gamma_A=e^2/(12\pi^2)$与$\gamma_m=-3e^2/(8\pi^2)$，质量的负号和场的平方根因子由此相互吻合。

下一节将从规范固定后的BRST对称性出发，说明共同裸耦合关系所需的量子条件。

---

[← 第 72 节](/posts/srednicki-72/) · [章节地图](/srednicki/) · [第 74 节 →](/posts/srednicki-74/)
