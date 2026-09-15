---
title: 'Srednicki §15 Lehmann–Källén 形式下的单圈修正'
date: 2026-09-14
category: 笔记
tags: [物理, 量子场论, Srednicki]
series: 'Srednicki QFT'
srednickiSections: [15]
hideFromHome: true
draft: false
---

<span id="c15"></span>

第13节从中间态的谱分解得到精确传播子，第14节则用圈图算出了自能。这两种方法描述同一个二点函数，因此圈积分的结果应当能够重新写成谱表示。先考察传播子的虚部最为方便：它可以直接选出指定不变质量处的谱权重，使单粒子极点和多粒子连续谱分别显现出来。

<span id="c15-boundary"></span>

## 两种表示与主值恒等式

记 $z=k^2$，将第13节的谱表示与第14节的自能表示并列写出：

<span id="eq:c15-two-representations"></span>

$$
\begin{aligned}
\widetilde{\boldsymbol\Delta}(z)
&=\frac1{z+m^2-i0}
+\int_{4m^2}^{\infty}ds\,\frac{\rho(s)}{z+s-i0},\\
\widetilde{\boldsymbol\Delta}(z)
&=\frac1{z+m^2-i0-\Pi(z)}.
\end{aligned}
\tag{15.1}
$$

场仍取单位单粒子重叠，所以第一行已显式分出单粒子项，$\rho$ 只包含其余谱。以下继续采用第13节的稳定单粒子和正谱条件；第二行中的自能则用上一节的圈展开计算。六维的一圈结果及其中的参数为

<span id="eq:c15-loop-input"></span>

$$
\begin{aligned}
\Pi_1(z)
&=\frac\alpha2\int_0^1dx\,D\ln\frac D{D_0}
-\frac\alpha{12}(z+m^2),\\
\alpha&=\frac{g^2}{(4\pi)^3},\qquad a_x=x(1-x),\\
D&=m^2+a_xz-i0,\qquad D_0=m^2(1-a_x).
\end{aligned}
\tag{15.2}
$$

下标1表示只取 $O(\alpha)$ 项，即 $\Pi=\Pi_1+O(\alpha^2)$。要比较两种表示的虚部，先求出传播分母在实轴上的边界值。对实变量 $v$ 和有限调节 $\eta>0$，乘以分母的复共轭，可以把实部与虚部分开：

<span id="eq:c15-finite-boundary"></span>

$$
\frac1{v-i\eta}
=\frac{v}{v^2+\eta^2}
+i\frac{\eta}{v^2+\eta^2}.
\tag{15.3}
$$

当 $\eta\to0$ 时，虚部在原点附近越来越窄、越来越高，它的极限要通过与试验函数积分来确定。取任意施瓦茨试验函数 $f$，作代换 $v=\eta u$，得到

<span id="eq:c15-imaginary-delta-limit"></span>

$$
\int_{-\infty}^{\infty}dv\,
\frac{\eta f(v)}{v^2+\eta^2}
=\int_{-\infty}^{\infty}du\,\frac{f(\eta u)}{1+u^2}
\longrightarrow \pi f(0).
\tag{15.4}
$$

右边的被积函数受可积函数 $\sup|f|/(1+u^2)$ 控制，因而可以把极限移入积分；剩下的核积分为 $\pi$，所以分布极限正是 $\pi\delta(v)$。

实部也用同样的办法求极限。它的核关于原点奇对称，将负半轴换到正半轴后，两侧试验函数相减，便有

<span id="eq:c15-real-principal-value"></span>

$$
\begin{aligned}
\int_{-\infty}^{\infty}dv\,\frac{vf(v)}{v^2+\eta^2}
&=\int_0^\infty dv\,
\frac{v[f(v)-f(-v)]}{v^2+\eta^2}\\
&\longrightarrow
\int_0^\infty dv\,\frac{f(v)-f(-v)}v
=\operatorname{PV}\int_{-\infty}^{\infty}dv\,\frac{f(v)}v .
\end{aligned}
\tag{15.5}
$$

在原点附近，$f(v)-f(-v)=2vf'(0)+O(v^3)$，使第一行的被积函数一致有界；在远处，$f$ 的快速衰减又给出可积控制，所以可以取所写的极限。最后一项称为主值（principal value），其定义是在原点两侧对称去掉 $(-a,a)$，再取 $a\to0$。将实部与虚部的极限合在一起，得到

<span id="eq:c15-sokhotski"></span>

$$
\frac1{v-i0}
=\operatorname{PV}\frac1v+i\pi\delta(v).
\tag{15.6}
$$

上式给出了分布的边界值，前面的有限 $\eta$ 表达式则给出趋向它的普通函数。将这一关系用于式[（15.1）](#eq:c15-two-representations)中的每个谱质量，传播子的虚部就成为

<span id="eq:c15-spectral-imaginary"></span>

$$
\begin{aligned}
\operatorname{Im}\widetilde{\boldsymbol\Delta}(z)
&=\pi\delta(z+m^2)
+\pi\int_{4m^2}^{\infty}ds\,\rho(s)\delta(z+s)\\
&=\pi\delta(z+m^2)+\pi\rho(-z).
\end{aligned}
\tag{15.7}
$$

delta函数消去关于 $s$ 的积分，换元因子为 $|\partial(z+s)/\partial s|^{-1}=1$。由于约定 $\rho(s)$ 在 $s<4m^2$ 时为零，谱积分下限的作用已包含在这一记号中，无须再写阶跃函数。因而在连续谱区域，可以直接由虚部读出

<span id="eq:c15-density-from-imaginary"></span>

$$
\rho(s)=\frac1\pi
\operatorname{Im}\widetilde{\boldsymbol\Delta}(-s),
\qquad s>4m^2 .
\tag{15.8}
$$

这就将稳定单粒子的delta峰与连续谱密度分开，阈值端则按相应分布或连续极限理解。下面用自能表示计算同一虚部，看这两类贡献怎样出现。

<span id="c15-pole"></span>

## 实自能区域中的单粒子极点

先取物理质量壳附近没有吸收部分的区间，其中 $\operatorname{Im}\Pi(z)=0$。传播分母的实部记为 $h(z)=z+m^2-\Pi(z)$，则两个在壳条件给出

<span id="eq:c15-inverse-root"></span>

$$
h(-m^2)=0,\qquad h'(-m^2)=1,
\qquad
h(z)=(z+m^2)+O((z+m^2)^2).
\tag{15.9}
$$

因此在足够小的邻域内，$h$ 单调且只有这个简单零点，Feynman边界的方向也保持不变。此时传播子的虚部为 $\operatorname{Im}\widetilde{\boldsymbol\Delta}=\pi\delta(h(z))$，其权重由根处的导数决定。应用第3节的delta函数换元公式：若 $h$ 在积分区间内有简单零点 $z_j$，则

<span id="eq:c15-delta-of-inverse"></span>

$$
\delta(h(z))
=\sum_j\frac{\delta(z-z_j)}{|h'(z_j)|}.
\tag{15.10}
$$

将式[（15.9）](#eq:c15-inverse-root)中的零点和导数代入，质量壳附近只有一项，且Jacobian等于1，于是得到

<span id="eq:c15-unit-pole-delta"></span>

$$
\operatorname{Im}\widetilde{\boldsymbol\Delta}(z)
=\pi\delta(z+m^2).
\tag{15.11}
$$

导数条件使这个单粒子 delta 峰具有单位权重。在没有其他孤立谱极点的无吸收区间，虚部只含这一单粒子项，连续谱密度为零。

<span id="c15-density"></span>

## 从自能虚部读出连续谱

再看自能具有吸收部分的区域。令 $\Pi_I(z)\equiv\operatorname{Im}\Pi(z)$ 非零，并记 $\Pi_R(z)=\operatorname{Re}\Pi(z)$。在固定的这种动量处，可以先取 $\eta\to0$，再乘以逆核的复共轭，将传播子分解为

<span id="eq:c15-complex-reciprocal"></span>

$$
\begin{aligned}
\widetilde{\boldsymbol\Delta}(z)
&=\frac1{z+m^2-\Pi_R(z)-i\Pi_I(z)}\\
&=\frac{z+m^2-\Pi_R(z)+i\Pi_I(z)}
{[z+m^2-\Pi_R(z)]^2+\Pi_I(z)^2},\\
\operatorname{Im}\widetilde{\boldsymbol\Delta}(z)
&=\frac{\Pi_I(z)}
{[z+m^2-\Pi_R(z)]^2+\Pi_I(z)^2}.
\end{aligned}
\tag{15.12}
$$

逆核的实部为 $z+m^2-\Pi_R(z)$，乘以复共轭后便得到上式中的平方和；其中减去自能的号仍与式[（15.1）](#eq:c15-two-representations)相同。将这个结果用于连续谱，精确关系为

<span id="eq:c15-exact-density"></span>

$$
\pi\rho(s)
=\frac{\Pi_I(-s)}
{[m^2-s-\Pi_R(-s)]^2+\Pi_I(-s)^2}.
\tag{15.13}
$$

分母是正的平方和，所以正谱要求该区域的 $\Pi_I(-s)$ 非负；在分母非零而密度为零的区域，同一关系又给出 $\Pi_I(-s)=0$。这个分式用于连续谱，孤立极点仍以先前的delta项表示。

吸收部分从哪里开始，可以直接查看式[（15.2）](#eq:c15-loop-input)中的参数质量 $D$。决定对数是否进入负实轴的二次函数满足

<span id="eq:c15-parameter-maximum"></span>

$$
a_x=x(1-x)=\frac14-\left(x-\frac12\right)^2,\qquad
0\le a_x\le\frac14,
\tag{15.14}
$$

当 $z\ge0$ 时，所有 $D$ 的实部都不小于 $m^2$；当 $-4m^2<z<0$ 时，其最小值为 $m^2+z/4>0$。同时 $D_0\ge3m^2/4$ 始终为正，故在 $z>-4m^2$ 的零调节边界，对数没有虚部。到 $z=-4m^2$ 时，仅 $x=1/2$ 这一点使 $D=0$，而 $D\ln D$ 的连续极限仍为零。

越过阈值，取 $z=-s<-4m^2$，便有实数 $\beta=\sqrt{1-4m^2/s}$，并在 $x_\pm=(1\pm\beta)/2$ 之间出现负的 $D$。这一区间的对数虚部为 $-\pi$，而它所乘的 $D$ 也为负，因而积分给出正的吸收部分。[第14节已完成这个有限积分](/posts/srednicki-14/#c14-branches)，代入 $-z=s$ 即得

<span id="eq:c15-one-loop-absorptive"></span>

$$
\Pi_{1I}(-s)
=\frac{\pi\alpha s}{12}
\left(1-\frac{4m^2}{s}\right)^{3/2},
\qquad s>4m^2.
\tag{15.15}
$$

于是吸收部分在阈值以前为零、在阈值以后非零，恰好与两粒子连续谱的支集相配。还可以进一步读出谱权重的大小。在一圈精度下，式[（15.13）](#eq:c15-exact-density)的分子已是 $O(\alpha)$，所以分母只须保留零阶 $(s-m^2)^2$。具体地，将其中的平方项展开为 $(s-m^2)^2+2(s-m^2)\Pi_R+O(\alpha^2)$，这个分母修正对整个比值的贡献从 $O(\alpha^2)$ 开始。因此一圈谱密度为

<span id="eq:c15-one-loop-density"></span>

$$
\rho_1(s)
=\frac{\alpha s}{12(s-m^2)^2}
\left(1-\frac{4m^2}{s}\right)^{3/2}
\theta(s-4m^2),
\qquad
\rho=\rho_1+O(\alpha^2).
\tag{15.16}
$$

所得密度非负，质量维数为 $-2$，符合第13节的谱测度约定。从阈值上方趋近时，令 $s=4m^2+\delta s$，可展开为

<span id="eq:c15-density-threshold"></span>

$$
\rho_1(s)
=\frac{\alpha}{216m^2}
\left(\frac{\delta s}{m^2}\right)^{3/2}
\left[1+O(\delta s/m^2)\right].
\tag{15.17}
$$

分母在阈值处仍等于 $9m^4$，因此这个非整数幂来自两粒子通道的开启。谱密度由此描述场与两粒子中间态的重叠权重怎样从阈值处增长。

<span id="c15-matching"></span>

## 连同实部一起恢复谱表示

把割线上的虚部代回围道积分，可以同时恢复传播子的实部。令

<span id="eq:c15-subtracted-contour"></span>

$$
H(z)=\frac{\Pi(z)}{(z+m^2)^2},\qquad
H(z)=\frac{1}{2\pi i}\oint_C\frac{H(w)}{w-z}\,dw.
$$

在壳条件消去了 $H$ 在 $-m^2$ 处的表观奇点。对本节的一圈函数，其余有限奇性位于 $(-\infty,-4m^2]$，阈值处函数有限，大动量下 $\Pi(w)=O(w\log w)$。因此，把围道扩大到半径 $R$ 时，大圆积分为 $O(\log R/R)$；绕阈值的小圆积分也趋零，余下的只有割线两岸。

上下岸满足实解析关系 $\Pi(w+i0)=\Pi(w-i0)^*$，故其差为 $-2i\operatorname{Im}\Pi(w-i0)$。将两岸积分合并，再令 $w=-s$，便得

<span id="eq:c15-cut-contour-evaluation"></span>

$$
\begin{aligned}
H(z)
&=-\frac1\pi\int_{-\infty}^{-4m^2}dw\,
\frac{\operatorname{Im}\Pi(w-i0)}{(w+m^2)^2(w-z)}\\
&=\frac1\pi\int_{4m^2}^{\infty}ds\,
\frac{\operatorname{Im}\Pi(-s-i0)}{(s-m^2)^2(s+z)}.
\end{aligned}
$$

乘回 $(z+m^2)^2$，得到两次减除的色散关系：

<span id="eq:c15-onshell-dispersion"></span>

$$
\Pi(z)=\frac{(z+m^2)^2}{\pi}
\int_{4m^2}^{\infty}ds\,
\frac{\operatorname{Im}\Pi(-s-i0)}
{(s-m^2)^2(s+z)}.
\tag{15.18}
$$

对满足同样割线解析性、阈值可积性与 $\Pi(w)=o(w^2)$ 无穷远条件的自能，同一围道推导也成立。这里将式[（15.16）](#eq:c15-one-loop-density)代入，一圈关系化为

<span id="eq:c15-loop-dispersion-to-density"></span>

$$
\frac{\Pi_1(z)}{(z+m^2)^2}
=\int_{4m^2}^{\infty}ds\,\frac{\rho_1(s)}{s+z}.
\tag{15.19}
$$

这条关系把满足在壳条件的自能与谱密度联系起来。另一方面，在同一精度下将精确逆核按 $\alpha$ 展开，有

<span id="eq:c15-fixed-order-propagator"></span>

$$
\widetilde{\boldsymbol\Delta}(z)
=\frac1{z+m^2-i0}
+\frac{\Pi_1(z)}{(z+m^2-i0)^2}
+O(\alpha^2).
\tag{15.20}
$$

由于 $\Pi_1$ 在 $z=-m^2$ 有二阶零点，第二项的表观极点可去，其边界值由式[（15.19）](#eq:c15-loop-dispersion-to-density)给出的解析函数延拓确定。因此可以将两式合并，得到

<span id="eq:c15-one-loop-kallen-lehmann"></span>

$$
\widetilde{\boldsymbol\Delta}(z)
=\frac1{z+m^2-i0}
+\int_{4m^2}^{\infty}ds\,\frac{\rho_1(s)}{z+s-i0}
+O(\alpha^2).
\tag{15.21}
$$

这样，自由极点和连续谱不仅给出正确的虚部，也连同实部一起恢复了传播子。一圈展开适用于自能相对自由逆核仍为小修正的区域；在第14节讨论的大对数区间，也须保持相应的小量条件。

高质量处，式[（15.16）](#eq:c15-one-loop-density)给出 $\rho_1(s)=\alpha/(12s)+O(\alpha m^2/s^2)$。因此传播子谱积分含有的 $(s+z)^{-1}$ 使它收敛，而这一圈系数的总谱积分按对数发散。可以先在 $d=6-\varepsilon$、$0<\varepsilon<2$ 下检验第13节的等时求和规则。

记未加反项的一圈自能为 $\Pi_{\rm loop,\varepsilon}$。第14节的导数条件给出 $A_\varepsilon=\Pi'_{\rm loop,\varepsilon}(-m^2)$。用柯西导数公式表示，再把围道移到割线两岸，得到

<span id="eq:c15-regulated-spectral-sum"></span>

$$
\begin{aligned}
A_\varepsilon
&=\frac{1}{2\pi i}\oint
\frac{\Pi_{\rm loop,\varepsilon}(w)}{(w+m^2)^2}\,dw\\
&=-\frac1\pi\int_{4m^2}^{\infty}ds\,
\frac{\operatorname{Im}\Pi_{\rm loop,\varepsilon}(-s-i0)}{(s-m^2)^2}
=-\int_{4m^2}^{\infty}ds\,\rho_{1,\varepsilon}(s).
\end{aligned}
\tag{15.22}
$$

此时大动量行为为 $O(w^{1-\varepsilon/2})$，大圆积分按 $R^{-\varepsilon/2}$ 消失；谱尾相应为 $s^{-1-\varepsilon/2}$，总谱积分收敛。实反项没有割线虚部，所以式中可直接使用未加反项的圈函数。将 $Z_\varphi=1+A_\varepsilon+O(\alpha^2)$ 展开为倒数，便有

$$
Z_\varphi^{-1}
=1-A_\varepsilon+O(\alpha^2)
=1+\int_{4m^2}^{\infty}ds\,\rho_{1,\varepsilon}(s)+O(\alpha^2).
$$

这就在同一调节、同一耦合阶内验证了谱求和规则。随 $\varepsilon\downarrow0$ 出现的极点对应第14节场反项中的发散系数；完整谱在任意高质量处的行为还涉及更高圈修正及其重求和。

---

[← 第 14 节](/posts/srednicki-14/) · [章节地图](/srednicki/) · [第 16 节 →](/posts/srednicki-16/)
