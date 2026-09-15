---
title: 'Srednicki §61 标量电动力学'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [61]
hideFromHome: true
draft: false
---

<span id="c61"></span>

现在把带电物质换成自旋为零的粒子，仍要求它与电磁场的相互作用具有局域
$U(1)$对称性，便得到标量电动力学。
复标量场的动能含两个导数，协变导数展开后因而同时产生单光子顶角和双光子
顶角。这个差别将贯穿本节：它先出现在电流中，再决定费曼图的种类，最后使
两光子散射的纵向贡献恰好相消。

<span id="c61-gauge"></span>

## 从复标量场引入电磁相互作用

第22节已讨论过具有整体相位对称性的复场。保留相同的四次项归一，
从拉氏量
<span id="eq:c61-ungauged-lagrangian"></span>

$$
\mathcal L_{\rm scalar}
=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
 -m^2\varphi^\dagger\varphi
 -\frac{\lambda}{4}(\varphi^\dagger\varphi)^2
\tag{61.1}
$$

出发。整体变换使$\varphi$与$\varphi^\dagger$带相反相位，每个乘积中的
相位都抵消。如果让相位随位置变化，普通导数却会作用到它：
<span id="eq:c61-local-phase"></span>

$$
\begin{gathered}
\varphi\longmapsto e^{-i\alpha}\varphi,\qquad
\varphi^\dagger\longmapsto e^{i\alpha}\varphi^\dagger
\qquad(\alpha\text{为常数}),\\
u(x)=e^{-ie\Gamma(x)},\qquad
\varphi'=u\varphi,\qquad
\varphi'{}^\dagger=\varphi^\dagger u^{-1},\\
\partial_\mu\varphi'
=u\,\partial_\mu\varphi-ie(\partial_\mu\Gamma)u\varphi .
\end{gathered}
\tag{61.2}
$$

因此质量项和四次项已经适合局域对称性，动能还需要补偿最后一项。
电荷仍按第58节取$e<0$。引入
$D_\mu=\partial_\mu-ieA_\mu$，并令$A'_\mu=A_\mu-\partial_\mu\Gamma$。
将它作用在变换后的场上，有
<span id="eq:c61-covariant-action"></span>

$$
\begin{aligned}
D'_\mu(u\varphi)
&=(\partial_\mu-ieA_\mu+ie\partial_\mu\Gamma)(u\varphi)\\
&=u\partial_\mu\varphi-ie(\partial_\mu\Gamma)u\varphi
  -ieA_\mu u\varphi+ie(\partial_\mu\Gamma)u\varphi\\
&=uD_\mu\varphi,\qquad D'_\mu=uD_\mu u^{-1}.
\end{aligned}
\tag{61.3}
$$

最后一个等号是作用于右侧场的算符等式。
于是$D_\mu\varphi$与$\varphi$具有同一个相位，而其厄米共轭具有相反相位。
电磁场强的变化为
$F'_{\mu\nu}-F_{\mu\nu}=-\partial_\mu\partial_\nu\Gamma
+\partial_\nu\partial_\mu\Gamma=0$，故麦克斯韦动能也可同时加入。
于是得到规范不变的拉氏量：
<span id="eq:c61-lagrangian"></span>

$$
\mathcal L
=-(D^\mu\varphi)^\dagger D_\mu\varphi
 -m^2\varphi^\dagger\varphi
 -\frac{\lambda}{4}(\varphi^\dagger\varphi)^2
 -\frac14F^{\mu\nu}F_{\mu\nu}.
\tag{61.4}
$$

这里仍取四维度规$(-,+,+,+)$。动能给出$[\varphi]=[A]=1$，因而
$[e]=[\lambda]=0$、$[m]=1$。以下取$m^2>0$、$\lambda\ge0$，在零场真空附近作微扰；
求树级散射时把重整化因子置为1。

四次耦合不仅是幂次计数允许的一项，电磁圈修正本身也会
产生这种局域结构。用一个补充计算可以看清这一点。暂取$\lambda=0$，以
勒让德源固定常背景$\varphi_0$，记$\rho_0=|\varphi_0|^2$。
用整体相位将背景取成实数，写$\varphi=(v+\eta+i\chi)/\sqrt2$，
$\varphi_0=v/\sqrt2$。欧氏动能中的相位部分为
$(\partial\chi-evA_E)^2/2$。在朗道规范中，混合项分部积分后消失；
按相同的边界条件略去表面项，便有
<span id="eq:c61-background-determinant"></span>

$$
\begin{gathered}
\int d^4x_E\,(-evA_E^\mu\partial_\mu\chi)
=\int d^4x_E\,ev\chi\,\partial_\mu A_E^\mu=0,\\
M_A^2=e^2v^2=2e^2\rho_0,\qquad
U_{1,A}(\rho_0)=\frac32\int\frac{d^4\ell_E}{(2\pi)^4}
       \ln(\ell_E^2+M_A^2).
\end{gathered}
\tag{61.5}
$$

在$\lambda=0$时，两个标量的二次质量不依赖$\rho_0$，
所以这里的背景依赖只来自光子。因子3是欧氏四维中垂直于$\ell_E$的三个分量，$1/2$来自每个实高斯变量的
行列式，已在[第53节](/posts/srednicki-53/#c53-half-weights)推导。阿贝尔规范固定的行列式
与此背景无关。只考察$\kappa<|\ell_E|<\Lambda$、$\kappa^2\gg M_A^2$的
高动量区间，将对数展开到$(M_A^2/\ell_E^2)^2$，四次背景项为
<span id="eq:c61-quartic-logarithm"></span>

$$
\begin{aligned}
\ln(\ell_E^2+M_A^2)
&=\ln\ell_E^2+\frac{M_A^2}{\ell_E^2}
 -\frac{M_A^4}{2\ell_E^4}
 +O\!\left(\frac{M_A^6}{\ell_E^6}\right),\\
U_{1,A}\big|_{\rho_0^2}
&=-3e^4\rho_0^2
  \frac{2\pi^2}{(2\pi)^4}\int_\kappa^\Lambda\frac{d\ell_E}{\ell_E}
 =-\frac{3e^4\rho_0^2}{8\pi^2}\ln\frac{\Lambda}{\kappa}.
\end{aligned}
\tag{61.6}
$$

这里球面面积$2\pi^2$与径向测度$\ell_E^3d\ell_E$都已计入。更高项的
高动量积分至多为$O(M_A^6/\kappa^2)$，不能消去显示的四次对数。
真空能、质量及动能反项的场依赖也各不相同，因此必须允许一个
$(\varphi^\dagger\varphi)^2$反项。重整化耦合仍可在某一尺度选为零，
但不能从裸作用量中永久删去这一参数。下面的树级散射改用费曼规范。

<span id="c61-current"></span>

## 电流为何含有电磁势

局域相位变换包含整体相位变换，故仍可按第22节求诺特流。
把$\varphi,\varphi^\dagger$看作独立变分坐标，先对各自的导数求偏导，再乘
单位相位变分$-i\varphi,+i\varphi^\dagger$，得到
<span id="eq:c61-noether-current"></span>

$$
\begin{aligned}
\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi)}
 &=-(D^\mu\varphi)^\dagger,\qquad
\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi^\dagger)}
 =-D^\mu\varphi,\\
j^\mu
 &=-(D^\mu\varphi)^\dagger(-i\varphi)
   -(D^\mu\varphi)(i\varphi^\dagger)\\
 &=-i\left[\varphi^\dagger D^\mu\varphi
             -(D^\mu\varphi)^\dagger\varphi\right].
\end{aligned}
\tag{61.7}
$$

这里先按经典场求流，场分量可交换。$j^\mu$按单位相位变换定义，不含总体电荷$e$；电磁流另记为$J^\mu=e j^\mu$。第58节的带电荷流在本节对应$J^\mu$。
对$\varphi^\dagger$变分，动能分部积分一次给出$D_\mu D^\mu\varphi$；
势的导数为$(m^2+\lambda\varphi^\dagger\varphi/2)\varphi$。
由这份场方程及其共轭，电流的守恒成为
<span id="eq:c61-current-conservation"></span>

$$
\begin{aligned}
D_\mu D^\mu\varphi
 &=\left(m^2+\frac{\lambda}{2}\varphi^\dagger\varphi\right)\varphi,\\
\partial_\mu j^\mu
 &=-i\left[\varphi^\dagger D_\mu D^\mu\varphi
       -(D_\mu D^\mu\varphi)^\dagger\varphi\right]=0 .
\end{aligned}
\tag{61.8}
$$

求散度时两个一阶导数的乘积相消；将普通导数合成协变导数时，相反电荷的
两项又消去显式连接项。最后两份场方程含相同的实系数
$m^2+\lambda\varphi^\dagger\varphi/2$，所以剩余差为零。

与旋量流$\bar\Psi\gamma^\mu\Psi$相比，标量流已经含$A^\mu$。
将协变导数实际展开，可以同时看见这一项的系数和它的必要性：
<span id="eq:c61-electromagnetic-current"></span>

$$
\begin{aligned}
j_0^\mu
 &:=-i\left[\varphi^\dagger\partial^\mu\varphi
           -(\partial^\mu\varphi^\dagger)\varphi\right],\\
j^\mu&=j_0^\mu-2eA^\mu\varphi^\dagger\varphi,\qquad
J^\mu=e j^\mu
 =\frac{\partial\mathcal L_{\rm matter}}{\partial A_\mu},\\
j_0'{}^\mu&=j_0^\mu-2e(\partial^\mu\Gamma)\varphi^\dagger\varphi,\\
-2eA'{}^\mu\varphi'{}^\dagger\varphi'
 &=-2eA^\mu\varphi^\dagger\varphi
   +2e(\partial^\mu\Gamma)\varphi^\dagger\varphi .
\end{aligned}
\tag{61.9}
$$

第三行的两份相位导数各给$-e\,\partial^\mu\Gamma$，第四行则恰好补回。
因此完整$j^\mu$规范不变。这个电流作为麦克斯韦方程的源，
满足沿第54节约定的$\partial_\nu F^{\mu\nu}=J^\mu$。
由于它本身依赖$A$，相互作用不能简单地把完整$J$乘一次$A$：
拉氏量中的二光子项必须按式[（61.4）](#eq:c61-lagrangian)展开，才能得到正确系数。

<span id="c61-vertices"></span>

## 有方向的标量线与三个顶角

量子化沿用[第58节的联合规范固定](/posts/srednicki-58/#c58-gauge-fixing)。
一个规范轨道同时改变带电场与电磁势；复标量的相位变换在两个实分量上是
行列式为1的旋转。采用相同的边界条件和相容调节定义后，洛伦茨规范的
阿贝尔行列式仍与场无关。取费曼规范$\xi=1$，光子内线可直接沿用
前面的结果，接下来只需接上复标量的内外线。

沿第22节的$a,b$记号，自由或渐近复场为
<span id="eq:c61-scalar-modes"></span>

$$
\begin{aligned}
\varphi(x)&=\int d\widetilde k\,
 \left[a(\mathbf k)e^{ikx}+b^\dagger(\mathbf k)e^{-ikx}\right],\\
\varphi^\dagger(x)&=\int d\widetilde k\,
 \left[b(\mathbf k)e^{ikx}+a^\dagger(\mathbf k)e^{-ikx}\right],\\
d\widetilde k&=\frac{d^3k}{(2\pi)^3\,2\omega_{\mathbf k}},
\qquad kx=\mathbf k\cdot\mathbf x-\omega_{\mathbf k}t .
\end{aligned}
\tag{61.10}
$$

两套产生湮灭算符服从玻色对易关系，非零对易子均为
$(2\pi)^3\,2\omega_{\mathbf k}\delta^3(\mathbf k-\mathbf k')$。
第22节的荷计算乘上$e$后给$Q_{\rm em}=e(N_a-N_b)$，所以
$a^\dagger$产生电荷$+e<0$的标量电子，
$b^\dagger$产生电荷$-e>0$的标量正电子。
这两个名称在本节只指该模型的两类自旋零粒子。

令$|k\rangle=a^\dagger(\mathbf k)|0\rangle$。收缩湮灭算符与$a^\dagger$，
动量δ函数消去积分，$2\omega_{\mathbf k}$恰好抵消测度中的分母，因此
<span id="eq:c61-external-overlaps"></span>

$$
\begin{aligned}
\langle0|\varphi(x)|k\rangle&=e^{ikx},&
\langle0|\varphi^\dagger(x)|k\rangle&=0,\\
\langle k'|\varphi^\dagger(x)|0\rangle&=e^{-ik'x},&
\langle k'|\varphi(x)|0\rangle&=0 .
\end{aligned}
\tag{61.11}
$$

零式使用了混合对易子为零及真空被湮灭算符湮灭。对标量正电子交换$\varphi$与
$\varphi^\dagger$即可；剥去外平面波后，四类标量外线的因子均为1。

内线也可从两实场立即确定。写$\varphi=(\varphi_1+i\varphi_2)/\sqrt2$，
自由拉氏量分成两个相同的实标量拉氏量；混合收缩为零，两份同类收缩相同，
故
<span id="eq:c61-directed-propagator"></span>

$$
\begin{aligned}
\langle{\rm T}\varphi(x)\varphi^\dagger(y)\rangle_0
 &=\frac12\left[
 \langle{\rm T}\varphi_1(x)\varphi_1(y)\rangle_0+
 \langle{\rm T}\varphi_2(x)\varphi_2(y)\rangle_0\right]\\
 &=\int\frac{d^4k}{(2\pi)^4}
       \frac{-i\,e^{ik(x-y)}}{k^2+m^2-i0},\\
\langle{\rm T}\varphi(x)\varphi(y)\rangle_0
 &=\langle{\rm T}\varphi^\dagger(x)\varphi^\dagger(y)\rangle_0=0 .
\end{aligned}
\tag{61.12}
$$

最后一行是两实场收缩的差，系数中的$i^2=-1$使其相消。
因而每条非零内线总是一端接$\varphi$、另一端接$\varphi^\dagger$，
用连续箭头记录这一电荷流向，便可将标量线与光子顶角相接。

展开式[（61.4）](#eq:c61-lagrangian)中的两个协变导数，
一个来自共轭场的$+ieA^\mu$与另一个来自$\varphi$的$-ieA_\mu$相乘，
再保留动能前面的负号，得到相互作用项：
<span id="eq:c61-expanded-interactions"></span>

$$
\mathcal L_1
=ieA^\mu\left[(\partial_\mu\varphi^\dagger)\varphi
              -\varphi^\dagger\partial_\mu\varphi\right]
 -e^2A^\mu A_\mu\varphi^\dagger\varphi
 -\frac{\lambda}{4}(\varphi^\dagger\varphi)^2 .
\tag{61.13}
$$

三价顶角中的导数作用在哪一端，决定其动量符号。求连接入、出两条标量外腿
的树顶角矩阵元，等价地在这一步对插入作正规序，式
[（61.11）](#eq:c61-external-overlaps)分别给
<span id="eq:c61-derivative-endpoints"></span>

$$
\begin{aligned}
\langle k'|{:}(\partial_\mu\varphi^\dagger)\varphi{:}|k\rangle
 &=(-ik'_\mu)e^{-ik'x}e^{ikx},\\
\langle k'|{:}\varphi^\dagger\partial_\mu\varphi{:}|k\rangle
 &=e^{-ik'x}(ik_\mu)e^{ikx}.
\end{aligned}
\tag{61.14}
$$

正规序去掉同点的真空收缩，保留连接两条外腿的这两项。
将两项的系数与$iS_1$中的$i$相乘，剥去共同的外平面波后，
<span id="eq:c61-three-vertex"></span>

$$
iV_\mu(k',k)
=i(ie)\left[(-ik'_\mu)-(ik_\mu)\right]
=ie(k+k')_\mu .
\tag{61.15}
$$

这里$k$沿标量箭头进入顶角，$k'$沿同一箭头离开顶角。
若改用所有腿都入射的动量，$\varphi^\dagger$腿的动量便为$-k'$，
同一个因子相应写成入$\varphi$动量减去入$\varphi^\dagger$动量。
指定方向之后，导数顶角的动量和与差就没有歧义。

其余两个顶角只需数相同场的排列。两光子接触项有两种光子收缩次序，
两个标量场却不同；四标量项中两个$\varphi$和两个$\varphi^\dagger$各有
两种排列。因此
<span id="eq:c61-contact-vertices"></span>

$$
\begin{aligned}
iV_{\mu\nu}^{AA\varphi^\dagger\varphi}
 &=i(-e^2)\,2!\,g_{\mu\nu}=-2ie^2g_{\mu\nu},\\
iV^{(\varphi^\dagger)^2\varphi^2}
 &=i\left(-\frac{\lambda}{4}\right)(2!)(2!)=-i\lambda .
\end{aligned}
\tag{61.16}
$$

顶角因子已包括这些排列，画出一幅接触图后不再为它另乘一个$2!$。
图61a把三种顶角集中画出。

<span id="c61-vertex-figure"></span>

![标量电动力学的单光子、双光子及四标量顶角与因子](/images/srednicki/s61-c61_01.svg)

图61a：标量电动力学的三个顶角。虚线箭头记录标量电荷流，
左图的$k,k'$沿同一箭头；中图连接两条光子与一入一出的标量线；
右图有两条箭头进入、两条箭头离开。波浪线分别带光子指标，
顶角取下指标，与偏振或内光子的上指标连接。

三价顶角还有一个有用的检验。让光子动量$h=k'-k$进入顶角，收缩其指标，
两个标量动量的交叉项相消，得到
<span id="eq:c61-vertex-ward"></span>

$$
h^\mu iV_\mu(k',k)
=ie(k'^2-k^2)
=ie\left[(k'^2+m^2)-(k^2+m^2)\right].
\tag{61.17}
$$

右边是两个自由标量逆核的差，甚至不要求这两条标量线在质量壳上。
当某条标量是内线时，这个差可以消去其传播子分母，后面的规范抵消就由此发生。

<span id="c61-rules"></span>

## 怎样使用树图规则

有了内外线和顶角因子，便可以按以下顺序计算树级振幅。
先画出所有外线，并用下表把粒子种类、物理动量和沿箭头的动量联系起来。
表中的$p$均为正能物理动量，“进入”与“离开”指相对于相连顶角的方向。

| 外线         | 箭头方向 | 沿箭头标的动量 | 外线因子                        |
| ------------ | -------- | -------------- | ------------------------------- |
| 入标量电子   | 进入     | $p$            | $1$                             |
| 出标量电子   | 离开     | $p$            | $1$                             |
| 入标量正电子 | 离开     | $-p$           | $1$                             |
| 出标量正电子 | 进入     | $-p$           | $1$                             |
| 入光子       | 进入     | $p$            | $\varepsilon_\lambda^{\mu*}(p)$ |
| 出光子       | 离开     | $p$            | $\varepsilon_\lambda^\mu(p)$    |

例如一条入标量正电子线虽然带正能物理动量$p$，它的电荷箭头却离开图，
故必须标$-p$才能在每个顶角使用同一种动量守恒。两类标量都是玻色子，
交换同类外线不会产生费米统计的负号。光子箭头只标物理动量方向，
其入射因子的星号仍来自第55、56节的场展开。

用图61a的三种顶角连接这些外线，列出拓扑不同的所有连通树图。
每条内部标量线的箭头应连续通过顶角，内部光子任选一个动量方向即可；
按箭头的正负号逐顶角守恒，树图全部内动量由外动量确定。随后乘上下列因子：

| 图的组成           | 因子                    |
| ------------------ | ----------------------- |
| 单光子标量顶角     | $ie(k+k')_\mu$          |
| 双光子标量接触顶角 | $-2ie^2g_{\mu\nu}$      |
| 四标量顶角         | $-i\lambda$             |
| 内部光子           | $-ig^{\mu\nu}/(k^2-i0)$ |
| 内部标量           | $-i/(k^2+m^2-i0)$       |

各光子指标按连线缩并，同一树图中的所有因子相乘，最后把各图相加，
所得为$i\mathcal T$。这里的$1/i=-i$已包括在每条内线中；
振幅$\mathcal T$还要除去图之和外面的总$i$。下面的三个图会具体显示
这种记号怎样同时固定交换项和接触项的相对符号。

<span id="c61-annihilation"></span>

## 标量电子正电子湮灭的三幅图

考虑一对标量电子正电子湮灭为两个光子。
用$p,q$分别表示入射标量电子、正电子的动量，用$k,l$
表示两个出光子的动量，均取正能。定义
<span id="eq:c61-annihilation-kinematics"></span>

$$
\begin{aligned}
p+q&=k+l,\qquad p^2=q^2=-m^2,\qquad k^2=l^2=0,\\
s&=-(p+q)^2,\qquad t=-(p-k)^2,\qquad u=-(p-l)^2,\\
s+t+u&=2m^2,\qquad
d_t=m^2-t,\qquad d_u=m^2-u,\qquad d_t+d_u=s .
\end{aligned}
\tag{61.18}
$$

与第59节相同，两个光子可以按两种次序接在有方向的带电线上。
现在还存在一个把两光子直接连在同一顶角的接触图，故共有图61b的三项。
数腿也能确定图已列全。记三类顶角数为$V_3,V_{AA},V_4$，
四外腿的树图满足$V_3+2V_{AA}+2V_4=2$。
若$V_4=1$，其余顶角数只能为零，便没有光子外腿；
允许的情形因而只有$V_3=2$或$V_{AA}=1$。
前者给两种光子次序，后者给一幅接触图。因此本过程的树幅只含$e^2$，不含$\lambda$。

<span id="c61-annihilation-figure"></span>

![标量电子正电子湮灭的两幅交换图及双光子接触图](/images/srednicki/s61-c61_02.svg)

图61b：两幅交换图与一幅接触图。两幅交换图的内部标量箭头
分别带$p-k$与$p-l$，入标量正电子端沿箭头标$-q$。
例如左图下顶角有$p-k=l-q$；第二图的下光子为$k$，
该顶角的动量守恒为$p-l=k-q$。
接触图的两条光子同接一顶角，图间相加，其耦合系数的负号已包括在顶角中。

先读左图。上顶角沿标量线进入、离开的动量为$p,p-k$，其和为$2p-k$；
下顶角则为$p-k,-q$，其和为$p-k-q=l-2q$。乘入两个出光子偏振，
得到
<span id="eq:c61-one-exchange"></span>

$$
\begin{aligned}
i\mathcal T_t
 &=(ie)^2\frac{-i}{(p-k)^2+m^2-i0}\,
  (2p-k)_\mu\varepsilon_k^\mu
  (p-k-q)_\nu\varepsilon_l^\nu\\
 &=ie^2\,
  \frac{(2p-k)_\mu(l-2q)_\nu}{d_t}\,
       \varepsilon_k^\mu\varepsilon_l^\nu .
\end{aligned}
\tag{61.19}
$$

最后一行用了$(ie)^2(-i)=ie^2$。在$m>0$的湮灭物理区，
第59节相同的运动学给$d_t=s(1-\beta\cos\theta)/2>0$、
$d_u=s(1+\beta\cos\theta)/2>0$，其中$\beta=\sqrt{1-4m^2/s}<1$。
两个内线没有落在极点上，因此这里可以取实分母。
交换$k,l$得到第二幅图，接触图则直接给
$-2ie^2g_{\mu\nu}\varepsilon_k^\mu\varepsilon_l^\nu$。
除去共同$i$后，把总幅写成
<span id="eq:c61-full-tensor"></span>

$$
\begin{aligned}
\mathcal T&=\varepsilon_k^\mu\varepsilon_l^\nu M_{\mu\nu},\\
M_{\mu\nu}
 &=-e^2\left[
  \frac{(2p-k)_\mu(2q-l)_\nu}{d_t}
 +\frac{(2q-k)_\mu(2p-l)_\nu}{d_u}
 +2g_{\mu\nu}\right].
\end{aligned}
\tag{61.20}
$$

这个张量尚未使用外偏振的横向性。
每个交换项的分子、分母质量维数都是2，接触项也无量纲。
本节保留树幅的$e^2$阶及模方的$e^4$阶；标量质量完整保留，
圈修正及相应反项不包括在下面的散射结果内。

对实际出光子，$k\cdot\varepsilon_k=l\cdot\varepsilon_l=0$。
所以第一项的两个分子可分别化成$2p\cdot\varepsilon_k$和
$2q\cdot\varepsilon_l$，第二项也一样。于是振幅简化为
<span id="eq:c61-transverse-amplitude"></span>

$$
\mathcal T=-e^2\left[
 \frac{4(p\cdot\varepsilon_k)(q\cdot\varepsilon_l)}{d_t}
 +\frac{4(q\cdot\varepsilon_k)(p\cdot\varepsilon_l)}{d_u}
 +2\varepsilon_k\cdot\varepsilon_l\right].
\tag{61.21}
$$

在计算指定偏振时，这种形式最方便。若要用度规作偏振和，
则须先回到完整张量，弄清哪些分量已在这次化简中被删去了。

<span id="c61-ward"></span>

## 接触图与偏振求和

将一条外光子的偏振换成它的动量，标量顶角的逆核差
[（61.17）](#eq:c61-vertex-ward)就会消去内部传播子。
在当前运动学下，所需四个收缩具体为
<span id="eq:c61-ward-numerators"></span>

$$
\begin{aligned}
k\cdot(2p-k)&=-d_t,&
k\cdot(2q-k)&=-d_u,\\
l\cdot(2q-l)&=-d_t,&
l\cdot(2p-l)&=-d_u .
\end{aligned}
\tag{61.22}
$$

例如$t=m^2+2p\cdot k$，所以$2p\cdot k=-d_t$；
另外三式由$p+q=k+l$及外腿在壳条件得到。逐项作用到
式[（61.20）](#eq:c61-full-tensor)上，两条沃德恒等式便是
<span id="eq:c61-two-ward-identities"></span>

$$
\begin{aligned}
k^\mu M_{\mu\nu}
 &=-e^2\left[-(2q-l)_\nu-(2p-l)_\nu+2k_\nu\right]=0,\\
l^\nu M_{\mu\nu}
 &=-e^2\left[-(2p-k)_\mu-(2q-k)_\mu+2l_\mu\right]=0 .
\end{aligned}
\tag{61.23}
$$

每行最后都用$p+q=k+l$。若只保留两幅交换图，它们在第一行留下
$2e^2k_\nu$，在第二行留下$2e^2l_\mu$；接触图正好将其消去。
这样，电流中显含$A$的项、双光子顶角的因子2以及散射幅的规范不变性，
便成为同一协变动能在三个计算中的表现。

现在可以沿[第59节的物理投影](/posts/srednicki-59/#c59-polarizations)求偏振和。
取一个单位类时矢量$n$来指定时间方向；展开横向投影后有
<span id="eq:c61-physical-sum"></span>

$$
\begin{aligned}
P^{\mu\rho}(k;n)
 &=g^{\mu\rho}
  -\frac{k^\mu n^\rho+n^\mu k^\rho}{k\cdot n}
  +\frac{n^2k^\mu k^\rho}{(k\cdot n)^2},\qquad n^2=-1,\\
\mathcal A
 &:=\sum_{\lambda_k,\lambda_l}|\mathcal T|^2
  =P^{\mu\rho}(k;n)P^{\nu\sigma}(l;n)
       M_{\mu\nu}M_{\rho\sigma}^*
  =M_{\mu\nu}M^{\mu\nu *}.
\end{aligned}
\tag{61.24}
$$

投影中每个非度规项都含一个该光子的动量。
无论它收缩在振幅还是共轭幅一侧，式[（61.23）](#eq:c61-two-ward-identities)
都会使其消失。因此可用度规求偏振和。两个初态标量各只有一种自旋，
这里不再附加自旋平均因子。

对已化简的振幅，情况有所不同。
将式[（61.21）](#eq:c61-transverse-amplitude)中已经用过横向性的系数另记为$K_{\mu\nu}$，则
<span id="eq:c61-reduced-tensor"></span>

$$
\begin{aligned}
K_{\mu\nu}
 &=-e^2\left[
    \frac{4p_\mu q_\nu}{d_t}
   +\frac{4q_\mu p_\nu}{d_u}+2g_{\mu\nu}\right],\\
k^\mu K_{\mu\nu}&=2e^2l_\nu,\qquad
l^\nu K_{\mu\nu}=2e^2k_\mu .
\end{aligned}
\tag{61.25}
$$

例如第一条收缩留下
$-e^2[-2q_\nu-2p_\nu+2k_\nu]=2e^2l_\nu$。
它再乘另一个物理偏振仍为零，所以简化幅本身正确；
但对自由指标的收缩没有变为零，不能把两个物理投影都直接去掉。
下面先用两个物理偏振求和，再计算两次度规收缩产生的额外项。
[下文](#c61-covariant-square)也从完整$M_{\mu\nu}$作协变缩并，核对这一结果。

<span id="c61-evaluation"></span>

## 把偏振和实际算完

取质心系，并将入射标量电子的空间动量放在第三轴，
第一个光子放在第一、三轴构成的散射平面内：
<span id="eq:c61-cm-momenta"></span>

$$
\begin{aligned}
p&=E(1,0,0,\beta),\qquad q=E(1,0,0,-\beta),\\
k&=E(1,\sin\theta,0,\cos\theta),\qquad
l=E(1,-\sin\theta,0,-\cos\theta),\\
E&=\frac{\sqrt s}{2},\qquad
\beta^2=1-\frac{m^2}{E^2},\qquad c=\cos\theta,\\
d_t&=2E^2(1-\beta c),\qquad
d_u=2E^2(1+\beta c),\\
\frac1{d_t}+\frac1{d_u}
 &=\frac{1}{E^2(1-\beta^2c^2)} .
\end{aligned}
\tag{61.26}
$$

两光子的空间方向相反，因而可以共用两根实的单位横向矢量：
一根在散射平面内，另一根垂直于该平面。
<span id="eq:c61-linear-polarizations"></span>

$$
\begin{aligned}
\varepsilon_\parallel&=(0,c,0,-\sin\theta),\qquad
\varepsilon_\perp=(0,0,1,0),\\
\varepsilon_a\cdot\varepsilon_b&=\delta_{ab},\qquad
k\cdot\varepsilon_a=l\cdot\varepsilon_a=0,\\
p\cdot\varepsilon_\parallel&=-\beta E\sin\theta,\qquad
q\cdot\varepsilon_\parallel=+\beta E\sin\theta,\\
p\cdot\varepsilon_\perp&=q\cdot\varepsilon_\perp=0 .
\end{aligned}
\tag{61.27}
$$

改变偏振基不会改变两种偏振的总和。选线偏振的好处是所有内积都为实数，
而且混合偏振立即消失：两个交换项各含一个零内积，接触项也因
$\varepsilon_\parallel\cdot\varepsilon_\perp=0$而为零。
两个相同偏振的幅由式[（61.21）](#eq:c61-transverse-amplitude)成为
<span id="eq:c61-four-linear-amplitudes"></span>

$$
\begin{aligned}
\mathcal T_{\parallel\parallel}
 &=-e^2\left[
   -4\beta^2E^2(1-c^2)
       \left(\frac1{d_t}+\frac1{d_u}\right)+2\right]\\
 &=-2e^2\left[1-\frac{2\beta^2(1-c^2)}{1-\beta^2c^2}\right],\\
\mathcal T_{\perp\perp}&=-2e^2,\qquad
\mathcal T_{\parallel\perp}=\mathcal T_{\perp\parallel}=0 .
\end{aligned}
\tag{61.28}
$$

第一行的负乘积来自两入射标量相反的空间动量，因而交换图与接触图发生干涉。
为把结果换回不变量，令
<span id="eq:c61-invariant-ratio"></span>

$$
\begin{gathered}
\rho=\frac{1-\beta^2}{1-\beta^2c^2}
     =\frac{m^2s}{d_td_u},\\
\frac{\beta^2(1-c^2)}{1-\beta^2c^2}=1-\rho,\qquad
\mathcal T_{\parallel\parallel}=2e^2(1-2\rho).
\end{gathered}
\tag{61.29}
$$

将两个非零偏振振幅的模平方相加，得到
<span id="eq:c61-annihilation-square"></span>

$$
\begin{aligned}
\mathcal A(s,t,u)
 &=4e^4\left[(1-2\rho)^2+1\right]\\
 &=8e^4\left[
  1-\frac{2m^2s}{(m^2-t)(m^2-u)}
   +\frac{2m^4s^2}{(m^2-t)^2(m^2-u)^2}\right].
\end{aligned}
\tag{61.30}
$$

求和只含刚才得到的两个非零幅，每个偏振组合恰好计一次。
相同末态光子的$1/2!$将在完整带标签相空间积分中加入，它不改变这里的偏振和。
式中的$t,u$对称性对应两个光子的交换；所有项无量纲，第一行也使正性清楚可见。

还可以定量算出对简化$K$误作两次度规收缩的结果。
用$w=p\cdot q=m^2-s/2$以及$p^2=q^2=-m^2$，所得为
<span id="eq:c61-spurious-polarization-term"></span>

$$
\begin{aligned}
K_{\mu\nu}K^{\mu\nu}
 &=e^4\left[
 16m^4\left(\frac1{d_t^2}+\frac1{d_u^2}\right)
 +\frac{32w^2}{d_td_u}
 +16w\left(\frac1{d_t}+\frac1{d_u}\right)+16\right]\\
 &=16e^4\left[
 1-m^2\left(\frac1{d_t}+\frac1{d_u}\right)
 +m^4\left(\frac1{d_t}+\frac1{d_u}\right)^2\right]\\
 &=16e^4(1-\rho+\rho^2)=\mathcal A+8e^4 .
\end{aligned}
\tag{61.31}
$$

第一行的四项依次来自两个交换项各自的平方、两者互乘、与接触项的交叉项，
以及$4g_{\mu\nu}g^{\mu\nu}=16$。把$w=m^2-s/2$代入并用$d_t+d_u=s$，
含$s^2/(d_td_u)$的两项相消，含$m^2s/(d_td_u)$的项合成
$-16m^2s/(d_td_u)$，四次质量项合成
$16m^4(1/d_t+1/d_u)^2$，即第二行。因此误差恒为$8e^4$。

最后看两个物理极限。阈值$\beta=0$时，标量的空间动量为零，
两幅交换图在所选偏振下均消失，只剩接触图：
$\mathcal T_{\parallel\parallel}=\mathcal T_{\perp\perp}=-2e^2$，
故$\mathcal A=8e^4$，并与出光子方向无关。固定非共线角度而取
$m^2/s\to0$时，$\rho\to0$，两个非零幅变为相反号而等模，
偏振和又趋于$8e^4$。在中间能量与角度处，交换图和接触图改变了平行偏振的幅；
由于$0\le\rho\le1$，其总平方在$4e^4$与$8e^4$之间。
这与旋量电动力学的高能角分布不同，反映了物质自旋以及相应顶角结构的差别。

同一三图振幅还可以交叉为标量康普顿散射。此时初态多了一个有两种偏振的光子，
未极化平均应取$\mathcal C(s,t,u)=\mathcal A(t,s,u)/2$。
[后面的康普顿计算](#c61-compton)将逐腿完成这个替换，并在初标量静止系求出角分布。

<span id="c61-covariant-square"></span>

## 完整张量的协变缩并

考虑质量同为$m$的标量电子$p$与正电子$q$湮灭为光子$k,l$，各动量正能且$p+q=k+l$。令$r=m^2$、$a=r-t$、$b=r-u$，其中$s=-(p+q)^2$、$t=-(p-k)^2$、$u=-(p-l)^2$，故$a+b=s$。
为缩短张量乘法，将完整幅的四个动量分子记为
<span id="eq:c61-ex-four-numerators"></span>

$$
\begin{aligned}
A&=2p-k,\qquad B=2q-l,\qquad
C=2q-k,\qquad D=2p-l,\\
M_{\mu\nu}
 &=-e^2\left(\frac{A_\mu B_\nu}{a}
            +\frac{C_\mu D_\nu}{b}+2g_{\mu\nu}\right).
\end{aligned}
\tag{61.32}
$$

这里$A,B,C,D$只是四个矢量的临时名称。上文
[（61.23）](#eq:c61-two-ward-identities)已证明$k^\mu M_{\mu\nu}=l^\nu M_{\mu\nu}=0$，
因此现在确实可以用两个度规替代物理偏振投影。
所需的外动量内积都由在壳条件和曼德尔斯塔姆变量得到：
<span id="eq:c61-ex-dot-products"></span>

$$
\begin{aligned}
p^2=q^2&=-r,\qquad k^2=l^2=0,\qquad
p\cdot q=r-\frac{s}{2},\qquad k\cdot l=-\frac{s}{2},\\
p\cdot k=q\cdot l&=-\frac a2,\qquad
p\cdot l=q\cdot k=-\frac b2 .
\end{aligned}
\tag{61.33}
$$

例如$A^2=4p^2-4p\cdot k=2a-4r$。
两种交换图互乘时，需要
$A\cdot C=4p\cdot q-2p\cdot k-2q\cdot k=4r-s$；
交换图与接触图相乘时，则有
$A\cdot B=4p\cdot q-2p\cdot l-2q\cdot k+k\cdot l$。
把式[（61.33）](#eq:c61-ex-dot-products)代入，全部缩并归结为
<span id="eq:c61-ex-numerator-contractions"></span>

$$
\begin{aligned}
A^2=B^2&=2a-4r,\qquad C^2=D^2=2b-4r,\\
A\cdot C=B\cdot D&=4r-s,\\
A\cdot B&=4r-\frac{5a+b}{2},\qquad
C\cdot D=4r-\frac{a+5b}{2}.
\end{aligned}
\tag{61.34}
$$

平方包含两个交换项各自的平方、两者的交叉项、两项与接触项的交叉项，
以及接触项的平方。按这个顺序写全，
<span id="eq:c61-ex-full-contracted-square"></span>

$$
\begin{aligned}
\frac{M_{\mu\nu}M^{\mu\nu}}{e^4}
 &=\frac{A^2B^2}{a^2}
  +\frac{C^2D^2}{b^2}
  +\frac{2(A\cdot C)(B\cdot D)}{ab}\\
 &\quad+\frac{4A\cdot B}{a}
       +\frac{4C\cdot D}{b}
       +4g_{\mu\nu}g^{\mu\nu}\\
 &=4\left(1-\frac{2r}{a}\right)^2
  +4\left(1-\frac{2r}{b}\right)^2
  +\frac{2(4r-s)^2}{ab}\\
 &\quad+\frac{16r-10a-2b}{a}
       +\frac{16r-2a-10b}{b}+16 .
\end{aligned}
\tag{61.35}
$$

交叉项的因子2来自两种乘法次序，与接触项中的2再相乘便产生因子4。
接下来可以按$r$的次数合并。$r^2$项为
$16r^2(a^{-2}+b^{-2})+32r^2/(ab)=16r^2(a^{-1}+b^{-1})^2$。
线性$r$项中，两个平方贡献$-16r(a^{-1}+b^{-1})$，
接触交叉项给其相反数，余下$-16rs/(ab)$。
常数项为
$8-20+16+2s^2/(ab)-2(a/b+b/a)$；
由于$s^2=(a+b)^2$，它恰好等于8。因此
<span id="eq:c61-ex-covariant-answer"></span>

$$
\begin{aligned}
\mathcal A(s,t,u)
 &=8e^4\left[
     1-\frac{2rs}{ab}+\frac{2r^2s^2}{a^2b^2}\right]\\
 &=8e^4\left[
 1-\frac{2m^2s}{(m^2-t)(m^2-u)}
 +\frac{2m^4s^2}{(m^2-t)^2(m^2-u)^2}\right].
\end{aligned}
\tag{61.36}
$$

这与上文用两个显式偏振得到的式[（61.30）](#eq:c61-annihilation-square)相同。
整个缩并都保留完整的四个分子；若提前使用横向性删去其中的$k,l$项，
就会产生上文已算出的额外$8e^4$。因此度规求和必须作用于满足完整沃德恒等式的张量。

<span id="c61-compton"></span>

## 标量康普顿散射

现在的过程是标量电子与光子散射，
用$p,k$标入射动量，$p',l$标出射动量。将湮灭过程中的入标量正电子
改到末态，动量$q$延拓为$-p'$；再将第一条出光子改到初态，原来的$k$
延拓为$-k$。为区别两套不变量，暂在湮灭变量上加下标$a$：
<span id="eq:c61-ex-compton-crossing"></span>

$$
\begin{aligned}
\widetilde e^-(p)+\gamma(k)&\longrightarrow
     \widetilde e^-(p')+\gamma(l),\qquad p+k=p'+l,\\
s&=-(p+k)^2,\qquad t=-(p-p')^2=-(k-l)^2,\qquad
u=-(p-l)^2,\\
s_a&=-(p-p')^2=t,\qquad
t_a=-(p+k)^2=s,\qquad u_a=u .
\end{aligned}
\tag{61.37}
$$

标量外线因子在交叉时仍为1，所有外标量算符都服从玻色统计。
入光子的外因子改为$\varepsilon_k^{\mu*}$。将上述动量逐个代入完整
式[（61.20）](#eq:c61-full-tensor)，便得到
<span id="eq:c61-ex-compton-tensor"></span>

$$
\begin{aligned}
\mathcal T_{\rm C}
 &=\varepsilon_k^{\mu*}\varepsilon_l^\nu M^{\rm C}_{\mu\nu},\\
M^{\rm C}_{\mu\nu}
 &=e^2\left[
  \frac{(2p+k)_\mu(2p'+l)_\nu}{m^2-s}
 +\frac{(2p'-k)_\mu(2p-l)_\nu}{m^2-u}
 -2g_{\mu\nu}\right].
\end{aligned}
\tag{61.38}
$$

两项各自的负号来自$q=-p'$，再与原幅外面的负号相消；
接触项仍为$-2e^2g_{\mu\nu}$。这也是直接使用标量规则画出两个交换图与
接触图所得的结果。与费米子例不同，这个替换没有旋量自旋密度引起的交叉负号。

对两光子偏振不加权求和，交叉后的张量缩并就是$\mathcal A(t,s,u)$。
未极化康普顿初态却包含两个等概率光子偏振，所以还须除以2。
定义$\mathcal C$为包含这个初态平均的结果，则
<span id="eq:c61-ex-compton-average"></span>

$$
\begin{aligned}
\mathcal C(s,t,u)
 &:=\frac12\sum_{\lambda_k,\lambda_l}
      |\mathcal T_{\rm C}|^2
   =\frac12\mathcal A(t,s,u)\\
 &=4e^4\left[
 1-\frac{2m^2t}{(m^2-s)(m^2-u)}
 +\frac{2m^4t^2}{(m^2-s)^2(m^2-u)^2}\right].
\end{aligned}
\tag{61.39}
$$

未平均的总偏振和只需交换$s,t$，初态平均则还须包括上述$1/2$。交叉对称性作用于振幅张量，初态平均的权重由所考察的过程另行确定。

可以在初标量静止系直接检查这个结果。设入、出光子能量为$\omega,\omega'$，
散射角为$\theta$，取
<span id="eq:c61-ex-compton-laboratory"></span>

$$
\begin{aligned}
p&=(m,0,0,0),\qquad k=\omega(1,0,0,1),\\
l&=\omega'(1,\sin\theta,0,c),\qquad
p'=p+k-l,\qquad c=\cos\theta,\\
p'^2=p^2
&\quad\Longrightarrow\quad
m(\omega-\omega')=\omega\omega'(1-c),\\
\omega'&=\frac{\omega}{1+(\omega/m)(1-c)} .
\end{aligned}
\tag{61.40}
$$

第三行来自$2p\cdot(k-l)-2k\cdot l=0$。于是
<span id="eq:c61-ex-compton-lab-square"></span>

$$
\begin{aligned}
m^2-s&=-2m\omega,\qquad m^2-u=2m\omega',\qquad
t=-2\omega\omega'(1-c),\\
\frac{m^2t}{(m^2-s)(m^2-u)}
 &=\frac{1-c}{2},\\
\mathcal C&=4e^4\left[1-(1-c)+\frac12(1-c)^2\right]
          =2e^4(1+c^2).
\end{aligned}
\tag{61.41}
$$

这个简单形式还可以直接从三图振幅看出。选两光子的时间偏振分量为零，
则$p\cdot\varepsilon_k^*=p\cdot\varepsilon_l=0$。
式[（61.38）](#eq:c61-ex-compton-tensor)的第一幅交换图含
$(2p+k)\cdot\varepsilon_k^*=0$，第二幅含
$(2p-l)\cdot\varepsilon_l=0$，因而只留下接触项。
将入射的平行偏振取沿第一轴，出射的平行偏振取在散射平面内，
两根垂直偏振都取沿第二轴，得到
<span id="eq:c61-ex-compton-contact-check"></span>

$$
\begin{gathered}
\varepsilon_{k,\parallel}=(0,1,0,0),\qquad
\varepsilon_{l,\parallel}=(0,c,0,-\sin\theta),\\
\varepsilon_{k,\perp}=\varepsilon_{l,\perp}=(0,0,1,0),\\
\bigl(\mathcal T_{{\rm C},ab}\bigr)
 =-2e^2\begin{pmatrix}c&0\\0&1\end{pmatrix},\qquad
 \frac12\sum_{a,b}|\mathcal T_{{\rm C},ab}|^2
 =2e^4(1+c^2).
\end{gathered}
\tag{61.42}
$$

因此式[（61.41）](#eq:c61-ex-compton-lab-square)在整个有质量树级物理区域成立，
不要求$\omega\ll m$。反冲仍通过式[（61.40）](#eq:c61-ex-compton-laboratory)
改变出射能量和相空间。

[第59节的实验室相空间积分](/posts/srednicki-59/#c59-compton)只依赖质量与运动学，
仍可直接使用。以入射通量$4m\omega$除两体相空间，得到
<span id="eq:c61-compton-cross-section"></span>

$$
\begin{aligned}
\frac{d\sigma}{d\Omega}
 &=\frac{1}{64\pi^2m^2}\left(\frac{\omega'}{\omega}\right)^2\mathcal C
 =\frac{\alpha^2}{2m^2}\left(\frac{\omega'}{\omega}\right)^2(1+\cos^2\theta),\\
\alpha&=\frac{e^2}{4\pi},\qquad
\lim_{\omega/m\to0}\sigma=\frac{8\pi\alpha^2}{3m^2}.
\end{aligned}
\tag{61.43}
$$

低能时$\omega'/\omega\to1$，对$1+\cos^2\theta$作全角积分给$16\pi/3$，
恢复汤姆孙截面。有限能量时，标量和旋量的模方不同，反冲的相空间因子则相同。

---

[← 第 60 节](/posts/srednicki-60/) · [章节地图](/srednicki/) · [第 62 节 →](/posts/srednicki-62/)
