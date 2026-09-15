---
title: 'Srednicki §3 标量场的正则量子化'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [3]
hideFromHome: true
draft: false
---

<span id="c03"></span>

现在把第 1 节的多粒子哈密顿量简化为自由粒子的情形。在动量表象中，每个模式的能量可以直接换成相对论表达式。我们将从一个洛伦兹不变的经典实标量场作用量出发，通过正则量子化重新得到这个哈密顿量。

<span id="c03-fourier"></span>

## 自由粒子的动量表象

先暂时只令 $\hbar=1$，保留 $c$。第1节的无相互作用哈密顿量是 $H=\int d^3x\,a^\dagger(-\nabla^2/2m)a$。自由粒子的动量不随时间改变，因此在动量表象中，哈密顿量应当最为简单。定义如下傅里叶变换，并为这一归一化的动量算符保留波浪号：

<span id="eq:c03-fourier"></span>

$$
\begin{aligned}
\widetilde a(\mathbf p)
 &=\int\frac{d^3x}{(2\pi)^{3/2}}
       e^{-i\mathbf p\cdot\mathbf x}a(\mathbf x),\\
a(\mathbf x)
 &=\int\frac{d^3p}{(2\pi)^{3/2}}
       e^{i\mathbf p\cdot\mathbf x}\widetilde a(\mathbf p).
\end{aligned}
\tag{3.1}
$$

把第二行代回第一行，空间平面波的完备关系便还原原函数，因而两式确实互为逆变换。接下来把两份逆变换代入 $H$。拉普拉斯只作用于它右侧的指数，于是

<span id="eq:c03-free-nr"></span>

$$
\begin{aligned}
H&=\int\frac{d^3x\,d^3p\,d^3q}{(2\pi)^3}
\widetilde a^\dagger(\mathbf p)e^{-i\mathbf p\cdot\mathbf x}
\frac{\mathbf q^2}{2m}e^{i\mathbf q\cdot\mathbf x}
\widetilde a(\mathbf q)\\
&=\int d^3p\,\frac{\mathbf p^2}{2m}
\widetilde a^\dagger(\mathbf p)\widetilde a(\mathbf p).
\end{aligned}
\tag{3.2}
$$

动能前的负号被 $\nabla^2e^{i\mathbf q\cdot\mathbf x}=-\mathbf q^2e^{i\mathbf q\cdot\mathbf x}$抵消；空间积分产生的 $(2\pi)^3\delta^3(\mathbf q-\mathbf p)$再消去两个傅里叶因子的乘积，得到哈密顿量的动量空间形式。哈密顿量因而对每个动量模式分别计数。

要把这些模式解释为产生和湮灭算符，还须变换它们的代数。用 $[A,B]_- = AB-BA$ 表示对易子，$[A,B]_+=AB+BA$ 表示反对易子。从位置空间的正则对易关系（CCR）或反对易关系（CAR）出发，对两种统计都有

<span id="eq:c03-fourier-bracket"></span>

$$
\begin{aligned}
\relax[\widetilde a(\mathbf p),\widetilde a^\dagger(\mathbf q)]_{\mp}
&=\int\frac{d^3x\,d^3y}{(2\pi)^3}
 e^{-i\mathbf p\cdot\mathbf x+i\mathbf q\cdot\mathbf y}
 \delta^3(\mathbf x-\mathbf y)\\
&=\delta^3(\mathbf p-\mathbf q).
\end{aligned}
\tag{3.3}
$$

同类算符的两个括号也为零，因为相应的位置空间括号本来就是零。定义真空满足 $\widetilde a(\mathbf p)|0\rangle=0$后，便可逐个加入动量模式来构造多粒子态。第1节已经求过偶双线性哈密顿量与产生算符的普通对易子；这里的一体核是动量对角函数 $E(\mathbf p)$，所以相应结果为
$[H,\widetilde a^\dagger(\mathbf p)]=E(\mathbf p)\widetilde a^\dagger(\mathbf p)$。反复使用普通对易子的乘积法则，一条产生算符链的能量就是各 $E$之和。动量确定态是广义本征态，正规化的态则由波包构成。

既然上述代数只要求能量对各模式相加，最直接的相对论推广便是把色散关系换成

<span id="eq:c03-rel-start"></span>

$$
H_{\rm rel}=\int d^3p\,
\sqrt{\mathbf p^2c^2+m^2c^4}\,
\widetilde a^\dagger(\mathbf p)\widetilde a(\mathbf p)
\tag{3.4}
$$

这样就得到正能、可加的自由粒子谱。为了使洛伦兹不变性直接体现在动力学方程中，下面用经典标量场重新构造这一理论。

<span id="c03-action"></span>

## 经典场、作用量与自然单位

从这里起再令 $c=1$，于是 $x^0=t$、$k^0=\omega$。经典理论先以场及其运动方程为出发点；下面引入的 $m$此时只是逆长度参数，还没有粒子质量的解释。所选的方程为

<span id="eq:c03-kg"></span>

$$
(-\partial^2+m^2)\varphi=0,\qquad
\partial^2=-\partial_t^2+\nabla^2.
\tag{3.5}
$$

此时，$\varphi(x)$ 给每个时空点赋予一个实数。它的标量性质要求不同惯性系的观察者在同一事件上得到相同的场值，即 $\bar\varphi(\bar x)=\varphi(x)$，其中 $\bar x^\mu=\Lambda^\mu{}_\nu x^\nu+a^\mu$。

KG方程具有局域形式，因而可以尝试从只含同一点场及其导数的作用量密度导出它。最简单的选择是

<span id="eq:c03-action"></span>

$$
\begin{aligned}
S&=\int d^4x\,\mathcal L,\\
\mathcal L&=-\frac12\partial^\mu\varphi\,\partial_\mu\varphi
-\frac12m^2\varphi^2+\Omega_0\\
&=\frac12\dot\varphi^2-\frac12(\boldsymbol\nabla\varphi)^2
-\frac12m^2\varphi^2+\Omega_0.
\end{aligned}
\tag{3.6}
$$

总拉格朗日量为 $L(t)=\int d^3x\,\mathcal L(\mathbf x,t)$，相应作用量是 $S=\int dt\,L(t)=\int d^4x\,\mathcal L$。由 $\Lambda^Tg\Lambda=g$可知 $|\det\Lambda|=1$，四维体积元保持不变；密度中的导数指标又完全缩并，所以整个作用量具有洛伦兹不变性。在相应边界条件下，加上全导数也不会改变场方程。这里保留常数 $\Omega_0$，因为它虽不参与场方程，却会进入哈密顿量的常数项，稍后可以用来选择能量零点。

现在检验这个作用量是否给出所需方程。对场作变分时，动能的两个场因子各贡献一项，两项相同，消去原来的 $1/2$。在有限区域 $\mathcal D$上分部积分，把导数从变分移回场，得

<span id="eq:c03-variation"></span>

$$
\begin{aligned}
\delta S
&=\int_{\mathcal D}d^4x\,
\bigl[-\partial^\mu\varphi\,\partial_\mu\delta\varphi
-m^2\varphi\,\delta\varphi\bigr]\\
&=-\int_{\partial\mathcal D}d\Sigma_\mu\,
  \partial^\mu\varphi\,\delta\varphi
+\int_{\mathcal D}d^4x\,(\partial^2\varphi-m^2\varphi)\delta\varphi.
\end{aligned}
\tag{3.7}
$$

要求边界上 $\delta\varphi=0$，表面项便消失。区域内部的变分任意，所以它的系数必须为零，得到式[（3.5）](#eq:c03-kg)。

为了随后量子化，先将场改写成哈密顿形式。固定时间后，每个 $\mathbf x$都是一个连续的坐标标签，其共轭动量密度定义为 $\Pi=\partial\mathcal L/\partial\dot\varphi$。本例的速度二次项非退化，可以解出 $\dot\varphi=\Pi$，所以Legendre变换逐项给出

<span id="eq:c03-legendre"></span>

$$
\begin{aligned}
\Pi&=\dot\varphi,\\
\mathcal H&=\Pi\dot\varphi-\mathcal L
=\frac12\Pi^2+\frac12(\boldsymbol\nabla\varphi)^2
+\frac12m^2\varphi^2-\Omega_0,\qquad
H=\int d^3x\,\mathcal H.
\end{aligned}
\tag{3.8}
$$

哈密顿形式明确了一个场在固定时刻需要的正则资料：空间每一点都有场坐标和共轭动量，共轭动量本身是密度，哈密顿密度还须对空间积分才给出能量。下面反演模式系数时，正好要同时使用这两份资料。

<span id="c03-modes"></span>

## 实性如何联系两支频率

自由场的方程对不同空间波矢彼此独立，因而适合用傅里叶变换求解。对空间作变换后，式[（3.5）](#eq:c03-kg)化为常系数方程
$\ddot\varphi_{\mathbf k}+\omega_{\mathbf k}^2\varphi_{\mathbf k}=0$，其中 $\omega_{\mathbf k}=\sqrt{\mathbf k^2+m^2}>0$。先取 $m>0$，用光滑且迅速衰减的初始数据作傅里叶展开。每个模式都是二阶时间方程，需要两份初始数据，因此一般解含有两支频率：

<span id="eq:c03-two-frequency"></span>

$$
\varphi(\mathbf x,t)=\int\frac{d^3k}{f(\mathbf k)}
\left[A(\mathbf k)e^{i\mathbf k\cdot\mathbf x-i\omega t}
+B(\mathbf k)e^{i\mathbf k\cdot\mathbf x+i\omega t}\right].
\tag{3.9}
$$

这里暂取 $f$为实、偶、非零的径向函数；它可以吸收到系数中，当前只用来保留归一化的选择。两支系数也不能任意独立，因为我们要求场为实。对上式取共轭，再在整个积分中作 $\mathbf k\mapsto-\mathbf k$换元，Jacobian的绝对值为一，得到

<span id="eq:c03-reality"></span>

$$
\varphi^*(\mathbf x,t)=\int\frac{d^3k}{f(\mathbf k)}
\left[B^*(-\mathbf k)e^{i\mathbf k\cdot\mathbf x-i\omega t}
+A^*(-\mathbf k)e^{i\mathbf k\cdot\mathbf x+i\omega t}\right].
\tag{3.10}
$$

现在两个展开已经使用相同的平面波，可以比较各支频率的系数。实性要求 $B^*(-\mathbf k)=A(\mathbf k)$；把这一关系代回原展开，再只对负频率项反向换元，便得到

<span id="eq:c03-real-modes"></span>

$$
\varphi(x)=\int\frac{d^3k}{f(\mathbf k)}
\left[A(\mathbf k)e^{ikx}+A^*(\mathbf k)e^{-ikx}\right],
\quad kx=\mathbf k\cdot\mathbf x-\omega t,\quad k^2=-m^2.
\tag{3.11}
$$

实性把正、负频率的系数联系起来，而 $A(\mathbf k)$ 与 $A(-\mathbf k)$ 仍是两个独立的模式。对一对相反波矢，这也对应余弦和正弦两份实振动，所以式[（3.11）](#eq:c03-real-modes)中的积分遍及全部空间波矢。

<span id="c03-measure"></span>

## 为什么不变测度含有 $2\omega$

展开中的四动量满足 $k^2=-m^2$，称为在质量壳上（on shell），简称在壳。系数用 $k^0>0$ 壳上的点编号，负频率部分由共轭项给出。为了使展开便于作洛伦兹变换，现在选择归一化函数，使三维测度成为质量壳上的不变测度。从四维形式 $d^4k\,\delta(k^2+m^2)\theta(k^0)$ 出发：$d^4k$ 和壳约束都不变，正时洛伦兹变换又保持正能支，所以整个测度不变。

消去能量积分后，就能读出所需的三维测度。为此先说明delta函数的换元：设光滑函数 $g(z)$有简单零点 $z_j$，在各零点附近令 $u=g(z)$，由 $|dz/du|=1/|g'(z_j)|$，对任意测试函数 $F$得

<span id="eq:c03-delta-jacobian"></span>

$$
\int dz\,F(z)\delta(g(z))
=\sum_j\frac{F(z_j)}{|g'(z_j)|}.
\tag{3.12}
$$

绝对值来自积分测度的换元，使每个简单零点都贡献正的权重。这里 $g(k^0)=\omega^2-(k^0)^2$有两个零点 $\pm\omega$，两处导数的绝对值都是 $2\omega$，因此

<span id="eq:c03-measure"></span>

$$
\begin{aligned}
\delta(k^2+m^2)
&=\frac{\delta(k^0-\omega)+\delta(k^0+\omega)}{2\omega},\\
\int dk^0\,\delta(k^2+m^2)\theta(k^0)&=\frac1{2\omega},\\
d\widetilde k&\equiv\frac{d^3k}{(2\pi)^3\,2\omega_{\mathbf k}}.
\end{aligned}
\tag{3.13}
$$

二次函数的正负两个根都进入delta函数的分解，乘上 $\theta$以后才只剩正根的贡献。其中 $2\omega$由Jacobian固定，$(2\pi)^3$则是配合傅里叶变换的常数选择。取 $f=(2\pi)^3\,2\omega$，再把 $A$改记为 $a$，实场展开便成为

<span id="eq:c03-field-expansion"></span>

$$
\varphi(x)=\int d\widetilde k\,
\left[a(\mathbf k)e^{ikx}+a^*(\mathbf k)e^{-ikx}\right].
\tag{3.14}
$$

把所有模式写在同一个不变测度下以后，参考系改变时只需重新标记质量壳上的点。也可以直接用三维Jacobian看出这一点。沿第一轴取速度参数 $\beta$，有
$k'_1=\gamma(k_1-\beta\omega)$、$k'_{2,3}=k_{2,3}$、
$\omega'=\gamma(\omega-\beta k_1)$。由于 $\partial\omega/\partial k_1=k_1/\omega$，三维换元矩阵的后两行是单位行，只须求第一行的导数。这里用了相对运动参考系常见的负非对角元写法；相对于第2节正参数 $\eta$的主动推动，参数关系为 $\beta=-\tanh\eta$。在这一约定下，

<span id="eq:c03-boost-jacobian"></span>

$$
\det\frac{\partial\mathbf k'}{\partial\mathbf k}
=\gamma\left(1-\frac{\beta k_1}{\omega}\right)
=\frac{\omega'}{\omega}>0.
\tag{3.15}
$$

因此 $d^3k'/\omega'=d^3k/\omega$，与四维壳约束的计算一致。

<span id="c03-inversion"></span>

## 从场的初始数据反演模式

展开式给出了从模式到场的映射；要将场的正则关系转成模式的量子代数，还需要把它反解。式[（3.14）](#eq:c03-field-expansion)同时含正负两项，因此只对 $\varphi$作空间傅里叶变换还不能分离出 $a$。利用同一时刻的场和速度，定义两份投影
$F_{\mathbf k}=\int d^3x\,e^{-ikx}\varphi(x)$、
$G_{\mathbf k}=\int d^3x\,e^{-ikx}\dot\varphi(x)$。对正频率项，空间积分给 $\delta^3(\mathbf q-\mathbf k)$，对负频率项则给 $\delta^3(\mathbf q+\mathbf k)$；后者在 $\mathbf q=-\mathbf k$时仍留下时间相位 $e^{2i\omega t}$。因此

<span id="eq:c03-two-projections"></span>

$$
\begin{aligned}
F_{\mathbf k}
&=\frac{a(\mathbf k)+e^{2i\omega t}a^*(-\mathbf k)}{2\omega},\\
G_{\mathbf k}
&=-\frac{i}{2}a(\mathbf k)
+\frac{i}{2}e^{2i\omega t}a^*(-\mathbf k).
\end{aligned}
\tag{3.16}
$$

第二行的正负号来自 $\partial_te^{\mp i\omega t}=\mp i\omega e^{\mp i\omega t}$。这使两份投影恰好可以分离两支频率：在 $\omega F+iG$中，负频率系数相消，正频率的两个 $1/2$相加，便得到反演公式：

<span id="eq:c03-inverse"></span>

$$
\begin{aligned}
a(\mathbf k)&=\int d^3x\,e^{-ikx}(\omega\varphi+i\Pi)
=i\int d^3x\,e^{-ikx}\overleftrightarrow{\partial_0}\varphi,\\
a^*(\mathbf k)&=\int d^3x\,e^{ikx}(\omega\varphi-i\Pi).
\end{aligned}
\tag{3.17}
$$

第一行的第二种写法使用双向导数的定义 $f\overleftrightarrow{\partial_0}g=f\dot g-\dot f\,g$。因为 $\partial_0e^{-ikx}=i\omega e^{-ikx}$，双向导数前的 $i$使第二项成为 $+\omega\varphi$，还原同一行中的 $\omega\varphi+i\Pi$。

同一个经典解可以在不同时刻提供初始资料，反演所得的模式系数却应当相同。对第一行求总时间导数，两个交叉项先抵消，再代入KG方程，得

<span id="eq:c03-mode-constant"></span>

$$
\frac{d a(\mathbf k)}{dt}
=i\int d^3x\,e^{-ikx}(\ddot\varphi+\omega^2\varphi)
=i\int d^3x\,e^{-ikx}(\nabla^2+\mathbf k^2)\varphi=0.
\tag{3.18}
$$

最后一步对空间作两次分部积分，边界项按本节的衰减假设消失。这说明反演系数确实与所选时刻无关。量子化后，反演仍带有显式时间核，其不随时间改变的含义不变；通常的振子海森堡算符则是 $a_H(t)=e^{-i\omega t}a$，时间因子已被放在算符中。两种写法只是把同一模式的时间依赖放在不同位置。

<span id="c03-ccr"></span>

## 正则量子化与模式对易关系

有了场、共轭动量以及它们与模式的相互转换，就可以实施正则量子化。把 $\varphi,\Pi$提升为厄米算符值分布，并在同一时刻施加正则对易公设：

<span id="eq:c03-canonical"></span>

$$
\begin{gathered}
\relax[\varphi(\mathbf x,t),\varphi(\mathbf y,t)]=0,\qquad
[\Pi(\mathbf x,t),\Pi(\mathbf y,t)]=0,\\
[\varphi(\mathbf x,t),\Pi(\mathbf y,t)]
=i\delta^3(\mathbf x-\mathbf y).
\end{gathered}
\tag{3.19}
$$

这把量子力学的 $[q_j,p_l]=i\delta_{jl}$ 推广到连续的坐标标签。算符值分布的等式可通过与光滑测试函数积分来理解。计算能量时，我们会先放入有限周期盒并截断高动量模式，将它化为有限个谐振子的计算。

经典模式系数现在也成为算符，反演式中的复共轭相应改为厄米共轭 $a^\dagger$。为求模式代数，令 $\omega=\omega_{\mathbf k}$、$\omega'=\omega_{\mathbf q}$。场与场、动量与动量的对易子都为零，只有两个交叉收缩保留下来：
$[\omega\varphi_{\mathbf x},-i\Pi_{\mathbf y}]=\omega\delta^3(\mathbf x-\mathbf y)$和
$[i\Pi_{\mathbf x},\omega'\varphi_{\mathbf y}]=\omega'\delta^3(\mathbf x-\mathbf y)$。第二项也为正，是因为 $[\Pi_{\mathbf x},\varphi_{\mathbf y}]=-i\delta^3(\mathbf x-\mathbf y)$。将它们连同反演中的指数一起积分，得到

<span id="eq:c03-mode-ccr"></span>

$$
\begin{aligned}
\relax[a(\mathbf k),a^\dagger(\mathbf q)]
&=(\omega+\omega')e^{i(\omega-\omega')t}
  \int d^3x\,e^{i(\mathbf q-\mathbf k)\cdot\mathbf x}\\
&=(2\pi)^3\,2\omega\,\delta^3(\mathbf k-\mathbf q).
\end{aligned}
\tag{3.20}
$$

同类模式的计算只改变一个符号：第二个反演也含 $+i\Pi$，因此两个交叉收缩相减，系数变为 $\omega'-\omega$。相应的指数积分给出

<span id="eq:c03-aa-zero"></span>

$$
[a(\mathbf k),a(\mathbf q)]
=(2\pi)^3(\omega'-\omega)e^{i(\omega+\omega')t}
\delta^3(\mathbf k+\mathbf q)=0.
\tag{3.21}
$$

在 delta 的支撑上 $\mathbf q=-\mathbf k$，色散又是偶函数，因而整个系数为零。再取厄米共轭，得 $[a^\dagger,a^\dagger]=0$，这就求出了全部模式对易关系。

还可以从模式代数回到场代数，确认两份频率各自怎样贡献正则归一化。将所得关系代回场展开，在等时条件下有

<span id="eq:c03-ccr-back"></span>

$$
[\varphi(\mathbf x,t),\Pi(\mathbf y,t)]
=\frac i2\int\frac{d^3k}{(2\pi)^3}
\left[e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}
+e^{-i\mathbf k\cdot(\mathbf x-\mathbf y)}\right]
=i\delta^3(\mathbf x-\mathbf y).
\tag{3.22}
$$

两个频率部分各贡献一半。对于 $\varphi\varphi$ 和 $\Pi\Pi$ 的对易子，得到的则是两个指数之差，权重分别为偶函数 $1/(2\omega)$ 和 $\omega/2$；作 $\mathbf k\mapsto-\mathbf k$ 换元，两项便相消。场和模式的正则对易关系因此互相还原。接下来计算哈密顿量，求出产生算符对能量的作用。

<span id="c03-hamiltonian"></span>

## 哈密顿量中四类模式项的去向

现在用模式重写能量，看看场量子是否具有本节开头所需的相对论粒子谱。经典乘积 $a^*a$量子化后会涉及排序，不同排序可相差常数。因此先保留场哈密顿量中所有因子的次序，待空间积分完成以后，再用对易关系整理成 $a^\dagger a$的形式。先写出场及其时间、空间导数：

<span id="eq:c03-derivative-modes"></span>

$$
\begin{aligned}
\varphi&=\int d\widetilde k\,(a_{\mathbf k}e^{ikx}
+a^\dagger_{\mathbf k}e^{-ikx}),\\
\Pi&=\int d\widetilde k\,(-i\omega a_{\mathbf k}e^{ikx}
+i\omega a^\dagger_{\mathbf k}e^{-ikx}),\\
\boldsymbol\nabla\varphi&=\int d\widetilde k\,
(i\mathbf k a_{\mathbf k}e^{ikx}
-i\mathbf k a^\dagger_{\mathbf k}e^{-ikx})
\end{aligned}
\tag{3.23}
$$

把它们逐项代入式[（3.8）](#eq:c03-legendre)，即可按频率组合整理能量。$\Pi^2$的同频率系数是 $(-i\omega)(-i\omega')=-\omega\omega'$，梯度平方贡献 $-\mathbf k\cdot\mathbf q$，质量项贡献 $m^2$；相反频率时，前两项都变为正号。为合并三种贡献，定义
$C_s=-\omega\omega'-\mathbf k\cdot\mathbf q+m^2$、
$C_o=\omega\omega'+\mathbf k\cdot\mathbf q+m^2$，
空间积分后保留下列四类模式项：

<span id="eq:c03-h-four-terms"></span>

$$
\begin{aligned}
H+\Omega_0 V
=\frac{(2\pi)^3}{2}\int d\widetilde k\,d\widetilde q\,
\bigl\{&
C_s\delta^3(\mathbf k+\mathbf q)
\bigl[a_{\mathbf k}a_{\mathbf q}e^{-i(\omega+\omega')t}
+a^\dagger_{\mathbf k}a^\dagger_{\mathbf q}e^{i(\omega+\omega')t}\bigr]\\
&+C_o\delta^3(\mathbf k-\mathbf q)
\bigl[a^\dagger_{\mathbf k}a_{\mathbf q}e^{i(\omega-\omega')t}
+a_{\mathbf k}a^\dagger_{\mathbf q}e^{-i(\omega-\omega')t}\bigr]\bigr\}.
\end{aligned}
\tag{3.24}
$$

这里的空间积分用了平面波完备关系 $\int d^3x\,e^{i\mathbf Q\cdot\mathbf x}=(2\pi)^3\delta^3(\mathbf Q)$。delta函数随后把两个动量联系起来：同频率项取 $\mathbf q=-\mathbf k$，于是 $C_s=-\omega^2+\mathbf k^2+m^2=0$，使 $aa$与 $a^\dagger a^\dagger$项消失；混合项取 $\mathbf q=\mathbf k$，得到 $C_o=2\omega^2$，两个时间相位也都成为一。积分掉的 $d\widetilde q$提供 $1/[(2\pi)^3 2\omega]$，与空间积分系数和原来的 $1/2$合并为 $\omega/2$。因此

<span id="eq:c03-h-symmetric"></span>

$$
H=-\Omega_0V+\frac12\int d\widetilde k\,\omega
\left(a^\dagger_{\mathbf k}a_{\mathbf k}
+a_{\mathbf k}a^\dagger_{\mathbf k}\right).
\tag{3.25}
$$

为了把这个结果与普通谐振子联系起来，先放入体积 $V=L^3$的周期盒。此时 $\mathbf k=2\pi\mathbf n/L$，
$d^3k/(2\pi)^3$换成 $V^{-1}\sum_{\mathbf k}$，
$(2\pi)^3\delta^3(\mathbf k-\mathbf q)$换成 $V\delta_{\mathbf k\mathbf q}$。再令
$a_{\mathbf k}=\sqrt{2\omega_{\mathbf k}V}\,b_{\mathbf k}$，就得到通常的离散振子归一化：

<span id="eq:c03-box"></span>

$$
\begin{aligned}
\relax[b_{\mathbf k},b^\dagger_{\mathbf q}]&=\delta_{\mathbf k\mathbf q},\\
\varphi(x)&=\sum_{\mathbf k}
\frac{b_{\mathbf k}e^{ikx}+b^\dagger_{\mathbf k}e^{-ikx}}
{\sqrt{2\omega_{\mathbf k}V}},\\
H&=\sum_{\mathbf k}\omega_{\mathbf k}
\left(b^\dagger_{\mathbf k}b_{\mathbf k}+\frac12\right)-\Omega_0V.
\end{aligned}
\tag{3.26}
$$

量子实标量场由此分解成一组谐振子，每个空间波矢对应一个模式。两支频率共同保证场的厄米性。

<span id="c03-vacuum"></span>

## 零点能与真空能量

每个谐振子都有零点能，把无穷多个模式相加便会产生真空能的问题。回到连续记号，用模式CCR将式[（3.25）](#eq:c03-h-symmetric)中的 $aa^\dagger$移序。有限周期盒说明，其中出现的 $(2\pi)^3\delta^3(0)$表示 $V$的极限记号，而不是delta函数的普通点值。移序后得到

<span id="eq:c03-vacuum-density"></span>

$$
\begin{aligned}
H&=\int d\widetilde k\,\omega a^\dagger_{\mathbf k}a_{\mathbf k}
+(\mathcal E_0-\Omega_0)V,\\
\mathcal E_0&=\frac12\int\frac{d^3k}{(2\pi)^3}
\sqrt{\mathbf k^2+m^2}.
\end{aligned}
\tag{3.27}
$$

$\mathcal E_0$是每单位体积的零点能。先在所选参考系中引入球形紫外截断 $|\mathbf k|\leq\Lambda$，使积分有限。角积分给出 $4\pi$，剩下径向积分
$\mathcal E_0(\Lambda,m)=(4\pi^2)^{-1}\int_0^\Lambda dk\,k^2\sqrt{k^2+m^2}$。为了看清大截断近似舍去了哪些项，先完整求出这个积分。对 $m>0$令 $k=m\sinh u$，根号与微分便一起化成双曲函数：

<span id="eq:c03-vacuum-integral"></span>

$$
\begin{aligned}
k^2\sqrt{k^2+m^2}\,dk
&=m^4\sinh^2u\cosh^2u\,du
=\frac{m^4}{8}(\cosh4u-1)\,du,\\
\int_0^\Lambda dk\,k^2\sqrt{k^2+m^2}
&=m^4\left[\frac{\sinh4u}{32}-\frac u8\right]
 _{u=0}^{u=\operatorname{arsinh}(\Lambda/m)}.
\end{aligned}
\tag{3.28}
$$

积分下限为零。上限处用 $\sinh4u=4\sinh u\cosh u(1+2\sinh^2u)$还原原变量，得到

<span id="eq:c03-vacuum-exact"></span>

$$
\mathcal E_0(\Lambda,m)=\frac1{32\pi^2}
\left[
\Lambda\sqrt{\Lambda^2+m^2}(2\Lambda^2+m^2)
-m^4\operatorname{arsinh}\frac{\Lambda}{m}
\right].
\tag{3.29}
$$

这个闭式保留了质量与截断的完整关系。若截断远大于质量，可令 $z=m^2/\Lambda^2\ll1$，分别展开
$\sqrt{1+z}=1+z/2-z^2/8+O(z^3)$和
$\operatorname{arsinh}(\Lambda/m)=\log(2\Lambda/m)+z/4+O(z^2)$。前一项乘积为
$2\Lambda^4+2m^2\Lambda^2+m^4/4+O(m^6/\Lambda^2)$，合并后得

<span id="eq:c03-vacuum-asymptotic"></span>

$$
\mathcal E_0
=\frac{\Lambda^4}{16\pi^2}
+\frac{m^2\Lambda^2}{16\pi^2}
-\frac{m^4}{32\pi^2}\log\frac{2\Lambda}{m}
+\frac{m^4}{128\pi^2}
+O\left(\frac{m^6}{\Lambda^2}\right).
\tag{3.30}
$$

在 $\Lambda\gg m$时，只保留首项的相对误差从 $m^2/\Lambda^2$阶开始。若 $m=0$，径向积分直接成为 $k^3$的积分，首项才是该截断下的精确结果；在 $\Lambda\lesssim m$时，则应使用完整闭式而非大截断近似。

现在选择拉格朗日量中的常数为 $\Omega_0(\Lambda)=\mathcal E_0(\Lambda)$，就有 $H|0\rangle=0$。在当前平直时空的自由场论中，这相当于把真空选作能量零点：所有态的能量同时平移一个常数，能差与跃迁概率保持不变。减去这个常数后，哈密顿量便可在有限粒子波包上取 $\Lambda\to\infty$ 的极限。

<span id="c03-particles"></span>

## 粒子质量、态归一化与场的量纲

减去真空常数后，哈密顿量只剩模式占据数项。要与本节开头的粒子哈密顿量直接比较，只须改回最初的模式归一化。令

<span id="eq:c03-normalization-conversion"></span>

$$
a(\mathbf k)=\sqrt{(2\pi)^3\,2\omega_{\mathbf k}}\,
\widetilde a(\mathbf k).
\tag{3.31}
$$

将它代入式[（3.20）](#eq:c03-mode-ccr)，两个平方根在delta支撑上合并成 $(2\pi)^3 2\omega$，所以 $\widetilde a$满足式[（3.3）](#eq:c03-fourier-bracket)的玻色CCR。代入 $H$时，同一因子消去 $d\widetilde k$的分母，得到
$H=\int d^3k\,\omega_{\mathbf k}\widetilde a^\dagger\widetilde a$。这正是式[（3.4）](#eq:c03-rel-start)取自然单位后的形式：经典实标量场的量子化重新给出了自由相对论玻色子的能谱。

这一比较也赋予经典参数以粒子解释。若仍将 $m$视为逆长度并恢复单位，经典频率满足
$\omega_{\rm phys}^2/c^2=\mathbf k^2+m^2$。再用量子关系 $\mathbf p=\hbar\mathbf k$、$E=\hbar\omega_{\rm phys}$，得

<span id="eq:c03-mass-restoration"></span>

$$
E^2=c^2\mathbf p^2+\hbar^2c^2m^2,\qquad
M_{\rm phys}=\frac{\hbar m}{c},\qquad
E_{\rm rest}=\hbar c m.
\tag{3.32}
$$

把第一式与粒子的能量关系 $E^2=c^2\mathbf p^2+M_{\rm phys}^2c^4$比较，就能读出后两式的质量与静止能量。由于 $[m]=L^{-1}$，$\hbar cm$具有静止能量的量纲，而 $\hbar m/c$才具有质量的量纲。自然单位下两者的数值同为 $m$，恢复单位后则须使用各自的表达式。

除了能量，还要固定粒子态的归一化，才能计算波包和矩阵元。由模式代数，单粒子态 $|\mathbf k\rangle=a^\dagger(\mathbf k)|0\rangle$满足

<span id="eq:c03-state-norm"></span>

$$
\langle\mathbf q|\mathbf k\rangle
=(2\pi)^3\,2\omega_{\mathbf k}\delta^3(\mathbf q-\mathbf k).
\tag{3.33}
$$

因此，对波包 $|f\rangle=\int d\widetilde k\,f(\mathbf k)|\mathbf k\rangle$ 求内积时，用 delta 积掉一个动量，便得到范数平方 $\int d\widetilde k\,|f|^2$。

多粒子态的能量可以直接由对易关系求出。先计算

$$
\begin{aligned}
[H,a^\dagger(\mathbf q)]
&=\int d\widetilde k\,\omega_{\mathbf k}
a^\dagger(\mathbf k)[a(\mathbf k),a^\dagger(\mathbf q)]\\
&=\omega_{\mathbf q}a^\dagger(\mathbf q).
\end{aligned}
$$

令 $|\mathbf k_1\cdots\mathbf k_n\rangle=a^\dagger(\mathbf k_1)\cdots a^\dagger(\mathbf k_n)|0\rangle$，把 $H$ 逐个移过产生算符，每次都带出一份相应的 $\omega_j$；最后 $H$ 作用在真空上为零，所以

$$
H|\mathbf k_1\cdots\mathbf k_n\rangle
=(\omega_1+\cdots+\omega_n)|\mathbf k_1\cdots\mathbf k_n\rangle.
$$

再看洛伦兹变换。在场的展开式中，利用 $(\Lambda q)\cdot x=q\cdot\Lambda^{-1}x$ 和不变测度，有

$$
\varphi(\Lambda^{-1}x)=\int d\widetilde q\,
\left[a(\Lambda^{-1}\mathbf q)e^{iqx}
+a^\dagger(\Lambda^{-1}\mathbf q)e^{-iqx}\right].
$$

这里 $\Lambda^{-1}\mathbf q$ 表示四动量变换后的空间部分。与 $U(\Lambda)^{-1}\varphi(x)U(\Lambda)$ 的正、负频率系数比较，得到

<span id="eq:c03-mode-lorentz"></span>

$$
\begin{aligned}
U(\Lambda)^{-1}a(\mathbf k)U(\Lambda)&=a(\Lambda^{-1}\mathbf k),\\
U(\Lambda)^{-1}a^\dagger(\mathbf k)U(\Lambda)&=a^\dagger(\Lambda^{-1}\mathbf k).
\end{aligned}
$$

真空取为洛伦兹不变态，将 $U$ 逐个移过产生算符，就有

$$
U(\Lambda)|\mathbf k_1\cdots\mathbf k_n\rangle
=|\Lambda\mathbf k_1\cdots\Lambda\mathbf k_n\rangle.
$$

采用不变测度和式[（3.33）](#eq:c03-state-norm)的归一化后，变换粒子态只需变换各个四动量。

最后整理这些对象的量纲，以便随后加入相互作用。在四维自然单位中，$S$无量纲、$[\partial]=1$，动能项因而要求 $[\varphi]=1$，继而给出 $[\Pi]=2$、$[\mathcal L]=[\mathcal H]=[\Omega_0]=4$。不变测度有质量维数2，所以展开中的 $[a]=-1$；普通动量测度的维数为3，式[（3.3）](#eq:c03-fourier-bracket)便给出 $[\widetilde a]=-3/2$，与式[（3.31）](#eq:c03-normalization-conversion)相符。第1节的场 $a(\mathbf x)$只包含湮灭算符，这里的厄米场 $\varphi(x)$同时包含产生和湮灭部分。这两种场的定义和量纲都不同。

<span id="c03-car"></span>

## 采用反对易关系会怎样

本节开头的自由多粒子谱允许两种统计，局域实标量场的正则量子化却给出了玻色子。为了理解差别，考察把对易关系换成反对易关系会发生什么。先从等时场关系着手：若将式[（3.19）](#eq:c03-canonical)中的括号全部替换，对实测试函数涂抹后的厄米场 $\Phi_f$便有 $\{\Phi_f,\Phi_f\}=2\Phi_f^2=0$。在正定内积空间的适当公共域上，这意味着
$\|\Phi_f\psi\|^2=\langle\psi|\Phi_f^2|\psi\rangle=0$，所以场只能为零。两个厄米算符的反对易子本身又是厄米的，也不能等于非零纯虚数 $i\delta$。因此，直接替换等时场括号已经无法构造所需的非平凡实场。

还有另一种尝试：放弃上述场反对易关系，只选一套自身一致的模式CAR，令
$\{a_{\mathbf k},a^\dagger_{\mathbf q}\}=(2\pi)^3 2\omega\delta^3(\mathbf k-\mathbf q)$。这时再代入已经由作用量固定的对称哈密顿量，得到

<span id="eq:c03-car-failure"></span>

$$
H=-\Omega_0V+\frac12\int d\widetilde k\,\omega
\{a^\dagger_{\mathbf k},a_{\mathbf k}\}
=(\mathcal E_0-\Omega_0)V.
\tag{3.34}
$$

哈密顿量只剩常数，因而 $[H,a^\dagger]=0$，不能给出所需的升能关系 $[H,a^\dagger]=\omega a^\dagger$。零点能常数也可吸收入 $\Omega_0$，但这不改变占据数项消失的结论。若另选 $H=\int d\widetilde k\,\omega a^\dagger a$，费米Fock空间仍可具有正能谱，但这已不是从本节局域实标量作用量得到的哈密顿量。下一节将进一步用局域性考察这种选择，从而说明自旋零场与统计的关系。

局域作用量也为相互作用提供了自然的引入办法。例如可以加入 $\varphi^3$ 或 $\varphi^4$：同一点标量的乘积仍是标量，所以这样的相互作用保持作用量的洛伦兹不变性。若将 $-\lambda_n\varphi^n/n!$ 加入 $\mathcal L$，四维耦合的质量维数为 $[\lambda_n]=4-n$。后面的微扰论将给出这些相互作用下的散射振幅；在此之前，先用局域性进一步考察自旋与统计的关系。

---

[← 第 2 节](/posts/srednicki-02/) · [章节地图](/srednicki/) · [第 4 节 →](/posts/srednicki-04/)
