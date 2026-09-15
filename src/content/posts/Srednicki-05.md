---
title: 'Srednicki §5 LSZ 约化公式'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [5]
hideFromHome: true
draft: false
---

<span id="c05"></span>

散射实验在遥远过去准备彼此分离的入射粒子，在遥远未来测量出射粒子。LSZ（Lehmann–Symanzik–Zimmermann）约化公式把这些粒子态之间的散射振幅写成场的时间序关联函数：每约化一个外部粒子，就引入一次场插入和一个克莱因–戈登算符。下面从自由粒子的波包出发推导这一关系。

<span id="c05-packets"></span>

## 单粒子归一化与波包测度

先从自由理论中已经明确的单粒子态出发。沿用第3节的归一化，暂取 $\varphi$为自由实场，令
$|\mathbf k\rangle=a^\dagger(\mathbf k)|0\rangle$、
$a(\mathbf k)|0\rangle=0$、$\langle0|0\rangle=1$，于是

<span id="eq:c05-one-particle"></span>

$$
\begin{aligned}
a^\dagger(\mathbf k)
&=-i\int d^3x\,e^{ikx}\overleftrightarrow{\partial_0}\varphi(x),\\
\langle\mathbf k|\mathbf q\rangle
&=\langle0|[a(\mathbf k),a^\dagger(\mathbf q)]|0\rangle\\
&=(2\pi)^3 2\omega_{\mathbf k}\delta^3(\mathbf k-\mathbf q).
\end{aligned}
\tag{5.1}
$$

第一式由式[（3.17）](/posts/srednicki-03/#eq:c03-inverse)取共轭得到：因 $\partial_0e^{ikx}=-i\omega e^{ikx}$，右端等于 $\int e^{ikx}(\omega\varphi-i\Pi)$。求第二式时，将 $a^\dagger a$移到真空右侧就得到零，留下的模式CCR便决定单粒子态的归一化。

精确动量态遍布全空间。要描述局域于有限区域的粒子，用普通测度 $d^3k$把这些态叠加成波包：

<span id="eq:c05-packet-operators"></span>

$$
A^\dagger[f]\equiv\int d^3k\,f(\mathbf k)a^\dagger(\mathbf k),
\qquad
A[f]\equiv A^\dagger[f]^\dagger
=\int d^3k\,f(\mathbf k)^*a(\mathbf k).
\tag{5.2}
$$

这与第3节使用不变测度的写法有不同的权函数。把那里的振幅另记为 $F$，两种积分表示同一态时应有
$F(\mathbf k)=(2\pi)^3 2\omega_{\mathbf k}f(\mathbf k)$。因此，波包的归一化也须按本节的测度重新读出。将式[（5.1）](#eq:c05-one-particle)代入两包的内积，得

<span id="eq:c05-packet-inner"></span>

$$
\langle h,f\rangle_{\rm pkt}
\equiv[A[h],A^\dagger[f]]
=\int d^3k\,(2\pi)^3 2\omega_{\mathbf k}\,
h(\mathbf k)^*f(\mathbf k).
\tag{5.3}
$$

例如选择高斯包
$f(\mathbf k)=N\exp[-(\mathbf k-\mathbf k_1)^2/(4\sigma^2)]$。在窄包条件 $\sigma/\omega_1\ll1$下，能量可在 $\mathbf k_1$附近展开；线性项对中心对称的高斯积分为零，故

<span id="eq:c05-gaussian-norm"></span>

$$
|N|^{-2}=(2\pi)^3\,2\omega_1(2\pi\sigma^2)^{3/2}
\left[1+O\left(\frac{\sigma^2}{\omega_1^2}\right)\right].
\tag{5.4}
$$

其中的常数来自 $\int d^3q\,e^{-\mathbf q^2/(2\sigma^2)}=(2\pi\sigma^2)^{3/2}$，且 $\omega_1=\sqrt{\mathbf k_1^2+m^2}$。宽度不小时，应直接用式[（5.3）](#eq:c05-packet-inner)的加权积分确定精确的 $N$，保留能量在包内的变化。

动量宽度怎样反映为空间尺度，可以由场与波包态的矩阵元直接看出：

<span id="eq:c05-packet-envelope"></span>

$$
\begin{aligned}
u_f(\mathbf x,t)
&\equiv\langle0|\varphi(\mathbf x,t)A^\dagger[f]|0\rangle
=\int d^3k\,f(\mathbf k)e^{i\mathbf k\cdot\mathbf x-i\omega_{\mathbf k}t},\\
u_f(\mathbf x,0)
&=N(2\sqrt\pi\,\sigma)^3
e^{-\sigma^2\mathbf x^2+i\mathbf k_1\cdot\mathbf x}.
\end{aligned}
\tag{5.5}
$$

第一行只需一次模式收缩。第二行令 $\mathbf q=\mathbf k-\mathbf k_1$，将三维积分拆成三个一维高斯积分。每一维配方后都有

$$
\begin{aligned}
-\frac{q^2}{4\sigma^2}+iqx
&=-\frac{(q-2i\sigma^2x)^2}{4\sigma^2}-\sigma^2x^2,\\
\int_{-\infty}^{\infty}dq\,e^{-q^2/(4\sigma^2)+iqx}
&=2\sqrt\pi\,\sigma e^{-\sigma^2x^2}.
\end{aligned}
$$

被积函数是整函数，平移积分路径时两端的高斯衰减使竖直边的积分消失。三个方向的结果相乘，再乘回 $Ne^{i\mathbf k_1\cdot\mathbf x}$，便得到式[（5.5）](#eq:c05-packet-envelope)。动量分布越窄，空间包络便越宽，其尺度约为 $\sigma^{-1}$。

散射初态通常不止一个粒子，所以还须处理全同粒子的交换。用CCR把两个湮灭算符依次移过两个产生算符，得到

<span id="eq:c05-two-packet-norm"></span>

$$
\begin{aligned}
\|A^\dagger[f_1]A^\dagger[f_2]|0\rangle\|^2
={}&\langle f_1,f_1\rangle_{\rm pkt}
\langle f_2,f_2\rangle_{\rm pkt}\\
&+|\langle f_1,f_2\rangle_{\rm pkt}|^2.
\end{aligned}
\tag{5.6}
$$

两项分别来自原次序配对和交换配对。若两个单包分别归一且彼此正交，总态范数就是一；若它们有重叠，归一化两粒子态时还须除以 $\sqrt{1+|\langle f_1,f_2\rangle_{\rm pkt}|^2}$。

<span id="c05-asymptotic"></span>

## 波包运动与渐近态

为了构造入射和出射态，还要看这些包怎样运动。自由波包的驻相点满足
$\mathbf x/t=\nabla_{\mathbf k}\omega_{\mathbf k}
=\mathbf k/\omega_{\mathbf k}$。对窄包作一阶色散展开，包络中心沿
$\mathbf x=\mathbf v_1t$运动，其中 $\mathbf v_1=\mathbf k_1/\omega_1$；二阶项
$\partial_i\partial_j\omega=(\delta_{ij}-v_iv_j)/\omega$
则引起展宽，沿运动方向与横向的曲率分别为 $m^2/\omega_1^3$和 $1/\omega_1$。这种二阶展开要求被略去的相位
$|t|\,O(\sigma^3\sup|\partial^3\omega|)$足够小，因此研究无穷时间的分离时，应直接估计完整相位积分。

取光滑、紧动量支撑且**速度支撑不相交**的两个包。令 $\mathbf x=t\mathbf v$，相位为
$t\Phi_{\mathbf v}(\mathbf k)$，其中
$\Phi_{\mathbf v}=\mathbf k\cdot\mathbf v-\omega_{\mathbf k}$。当 $\mathbf v$与包的速度支撑有正距离时，支撑上的
$|\nabla\Phi_{\mathbf v}|$有正下界，也就没有驻相点。利用这一点，定义

<span id="eq:c05-nonstationary"></span>

$$
\mathcal D_{\mathbf v,t}
=\frac{\nabla_{\mathbf k}\Phi_{\mathbf v}}
{it|\nabla_{\mathbf k}\Phi_{\mathbf v}|^2}
\cdot\nabla_{\mathbf k},
\qquad
\mathcal D_{\mathbf v,t}e^{it\Phi_{\mathbf v}}
=e^{it\Phi_{\mathbf v}}.
\tag{5.7}
$$

在动量积分中，把左侧的微分算符分部积分到光滑紧支撑的 $f$上，边界项为零。相应的形式转置为

$$
\mathcal D_{\mathbf v,t}^{\,T}f
=-\frac1{it}\boldsymbol\nabla_{\mathbf k}\cdot
\left(\frac{f\,\boldsymbol\nabla_{\mathbf k}\Phi_{\mathbf v}}
{|\boldsymbol\nabla_{\mathbf k}\Phi_{\mathbf v}|^2}\right);
$$

散度同时作用于 $f$和相位系数，每作一次分部积分就取出一个 $1/t$。在满足共同下界 $|\boldsymbol\nabla\Phi_{\mathbf v}|\geq\delta>0$的速度区域中，其余系数及其导数有界；重复 $N$次便得到一致的 $O(|t|^{-N})$估计。因此，两个不交的速度支撑对应渐近分离的空间区域。对 $m>0$，映射 $\mathbf k\mapsto\mathbf k/\omega_{\mathbf k}$为单射，分离的紧动量支撑也给出分离的速度支撑。

在相互作用理论中，取唯一不变真空和稳定、孤立的质量 $m>0$单粒子壳，并选择与该粒子有非零重叠的场。把式[（5.1）](#eq:c05-one-particle)中的自由场换成这个相互作用场，所得投影记为 $A^\dagger[f;t]$。它随时间改变，入、出粒子则由其遥远过去和未来的渐近投影 $A^\dagger_{\rm in/out}[f]$产生：

<span id="eq:c05-asymptotic-ansatz"></span>

$$
\begin{aligned}
|f_1,f_2;{\rm in}\rangle
&=A^\dagger_{\rm in}[f_1]A^\dagger_{\rm in}[f_2]|0\rangle,\\
|h_1,h_2;{\rm out}\rangle
&=A^\dagger_{\rm out}[h_1]A^\dagger_{\rm out}[h_2]|0\rangle.
\end{aligned}
\tag{5.8}
$$

约化计算在矩阵元中依次取渐近极限，并把场归一化为零真空期望、单位单粒子重叠。下文先用这些渐近关系求散射振幅，再由精确能谱说明场的归一化和时间平均怎样选出单粒子分量。

出入态内积就是散射振幅。将多粒子态的整体归一化吸收入波包权函数，使式[（5.6）](#eq:c05-two-packet-norm)给出的入、出态范数各为一。以两入两出为例，

<span id="eq:c05-s-matrix-element"></span>

$$
S[h_1,h_2;f_1,f_2]
=\langle0|A_{\rm out}[h_1]A_{\rm out}[h_2]
A_{\rm in}^\dagger[f_1]A_{\rm in}^\dagger[f_2]|0\rangle.
\tag{5.9}
$$

出态取共轭会反转两个算符的次序，而玻色出射湮灭算符彼此对易，所以可以采用上式顺序。若有更多出射粒子，只须增加相应产生链，并按多粒子内积归一化。这个内积同时包含散射和未散射的重叠，后面约化时需要保留两部分。

<span id="c05-boundary"></span>

## 外腿投影的时间变化

目标是把渐近端点的粒子投影换成整个时空中的场插入。先固定有限端点 $t_-<t_+$，并定义
$F_f(x)=\int d^3k\,f(\mathbf k)e^{ikx}$。取 $f$为Schwartz函数或光滑紧支撑函数，使固定有限时间的空间边界操作可在适当涂抹的矩阵元上进行。再记
$D_m=-\partial^2+m^2=\partial_t^2-\nabla^2+m^2$，投影定义为

<span id="eq:c05-projection"></span>

$$
A^\dagger[f;t]=-i\int d^3x\,
F_f(x)\overleftrightarrow{\partial_0}\varphi(x).
\tag{5.10}
$$

求端点之差可以先求时间导数。双向导数的两项各产生一个交叉项，恰好相消，只剩两份二阶时间导数：

<span id="eq:c05-flux-time"></span>

$$
\partial_t\left(F_f\dot\varphi-\dot F_f\varphi\right)
=F_f\ddot\varphi-\ddot F_f\varphi.
\tag{5.11}
$$

核中的每个平面波都满足自由色散关系，因此
$\ddot F_f=\nabla^2F_f-m^2F_f$。把第二项中的拉普拉斯作两次空间分部积分，两个负号相消，得到
$\int(\nabla^2F_f)\varphi=\int F_f\nabla^2\varphi$。现在两份二阶导数都已作用于场，可以合并为

<span id="eq:c05-flux-derivative"></span>

$$
\frac{d}{dt}A^\dagger[f;t]
=-i\int d^3x\,F_f(x)D_m\varphi(x).
\tag{5.12}
$$

再按微积分基本定理对有限时间区间积分，就把瞬时投影的变化转成时空积分：

<span id="eq:c05-finite-boundary"></span>

$$
A^\dagger[f;t_+]-A^\dagger[f;t_-]
=-i\int_{t_-}^{t_+}d^4x\,F_f(x)D_m\varphi(x).
\tag{5.13}
$$

自由场满足 $D_m\varphi=0$，所以恢复第3节不随时间改变的投影。加入相互作用以后，右端由相互作用项决定。例如在自由真空附近作三次相互作用的微扰展开，取 $\mathcal L_1=g\varphi^3/6$，经典变分给出
$(\partial^2-m^2)\varphi+g\varphi^2/2=0$，即 $D_m\varphi=g\varphi^2/2$，其中 $1/2$来自 $3/3!$。量子计算中右端采用重整化后的复合场。纯三次势无全局下界，这里用它说明微扰公式的结构。

将式[（5.13）](#eq:c05-finite-boundary)移项，便可由晚端点表示早端点的产生算符；再取厄米共轭并移项，则可由早端点表示晚端点的湮灭算符：

<span id="eq:c05-two-boundaries"></span>

$$
\begin{aligned}
A^\dagger[f;t_-]
&=A^\dagger[f;t_+]+i\int_{t_-}^{t_+}d^4x\,F_f(x)D_m\varphi(x),\\
A[f;t_+]
&=A[f;t_-]+i\int_{t_-}^{t_+}d^4x\,F_f(x)^*D_m\varphi(x).
\end{aligned}
\tag{5.14}
$$

两个方向都出现 $+i$。第一行只作了一次移项；第二行先由共轭把 $i$变成 $-i$，再由移项反转一次符号。出腿的核是
$F_f^*(x)=\int d^3k\,f(\mathbf k)^*e^{-ikx}$，所以不仅指数，波包权函数也要取共轭。实高斯满足 $f^*=f$，一般复波包则必须保留这一共轭。

在相应渐近极限存在时，有限时间公式就能连接入、出投影。在“出端点在左、入端点在右”的乘积中插入时间排序符号 $T$，算符次序不变。不过代入式[（5.14）](#eq:c05-two-boundaries)以后，某个产生算符已从早端点改到晚端点，把它移过其余算符就须计算对易子。它与出射湮灭算符的CCR给出式[（5.3）](#eq:c05-packet-inner)中的波包内积，正是未散射项的来源。下一步将把这项与场插入一起算出。

<span id="c05-lsz-single"></span>

## 将一个外部粒子换成场插入

为便于重复约化，令
$B=T\{\varphi(z_1)\cdots\varphi(z_r)\}$代表矩阵元中已有的场插入，各 $z_j^0$先固定在有限区间内。尚未约化的入、出粒子分别记作 $\alpha,\beta$，并定义

<span id="eq:c05-timeordered-flux"></span>

$$
\begin{aligned}
G_B(x)&=\langle\beta,{\rm out}|
T\{\varphi(x)B\}|\alpha,{\rm in}\rangle,\\
Q_f(t)&=-i\int d^3x\,
F_f(x)\overleftrightarrow{\partial_t}G_B(x).
\end{aligned}
\tag{5.15}
$$

先选 $t_-$早于全部插入时间，$t_+$晚于全部插入时间。这样，时间序在两个端点分别把新场放到乘积的右端和左端，得到

<span id="eq:c05-ordered-endpoints"></span>

$$
\begin{aligned}
Q_f(t_-)&=\langle\beta|B A^\dagger[f;t_-]|\alpha\rangle,\\
Q_f(t_+)&=\langle\beta|A^\dagger[f;t_+]B|\alpha\rangle.
\end{aligned}
\tag{5.16}
$$

对 $Q_f$求导，双向导数的交叉项相消，再作空间分部积分，得到
$\dot Q_f=-i\int d^3x\,F_fD_xG_B$。因此端点之差为

<span id="eq:c05-ordered-boundary"></span>

$$
\begin{aligned}
&\langle\beta|B A^\dagger[f;t_-]|\alpha\rangle
-\langle\beta|A^\dagger[f;t_+]B|\alpha\rangle\\
&\hspace{2em}
=i\int_{t_-}^{t_+}d^4x\,F_f(x)D_xG_B(x).
\end{aligned}
\tag{5.17}
$$

与前面的单场边界关系相比，这次微分的是整个时间序矩阵元。时间经过某个 $z_j^0$时，算符次序会改变，其贡献已经包含在 $D_xG_B$中，稍后将用两点函数具体说明。

令 $\beta=(h_1,\ldots,h_{n'})$。取端点极限后，晚端点的产生算符出现在出态左矢的右侧。将它依次移过各出射湮灭算符，每经过一次都产生一个波包内积，于是

<span id="eq:c05-spectator-commutator"></span>

$$
\langle\beta,{\rm out}|A^\dagger_{\rm out}[f]
=\sum_{r=1}^{n'} C(h_r,f)
\langle\beta\setminus h_r,{\rm out}|,
\qquad C(h,f)\equiv\langle h,f\rangle_{\rm pkt}.
\tag{5.18}
$$

完全移到最左端的产生算符湮灭真空左矢，而各次交换产生的内积项保留下来。将这个结果代回端点关系，就得到一个入射粒子的约化公式：

<span id="eq:c05-in-reduction"></span>

$$
\begin{aligned}
\langle\beta,{\rm out}|B|f,\alpha,{\rm in}\rangle
={}&\sum_r C(h_r,f)
\langle\beta\setminus h_r,{\rm out}|B|\alpha,{\rm in}\rangle\\
&+i\int d^4x\,F_f(x)D_x
\langle\beta,{\rm out}|T\{\varphi(x)B\}|\alpha,{\rm in}\rangle.
\end{aligned}
\tag{5.19}
$$

第一项使 $f$中的粒子直接进入某个出射包 $h_r$，其余粒子仍可继续散射；第二项把该粒子换成场插入，并附上 $iD_x$。因此，“约化一条外腿”同时产生一个直接配对项和一个场积分项。

出射腿用同一边界思路处理。改取投影
$+i\int F_h^*\overleftrightarrow{\partial_t}G_B$，晚端点成为 $A_{\rm out}[h]B$，早端点成为 $BA_{\rm in}[h]$。让早端点的湮灭算符作用于入态，便得

<span id="eq:c05-out-reduction"></span>

$$
\begin{aligned}
\langle h,\beta,{\rm out}|B|\alpha,{\rm in}\rangle
={}&\sum_s C(h,f_s)
\langle\beta,{\rm out}|B|\alpha\setminus f_s,{\rm in}\rangle\\
&+i\int d^4y\,F_h(y)^*D_y
\langle\beta,{\rm out}|T\{\varphi(y)B\}|\alpha,{\rm in}\rangle.
\end{aligned}
\tag{5.20}
$$

约化下一条腿时，已有插入的坐标先保持有限，最后完成相应的外层积分。式[（5.18）](#eq:c05-spectator-commutator)的内积项保留了未散射的粒子。

<span id="c05-contact"></span>

## 时间序微分产生的接触项

约化关系中的 $D$作用于整个时间序乘积。用最简单的两个场展开时间序，就能看清为什么不能只对每个场分别使用运动方程：

$$
T\{\varphi(x)\varphi(y)\}
=\theta(x^0-y^0)\varphi(x)\varphi(y)
+\theta(y^0-x^0)\varphi(y)\varphi(x).
$$

第一次对 $x^0$求导，阶跃函数的导数乘上等时的
$[\varphi(x),\varphi(y)]$，这一项为零。第二次求导时，阶跃函数的导数改为乘场速度的对易子，因而

<span id="eq:c05-contact-derivative"></span>

$$
\partial_{x^0}^2T\{\varphi(x)\varphi(y)\}
=T\{\ddot\varphi(x)\varphi(y)\}
+\delta(x^0-y^0)[\dot\varphi(x),\varphi(y)]_{x^0=y^0}.
\tag{5.21}
$$

若 $\Pi=\dot\varphi$，等时CCR把最后一项化为
$-i\delta^4(x-y)$。于是完整的波算符作用给出

<span id="eq:c05-contact-green"></span>

$$
\begin{aligned}
D_xG_2(x,y)
&=\langle0|T\{(D_x\varphi(x))\varphi(y)\}|0\rangle
-i\delta^4(x-y),\\
G_2(x,y)&=\langle0|T\{\varphi(x)\varphi(y)\}|0\rangle .
\end{aligned}
\tag{5.22}
$$

delta只在两个点重合时有支撑，因此称为接触项（contact term）。若动能改成 $Z_\varphi$倍，共轭动量就是
$\Pi=Z_\varphi\dot\varphi$；在保持正则CCR的有调节器模型中，接触项系数便相应改为 $-i/Z_\varphi$。

自由场可以把这项具体显示出来。固定空间动量以后，两点函数为
$g_\omega(t)=e^{-i\omega|t|}/(2\omega)$。在 $t\ne0$处，它满足 $(\partial_t^2+\omega^2)g_\omega=0$，但原点两侧有
$g_\omega'(0^+)=-i/2$、$g_\omega'(0^-)=+i/2$。一阶导数的跳变为 $-i$，所以二阶导数含有

<span id="eq:c05-free-contact"></span>

$$
(\partial_t^2+\omega^2)g_\omega(t)=-i\delta(t).
\tag{5.23}
$$

再作空间傅里叶积分，便得到 $D_xG_2=-i\delta^4$。自由KG方程约束场在非重合点处的演化，时间序则在重合点引入了这个非零右端。因此外腿微分须保留在 $T$外面，逐场套用运动方程会漏掉接触项。

<span id="c05-lsz"></span>

## 逐腿约化与完整的散射矩阵

单腿关系已把两种贡献分开，现在可以反复使用它。令 $F=(f_1,\ldots,f_n)$、$H=(h_1,\ldots,h_{n'})$，先按固定次序约化全部入射腿。每次应用式[（5.19）](#eq:c05-in-reduction)，该腿或者与一条尚未使用的出射腿配对，或者成为场插入。入射腿全部处理后，剩余入态为真空；再用式[（5.20）](#eq:c05-out-reduction)约化剩余出射腿时，早端点湮灭算符作用于真空为零，于是只留下场积分。

将所有未配对外腿都换成场的结果记为

<span id="eq:c05-amputated-packet"></span>

$$
\begin{aligned}
\mathcal R(H;F)
={}&
\left[\prod_{s=1}^{n}i\int d^4x_s\,F_{f_s}(x_s)D_{x_s}\right]
\left[\prod_{r=1}^{n'}i\int d^4y_r\,F_{h_r}(y_r)^*D_{y_r}\right]\\
&\quad\times
\langle0|T\{\varphi(y_1)\cdots\varphi(y_{n'})
\varphi(x_1)\cdots\varphi(x_n)\}|0\rangle.
\end{aligned}
\tag{5.24}
$$

方括号中的运算按从左到右、从外层到内层嵌套：最先引入的 $x_1$积分在最外层，接着是其余入腿，最后才是出腿。求内层端点极限时，外层坐标保持有限；即使部分腿已经配对删去，也保留其余腿的相对次序。约定
$\mathcal R(\varnothing;\varnothing)=1$；若只剩单个场，则由零真空期望得到零。

完整内积还要把所有直接配对选择相加。记 $M$为入、出腿间的一个部分匹配，每条腿至多出现于一对中；以 $H_M,F_M$表示删去这些配对后剩下的波包，便有

<span id="eq:c05-full-s"></span>

$$
S(H;F)
=\sum_M\left[\prod_{(r,s)\in M}C(h_r,f_s)\right]
\mathcal R(H_M;F_M).
\tag{5.25}
$$

其中空匹配给出 $\mathcal R(H;F)$。若共有 $k$对，可选择的匹配数为
$\binom{n'}k\binom nk k!$：先选两侧参与配对的腿，再选它们的一一对应。固定的入射约化顺序使每个匹配只出现一次，故式[（5.25）](#eq:c05-full-s)不再带额外的粒子数阶乘。外腿的玻色交换对称性已由配对求和与时间序函数体现。

来看两个简单情形。稳定单粒子在入、出描述中是同一个精确能量本征态，选定一致相位后有 $S(h;f)=C(h,f)$。单腿公式也给出同样结果：单位重叠使
$\langle h|\varphi(x)|0\rangle=F_h(x)^*$，右端满足自由KG方程，积分项因此为零，即
$\mathcal R(h;f)=0$。所以对两入两出，式[（5.25）](#eq:c05-full-s)化为

<span id="eq:c05-two-two-full"></span>

$$
\begin{aligned}
S(h_1,h_2;f_1,f_2)
={}&C(h_1,f_1)C(h_2,f_2)+C(h_1,f_2)C(h_2,f_1)\\
&+\mathcal R(h_1,h_2;f_1,f_2).
\end{aligned}
\tag{5.26}
$$

前两项正是两粒子恒等算符的矩阵元。在自由理论中，$A_{\rm out}=A_{\rm in}$，两次CCR就给出这两项，此时 $\mathcal R=0$、$S=1$。

粒子更多时，$S-1$还可含有未散射的旁观粒子，以及彼此独立的散射过程。例如四个粒子可分为两组，各自发生一次两粒子散射。连通振幅则要求全部外腿参与同一过程，计算时在式[（5.24）](#eq:c05-amputated-packet)中使用连通关联函数；它的图形组织将在费曼图章节展开。若入、出包间的所有 $C(h_r,f_s)$都为零，式[（5.25）](#eq:c05-full-s)便只剩全部外腿的约化积分。

<span id="c05-plane-wave"></span>

## 从波包转到确定动量的振幅

散射公式通常用确定动量的外态书写。先把波包振幅表示为动量振幅的积分，便能明确确定动量振幅是怎样的积分核：

<span id="eq:c05-smearing-s"></span>

$$
\begin{aligned}
S(H;F)
={}&\int\left[\prod_r d^3p_r\,h_r(\mathbf p_r)^*\right]
\left[\prod_s d^3k_s\,f_s(\mathbf k_s)\right]\\
&\quad\times
\langle p_1,\ldots,p_{n'},{\rm out}
|k_1,\ldots,k_n,{\rm in}\rangle .
\end{aligned}
\tag{5.27}
$$

动量本征态采用delta归一化，所以将 $f$换成
$\delta^3(\mathbf k-\mathbf k_s)$是在提取上述积分核。它与保持态范数为一的窄包极限不同。对单位范数高斯，由式[（5.4）](#eq:c05-gaussian-norm)有
$N\propto\sigma^{-3/2}$，其普通积分却正比于
$N\sigma^3\propto\sigma^{3/2}\to0$，因此不会趋于delta函数。delta逼近应改取
$(4\pi\sigma^2)^{-3/2}\exp[-|\mathbf k-\mathbf k_s|^2/(4\sigma^2)]$，使普通积分保持为一；相应态范数平方按 $\sigma^{-3}$发散，正好反映精确动量态的非普通归一化。

按这个意义提取式[（5.24）](#eq:c05-amputated-packet)中的动量积分核，得到

<span id="eq:c05-lsz-momentum"></span>

$$
\begin{aligned}
\mathcal R(p_1,\ldots,p_{n'};k_1,\ldots,k_n)
={}&
\left[\prod_{s=1}^{n}i\int d^4x_s\,e^{ik_sx_s}D_{x_s}\right]
\left[\prod_{r=1}^{n'}i\int d^4y_r\,e^{-ip_ry_r}D_{y_r}\right]\\
&\quad\times
\langle0|T\{\varphi(y_1)\cdots\varphi(y_{n'})
\varphi(x_1)\cdots\varphi(x_n)\}|0\rangle .
\end{aligned}
\tag{5.28}
$$

所有外部动量都取正能在壳值。各因子的来源可以逐一对应前面的运算：每个 $i$来自端点移项，每个 $D$来自自由波包核的KG方程，出射指数的共轭来自出态取左矢。式中不再另有 $(2\pi)^3 2\omega$分母：本节波包采用普通 $d^3k$，反演投影已消去模式测度中的相应归一化。完整动量态内积仍须按式[（5.25）](#eq:c05-full-s)补回直接配对项，只需把
$C$换成 $(2\pi)^3 2\omega\,\delta^3$。

LSZ由此将散射问题转成了时间序关联函数的计算。外腿投影所选出的粒子质量和场归一化，则由精确能谱确定。

<span id="c05-spectrum"></span>

## 插值场所见的精确谱

沿用前面有质量隙的标量理论，真空满足 $P^\mu|0\rangle=0$。先取没有束缚态、最低连续谱为双粒子态的情形。

单粒子壳之外是多粒子连续谱。双粒子谱的下边界是不变质量为 $2m$的双曲线，可以从能量最小化看出其原因。在固定总动量 $\mathbf P$下，两粒子的自由渐近能量为
$E(\mathbf q)=\sqrt{\mathbf q^2+m^2}+\sqrt{(\mathbf P-\mathbf q)^2+m^2}$。对相对动量求导，梯度为 $\mathbf q/\omega_{\mathbf q}-(\mathbf P-\mathbf q)/\omega_{\mathbf P-\mathbf q}$。在 $m>0$时，速度映射单射，驻点只有 $\mathbf q=\mathbf P/2$；每份能量的Hessian
$(\delta_{ij}-v_iv_j)/\omega$又正定，所以这个驻点给出全局最低能量：

<span id="eq:c05-threshold"></span>

$$
E_{\rm one}(\mathbf P)=\sqrt{\mathbf P^2+m^2},\qquad
E_{\rm threshold}(\mathbf P)=
2\sqrt{\frac{\mathbf P^2}{4}+m^2}
=\sqrt{\mathbf P^2+4m^2}.
\tag{5.29}
$$

相对动量的连续变化给出阈值以上的连续谱。若存在束缚态，则须在连续谱下添加相应支线，并为它们分别选择插值场。

![真空、单粒子质量壳与双粒子连续谱阈值](/images/srednicki/05-inline-1.svg)

图5.1：按式[（5.29）](#eq:c05-threshold)绘制的谱图。横轴是总动量沿固定方向的有符号截面，两个曲面在三维动量中具有旋转对称性。两轴均以 $m$ 为单位；真空位于原点，单粒子态构成孤立质量壳，阴影表示多粒子连续谱的支撑。

图像确定了可能的能谱分量，下面求场与这些分量的重叠。第2节的平移协变性给出

<span id="eq:c05-translation-field"></span>

$$
\varphi(x)=e^{-iP^\mu x_\mu}\varphi(0)e^{iP^\mu x_\mu}.
\tag{5.30}
$$

左右都取真空时，两个指数的作用均为一，真空期望
$v=\langle0|\varphi(x)|0\rangle=\langle0|\varphi(0)|0\rangle$
因而与坐标无关。对厄米场，$v$还是实数。若将左矢改成四动量为 $p$的单粒子态，左指数就给出 $e^{-ipx}$，右指数仍给一，于是

<span id="eq:c05-one-overlap"></span>

$$
\langle p|\varphi(x)|0\rangle=e^{-ipx}c,\qquad
c\equiv\langle p|\varphi(0)|0\rangle.
\tag{5.31}
$$

重叠常数 $c$不依赖动量，还用到了自旋零、原点标量场和不变真空：正能质量壳上的任意两点都能由正规正时变换联系，在相对论态归一化下，相应矩阵元相同。若有自旋或物种混合，重叠就还须携带相应指标。

<span id="c05-field-normalization"></span>

## 去掉真空重叠并选定单粒子留数

要让投影只挑出所需粒子，先须去掉真空分量。将非零常数 $v$代入式[（5.10）](#eq:c05-projection)，可以直接求出 $v$对投影的贡献：

<span id="eq:c05-vacuum-contamination"></span>

$$
\langle0|A^\dagger[f;t]|0\rangle
=(2\pi)^3m\,f(\mathbf0)\,v\,e^{-imt}.
\tag{5.32}
$$

双向导数只剩 $-\dot F_fv$，而 $\dot F_f=-i\int d^3k\,\omega f e^{ikx}$，与外面的 $-i$相乘后给正号，空间积分再选出 $\mathbf k=0$。这个真空项不会随时间增大而衰减。虽然对满足 $f(\mathbf0)=0$的特殊包它不贡献，要对任意波包使用同一插值场，适合的选择仍是
$\varphi_{\rm shifted}=\varphi_{\rm old}-v$。这样移去真空期望以后，改写原拉格朗日量时应把旧变量代成
$\varphi_{\rm shifted}+v$，并相应展开各项。

接下来调节单粒子分量。将式[（5.31）](#eq:c05-one-overlap)代入投影，空间积分选出 $\mathbf k=\mathbf p$，双向导数给出 $\omega_{\mathbf k}+p^0=2\omega_{\mathbf p}$，同时两个时间相位相消，因此

<span id="eq:c05-one-projection"></span>

$$
\langle p|A^\dagger[f;t]|0\rangle
=(2\pi)^3 2\omega_{\mathbf p}\,f(\mathbf p)c.
\tag{5.33}
$$

投影产生了所需的单粒子波包，只是带有一个额外的重叠常数 $c$。当 $c$非零且有限时，可以先选单粒子态的共同相位，使 $c>0$，再用实数重标度场，令
$\varphi_R=(\varphi_{\rm old}-v)/c$。新场仍厄米，并满足两个归一化条件：

<span id="eq:c05-lsz-field-normalization"></span>

$$
\langle0|\varphi_R(x)|0\rangle=0,\qquad
\langle p|\varphi_R(x)|0\rangle=e^{-ipx}.
\tag{5.34}
$$

此后省去下标 $R$，采用单位单粒子重叠。保留旧场时，每条LSZ外腿应带 $i/c$；代入 $\varphi_{\rm old}=c\varphi_R+v$以后，就恢复前文的 $i$。这种场尺度的选择也会改变拉格朗日量中的动能系数 $Z_\varphi$。

<span id="c05-continuum"></span>

## 振荡如何消去多粒子矩阵元

真空和单粒子分量已经处理，点场仍一般会产生多粒子成分。记 $|p,n\rangle$为总四动量 $p$的广义态，$n$包括不变质量 $M$、相对动量等其余标签。再次应用平移协变性，有

<span id="eq:c05-many-overlap"></span>

$$
\langle p,n|\varphi(x)|0\rangle=e^{-ipx}A_n(\mathbf p),
\qquad p^0=\sqrt{\mathbf p^2+M^2},\quad M\geq2m.
\tag{5.35}
$$

其中 $A_n$可以依赖多粒子动量的洛伦兹不变组合。把测试态展开为

$$
|\psi\rangle=\sum_n\int d^3p\,\psi_n(\mathbf p)|p,n\rangle.
$$

这里的 $\sum_n$同时包含连续谱积分及其规范化权重，并非只对整数粒子数求和。固定一个可归一化的多粒子测试态，再用它检测 $A^\dagger[f;t]|0\rangle$，代入前面的场矩阵元，便得到

<span id="eq:c05-many-projection"></span>

$$
\begin{aligned}
\langle\psi|A^\dagger[f;t]|0\rangle
={}&-i\sum_n\int d^3p\,d^3k\,d^3x\,
\psi_n(\mathbf p)^*f(\mathbf k)A_n(\mathbf p)\\
&\hspace{1em}\times
e^{ikx}\overleftrightarrow{\partial_0}e^{-ipx}.
\end{aligned}
\tag{5.36}
$$

对两个指数求时间导数，分别得到 $-ik^0e^{ikx}$和 $+ip^0e^{-ipx}$，所以
$-i e^{ikx}\overleftrightarrow{\partial_0}e^{-ipx}
=(p^0+k^0)e^{i(k-p)x}$。空间积分随后产生
$(2\pi)^3\delta^3(\mathbf k-\mathbf p)$，将两份动量联系起来，得到

<span id="eq:c05-oscillatory-projection"></span>

$$
\langle\psi|A^\dagger[f;t]|0\rangle
=\sum_n\int d^3p\,G_n(\mathbf p)
e^{it\Delta_M(\mathbf p)},
\tag{5.37}
$$

其中记
$G_n=(2\pi)^3(E_M+\omega)\psi_n^* f A_n$、
$\Delta_M(\mathbf p)=\sqrt{\mathbf p^2+M^2}-\sqrt{\mathbf p^2+m^2}$。两能量共用同一三动量，因此在 $M\geq2m>m$时有 $\Delta_M>0$。相位还随动量改变，由这一变化可以把积分改写成Riemann–Lebesgue引理所用的线性相位形式。

对满足
$\sum_n\int d^3p\,|G_n(\mathbf p)|<\infty$的矩阵元，连续标签按选定谱测度积分。对固定 $M>m$，令 $q=|\mathbf p|$，先作角积分，记
$g_n(q)=q^2\int d\Omega\,G_n(q\widehat{\mathbf p})$。当 $q>0$时，

<span id="eq:c05-phase-monotone"></span>

$$
\frac{d\Delta_M}{dq}
=q\left(\frac1{\sqrt{q^2+M^2}}-\frac1{\sqrt{q^2+m^2}}\right)<0.
\tag{5.38}
$$

因而 $u=\Delta_M(q)$把 $q\in(0,\infty)$一一映到
$u\in(0,M-m)$，但方向相反。连同Jacobian换元，积分成为

<span id="eq:c05-phase-density"></span>

$$
\int_0^\infty dq\,g_n(q)e^{it\Delta_M(q)}
=\int_0^{M-m}du\,\rho_n(u)e^{itu},
\qquad
\rho_n(u)=\frac{g_n(q(u))}{|\Delta_M'(q(u))|}.
\tag{5.39}
$$

端点处虽然有 $q=0$的导数为零，以及 $q\to\infty$时导数趋零，换元后的密度仍满足
$\int du\,|\rho_n(u)|\leq\int dq\,q^2\int d\Omega\,|G_n|<\infty$。因此，原来假设的绝对可积性恰好转化为线性相位积分所需的可积性。

对这个可积密度，Riemann–Lebesgue结论也可直接证明。先用有限个区间上的常数函数 $s(u)$在 $L^1$中逼近 $\rho_n$。每个区间的振荡积分是
$(e^{itb}-e^{ita})/(it)$，故 $s$的积分趋于零；余差对任意 $t$都满足
$|\int(\rho_n-s)e^{itu}du|\leq\|\rho_n-s\|_1$。先让逼近足够好，再取 $|t|\to\infty$，便得到每个 $n$的极限为零。最后用最初可和的 $L^1$界控制连续及离散 $n$的积分，得
$\langle\psi|A^\dagger[f;t]|0\rangle\to0$。

不同能量的分量在固定测试态上的贡献通过振荡相互抵消。这给出矩阵元的弱极限。若在谱表示中，多粒子分量为平方可积的 $B_n(\mathbf p)e^{it\Delta_M(\mathbf p)}$，它本身的范数却是

<span id="eq:c05-weak-not-strong"></span>

$$
\|\Psi_{\rm multi}(t)\|^2
=\sum_n\int d\mu_n(\mathbf p)\,|B_n(\mathbf p)|^2
\tag{5.40}
$$

其范数与时间无关。要使多粒子分量的范数也趋于零，可以给投影加上时间平均。取宽度为 $\tau$的归一化高斯，定义

<span id="eq:c05-time-average"></span>

$$
\overline A^\dagger[f;t,\tau]
=\int_{-\infty}^{\infty}\frac{ds}{\sqrt{2\pi}\tau}
 e^{-(s-t)^2/(2\tau^2)}A^\dagger[f;s].
$$

对任一能量差 $\Delta$，这个积分给出

$$
\int\frac{ds}{\sqrt{2\pi}\tau}
 e^{-(s-t)^2/(2\tau^2)}e^{is\Delta}
=e^{it\Delta}e^{-\tau^2\Delta^2/2}.
$$

单粒子分量满足 $\Delta=0$，因而保持原值；多粒子分量则乘上衰减因子。取 $f$的动量支撑包含于 $|\mathbf p|\leq K$，由 $M\geq2m$可得共同下界

$$
\Delta_M(\mathbf p)\geq
\delta_K\equiv\sqrt{K^2+4m^2}-\sqrt{K^2+m^2}>0.
$$

设某个 $\tau_0>0$的平均已使谱积分有限。对 $\tau\geq\tau_0$，

$$
\begin{aligned}
\|\overline\Psi_{\rm multi}(t,\tau)\|^2
&=\sum_n\int d\mu_n\,|B_n|^2e^{-\tau^2\Delta_M^2}\\
&\leq e^{-(\tau^2-\tau_0^2)\delta_K^2}
\sum_n\int d\mu_n\,|B_n|^2e^{-\tau_0^2\Delta_M^2}
\longrightarrow0.
\end{aligned}
$$

谱权重至多按能量的幂增长时，高斯因子保证右端的积分有限。这就直接给出了平均投影作用于真空时的单粒子范数极限。在散射构造中同时取 $t\to\pm\infty$、$\tau\to\infty$和 $\tau/|t|\to0$，平均区间相对于传播时间仍很短，速度支撑分离的波包保持在相应的渐近区域。多粒子渐近算符的构造及其与逐腿约化的联系，可进一步参看 Collins 的[时间平均推导](https://arxiv.org/abs/1904.10923)。

<span id="c05-parameters"></span>

## 移场与重标度如何改变拉格朗日量

为挑出单粒子态所作的移场和重标度，也会改变拉格朗日量的系数。用三次模型可以具体说明这一点。暂以 $\varphi_0,m_0,g_0$表示旧场和旧参数，写成
$\mathcal L_0=-\tfrac12(\partial\varphi_0)^2
-\tfrac12m_0^2\varphi_0^2+g_0\varphi_0^3/6$。按前面的定义，旧场为 $\varphi_0=c\varphi+v$。动能中的常数导数为零，平方项与立方项则分别展开为
$c^2\varphi^2+2cv\varphi+v^2$和
$c^3\varphi^3+3c^2v\varphi^2+3cv^2\varphi+v^3$。把同次幂逐项合并，得到

<span id="eq:c05-shift-rescale"></span>

$$
\begin{aligned}
\mathcal L_0={}&-\frac{c^2}{2}(\partial\varphi)^2
-\frac{c^2}{2}(m_0^2-g_0v)\varphi^2
+\frac{g_0c^3}{6}\varphi^3\\
&+c\left(-m_0^2v+\frac{g_0v^2}{2}\right)\varphi
-\frac{m_0^2v^2}{2}+\frac{g_0v^3}{6}.
\end{aligned}
\tag{5.41}
$$

最后两项与场无关，在当前平直背景并已指定能量零点的讨论中可另作调整，不进入场方程。再用物理质量 $m$以及由指定观测条件定义的耦合 $g$标记参数，便可把拉格朗日密度写成

<span id="eq:c05-renormalized-parameters"></span>

$$
\mathcal L=
-\frac12Z_\varphi(\partial\varphi)^2
-\frac12Z_m m^2\varphi^2
+\frac16Z_g g\varphi^3+Y\varphi.
\tag{5.42}
$$

逐项比较上述变量代换，系数为
$Z_\varphi=c^2$、
$Z_m m^2=c^2(m_0^2-g_0v)$、
$Z_g g=g_0c^3$、
$Y=c(-m_0^2v+g_0v^2/2)$。量子修正通过真空期望、场的单粒子重叠以及裸参数与物理参数的关系进入这些系数。物理质量 $m$由精确谱中的单粒子质量壳定义。

四项归一化条件各有作用：零真空期望去掉真空分量，单位单粒子重叠固定场尺度，质量壳位置定义 $m$，指定散射观测量定义 $g$。在微扰计算中，这些条件逐阶确定 $Y$和三个 $Z$。四维自然单位中 $[g]=1$、$[Y]=3$，各 $Z$无量纲，与上面的代数关系一致。

例如，可以用低能库仑散射截面的系数定义物理电荷 $e$，使其在指定的低能极限下具有库仑散射的形式。三次模型也通过选定散射过程和运动学条件来定义耦合 $g$。

选定这些归一化条件以后，散射振幅的计算归结为时间序关联函数。[下一节](/posts/srednicki-06/)从量子力学的路径积分建立计算方法，再将它推广到场论。

---

[← 第 4 节](/posts/srednicki-04/) · [章节地图](/srednicki/) · [第 6 节 →](/posts/srednicki-06/)
