---
title: 'Srednicki §9 相互作用场论的路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [9]
hideFromHome: true
draft: false
---

<span id="c09"></span>

将相互作用按耦合常数展开，每个场因子都可以用源导数产生，再对自由高斯泛函逐项求导。费曼图（Feynman diagram）记录这些微分产生的连接关系，把相同的积分合并起来。本节以三次相互作用为例，求出图的权重、对称因子，以及维持场归一化的反项。

<span id="c09-model"></span>

## 参数与场的归一化

沿用第5节的三次相互作用模型，拉格朗日密度取为

<span id="eq:c09-lagrangian"></span>

$$
\mathcal L=
-\frac{Z_\varphi}{2}\partial^\mu\varphi\,\partial_\mu\varphi
-\frac{Z_m m^2}{2}\varphi^2
+\frac{Z_g g}{3!}\varphi^3+Y\varphi.
\tag{9.1}
$$

参数 $m$ 要表示粒子的物理质量，$g$ 则由指定的散射观测量定义。除此之外，场的尺度和平均值也必须与第5节的LSZ约化相配，因此要求

<span id="eq:c09-field-conditions"></span>

$$
\langle0|\varphi(x)|0\rangle=0,\qquad
\langle k|\varphi(x)|0\rangle=e^{-ikx},
\qquad k^2=-m^2,\quad k^0>0.
\tag{9.2}
$$

真空取 $\langle0|0\rangle=1$，单粒子态仍采用相对论归一化：

<span id="eq:c09-state-normalization"></span>

$$
\langle k'|k\rangle
=(2\pi)^3\,2k^0\,\delta^3(\mathbf k-\mathbf k').
\tag{9.3}
$$

质量、相互作用强度、场平均值以及场产生单粒子的强度，共给出四项条件，用来确定三个 $Z$ 和 $Y$。这些条件规定的是参数的物理意义及场的归一化；本节先建立求解它们的微扰展开，指定散射观测量的具体做法留待能够计算散射过程以后再讨论。

先看各量的量纲，以明确这里的阶数记法。四维作用量无量纲，动能项给出 $[\varphi]=1$，所以 $[g]=1$、$[Y]=3$，而 $Z_\varphi,Z_m,Z_g$ 无量纲。可以暂将 $g$ 换成 $\lambda g$，用无量纲的 $\lambda$ 标记展开阶数；以下 $O(g^n)$ 表示固定 $m$ 和调节器后的这个阶数。自由极限对应

<span id="eq:c09-orders"></span>

$$
Z_\varphi=Z_m=Z_g=1+O(g^2),\qquad Y=O(g).
\tag{9.4}
$$

这些起始阶数也有直接的收缩解释：一个立方顶点就能产生一点平均值，两点修正至少需要两个立方顶点，而三点顶点的相对修正从两个附加顶点开始。后面从图的价数关系还会得到相同的奇偶性。

为了看清模型的能量，先由式[（9.1）](#eq:c09-lagrangian)求正则动量，得到 $\Pi=\partial\mathcal L/\partial\dot\varphi=Z_\varphi\dot\varphi$。再作Legendre变换，连同空间梯度项一起保留：

<span id="eq:c09-hamiltonian"></span>

$$
\begin{aligned}
\mathcal H
&=\Pi\dot\varphi-\mathcal L\\
&=\frac{\Pi^2}{2Z_\varphi}
+\frac{Z_\varphi}{2}(\nabla\varphi)^2
+\frac{Z_m m^2}{2}\varphi^2
-\frac{Z_g g}{3!}\varphi^3-Y\varphi .
\end{aligned}
\tag{9.5}
$$

均匀场 $\varphi=v$的势能密度为 $Z_m m^2v^2/2-Z_g gv^3/6-Yv$。沿 $Z_g gv^3>0$的方向增大 $|v|$，三次项压过其余项，能量趋于负无穷。因此，纯实三次理论没有最低能态；这里在自由真空附近按 $g$作形式微扰展开，用它说明费曼图计算。

<span id="c09-source-operator"></span>

## 将相互作用换成源导数

将拉格朗日量分为自由部分和相互作用部分：

<span id="eq:c09-free-interacting-split"></span>

$$
\begin{aligned}
\mathcal L_0
&=-\frac12\partial^\mu\varphi\,\partial_\mu\varphi
-\frac12m^2\varphi^2,\\
\mathcal L_1
&=\frac{Z_g g}{3!}\varphi^3+\mathcal L_{\rm ct},\\
\mathcal L_{\rm ct}
&=-\frac{Z_\varphi-1}{2}\partial^\mu\varphi\,\partial_\mu\varphi
-\frac{Z_m-1}{2}m^2\varphi^2+Y\varphi .
\end{aligned}
\tag{9.6}
$$

自由部分 $\mathcal L_0$ 已由上一节的 $Z_0$ 固定，原拉格朗日量中余下的项便全部归入 $\mathcal L_1$。其中称为反项（counterterm）的 $\mathcal L_{\rm ct}$，正是为维持前面四项物理条件而调节的部分；它们和立方项一样，作为插入来计算。

为统一表示这些插入，记

<span id="eq:c09-free-functional"></span>

$$
\mathscr D_x=\frac1i\frac{\delta}{\delta J(x)},\qquad
Z_0[J]=\exp\!\left[\frac i2\int d^4x\,d^4y\,
J(x)\Delta(x-y)J(y)\right].
\tag{9.7}
$$

在受调节的有限积分中，$\mathscr D_x e^{i\int J\varphi}=\varphi(x)e^{i\int J\varphi}$，所以源导数可以取出指定位置的一份场。将 $e^{i\int\mathcal L_1}$ 展开后，每一项的场多项式都能这样产生；把这些导数移到自由积分之外，再将展开合回指数，就有

<span id="eq:c09-normalized-interaction"></span>

$$
\mathcal Z[J]=
\exp\!\left[i\int d^4x\,
\mathcal L_1(\mathscr D_x,\partial\mathscr D_x)\right]Z_0[J],
\qquad
Z[J]=\frac{\mathcal Z[J]}{\mathcal Z[0]}.
\tag{9.8}
$$

相互作用顶点产生了额外的真空因子。除以 $\mathcal Z[0]$，便使完整生成泛函满足 $Z[0]=1$。

含时间导数的反项还需要说明动量变量的处理，我们将在节末从完整相空间积分给出这一步。现在先保留立方项，定义

<span id="eq:c09-cubic-functional"></span>

$$
\mathcal Z_1[J]=
\exp\!\left[\frac{iZ_g g}{3!}
\int d^4y\,\mathscr D_y^3\right]Z_0[J],
\qquad
Z_1[J]=\frac{\mathcal Z_1[J]}{\mathcal Z_1[0]}.
\tag{9.9}
$$

分母的常数项为一，因此可以按 $g$逐阶求逆。各阶系数由自由高斯积分确定。

<span id="c09-first-graphs"></span>

## 从一次微分计算看出图形

先只加入一个立方顶点，图的连接关系就会从乘积法则中出现。记

<span id="eq:c09-F-and-C"></span>

$$
F_y[J]=\int d^4x\,\Delta(y-x)J(x),\qquad
C(y-z)=\frac{\Delta(y-z)}i.
\tag{9.10}
$$

上一节已得到 $\mathscr D_yZ_0=F_yZ_0$，而 $\mathscr D_zF_y=C(y-z)$。在共同调节下，将三次微分的位置都取为 $y$，逐次使用乘积法则，得到

<span id="eq:c09-third-derivative"></span>

$$
\begin{aligned}
\mathscr D_y^2Z_0&=(C(0)+F_y^2)Z_0,\\
\mathscr D_y^3Z_0
&=\big[2F_yC(0)+(C(0)+F_y^2)F_y\big]Z_0\\
&=\big[F_y^3+3C(0)F_y\big]Z_0.
\end{aligned}
\tag{9.11}
$$

把这三次微分代入立方指数的一次项，便有

<span id="eq:c09-first-order"></span>

$$
\mathcal Z_1[J]
=Z_0[J]\left\{1+\frac{iZ_g g}{3!}\int d^4y\,
\big[F_y^3+3C(0)F_y\big]+O(g^2)\right\}.
\tag{9.12}
$$

由于 $F_y=\int d^4x\,C(y-x)iJ(x)$，第一项表示三价点 $y$分别连到三个源点；第二项把顶点的两个场槽在同点收缩，只留一条线接向源。后一项的系数三来自三个场槽中接向外源的三种选择。图中的空心端点 $J$表示积分源，实心点 $T$表示三次相互作用顶点。

<div class="srednicki-diagram-grid">
<figure>
<img src="/images/srednicki/s09-g08-01.svg" alt="三源树图：三个场槽分别接向外源" loading="lazy" />
<figcaption>三源树图：三个场槽分别接向外源</figcaption>
</figure>
<figure>
<img src="/images/srednicki/s09-g03-01.svg" alt="一源自收缩图：两个场槽形成自环" loading="lazy" />
<figcaption>一源自收缩图：两个场槽形成自环</figcaption>
</figure>
</div>

在一般阶数，既要展开相互作用指数，也要展开自由泛函的二次源指数。将二者写成双重Taylor级数：

<span id="eq:c09-double-series"></span>

$$
\begin{aligned}
\mathcal Z_1[J]
=\sum_{V=0}^\infty\sum_{P=0}^\infty&
\frac{(iZ_g g)^V}{(3!)^V V!}\,
\frac{i^P}{2^P P!}\\
{}\times&
\left[\prod_{a=1}^{V}\int d^4y_a\,\mathscr D_{y_a}^3\right]
\left[\int d^4x\,d^4z\,J(x)\Delta(x-z)J(z)\right]^P .
\end{aligned}
\tag{9.13}
$$

相互作用的Taylor阶数 $V$ 就是三价顶点数，自由源指数的阶数 $P$ 是传播核数。前者提供 $3V$ 个源导数，后者含 $2P$ 个源槽，因此微分后非零项留下

<span id="eq:c09-leg-count"></span>

$$
E=2P-3V\ge0
\tag{9.14}
$$

份外源。为数清微分的分配，先给导数和源槽临时编号：第一个导数可选 $2P$ 个槽，第二个可选 $2P-1$ 个，依次作用到第 $3V$ 个，总数为 $(2P)!/(2P-3V)!=(2P)!/E!$。这些分配未必代表相同的积分；只有最终连接关系相同的那些项，才能合并在一幅图中。

图还要保留各部分的相位。计入每个源导数的 $1/i$，原展开项总共带有

<span id="eq:c09-graph-phase"></span>

$$
i^V\,i^{-3V}\,i^P=i^{P-2V}
=i^{V+E-P}.
\tag{9.15}
$$

最后的形式可以分别分配给 $V$ 个三价点、$E$ 个源点及 $P$ 条传播线，于是得到坐标空间的图规则：

<span id="eq:c09-position-rules"></span>

$$
\begin{aligned}
\text{一条连接 }x,y\text{ 的线}:&\quad C(x-y)=\Delta(x-y)/i,\\
\text{一个源点}:&\quad i\int d^4x\,J(x),\\
\text{一个三价点}:&\quad iZ_g g\int d^4y .
\end{aligned}
\tag{9.16}
$$

每个顶点都带独立积分变量。线画成直线还是曲线、长一些还是短一些，都不改变积分；决定积分的是端点怎样相连。两条线交叉时，只有交叉处明确画出了顶点，才表示它们在那里参与同一次收缩。

式[（9.14）](#eq:c09-leg-count)还限制了允许的图形：$E$ 与 $V$ 必须同奇偶。对连通图，除 $V$ 个三价点外，还有 $E$ 个源点；连接全部节点的一棵树需要 $V+E-1$ 条线，再加的每条线各产生一个独立环。因此

<span id="eq:c09-loop-count"></span>

$$
L=P-(V+E)+1=\frac{V-E}{2}+1.
\tag{9.17}
$$

例如，$V=1,E=3$对应树图，$V=2,E=2$含一个环，$V=2,E=0$含两个环。消去真空泡和一点支路后，$2\leq E\leq4$、$V\leq4$范围内的13种连通图将在下文列出。

<span id="c09-symmetry"></span>

## 对称因子与重复计数

图形把相同积分归在一起以后，还须确定各积分前的系数。这个系数可以从顶点槽和线槽的重排求出。先将式[（9.13）](#eq:c09-double-series)中的 $V$ 个顶点、各顶点的三条槽、$P$ 条线及各线的两个端点全部临时编号。它们的重排给出 $(3!)^V V!\,2^P P!$，看起来恰好抵消Taylor分母；然而，某些重排保持原来的整个连接关系，并没有产生新的分配。这些重复的重排还要除去，其数目就是对称因子 $S$。

也可以直接从Wick配对来确定剩余系数。分别展开立方相互作用与线性源 $e^{i\int J\varphi}$，固定 $V,E$ 时的分母是 $(3!)^V V!E!$。给 $V$ 个三价槽组、每组内的三个槽及 $E$ 个源槽编号后，Wick定理把全部 $3V+E=2P$ 个槽分成 $P$ 对。保持同一幅无标号图的所有槽重排中，有 $S$ 个使原配对不变；因此，每一种实际不同的标号配对都被这 $S$ 个重排重复生成，其数目为

<span id="eq:c09-orbit-count"></span>

$$
N_{\rm pair}(G)=\frac{(3!)^V V!E!}{S_G}.
\tag{9.18}
$$

乘回Taylor分母，每幅图的系数就只剩 $1/S_G$。这也解释了为什么此时交换等价源点应计入对称性：积分中的 $J(x)$ 还没有固定的外部标号。

实际求 $S$ 时，可以把这种重排分成几类。先求保持节点类型和连接关系的顶点置换数 $a_G$，将源叶也作为节点；有线性反项时，叉号节点须与源点区分。再令自环总数为 $\ell$，同一对节点 $u,v$ 之间有 $m_{uv}$ 条平行线；当 $u=v$ 时，$m_{uu}$ 表示该点的自环数。则

<span id="eq:c09-symmetry-formula"></span>

$$
S_G=a_G\,2^\ell\prod_{u\le v}m_{uv}!.
\tag{9.19}
$$

其中 $a_G$ 记录节点的交换；每个自环的两个端点还能互换，合起来给 $2^\ell$；同一对节点之间的等价线又可排列成 $m_{uv}!$ 种方式。这些选择彼此独立，因此相乘。等价源叶的置换已经包含在 $a_G$ 中，不再另外乘源叶阶乘。

两个三价点之间有三条平行线时，交换两点给二，交换三线给 $3!$，故 $S=2\cdot3!=12$。若两个三价点各带一个自环，再以一条线连接，节点交换给二，两个自环各给二，所以 $S=2\cdot2\cdot2=8$。

<div class="srednicki-diagram-grid">
<figure>
<img src="/images/srednicki/s09-g01-02.svg" alt="三平行线真空图：S = 12" loading="lazy" />
<figcaption>三平行线真空图：S = 12</figcaption>
</figure>
<figure>
<img src="/images/srednicki/s09-g01-01.svg" alt="双自环真空图：S = 8" loading="lazy" />
<figcaption>双自环真空图：S = 8</figcaption>
</figure>
</div>

这两幅真空图也可以用六个场的15种配对直接求系数。全部跨顶点收缩时，第一组三槽与第二组三槽有 $3!=6$ 种对应；若每点内部各收缩一对，则各有三种选择，总共 $3\cdot3=9$ 种。于是

<span id="eq:c09-vacuum-pair-check"></span>

$$
\left.\mathcal Z_1[0]\right|_{g^2}
=\frac{(iZ_g g)^2}{2!(3!)^2}
\int d^4y\,d^4z\,
\big[6C(y-z)^3+9C(0)^2C(y-z)\big].
\tag{9.20}
$$

两个积分的系数分别为 $6/72=1/12$ 和 $9/72=1/8$，正是刚才两个 $S$ 的倒数。

双线泡中，整图左右交换给二，泡内双线交换再给二，故 $S=4$。四源树图允许两端交换，也允许每端的两个源叶交换，所以 $S=2\cdot2\cdot2=8$。

<div class="srednicki-diagram-grid">
<figure>
<img src="/images/srednicki/s09-g06-01.svg" alt="双线泡图：S = 4" loading="lazy" />
<figcaption>双线泡图：S = 4</figcaption>
</figure>
<figure>
<img src="/images/srednicki/s09-g10-01.svg" alt="四源树图：S = 8" loading="lazy" />
<figcaption>四源树图：S = 8</figcaption>
</figure>
</div>

对生成泛函求导、固定外部位置以后，源叶的计数随之改变。比如对两源泡图作用 $\mathscr D_{x_1}\mathscr D_{x_2}$，两个导数分配到源叶有两种方式，将原系数 $1/4$ 变为 $1/2$。四源树图则有 $4!=24$ 种外点分配，除以原来的八重对称后，成为三种外点两两分组，每种交换图的系数为一。下一节的散射计算采用的就是这种固定外腿的规则。

<span id="c09-connected"></span>

## 连通图的指数与真空归一化

图上任意两点都能沿线相通，便称为连通图（connected diagram）。不连通图可拆成若干连通分支，各分支的积分变量只出现在自己的因子中，所以整体权重是分支权重的乘积。记 $C_I[J]$ 为第 $I$ 种连通图的完整权重，已包含式[（9.16）](#eq:c09-position-rules)的全部因子和自身的 $1/S_I$。若这个分支出现 $n_I$ 次，其贡献为

<span id="eq:c09-components"></span>

$$
D_{\{n_I\}}[J]
=\prod_I\frac{C_I[J]^{n_I}}{n_I!}.
\tag{9.21}
$$

额外的 $n_I!$ 来自完全相同的整个分支之间的交换。不同种类不能这样互换，每个分支内部的交换又已收入 $S_I$，所以这里恰好只需除去这一个阶乘。

一般图由各类分支出现的次数唯一标记。对每一类独立求和，即令 $n_I=0,1,2,\ldots$，便得到

<span id="eq:c09-connected-exponential"></span>

$$
\begin{aligned}
\mathcal Z_1[J]
&=\sum_{\{n_I\}}\prod_I\frac{C_I[J]^{n_I}}{n_I!}\\
&=\prod_I\left[\sum_{n_I=0}^{\infty}
\frac{C_I[J]^{n_I}}{n_I!}\right]
=\exp\!\left[\sum_I C_I[J]\right].
\end{aligned}
\tag{9.22}
$$

在固定顶点阶数和源次数下，这个重组只涉及有限次乘法及配对，因此连通指数关系也是逐阶成立的形式级数恒等式。

现在归一化可以直接按分支处理。不含源的 $E=0$ 分支称为真空图或真空泡（vacuum bubble），其权重与 $J$ 无关。将指数中的和分成 $E=0$ 与 $E\ge1$ 两部分，再除以零源值，得到

<span id="eq:c09-connected-generator"></span>

$$
\begin{aligned}
Z_1[J]&=\frac{\mathcal Z_1[J]}{\mathcal Z_1[0]}
=\exp\!\left[\sum_{I:E_I\ge1}C_I[J]\right]
\equiv e^{iW_1[J]},\\
iW_1[J]&=\sum_{I:E_I\ge1}C_I[J].
\end{aligned}
\tag{9.23}
$$

归一化同时给出 $W_1[0]=0$。在有限盒和共同时间边界调节下，任何有源图旁边的真空泡都会组成同一个乘法因子，因而被分子、分母完全约去。连在源上的闭环并不属于独立真空分支，仍须保留在关联函数中。

按式[（9.16）](#eq:c09-position-rules)的顶点和线因子求和，所得为 $iW_1$。自由理论中 $W_0$的虚部也有直接的物理意义。对实源，由

$$
\operatorname{Im}\frac1{u-i\eta}
=\frac{\eta}{u^2+\eta^2}\longrightarrow\pi\delta(u)
$$

得到

$$
\begin{aligned}
\operatorname{Im}W_0[J]
&=\frac\pi2\int\frac{d^4k}{(2\pi)^4}
 |\widetilde J(k)|^2\delta(k^2+m^2)\\
&=\frac14\int d\widetilde k\,
 \bigl[|\widetilde J(\omega_{\mathbf k},\mathbf k)|^2
 +|\widetilde J(-\omega_{\mathbf k},\mathbf k)|^2\bigr].
\end{aligned}
$$

实源满足 $\widetilde J(-k)=\widetilde J(k)^*$，第二项再作 $\mathbf k\to-\mathbf k$，两项相等。因此

<span id="eq:c09-W-imaginary"></span>

$$
\operatorname{Im}W_0[J]
=\frac12\int d\widetilde k\,
|\widetilde J(\omega_{\mathbf k},\mathbf k)|^2.
\tag{9.24}
$$

外源在质量壳上有分量时，$\operatorname{Im}W_0>0$，而 $|Z_0[J]|^2=e^{-2\operatorname{Im}W_0[J]}<1$：外源可以产生粒子，最终留在真空的概率下降。

<span id="c09-one-point"></span>

## 用线性反项确定场的平均值

消去了独立真空泡，还剩下带源的连通图。其中一源图决定场的平均值，因此可用它检查最初的场归一化条件。对归一化泛函求一次源导数，有

<span id="eq:c09-one-point"></span>

$$
\langle0|\varphi(x)|0\rangle
=\left.\mathscr D_xZ_1[J]\right|_{J=0}
=\left.\frac{\delta W_1[J]}{\delta J(x)}\right|_{J=0}.
\tag{9.25}
$$

第二个等号用了 $Z_1[0]=1$。从式[（9.12）](#eq:c09-first-order)中取出一次源项，就得到领先贡献：

<span id="eq:c09-leading-tadpole"></span>

$$
\left.\langle\varphi(x)\rangle\right|_{Y=0}
=\frac{ig}{2}\int d^4y\,C(x-y)C(0)+O(g^3).
\tag{9.26}
$$

也可直接从一次相互作用插入看出这个系数：外部的 $\varphi(x)$ 可与 $\varphi(y)^3$ 中任一场收缩，共三种选择，其余两场自相配对，所以给出 $ig\cdot3/3!=ig/2$。此阶可取 $Z_g=1$，因为 $g(Z_g-1)$ 已为三阶；一源图又要求立方顶点数为奇数，因而余项从三阶开始。

为使式[（9.2）](#eq:c09-field-conditions)中的场平均值为零，加入 $Y\varphi$反项。它给出因子 $iY\int d^4y$的单价顶点，图中用叉号标出。

<div class="srednicki-diagram-grid">
<figure>
<img src="/images/srednicki/s09-g12-01.svg" alt="线性反项接向一个源：顶点因子为 iY" loading="lazy" />
<figcaption>线性反项接向一个源：顶点因子为 iY</figcaption>
</figure>
</div>

这幅图贡献 $iY\int d^4y\,C(x-y)$，与式[（9.26）](#eq:c09-leading-tadpole)合并后为

<span id="eq:c09-Y-cancellation"></span>

$$
\langle\varphi(x)\rangle
=\left[iY+\frac{ig}{2}C(0)\right]
\int d^4y\,C(x-y)+O(g^3).
\tag{9.27}
$$

两项都有同一条外线，因此可以先提出共同积分。对于 $m>0$，有 $\int d^4y\,C(x-y)=1/[i(m^2-i0)]$：把传播子的傅里叶式代入，$y$ 积分产生 $(2\pi)^4\delta^4(k)$，选出零四动量处的分母。共同因子非零，令方括号为零，就确定了所需的反项：

<span id="eq:c09-Y-condition"></span>

$$
Y=-\frac g2 C(0)+O(g^3)
=\frac{ig}{2}\Delta(0)+O(g^3).
\tag{9.28}
$$

下面算出受调节的 $\Delta(0)$，便可写出实系数 $Y$的显式值。

还可以由场方程理解这一抵消。对式[（9.1）](#eq:c09-lagrangian)变分，领先阶给出 $(-\partial^2+m^2)\varphi=g\varphi^2/2+Y$。在平移不变真空中取期望，左边为 $m^2\langle\varphi\rangle$，右边最低阶为 $gC(0)/2+Y$；令平均值为零，便得到与式[（9.28）](#eq:c09-Y-condition)相同的 $Y$。

<span id="c09-cutoff"></span>

## 将同点传播子积分算完

同点传播子包含全部模式在同一位置的收缩。由传播子的傅里叶表示，它等于

<span id="eq:c09-coincident-integral"></span>

$$
\Delta(0)=\int\frac{d^4k}{(2\pi)^4}\,
\frac1{k^2+m^2-i0}.
\tag{9.29}
$$

与非零间隔时相比，同点极限不再有空间时间相位的振荡抑制，大动量模式便产生紫外发散，类似第3节的零点能积分。要使当前计算有定义，先乘上只依赖 $k^2$ 的调节因子：

<span id="eq:c09-covariant-regulator"></span>

$$
\Delta_\Lambda(0)=
\int\frac{d^4k}{(2\pi)^4}\,
\frac{\Lambda^4}
{(k^2+m^2-i0)(k^2+\Lambda^2-i0)^2},
\qquad \Lambda>0.
\tag{9.30}
$$

新增因子在 $|k^2|\ll\Lambda^2$时接近一，并只依赖洛伦兹标量 $k^2$。积分按所写的Feynman极点处方计算。

固定 $\mathbf k$ 后，正能极点 $\sqrt{\mathbf k^2+m^2-i0}$ 和重质量双极点 $\sqrt{\mathbf k^2+\Lambda^2-i0}$ 都在实轴下方，两负能极点则在上方。因此，正的 $k^0$ 半轴可以经过第一象限转到正虚轴，负半轴可以经过第三象限转到负虚轴，两段变形均不跨过极点。大圆弧上调节后的被积函数为 $(k^0)^{-6}$ 阶，弧积分因而按 $R^{-5}$ 消失。作 $k^0=ik_4$，连同 $dk^0=i\,dk_4$，得到Wick旋转（Wick rotation）：

<span id="eq:c09-wick-rotation"></span>

$$
\Delta_\Lambda(0)
=i\int\frac{d^4k_E}{(2\pi)^4}
\frac{\Lambda^4}
{(k_E^2+m^2)(k_E^2+\Lambda^2)^2},
\qquad
k_E^2=k_4^2+\mathbf k^2 .
\tag{9.31}
$$

旋转后的欧几里得径向测度为 $r^3dr$，大半径被积函数为 $O(r^{-6})$，在 $m>0$时原点也有限，所以积分收敛。右侧是正实积分乘 $i$，式[（9.28）](#eq:c09-Y-condition)中的 $Y$因此为实数。

接着作角积分。四份一维高斯相乘给出 $\int d^4q\,e^{-q^2}=\pi^2$。若单位三维球面的面积为 $\Omega_3$，改用径向变量后，同一个积分为 $\Omega_3\int_0^\infty dr\,r^3e^{-r^2}$。令 $u=r^2$，径向部分化为 $\frac12\int_0^\infty du\,ue^{-u}=1/2$，因此

<span id="eq:c09-sphere-measure"></span>

$$
\Omega_3=2\pi^2,\qquad
\frac{d^4k_E}{(2\pi)^4}
\longrightarrow\frac{u\,du}{16\pi^2}.
\tag{9.32}
$$

用 $a=m^2$、$b=\Lambda^2$ 简化记号，式[（9.31）](#eq:c09-wick-rotation)便只剩径向积分：

<span id="eq:c09-radial-integral"></span>

$$
\Delta_\Lambda(0)=\frac{ib^2}{16\pi^2}
\int_0^\infty du\,
\frac{u}{(u+a)(u+b)^2}.
\tag{9.33}
$$

剩下的有理函数积分可以直接用部分分式做完。先取 $a\ne b$，设 $u/[(u+a)(u+b)^2]=A_1/(u+a)+B_1/(u+b)+C_1/(u+b)^2$。乘公分母并令 $u=-a$，得 $A_1=-a/(b-a)^2$；比较 $u^2$ 的系数得 $B_1=-A_1$，再比较 $u$ 的系数得 $C_1=b/(b-a)$。于是

<span id="eq:c09-partial-fractions"></span>

$$
\frac{u}{(u+a)(u+b)^2}
=-\frac{a}{(b-a)^2}\left(\frac1{u+a}-\frac1{u+b}\right)
+\frac{b}{b-a}\frac1{(u+b)^2}.
\tag{9.34}
$$

第一对分式应合在一起积分，给出 $[\ln((u+a)/(u+b))]_0^\infty=\ln(b/a)$；最后一项使用 $[-1/(u+b)]_0^\infty=1/b$。先合并两个对数再取上限，才能保留它们在无穷远的相消。由此得到有限截断下的精确表达式：

<span id="eq:c09-regulated-closed-form"></span>

$$
\begin{aligned}
\Delta_\Lambda(0)
&=\frac{i}{16\pi^2}\,
\frac{b^2[(b-a)-a\ln(b/a)]}{(b-a)^2}\\
&=\frac{i\Lambda^2}{16\pi^2}\,
\frac{1-x+x\ln x}{(1-x)^2},
\qquad x=\frac{m^2}{\Lambda^2}.
\end{aligned}
\tag{9.35}
$$

当 $a=b$ 时，部分分式的系数虽不再适用，原积分却仍有限。直接从式[（9.33）](#eq:c09-radial-integral)求得

<span id="eq:c09-equal-cutoff-mass"></span>

$$
\int_0^\infty\frac{u\,du}{(u+a)^3}
=\int_a^\infty\left(\frac1{v^2}-\frac a{v^3}\right)dv
=\frac1{2a},
\qquad
\Delta_{\sqrt a}(0)=\frac{ia}{32\pi^2}.
\tag{9.36}
$$

另一个简单极限由 $x\ln x\to0$ 给出：当 $m\to0$ 时，结果为 $i\Lambda^2/(16\pi^2)$，也等于在径向积分中先置 $a=0$ 所得的值。

在截断尺度远大于质量时，取 $x\ll1$，使用 $(1-x)^{-2}=1+2x+O(x^2)$，便有 $(1-x+x\ln x)/(1-x)^2=1+x(1+\ln x)+O(x^2|\ln x|)$。于是

<span id="eq:c09-cutoff-expansion"></span>

$$
\Delta_\Lambda(0)
=\frac{i}{16\pi^2}\left[
\Lambda^2+m^2\left(1-\ln\frac{\Lambda^2}{m^2}\right)
+O\!\left(\frac{m^4}{\Lambda^2}
\ln\frac{\Lambda^2}{m^2}\right)\right].
\tag{9.37}
$$

当 $\Lambda\gg m$ 时，领先项为 $i\Lambda^2/(16\pi^2)$；有限截断时其余项仍应按所需精度保留。代回一点条件，线性反项为

<span id="eq:c09-Y-regulated"></span>

$$
Y=-\frac{g\Lambda^2}{32\pi^2}
\frac{1-x+x\ln x}{(1-x)^2}+O(g^3).
\tag{9.38}
$$

这里在固定 $\Lambda$ 下只保留 $g$ 的一阶，但 $m/\Lambda$ 的依赖已经完整求出。其量纲 $[g\Lambda^2]=3$ 也与线性反项相符。

一个熟悉的大质量尺度是 $G_N^{-1/2}\sim10^{19}\,\mathrm{GeV}$，远高于质子质量约 $1\,\mathrm{GeV}$ 的尺度。自然单位中，Newton势 $-G_Nm_1m_2/r$ 给出 $[G_N]=-2$，因而 $G_N^{-1/2}$ 的确具有质量量纲。这为引入大尺度 $\Lambda$ 提供了物理启发；当前计算中，$\Lambda$ 用来定义逐阶积分，其具体调节形式由式[（9.30）](#eq:c09-covariant-regulator)规定。

随着 $\Lambda$增大，$Y$按式[（9.38）](#eq:c09-Y-regulated)调整，使 $\langle\varphi\rangle=0$保持成立。[第14节](/posts/srednicki-14/)起将计算其他反项，并将这些归一化条件用于散射振幅。

<span id="c09-tadpoles"></span>

## 高阶的一点条件与蝌蚪图

将三阶一源图与同阶反项图相加，就能确定 $Y$的后续系数。写成 $Y=Y_1g+Y_3g^3+\cdots$，三阶的新系数 $Y_3$只通过一个线性顶点进入；其余贡献来自三次顶点、已有 $Y_1$，以及 $Z_g-1$和下文 $A,B=O(g^2)$对领先图的修正。因此，逐阶令一点函数为零，就递归确定各个 $Y_{2n+1}$。

一点条件的作用还不止于整幅一源图。把所有连通一源图截去共同外线后的总和记为 $\mathcal T(y)$，其中也包括线性顶点，就有

<span id="eq:c09-amputated-one-point"></span>

$$
\begin{aligned}
\langle\varphi(x)\rangle
&=\int d^4y\,C(x-y)\mathcal T(y),\\
D_{{\rm line},x}C(x-y)&=-i\delta^4(x-y)
\quad\Longrightarrow\quad
\mathcal T(x)=0.
\end{aligned}
\tag{9.39}
$$

这里 $D_{\rm line}$ 是所采用自由线的逆核算符。没有额外紫外调节时，它为 $D=-\partial^2+m^2$；若整条线也按式[（9.30）](#eq:c09-covariant-regulator)调节，傅里叶乘子则为 $(k^2+m^2-i0)[(k^2+\Lambda^2-i0)/\Lambda^2]^2$。在同一调节下，对恒为零的一点函数作用这个逆算符，即可逐阶得到 $\mathcal T=0$。

先删去 $E=1$ 的全部贡献，再考察 $E\ge2$ 的连通图。若切断某条内部线后图分为两块，这条线称为桥边；如果一侧不含源，该侧就是以割口为根的一点子图。固定含源部分，把割口可能连接的一点子图全部相加，出现的正是 $\mathcal T$，所以总和为零。这就使一点条件消去了蝌蚪图（tadpole diagram）。

这一相消必须包括原来的对称因子。可先给割口一个临时标号，此时接入子图的槽计数与一点函数相同；撤去标号后，$r$ 个相同附着分支的交换仍给出 $1/r!$，与连通指数中的计数一致。存在多个无源桥支时，先将最外层的整个无源分支收入带根子图，其内部的桥支已经包含在 $\mathcal T$ 的展开中。这样每个最大附着分支只计一次，再逐个代入 $\mathcal T=0$。所有叉号都属于单价无源顶点，也随这些分支一起抵消。

双线泡、三角环和四边形环都没有这种无源桥支，仍保留在多点函数中。下图列出 $2\leq E\leq4$、$V\leq4$的13种无蝌蚪有源连通图；图下的 $S$按尚未固定外部标号的积分源计数。

<span id="c09-surviving-graphs"></span>

<div class="srednicki-diagram-grid">
<figure id="c09-gallery-1">
<img src="/images/srednicki/s09-g05-01.svg" alt="自由传播线：E = 2，V = 0，S = 2" loading="lazy" />
<figcaption>自由传播线：E = 2，V = 0，S = 2</figcaption>
</figure>
<figure id="c09-gallery-2">
<img src="/images/srednicki/s09-g06-01.svg" alt="双线泡：E = 2，V = 2，S = 4" loading="lazy" />
<figcaption>双线泡：E = 2，V = 2，S = 4</figcaption>
</figure>
<figure id="c09-gallery-3">
<img src="/images/srednicki/s09-g07-02.svg" alt="含弦闭环：E = 2，V = 4，S = 4" loading="lazy" />
<figcaption>含弦闭环：E = 2，V = 4，S = 4</figcaption>
</figure>
<figure id="c09-gallery-4">
<img src="/images/srednicki/s09-g07-03.svg" alt="串联双线泡：E = 2，V = 4，S = 8" loading="lazy" />
<figcaption>串联双线泡：E = 2，V = 4，S = 8</figcaption>
</figure>
<figure id="c09-gallery-5">
<img src="/images/srednicki/s09-g07-08.svg" alt="双线泡中的自能插入：E = 2，V = 4，S = 4" loading="lazy" />
<figcaption>双线泡中的自能插入：E = 2，V = 4，S = 4</figcaption>
</figure>
<figure id="c09-gallery-6">
<img src="/images/srednicki/s09-g08-01.svg" alt="三源树：E = 3，V = 1，S = 6" loading="lazy" />
<figcaption>三源树：E = 3，V = 1，S = 6</figcaption>
</figure>
<figure id="c09-gallery-7">
<img src="/images/srednicki/s09-g09-01.svg" alt="三角环：E = 3，V = 3，S = 6" loading="lazy" />
<figcaption>三角环：E = 3，V = 3，S = 6</figcaption>
</figure>
<figure id="c09-gallery-8">
<img src="/images/srednicki/s09-g09-02.svg" alt="三源树的外腿修正：E = 3，V = 3，S = 4" loading="lazy" />
<figcaption>三源树的外腿修正：E = 3，V = 3，S = 4</figcaption>
</figure>
<figure id="c09-gallery-9">
<img src="/images/srednicki/s09-g10-01.svg" alt="四源树：E = 4，V = 2，S = 8" loading="lazy" />
<figcaption>四源树：E = 4，V = 2，S = 8</figcaption>
</figure>
<figure id="c09-gallery-10">
<img src="/images/srednicki/s09-g11-02.svg" alt="四边形环：E = 4，V = 4，S = 8" loading="lazy" />
<figcaption>四边形环：E = 4，V = 4，S = 8</figcaption>
</figure>
<figure id="c09-gallery-11">
<img src="/images/srednicki/s09-g11-04.svg" alt="三角环接树叉：E = 4，V = 4，S = 4" loading="lazy" />
<figcaption>三角环接树叉：E = 4，V = 4，S = 4</figcaption>
</figure>
<figure id="c09-gallery-12">
<img src="/images/srednicki/s09-g11-05.svg" alt="四源树的外腿修正：E = 4，V = 4，S = 4" loading="lazy" />
<figcaption>四源树的外腿修正：E = 4，V = 4，S = 4</figcaption>
</figure>
<figure id="c09-gallery-13">
<img src="/images/srednicki/s09-g11-01.svg" alt="四源树的内部线修正：E = 4，V = 4，S = 16" loading="lazy" />
<figcaption>四源树的内部线修正：E = 4，V = 4，S = 16</figcaption>
</figure>
</div>

<span id="c09-quadratic"></span>

## 动能与质量反项的二价顶点

最后恢复二次反项。记

<span id="eq:c09-AB"></span>

$$
A=Z_\varphi-1,\qquad B=Z_m-1,\qquad A,B=O(g^2).
\tag{9.40}
$$

为将它们也写成源导数，先对二次反项分部积分，并按前面的共同处方处理边界：

<span id="eq:c09-quadratic-action"></span>

$$
\begin{aligned}
\int d^4x\,\mathcal L_{{\rm ct},2}
&=-\frac A2\int d^4x\,\partial^\mu\varphi\,\partial_\mu\varphi
-\frac{Bm^2}{2}\int d^4x\,\varphi^2\\
&=-\frac12\int d^4x\,\varphi K_{\rm ct}\varphi,
\qquad K_{\rm ct}=-A\partial^2+Bm^2 .
\end{aligned}
\tag{9.41}
$$

其中 $K_{\rm ct}$ 的两个导数已经全部作用于同一份场；改成源导数以后，也要保持这一作用范围。

时间导数项可以从完整的相空间积分直接推到这里。式[（9.5）](#eq:c09-hamiltonian)仍只含二次动量，在每个格点和时间片完成平方：

<span id="eq:c09-momentum-gaussian"></span>

$$
\Pi\dot\varphi-\frac{\Pi^2}{2Z_\varphi}
=-\frac1{2Z_\varphi}
(\Pi-Z_\varphi\dot\varphi)^2
+\frac{Z_\varphi}{2}\dot\varphi^2.
\tag{9.42}
$$

先取 $Z_\varphi>0$，沿第6节的Fresnel处方，从 $Z_\varphi=1$ 连续选择平方根分支。积掉平方项以后，就精确留下所需的速度项。每个动量积分比自由情况多一份 $Z_\varphi^{1/2}$，而 $Z_\varphi$ 是常参数，这些与外源无关的因子在零源比值中消去。再合入空间梯度和势能，恢复的正是式[（9.1）](#eq:c09-lagrangian)；因此可以在所得位形积分中按 $A$ 展开，并用源导数取代场。

完整理论和自由相互作用绘景使用的正则变量须区分。完整理论中是 $\Pi=Z_\varphi\dot\varphi$，只有自由相互作用绘景变量才满足 $\Pi_I=\dot\varphi_I$。若先展开哈密顿量中的 $1/(1+A)$，还会出现高阶动量插入及等时接触项；上面的高斯积分已将这些项共同求和，空间和时间导数因而合并成 $\partial^2$。

据此定义

<span id="eq:c09-quadratic-normalized"></span>

$$
\mathcal O_2=
\exp\!\left[-\frac i2\int d^4x\,
\mathscr D_xK_{\rm ct}\mathscr D_x\right],
\qquad
Z[J]=\frac{\mathcal O_2Z_1^{(Y)}[J]}
{(\mathcal O_2Z_1^{(Y)})[0]} .
\tag{9.43}
$$

这里 $Z_1^{(Y)}$ 表示包含立方项和线性项的泛函；$Y$ 在加入 $A,B$ 后也须按完整的一点条件重新确定。二次顶点同样会产生真空环，因此作用 $\mathcal O_2$ 后还须再除以新的零源值。

再展开 $\mathcal O_2$ 的一次项。两份场槽接向两条线共有 $2!$ 种等价安排，恰好抵消指数中的 $1/2$，于是得到一类新的二价顶点：

<span id="eq:c09-two-leg-vertex"></span>

$$
-i\int d^4x\,K_{{\rm ct},x}
=-i\int d^4x\,(-A\partial_x^2+Bm^2).
\tag{9.44}
$$

导数整体作用于一条相邻传播子上，通过分部积分也可移到另一条，二者表示同一个积分。利用傅里叶关系 $\partial^2e^{ikx}=-k^2e^{ikx}$，顶点在动量空间中写成

<span id="eq:c09-counterterm-momentum"></span>

$$
-iK_{\rm ct}(k)=-i(Ak^2+Bm^2).
\tag{9.45}
$$

这个顶点的符号还可与可精确积分的二次理论相联系。暂令 $g=Y=0$，则总二次核为 $D+K_{\rm ct}$，按上一节的有限高斯归一化得到

<span id="eq:c09-quadratic-exact"></span>

$$
Z_2[J]=
\exp\!\left[\frac i2
\int J(D+K_{\rm ct})^{-1}J\right].
\tag{9.46}
$$

把 $(D+K_{\rm ct})=(1+K_{\rm ct}D^{-1})D$ 求逆并展开，就有

<span id="eq:c09-neumann-series"></span>

$$
\begin{aligned}
(D+K_{\rm ct})^{-1}
={}&D^{-1}-D^{-1}K_{\rm ct}D^{-1}\\
&+D^{-1}K_{\rm ct}D^{-1}K_{\rm ct}D^{-1}+\cdots .
\end{aligned}
\tag{9.47}
$$

这里按 $A,B$ 作形式展开；在有限矩阵下，若相应算符范数小于一，它也就是收敛的几何级数。另一方面，用传播线和二价顶点直接相乘，前两次插入给出

<span id="eq:c09-insertion-sign-check"></span>

$$
\begin{aligned}
C(-iK_{\rm ct})C&=iD^{-1}K_{\rm ct}D^{-1},\\
C(-iK_{\rm ct})C(-iK_{\rm ct})C
&=-iD^{-1}K_{\rm ct}D^{-1}K_{\rm ct}D^{-1}.
\end{aligned}
\tag{9.48}
$$

这正是式[（9.47）](#eq:c09-neumann-series)乘 $1/i$ 后的一次和二次修正。二价顶点前不再另有 $1/2$，其符号也与精确逆核的展开一致。未归一化的二次积分还带有行列式比 $\det(1+D^{-1}K_{\rm ct})^{-1/2}$，一般并不等于一；式[（9.43）](#eq:c09-quadratic-normalized)的分母消去的正是这类无源因子。

由于 $A,B$ 都从二阶开始，在给定目标阶数内，只须在原有传播线上插入有限个二价顶点，同时将 $Z_g$ 和 $Y$ 展开到相应阶数。真空分支由零源比值消去，一点分支则由完整的 $\langle\varphi\rangle=0$ 条件消去。最终得到

<span id="eq:c09-final-generator"></span>

$$
Z[J]=e^{iW[J]},\qquad
iW[J]=
\sum_{\substack{\text{连通、无真空及无蝌蚪}\\
\text{至少两源，含所需反项}}} C_I[J].
\tag{9.49}
$$

连接关系、对称因子和反项共同给出每阶的生成泛函。[下一节](/posts/srednicki-10/)将源导数与LSZ约化相接，用这些图计算散射振幅。

---

[← 第 8 节](/posts/srednicki-08/) · [章节地图](/srednicki/) · [第 10 节 →](/posts/srednicki-10/)
