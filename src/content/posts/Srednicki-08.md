---
title: 'Srednicki §8 自由场论的路径积分'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [8]
hideFromHome: true
draft: false
---

<span id="c08"></span>

自由标量场可以分解为一组独立的谐振子，每个动量模式的频率由自由粒子的能量决定。把上一节的高斯积分用于全部模式，就能求出自由场的外源生成泛函；二次核的逆给出费曼传播子，源导数则生成场的时间序关联函数。

<span id="c08-modes"></span>

## 把场看成一组耦合振子

从自由标量场的哈密顿量出发：

<span id="eq:c08-hamiltonian"></span>

$$
H_0=\int d^3x\,\mathcal H_0,\qquad
\mathcal H_0=\frac12\Pi^2+
\frac12(\nabla\varphi)^2+\frac12m^2\varphi^2.
\tag{8.1}
$$

沿用 $c=\hbar=1$ 和 $(-,+,+,+)$ 度规，先取 $m>0$。与谐振子相比，场的坐标还要标明空间中的哪个点：路径中的普通坐标 $q(t)$ 推广为普通实函数 $\varphi(\mathbf x,t)$，位置算符 $Q(t)$ 推广为场算符 $\varphi(\mathbf x,t)$，外源则由 $f(t)$ 推广为 $J(\mathbf x,t)$。因此，路径积分中的 $\varphi$ 表示待积的场位形，而矩阵元中的 $\varphi$ 表示算符；两者的角色由所在表达式区分。

先把这个对应放在有限系统中看清。将空间置于有限周期盒，格距记为 $a$，格点用 $r,s$ 标记。等时场对易关系离散后为

<span id="eq:c08-canonical-lattice"></span>

$$
[\varphi_r,\Pi_s]=\frac{i}{a^3}\delta_{rs}.
\qquad
q_r=a^{3/2}\varphi_r,\quad p_r=a^{3/2}\Pi_r
\quad\Longrightarrow\quad [q_r,p_s]=i\delta_{rs}.
\tag{8.2}
$$

其中 $a^{-3}$ 来自空间delta函数的归一化，因为 $a^3\sum_s\delta_{rs}/a^3=1$。按上式重标度后，每个 $q_r,p_r$ 恰好成为一对普通正则坐标，哈密顿量相应写成

<span id="eq:c08-coupled-oscillators"></span>

$$
H_0=\frac12\sum_r p_r^2+\frac12\sum_{rs}q_rK_{rs}q_s,
\qquad K=m^2I-\nabla_a^2.
\tag{8.3}
$$

势能中的梯度平方耦合相邻格点；在傅里叶模式中，这种耦合转化为不同的振动频率。最近邻差分作用于 $e^{i\mathbf k\cdot\mathbf x_r}$ 时，每个方向给出 $[e^{ik_ja}+e^{-ik_ja}-2]/a^2=-4\sin^2(k_ja/2)/a^2$，于是 $K$ 的本征值为

<span id="eq:c08-lattice-frequencies"></span>

$$
\omega_{\mathbf k,a}^2
=m^2+\frac4{a^2}\sum_{j=1}^{3}\sin^2\frac{k_ja}{2}
\ \longrightarrow\ \mathbf k^2+m^2.
\tag{8.4}
$$

由于 $K$ 实对称且正定，可以用实正交矩阵对角化。对 $q,p$ 同作这个变换，就得到一组彼此独立的谐振子，且Jacobian的绝对值为一。也可以使用复傅里叶模式，但实场的正、负动量分量互为共轭，所代表的仍是同一组实自由度。

与坐标的重标度相配，外源的对应也要包含胞元体积：

<span id="eq:c08-lattice-source"></span>

$$
\int d^3x\,J\varphi
\ \longrightarrow\ \sum_r a^3J_r\varphi_r
=\sum_rF_rq_r,\qquad F_r=a^{3/2}J_r.
\tag{8.5}
$$

在某一时刻指定全部 $q_r$，就是给定一次场位形；让这些坐标随时间演化，便得到场位形空间中的路径。因此，我们可以对每个格点使用第6节的时间切片。若空间有 $N_s$ 个格点，时间分成 $N_t+1$ 段，逐段积掉全部正则动量后，位置测度为

<span id="eq:c08-time-sliced-measure"></span>

$$
\left(\frac1{2\pi i\delta t}\right)^{(N_t+1)N_s/2}
\prod_{j=1}^{N_t}\prod_{r=1}^{N_s}dq_{rj}.
\tag{8.6}
$$

转回场值时，还有 $\prod dq=a^{3N_tN_s/2}\prod d\varphi$。这些常数都与外源无关，连同真空端点因子一起由零源归一化确定，因而可简记为 $\mathcal D\varphi\propto\prod_x d\varphi(x)$。这一符号所代表的，是有限盒、空间格点和时间切片的相应极限。

<span id="c08-functional"></span>

## 真空泛函与质量的无穷小虚部

与谐振子一样，场论积分也要保留选择真空的收敛处方。令 $\alpha=1-i\epsilon_0$，把整个 $H_0$ 乘以 $\alpha$，再对每个空间模式完成动量平方，所得受调节拉格朗日密度为

<span id="eq:c08-hamiltonian-regulator"></span>

$$
\mathcal L_{\epsilon_0}+J\varphi
=\frac1{2\alpha}\dot\varphi^2
-\frac{\alpha}{2}\big[(\nabla\varphi)^2+m^2\varphi^2\big]
+J\varphi.
\tag{8.7}
$$

对于固定的 $\mathbf k$，这一计算就是上一节的谐振子，只须代入 $\omega=\omega_{\mathbf k}=\sqrt{\mathbf k^2+m^2}$。频率作用量中的二次核为 $(k^0)^2/\alpha-\alpha\omega_{\mathbf k}^2$，其零点在 $k^0=\pm\alpha\omega_{\mathbf k}$，所以正能极点仍在实轴下方，负能极点在上方。

同一边界处方还可以用质量平方的微小负虚部表示。为与无量纲的 $\epsilon_0$区分，令 $m^2\to m^2-i\eta$，其中 $\eta>0$，并定义

<span id="eq:c08-kernel-convention"></span>

$$
D_\eta=-\partial^2+m^2-i\eta,\qquad
D_\eta(k)=k^2+m^2-i\eta,
\qquad k^2=-(k^0)^2+\mathbf k^2.
\tag{8.8}
$$

这项质量虚部是对实轴边界值的简洁表示。精确二次核的相反数为 $\alpha\omega_{\mathbf k}^2-(k^0)^2/\alpha$，一阶虚部为 $-i\epsilon_0[(k^0)^2+\omega_{\mathbf k}^2]$；两个质量壳点上的正权重均等于 $2\omega_{\mathbf k}^2$，因此它与 $D_\eta(k)$ 指定相同的极点方向。两种调节量的量纲不同：$\eta$ 为质量平方，$\epsilon_0$ 则无量纲。

采用这一记法，自由场泛函可写为

<span id="eq:c08-source-functional"></span>

$$
\begin{aligned}
Z_0[J]&=\mathcal N_\eta\int\mathcal D\varphi\,
e^{iS_0[\varphi,J]},\qquad Z_0[0]=1,\\
S_0[\varphi,J]&=\int d^4x\left[
-\frac12\partial^\mu\varphi\,\partial_\mu\varphi
-\frac12(m^2-i\eta)\varphi^2+J\varphi\right].
\end{aligned}
\tag{8.9}
$$

常数 $\mathcal N_\eta$ 包含除以无源振幅的归一化，第3节对零点能的平移也可在此统一处理。在有限实模式下，作用量中的 $+i\eta\varphi^2/2$ 使积分含有 $e^{-\eta\int d^4x\,\varphi^2/2}$，所以接下来的高斯运算具有所需的衰减。

<span id="c08-fourier"></span>

## 四维 傅里叶 变换与完成平方

与上一节对时间的变换相仿，现在对全部时空坐标作傅里叶变换，使自由二次作用量在四动量中对角化。定义四维傅里叶变换为

<span id="eq:c08-fourier"></span>

$$
\widetilde\varphi(k)=\int d^4x\,e^{-ikx}\varphi(x),
\qquad
\varphi(x)=\int\frac{d^4k}{(2\pi)^4}e^{ikx}\widetilde\varphi(k),
\qquad kx=-k^0t+\mathbf k\cdot\mathbf x.
\tag{8.10}
$$

源 $J$ 也采用同一变换。这里的 $k^0$ 与空间动量一样，是独立积分变量，还没有取成在壳能量 $\omega_{\mathbf k}$。每个场导数由 $\partial_\mu e^{ikx}=ik_\mu e^{ikx}$ 转换成动量因子，而时空积分给出

<span id="eq:c08-fourier-delta"></span>

$$
\int d^4x\,e^{i(k+k')x}=(2\pi)^4\delta^4(k+k').
\tag{8.11}
$$

先看动能项的符号。将两份场的傅里叶积分代入，两个 $i$ 与拉氏量前的负号相乘，得到 $\frac12 k^\mu k'_\mu$；随后delta函数令 $k'=-k$，于是该系数变成 $-\frac12 k^2$。再加上质量项，将源项对称写开，得到

<span id="eq:c08-frequency-action"></span>

$$
\begin{aligned}
S_0=\frac12\int\frac{d^4k}{(2\pi)^4}
\big[&
-\widetilde\varphi(k)D_\eta(k)\widetilde\varphi(-k)\\
&+\widetilde J(k)\widetilde\varphi(-k)
+\widetilde J(-k)\widetilde\varphi(k)\big].
\end{aligned}
\tag{8.12}
$$

两份源项经 $k\leftrightarrow-k$ 换元后相等，外面的 $1/2$ 因而正好恢复原系数。也可以先在坐标空间分部积分；当边界项已按所选端点处方处理后，作用量为 $S_0=-\frac12\int\varphi D_\eta\varphi+\int J\varphi$，与上面的频域二次型一致。

第7节的二次核 $A=E^2-\omega^2+i0$在这里对应 $-D$。相应的完成平方采用平移

<span id="eq:c08-shift"></span>

$$
\widetilde\chi(k)=\widetilde\varphi(k)
-\frac{\widetilde J(k)}{D_\eta(k)}.
\tag{8.13}
$$

将 $\widetilde\varphi=\widetilde\chi+D_\eta^{-1}\widetilde J$ 代回式[（8.12）](#eq:c08-frequency-action)，负二次项产生的两份负交叉项被显式源项分别消去；剩余源平方项的系数为 $-1+1+1=1$。作用量因而成为

<span id="eq:c08-completed-action"></span>

$$
S_0=\frac12\int\frac{d^4k}{(2\pi)^4}
\left[
\frac{\widetilde J(k)\widetilde J(-k)}{D_\eta(k)}
-\widetilde\chi(k)D_\eta(k)\widetilde\chi(-k)
\right].
\tag{8.14}
$$

原来的场变量已经与外源分开。要在积分中使用这个复平移，可直接沿用式[（7.15）](/posts/srednicki-07/#eq:c07-gaussian-ratio)的恒等式，并把本题的核和测度代入。若四维离散胞元体积为 $v_4$，相应矩阵取 $A=-v_4D_\eta$，源列向量取 $v_4J$。矩阵的虚部为正定的 $v_4\eta I$，因此

<span id="eq:c08-finite-gaussian"></span>

$$
\frac{I(v_4J)}{I(0)}
=\exp\!\left[
-\frac i2(v_4J)^T(-v_4D_\eta)^{-1}(v_4J)\right]
=\exp\!\left[\frac i2v_4J^TD_\eta^{-1}J\right].
\tag{8.15}
$$

从矩阵逆转为连续积分核时，还要计入求和的体积因子：离散核是 $(\Delta_\eta)_{rs}=(D_\eta^{-1})_{rs}/v_4$，所以上式右边等于 $\exp[(i/2)v_4^2\sum_{rs}J_r(\Delta_\eta)_{rs}J_s]$，恰具有两个时空积分的形式。无源高斯因子、傅里叶变换的常数Jacobian和动量积分常数，则全在有源、无源的比值中相消。

将外源因子提出后，取相同的连续极限与真空边界极限，得到自由生成泛函：

<span id="eq:c08-gaussian-functional"></span>

$$
\begin{aligned}
Z_0[J]
&=\exp\!\left[
\frac i2\int\frac{d^4k}{(2\pi)^4}
\frac{\widetilde J(k)\widetilde J(-k)}{k^2+m^2-i0}\right]\\
&=\exp\!\left[
\frac i2\int d^4x\,d^4y\,
J(x)\Delta(x-y)J(y)\right],
\end{aligned}
\tag{8.16}
$$

这里定义Feynman传播子（Feynman propagator）：

<span id="eq:c08-propagator-definition"></span>

$$
\Delta(z)=\lim_{\eta\downarrow0}\Delta_\eta(z),
\qquad
\Delta_\eta(z)=\int\frac{d^4k}{(2\pi)^4}
\frac{e^{ikz}}{k^2+m^2-i\eta}.
\tag{8.17}
$$

将双源指数从动量表示改写为坐标表示时，两份源的傅里叶相位最初给出 $e^{-ik(x-y)}$；分母为偶函数，作 $k\to-k$ 后便成为传播子定义中的相位。这个结果的量纲也与源作用量相符：$[\varphi]=1$、$[J]=3$、$[\Delta]=2$，所以双源指数的总质量维数为 $3+3+2-8=0$。

<span id="c08-propagator"></span>

## 作完能量积分

为了看出传播子怎样联系两个时空点，令 $z=x-y=(\tau,\mathbf r)$，先在式[（8.17）](#eq:c08-propagator-definition)中固定三动量并作 $k^0$ 积分。它就是第7节的振子积分，替换为 $E=k^0$、$\omega=\omega_{\mathbf k}$ 即可。具体取 $\Omega_{\mathbf k}=\sqrt{\omega_{\mathbf k}^2-i\eta}$，正实部、负虚部的根位于下半平面。当 $\tau>0$ 时，顺时针围道包围这一根，给出 $-i[-e^{-i\Omega_{\mathbf k}\tau}/(2\Omega_{\mathbf k})]$；当 $\tau<0$ 时，在上半平面取负根，给出 $i e^{i\Omega_{\mathbf k}\tau}/(2\Omega_{\mathbf k})$。再撤去 $\eta$，得到

<span id="eq:c08-energy-integral"></span>

$$
\int\frac{dk^0}{2\pi}
\frac{e^{-ik^0\tau}}{-(k^0)^2+\omega_{\mathbf k}^2-i0}
=\frac{i}{2\omega_{\mathbf k}}e^{-i\omega_{\mathbf k}|\tau|}.
\tag{8.18}
$$

圆弧积分与式[（7.20）](/posts/srednicki-07/#eq:c07-contour-positive)、[（7.21）](/posts/srednicki-07/#eq:c07-contour-negative)一样消失：所选半平面中的指数不增长，二次分母又提供 $R^{-2}$ 的衰减。将结果代回剩余的三动量积分，得到

<span id="eq:c08-spatial-propagator"></span>

$$
\Delta(z)
=i\int\frac{d^3k}{(2\pi)^3\,2\omega_{\mathbf k}}\,
e^{i\mathbf k\cdot\mathbf r-i\omega_{\mathbf k}|\tau|}.
\tag{8.19}
$$

因此，在壳测度 $d\widetilde k$ 是作完能量积分之后才出现的；分母中的 $2\omega_{\mathbf k}$ 正是简单极点留数所包含的导数因子。

为了把两支的时间次序显式写出，对负时间支将空间积分变量换成 $-\mathbf k$，而 $\omega_{\mathbf k}$ 保持不变。这样就能用两份在壳积分写出传播子：

<span id="eq:c08-time-ordered-propagator"></span>

$$
\Delta(z)
=i\theta(\tau)\int d\widetilde k\,e^{ikz}
+i\theta(-\tau)\int d\widetilde k\,e^{-ikz},
\qquad k^0=\omega_{\mathbf k}.
\tag{8.20}
$$

第一支将正频率模式从较早的 $y^0$联系到较晚的 $x^0$，第二支交换两点的次序。它们共同组成真空时间序条件所选定的传播子。

外源作用后的响应由推迟Green函数描述。将两个能量极点都移到下半平面，定义

<span id="eq:c08-retarded"></span>

$$
\Delta_{\rm ret}(\tau,\mathbf r)
=\lim_{\epsilon\downarrow0}\int\frac{d^3k\,dE}{(2\pi)^4}
\frac{e^{i\mathbf k\cdot\mathbf r-iE\tau}}
{\omega_{\mathbf k}^2-(E+i\epsilon)^2}.
$$

当 $\tau<0$时在上半平面闭合，内部没有极点，所以积分为零。当 $\tau>0$时，顺时针围道同时包围 $E=\omega_{\mathbf k}-i\epsilon$和 $E=-\omega_{\mathbf k}-i\epsilon$，两份留数相加给出

$$
\begin{aligned}
-i\left[-\frac{e^{-i\omega_{\mathbf k}\tau}}{2\omega_{\mathbf k}}
+\frac{e^{i\omega_{\mathbf k}\tau}}{2\omega_{\mathbf k}}\right]
&=\frac{\sin(\omega_{\mathbf k}\tau)}{\omega_{\mathbf k}},\\
\Delta_{\rm ret}(\tau,\mathbf r)
&=\theta(\tau)\int\frac{d^3k}{(2\pi)^3}
 e^{i\mathbf k\cdot\mathbf r}
 \frac{\sin(\omega_{\mathbf k}\tau)}{\omega_{\mathbf k}}.
\end{aligned}
$$

它在零时刻连续，时间导数从零跳到 $\delta^3(\mathbf r)$，故同样满足 $D\Delta_{\rm ret}=\delta^4$。通过卷积 $\varphi_J(x)=\int d^4y\,\Delta_{\rm ret}(x-y)J(y)$，可得到外源作用前为零的受迫解。超前Green函数则把两个极点都移到上半平面，即采用 $\omega_{\mathbf k}^2-(E-i0)^2$，得到

$$
\Delta_{\rm adv}(\tau,\mathbf r)
=-\theta(-\tau)\int\frac{d^3k}{(2\pi)^3}
 e^{i\mathbf k\cdot\mathbf r}\frac{\sin(\omega_{\mathbf k}\tau)}{\omega_{\mathbf k}}.
$$

<span id="c08-contact"></span>

## Green 方程中的接触项

传播子是自由二次核的逆，因此应满足相应的Green方程。先利用 $\partial^2e^{ikz}=-k^2e^{ikz}$，在有限 $\eta$ 下直接作用波算符：

<span id="eq:c08-inverse-kernel"></span>

$$
D_\eta\Delta_\eta(z)
=\int\frac{d^4k}{(2\pi)^4}e^{ikz}
=\delta^4(z).
\tag{8.21}
$$

分母被波算符抵消后只剩傅里叶表示的delta函数，取边界极限便有

<span id="eq:c08-green-equation"></span>

$$
(-\partial^2+m^2)\Delta(z)=\delta^4(z).
\tag{8.22}
$$

也可从式[（8.19）](#eq:c08-spatial-propagator)的时间表示求出同一个delta源。两支在 $\tau=0$连续，一阶时间导数之差为

<span id="eq:c08-time-jump"></span>

$$
\begin{aligned}
\partial_\tau\Delta(0^+,\mathbf r)
-\partial_\tau\Delta(0^-,\mathbf r)
&=2\int d\widetilde k\,\omega_{\mathbf k}
e^{i\mathbf k\cdot\mathbf r}\\
&=\int\frac{d^3k}{(2\pi)^3}
e^{i\mathbf k\cdot\mathbf r}
=\delta^3(\mathbf r).
\end{aligned}
\tag{8.23}
$$

这些等时关系按空间分布理解。离开 $\tau=0$，每个模式满足 $(\partial_\tau^2+\omega_{\mathbf k}^2)e^{-i\omega_{\mathbf k}|\tau|}=0$；原点处的一阶导数跳跃则使二阶导数产生 $\delta(\tau)\delta^3(\mathbf r)$，这就给出完整的四维源。

也可以直接对式[（8.20）](#eq:c08-time-ordered-propagator)中的阶跃函数求导，但须将所产生的 $\delta$ 和 $\delta'$ 一起保留。设两条平滑支的差为 $F(\tau)$，连续性给出 $F(0)=0$。从测试函数上的乘积法则可得

<span id="eq:c08-delta-prime-product"></span>

$$
F(\tau)\delta'(\tau)
=F(0)\delta'(\tau)-F'(0)\delta(\tau).
\tag{8.24}
$$

所以二阶导数中暂时出现的 $2F'\delta+F\delta'$ 最后只留下 $F'(0)\delta$，与跳跃计算相同。

<span id="c08-bessel"></span>

## 剩余空间积分的 Bessel 表示

剩余空间积分可用Bessel函数表示。第4节已求出等时类空核，现在只需把时间依赖接到同一积分中。为控制收敛，先取正实欧几里得时间 $s>0$，定义

<span id="eq:c08-euclidean-time"></span>

$$
C_E(s,\mathbf r)=
\int d\widetilde k\,e^{i\mathbf k\cdot\mathbf r-\omega_{\mathbf k}s}.
\tag{8.25}
$$

因 $s$ 为正，空间动量积分绝对收敛。引入辅助积分变量 $k_4$，在上半平面取极点 $k_4=i\omega_{\mathbf k}$，便有 $\int dk_4\,e^{ik_4s}/[2\pi(k_4^2+\omega_{\mathbf k}^2)]
=e^{-\omega_{\mathbf k}s}/(2\omega_{\mathbf k})$。因此 $C_E$ 可以写为四维欧几里得逆核。再使用 $1/(k_E^2+m^2)=\int_0^\infty du\,e^{-u(k_E^2+m^2)}$，四个动量积分都化成高斯积分：

<span id="eq:c08-four-dimensional-heat"></span>

$$
\begin{aligned}
C_E(s,\mathbf r)
&=\int\frac{d^4k_E}{(2\pi)^4}
\frac{e^{ik_EX}}{k_E^2+m^2}\\
&=\frac1{16\pi^2}\int_0^\infty\frac{du}{u^2}
\exp\!\left[-m^2u-\frac{R^2}{4u}\right],
\qquad R=\sqrt{r^2+s^2}>0 .
\end{aligned}
\tag{8.26}
$$

每个方向给出 $(4\pi u)^{-1/2}e^{-X_j^2/(4u)}$，四者相乘便得到上式的系数和径向指数。交换积分时，可先将辅助参数限制在 $u\in[\varepsilon,M]$；完成四维高斯积分后，$u\downarrow0$ 端由 $e^{-R^2/(4u)}$ 控制，$u\to\infty$ 端则由质量指数控制。

此时剩余的正是式[（4.14）](/posts/srednicki-04/#eq:c04-heat-kernel)，只须把 $r$ 换为 $R$。令 $v=R^2/(4u)$，Jacobian为 $du/u^2=-4\,dv/R^2$；再代入式[（4.16）](/posts/srednicki-04/#eq:c04-bessel-evaluation)已求出的 $\int_0^\infty dv\,e^{-v-(mR)^2/(4v)}=mR K_1(mR)$，即得

<span id="eq:c08-euclidean-bessel"></span>

$$
C_E(s,\mathbf r)=\frac{m}{4\pi^2R}K_1(mR).
\tag{8.27}
$$

接下来将欧几里得时间延拓回实时间。在复 $s$ 的右半平面，式[（8.25）](#eq:c08-euclidean-time)因 $e^{-\omega_{\mathbf k}\operatorname{Re}s}$ 衰减而收敛，并定义解析函数；右边Bessel表达式取连续的同一平方根，也在这个区域解析。两边在正实轴的各阶导数相同，局部幂级数便相同，再用相接的收敛圆把等式延拓到整个右半平面。于是可从正实 $s$ 连续到达 $s=\delta+i|\tau|$，其中 $\delta>0$，最后取边界值。由式[（8.19）](#eq:c08-spatial-propagator)得到

<span id="eq:c08-lorentz-bessel"></span>

$$
\Delta(z)=
\frac{im}{4\pi^2\sqrt{z^2+i0}}\,
K_1\!\left(m\sqrt{z^2+i0}\right),
\qquad z^2=r^2-\tau^2 .
\tag{8.28}
$$

这个延拓同时指定平方根的分支：类空区域取正实根，类时区域从负实轴上方趋近，光锥上则按相应的分布边界值理解。

在 $z^2>0$ 时，上式直接成为第4节类空核乘以 $i$。若再取 $m\to0$，式[（4.15）](/posts/srednicki-04/#eq:c04-v-integral)中的积分趋于一，传播子简化为

<span id="eq:c08-massless-propagator"></span>

$$
\Delta_{m=0}(z)=\frac{i}{4\pi^2(z^2+i0)}.
\tag{8.29}
$$

传播子在光锥上具有奇异性；相互作用展开中的同点传播子 $\Delta(0)$将在调节后计算。

<span id="c08-correlators"></span>

## 场关联函数与 Wick 配对

自由生成泛函一经求出，关联函数仍按第7节的方法产生。将每次位置源微分推广为四维源微分，得到

<span id="eq:c08-source-insertions"></span>

$$
\langle0|T\varphi(x_1)\cdots\varphi(x_n)|0\rangle
=\left.
\prod_{a=1}^{n}\frac1i\frac{\delta}{\delta J(x_a)}
Z_0[J]\right|_{J=0}.
\tag{8.30}
$$

泛函导数的归一化也与先前的胞元体积相配。沿式[（8.5）](#eq:c08-lattice-source)，四维源作用量写成 $\sum_rv_4J_r\varphi_r$，普通导数 $\partial/\partial J_r$ 带下 $iv_4\varphi_r$。因此连续导数应对应 $v_4^{-1}\partial/\partial J_r$，而 $\delta^4(x_r-x_s)$ 对应 $\delta_{rs}/v_4$，这样每次微分才恰好产生一个场插入。

记 $F_x[J]=\int d^4y\,\Delta(x-y)J(y)$、$\mathscr D_x=i^{-1}\delta/\delta J(x)$。由于 $\Delta(z)=\Delta(-z)$，对源二次型中两份源微分得到的项相同；按第7节的链式法则，前两次导数为

<span id="eq:c08-two-derivatives"></span>

$$
\mathscr D_xZ_0=F_xZ_0,\qquad
\mathscr D_y\mathscr D_xZ_0
=\left[\frac{\Delta(x-y)}i+F_xF_y\right]Z_0 .
\tag{8.31}
$$

第一项已不含源，第二项则仍带两份源；因而在 $J=0$ 处只留下

<span id="eq:c08-field-two-point"></span>

$$
C(x,y)\equiv\langle0|T\varphi(x)\varphi(y)|0\rangle
=\frac{\Delta(x-y)}i,\qquad \Delta=iC .
\tag{8.32}
$$

传播子与时间序矩阵元由此相差一个 $i$，以后书写图规则时也要沿用这个定义。于是 $D\Delta=\delta^4$ 等价于 $DC=-i\delta^4$，与第5节由时间序导数求出的接触项关系一致。

模式展开也给出同一结果。由第3节的场展开和式[（3.20）](/posts/srednicki-03/#eq:c03-mode-ccr)，有 $\varphi(x)=\int d\widetilde k\,[ae^{ikx}+a^\dagger e^{-ikx}]$，利用真空湮灭条件，只保留湮灭算符在左、产生算符在右的一项：

<span id="eq:c08-operator-two-point"></span>

$$
\begin{aligned}
\langle0|\varphi(x)\varphi(y)|0\rangle
&=\int d\widetilde k\,d\widetilde p\,
e^{ikx-ipy}
(2\pi)^3\,2\omega_{\mathbf k}\delta^3(\mathbf k-\mathbf p)\\
&=\int d\widetilde k\,e^{ik(x-y)}.
\end{aligned}
\tag{8.33}
$$

对易子系数抵消 $\mathbf p$ 测度中的 $(2\pi)^3 2\omega_{\mathbf p}$，因而只剩一份在壳积分。对于 $x^0>y^0$，使用上式；时间次序相反时，交换 $x,y$，二者合起来恰好等于式[（8.20）](#eq:c08-time-ordered-propagator)除以 $i$。

高阶关联的组合计数也可以直接沿用第7节。现在插入标号由时间改成时空点，每个配对的核由 $G$ 换成 $\Delta$，源导数的分配方式不变。四个插入仍只有三种不同配对，所以四点函数为

<span id="eq:c08-four-point"></span>

$$
\begin{aligned}
\langle0|T\varphi_1\varphi_2\varphi_3\varphi_4|0\rangle
=\frac1{i^2}\big[
&\Delta_{12}\Delta_{34}
+\Delta_{13}\Delta_{24}
+\Delta_{14}\Delta_{23}\big],\\
&\varphi_a=\varphi(x_a),\qquad
\Delta_{ab}=\Delta(x_a-x_b).
\end{aligned}
\tag{8.34}
$$

对于一般 $2n$ 点函数，零源处只有源指数展开的第 $n$ 项有贡献。同一个无序配对出现 $2^n n!$ 次，抵消该项的 $2^n n!$ 分母；每次导数还带 $1/i$，最终留下 $i^{-n}$。由此得到一般偶数点函数：

<span id="eq:c08-wick"></span>

$$
\langle0|T\varphi(x_1)\cdots\varphi(x_{2n})|0\rangle
=\frac1{i^n}\sum_{\mathcal P}
\prod_{(a,b)\in\mathcal P}\Delta(x_a-x_b).
\tag{8.35}
$$

奇数点函数为零，而上式不重复的配对数为 $(2n-1)!!$。这就是本节所用的Wick定理（Wick's theorem）：自由真空中的时间序关联，全部归结为二点函数的配对。同点乘积先在共同调节下计算，具体的重整化将在相互作用理论中展开。

## 复标量场的外源与配对

把两个独立、质量相同的实场组合为 $\phi=(\varphi_1+i\varphi_2)/\sqrt2$，自由拉格朗日密度及源项为

<span id="eq:c08-complex-source"></span>

$$
\mathcal L_0+\mathcal L_J
=-\partial^\mu\phi^\dagger\partial_\mu\phi-m^2\phi^\dagger\phi
+J^\dagger\phi+\phi^\dagger J.
$$

令 $J=(J_1+iJ_2)/\sqrt2$，源项恰好化为 $J_1\varphi_1+J_2\varphi_2$。两个实场独立，生成泛函相乘，得到

<span id="eq:c08-complex-functional"></span>

$$
\begin{aligned}
Z_0[J^\dagger,J]
&=\exp\!\left[\frac i2\int d^4x\,d^4y\,
 \bigl(J_1(x)\Delta(x-y)J_1(y)+J_2(x)\Delta(x-y)J_2(y)\bigr)\right]\\
&=\exp\!\left[i\int d^4x\,d^4y\,
 J^\dagger(x)\Delta(x-y)J(y)\right].
\end{aligned}
$$

第二行利用 $\Delta(x-y)=\Delta(y-x)$消去了两份虚交叉项。将 $J,J^\dagger$视作独立变量求导，$i^{-1}\delta/\delta J^\dagger$插入 $\phi$，$i^{-1}\delta/\delta J$插入 $\phi^\dagger$。指数中的每一项各含一份 $J$和 $J^\dagger$，故

$$
\langle0|T\phi(x)\phi^\dagger(y)|0\rangle=\frac{\Delta(x-y)}i,
\qquad
\langle T\phi(x)\phi(y)\rangle
=\langle T\phi^\dagger(x)\phi^\dagger(y)\rangle=0.
$$

一般关联函数在两种场的数目相等时才能非零。含 $n$个 $\phi$和 $n$个 $\phi^\dagger$时，每个场只能与一份共轭场配对，配对数为 $n!$，于是

<span id="eq:c08-complex-wick"></span>

$$
\langle0|T\phi(x_1)\cdots\phi(x_n)
\phi^\dagger(y_1)\cdots\phi^\dagger(y_n)|0\rangle
=\frac1{i^n}\sum_{\sigma\in S_n}
\prod_{a=1}^n\Delta(x_a-y_{\sigma(a)}).
$$

这里 $S_n$表示 $n$个标号的全部排列。例如两场两共轭场有两种配对，得到 $i^{-2}[\Delta(x_1-y_1)\Delta(x_2-y_2)+\Delta(x_1-y_2)\Delta(x_2-y_1)]$。

[下一节](/posts/srednicki-09/)将相互作用写成作用于 $Z_0[J]$的微分算符。Wick配对使微扰展开的每一项化为传播子的乘积。

---

[← 第 7 节](/posts/srednicki-07/) · [章节地图](/srednicki/) · [第 9 节 →](/posts/srednicki-09/)
