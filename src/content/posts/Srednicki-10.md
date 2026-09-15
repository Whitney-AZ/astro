---
title: 'Srednicki §10 散射振幅与费曼规则'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [10]
hideFromHome: true
draft: false
---

<span id="c10"></span>

对生成泛函 $Z[J]=e^{iW[J]}$求源导数，得到相互作用场的关联函数；再用LSZ公式约去外部传播线，就得到散射振幅。以两个粒子入射、两个粒子出射的最低阶过程为例，源微分产生三个树图，顶点积分确定内线动量，动量空间的费曼规则也随之得到。

<span id="c10-connected"></span>

## 精确传播子与连通关联函数

先考虑两个场的时间序乘积。相互作用会修正其真空期望值，为此用粗体定义精确传播子：

<span id="eq:c10-exact-propagator"></span>

$$
G_2(x_1,x_2)\equiv
\langle0|\mathrm T\varphi(x_1)\varphi(x_2)|0\rangle
=\frac1i\boldsymbol\Delta(x_1-x_2).
\tag{10.1}
$$

普通 $\Delta$ 仍表示上一节图中的自由核。要计算精确核，只须对完整生成泛函求两次源导数；简写为

<span id="eq:c10-derivative-notation"></span>

$$
\delta_j=\frac1i\frac{\delta}{\delta J(x_j)},\qquad
\mathcal F[J]=iW[J],\qquad Z[J]=e^{\mathcal F[J]}.
\tag{10.2}
$$

这里 $\delta_j$ 就是此前的 $\mathscr D_{x_j}$。求导时先保留外源。第一次用指数函数的求导法则，第二次再对所得两因子的乘积求导：

<span id="eq:c10-two-chain-rule"></span>

$$
\begin{aligned}
\delta_2Z&=(\delta_2\mathcal F)Z,\\
\delta_1\delta_2Z
&=\big[\delta_1\delta_2\mathcal F
+(\delta_1\mathcal F)(\delta_2\mathcal F)\big]Z.
\end{aligned}
\tag{10.3}
$$

然后令外源为零。此时 $Z=1$，而上一节选定的零平均值条件给出 $\delta_j\mathcal F|_0=\langle\varphi(x_j)\rangle=0$，乘积项便消失，只留下

<span id="eq:c10-two-connected"></span>

$$
G_2(x_1,x_2)
=\left.\delta_1\delta_2(iW)\right|_{J=0}.
\tag{10.4}
$$

这个微分过程在图上十分直接：一次 $\delta_j$ 移去一个源，把相连线端固定在 $x_j$。最低阶两点图只有一条自由线，两个导数分配到两端有两种方式，恰好抵消源图的 $S=2$。于是 $\boldsymbol\Delta=\Delta+O(g^2)$；两点圈图与反项给出其二阶修正，第14节将计算这些贡献。

四点函数则还含有分成两个两点函数的项。为把这种结构数清楚，可以继续使用同一乘积法则：每一项将外点标签分成若干块，同一块的导数全作用在同一份 $\mathcal F$ 上。设 $n$ 次导数已经按这些集合分拆列出，再作用第 $n+1$ 个导数。如果它打在 $e^{\mathcal F}$ 上，就产生一个单独的新块；如果打在已有某块上，就把新标签并入该块。任何新分拆都恰好属于其中一种情形，因此

<span id="eq:c10-set-partitions"></span>

$$
\delta_1\cdots\delta_n Z
=Z\sum_{\pi}
\prod_{B\in\pi}\left(\prod_{j\in B}\delta_j\right)\mathcal F,
\tag{10.5}
$$

其中 $\pi$ 遍历 $\{1,\ldots,n\}$ 的不重复集合分拆，每种分拆的系数都是1。再使用一点函数为零的条件，所有含单元素块的项都消失；四点函数剩下一整块及三种两两分拆，即

<span id="eq:c10-four-partitions"></span>

$$
\begin{aligned}
G_4(1,2,3,4)
={}&G_{4,C}(1,2,3,4)
+G_2(1,2)G_2(3,4)\\
&+G_2(1,3)G_2(2,4)
+G_2(1,4)G_2(2,3),
\end{aligned}
\tag{10.6}
$$

第一项把全部四个点接在同一连通部分中，后三项则分别是两个精确二点函数的乘积。将所有外点导数作用在同一份连通泛函上的结果，定义为

<span id="eq:c10-connected-definition"></span>

$$
G_{E,C}(x_1,\ldots,x_E)
=\left.\delta_1\cdots\delta_E(iW)\right|_{J=0}.
\tag{10.7}
$$

下标 $C$ 表示连通（connected）。上一节的 $iW$ 是连通图之和，求导把其中的源叶换成固定外点，所以它生成的正是这里的连通关联函数。相互作用下，三点函数一般也不为零：第8节奇数点的消失来自自由高斯的两两配对，立方相互作用则允许奇数个外点接成连通图。

<span id="c10-disconnected"></span>

## 非连通项与未散射的粒子

现在把这些关联函数用于散射。令入射动量为 $k_1,k_2$，出射动量为 $k_1',k_2'$，都取正能质量壳。第5节的LSZ公式给每条外腿一个约化因子 $+iD_x$，其中 $D_x=-\partial_x^2+m^2$。若先取四腿连通部分，约化式为

<span id="eq:c10-connected-lsz"></span>

$$
\begin{aligned}
S_{fi}^{\rm conn}
={}&i^4\int d^4x_1\,d^4x_2\,d^4x_1'\,d^4x_2'\,
e^{i(k_1x_1+k_2x_2-k_1'x_1'-k_2'x_2')}\\
&\hspace{2em}\times
D_1D_2D_{1'}D_{2'}\,
G_{4,C}(x_1,x_2,x_1',x_2').
\end{aligned}
\tag{10.8}
$$

这里继续使用第5节建立的波包、渐近态和单位单粒子重叠条件。选择连通部分的物理意义，可以从其余三种分拆看出。

例如取 $G_2(x_1,x_1')G_2(x_2,x_2')$，两组坐标各在自己的因子中，约化积分也随之分开。先将能量与三动量都保留为独立的傅里叶变量，用平移不变核 $F(x-x')$ 表示每组坐标的依赖。把其中一组换成相对坐标与中心坐标，令

<span id="eq:c10-relative-coordinates"></span>

$$
r=x-x',\qquad R=\frac{x+x'}2,\qquad
x=R+\frac r2,\quad x'=R-\frac r2.
\tag{10.9}
$$

每个四矢量分量的变换矩阵为 $\left(\begin{smallmatrix}1&1/2\\1&-1/2\end{smallmatrix}\right)$，行列式为 $-1$。四组分量合起来的绝对Jacobian仍为1，因此 $d^4x\,d^4x'=d^4R\,d^4r$。相位随之变为 $(k-k')R+\bar kr$，其中 $\bar k=(k+k')/2$，于是

<span id="eq:c10-pair-fourier"></span>

$$
\begin{aligned}
\int d^4x\,d^4x'\,e^{i(kx-k'x')}F(x-x')
&=\int d^4R\,e^{i(k-k')R}
\int d^4r\,e^{i\bar kr}F(r)\\
&=(2\pi)^4\delta^4(k-k')\,\widetilde F(-\bar k).
\end{aligned}
\tag{10.10}
$$

按式[（8.10）](/posts/srednicki-08/#eq:c08-fourier)的傅里叶约定，右边出现 $-\bar k$。实标量时间序二点核满足 $F(r)=F(-r)$，再令 $r\to-r$，也可将它写成 $\widetilde F(\bar k)$。

对两组坐标分别作这一步，便得到

<span id="eq:c10-two-delta-support"></span>

$$
(2\pi)^4\delta^4(k_1-k_1')
(2\pi)^4\delta^4(k_2-k_2')
\,\widetilde F(\bar k_{11'})\widetilde F(\bar k_{22'}).
\tag{10.11}
$$

两份delta各自要求一对入、出动量相等，说明两个粒子保持了原来的动量，这一分拆因而属于未散射部分。另一种入出配对只把两个相同的出射粒子交换。若改为将两个入射腿相配，就出现 $\delta^4(k_1+k_2)$；正能质量壳上 $k_1^0+k_2^0\ge2m>0$，所以该项没有支撑。

前面的傅里叶计算显示了各对动量相等的支撑。未散射内积的系数由[第5节的波包约化](/posts/srednicki-05/#c05-lsz)确定：先依次取渐近极限，再提取在壳动量核，得到

<span id="eq:c10-full-two-particle-S"></span>

$$
\begin{aligned}
N_{a'b}&=(2\pi)^3\,2\omega_{\mathbf k_b}\,
\delta^3(\mathbf k_a'-\mathbf k_b),
\\
S_{fi}&=N_{1'1}N_{2'2}+N_{1'2}N_{2'1}+S_{fi}^{\rm conn}.
\end{aligned}
\tag{10.12}
$$

对本节相同稳定粒子的 $2\to2$ 过程，两个未散射内积以外的部分就是 $S_{fi}^{\rm conn}$。外粒子数更多时，还可能有其他分拆，例如 $3\to3$ 中一粒子旁观，另外两粒子散射。这些过程也属于完整 $S$；连通振幅对应的是将全部指定外腿连在一起的过程。以下便计算这样的四腿振幅。

<span id="c10-trees"></span>

## 四个源怎样给出三个树图

最低阶连通四点来自[上一节的四源树图](/posts/srednicki-09/#c09-gallery-9)：两个三价点由一条内线相连，另有四条线各接一个源。对它求四次源导数，共有 $4!=24$ 种外点标记方式。按两个顶点各接哪一对外点来分，只有三种不重复的无序分组：

<span id="eq:c10-three-partitions"></span>

$$
\{1,2\}\mid\{1',2'\},\qquad
\{1,1'\}\mid\{2,2'\},\qquad
\{1,2'\}\mid\{2,1'\}.
\tag{10.13}
$$

在每种分组内，交换两个内部顶点，以及分别交换每端的两个外点，共有 $2\cdot2!\cdot2!=8$ 种分配给出同一积分。这八种分配抵消原来带源图的 $S=8$，所以每个固定外腿图的系数为1。

对于一般三价树图，这个结论也可从连接关系看出。任取一个内部顶点，从它伸出的三个分支各选一个外叶，这个顶点就是三叶之间路径的共同交点。保持每个外叶不动的图置换，也必须保持这些路径及其交点不动，因而全部内部顶点都被固定。树中又没有自环或平行线构成的圈，也就不再有线的交换，所以 $S=1$。

下图将三种连接画在一起，并标出随后傅里叶变换所用的动量。端点 $1,2,1',2'$ 是外部场位置，内部顶点记为 $y,z$；箭头表示动量方向，入射流入顶点，出射流出顶点。

<div class="srednicki-diagram-grid">
<figure id="c10-graph-s">
<img src="/images/srednicki/10-inline-1.svg" alt="s 道树图，内线传递两个入射粒子的总动量" />
<figcaption>s 道：两个入射粒子接在同一顶点。</figcaption>
</figure>
<figure id="c10-graph-t">
<img src="/images/srednicki/10-inline-2.svg" alt="t 道树图，内线动量为第一对入出动量之差" />
<figcaption>t 道：1 与 1′ 接在同一顶点。</figcaption>
</figure>
<figure id="c10-graph-u">
<img src="/images/srednicki/10-inline-3.svg" alt="u 道树图，交换两个出射粒子后的连接" />
<figcaption>u 道：1 与 2′ 接在同一顶点。</figcaption>
</figure>
</div>

三条内线的动量分别为 $q_s=k_1+k_2$、$q_t=k_1-k_1'$、$q_u=k_1-k_2'$。图中的连接关系决定散射道；移动外点的位置或弯曲线条不改变图的贡献。

把每条线换成上一节的坐标空间核 $C=\Delta/i$，对两个内部顶点积分，三个分组的贡献便为

<span id="eq:c10-tree-four-point"></span>

$$
\begin{aligned}
G_{4,C}(1,2,1',2')
={}&(ig)^2\int d^4y\,d^4z\,C(y-z)\\
&\times\big[
C(x_1-y)C(x_2-y)C(x_1'-z)C(x_2'-z)\\
&\quad+C(x_1-y)C(x_1'-y)C(x_2-z)C(x_2'-z)\\
&\quad+C(x_1-y)C(x_2'-y)C(x_2-z)C(x_1'-z)
\big]+O(g^4).
\end{aligned}
\tag{10.14}
$$

每项共有五条传播线，改写为 $\Delta$ 时就带有 $(1/i)^5$。由于 $Z_g-1=O(g^2)$，当前两个顶点各取 $ig$ 即可；顶点修正、圈图与二次反项都从四阶进入。

<span id="c10-amputation"></span>

## 逐条截去外部传播线

关联函数已经写出，接着将式[（10.14）](#eq:c10-tree-four-point)代入式[（10.8）](#eq:c10-connected-lsz)。每个外坐标只出现在一条传播线中，约化算符便只作用于这条线。利用传播核的Green方程，有

<span id="eq:c10-external-amputation"></span>

$$
+iD_x\,C(x-y)
=+iD_x\,\frac{\Delta(x-y)}i
=\delta^4(x-y).
\tag{10.15}
$$

这里使用带Feynman边界条件的 $D\Delta=\delta^4$。

外坐标积分现在由delta完成。以第一项为例，四次积分依次给出 $e^{ik_1y}$、$e^{ik_2y}$、$e^{-ik_1'z}$、$e^{-ik_2'z}$，留下两个顶点和相连的一条内部传播线。把LSZ、顶点与五条原传播线的相位合在一起，有

<span id="eq:c10-amputation-phase"></span>

$$
i^4(ig)^2\left(\frac1i\right)^5
=(ig)^2\frac1i=ig^2.
\tag{10.16}
$$

其余两种分组的外坐标积分同样完成，只在两顶点所带的外动量组合上不同。把三项列在一起，得到

<span id="eq:c10-three-coordinate-amplitudes"></span>

$$
\begin{aligned}
S_{fi}^{\rm conn}
={}&ig^2\int d^4y\,d^4z\,\Delta(y-z)\\
&\times\big[
e^{i[(k_1+k_2)y-(k_1'+k_2')z]}\\
&\quad+e^{i[(k_1-k_1')y+(k_2-k_2')z]}\\
&\quad+e^{i[(k_1-k_2')y+(k_2-k_1')z]}
\big]+O(g^4).
\end{aligned}
\tag{10.17}
$$

外线的因子成为1，正是 $+iD$ 与 $\Delta/i$ 相消的结果。第5节的约化已经采用相对论态的 $(2\pi)^3 2\omega$ 归一化，因此这里不再出现另一套 $1/\sqrt{2\omega}$ 因子。经过约化，计算只涉及内部传播和顶点之间的动量传递。

<span id="c10-momentum"></span>

## 作完顶点积分并定义振幅

三个积分只有相位中的动量组合不同，可以统一计算。把两顶点上的有号外动量和记为 $a,b$：第一道为 $a=k_1+k_2$、$b=-k_1'-k_2'$，第二道为 $a=k_1-k_1'$、$b=k_2-k_2'$，第三道为 $a=k_1-k_2'$、$b=k_2-k_1'$。于是只须求

<span id="eq:c10-vertex-integral"></span>

$$
\begin{aligned}
I(a,b)
&=\int d^4y\,d^4z\,e^{iay+ibz}\Delta(y-z)\\
&=\int\frac{d^4k}{(2\pi)^4}
\frac1{k^2+m^2-i0}
\left[\int d^4y\,e^{i(a+k)y}\right]
\left[\int d^4z\,e^{i(b-k)z}\right]\\
&=\int\frac{d^4k}{(2\pi)^4}
\frac{(2\pi)^4\delta^4(a+k)(2\pi)^4\delta^4(b-k)}
{k^2+m^2-i0}\\
&=(2\pi)^4\delta^4(a+b)\,
\frac1{a^2+m^2-i0}.
\end{aligned}
\tag{10.18}
$$

第二行代入内部传播子的傅里叶表示以后，顶点坐标只出现在相位中，各自产生一份动量delta。第一份令 $k=-a$，并用它的 $(2\pi)^4$ 消去动量积分测度中的分母；第二份留下总体守恒delta和一份 $(2\pi)^4$。传播核的分母依赖 $k^2$，所以也可按图中箭头的方向，将内线动量记为 $q=a=-k$，这个反向变量变换的绝对Jacobian为1。

三道的 $a+b=k_1+k_2-k_1'-k_2'$ 相同，故都带同一总体守恒因子：

<span id="eq:c10-tree-S"></span>

$$
\begin{aligned}
S_{fi}^{\rm conn}
={}&(2\pi)^4\delta^4(k_1+k_2-k_1'-k_2')\,ig^2\\
&\times\left[
\frac1{q_s^2+m^2-i0}
+\frac1{q_t^2+m^2-i0}
+\frac1{q_u^2+m^2-i0}
\right]+O(g^4).
\end{aligned}
\tag{10.19}
$$

总体delta是平移不变性所要求的动量守恒，过程的其余信息都在它的系数中。将这个因子和一个 $i$ 提出，定义散射振幅（scattering amplitude）$\mathcal T$：

<span id="eq:c10-amplitude-definition"></span>

$$
\begin{aligned}
S_{fi}^{\rm conn}
&=(2\pi)^4\delta^4(k_{\rm in}-k_{\rm out})\,i\mathcal T,\\
\mathcal T_{\rm tree}
&=g^2\sum_{r=s,t,u}\frac1{q_r^2+m^2-i0}.
\end{aligned}
\tag{10.20}
$$

其中 $k_{\rm in}$、$k_{\rm out}$ 分别是全部入射和出射粒子的总四动量；时间排序仍用 $\mathrm T$ 表示。振幅 $\mathcal T$ 的整体号承接本节的传播子及相互作用约定，由式[（10.16）](#eq:c10-amputation-phase)中的相位乘积确定。

为了看出三道与散射运动学的关系，引入Mandelstam变量（Mandelstam variables）$s=-q_s^2$、$t=-q_t^2$、$u=-q_u^2$。在 $(-+++)$ 度规下，振幅因而可写为

<span id="eq:c10-mandelstam-amplitude"></span>

$$
\mathcal T_{\rm tree}
=-g^2\left[
\frac1{s-m^2+i0}
+\frac1{t-m^2+i0}
+\frac1{u-m^2+i0}
\right].
\tag{10.21}
$$

整体负号来自每个传播子分母中提出的一份负号，相互作用的约定保持不变。以质心系为例，入射三动量取为 $\pm\mathbf p$，出射三动量取为 $\pm\mathbf p'$，其中 $|\mathbf p'|=|\mathbf p|=p$。四个粒子的能量均为 $E=\sqrt{m^2+p^2}$，散射角由 $\mathbf p\cdot\mathbf p'=p^2\cos\theta$ 确定。把这些动量代入三个四矢量平方，得到

<span id="eq:c10-com-invariants"></span>

$$
\begin{aligned}
s&=4(m^2+p^2),&
t&=-2p^2(1-\cos\theta),\\
u&=-2p^2(1+\cos\theta),&
s+t+u&=4m^2.
\end{aligned}
\tag{10.22}
$$

交换两个出射粒子，将 $\theta\to\pi-\theta$，也就是 $t\leftrightarrow u$，而三道之和保持不变，符合相同粒子的交换对称性。对 $m>0$ 的物理弹性区，$s\ge4m^2$、$t,u\le0$，三个内部单粒子极点都在该区域之外。再取阈值极限 $p\to0$，振幅为 $\mathcal T_{\rm tree}=5g^2/(3m^2)$：其中 $s$ 道给出 $-g^2/(3m^2)$，另外两道各给 $g^2/m^2$。这个简单极限同时保留了三种交换途径的相对号及总的质量量纲。

<span id="c10-loops"></span>

## 从顶点守恒得到圈积分测度

前面的两个顶点各产生一份四维delta，一份消去内线动量，另一份表示整个过程的四动量守恒。推广到一般连通图时，也可以先按这个办法处理所有顶点。考虑至少含一个相互作用顶点的图，设其内部线数为 $I$，内部顶点数为 $V$。给每条内线任选方向并赋予四动量 $q_e$，则每个顶点的坐标积分给出

<span id="eq:c10-vertex-conservation"></span>

$$
\int d^4x_v\,
\exp\!\left[i x_v\left(p_v+\sum_e \mathsf B_{ve}q_e\right)\right]
=(2\pi)^4\delta^4\!\left(p_v+\sum_e\mathsf B_{ve}q_e\right).
\tag{10.23}
$$

这里 $p_v$ 是进入该顶点的有号外动量之和，出射动量取负号。连接矩阵 $\mathsf B$ 在内线起点取 $-1$，在终点取 $+1$，其余为零；若选用相反的傅里叶动量方向，同时令 $q_e\to-q_e$，所得关系不变。把全部顶点的约束相加，一条内线总是出现两次且符号相反，内部动量于是全部抵消，留下 $\sum_vp_v=k_{\rm in}-k_{\rm out}=0$ 这一总体约束。

其余 $V-1$ 个约束的独立性，可以用生成树直接说明。在连通图中选一棵连接全部顶点的树，它含有 $V-1$ 条线。先将其余内线动量作为自由变量，再从树的一片叶子开始消元：该叶子只有一条尚未确定的树线，顶点守恒以系数 $+1$ 或 $-1$ 唯一解出它的四动量。删去这个叶子，便可对新的叶子重复同一步骤，直到只剩根点。这样恰好确定全部 $V-1$ 条树线，根点方程则是总体守恒；各次消元的绝对Jacobian均为1，所以不再产生额外的行列式。

每条非树内线与树上连接其两端的唯一路径组成一个独立圈。把这些非树线的动量作为圈动量，尚未被守恒确定的四动量数便为

<span id="eq:c10-loop-number"></span>

$$
L=I-V+1.
\tag{10.24}
$$

这里 $L$ 指独立圈数。复杂图中可能画出更多闭合路径，但其他路径可由这些独立圈组合得到，不会增加独立积分变量。树图的 $L=0$，因此所有内线动量都已由外动量确定。

积分测度也随消元一同确定。每条内线最初的傅里叶变换带有 $d^4q_e/(2\pi)^4$，每个顶点则带 $(2\pi)^4\delta^4$。用 $V-1$ 份delta依次积掉树线动量，每次恰好消去一组 $(2\pi)^4$，最终剩下

<span id="eq:c10-loop-measure"></span>

$$
(2\pi)^4\delta^4(k_{\rm in}-k_{\rm out})
\prod_{\alpha=1}^{L}\int\frac{d^4\ell_\alpha}{(2\pi)^4}.
\tag{10.25}
$$

圈积分测度和树图内线动量的唯一确定，都由这一顶点消元过程得到。实标量传播子的分母是动量的偶函数，反转任一内线箭头并同时换变量也不会改变图值；有调节器时，调节因子须随变量一起变换。

<span id="c10-rules"></span>

## 动量空间的费曼规则

现在可以将这些计算整理成动量空间费曼规则。先为给定的外粒子标签列出所有拓扑不等价的连通图，每条外线接到相互作用顶点上；在本节模型中，普通顶点都是三价的。再标上外线的物理入、出动量，为内线选定方向，并按刚才的方法施加顶点守恒。完成这些步骤以后，线和顶点各提供一个局部因子：

<span id="eq:c10-momentum-rules"></span>

$$
\begin{aligned}
\text{已约化外线}:&\quad 1,\\
\text{内线 }q:&\quad \frac{-i}{q^2+m^2-i0},\\
\text{三价顶点}:&\quad iZ_g g,\\
\text{二价反项}:&\quad -i(Aq^2+Bm^2).
\end{aligned}
\tag{10.26}
$$

外线因子1来自式[（10.15）](#eq:c10-external-amputation)的约化，内部传播因子和三价顶点则分别来自 $\Delta/i$ 的傅里叶变换与坐标空间顶点。二价反项已在式[（9.45）](/posts/srednicki-09/#eq:c09-counterterm-momentum)中求出，其两侧只有同一四动量流过。由于 $A,B=O(g^2)$，插入这些反项时，也必须把它们自身的阶数计入所要计算的总阶数。

将内部动量约束解出，再乘上各线及顶点的因子，每幅图对振幅的贡献为

<span id="eq:c10-general-graph"></span>

$$
\begin{aligned}
(i\mathcal T)_G
={}&\frac1{S_G^{\rm fixed}}
\left[\prod_{\alpha=1}^{L}
\int\frac{d^4\ell_\alpha}{(2\pi)^4}\right]
\prod_{e=1}^{I}\frac{-i}{q_e^2+m^2-i0}\\
&\times
\prod_{v\ {\rm cubic}}iZ_g g
\prod_{w\ {\rm ct}}[-i(Aq_w^2+Bm^2)].
\end{aligned}
\tag{10.27}
$$

总体守恒delta已经依照振幅的定义提出。各条内线的 $q_e$ 由外动量和独立圈动量 $\ell_\alpha$ 线性组成，因此只须对剩余圈动量积分。将给定阶数的全部图相加，得到该阶的 $i\mathcal T$，再除以整体的 $i$，便是 $\mathcal T$。

系数 $S_G^{\rm fixed}$ 要在保持全部外标签不动的条件下计算，允许的交换只涉及相同内部顶点、内部线及自环端点。上一节积分源叶的交换因子已经由源导数处理；这里的树图有 $S_G^{\rm fixed}=1$，圈图则还可能保留内部对称性。例如固定双线泡的两端后，两条内部线仍可互换，故 $S^{\rm fixed}=2$，而相应积分源图的因子为 $S=4$。将这个泡插入一幅已区别左右两端的图中，仍应保留它的 $1/2$。

还需要按目标阶数决定画哪些图。对于纯三价连通图，场槽的计数给 $3V=2I+E$，独立圈数为 $L=I-V+1$，消去内部线数就有

<span id="eq:c10-coupling-order"></span>

$$
V=E+2L-2.
\tag{10.28}
$$

固定外腿数 $E$ 后，每添一个圈都要增加两个三价顶点。因此，有树图的过程从 $g^{E-2}$ 阶开始，下一圈通常进入 $g^E$ 阶；本节 $2\to2$ 过程的树阶为 $g^2$，一圈及相应反项为 $g^4$。这一计数确定给定阶数需要纳入的图。

图规则还应保持振幅的质量量纲。若有 $V_3$ 个三价顶点和 $V_2$ 个二价反项，计数关系变为 $3V_3+2V_2=2I+E$，圈数为 $L=I-V_3-V_2+1$。四维中一个圈测度的维数为4，内部传播子的维数为 $-2$，三价顶点为1，二价顶点为2，所以

<span id="eq:c10-amplitude-dimension"></span>

$$
[\mathcal T]
=4L-2I+V_3+2V_2
=4-E.
\tag{10.29}
$$

四腿振幅因而无量纲，树级结果中的 $g^2/(q^2+m^2)$ 正具有这一性质。

外线因子1对应物理质量和单位单粒子重叠。圈阶计算将自能与反项组合，使精确传播子在物理质量处具有单位留数，然后取LSZ极限。自能及其归一化将在[第14节](/posts/srednicki-14/)具体计算。

振幅由各道的相干叠加给出。[下一节](/posts/srednicki-11/)将把它换成可测量的截面和衰变率。

---

[← 第 9 节](/posts/srednicki-09/) · [章节地图](/srednicki/) · [第 11 节 →](/posts/srednicki-11/)
