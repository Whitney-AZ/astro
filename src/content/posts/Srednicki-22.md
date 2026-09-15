---
title: 'Srednicki §22 连续对称性与守恒流'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [22]
hideFromHome: true
draft: false
---

<span id="c22"></span>

第2节用生成元描述了平移和洛伦兹变换，现在可以从拉格朗日量出发，构造出这些生成元的具体表达式。我们先研究经典场论：拉格朗日量在连续变换下的不变性给出诺特流，流的时间分量在空间积分后给出守恒荷。接着把场变换放进路径积分，同一个守恒关系就成为关联函数之间的恒等式。其中的接触项将说明，守恒荷怎样作用于场。最后把这套方法用于时空对称性，便能得到能量、动量和洛伦兹生成元。

本节回到四维时空，采用度规$(-,+,+,+)$。先考虑一组实标量$\varphi_a$及只含一阶场导数的$\mathcal L(\varphi_a,\partial_\mu\varphi_a)$。以下$\Pi_a$表示正则动量，其场分量下标使它与前面的两点自能$\Pi(k^2)$相区别。

<span id="c22-noether"></span>

## 从场的变分得到诺特流

在固定坐标处作无穷小变换$\varphi_a\mapsto\varphi_a+\delta\varphi_a$。拉氏密度同时通过场和场的导数发生变化，依次使用链式法则，得到
<span id="eq:c22-lagrangian-variation"></span>

$$
\delta\mathcal L
=\frac{\partial\mathcal L}{\partial\varphi_a}\delta\varphi_a
+p_a^\mu\partial_\mu\delta\varphi_a,
\qquad
p_a^\mu=\frac{\partial\mathcal L}
 {\partial(\partial_\mu\varphi_a)}.
\tag{22.1}
$$

要看出这种变化与场方程的关系，需要对作用量$S=\int d^4y\,\mathcal L(y)$求泛函导数。场在一点的变动只直接影响同一点的场值，因此所需的两个基本关系为
<span id="eq:c22-functional-deltas"></span>

$$
\frac{\delta\varphi_b(y)}{\delta\varphi_a(x)}
=\delta_{ab}\delta^4(y-x),\qquad
\frac{\delta\partial_\mu\varphi_b(y)}{\delta\varphi_a(x)}
=\delta_{ab}\partial_\mu^y\delta^4(y-x).
\tag{22.2}
$$

第二式的delta导数作用于$y$。代入作用量后，把这个导数从delta函数移到$p_a^\mu(y)$上，分部积分便产生一个负号：
<span id="eq:c22-euler-derivative"></span>

$$
\begin{aligned}
E_a(x):=\frac{\delta S}{\delta\varphi_a(x)}
&=\int d^4y\left[
 \frac{\partial\mathcal L(y)}{\partial\varphi_a(y)}\delta^4(y-x)
 +p_a^\mu(y)\partial_\mu^y\delta^4(y-x)\right]\\
&=\frac{\partial\mathcal L(x)}{\partial\varphi_a(x)}
 -\partial_\mu p_a^\mu(x).
\end{aligned}
\tag{22.3}
$$

这一步可先取紧支撑变分，或取保持边界数据的变分，使表面项消失。经典作用量原理要求$E_a=0$，式[（22.3）](#eq:c22-euler-derivative)给出了其中的欧拉导数。现在便能在拉氏密度的变分中分出场方程项。

用式[（22.3）](#eq:c22-euler-derivative)把$\partial\mathcal L/\partial\varphi_a$改写为$\partial_\mu p_a^\mu+E_a$。这样，两个含$p_a^\mu$的项恰好合成乘积的导数，得到
<span id="eq:c22-off-shell-identity"></span>

$$
\delta\mathcal L
=\partial_\mu(p_a^\mu\delta\varphi_a)+E_a\delta\varphi_a.
\tag{22.4}
$$

将全导数内的量定义为诺特流，上式就成为这个流的散度关系：
<span id="eq:c22-noether-with-parameter"></span>

$$
j_\delta^\mu=p_a^\mu\delta\varphi_a,
\qquad
\partial_\mu j_\delta^\mu
=\delta\mathcal L-E_a\delta\varphi_a.
\tag{22.5}
$$

这个恒等式把拉氏密度的变化、流的散度和场方程联系在一起，而且到这一步仍未使用场方程。若变换使拉氏密度不变，再令场满足经典方程，右边两项都为零，便得到守恒流。

通常将无穷小变换写成$\delta\varphi_a=\epsilon R_a$，并提出常参数$\epsilon$。以下用$j^\mu=p_a^\mu R_a$表示去参数的流，于是$j_\delta^\mu=\epsilon j^\mu$。对上述对称变换，在场方程成立时，这个流满足连续性方程
<span id="eq:c22-continuity-equation"></span>

$$
\partial_\mu j^\mu
=\frac{\partial j^0}{\partial t}+\boldsymbol\nabla\cdot\mathbf j=0.
\tag{22.6}
$$

因此可以把$j^0$解释为荷密度，把$\mathbf j$解释为相应的流密度。对有限空间区域积分并使用散度定理，就把局域关系写成区域内的荷与穿过边界的通量之间的关系：
<span id="eq:c22-charge-flux"></span>

$$
\frac{d}{dt}\int_{|\mathbf x|<R}d^3x\,j^0
=-\int_{|\mathbf x|=R}dS_i\,j^i.
\tag{22.7}
$$

如果无穷远的总通量消失，$Q=\int d^3x\,j^0$便不随时间改变。对于局域波包，足够快的空间衰减可以保证这一点；在周期空间中，则由相对边界的通量相消。下面用一个具体的对称性来看，这个守恒荷究竟计数什么。

<span id="c22-complex-symmetry"></span>

## 一个复标量的相位对称性

考虑具有四次相互作用的复标量模型：
<span id="eq:c22-complex-lagrangian"></span>

$$
\mathcal L
=-\partial^\mu\varphi^\dagger\partial_\mu\varphi
-m^2\varphi^\dagger\varphi
-\frac\lambda4(\varphi^\dagger\varphi)^2.
\tag{22.8}
$$

将复场写成$\varphi=(\varphi_1+i\varphi_2)/\sqrt2$，就有$\varphi^\dagger\varphi=(\varphi_1^2+\varphi_2^2)/2$。动能展开中的两个交叉项也相消，因而同一个理论可写为
<span id="eq:c22-two-real-fields"></span>

$$
\mathcal L
=-\frac12\sum_{a=1}^2\partial^\mu\varphi_a\partial_\mu\varphi_a
-\frac{m^2}{2}(\varphi_1^2+\varphi_2^2)
-\frac{\lambda}{16}(\varphi_1^2+\varphi_2^2)^2.
\tag{22.9}
$$

这里的$1/\sqrt2$使每个实场都具有标准的$1/2$动能系数；四次势的$1/16$则来自原系数$1/4$再乘两个$1/2$。复场和两个实场因此只是同一理论的两种场坐标，下面也可以用这两种写法分别求出其守恒流。

先在复场形式下，对实常数$\alpha$作相位变换
<span id="eq:c22-u1-transformation"></span>

$$
\varphi\mapsto e^{-i\alpha}\varphi,\qquad
\varphi^\dagger\mapsto e^{i\alpha}\varphi^\dagger.
\tag{22.10}
$$

每个$\varphi^\dagger\varphi$中的相位互相消去，常相位又可穿过导数，所以拉氏密度保持不变。相位因子$e^{-i\alpha}$可看作一个$1\times1$酉矩阵，这些变换组成$U(1)$群。把实部和虚部分开，同一变换就成为两个实场之间的旋转：
<span id="eq:c22-so2-transformation"></span>

$$
\begin{pmatrix}\varphi_1\\\varphi_2\end{pmatrix}
\mapsto
\begin{pmatrix}
\cos\alpha&\sin\alpha\\
-\sin\alpha&\cos\alpha
\end{pmatrix}
\begin{pmatrix}\varphi_1\\\varphi_2\end{pmatrix}.
\tag{22.11}
$$

这个矩阵的转置乘自身为1，行列式为$\cos^2\alpha+\sin^2\alpha=1$，所以它属于$SO(2)$。若采用平面内逆时针为正的习惯，矩阵所表示的旋转角是$-\alpha$。如此便得到$U(1)$相位与$SO(2)$实旋转之间的对应。

求流时只需要无穷小形式，即$R_\varphi=-i\varphi$、$R_{\varphi^\dagger}=i\varphi^\dagger$。可以把$\varphi,\varphi^\dagger$作为独立变分坐标；这等价于先对$\varphi_1,\varphi_2$求导，再取相应的线性组合。对两个坐标分别求动量密度，并代入诺特流定义，得到
<span id="eq:c22-complex-current"></span>

$$
\begin{aligned}
j^\mu
&=(-\partial^\mu\varphi^\dagger)(-i\varphi)
  +(-\partial^\mu\varphi)(i\varphi^\dagger)\\
&=-i\left[
 \varphi^\dagger\partial^\mu\varphi
 -(\partial^\mu\varphi^\dagger)\varphi\right]
=-i\varphi^\dagger\overleftrightarrow{\partial^\mu}\varphi.
\end{aligned}
\tag{22.12}
$$

这里采用双向导数$A\overleftrightarrow{\partial^\mu}B
=A\partial^\mu B-(\partial^\mu A)B$。方括号取共轭后变为自身的负值，因而是纯虚的；乘以$-i$便得到它的虚部。因此，流也可写成$\operatorname{Im}[\varphi^\dagger\overleftrightarrow{\partial^\mu}\varphi]$，其中仍包含双向导数的两项。

用实场形式也能求出相同的流。由式[（22.11）](#eq:c22-so2-transformation)读出$R_1=\varphi_2$、$R_2=-\varphi_1$，代入两项实场动量密度，便有
<span id="eq:c22-real-current"></span>

$$
j^\mu
=(-\partial^\mu\varphi_1)\varphi_2
 +(-\partial^\mu\varphi_2)(-\varphi_1)
=\varphi_1\partial^\mu\varphi_2
 -\varphi_2\partial^\mu\varphi_1.
\tag{22.13}
$$

直接展开式[（22.12）](#eq:c22-complex-current)也得到这一表达式，因此流与选择复场还是实场坐标无关。再用$\partial^0=-\partial_t$写出时间分量，就得到荷密度及其空间积分：
<span id="eq:c22-charge-definition"></span>

$$
j^0=i(\varphi^\dagger\dot\varphi-\dot\varphi^\dagger\varphi)
=\Pi_1\varphi_2-\Pi_2\varphi_1,\qquad
Q=\int d^3x\,j^0.
\tag{22.14}
$$

<span id="c22-particle-charge"></span>

## 荷为什么是两种粒子数之差

守恒流已经确定，要理解总荷的粒子意义，还需把它写成模式系数。先在经典理论中采用如下模式坐标：
<span id="eq:c22-classical-modes"></span>

$$
\begin{aligned}
\varphi(x)&=\int d\widetilde k\,
 [a(\mathbf k)e^{ikx}+b^*(\mathbf k)e^{-ikx}],\\
\varphi^\dagger(x)&=\int d\widetilde k\,
 [b(\mathbf k)e^{ikx}+a^*(\mathbf k)e^{-ikx}],\\
d\widetilde k&=\frac{d^3k}{(2\pi)^3\,2\omega_{\mathbf k}},
\qquad
kx=\mathbf k\cdot\mathbf x-\omega_{\mathbf k}t.
\end{aligned}
\tag{22.15}
$$

对自由场，这些系数不随时间变化。对于相互作用场，也可在某个固定时刻用同样的展开表示场值及其一阶时间导数，此时模式系数是一组初始数据；若要取到渐近时刻，则仍须使用此前散射理论的渐近场条件。

现在把两份模式展开及其时间导数代入$j^0$。令左边来自$\varphi^\dagger$的动量为$p$，右边来自$\varphi$的动量为$k$。两种模式各取一项，共有下面四类乘积，时间导数分别给出所列的频率系数：

| 模式乘积                       | $j^0$中的频率系数                          | 空间积分产生的条件     |
| ------------------------------ | ------------------------------------------ | ---------------------- |
| $a^*(\mathbf p)a(\mathbf k)$   | $\omega_{\mathbf p}+\omega_{\mathbf k}$    | $\mathbf p=\mathbf k$  |
| $b(\mathbf p)b^*(\mathbf k)$   | $-(\omega_{\mathbf p}+\omega_{\mathbf k})$ | $\mathbf p=\mathbf k$  |
| $b(\mathbf p)a(\mathbf k)$     | $\omega_{\mathbf k}-\omega_{\mathbf p}$    | $\mathbf p=-\mathbf k$ |
| $a^*(\mathbf p)b^*(\mathbf k)$ | $\omega_{\mathbf p}-\omega_{\mathbf k}$    | $\mathbf p=-\mathbf k$ |

例如第一行来自$i[a^*e^{-ipx}(-i\omega_k a e^{ikx})
 -(i\omega_p a^*e^{-ipx})a e^{ikx}]$，两个时间导数因而给出频率之和。后两行在空间delta函数上满足$\omega_{\mathbf p}=\omega_{\mathbf k}$，频率之差为零，所以它们对总荷没有贡献。第一行剩下的归一化则为
<span id="eq:c22-charge-mode-normalization"></span>

$$
\begin{aligned}
&\int d\widetilde p\,d\widetilde k\,
 (\omega_{\mathbf p}+\omega_{\mathbf k})
 (2\pi)^3\delta^3(\mathbf p-\mathbf k)
 a^*(\mathbf p)a(\mathbf k)\\
&\hspace{10mm}=\int d\widetilde k\,
 \frac{2\omega_{\mathbf k}}{2\omega_{\mathbf k}}
 a^*(\mathbf k)a(\mathbf k).
\end{aligned}
\tag{22.16}
$$

第二行作相同的积分，同时保留其频率系数前的负号。把两个非零部分合起来，总荷为
<span id="eq:c22-classical-mode-charge"></span>

$$
Q_{\rm cl}
=\int d\widetilde k\,
 [a^*(\mathbf k)a(\mathbf k)-b(\mathbf k)b^*(\mathbf k)].
\tag{22.17}
$$

量子化以后，两套模式满足$[a(\mathbf p),a^\dagger(\mathbf k)]
=[b(\mathbf p),b^\dagger(\mathbf k)]
=(2\pi)^3\,2\omega_{\mathbf k}\delta^3(\mathbf p-\mathbf k)$，混合对易子为零。若沿用上面的经典次序，荷算符先写成$a^\dagger a-bb^\dagger$，其中含有一个排序产生的真空常数。本节选择相位不变的真空并令$Q|0\rangle=0$，对自由或渐近模式作正规排序，就得到
<span id="eq:c22-number-difference"></span>

$$
Q=\int d\widetilde k\,
 [a^\dagger(\mathbf k)a(\mathbf k)
  -b^\dagger(\mathbf k)b(\mathbf k)]
=N_a-N_b.
\tag{22.18}
$$

总荷于是等于两种粒子数之差。它对单粒子的作用可以直接由对易子看出：用$[AB,C]=A[B,C]+[A,C]B$展开，模式对易关系中的delta函数消去积分测度，便有
<span id="eq:c22-creation-charges"></span>

$$
[Q,a^\dagger(\mathbf k)]=a^\dagger(\mathbf k),\qquad
[Q,b^\dagger(\mathbf k)]=-b^\dagger(\mathbf k).
\tag{22.19}
$$

因此每个$a$粒子对总荷贡献$+1$，每个$b$粒子贡献$-1$。将这些关系代回场展开，得到$[Q,\varphi]=-\varphi$、$[Q,\varphi^\dagger]=\varphi^\dagger$，正好产生最初的相位变换。

这一生成作用也可由正则场直接求出。对于不含时间导数的内部变换 $R_a$，取对称排序的荷

<span id="eq:c22-canonical-internal-charge"></span>

$$
Q_R=\frac12\int d^3y\,[\Pi_aR_a+R_a\Pi_a].
$$

$R_a$ 只依赖等时场及其空间导数，与 $\varphi_b$ 对易。因此只有荷中的正则动量参与收缩：

<span id="eq:c22-canonical-charge-action"></span>

$$
\begin{aligned}
\relax[\varphi_b(\mathbf x),Q_R]
&=\frac i2\int d^3y\,\delta_{ab}\delta^3(\mathbf x-\mathbf y)
 [R_a(\mathbf y)+R_a(\mathbf y)]\\
&=iR_b(\mathbf x).
\end{aligned}
$$

取 $R_\varphi=-i\varphi$ 就回到上述荷对易子。保留局域密度时，同一计算给出 $[j_R^0(x),\varphi_b(y)]_{x^0=y^0}=-iR_b(y)\delta^3(\mathbf x-\mathbf y)$，后面时间序乘积中的接触项正由它产生。

荷的守恒进一步限制了可能的散射过程。若入、出态$|\alpha\rangle,|\beta\rangle$都是守恒荷的本征态，而且散射保持这项对称性，就有
<span id="eq:c22-selection-rule"></span>

$$
0=\langle\beta|[Q,S]|\alpha\rangle
=(q_\beta-q_\alpha)\langle\beta|S|\alpha\rangle.
\tag{22.20}
$$

只要入出净荷不同，散射振幅便为零。这个选择定则也逐顶点体现在费曼图中：相互作用$(\varphi^\dagger\varphi)^2$包含两条$\varphi$腿和两条$\varphi^\dagger$腿，所以每个顶角流入、流出的净荷相等。其$2!\,2!$种微分分配又恰好抵消拉氏密度中的$1/4$，留下固定腿标签的顶角权重$-i\lambda$。

<span id="c22-schwinger-dyson"></span>

## 路径积分中的场方程

模式展开已经给出守恒荷的粒子解释。为了把局域流的守恒也写成量子理论中的关系，先研究场方程在关联函数里以什么形式出现。仍从带源路径积分出发：
<span id="eq:c22-source-generator"></span>

$$
Z[J]=\int\mathcal D\varphi\,
 \exp\!\left(iS[\varphi]+i\int d^4x\,J_a\varphi_a\right),
\qquad Z[0]=1.
\tag{22.21}
$$

作与场无关的无穷小位移$\varphi_a(x)\mapsto\varphi_a(x)+h_a(x)$，其中$h_a$光滑且具有紧支撑，并假定所用调节的测度和边界允许这一换元。积分值保持不变；将指数按$h$展开到一阶，便有
<span id="eq:c22-shift-identity"></span>

$$
0=i\int\mathcal D\varphi\,e^{iS+i\int J\varphi}
 \int d^4x\,h_a(x)[E_a(x)+J_a(x)].
\tag{22.22}
$$

要由这个积分恒等式得到关联函数之间的关系，对$J_{a_r}(x_r)$作$n$次导数，再令$J=0$。记$O=\prod_{r=1}^n\varphi_{a_r}(x_r)$，并用$O_{\widehat r}$表示去掉第$r$个因子的乘积。

这些导数有两种作用方式。若全部落在指数上，连同积分外面的$i$，会产生$i^{n+1}E_aO$；若其中一次落在显式的$J_a(x)$上，就产生$\delta_{aa_r}\delta^4(x-x_r)$，其余$n-1$次仍作用于指数，系数为$i^n$。由于显式源只出现一次，对它作第二次导数便为零。约去公共的$i^n$后，剩下
<span id="eq:c22-source-differentiated"></span>

$$
0=\int d^4x\,h_a(x)\left[
 i\langle E_a(x)O\rangle_{\rm PI}
 +\sum_{r=1}^n\delta_{aa_r}\delta^4(x-x_r)
  \langle O_{\widehat r}\rangle_{\rm PI}\right].
\tag{22.23}
$$

下标PI表示按照原路径积分定义的插入。每个外标签各有一次机会与显式源配对，因此恰好出现$n$个接触项，计数中没有另一个$n!$。再利用测试函数$h_a(x)$的任意性，取出它在每一点的系数，就得到施温格–戴森方程（Schwinger–Dyson equations）：
<span id="eq:c22-schwinger-dyson"></span>

$$
i\langle\mathrm T E_a(x)O\rangle
+\sum_{r=1}^n\delta_{aa_r}\delta^4(x-x_r)
 \langle\mathrm T O_{\widehat r}\rangle=0.
\tag{22.24}
$$

场方程由此成为关联函数之间的恒等式。含导数的插入仍按路径积分的导数处方解释，也就是对整个时间序关联函数求导，包括其中表示时间排序的阶跃函数。这个规定正是接触项的来源，在自由实场中可以直接看到。

令$C(x-y)=\langle\mathrm T\varphi(x)\varphi(y)\rangle$，先显式写出两个时间顺序：
<span id="eq:c22-time-ordering"></span>

$$
C=\theta(x^0-y^0)\langle\varphi(x)\varphi(y)\rangle
 +\theta(y^0-x^0)\langle\varphi(y)\varphi(x)\rangle.
\tag{22.25}
$$

第一次对时间求导，阶跃函数产生的delta项乘以$[\varphi(x),\varphi(y)]$，在等时为零。再求一次导数，则留下$[\dot\varphi(x),\varphi(y)]$，由正则对易关系得到
<span id="eq:c22-time-contact"></span>

$$
\partial_{x^0}^2 C
=\langle\mathrm T\ddot\varphi(x)\varphi(y)\rangle
-i\delta(x^0-y^0)\delta^3(\mathbf x-\mathbf y).
\tag{22.26}
$$

将自由场方程用于通常的二阶导数部分，这些项互相抵消，而时间排序产生的接触项留下来，使二点函数满足
<span id="eq:c22-green-contact"></span>

$$
(-\Box_x+m^2)\,iC(x-y)=\delta^4(x-y),
\qquad
\Delta(x-y)=iC(x-y).
\tag{22.27}
$$

这也重现了[第8节的格林方程](/posts/srednicki-08/#c08-contact)。传播子成为波动算符的格林函数，所需的非齐次项恰好来自时间排序的接触项。

当$x$与所有$x_r$分离时，式[（22.24）](#eq:c22-schwinger-dyson)中的delta函数都没有支撑，因而$\langle\mathrm T E_a(x)O\rangle=0$。这说明场方程在不重合的关联函数插入中仍然成立；到了重合点，就要保留接触项。对于相互作用理论，$E_a$和其他复合插入也须采用同一调节及重整化定义，才能在这些关系中一致地使用。

<span id="c22-ward"></span>

## 量子流与Ward恒等式

现在把一般场位移换成使拉氏密度不变的对称变换，以求出量子流的守恒关系。为提取局域信息，先将常参数换成紧支撑函数$\epsilon(x)$：
<span id="eq:c22-localized-variation"></span>

$$
\delta_\epsilon\varphi_a(x)=\epsilon(x)R_a[\varphi](x).
\tag{22.28}
$$

常参数变换使拉氏密度不变，但参数依赖位置以后，它的导数会产生新的项。把$\partial_\mu(\epsilon R_a)
=\epsilon\partial_\mu R_a+(\partial_\mu\epsilon)R_a$代入链式变分，便可将两类项分开：
<span id="eq:c22-local-action-variation"></span>

$$
\delta_\epsilon\mathcal L
=\epsilon\,\delta_R\mathcal L
 +(\partial_\mu\epsilon)p_a^\mu R_a
=(\partial_\mu\epsilon)j^\mu.
\tag{22.29}
$$

最后一步用了常参数对称性$\delta_R\mathcal L=0$。对时空积分，再通过分部积分移去$\epsilon$上的导数，就有$\delta_\epsilon S=-\int d^4x\,\epsilon\,\partial_\mu j^\mu$。因此局域参数把流的散度从作用量变分中挑了出来，而且这个等式对路径积分中的任意场都成立，无须先满足运动方程。

在含插入$O$的零源路径积分中作同一换元。如果测度和积分域保持不变，一阶变化便由插入本身及作用量的变化组成：
<span id="eq:c22-ward-variable-change"></span>

$$
0=\langle\delta_\epsilon O\rangle
 +i\langle O\,\delta_\epsilon S\rangle.
\tag{22.30}
$$

插入是各点场的乘积，所以它的变分是依次改变其中一个因子的和：

$$
\delta_\epsilon O
=\sum_r\epsilon(x_r)\varphi_{a_1}(x_1)\cdots
 R_{a_r}(x_r)\cdots\varphi_{a_n}(x_n).
$$

把每个$\epsilon(x_r)$改写为$\int d^4x\,\epsilon(x)\delta^4(x-x_r)$，所有项就带有同一个测试函数。再取任意$\epsilon(x)$的系数，得到
<span id="eq:c22-ward-identity"></span>

$$
\begin{aligned}
\partial_\mu\langle\mathrm Tj^\mu(x)O\rangle
=-i\sum_{r=1}^n\delta^4(x-x_r)
 \left\langle\mathrm T
 \varphi_{a_1}(x_1)\cdots R_{a_r}(x_r)\cdots
 \varphi_{a_n}(x_n)\right\rangle .
\end{aligned}
\tag{22.31}
$$

这个关系称为Ward恒等式，也称Ward–Takahashi恒等式。若从始至终保留无穷小常参数，只须同时以$j_\delta^\mu,\delta\varphi_a$替换$j^\mu,R_a$，便得到含常参数的同一个恒等式。

对本节的 $SO(2)$ 模型，可以在每个调节格点上分别作实旋转；即使角度随位置改变，旋转矩阵的行列式仍为1，因而满足推导所用的局域测度不变性。Ward 式于是把流的散度集中在各插入点，接触项由相应场的对称变换决定。

为看清这些接触项如何表达荷，考察自由复场的一个三点函数。记$C=\Delta/i$，对去掉真空常数的$j^\mu$和$\varphi(y)\varphi^\dagger(z)$作Wick收缩。只有两种$\varphi$与$\varphi^\dagger$的配对参与连通部分，因而
<span id="eq:c22-current-three-point"></span>

$$
\begin{aligned}
G^\mu(x;y,z)
&:=\langle\mathrm Tj^\mu(x)\varphi(y)\varphi^\dagger(z)
 \rangle_{\rm conn}\\
&=-i\left[
 C(y-x)\partial_x^\mu C(x-z)
 -\partial_x^\mu C(y-x)\,C(x-z)\right].
\end{aligned}
\tag{22.32}
$$

对它取散度时，两个一阶导数的乘积互相消去。余下的两个$\Box C$用$(\Box-m^2)C=i\delta^4$改写，质量项也成对相消，最后只剩
<span id="eq:c22-explicit-ward-check"></span>

$$
\partial_\mu G^\mu(x;y,z)
=[\delta^4(x-z)-\delta^4(x-y)]C(y-z).
\tag{22.33}
$$

另一方面，在式[（22.31）](#eq:c22-ward-identity)中代入$R_\varphi=-i\varphi$和$R_{\varphi^\dagger}=i\varphi^\dagger$，同样得到$y$点的负号和$z$点的正号。两个接触项的相反符号，由此与两类粒子的相反荷联系起来。

<span id="c22-energy-momentum"></span>

## 平移对称性与能量–动量张量

还可以把对称性的条件稍作推广：拉氏密度的变分只要是全散度，作用量仍可在适当边界条件下不变。设$\delta\mathcal L=\partial_\mu K^\mu$，由式[（22.4）](#eq:c22-off-shell-identity)移项，便得到相应的流
<span id="eq:c22-quasisymmetry-current"></span>

$$
j_\delta^\mu=p_a^\mu\delta\varphi_a-K^\mu,
\qquad
\partial_\mu j_\delta^\mu=-E_a\delta\varphi_a.
\tag{22.34}
$$

场方程成立时，这个流仍然守恒。若重复局域参数的推导，拉氏变分中会多出$\partial_\mu(\epsilon K^\mu)$，但积分后该表面项消失，只留下$(\partial_\mu\epsilon)j^\mu$，因而仍可按前面的方式得到流的关系。

时空平移正属于这种情形。对主动变换$\varphi_a(x)\mapsto\varphi_a(x-a)$取无穷小参数，场和拉氏密度分别变化为
<span id="eq:c22-translation-variation"></span>

$$
\delta\varphi_a=-a^\nu\partial_\nu\varphi_a,\qquad
\delta\mathcal L=-a^\nu\partial_\nu\mathcal L
=\partial_\mu(-a^\mu\mathcal L),
\qquad K^\mu=-a^\mu\mathcal L.
\tag{22.35}
$$

将这个结果代入式[（22.34）](#eq:c22-quasisymmetry-current)，再提出常参数$a_\nu$，就能从流中读出一个二阶张量：
<span id="eq:c22-stress-tensor"></span>

$$
\begin{aligned}
j_\delta^\mu
&=-p_a^\mu a^\nu\partial_\nu\varphi_a+a^\mu\mathcal L
=a_\nu T^{\mu\nu},\\
T^{\mu\nu}
&=-p_a^\mu\partial^\nu\varphi_a+g^{\mu\nu}\mathcal L.
\end{aligned}
\tag{22.36}
$$

其中$+a^\mu\mathcal L$来自流定义中的$-K^\mu$。平移参数$a_\nu$任意，所以场方程给出$\partial_\mu T^{\mu\nu}=0$，每个平移方向都有相应的守恒流。

为识别这些流的物理意义，取具有标准动能的实标量模型：
<span id="eq:c22-canonical-scalar-model"></span>

$$
\mathcal L=-\frac12\partial^\mu\varphi_a\partial_\mu\varphi_a-V(\varphi),
\qquad
p_a^\mu=-\partial^\mu\varphi_a,\qquad
\Pi_a=p_a^0=\dot\varphi_a.
\tag{22.37}
$$

四维可重整化势 $V$ 的次数至多为四；以下荷的计算适用于一般的无导数势。将当前标准动能的动量密度代入便得
<span id="eq:c22-symmetric-stress"></span>

$$
T^{\mu\nu}
=\partial^\mu\varphi_a\partial^\nu\varphi_a
 +g^{\mu\nu}\mathcal L,
\qquad T^{\mu\nu}=T^{\nu\mu}.
\tag{22.38}
$$

这一张量是对称的。再用$\partial^0=-\partial_t$和$g^{00}=-1$展开其时间分量，得到
<span id="eq:c22-energy-and-momentum-density"></span>

$$
\begin{aligned}
T^{00}
&=\Pi_a^2-\mathcal L
=\frac12\Pi_a^2+\frac12(\boldsymbol\nabla\varphi_a)^2+V(\varphi)
=\mathcal H,\\
T^{0i}&=-\Pi_a\,\partial_i\varphi_a.
\end{aligned}
\tag{22.39}
$$

$T^{00}$就是正则哈密顿密度，而$T^{0i}$则应当描述动量密度。为求出它的模式形式，先取自由质量矩阵的对角场，对每个实场在式[（22.15）](#eq:c22-classical-modes)中令$b=a$。不同场的模式对易子带有$\delta_{ab}$，所以各物种分别贡献。

把展开代入空间积分后，$a_aa_a$及其共轭项中的delta函数要求$\mathbf p=-\mathbf k$，余下被积式在$\mathbf k\mapsto-\mathbf k$下为奇，故对称积分为零。混合项则留下$k^i$乘以数算符。正规排序后，总动量写成
<span id="eq:c22-momentum-modes"></span>

$$
P^i=\int d^3x\,T^{0i}
=\sum_a\int d\widetilde k\,k^i a_a^\dagger(\mathbf k)a_a(\mathbf k).
\tag{22.40}
$$

混合项的系数可以直接核对：来自 $-\dot\varphi\,\partial_i\varphi$ 的 $a^\dagger(\mathbf p)a(\mathbf k)$ 和 $a(\mathbf p)a^\dagger(\mathbf k)$ 都带 $+\omega_{\mathbf p}k_i$。空间积分给 $(2\pi)^3\delta^3(\mathbf p-\mathbf k)$，消去 $p$ 测度中的 $2\omega_{\mathbf p}$ 后，两项各留下 $k_i/2$，故

<span id="eq:c22-momentum-normalization"></span>

$$
P^i=\frac12\sum_a\int d\widetilde k\,k^i
 [a_a^\dagger a_a+a_a a_a^\dagger]
\;\longrightarrow\;
\sum_a\int d\widetilde k\,k^i a_a^\dagger a_a.
$$

箭头表示将真空动量取为零的正规排序；各物种的测度使用各自质量。每个粒子对总动量贡献自己的动量，加上前面识别出的总能量，得到能量–动量四矢量
<span id="eq:c22-four-momentum"></span>

$$
P^\mu=\int d^3x\,T^{0\mu}(x).
\tag{22.41}
$$

<span id="c22-translations"></span>

## 守恒荷实际生成平移

得到荷的显式形式后，就可以进一步确定它对场的作用。无穷小平移关系可由正则对易子$[\varphi_a(t,\mathbf x),\Pi_b(t,\mathbf y)]
=i\delta_{ab}\delta^3(\mathbf x-\mathbf y)$直接求出。哈密顿量中的势与梯度只含等时场，因而都与$\varphi_a$对易；动量平方则产生两个相等的项。分别计算时间与空间分量，得到
<span id="eq:c22-translation-commutators"></span>

$$
\begin{aligned}
\relax[\varphi_a(\mathbf x),P^0]
&=\frac12\int d^3y\,
 [\varphi_a(\mathbf x),\Pi_b(\mathbf y)^2]
=i\Pi_a(\mathbf x)
=\frac1i\partial^0\varphi_a(\mathbf x),\\
[\varphi_a(\mathbf x),P^i]
&=-\int d^3y\,
 [\varphi_a(\mathbf x),\Pi_b(\mathbf y)]
 \partial_i\varphi_b(\mathbf y)\\
&=-i\partial_i\varphi_a(\mathbf x)
=\frac1i\partial^i\varphi_a(\mathbf x).
\end{aligned}
\tag{22.42}
$$

空间动量若写成厄米排序 $P^i=-\frac12\int(\Pi_b\partial_i\varphi_b+\partial_i\varphi_b\Pi_b)$，两个收缩各贡献一半，结果相同。两个分量合起来，正是$[\varphi_a,P^\mu]=\partial^\mu\varphi_a/i$，所以这些荷的无穷小作用已经具有平移的形式。

接着定义$T(a)=e^{-iP^\mu a_\mu}$，并引入$F(\tau)=e^{i\tau P\cdot a}\varphi_a(x)e^{-i\tau P\cdot a}$。这样就能把有限共轭作用化成关于参数的微分方程。使用刚求出的对易子，有
<span id="eq:c22-translation-exponentiation"></span>

$$
\frac{dF}{d\tau}
=i\,e^{i\tau P\cdot a}[P\cdot a,\varphi_a(x)]e^{-i\tau P\cdot a}
=-a^\mu\partial_\mu F,\qquad F(0)=\varphi_a(x).
\tag{22.43}
$$

沿初始条件解这个一阶方程，得到$F(\tau)=\varphi_a(x-\tau a)$，从而
<span id="eq:c22-finite-translation"></span>

$$
T(a)^{-1}\varphi_a(x)T(a)=\varphi_a(x-a).
\tag{22.44}
$$

因此，从拉格朗日量构造的正则荷确实实现了第2节规定的平移作用；时间分量和有限变换指数中的符号也随同一个对易关系确定下来。

<span id="c22-lorentz"></span>

## 洛伦兹流与生成元

最后考虑洛伦兹对称性。标量场的无穷小变化为$\delta\varphi_a=\delta\omega^\nu{}_\rho x^\rho\partial_\nu\varphi_a$，其中$\delta\omega_{\nu\rho}=-\delta\omega_{\rho\nu}$。与平移变分相比，它相当于取位置依赖的参数$a^\nu(x)=-\delta\omega^\nu{}_\rho x^\rho$。参数现在也要参与求导，流的散度因而成为
<span id="eq:c22-lorentz-parameter-gradient"></span>

$$
\partial_\mu(a_\nu T^{\mu\nu})
=(\partial_\mu a_\nu)T^{\mu\nu}
+a_\nu\partial_\mu T^{\mu\nu}.
\tag{22.45}
$$

第二项由场方程下的能量–动量守恒而消失；第一项则是反对称参数与对称张量$T^{\mu\nu}$的缩并，也为零。因此，对当前标量模型仍能得到守恒流。将洛伦兹参数提出，并只保留与它反对称部分相配的系数，就可写成
<span id="eq:c22-lorentz-current"></span>

$$
\begin{aligned}
j_\delta^\mu
&=\frac12\delta\omega_{\nu\rho}\mathcal M^{\mu\nu\rho},\\
\mathcal M^{\mu\nu\rho}
&=x^\nu T^{\mu\rho}-x^\rho T^{\mu\nu}.
\end{aligned}
\tag{22.46}
$$

由于$\delta\omega_{\nu\rho}$反对称，第二行的两项与它缩并后相等，所以第一行要乘$1/2$。也可以直接对这个流求散度，观察张量对称性与平移守恒怎样共同使它为零：
<span id="eq:c22-lorentz-current-divergence"></span>

$$
\begin{aligned}
\partial_\mu\mathcal M^{\mu\nu\rho}
&=T^{\nu\rho}-T^{\rho\nu}
 +x^\nu\partial_\mu T^{\mu\rho}
 -x^\rho\partial_\mu T^{\mu\nu}
=0.
\end{aligned}
\tag{22.47}
$$

这里求导时缩并的是第一个指标，后两个指标则反对称。标量场没有独立的自旋指标，所以洛伦兹流由这个轨道形式给出。将其时间分量作空间积分，得到相应的守恒荷：
<span id="eq:c22-lorentz-charge"></span>

$$
M^{\nu\rho}
=\int d^3x\,[x^\nu T^{0\rho}-x^\rho T^{0\nu}].
\tag{22.48}
$$

由于流中带有坐标因子，荷的守恒还要求带坐标权重的无穷远通量消失。再用推导式[（22.42）](#eq:c22-translation-commutators)时的局域delta函数，把积分中的坐标取在场所在的点，就得到荷对场的作用
<span id="eq:c22-lorentz-field-action"></span>

$$
[\varphi_a(x),M^{\nu\rho}]
=\frac1i(x^\nu\partial^\rho-x^\rho\partial^\nu)\varphi_a(x).
\tag{22.49}
$$

这正是第2节中的标量微分表示，式[（22.48）](#eq:c22-lorentz-charge)因而给出了所需洛伦兹生成元的具体场表达式。

<span id="c22-generator-algebra"></span>

## 从能量和动量密度算出生成元代数

先在经典正则理论中计算。用光滑紧支撑权重积分能量和动量密度，定义

<span id="eq:c22-weighted-charges"></span>

$$
H[f]=\int d^3x\,fT^{00},\qquad
P[\xi]=-\int d^3x\,\Pi_a\xi_i\partial_i\varphi_a.
$$

对场及正则动量分别变分，再把 $\delta\varphi_a$ 上的导数分部积分，得到四个泛函导数：

<span id="eq:c22-weighted-derivatives"></span>

$$
\begin{aligned}
\frac{\delta H[f]}{\delta\Pi_a}&=f\Pi_a,&
\frac{\delta H[f]}{\delta\varphi_a}&=-\partial_i(f\partial_i\varphi_a)+fV_{,a},\\
\frac{\delta P[\xi]}{\delta\Pi_a}&=-\xi_i\partial_i\varphi_a,&
\frac{\delta P[\xi]}{\delta\varphi_a}&=\partial_i(\xi_i\Pi_a).
\end{aligned}
$$

将它们放入泊松括号的定义

$$
\{F,G\}_{\rm P}=\int d^3x\left(
\frac{\delta F}{\delta\varphi_a}\frac{\delta G}{\delta\Pi_a}
-\frac{\delta F}{\delta\Pi_a}\frac{\delta G}{\delta\varphi_a}\right).
$$

两份能量的势项相消，空间二阶导数也相消，只剩权重的一阶导数：

<span id="eq:c22-energy-bracket"></span>

$$
\begin{aligned}
\{H[f],H[g]\}_{\rm P}
&=\int d^3x\,\Pi_a
 [f\partial_i(g\partial_i\varphi_a)-g\partial_i(f\partial_i\varphi_a)]\\
&=\int d^3x\,\Pi_a(f\partial_i g-g\partial_i f)\partial_i\varphi_a\\
&=P[g\nabla f-f\nabla g].
\end{aligned}
$$

对一份动量和一份能量，将动量平方、梯度平方及势的贡献分别积分，三部分为

<span id="eq:c22-mixed-bracket-pieces"></span>

$$
\begin{aligned}
I_\Pi&=\frac12\int d^3x\,\Pi_a^2
 [-\xi_i\partial_i f+f\partial_i\xi_i],\\
I_\nabla&=-\frac12\int d^3x\,(\nabla\varphi_a)^2
 [\xi_i\partial_i f+f\partial_i\xi_i]
 +\int d^3x\,f\,\partial_j\xi_i\partial_i\varphi_a\partial_j\varphi_a,\\
I_V&=-\int d^3x\,V[\xi_i\partial_i f+f\partial_i\xi_i].
\end{aligned}
$$

例如梯度项原为 $-\int\xi_i\partial_i\varphi_a\partial_j(f\partial_j\varphi_a)$；分部积分后，用 $\partial_j\varphi_a\partial_i\partial_j\varphi_a=\frac12\partial_i(\nabla\varphi_a)^2$ 就得到第二行。将三行相加，$\partial_i f$ 的系数组成能量密度，其余部分组成 $T^{ij}$。两份动量的计算则消去二阶场导数，给出

<span id="eq:c22-weighted-brackets"></span>

$$
\begin{aligned}
\{P[\xi],H[f]\}_{\rm P}
&=-H[\xi\cdot\nabla f]+\int d^3x\,fT^{ij}\partial_j\xi_i,\\
\{P[\xi],P[\eta]\}_{\rm P}
&=\int d^3x\,\Pi_a[
 \xi_i\partial_i(\eta_j\partial_j\varphi_a)
 -\eta_j\partial_j(\xi_i\partial_i\varphi_a)]\\
&=P[\eta\cdot\nabla\xi-\xi\cdot\nabla\eta].
\end{aligned}
$$

现在选取全局荷的权重。常数或坐标权重可先乘大半径截断，再在前述衰减条件下去掉截断。设 $e_i$ 为第 $i$ 个常单位向量，记

<span id="eq:c22-global-weights"></span>

$$
\begin{gathered}
H=H[1],\qquad P_i=P[e_i],\qquad B_i=H[x_i],\qquad
K_i=M^{i0}=B_i-tP_i,\\
J_i=\frac12\epsilon_{ijk}M^{jk}=P[\xi_i],\qquad
(\xi_i)_k=\epsilon_{ijk}x_j.
\end{gathered}
$$

常权重的导数为零，所以 $\{P_i,P_j\}_{\rm P}=\{P_i,H\}_{\rm P}=0$。含一个坐标权重时，有

<span id="eq:c22-boost-brackets"></span>

$$
\begin{aligned}
\{B_i,H\}_{\rm P}&=P_i,&
\{B_i,P_j\}_{\rm P}&=\delta_{ij}H,\\
\{B_i,B_j\}_{\rm P}
&=P[x_j e_i-x_i e_j]=-M^{ij},\\
\{K_i,K_j\}_{\rm P}
&=-M^{ij}-t\delta_{ij}H+t\delta_{ij}H=-M^{ij}.
\end{aligned}
$$

转动权重的导数 $\partial_\ell(\xi_i)_k=\epsilon_{i\ell k}$ 反对称，与 $T^{k\ell}$ 缩并为零。因而混合括号给 $\{J_i,H\}_{\rm P}=0$、$\{J_i,B_j\}_{\rm P}=\epsilon_{ijk}B_k$；两份动量的括号给 $\{J_i,P_j\}_{\rm P}=\epsilon_{ijk}P_k$。最后，

$$
(\xi_j\cdot\nabla\xi_i-\xi_i\cdot\nabla\xi_j)_\ell
=\delta_{j\ell}x_i-\delta_{i\ell}x_j
=\epsilon_{ijk}(\xi_k)_\ell,
$$

所以 $\{J_i,J_j\}_{\rm P}=\epsilon_{ijk}J_k$，各个经典括号均已确定。

在量子理论中，取保持平移与洛伦兹对称性的厄米荷，以及场和荷的共同不变定义域；在所讨论的真空扇区中令各荷湮灭真空。相应的量子代数为
<span id="eq:c22-poincare-algebra"></span>

$$
\begin{gathered}
\relax[J_i,J_j]=i\epsilon_{ijk}J_k,\qquad
[J_i,K_j]=i\epsilon_{ijk}K_k,\qquad
[K_i,K_j]=-i\epsilon_{ijk}J_k,\\
[J_i,P_j]=i\epsilon_{ijk}P_k,\qquad [J_i,H]=0,\\
[K_i,P_j]=i\delta_{ij}H,\qquad [K_i,H]=iP_i,\qquad
[P_\mu,P_\nu]=0.
\end{gathered}
\tag{22.50}
$$

这一量子关系可从荷对场的作用直接确定。将各个荷记为 $Q_A$，把式[（22.42）](#eq:c22-translation-commutators)与式[（22.49）](#eq:c22-lorentz-field-action)写成 $[\varphi,Q_A]=D_A\varphi$；这些微分算符满足 $[D_A,D_B]=if_{AB}{}^CD_C$，其中 $f_{AB}{}^C$ 就是上述结构常数。雅可比恒等式于是给出

<span id="eq:c22-quantum-algebra-proof"></span>

$$
\begin{aligned}
\relax[\varphi,[Q_A,Q_B]]
&=[[\varphi,Q_A],Q_B]-[[\varphi,Q_B],Q_A]\\
&=[D_A,D_B]\varphi=[\varphi,if_{AB}{}^CQ_C],\\
C_{AB}&=[Q_A,Q_B]-if_{AB}{}^CQ_C,\qquad[\varphi,C_{AB}]=0.
\end{aligned}
$$

由于 $C_{AB}|0\rangle=0$，把它移过任意涂抹场多项式，便知它湮灭这些多项式作用在真空上产生的态。若这些态在当前真空扇区稠密且属于共同定义域，则对其中的任意 $|\chi\rangle$ 和域内的 $|\psi\rangle$，厄米荷使 $C_{AB}$ 反厄米，因而 $\langle\chi|C_{AB}\psi\rangle=-\langle C_{AB}\chi|\psi\rangle=0$。稠密性随即给出 $C_{AB}|\psi\rangle=0$，得到式[（22.50）](#eq:c22-poincare-algebra)的全局荷代数。

---

[← 第 21 节](/posts/srednicki-21/) · [章节地图](/srednicki/) · [第 23 节 →](/posts/srednicki-23/)
