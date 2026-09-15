---
title: 'Srednicki §74 BRST 对称性'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [74]
hideFromHome: true
draft: false
---

<span id="c74"></span>

规范固定使自由场的二次算符可逆，因而可以定义传播子，却也使拉格朗日密度
失去了原来的局域规范不变性。
上一节仍然要求不同顶角给出同一个裸耦合常数。这一要求究竟由什么对称性保证？
另一个相关的问题是，协变规范引入了四种规范场偏振和两种鬼场，而散射的外态
只应含物质粒子和两种横向规范玻色子。我们需要一种能在规范固定以后继续使用的
对称性，同时回答这两个问题。

这就是本节的BRST对称性，名称来自Becchi、Rouet、Stora和Tyutin。
它把规范场、物质场与鬼场联系起来。先构造这种变换，
再用它写出规范固定项，最后考察它在态空间中的意义。
最后[直接求出偏振改变的恰当原像](#c74-polarization-shift)。

<span id="c74-nilpotence"></span>

## 从规范变换到幂零变换

把规范场和物质场的规范不变密度合记为$\mathcal L_{\rm YM}$。
物质场$\varphi_i$可以是标量，也可以是旋量，生成元$T_R^a$作用在它的群指标上。
第70节所取的负相位约定给出无穷小变换

<span id="eq:c74-gauge-input"></span>

$$
\begin{aligned}
\delta A_\mu^a&=-D_\mu^{ab}\theta^b,&
\delta\varphi_i&=-ig\theta^a(T_R^a)_{ij}\varphi_j,\\
D_\mu^{ab}&=\delta^{ab}\partial_\mu-gf^{abc}A_\mu^c,&
[T_R^a,T_R^b]&=if^{abc}T_R^c .
\end{aligned}
\tag{74.1}
$$

现在引入伴随表示的格拉斯曼奇标量$c^a(x)$，将$-\theta^a$换成$c^a$。
所得变分记为$s$：

<span id="eq:c74-brst-definition"></span>

$$
\begin{aligned}
sA_\mu^a&=(D_\mu c)^a
          =\partial_\mu c^a-gf^{abc}A_\mu^cc^b,\\
s\varphi_i&=igc^a(T_R^a)_{ij}\varphi_j,\\
s(XY)&=(sX)Y+(-1)^{|X|}X(sY),\qquad
s\partial_\mu=\partial_\mu s .
\end{aligned}
\tag{74.2}
$$

$|X|$是$X$的格拉斯曼奇偶性。由于$c$是奇的，$s$也必须是奇变分：
它通过一个奇因子时多出负号。若希望变换本身保持每个场的奇偶性，可以引入
置于最左边的奇常数$\eta$，写$\delta_\eta\Phi=\eta s\Phi$。
这时$\delta_\eta$是普通的偶变换，乘积法则恢复通常的形式。
规范不变密度对任意函数$\theta^a(x)$的变分为零，把这个函数换成$-\eta c^a(x)$，
仍然得到

<span id="eq:c74-invariant-density"></span>

$$
s\mathcal L_{\rm YM}=0 .
\tag{74.3}
$$

还没有规定$c$自身怎样变换。选择这一变换的原则，是要求$s$具有幂零性，即连续作用两次给零。先在物质场上计算：

<span id="eq:c74-matter-nilpotence"></span>

$$
\begin{aligned}
s^2\varphi
 &=ig(sc^a)T_R^a\varphi-igc^aT_R^a(s\varphi)\\
 &=ig(sc^a)T_R^a\varphi
   +g^2c^ac^bT_R^aT_R^b\varphi\\
 &=ig\left(sc^c+\frac g2 f^{abc}c^ac^b\right)T_R^c\varphi .
\end{aligned}
\tag{74.4}
$$

第一行的负号来自$s$越过$c^a$。第二行的系数是$(-i)(i)g^2=+g^2$；
最后一行用了$c^ac^b=-c^bc^a$，所以矩阵积只留下
$c^ac^b[T_R^a,T_R^b]/2$。因此在李代数上规定

<span id="eq:c74-ghost-transform"></span>

$$
sc^a=-\frac g2 f^{abc}c^bc^c .
\tag{74.5}
$$

这个规定适用于所有物质表示。若仅从某一个物质表示中的$s^2\varphi=0$
反推它，则须该表示忠实；例如规范单态的生成元全为零，不能用它确定$sc$。
把式[（74.5）](#eq:c74-ghost-transform)作为规范李代数本身的变换规则，就没有这个问题。

接着检验规范场。把协变导数中显含$A$的一项也作变分，得到

<span id="eq:c74-vector-nilpotence-start"></span>

$$
\begin{aligned}
s^2A_\mu^a
 &=D_\mu^{ab}sc^b-gf^{abc}(sA_\mu^c)c^b\\
 &=D_\mu^{ab}sc^b-gf^{abc}(\partial_\mu c^c)c^b
   +g^2f^{abc}f^{cde}A_\mu^ec^dc^b .
\end{aligned}
\tag{74.6}
$$

第二项已有反对称的$f^{abc}$，故可将后面的乘积对$b,c$反对称化。
导数$\partial_\mu c$仍是奇量，于是

<span id="eq:c74-ghost-derivative-antisymmetry"></span>

$$
\begin{aligned}
(\partial_\mu c^{[c})c^{b]}
 &=\frac12(\partial_\mu c^c)c^b
   -\frac12(\partial_\mu c^b)c^c\\
 &=\frac12(\partial_\mu c^c)c^b
   +\frac12c^c(\partial_\mu c^b)
 =\frac12\partial_\mu(c^cc^b).
\end{aligned}
\tag{74.7}
$$

第三项中的$c^dc^b$同样只选取颜色系数对$b,d$的反对称部分。
用第70节的伴随生成元$(T_A^b)_{ac}=-if^{bac}$，这一部分可以直接算成

<span id="eq:c74-adjoint-jacobi"></span>

$$
\begin{aligned}
\frac12\left(f^{abc}f^{cde}-f^{adc}f^{cbe}\right)
 &=-\frac12[T_A^b,T_A^d]_{ae}\\
 &=-\frac i2 f^{bdh}(T_A^h)_{ae}
 =-\frac12 f^{bdh}f^{hae}.
\end{aligned}
\tag{74.8}
$$

将两式放回去，导数部分和含$A$部分恰好拼成同一个协变导数：

<span id="eq:c74-vector-nilpotence-end"></span>

$$
\begin{aligned}
s^2A_\mu^a
 &=D_\mu^{ab}sc^b-\frac g2f^{abc}\partial_\mu(c^cc^b)
   -\frac{g^2}{2}f^{bdh}f^{hae}A_\mu^ec^dc^b\\
 &=D_\mu^{ah}\left(sc^h+\frac g2 f^{bch}c^bc^c\right)=0 .
\end{aligned}
\tag{74.9}
$$

要在任意场的多项式上使用$s^2=0$，还须检验鬼场本身。
先按奇乘积法则作用，再将第一项的$b,c$交换，便有

<span id="eq:c74-ghost-nilpotence"></span>

$$
\begin{aligned}
s^2c^a
 &=-\frac g2 f^{abc}\bigl[(sc^b)c^c-c^b(sc^c)\bigr]\\
 &=\frac{g^2}{4}f^{abc}f^{bde}c^dc^ec^c
   -\frac{g^2}{4}f^{abc}f^{cde}c^bc^dc^e\\
 &=-\frac{g^2}{2}f^{abc}f^{cde}c^bc^dc^e\\
 &=-\frac{g^2}{6}
 \left(f^{abc}f^{cde}+f^{adc}f^{ceb}+f^{aec}f^{cbd}\right)c^bc^dc^e=0 .
\end{aligned}
\tag{74.10}
$$

三个鬼的循环置换是偶置换，所以倒数第二行可以换成最后一行的循环平均。
括号内正是雅可比恒等式。现在$s^2$在每个基本场上为零；又因为$s$是奇导数，
两次作用于乘积时的交叉项互相抵消，$s^2$在任意局域场多项式上也为零。

<span id="c74-gauge-fixing"></span>

## 用一个恰当项固定规范

已有$c$还不足以写出第71节的鬼作用量，我们再引入独立的反鬼场$\bar c^a$
和格拉斯曼偶辅助场$B^a$，规定

<span id="eq:c74-antighost-doublet"></span>

$$
s\bar c^a=B^a,\qquad sB^a=0 .
\tag{74.11}
$$

因此反鬼也满足$s^2\bar c=0$。$B$不必有自己的传播自由度；它的作用是使
这个等式在使用任何运动方程以前就成立。$c$与$\bar c$在路径积分中是两个
独立的格拉斯曼积分变量，第71节的行列式表示并不要求把一个当成另一个的共轭。
它们的算符伴随关系将在构造守恒荷时固定。

由于$s^2=0$，任何形如$sO$的项都在BRST变换下不变。这类项称为
BRST恰当项（BRST-exact term）。为了得到协变规范，选择奇函数

<span id="eq:c74-gauge-fermion"></span>

$$
\begin{aligned}
\mathcal L&=\mathcal L_{\rm YM}+sO,\\
O&=\bar c^a\left(\frac\xi2B^a-G^a\right),\qquad
G^a=\partial^\mu A_\mu^a .
\end{aligned}
\tag{74.12}
$$

$O$常称为规范固定费米子（gauge-fixing fermion）；这里的“费米子”指奇偶性，
它并非旋量。这个$O$使$B$至多二次、规范条件对$A$线性。
逐项作用$s$时，越过反鬼的负号很关键：

<span id="eq:c74-exact-gauge-density"></span>

$$
\begin{aligned}
sO
 &=(s\bar c^a)\left(\frac\xi2B^a-\partial^\mu A_\mu^a\right)
  -\bar c^a\left(\frac\xi2sB^a-\partial^\mu sA_\mu^a\right)\\
 &=\frac\xi2B^aB^a-B^a\partial^\mu A_\mu^a
     +\bar c^a\partial^\mu D_\mu^{ab}c^b .
\end{aligned}
\tag{74.13}
$$

最后一项就是Faddeev–Popov项。将它的一次导数分部积分，可用只含场的一阶
导数的密度代替原密度：

<span id="eq:c74-first-order-density"></span>

$$
\begin{aligned}
\mathcal L'
 &=\mathcal L_{\rm YM}+\frac\xi2B^aB^a-B^a\partial^\mu A_\mu^a
       -(\partial^\mu\bar c^a)D_\mu^{ab}c^b,\\
\mathcal L-\mathcal L'
 &=\partial_\mu\left[\bar c^a(D^\mu c)^a\right].
\end{aligned}
\tag{74.14}
$$

取边界处场的适当衰减，两者给出相同的作用量$S=\int d^4x\,\mathcal L$。
$B$没有动能，它的运动方程是$\xi B^a-G^a=0$。
在$\xi\ne0$时，对$B$积分也能直接说明为什么可以代回这个方程：

<span id="eq:c74-auxiliary-gaussian"></span>

$$
\begin{aligned}
\frac\xi2B^2-BG
 &=\frac\xi2\left(B-\frac G\xi\right)^2-\frac{G^2}{2\xi},\\
\int\mathcal DB\,
 e^{\,i\int(\xi B^2/2-BG)}
 &=\mathcal N_\xi\,
 e^{-i\int G^2/(2\xi)},\\
\mathcal L'_{\rm red}
 &=\mathcal L_{\rm YM}-\frac1{2\xi}(\partial\cdot A^a)^2
       -(\partial^\mu\bar c^a)D_\mu^{ab}c^b .
\end{aligned}
\tag{74.15}
$$

平移$B\mapsto B-G/\xi$的雅可比因子为一。带收敛处方的振荡高斯积分只留下
与场无关的$\mathcal N_\xi$，它在归一化关联函数中约去。这样就恢复了第71节的
$R_\xi$规范作用量。Landau规范可在保留$B$的表达式中直接取$\xi=0$，
此时$B$积分给$\delta[G]$，不必使用含$1/\xi$的式子。

保留$B$还有一个代数上的好处。若在变换规则中也代入$B=G/\xi$，则

<span id="eq:c74-onshell-antighost"></span>

$$
s^2\bar c^a=\xi^{-1}\partial^\mu(D_\mu c)^a .
\tag{74.16}
$$

右边要用反鬼变分所得的鬼场方程才为零。这时幂零性只在壳上成立；保留辅助场时，
式[（74.11）](#eq:c74-antighost-doublet)给出的幂零性则是离壳的。
推导量子恒等式时，我们使用保留$B$的形式。

<span id="c74-st"></span>

## 对称性怎样约束重整化

现在的作用量同时保留洛伦兹对称性、常数参数的全局规范对称性以及BRST对称性。
它还具有两种容易从式[（74.14）](#eq:c74-first-order-density)看出的对称性。
首先，给$c$指定鬼数$+1$、$\bar c$指定鬼数$-1$，其余场的鬼数为零，
每一项的总鬼数都为零。其次，反鬼只通过导数出现，故常数奇平移
$\bar c^a(x)\mapsto\bar c^a(x)+\chi^a$不改变作用量。
如果物质相互作用还保持$P,T,C$，这些离散对称性也继续成立。
若选择手征耦合或破坏这些对称性的物质势，就应相应改变反项的限制条件。

BRST对称性的量子内容可以先从路径积分的变量代换看出。
令$\Phi_I$遍历所有场，把外源放在右边，定义

<span id="eq:c74-source-functional"></span>

$$
Z[J]=\int\mathcal D\Phi\,
 \exp\!\left[iS+i\int d^4x\,\sum_I\Phi_IJ_I\right].
\tag{74.17}
$$

外源与相应场有相同奇偶性，故指数为偶。进行
$\Phi_I\mapsto\Phi_I+\eta s\Phi_I$；在作用量和正则化后的积分测度都不变的条件下，
积分值不变。把公共参数$\eta$移至最左，并比较它的一次项，得到

<span id="eq:c74-brst-ward-identity"></span>

$$
\int d^4x\,\sum_I\langle s\Phi_I(x)\rangle_J J_I(x)=0 .
\tag{74.18}
$$

这是一组关联函数恒等式：对外源继续求导、最后令$J=0$，就得到含不同场插入的
关系。由于$sA$和$sc$中有场的乘积，变换中会出现复合算符；若转成一粒子不可约
顶角的恒等式，须同时为这些复合变分引入外源并进行重整化。
所得非阿贝尔恒等式就是斯拉夫诺夫—泰勒恒等式。

量子理论还要处理测度和反项中的规范反常。若前几圈已经满足恒等式，下一圈的破缺是局域泛函，且满足线性化BRST一致性条件；其中BRST恰当的部分可以用有限反项消去。这样，在规范反常消失时，恒等式可以逐圈恢复。对于四维半单规范群，物质耦合取完备的可重整化形式，并保持相容的规范固定恒等式后，允许的局域反项除场与规范固定的重定义外，可以选为规范不变量。这两项结果分别见Barnich、Brandt和Henneaux的[第2.6节](https://arxiv.org/pdf/hep-th/0002245v3#page=17)和[第12.2节](https://arxiv.org/pdf/hep-th/0002245v3#page=119)。[^c74-external-conversion]

[^c74-external-conversion]:
    该文§2用反厄米生成元。
    转到本节约定为$T_{\rm ref}=-iT_R$、$e_{\rm ref}=g$、
    $\varepsilon_{\rm ref}=-\theta$、$C_{ \rm ref}=c$；
    §2.6的$s\bar C=ib$对应$\bar C=i\bar c$、$b=B$。

这项结果说明反项的组织方式。局域性与幂次计数先把候选项限制为质量维数不超过四
的局域多项式；规范不变性再把规范场动能、三点和四点相互作用组合进同一个
$F_{0\mu\nu}^aF_0^{a\mu\nu}$。物质动能则包含同一个协变导数
$D_{0\mu}=\partial_\mu-ig_0A_{0\mu}^aT_R^a$。规范固定与鬼项一起由
BRST恰当项决定。每个简单群因子于是有一个规范耦合$g_0$；允许的质量、物质势
和汤川耦合各有自己的反项。

把第73节的裸场重定义代入这些局域算符，夸克、鬼、三胶子和四胶子顶角的系数
依次为

<span id="eq:c74-bare-vertex-coefficients"></span>

$$
g_0Z_2Z_3^{1/2},\qquad
g_0Z_2'Z_3^{1/2},\qquad
g_0Z_3^{3/2},\qquad g_0^2Z_3^2 .
\tag{74.19}
$$

分别与$g\widetilde\mu^{\epsilon/2}Z_1$、
$g\widetilde\mu^{\epsilon/2}Z_1'$、
$g\widetilde\mu^{\epsilon/2}Z_{3g}$和
$g^2\widetilde\mu^\epsilon Z_{4g}$比较，再除去场因子，就得到
式[（73.4）](/posts/srednicki-73/#eq:c73-common-bare-coupling)。
这里仍沿用上一节$d=4-\epsilon$的调节记号。
这补出了上一节共同裸耦合关系的根据，也说明它为什么以无规范反常为条件。
局域重整化定理的完整证明采用上述外引结果；
下一节将具体研究可能破坏这一条件的手征规范反常。

<span id="c74-charge"></span>

## 守恒荷及其伴随性质

BRST变换含一个常数奇参数，因此同其他连续对称性一样，可以用诺特方法构造
守恒流。不过，在式[（74.14）](#eq:c74-first-order-density)中已经作过一次分部积分，
这一步会影响流的表达式。用$s(Dc)=s^2A=0$和$s\bar c=B$计算，有

<span id="eq:c74-noether-boundary"></span>

$$
\begin{aligned}
s\mathcal L'
 &=-B^a\partial_\mu(D^\mu c)^a
     -(\partial_\mu B^a)(D^\mu c)^a
   =\partial_\mu K^\mu,\\
K^\mu&=-B^a(D^\mu c)^a .
\end{aligned}
\tag{74.20}
$$

对称的是作用量，一阶密度本身的变分是一个散度。求流时可以暂令参数为$\eta(x)$，
直接收集$\partial_\mu\eta$的系数。这样也能固定鬼场求导时的次序。
规范动能$-F^2/4$给$-F^{a\mu\nu}(D_\nu c)^a$；$-B\partial\cdot A$给
$-B^a(D^\mu c)^a$。鬼项的两个因子分别变分，所含参数导数为

<span id="eq:c74-local-parameter-ghost"></span>

$$
\begin{aligned}
\delta_\eta\mathcal L'_{\rm gh}\big|_{\partial\eta}
 &=- (\partial^\mu\eta)B^a(D_\mu c)^a
   -(\partial^\mu\bar c^a)(\partial_\mu\eta)sc^a\\
 &=(\partial_\mu\eta)
       \left[-B^a(D^\mu c)^a+(\partial^\mu\bar c^a)sc^a\right].
\end{aligned}
\tag{74.21}
$$

第二行把奇量$\partial_\mu\eta$移过奇量$\partial^\mu\bar c$，因此第二项变号。
加上物质密度给出的系数$j_{\rm matter}^\mu$，并将
$\eta\partial_\mu K^\mu$分部积分，守恒流便是

<span id="eq:c74-brst-current"></span>

$$
\begin{aligned}
j_B^\mu
 &=-F^{a\mu\nu}(D_\nu c)^a-B^a(D^\mu c)^a
       +(\partial^\mu\bar c^a)sc^a+j_{\rm matter}^\mu,\\
\delta_\eta S&=\int d^4x\,(\partial_\mu\eta)j_B^\mu,
\qquad \partial_\mu j_B^\mu=0\quad\hbox{在运动方程上}.
\end{aligned}
\tag{74.22}
$$

例如，实表示中的实标量密度为$-(D\varphi)^2/2-V$。
在局域参数变分中，$\delta_\eta(D_\mu\varphi)$多出
$(\partial_\mu\eta)igc^aT_R^a\varphi$，因此

<span id="eq:c74-matter-current"></span>

$$
\begin{aligned}
j_{\rm scalar}^\mu
 &=-igc^a(D^\mu\varphi)_i(T_R^a)_{ij}\varphi_j,\\
j_{\rm Dirac}^\mu
 &=-gc^a\bar\Psi\gamma^\mu T_R^a\Psi .
\end{aligned}
\tag{74.23}
$$

第二行来自$i\bar\Psi\gamma^\mu D_\mu\Psi$：含参数导数的项先是
$i\bar\Psi\gamma^\mu(\partial_\mu\eta)igc^aT_R^a\Psi$，把$\partial_\mu\eta$
移到最左、再把$c$移过$\bar\Psi$，就得到所示符号。
无导数的质量和势能项不给流增加参数导数项。
诺特流须包含所有场对局域参数导数的贡献，并减去
一阶密度变分中的$K^\mu$。流还可以增加一个反对称张量的散度；在空间边界项为零时，
这不改变守恒荷

<span id="eq:c74-charge-definition"></span>

$$
Q_B=\int d^3x\,j_B^0(x),\qquad
s\Phi=i[Q_B,\Phi]_{\rm gr} .
\tag{74.24}
$$

分级括号对偶场是对易子，对奇场是反对易子$\{X,Y\}=XY+YX$。
将各场的变换分别代入，五条生成关系为

<span id="eq:c74-charge-action"></span>

$$
\begin{aligned}
i[Q_B,A_\mu^a]&=(D_\mu c)^a,&
i\{Q_B,c^a\}&=-\frac g2f^{abc}c^bc^c,\\
i\{Q_B,\bar c^a\}&=B^a,&
i[Q_B,B^a]&=0,\\
i[Q_B,\varphi_i]_{\rm gr}
 &=igc^a(T_R^a)_{ij}\varphi_j .
\end{aligned}
\tag{74.25}
$$

为使作用量、BRST生成关系及内积相容，取

<span id="eq:c74-adjoint-convention"></span>

$$
\begin{gathered}
A_\mu^{a\dagger}=A_\mu^a,\qquad B^{a\dagger}=B^a,\qquad Q_B^\dagger=Q_B,\\
c^{a\dagger}=c^a,\qquad \bar c^{a\dagger}=-\bar c^a .
\end{gathered}
\tag{74.26}
$$

这一伴随选择与生成关系相互约束。若$Q_B$和$\bar c$都厄米，
则$i\{Q_B,\bar c\}$是反厄米的，不能等于实辅助场$B$。
取反鬼为反厄米以后，两边都厄米；在相容的局域乘积排序下，鬼密度
$-(\partial\bar c)Dc$在取伴随并将两个奇场交换回来后也保持不变。
这里仍有两个独立的鬼变量，前面路径积分的行列式与有向鬼线规则保持原有次序。

分级括号还把$s$的幂零性转为荷的性质：

<span id="eq:c74-central-square"></span>

$$
s^2\Phi=-[Q_B^2,\Phi] .
\tag{74.27}
$$

所以场上的幂零性首先说明$Q_B^2$与全部场对易。
在无BRST反常的量子实现中，取BRST不变的循环真空$Q_B|0\rangle=0$。
对任意场多项式$P$，有
$Q_B^2P|0\rangle=P Q_B^2|0\rangle=0$；这些态张成共同的稠密定义域，
因而在该域上得到荷的幂零性：

<span id="eq:c74-charge-nilpotence"></span>

$$
Q_B^2=0 .
\tag{74.28}
$$

在下面的自由场实现中，真空不变性和荷的幂零性还可直接核算。
相互作用理论则使用前面建立的量子恒等式及BRST不破缺的真空条件。

<span id="c74-cohomology"></span>

## 闭态、恰当态和物理等价类

在继续计算之前，先看厄米幂零荷对态空间意味着什么。
若在整个辅助态空间上使用正定内积，则任意$|\chi\rangle$都满足
$\|Q_B\chi\|^2=\langle\chi|Q_B^2|\chi\rangle=0$，从而$Q_B=0$。
非平凡的BRST荷因此是在含负范数及零范数态的辅助空间中实现的。
这种不定内积正是协变规范下的非物理模式所需要的；物理态的正定性要在取商以后判断。

我们称被$Q_B$湮灭的态为闭态（closed state），称能写成$Q_B|\chi\rangle$的态
为恰当态（exact state）。由于$Q_B^2=0$，每个恰当态都是闭态。
物理态由鬼数为零的BRST上同调给出：

<span id="eq:c74-physical-quotient"></span>

$$
\begin{aligned}
\mathcal H_{ \rm phys}
 &=\frac{\ker Q_B|_{{\rm gh}=0}}
         {\operatorname{im}Q_B|_{{\rm gh}=-1}},\\
|\psi'\rangle&\sim|\psi\rangle
\quad\Longleftrightarrow\quad
|\psi'\rangle=|\psi\rangle+Q_B|\chi\rangle .
\end{aligned}
\tag{74.29}
$$

第一行分母表示鬼数$-1$的态经$Q_B$映到鬼数零所得的子空间。
闭而非恰当的态代表这个商空间中的非零元素；商空间本身还包含零类。
相差恰当态的两个向量表示同一物理态，这是因为恰当态与所有闭态都正交：

<span id="eq:c74-exact-null"></span>

$$
\begin{aligned}
Q_B|\psi\rangle=0
 &\ \Longrightarrow\ \langle\psi|Q_B=0,\\
\langle\psi|Q_B|\chi\rangle&=0,\\
\langle Q_B\chi|Q_B\chi\rangle
 &=\langle\chi|Q_B^2|\chi\rangle=0 .
\end{aligned}
\tag{74.30}
$$

特别地，单位范数闭态不可能是恰当态。取商以后，闭态之间的内积不依赖代表的选择。
守恒荷满足$[H,Q_B]=0$，于是

<span id="eq:c74-time-evolution"></span>

$$
\begin{aligned}
Q_Be^{-iHt}|\psi\rangle&=e^{-iHt}Q_B|\psi\rangle,\\
e^{-iHt}Q_B|\chi\rangle&=Q_Be^{-iHt}|\chi\rangle .
\end{aligned}
\tag{74.31}
$$

第一行说明演化保持闭态，第二行说明演化也保持恰当态，因而在商空间上有良好的
定义。若$H$相对于辅助内积厄米，演化还保持范数。接下来要辨认这个商空间中的
粒子，确认它恰好具有预期的两种规范玻色子偏振。

<span id="c74-modes"></span>

## 自由渐近场及四种偏振

沿第5节的散射态构造，在渐近区使用自由场，并暂略去群指标。
以下模式计算取费曼规范$\xi=1$。这一选择可以从自由场方程看出来：

<span id="eq:c74-free-equations"></span>

$$
\begin{aligned}
\partial_\nu F^{\nu\mu}+\partial^\mu B&=0,&
\partial\cdot A&=\xi B,\\
\partial^2A_\mu&=(\xi-1)\partial_\mu B,&
\partial^2B= \partial^2c= \partial^2\bar c&=0 .
\end{aligned}
\tag{74.32}
$$

第一个方程取散度给$\partial^2B=0$。只有在$\xi=1$时，四个独立的$A_\mu$
分量都直接满足普通无质量波动方程；一般$\xi$还含非横向的额外解。
[偏振改变的推导](#c74-polarization-equations)将从场方程出发保留一般$\xi$。

记$\omega=|\mathbf k|>0$、$k\cdot x=-\omega t+\mathbf k\cdot\mathbf x$以及
$\widetilde{dk}=d^3k/[(2\pi)^3\,2\omega]$。按
式[（74.26）](#eq:c74-adjoint-convention)的伴随关系，模式展开为

<span id="eq:c74-free-expansions"></span>

$$
\begin{aligned}
A^\mu(x)
 &=\sum_{\lambda=>,<,+,-}\int\widetilde{dk}
  \left[\varepsilon_\lambda^{\mu *}a_\lambda(\mathbf k)e^{ikx}
       +\varepsilon_\lambda^\mu a_\lambda^\dagger(\mathbf k)e^{-ikx}\right],\\
c(x)&=\int\widetilde{dk}
  \left[c(\mathbf k)e^{ikx}+c^\dagger(\mathbf k)e^{-ikx}\right],\\
\bar c(x)&=\int\widetilde{dk}
  \left[b(\mathbf k)e^{ikx}-b^\dagger(\mathbf k)e^{-ikx}\right],\\
\varphi(x)&=\int\frac{d^3k}{(2\pi)^3\,2\omega_\varphi}
  \left[a_\varphi(\mathbf k)e^{ik_\varphi x}
       +a_\varphi^\dagger(\mathbf k)e^{-ik_\varphi x}\right].
\end{aligned}
\tag{74.33}
$$

最后一行选实表示中的实标量来简化记号；有质量时
$\omega_\varphi=\sqrt{\mathbf k^2+m^2}$，鬼场的能量则仍为$\omega=|\mathbf k|$。
反鬼的负频率项为$-b^\dagger$，这个负号由$\bar c^\dagger=-\bar c$确定。

将动量转到第三轴，取四个偏振矢量

<span id="eq:c74-polarization-basis"></span>

$$
\begin{gathered}
k^\mu=\omega(1,0,0,1),\qquad
\varepsilon_>^\mu=\frac1{\sqrt2}(1,0,0,1),\quad
\varepsilon_<^\mu=\frac1{\sqrt2}(1,0,0,-1),\\
\varepsilon_+^\mu=\frac1{\sqrt2}(0,1,-i,0),\qquad
\varepsilon_-^\mu=\frac1{\sqrt2}(0,1,i,0),\\
\varepsilon_>^2=\varepsilon_<^2=0,\qquad
\varepsilon_>\cdot\varepsilon_<=-1,\qquad
\varepsilon_\pm^*\cdot\varepsilon_\pm=1,\qquad
k\cdot\varepsilon_<=-\sqrt2\omega .
\end{gathered}
\tag{74.34}
$$

$\varepsilon_>$平行于$k$，$\varepsilon_<$沿相反的类光方向；它们组成不定内积的
非横向二元组。$\varepsilon_\pm$是两种横向圆偏振，彼此在厄米内积下正交。
这四个矢量的格拉姆矩阵足以反演模式展开，并给出规范场模的对易关系。
记$\Delta_{kq}=(2\pi)^3\,2\omega\delta^3(\mathbf k-\mathbf q)$，则

<span id="eq:c74-mode-brackets"></span>

$$
\begin{aligned}
\relax[a_<(\mathbf k),a_>^\dagger(\mathbf q)]
 &=[a_>(\mathbf k),a_<^\dagger(\mathbf q)]=-\Delta_{kq},\\
[a_\pm(\mathbf k),a_\pm^\dagger(\mathbf q)]&=+\Delta_{kq},\\
\{c(\mathbf k),b^\dagger(\mathbf q)\}
 &=\{b(\mathbf k),c^\dagger(\mathbf q)\}=-\Delta_{kq} .
\end{aligned}
\tag{74.35}
$$

未列出的鬼反对易子和不同偏振的对易子为零；物质模具有通常的正号归一。
鬼的符号也可从动能直接核对：自由鬼密度的时间部分为
$\dot{\bar c}\dot c$。固定右导数定义正则动量后，
$\pi_c=\dot{\bar c}$、$\pi_{\bar c}=-\dot c$，故等时关系为
$\{c,\dot{\bar c}\}=i\delta^3$、$\{\bar c,\dot c\}=-i\delta^3$。
代入式[（74.33）](#eq:c74-free-expansions)，两个异频率项各贡献一半空间$\delta$函数，
就得到式[（74.35）](#eq:c74-mode-brackets)的负号。

现在可以把自由荷完整算出。在$g=0$时，$sc=0$，物质电流也为零。
用自由场方程把式[（74.22）](#eq:c74-brst-current)中的第一项展开成散度，有

<span id="eq:c74-free-charge-position"></span>

$$
\begin{aligned}
j_B^\mu
 &=-\partial_\nu(F^{\mu\nu}c)
       +(\partial^\mu B)c-B\partial^\mu c,\\
Q_B&=\int d^3x\,[B\dot c-\dot Bc] .
\end{aligned}
\tag{74.36}
$$

第一行的反对称散度在$j^0$中只是空间边界项。第二行还用了$\partial^0=-\partial_0$。
写$\kappa=\sqrt2\omega$，偏振收缩给

<span id="eq:c74-free-charge-modes"></span>

$$
\begin{aligned}
B(x)&=\partial\cdot A(x)
 =\int\widetilde{dk}
       [-i\kappa a_<(\mathbf k)e^{ikx}
          +i\kappa a_<^\dagger(\mathbf k)e^{-ikx}],\\
Q_B&=\int\widetilde{dk}\,\kappa
       [a_<(\mathbf k)c^\dagger(\mathbf k)
           +a_<^\dagger(\mathbf k)c(\mathbf k)] .
\end{aligned}
\tag{74.37}
$$

例如$B$的正频率项与$c$的负频率项相乘，在$B\dot c$和$-\dot Bc$中各给
$\kappa\omega a_<c^\dagger$，合起来是$2\kappa\omega a_<c^\dagger$。
空间积分给$(2\pi)^3\delta^3(\mathbf k-\mathbf q)$，与两份测度中的一份
$1/[(2\pi)^3\,2\omega]$约去，留下第二行的系数$\kappa$。
另一个异频率项同样计算；同频率项的两个时间导数相消。
所得$Q_B$取伴随后两项互换，且每一项都含湮灭算符，因此$Q_B^\dagger=Q_B$、
$Q_B|0\rangle=0$。

用式[（74.35）](#eq:c74-mode-brackets)逐一对易，便得到

<span id="eq:c74-creation-transforms"></span>

$$
\begin{aligned}
\relax[Q_B,a_>^\dagger]&=-\kappa c^\dagger,&
[Q_B,a_<^\dagger]&=[Q_B,a_\pm^\dagger]=0,\\
\{Q_B,c^\dagger\}&=0,&
\{Q_B,b^\dagger\}&=-\kappa a_<^\dagger,\\
[Q_B,a_\varphi^\dagger]&=0 .
\end{aligned}
\tag{74.38}
$$

第一式也能直接由$i[Q_B,A^\mu]=\partial^\mu c$的负频率项读出：
左边是$i\varepsilon_>^\mu[Q_B,a_>^\dagger]$，右边是$-ik^\mu c^\dagger$，
而$k^\mu=\kappa\varepsilon_>^\mu$，所以必须取负号。
反鬼一式还须保留展开中的$-b^\dagger$：
将其代入$i\{Q_B,\bar c\}=B$的负频率部分，便得到所列的第二个负号。

<span id="c74-quartet"></span>

## 从单粒子到完整的物理福克空间

先让这些产生算符作用在真空上。$a_>^\dagger|0\rangle$与$b^\dagger|0\rangle$
经$Q_B$作用分别得到非零的鬼态与类光规范态，因而不是闭态。
另一方面，$a_<^\dagger|0\rangle$和$c^\dagger|0\rangle$虽然闭合，却分别是
$-Q_Bb^\dagger|0\rangle/\kappa$和$-Q_Ba_>^\dagger|0\rangle/\kappa$。
它们都属于零类。两种横向态及物质态则是正范数闭态，所以不是恰当态。

对任意闭态$|\psi\rangle$，仍有

<span id="eq:c74-single-exact"></span>

$$
\begin{aligned}
a_<^\dagger|\psi\rangle
 &=-\kappa^{-1}Q_Bb^\dagger|\psi\rangle,\\
c^\dagger|\psi\rangle
 &=-\kappa^{-1}Q_Ba_>^\dagger|\psi\rangle .
\end{aligned}
\tag{74.39}
$$

多个非物理产生算符也可能组成闭组合。要一并求出这些组合的恰当原像，固定一个非零动量及颜色，简记
$x=a_>^\dagger$、$y=c^\dagger$、$u=b^\dagger$、$v=a_<^\dagger$。
$x,v$是偶变量，$y,u$是奇变量。$Q_B$在产生算符多项式上的作用可写为

<span id="eq:c74-contracting-homotopy"></span>

$$
q=-\kappa\left(y\frac{\partial}{\partial x}
                   +v\frac{\partial}{\partial u}\right),\qquad
h=-\kappa^{-1}\left(x\frac{\partial}{\partial y}
                   +u\frac{\partial}{\partial v}\right),
\tag{74.40}
$$

其中奇偏导取左导数。$q$给出式[（74.38）](#eq:c74-creation-transforms)的两组变换，
$h$则把每组变换反向连接起来。直接在四个生成元上作用，得到

<span id="eq:c74-homotopy-number"></span>

$$
\begin{gathered}
\begin{array}{c|rrrr}
 &x&y&u&v\\ \hline
q&-\kappa y&0&-\kappa v&0\\
h&0&-x/\kappa&0&-u/\kappa\\
qh+hq&x&y&u&v
\end{array}\\[3pt]
\{q,h\}=N_{\rm aux}
 =x\partial_x+y\partial_y+u\partial_u+v\partial_v .
\end{gathered}
\tag{74.41}
$$

两个奇导数的反对易子是偶导数，故在生成元上相等，就在全部多项式上相等。
$N_{\rm aux}$数出非物理产生算符的总次数。若一个次数为$n>0$的多项式满足
$qP=0$，则

<span id="eq:c74-acyclic-positive-degree"></span>

$$
P=\frac1n(qh+hq)P=q\left(\frac{hP}{n}\right).
\tag{74.42}
$$

它必为恰当态的系数多项式。这一论证同时处理任意多个非物理量子。
例如按左奇导数的乘积法则，
$q(xu)=-\kappa(yu+xv)$，而$q(yu+xv)=\kappa yv-\kappa yv=0$；
看似新的闭组合$yu+xv$正好是一个恰当项。
有多个动量与颜色时，把$q,h,N_{\rm aux}$分别求和，恒等式保持相同形式。
对有限粒子数、避开零动量的光滑波包，$1/\kappa$有良好定义，因而上述消去可以逐项进行。

于是每个物理类都能选取只含$a_+^\dagger,a_-^\dagger,a_\varphi^\dagger$的代表。
这些算符都被$Q_B$湮灭；它们也不能成为恰当态，因为$q$保持$N_{\rm aux}$，
而在$N_{\rm aux}=0$的子空间上$q=0$。横向规范模和物质模的正号对易关系
又保证这个代表空间具有通常的正定福克内积。
这样，物理态空间的结论已从单粒子推广到任意有限粒子数的态。

真空也属于这个空间：式[（74.37）](#eq:c74-free-charge-modes)已经给出$Q_B|0\rangle=0$，
将真空归一为正范数后，它由式[（74.30）](#eq:c74-exact-null)不可能恰当。
这里的真空闭性由自由荷的显式表达式给出；相互作用理论中使用前面说明的BRST不变真空条件。

最后，若散射算符满足$[S,Q_B]=0$，两端都取闭态，就有

<span id="eq:c74-exact-decoupling"></span>

$$
\langle\psi_{ \rm out}|S Q_B|\chi\rangle
 =\langle\psi_{ \rm out}|Q_B S|\chi\rangle=0 .
\tag{74.43}
$$

在初态或末态中加入恰当态都不改变散射振幅。
所谓非物理偏振与鬼的退耦，正是这种商空间意义下的退耦；闭态的某个代表本身
可以含有它们组成的恰当部分。对于微扰散射，这给出了在协变规范中只保留物质粒子
和两种横向外态的依据。这里采用自由渐近态以及适当的红外调节；强耦合禁闭理论的
实际渐近粒子还要由动力学确定。

偏振矢量加上$\zeta k^\mu$就是代表改变的一个具体例子。下面直接求出它的恰当原像。

<span id="c74-polarization-shift"></span>

## 偏振改变的恰当原像

以下使用自由渐近场，略去群指标，取$k^\mu=(\omega,\mathbf k)$、$\omega=|\mathbf k|>0$。令普通复数$\zeta$指定偏振的改变：
<span id="eq:c74-ex-polarization-shift"></span>

$$
\widetilde\varepsilon_+^\mu(k)
 =\varepsilon_+^\mu(k)+\zeta k^\mu,
\qquad k^2=0,\qquad
k_\mu\varepsilon_+^\mu=0 .
\tag{74.44}
$$

这个改变保持横向条件及偏振的单位范数。$\zeta$不必为实数，而产生算符含偏振的复共轭，所以结果中将出现$\zeta^*$。

取闭态$|\psi\rangle$，即$Q_B|\psi\rangle=0$，并使用式[（74.25）](#eq:c74-charge-action)在$g=0$时的生成关系。守恒的$Q_B$与时间导数可交换。定动量算符仍以避开零动量的光滑波包理解，使空间边界项为零。

记固定时间的波数投影为
<span id="eq:c74-ex-mode-projector"></span>

$$
\begin{aligned}
\mathcal J_k(F)
 &=\int d^3x\,e^{ikx}\overleftrightarrow{\partial}_0F(x)\\
 &=\int d^3x\,e^{ikx}
       [\partial_0F(x)+i\omega F(x)].
\end{aligned}
\tag{74.45}
$$

这里$\partial_0=\partial/\partial t$，而$k_0=-\omega$，故$\partial_0e^{ikx}=-i\omega e^{ikx}$。将这个投影代入产生算符及其偏振改变量，得到
<span id="eq:c74-ex-operator-difference"></span>

$$
\begin{aligned}
a_+^\dagger(k)&=-i\varepsilon_+^{\mu *}(k)\mathcal J_k(A_\mu),\\
\widetilde a_+^\dagger(k)-a_+^\dagger(k)
 &=-i\zeta^* k^\mu\mathcal J_k(A_\mu).
\end{aligned}
\tag{74.46}
$$

自由鬼场的模式展开给$\mathcal J_k(\partial_\mu c)=k_\mu c^\dagger(k)$：投影消去正频率项，负频率项上的导数$-ik_\mu$与投影给出的$i$相乘，留下$k_\mu$。因此式[（74.25）](#eq:c74-charge-action)还给$[Q_B,a_+^\dagger]=-(\varepsilon_+^*\cdot k)c^\dagger=0$，从闭态$|\psi\rangle$出发仍得到闭态。余下的工作就是把第二行改写成$Q_B$与某个奇算符的反对易子。

<span id="c74-polarization-equations"></span>

### 保留一般规范参数

自由场方程已列于式[（74.32）](#eq:c74-free-equations)。其中$\partial\cdot A=\xi B$来自对$B$变分，而$-B\partial^\mu\delta A_\mu$分部积分给$+\partial^\mu B\,\delta A_\mu$，从而$\partial^2A_\mu=(\xi-1)\partial_\mu B$。在一般$\xi$下，下面的$a^\dagger$记号表示上式定义的定时投影；四个分量并非都由普通平面波组成，投影也可能带有显式时间依赖。

由于$\partial\cdot A=-\partial_0A_0+\partial_iA_i$，空间分部积分及$\omega^2=\mathbf k^2$分别给
<span id="eq:c74-ex-projector-integration-by-parts"></span>

$$
\begin{aligned}
\mathcal J_k(\partial_iA_i)
 &=-ik_i\mathcal J_k(A_i),\\
\mathcal J_k(-\partial_0A_0)+i\omega\mathcal J_k(A_0)
 &=-\int d^3x\,e^{ikx}(\partial_0^2+\omega^2)A_0\\
 &=\int d^3x\,e^{ikx}\partial^2 A_0 .
\end{aligned}
\tag{74.47}
$$

第二行中的一阶时间导数相消。最后一步把空间拉普拉斯从$A_0$移到$e^{i\mathbf k\cdot\mathbf x}$，产生$-\mathbf k^2$。合并两部分，便得到
<span id="eq:c74-ex-divergence-projector"></span>

$$
\mathcal J_k(\partial\cdot A)
 =-ik^\mu\mathcal J_k(A_\mu)
   +\int d^3x\,e^{ikx}\partial^2 A_0 .
\tag{74.48}
$$

将式[（74.32）](#eq:c74-free-equations)代入，右边的额外项正好可以用$B$表示：
<span id="eq:c74-ex-difference-as-b-field"></span>

$$
\begin{aligned}
-ik^\mu\mathcal J_k(A_\mu)
 &=\xi\mathcal J_k(B)
       -(\xi-1)\int d^3x\,e^{ikx}\partial_0B\\
 &=\int d^3x\,e^{ikx}
                  [\partial_0B+i\omega\xi B].
\end{aligned}
\tag{74.49}
$$

保留辅助场使这个恒等式不含$\xi^{-1}$，接下来便可直接利用$\bar c$的BRST变换。

由$i\{Q_B,\bar c\}=B$，可选择
<span id="eq:c74-ex-exact-state-general"></span>

$$
|\chi(k,t)\rangle
 =i\zeta^*\int d^3x\,e^{ikx}
       [\partial_0\bar c(x)+i\omega\xi\bar c(x)]
                           |\psi\rangle .
\tag{74.50}
$$

把$Q_B$移过奇场$\bar c$时，用反对易子并留下$-\bar c Q_B|\psi\rangle$。后一项由闭态条件消失，因此
<span id="eq:c74-ex-exact-state-verification"></span>

$$
\begin{aligned}
Q_B|\chi\rangle
 &=i\zeta^*\int d^3x\,e^{ikx}
       (\partial_0+i\omega\xi)\{Q_B,\bar c(x)\}
                                    |\psi\rangle\\
 &=\zeta^*\int d^3x\,e^{ikx}
       [\partial_0B+i\omega\xi B]|\psi\rangle\\
 &=\bigl(\widetilde a_+^\dagger-a_+^\dagger\bigr)|\psi\rangle.
\end{aligned}
\tag{74.51}
$$

第一行到第二行用了$\{Q_B,\bar c\}=-iB$，所以$i(-i)=1$。这就把两个代表的差写成了一个恰当态。在$Q_B^2=0$下，右边的差本身也被$Q_B$湮灭，两个代表向量属于同一个商空间元素。若在$|\chi\rangle$上再加任意闭态，这一等式仍成立，所以原像态不唯一。

<span id="c74-polarization-modes"></span>

### 反鬼模与费曼规范下的结果

为了把式[（74.50）](#eq:c74-ex-exact-state-general)写成反鬼模，先分别命名它的两个频率系数：
<span id="eq:c74-ex-antighost-frequency-coefficients"></span>

$$
\bar c(x)=\int\frac{d^3q}{(2\pi)^3\,2\omega_{\mathbf q}}
 \left[
 \bar c_{(+)}(\mathbf q)e^{iqx}
 +\bar c_{(-)}(\mathbf q)e^{-iqx}
 \right].
\tag{74.52}
$$

由式[（74.26）](#eq:c74-adjoint-convention)的$\bar c^\dagger=-\bar c$，正频率系数记作$b$时，负频率系数便是$-b^\dagger$，即$\bar c_{(+)}=b$、$\bar c_{(-)}=-b^\dagger$。自由鬼方程是$\partial^2\bar c=0$，在一般$\xi$下仍可使用这个展开。空间积分对两项分别给$\delta^3(\mathbf k+\mathbf q)$和$\delta^3(\mathbf k-\mathbf q)$；因此
<span id="eq:c74-ex-antighost-mode-projection"></span>

$$
\begin{aligned}
\int d^3x\,e^{ikx}\bar c(x)
 &=\frac1{2\omega}
   \left[\bar c_{(+)}(-\mathbf k)e^{-2i\omega t}
                    +\bar c_{(-)}(\mathbf k)\right],\\
\int d^3x\,e^{ikx}\partial_0\bar c(x)
 &=\frac{i}{2}
   \left[-\bar c_{(+)}(-\mathbf k)e^{-2i\omega t}
                    +\bar c_{(-)}(\mathbf k)\right].
\end{aligned}
\tag{74.53}
$$

$(2\pi)^3$由空间积分与模式测度相消，$\partial_0$的$\omega$则与测度中的$2\omega$约去。将两行代入所求态，得到一般规范参数下的模式形式：
<span id="eq:c74-ex-exact-state-frequency-form"></span>

$$
\begin{aligned}
|\chi(k,t)\rangle
 &=-\frac{\zeta^*}{2}
 \left[(1+\xi)\bar c_{(-)}(\mathbf k)
       +(\xi-1)\bar c_{(+)}(-\mathbf k)e^{-2i\omega t}\right]
                    |\psi\rangle\\
 &=\frac{\zeta^*}{2}
 \left[(1+\xi)b^\dagger(\mathbf k)
       +(1-\xi)b(-\mathbf k)e^{-2i\omega t}\right]
                    |\psi\rangle .
\end{aligned}
\tag{74.54}
$$

一般$\xi$下，式[（74.45）](#eq:c74-ex-mode-projector)的积分还留下一个反鬼湮灭模，
其系数由自由场方程固定。它与产生模共同组成偏振改变的恰当原像。

取$\xi=1$，投影消去正频率模，只剩
<span id="eq:c74-ex-exact-state-feynman"></span>

$$
|\chi\rangle=-\zeta^*\bar c_{(-)}(\mathbf k)|\psi\rangle
            =+\zeta^*b^\dagger(\mathbf k)|\psi\rangle .
\tag{74.55}
$$

结果的正号来自$\bar c_{(-)}=-b^\dagger$，与式[（74.38）](#eq:c74-creation-transforms)的$\{Q_B,b^\dagger\}=-\kappa a_<^\dagger$相容。

还可取$\mathbf k$沿$z$轴，直接核对偏振和。此时$k\cdot\varepsilon_<=-\sqrt2\omega$，$k\cdot\varepsilon_>=k\cdot\varepsilon_\pm=0$。在$\xi=1$的普通平面波展开中，式[（74.45）](#eq:c74-ex-mode-projector)给$\mathcal J_k(A_\mu)=i\sum_\lambda\varepsilon_{\lambda\mu}a_\lambda^\dagger$，所以
<span id="eq:c74-ex-null-polarization-check"></span>

$$
\begin{aligned}
\widetilde a_+^\dagger-a_+^\dagger
 &=-\zeta^*\sqrt2\omega\,a_<^\dagger,\\
\{Q_B,\bar c_{(-)}\}
 &=\sqrt2\omega\,a_<^\dagger .
\end{aligned}
\tag{74.56}
$$

第二行由$B=\partial\cdot A$的负频率系数和$i\{Q_B,\bar c\}=B$得到，与式[（74.55）](#eq:c74-ex-exact-state-feynman)完全相合。于是偏振中增加的类光部分只改变态的代表，不改变其物理上同调类。

---

[← 第 73 节](/posts/srednicki-73/) · [章节地图](/srednicki/) · [第 75 节 →](/posts/srednicki-75/)
